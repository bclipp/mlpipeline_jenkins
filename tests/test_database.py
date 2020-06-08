"""
tests for the stock module
"""
from unittest.mock import Mock

import app.modules.database as db


def test_initialize_database():
    """
    Used to test the basic functionality of get_stock with a start date
    """
    database_manager: Mock = Mock()
    db.initialize_database(database_manager,
                           "test")
    assert database_manager.calledsend_sql
