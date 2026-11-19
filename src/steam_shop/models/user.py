"""Database model of store user (player / admin)."""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

# PL: opisy kolumn w stylu sqlalchemy 2.0 i typy danych w pythonie
from steam_shop.models.base import Base


class User(Base):
    """Store account with wallet balance in grosze."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    # PL: stan konta w groszach i domyślnie 0
    balance: Mapped[int] = mapped_column(default=0)
    is_admin: Mapped[bool] = mapped_column(default=False)
