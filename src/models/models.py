from src.configurations.config import connect
import psycopg2

# Establish a connection
conn = connect()

# Check if the connection was successful
if conn is not None:
    try:
        # Create a cursor object
        cursor = conn.cursor()

        # Execute a query
        cursor.execute('SELECT version()')

        # Fetch and print the result
        db_version = cursor.fetchone()
        print(f"PostgreSQL version: {db_version[0]}")

        # Close the cursor
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        # Close the connection
        conn.close()
else:
    print("Failed to connect to the database. Please check your configuration.")
