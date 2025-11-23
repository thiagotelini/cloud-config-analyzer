import json
import pandas as pd
from analyzer.json_configurations_adapter import adapt_bucket_config

def get_data_to_analyze():
    secure_bucket_data = json.load(open("analyzer/data_mocks/secure_bucket.json"))
    insecure_bucket_data = json.load(open("analyzer/data_mocks/insecure_bucket.json"))
    attention_bucket_data = json.load(open("analyzer/data_mocks/attention_bucket.json"))

    secure_bucket = adapt_bucket_config(secure_bucket_data)
    insecure_bucket = adapt_bucket_config(insecure_bucket_data)
    attention_bucket = adapt_bucket_config(attention_bucket_data)

    return [secure_bucket, insecure_bucket, attention_bucket]

def analyze(model):
    print('Getting data to analyze')
    buckets_to_check = get_data_to_analyze()

    model_input = pd.DataFrame(buckets_to_check)
    bucket_names = model_input["bucket_name"]

    model_input = model_input.drop(columns=["bucket_name"])
    
    print('Returning model predict')
    predictions = model.predict(model_input)
    
    return list(zip(bucket_names, predictions))

