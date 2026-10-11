"""Tests of the repository layout and of the tracked files."""

import subprocess
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
LIMITE_OCTETS = 10 * 1024 * 1024

DOSSIERS = [
    "pipeline/collecte",
    "pipeline/schemas",
    "data/tables",
    "data/fictif",
    "data/saisies",
    "data/brut",
    "docs/adr",
    "docs/inventaire",
    "docs/sources",
    "docs/methode",
    "tests",
]


def test_l_arborescence_commune_existe():
    absents = [d for d in DOSSIERS if not (RACINE / d).is_dir()]
    assert not absents, f"Dossiers manquants : {', '.join(absents)}"
    sans_readme = [
        d.name
        for d in (RACINE / "data").iterdir()
        if d.is_dir() and not (d / "README.md").is_file()
    ]
    assert not sans_readme, (
        f"Dossiers de data/ sans README.md : {', '.join(sans_readme)}"
    )


def test_aucun_fichier_suivi_ne_depasse_10_mo():
    sortie = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=RACINE,
        check=True,
        capture_output=True,
    ).stdout
    trop_gros = []
    for nom in sortie.decode().split("\0"):
        chemin = RACINE / nom
        if nom and chemin.is_file() and chemin.stat().st_size > LIMITE_OCTETS:
            trop_gros.append(f"{nom} ({chemin.stat().st_size / 1024 / 1024:.1f} Mo)")
    assert not trop_gros, (
        "Fichiers suivis de plus de 10 Mo, à retirer de git : " + ", ".join(trop_gros)
    )
