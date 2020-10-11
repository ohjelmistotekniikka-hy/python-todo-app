import sqlite3
from config import DATABASE_FILE_PATH


def get_database_connection():
    connection = sqlite3.connect(DATABASE_FILE_PATH)

    connection.row_factory = sqlite3.Row

    return connection
