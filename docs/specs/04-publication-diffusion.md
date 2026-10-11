# Publication et diffusion

**Projet Linear :** https://linear.app/owlaris/project/publication-et-diffusion-456c46f873ac

*Projet 4 sur 4 du projet global « Dépense publique par élève, établissement par établissement ». Les autres specs se trouvent dans le même dossier : [index](README.md).*

## 1. Contexte et problème

En pleine mobilisation étudiante, la parole gouvernementale répète que « ce n'est pas un problème de moyens ». Pourtant, personne n'a jamais publié combien l'argent public dépense pour un élève, établissement par établissement. Le ministère ne publie que des moyennes nationales. En 2024, la dépense moyenne était de 10 450 € par collégien, 13 020 € par lycéen en voie générale ou technologique et 14 700 € par lycéen en voie professionnelle (DEPP, *Repères et références statistiques 2026*, chapitre 10). Les travaux les plus proches comptent des postes ou des heures d'enseignement par élève, mais jamais des euros : une étude de France Stratégie en 2017 et une enquête de Franceinfo en 2024.

Le projet global estime la dépense publique par élève de chaque collège et de chaque lycée public et privé sous contrat de France, outre-mer compris, pour la rentrée 2024. Il la publie sur un site pensé d'abord pour le téléphone, avec une carte, une fiche par établissement et des comparaisons. Le but est de rendre visibles les inégalités de moyens entre établissements, auprès du plus grand nombre de personnes possible. La question à laquelle le site répond est : « Combien dépense-t-on pour moi, par rapport à la moyenne nationale, à l'académie où l'on dépense le plus et à l'établissement où l'on dépense le plus ? »

Le travail est découpé en quatre projets qui avancent en parallèle : l'inventaire et la collecte des données, le modèle de coût et les statistiques, le site interactif, et la publication et la diffusion. Des formats de données figés dès le 14 octobre 2026 permettent ce parallélisme. La première version publique est prévue le 15 novembre 2026.

Le projet a aussi un objectif secondaire : monter en compétence sur une architecture JavaScript moderne, avec un front en React et un back en Node.js. Cet objectif explique certains choix techniques. Il ne doit jamais dégrader l'objectif principal, qui est un site rapide, lisible et crédible.

Le principe de méthode qui traverse les quatre projets est simple. On ne calcule jamais le montant total nous-mêmes : on part des totaux officiels publiés (budget de l'État, comptes des collectivités, chiffres de la DEPP) et on les répartit au plus juste entre les établissements. Personne ne peut alors dire qu'on a inventé des montants. Notre apport, c'est la répartition.

**Ce que fait ce projet-ci.** Il met le site en ligne et le fait connaître. Dès la première semaine, il installe un site vide avec une mise en ligne automatique, pour que la publication du 15 novembre ne soit pas un saut dans le vide. Il mène une étude d'infrastructure pour choisir un hébergement qui s'ajuste tout seul au trafic, à la hausse comme à la baisse. Il publie la première version avec tout ce qui fonde la confiance : la méthode, les sources, les mentions légales et le journal des corrections. Puis il diffuse : le jeu de données sur data.gouv.fr, un dossier de presse et des contacts avec les journalistes.

Le contexte impose deux exigences.

D'abord, le site peut recevoir un pic de visites d'un coup, si un média ou un compte connu le partage. Il doit tenir sans facture surprise. Le porteur prévoit un petit budget d'infrastructure si le projet prend.

Ensuite, le sujet est politique, et chaque erreur sera exploitée. La transparence sur les corrections doit donc être exemplaire : le porteur veut que les gens puissent remonter de l'information en toute transparence, et que les données soient irréprochables sur leur fraîcheur et leur traçabilité.

## 2. Mesures de succès

1. Un site vide est en ligne le 14 octobre 2026. Il est mis à jour automatiquement à chaque modification de la branche principale.
2. La première version est en ligne le 15 novembre 2026. Elle tient un test de charge au seuil fixé par l'étude d'infrastructure.
3. Le jeu de données est publié sur data.gouv.fr.
4. Chaque signalement reçoit une réponse publique.

Ces mesures servent la mesure de succès globale : une estimation pour au moins 90 % des collèges et lycées publics et privés sous contrat, accessible à tous.

## 3. Personas

**L'élève mobilisé (persona principal).** C'est un collégien, un lycéen, ou un étudiant qui pense à son ancien lycée. Il découvre le site par un lien partagé sur Instagram, WhatsApp ou TikTok, depuis son téléphone. Il veut savoir en quelques secondes combien on dépense pour lui, comparé aux autres, puis partager ce chiffre. Il ne lira pas la méthode, mais il doit pouvoir la trouver en un clic.

**Le journaliste.** C'est un journaliste, un vérificateur ou un chercheur. Il cherche les plus gros écarts pour écrire un article. Il vérifie la méthode avant de citer un chiffre, et il télécharge les données pour faire ses propres calculs. Il a besoin de sources, de numéros de version et d'un moyen de signaler une erreur.

**Le mainteneur.** C'est le porteur du projet et les agents de code qui travaillent pour lui. Il a besoin d'une chaîne de données reproductible, de formats figés entre les projets, et d'être prévenu automatiquement quand une source change.

Les parents qui choisissent un établissement ne sont pas un persona du projet. Ils choisissent rarement leur établissement, à cause de la carte scolaire, et le coût par élève ne les aiderait pas à décider.

Dans ce projet, le mainteneur est servi par la mise en ligne automatique et l'étude d'infrastructure. Le journaliste est servi par le journal des corrections, data.gouv.fr et le dossier de presse. L'élève est servi par un site qui tient pendant les pics de visites.

## 4. User stories

### US-1 : Mise en ligne automatique

En tant que mainteneur, je veux que chaque modification de la branche principale soit mise en ligne automatiquement, afin de publier sans stress le jour de la sortie.

- AC1 : une page d'attente est en ligne le 14 octobre, sur un hébergement statique gratuit.
- AC2 : à chaque push sur `main`, la chaîne de mise en ligne fabrique et publie le front. Une fabrication qui échoue ne remplace jamais la version en ligne.
- AC3 : on peut revenir à la version précédente en une seule action.

### US-2 : Étude d'infrastructure

En tant que mainteneur, je veux comparer trois ou quatre hébergeurs pour le front et l'API, afin de choisir une solution qui s'ajuste toute seule au trafic, à la hausse comme à la baisse, sans facture surprise.

- AC1 : la comparaison porte sur six critères. Le premier est l'ajustement automatique des ressources, à la hausse comme à la baisse, jusqu'à zéro quand personne ne visite. Les autres sont le coût à 0, 10 000, 100 000 et 1 million de visites par jour, le délai de réveil d'un serveur en veille, la possibilité de plafonner les dépenses, l'hébergement en Europe et la facilité de mise en ligne.
- AC2 : le coût du fond de carte en cas de pic est inclus dans la comparaison.
- AC3 : l'étude produit la décision ADR-PUB-A et un plan de test de charge. Elle fixe le seuil de trafic qui déclenche le budget payant du porteur.

### US-3 : Première version en ligne

En tant qu'élève ou journaliste, je veux un site en ligne avec la méthode, la liste des sources, les mentions légales et le téléchargement des données, afin de pouvoir faire confiance aux chiffres.

- AC1 : la première version est en ligne le 15 novembre 2026.
- AC2 : le site contient une page de méthode (tirée de la note du projet 2), une page des sources (tirée du manifeste du projet 1), les mentions légales (identité de l'éditeur et de l'hébergeur) et le téléchargement du fichier agrégé.
- AC3 : l'audience est mesurée avec un outil qui ne demande pas de bandeau de consentement aux cookies.
- AC4 : le test de charge est réussi au seuil fixé par l'étude d'infrastructure.
- AC5 : la version et la date des données sont visibles sur chaque page.

### US-4 : Journal public des corrections

En tant que journaliste, je veux voir toutes les corrections apportées aux données et les réponses aux signalements, afin de vérifier que le site corrige ses erreurs en toute transparence.

- AC1 : chaque signalement, reçu sous forme de ticket GitHub, reçoit une réponse publique dans un délai annoncé sur le site.
- AC2 : chaque nouvelle version des données a son entrée dans le journal. L'entrée dit ce qui a changé, pourquoi, et quels établissements sont concernés.
- AC3 : le journal est consultable sur une page du site, avec un lien vers chaque ticket.

### US-5 : Publication sur data.gouv.fr

En tant que journaliste, je veux trouver le jeu de données agrégé sur data.gouv.fr, afin de le réutiliser et de le citer.

- AC1 : le jeu de données est publié sous Licence Ouverte 2.0, la licence standard des données publiques françaises. Il est accompagné de sa documentation, du manifeste des sources et d'un lien vers la méthode.
- AC2 : il est mis à jour à chaque nouvelle version des données.

### US-6 : Dossier de presse

En tant que journaliste, je veux un dossier de presse d'une page, afin d'écrire un article rapidement et sans erreur.

- AC1 : le dossier donne les chiffres clés, un résumé de la méthode en cinq lignes, trois à cinq visuels et un contact.
- AC2 : chaque chiffre du dossier est vérifié contre une version précise du fichier agrégé, citée dans le dossier.

### US-7 : Contacts avec les journalistes

En tant que mainteneur, je veux une liste de journalistes et de rédactions à contacter, avec un message adapté, afin que la publication soit reprise.

- AC1 : la liste compte une vingtaine de contacts, surtout des cellules de données et des journalistes spécialisés dans l'éducation, avec le moyen de les joindre.
- AC2 : les messages sont envoyés au plus tard le 22 novembre 2026.

## 5. Périmètre

**Dans le périmètre :**
1. Le site vide en ligne et la mise en ligne automatique.
2. L'étude d'infrastructure et le choix de l'hébergement.
3. La mise en ligne de la première version, avec la méthode, les sources, les mentions légales, la mesure d'audience et le test de charge.
4. Le journal public des corrections et le délai de réponse aux signalements.
5. La publication sur data.gouv.fr.
6. Le dossier de presse et les contacts avec les journalistes.

**Hors périmètre :**
1. La publicité payante.
2. Une agence de relations presse.
3. La gestion de comptes sur les réseaux sociaux au-delà du lancement.
4. Le pseudonymat de l'éditeur, que le porteur a choisi de ne pas traiter.

## 6. Jalons et enchaînement

**Jalon 1 : Site vide en ligne, le 14 octobre 2026.** C'est le jalon fondateur. Il porte US-1. Il utilise un hébergement statique gratuit, donc il ne dépend pas de l'étude d'infrastructure.

**Jalon 2 : Étude d'infrastructure, le 25 octobre 2026.** Il porte US-2. Il fixe l'hébergement de l'API dont le projet 3 a besoin pour son jalon de développement.

**Jalon 3 : Mise en ligne de la première version, le 15 novembre 2026.** Il porte US-3 et US-4. Il dépend des tests sur téléphone du projet 3 (12 novembre) et des chiffres du projet 2 (1er novembre).

**Jalon 4 : Diffusion, le 22 novembre 2026.** Il porte US-5, US-6 et US-7.

## 7. Où en est-on et contexte technique

**État du dépôt.** Le dépôt public `gambitl/open-data-college-lycee-france` est vide à ce jour, à part ces specs. La mise en ligne automatique est prévue avec GitHub Actions, l'outil d'automatisation intégré à GitHub.

**Hébergement par défaut, en attendant l'étude.** Le front irait sur un hébergement statique gratuit avec une bande passante illimitée, par exemple Cloudflare Pages. L'API irait sur une offre gratuite, à choisir. L'étude d'infrastructure tranche.

**Obligations légales.** La loi française oblige un site à identifier son éditeur et son hébergeur dans des mentions légales. Les données réutilisées sont sous Licence Ouverte, qui impose de citer la source et la date de mise à jour : le manifeste des sources y répond.

**Dépendances.** Ce projet dépend du projet 3 pour le site et du projet 2 pour les chiffres, la méthode et le dossier de presse. Le projet 3 dépend de lui pour l'hébergement.

## 8. Fiches de design

Les pages de ce projet utilisent le système de design défini par le projet 3. Elles passent par open design sous la forme d'un seul gabarit de page de contenu.

### Pages de contenu : méthode, sources, journal des corrections, mentions légales

**Ce que c'est.** Des pages de texte, lisibles sur téléphone, avec des tableaux pour les sources et une liste chronologique pour le journal des corrections.

**États à dessiner :**
- *Texte long sur téléphone*, avec un sommaire.
- *Tableau des sources* qui défile horizontalement sur petit écran.
- *Journal des corrections vide* : « Aucune correction pour l'instant ».
- *Entrée du journal* avec le lien vers le ticket GitHub.

### Visuels du dossier de presse

Trois à cinq visuels, déclinés des images de partage du projet 3, au format des réseaux sociaux et des articles.

## 9. Questions ouvertes et décisions d'architecture

**Questions ouvertes**
1. **Le nom du site et le nom de domaine**, environ 10 € par an. Par défaut, le site vide vit sur une adresse gratuite fournie par l'hébergeur. *Recommandation :* choisir un nom court et parlant avant la mise en ligne de la première version.
2. **L'outil de mesure d'audience.** Par défaut, il n'y en a pas. *Recommandation :* un outil respectueux de la vie privée, qui ne demande pas de bandeau de consentement.
3. **Contacter les organisations étudiantes et lycéennes.** Par défaut, on ne les contacte pas. *Recommandation :* décider consciemment. Elles augmenteraient beaucoup la diffusion, mais pourraient affaiblir la neutralité perçue du site auprès des journalistes.
4. **Le seuil qui déclenche le budget d'infrastructure payant.** Il est fixé par l'étude d'infrastructure.
5. **Le délai de réponse aux signalements.** *Recommandation :* une première réponse sous 72 heures, annoncée sur le site.
6. **L'identité de l'éditeur dans les mentions légales.** Le porteur a choisi de ne pas chercher le pseudonymat. Par défaut, il signe sous son nom.

**Décision d'architecture à créer** (dans `docs/adr/`)
- **ADR-PUB-A : l'hébergement du front et de l'API.** C'est le résultat de l'étude d'infrastructure. Statut : à créer.

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

- **Le rôle du projet 4.** Au départ, le porteur voulait une dernière étape pour publier le site. L'agent a objecté qu'une mise en ligne à la toute fin est un saut dans le vide, et qu'en plein contexte de mobilisation, le temps compte. Le site vide est donc en ligne dès la première semaine, et le projet est recentré sur la diffusion.
- **L'ajustement automatique au trafic.** Le porteur a demandé une étude d'infrastructure avec ajustement automatique à la hausse et à la baisse. C'est US-2.
- **La transparence des corrections.** Le porteur veut « mettre le paquet » sur ce sujet. Le journal public des corrections (US-4) et le formulaire de signalement du projet 3 en découlent.

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
