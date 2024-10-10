from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from models import db, User
import openai
import os

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)
mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    fitness_goal = request.form['fitness_goal']
    preferences = request.form['preferences']
    
    new_user = User(email=email, fitness_goal=fitness_goal, preferences=preferences)
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for('home'))

@app.route('/send_workout', methods=['POST'])
def send_workout():
    email = request.form['email']
    user = User.query.filter_by(email=email).first()
    
    if user:
        workout_plan = generate_workout_plan(user.preferences)
        send_email(user.email, workout_plan)
        return f'Workout sent to {user.email}'a
    return 'User not found'

def generate_workout_plan(preferences):
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": f"Create a workout plan for someone who {preferences}."}
        ]
    )
    return response.choices[0].message['content']

def send_email(to_email, workout_plan):
    msg = Message("Your Daily Workout Plan", sender=app.config['MAIL_USERNAME'], recipients=[to_email])
    msg.body = workout_plan
    mail.send(msg)

if __name__ == '__main__':
    app.run(debug=True)
