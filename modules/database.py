"""

"""

import pandas as pd
import psycopg2
from psycopg2 import pool


class DatabaseManager():
    """

    """

    def __init__(self, config_dict):
        self.config_dict = config_dict
        self.conn = None
        self.pool = None
        self.cursor = None

    def connect_db(self):
        user = self.config_dict["username"]
        password = self.config_dict["password"]
        host = self.config_dict["ip"]
        # port = self.config_dict["port"]
        database = self.config_dict["database"]
        conn = psycopg2 \
            .connect(f"dbname={database} user={user} host={host} password={password}")
        self.cursor = conn.cursor()
        self.conn = conn

    def receive_sql_fetchall(self,
                             sql: str) -> pd.DataFrame:
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def send_sql(self,
                 sql: str) -> pd.DataFrame:
        self.execute(sql)

    def close_conn(self):
        self.cursor.close()
        self.pool.putconn(self.conn)
        self.pool.closeall


class DatabaseManager2():
    """

    """

    def __init__(self, config_dict):
        self.config_dict = config_dict
        self.conn = None
        self.pool = None
        self.cursor = None

    def connect_db(self):
        psypool = psycopg2.pool.SimpleConnectionPool(1,
                                                     20,
                                                     user=self.config_dict["username"],
                                                     password=self.config_dict["password"],
                                                     host=self.config_dict["ip"],
                                                     port=self.config_dict["port"],
                                                     database=self.config_dict["database"])
        if (self.pool):
            print("Connection pool created successfully")
        self.pool = psypool
        self.conn = self.pool.getconn()
        self.cursor = self.conn.cursor()

    def receive_sql_fetchall(self,
                             sql: str) -> pd.DataFrame:
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def send_sql(self,
                 sql: str) -> pd.DataFrame:
        self.execute(sql)

    def close_conn(self):
        self.cursor.close()
        self.pool.putconn(self.conn)
        self.pool.closeall


def initialize_database(database_manager: DatabaseManager) -> pd.DataFrame:
    test_dict = {"Open": 1.2,
                 "High": 1.2,
                 "Low": 1.2,
                 "Close": 1.2,
                 "Volume": 1,
                 "Dividends": 1,
                 "Stock Splits": 1}
    data_frame: pd.DataFrame = pd.DataFrame(test_dict, index=test_dict.keys())
    return data_frame
