import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_model():
    print('Loading dataframe from csv')
    dataframe = pd.read_csv("model/configs_dataset.csv")

    X = dataframe.drop(columns=["classification", "bucket_name"], axis=1)
    y = dataframe["classification"]

    print('Training model with generated dataset')
    model = RandomForestClassifier()
    model.fit(X, y)

    return model
