# Générateur d'élections

Ce programme sert à générer des questionnaires pour Limesurvey (format .lss) pour les élections de l'AGEG. Ceci ce fait en lui passant en entrée un classeur avec les candidatures.

## Rouler avec Docker
Savoir plus sur Docker : https://www.docker.com/why-docker
### Si vous faites les élections de l'AGEG : 
Avant tout il faut avoir les csv des inscriptions dans `/example`. Il vous fait `admin.csv` et `executif.csv`. Ensuite vous pouvez faire : 

```
    docker build -t ageg-election .
    docker run -i ageg-election /bin/bash -c 'cat result/ageg-survey.lss' > $PWD/result/ageg-survey.lss
```

### Si vous faites les élections de promo : 
Avant tout il faut avoir les csv des inscriptions dans `/example`. Il vous fait `Candidatures.csv` Ensuite vous pouvez faire : 

```
    docker build -t ageg-election .
    docker run -i ageg-election /bin/bash -c 'cat result/finissante-survey.lss' > $PWD/result/finissante-survey.lss
```

## Setup environnement

Le script a été développé avec Python 3.6. Exécutez la commande suivante pour créer un environnement virtuel.

```python3.6 -m venv venv```

## Dépendances

Toutes les dépendances sont dans le fichier requirements. Il suffit de les installer.

```pip install -r requirements.txt```

# AGEG

## Préparation

Vous aurez besoin de deux fichiers .csv pour générer les deux sections du formulaire. Le CSV pour l'exécutif doit avoir les colonnes ci-bas et se nommer *example/executif.csv*.

Nom Usuel | Concentration | Promotion | Poste Visé | Photo | Texte descriptif
----------|---------------|-----------|------------|-------|-----------------

Le second fichier, pour le conseil d'administration, doit se nommer *example/admin.csv* et comporter les colonnes suivantes. La seule colonne de l'autre CSV qui ne se trouve pas dans celui-ci est *Poste Visé*.

Nom Usuel | Concentration | Promotion | Photo | Texte descriptif
----------|---------------|-----------|-------|-----------------

## Exécution

Exécutez le fichier *ageg.py* avec Python.

```python ageg.py```

# Finissante
Template : https://docs.google.com/forms/d/1cK_dzTf8hwymZAxEGyuokbktFlXucpTPfzxWo_52Ejs/edit?usp=sharing

## Préparation

Vous devez mettre un fichier CSV qui doit se nommer *example/Candidatures.csv* et comporter les colonnes suivantes.

Nom Usuel | Concentration | Poste visé #1 | Poste visé #2 | Poste visé #3 | Photo_URL | Texte descriptif
----------|---------------|---------------|---------------|---------------|-------|-----------------

## Exécution

Exécutez le fichier *finissante.py* avec Python.

```python finissante.py```

# Limesurvey (Importer)

Le formualire généré à *result/survey.lss*. Suivez les instructions suivantes pour l'importer dans Limesurvey: https://manual.limesurvey.org/Surveys_-_introduction#Import_a_survey

## Resultat de Finissante
Pour avoir les résultats de la finissante après un sondage il faut exporter les résultats en CSV. Vous pouvez suivre cela : https://manual.limesurvey.org/Exporting_results. Ensuite il faut mettre les résultats dans `/example` avec le nom `results.csv`. Vous pouvez ensuite utiliser phyton 3 directement sur votre ordinateur ou utiliser votre image Docker en changent le Dockerfile avec : `RUN python result.py`. Le résultat sera imprimé dans la console.
