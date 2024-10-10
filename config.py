import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///fitness_trainer.db'  # SQLite for development
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'  # For Gmail
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')  # Your email
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')  # Your email password
