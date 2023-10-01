#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Post, Car, interesting
from faker import Faker
from faker_vehicle import VehicleProvider
import random
from config import app


fake = Faker()
fake.add_provider(VehicleProvider)


def generate_fake_vin():
    # The first character in a VIN is typically a letter, so we'll start with that.
    vin = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    # Generate the remaining 16 characters, which can be letters and numbers.
    vin += "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
                   for _ in range(16))
    return vin


def clear_database():
    with app.app_context():
        print('~~~~~~Drop All Data~~~~~~')
        db.drop_all()
        print('~~~~~~Create All Data~~~~~~')
        db.create_all()


def seed_database():
    with app.app_context():
        clear_database()

        # Seed Users
        users = []
        for _ in range(50):
            username = fake.user_name()
            user_email = fake.email()
            user = User(username=username, user_email=user_email)
            users.append(user)

        db.session.bulk_save_objects(users)
        db.session.commit()

        posts = []
        for user in User.query.all():
            for _ in range(4):  # Create 4 posts for each user
                title = fake.sentence(nb_words=3)
                description = fake.text(max_nb_chars=200)
                post = Post(title=title, description=description,
                            user_id=user.id)
                posts.append(post)

        db.session.bulk_save_objects(posts)
        db.session.commit()

        # Create cars for each user
        cars = []
        for _ in range(50):
            make = fake.vehicle_make()
            model = fake.vehicle_model()
            year = fake.random_int(min=1990, max=2023)
            image = fake.image_url()
            price = round(fake.random_int(min=1000, max=50000) / 100, 2)
            vin = generate_fake_vin()
            engine = fake.random_int(min=4, max=12)
            miles = fake.random_int(min=5000, max=170000)
            car = Car(
                make=make,
                model=model,
                year=year,
                image=image,
                price=price,
                vin=str(vin),
                engine=engine,
                miles=miles,
                user_id=random.choice(users).id
            )
            cars.append(car)

        db.session.bulk_save_objects(cars)
        db.session.commit()

        # Generate a list of 20 interested_posts
        interesting_posts = []
        for _ in range(20):
            # Assuming you have 50 users in your database
            user = random.choice(users)
            # Assuming you have 200 posts in your database
            post = random.choice(posts)
            interesting_post = {
                'user_id': user.id,
                'post_id': post.id
            }
            interesting_posts.append(interesting_post)

        db.session.execute(interesting.insert().values(interesting_posts))
        db.session.commit()


if __name__ == '__main__':
    seed_database()
    print("Database seeded successfully.")
