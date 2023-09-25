from flask import request, session, jsonify, make_response
from flask_restful import Resource
from config import app, db, api
from models import User, Car, views, Post


class Signup(Resource):

    def post(self):
        request_json = request.get()
        username = request_json.get('username')
        password = request_json.get('password')
        email = request_json.get('email')
        image = request_json.get('image')
        user = User(
            username=username,
            email=email,
            image=image,
        )
        user.password_hash = password
        print('first')
        try:
            print('here')
            db.session.add(user)
            db.session.commit()
            session['user_id'] = user.id
            print(user.to_dict())
            return user.to_dict(), 201
        except ImportError:
            print('no, here!')
            return {'error': '422 Unprocessable Entity'}, 422


class Check_Session(Resource):
    def get():
        if session.get('user_id'):
            user = User.query.filter(User.id == session['user_id']).first()
            return user.to_dict(), 200
        return {'error': '401 UnAuthorized'}, 401


class Login(Resource):
    def post(self):
        request_json = request.get()
        username = request_json.get('username')
        password = request_json.get('password')
        if user := User.query.filter(User.username == username).first():
            if user.authenticated(password):
                session['user_id'] = user.id
                return user.to_dict(), 200
            return {'error': '401 UnAuthorized'}, 401


class Logout(Resource):
    def delete(self):
        if session.get('user_id'):
            session['user_id'] = None
            return {}, 204
        return {'error': '401 Unauthorized'}, 401


api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(Check_Session, '/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(RecipeIndex, '/recipes', endpoint='recipes')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
