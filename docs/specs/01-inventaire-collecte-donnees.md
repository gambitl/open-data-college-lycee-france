# Inventaire et collecte des données de dépenses

*Projet 1 sur 4 du projet global « Dépense publique par élève, établissement par établissement ». Les autres specs se trouvent dans le même dossier : [index](README.md).*

## 1. Contexte et problème

En pleine mobilisation étudiante, la parole gouvernementale répète que « ce n'est pas un problème de moyens ». Pourtant, personne n'a jamais publié combien l'argent public dépense pour un élève, établissement par établissement. Le ministère ne publie que des moyennes nationales. En 2024, la dépense moyenne était de 10 450 € par collégien, 13 020 € par lycéen en voie générale ou technologique et 14 700 € par lycéen en voie professionnelle (DEPP, *Repères et références statistiques 2026*, chapitre 10). Les travaux les plus proches comptent des postes ou des heures d'enseignement par élève, mais jamais des euros : une étude de France Stratégie en 2017 et une enquête de Franceinfo en 2024.

Le projet global estime la dépense publique par élève de chaque collège et de chaque lycée public et privé sous contrat de France, outre-mer compris, pour la rentrée 2024. Il la publie sur un site pensé d'abord pour le téléphone, avec une carte, une fiche par établissement et des comparaisons. Le but est de rendre visibles les inégalités de moyens entre établissements, auprès du plus grand nombre de personnes possible. La question à laquelle le site répond est : « Combien dépense-t-on pour moi, par rapport à la moyenne nationale, à l'académie où l'on dépense le plus et à l'établissement où l'on dépense le plus ? »

Le travail est découpé en quatre projets qui avancent en parallèle : l'inventaire et la collecte des données, le modèle de coût et les statistiques, le site interactif, et la publication et la diffusion. Des formats de données figés dès le 14 octobre 2026 permettent ce parallélisme. La première version publique est prévue le 15 novembre 2026.

Le projet a aussi un objectif secondaire : monter en compétence sur une architecture JavaScript moderne, avec un front en React et un back en Node.js. Cet objectif explique certains choix techniques. Il ne doit jamais dégrader l'objectif principal, qui est un site rapide, lisible et crédible.

Le principe de méthode qui traverse les quatre projets est simple. On ne calcule jamais le montant total nous-mêmes : on part des totaux officiels publiés (budget de l'État, comptes des collectivités, chiffres de la DEPP) et on les répartit au plus juste entre les établissements. Personne ne peut alors dire qu'on a inventé des montants. Notre apport, c'est la répartition.

**Ce que fait ce projet-ci.** C'est la fondation des trois autres. Il recense toutes les dépenses publiques d'un collège ou d'un lycée et trouve, pour chacune, la meilleure source ouverte. Il construit ensuite les tables dont le modèle de coût a besoin. Il garantit aussi la transparence et la fraîcheur des données : chaque chiffre publié doit pouvoir être relié à une source datée, et le projet doit savoir tout seul quand une source change.

Une recherche préalable a établi un fait important : **aucune base ouverte ne donne la dépense réelle de chaque établissement.** Le ministère collecte bien les comptes financiers des établissements, mais il ne les publie pas. Et même complets, ces comptes ne contiendraient ni les salaires des enseignants, ni ceux des agents des collectivités, ni les gros travaux.

En revanche, un jeu de données officiel change la donne : « Les personnels dans les établissements du second degré ». Pour 10 697 établissements publics et privés à la rentrée 2024, il donne le nombre d'enseignants en ETP, ventilé par corps et par tranche d'âge. Les salaires suivent une grille officielle très précise, donc on peut en déduire une estimation solide de la masse salariale des enseignants, qui est la plus grosse part du coût d'un élève. Dans le public, en 2024, l'État paie 73 % de la dépense, les collectivités 22 % et les familles environ 4 %.

La part des collectivités est beaucoup moins bien connue. Elle n'est publiée établissement par établissement qu'en Centre-Val de Loire et en Île-de-France. Ailleurs, on ne connaît que le total dépensé par chaque département et chaque région.

## 2. Mesures de succès

1. Chaque ligne de l'inventaire des dépenses a un payeur, une source (ou la mention « pas de source ouverte »), une couverture, une année et une décision de traitement.
2. La table de référence contient au moins 95 % des établissements du jeu de données sur le personnel, avec un nombre d'élèves et une position géographique. Les établissements manquants sont listés avec la raison.
3. Relancer la chaîne de données à partir des copies datées des sources reproduit exactement les mêmes tables.
4. Chaque source utilisée figure dans le manifeste. Un changement de source est détecté en moins d'une semaine.

Ces mesures servent la mesure de succès globale : une estimation pour au moins 90 % des collèges et lycées publics et privés sous contrat.

## 3. Personas

**L'élève mobilisé (persona principal).** C'est un collégien, un lycéen, ou un étudiant qui pense à son ancien lycée. Il découvre le site par un lien partagé sur Instagram, WhatsApp ou TikTok, depuis son téléphone. Il veut savoir en quelques secondes combien on dépense pour lui, comparé aux autres, puis partager ce chiffre. Il ne lira pas la méthode, mais il doit pouvoir la trouver en un clic.

**Le journaliste.** C'est un journaliste, un vérificateur ou un chercheur. Il cherche les plus gros écarts pour écrire un article. Il vérifie la méthode avant de citer un chiffre, et il télécharge les données pour faire ses propres calculs. Il a besoin de sources, de numéros de version et d'un moyen de signaler une erreur.

**Le mainteneur.** C'est le porteur du projet et les agents de code qui travaillent pour lui. Il a besoin d'une chaîne de données reproductible, de formats figés entre les projets, et d'être prévenu automatiquement quand une source change.

Les parents qui choisissent un établissement ne sont pas un persona du projet. Ils choisissent rarement leur établissement, à cause de la carte scolaire, et le coût par élève ne les aiderait pas à décider.

Dans ce projet, le persona principal est le mainteneur. Le journaliste est servi par le manifeste des sources et la surveillance des sources.

## 4. User stories

### US-1 : Inventaire des dépenses et des sources

En tant que mainteneur, je veux un inventaire de toutes les lignes de dépense publique d'un collège ou d'un lycée, avec qui paie, la source disponible et la décision de traitement, afin que le modèle de coût sache exactement quoi calculer et que la méthode publiée soit complète.

- AC1 : l'inventaire couvre au minimum les treize lignes du tableau de départ (section 7). Chaque ligne a un payeur, une source avec son lien ou la mention « pas de source ouverte », une couverture géographique et une année. Elle a aussi une décision parmi quatre : calculée par établissement, moyenne du territoire appliquée, exclue, ou reportée à la deuxième version.
- AC2 : le découpage officiel du coût d'un élève est retrouvé. Il s'agit des montants par niveau d'enseignement des programmes budgétaires de l'État 141 (public) et 139 (privé sous contrat), et du découpage de la DEPP par financeur. La somme des montants retrouvés recoupe les totaux publiés à 1 % près.
- AC3 : chaque décision « exclue » ou « reportée » est justifiée par une phrase, reprise ensuite dans la note de méthode du projet 2.

### US-2 : Format des tables livrées au modèle de coût

En tant que mainteneur, je veux un format figé et documenté pour chaque table que ce projet livre, afin que le projet de modèle de coût puisse coder en parallèle sur des données fictives.

- AC1 : chaque table a un schéma écrit, avec ses colonnes, leurs types, leurs unités, les valeurs manquantes autorisées et sa clé (l'UAI).
- AC2 : un script valide une table contre son schéma. Il échoue avec un message clair si une colonne manque ou change de type.
- AC3 : après le 14 octobre, toute modification du format change son numéro de version et laisse une note dans le journal des changements.

### US-3 : Table de référence des établissements

En tant que mainteneur, je veux une table unique de tous les collèges et lycées publics et privés sous contrat à la rentrée 2024, afin que les calculs et le site partagent exactement la même liste d'établissements.

- AC1 : chaque ligne a l'UAI, le nom, le type (collège, lycée général et technologique, lycée professionnel, lycée polyvalent), le secteur (public ou privé sous contrat), la commune, le département, l'académie, la région et la position GPS. Elle a aussi le nombre d'élèves de la rentrée 2024, l'IPS et le classement en éducation prioritaire.
- AC2 : au moins 95 % des établissements du jeu de données sur le personnel sont présents avec un nombre d'élèves non nul. La liste des absents est publiée avec la raison de chaque absence.
- AC3 : le privé hors contrat, les écoles primaires et les lycées agricoles sont absents de la table.
- AC4 : les élèves d'un lycée polyvalent sont la somme de ses effectifs généraux, technologiques et professionnels, sans double compte.
- AC5 : la table est livrée avec les contours des régions et des départements et la position de chaque commune (IGN Admin Express, licence ouverte). La carte à plusieurs niveaux de zoom en a besoin.

### US-4 : Cités scolaires et classes post-bac

En tant que journaliste, je veux que les établissements avec des classes post-bac ou en cité scolaire soient repérés, et que leurs étudiants soient comptés, afin que leur coût par élève ne soit pas artificiellement gonflé.

- AC1 : chaque établissement porte deux marqueurs, « classes post-bac » et « cité scolaire ».
- AC2 : le nombre d'étudiants en classes post-bac (CPGE et BTS) de chaque lycée concerné est collecté depuis une source ouverte, Parcoursup ou les données de l'enseignement supérieur (à confirmer). Il est ajouté au nombre d'élèves pris en compte pour le calcul.
- AC3 : pour les cités scolaires, la règle qui répartit le personnel partagé entre le collège et le lycée est écrite et justifiée.

Le porteur note que ces établissements sont souvent bien, voire très bien dotés. La correction réduira leur coût apparent, mais elle le rendra honnête.

### US-5 : Enseignants et coût employeur

En tant que mainteneur, je veux connaître, pour chaque établissement, les ETP d'enseignants par corps et par tranche d'âge, ainsi que le coût employeur moyen correspondant, afin d'estimer la masse salariale des enseignants.

- AC1 : les ETP viennent du jeu « Les personnels dans les établissements du second degré », rentrée 2024. Pour le public, les heures d'enseignement par élève du jeu « Indicateurs d'encadrement » sont jointes pour servir de contrôle.
- AC2 : le coût employeur annuel moyen est donné pour chaque corps et chaque tranche d'âge. Il est donné avec et sans la contribution retraite de l'État, et séparément pour le public (régime des fonctionnaires) et pour le privé sous contrat (régime général). Chaque valeur cite sa source : grilles de salaire, notes de la DEPP sur les salaires des enseignants.
- AC3 : les valeurs masquées par le secret statistique sont marquées comme manquantes. Elles ne sont jamais remplacées par zéro.
- AC4 (négatif) : aucune table ne permet de déduire le salaire d'une personne identifiable. On ne publie jamais de coût par enseignant pour un établissement.
- AC5 : la liste des établissements REP et REP+ et le montant des primes correspondantes sont collectés, pour que le modèle les ajoute là où elles s'appliquent.

### US-6 : Dépenses des collectivités et forfaits d'externat

En tant que mainteneur, je veux la dépense de fonctionnement de chaque département pour ses collèges et de chaque région pour ses lycées, ainsi que le forfait d'externat par élève versé au privé sous contrat, afin de calculer la part collectivité.

- AC1 : un total de fonctionnement est disponible pour chaque collectivité qui finance des collèges ou des lycées. Cela inclut la Métropole de Lyon, Paris, la Corse et les collectivités d'outre-mer. La source est celle des comptes publics des collectivités (balances de la DGFiP, base de l'OFGL).
- AC2 : le forfait d'externat, avec ses parts matériel et personnel, est collecté pour chaque collectivité, avec le lien vers la délibération et l'année.
- AC3 : quand le forfait est introuvable, on utilise la valeur de repli, c'est-à-dire le coût moyen de fonctionnement d'un élève du public de la même collectivité. Elle est marquée comme telle.
- AC4 : les montants mesurés lycée par lycée en Centre-Val de Loire et en Île-de-France sont collectés et rattachés par UAI, y compris les subventions aux lycées privés en Île-de-France.

### US-7 : Manifeste des sources et copies datées

En tant que journaliste, je veux la liste de toutes les sources utilisées, avec leur lien, leur licence et leur date de téléchargement, afin de pouvoir vérifier n'importe quel chiffre.

- AC1 : chaque fichier lu par la chaîne de données figure dans le manifeste, avec son nom, son producteur, son lien, sa licence, sa date de téléchargement et son empreinte de contrôle.
- AC2 : une copie datée de chaque fichier brut est conservée hors de l'historique git, par exemple dans une release GitHub. La chaîne de données peut tourner entièrement à partir de ces copies.
- AC3 : le manifeste est publié avec le fichier agrégé.

### US-8 : Surveillance automatique des sources

En tant que mainteneur, je veux être prévenu automatiquement quand une source change ou disparaît, afin que les données publiées restent fraîches et que rien ne change sans que je le sache.

- AC1 : une tâche planifiée tourne chaque semaine. Elle vérifie chaque source du manifeste (date de mise à jour, empreinte, colonnes) et ouvre un ticket GitHub quand une source change, disparaît ou change de colonnes.
- AC2 : si la tâche elle-même échoue, elle ouvre aussi un ticket.

### US-9 : Données de travaux (deuxième version)

En tant que mainteneur, je veux les montants de travaux rattachés à chaque établissement depuis 2019 environ, et la liste des établissements protégés au titre des monuments historiques, afin de construire l'indicateur travaux.

- AC1 : on prend les marchés publics (données essentielles de la commande publique) dont l'acheteur est un département ou une région et dont l'objet cite un établissement. Ils sont rattachés à son UAI. La précision de ce rattachement est mesurée sur un échantillon de 100 marchés vérifiés à la main.
- AC2 : les données de travaux du Centre-Val de Loire et de l'Île-de-France sont intégrées.
- AC3 : les établissements protégés au titre des monuments historiques sont repérés grâce à la base Mérimée du ministère de la Culture.
- AC4 : la couverture obtenue, c'est-à-dire la part des établissements qui ont des montants, est mesurée et publiée.

## 5. Périmètre

**Dans le périmètre :**
1. L'inventaire des dépenses et des sources, avec une décision pour chaque ligne.
2. Le format figé des tables livrées au projet 2.
3. La table de référence des établissements, avec la géographie nécessaire à la carte.
4. Le repérage des cités scolaires et des classes post-bac, et le comptage des étudiants post-bac.
5. Les enseignants par corps et par âge, et leur coût employeur, public et privé, avec et sans retraite.
6. Les dépenses des collectivités et les forfaits d'externat.
7. Le manifeste des sources et les copies datées.
8. La surveillance automatique des sources.
9. Les données de travaux, pour la deuxième version.

**Hors périmètre :**
1. Plusieurs années scolaires. Seule la rentrée 2024 est couverte, parce que c'est la seule année disponible pour les données sur le personnel.
2. Le privé hors contrat, qui ne reçoit pas d'argent public.
3. Les écoles primaires.
4. Les lycées agricoles, qui dépendent du ministère de l'Agriculture.
5. Les dépenses des familles (cantine, internat, frais de scolarité du privé).
6. Les travaux réalisés avant 2019 environ. Il n'existe pas de données numériques ouvertes sur cette période, établissement par établissement.

## 6. Jalons et enchaînement

**Jalon 1 : Inventaire des dépenses et des sources, le 14 octobre 2026.** C'est le jalon fondateur. Il porte US-1 et US-2. Il bloque le format du fichier agrégé et le modèle de coût du projet 2.

**Jalon 2 : Table de référence des établissements, le 17 octobre 2026.** Il porte US-3, US-4 et US-7. Il alimente le modèle de coût du projet 2 et la carte du projet 3, qui a besoin de la géographie.

**Jalon 3 : Données de coût, le 21 octobre 2026.** Il porte US-5, US-6 et US-8. Il alimente le modèle de coût du projet 2, qui doit être recalé sur les vraies données le 28 octobre.

**Jalon 4 : Données de travaux (deuxième version), le 13 décembre 2026.** Il porte US-9. Il alimente l'indicateur travaux du projet 2.

Les jalons 2 et 3 peuvent avancer en parallèle dès que le jalon 1 a figé les formats. À l'intérieur du jalon 3, la collecte des forfaits d'externat est le chantier le plus risqué, parce qu'elle se fait en partie à la main dans des PDF. S'il prend du retard, la valeur de repli permet au projet 2 d'avancer.

## 7. Où en est-on et contexte technique

**État du dépôt.** Le dépôt est vide à ce jour. Organisation proposée, qui reste à créer :
- `pipeline/` : la chaîne de données en Python. Python lit et nettoie les sources. DuckDB, une base de données qui tient dans un simple fichier, fait les jointures et les calculs en SQL.
- `data/` : le fichier agrégé et le manifeste des sources, publiés dans le dépôt.
- Les copies brutes des sources sont conservées dans des releases GitHub, pas dans l'historique git, à cause de leur taille.

**Tableau de départ de l'inventaire.** Ce tableau a été établi pendant le cadrage. US-1 doit le compléter et le sourcer.

| Dépense | Qui paie | Varie selon l'établissement ? | Donnée ouverte par établissement ? |
|---|---|---|---|
| Salaires des enseignants (salaire de base et cotisations, dont la retraite) | État | Oui, fortement | Indirecte : nombre d'enseignants par corps et par âge, puis la grille de salaire |
| Primes et heures supplémentaires (REP et REP+, pacte enseignant) | État | Oui | Partielle : la liste des REP et REP+ est publique, les heures supplémentaires non |
| Vie scolaire (conseillers principaux d'éducation, assistants d'éducation) | État | Oui | Oui, en ETP |
| Direction, gestion, santé (proviseur, gestionnaire, infirmière, psychologue) | État | Un peu | Probablement dans l'ETP total, à vérifier |
| Accompagnants des élèves en situation de handicap (AESH) | État | Oui | Non, à chercher |
| Bourses et fonds sociaux | État | Oui, selon le profil social | À chercher |
| Agents techniques (cantine, ménage, entretien, accueil) | Département ou région | Oui | Non, sauf exception |
| Dotation de fonctionnement (chauffage, énergie, fournitures) | Département ou région | Oui | Centre-Val de Loire seulement, plus quelques PDF |
| Travaux et investissement (construction, rénovation, patrimoine) | Département ou région | Énormément, et de façon irrégulière | Centre-Val de Loire et Île-de-France, le reste à chercher |
| Équipement (ordinateurs, manuels scolaires) | Surtout la région | Peu | Non |
| Transport scolaire, aide à la cantine | Région ou département | Plutôt par élève | Non |
| Privé : forfait d'externat (fonctionnement et personnel non enseignant) | Département ou région | Montant fixé par élève | Dans les délibérations, souvent en PDF |
| Privé : subventions d'investissement | Collectivités | Oui | Île-de-France seulement |

**Sources déjà identifiées.**
- Personnel par établissement : [Les personnels dans les établissements du second degré](https://data.education.gouv.fr/explore/dataset/fr-en-indicateurs_personnels_etablissements2d/), rentrée 2024, 10 697 établissements. Les colonnes ont été vérifiées : ETP total, vie scolaire, enseignants, agrégés, certifiés, PLP, autres titulaires, non titulaires, trois tranches d'âge (moins de 35 ans, 35 à 50 ans, 50 ans ou plus) et ancienneté dans l'établissement. Les valeurs inférieures à 5 ETP sont masquées. Pour le privé, seuls les enseignants sont présents.
- Heures d'enseignement par élève dans le public : [Indicateurs d'encadrement](https://data.education.gouv.fr/explore/dataset/fr-en-moyens_enseignants_2d_public/), rentrées 2023 à 2025.
- Annuaire et géolocalisation : `fr-en-annuaire-education` et `fr-en-adresse-et-geolocalisation-etablissements-premier-et-second-degre` sur data.education.gouv.fr.
- Effectifs d'élèves : `fr-en-college-effectifs-niveau-sexe-lv`, `fr-en-lycee_gt-effectifs-niveau-sexe-lv` et `fr-en-lycee_pro-effectifs-niveau-sexe-lv`, rentrées 2019 à 2025.
- IPS : `fr-en-ips-colleges-ap2023` et les jeux équivalents pour les lycées.
- Coûts moyens et financeurs : [DEPP, RERS 2026, chapitre 10](https://www.education.gouv.fr/sites/default/files/document/10-budget-couts-et-financementpdf-519303.pdf) et la note DEPP 26.42 (données provisoires 2025).
- Salaires moyens par corps : [note DEPP 26.36](https://www.education.gouv.fr/depp/l-evolution-du-salaire-des-enseignants-fonctionnaires-ou-assimiles-entre-2023-et-2024-505401).
- Comptes des collectivités : [balances comptables de la DGFiP](https://www.data.gouv.fr/datasets/balances-comptables-des-collectivites-et-des-etablissements-publics-locaux-avec-la-presentation-croisee-nature-fonction-2024) et [base fonctionnelle de l'OFGL](https://data.ofgl.fr/explore/dataset/ofgl-base-departements-fonctionnelle/).
- Données régionales par lycée : [dotations du Centre-Val de Loire](https://www.data.gouv.fr/datasets/dotations-de-fonctionnement-versees-aux-lycees-de-la-region-centre-val-de-loire-en-2025) (une publication par année depuis 2017), [subventions votées en Île-de-France](https://www.data.gouv.fr/datasets/donnees-budgetaires-des-lycees-subventions-votees) et [opérations directes votées en Île-de-France](https://www.data.gouv.fr/datasets/donnees-budgetaires-des-lycees-operations-directes-votees) (2021 à 2023, montants votés et non payés).
- Pour la deuxième version : les données essentielles de la commande publique sur data.gouv.fr, et la base Mérimée des monuments historiques.

**Dépendances.** Ce projet ne dépend d'aucun autre. Les projets 2 et 3 dépendent de lui.

## 8. Fiches de design

Pas d'écran : ce projet ne produit que des données.

## 9. Questions ouvertes et décisions d'architecture

**Questions ouvertes**
1. **Les valeurs masquées par le secret statistique.** Par défaut, elles sont marquées comme manquantes et l'établissement reçoit le marqueur « estimation partielle ». *Recommandation :* pour le public, estimer les valeurs manquantes à partir des heures d'enseignement par élève, et signaler l'estimation.
2. **La précision de l'âge comme approximation de l'échelon.** Par défaut, on associe chaque tranche d'âge à un salaire moyen par corps. *Recommandation :* mesurer la sensibilité du résultat, en comparant pour le public avec une estimation fondée sur les heures d'enseignement.
3. **La source des étudiants post-bac.** Les effectifs réels de l'enseignement supérieur sont meilleurs que les capacités d'accueil de Parcoursup. *Recommandation :* utiliser les effectifs réels s'ils sont publiés par établissement, et les capacités de Parcoursup en solution de repli.
4. **La couverture en outre-mer**, en particulier à Mayotte. Par défaut, on prend tout ce qui existe et on liste les manques. *Recommandation :* garder ce comportement par défaut et publier la liste des manques.
5. **Les heures supplémentaires et le pacte enseignant**, qui n'ont pas de données par établissement. Par défaut, ils sont répartis par le coefficient de recalage. *Recommandation :* accepter ce choix et le documenter dans la note de méthode.
6. **Le type des lycées polyvalents** dans les comparaisons. Par défaut, ils forment un type à part. *Recommandation :* trancher au jalon 1, avec le projet 2.

**Décisions d'architecture à créer** (dans `docs/adr/`)
- **ADR-DATA-A : conserver une copie datée des sources brutes.** Où la stocker, sous quel nom, et comment la chaîne choisit entre la source en ligne et la copie. Statut : à créer.
- **ADR-DATA-B : utiliser l'âge comme approximation de l'échelon.** Quelle correspondance entre tranche d'âge et salaire moyen, avec quelle source. Statut : à créer.
- **ADR-DATA-C : rattacher les marchés publics aux établissements** (deuxième version). Méthode de correspondance entre l'objet du marché et l'établissement. Statut : à créer.

## 10. Choix contestés

Les choix suivants concernent le projet global. Ils sont repris dans chacune des quatre specs.

- **Comparer à l'établissement qui dépense le plus.** L'agent a objecté que le maximum sera presque toujours un cas à part : un très petit établissement, un lycée avec des classes prépa ou un établissement spécialisé. Un contradicteur pourrait donc le balayer facilement. L'agent proposait de comparer plutôt aux 10 % d'établissements les mieux dotés. Le porteur a gardé son choix : on doit pouvoir savoir quel établissement dépense le plus, même si c'est une exception, à condition de l'expliciter. En conséquence, le maximum est toujours affiché avec son contexte (nombre d'élèves, type, signalements).
- **Le privé limité aux enseignants.** Au départ, l'agent supposait que seule la part des enseignants comptait pour le privé sous contrat. Le porteur l'a corrigé : le privé sous contrat reçoit aussi le forfait d'externat et parfois des subventions, avec l'exemple de Stanislas à Paris. En conséquence, on ajoute le forfait d'externat et les subventions publiées.
- **Les outils techniques.** L'agent a d'abord proposé Astro, puis les composants UI5 de SAP. Le porteur les a refusés. Il veut React et Node.js, hors de l'écosystème SAP, pour l'objectif de montée en compétence. L'agent a signalé que ce choix est guidé par l'apprentissage, alors que le porteur avait d'abord dit que le résultat primait. En conséquence, l'objectif secondaire est écrit dans le contexte, et une règle protège l'objectif principal : le site doit fonctionner même si l'API tombe.
- **Le calendrier.** L'agent proposait des étapes successives et une mise en ligne le 22 novembre. Le porteur a choisi de faire avancer les quatre projets en parallèle avec des agents. En conséquence, les formats de données sont figés le 14 octobre et la mise en ligne est avancée au 15 novembre. Le vrai goulot d'étranglement devient le temps de relecture du porteur.
- **Le filtre de la carte.** L'agent a objecté qu'une moyenne régionale qui mélange collèges et lycées est trompeuse. Une région qui a beaucoup de lycées professionnels paraîtrait chère simplement parce que ces lycées coûtent plus cher par nature. L'agent proposait d'afficher un seul type d'établissement à la fois, avec les collèges par défaut. Le porteur garde une carte sans filtre par défaut, avec un filtre par type disponible en option.
- **Le pseudonymat de l'éditeur.** L'agent a montré que le compte GitHub du porteur est déjà relié à son nom par ses commits publics, et proposait des mesures pour rester pseudonyme. Le porteur a choisi de ne pas s'en occuper.
- **Les parents comme persona.** Ils ont été écartés, pour la raison donnée dans la section des personas.
- **Les mesures de succès.** L'agent proposait aussi de mesurer les reprises dans les médias et le nombre de visites. Le porteur n'a gardé que la couverture : au moins 90 % des établissements avec une estimation. Il verra ensuite si le projet prend.

Choix propres à ce projet :

- **Le cumul des travaux depuis les années 80, puis leur amortissement.** Le porteur voulait savoir combien de travaux on a mis dans un lycée encore debout depuis les années 80, puis il a proposé un amortissement annuel. L'agent a objecté deux choses. D'abord, les données n'existent pas avant 2019 environ, sauf dans deux régions. Ensuite, amortir sur 40 ans avec seulement 7 ans de données fausserait tout : un lycée rénové en 2020 paraîtrait très cher, un lycée rénové en 2005 paraîtrait gratuit. Les deux ont convenu d'un indicateur travaux séparé, jamais additionné au chiffre principal, pour la deuxième version. Le porteur a jugé très bonne la piste des marchés publics.

## 11. Glossaire

- **Établissement** : un collège ou un lycée, public ou privé sous contrat, identifié par son UAI. Le privé hors contrat est exclu, parce qu'il ne reçoit pas d'argent public.
- **UAI** (unité administrative immatriculée) : l'identifiant unique de huit caractères de chaque établissement, par exemple `0141796B`. C'est la clé de jointure entre toutes les sources.
- **Dépense publique estimée par élève** : la somme de l'argent public attribué à un établissement pour une année scolaire, divisée par son nombre d'élèves. Elle exclut ce que paient les familles et les travaux. C'est le chiffre principal du site.
- **Part État** : ce que l'État paie pour l'établissement, surtout les salaires des enseignants et du personnel de vie scolaire. Elle est calculée établissement par établissement.
- **Part collectivité** : ce que paie le département pour un collège, ou la région pour un lycée : agents techniques, chauffage, fonctionnement. C'est le plus souvent une moyenne du territoire.
- **ETP** (équivalent temps plein) : une mesure du personnel dans laquelle deux mi-temps comptent pour un.
- **Corps** : la catégorie statutaire d'un enseignant. Les données en distinguent cinq : agrégé, certifié, professeur de lycée professionnel (PLP), autre titulaire, et contractuel (non titulaire). Chaque corps a sa grille de salaire.
- **Grille de salaire** (ou grille indiciaire) : le tableau officiel qui fixe le salaire selon le corps et l'échelon.
- **Échelon** : le niveau d'avancement dans la grille. Il dépend surtout de l'ancienneté de carrière. Les données ne le donnent pas, donc on l'approche par l'âge.
- **Recalage** : l'opération qui multiplie nos estimations par un coefficient, pour que leur somme retombe exactement sur le total officiel publié.
- **Tableau de passage** : le tableau public qui explique l'écart entre le chiffre officiel du ministère et notre moyenne nationale, par exemple les dépenses des familles et les travaux qu'on retire.
- **Contribution retraite de l'État** : ce que l'État verse pour la retraite de ses enseignants fonctionnaires, environ 75 % du salaire de base (ordre de grandeur à vérifier). Les enseignants du privé sous contrat relèvent du régime général, avec des cotisations de l'ordre de 15 à 20 %. Le site affiche les chiffres avec ou sans cette contribution.
- **Forfait d'externat** : la somme par élève que le département ou la région doit verser chaque année aux établissements privés sous contrat. Il a une part « matériel », pour le fonctionnement, et une part « personnel », pour le personnel non enseignant.
- **Valeur de repli** : la valeur provisoire utilisée quand une donnée manque. Par exemple, le coût moyen de fonctionnement d'un élève du public de la même collectivité remplace un forfait d'externat introuvable. Elle est toujours signalée.
- **IPS** (indice de position sociale) : un score publié pour chaque établissement, qui résume le milieu social des familles des élèves. Plus il est élevé, plus le milieu est favorisé.
- **Éducation prioritaire** : le classement REP (réseau d'éducation prioritaire) ou REP+ (réseau renforcé) des établissements qui accueillent des élèves plus défavorisés. Ces établissements reçoivent en principe plus de moyens.
- **Courbe de Lorenz** : une courbe qui montre quelle part de la dépense totale reçoivent les X % d'élèves les moins dotés. Plus elle s'éloigne de la diagonale, plus la dépense est concentrée.
- **Indice de Gini** : un nombre entre 0 et 1 tiré de la courbe de Lorenz. 0 veut dire que tout le monde reçoit la même chose, 1 veut dire qu'une seule personne reçoit tout.
- **Secret statistique** : la règle qui masque les valeurs trop petites, ici moins de 5 ETP, pour qu'on ne puisse pas reconnaître des personnes.
- **Cité scolaire** : un établissement qui réunit un collège et un lycée, et qui partage une partie de leur personnel.
- **Classes post-bac** : les classes préparatoires aux grandes écoles (CPGE) et les sections de technicien supérieur (BTS) installées dans certains lycées.
- **Fichier agrégé** : le fichier final publié, avec une ligne par établissement et tous les chiffres calculés, plus les tableaux par territoire. C'est le contrat entre le modèle de coût et le site.
- **Manifeste des sources** : la liste de toutes les sources utilisées, avec leur lien, leur licence, leur date de téléchargement et leur empreinte de contrôle.
- **Empreinte de contrôle** (checksum) : un code calculé à partir d'un fichier, qui change dès que le fichier change d'un seul octet.
- **Indicateur travaux** : le montant moyen des travaux par an et par élève sur la période connue, depuis 2019 environ. Il est affiché à côté du chiffre principal et n'y est jamais additionné. Il est prévu pour la deuxième version.
- **Académie** : la circonscription administrative de l'Éducation nationale. Une région en compte une ou plusieurs.
- **Première version** : la première version publique du site, prévue le 15 novembre 2026. La **deuxième version** ajoute l'indicateur travaux.
