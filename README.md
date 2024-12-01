# AI Personal Trainer App Prototype

This repository contains the prototype for the **AI Personal Trainer App**, an interactive chatbot application designed to provide personalized fitness guidance and workout plans based on user preferences. The prototype uses **Streamlit** for a simple GUI and **OpenAI's GPT-4 model** for generating workout recommendations.

---

## Features

1. **User-Friendly Interface**:
   - A sidebar allows users to input their fitness preferences, including name, fitness level, goals, equipment, time available, focus areas, and any injuries.
2. **Interactive Chat**:

   - Users can engage in a dynamic chat with the AI Personal Trainer to receive customized workout advice.

3. **AI-Generated Responses**:

   - The app leverages OpenAI's GPT-4 to generate personalized fitness guidance based on user inputs.

4. **Streamlit Integration**:
   - Provides a lightweight, interactive UI for quick prototyping without the need for front-end design.

---

## How It Works

1. Users input their fitness preferences via a sidebar form.
2. On submission, the app initializes a conversation with the AI Trainer.
3. The AI generates an initial workout plan tailored to the user.
4. Users can chat with the AI Trainer to ask follow-up questions or request modifications to their plan.

---

## Technologies Used

### Current Prototype

- **Streamlit**: A Python framework for creating interactive GUIs.
- **OpenAI API**: Used to access GPT-4 for generating personalized responses.
- **Python**: The core language for implementing the app's logic.
- **dotenv**: For managing API keys and environment variables securely.

---

## Scalability and Future Plans

This prototype is designed as a foundation for a full-stack application. The project is highly scalable and intended to evolve into a robust platform with the following components:

### Back-End

- **Flask**: To handle API requests, manage user data, and serve as the back-end server.
- **Database**: Integration with a database (e.g., PostgreSQL, MongoDB) to store user preferences, workout history, and progress tracking data.
- **Authentication**: Implement secure user authentication and authorization.

### Front-End

- **React**: Build a dynamic, responsive client interface with modern UI/UX design.
- **Material-UI or Tailwind CSS**: For styling and layout improvements.

### Additional Features

- **User Accounts**: Allow users to register, log in, and save their workout preferences and progress.
- **Progress Tracking**: Enable users to track their workouts, weight, and goals over time.
- **Push Notifications**: Send reminders and motivational messages to users.
- **Custom Workout Scheduling**: Allow users to create and edit workout schedules.

---

## How to Run the Prototype

1. Clone this repository:

   ```bash
   git clone https://github.com/mhines2/ai-personal-trainer.git
   cd ai-personal-trainer/prototypes
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your OpenAI API key:

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   ```

4. Run the app:

   ```bash
   streamlit run ai_trainer.app.py
   ```

5. Open the app in your browser (typically at http://localhost:8501) to start interacting with the AI Personal Trainer.

---

## Acknowledgments

- **OpenAI**: For providing GPT-4, the core of this project’s AI functionality.
- **Streamlit**: For enabling rapid prototyping with an easy-to-use Python-based GUI framework.

---

This project is in its prototype phase and will evolve significantly. Stay tuned for updates! 🚀
