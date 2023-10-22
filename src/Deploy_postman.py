# Import necessary libraries and modules
from flask import Flask, request  # Import Flask for creating a web service
from ML_Pipeline import Utils  # Import Utils from ML_Pipeline for model loading
from feast import FeatureStore  # Import FeatureStore for managing feature data
import pandas as pd  # Import pandas for data manipulation

# Create a Flask web application
app = Flask(__name__)

# Load the machine learning model from Utils
uploaded_model = Utils.load_model()

# Initialize a Feast FeatureStore with the specified repository path
store = FeatureStore(repo_path="../feast_repo/")

# Define a list of feature references you want to use for predictions
features = ['customer_hourly_stats__category', 'customer_hourly_stats__order_gmv',
            'customer_hourly_stats__sex', 'customer_hourly_stats__age',
            'customer_hourly_stats__credit_type']

# Define a route for handling HTTP GET requests
@app.route("/get_churn_score", methods=['GET'])
def get_churn_score():
    # Get the 'customer_id' from the query parameters
    customer_id = request.args.get('customer_id')
    print("Customer Id: ", customer_id)

    # Retrieve online features for the specified customer_id
    pred_df = store.get_online_features(
        feature_refs=[
            "customer_hourly_stats:category",
            "customer_hourly_stats:order_gmv",
            "customer_hourly_stats:sex",
            "customer_hourly_stats:age",
            "customer_hourly_stats:credit_type",
            "customer_hourly_stats:churned",
        ],
        entity_rows=[
            {"customer_id": int(customer_id)},
            {"customer_id": 23},
            {"customer_id": 2},
            {"customer_id": 6},
            {"customer_id": 7},
            {"customer_id": 1},
            {"customer_id": 4},
            {"customer_id": 10}
        ],
    ).to_df()

    # Remove rows with missing values
    pred_df.dropna(inplace=True)

    # Perform one-hot encoding on selected features
    pred_df = pd.get_dummies(data=pred_df[features])

    # Select the row corresponding to the customer_id of interest (assuming 0 is the correct index)
    pred_df = pred_df[pred_df.index == 0]

    # Make predictions using the loaded machine learning model
    pred = uploaded_model.predict(pred_df)

    # Return a response based on the prediction result
    if pred == 0:
        return "Customer won't churn"
    else:
        return "Customer would churn"

# Start the Flask application if this script is executed directly
if __name__ == "__main__":
    app.run(port=12345)
