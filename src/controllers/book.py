from src.models.models import Library


class Book:
    def __init__(self):
        self.books = Library()

    def add_book(self, book_id, title, author, year, isin, count):
        query = (f"INSERT INTO books(book_id, title, author, year, isin, count) "
                 f"VALUES ({book_id}, \'{title}','{author}',{year},{isin},{count});")
        self.books.add_book_db(query)

    def get_all_books(self):
        return self.books.get_all_books_db()

    def delete_book(self, title):
        self.books.delete_book_db(title)


book = Book()
book.add_book(11, 'The Alchemist', 'Paulo', 1997, 4834, 7)
print(book.get_all_books())
book.delete_book('The Alchemist')
