Ideal Function Selector

This project is a Python implementation for selecting suitable ideal functions based on training data and assigning test data points to those functions using a deviation limit. The main idea is to avoid visual guessing and instead rely on numerical error calculations to decide which functions fit best.

Training data is compared against a fixed set of ideal functions using a least-squares approach. For each training function, the ideal function with the lowest overall error is selected. Test data points are then checked against these selected functions and only assigned if their deviation stays within an acceptable range. All data and results are stored in an SQLite database, and plots are generated to visually verify the outcome.

The project uses Pandas for data handling, SQLAlchemy for database access, and Bokeh for visualization. The database is created automatically when the program runs.

How to run:
pip install -r requirements.txt
python src/main.py

Notes:
This project was created as part of a data analysis assignment and focuses on clear structure, reproducibility, and correctness rather than performance optimization.
