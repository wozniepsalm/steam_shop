"""Logic for games in shop."""

from sqlalchemy import select
from sqlalchemy.orm import Session
    
from steam_shop.models import Game


def list_games(session: Session) -> list[Game]:
    """Return a list of all games in the shop."""
    return list(session.scalars(select(Game))) # scalars wykonuje zapytanie i zwraca wiele wynikow jako obiekty game
   