from tkinter import ttk, StringVar, constants
from services.todo_service import todo_service


class CreateUserView:
    def __init__(self, root, handle_create_user):
        self.root = root
        self.handle_create_user = handle_create_user
        self.frame = None
        self.username_entry = None
        self.password_entry = None
        self.error_variable = None
        self.error_label = None

        self.initialize()

    def login_handler(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        created_user = todo_service.create_user(username, password)

        if created_user:
            self.handle_create_user()
        else:
            self.show_error(f'Username "{username}" already exists')

    def show_error(self, message):
        self.error_variable.set(message)
        self.error_label.grid()

    def hide_error(self):
        self.error_label.grid_remove()

    def initialize_username_field(self):
        username_label = ttk.Label(master=self.frame, text='Username')

        self.username_entry = ttk.Entry(master=self.frame)

        username_label.grid(row=1, column=0, padx=5,
                            pady=5, sticky=constants.W)
        self.username_entry.grid(
            row=1, column=1, padx=5, pady=5, sticky=constants.EW)

    def initialize_password_field(self):
        password_label = ttk.Label(master=self.frame, text='Password')

        self.password_entry = ttk.Entry(master=self.frame)

        password_label.grid(row=2, column=0, padx=5,
                            pady=5, sticky=constants.W)
        self.password_entry.grid(
            row=2, column=1, padx=5, pady=5, sticky=constants.EW)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        self.error_variable = StringVar(self.frame)

        self.error_label = ttk.Label(
            master=self.frame,
            textvariable=self.error_variable,
            foreground='red'
        )

        self.error_label.grid(column=1, columnspan=2, padx=5, pady=5)

        self.initialize_username_field()
        self.initialize_password_field()

        login_button = ttk.Button(
            master=self.frame,
            text='Create',
            command=self.login_handler
        )

        self.frame.grid_columnconfigure(0, weight=0)
        self.frame.grid_columnconfigure(1, weight=1)

        login_button.grid(column=1, padx=5, pady=5, sticky=constants.EW)

        self.hide_error()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()
