from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
import bcrypt


db = SQLAlchemy()


# Define the association table for the many-to-many relationship between users and car posts
interesting = db.Table('Interesting',
                       db.Column('user_id', db.Integer,
                                 db.ForeignKey('users.id')),
                       db.Column('post_id', db.Integer,
                                 db.ForeignKey('posts.id'))
                       )
# ===============#===============#===============#===============#===============#===============


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('interesting', 'cars', 'password',
                       'admin', 'cars.posts', 'posts.user')

    id = db.Column(db.Integer(), unique=True, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    user_email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String(60))  # Store the hashed password
    created = db.Column(db.DateTime, default=db.func.now())
    admin = db.Column(db.Boolean, nullable=False, default=False)

    posts = db.relationship('Post', backref='user')
    cars = db.relationship('Car', backref='user')

# ===============#===============#===============#===============#===============#===============
    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(
            password).decode('utf-8')

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.username}, ID: {self.id}'

# ===============#===============#===============#===============#===============#===============


class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'

    serialize_rules = ('users_shows_interest', 'user.posts',
                       'user.cars', 'user.interesting_posts', 'car')

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String())
    created = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Define the foreign key relationship
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # Define the foreign key relationship
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'))

    # Establish the relationship with the 'Car' model
    users_shows_interest = db.relationship(
        'User', secondary=interesting, backref='interesting_posts')

    def __repr__(self):
        return f'Post: {self.id}, Title: {self.title}, Created: {self.created}'

# ===============#===============#===============#===============#===============#===============


class Car(db.Model, SerializerMixin):
    __tablename__ = 'cars'

    serialize_rules = ('posts.user', 'user.cars',
                       'user.posts', 'user.interesting_posts')

    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(20))
    model = db.Column(db.String(20))
    year = db.Column(db.Integer)
    image = db.Column(db.String)
    price = db.Column(db.Float(precision=2))
    vin = db.Column(db.String(17), unique=True)
    engine = db.Column(db.Integer)
    miles = db.Column(db.Float)

    # Define the foreign key relationship
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    posts = db.relationship('Post', backref='car')

    def __repr__(self):
        return (f'Car Id: {self.id},Make: {self.make},Model:{self.model},Year: {self.year},Miles: {self.miles},Price: {self.price},VIN: {self.vin},Engine:{self.engine}')
