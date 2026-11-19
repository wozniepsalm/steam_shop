# Steam shop 
Chat bot for the game shop inspired by Steam.

## Author
Maja Woźniak

## Running
uv sync \
uv run steam-shop

# Notes for me
## Wymagania przełożone na Steam
1. Panel admina: użytkownicy	Admin dodaje i usuwa konta graczy
2. Panel admina: produkty:	Admin dodaje i usuwa gry (tytuł, cena, gatunek)
3. Użytkownik podaje nazwę:	Na starcie: Podaj swój nick:
4. Zadanie specyficzne dla projektu:	Przeglądanie sklepu, kupowanie gier, doładowanie portfela, przeglądanie swojej biblioteki
5. Proste zapytania przez CFG	Polecenia typu kup Wiedźmin 3, pokaż gry RPG, doładuj 50 są rozpoznawane przez gramatykę
6. Gdy CFG sobie nie radzi, idzie do LLM:	Np. „poleć mi coś podobnego do Wiedźmina” trafia do modelu językowego
7. Stan zapisany w bazie:	SQLite: użytkownicy, gry, zakupy i saldo zostają po zamknięciu programu
8. Weryfikacja poprawności: 	Nie można kupić tej samej gry dwa razy, kupić za mało pieniędzy ani kupić gry, której nie ma

## Architektura plików 
steam_shop/
├── src/steam_shop/
│   ├── models/      → tabele bazy: User, Game, Purchase
│   ├── core/        → logika: "kup grę" (sprawdź saldo, sprawdź duplikat, zapisz)
│   ├── services/    → interfejs tekstowy: menu, parser CFG, klient LLM
│   ├── settings/    → konfiguracja (ścieżka do bazy, nazwa modelu LLM)
│   ├── utils/       → drobne pomocnicze funkcje (np. formatowanie ceny)
│   └── steam_shop.py → punkt startowy programu
├── tests/           → testy pytest
├── scripts/         → np. skrypt wypełniający bazę przykładowymi grami
├── local/           → plik bazy .db (nie trafia do gita)
├── pyproject.toml, README.md, .gitignore

### services 
rozmawia z użytkownikiem (input i print). Nie wie nic o SQL.
### core 
podejmuje decyzje (czy można kupić?). Nie robi print ani input.
### models 
opisuje tylko, jak dane wyglądają w bazie.

## Plan etapów
0. Szkielet projektu: środowisko, pyproject.toml, .gitignore, README, git ← zaczynamy tutaj
1. Modele bazy danych: tabele User, Game, Purchase (SQLAlchemy + SQLite)
2. Logika core: kupowanie, doładowanie, biblioteka, z walidacją i wyjątkami
3. Testy do logiki core (pytest)
4. Panel admina: dodawanie i usuwanie użytkowników oraz gier
5. Interfejs tekstowy: logowanie nickiem, pętla poleceń
6. Parser CFG: gramatyka poleceń (biblioteka lark)
7. Integracja LLM: zapasowa ścieżka dla zapytań, których gramatyka nie rozumie
8. Porządki: ruff, mypy, docstringi, README, ostatnie poprawki