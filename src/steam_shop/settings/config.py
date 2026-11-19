"""Application configuration : file paths and settings used across the project."""

# PL: klasa do obslugi sciezek do plików
from pathlib import Path

# PL: ścieka do tego pliku a resolve zmienia ja na bezwzgledna sciezke a parents idzie 4 poziomy w góre do katalogu projektu
PROJECT_ROOT = Path(__file__).resolve().parents[3]
# PL: ścieżka do pliku bazy danych i ukośnik skleja ścieki
DATABASE_PATH = PROJECT_ROOT / "local" / "steam_shop.db"
# PL: adres do bazy w formecie dla sqlalchemy  a  sqlite i sciezka f wstawiaja wartość zmiennej do tekstu
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# PL: wielkie litery bo w pythonie oznaczają stałe wartości których nie zmieniamy w trakcie działania programu
