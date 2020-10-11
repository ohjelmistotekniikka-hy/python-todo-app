import tkinter as tk
from repositories.user_repository import user_repository
from repositories.todo_repository import todo_repository
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
        todos = todo_repository.find_by_username(self.user.username)
        self.todos_view = TodosView(self.window, todos, self.user)
        self.todos_view.pack()

    def hide_todos_view(self):
        self.todos_view.destroy()
        self.todos_view = None

    def handle_login(self, username, password):
        user = user_repository.find_by_username(username)

        if not user or user.password != password:
            return False

        self.user = user

        self.hide_login_view()
        self.show_todos_view()

        return True

    def handle_create_todo(self, todo):
        todo_repository.create(todo)
    
    def handle_delete_todo(self, todo_id):
        todo_repository.delete(todo_id)

    def handle_set_todo_done(self, todo_id, done = True):
        todo_repository.set_done(todo_id, done)

    def start(self):
        self.show_login_view()

        self.window.mainloop()


gui = Gui(tk.Tk())
