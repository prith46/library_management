from src.configurations.config import connect

config_file_path = 'E:/Projects/library_management/src/configurations/database.ini'
conn = connect(config_file=config_file_path)
cursor = conn.cursor()


def execute_test_sql(filename):
    cursor.execute('CREATE TABLE IF NOT EXISTS books ('
                   'book_id INT,'
                   'title VARCHAR(255),'
                   'author VARCHAR(255),'
                   'year INT,'
                   'isin BIGINT,'
                   'count INT );')

    cursor.execute('CREATE TABLE IF NOT EXISTS members ('
                   'member_id INT,'
                   'name VARCHAR(255),'
                   'phone BIGINT );')

    cursor.execute('CREATE TABLE IF NOT EXISTS rent ('
                   'rent_id INT,'
                   'member_id INT,'
                   'book_id INT,'
                   'rent_date DATE,'
                   'return_date DATE );')

    cursor.execute('TRUNCATE TABLE books')
    cursor.execute('TRUNCATE TABLE members')
    cursor.execute('TRUNCATE TABLE rent')

    conn.commit()
    try:
        with open(filename, 'r') as file:
            # Process file contents
            contents = file.read()
            print(contents)
    except OSError as e:
        print(f"Error opening file: {e}")

def get_one_data(book_id):
    query = f'SELECT * FROM books WHERE book_id = {book_id};'
    cursor.execute(query)
    return cursor.fetchone()









