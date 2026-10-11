"""Smoke tests for the repository base."""

import importlib
import pkgutil
import subprocess
import sys

import duckdb
import pytest

import pipeline
import pipeline.collecte
from pipeline.__main__ import ETAPES, lancer


def test_importe_pipeline_et_interroge_duckdb():
    connexion = duckdb.connect(":memory:")
    assert connexion.execute("select 1").fetchone() == (1,)


def test_la_chaine_vide_se_termine_sans_erreur(capsys):
    # Use an empty list, not the real ETAPES: real steps may use the network.
    lancer([])
    assert "Aucune étape" in capsys.readouterr().out


@pytest.mark.skipif(
    bool(ETAPES),
    reason="la liste ETAPES n'est plus vide : on ne lance pas les vraies étapes",
)
def test_la_commande_python_m_pipeline_se_termine_sans_erreur():
    # Only meaningful while ETAPES is empty: it must not run real steps.
    resultat = subprocess.run(
        [sys.executable, "-m", "pipeline"], check=False, capture_output=True, text=True
    )
    assert resultat.returncode == 0, resultat.stderr


def test_les_etapes_tournent_dans_l_ordre():
    passages = []

    def etape_a():
        passages.append("a")

    def etape_b():
        passages.append("b")

    lancer([etape_a, etape_b])
    assert passages == ["a", "b"]


def test_la_premiere_erreur_arrete_la_chaine():
    passages = []

    def etape_qui_echoue():
        raise RuntimeError("echec voulu")

    def etape_b():
        passages.append("b")

    with pytest.raises(RuntimeError):
        lancer([etape_qui_echoue, etape_b])
    assert passages == []


def test_chaque_module_de_collecte_est_dans_etapes():
    manquants = []
    for info_module in pkgutil.iter_modules(pipeline.collecte.__path__):
        module = importlib.import_module(f"pipeline.collecte.{info_module.name}")
        if not hasattr(module, "executer") or module.executer not in ETAPES:
            manquants.append(info_module.name)
    assert not manquants, (
        "Ces modules de pipeline/collecte/ n'ont pas leur fonction executer "
        f"dans ETAPES (pipeline/__main__.py) : {', '.join(manquants)}"
    )
