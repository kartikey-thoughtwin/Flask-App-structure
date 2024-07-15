from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from instance.config import Config
from flask_restx import Api

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)
api = Api(app, version="1.0", title="Notes API", description="A simple Notes API")
# Initialize database
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Register blueprint
from .routes import note_bp


app.register_blueprint(note_bp)


