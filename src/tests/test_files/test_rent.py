from datetime import date, timedelta
from src.tests.database import database_function as db
from src.tests.conftest import load_rent_test_data


def test_issue_rent(load_rent_test_data):
    load_rent_test_data.issue_rent(101, 89, 11, date.today(), date.today()+timedelta(10))
    data = db.get_rent_data(101)
    assert data[0] == 101
    assert data[1] == 11
    assert data[2] == 89
    assert data[3] == date.today()
    assert data[4] == date.today()+timedelta(10)


def test_get_all_rent_data(load_rent_test_data):
    data = load_rent_test_data.get_all_rent()
    assert len(data) == 101


def test_delete_rent_data(load_rent_test_data):
    load_rent_test_data.delete_rent(11, 89)
    data = db.get_rent_data(101)
    assert data is None


def test_update_rent_data(load_rent_test_data):
    load_rent_test_data.update_rent(88, 88, date.today()+timedelta(20))
    data = db.get_rent_data_member_and_rent(88, 88)
    assert data[4] == date.today()+timedelta(20)
