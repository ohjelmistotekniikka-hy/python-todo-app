from tkinter import ttk, StringVar, constants
from services.todo_service import todo_service, UsernameExists


class CreateUserView:
    def __init__(self, root, handle_create_user, handle_show_login_view):
        self.root = root
        self.handle_create_user = handle_create_user
        self.handle_show_login_view = handle_show_login_view
        self.frame = None
        self.username_entry = None
        self.password_entry = None
        self.error_variable = None
        self.error_label = None

        self.initialize()

    def create_user_handler(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if len(username) == 0 or len(password) == 0:
            self.show_error('Username and password is required')
            return

        try:
            todo_service.create_user(username, password)
            todo_service.login(username, password)
            self.handle_create_user()
        except UsernameExists:
            self.show_error(f'Username {username} already exists')

    def show_error(self, message):
        self.error_variable.set(message)
        self.error_label.grid()

    def hide_error(self):
        self.error_label.grid_remove()

    def initialize_username_field(self):
        username_label = ttk.Label(master=self.frame, text='Username')

        self.username_entry = ttk.Entry(master=self.frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self.username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def initialize_password_field(self):
        password_label = ttk.Label(master=self.frame, text='Password')

        self.password_entry = ttk.Entry(master=self.frame)

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self.password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        self.error_variable = StringVar(self.frame)

        self.error_label = ttk.Label(
            master=self.frame,
            textvariable=self.error_variable,
            foreground='red'
        )

        self.error_label.grid(padx=5, pady=5)

        self.initialize_username_field()
        self.initialize_password_field()

        create_user_button = ttk.Button(
            master=self.frame,
            text='Create',
            command=self.create_user_handler
        )

        login_button = ttk.Button(
            master=self.frame,
            text='Login',
            command=self.handle_show_login_view
        )

        self.frame.grid_columnconfigure(0, weight=1)

        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)
        login_button.grid(padx=5, pady=5, sticky=constants.EW)

        self.hide_error()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()
