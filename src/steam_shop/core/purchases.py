"""Logic for buying games."""

from sqlalchemy import select 
from sqlalchemy.orm import Session

from steam_shop.core.exceptions import ShopError
from steam_shop.core.games import list_games
from steam_shop.models import User, Game, Purchase


def buy_game(session: Session, user: User, title: str) -> Purchase: # dostaje sesje zalogowanego uzytkownika i wybiera mi te rzeczy wpisane
    """Buying the game with the given title for the given user."""
    game = session.scalar(select(Game).where(Game.title == title.strip()))
    if game is None:
        raise ShopError(f"Game '{title}' does not exist.")

    already_bought = session.scalar(
        select(Purchase).where(Purchase.user_id == user.id, Purchase.game_id == game.id)
    )
    if already_bought is not None:
        raise ShopError(f"You already bought '{game.title}'.")

    if user.balance < game.price:
        raise ShopError(f"Not enough money in your account to buy '{game.title}'.")

    user.balance -= game.price # odejmuje cene od salda 
    purchase = Purchase(user=user, game=game, price_paid=game.price) # tworzy zakup w pamieci, dzieki relationship podajemy obiekty i sqlalchemy uzupelni reszte sam
    session.add(purchase) # dodaje zakup do sesji
    session.commit() # jeden comit by zabranie pieniedzy i kupno zrobilo sie naraz 
    return purchase