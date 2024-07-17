from src.models.models import Library
from datetime import date, timedelta


class Rent:
    def __init__(self):
        self.rent = Library()

    def issue_rent(self, rent_id, book_id, member_id, rent_date, return_data):
        query = (f'INSERT INTO rent (rent_id, member_id, book_id, rent_date, return_date) '
                 f'VALUES ({rent_id}, {member_id}, {book_id}, \'{rent_date}\', \'{return_data}\');')
        self.rent.issue_rent_db(query)

    def get_all_rent(self):
        return self.rent.get_all_rent_db()

    def delete_rent(self, member_id, book_id):
        self.rent.delete_rent_db(member_id, book_id)

    def update_rent(self, member_id, book_id, return_date):
        self.rent.update_rent_db(member_id, book_id, return_date)
