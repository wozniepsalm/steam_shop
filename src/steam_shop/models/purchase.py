"""Database model for purchases: links user with game they bought."""

from datetime import datetime

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from steam_shop.models.base import Base


class Purchase(Base):
    """A single game bought by a single user."""

    __tablename__ = "purchases"
    # PL: unique constraint pozwala wymusić unikalność kombinacji kolumn user_id i game_id (ta sama para tylko raz ale kombinacje wiele razy)
    __table_args__ = (UniqueConstraint("user_id", "game_id"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    game_id: Mapped[int] = mapped_column(ForeignKey("games.id"))
    price_paid: Mapped[int] = mapped_column()
    purchased_at: Mapped[datetime] = mapped_column(default=datetime.now)