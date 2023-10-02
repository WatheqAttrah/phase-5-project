# Standard library imports

# Remote library imports
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_bcrypt import Bcrypt

# Local imports

# Instantiate app, set attributes
app = Flask(__name__)

# # Sets a secret key for the application. The secret key is essential for security purposes,
# # such as protecting against cross-site request forgery (CSRF) attacks and session management.
# app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.secret_key = b'53b02f2137d6a4782ddae57bd271b3d0'

# # You can change this URI to connect to a different database system like MySQL or PostgreSQL.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# # Disables SQLAlchemy's modification tracking. This can improve performance,
# # especially in larger applications, by turning off automatic tracking of database changes.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # Configures the JSON serialization options for the Flask application.
# # Setting compact to False means that the JSON output will be formatted with whitespace for readability.
app.json.compact = False

# Define metadata, instantiate db
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# Creates an instance of SQLAlchemy and associates it with the custom naming convention defined earlier.
db = SQLAlchemy(metadata=metadata)

# Initializes database migration with Flask-Migrate,
# which allows for easier database schema changes and versioning.
migrate = Migrate(app, db)

# Initializes the SQLAlchemy extension with the Flask application.
db.init_app(app)

# # Sets up a Flask-RESTful API instance for creating RESTful web services in the Flask application
api = Api(app)

# Instantiate CORS
CORS(app)

# Initializes the SQLAlchemy extension with the Flask application.
bcrypt = Bcrypt()
