#!/usr/bin/python3
"""
A simple Flask API for demonstration purposes.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"},
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"}}


def home():
    return "Welcome to the Flask API!"


def get_usernames():
    return jsonify(list(users.keys()))


def status():
    return "OK"


def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


def add_user():
    user_data = request.json
    if 'username' not in user_data:
        return jsonify({"error": "Username is required"}), 400

    username = user_data['username']
    if username in users:
        return jsonify({"error": "User already exists"}), 409

    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    app.run()
