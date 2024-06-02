#!/usr/bin/python3
"""
A simple Flask API to demonstrate basic endpoint handling and \
request handling.

Endpoints:
- /: Returns a welcome message.
- /data: Returns a list of usernames stored in the API.
- /status: Returns "OK".
- /users/<username>: Returns user data based on the provided username.
- /add_user: Adds a new user to the API.

Requirements:
- Flask: pip install Flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for user data
users = {}


@app.route("/")
def home():
    """Returns a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Returns a list of usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    """Returns "OK"."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    Returns user data based on the provided username.

    If the user does not exist, returns a JSON response with an \
    error message and a 404 status code.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Adds a new user to the API.

    Accepts POST requests with JSON payload containing user data.
    Returns a JSON response with a confirmation message and the \
    added user's data.
    If the request payload is missing the username, \
    returns an error message with a 400 status code.
    """
    user_data = request.get_json()
    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    app.run()
