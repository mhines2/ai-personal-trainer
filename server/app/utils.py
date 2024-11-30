import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("The OpenAI API key is not set. Please add it to the .env file.")

# Instantiate OpenAI client
client = OpenAI(api_key=openai_api_key)
client = OpenAI(api_key=openai_api_key)

def generate_initial_message(preferences):
    """
    Generate the initial message to set the context for the AI.
    """
    return [
        {
            "role": "system",
            "content": "You are a world-famous personal fitness trainer. Provide fitness guidance and generate workout plans based on user inputs."
        },
        {
            "role": "user",
            "content": f"""
            My name is {preferences.get('name', 'User')}.
            I am a {preferences.get('fitness_level', 'beginner')} level user with a goal of {preferences.get('goal', 'general fitness')}.
            I have {preferences.get('equipment', 'no equipment')} available, and I can work out for {preferences.get('time_per_day', '30')} minutes per day.
            My focus areas are {', '.join(preferences.get('focus_areas', ['general fitness']))}, and I have the following injury considerations: {preferences.get('injury', 'none')}.
            """
        }
    ]

def get_ai_response(messages):
    """
    Send messages to OpenAI API and get the assistant's response.
    """
    response = client.chat.completions.create(
        messages=messages,
        model="gpt-4o"  # replace with accessible model like "gpt-3.5-turbo" if needed
    )
    return response.choices[0].message.content.strip()
