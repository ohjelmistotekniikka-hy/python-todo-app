import unittest
from entities.todo import Todo
from entities.user import User
from services.todo_service import (
    TodoService,
    InvalidCredentialsError,
    UsernameExistsError
)


class FakeTodoRepository:
    def __init__(self, todos=None):
        self.todos = todos or []

    def find_all(self):
        return self.todos

    def find_by_username(self, username):
        user_todos = filter(
            lambda todo: todo.user and todo.user.username == username,
            self.todos
        )

        return list(user_todos)

    def create(self, todo):
        self.todos.append(todo)

        return todo

    def set_done(self, todo_id, done=True):
        for todo in self.todos:
            if todo.id == todo_id:
                todo.done = done
                break

    def delete(self, todo_id):
        todos_without_id = filter(lambda todo: todo.id != todo_id, self.todos)

        self.todos = list(todos_without_id)

    def delete_all(self):
        self.todos = []


class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []

    def find_all(self):
        return self.users

    def find_by_username(self, username):
        matching_users = filter(
            lambda user: user.username == username,
            self.users
        )

        matching_users_list = list(matching_users)

        return matching_users_list[0] if len(matching_users_list) > 0 else None

    def create(self, user):
        self.users.append(user)

        return user

    def delete_all(self):
        self.users = []


class TestTodoService(unittest.TestCase):
    def setUp(self):
        self.todo_service = TodoService(
            FakeTodoRepository(),
            FakeUserRepository()
        )

        self.todo_a = Todo('testing a')
        self.todo_b = Todo('testing b')
        self.user_kalle = User('kalle', 'kalle123')

    def login_user(self, user):
        self.todo_service.create_user(user.username, user.password)

    def test_create_todo(self):
        self.login_user(self.user_kalle)

        self.todo_service.create_todo('testing')
        todos = self.todo_service.get_undone_todos()

        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0].content, 'testing')
        self.assertEqual(todos[0].user.username, self.user_kalle.username)

    def test_get_undone_todos(self):
        self.login_user(self.user_kalle)

        self.todo_service.create_todo(self.todo_a.content)

        created_todo_b = self.todo_service.create_todo(self.todo_b.content)

        self.todo_service.set_todo_done(created_todo_b.id)

        undone_todos = self.todo_service.get_undone_todos()

        self.assertEqual(len(undone_todos), 1)
        self.assertEqual(undone_todos[0].content, self.todo_a.content)

    def test_set_todo_done(self):
        self.login_user(self.user_kalle)

        self.todo_service.create_todo('testing')

        undone_todos = self.todo_service.get_undone_todos()

        self.assertEqual(len(undone_todos), 1)

        self.todo_service.set_todo_done(undone_todos[0].id)

        undone_todos = self.todo_service.get_undone_todos()

        self.assertEqual(len(undone_todos), 0)

    def test_login_with_valid_username_and_password(self):
        self.todo_service.create_user(
            self.user_kalle.username,
            self.user_kalle.password
        )

        user = self.todo_service.login(
            self.user_kalle.username,
            self.user_kalle.password
        )

        self.assertEqual(user.username, self.user_kalle.username)

    def test_login_with_invalid_username_and_password(self):
        self.assertRaises(
            InvalidCredentialsError,
            lambda: self.todo_service.login('testing', 'invalid')
        )

    def test_get_current_user(self):
        self.login_user(self.user_kalle)

        current_user = self.todo_service.get_current_user()

        self.assertEqual(current_user.username, self.user_kalle.username)

    def test_create_user_with_non_existing_username(self):
        username = self.user_kalle.username
        password = self.user_kalle.password

        self.todo_service.create_user(username, password)

        users = self.todo_service.get_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, username)

    def test_create_user_with_existing_username(self):
        username = self.user_kalle.username

        self.todo_service.create_user(username, 'something')

        self.assertRaises(
            UsernameExistsError,
            lambda: self.todo_service.create_user(username, 'random')
        )
