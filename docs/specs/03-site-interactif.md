# Site interactif : carte, fiche établissement et comparaison

**Projet Linear :** https://linear.app/owlaris/project/site-interactif-carte-fiche-etablissement-et-comparaison-70883a260d9e

*Projet 3 sur 4 du projet global « Dépense publique par élève, établissement par établissement ». Les autres specs se trouvent dans le même dossier : [index](README.md).*

## 1. Contexte et problème

En pleine mobilisation étudiante, la parole gouvernementale répète que « ce n'est pas un problème de moyens ». Pourtant, personne n'a jamais publié combien l'argent public dépense pour un élève, établissement par établissement. Le ministère ne publie que des moyennes nationales. En 2024, la dépense moyenne était de 10 450 € par collégien, 13 020 € par lycéen en voie générale ou technologique et 14 700 € par lycéen en voie professionnelle (DEPP, *Repères et références statistiques 2026*, chapitre 10). Les travaux les plus proches comptent des postes ou des heures d'enseignement par élève, mais jamais des euros : une étude de France Stratégie en 2017 et une enquête de Franceinfo en 2024.

Le projet global estime la dépense publique par élève de chaque collège et de chaque lycée public et privé sous contrat de France, outre-mer compris, pour la rentrée 2024. Il la publie sur un site pensé d'abord pour le téléphone, avec une carte, une fiche par établissement et des comparaisons. Le but est de rendre visibles les inégalités de moyens entre établissements, auprès du plus grand nombre de personnes possible. La question à laquelle le site répond est : « Combien dépense-t-on pour moi, par rapport à la moyenne nationale, à l'académie où l'on dépense le plus et à l'établissement où l'on dépense le plus ? »

Le travail est découpé en quatre projets qui avancent en parallèle : l'inventaire et la collecte des données, le modèle de coût et les statistiques, le site interactif, et la publication et la diffusion. Des formats de données figés dès le 14 octobre 2026 permettent ce parallélisme. La première version publique est prévue le 15 novembre 2026.

Le projet a aussi un objectif secondaire : monter en compétence sur une architecture JavaScript moderne, avec un front en React et un back en Node.js. Cet objectif explique certains choix techniques. Il ne doit jamais dégrader l'objectif principal, qui est un site rapide, lisible et crédible.

Le principe de méthode qui traverse les quatre projets est simple. On ne calcule jamais le montant total nous-mêmes : on part des totaux officiels publiés (budget de l'État, comptes des collectivités, chiffres de la DEPP) et on les répartit au plus juste entre les établissements. Personne ne peut alors dire qu'on a inventé des montants. Notre apport, c'est la répartition.

**Ce que fait ce projet-ci.** Il construit ce que les gens voient : un site pensé d'abord pour le téléphone, qui répond en quelques secondes à la question « combien dépense-t-on pour moi ? ». Il comprend un front en React et une API en Node.js. Le front fonctionne seul, à partir de fichiers statiques fabriqués à l'avance. L'API ajoute trois choses : une interface publique pour les journalistes, la fabrication à la demande des images de partage des comparaisons, et le formulaire de signalement des erreurs.

Le projet commence par décider quelles données on affiche et comment on les formule. Ensuite, chaque écran passe par une maquette validée dans l'outil de design externe du porteur, open design, avant que la moindre ligne de code soit écrite. Le site se limite volontairement à trois écrans, pour que cette étape de design ne retarde pas la mise en ligne.

Ce que l'élève partage, c'est ce qui circule pendant une mobilisation. L'image de partage compte donc autant que la page elle-même. Par exemple : « Au lycée Victor-Hugo, on dépense 8 900 € par élève, contre 13 000 € en moyenne ».

## 2. Mesures de succès

1. Depuis l'accueil, un élève arrive sur la fiche de son établissement en moins de 15 secondes sur téléphone.
2. La fiche d'un établissement se charge en moins de 2 secondes sur une connexion 4G.
3. Le site reste utilisable quand l'API est en panne : la recherche, la carte et les fiches fonctionnent toujours.

Ces mesures servent la mesure de succès globale : une estimation affichée pour au moins 90 % des collèges et lycées publics et privés sous contrat.

## 3. Personas

**L'élève mobilisé (persona principal).** C'est un collégien, un lycéen, ou un étudiant qui pense à son ancien lycée. Il découvre le site par un lien partagé sur Instagram, WhatsApp ou TikTok, depuis son téléphone. Il veut savoir en quelques secondes combien on dépense pour lui, comparé aux autres, puis partager ce chiffre. Il ne lira pas la méthode, mais il doit pouvoir la trouver en un clic.

**Le journaliste.** C'est un journaliste, un vérificateur ou un chercheur. Il cherche les plus gros écarts pour écrire un article. Il vérifie la méthode avant de citer un chiffre, et il télécharge les données pour faire ses propres calculs. Il a besoin de sources, de numéros de version et d'un moyen de signaler une erreur.

**Le mainteneur.** C'est le porteur du projet et les agents de code qui travaillent pour lui. Il a besoin d'une chaîne de données reproductible, de formats figés entre les projets, et d'être prévenu automatiquement quand une source change.

Les parents qui choisissent un établissement ne sont pas un persona du projet. Ils choisissent rarement leur établissement, à cause de la carte scolaire, et le coût par élève ne les aiderait pas à décider.

Dans ce projet, l'élève est le persona principal de la carte, de la recherche, de la fiche, de la comparaison et du partage. Le journaliste est le persona principal de la vue des inégalités et de l'API.

## 4. User stories

### US-1 : Choisir ce qu'on affiche

En tant qu'élève, je veux comprendre le message principal d'un écran en moins de 10 secondes, afin d'avoir envie d'aller plus loin et de partager.

- AC1 : pour chacun des trois écrans, une liste validée par le porteur donne les chiffres affichés, leur formulation et leur ordre de lecture.
- AC2 : chaque chiffre affiché correspond à une colonne du fichier agrégé (projet 2, US-1).
- AC3 : le texte des images de partage est choisi.

### US-2 : Recherche d'un établissement

En tant qu'élève, je veux trouver mon établissement en tapant son nom ou sa ville, même avec une faute de frappe, afin d'arriver à sa fiche en quelques secondes.

- AC1 : la recherche tourne dans le navigateur, sur un index statique d'environ 200 Ko compressé, sans appel à l'API.
- AC2 : avec une faute de frappe, le bon établissement apparaît dans les cinq premiers résultats.
- AC3 : les établissements qui portent le même nom, comme les nombreux « Lycée Victor-Hugo », sont distingués par leur ville.

### US-3 : Carte à plusieurs niveaux de zoom

En tant qu'élève, je veux une carte qui montre la dépense par élève par région, puis par département, puis par commune, puis établissement par établissement quand je zoome, afin de voir les écarts autour de moi.

- AC1 : la carte a quatre niveaux. Les régions et les départements sont des zones colorées, les communes sont des cercles et les établissements sont des points. La légende change avec le niveau.
- AC2 : par défaut, la carte affiche tous les établissements. Un filtre optionnel permet de choisir un type (collège, lycée général et technologique, lycée professionnel) et un secteur (public, privé, tous).
- AC3 : l'outre-mer apparaît dans des encarts.
- AC4 : la carte reste fluide sur un téléphone de milieu de gamme avec environ 11 000 points.
- AC5 : toucher un établissement ouvre sa fiche.

### US-4 : Fiche établissement

En tant qu'élève, je veux une page pour mon établissement avec la dépense par élève, sa répartition et les comparaisons, afin de savoir combien on dépense pour moi par rapport aux autres.

- AC1 : chaque établissement a une adresse web stable. Sa page est fabriquée à l'avance, pour que les moteurs de recherche l'indexent.
- AC2 : la fiche montre le chiffre principal, sa répartition entre part État et part collectivité, la moyenne nationale, l'académie qui dépense le plus, l'établissement qui dépense le plus (avec son contexte), le rang et la position sur la courbe de Lorenz.
- AC3 : un interrupteur affiche les chiffres avec ou sans la contribution retraite de l'État.
- AC4 : les marqueurs de qualité sont expliqués en mots simples : estimation partielle, valeur de repli, classes post-bac, cité scolaire.
- AC5 : la version et la date des données sont affichées.

### US-5 : Comparaison entre deux établissements

En tant qu'élève, je veux comparer mon établissement à un autre de mon choix et partager le lien, afin de montrer l'écart à mes amis.

- AC1 : depuis une fiche, une seconde recherche permet de choisir l'établissement à comparer.
- AC2 : l'adresse de la page contient les deux identifiants. Ouvrir le lien affiche directement la comparaison.
- AC3 : l'image d'aperçu du lien est fabriquée à la demande par l'API. Si l'API est en panne, l'aperçu utilise l'image déjà fabriquée du premier établissement, et le partage ne casse jamais.

### US-6 : Vue des inégalités

En tant que journaliste, je veux une vue d'ensemble avec la courbe de Lorenz, la position de mon établissement et la dépense selon l'IPS, afin de voir le tableau général et pas seulement un cas.

- AC1 : la courbe de Lorenz est affichée avec l'indice de Gini, au niveau national et par académie, avec une explication en langage courant.
- AC2 : la dépense est affichée par décile d'IPS et par classement en éducation prioritaire.
- AC3 : un établissement choisi peut être mis en évidence sur ces graphiques.

### US-7 : Images de partage

En tant qu'élève, je veux un bouton de partage qui produit une image prête pour les réseaux sociaux, afin de diffuser le chiffre de mon établissement.

- AC1 : une image est fabriquée à l'avance pour chaque établissement, soit environ 11 000 images. Elle montre le chiffre, la comparaison avec la moyenne nationale et la version des données.
- AC2 : chaque fiche porte les balises d'aperçu des réseaux sociaux (Open Graph), qui pointent vers son image.
- AC3 : sur téléphone, le bouton ouvre le menu de partage natif.

### US-8 : API publique en lecture seule

En tant que journaliste, je veux une API documentée et le téléchargement du fichier agrégé, afin de faire mes propres analyses.

- AC1 : l'API expose un établissement par son UAI, une liste filtrée par territoire et par type, et les moyennes par territoire. Elle est documentée.
- AC2 (négatif) : l'API n'a aucune route d'écriture, à part l'envoi d'un signalement (US-9). Le nombre de requêtes est limité par visiteur.
- AC3 : les réponses peuvent être mises en cache. Le site fonctionne sans l'API.

### US-9 : Signaler une erreur ou apporter une source

En tant qu'élève ou journaliste, je veux signaler une erreur ou apporter une source depuis la fiche d'un établissement, sans créer de compte, afin que les données soient corrigées en toute transparence.

- AC1 : chaque fiche a un formulaire, déjà rempli avec l'UAI et la version des données. Il demande un message, un lien vers une source (facultatif) et une adresse e-mail (facultative).
- AC2 : l'API crée un ticket public sur GitHub, marqué « à trier », avec le message, l'UAI et la version des données.
- AC3 (négatif) : l'adresse e-mail de la personne n'est jamais publiée. Elle n'apparaît jamais dans le ticket.
- AC4 (négatif) : le nombre d'envois est limité et un piège à robots protège le formulaire. Un contenu trop long est refusé et le code HTML est neutralisé.
- AC5 (négatif) : la clé d'accès à GitHub reste uniquement sur le serveur. Elle ne permet que de créer des tickets dans ce dépôt.

## 5. Périmètre

**Dans le périmètre :**
1. Le choix de ce qu'on affiche et des formulations.
2. Les maquettes des trois écrans, validées dans open design.
3. La recherche, la carte à quatre niveaux, la fiche établissement, la comparaison, la vue des inégalités et les images de partage.
4. L'API publique en lecture seule et la fabrication des images de comparaison.
5. Le formulaire de signalement.
6. Les tests sur téléphone et la rapidité.

**Hors périmètre :**
1. Les comptes utilisateurs.
2. Les commentaires publics sur le site. Le signalement passe par des tickets GitHub.
3. Une application mobile native.
4. D'autres langues que le français.
5. Les évolutions dans le temps, puisqu'une seule année est couverte.
6. L'envoi de fichiers par les visiteurs. Les contributions de données sourcées sont une question ouverte pour la deuxième version.

## 6. Jalons et enchaînement

**Jalon 1 : Choisir ce qu'on affiche, le 18 octobre 2026.** C'est le jalon fondateur du design. Il porte US-1. Il peut commencer tout de suite, parce que le cadrage a déjà fixé les comparaisons principales.

**Jalon 2 : Maquettes validées dans open design, le 25 octobre 2026.** Il couvre le design des trois écrans décrits en section 8, donc les surfaces de US-2 à US-7 et de US-9. Aucun écran n'est codé avant la validation de sa maquette.

**Jalon 3 : Développement du front et de l'API, le 8 novembre 2026.** Il porte US-2 à US-9. Le développement commence sur le fichier fictif du projet 2 (disponible le 14 octobre), puis branche les vrais chiffres dès qu'ils sont livrés (28 octobre et 1er novembre).

**Jalon 4 : Tests sur téléphone et rapidité, le 12 novembre 2026.** Il vérifie les trois mesures de succès, avant la mise en ligne du 15 novembre par le projet 4.

## 7. Où en est-on et contexte technique

**État du dépôt.** Le dépôt est vide à ce jour. Organisation proposée, qui reste à créer :
- `web/` : le front en React avec TypeScript. La carte utilise MapLibre, une bibliothèque libre et gratuite. Environ 11 000 fiches sont fabriquées à l'avance, avec leurs images de partage.
- `api/` : le back en Node.js avec TypeScript, avec un framework d'API léger. L'API charge le fichier agrégé en mémoire au démarrage : il n'y a pas de serveur de base de données. Elle fabrique les images de comparaison à la demande.

**Principe de robustesse.** Les données essentielles (index de recherche, fiches, moyennes par territoire) sont servies sous forme de fichiers statiques. Le site ne dépend donc pas de l'API pour fonctionner. L'API apporte des fonctions en plus.

**Dépendances.**
- Projet 2 : le format du fichier agrégé (14 octobre), puis les vrais chiffres.
- Projet 1 : les contours des régions et des départements, et la position des communes.
- Projet 4 : l'hébergement du front et de l'API, et la mise en ligne automatique.

## 8. Fiches de design

Il n'existe pas encore de système de design. Il sera défini dans open design pendant le jalon 2 : couleurs, typographie et style des graphiques. **Chaque écran passe par une maquette validée dans open design avant le code.**

### Écran A : Accueil, avec la carte et la recherche

**Ce que c'est.** Sur téléphone, une carte en plein écran avec une barre de recherche en haut. L'utilisateur peut chercher son établissement directement, ou explorer la carte en zoomant.

**États à dessiner :**
- *Initial* : vue de la France, régions colorées, recherche vide.
- *Chargement* : fond de carte et données en cours de chargement.
- *Erreur de carte* : si la carte ne se charge pas, la recherche reste disponible et une liste remplace la carte.
- *Succès* : la carte est affichée avec sa légende.
- *Changement de niveau de zoom* : passage des régions aux départements, puis aux communes et aux établissements, avec une légende qui change à chaque niveau.
- *Filtre actif* : un badge montre le filtre choisi et permet de l'enlever.
- *Recherche sans résultat* : un message propose de vérifier l'orthographe ou de chercher par ville.

**Cas limites :** encarts de l'outre-mer, points qui se superposent dans les grandes villes, noms d'établissements très longs, très petits écrans.

### Écran B : Fiche établissement, avec la comparaison, le partage et le signalement

**Ce que c'est.** La page d'un établissement : le chiffre principal en grand, sa répartition, les comparaisons et le rang. On y trouve aussi le bouton de partage, le passage en mode comparaison et le formulaire de signalement.

**États à dessiner :**
- *Estimation complète.*
- *Estimation partielle*, avec un marqueur et une explication courte.
- *Valeur de repli*, avec un marqueur.
- *Marqueurs classes post-bac et cité scolaire.*
- *Établissement privé sous contrat*, avec l'explication du forfait d'externat et de l'interrupteur retraite.
- *Interrupteur retraite* : chiffres avec et sans la contribution retraite.
- *Mode comparaison* : deux établissements côte à côte.
- *API en panne* : le partage utilise l'image de secours, et le formulaire de signalement est remplacé par un message avec un lien direct vers les tickets GitHub.
- *Formulaire de signalement* : vide, envoi en cours, envoyé, erreur, trop d'envois.
- *Établissement introuvable* : une adresse inconnue mène à une page qui propose la recherche.

**Cas limites :** comparaison d'un établissement avec lui-même (à empêcher), très petit établissement, établissement d'outre-mer, établissement qui est le maximum national.

### Écran C : Vue des inégalités

**Ce que c'est.** Une vue d'ensemble pour le journaliste : la courbe de Lorenz avec l'indice de Gini, et la dépense selon l'IPS et l'éducation prioritaire. Un établissement choisi peut y être mis en évidence.

**États à dessiner :**
- *Vue nationale.*
- *Vue par académie.*
- *Établissement mis en évidence.*
- *Chargement des données.*
- *Mise en page des graphiques sur un petit écran.*

Chaque graphique est accompagné d'une phrase d'explication en langage courant.

## 9. Questions ouvertes et décisions d'architecture

**Questions ouvertes**
1. **Le format des adresses des fiches.** *Recommandation :* l'UAI suivi d'un nom lisible, par exemple `/etablissement/0141796B-lycee-salvador-allende`. L'UAI garantit la stabilité et le nom aide le référencement.
2. **Le regroupement des points** au niveau des établissements, dans les grandes villes. Par défaut, il n'y a pas de regroupement. *Recommandation :* le décider pendant les maquettes, au jalon 2.
3. **L'accessibilité** (contrastes, lecteurs d'écran). Par défaut, rien n'est prévu. *Recommandation :* respecter les règles de base des recommandations d'accessibilité du web (WCAG), niveau AA, pour les contrastes et la navigation au clavier.
4. **Les contributions de données sourcées** (deuxième version). Par exemple, le budget d'un établissement voté en conseil d'administration est un document public, et des parents ou des personnels pourraient l'apporter. Par défaut, ces contributions passent par le formulaire de signalement, avec le champ « source ».

**Décisions d'architecture à créer** (dans `docs/adr/`)
- **ADR-SITE-A : l'outil React qui fabrique les fiches à l'avance**, React Router en mode framework ou Next.js. Statut : à créer.
- **ADR-SITE-B : le framework de l'API Node.js**, Express ou Fastify, et l'outil de fabrication des images. Statut : à créer.
- **ADR-SITE-C : le fond de carte.** Quel fournisseur de tuiles, et combien il coûte en cas de pic de visites. Statut : à créer.

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

- **Les maquettes.** L'agent proposait des maquettes en pages HTML cliquables, qu'il générerait lui-même, pour aller plus vite. Le porteur a choisi son outil externe open design, et une première phase de réflexion sur les données à afficher.
- **La recherche puis la comparaison.** Le porteur a demandé s'il était possible de trouver son établissement, puis de le comparer à un autre de son choix. C'est possible, avec une limite : une image ne peut pas être fabriquée à l'avance pour chacune des 121 millions de paires possibles. D'où la fabrication à la demande par l'API, avec une image de secours.
- **La carte à plusieurs niveaux de zoom.** Elle a été ajoutée à la demande du porteur. L'agent a choisi des cercles pour les communes plutôt que leurs contours, parce que les contours des 35 000 communes seraient trop lourds pour un téléphone.

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
