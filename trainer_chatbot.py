#!/usr/bin/env python3
"""
This code file was the original version of the AI Personal Trainer chatbot so that users could interact with the AI trainer in a conversational manner.
"""

from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables from .env file
load_dotenv() 

# Instantiate OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")  # ensure your API key is in .env file
)

def get_initial_preferences(): 
    """Collect user preferences for fitness trainer."""

    print("Welcome to the AI Personal Trainer!\n")

    name = input("Enter your name: ")
    fitness_level = input("Enter your fitness level (beginner/intermediate/advanced): ").lower()
    goal = input("Enter your fitness goal (e.g., weight loss, muscle gain, general fitness): ").lower()
    equipment = input("Enter available equipment (e.g., bodyweight, free-weights, full gym): ").lower()
    time_per_day = input("Enter the time you can dedicate per day (in minutes): ")
    focus_areas = input("Enter focus areas (e.g., cardio, core, arms, legs) separated by commas: ").lower()
    injury = input("Any injuries to consider (type 'none' if no injuries): ").lower()

    # Consolidate inputs into dictionary
    user_preferences = {
        "name": name,
        "fitness_level": fitness_level,
        "goal": goal,
        "equipment": equipment,
        "time_per_day": time_per_day, 
        "focus_areas": [area.strip() for area in focus_areas.split(",")],
        "injury": injury
    }
    return user_preferences

def chat_with_trainer(initial_preferences):
    """Run chat session with AI personal trainer."""
    
    # Initialize conversation
    messages = [
        {"role": "system", "content": "You are a world-famous personal fitness trainer. Provide fitness guidance and generate workout plans based on user inputs."},
        {"role": "user", "content": f"""
        My name is {initial_preferences['name']}.
        I am a {initial_preferences['fitness_level']} level user with a goal of {initial_preferences['goal']}.
        I have {initial_preferences['equipment']} available, and I can work out for {initial_preferences['time_per_day']} minutes per day.
        My focus areas are {', '.join(initial_preferences['focus_areas'])}, and I have the following injury considerations: {initial_preferences['injury']}.
        """}
    ]

    # Generate initial plan
    print("\nGenerating your initial personalized workout plan...\n")
    response = client.chat.completions.create(
        messages=messages,
        model="gpt-4o",  # or use another model you have access to
    )
    print("Here is your initial workout plan:")
    print("-" * 50)
    print(response.choices[0].message.content.strip())
    print("-" * 50)

    # Keep chat going
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("\nGoodbye! Stay active and healthy!\n")
            break
        
        # Append user's message to conversation
        messages.append({"role": "user", "content": user_input})
        
        print("\nPlease wait, loading response...\n") # notify user system is generating response

        # Generate chatbot's response
        try:
            response = client.chat.completions.create(
                messages=messages,
                model="gpt-4o",
            )
            bot_reply = response.choices[0].message.content.strip()
            print(f"Trainer: {bot_reply}")
            
            # Append AI's response to conversation history
            messages.append({"role": "assistant", "content": bot_reply})
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    """Main function to initiate chatbot interaction."""

    initial_preferences = get_initial_preferences()
    chat_with_trainer(initial_preferences)

if __name__ == "__main__":
    main()