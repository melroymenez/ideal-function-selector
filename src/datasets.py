import pandas as pd

class BaseDataSet:
    def __init__(self, df: pd.DataFrame | None = None):
        self.df = df

    def load_from_csv(self, path: str):
        try:
            self.df = pd.read_csv(path)
        except FileNotFoundError as e:
            # custom exception or re-raise
            raise e

class TrainingDataSet(BaseDataSet):
    def get_training_columns(self):
        return ["y1", "y2", "y3", "y4"]

class IdealFunctionSet(BaseDataSet):
    def get_ideal_columns(self):
        # all columns except 'x'
        return [c for c in self.df.columns if c != "x"]

class TestDataSet(BaseDataSet):
    def iterate_points(self):
        for _, row in self.df.iterrows():
            yield row["x"], row["y"]
