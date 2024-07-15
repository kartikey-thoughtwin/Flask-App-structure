from datetime import datetime
from app import db

class User(db.Model):
    """
    User model for storing user details.

    Attributes:
        id (int): The primary key for the user.
        name (str): The name of the user.
        created_at (datetime): The timestamp when the user was created.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        """
        Returns a string representation of the User instance.

        Returns:
            str: A string representation of the User instance.
        """
        return f'<User {self.name}>'

    def to_dict(self):
        """
        Converts the User instance to a dictionary.

        Returns:
            dict: A dictionary representation of the User instance.
        """
        return {
            "id": self.id,
            "name": self.name,
        }