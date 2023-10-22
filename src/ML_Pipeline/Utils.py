# Import the pickle module, which is used for serializing and deserializing Python objects
import pickle

# Define a function to save a machine learning model to a file
def save_model(model):
    # Open a binary file in write mode for saving the model
    with open('../output/ml_model.pkl', 'wb') as output:
        # Use pickle to serialize and save the model to the file
        pickle.dump(model, output, pickle.HIGHEST_PROTOCOL)

# Define a function to load a machine learning model from a file
def load_model():
    # Open a binary file in read mode for loading the model
    with open('../output/ml_model.pkl', 'rb') as model:
        # Use pickle to deserialize and load the model from the file
        ml_model = pickle.load(model)
        # Return the loaded model for further use in the code

# These functions provide a convenient way to save and load machine learning models,
# allowing you to persist trained models for future use in your applications.
