"""Database model for purchases: links user with game they bought."""

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from steam_shop.models.base import Base

if TYPE_CHECKING:
    from steam_shop.models.game import Game
    from steam_shop.models.user import User


class Purchase(Base):
    """A single game bought by a single user."""

    __tablename__ = "purchases"
    
    __table_args__ = (UniqueConstraint("user_id", "game_id"),) # unique constraint wymusza unikalność kombinacji kolumn user_id i game_id (ta sama para tylko raz ale kombinacje wiele razy)

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    game_id: Mapped[int] = mapped_column(ForeignKey("games.id"))
    price_paid: Mapped[int] = mapped_column()
    purchased_at: Mapped[datetime] = mapped_column(default=datetime.now)
    
    user: Mapped["User"] = relationship(back_populates="purchases") # relationship to nie kolejna kolumna a skrót by łączyć informacje z tabel by się same uzupełniały
    game: Mapped["Game"] = relationship(back_populates="purchases") # back_populates łączy obie strony tabel ze sobą
