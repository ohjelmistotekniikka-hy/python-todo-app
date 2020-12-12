from tkinter import ttk, constants
from services.todo_service import todo_service


class TodoListView:
    def __init__(self, root, todos, handle_set_todo_done):
        self._root = root
        self._todos = todos
        self._handle_set_dodo_done = handle_set_todo_done
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_todo_item(self, todo):
        item_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=item_frame, text=todo.content)

        set_done_button = ttk.Button(
            master=item_frame,
            text='Done',
            command=lambda: self._handle_set_dodo_done(todo.id)
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

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for todo in self._todos:
            self._initialize_todo_item(todo)


class TodosView:
    def __init__(self, root, handle_logout):
        self._root = root
        self._handle_logout = handle_logout
        self._user = todo_service.get_current_user()
        self._frame = None
        self._create_todo_entry = None
        self._todo_list_frame = None
        self._todo_list_view = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        todo_service.logout()
        self._handle_logout()

    def _handle_set_todo_done(self, todo_id):
        todo_service.set_todo_done(todo_id)
        self._initialize_todo_list()

    def _initialize_todo_list(self):
        if self._todo_list_view:
            self._todo_list_view.destroy()

        todos = todo_service.get_undone_todos()

        self._todo_list_view = TodoListView(
            self._todo_list_frame,
            todos,
            self._handle_set_todo_done
        )

        self._todo_list_view.pack()

    def _initialize_header(self):
        user_label = ttk.Label(
            master=self._frame,
            text=f'Logged in as {self._user.username}'
        )

        logout_button = ttk.Button(
            master=self._frame,
            text='Logout',
            command=self._logout_handler
        )

        user_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        logout_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _handle_create_todo(self):
        todo_content = self._create_todo_entry.get()

        if todo_content:
            todo_service.create_todo(todo_content)
            self._initialize_todo_list()
            self._create_todo_entry.delete(0, constants.END)

    def _initialize_footer(self):
        self._create_todo_entry = ttk.Entry(master=self._frame)

        create_todo_button = ttk.Button(
            master=self._frame,
            text='Create',
            command=self._handle_create_todo
        )

        self._create_todo_entry.grid(
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

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._todo_list_frame = ttk.Frame(master=self._frame)

        self._initialize_header()
        self._initialize_todo_list()
        self._initialize_footer()

        self._todo_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)
