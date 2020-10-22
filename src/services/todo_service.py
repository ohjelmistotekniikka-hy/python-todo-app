from entities.todo import Todo
from entities.user import User

from repositories.todo_repository import (
    todo_repository as default_todo_repository
)

from repositories.user_repository import (
    user_repository as default_user_repository
)


class InvalidCredentials(Exception):
    pass


class UsernameExists(Exception):
    pass


class TodoService:
    """Sovelluslogiikasta vastaa luokka.

    Attributes:
        user: User-olio, joka kuvaa soovellukseen kirjautunutta käyttäjää.
        todo_repository: Olio, jolla on TodoRepository-luokkaa vastaavat metodit.
        user_repository: Olio, jolla on UserRepository-luokkaa vastaavat metodit.
    """

    def __init__(
        self,
        todo_repository=default_todo_repository,
        user_repository=default_user_repository
    ):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun.

        Args:
            todo_repository:
                Vapaaehtoinen, oletusarvoltaan TodoRepository-olio.
                Olio, jolla on TodoRepository-luokkaa vastaavat metodit.
            user_repository:
                Vapaaehtoinen, oletusarvoltaan UserRepository-olio.
                Olio, jolla on UserRepository-luokkaa vastaavat metodit.
        """
        self.user = None
        self.todo_repository = todo_repository
        self.user_repository = user_repository

    def create_todo(self, content):
        """Luo uuden tehtävän.

        Args:
            content: Merkkijonoarvo, joka kuvaa tehtävän sisältöä.
        Returns:
            Luotu tehtävä Todo-olion muodossa.
        """

        todo = Todo(content=content, user=self.user)

        return self.todo_repository.create(todo)

    def get_undone_todos(self):
        """Palauttaa kirjautuneen käyttäjän tekemättömät tehtävät.

        Returns:
            Palauttaa kirjautuneen käyttäjän tekemättömät tehtävät Todo-olioden listana.
            Jos kirjautunutta käyttäjää ei ole, palauttaa tyhjän listan.
        """

        if not self.user:
            return []

        todos = self.todo_repository.find_by_username(self.user.username)
        undone_todos = filter(lambda todo: not todo.done, todos)

        return list(undone_todos)

    def set_todo_done(self, todo_id):
        """Asettaa tehtävän tehdyksi.

        Args:
            todo_id: Merkkijonoarvo, joka kuvaa tehtävän id:tä.
        """

        self.todo_repository.set_done(todo_id)

    def login(self, username, password):
        """Luo uuden tehtävän.

        Args:
            username: Merkkijonoarvo, joka kuvaa kirjautuvan käyttäjän käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvaa kirjautuvan käyttäjän salasanaa.
        Returns:
            Kirjautunut käyttäjä User-olion muodossa.
        Raises:
            InvalidCredentials:
                Virhe, joka tapahtuu, kun käyttäjätunnus ja salasana eivät täsmää.
        """

        user = self.user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentials('Invalid username or password')

        self.user = user

        return user

    def get_current_user(self):
        """Paluttaa kirjautuunen käyttäjän.

        Returns:
            Kirjautunut käyttäjä User-olion muodossa.
        """
        return self.user

    def get_users(self):
        """Palauttaa kaikki käyttäjät.

        Returns:
            User-oliota sisältä lista kaikista käyttäjistä.
        """
        return self.user_repository.find_all()

    def logout(self):
        """Kirjaa nykyisen käyttäjän ulos.
        """
        self.user = None

    def create_user(self, username, password, login=True):
        """Luo uuden käyttäjän ja tarvittaessa kirjaa sen sisään.

        Args:
            username: Merkkijonoarvo, joka kuvastaa käyttäjän käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvastaa käyttäjän salasanaa.
            login:
                Vapaahtoinen, oletusarvo True.
                Boolean-arvo, joka kertoo kirjataanko käyttäjä sisään onnistuneen luonnin jälkeen.

        Raises:
            UsernameExists: Virhe, joka tapahtuu, kun käyttäjätunnus on jo käytössä.

        Returns:
            Luotu käyttäjä User-olion muodossa.
        """

        existing_user = self.user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExists(f'Username {username} already exists')

        user = self.user_repository.create(User(username, password))

        if login:
            self.user = user

        return user


todo_service = TodoService()
