"""

"""


import pandas as pd
import psycopg2
from psycopg2 import pool




class DatabaseManager():
    """

    """

    def __init__(self, config_dict):
        self.first = config_dict

    def connect_db(self):
        try:
            postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(1, 20, user="postgres",
                                                                 password="pass@#29",
                                                                 host="127.0.0.1",
                                                                 port="5432",
                                                                 database="postgres_db")
            if (postgreSQL_pool):
                print("Connection pool created successfully")

            # Use getconn() to Get Connection from connection pool
            ps_connection = postgreSQL_pool.getconn()

            if (ps_connection):
                print("successfully recived connection from connection pool ")
                ps_cursor = ps_connection.cursor()
                ps_cursor.execute("select * from mobile")
                mobile_records = ps_cursor.fetchall()

                print("Displaying rows from mobile table")
                for row in mobile_records:
                    print(row)

                ps_cursor.close()

                # Use this method to release the connection object and send back to connection pool
                postgreSQL_pool.putconn(ps_connection)
                print("Put away a PostgreSQL connection")

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)

        finally:
            # closing database connection.
            # use closeall method to close all the active connection if you want to turn of the application
            if (postgreSQL_pool):
                postgreSQL_pool.closeall
            print("PostgreSQL connection pool is closed")


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

