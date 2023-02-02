# from flask import Flask, jsonify
# from flask_httpauth import HTTPDigestAuth
# import random

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret key here'
# auth = HTTPDigestAuth()

# users = {
#     "vcu":"rams"
# }

# @auth.get_password
# def get_pw(username):
#     if username in users:
#         return users.get(username)
#     return None

# @app.route('/pong')
# # @auth.login_required
# def index():
#     return jsonify({"random number":random.randint(0,100)}),201


from random import randint
from flask import Flask, jsonify
from flask_httpauth import HTTPDigestAuth as Flaskauth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key here'
auth = Flaskauth()

users = {
    "vcu": "rams"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/pong')
# @auth.login_required
def index():
    return jsonify(randint(1,10)), 201