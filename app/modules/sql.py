"""
This module is used for storing SQL queries
"""


def create_stock_table(table: str) -> str:
    """
    create_stock_table is used to create  a table
    :param table:  table name to be created
    :return:
    """
    return f"""
    CREATE TABLE {table}(
        date_symbol VARCHAR (50) NOT NULL ,
        id SERIAL,
        date DATE NOT NULL,
        symbol VARCHAR (50)  NOT NULL,
        High INT,
        clse INT,
        Volume INT,
        Dividends INT,
        stock_splits INT,
        Open INT,
        Low INT
    );"""


def select_all_table(table: str) -> str:
    """
    select_all_table is used for returning all the table data.
    :param table:  return stock table data
    :return:
    """
    sql_query = f"SELECT * FROM {table}"
    return sql_query


def drop_table(table: str) -> str:
    """
    drop_table is used for dropping a table
    :param table: the table to drop
    :return:
    """
    sql_query = f"DROP TABLE {table};"
    return sql_query
