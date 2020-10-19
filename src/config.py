import os

dirname = os.path.dirname(__file__)

TODOS_FILENAME = os.getenv('TODOS_FILENAME') or 'todos.csv'
TODOS_FILE_PATH = os.path.join(dirname, '..', 'data', TODOS_FILENAME)

DATABASE_FILENAME = os.getenv('DATABASE_FILENAME') or 'database.sqlite'
DATABASE_FILE_PATH = os.path.join(dirname, '..', 'data', DATABASE_FILENAME)
