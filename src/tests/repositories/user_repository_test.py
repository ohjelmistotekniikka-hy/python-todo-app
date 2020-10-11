import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_kalle = User('kalle', 'kalle123')
        self.user_matti = User('matti', 'matti123')

    def test_create(self):
        user_repository.create(self.user_kalle)
        users = user_repository.find_all()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_kalle.username)

    def test_find_all(self):
        user_repository.create(self.user_kalle)
        user_repository.create(self.user_matti)
        users = user_repository.find_all()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, self.user_kalle.username)
        self.assertEqual(users[1].username, self.user_matti.username)

    def test_find_by_username(self):
        user_repository.create(self.user_kalle)

        user = user_repository.find_by_username(self.user_kalle.username)

        self.assertEqual(user.username, self.user_kalle.username)
