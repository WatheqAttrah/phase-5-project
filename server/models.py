from sqlalchemy.ext.hybrid import hybrid_property
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from config import db, bcrypt


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('password', 'posts',)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, default=db.func.now())

    cars = db.relationship('Post', backref='user')
    posts = db.relationship('Post', backref='user')

    @hybrid_property
    def password_hash(self):  # sourcery skip: raise-specific-error
        raise Exception('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))

    def __repr__(self) -> str:
        return super({self.username}).__repr__({self.id})


class Car(db.Model, SerializerMixin):
    __tablename__ = 'cars'

    serialize_rules = ('user', 'post')

    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(20))
    model = db.Column(db.String(20))
    image = db.Column(db.String(min=1, max=4))  # 255min=1,max=4
    price = db.Column(db.Float)
    vin = db.Column(db.String, unique=True)
    created = db.Column(db.DateTime, default=db.func.now())
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    
    
    def __repr__(self):
        return f'<Car {self.make} |Price: {self.price}>'


class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'

    serialize_rules = ('-user', '-prompt',)
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(600), nullable=False)
    likes = db.Column(db.Integer, default=0, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    prompt_id = db.Column(db.Integer, db.ForeignKey('prompts.id'))
    created = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
