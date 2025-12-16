from sqlalchemy import create_engine

class DatabaseManager:
    def __init__(self, db_path: str = "assignment.db"):
        self.engine = create_engine(f"sqlite:///{db_path}")

    def store_dataframe(self, df, table_name: str):
        df.to_sql(table_name, self.engine, if_exists="replace", index=False)
