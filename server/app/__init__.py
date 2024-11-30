from flask import Flask
from flask_cors import CORS
from .routes import main_bp

def create_app():
    """Application factory function."""
    app = Flask(__name__)

    # Enable CORS for cross-origin requests from React frontend
    CORS(app)

    # Import and register routes
    app.register_blueprint(main_bp)

    return app
