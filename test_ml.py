import pytest
# TODO: add necessary import
import numpy as np
from sklearn.metrics import precision_score, recall_score
from ml.model import inference, compute_model_metrics, performance_on_categorical_slice
from ml.data import process_data

def process_data(
    X, categorical_features=[], label=None, training=True, encoder=None, lb=None
):
    if label is not None:
        y = X[label]
        X = X.drop([label], axis=1)
    else:
        y = np.array([])

    X_categorical = X[categorical_features].values
    X_continuous = X.drop(*[categorical_features], axis=1)

    if training is True:
        encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
        lb = LabelBinarizer()
        X_categorical = encoder.fit_transform(X_categorical)
        y = lb.fit_transform(y).ravel()
    else:
        X_categorical = encoder.transform(X_categorical)
        try:
            y = lb.transform(y.values).ravel()
        # Catch the case where y is None because we're doing inference.
        except AttributeError:
            pass

    X = np.concatenate([X_continuous, X_categorical], axis=1)
    return X, y, encoder, lb

# TODO: implement the first test. Change the function name and input as needed
@pytest.fixture(scope="session")
def test_one(model):
    """
    # add description for the first test
    Ensure model has 15 columns
    """ 
    assert model.shape == 15
    pass

# TODO: implement the second test. Change the function name and input as needed
def test_two(y, preds):
    """
    # add description for the second test
    testing if precision is less than 1
    """
    # Your code here
    precision = precision_score(y, preds, zero_division=1)
    assert precision < 1
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_three(y, preds):
    """
    # add description for the third test
    testing if precision is less than 1
    """
    # Your code here
    recall = recall_score(y, preds, zero_division=1)
    assert recall < 1
    pass
