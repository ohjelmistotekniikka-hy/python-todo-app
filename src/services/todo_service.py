from entities.todo import Todo
from entities.user import User

from repositories.todo_repository import (
    todo_repository as default_todo_repository
)

from repositories.user_repository import (
    user_repository as default_user_repository
)


class InvalidCredentials(Exception):
    pass


class UsernameExists(Exception):
    pass


class TodoService:
    def __init__(
        self,
        todo_repository=default_todo_repository,
        user_repository=default_user_repository
    ):
        self.user = None
        self.todo_repository = todo_repository
        self.user_repository = user_repository

    def create_todo(self, content):
        todo = Todo(content=content, user=self.user)

        return self.todo_repository.create(todo)

    def get_undone_todos(self):
        if not self.user:
            return []

        todos = self.todo_repository.find_by_username(self.user.username)
        undone_todos = filter(lambda todo: not todo.done, todos)

        return list(undone_todos)

    def set_todo_done(self, todo_id):
        self.todo_repository.set_done(todo_id)

    def login(self, username, password):
        user = self.user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentials('Invalid username or password')

        self.user = user

        return user

    def get_current_user(self):
        return self.user

    def get_users(self):
        return self.user_repository.find_all()

    def logout(self):
        self.user = None

    def create_user(self, username, password):
        existing_user = self.user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExists(f'Username {username} already exists')

        return self.user_repository.create(User(username, password))


todo_service = TodoService()
