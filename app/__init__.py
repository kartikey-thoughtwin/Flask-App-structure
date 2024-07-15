from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from instance.config import Config
from flask_restx import Api

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Flask-RESTX API
api = Api(app, version="1.0", title="API", description="Simple API")

# Initialize SQLAlchemy database
db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Import models and routes
from app.models import User
from app.routes import API
