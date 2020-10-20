import unittest
from repositories.todo_repository import todo_repository
from repositories.user_repository import user_repository
from entities.todo import Todo
from entities.user import User
from services.todo_service import (
    todo_service,
    InvalidCredentials,
    UsernameExists
)


class TestTodoService(unittest.TestCase):
    def setUp(self):
        todo_service.logout()
        todo_repository.delete_all()
        user_repository.delete_all()

        self.todo_a = Todo('testing a')
        self.todo_b = Todo('testing b')
        self.todo_c = Todo('testing c')
        self.user_kalle = User('kalle', 'kalle123')
        self.user_matti = User('matti', 'matti123')

    def login_user(self, user):
        todo_service.create_user(user.username, user.password)
        todo_service.login(user.username, user.password)

    def test_create_todo(self):
        self.login_user(self.user_kalle)

        todo_service.create_todo('testing')
        todos = todo_repository.find_all()

        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0].content, 'testing')
        self.assertEqual(todos[0].user.username, self.user_kalle.username)

    def test_get_undone_todos(self):
        self.login_user(self.user_kalle)

        self.todo_a.user = self.user_kalle
        self.todo_b.user = self.user_kalle
        self.todo_b.done = True
        self.todo_c.user = self.user_matti

        todo_repository.create(self.todo_a)
        todo_repository.create(self.todo_b)
        todo_repository.create(self.todo_b)

        undone_todos = todo_service.get_undone_todos()

        self.assertEqual(len(undone_todos), 1)
        self.assertEqual(undone_todos[0].content, self.todo_a.content)

    def test_set_todo_done(self):
        self.login_user(self.user_kalle)

        todo_service.create_todo('testing')

        undone_todos = todo_service.get_undone_todos()

        self.assertEqual(len(undone_todos), 1)

        todo_service.set_todo_done(undone_todos[0].id)

        undone_todos = todo_service.get_undone_todos()

        self.assertEqual(len(undone_todos), 0)

    def test_login_with_valid_username_and_password(self):
        self.login_user(self.user_kalle)

    def test_login_with_invalid_username_and_password(self):
        self.assertRaises(InvalidCredentials,
                          lambda: todo_service.login('testing', 'invalid'))

    def test_get_current_user(self):
        self.login_user(self.user_kalle)

        self.assertEqual(todo_service.get_current_user(
        ).username, self.user_kalle.username)

    def test_create_user_with_non_existing_username(self):
        username = self.user_kalle.username
        password = self.user_kalle.password

        todo_service.create_user(username, password)

        users = user_repository.find_all()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, username)

    def test_create_user_with_existing_username(self):
        username = self.user_kalle.username

        todo_service.create_user(username, 'something')

        self.assertRaises(UsernameExists,
                          lambda: todo_service.create_user(username, 'random'))
