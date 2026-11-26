"""Base class shared by all database models."""


from sqlalchemy.orm import DeclarativeBase # ORM (Object relational mapping) pozwala opisać tabele z bazy jako klase a wiersz jako obiekt tej klasy


# własna klasa bazowa dziedzicząca po DeclarativeBase
class Base(DeclarativeBase):
    """Parent class for all database models."""


# nic wiecej nie trzeba tutaj pisac i wystarczy docstring bo jest funkcjonalność z DeclarativeBase
# to jest wspólny rejest wszystkich modeli
