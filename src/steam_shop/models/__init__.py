"""Database models of the Steam Shop application."""

from steam_shop.models.base import Base
from steam_shop.models.game import Game
from steam_shop.models.purchase import Purchase
from steam_shop.models.user import User

# importy sprawiają ze wszystkie modele są w w Base

__all__ = ["Base", "Game", "Purchase", "User"]
# pozwala na importowanie wszystkiego z tego modłu
