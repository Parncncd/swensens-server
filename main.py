from config import app, db
from models import User
from auth.login import login
from auth.register import register
from flask import request, jsonify


@app.route('/users', methods = ['GET'])
def get_user():
    users = User.query.all()
    json_contacts = list(map(lambda x: x.to_json(), users))
    return jsonify({"users": json_contacts})

@app.route('/update_userinfo/<int:user_id>', methods = ['PATCH'])
def update_userinfo(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify(
            {
                'message':'User not found'
            }
        ), 404
    
    data = request.json
    user.firstName = data.get('firstName', user.firstName)
    user.lastName = data.get('lastName', user.lastName)
    user.email = data.get('email', user.email)
    
    db.session.commit()
    
    return jsonify({
        'message': ' User updated'
    }), 200

@app.route('/delete_user/<int:user_id>', methods = ['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted!"}), 200

if __name__ == '__main__' :
    with app.app_context() :
        db.create_all()
    app.run(host="0.0.0.0",debug=True)