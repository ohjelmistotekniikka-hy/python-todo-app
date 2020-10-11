from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
    drop table if exists users;
  ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
    create table users (
      username text primary key,
      password text
    );
  ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

    connection.close()


# This allows us to call the initialize_database function using command line
if __name__ == '__main__':
    initialize_database()
