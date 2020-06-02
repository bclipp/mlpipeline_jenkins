"""

"""

import pandas as pd
import psycopg2
import psycopg2.extras

import modules.sql as sql


class DatabaseManager():
    """

    """

    def __init__(self, config):
        self.config = config
        self.conn = None
        self.cursor = None

    def connect_db(self):
        user = self.config["username"]
        password = self.config["password"]
        host = self.config["ip"]
        # port = self.config_dict["port"]
        database = self.config["database"]
        conn = psycopg2 \
            .connect(f"dbname={database} user={user} host={host} password={password}")
        self.cursor = conn.cursor()
        self.conn = conn
        self.conn.autocommit = True

    def receive_sql_fetchall(self,
                             sql_query: str) -> pd.DataFrame:
        try:
            self.cursor.execute(sql_query)
        except psycopg2.DatabaseError as error:
            print(error)
            self.conn.rollback()
        return self.cursor.fetchall()

    def send_sql(self,
                 sql_query: str) -> pd.DataFrame:
        try:
            self.cursor.execute(sql_query)
        except psycopg2.DatabaseError as error:
            print(error)
            self.conn.rollback()

    def df_to_sql(self,
                  data_frame: pd.DataFrame,
                  table: str):
        try:
            if len(data_frame) > 0:
                data_frame_columns = list(data_frame)
                columns = ",".join(data_frame_columns)
                values = "VALUES({})".format(",".join(["%s" for _ in data_frame_columns]))
                insert_stmt = "INSERT INTO {} ({}) {}".format(table, columns, values)
                psycopg2.extras.execute_batch(self.cursor, insert_stmt, data_frame.values)
                # self.conn.commit()
        except psycopg2.DatabaseError as error:
            print(error)
            self.conn.rollback()

    def close_conn(self):
        self.cursor.close()


def initialize_database(database_manager: DatabaseManager,
                        table: str):
    """
    :param database_manager:
    :return:
    """
    database_manager.connect_db()
    database_manager.send_sql(sql_query=sql.create_stock_table(table))

