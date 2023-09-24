from sqlalchemy.ext.hybrid import hybrid_property
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from config import db, Bcrypt

db = SQLAlchemy()


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String)

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
