"""
This code file is a prototype for an AI Personal Trainer app that uses:
    - Streamlit for GUI (no front-end design required)
    - OpenAI's API for generating workout plans based on user preferences
"""

import os
import dotenv
import openai
import streamlit as st

# Load environment variables from .env file
dotenv.load_dotenv()

# Instantiate OpenAI client
client = openai.OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")  # ensure your API key is in .env file
)

# Streamlit App
def main():
    st.set_page_config(page_title="AI Personal Trainer", layout="wide") # set page title and layout
    st.title("AI Personal Trainer 🤖💪")
    
    # Sidebar for user preferences
    st.sidebar.header("Your Fitness Preferences")
    
    name = st.sidebar.text_input("Enter your name", "")
    fitness_level = st.sidebar.selectbox("Select your fitness level", ["Beginner", "Intermediate", "Advanced"])
    goal = st.sidebar.text_input("Enter your fitness goal (e.g., weight loss, muscle gain)", "")
    equipment = st.sidebar.selectbox(
        "Available equipment", ["Bodyweight", "Free Weights", "Full Gym"]
    )
    day_split = st.sidebar.slider("Number of days per week (to work out)", 1, 7, 4) # min, max, default
    time_per_day = st.sidebar.slider("Time available per day (minutes)", 10, 120, 60) # min, max, default
    focus_areas = st.sidebar.text_input(
        "Enter focus areas (e.g., cardio, core, arms, legs) separated by commas", ""
    )
    injury = st.sidebar.text_input("Injury considerations (leave blank if none)", "none") # default to "none"
    
    if st.sidebar.button("Submit Preferences"): # store preferences in session state
        initial_preferences = {
            "name": name,
            "fitness_level": fitness_level.lower(),
            "goal": goal.lower(),
            "equipment": equipment.lower(),
            "day_split": day_split,
            "time_per_day": time_per_day,
            "focus_areas": [area.strip().lower() for area in focus_areas.split(",") if area.strip()],
            "injury": injury.lower()
        }
        st.session_state.preferences = initial_preferences
        st.session_state.conversation = [] # initialize conversation list

        st.success("Preferences submitted successfully! You can now chat with your AI Trainer.")  

        # Prepare initial conversation
        preferences = st.session_state.preferences
        initial_message = {
            "role": "system",
            "content": "You are a world-famous personal fitness trainer. Provide fitness guidance and generate workout plans based on user inputs." # establish persona for AI (using CRAFT)
        }
        user_message = {
            "role": "user",
            "content": f"""
            My name is {preferences['name']}.
            I am a {preferences['fitness_level']} level user with a goal of {preferences['goal']}.
            I have {preferences['equipment']} available, and I plan to work out {preferences['day_split']} days per week.
            I can work out for {preferences['time_per_day']} minutes per day.
            My focus areas are {', '.join(preferences['focus_areas'])}, and I have the following injury considerations: {preferences['injury']}.
            """
        }

        # Add messages to session conversation
        st.session_state.conversation = [initial_message, user_message]
        
        with st.spinner("Generating your initial workout plan..."):
            response = client.chat.completions.create(
                messages=st.session_state.conversation,
                model="gpt-4o" # or use another available model like "gpt-3.5turbo"
            )
        bot_reply = response.choices[0].message.content.strip() 

        # Append bot's response to conversation
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

        # Add user input at bottom
        def send_message():
            user_input = st.session_state.user_input
            if user_input:
                st.session_state.conversation.append({"role": "user", "content": user_input})
                with message_container:
                    st.chat_message("user").write(user_input)

                # Indicate that bot is generating answer
                with st.spinner("Generating answer..."): # for some reason, spinner does not show up but when I remove spinner, it generates conversation twice
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
                        # Clear input box
                        st.session_state.user_input = ""

        # Add text input for messages with `on_change` callback
        st.text_input("Type your message:", key="user_input", on_change=send_message)

if __name__ == "__main__":
    main()