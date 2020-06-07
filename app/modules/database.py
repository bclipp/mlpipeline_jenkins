"""
This module is for abstracted intearctions with the stocks database
"""

import pandas as pd  # type: ignore
import psycopg2  # type: ignore
import psycopg2.extras  # type: ignore

import modules.sql as sql  # type: ignore


class DatabaseManager:
    """
    Used as the main interactions with the postgresql database.

    """

    def __init__(self, config):
        self.config = config
        self.conn = None
        self.cursor = None

    def connect_db(self):
        """
        Used to setup the initial connection to the databse. Direct access is
        not given for testing purposes.
        :return:
        """
        user = self.config["username"]
        password = self.config["password"]
        host = self.config["db_ip"]
        # port = self.config_dict["port"]
        database = self.config["database"]
        conn = psycopg2.connect(
            f"dbname={database} user={user} host={host} password={password}"
        )
        self.cursor = conn.cursor()
        self.conn = conn
        self.conn.autocommit = True

    def receive_sql_fetchall(self, sql_query: str) -> pd.DataFrame:
        """
        receive_sql_fetchall is used to send a query, and get all the data right away.

        :param sql_query: am SQL query
        :return:
        """
        try:
            self.cursor.execute(sql_query)
        except psycopg2.DatabaseError as error:
            print(error)
            self.conn.rollback()
        return self.cursor.fetchall()

    def send_sql(self, sql_query: str) -> pd.DataFrame:
        """
        send_sql is used to send a query but not receive any data.
        :param sql_query:
        :return:
        """
        try:
            self.cursor.execute(sql_query)
        except psycopg2.DatabaseError as error:
            print(error)
            self.conn.rollback()

    def df_to_sql(self, data_frame: pd.DataFrame, table: str):
        """
        df_to_sql is used for UPDATING a table with a dataframe.
        :param data_frame: dataframe in question, verify schema matches target table
        :param table: table to update
        :return:
        """
        try:
            if not data_frame.empty:
                data_frame_columns = list(data_frame)
                columns = ",".join(data_frame_columns)
                values = "VALUES({})".format(
                    ",".join(["%s" for _ in data_frame_columns])
                )
                insert_stmt = "INSERT INTO {} ({}) {}".format(table, columns, values)
                psycopg2.extras.execute_batch(
                    self.cursor, insert_stmt, data_frame.values
                )
                # self.conn.commit()
        except psycopg2.DatabaseError as error:
            print(error)
            self.conn.rollback()

    def close_conn(self):
        """
        an abstracted way to control database connection.
        :return:
        """
        self.cursor.close()


def initialize_database(database_manager: DatabaseManager, table: str):
    """
    initialize_database is a a simple abstraction to setup the database.

    :param database_manager: to manage the database.
    :param table: table to setup
    :return:
    """
    database_manager.connect_db()
    database_manager.send_sql(sql_query=sql.create_stock_table(table))
