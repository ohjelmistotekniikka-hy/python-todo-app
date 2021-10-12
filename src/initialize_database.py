from database_connection import get_database_connection


def drop_tables(connection):
    """Poistaa tietokantataulut.

    Args:
        connection: Tietokantayhteyden Connection-olio
    """

    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')

    connection.commit()


def create_tables(connection):
    """Luo tietokantataulut.

    Args:
        connection: Tietokantayhteyden Connection-olio
    """

    cursor = connection.cursor()

    cursor.execute('''
        create table users (
            username text primary key,
            password text
        );
    ''')

    connection.commit()


def initialize_database():
    """Alustaa tietokantataulut.
    """

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == '__main__':
    initialize_database()
