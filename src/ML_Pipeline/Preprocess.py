import pandas as pd

# Define a function for creating training data
def create_training_data(store, id_range, fetch_features, start_date):
    # Create an entity DataFrame containing customer IDs and event timestamps
    entity_df = pd.DataFrame.from_dict(
        {
            "customer_id": [cust_id for cust_id in id_range],
            "event_timestamp": [start_date for cust_id in id_range],
        }
    )
    
    # Ensure that the 'customer_id' column is of type int32
    entity_df['customer_id'] = entity_df['customer_id'].astype('int32')

    # Fetch historical features from the Feast FeatureStore
    training_df = store.get_historical_features(
        entity_df=entity_df,
        feature_refs=fetch_features,
    ).to_df()

    # Remove rows with missing values
    training_df.dropna(inplace=True)

    return training_df
