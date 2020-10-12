import tkinter as tk
from gui.login_view import LoginView
from gui.todos_view import TodosView


class Gui:
    def __init__(self, window):
        self.window = window
        self.login_view = None
        self.todos_view = None
        self.user = None

    def show_login_view(self):
        self.login_view = LoginView(self.window, self.handle_login)
        self.login_view.pack()

    def hide_login_view(self):
        self.login_view.destroy()
        self.login_view = None

    def show_todos_view(self):
        self.todos_view = TodosView(
            self.window,
            self.user,
            self.handle_logout
        )

        self.todos_view.pack()

    def hide_todos_view(self):
        self.todos_view.destroy()
        self.todos_view = None

    def handle_login(self, user):
        self.user = user

        self.hide_login_view()
        self.show_todos_view()

        return True

    def handle_logout(self):
        self.user = None

        self.hide_todos_view()
        self.show_login_view()

    def handle_create_user(self, user):
        self.user = user

    def start(self):
        self.show_login_view()

        self.window.mainloop()


gui = Gui(tk.Tk())
