"""Application configuration : file paths and settings used across the project."""

from pathlib import Path # klasa do obslugi sciezek do plików


PROJECT_ROOT = Path(__file__).resolve().parents[3] # ścieka do tego pliku a resolve zmienia ja na bezwzgledna sciezke a parents idzie 4 poziomy w góre do katalogu projektu
DATABASE_PATH = PROJECT_ROOT / "local" / "steam_shop.db" # ścieżka do pliku bazy danych i ukośnik skleja ścieki
DATABASE_URL = f"sqlite:///{DATABASE_PATH}" # adres do bazy w formecie dla sqlalchemy 
# wielkie litery bo w pythonie oznaczają stałe wartości których nie zmieniamy w trakcie działania programu
