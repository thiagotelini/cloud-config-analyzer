import random
import pandas as pd

def classify(row):
    if row["public_read"] == 1 or row["acl_all_users"] == 1:
        return "insecure"

    if row["encryption"] == 0:
        return "attention"

    return "secure"

def mock_config():
    row = {
        "bucket_name": "generic-bucket",
        "public_read": random.choice([0, 1]),
        "encryption": random.choice([0, 1]),
        "acl_all_users": random.choice([0, 1])
    }

    classification = classify(row)
    row["classification"] = classification
    
    return row

def data_set_generator():
    print('Creating Dataset')
    dataset = [mock_config() for _ in range(100)]

    print('Creating Dataframe')
    dataframe = pd.DataFrame(dataset)

    print('Exporting Dataframe as csv')
    dataframe.to_csv("model/configs_dataset.csv", index=False)