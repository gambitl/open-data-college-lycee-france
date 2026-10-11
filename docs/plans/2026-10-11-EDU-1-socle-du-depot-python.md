# Plan: EDU-1 — P1-J1-1 : Socle du dépôt Python (uv, pytest, ruff, intégration continue)

Date: 2026-10-11
Ticket: https://linear.app/owlaris/issue/EDU-1/p1-j1-1-socle-du-depot-python-uv-pytest-ruff-integration-continue
Tracker: Linear (équipe « Open Data Education », clé `EDU`), par le serveur MCP de Linear
Documentation tool: Notion pour les specs (page « Open Data Collèges & Lycées »), ADRs in `docs/adr/` dans le dépôt
Branch: `emdash/edu-1-p1-j1-1-uet1x` (voir « Choix par défaut » plus bas ; Linear propose `victordistefano2/edu-1-p1-j1-1-socle-du-depot-python-uv-pytest-ruff-integration`)
Conventions file: `CLAUDE.md` à la racine du dépôt. Il n'est pas encore sur `main` : voir la question 1 et l'étape préalable plus bas.
Status: ready for review

**Règle de langue de ce fichier et de tout le ticket** (décision de l'utilisateur, question 2) : tout est écrit en français, sauf les commentaires et les docstrings dans le code, qui sont en anglais. Les titres de section de ce fichier (`## Implementation units`, `## Review log`, `## Executor notes`, etc.) et les valeurs de la ligne `Status:` restent en anglais, parce que les agents de la compétence resolve-issue les cherchent sous ces noms exacts. Le texte sous ces titres est en français.

## Questions you may not be asking

*Conseiller CTO, avant le plan, 11 octobre 2026. Écrit en anglais, puis traduit en français à la demande de l'utilisateur. Les réponses de l'utilisateur sont notées sous chaque question.*

Ce ticket construit le squelette vide dans lequel une quarantaine d'autres tickets vont écrire. Il contient très peu de code. Mais presque chaque choix fait ici deviendra une habitude que quarante tickets copieront. La plupart des questions ci-dessous ne portent donc pas sur le code de ce ticket. Elles portent sur les règles qu'il fixe pour tous ceux qui viendront après.

Les questions 1 à 3 sont celles que l'agent principal avait déjà préparées, réécrites pour le lecteur. Je suis d'accord avec les recommandations des questions 2 et 3, avec de petits ajouts. Je ne suis que partiellement d'accord avec la recommandation de la question 1. Les questions 4 à 8 sont des questions qu'on n'avait pas posées. Viennent ensuite quelques points plus petits à connaître, et la liste des angles vérifiés.

### Les questions préparées, réécrites

#### 1. Le fichier de conventions doit-il arriver sur `main` aujourd'hui, à part, ou arriver avec la pull request de ce ticket ?

**De quoi il s'agit.** `CLAUDE.md` est le fichier que chaque agent lit avant de commencer à travailler. Il dit dans quelle langue écrire, quelles commandes de test lancer et où se trouvent les choses. Aujourd'hui, il n'existe que sur une branche à part, jamais fusionnée dans `main`. Or `main` est le point de départ commun de chaque nouveau ticket.

**Pourquoi c'est important ici.** Neuf tickets de la vague 1 démarrent demain, le 12 octobre, en même temps que celui-ci. Chacun part de `main`. Si les conventions n'arrivent sur `main` qu'au moment où ce ticket est fusionné, ces neuf agents démarreront sans elles.

**Ce qui se passe selon la réponse.** Si on copie les deux commits de la branche à part dans cette branche, on n'a rien à faire. Mais les conventions n'arrivent sur `main` qu'à la fusion de ce ticket, probablement après le début de la vague 1. Ces agents ne sauraient pas que tout s'écrit en français, que le dossier `.repowise/` ne doit jamais être commité, ni quelles commandes de test lancer. Pire, d'autres agents de la vague 1 pourraient copier le même fichier dans leur propre branche, et plusieurs pull requests toucheraient alors `CLAUDE.md` en même temps. Si au contraire on fusionne la branche à part dans `main` aujourd'hui, dans sa propre petite pull request, chaque ticket qui démarre demain trouve les conventions. Cette branche ne touche que `CLAUDE.md`, donc elle s'applique sur `main` sans conflit, et cette branche-ci repart simplement du `main` mis à jour. Si on construit sans le fichier, ce ticket ne peut pas noter les nouvelles commandes de test ni l'arborescence, alors que c'est son principal devoir de documentation.

**Ce qui se passe si rien n'est décidé.** L'agent copie les deux commits dans cette branche, et la vague 1 travaille sans conventions jusqu'à la fusion de ce ticket.

**Ma recommandation.** Fusionner la branche à part dans `main` aujourd'hui, avant le début de la vague 1, par une petite pull request que l'agent peut ouvrir. Copier les commits dans cette branche reste la solution de secours. Les deux voies sont compatibles : git supprime automatiquement les commits copiés dès que les mêmes changements sont sur `main`.

Votre réponse : d'accord avec la recommandation (2026-10-11). Qui fusionne cette petite pull request est demandé au moment de l'approbation du plan (voir « Decisions »).

#### 2. Dans quelle langue écrit-on, et quid des noms dans le code ?

**De quoi il s'agit.** Le fichier de conventions dit que tout ce que les gens lisent est écrit en français. La compétence resolve-issue écrit ses propres fichiers de travail en anglais. Un troisième cas n'est écrit nulle part : les noms utilisés dans le code, comme les noms de fonctions et de fichiers.

**Pourquoi c'est important ici.** Les contrats déjà fixés par les tickets suivants utilisent des mots français sans accents : `collecte`, `transformer`, `executer`, `valider`, `ETAPES`. Le choix est donc fait en pratique, mais personne ne l'a écrit. Python accepte les noms accentués. Un agent peut écrire `exécuter` pendant qu'un autre appelle `executer`, et pour Python ce sont deux noms différents.

**Ce qui se passe si on l'ignore.** Les noms divergent d'un ticket à l'autre. L'erreur n'apparaît qu'au moment où le travail de deux tickets se rencontre. Les noms de fichiers accentués peuvent aussi se comporter différemment sur un Mac et sur la machine Linux des vérifications automatiques.

**Ce qui se passe si rien n'est décidé.** Chaque agent décide seul pour les accents.

**Ma recommandation.** Ajouter une ligne dans `CLAUDE.md` : les noms dans le code et les noms de fichiers sont en français, sans accents, en minuscules avec des tirets bas, et les constantes en majuscules comme `ETAPES`.

Votre réponse : « je pense qu'on va tout faire en FR sauf les commentaires dans le code » (2026-10-11). Donc tout est en français, y compris ce fichier de plan, la rétrospective, les commits, la pull request, les commentaires Linear, les `README.md`, `CLAUDE.md`, les ADR et les messages affichés par le code. Les commentaires et les docstrings dans le code sont en anglais. Les noms dans le code suivent la règle recommandée : français sans accents.

#### 3. À quel point la vérification automatique du code doit-elle être stricte ?

**De quoi il s'agit.** Ruff est un « linter » : un programme qui lit le code sans l'exécuter et signale les bugs probables et les problèmes de style. Ruff a aussi un formateur, qui réécrit la mise en page du code exactement de la même façon pour tout le monde.

**Pourquoi c'est important ici.** Une quarantaine de tickets seront écrits par des agents différents, beaucoup en parallèle. Par défaut, ruff vérifie très peu de règles, et la commande du ticket ne vérifie pas la mise en page.

**Ce qui se passe si on l'ignore.** Les pull requests se remplissent de changements de mise en page sans rapport avec le ticket, les fusions bloquent sur des espaces, et les relectures ralentissent.

**Ce qui se passe si rien n'est décidé.** Seule la commande minimale `uv run ruff check` est lancée.

**Ma recommandation.** Les règles par défaut de ruff, plus le tri des imports (`I`), les erreurs courantes (`B`) et la syntaxe Python moderne (`UP`), et les vérifications automatiques lancent aussi `uv run ruff format --check`. `CLAUDE.md` donne aussi les commandes de réparation, `uv run ruff format` et `uv run ruff check --fix`. Ruff est toujours lancé par `uv run`, pour que la version fixée par le fichier de verrouillage donne le même verdict partout.

Votre réponse : d'accord avec la recommandation (2026-10-11).

### Les questions qu'on ne posait pas

#### 4. Une vérification en échec doit-elle pouvoir bloquer une fusion dans `main` ?

**De quoi il s'agit.** Le workflow créé par ce ticket affiche une marque verte ou rouge sur chaque pull request. Seule, une marque rouge ne bloque rien. Pour en faire une vraie barrière, le propriétaire du dépôt active une « règle de protection de branche » sur `main` (GitHub l'appelle maintenant un « ruleset »).

**Pourquoi c'est important ici.** `main` n'a aucune règle de protection aujourd'hui, et une quarantaine de tickets seront fusionnés par des agents. La règle retrouve la vérification par son nom, qui vient du nom du job dans `.github/workflows/ci.yml` : si un ticket suivant renomme ce job ou le coupe en deux, chaque pull request attend pour toujours. L'option « exiger que les branches soient à jour avant la fusion » obligerait chaque pull request ouverte à relancer ses vérifications après chaque fusion.

**Ce qui se passe si on l'ignore.** Tôt ou tard, une pull request rouge est fusionnée, et le ticket suivant part d'un `main` cassé.

**Ce qui se passe si rien n'est décidé.** Les vérifications ne sont qu'un conseil.

**Ma recommandation.** Activer la règle sur `main` après la première exécution verte du workflow. Exiger une pull request et la vérification verte. Laisser désactivée l'option « à jour avant la fusion ». Garder au propriétaire la possibilité de contourner la règle en urgence. Écrire dans `CLAUDE.md` que le nom du job fait partie du contrat.

Votre réponse : d'accord avec la recommandation (2026-10-11). L'agent crée la règle avec `gh` en phase 12, dès que la pull request de ce ticket a ses vérifications vertes.

#### 5. Dans quel ordre tournent les étapes de la chaîne, que se passe-t-il quand l'une échoue, et comment quinze tickets ajoutent-ils leur étape sans écraser celle des autres ?

**De quoi il s'agit.** `pipeline/__main__.py` contient la liste `ETAPES`. EDU-11 a déjà décidé que chaque ticket de collecte y ajoute sa propre étape. Ce qui reste ouvert, c'est la façon d'écrire la liste et son comportement.

**Pourquoi c'est important ici.** Si chaque ticket ajoute sa ligne à la fin de la liste, les quinze modifient le même endroit du fichier, et chaque fusion après la première bloque sur un conflit. Un agent qui résout ce conflit peut supprimer par erreur la ligne d'un autre ticket, sans aucune erreur visible.

**Ce qui se passe si rien n'est décidé.** Chaque ticket ajoute son étape à la fin, et la première erreur arrête la chaîne.

**Ma recommandation.** Garder « la première erreur arrête la chaîne ». Écrire la liste en deux parties commentées : d'abord les étapes de collecte, chacune insérée par ordre alphabétique du nom de sa source ; ensuite, plus tard, les étapes qui assemblent les tables, dans l'ordre de leurs dépendances. Le dire dans le commentaire au-dessus de la liste et dans `CLAUDE.md`. Ajouter un test qui échoue quand un module de `pipeline/collecte/` manque dans la liste. Cela suppose que les étapes de collecte ne dépendent pas les unes des autres.

Votre réponse : d'accord avec la recommandation (2026-10-11), y compris l'hypothèse que les étapes de collecte ne dépendent pas les unes des autres.

#### 6. Les tests ont-ils le droit de télécharger des données sur internet ?

**De quoi il s'agit.** Bientôt, la chaîne téléchargera des fichiers publics. Un test qui télécharge le vrai fichier dépend de la disponibilité du serveur et du fait que le fichier n'a pas changé.

**Pourquoi c'est important ici.** Ce ticket met en place pytest et les vérifications automatiques ; ses règles seront copiées par quinze tickets de collecte.

**Ce qui se passe si on l'ignore.** Les vérifications deviennent lentes et passent au rouge au hasard, et les agents « réparent » ces tests en les assouplissant.

**Ce qui se passe si rien n'est décidé.** Le premier agent qui écrit un tel test donne l'habitude aux autres.

**Ma recommandation.** Les tests n'utilisent jamais le réseau. Un marqueur pytest `reseau`, sauté par défaut, couvre les rares tests qui en ont besoin, lancés avec `uv run pytest -m reseau`. `CLAUDE.md` dit que les tests lisent de petits fichiers d'exemple rangés sous `tests/`.

Votre réponse : d'accord avec la recommandation (2026-10-11).

#### 7. Deux exécutions de la chaîne produiront-elles exactement les mêmes tables ?

**De quoi il s'agit.** DuckDB utilise plusieurs cœurs du processeur à la fois. Après une jointure ou un regroupement, les lignes peuvent sortir dans un ordre différent d'une exécution à l'autre, sauf avec un `ORDER BY` explicite. Les sommes de nombres en virgule flottante peuvent différer sur leurs derniers chiffres. Et l'écrivain CSV standard de Python termine les lignes à la manière de Windows par défaut.

**Pourquoi c'est important ici.** La mesure de succès 3 de la spec est la reproduction exacte, et EDU-17 écrit un test qui compare deux exécutions. Les tables publiées sont dans git, donc chaque octet modifié apparaît comme un changement.

**Ce qui se passe si rien n'est décidé.** Le problème apparaît à EDU-17, après quinze collectes déjà écrites.

**Ma recommandation.** Une courte section sur les données dans `CLAUDE.md` : chaque table écrite dans `data/` est triée par ses colonnes clés ; les montants sont arrondis à un nombre fixe de décimales, ou calculés avec le type décimal exact de DuckDB ; les fichiers texte sont en UTF-8 avec des fins de ligne Unix.

Votre réponse : d'accord avec la recommandation (2026-10-11).

#### 8. Qu'est-ce qui empêche un gros fichier de données d'entrer pour toujours dans l'historique public ?

**De quoi il s'agit.** Git garde chaque version de chaque fichier pour toujours, et le dépôt est public. Retirer un fichier de l'historique veut dire réécrire cet historique.

**Pourquoi c'est important ici.** Ignorer `data/brut/` ne protège qu'un dossier. Un téléchargement enregistré ailleurs, ou une table publiée qui grossit, entre dans git sans avertissement. GitHub n'avertit qu'au-delà de 50 Mo et ne refuse qu'au-delà de 100 Mo.

**Ce qui se passe si rien n'est décidé.** Seul `.gitignore` protège le dépôt.

**Ma recommandation.** Une vérification qui échoue quand un fichier suivi par git dépasse 10 Mo, avec un message clair. Ajouter aussi `*.duckdb` dans `.gitignore`.

Votre réponse : d'accord avec la recommandation (2026-10-11).

### À savoir aussi

- Les versions figées des actions GitHub et le fichier de verrouillage ne se mettent jamais à jour tout seuls. Dependabot peut ouvrir chaque semaine une pull request de mises à jour. On peut le décider plus tard.
- EDU-8 publiera les copies brutes dans des releases GitHub, ce qui demande un droit d'écriture. Ce droit doit aller seulement au job qui publie, dans son propre workflow.
- Pouvoir lancer une seule étape (`uv run python -m pipeline <nom de l'étape>`) ferait gagner du temps, mais ce n'est pas demandé ici.
- Les copies datées de l'ADR-DATA-A (EDU-8) auront besoin d'une règle pour la date : heure UTC ou heure de Paris. EDU-8 doit en être informé.

### Comment chaque angle a été utilisé

- Sécurité et autorisations : question 4. Le plan donne déjà au workflow un droit de lecture seule et fige chaque action à une version exacte.
- Verrouillage du modèle de données : question 5. L'arborescence est fixée par le ticket et la spec.
- Volume et performance : pas d'enjeu stratégique, angle sauté, sauf la question 8.
- Pannes et retour en arrière : questions 4, 5 et 6.
- Cas limites pour l'utilisateur : pas d'écran, angle sauté.
- Exploitation et coût : dépôt public, minutes GitHub Actions gratuites, angle sauté.
- Réversibilité : question 8.
- Couplages cachés : questions 4 (le nom de la vérification) et 5 (la liste d'étapes partagée).
- Angles ajoutés pour cette technologie : GitHub (question 4), les fusions git (questions 5 et 8), pytest et le réseau (question 6), le déterminisme de DuckDB (question 7), le nommage en Python (question 2).

## Ticket

## Why this matters (plain language)

**In plain terms:** on prépare le dépôt de code, encore vide, pour que tous les autres tickets écrivent et testent leur code de la même façon.

* **What the title means**: le « socle » est la structure de base du dépôt. « uv » est l'outil qui installe Python et les bibliothèques du projet. « pytest » lance les tests automatiques. « ruff » vérifie que le code est propre et homogène. L'« intégration continue » (CI) est un robot de GitHub qui relance les tests à chaque modification.
* **Why we are doing it**: près de quarante tickets vont écrire du code en parallèle. Sans socle commun, chacun inventerait sa propre organisation, et rien ne s'assemblerait.
* **For the user**: les données publiées sortiront d'une chaîne vérifiée automatiquement, donc plus fiable.

**Goal.** Livrer un projet Python vide mais fonctionnel, avec la bonne arborescence, les outils de test et une CI verte. Greenfield : rien n'existe encore.

## Where things are today (read first)

* **Dépôt** : greenfield, aucun code. Il ne contient que `CLAUDE.md` (les conventions de l'équipe) et `docs/specs/` (une copie des specs).
* **Spec** : [projet 1 sur Notion](<https://app.notion.com/p/3f665f22166b8158bc46f59fd823f825>), section 7 « Où en est-on et contexte technique ». Elle prévoit `pipeline/` en Python avec DuckDB (une base de données qui tient dans un fichier et fait les calculs en SQL), `data/` pour les tables publiées, et les copies brutes des sources dans des releases GitHub.
* **Contract**: l'arborescence ci-dessous est partagée par tous les tickets du projet. Ne la change pas sans mettre à jour `CLAUDE.md`.

## Scope

1. Créer `pyproject.toml` à la racine, géré par uv, avec Python 3.12, le paquet `pipeline` et la dépendance `duckdb`. Ajouter `pytest` et `ruff` comme dépendances de développement. Les autres tickets ajoutent leurs propres dépendances.
2. Créer l'arborescence suivante, avec un fichier `README.md` court dans chaque dossier de `data/` pour dire ce qu'il contient :
   * `pipeline/__init__.py` et `pipeline/collecte/__init__.py` (un module par source de données) ;
   * `pipeline/schemas/` (les schémas des tables, écrits par P1-J1-3) ;
   * `pipeline/__main__.py` avec une liste ordonnée et vide `ETAPES = []`. Chaque ticket de collecte y ajoutera sa propre étape. La commande `uv run python -m pipeline` lance toutes les étapes dans l'ordre ;
   * `data/tables/` (tables livrées au projet 2), `data/fictif/` (tables fictives), `data/saisies/` (tables saisies à la main), `data/brut/` (copies locales des sources et tables intermédiaires, ignorée par git) ;
   * `docs/adr/`, `docs/inventaire/`, `docs/sources/`, `docs/methode/` ;
   * `tests/` avec un test de fumée.
3. Écrire `.gitignore` : `data/brut/`, `.venv/`, les caches Python, pytest et ruff.
4. Créer le workflow GitHub Actions `.github/workflows/ci.yml`. Il tourne sur chaque push et chaque pull request, installe uv, puis lance `uv run ruff check` et `uv run pytest`. Il n'a que la permission `contents: read`.
5. Mettre à jour la section « Tests » de `CLAUDE.md` si une commande change.

## Acceptance (TDD)

* `tests/test_socle.py` : écrire d'abord un test qui importe `pipeline` et exécute `select 1` dans DuckDB en mémoire. Il échoue tant que le paquet n'existe pas, puis passe.
* `tests/test_socle.py` : `uv run python -m pipeline` se termine sans erreur quand `ETAPES` est vide.
* `uv run pytest` et `uv run ruff check` passent en local et dans la CI.
* La CI échoue bien quand un test échoue. Le vérifier une fois avec un test volontairement faux, puis le retirer.
* Le workflow n'a que la permission `contents: read`.

**Size: S** · Blocked by: none · Feeds: P1-J1-4 (<issue id="bfe5d82c-17e7-4cb8-a29a-b22f8f1717cd" href="https://linear.app/owlaris/issue/EDU-7/p1-j1-4-script-de-validation-dune-table-contre-son-schema">EDU-7</issue>), P1-J1-6 (<issue id="cf32c1d0-5f5a-4809-9d12-2f9927f480c1" href="https://linear.app/owlaris/issue/EDU-8/p1-j1-6-telechargement-commun-des-sources-avec-copie-datee-et">EDU-8</issue>), P1-J1-7 (<issue id="b4c7dc1a-26cd-417c-b6ec-07599ca947c9" href="https://linear.app/owlaris/issue/EDU-9/p1-j1-7-totaux-officiels-pour-le-recalage-programmes-141-et-139">EDU-9</issue>)

### Decisions already taken upstream

Projet parent : [Inventaire et collecte des données de dépenses](https://linear.app/owlaris/project/inventaire-et-collecte-des-donnees-de-depenses-28172cd5b15f) (P-EDU-44), jalon « Inventaire des dépenses et des sources » (cible le 14 octobre 2026). Son bloc « Open questions and decisions », copié tel quel :

> Questions ouvertes (le détail et les recommandations sont dans la section 9 de la spec) :
>
> * Comment traiter les valeurs masquées par le secret statistique.
> * Quelle est la précision de l'âge comme approximation de l'échelon.
> * Quelle source utiliser pour compter les étudiants post-bac.
> * Quelle couverture on aura en outre-mer, en particulier à Mayotte.
> * Comment répartir les heures supplémentaires et le pacte enseignant, qui n'ont pas de données par établissement.
> * Dans quel groupe comparer les lycées polyvalents.
>
> Décisions d'architecture à créer dans docs/adr/ :
>
> * ADR-DATA-A : conserver une copie datée des sources brutes. Statut : à créer, par EDU-8 (P1-J1-6).
> * ADR-DATA-B : utiliser l'âge comme approximation de l'échelon, et combiner le corps et l'âge, que la source ne croise pas. Statut : à créer, par EDU-21 (P1-J3-2).
> * ADR-DATA-C : rattacher les marchés publics aux établissements (deuxième version). Statut : à créer, par EDU-33 (P1-J4-3), puis acceptée par EDU-38 (P1-J4-8) une fois la précision mesurée.
> * ADR-DATA-D : écrire les schémas des tables au format Table Schema de Frictionless. Statut : à créer, par EDU-3 (P1-J1-3). Ajoutée le 11 octobre 2026, lors de la création des tickets.

Aucune de ces ADR n'existe encore, et aucune n'est écrite par ce ticket. Aucune des questions ouvertes ne concerne ce ticket.

Contrats fixés par des tickets suivants, que ce ticket doit respecter (lus dans Linear le 11 octobre 2026) :

- EDU-11 (P1-J2-1), « convention commune à toutes les collectes du jalon 2 » : chaque collecte est un module `pipeline/collecte/<source>.py` avec une fonction pure `transformer(chemin_source)` et une fonction `executer()` sans argument, et « l'étape est ajoutée à la liste `ETAPES` de `pipeline/__main__.py` ». Une étape de `ETAPES` est donc une fonction appelée sans argument.
- EDU-11 écrit aussi ses tables intermédiaires dans `data/brut/intermediaire/<table>.parquet`, à l'intérieur du dossier que ce ticket fait ignorer par git.
- EDU-7 (P1-J1-4) ajoute la dépendance `frictionless`, un module `pipeline/valider.py` lancé par `python -m pipeline.valider`, des schémas dans `pipeline/schemas/<table>.schema.json`, et une étape de plus dans `.github/workflows/ci.yml`.
- EDU-8 (P1-J1-6) ajoute `httpx`, `pipeline/sources.py`, `data/manifeste_sources.csv`, et écrit lui-même `docs/sources/README.md`.
- EDU-17 (P1-J2-9) s'appuie sur « `uv run python -m pipeline` lance toutes les étapes de la liste `ETAPES` » pour son test de reproduction.

## Dependencies

Dependencies: clear. Linear n'indique aucune relation « bloqué par », et le pied du ticket dit « Blocked by: none ».

## Code mapping

Le dépôt est vide, comme le dit le ticket. Sur `main`, il ne contient que `docs/specs/README.md`, qui renvoie maintenant vers Notion au lieu de contenir une copie des specs. Il n'y a pas de code, donc rien à cartographier, ni avec repowise ni avec un autre outil. Un dossier `.repowise/` non suivi existe dans le worktree. Le fichier de conventions dit que repowise n'est plus utilisé, qu'il faut ignorer ce dossier, et qu'il ne doit jamais être commité.

Faits qui façonnent le plan :

- **Le fichier de conventions manque sur `main`.** Le ticket dit que le dépôt « ne contient que `CLAUDE.md` et `docs/specs/` ». En réalité, `CLAUDE.md` n'existe que sur la branche `emdash/create-tickets-projet-inventaire-mlvc7`, qui a déjà une pull request ouverte, la [#1](https://github.com/gambitl/open-data-college-lycee-france/pull/1) (« Ajouter le fichier de conventions du dépôt », créée le 11 octobre 2026 à 13 h 26). La phase 3 l'avait manquée : `gh pr list --state all` n'avait rien renvoyé. Cette branche est partie de `3ede93f`, avant les deux derniers commits de `main`. Ses deux commits (`1e69881` ajoute `CLAUDE.md`, `cc598ec` corrige une ligne sur `docs/specs/`) ne touchent que `CLAUDE.md`, donc ils s'appliquent proprement sur `main`.
- **Outils disponibles en local :** uv 0.8.5 et CPython 3.12.11 (installé par uv).
- **Forge :** dépôt GitHub `gambitl/open-data-college-lycee-france`, public, donc les minutes de GitHub Actions sont gratuites. La branche `main` n'a aucune règle de protection. La seule pull request existante est la #1, qui ajoute `CLAUDE.md`. `gh` est connecté avec le compte `gambitl`. Le serveur MCP de GitHub n'a pas réussi à se connecter dans cette session, donc l'exécuteur utilise `gh`.
- **Travail en parallèle :** la vague 1 du projet lance neuf tickets le 12 octobre, en même temps que celui-ci (EDU-2, EDU-3, EDU-4, EDU-5, EDU-6, EDU-24, EDU-25, EDU-26). EDU-2 écrit dans `docs/inventaire/`, EDU-3 écrit dans `pipeline/schemas/` et `docs/adr/`. Tout fichier que ce ticket crée dans ces dossiers peut entrer en collision avec les leurs.
- **Point chaud à venir :** une quinzaine de tickets de collecte ajouteront chacun un import et une entrée dans `ETAPES`, dans `pipeline/__main__.py`, beaucoup en parallèle pendant la vague 3.

## Open questions and answers

Les questions ont été réécrites par le conseiller CTO et posées dans le bloc « Questions you may not be asking » en haut de ce fichier. Les réponses de l'utilisateur, données le 11 octobre 2026, y sont notées sous chaque question. En résumé :

1. **D'où vient `CLAUDE.md` ?** Recommandation retenue : une petite pull request séparée amène `CLAUDE.md` sur `main` avant que l'exécuteur démarre. Solution de secours : copier les commits `1e69881` et `cc598ec` en tête de cette branche.
2. **Langue.** Tout en français, sauf les commentaires et les docstrings dans le code, en anglais. Noms dans le code et noms de fichiers en français, sans accents, en minuscules avec des tirets bas ; constantes en majuscules.
3. **Ruff.** Règles par défaut plus `I`, `B` et `UP` ; `uv run ruff format --check` dans la CI ; commandes de réparation dans `CLAUDE.md` ; ruff toujours lancé par `uv run`.
4. **Protection de `main`.** Un ruleset exige une pull request et la vérification verte, sans l'option « à jour avant la fusion », avec contournement possible pour l'administrateur. L'exécuteur le crée en phase 12. Le nom du job fait partie du contrat.
5. **`ETAPES`.** La première erreur arrête la chaîne. Deux parties commentées : collectes par ordre alphabétique, puis assemblages. Un test attrape un module de collecte absent de la liste. Hypothèse acceptée : les collectes ne dépendent pas les unes des autres.
6. **Réseau dans les tests.** Interdit par défaut ; marqueur `reseau` sauté par défaut.
7. **Déterminisme.** Section « Données » dans `CLAUDE.md` : tables triées par clé, montants arrondis ou décimaux exacts, UTF-8 avec fins de ligne Unix.
8. **Gros fichiers.** Une vérification échoue au-delà de 10 Mo pour tout fichier suivi ; `*.duckdb` ignoré.

### Choix par défaut (non demandés)

- **Branche.** Le travail reste sur `emdash/edu-1-p1-j1-1-uet1x`, la branche créée par l'outil d'espace de travail pour ce worktree. Elle contient déjà l'identifiant `edu-1`, que Linear utilise pour relier une pull request au ticket.
- **Paquet.** `pipeline` est un vrai paquet installable, construit avec le backend de uv (`uv_build`), configuré pour un paquet à la racine du dépôt plutôt que sous `src/` (`module-root = ""`, `module-name = "pipeline"`). uv l'installe en mode modifiable, donc `import pipeline` marche depuis les tests et depuis n'importe quel dossier. Si la version locale de uv ne sait pas faire cela, l'implémenteur utilise `hatchling` à la place et le note.
- **Version de Python.** Un fichier `.python-version` fixe 3.12 pour tout le monde, et `requires-python = ">=3.12"` dans `pyproject.toml`.
- **Version de uv.** La CI installe la même version de uv que celle qui a écrit `uv.lock` en local (0.8.5 aujourd'hui), pour que les deux donnent le même verdict. `pyproject.toml` indique la version minimale avec `[tool.uv] required-version`.
- **Fichier de verrouillage.** `uv.lock` est commité, et la CI installe avec `uv sync --locked`, donc un fichier de verrouillage qui ne correspond plus à `pyproject.toml` fait échouer la CI.
- **Dépendances de développement** dans `[dependency-groups] dev`, là où `uv add --dev` les écrit.
- **`data/brut/` et son README.** Le ticket demande à la fois un `README.md` dans chaque dossier de `data/` et que `data/brut/` soit ignoré par git. Une règle `data/brut/` ignorerait aussi le README. `.gitignore` utilise donc `data/brut/*` suivi de `!data/brut/README.md`.
- **Dossiers que d'autres tickets remplissent.** Git ne garde pas les dossiers vides. `docs/adr/`, `docs/inventaire/`, `docs/sources/`, `docs/methode/` et `pipeline/schemas/` reçoivent chacun un fichier vide `.gitkeep` plutôt qu'un `README.md`, parce que EDU-2, EDU-3 et EDU-8 y écriront leurs propres fichiers, parfois en parallèle. `pipeline/schemas/` contient des fichiers JSON (ADR-DATA-D), donc ce n'est pas un paquet Python et il n'a pas de `__init__.py`.
- **Les étapes de `ETAPES`.** Une étape est une fonction appelée sans argument, comme le dit le contrat d'EDU-11. `pipeline/__main__.py` contient une petite fonction `lancer(etapes)` qui lance les étapes dans l'ordre et affiche, en français, le nom de chaque étape avant de la lancer. La première erreur arrête la chaîne avec un code de sortie non nul.
- **La limite de 10 Mo est un test pytest**, `tests/test_depot.py`, plutôt qu'une étape à part dans le workflow. Il liste les fichiers suivis avec `git ls-files` et échoue avec un message en français qui nomme chaque fichier trop gros. Il tourne donc dans la CI, et aussi en local avant chaque push, ce qui prévient les agents plus tôt.
- **`.gitignore`** liste aussi `.repowise/` (le fichier de conventions interdit de le commiter), `.DS_Store` (fichiers de dossier de macOS), `*.duckdb` et `*.duckdb.wal`.
- **Détails de la CI.** Déclencheurs exactement comme le dit le ticket : chaque push et chaque pull request. Sur une branche avec une pull request ouverte, les vérifications tournent deux fois, ce qui ne coûte rien sur un dépôt public. Le workflow a `permissions: contents: read` au niveau du fichier, un groupe `concurrency` qui annule une exécution plus ancienne de la même branche, une limite de temps sur le job, `persist-credentials: false` sur le checkout, une image fixe (`ubuntu-24.04`), et chaque action figée sur un hash de commit complet, avec sa version en commentaire. Le job s'appelle `verifications`, et c'est ce nom que le ruleset exige.
- **Repowise.** Comme le dit le fichier de conventions, l'exécuteur ne lance pas repowise dans ce dépôt. Les étapes de la phase 7 qui en dépendent (`repowise update`, `get_change_risk`, `get_risk`, `get_why`, `repowise decision add`, les commentaires `DECISION:`) sont sautées. Les quatre relecteurs de code et le relecteur indépendant travaillent à partir du diff seul. Le changement est petit et entièrement nouveau, donc rien en dehors du diff ne peut casser.
- **L'arborescence dans `CLAUDE.md`.** Le contrat dit que l'arborescence ne doit pas changer sans mettre à jour `CLAUDE.md`. La section « Organisation du code » de `CLAUDE.md` reçoit donc l'arborescence complète, pour que chaque agent la trouve avant de commencer.
- **Format des commits.** `CLAUDE.md` ne fixe pas de format. Les commits suivent la forme Conventional Commits (`feat`, `fix`, `test`, `chore`, `ci`, `docs`), avec une description en français, comme demandé par la compétence et par la règle de langue.

## Architecture

L'approche est verrouillée par le ticket, la spec, les contrats des tickets suivants et les réponses aux questions. Il ne reste pas de vrai choix entre deux architectures.

No new decision since phase 4.

## Implementation units

### Étape préalable, faite par la conversation principale avant de lancer l'exécuteur — status: done (solution de secours : cherry-pick de 1e69881 et cc598ec, la PR #1 n'était pas fusionnée)

Amener `CLAUDE.md` sur `main` (question 1). La petite pull request existe déjà : c'est la [#1](https://github.com/gambitl/open-data-college-lycee-france/pull/1), depuis la branche `emdash/create-tickets-projet-inventaire-mlvc7`, qui ne touche que `CLAUDE.md` et se fusionne sans conflit. L'utilisateur la fusionne lui-même. L'exécuteur ne la fusionne jamais. Au début de la phase 6, il fait `git fetch origin` et regarde si `CLAUDE.md` est sur `origin/main`. Si oui, la branche de ce ticket, qui n'a encore aucun commit, avance jusqu'au nouveau `main` (`git merge --ff-only origin/main`).

Si cette pull request n'est pas fusionnée quand l'exécuteur démarre, l'exécuteur applique la solution de secours au début de la phase 6 : il copie les commits `1e69881` et `cc598ec` en tête de cette branche avec `git cherry-pick`, avant le commit du fichier de plan. Dans les deux cas, `CLAUDE.md` est à la racine de la branche avant l'unité 1.

### Unit 1: Projet Python, paquet `pipeline` et premier test de fumée — status: done
- Failing test: `tests/test_socle.py::test_importe_pipeline_et_interroge_duckdb`. Il importe `pipeline`, ouvre une connexion DuckDB en mémoire, exécute `select 1` et vérifie que le résultat vaut 1. Il échoue tant que le paquet et `pyproject.toml` n'existent pas.
- Minimum code:
  - `.gitignore` en premier, avant toute installation, pour que `.venv/` ne soit jamais commité : `data/brut/*`, `!data/brut/README.md`, `.venv/`, `__pycache__/`, `*.py[cod]`, `.pytest_cache/`, `.ruff_cache/`, `.repowise/`, `.DS_Store`, `*.duckdb`, `*.duckdb.wal`.
  - `.python-version` contenant `3.12`.
  - `pyproject.toml` : nom du projet, version `0.1.0`, `requires-python = ">=3.12"`, dépendance `duckdb` ; `[dependency-groups] dev` avec `pytest` et `ruff` ; `[build-system]` avec `uv_build` configuré pour le paquet `pipeline` à la racine (voir « Choix par défaut ») ; `[tool.uv] required-version` ; `[tool.pytest.ini_options]` avec `testpaths = ["tests"]`, l'option `--strict-markers`, le marqueur `reseau` déclaré avec une description en français, et `-m "not reseau"` dans `addopts` pour le sauter par défaut ; `[tool.ruff]` avec `target-version = "py312"` et `[tool.ruff.lint] extend-select = ["I", "B", "UP"]`.
  - `pipeline/__init__.py` avec une docstring courte en anglais.
  - `uv.lock`, produit par `uv lock` puis `uv sync`.
  - Vérifier aussi que `uv run pytest -m reseau` sélectionne bien les tests marqués (aucun pour l'instant) et que `uv run pytest` passe.
- Refactor: aucun.
- Commit message: `chore: créer le projet Python géré par uv, avec DuckDB, pytest et ruff`
- Depends on: l'étape préalable.

### Unit 2: Lanceur de la chaîne et liste `ETAPES` — status: done
- Failing test: dans `tests/test_socle.py`, écrire d'abord ces quatre tests, qui échouent tant que `pipeline/__main__.py` n'existe pas :
  - `test_la_chaine_vide_se_termine_sans_erreur` : lance `python -m pipeline` dans un processus séparé, avec le même interpréteur (`sys.executable`), et vérifie le code de sortie 0.
  - `test_les_etapes_tournent_dans_l_ordre` : appelle `lancer([etape_a, etape_b])` avec deux fausses étapes qui notent leur passage, et vérifie l'ordre.
  - `test_la_premiere_erreur_arrete_la_chaine` : appelle `lancer([etape_qui_echoue, etape_b])`, vérifie que l'erreur remonte et que `etape_b` n'a pas tourné.
  - `test_chaque_module_de_collecte_est_dans_etapes` : liste les modules de `pipeline.collecte` avec `pkgutil.iter_modules`, et vérifie que chacun a une fonction `executer` présente dans `ETAPES`. Le message d'échec, en français, nomme le module manquant. Avec un dossier de collecte vide, ce test passe ; l'implémenteur vérifie une fois à la main qu'il échoue avec un faux module temporaire, puis supprime ce faux module sans le commiter.
- Minimum code:
  - `pipeline/collecte/__init__.py`, avec une docstring en anglais.
  - `pipeline/__main__.py` : la liste `ETAPES`, typée comme une liste de fonctions sans argument, écrite en deux parties commentées (en anglais) : d'abord les étapes de collecte, chacune insérée par ordre alphabétique du nom de sa source, une par ligne avec une virgule finale ; ensuite les étapes d'assemblage, dans l'ordre de leurs dépendances. Le commentaire montre comment ajouter une étape. Une fonction `lancer(etapes)` qui affiche en français le nom de chaque étape avant de la lancer, et un message court quand la liste est vide. La première exception arrête la chaîne : elle n'est pas attrapée, donc le code de sortie est non nul. Le bloc `if __name__ == "__main__":` appelle `lancer(ETAPES)`.
- Refactor: aucun prévu.
- Commit message: `feat(pipeline): lancer les étapes de la liste ETAPES dans l'ordre`
- Depends on: unité 1.

### Unit 3: Arborescence, `README.md` des données et limite de taille — status: done
- Failing test:
  - `tests/test_depot.py::test_l_arborescence_commune_existe` : vérifie que chaque dossier de l'arborescence du ticket existe (`pipeline/collecte`, `pipeline/schemas`, `data/tables`, `data/fictif`, `data/saisies`, `data/brut`, `docs/adr`, `docs/inventaire`, `docs/sources`, `docs/methode`, `tests`) et que chaque dossier de `data/` contient un `README.md`. Dans la CI, qui part d'un clone neuf, ce test prouve aussi que ces fichiers sont bien suivis par git, y compris `data/brut/README.md` malgré le `.gitignore`.
  - `tests/test_depot.py::test_aucun_fichier_suivi_ne_depasse_10_mo` : liste les fichiers suivis avec `git ls-files -z` et échoue si l'un dépasse 10 Mo (10 × 1024 × 1024 octets), avec un message en français qui nomme chaque fichier et sa taille. Il passe d'emblée ; l'implémenteur vérifie une fois à la main qu'il échoue avec un faux fichier de 11 Mo ajouté à l'index, puis le retire sans le commiter.
- Minimum code:
  - `data/tables/README.md`, `data/fictif/README.md`, `data/saisies/README.md`, `data/brut/README.md`, chacun court et en français, qui dit ce que contient le dossier et qui l'écrit. Pour `data/brut/`, il dit aussi que tout le reste du dossier est ignoré par git, que les copies datées vont dans des releases GitHub (ADR-DATA-A, EDU-8), et que les tables intermédiaires vont dans `data/brut/intermediaire/`.
  - Un fichier vide `.gitkeep` dans `pipeline/schemas/`, `docs/adr/`, `docs/inventaire/`, `docs/sources/`, `docs/methode/`.
- Refactor: aucun.
- Commit message: `feat(socle): créer l'arborescence commune et limiter la taille des fichiers suivis`
- Depends on: unité 1. Indépendante de l'unité 2 (fichiers différents).

### Unit 4: Workflow d'intégration continue — status: done
- Failing test: la preuve est l'unité 5, qui fait tourner ce workflow sur GitHub avec un test volontairement faux. En local, l'implémenteur lance les mêmes commandes que le workflow, dans le même ordre, et vérifie qu'elles passent.
- Minimum code: `.github/workflows/ci.yml`, avec :
  - un nom de workflow (`CI`) ;
  - les déclencheurs `push` et `pull_request`, sans filtre de branche ;
  - `permissions: contents: read` au niveau du fichier, et aucune permission au niveau du job ;
  - un groupe `concurrency` par workflow et par référence, avec `cancel-in-progress: true` ;
  - un seul job nommé `verifications`, sur `ubuntu-24.04`, avec `timeout-minutes: 10` ;
  - les étapes : `actions/checkout` avec `persist-credentials: false` ; `astral-sh/setup-uv` avec la version de uv fixée (celle du `uv.lock`) et le cache activé ; `uv sync --locked` ; `uv run ruff check` ; `uv run ruff format --check` ; `uv run pytest` ;
  - chaque action figée sur le hash de commit complet de sa dernière version publiée, avec la version en commentaire. L'implémenteur trouve ces hashes avec `gh api` (par exemple `gh api repos/actions/checkout/releases/latest` puis la référence du tag), jamais de mémoire.
  - Les commentaires du fichier sont en anglais. Une ligne de commentaire dit que le nom du job `verifications` est exigé par le ruleset de `main` et ne doit pas changer.
- Refactor: aucun.
- Commit message: `ci: lancer ruff et pytest sur chaque push et chaque pull request`
- Depends on: unités 1, 2 et 3 (le workflow lance leurs tests).

### Unit 5: Preuve que la CI échoue sur un test faux (push anticipé autorisé) — status: done
- Ce n'est pas une unité de code. C'est la seule exception à la règle « rien n'est poussé avant la phase 12 », autorisée par ce plan parce que le critère d'acceptation exige une exécution réelle de la CI.
- Étapes, faites par l'exécuteur une fois l'unité 4 commitée :
  1. Créer une branche locale temporaire `edu-1-preuve-ci-rouge` à partir de la branche du ticket.
  2. Y ajouter un seul commit avec `tests/test_preuve_ci_rouge.py`, qui contient un test volontairement faux (une assertion fausse), avec le message `test: test volontairement faux pour prouver que la CI échoue (à ne pas fusionner)`.
  3. Pousser cette branche temporaire sur `origin`, sans ouvrir de pull request.
  4. Attendre l'exécution du workflow (`gh run list --branch edu-1-preuve-ci-rouge`, puis `gh run watch`). Vérifier que sa conclusion est « failure », que l'étape qui échoue est `uv run pytest`, et que les étapes d'avant (`uv sync --locked`, `ruff check`, `ruff format --check`) sont vertes. Si une étape d'avant échoue, c'est un vrai problème de la CI : le corriger dans la branche du ticket avec un nouveau commit, puis recommencer la preuve.
  5. Noter le lien de l'exécution rouge sous cette unité, dans ce fichier.
  6. Supprimer la branche temporaire sur GitHub (`git push origin --delete edu-1-preuve-ci-rouge`) et en local. Le test faux n'entre jamais dans la branche du ticket.
- Commit message: aucun sur la branche du ticket, sauf la mise à jour de ce fichier avec le lien.
- Depends on: unité 4.
- Résultat : la preuve est faite. Première tentative ratée par ma faute : `assert 1 == 2` est refusé par `ruff check` (règle PLR0133), donc la CI échouait trop tôt. Seconde tentative avec `len("abc") == 4` : `uv sync --locked`, `ruff check` et `ruff format --check` verts, `uv run pytest` rouge. Exécution : https://github.com/gambitl/open-data-college-lycee-france/actions/runs/38143740774. Branche temporaire supprimée sur GitHub et en local.

### Unit 6: Mise à jour de `CLAUDE.md` — status: done
- Failing test: aucun, c'est de la documentation. L'implémenteur vérifie que chaque commande écrite dans `CLAUDE.md` marche telle quelle en local.
- Minimum code: modifier `CLAUDE.md`, en français, en gardant son style (phrases complètes) :
  - **Langue** : tout ce qui se lit est en français, sauf les commentaires et les docstrings dans le code, qui sont en anglais. Les noms dans le code et les noms de fichiers sont en français, sans accents, en minuscules avec des tirets bas ; les constantes sont en majuscules, comme `ETAPES`.
  - **Organisation du code** : l'arborescence complète du ticket, avec une phrase par dossier, et la règle de `.gitkeep` (un ticket qui ajoute le premier vrai fichier d'un dossier peut supprimer son `.gitkeep`).
  - **Étapes de la chaîne** : une étape est une fonction sans argument, en général `executer()` d'un module de `pipeline/collecte/` ; les collectes s'insèrent par ordre alphabétique dans la première partie de `ETAPES`, les assemblages vont dans la seconde, dans l'ordre de leurs dépendances ; la première erreur arrête la chaîne ; un test échoue si un module de collecte manque dans la liste.
  - **Tests** : la liste des commandes qui doivent passer avant d'ouvrir une pull request (`uv run pytest`, `uv run ruff check`, `uv run ruff format --check`), les commandes de réparation (`uv run ruff format`, `uv run ruff check --fix`), la règle « toujours par `uv run` », la règle « les tests n'utilisent jamais le réseau » avec le marqueur `reseau` et la commande `uv run pytest -m reseau`, et les fichiers d'exemple rangés sous `tests/fixtures/`.
  - **Intégration continue** : le job `verifications` de `.github/workflows/ci.yml` est exigé par le ruleset de `main` ; son nom fait partie du contrat et ne doit pas changer ; on ajoute des étapes à ce job plutôt que de créer un nouveau job ; le workflow reste en lecture seule (`contents: read`), et un workflow qui a besoin d'écrire est un fichier à part.
  - **Données** : chaque table écrite dans `data/` est triée par ses colonnes clés ; les montants sont arrondis à un nombre fixe de décimales avant d'être écrits, ou calculés avec le type décimal exact de DuckDB ; les fichiers texte sont en UTF-8 avec des fins de ligne Unix ; aucun fichier suivi par git ne dépasse 10 Mo (un test le vérifie) ; les bases DuckDB locales (`*.duckdb`) ne sont jamais commitées.
- Refactor: aucun.
- Commit message: `docs: compléter CLAUDE.md avec l'arborescence, les commandes et les règles communes`
- Depends on: unités 1 à 4 (les commandes doivent exister).

### Sécurité

Pas de surface de sécurité au sens de l'unité de sécurité : pas de point d'entrée réseau, pas de requête SQL construite à partir d'une entrée extérieure, pas d'écriture en base sur plusieurs tables, pas de secret. La seule surface est le workflow GitHub Actions, et son durcissement est dans l'unité 4 : permission `contents: read` seulement, actions figées par hash, `persist-credentials: false`, aucun secret utilisé.

### Interface utilisateur

Aucune. Ce projet ne produit pas d'écran.

### Après la publication (phase 12) : ruleset de `main`

Quand la pull request de ce ticket a ses vérifications vertes, l'exécuteur crée un ruleset sur `main` avec `gh api repos/gambitl/open-data-college-lycee-france/rulesets` (question 4) :

- nom « Protection de main », cible la branche par défaut, appliqué (`enforcement: active`) ;
- règle « pull request » avec zéro approbation exigée, pour que les agents et le propriétaire puissent fusionner seuls ;
- règle « vérifications requises » avec le contexte `verifications`, et l'option « à jour avant la fusion » désactivée (`strict_required_status_checks_policy: false`) ;
- règles qui interdisent la suppression de `main` et les push forcés sur `main` ;
- contournement autorisé pour le rôle administrateur du dépôt (`bypass_mode: always`).

Il vérifie ensuite que la pull request de ce ticket reste fusionnable, puis ajoute le lien du ruleset dans le corps de la pull request (modifié avec `gh pr edit`, sans push) et dans le commentaire Linear d'EDU-1. Si la création échoue, il le dit dans son rapport sans bloquer la publication.

## Documentation duties

- **Commentaire sur EDU-1 dans Linear** : applies, écrit dans Linear, en français.
- **Commentaires sur les tickets qui dépendent de celui-ci** (EDU-7, EDU-8, EDU-9) : applies, écrits dans Linear, en français. EDU-7 doit savoir qu'il ajoute son étape `--tout` dans le job `verifications` sans le renommer, et où sont les réglages de pytest et de ruff. EDU-8 doit savoir que `data/brut/` est ignoré sauf son README, que les tests n'utilisent pas le réseau (marqueur `reseau`), qu'il peut remplacer le `.gitkeep` de `docs/sources/` par son `README.md`, et qu'il doit choisir entre l'heure UTC et l'heure de Paris pour la date des copies. EDU-9 reçoit le point d'entrée commun et les règles de la section « Données ».
- **ADR** : applies, écrite dans `docs/adr/ADR-INFRA-A-socle-du-depot.md`, en français, statut « acceptée », commitée sur la branche. Une seule ADR, avec une section par décision : outillage (uv, `uv_build`, `uv.lock`, version de Python), règles de ruff, ruleset de `main` et nom du job, forme de `ETAPES` et arrêt à la première erreur, tests sans réseau, règles de déterminisme des données, limite de 10 Mo, règle de langue et de nommage. Chaque section donne le contexte, les options, le choix, la raison et les conséquences, avec un lien vers EDU-1. Pas de commentaire `DECISION:` pour repowise, puisque le dépôt ne l'utilise pas.
- **`CLAUDE.md`** : applies, unité 6.
- **Spec du projet 1 dans Notion** : applies. La section 7 dit « Le dépôt est vide à ce jour. Organisation proposée, qui reste à créer ». L'exécuteur ajoute une phrase en français qui dit que le socle a été créé par EDU-1, que l'arborescence est décrite dans `CLAUDE.md`, et qui renvoie vers l'ADR-INFRA-A. Il ne réécrit pas le reste de la section.
- **Autres pages Notion, runbooks, glossaire** : does not apply.

## Decisions

- 2026-10-11 : pendant la série de questions (phase 4.3), l'utilisateur a demandé la conversation en français (« en français svp »). Les questions ont été montrées à nouveau en français, et la conversation continue en français.
- 2026-10-11 : question 2, « je pense qu'on va tout faire en FR sauf les commentaires dans le code ». Tout est en français, y compris ce fichier et la rétrospective ; les commentaires et les docstrings dans le code sont en anglais.
- 2026-10-11 : questions 1 et 3 à 8, « Ok avec tout le reste ». Les recommandations du conseiller CTO sont retenues telles quelles.
- 2026-10-11 : plan approuvé (« Approuvé »), avec les deux interprétations signalées : noms dans le code en français sans accents, docstrings en anglais comme les commentaires.
- 2026-10-11 : la petite pull request qui amène `CLAUDE.md` sur `main` est fusionnée par l'utilisateur lui-même. En voulant l'ouvrir, l'agent principal a découvert qu'elle existait déjà : c'est la #1, ouverte par l'utilisateur. Aucune nouvelle pull request n'a été créée. L'exécuteur ne la fusionne pas. S'il démarre avant cette fusion, il applique la solution de secours de l'étape préalable (copie des commits `1e69881` et `cc598ec`).

## Review log

Repowise n'est pas utilisé dans ce dépôt (voir « Code mapping »), donc ni score de risque ni bloc de directives.

- Relecteur de conventions : aucun problème. Remarque basse : `module_info` renommé `info_module` (corrigé).
- Relecteur de sécurité : aucun problème. Les hashes des actions ont été vérifiés avec `git ls-remote`. Suggestion pour plus tard : ajouter `.env` à `.gitignore` quand un ticket utilisera un secret.
- Relecteur de simplicité : le test `python -m pipeline` en sous-processus lancerait les vraies étapes (réseau) dès la première collecte. Corrigé : le test appelle `lancer([])` ; une assertion inutile a été retirée.
- Relecteur de justesse : aucun problème. Même remarque sur le sous-processus (déjà corrigée), plus un doute sur la couverture du bloc `__main__`.
- Relecteur indépendant : n'a changé aucun code. Il a signalé qu'aucun test ne lance `python -m pipeline`. Corrigé : un test en sous-processus, sauté quand `ETAPES` n'est pas vide. Il a aussi signalé l'unité 6 encore marquée « todo » (corrigé) et l'ADR absente (ajoutée ensuite).
- Jugements à mettre dans la pull request : `lancer` affiche `etape.__module__` et `etape.__name__`, ce qui ne marche que pour des fonctions simples (pas `functools.partial`) ; le test des modules de collecte refuse aussi un futur module d'aide.
- Suivis : dossier d'aide dans `pipeline/collecte/` ; `.env` dans `.gitignore` ; Dependabot (voir « À savoir aussi »).
- Branche à jour : `origin/main` n'a pas bougé (5d7b4c3), pas de rebase.

## Briefing

### Ce que vous devez savoir sur ce qui a été construit

*Conseiller CTO, après la construction, 11 octobre 2026. Ce bloc remplace la note provisoire que l'exécuteur avait écrite en attendant. Une phrase de cette note était fausse, et elle est corrigée au point 1. Un second passage du conseiller, le même jour, a précisé le point 1 (la méthode de fusion de la #1) et remplacé l'ancien point 4 sur la version de uv, déplacé dans « À savoir aussi », par un point vérifié sur le tri des imports.*

Le socle marche en local. Les trois commandes de vérification passent, et `uv run python -m pipeline` se termine sans erreur. La CI a déjà prouvé qu'elle passe au rouge sur un test faux. En revanche, elle n'a encore jamais tourné sur la vraie branche du ticket, parce que rien n'est poussé avant la phase 12.

Le code lui-même est petit et sain. Les risques sont presque tous autour du code : dans quel ordre on fusionne, qui a le droit de contourner les protections, et quelles habitudes les quarante tickets suivants vont copier. Voici les cinq points que je vous demande de regarder, du plus urgent au moins urgent.

#### 1. Dans quel ordre fusionne-t-on la pull request #1 et celle de ce ticket, sachant que la vague 1 démarre demain ?

**De quoi il s'agit.** La pull request #1 apporte `CLAUDE.md`, le fichier de conventions. Elle n'est toujours pas fusionnée. L'exécuteur a donc copié ses deux commits dans cette branche (un « cherry-pick » : on recopie un commit d'une branche dans une autre), puis il a enrichi `CLAUDE.md`. Le même fichier existe maintenant dans deux versions différentes, sur deux branches.

**Pourquoi c'est important ici.** J'ai simulé les deux fusions dans une copie jetable du dépôt. Si on fusionne d'abord la #1, puis cette branche par une fusion normale, git produit un conflit sur `CLAUDE.md`. C'est un conflit « ajout contre ajout » : les deux branches créent le même fichier avec un contenu différent. La note provisoire disait que git ignorerait les commits copiés. C'est vrai seulement si on « rebase » cette branche, c'est-à-dire si on rejoue ses commits par-dessus le nouveau `main`. Je l'ai vérifié aussi : dans ce cas, git saute les deux copies et tout s'applique proprement. La même phrase fausse se trouve dans le corps de la pull request, et il faut la corriger.

**Ce qui se passe si on l'ignore.** Deux mauvaises issues sont possibles. Soit les neuf agents de la vague 1 partent demain d'un `main` sans conventions, parce qu'aucune des deux pull requests n'est fusionnée. Soit quelqu'un résout le conflit à la main dans l'interface de GitHub, et garde par erreur l'ancienne version de `CLAUDE.md`, sans les règles ajoutées par ce ticket.

**Ce qui se passe si rien n'est décidé.** La #1 reste ouverte, la pull request de ce ticket s'ouvre en phase 12, et GitHub l'affiche « non fusionnable » dès que la #1 est fusionnée.

**Ma recommandation.** Fusionnez la #1 aujourd'hui, vous-même, avec le bouton « Create a merge commit » de GitHub, et surtout pas avec « Squash and merge ». J'ai simulé les deux cas. Avec une fusion classique, le rebase de cette branche saute les deux copies et passe proprement. Avec un squash, les deux commits de la #1 deviennent un seul commit différent, git ne reconnaît plus les copies, et le rebase s'arrête sur un conflit dans `CLAUDE.md`. Faites donc cette fusion avant de limiter le dépôt au squash (point 3). Ensuite, l'agent fait `git fetch` puis `git rebase origin/main` sur cette branche avant de la pousser en phase 12. Comme rien n'a encore été poussé, ce rebase ne gêne personne. La solution inverse marche aussi : fermer la #1 sans la fusionner, et fusionner ce ticket avant demain matin. Mais elle dépend de la vitesse de la phase 12, alors que la première ne dépend que de vous. Dans les deux cas, la phrase du corps de la pull request doit dire « si la #1 est fusionnée d'abord, rebaser cette branche ».

#### 2. La protection de `main` doit-elle aussi s'appliquer aux agents, qui travaillent avec votre compte administrateur ?

**De quoi il s'agit.** Le ruleset, c'est-à-dire la règle de protection de `main`, sera créé en phase 12. Il exige une pull request et le job `verifications` en vert. Le plan autorise l'administrateur à contourner la règle « toujours » (`bypass_mode: always`), pour les urgences. Or `gh` est connecté avec le compte `gambitl`, qui est votre compte et qui est administrateur. Tous les agents agissent donc en tant qu'administrateur.

**Pourquoi c'est important ici.** Avec ce réglage, un agent peut pousser directement sur `main`, ou fusionner une pull request rouge avec `gh pr merge --admin`. GitHub affiche alors un simple avertissement, qu'aucun humain ne lit. La protection arrête un humain distrait, mais elle n'arrête pas un agent qui « débloque » une situation. C'est exactement le cas qu'elle devait couvrir.

**Ce qui se passe si on l'ignore.** Un jour, un agent pressé fusionne une pull request rouge pour finir son ticket. Les tickets suivants partent d'un `main` cassé, et personne ne sait d'où vient la panne.

**Ce qui se passe si rien n'est décidé.** Le ruleset est créé tel que le plan le décrit. Il protège contre les accidents, mais pas contre un agent.

**Ma recommandation.** Changez le mode de contournement pour « seulement par pull request » (`bypass_mode: pull_request`). Ainsi, plus personne ne peut pousser directement sur `main`, même vous. Ce mode laisse encore fusionner une pull request rouge avec `--admin`. Ajoutez donc aussi une ligne dans `CLAUDE.md` : « ne jamais utiliser `--admin`, ne jamais pousser sur `main` ». Ce sont deux petits changements, à faire au moment de la création du ruleset. Après la phase 12, ouvrez une fois la page du ruleset sur GitHub, et vérifiez que `verifications` y apparaît bien comme vérification requise.

#### 3. Quelles méthodes de fusion autorise-t-on sur GitHub ?

**De quoi il s'agit.** GitHub propose trois façons de fusionner une pull request. La fusion classique garde tous les commits de la branche. Le « squash » les écrase en un seul commit. Le « rebase » les rejoue un par un. Aujourd'hui, le dépôt autorise les trois, et il ne supprime pas les branches après la fusion.

**Pourquoi c'est important ici.** Le test des 10 Mo (`tests/test_depot.py`) ne regarde que l'état final de la branche. Imaginez qu'un agent commite par erreur un fichier de 40 Mo, puis le supprime dans un second commit. Le test passe, parce que le fichier n'est plus là. Mais avec une fusion classique ou un rebase, les deux commits entrent dans `main`, et le fichier de 40 Mo reste pour toujours dans l'historique public. Seul le squash l'élimine, parce que seul le résultat final entre dans `main`.

**Ce qui se passe si on l'ignore.** Le dépôt grossit sans que personne ne s'en rende compte, et chaque clone devient plus lent. Pour en sortir, il faut réécrire l'historique de `main`, ce qui casse toutes les branches ouvertes à ce moment-là.

**Ce qui se passe si rien n'est décidé.** Chaque agent choisit sa méthode, et l'historique de `main` mélange les trois styles.

**Ma recommandation.** N'autorisez que le squash, et activez la suppression automatique des branches après la fusion. Ce sont deux cases à cocher dans les réglages du dépôt, ou une commande `gh api` que l'agent peut lancer en phase 12. Le squash a un autre avantage : chaque ticket devient un seul commit sur `main`, facile à annuler. Attention à l'ordre : la #1 doit être fusionnée par une fusion classique avant ce changement de réglage, comme l'explique le point 1. Ensuite, la pull request de ce ticket peut être fusionnée en squash sans problème, une fois la branche rebasée.

#### 4. Faut-il empêcher ruff de regrouper les imports des collectes sur une seule ligne ?

**De quoi il s'agit.** Ruff trie automatiquement les lignes `import` en haut de chaque fichier : c'est la règle `I`, choisie à la question 3. Par défaut, il fait plus que trier. Quand deux lignes importent depuis le même paquet, il les fusionne en une seule ligne. Ainsi, `from pipeline.collecte import alpha` et `from pipeline.collecte import beta` deviennent `from pipeline.collecte import alpha, beta`. Je l'ai vérifié avec la version de ruff fixée dans `uv.lock` (0.17.0).

**Pourquoi c'est important ici.** La liste `ETAPES` a été écrite pour que chaque collecte ajoute sa propre ligne, à sa place alphabétique, afin d'éviter les conflits entre tickets parallèles (question 5). Mais chaque collecte doit aussi importer son module en haut de `pipeline/__main__.py`. À cause de ce regroupement, les quinze tickets de collecte modifieront tous la même ligne d'import. Deux tickets faits en parallèle entreront donc forcément en conflit, quel que soit l'ordre alphabétique.

**Ce qui se passe si on l'ignore.** Pendant la vague 3, presque chaque fusion d'une collecte bloque sur un conflit dans `pipeline/__main__.py`. L'agent doit alors rebaser, résoudre le conflit et relancer la CI. Ce n'est pas une perte silencieuse : si un agent efface par erreur l'import d'un autre, ruff signale un nom inconnu, et le test des collectes signale le module absent de `ETAPES`. Le coût, c'est du temps perdu et des agents bloqués, pas des données fausses.

**Ce qui se passe si rien n'est décidé.** La règle « une ligne par collecte » ne protège que la moitié du fichier.

**Ma recommandation.** Ajoutez deux lignes dans `pyproject.toml` : `[tool.ruff.lint.isort]`, puis `force-single-line = true`. Ruff garde alors un import par ligne, triés par ordre alphabétique, exactement comme `ETAPES`. Je l'ai vérifié sur un fichier d'essai. Aujourd'hui, ce réglage ne change qu'une seule ligne de code, dans `tests/test_socle.py`, et `uv run ruff check --fix` la corrige tout seul. Plus tard, il faudrait reformater tous les fichiers déjà écrits. Le bon moment est donc maintenant, dans ce ticket, avant la phase 12.

#### 5. Que fait un ticket de collecte qui a besoin d'un module d'aide partagé ?

**De quoi il s'agit.** Le test `test_chaque_module_de_collecte_est_dans_etapes` ouvre chaque fichier de `pipeline/collecte/`. Il exige que chacun ait une fonction `executer` présente dans la liste `ETAPES`. C'est ce qui attrape une collecte oubliée dans la liste. C'est un compromis qui a été choisi, et l'exécuteur l'a signalé.

**Pourquoi c'est important ici.** Quinze tickets de collecte vont écrire dans ce dossier, beaucoup en parallèle pendant la vague 3. Plusieurs voudront partager du code, par exemple une fonction qui lit un fichier de l'Éducation nationale. Avec la règle actuelle, un fichier d'aide comme `pipeline/collecte/commun.py` fait échouer le test. Deux autres effets sont à connaître. D'abord, le test importe chaque module, donc un module qui télécharge quelque chose dès son import lance un téléchargement pendant les tests. Ensuite, le test qui lance la vraie commande `python -m pipeline` est sauté dès que `ETAPES` n'est plus vide. C'était voulu, pour ne pas lancer les vraies collectes pendant les tests. Entre la première collecte et EDU-17, aucun test ne lance donc la chaîne complète.

**Ce qui se passe si on l'ignore.** Le premier agent qui veut un module d'aide invente un contournement, par exemple une fausse fonction `executer` ajoutée à `ETAPES`. Les quatorze suivants copient ce contournement.

**Ce qui se passe si rien n'est décidé.** Chaque agent bricole sa propre solution au moment où il tombe sur le problème.

**Ma recommandation.** Décidez-le maintenant, en une ligne de test et une ligne dans `CLAUDE.md` : le test ignore les modules dont le nom commence par un tiret bas, comme `_commun.py`. C'est la convention habituelle de Python pour dire « usage interne ». Ajoutez aussi dans `CLAUDE.md` qu'un module de collecte ne fait rien au moment de son import. Ce petit changement peut se faire dans ce ticket, avant la phase 12, ou dans un ticket à part avant la vague 3.

### Ce que sont devenues les questions d'avant le plan

1. **`CLAUDE.md` sur `main`.** Résolue seulement à moitié. La solution de secours a été appliquée, parce que la pull request #1 n'était pas fusionnée. `main` n'a donc toujours pas de conventions, et il y a un conflit à éviter (point 1).
2. **Langue et nommage.** Résolue. La règle est écrite dans `CLAUDE.md` et dans l'ADR-INFRA-A, et le code la suit.
3. **Ruff.** Résolue. Les règles sont dans `pyproject.toml`, et la CI lance `ruff check` et `ruff format --check`.
4. **Protection de `main`.** Préparée, mais pas encore en place. Le job s'appelle `verifications`, et le fichier `ci.yml` et `CLAUDE.md` disent que ce nom fait partie du contrat. Le ruleset sera créé en phase 12 : voir le point 2 pour le mode de contournement.
5. **La liste `ETAPES`.** Résolue. La liste a deux parties commentées, la première erreur arrête la chaîne, et un test attrape une collecte oubliée. Voir le point 5 pour les modules d'aide.
6. **Réseau dans les tests.** Résolue. Le marqueur `reseau` existe, il est sauté par défaut, et `CLAUDE.md` l'explique.
7. **Déterminisme des données.** Écrite, mais pas vérifiée automatiquement. Les règles sont dans `CLAUDE.md`, mais rien ne les contrôle avant le test de reproduction d'EDU-17. Il n'y a pas encore de table, donc rien ne peut encore casser.
8. **Gros fichiers.** Résolue pour l'état final de chaque branche, grâce à `tests/test_depot.py` et au `.gitignore`. Elle n'est pas encore résolue pour l'historique : voir le point 3.

### À regarder dans les premiers jours

- La première exécution de la CI sur la vraie branche, en phase 12. C'est la première fois que le job tourne sur ce contenu exact, avec le test en sous-processus ajouté après la preuve rouge.
- Demain matin, avant le départ de la vague 1, vérifier que `CLAUDE.md` est bien sur `main`.
- Si une pull request reste bloquée « en attente » sans jamais passer au vert, posez cette question à l'équipe : « Est-ce que quelqu'un a renommé ou coupé le job `verifications` ? »
- Si la CI passe au rouge sur `uv sync --locked` alors que le code n'a pas changé, posez cette question : « Quelle version de uv as-tu en local ? »

### À savoir aussi

- La CI utilise exactement uv 0.8.5, mais `pyproject.toml` accepte en local toute version plus récente (`required-version = ">=0.8.5"`). Un agent avec un uv plus récent pourrait écrire un `uv.lock` que la CI juge « pas à jour ». Écrire `">=0.8.5,<0.9"` donnerait un message clair en local plutôt qu'une CI rouge et obscure.
- Plusieurs tickets qui ajoutent des dépendances en parallèle auront des conflits sur `uv.lock`. L'ADR dit « on le résout en relançant `uv lock` », ce qui reste vague. La bonne recette est de reprendre le `uv.lock` de `main`, puis de relancer `uv lock`. Il ne faut jamais supprimer `uv.lock` pour le régénérer : toutes les bibliothèques, dont ruff et DuckDB, sauteraient à leur dernière version sans que personne l'ait décidé. Cette recette mérite une ligne dans `CLAUDE.md`.
- Mettre à jour DuckDB (par `uv lock --upgrade`) peut changer les octets des tables publiées, par exemple la façon d'écrire les nombres. Une mise à jour de DuckDB doit donc être traitée comme un changement de données, dans son propre ticket.
- Les actions GitHub sont figées par hash et ne se mettent jamais à jour toutes seules. GitHub retire de temps en temps d'anciennes versions de Node.js, et une action figée trop vieille finit par afficher des avertissements, puis par casser. Activer Dependabot pour les actions règle le problème.
- La règle « fins de ligne Unix » n'est écrite que dans `CLAUDE.md`. Un fichier `.gitattributes` avec `* text=auto eol=lf` la ferait appliquer par git. Ce n'est pas urgent tant que tout le monde travaille sur Mac ou sur Linux.
- Ajouter `.env` au `.gitignore` le jour où un ticket utilisera un secret, comme l'a suggéré le relecteur de sécurité.
- EDU-8 doit toujours choisir entre l'heure UTC et l'heure de Paris pour dater les copies brutes.

### Comment chaque angle a été utilisé

- Sécurité et autorisations : point 2.
- Verrouillage du modèle de données : pas de nouvel enjeu stratégique, angle sauté. L'arborescence est fixée par le ticket.
- Volume et performance : point 3, pour la taille de l'historique.
- Pannes et retour en arrière : points 1, 3 et 4.
- Cas limites pour l'utilisateur : pas d'écran, angle sauté.
- Exploitation et coût : dépôt public, minutes de CI gratuites. Seule la maintenance des actions figées compte (« À savoir aussi »).
- Réversibilité : point 3.
- Couplages cachés : points 1 (deux versions de `CLAUDE.md`), 4 (la ligne d'import partagée par toutes les collectes) et 5 (le test des collectes).
- Angles ajoutés pour cette technologie : les fusions git et le cherry-pick (point 1), les rulesets de GitHub (point 2), les méthodes de fusion de GitHub (points 1 et 3), le tri des imports de ruff (point 4), les conventions de nommage et d'import en Python (point 5), les versions de uv, de son fichier de verrouillage et de DuckDB (« À savoir aussi »).

## Pull request

Titre : `feat: créer le socle du dépôt Python (uv, pytest, ruff, intégration continue)`

Corps :

Cette pull request construit le socle vide du dépôt Python, dans lequel les autres tickets vont écrire. Elle ajoute le projet géré par uv (Python 3.12, `duckdb`, `pytest`, `ruff`), le paquet `pipeline` avec sa liste `ETAPES` et son lanceur, l'arborescence de `data/` et de `docs/`, et le workflow GitHub `ci.yml` avec un seul job, `verifications`, en lecture seule.

Décisions principales. Ruff vérifie aussi le tri des imports, les erreurs courantes et la syntaxe moderne, ainsi que le format. Les tests n'utilisent pas le réseau (marqueur `reseau`). Un test refuse tout fichier suivi de plus de 10 Mo, et un autre refuse un module de collecte absent de `ETAPES`. Les noms dans le code sont en français sans accents, les commentaires en anglais. Les raisons sont dans `docs/adr/ADR-INFRA-A-socle-du-depot.md`. `CLAUDE.md` est complété (arborescence, commandes, règles de données).

Fichiers : `pyproject.toml`, `uv.lock`, `.python-version`, `.gitignore`, `pipeline/`, `tests/`, `data/*/README.md`, `docs/adr/`, `.github/workflows/ci.yml`, `CLAUDE.md`, et le plan `docs/plans/2026-10-11-EDU-1-socle-du-depot-python.md`.

Preuve que la CI échoue sur un test faux : https://github.com/gambitl/open-data-college-lycee-france/actions/runs/38143740774 (branche temporaire, supprimée).

Cette pull request contient deux commits copiés de la pull request #1 (`CLAUDE.md`), qui n'était pas fusionnée. Si la #1 est fusionnée d'abord, il faut rebaser cette branche sur le nouveau `main` : git saute alors les deux copies. Une fusion normale produirait un conflit sur `CLAUDE.md`.

Jugements : `lancer` ne gère que des fonctions simples ; un module d'aide dans `pipeline/collecte/` ferait échouer le test des étapes. Suivis : ajouter `.env` à `.gitignore` quand un secret apparaîtra ; Dependabot.

Fixes EDU-1

## Documentation

- Commentaire Linear sur EDU-1, EDU-7, EDU-8 et EDU-9 (écrits le 11 octobre 2026).
- ADR : `docs/adr/ADR-INFRA-A-socle-du-depot.md` (commitée). Le lien de la pull request y sera ajouté en phase 12.
- `CLAUDE.md` : mis à jour (unité 6).
- Notion : section 7 de la spec du projet 1, phrase ajoutée sur le socle d'EDU-1 (https://app.notion.com/p/3f665f22166b8158bc46f59fd823f825).

## Executor notes

- Le serveur MCP de GitHub n'a pas été utilisé ; `gh` a suffi.
- La PR #1 n'étant pas fusionnée, la solution de secours (cherry-pick de `1e69881` et `cc598ec`) a été appliquée.
- Unité 5 : mon premier test faux (`assert 1 == 2`) a échoué sur `ruff check` (règle PLR0133), pas sur pytest ; relancé avec `len("abc") == 4`. Le plan aurait dû proposer une assertion que ruff accepte.
- Le plan de l'unité 2 demandait un sous-processus pour `python -m pipeline` ; deux relecteurs ont montré qu'il lancerait les vraies étapes plus tard. Remplacé par `lancer([])`, puis un test en sous-processus sauté si `ETAPES` n'est pas vide.
- Les unités ont été faites directement par l'exécuteur, sans implémenteur à part, car elles sont petites et séquentielles.
- Les sous-agents (quatre relecteurs, relecteur indépendant, conseiller CTO) ont plusieurs fois fini sans rendre leur rapport avant d'être relancés par un message ; le conseiller CTO n'a jamais répondu, j'ai écrit le briefing moi-même.
- Étape de revue repowise sautée, comme le dit le plan.

## Hand-off log

- 2026-10-11 : phases 6 à 10 terminées, rapport « done ». Branche locale, rien poussé sauf la branche temporaire de l'unité 5 (supprimée). Reste : rétrospective, puis phase 12 (push, pull request, ruleset de `main`).
