# Conventions du dépôt

Ce dépôt estime la dépense publique par élève de chaque collège et de chaque lycée public et privé sous contrat de France, pour la rentrée 2024. Le travail est découpé en quatre projets qui avancent en parallèle.

## Où vivent les choses (Where things live)

- **Specs** : dans Notion, sous la page [Open Data Collèges & Lycées](https://app.notion.com/p/3f665f22166b81819f10fa04087336ea). Ces pages Notion sont la seule source de référence. Le dossier `docs/specs/` ne contient qu'un README qui renvoie vers elles.
- **Tickets** : dans Linear, équipe « Open Data Education » (clé `EDU`), sous l'initiative « Dépense publique par élève, établissement par établissement ». Chaque projet de la spec a son projet Linear, et chaque jalon de la spec a son jalon Linear.
- **États** : un nouveau ticket arrive dans l'état « Backlog ».
- **Titres des tickets** : `P<projet>-J<jalon>-<numéro> : <titre>`, par exemple `P1-J1-3 : Schémas figés des tables livrées au modèle de coût`.
- **Étiquettes de couche** : `data` pour la chaîne de données (Python et DuckDB), `infra` pour l'automatisation (GitHub Actions, releases GitHub), `docs` pour les textes (inventaire, ADR, notes de méthode). Un ticket peut en porter plusieurs.
- **Décisions d'architecture (ADR)** : dans `docs/adr/`. Chaque ADR est écrite par le ticket qui met la décision en œuvre.
- **Langue** : tout ce qui se lit est écrit en français. Cela vaut pour les tickets, les commits, les pull requests, la documentation et les messages affichés par le code. Seuls les commentaires et les docstrings dans le code sont en anglais. Les noms dans le code et les noms de fichiers sont en français, sans accents, en minuscules avec des tirets bas ; les constantes sont en majuscules, comme `ETAPES`.
- **Exploration du code** : l'équipe utilise graphify. L'outil repowise n'est plus utilisé : ignorer le dossier `.repowise/` s'il existe, et ne jamais le commiter.

## Organisation du code

L'organisation suit la spec du projet 1. Tous les tickets partagent cette arborescence : ne la changez pas sans mettre à jour ce fichier.

- `pyproject.toml` et `uv.lock` : le projet Python géré par uv (Python 3.12). Chaque ticket ajoute ses propres dépendances avec `uv add`, et commite `uv.lock`.
- `pipeline/` : la chaîne de données en Python. Python lit et nettoie les sources, et DuckDB fait les jointures et les calculs en SQL.
- `pipeline/collecte/` : un module par source de données.
- `pipeline/schemas/` : les schémas des tables, en fichiers JSON (ce n'est pas un paquet Python).
- `pipeline/__main__.py` : la liste `ETAPES` et le lanceur. `uv run python -m pipeline` lance toutes les étapes dans l'ordre.
- `data/tables/` : les tables livrées au projet 2. `data/fictif/` : les tables fictives. `data/saisies/` : les tables saisies à la main. `data/brut/` : les copies locales des sources et les tables intermédiaires (`data/brut/intermediaire/`), ignorées par git sauf le README.
- `docs/adr/` : les décisions d'architecture. `docs/inventaire/`, `docs/sources/`, `docs/methode/` : les textes de l'inventaire, des sources et de la méthode.
- `tests/` : les tests. Les petits fichiers d'exemple vont dans `tests/fixtures/`.
- Les copies brutes des sources ne vont pas dans l'historique git, à cause de leur taille. Elles sont conservées dans des releases GitHub.
- Git ne garde pas les dossiers vides, donc certains dossiers contiennent un fichier `.gitkeep`. Le ticket qui ajoute le premier vrai fichier d'un de ces dossiers peut supprimer son `.gitkeep`.

## Étapes de la chaîne

- Une étape est une fonction sans argument, en général `executer()` d'un module de `pipeline/collecte/`.
- Dans `ETAPES`, la première partie contient les collectes, insérées par ordre alphabétique du nom de la source, une par ligne. La seconde partie contient les assemblages de tables, dans l'ordre de leurs dépendances. Les collectes ne dépendent pas les unes des autres.
- Un module d'aide partagé de `pipeline/collecte/` a un nom qui commence par un tiret bas (`_commun.py`). Il n'a pas de fonction `executer` et n'entre pas dans `ETAPES`.
- Un module de collecte ne fait rien au moment de son import (pas de téléchargement, pas d'écriture). Tout se passe dans `executer()`.
- La première erreur arrête la chaîne.
- Un test échoue si un module de `pipeline/collecte/` n'a pas son `executer` dans `ETAPES`.

## Tests

- L'environnement Python est géré par `uv`. Lancez toujours les outils par `uv run`, pour que la version fixée par `uv.lock` donne le même verdict partout.
- On écrit d'abord le test qui échoue, puis le code qui le fait passer.
- Avant d'ouvrir une pull request, ces trois commandes doivent passer :
  - `uv run pytest`
  - `uv run ruff check`
  - `uv run ruff format --check`
- Pour réparer ce que ruff signale : `uv run ruff format` et `uv run ruff check --fix`.
- Ruff garde un seul import par ligne (réglage `force-single-line`). `uv run ruff check --fix` le corrige tout seul.
- La version de uv attendue est une 0.8, à partir de la 0.8.5 (`pyproject.toml` refuse les autres). La CI utilise exactement la 0.8.5.
- En cas de conflit sur `uv.lock`, reprenez celui de `main` (`git checkout origin/main -- uv.lock`), puis relancez `uv lock`. Ne supprimez jamais `uv.lock` pour le régénérer : toutes les bibliothèques sauteraient à leur dernière version.
- Les tests n'utilisent jamais le réseau. Un test qui en a vraiment besoin porte le marqueur `reseau`. Il est sauté par défaut, et se lance avec `uv run pytest -m reseau`.
- Les tests lisent de petits fichiers d'exemple rangés sous `tests/fixtures/`.

## Intégration continue

- Le workflow `.github/workflows/ci.yml` tourne sur chaque push et chaque pull request. Son job `verifications` lance `uv sync --locked`, `uv run ruff check`, `uv run ruff format --check` et `uv run pytest`.
- Le ruleset de `main` exige que le job `verifications` soit vert. Son nom fait partie du contrat et ne doit pas changer. Ajoutez des étapes à ce job plutôt que de créer un nouveau job.
- Le workflow reste en lecture seule (`contents: read`). Un workflow qui a besoin d'écrire est un fichier à part.

## Fusions

- `main` est protégé par un ruleset. On ne pousse jamais directement sur `main`, et on n'utilise jamais `gh pr merge --admin`.
- Les pull requests sont fusionnées en squash, qui est la seule méthode autorisée. La branche est supprimée après la fusion.

## Données

- Chaque table écrite dans `data/` est triée par ses colonnes clés, pour que deux exécutions donnent exactement les mêmes octets.
- Les montants sont arrondis à un nombre fixe de décimales avant d'être écrits, ou calculés avec le type décimal exact de DuckDB.
- Les fichiers texte sont en UTF-8 avec des fins de ligne Unix.
- Aucun fichier suivi par git ne dépasse 10 Mo (`tests/test_depot.py` le vérifie). Les bases DuckDB locales (`*.duckdb`) ne sont jamais commitées.

## Design

Les projets 1 et 2 ne produisent aucun écran. La règle de design des écrans du site (projet 3) sera précisée quand ses tickets seront créés.
