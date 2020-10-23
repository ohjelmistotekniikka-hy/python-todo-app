from tkinter import ttk, constants
from services.todo_service import todo_service


class TodoListView:
    def __init__(self, root, todos, handle_set_todo_done):
        self.root = root
        self.todos = todos
        self.handle_set_todo_done = handle_set_todo_done
        self.frame = None

        self.initialize()

    def initialize_todo_item(self, todo):
        item_frame = ttk.Frame(master=self.frame)
        label = ttk.Label(master=item_frame, text=todo.content)

        set_done_button = ttk.Button(
            master=item_frame,
            text='Done',
            command=lambda: self.handle_set_todo_done(todo.id)
        )

        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        set_done_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        for todo in self.todos:
            self.initialize_todo_item(todo)

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()


class TodosView:
    def __init__(self, root, handle_logout):
        self.root = root
        self.handle_logout = handle_logout
        self.user = todo_service.get_current_user()
        self.frame = None
        self.create_todo_entry = None
        self.todo_list_frame = None
        self.todo_list_view = None

        self.initialize()

    def logout_handler(self):
        todo_service.logout()
        self.handle_logout()

    def handle_set_todo_done(self, todo_id):
        todo_service.set_todo_done(todo_id)
        self.initialize_todo_list()

    def initialize_todo_list(self):
        if self.todo_list_view:
            self.todo_list_view.destroy()

        todos = todo_service.get_undone_todos()

        self.todo_list_view = TodoListView(
            self.todo_list_frame,
            todos,
            self.handle_set_todo_done
        )

        self.todo_list_view.pack()

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

    def handle_create_todo(self):
        todo_content = self.create_todo_entry.get()

        if todo_content:
            todo_service.create_todo(todo_content)
            self.initialize_todo_list()
            self.create_todo_entry.delete(0, constants.END)

    def initialize_footer(self):
        self.create_todo_entry = ttk.Entry(master=self.frame)

        create_todo_button = ttk.Button(
            master=self.frame,
            text='Create',
            command=self.handle_create_todo
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
        self.todo_list_frame = ttk.Frame(master=self.frame)

        self.initialize_header()
        self.initialize_todo_list()
        self.initialize_footer()

        self.todo_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self.frame.grid_columnconfigure(0, weight=1, minsize=400)
        self.frame.grid_columnconfigure(1, weight=0)

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()
