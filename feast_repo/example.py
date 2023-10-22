# This is an example feature definition file

from google.protobuf.duration_pb2 import Duration

from feast import Entity, Feature, FeatureView, ValueType
from feast.data_source import FileSource


# Read data from parquet files. Parquet is convenient for local development mode. For
# production, you can use your favorite DWH, such as BigQuery. See Feast documentation
# for more info.
customer_hourly_stats = FileSource(
    path="C:/Users/bhaga/Downloads/Feast-Feature-Store/feast_repo/data/buyer_credit_data.parquet",
    event_timestamp_column="created_at",
    created_timestamp_column="created_at",
)

# Define an entity for the customer. You can think of entity as a primary key used to
# fetch features.
customer = Entity(name="customer_id", value_type=ValueType.INT32, description="customer id",)

# Our parquet files contain sample data that includes a customer_id column, timestamps and
# three feature column. Here we define a Feature View that will allow us to serve this
# data to our model online.
customer_hourly_stats_view = FeatureView(
    name="customer_hourly_stats",
    entities=["customer_id"],
    ttl=Duration(seconds=30 * 24 * 60 * 60 * 1),
    features=[
        Feature(name="churned", dtype=ValueType.INT32),
        Feature(name="sex", dtype=ValueType.STRING),
        Feature(name="category", dtype=ValueType.STRING),
        Feature(name="age", dtype=ValueType.INT32),
        Feature(name="order_gmv", dtype=ValueType.FLOAT),
        Feature(name="credit_type", dtype=ValueType.STRING),
    ],
    online=True,
    input=customer_hourly_stats,
    tags={},
)
