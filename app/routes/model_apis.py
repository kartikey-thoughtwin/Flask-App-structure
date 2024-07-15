from flask_restx import Resource
from app import api

class API(Resource):
    """
    API Resource class for handling HTTP requests.

    This class defines a simple GET API that returns a 'Hello, World!' message.
    """

    def get(self):
        """
        Handle GET requests.

        This method handles GET requests and returns a JSON response with a 'Hello, World!' message.

        Returns:
            dict: A dictionary containing a message.
        """
        return {"message": "Hello, World!"}

# Register the API resource with the Flask-RESTX API
api.add_resource(API, "/hello/", methods=["GET"])
