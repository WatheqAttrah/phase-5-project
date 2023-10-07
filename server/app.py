#!/usr/bin/env python3
from flask import jsonify, make_response, session, request
from sqlalchemy.ext.associationproxy import association_proxy
from flask_restful import Resource
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
# from urllib import response
# import functools
# from sqlalchemy import func
from config import app, db, api, bcrypt
from models import User, Post, Car


@app.route('/')
def index():
    return "Project Server"


class Signup(Resource):
    def post(self):
        username = request.get_json()['username']
        password = request.get_json()['password']

        if username:
            new_user = User(username=username)
            new_user.password_hash = password

            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id
            return new_user.to_dict(), 201
        return {'error': '422 Unprocessable Entity'}, 422


api.add_resource(Signup, '/signup', endpoint='signup')


class CheckSession(Resource):
    def get(self):
        if session.get('user_id') == None:
            return {}, 204
        user = User.query.filter(User.id == session.get('user_id')).first()
        return user.to_dict(), 200


api.add_resource(CheckSession, '/check_session')


class Login(Resource):
    def post(self):
        username = request.get_json()['username']
        password = request.get_json()['password']
        user = User.query.filter(User.username == username).first()

        if user:
            session['user_id'] = user.id
            return user.to_dict(), 200
        return {'error': '401 Unauthorized'}, 401


api.add_resource(Login, '/login', endpoint='login')


class Logout(Resource):
    def delete(self):

        if session.get('user_id'):

            session['user_id'] = None

            return {}, 204

        return {'error': '401 Unauthorized'}, 401


api.add_resource(Logout, '/logout', endpoint='logout')


# ================#================#================#================#================


class Posts(Resource):
    def get(self):
        posts = []
        for post in Post.query.all():
            post_dict = {
                "title": post.title,
                "description": post.description,
                "created_at": post.created_at,
                "updated_at": post.updated_at,
                "user_id": post.user_id,
            }
            posts.append(post_dict)

        return make_response(jsonify(posts), 200)


api.add_resource(Posts, '/posts', endpoint='posts')


class PostByID(Resource):
    def get(self, id):
        post = Post.query.filter_by(id=id).first()
        if post is not None:
            post_dict = {
                "title": post.title,
                "description": post.description,
                "created_at": post.created_at,
                "updated_at": post.updated_at,
                "user_id": post.user_id,
            }
            response = make_response(jsonify(post_dict), 200)
        else:
            response = make_response(jsonify({"error": "Post not found"}), 400)
        return response


api.add_resource(PostByID, '/posts/<int:id>')


class PostByTitle(Resource):
    def get(self, title):
        title = title.lower()
        post_by_title = Post.query.filter(
            func.lower(Post.title) == title).first()
        if post_by_title is not None:
            post_dict = {
                "title": post_by_title.title,
                "description": post_by_title.description,
                "created_at": post_by_title.created_at,
                "updated_at": post_by_title.updated_at,
                "user_id": post_by_title.user_id,
            }
            response = make_response(jsonify(post_dict), 200)
        else:
            response = make_response(jsonify({"error": "Post not found"}), 404)

        return response


api.add_resource(PostByTitle, '/posts/<string:title>')

# ===================#===================#===================#===================


class Users(Resource):
    def get(self):
        try:
            users = []
            for user in User.query.all():
                user_dict = {
                    "username": user.username,
                    "email": user.email,
                    "image_url": user.image_url,
                }
                users.append(user_dict)
            if not users:
                return make_response(jsonify({"error": "No users found"}), 404)
            users_json = jsonify(users)
            return make_response(users_json, 200)
        except Exception as e:
            error_message = {"error": str(e)}
            return make_response(jsonify(error_message), 500)


api.add_resource(Users, '/users', endpoint='users')


class UserByID(Resource):
    def get(self, id):
        try:
            user = User.query.filter_by(id=id).first()
            if user is not None:
                user_dict = {
                    "username": user.username,
                    "email": user.email,
                    "image_url": user.image_url,
                }
                response = make_response(jsonify(user_dict), 200)
            else:
                response = make_response(
                    jsonify({"error": "User not found"}), 404)
            return response
        except Exception as e:
            error_message = {"error": str(e)}
            response = make_response(jsonify(error_message), 500)
            return response


api.add_resource(UserByID, '/users/<int:id>')


class UserByUsername(Resource):
    def get(self, username):
        username = username.lower()
        user_by_name = User.query.filter(
            func.lower(User.username) == username).first()
        if user_by_name is not None:
            user_dict = {
                "username": user_by_name.username,
                "email": user_by_name.email,
                "image_url": user_by_name.image_url,
            }
            response = make_response(jsonify(user_dict), 200)
        else:
            response = make_response(
                jsonify({"error": "User not found"}), 404)
        return response


api.add_resource(UserByUsername, '/users/<string:username>')


class Cars(Resource):
    def get(self):
        try:
            cars = []
            for car in Car.query.all():
                car_dict = {
                    "Make": car.make,
                    "model": car.model,
                    "year": car.year,
                    "image": car.image,
                    "price": car.price,
                    "vin": car.vin,
                    "engine": car.engine,
                    "miles": car.miles,
                }
                cars.append(car_dict)
            if not cars:
                response = make_response(
                    jsonify({"error": "No cars found"}), 404)
            else:
                cars_json = jsonify(cars)
                response = make_response(cars_json, 200)
            return response
        except Exception as e:
            error_message = {"error": str(e)}
            response = make_response(jsonify(error_message), 500)
            return response


api.add_resource(Cars, '/cars', endpoint='cars')


class CarByID(Resource):
    def get(self, id):
        car = Car.query.filter(Car.id == id).first()

        if car is not None:
            car_dict = {
                "Make": car.make,
                "model": car.model,
                "year": car.year,
                "image": car.image,
                "price": car.price,
                "vin": car.vin,
                "engine": car.engine,
                "miles": car.miles,
            }
            response = make_response(jsonify(car_dict), 200)
        else:
            response = make_response(jsonify({"error": "Car not found"}), 404)
        return response


api.add_resource(CarByID, '/cars/<int:id>')


class CarByMake(Resource):
    def get(self, make):
        make = make.lower()
        car_by_make = Car.query.filter(func.lower(Car.make) == make).first()
        if car_by_make is not None:
            car_dict = {
                "Make": car_by_make.make,
                "model": car_by_make.model,
                "year": car_by_make.year,
                "image": car_by_make.image,
                "price": car_by_make.price,
                "vin": car_by_make.vin,
                "engine": car_by_make.engine,
                "miles": car_by_make.miles,
            }
            response = make_response(jsonify(car_dict), 200)
        else:
            response = make_response(jsonify({"error": "Car not found"}), 404)
        return response


api.add_resource(CarByMake, '/cars/<string:make>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
