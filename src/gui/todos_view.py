import tkinter as tk
from entities.todo import Todo
from repositories.todo_repository import todo_repository


def handle_create_todo(todo):
    todo_repository.create(todo)


def handle_set_todo_done(root, todo):
    todo_repository.set_done(todo.id, True)
    root.destroy()


class TodosView:
    def __init__(self, root, user, handle_logout):
        self.root = root
        self.user = user
        self.handle_logout = handle_logout
        self.todos = self.get_not_done_todos()
        self.frame = None
        self.todo_list_frame = None
        self.create_todo_entry = None

        self.initialize()

    def logout_handler(self):
        self.handle_logout()

    def initialize_todo_item(self, todo):
        todo_item_frame = tk.Frame(master=self.todo_list_frame)

        label = tk.Label(master=todo_item_frame, text=todo.content)

        set_done_button = tk.Button(
            master=todo_item_frame,
            text='Done',
            command=lambda: handle_set_todo_done(todo_item_frame, todo)
        )

        label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        set_done_button.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)

        todo_item_frame.grid_columnconfigure(0, weight=1)

        todo_item_frame.pack(fill=tk.X)

    def initialize_todo_list(self):
        self.todo_list_frame = tk.Frame(master=self.frame)

        for todo in self.todos:
            self.initialize_todo_item(todo)

        self.todo_list_frame.grid(row=1, column=0, columnspan=2, sticky=tk.EW)

    def initialize_header(self):
        user_label = tk.Label(
            master=self.frame,
            text=f'Logged in as {self.user.username}'
        )

        logout_button = tk.Button(
            master=self.frame,
            text='Logout',
            command=self.logout_handler
        )

        user_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        logout_button.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)

    def create_todo_handler(self):
        todo_content = self.create_todo_entry.get()
        todo = Todo(content=todo_content, user=self.user)

        if todo_content:
            handle_create_todo(todo)
            self.initialize_todo_item(todo)
            self.create_todo_entry.delete(0, tk.END)

    def initialize_footer(self):
        self.create_todo_entry = tk.Entry(master=self.frame)

        create_todo_button = tk.Button(
            master=self.frame,
            text='Create',
            command=self.create_todo_handler
        )

        self.create_todo_entry.grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky=tk.EW
        )

        create_todo_button.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)

    def get_not_done_todos(self):
        todos = todo_repository.find_by_username(self.user.username)
        done_todos = filter(lambda todo: not todo.done, todos)

        return list(done_todos)

    def initialize(self):
        self.frame = tk.Frame(master=self.root)

        self.initialize_header()
        self.initialize_todo_list()
        self.initialize_footer()

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=0)

    def pack(self):
        self.frame.pack(fill=tk.X)

    def destroy(self):
        self.frame.destroy()
