"""Database model of games available in the store."""

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

# opisy kolumn w stylu sqlalchemy 2.0 i typy danych w pythonie
from steam_shop.models.base import Base

if TYPE_CHECKING:
    from steam_shop.models.purchase import Purchase


class Game(Base):
    """Game available in the store."""

    __tablename__ = "games"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), unique=True)
    genre: Mapped[str] = mapped_column(String(50))
    price: Mapped[int] = mapped_column()

    purchases: Mapped[list["Purchase"]] = relationship(
        back_populates="game", cascade="all, delete-orphan"
    )
