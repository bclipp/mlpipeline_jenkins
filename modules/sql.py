"""
reusable SQL statements

"""

# https://www.psycopg.org/docs/usage.html


def create_stock_table() -> str:
    """
    will create the stock table
    :return:
    """
    return """
    CREATE TABLE stock(
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
    will create the stock table
    :return: a dict of sql and data
    """
    sql = f"SELECT * FROM {table}"
    return sql
