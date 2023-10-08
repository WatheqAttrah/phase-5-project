#!/usr/bin/env python3
from flask import jsonify, make_response, render_template, session, request
from sqlalchemy.ext.associationproxy import association_proxy
from flask_restful import Resource
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from config import app, db, api, bcrypt
from models import User, Review, Car, Password

# ============#============#============#============#============
# API's Starts Here


@app.route('/')
@app.route('/<int:id>')
def index(id=0):
    return render_template("index.html")

# ClearSession


class ClearSession(Resource):
    def delete(self):
        session['page_views'] = None
        session['user_id'] = None
        return {}, 204


api.add_resource(ClearSession, '/clear', endpoint='clear')

# ============#============#============#============#============
# Check_Session


class CheckSession(Resource):
    def get(self):
        if session.get('user_id') == None:
            return {}, 204
        user = User.query.filter(User.id == session.get('user_id')).first()
        return user.to_dict(), 200


api.add_resource(CheckSession, '/check_session', endpoint='check_session')

# ============#============#============#============#============


class Login(Resource):
    def post(self):
        username = request.get_json()['username']
        password = request.get_json()['password']

        user = User.query.filter(User.username == username).first()

        if user and user.authenticate(password):
            # Successful authentication
            session['user_id'] = user.id
            return user.to_dict(), 200
        # Authentication failed
        return {'error': '401 Unauthorized'}, 401


api.add_resource(Login, '/login', endpoint='login')

# ============#============#============#============#============


class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        return {}, 204


api.add_resource(Logout, '/logout', endpoint='logout')
# ============#============#============#============#============


class Signup(Resource):

    def post(self):

        username = request.get_json()['username']
        email = request.get_json()['email']
        password = request.get_json()['password']

        if len(username) < 15 and len(password) > 8:
            # hash the input password, then add it in database
            hashed_password = bcrypt.generate_password_hash(
                password).decode('utf-8')
            password_record = Password(_password_hash=hashed_password)
            db.session.add(password_record)
            db.session.commit()

            # Create a new user with the password foreign key
            new_user = User(username=username, email=email,
                            password_id=password_record.id)
            try:
                db.session.add(new_user)
                db.session.commit()
                session['user_id'] = new_user.id
                return new_user.to_dict(), 201

            except IntegrityError as e:
                db.session.rollback()
                return {'errors': 'username already taken'}, 400
        return {'errors' 'unproceessable entity'}, 422


api.add_resource(Signup, '/signup')


# ============#============#============#============#============

class Cars(Resource):
    def get(self):
        cars = []
        for car in Car.query.all():
            car = {
                "id": car.id,
                "make": car.make,
                "model": car.model,
                "year": car.year,
                "image": car.image,
                "price": car.price,
                "vin": car.vin,
                "engine": car.engine,
                "miles": car.miles,
            }
            cars.append(car)
        return make_response(jsonify(cars), 200)


api.add_resource(Cars, '/cars', endpoint='cars')
# ============#============#============#============#============


class CarByID(Resource):
    # get reviews for a specific car
    def get(self, id):
        reviews = Review.query.filter_by(car_id=id)
        reviews_data = {'reviews': [
            {'id': review.id, 'review': review.review, 'user': review.user.username} for review in reviews]}
        return make_response(jsonify(reviews_data), 200)

    # add a review for a specific car
    def post(self, id):
        data = request.get_json()
        user_id = data['user_id']
        car_id = data['car_id']
        review_text = data['review_text']

        car = Car.query.get(id)
        if car:
            review = Review(review=review_text, car_id=car_id, user_id=user_id)
            db.session.add(review)
            db.session.commit()
        return {'message': 'Review added successfully'}, 201


api.add_resource(CarByID, '/cars/<int:id>')


if __name__ == '__main__':
    app.run(port=5555, debug=True)
