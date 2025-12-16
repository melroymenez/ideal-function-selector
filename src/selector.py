import numpy as np
import pandas as pd

class FunctionSelector:
    def __init__(self, train_df, ideal_df):
        self.train_df = train_df
        self.ideal_df = ideal_df
        self.error_table = None  

    def _compute_error_table(self):
        rows = []
        train_cols = [c for c in self.train_df.columns if c != "x"]
        ideal_cols = [c for c in self.ideal_df.columns if c != "x"]

        for t_col in train_cols:
            t_values = self.train_df[t_col].values
            for i_col in ideal_cols:
                i_values = self.ideal_df[i_col].values
                sse = float(np.sum((t_values - i_values) ** 2))
                rows.append({
                    "train_func": t_col,
                    "ideal_func": i_col,
                    "sse": sse
                })

        self.error_table = pd.DataFrame(rows)

    def find_best_ideals(self, verbose=False):
        if self.error_table is None:
            self._compute_error_table()

        mapping = {}
        train_cols = [c for c in self.train_df.columns if c != "x"]

        for t_col in train_cols:
            subset = self.error_table[self.error_table["train_func"] == t_col]
            best_row = subset.loc[subset["sse"].idxmin()]
            best_ideal = best_row["ideal_func"]
            mapping[t_col] = best_ideal

            if verbose:
                print(f"\nErrors for {t_col}:")
                for _, row in subset.iterrows():
                    print(f"  Error for {t_col} with {row['ideal_func']}: {row['sse']}")

        return mapping

    def max_deviation(self, train_col, ideal_col):
        diff = np.abs(self.train_df[train_col] - self.ideal_df[ideal_col])
        return float(diff.max())
