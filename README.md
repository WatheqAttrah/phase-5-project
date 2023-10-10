# phase-5-project
## Project 5 Guideline & Requirements
- [Phase 5 Full-Stack Application Project Template](https://my.learn.co/courses/655/pages/phase-5-full-stack-application-project-template?module_item_id=90938)
- [Phase 5 Project Guidelines And Schedule](https://my.learn.co/courses/655/pages/phase-5-project-guidelines-and-schedule?module_item_id=83806)

## Creating Your Own Git Repo
- New Repo in Github.
- Clone & Copy the SSH Key

## Local Machine 
- Select the directory intended to clone the repo in.
- Open the Terminal  
- Run command `git@github.com:WatheqAttrah/phase-5-project.git`

## Backend Setup 
================

## `server/` directory contains all the backend code.
### Install Python Virtual Environment Tool 
- Run command `pipenv install`
- Enter the shell with `pipenv shell`


### Packages Installed 
- [Resources](https://pypi.org/)
- Run the following command before each package 
    - `pipenv install [Package]`

- `flask-sqlalchemy`
    - provide ways to interact with several database.
- `flask-migrate` = "*"
    - Handles SQLAlchemy database migrations.
- `sqlalchemy-serializer`
    - SQLAlchemy model to become serializable.
- `flask-restful`
    - Adds support for handling REST APIs in Python.
- `flask-cors`
    - Enables communications with resources in many domains
- `flask-marshmallow`
    - adds additional features to marshmallow, including URL and Hyperlinks fields for HATEOAS-ready APIs.
- `faker` 
    - To generate Fake data
- `faker-vehicle`
    - Provides vehicle and machinery related fake data for testing purposes.
- `faker-sqlalchemy`
    - Provider for the Faker library that helps populate SQLAlchemy ORM models.
- `gunicorn`
    - Python Web Server Gateway Interface (WSGI) HTTP serve
- `bcrypt-flask`
    - hashing function for password
- `flask`
    - Flask is a lightweight WSGI web application framework
- `psycopg-binary`
    - create and destroy lots of cursors and create a large number of “INSERTs” or “UPDATEs” 
- `requests`
    - Using requests, you can get, post, delete, update the data for the URL given.

## Create Backend files
-  Test Python Environment test=Pass
- config.py
    - Python application configurations.
        - app = Flask
        - app.secret key
        - metaadata
        - app.json
        - CORS
        - bcrypt

- app.py
    - Routes to the API's [ '/' Home | Checksession , Login , Signup, Signout, Clearsession, CarByID ], 
    - HTTP GET | POST | Delete


- models.py
    - User Model [ id , username, admin, hashed_password]
    - Car Model [ id, make, model, year, vin, image , engine , miles]
    - Review Model [ id ,review, created_at, updated_at, user_id, car_id]
    - Many-To Many Realtionship [ Car - Review ]


- seed.py
    - Seed Fake Data for testing reasons.
        - Faker()
        - FakerVehicle() to generate fake car data.
        - Created Fake Associattion Table [ Car <=> Review ]



## Frontend 
- Create client directory
    - Run `mkdir client`
- - Create react app inside /client directory.
    - Run `npm create-react-app client`
- Install Node 
    - Run `npm install --prefix client`

- Components
    - Home.js
    - App.js
    - Login.js 
    - Signup.js
    - NavBar.js 
    - CarCard.js
    - CarList.js
    - AddReview.js



