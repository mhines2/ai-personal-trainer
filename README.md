# AI Personal Trainer

The **AI Personal Trainer** is a Python application that generates personalized workout plans based on user preferences. It uses OpenAI's GPT models to create safe, effective, and goal-oriented fitness routines.

**Created by Michael Hines**

## Features

- **Interactive Input**: Users provide details like fitness level, goals, available equipment, and time constraints.
- **Personalized Plans**: AI generates a workout tailored to the user's needs and preferences.
- **Secure**: API keys are managed securely using a `.env` file.

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (get one from the [OpenAI Platform](https://platform.openai.com/))

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/<your-username>/<repository-name>.git
    cd <repository-name>
    ```

2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file and add your OpenAI API key:
    ```plaintext
    OPENAI_API_KEY=your-api-key
    ```

5. Run the script:
    ```bash
    python fitness_assistant.py
    ```

## Usage

1. Run the script in your terminal.
2. Enter your fitness preferences when prompted:
    - **Fitness level** (e.g., beginner, intermediate, advanced)
    - **Fitness goal** (e.g., weight loss, muscle gain)
    - **Equipment availability** (e.g., bodyweight, free weights)
    - **Time per day** (in minutes)
    - **Any injuries or special considerations**

3. Receive a personalized workout plan directly in the terminal.

### Example Output

```plaintext
Welcome to the AI Personal Trainer!

Enter your name: John
Enter your fitness level (beginner/intermediate/advanced): beginner
Enter your fitness goal (e.g., weight loss, muscle gain, general fitness): weight loss
Enter available equipment (e.g., bodyweight, free-weights, full gym): bodyweight
Enter the time you can dedicate per day (in minutes): 30
Enter focus areas (e.g., cardio, core, arms, legs) separated by commas: cardio, core
Any injuries to consider (type 'none' if no injuries): none

Generating your initial personalized workout plan...

Here is your initial workout plan:
--------------------------------------------------
- Warm-up: 5 minutes of light jogging in place
- Circuit Training (repeat 3 times):
  1. Push-ups: 10 reps
  2. Bodyweight squats: 15 reps
  3. Plank: 30 seconds
  4. Mountain climbers: 20 seconds
- Cool-down: 5 minutes of stretching
--------------------------------------------------

You: Can you add more focus on core exercises?

Trainer: Sure! Here's an updated plan focusing on your core:
- Warm-up: 5 minutes of dynamic stretches
- Core Circuit (repeat 3 times):
  1. Plank: 45 seconds
  2. Side planks: 30 seconds per side
  3. Bicycle crunches: 20 reps
  4. Russian twists: 15 reps per side
- Cool-down: 5 minutes of stretching (focus on abs and lower back)

You: What should I eat before a workout?

Trainer: For a pre-workout meal, consider eating a mix of carbs and protein, like a banana with peanut butter or a small bowl of oatmeal with fruit. Avoid heavy or greasy foods.

You: exit

Goodbye! Stay active and healthy!

