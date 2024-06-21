# Get started
1. **Clone** this repository
2. run **pip install -r requirements.txt**
3. finally, start the server by running **python main.py**


note. This project use port 5000 for backend.


# API
- POST /login {email, password} => authenticaction (login)
- POST /register {FirstName, LastName, email, password, birthDate, gender (optional), acceptTerms, acceptPromotion) => create new account
- GET /users => get all users in the database
- DELETE /delete_user/<int:user_id> => delete a user with that specific ID
- PUT /update_userinfo/<int:user_id> => update user info
