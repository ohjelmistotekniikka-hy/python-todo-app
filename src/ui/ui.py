from ui.login_view import LoginView
from ui.todos_view import TodosView
from ui.create_user_view import CreateUserView


class UI:
    def __init__(self, root):
        self.root = root
        self.current_view = None

    def hide_current_view(self):
        if self.current_view:
            self.current_view.destroy()

        self.current_view = None

    def show_login_view(self):
        self.hide_current_view()

        self.current_view = LoginView(
            self.root,
            self.show_todos_view,
            self.show_create_user_view
        )

        self.current_view.pack()

    def show_todos_view(self):
        self.hide_current_view()

        self.current_view = TodosView(self.root, self.show_login_view)

        self.current_view.pack()

    def show_create_user_view(self):
        self.hide_current_view()

        self.current_view = CreateUserView(
            self.root,
            self.show_todos_view,
            self.show_login_view
        )

        self.current_view.pack()

    def start(self):
        self.show_login_view()
