from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1> Welcome to Phase 5 Project </h1>'


@app.route('/<string:username>')
def user_name(username):
    return f'<h2>Profile for {username}</h2>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
