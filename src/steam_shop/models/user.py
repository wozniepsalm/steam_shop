"""Database model of store user (player / admin)."""

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

# PL: opisy kolumn w stylu sqlalchemy 2.0 i typy danych w pythonie
from steam_shop.models.base import Base

if TYPE_CHECKING:
    from steam_shop.models.purchase import Purchase


class User(Base):
    """Store account with wallet balance in grosze."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    balance: Mapped[int] = mapped_column(default=0)
    is_admin: Mapped[bool] = mapped_column(default=False)

    # tutaj lista bo jeden uzytkownik ma wiele zakupów, cascade all i delete orphan usuwają zakupy wraz z usunięciem uzytkownika
    purchases: Mapped[list["Purchase"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
