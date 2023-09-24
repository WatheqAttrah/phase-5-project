from flask import request, session, jsonify, make_response
from flask_restful import Resource
from config import app, db, api
from models import User, Car, views, Post


class Clear_Session(Resource):
    pass


class Signup(Resource):
    pass



class Check_Session(Resource):
    pass


class Login(Resource):
    pass


if __name__ == '__main__':
    app.run(port=5555, debug=True)
