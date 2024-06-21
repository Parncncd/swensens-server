from flask import request, jsonify
from config import app
from models import User

@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({'message': 'Customer does not exist (invalid email)'}), 403
    
    if user.password != password:
        return jsonify({'message': 'You have entered an invalid username or password please try again'}), 401
    
    return jsonify({
        'message': 'Login successful',
        'user': user.to_json()
    }), 200
