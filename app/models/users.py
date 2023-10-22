from app import db
from bcrypt import hashpw, gensalt, checkpw


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    items = db.relationship('Item', back_populates='user')

    def set_password(self, password):
        # Hash and set the user's password
        salt = gensalt()
        self.password = hashpw(password.encode("utf-8"), salt)

    def check_password(self, password):
        # Check if the provided password matches the stored hash
        return checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

