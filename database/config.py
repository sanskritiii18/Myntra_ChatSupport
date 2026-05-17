from flask_sqlalchemy import SQLAlchemy
import os
import dotenv


class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:verma7272@localhost:5432/MyntraCHAT"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET = "6361ccfa5492106def265fa084e110dbd6a23ae95530fc1adb722e031b379109"



