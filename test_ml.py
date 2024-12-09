import pytest
# TODO: add necessary import
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from ml.data import process_data
from ml.model import (
    compute_model_metrics,
    inference,
    load_model,
    performance_on_categorical_slice,
    save_model,
    train_model,
)

# TODO: implement the first test. Change the function name and input as needed
@pytest.fixture
def model():

    project_path = "data"
    data_path = os.path.join(project_path, "census.csv")
    data = pd.read_csv(data_path)

    model_path = os.path.join(project_path, "model", "model.pkl")
    model = load_model(
    model_path
    ) 

    return model


def test_one(model):
    """
    # add description for the first test
    Ensure model has 15 columns
    """ 
    assert model.shape == 15
    pass

def train_test():

    data_train, data_test = train_test_split(data,
    test_size=0.2, random_state=42)

    return train_test

# TODO: implement the second test. Change the function name and input as needed
def test_two(train_test):
    """
    # add description for the second test
    ensure dataset has effectively split into training and testing sets
    """
    # Your code here
    assert len(data_train) < 32560
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_three(train_test):
    """
    # add description for the third test
    ensure dataset has effectively split into training and testing sets
    """
    # Your code here
    assert len(data_test) < 32560
    pass
