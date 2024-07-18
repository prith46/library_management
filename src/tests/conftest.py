import pytest
from src.controllers.book import Book
from src.tests.database import database_function as db
from src.controllers.members import Members
from src.controllers.rent import Rent


@pytest.fixture(scope="module")
def load_book_test_data():
    bk = Book()
    db.truncate()
    db.execute_test_sql('E:/Projects/library_management/src/tests/database/book_database.sql')
    yield bk


@pytest.fixture(scope="module")
def load_member_test_data():
    mm = Members()
    db.truncate()
    db.execute_test_sql('E:/Projects/library_management/src/tests/database/member_database.sql')
    yield mm


@pytest.fixture(scope="module")
def load_rent_test_data():
    rt = Rent()
    db.truncate()
    db.execute_test_sql('E:/Projects/library_management/src/tests/database/book_database.sql')
    db.execute_test_sql('E:/Projects/library_management/src/tests/database/member_database.sql')
    db.execute_test_sql('E:/Projects/library_management/src/tests/database/rent_database.sql')
    yield rt
