#!/usr/bin/env python3
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Instantiate OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")  # Ensure your API key is in .env file
)

def get_user_input():
    """Collect user preferences for fitness trainer."""

    print("Welcome to the AI Personal Trainer!")
    print()
    
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

def generate_workout_plan(preferences):
    """Generate workout plan using OpenAI API based on user preferences."""

    messages = [
        {"role": "system", "content": "You are a personal fitness trainer. Generate personalized workout plans based on user inputs."},
        {"role": "user", "content": f"""
        Create a personalized daily workout plan for a user based on the following preferences:
        - Name: {preferences['name']}
        - Fitness Level: {preferences['fitness_level']}
        - Goal: {preferences['goal']}
        - Available Equipment: {preferences['equipment']}
        - Time Per Day: {preferences['time_per_day']} minutes
        - Focus Areas: {', '.join(preferences['focus_areas'])}
        - Injury: {preferences['injury']}
        Ensure the plan is safe, balanced, and goal-oriented.
        """}
    ]

    response = client.chat.completions.create(
        messages=messages,
        model="gpt-4o",  # Or use different model like "gpt-3.5-turbo" (don't have access to gpt-4)
    )

    return response.choices[0].message.content.strip()

def main():
    """Main function to interact with user and display workout plan."""

    preferences = get_user_input()
    print("\nGenerating your personalized workout plan...\n")
    try:
        workout_plan = generate_workout_plan(preferences)
        print("Here is your personalized workout plan:")
        print("-" * 50)
        print(workout_plan)
        print("-" * 50)
    except Exception as e:
        print(f"An error occurred while generating your workout plan: {e}")

if __name__ == "__main__":
    main()
