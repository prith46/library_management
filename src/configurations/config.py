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
        raise Exception(f"Section {section} is not found in the {filename} file")
    return db


def connect(config_file='database.ini'):
    connection = None
    try:
        params = config(config_file)
        connection = psycopg2.connect(**params)
        # cursor = connection.cursor()
        return connection
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        if connection is not None:
            connection.close()
        return None


if __name__ == "__main__":
    connect()
