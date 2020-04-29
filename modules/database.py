"""

"""

import pandas as pd
import psycopg2
from psycopg2 import pool
import psycopg2.extras

import modules.sql as sql


class DatabaseManager():
    """

    """

    def __init__(self, config_dict):
        self.config_dict = config_dict
        self.conn = None
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
                             sql_query: str) -> pd.DataFrame:
        self.cursor.execute(sql_query)
        return self.cursor.fetchall()

    def send_sql(self,
                 sql: str) -> pd.DataFrame:
        self.cursor.execute(sql)

    def df_to_sql(self,
                  data_frame: pd.DataFrame,
                  table: str):
        if len(data_frame) > 0:
            data_frame_columns = list(data_frame)
            columns = ",".join(data_frame_columns)
            values = "VALUES({})".format(",".join(["%s" for _ in data_frame_columns]))
            insert_stmt = "INSERT INTO {} ({}) {}".format(table, columns, values)
            psycopg2.extras.execute_batch(self.cursor, insert_stmt, data_frame.values)
            self.conn.commit()

    def close_conn(self):
        self.cursor.close()


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
                             sql_dict: dict) -> pd.DataFrame:
        self.cursor.execute(sql_dict["sql"],
                            sql_dict["data"])
        return self.cursor.fetchall()

    def send_sql(self,
                 sql: str) -> pd.DataFrame:
        self.execute(sql)

    def df_to_sql(self,
                  data_frame: pd.DataFrame):
        if len(data_frame) > 0:
            data_frame_columns = list(data_frame)
            columns = ",".join(data_frame_columns)
            values = "VALUES({})".format(",".join(["%s" for _ in data_frame_columns]))
            insert_stmt = "INSERT INTO {} ({}) {}".format("store", columns, values)
            psycopg2.extras.execute_batch(self.cursor, insert_stmt, data_frame.values)
            self.conn.commit()

    def close_conn(self):
        self.cursor.close()
        self.pool.putconn(self.conn)
        self.pool.closeall


def initialize_database(database_manager: DatabaseManager) -> pd.DataFrame:
    """

    :param database_manager:
    :return:
    """
    database_manager.connect_db()
    database_manager.send_sql(sql=sql.create_stock_table())
    data_frame: pd.DataFrame = database_manager.receive_sql_fetchall(sql_query=sql.select_all_table("stock"))
    return data_frame


# add transation redo https://stackoverflow.com/questions/2979369/databaseerror-current-transaction-is-aborted-commands-ignored-until-end-of-tra