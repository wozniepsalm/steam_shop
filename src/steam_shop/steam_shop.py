"""Main code for the Steam Shop application."""

from steam_shop.models.database import init_db


def main() -> None:
    """Main function to run the Steam Shop application."""
    init_db() 
    print("Welcome to the Steam Shop application!")
# PL: Program zaczyna od przygotowania bazy, a dopiero potem wita użytkownika.


if __name__ == "__main__":
    main()
