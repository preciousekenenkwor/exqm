import os

# Configuration class to set up the Flask app's configuration
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///books.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
