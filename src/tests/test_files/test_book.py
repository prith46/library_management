from src.tests.database import database_function as db
from src.tests.conftest import load_book_test_data


def test_add_book(load_book_test_data):
    load_book_test_data.add_book(101, 'The Mindset', 'Thomas', 2012, 7728545662, 12)
    data = db.get_one_data(101)
    assert data[0] == 101
    assert data[1] == 'The Mindset'


def test_get_all_books(load_book_test_data):
    data = load_book_test_data.get_all_books()
    assert len(data) == 101


def test_delete_book(load_book_test_data):
    load_book_test_data.delete_book('The Mindset')
    data = db.get_one_data(101)
    assert data is None

