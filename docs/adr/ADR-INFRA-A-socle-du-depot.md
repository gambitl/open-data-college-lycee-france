# ADR-INFRA-A : Socle du dépôt Python

Statut : acceptée (11 octobre 2026)
Ticket : [EDU-1](https://linear.app/owlaris/issue/EDU-1/p1-j1-1-socle-du-depot-python-uv-pytest-ruff-integration-continue)

Cette décision regroupe les choix faits en construisant le socle du dépôt. Presque quarante tickets vont écrire dans ce squelette, donc chaque choix devient une habitude commune. Chaque section donne le contexte, les options, le choix, la raison et les conséquences.

## 1. Outillage : uv, `uv_build`, `uv.lock`, Python 3.12

**Contexte.** Il faut un seul moyen d'installer Python et les bibliothèques, le même sur chaque machine et dans la CI.

**Options.** uv avec un fichier de verrouillage, pip avec un fichier `requirements.txt`, ou poetry.

**Choix.** uv. Le paquet `pipeline` est un vrai paquet installable, construit avec `uv_build` et placé à la racine du dépôt. Python 3.12 est fixé par `.python-version` et `requires-python`. `uv.lock` est commité, et la CI installe avec `uv sync --locked`. La CI utilise la même version de uv que celle qui a écrit le fichier de verrouillage.

**Raison.** Le fichier de verrouillage donne le même résultat partout, et `--locked` fait échouer la CI si `pyproject.toml` et `uv.lock` ne correspondent plus.

**Conséquences.** Chaque ticket ajoute ses dépendances avec `uv add` et commite `uv.lock`. Deux tickets qui ajoutent des dépendances en parallèle peuvent avoir un conflit sur `uv.lock` : on le résout en relançant `uv lock`.

## 2. Règles de ruff

**Contexte.** Les agents écrivent le code en parallèle ; sans règles communes, les pull requests se remplissent de changements de mise en page.

**Options.** Règles par défaut seules, ou règles par défaut plus quelques familles.

**Choix.** Règles par défaut plus `I` (tri des imports), `B` (erreurs courantes) et `UP` (syntaxe moderne). La CI lance `ruff check` et `ruff format --check`. Ruff est toujours lancé par `uv run`.

**Raison.** La version de ruff fixée par `uv.lock` donne le même verdict partout.

**Conséquences.** Les commandes de réparation sont `uv run ruff format` et `uv run ruff check --fix`.

## 3. Ruleset de `main` et nom du job

**Contexte.** Une marque rouge seule ne bloque rien.

**Options.** Laisser les vérifications comme conseil, ou protéger `main`.

**Choix.** Un ruleset sur `main` exige une pull request et le job `verifications` vert. L'option « à jour avant la fusion » reste désactivée, et l'administrateur peut contourner la règle en urgence.

**Raison.** Une pull request rouge ne doit pas entrer dans `main`. Exiger la mise à jour obligerait chaque pull request ouverte à relancer ses vérifications après chaque fusion.

**Conséquences.** Le nom du job `verifications` fait partie du contrat. Renommer ou couper ce job bloquerait toutes les pull requests. On ajoute des étapes à ce job.

## 4. Forme de `ETAPES` et arrêt à la première erreur

**Contexte.** Une quinzaine de tickets de collecte ajoutent chacun une étape dans `pipeline/__main__.py`.

**Options.** Ajouter à la fin de la liste, ou une liste en deux parties avec ordre alphabétique pour les collectes.

**Choix.** Deux parties commentées : les collectes par ordre alphabétique, puis les assemblages dans l'ordre de leurs dépendances. La première erreur arrête la chaîne. Un test échoue si un module de collecte manque dans la liste.

**Raison.** Des insertions à des endroits différents limitent les conflits de fusion, et le test attrape un oubli.

**Conséquences.** Hypothèse acceptée : les collectes ne dépendent pas les unes des autres.

## 5. Tests sans réseau

**Contexte.** Un test qui télécharge un vrai fichier dépend du serveur distant.

**Choix.** Les tests n'utilisent jamais le réseau. Le marqueur `reseau` couvre les rares exceptions ; il est sauté par défaut et se lance avec `uv run pytest -m reseau`. Les fichiers d'exemple sont sous `tests/fixtures/`.

**Raison.** Des vérifications rapides et stables.

**Conséquences.** Les tests des collectes lisent des petits fichiers locaux.

## 6. Déterminisme des données

**Contexte.** DuckDB peut sortir les lignes dans un ordre différent d'une exécution à l'autre, et les tables publiées sont dans git.

**Choix.** Chaque table écrite dans `data/` est triée par ses colonnes clés. Les montants sont arrondis à un nombre fixe de décimales ou calculés en décimal exact. Les fichiers texte sont en UTF-8 avec des fins de ligne Unix.

**Raison.** Deux exécutions doivent donner les mêmes octets (test de reproduction d'EDU-17).

## 7. Limite de 10 Mo

**Contexte.** Git garde chaque version de chaque fichier pour toujours, et le dépôt est public.

**Choix.** `tests/test_depot.py` échoue si un fichier suivi dépasse 10 Mo. `data/brut/` (sauf son README) et `*.duckdb` sont ignorés.

**Raison.** GitHub n'avertit qu'à 50 Mo ; retirer un fichier de l'historique oblige à le réécrire.

## 8. Langue et nommage

**Contexte.** Les contrats des tickets suivants utilisent déjà des mots français sans accents (`collecte`, `executer`, `ETAPES`).

**Choix.** Tout ce qui se lit est en français, sauf les commentaires et les docstrings dans le code, en anglais. Les noms dans le code et les noms de fichiers sont en français, sans accents, en minuscules avec des tirets bas ; les constantes sont en majuscules.

**Raison.** Éviter que `exécuter` et `executer` coexistent, et les problèmes de noms de fichiers accentués entre macOS et Linux.
