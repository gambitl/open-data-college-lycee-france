"""Entry point: run every pipeline step in order (uv run python -m pipeline)."""

from collections.abc import Callable

# A step is a function called without any argument.
# The first error stops the whole chain.
ETAPES: list[Callable[[], None]] = [
    # Part 1: collection steps (the executer() function of a module in
    # pipeline/collecte/). Insert each one in alphabetical order of its
    # source name, one per line, with a trailing comma. Example:
    #     autre_source.executer,
    #     ma_source.executer,
    # Part 2: assembly steps, in the order of their dependencies.
]


def lancer(etapes: list[Callable[[], None]]) -> None:
    """Run the steps in order; the first exception is not caught."""
    if not etapes:
        print("Aucune étape à lancer.")
        return
    for etape in etapes:
        print(f"Étape : {etape.__module__}.{etape.__name__}")
        etape()


if __name__ == "__main__":
    lancer(ETAPES)
