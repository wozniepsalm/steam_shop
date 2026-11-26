"""Database connection: engine, session factory and table creation."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from steam_shop.models import Base
from steam_shop.settings.config import DATABASE_PATH, DATABASE_URL


engine = create_engine(DATABASE_URL) # Engine to obiekt, który wie, gdzie jest baza i jak z nią rozmawiać.
session_factory = sessionmaker(bind=engine) # session to jedna rozmowa z bazą, sessionmaker to fabryka sesji, tworzy przepis na nią
# bind=engine wskazuje do którego silnika mają nalezec sesje


def init_db() -> None: # przygotowuje baze, baze tworzymy przy starcie programu
    """Create database tables if they don't exist."""
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True) # DATABASE_PATH.parent to folder, w którym leży plik bazy, czyli local/. .mkdir tworzy ten folder, bo SQLite nie stworzy pliku w folderze, który nie istnieje. parents=True tworzy też brakujące foldery nadrzędne. exist_ok=True robi że nie ma błędu, jeśli folder już istnieje
    Base.metadata.create_all(engine) # Base.metadata to rejestr opisów wszystkich tabel, create_all tworzy w bazie tabele, których jeszcze nie ma. Istniejących nie rusza i nie kasuje danych.
