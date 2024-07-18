from src.tests.database import database_function as db
from src.tests.conftest import load_member_test_data


def test_add_member(load_member_test_data):
    load_member_test_data.add_member(101, 'Prithiviraj M', 4708789331)
    data = db.get_one_member_data(101)
    assert data[0] == 101
    assert data[1] == 'Prithiviraj M'
    assert data[2] == 4708789331


def test_get_all_members(load_member_test_data):
    data = load_member_test_data.get_all_members()
    assert len(data) == 101


def test_delete_member(load_member_test_data):
    load_member_test_data.delete_member('Prithiviraj M')
    data = db.get_one_member_data(101)
    assert data is None
