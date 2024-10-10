def send_email(to_email, workout_plan):
    msg = Message("Your Daily Workout Plan", sender="your_email@example.com", recipients=[to_email])
    msg.body = workout_plan
    mail.send(msg)
