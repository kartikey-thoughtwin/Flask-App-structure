import os

class Config:
    """
    Configuration class for the Flask application.

    Attributes:
        SQLALCHEMY_DATABASE_URI (str): Database URI for SQLAlchemy.
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/test'
