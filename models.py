from config import db
from sqlalchemy.orm import validates
from datetime import date

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    firstName = db.Column(db.String(80), nullable=False)
    lastName = db.Column(db.String(80), nullable=False)
    tel = db.Column(db.String(10), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    birthDate = db.Column(db.String(20), nullable=False) 
    address = db.Column(db.String(200), nullable=True)  

    @validates('password')
    def validate_password(self, key, password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if len(password) > 20:
            raise ValueError("Password must be at most 20 characters long")
        return password

    def to_json(self):
        return {
            'id': self.id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'email': self.email,
            'tel': self.tel,
            'gender': self.gender,
            'birthDate': self.birthDate,  # Convert date object to ISO format string
            # 'address': self.address,  # Uncomment and use if needed
        }

# Example usage
# user = User(f_name="John", l_name="Doe", email="john.doe@example.com", password="securepass123", tel="1234567890", gender="Male", birthDate=date(1990, 1, 1))
# print(user.to_json())
