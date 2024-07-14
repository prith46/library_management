from src.configurations.config import connect

config_file_path = 'E:/Projects/library_management/src/configurations/database.ini'
conn = connect(config_file=config_file_path)
cursor = conn.cursor()


class Library:
    def __init__(self):
        cursor.execute('CREATE TABLE IF NOT EXISTS books ('
                     'book_id INT,'
                     'title VARCHAR(255),'
                     'author VARCHAR(255),'
                     'year INT,'
                     'isin INT,'
                     'count INT );')
        cursor.execute('CREATE TABLE IF NOT EXISTS members ('
                       'member_id INT,'
                       'name VARCHAR(255),'
                       'phone INT );')
        conn.commit()

    def add_book_db(self, query):
        cursor.execute(query)
        conn.commit()

    def get_all_books_db(self):
        cursor.execute('SELECT title FROM books')
        all_books = cursor.fetchall()
        return all_books

    def delete_book_db(self, title):
        query = f'SELECT * FROM books WHERE title = \'{title}\';'
        cursor.execute(query)
        flag = cursor.fetchone()
        if flag:
            query = f'DELETE FROM BOOKS WHERE title = \'{title}\';'
            cursor.execute(query)
            conn.commit()
            print("Book is deleted successfully")
        else:
            print("Book is not available")

    def add_member_db(self, query):
        cursor.execute(query)
        conn.commit()

    def get_all_members_db(self):
        cursor.execute('SELECT name FROM members')
        members = cursor.fetchall()
        return members

    def delete_members_db(self, name):
        query = f'SELECT * FROM members WHERE name = \'{name}\';'
        if query:
            query = f'DELETE FROM members WHERE name = \'{name}\';'
            conn.commit()
            print("Member is deleted successfully")
        else:
            print("Member is not found")







