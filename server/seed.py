#!/usr/bin/env python3
from faker_vehicle import VehicleProvider
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
from app import app
from models import User, Car, Post
from config import db
db = SQLAlchemy(app)

app = Flask(__name__)


fake = Faker()
with app.app_context():
    User.query.delete()
    Car.query.delete()
    Post.query.delete()

    users = []
    for _ in range(10):
        user = User(username=fake.username)
        users.append(user)

    db.session.add_all(users)
