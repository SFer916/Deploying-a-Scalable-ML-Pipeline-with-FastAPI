import pytest
# TODO: add necessary import
import numpy as np
from sklearn.metrics import precision_score, recall_score, fbeta_score
from train_model import compute_model_metrics, process_data

# TODO: implement the first test. Change the function name and input as needed
@pytest.fixture(scope="session")
def test_one(y_test, preds):
    """
    # add description for the first test
    testing if fbeta score is less than 1
    """
    y_test = [0,1,0,1]
    preds = [0,1,0,1]
    p, r, fb = compute_model_metrics(y_test, preds)
    assert fb < 1
    pass

# TODO: implement the second test. Change the function name and input as needed
def test_two(y_test, preds):
    """
    # add description for the second test
    testing if precision is less than 1
    """
    # Your code here
    y_test = [0,1,0,1]
    preds = [0,1,0,1]
    p, r, fb = compute_model_metrics(y_test, preds)
    assert p < 1
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_three(y_test, preds):
    """
    # add description for the third test
    testing if precision is less than 1
    """
    # Your code here
    y_test = [0,1,0,1]
    preds = [0,1,0,1]
    p, r, fb = compute_model_metrics(y_test, preds)
    assert r < 1
    pass
