import tkinter as tk


class TodosView:
    def __init__(self, root, todos, user, handle_set_done, handle_delete, handle_create):
        self.root = root
        self.todos = todos
        self.user = user
        self.handle_set_done = handle_set_done
        self.handle_delete = handle_delete
        self.handle_create = handle_create

        self.initialize()

    def initialize(self):
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
