from pathlib import Path
from entities.todo import Todo
from repositories.user_repository import user_repository
from config import TODOS_FILE_PATH


class TodoRepository:
    def __init__(self, file_path):
        self.file_path = file_path

    def ensure_file_exists(self):
        # The touch method will create the file if it doesn't exist
        Path(self.file_path).touch()

    def read(self):
        todos = []

        self.ensure_file_exists()

        with open(self.file_path) as file:
            for row in file:
                row = row.replace('\n', '')
                parts = row.split(';')

                todo_id = parts[0]
                content = parts[1]
                done = parts[2] == '1'
                username = parts[3]

                user = user_repository.find_by_username(
                    username) if username else None

                todos.append(
                    Todo(content, done, user, todo_id)
                )

        return todos

    def write(self, todos):
        self.ensure_file_exists()

        with open(self.file_path, 'w') as file:
            for todo in todos:
                done_string = '1' if todo.done else '0'
                username = todo.user.username if todo.user else ''

                row = f'{todo.id};{todo.content};{done_string};{username}'

                file.write(row+'\n')

    def find_all(self):
        return self.read()

    def find_by_username(self, username):
        todos = self.find_all()

        user_todos = filter(
            lambda todo: todo.user and todo.user.username == username, todos)

        return list(user_todos)

    def create(self, todo):
        todos = self.find_all()

        todos.append(todo)

        self.write(todos)

        return todo

    def set_done(self, todo_id, done=True):
        todos = self.find_all()

        for todo in todos:
            if todo.id == todo_id:
                todo.done = done
                break

        self.write(todos)

    def delete(self, todo_id):
        todos = self.find_all()

        todos_without_id = filter(lambda todo: todo.id != todo_id, todos)

        self.write(todos_without_id)

    def delete_all(self):
        self.write([])


todo_repository = TodoRepository(TODOS_FILE_PATH)
