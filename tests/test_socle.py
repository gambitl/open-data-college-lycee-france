"""Smoke tests for the repository base."""

import importlib
import pkgutil
import subprocess
import sys
from types import SimpleNamespace

import duckdb
import pytest

import pipeline
import pipeline.collecte
from pipeline.__main__ import ETAPES
from pipeline.__main__ import lancer


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


def modules_absents(noms, importer, etapes):
    """Return the collection modules whose executer is missing from etapes."""
    manquants = []
    for nom in noms:
        if nom.startswith("_"):
            continue  # Helper modules are not steps.
        module = importer(nom)
        if not hasattr(module, "executer") or module.executer not in etapes:
            manquants.append(nom)
    return manquants


def test_un_module_d_aide_n_a_pas_besoin_d_etre_dans_etapes():
    def executer_annuaire():
        pass

    modules = {
        "_commun": SimpleNamespace(),
        "annuaire": SimpleNamespace(executer=executer_annuaire),
    }
    assert modules_absents(modules, modules.get, [executer_annuaire]) == []


def test_un_module_de_collecte_absent_de_etapes_est_signale():
    modules = {"annuaire": SimpleNamespace(executer=lambda: None)}
    assert modules_absents(modules, modules.get, []) == ["annuaire"]


def test_chaque_module_de_collecte_est_dans_etapes():
    noms = [info.name for info in pkgutil.iter_modules(pipeline.collecte.__path__)]
    manquants = modules_absents(
        noms,
        lambda nom: importlib.import_module(f"pipeline.collecte.{nom}"),
        ETAPES,
    )
    assert not manquants, (
        "Ces modules de pipeline/collecte/ n'ont pas leur fonction executer "
        f"dans ETAPES (pipeline/__main__.py) : {', '.join(manquants)}"
    )
