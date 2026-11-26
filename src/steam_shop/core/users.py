"""Logic for finding and creating users."""
# pusta linia oddziela importy zewnetrzne od tych z mojego projektu

from sqlalchemy import select # select buduje zapytania sql bez pisania ich w sql
from sqlalchemy.orm import Session

from steam_shop.core.exceptions import ShopError
from steam_shop.models import User 



def get_or_create_user(session: Session, username: str) -> User: # Funkcja dostaje sesję z zewnątrz zamiast tworzyć ją sama. Dzięki temu jedna sesja może obsłużyć wiele operacji, a core nie musi wiedzieć, skąd się bierze.
    """Return  the user with the given username, creating it if it doesn't exist."""
    username = username.strip() # usuwa spacje z początku i końca nazwy uzytkownika
    if not username: # pusty jest traktowany jako false 
        raise ShopError("Username cannot be empty.")

# sprawdzamy czy jest taki uzytkownik jak podajemy, session scalar wybiera nam z bazy uzytkownika jakiego podajemy i go zwraca albo wyrzuca None jesli nie istnieje
    user = session.scalar(select(User).where(User.username == username))
    if user is None: #  i jeśli nie istnieje taki uzytkownik to go tworzymy
        user = User(username=username) # tworzy obiekt User w pamieci, ale nie zapisuje go w bazie
        session.add(user) # dodaje obiekt do sesji
        session.commit() # zapisanie w pliku bazy i ma id
    return user
