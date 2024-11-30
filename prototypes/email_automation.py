#!/usr/bin/env python3
"""
In Progress: This code file is the email automation script that schedules daily workout emails to be sent to users.
"""

import os
import json
import schedule
import time
from datetime import datetime
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from server.initial_code.weekly_workout import get_initial_preferences  # import preferences collection

# Load environment variables from .env file
load_dotenv()

# Email sender credentials
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_email(to_email, subject, body):
    """Send email with generated workout plan."""

    from_email = EMAIL_ADDRESS

    # Create email
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        # Connect to server and send email
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_email, EMAIL_PASSWORD)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print(f"Workout plan emailed to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")


def load_weekly_plan():
    """Load weekly plan from JSON file."""

    if not os.path.exists("weekly_plan.json"):
        raise FileNotFoundError("Weekly plan not found. Please run 'weekly_workout.py' first to generate the plan.")
    
    with open("weekly_plan.json", "r") as file:
        return json.load(file)


def extract_current_day_workout(weekly_plan):
    """Extract workout plan for current day of week."""

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    current_day = datetime.now().strftime("%A")  # get current day of the week
    try:
        # Split plan by days and find section corresponding to current day
        for i, day in enumerate(days_of_week):
            if day in weekly_plan:
                # Find start and end of day's workout
                start = weekly_plan.index(day)
                end = weekly_plan.index(days_of_week[i + 1], start) if i + 1 < len(days_of_week) else len(weekly_plan)
                return weekly_plan[start:end].strip()
        return f"No workout plan found for {current_day}."
    except ValueError:
        return f"Error: Could not extract workout plan for {current_day}."


def send_daily_workout_email(preferences, weekly_plan):
    """Send workout for the current day via email."""

    workout_plan = extract_current_day_workout(weekly_plan)

    # Email content
    subject = f"Your Workout Plan for {datetime.now().strftime('%A')}"
    send_email(
        to_email=preferences['email'],
        subject=subject,
        body=workout_plan
    )

    print(f"Sent email for {datetime.now().strftime('%A')}:\n{workout_plan}")


def schedule_email_sending(preferences, weekly_plan, send_time="08:00"):
    """Schedule the email to be sent daily at the specified time."""

    schedule.every().day.at(send_time).do(send_daily_workout_email, preferences, weekly_plan)

    print(f"Email scheduling started. Emails will be sent daily at {send_time}.")
    while True:
        schedule.run_pending()
        time.sleep(1)  # prevent high CPU usage


def main():
    """Main function to schedule daily workout emails."""
    
    preferences = get_initial_preferences()

    # Load weekly plan
    print("\nLoading the weekly workout plan...\n")
    try:
        weekly_plan = load_weekly_plan()
    except FileNotFoundError as e:
        print(e)
        exit(1)

    # Ask user for email scheduling
    send_time = input("What time would you like to receive your email? (e.g., 08:00 = 8:00 AM): ")
    schedule_email_sending(preferences, weekly_plan, send_time)


if __name__ == "__main__":
    main()
