# Import necessary libraries and modules
from flask import Flask
from flask_restful import Resource, Api
from ML_Pipeline import Utils

# Create a Flask application
class FeastPred(Resource):
    def __init__(self, model):
        self.model = model

    # Define a GET request handler
    def get(self):
        # Placeholder response, you can modify this to return predictions
        return {'ans': 'success'}

# Initialization function for your application
def init():
    app = Flask(__name__)
    api = Api(app)

    # Load the machine learning model using Utils
    uploaded_model = Utils.load_model()

    # Add the FeastPred resource to your API
    api.add_resource(FeastPred, '/', resource_class_kwargs={'model': uploaded_model})

    # Start the Flask application on port 12345
    app.run(port=12345)

# This code defines a basic Flask application with a single resource (FeastPred).
# The GET method is defined in the FeastPred class, which currently returns a 'success' response.
# The init() function initializes the Flask app, loads the model, and starts the application on port 12345.
