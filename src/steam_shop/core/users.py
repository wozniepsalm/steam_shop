"""Logic for finding and creating users."""
# PL: pusta linia oddziela importy zewnetrzne od tych z mojego projektu

# PL: select buduje zapytania sql bez pisania ich w sql
from sqlalchemy import select
from sqlalchemy.orm import Session

from steam_shop.core.exceptions import ShopError
from steam_shop.models import User 


# PL: Funkcja dostaje sesję z zewnątrz zamiast tworzyć ją sama. Dzięki temu jedna sesja może obsłużyć wiele operacji, a core nie musi wiedzieć, skąd się bierze. -> User znaczy, że zwraca obiekt User.
def get_or_create_user(session: Session, username: str) -> User:
    """Return  the user with the given username, creating it if it doesn't exist."""
    username = username.strip() #PL: usuwa spacje z początku i końca nazwy uzytkownika
    if not username: #PL: pusty jest traktowany jako false 
        raise ShopError("Username cannot be empty.")

# PL: sprawdzamy czy jest taki uzytkownik jak podajemy, session scalar wybiera nam z bazy uzytkownika jakiego podajemy i go zwraca albo wyrzuca None jesli nie istnieje
    user = session.scalar(select(User).where(User.username == username))
    if user is None: # PL: i jeśli nie istnieje taki uzytkownik to go tworzymy
        user = User(username=username) # PL: tworzy obiekt User w pamieci, ale nie zapisuje go w bazie
        session.add(user) # PL: dodaje obiekt do sesji
        session.commit() # PL: zapisanie w pliku bazy i ma id
    return user
