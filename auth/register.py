from flask import request, jsonify
from config import app, db
from models import User

@app.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')
    email = User.query.get(email)
    if email:
        return jsonify(
            {
                'message':'This email address has already been registered, please login.'
            }
        ), 409
    else:        
        firstName = request.json.get('firstName')
        lastName = request.json.get('lastName')
        email = request.json.get('email')
        password = request.json.get('password')
        tel = request.json.get('tel')
        gender = request.json.get('gender')
        birthDate = request.json.get('birthDate')
        # address = request.json.get('address')
            
        new_user = User(
            firstName=firstName, 
            lastName=lastName, 
            email=email,
            password=password, 
            tel=tel, 
            gender=gender,
            birthDate=birthDate,
            # address=address,
            )
        try:
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            return jsonify({'message':str(e)}), 400
        return jsonify({
            'message' : 'User created'
        }), 201