import os
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

# Load environment variables from .env file
load_dotenv()

# Instantiate OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")  # ensure your API key is in .env file
)

# Streamlit App
def main():
    st.set_page_config(page_title="AI Personal Trainer", layout="wide")
    st.title("AI Personal Trainer 🤖💪")
    
    # Sidebar for user preferences
    st.sidebar.header("Your Fitness Preferences")
    
    name = st.sidebar.text_input("Enter your name", "")
    fitness_level = st.sidebar.selectbox("Select your fitness level", ["Beginner", "Intermediate", "Advanced"])
    goal = st.sidebar.text_input("Enter your fitness goal (e.g., weight loss, muscle gain)", "")
    equipment = st.sidebar.selectbox(
        "Available equipment", ["Bodyweight", "Free Weights", "Full Gym"]
    )
    time_per_day = st.sidebar.slider("Time available per day (minutes)", 10, 120, 30)
    focus_areas = st.sidebar.text_input(
        "Enter focus areas (e.g., cardio, core, arms, legs) separated by commas", ""
    )
    injury = st.sidebar.text_input("Injury considerations (leave blank if none)", "None")
    
    if st.sidebar.button("Submit Preferences"):
        initial_preferences = {
            "name": name,
            "fitness_level": fitness_level.lower(),
            "goal": goal.lower(),
            "equipment": equipment.lower(),
            "time_per_day": time_per_day,
            "focus_areas": [area.strip().lower() for area in focus_areas.split(",") if area.strip()],
            "injury": injury.lower()
        }
        st.session_state.preferences = initial_preferences
        st.session_state.conversation = []

        st.success("Preferences submitted! Generating your initial plan...")

        # Prepare initial conversation
        preferences = st.session_state.preferences
        initial_message = {
            "role": "system",
            "content": "You are a world-famous personal fitness trainer. Provide fitness guidance and generate workout plans based on user inputs."
        }
        user_message = {
            "role": "user",
            "content": f"""
            My name is {preferences['name']}.
            I am a {preferences['fitness_level']} level user with a goal of {preferences['goal']}.
            I have {preferences['equipment']} available, and I can work out for {preferences['time_per_day']} minutes per day.
            My focus areas are {', '.join(preferences['focus_areas'])}, and I have the following injury considerations: {preferences['injury']}.
            """
        }
        # Add messages to session conversation
        st.session_state.conversation = [initial_message, user_message]
        
        with st.spinner("Generating your initial plan..."):
            response = client.chat.completions.create(
                messages=st.session_state.conversation,
                model="gpt-4o"
            )
        bot_reply = response.choices[0].message.content.strip()

        # Append the bot's response to the conversation
        st.session_state.conversation.append({"role": "assistant", "content": bot_reply})

    # Chat Interface
    if "preferences" in st.session_state:
        st.subheader("Chat with your Trainer")
        message_container = st.container()

        with message_container:
            # Display previous conversation
            for message in st.session_state.conversation[2:]:
                if message["role"] == "user":
                    st.chat_message("user").write(message["content"])
                elif message["role"] == "assistant":
                    st.chat_message("assistant").write(message["content"])

        # Add user input at the bottom
        def send_message():
            user_input = st.session_state.user_input
            if user_input:
                st.session_state.conversation.append({"role": "user", "content": user_input})
                with message_container:
                    st.chat_message("user").write(user_input)

                # Indicate that the bot is generating an answer
                with st.spinner("Generating answer..."):
                    try:
                        response = client.chat.completions.create(
                            messages=st.session_state.conversation,
                            model="gpt-4o"
                        )
                        bot_reply = response.choices[0].message.content.strip()
                        st.session_state.conversation.append({"role": "assistant", "content": bot_reply})
                        with message_container:
                            st.chat_message("assistant").write(bot_reply)
                    except Exception as e:
                        st.error(f"An error occurred: {e}")
                    finally:
                        # Clear the input box
                        st.session_state.user_input = ""

        # Add a text input for messages with an `on_change` callback
        st.text_input("Type your message:", key="user_input", on_change=send_message)

if __name__ == "__main__":
    main()
