# Dépense publique par élève, établissement par établissement

**Initiative Linear :** https://linear.app/owlaris/initiative/depense-publique-par-eleve-etablissement-par-etablissement-849f6fdc0c44

Ce dossier contient les spécifications du projet. Le projet estime la dépense publique par élève de chaque collège et de chaque lycée public et privé sous contrat de France, outre-mer compris, pour la rentrée 2024. Il la publie sur un site pensé pour le téléphone, afin de rendre visibles les inégalités de moyens entre établissements.

La question à laquelle le site répond est : « Combien dépense-t-on pour moi, par rapport à la moyenne nationale, à l'académie où l'on dépense le plus et à l'établissement où l'on dépense le plus ? »

## Les quatre projets

Les quatre projets avancent en parallèle. Des formats de données figés dès le 14 octobre 2026 le permettent. La première version publique est prévue le 15 novembre 2026.

| Projet | Spécification | Fin prévue |
|---|---|---|
| 1. Inventaire et collecte des données de dépenses | [01-inventaire-collecte-donnees.md](01-inventaire-collecte-donnees.md) | 21 octobre 2026 |
| 2. Modèle de coût par élève et statistiques | [02-modele-cout-statistiques.md](02-modele-cout-statistiques.md) | 1er novembre 2026 |
| 3. Site interactif : carte, fiche établissement et comparaison | [03-site-interactif.md](03-site-interactif.md) | 12 novembre 2026 |
| 4. Publication et diffusion | [04-publication-diffusion.md](04-publication-diffusion.md) | 22 novembre 2026 |

Le projet 1 et le projet 2 ont aussi un jalon pour la deuxième version, le 13 décembre 2026, qui ajoute l'indicateur travaux.

## Comment ces specs sont organisées

Chaque spec est autonome et suit les mêmes onze sections : contexte, mesures de succès, personas, user stories, périmètre, jalons, contexte technique, fiches de design, questions ouvertes, choix contestés et glossaire. Les sections de contexte général, de personas, de choix communs et de glossaire sont identiques dans les quatre specs.

Les décisions d'architecture (ADR) annoncées dans les specs seront écrites dans `docs/adr/` par les tickets qui les mettent en œuvre.
