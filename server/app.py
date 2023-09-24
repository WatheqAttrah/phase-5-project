from flask import request, session
from flask_restful import Resource

from config import app , db, Api
from models import User



if __name__=='__main__':
    app.run(port=5555, debug=True)