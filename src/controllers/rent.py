from src.models.models import Library


class Rent:
    def __init__(self):
        self.rent = Library()

    def issue_rent(self, rent_id, book_id, member_id, rent_date, return_data):
        data = self.rent.get_book(book_id)
        if data[0] > 0:
            query = (f'INSERT INTO rent (rent_id, member_id, book_id, rent_date, return_date) '
                     f'VALUES ({rent_id}, {member_id}, {book_id}, \'{rent_date}\', \'{return_data}\');')
            self.rent.issue_rent_db(query)
            self.rent.reduce_book_count(book_id)
        else:
            print('Book is not available')

    def get_all_rent(self):
        return self.rent.get_all_rent_db()

    def delete_rent(self, member_id, book_id):
        self.rent.delete_rent_db(member_id, book_id)

    def update_rent(self, member_id, book_id, return_date):
        self.rent.update_rent_db(member_id, book_id, return_date)
