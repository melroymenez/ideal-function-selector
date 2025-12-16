from datasets import TrainingDataSet, IdealFunctionSet, TestDataSet
from database import DatabaseManager
from selector import FunctionSelector
from mapper import TestMapper
from visualizer import plot_results


def main():
    train = TrainingDataSet()
    train.load_from_csv(r"C:/Users/salda/OneDrive/Desktop/project/data/train.csv")

    ideal = IdealFunctionSet()
    ideal.load_from_csv(r"C:/Users/salda/OneDrive/Desktop/project/data/ideal.csv")

    test = TestDataSet()
    test.load_from_csv(r"C:/Users/salda/OneDrive/Desktop/project/data/test.csv")

    db = DatabaseManager("assignment.db")
    db.store_dataframe(train.df, "train_data")
    db.store_dataframe(ideal.df, "ideal_functions")
    db.store_dataframe(test.df, "test_raw")

    selector = FunctionSelector(train.df, ideal.df)

    # print full error list + get mapping
    mapping = selector.find_best_ideals(verbose=True)
    print("\nBest ideal per training function:", mapping)

    # store complete error table for 3.2
    db.store_dataframe(selector.error_table, "ideal_errors")

    # max deviations, keyed by IDEAL function
    max_devs = {}
    for t_col, i_col in mapping.items():
        max_devs[i_col] = selector.max_deviation(t_col, i_col)

    mapper = TestMapper(test.df, ideal.df, mapping, max_devs)
    mapped_test_df = mapper.map_points()

    db.store_dataframe(mapped_test_df, "test_mapped")

    plot_results(train.df, test.df, mapped_test_df)


if __name__ == "__main__":
    main()
