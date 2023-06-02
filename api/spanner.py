# Imports the Google Cloud Client Library.
from google.cloud import spanner

# Your Cloud Spanner instance ID.
# instance_id = "my-instance-id"
#
# Your Cloud Spanner database ID.
# database_id = "my-database-id"

# Instantiate a client.

instance_id = "test-instance"
database_id="test-database"
spanner_client = spanner.Client()

# Get a Cloud Spanner instance by ID.
instance = spanner_client.instance(instance_id)

# Get a Cloud Spanner database by ID.
database = instance.database(database_id)

# Execute a simple SQL statement.
with database.snapshot() as snapshot:
    results = snapshot.execute_sql("SELECT * from attributes")

    for row in results:
        print(row)
print('hello')