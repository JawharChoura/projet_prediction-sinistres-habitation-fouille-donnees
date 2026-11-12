# Prédiction des sinistres habitation par fouille de données

Projet universitaire de **fouille de données** réalisé sur des contrats d’assurance habitation.  
L’objectif est d’explorer les caractéristiques des biens assurés et d’étudier les facteurs associés à la présence d’un sinistre (`claim`).

## Présentation

Le projet couvre les étapes principales d’un cycle d’analyse de données :

- chargement et exploration des jeux de données d’assurance ;
- analyse des valeurs manquantes et des distributions ;
- traitement des variables catégorielles et numériques ;
- imputation des valeurs manquantes ;
- traitement des valeurs aberrantes ;
- discrétisation de `Geo_Code` ;
- analyse des relations entre les variables et la cible `claim` ;
- visualisations statistiques ;
- comparaison de modèles de classification, notamment **Random Forest** ;
- évaluation avec l’accuracy, les matrices de confusion et les rapports de classification.

## Nom recommandé du dépôt

**`prediction-sinistres-habitation-fouille-donnees`**

Description courte à utiliser sur GitHub :

> Analyse et prédiction des sinistres habitation avec Python, pandas, seaborn et scikit-learn.

## Contenu du dépôt

| Fichier | Description |
| --- | --- |
| [`projet.py`](projet.py) | Analyse exploratoire et préparation complète des données |
| [`projetDM1.py`](projetDM1.py) | Expérimentations de classification et comparaison de modèles |
| [`projetDM.ipynb`](projetDM.ipynb) | Version notebook de l’analyse |
| [`projetDM1.ipynb`](projetDM1.ipynb) | Version notebook détaillée et commentée |
| [`Enoncé_projet_DM.pdf`](Enoncé_projet_DM.pdf) | Énoncé du projet |

## Données nécessaires

Les scripts attendent deux fichiers CSV à placer à la racine du projet :

- `train_Insurance.csv` : données d’apprentissage avec la colonne cible `claim` ;
- `test_Insurance.csv` : données de test.

Les fichiers de données ne sont pas inclus dans ce dépôt. Ils peuvent contenir des informations sensibles ou être soumis à des restrictions de diffusion. Les noms de colonnes utilisés par l’analyse incluent notamment `policy_id`, `year`, `coverage_period`, `area_m2`, `window_count`, `risk_score`, `Geo_Code` et `claim`.

## Installation

Python 3.10 ou une version plus récente est recommandé.

```bash
python -m venv .venv
```

Activation sous Windows PowerShell :

```powershell
.\.venv\Scripts\Activate.ps1
```

Installation des dépendances :

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

## Exécution

Après avoir placé les deux fichiers CSV requis dans le dossier du projet :

```bash
python projet.py
```

Pour exécuter la version de classification :

```bash
python projetDM1.py
```

Pour ouvrir les notebooks :

```bash
jupyter notebook
```

Les scripts affichent les résultats et les graphiques. `projet.py` génère également `train_traite.csv` et `test_traite.csv` après le prétraitement.

## Méthodologie

1. Importation des données d’assurance.
2. Diagnostic des valeurs manquantes et des types de variables.
3. Conversion de `window_count` en variable numérique.
4. Imputation par le mode ou la médiane selon le type de variable.
5. Conversion et discrétisation de `Geo_Code`.
6. Traitement des valeurs aberrantes de `area_m2`.
7. Encodage des variables catégorielles.
8. Séparation des variables explicatives et de la cible `claim`.
9. Entraînement et comparaison de modèles de classification.
10. Évaluation des performances et interprétation des résultats.

## Limites et bonnes pratiques

- Les performances dépendent de la qualité et de la représentativité des données fournies.
- L’accuracy seule ne suffit pas si les classes `oui` et `non` sont déséquilibrées ; il faut aussi consulter la précision, le rappel, le score F1 et la matrice de confusion.
- Les fichiers CSV et les sorties générées doivent être vérifiés avant publication afin d’éviter de diffuser des données confidentielles.
- Les résultats sont destinés à un usage pédagogique et ne constituent pas une décision automatisée d’assurance.

## Technologies

Python · Jupyter · pandas · NumPy · Matplotlib · Seaborn · scikit-learn

