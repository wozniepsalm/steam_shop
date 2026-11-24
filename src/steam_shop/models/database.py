"""Database connection: engine, session factory and table creation."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from steam_shop.models import Base
from steam_shop.settings.config import DATABASE_PATH, DATABASE_URL

# PL: Engine to obiekt, który wie, gdzie jest baza i jak z nią rozmawiać.
# PL: Na tym etapie nic się jeszcze nie łączy. Połączenie powstaje dopiero przy pierwszym użyciu.
engine = create_engine(DATABASE_URL)
session_factory = sessionmaker(bind=engine)
# PL: session to jedna rozmowa z bazą, sessionmaker to fabryka sesji, tworzy przepis na nią
# PL: bind=engine wskazuje do którego silnika mają nalezec sesje

# PL: przygotowuje baze, baze tworzymy przy starcie programu
def init_db() -> None:
    """Create database tables if they don't exist."""
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    Base.metadata.create_all(engine)
# PL: DATABASE_PATH.parent to folder, w którym leży plik bazy, czyli local/.
    # PL: .mkdir(...) tworzy ten folder, bo SQLite nie stworzy pliku w folderze, który nie istnieje.
    # parents=True tworzy też brakujące foldery nadrzędne.
    # exist_ok=True sprawia, że nie ma błędu, jeśli folder już istnieje. Jest to potrzebne, bo git nie przechowuje folderu local/ (jest w .gitignore). U prowadzącego po pobraniu projektu tego folderu nie będzie.
# PL: Base.metadata to rejestr opisów wszystkich tabel.
    # PL: create_all tworzy w bazie tabele, których jeszcze nie ma. Istniejących nie rusza i nie kasuje danych. 