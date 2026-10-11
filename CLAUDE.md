# Conventions du dépôt

Ce dépôt estime la dépense publique par élève de chaque collège et de chaque lycée public et privé sous contrat de France, pour la rentrée 2024. Le travail est découpé en quatre projets qui avancent en parallèle.

## Où vivent les choses (Where things live)

- **Specs** : dans Notion, sous la page [Open Data Collèges & Lycées](https://app.notion.com/p/3f665f22166b81819f10fa04087336ea). Ces pages Notion sont la seule source de référence. Le dossier `docs/specs/` n'en est qu'une copie.
- **Tickets** : dans Linear, équipe « Open Data Education » (clé `EDU`), sous l'initiative « Dépense publique par élève, établissement par établissement ». Chaque projet de la spec a son projet Linear, et chaque jalon de la spec a son jalon Linear.
- **États** : un nouveau ticket arrive dans l'état « Backlog ».
- **Titres des tickets** : `P<projet>-J<jalon>-<numéro> : <titre>`, par exemple `P1-J1-3 : Schémas figés des tables livrées au modèle de coût`.
- **Étiquettes de couche** : `data` pour la chaîne de données (Python et DuckDB), `infra` pour l'automatisation (GitHub Actions, releases GitHub), `docs` pour les textes (inventaire, ADR, notes de méthode). Un ticket peut en porter plusieurs.
- **Décisions d'architecture (ADR)** : dans `docs/adr/`. Chaque ADR est écrite par le ticket qui met la décision en œuvre.
- **Langue** : tout ce qui se lit est écrit en français. Cela vaut pour les tickets, les commits, les pull requests et la documentation.
- **Exploration du code** : l'équipe utilise graphify. L'outil repowise n'est plus utilisé : ignorer le dossier `.repowise/` s'il existe, et ne jamais le commiter.

## Organisation du code

L'organisation suit la spec du projet 1.

- `pipeline/` contient la chaîne de données en Python. Python lit et nettoie les sources, et DuckDB fait les jointures et les calculs en SQL.
- `data/` contient les tables publiées et le manifeste des sources.
- Les copies brutes des sources ne vont pas dans l'historique git, à cause de leur taille. Elles sont conservées dans des releases GitHub.

## Tests

- L'environnement Python est géré par `uv`.
- On écrit d'abord le test qui échoue, puis le code qui le fait passer.
- Avant d'ouvrir une pull request, ces deux commandes doivent passer :
  - `uv run pytest`
  - `uv run ruff check`

## Design

Les projets 1 et 2 ne produisent aucun écran. La règle de design des écrans du site (projet 3) sera précisée quand ses tickets seront créés.
