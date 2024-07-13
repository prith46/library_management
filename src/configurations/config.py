from configparser import ConfigParser
import psycopg2


def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} is not found in the {filename} file')
    return db


def connect():
    connection = None
    try:
        params = config()
        connection = psycopg2.connect(**params)
        conn = connection.cursor()
        conn.execute('SELECT version()')
        db_version = conn.fetchone()
        print(db_version)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == "__main__":
    connect()
