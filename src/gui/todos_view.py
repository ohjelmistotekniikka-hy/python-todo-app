import tkinter as tk
from repositories.todo_repository import todo_repository


def handle_create_todo(todo):
    todo_repository.create(todo)


def handle_set_todo_done(todo_id, done=True):
    todo_repository.set_done(todo_id, done)


class TodosView:
    def __init__(self, root, user, handle_logout):
        self.root = root
        self.user = user
        self.handle_logout = handle_logout

        self.initialize()

    def initialize(self):
        self.todos = todo_repository.find_by_username(self.user.username)
        self.frame = tk.Frame(master=self.root)

        user_label = tk.Label(
            master=self.frame, text=f'Logged in as {self.user.username}')

        user_label.pack()

        for todo in self.todos:
            label = tk.Label(master=self.frame, text=todo.content)
            label.pack()

    def pack(self):
        self.frame.pack()

    def destroy(self):
        self.frame.destroy()
