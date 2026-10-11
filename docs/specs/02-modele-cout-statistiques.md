# Modèle de coût par élève et statistiques

*Projet 2 sur 4 du projet global « Dépense publique par élève, établissement par établissement ». Les autres specs se trouvent dans le même dossier : [index](README.md).*

## 1. Contexte et problème

En pleine mobilisation étudiante, la parole gouvernementale répète que « ce n'est pas un problème de moyens ». Pourtant, personne n'a jamais publié combien l'argent public dépense pour un élève, établissement par établissement. Le ministère ne publie que des moyennes nationales. En 2024, la dépense moyenne était de 10 450 € par collégien, 13 020 € par lycéen en voie générale ou technologique et 14 700 € par lycéen en voie professionnelle (DEPP, *Repères et références statistiques 2026*, chapitre 10). Les travaux les plus proches comptent des postes ou des heures d'enseignement par élève, mais jamais des euros : une étude de France Stratégie en 2017 et une enquête de Franceinfo en 2024.

Le projet global estime la dépense publique par élève de chaque collège et de chaque lycée public et privé sous contrat de France, outre-mer compris, pour la rentrée 2024. Il la publie sur un site pensé d'abord pour le téléphone, avec une carte, une fiche par établissement et des comparaisons. Le but est de rendre visibles les inégalités de moyens entre établissements, auprès du plus grand nombre de personnes possible. La question à laquelle le site répond est : « Combien dépense-t-on pour moi, par rapport à la moyenne nationale, à l'académie où l'on dépense le plus et à l'établissement où l'on dépense le plus ? »

Le travail est découpé en quatre projets qui avancent en parallèle : l'inventaire et la collecte des données, le modèle de coût et les statistiques, le site interactif, et la publication et la diffusion. Des formats de données figés dès le 14 octobre 2026 permettent ce parallélisme. La première version publique est prévue le 15 novembre 2026.

Le projet a aussi un objectif secondaire : monter en compétence sur une architecture JavaScript moderne, avec un front en React et un back en Node.js. Cet objectif explique certains choix techniques. Il ne doit jamais dégrader l'objectif principal, qui est un site rapide, lisible et crédible.

Le principe de méthode qui traverse les quatre projets est simple. On ne calcule jamais le montant total nous-mêmes : on part des totaux officiels publiés (budget de l'État, comptes des collectivités, chiffres de la DEPP) et on les répartit au plus juste entre les établissements. Personne ne peut alors dire qu'on a inventé des montants. Notre apport, c'est la répartition.

**Ce que fait ce projet-ci.** Il transforme les données du projet 1 en chiffres publiables. Pour chaque établissement, il estime la dépense publique par élève, découpée entre la part État et la part collectivité, et il la recale sur les totaux officiels. Il calcule ensuite tout ce que le site affiche : les comparaisons, le rang, les moyennes par territoire pour la carte, la courbe de Lorenz, l'indice de Gini et le croisement avec le profil social. Il écrit enfin la note de méthode, parce qu'un chiffre politique ne vaut que par la méthode qui le défend.

**Comment fonctionne le recalage, sur un exemple.** Les chiffres de cet exemple sont inventés. Supposons que le budget de l'État indique 30 milliards d'euros de salaires d'enseignants dans les collèges publics. Notre calcul collège par collège, qui multiplie le nombre d'enseignants par la grille de salaire, donne 28,5 milliards. Il manque 5 %, qui correspondent aux primes, aux heures supplémentaires et aux remplaçants. On multiplie alors chaque collège par le même coefficient pour retomber sur 30 milliards. Chaque collège garde sa place relative : celui qui a beaucoup d'agrégés expérimentés reste plus cher que celui qui a de jeunes contractuels. Mais le total est celui de l'État. Ce qu'on sait mieux répartir n'est pas réparti uniformément : les primes REP+ vont d'abord aux établissements REP+, puis le coefficient s'applique au reste.

Les dépenses qu'on ne connaît qu'au niveau d'une collectivité, comme les agents techniques ou le chauffage, sont divisées par le nombre d'élèves du territoire. Chaque établissement du territoire reçoit cette moyenne. C'est moins précis, mais c'est propre à chaque territoire : un collège de Lozère ne reçoit pas la même moyenne qu'un collège des Hauts-de-Seine.

Le chiffre officiel de la DEPP inclut ce que paient les familles et les travaux, alors que notre chiffre principal les exclut. Notre moyenne nationale sera donc plus basse que le chiffre officiel. Un tableau de passage public explique cet écart, pour qu'il ne paraisse pas suspect.

**Le cas du privé sous contrat.** La dépense publique y a trois sources. L'État paie les enseignants. On utilise la même méthode de grille de salaire, mais avec le régime de retraite du privé, beaucoup moins coûteux pour l'État que celui des fonctionnaires. La collectivité verse le forfait d'externat par élève. Enfin, il y a les aides facultatives, quand elles sont publiées, aujourd'hui seulement en Île-de-France. Le privé est recalé sur son propre total officiel : 10,8 milliards d'euros en 2024, dont 66 % payés par l'État.

## 2. Mesures de succès

1. Au moins 90 % des collèges et lycées publics et privés sous contrat ont une estimation. C'est la mesure de succès globale du projet.
2. Après le tableau de passage, notre moyenne nationale par type d'établissement retombe sur les chiffres officiels, avec moins de 1 % d'écart.
3. Chaque hypothèse de la note de méthode est accompagnée d'un test de sensibilité, qui dit de combien le résultat bouge si l'hypothèse change.

## 3. Personas

**L'élève mobilisé (persona principal).** C'est un collégien, un lycéen, ou un étudiant qui pense à son ancien lycée. Il découvre le site par un lien partagé sur Instagram, WhatsApp ou TikTok, depuis son téléphone. Il veut savoir en quelques secondes combien on dépense pour lui, comparé aux autres, puis partager ce chiffre. Il ne lira pas la méthode, mais il doit pouvoir la trouver en un clic.

**Le journaliste.** C'est un journaliste, un vérificateur ou un chercheur. Il cherche les plus gros écarts pour écrire un article. Il vérifie la méthode avant de citer un chiffre, et il télécharge les données pour faire ses propres calculs. Il a besoin de sources, de numéros de version et d'un moyen de signaler une erreur.

**Le mainteneur.** C'est le porteur du projet et les agents de code qui travaillent pour lui. Il a besoin d'une chaîne de données reproductible, de formats figés entre les projets, et d'être prévenu automatiquement quand une source change.

Les parents qui choisissent un établissement ne sont pas un persona du projet. Ils choisissent rarement leur établissement, à cause de la carte scolaire, et le coût par élève ne les aiderait pas à décider.

Dans ce projet, les chiffres servent l'élève, et la méthode sert le journaliste. Le format du fichier agrégé sert le mainteneur.

## 4. User stories

### US-1 : Format du fichier agrégé

En tant que mainteneur, je veux un format figé du fichier agrégé, livré avec un fichier fictif au bon format, afin que le site avance en parallèle sans attendre les vrais chiffres.

- AC1 : le schéma est documenté : une ligne par établissement, avec ses colonnes, leurs types, leurs unités et les valeurs manquantes autorisées. Il couvre aussi les tableaux annexes : moyennes par territoire, points de la courbe de Lorenz, dépense par décile d'IPS.
- AC2 : un fichier fictif d'environ 11 000 lignes, avec des valeurs plausibles, passe le même script de validation que le vrai fichier.
- AC3 : le fichier porte un numéro de version et une date de fabrication. Tout changement de format augmente la version et laisse une note dans le journal des changements.

### US-2 : Dépense par élève de chaque établissement

En tant qu'élève, je veux connaître la dépense publique estimée par élève dans mon établissement, découpée entre la part État et la part collectivité, afin de savoir combien on dépense pour moi.

- AC1 : au moins 90 % des établissements ont une estimation.
- AC2 : la part État comprend les enseignants (ETP multipliés par le coût employeur par corps et par âge, plus les primes REP et REP+ là où elles s'appliquent) et la vie scolaire. Elle est recalée sur les programmes budgétaires 141 (public) et 139 (privé), niveau par niveau.
- AC3 : la part collectivité est la moyenne de fonctionnement par élève du territoire pour le public, et le forfait d'externat pour le privé. En Centre-Val de Loire et en Île-de-France, ce sont les montants mesurés par lycée.
- AC4 : chaque établissement porte un marqueur de qualité : estimation complète, estimation partielle (valeurs masquées), valeur de repli, classes post-bac, cité scolaire.
- AC5 : le tableau de passage est publié pour chaque type d'établissement : chiffre officiel de la DEPP, moins les dépenses des familles, moins les travaux, moins les autres écarts identifiés, égale notre moyenne.
- AC6 : des cas de contrôle sont vérifiés et commentés : de grands lycées connus, et Stanislas si le rapport d'inspection rendu public en 2024 donne des montants.

### US-3 : Avec ou sans la retraite

En tant que journaliste, je veux voir chaque chiffre avec et sans la contribution retraite de l'État, afin de comparer le public et le privé sans que la différence de régime de retraite fausse la comparaison.

- AC1 : les deux variantes sont calculées pour chaque établissement et pour chaque moyenne.
- AC2 : la comparaison entre public et privé est disponible dans les deux variantes, avec une phrase d'explication en langage courant.

### US-4 : Comparaisons pour un établissement

En tant qu'élève, je veux comparer mon établissement à la moyenne nationale, à l'académie qui dépense le plus et à l'établissement qui dépense le plus, et connaître mon rang, afin de savoir si on dépense plus ou moins pour moi que pour les autres.

- AC1 : la moyenne nationale est disponible par type et par secteur, et tous types confondus.
- AC2 : l'académie qui dépense le plus par élève est identifiée, pour chaque type d'établissement.
- AC3 : l'établissement qui dépense le plus est identifié, avec son contexte : nombre d'élèves, type, marqueurs de qualité.
- AC4 : chaque établissement a un rang exprimé en pourcentage parmi les établissements du même type, par exemple « reçoit moins que 72 % des lycées professionnels ».
- AC5 : les estimations partielles sont exclues du calcul du maximum et signalées dans le classement. La règle est écrite dans la note de méthode.

### US-5 : Moyennes par territoire pour la carte

En tant qu'élève, je veux voir la dépense par élève par région, puis par département, puis par commune, afin de comprendre les écarts autour de moi avant de zoomer sur les établissements.

- AC1 : les moyennes sont pondérées par le nombre d'élèves. Elles sont calculées par région, département et commune, tous établissements confondus, puis par type et par secteur pour le filtre optionnel de la carte.
- AC2 : chaque moyenne indique le nombre d'établissements et d'élèves sur lesquels elle repose.
- AC3 : une commune qui n'a qu'un établissement affiche sa valeur, marquée comme telle.

### US-6 : Courbe de Lorenz et indice de Gini

En tant que journaliste, je veux la courbe de Lorenz et l'indice de Gini de la dépense par élève, afin de mesurer à quel point les moyens sont concentrés.

- AC1 : les points de la courbe de Lorenz (100 quantiles, pondérés par élève) sont calculés au niveau national, par académie et par type d'établissement.
- AC2 : l'indice de Gini est calculé au niveau national, par type, par secteur et par académie.
- AC3 : la position de chaque établissement sur la courbe nationale est calculée.

### US-7 : Dépense et profil social

En tant que journaliste, je veux la dépense par élève croisée avec l'IPS et l'éducation prioritaire, afin de vérifier si on dépense plus pour les élèves qui en ont le plus besoin.

- AC1 : la dépense moyenne est calculée par décile d'IPS et par classement (REP+, REP, hors éducation prioritaire), pour chaque type d'établissement.
- AC2 : le même calcul est fait sur la part État seule, pour isoler l'effet de l'ancienneté des enseignants.
- AC3 : les résultats sont publiés tels qu'ils sont, même s'ils nuancent la thèse du projet. Le porteur s'attend à être surpris.

### US-8 : Note de méthode

En tant que journaliste, je veux une note de méthode lisible, afin de défendre ou de critiquer les chiffres en connaissance de cause.

- AC1 : chaque ligne de l'inventaire des dépenses a un paragraphe qui explique comment elle est traitée.
- AC2 : chaque hypothèse est énoncée avec son effet attendu et son test de sensibilité : l'âge comme approximation de l'échelon, le recalage, les valeurs de repli, le comptage des étudiants post-bac.
- AC3 : la note est écrite pour un lecteur non spécialiste, avec un résumé de deux phrases en tête.

### US-9 : Indicateur travaux (deuxième version)

En tant qu'élève, je veux voir combien on a investi en travaux dans mon établissement depuis 2019, par an et par élève, afin de compléter le tableau des moyens.

- AC1 : l'indicateur est la moyenne annuelle des travaux par élève sur la période connue. Il n'est jamais additionné au chiffre principal.
- AC2 : il n'est affiché que là où les données existent, avec la période et la couverture écrites en clair.
- AC3 : les établissements protégés au titre des monuments historiques portent un marqueur.

## 5. Périmètre

**Dans le périmètre :**
1. Le format figé du fichier agrégé et un fichier fictif.
2. L'estimation par établissement, recalée sur les totaux officiels, avec les marqueurs de qualité et le tableau de passage.
3. Les deux variantes, avec et sans la retraite.
4. Les comparaisons et le rang.
5. Les moyennes par région, département et commune.
6. La courbe de Lorenz et l'indice de Gini.
7. Le croisement avec l'IPS et l'éducation prioritaire.
8. La note de méthode.
9. L'indicateur travaux, pour la deuxième version.

**Hors périmètre :**
1. Les travaux dans le chiffre principal, et l'amortissement sur la durée de vie des bâtiments, faute de données sur la période nécessaire.
2. Les dépenses des familles.
3. Les évolutions dans le temps : une seule année est couverte.
4. L'explication des causes des écarts par un modèle statistique. Le projet décrit les écarts, il n'en démontre pas les causes.

## 6. Jalons et enchaînement

**Jalon 1 : Format du fichier agrégé, le 14 octobre 2026.** C'est le jalon fondateur. Il porte US-1. Il débloque le développement du site (projet 3), qui travaille sur le fichier fictif dès cette date. Il dépend de l'inventaire du projet 1, livré le même jour : les deux doivent être construits ensemble.

**Jalon 2 : Modèle de coût par établissement, le 28 octobre 2026.** Il porte US-2, US-3 et la première version de US-8. Le code est écrit sur des données fictives dès le 14 octobre, puis recalé sur les vraies données livrées par le projet 1 le 21 octobre.

**Jalon 3 : Comparaisons, inégalités et profil social, le 1er novembre 2026.** Il porte US-4, US-5, US-6, US-7 et la version finale de US-8. Il alimente les écrans du projet 3 et le dossier de presse du projet 4.

**Jalon 4 : Indicateur travaux (deuxième version), le 13 décembre 2026.** Il porte US-9. Il dépend des données de travaux du projet 1.

## 7. Où en est-on et contexte technique

**État du dépôt.** Le dépôt est vide à ce jour. Organisation proposée, qui reste à créer :
- `pipeline/` : le modèle de coût et les statistiques, en Python, avec les calculs en SQL dans DuckDB. Le projet 1 utilise le même dossier.
- `data/` : le fichier agrégé publié en CSV, pour les journalistes, et en JSON, pour le site. Il est accompagné du manifeste des sources.
- Les tests comprennent le script de validation du format, les cas de contrôle et les tests de sensibilité.

**Totaux officiels utilisés pour le recalage.**
- Budget de l'État : programme 141 (enseignement scolaire public du second degré) et programme 139 (enseignement privé sous contrat), montants exécutés par niveau d'enseignement. Le détail par niveau est à confirmer au jalon 1 du projet 1.
- DEPP : dépense moyenne par élève en 2024, soit 10 450 € par collégien, 13 020 € par lycéen en voie générale ou technologique, 14 700 € par lycéen en voie professionnelle et 11 660 € pour l'ensemble du second degré. Pour le public, la dépense totale est de 57,7 milliards d'euros, dont 73 % payés par l'État, 22 % par les collectivités et environ 4 % par les familles. Pour le privé sous contrat, elle est de 10,8 milliards d'euros, dont 66 % payés par l'État.
- Comptes des collectivités : balances de la DGFiP et base de l'OFGL.

**Dépendances.** Ce projet dépend des tables du projet 1. Le site (projet 3) et le dossier de presse (projet 4) dépendent de lui.

## 8. Fiches de design

Pas d'écran : ce projet produit des données et un texte. La note de méthode est mise en page par le projet 4, et les chiffres sont affichés par le projet 3.

## 9. Questions ouvertes et décisions d'architecture

**Questions ouvertes**
1. **L'estimation des primes REP et REP+.** Par défaut, on applique un montant moyen par ETP dans les établissements concernés. *Recommandation :* garder ce défaut, avec les montants officiels des primes, et le documenter.
2. **Les heures supplémentaires et le pacte enseignant.** Par défaut, ils sont répartis par le coefficient de recalage, proportionnellement à la masse salariale. *Recommandation :* accepter ce défaut et le signaler comme une limite dans la note de méthode.
3. **Les règles d'exclusion pour le maximum et le classement.** Par défaut, les estimations partielles sont exclues du maximum mais gardées dans le classement avec un marqueur. *Recommandation :* garder ce défaut.
4. **La liste des cas de contrôle.** *Recommandation :* une dizaine d'établissements connus, publics et privés, dont des lycées avec classes prépa, des établissements REP+ et des établissements d'outre-mer.
5. **Le groupe de comparaison des lycées polyvalents.** À trancher avec le projet 1, au jalon 1.

**Décisions d'architecture à créer** (dans `docs/adr/`)
- **ADR-STATS-A : inclure la contribution retraite de l'État dans le coût, avec une option pour l'enlever.** Le choix est fait. Il reste à documenter ses raisons (le budget officiel l'inclut) et le débat qu'il soulève (le taux élevé finance aussi les pensions passées). Statut : à créer.
- **ADR-STATS-B : la méthode de recalage.** Un coefficient unique, ou un coefficient par ligne de dépense, par secteur et par niveau. *Recommandation :* un coefficient par ligne, par secteur et par niveau, après l'affectation des primes REP. Statut : à créer.

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

- **La retraite des fonctionnaires.** L'agent a expliqué qu'à salaire égal, l'État paie beaucoup plus pour la retraite d'un enseignant du public que pour celle d'un enseignant du privé. Le porteur a demandé que le site permette de voir les chiffres avec et sans ce coût. C'est US-3.
- **L'amortissement des travaux.** Le porteur a proposé un amortissement annuel des travaux. L'agent a objecté qu'avec 7 ans de données, un amortissement sur 40 ans mesurerait surtout qui a été rénové récemment. Les deux ont convenu d'un indicateur travaux séparé, pour la deuxième version. C'est US-9.
- **Le croisement avec l'IPS.** L'agent a insisté sur le fait qu'une différence de moyens n'est pas forcément une inégalité, puisque l'éducation prioritaire est censée recevoir plus. Le porteur a accepté de faire le calcul en s'attendant à être surpris, et de publier le résultat tel quel. C'est US-7.

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
