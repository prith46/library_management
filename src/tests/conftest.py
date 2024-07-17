import pytest
from src.controllers.book import Book
from src.tests.database import database_function as db


@pytest.fixture(scope="module")
def load_test_data():
    bk = Book()
    db.execute_test_sql('E:/Projects/library_management/src/tests/database/book_database.sql')
    yield bk
