import tkinter as tk
from repositories.user_repository import user_repository

class LoginView:
    def __init__(self, root, handle_login):
        self.root = root
        self.handle_login = handle_login

        self.initialize()

    def login_handler(self, _):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user = user_repository.find_by_username(username)

        if not user or user.password != password:
            print('Invalid credetinals')
        else:
            self.handle_login(user)

    def initialize(self):
        self.frame = tk.Frame(master=self.root)

        username_label = tk.Label(master=self.frame, text='Username')

        self.username_entry = tk.Entry(master=self.frame)

        password_label = tk.Label(master=self.frame, text='Password')

        self.password_entry = tk.Entry(master=self.frame)

        login_button = tk.Button(master=self.frame, text='Login')
        login_button.bind('<Button-1>', self.login_handler)

        username_label.pack()
        self.username_entry.pack()

        password_label.pack()
        self.password_entry.pack()

        login_button.pack()

    def pack(self):
        self.frame.pack()

    def destroy(self):
        self.frame.destroy()
