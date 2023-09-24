from sqlalchemy.ext.hybrid import hybrid_property
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from config import db, bcrypt


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)

    cars = db.relationship('Post', backref='user')
    posts = db.relationship('Post', backref='user')

    @hybrid_property
    def password_hash(self):  # sourcery skip: raise-specific-error
        raise Exception('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = Bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password.decode('utf-8')

    def authenticate(self, password):
        return Bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))

    def __repr__(self) -> str:
        return super({self.username}).__repr__({self.id})


class Car(db.Model, SerializerMixin):
    __tablename__ = 'cars'
    # id | make | model | year | price | vin  | user_id | created_date | description
    pass


class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'
    pass
