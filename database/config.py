from flask_sqlalchemy import SQLAlchemy
import os
import dotenv


class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:verma7272@localhost:5432/MyntraCHAT"

    SQLALCHEMY_TRACK_MODIFICATIONS = False


