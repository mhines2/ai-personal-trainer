#!/usr/bin/env python3
from dotenv import load_dotenv
import os
import json
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Instantiate OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")  # ensure your API key is in .env file
)

def generate_weekly_workout_plan(preferences):
    """ Generate weekly workout plan using OpenAI API based on user preferences. """

    messages = [
        {"role": "system", "content": "You are a world-famous personal fitness trainer. Create weekly workout plans based on user inputs."},
        {"role": "user", "content": f"""
        Create a weekly workout plan for the following user:
        - Name: {preferences['name']}
        - Fitness Level: {preferences['fitness_level']}
        - Goal: {preferences['goal']}
        - Available Equipment: {preferences['equipment']}
        - Time Per Day: {preferences['time_per_day']} minutes
        - Days Split: {preferences['days_split']} days
        - Focus Areas: {', '.join(preferences['focus_areas'])}
        - Injuries: {preferences['injury']}
        Ensure each day from Monday to Sunday includes a warm-up, main workout, and cool-down. Spread focus areas across the week.
        The output must contain each day of the week: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.
        """}
    ]

    response = client.chat.completions.create(
        messages=messages,
        model="gpt-4o",  # replace with appropriate model
    )

    weekly_plan = response.choices[0].message.content.strip()
    return weekly_plan # return weekly plan as string

'''
def load_current_day():
    """ Load current day index from file or default to Day 1. """

    if os.path.exists("current_day.json"):
        with open("current_day.json", "r") as file:
            return json.load(file)["day"]
    return 0  # start at Day 1 if file doesn't exist

def save_current_day(day_index):
    """ Save current day index to file. """

    with open("current_day.json", "w") as file:
        json.dump({"day": day_index}, file)
'''
# This code above was originally for saving and loading current day index; however, it is not needed for the current implementation
# because the weekly workout plan no longer follows a Day 1 to Day 7 structure. The weekly plan is now split by actual days of the week.

def get_initial_preferences():
    """ Collect user preferences for fitness trainer. """

    print("Welcome to the AI Personal Trainer!")
    print()

    name = input("Enter your name: ")
    fitness_level = input("Enter your fitness level (beginner/intermediate/advanced): ").lower()
    goal = input("Enter your fitness goal (e.g., weight loss, muscle gain, general fitness): ").lower()
    equipment = input("Enter available equipment (e.g., bodyweight, free-weights, full gym): ").lower()
    time_per_day = input("Enter the time you can dedicate per day (in minutes): ")
    days_split = input("Enter the number of days you prefer to workout per week (e.g., 3, 4, 5): ")
    focus_areas = input("Enter focus areas (e.g., cardio, core, arms, legs) separated by commas: ").lower()
    injury = input("Any injuries to consider (type 'none' if no injuries): ").lower()
    email = input("Enter your email address: ")

    # Consolidate inputs into dictionary
    return {
        "name": name,
        "fitness_level": fitness_level,
        "goal": goal,
        "equipment": equipment,
        "time_per_day": time_per_day,
        "days_split": days_split,
        "focus_areas": [area.strip() for area in focus_areas.split(",")],
        "injury": injury,
        "email": email
    }

def save_weekly_plan(weekly_plan):
    """ Save weekly plan to JSON file. """

    with open("weekly_plan.json", "w") as file:
        json.dump(weekly_plan, file)
    print("\nWeekly workout plan saved to 'weekly_plan.json'\n")

def print_workout_plan(weekly_plan):
    """ Print weekly workout plan to standard output. """

    print("Here is your weekly workout plan:\n")
    print("-" * 50)
    print(weekly_plan)
    print("-" * 50)

def main():
    """ Main function to run AI Personal Trainer program. """

    preferences = get_initial_preferences()
    print("\nGenerating your weekly workout plan...\n")
    weekly_plan = generate_weekly_workout_plan(preferences)

    # Print to standard output
    print_workout_plan(weekly_plan)

    # Save plan to file
    save_weekly_plan(weekly_plan)

if __name__ == "__main__":
    main()