from app import app, db
from models import User

def check_users_in_database():
    with app.app_context():
        users = User.query.all()
        if users:
            print("Users in the database:")
            for user in users:
                print(f"Email: {user.email}, Fitness Goal: {user.fitness_goal}, Preferences: {user.preferences}")
        else:
            print("No users found in the database.")

def check_specific_user(email):
    with app.app_context():
        user = User.query.filter_by(email=email).first()
        if user:
            print(f"User found: Email: {user.email}, Fitness Goal: {user.fitness_goal}, Preferences: {user.preferences}")
        else:
            print(f"No user found with email: {email}")

if __name__ == "__main__":
    # Check all users
    check_users_in_database()

    # Uncomment the line below to check for a specific user by email
    # check_specific_user('user@example.com')
