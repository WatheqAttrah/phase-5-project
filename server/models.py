from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt

# Models go here!


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-posts.user',)

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    image_url = db.Column(db.String)
    email = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String())

    posts = db.relationship('Post', backref='user')

    @hybrid_property
    def password_hash(self):
        raise Exception('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))

    def __repr__(self):
        return f'User {self.username}, ID: {self.id}'


class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'

    serialize_rules = ('-car.posts', '-user.posts',)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String())
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now)
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'))

    def __repr__(self):
        return f'<Post Id: {self.id}, Post Title: {self.title}, Post Description: {self.description}, Created Date: {self.created_at}>'


class Car(db.Model, SerializerMixin):
    __tablename__ = 'cars'

    serialize_rules = ('-post.car', 'cars')

    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(20))
    model = db.Column(db.String(20))
    year = db.Column(db.Integer())
    image = db.Column(db.String(256))
    price = db.Column(db.Float(precision=2))
    vin = db.Column(db.String(17), unique=True)
    engine = db.Column(db.Integer)
    miles = db.Column(db.Float)

    posts = db.relationship('Post', backref='cars')

    def __repr__(self):
        return f'<Car Id: {self.id}, Make: {self.make}, Model: {self.model}, Year: {self.year},Image: {self.image}, Price: {self.price}, VIN: {self.vin}, ,Engine: {self.engine}>'
