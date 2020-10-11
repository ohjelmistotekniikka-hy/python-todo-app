import unittest
from repositories.todo_repository import todo_repository
from repositories.user_repository import user_repository
from entities.todo import Todo
from entities.user import User


class TestTodoRepository(unittest.TestCase):
    def setUp(self):
        todo_repository.delete_all()
        user_repository.delete_all()

        self.todo_a = Todo('testing a')
        self.todo_b = Todo('testing b')
        self.user_kalle = User('kalle', 'kalle123')
        self.user_matti = User('matti', 'matti123')

    def test_create(self):
        todo_repository.create(self.todo_a)
        todos = todo_repository.find_all()

        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0].content, self.todo_a.content)

    def test_find_all(self):
        todo_repository.create(self.todo_a)
        todo_repository.create(self.todo_b)
        todos = todo_repository.find_all()

        self.assertEqual(len(todos), 2)
        self.assertEqual(todos[0].content, self.todo_a.content)
        self.assertEqual(todos[1].content, self.todo_b.content)

    def test_set_done(self):
        created_todo = todo_repository.create(self.todo_a)
        todos = todo_repository.find_all()

        self.assertEqual(todos[0].done, False)

        todo_repository.set_done(created_todo.id)

        todos = todo_repository.find_all()

        self.assertEqual(todos[0].done, True)

    def test_find_by_username(self):
        kalle = user_repository.create(self.user_kalle)
        matti = user_repository.create(self.user_matti)

        todo_repository.create(Todo(content='testing a', user=kalle))
        todo_repository.create(Todo(content='testing b', user=matti))

        kalle_todos = todo_repository.find_by_username(
            self.user_kalle.username)

        self.assertEqual(len(kalle_todos), 1)
        self.assertEqual(kalle_todos[0].content, 'testing a')

        matti_todos = todo_repository.find_by_username(
            self.user_matti.username)

        self.assertEqual(len(matti_todos), 1)
        self.assertEqual(matti_todos[0].content, 'testing b')

    def test_delete(self):
        created_todo = todo_repository.create(self.todo_a)
        todos = todo_repository.find_all()

        self.assertEqual(len(todos), 1)

        todo_repository.delete(created_todo.id)

        todos = todo_repository.find_all()

        self.assertEqual(len(todos), 0)
