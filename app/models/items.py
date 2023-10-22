from app import db
from .users import User  # Import the User model

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Define the foreign key relationship

    user = db.relationship('User', back_populates='items')  # Define the relationship

    def __init__(self, name, description, user_id):
        self.name = name
        self.description = description
        self.user_id = user_id