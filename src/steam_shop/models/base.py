"""Base class shared by all database models."""

from sqlalchemy.orm import DeclarativeBase # ORM (Object relational mapping) pozwala opisać tabele z bazy jako klase a wiersz jako obiekt tej klasy


class Base(DeclarativeBase): #własna klasa bazowa dziedzicząca po DeclarativeBase 
    """Parent class for all database models.""" # nic wiecej nie musimy tutaj pisac i wystarczy docstring bo mamy funkcjonalność z DeclarativeBase
# to jest wspólny rejest wszystkich modeli 