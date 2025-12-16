import pandas as pd
from selector import FunctionSelector

def test_find_best_ideals_simple():
    train = pd.DataFrame({
        "x": [0, 1],
        "y1": [1, 2]
    })
    ideal = pd.DataFrame({
        "x": [0, 1],
        "y1": [1, 2],  # perfect match
        "y2": [100, 200]
    })
    selector = FunctionSelector(train, ideal)
    mapping = selector.find_best_ideals()
    assert mapping["y1"] == "y1"
