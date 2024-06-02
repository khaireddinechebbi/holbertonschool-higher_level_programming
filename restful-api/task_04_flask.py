from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionary to store user data
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Route to welcome message
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Route to return list of usernames
@app.route('/data')
def data():
    return jsonify(list(users.keys()))

# Route to return status
@app.route('/status')
def status():
    return "OK"

# Route to return user data based on username
@app.route('/users/<username>')
def user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"})

# Route to add new user
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    if username:
        users[username] = data
        return jsonify({"message": "User added", "user": data})
    else:
        return jsonify({"error": "Username not provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)
