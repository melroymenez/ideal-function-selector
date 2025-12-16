import math
import pandas as pd

class TestMapper:
    def __init__(self, test_df, ideal_df, mapping, max_devs):
        # mapping: {train_col -> ideal_col}
        # max_devs: {ideal_col -> max_dev}   (if you use Option B above)
        self.test_df = test_df
        self.ideal_df = ideal_df
        self.mapping = mapping
        self.max_devs = max_devs

    def map_points(self, verbose=False):
        rows = []

        for _, row in self.test_df.iterrows():
            x_test = float(row["x"])
            y_test = float(row["y"])

            best_ideal = None
            best_delta = None

            # loop over the 4 selected ideal functions
            for train_col, ideal_col in self.mapping.items():
                # get the ideal y for this x
                ideal_row = self.ideal_df[self.ideal_df["x"] == x_test]
                if ideal_row.empty:
                    continue

                y_ideal = float(ideal_row[ideal_col].iloc[0])
                delta = abs(y_test - y_ideal)

                allowed = math.sqrt(2) * self.max_devs[ideal_col]

                # only consider if inside threshold
                if delta <= allowed:
                    if best_delta is None or delta < best_delta:
                        best_delta = delta
                        best_ideal = ideal_col

            # if we found a valid mapping, save it
            if best_ideal is not None:
                rows.append(
                    {
                        "x": x_test,
                        "y": y_test,
                        "delta_y": best_delta,
                        "ideal_func": best_ideal,
                    }
                )

                if verbose:
                    print(
                        f"Best mapping for x={x_test}, y={y_test}: "
                        f"ideal_function={best_ideal}, deviation={best_delta}"
                    )

        return pd.DataFrame(rows)
