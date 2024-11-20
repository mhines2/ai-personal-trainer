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
Here is your personalized workout plan:
--------------------------------------------------
Welcome, John! Here’s your workout plan for today:

- Warm-up: 5 minutes of light cardio
- Circuit Training (repeat 3 times):
  1. Push-ups: 10 reps
  2. Bodyweight squats: 15 reps
  3. Plank: 30 seconds
  4. Jumping jacks: 30 seconds
- Cool-down: Stretching for 5 minutes
--------------------------------------------------
