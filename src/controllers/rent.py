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


r = Rent()
current_data = date.today()
r.issue_rent(3, 42, 53, current_data, current_data+timedelta(10))
# print(r.get_all_rent())
r.delete_rent(53, 42)
r.issue_rent(3, 2, 3, current_data, current_data+timedelta(10))
r.update_rent(3, 2, current_data+timedelta(20))
