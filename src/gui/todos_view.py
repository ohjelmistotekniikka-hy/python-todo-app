from tkinter import ttk, constants
from services.todo_service import todo_service


def handle_create_todo(content):
    return todo_service.create_todo(content)


def handle_set_todo_done(root, todo_id):
    todo_service.set_todo_done(todo_id)
    root.destroy()


class TodosView:
    def __init__(self, root, handle_logout):
        self.root = root
        self.handle_logout = handle_logout
        self.user = todo_service.get_current_user()
        self.todos = todo_service.get_undone_todos()
        self.frame = None
        self.todo_list_frame = None
        self.create_todo_entry = None

        self.initialize()

    def logout_handler(self):
        todo_service.logout()
        self.handle_logout()

    def initialize_todo_item(self, todo):
        frame = ttk.Frame(master=self.todo_list_frame)

        label = ttk.Label(master=frame, text=todo.content)

        set_done_button = ttk.Button(
            master=frame,
            text='Done',
            command=lambda: handle_set_todo_done(frame, todo.id)
        )

        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        set_done_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        frame.grid_columnconfigure(0, weight=1)

        frame.pack(fill=constants.X)

    def initialize_todo_list(self):
        self.todo_list_frame = ttk.Frame(master=self.frame)

        for todo in self.todos:
            self.initialize_todo_item(todo)

        self.todo_list_frame.grid(
            row=1, column=0, columnspan=2, sticky=constants.EW)

    def initialize_header(self):
        user_label = ttk.Label(
            master=self.frame,
            text=f'Logged in as {self.user.username}'
        )

        logout_button = ttk.Button(
            master=self.frame,
            text='Logout',
            command=self.logout_handler
        )

        user_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        logout_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def create_todo_handler(self):
        todo_content = self.create_todo_entry.get()

        if todo_content:
            todo = handle_create_todo(todo_content)
            self.initialize_todo_item(todo)
            self.create_todo_entry.delete(0, constants.END)

    def initialize_footer(self):
        self.create_todo_entry = ttk.Entry(master=self.frame)

        create_todo_button = ttk.Button(
            master=self.frame,
            text='Create',
            command=self.create_todo_handler
        )

        self.create_todo_entry.grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        create_todo_button.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        self.initialize_header()
        self.initialize_todo_list()
        self.initialize_footer()

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=0)

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()
