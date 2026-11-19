"""Base class shared by all database models."""

# PL: ORM (Object relational mapping) pozwala opisać tabele z bazy jako klase a wiersz jako obiekt tej klasy
from sqlalchemy.orm import DeclarativeBase


# PL: własna klasa bazowa dziedzicząca po DeclarativeBase
class Base(DeclarativeBase):
    """Parent class for all database models."""


# PL: nic wiecej nie musimy tutaj pisac i wystarczy docstring bo mamy funkcjonalność z DeclarativeBase
# PL: to jest wspólny rejest wszystkich modeli
