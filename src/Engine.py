# Import necessary modules and classes from your custom ML_Pipeline
from ML_Pipeline import Preprocess, Train, Utils, Deploy
from datetime import datetime  # Import the datetime module for date/time manipulation
from feast import FeatureStore  # Import Feast's FeatureStore module for managing feature data

# Initialize a Feast FeatureStore with the specified repository path
store = FeatureStore(repo_path="../feast_repo/")

# Define a list of feature references you want to use for training and prediction
features = [
    "customer_hourly_stats:category",
    "customer_hourly_stats:order_gmv",
    "customer_hourly_stats:sex",
    "customer_hourly_stats:age",
    "customer_hourly_stats:credit_type",
    "customer_hourly_stats:churned",
]

# Define a range of customer IDs
id_range = range(1, 892)

# Define a start date for the data
start_date = datetime(1992, 5, 1, 0, 0, 0)

# Create training data by preprocessing and fetching features from the FeatureStore
training_df = Preprocess.create_training_data(store, fetch_features=features, id_range=id_range, start_date=start_date)

# Select a subset of features for training
select_features = [
    'customer_hourly_stats__category',
    'customer_hourly_stats__order_gmv',
    'customer_hourly_stats__sex',
    'customer_hourly_stats__age',
    'customer_hourly_stats__credit_type',
]

# Define the target variable for training
target_var = ["customer_hourly_stats__churned"]

# Fit a model using the training data and selected features
model = Train.fit_model(training_df, select_features, target_var)

# Save the trained model using the Utils module
Utils.save_model(model)

# Initialize the deployment process using the Deploy module
Deploy.init()
