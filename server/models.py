from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from app import app
from config import db, bcrypt

# ===============#===============#===============#===============#===============#===============#===============


class Car(db.Model, SerializerMixin):
    __tablename__ = 'cars'

    serialize_rules = ('-reviews.car',)

    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(20))
    model = db.Column(db.String(20))
    year = db.Column(db.Integer())
    image = db.Column(db.String(50))
    price = db.Column(db.Float(precision=2))
    vin = db.Column(db.String(17), unique=True)
    engine = db.Column(db.Integer)
    miles = db.Column(db.Float)

    reviews = db.relationship('Review', backref='cars')

    def __repr__(self):
        return f'<Car Id: {self.id}, Make: {self.make}, Model: {self.model}, Year: {self.year},Price: {self.price},VIN: {self.vin},Engine: {self.engine},Image: {self.image}>'

# ===============#===============#===============#===============#===============#===============#===============


class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    serialize_rules = ('-car.reviews', '-user.reviews',)

    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'))

    def __repr__(self):
        return f'<Review Id: {self.id},  {self.review}>'

# ===============#===============#===============#===============#===============#===============#===============


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-reviews.user',)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    admin = db.Column(db.String, default=False)

    password_id = db.Column(db.Integer, db.ForeignKey(
        'passwords.id'), nullable=False)

    reviews = db.relationship('Review', backref='user')
    password = db.relationship('Password', backref='user')

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

# ===============#===============#===============#===============#===============#===============#===============


class Password(db.Model, SerializerMixin):
    __tablename__ = 'passwords'

    serializ_rules = ('-reviews.user',)
    serializ_rules = ('-password.user',)

    id = db.Column(db.Integer, primary_key=True)
    _password_hash = db.Column(db.String, nullable=False)
