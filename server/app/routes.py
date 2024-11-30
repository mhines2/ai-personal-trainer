from flask import Blueprint, request, jsonify
from .utils import generate_initial_message, get_ai_response

# Define blueprint for routes
main_bp = Blueprint("main", __name__)

@main_bp.route("/chat", methods=["POST"])
def chat():
    """
    API endpoint to handle chat interaction with the AI Personal Trainer.
    Expects JSON payload with preferences and chat messages.
    """
    try:
        # Parse incoming JSON payload
        data = request.get_json()
        preferences = data.get("preferences", {})
        messages = data.get("messages", [])

        # Generate initial message if messages are empty
        if not messages:
            messages = generate_initial_message(preferences)

        # Get AI response
        ai_reply = get_ai_response(messages)

        # Append AI's reply to conversation history
        messages.append({"role": "assistant", "content": ai_reply})

        return jsonify({"reply": ai_reply, "messages": messages})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
