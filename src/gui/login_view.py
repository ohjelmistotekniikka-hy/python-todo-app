import tkinter as tk
from repositories.user_repository import user_repository


class LoginView:
    def __init__(self, root, handle_login):
        self.root = root
        self.handle_login = handle_login

        self.initialize()

    def login_handler(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user = user_repository.find_by_username(username)

        if not user or user.password != password:
            self.show_error('Invalid username or password')
        else:
            self.handle_login(user)

    def show_error(self, message):
        self.error_message.set(message)
        self.error_label.grid()

    def hide_error(self):
        self.error_label.grid_remove()

    def initialize_username_field(self):
        username_label = tk.Label(master=self.frame, text='Username')

        self.username_entry = tk.Entry(master=self.frame)

        username_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.username_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)

    def initialize_password_field(self):
        password_label = tk.Label(master=self.frame, text='Password')

        self.password_entry = tk.Entry(master=self.frame)

        password_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.password_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)

    def initialize(self):
        self.frame = tk.Frame(master=self.root)

        self.error_message = tk.StringVar()

        self.error_label = tk.Label(
            master=self.frame,
            textvariable=self.error_message,
            fg='red'
        )

        self.error_label.grid(column=1, columnspan=2, padx=5, pady=5)

        self.initialize_username_field()
        self.initialize_password_field()

        login_button = tk.Button(
            master=self.frame,
            text='Login',
            command=self.login_handler
        )

        self.frame.grid_columnconfigure(0, weight=0)
        self.frame.grid_columnconfigure(1, weight=1)

        login_button.grid(column=1, padx=5, pady=5, sticky=tk.EW)

        self.hide_error()

    def pack(self):
        self.frame.pack(fill=tk.X)

    def destroy(self):
        self.frame.destroy()
