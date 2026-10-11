"""Smoke tests for the repository base."""

import duckdb

import pipeline


def test_importe_pipeline_et_interroge_duckdb():
    assert pipeline is not None
    connexion = duckdb.connect(":memory:")
    assert connexion.execute("select 1").fetchone() == (1,)
