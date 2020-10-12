import tkinter as tk
from gui.login_view import LoginView
from gui.todos_view import TodosView
from gui.create_user_view import CreateUserView


class GUI:
    def __init__(self, window):
        self.window = window
        self.current_view = None

    def hide_current_view(self):
        if self.current_view:
            self.current_view.destroy()

        self.current_view = None

    def show_login_view(self):
        self.hide_current_view()

        self.current_view = LoginView(
            self.window,
            self.handle_login,
            self.handle_show_create_user_view
        )

        self.current_view.pack()

    def show_todos_view(self):
        self.hide_current_view()

        self.current_view = TodosView(self.window, self.handle_logout)

        self.current_view.pack()

    def handle_login(self):
        self.show_todos_view()

    def handle_logout(self):
        self.show_login_view()

    def show_create_user_view(self):
        self.hide_current_view()

        self.current_view = CreateUserView(
            self.window,
            self.handle_create_user
        )

        self.current_view.pack()

    def handle_create_user(self):
        self.show_todos_view()

    def handle_show_create_user_view(self):
        self.show_create_user_view()

    def start(self):
        self.show_login_view()

        self.window.mainloop()


gui_window = tk.Tk()

gui_window.title('TodoApp')

gui = GUI(gui_window)
