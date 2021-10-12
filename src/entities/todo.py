import uuid


class Todo:
    """Luokka, joka kuvaa yksittäistä tehtävää

    Attributes:
        content: Merkkijonoarvo, joka kuvaa tehtävän sisältöä.
        done: Boolean-arvo, joka kuvastaa, onko tehtävä jo tehty.
        user: User-olio, joka kuvaa tehtävän omistajaa.
        todo_id: Merkkijonoarvo, joku kuvaa tehtävän id:tä.
    """

    def __init__(self, content, done=False, user=None, todo_id=None):
        """Luokan konstruktori, joka luo uuden tehtävän.

        Args:
            content: Merkkijonoarvo, joka kuvaa tehtävän sisältöä.
            done:
                Vapaaehtoinen, oletusarvoltaan False.
                Boolean-arvo, joka kuvastaa, onko tehtävä jo tehty.
            user:
                Vapaaehtoinen, oletusarvoltaan None.
                User-olio, joka kuvaa tehtävän omistajaa.
            todo_id:
                Vapaaehtoinen, oletusarvoltaan generoitu uuid.
                Merkkijonoarvo, joku kuvaa tehtävän id:tä.
        """

        self.content = content
        self.done = done
        self.user = user
        self.id = todo_id or str(uuid.uuid4())
