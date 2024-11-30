from app import create_app

# Create Flask app
app = create_app()

if __name__ == "__main__":
    # Run Flask app
    app.run(host="0.0.0.0", port=5001, debug=True) # use port 5001 or any other free port