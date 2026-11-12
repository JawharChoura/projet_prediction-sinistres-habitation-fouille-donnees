# projet_assurance_carthage.py
"""
Projet Assurance - Carthage Assurances
Prédiction de sinistres habitation
Fouille de Données 2025-2026
"""

# ====================
# IMPORTS
# ====================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.impute import SimpleImputer
warnings.filterwarnings('ignore')

# Configuration des styles
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

# ====================
# FONCTIONS UTILITAIRES
# ====================
def impute_mode(df, col):
    """Impute les valeurs manquantes avec le mode"""
    imputer = SimpleImputer(strategy='most_frequent')
    df[[col]] = imputer.fit_transform(df[[col]])
    return df

def impute_median(df, col):
    """Impute les valeurs manquantes avec la médiane"""
    imputer = SimpleImputer(strategy='median')
    df[[col]] = imputer.fit_transform(df[[col]])
    return df

def boxplot_treatment(df, col_name, min_threshold=None):
    """
    Traitement des outliers
    """
    if col_name not in df.columns:
        return df
    
    Q1 = df[col_name].quantile(0.25)
    Q3 = df[col_name].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR
    
    if min_threshold is not None:
        lower_limit = max(lower_limit, min_threshold)
    
    df[col_name] = np.where(df[col_name] < lower_limit, lower_limit, df[col_name])
    df[col_name] = np.where(df[col_name] > upper_limit, upper_limit, df[col_name])
    
    return df

# ====================
# 1. CHARGEMENT DES DONNÉES
# ====================
print("="*70)
print("🏠 PROJET ASSURANCE - CARTHAGE ASSURANCES")
print("="*70)

# CORRECTION : Chargement avec decimal="," pour les virgules décimales
train = pd.read_csv("train_Insurance.csv", sep=";", decimal=",")
test = pd.read_csv("test_Insurance.csv", sep=";", decimal=",")

print("✅ Données chargées avec succès !")
print(f"\n📊 Dimensions :")
print(f"Train : {train.shape[0]} observations × {train.shape[1]} variables")
print(f"Test  : {test.shape[0]} observations × {test.shape[1]} variables")

# ====================
# 2. APERÇU DES DONNÉES
# ====================
print("\n" + "="*70)
print("2. APERÇU DES DONNÉES")
print("="*70)

print("\n📋 5 premières lignes du dataset TRAIN :")
print(train.head())

print("\n📋 5 premières lignes du dataset TEST :")
print(test.head())

# ====================
# 3. ANALYSE DES VALEURS MANQUANTES
# ====================
print("\n" + "="*70)
print("3. ANALYSE DES VALEURS MANQUANTES")
print("="*70)

print("\n🔍 Valeurs manquantes - TRAIN :")
missing_train = train.isnull().sum()
missing_percent_train = (missing_train / len(train) * 100).round(2)
missing_df_train = pd.DataFrame({
    'Valeurs manquantes': missing_train,
    '%': missing_percent_train
})
print(missing_df_train[missing_df_train['Valeurs manquantes'] > 0])

print("\n🔍 Valeurs manquantes - TEST :")
missing_test = test.isnull().sum()
missing_percent_test = (missing_test / len(test) * 100).round(2)
missing_df_test = pd.DataFrame({
    'Valeurs manquantes': missing_test,
    '%': missing_percent_test
})
print(missing_df_test[missing_df_test['Valeurs manquantes'] > 0])

# ====================
# 4. ANALYSE DE LA VARIABLE CIBLE
# ====================
print("\n" + "="*70)
print("4. ANALYSE DE LA VARIABLE CIBLE (CLAIM)")
print("="*70)

# Distribution de la variable cible
claim_dist = train['claim'].value_counts()
claim_percent = train['claim'].value_counts(normalize=True) * 100

print(f"\n📈 Distribution des sinistres :")
print(f"Non : {claim_dist.get('non', 0)} ({claim_percent.get('non', 0):.1f}%)")
print(f"Oui : {claim_dist.get('oui', 0)} ({claim_percent.get('oui', 0):.1f}%)")

# Visualisation
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Graphique à barres
axes[0].bar(claim_dist.index, claim_dist.values, color=['#3498db', '#e74c3c'])
axes[0].set_title('Distribution des sinistres', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Sinistre')
axes[0].set_ylabel('Nombre')
axes[0].grid(True, alpha=0.3)

# Graphique en camembert
axes[1].pie(claim_dist.values, labels=claim_dist.index, autopct='%1.1f%%', 
           colors=['#3498db', '#e74c3c'], explode=(0, 0.1))
axes[1].set_title('Proportion des sinistres', fontsize=14, fontweight='bold')

plt.suptitle('Analyse de la variable cible', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

# ====================
# 5. TRAITEMENT DES DONNÉES
# ====================
print("\n" + "="*70)
print("5. TRAITEMENT DES DONNÉES")
print("="*70)

# CORRECTION : Traitement de window_count
print("\n🔄 Traitement de window_count...")
train["window_count"] = train["window_count"].replace("without", "0").replace(">=10", "10")
test["window_count"] = test["window_count"].replace("without", "0").replace(">=10", "10")
train["window_count"] = pd.to_numeric(train["window_count"], errors='coerce')
test["window_count"] = pd.to_numeric(test["window_count"], errors='coerce')

print(f"✅ window_count converti en numérique")
print(f"   Valeurs uniques dans train : {sorted(train['window_count'].dropna().unique()[:10])}")

# Imputation des valeurs manquantes pour train
print("\n🔄 Imputation des valeurs manquantes - TRAIN...")
mode_cols = ['year', 'coverage_period', 'is_residential', 
             'is_finished_and_fenced', 'has_garden', 'locality', 
             'structure_type', 'Geo_Code']

for col in mode_cols:
    if col in train.columns:
        train = impute_mode(train, col)

median_cols = ['area_m2', 'window_count']
for col in median_cols:
    if col in train.columns:
        train = impute_median(train, col)

# Supprimer les lignes où claim est manquant
train = train.dropna(subset=['claim'])

# Imputation des valeurs manquantes pour test
print("🔄 Imputation des valeurs manquantes - TEST...")
mode_cols_test = ['has_garden', 'Geo_Code']
for col in mode_cols_test:
    if col in test.columns:
        test = impute_mode(test, col)

median_cols_test = ['area_m2']
for col in median_cols_test:
    if col in test.columns:
        test = impute_median(test, col)

# CORRECTION : Traitement de risk_score
print("\n🔍 Analyse de risk_score...")
if train['risk_score'].isnull().all() or (train['risk_score'].isnull().sum() / len(train) > 0.9):
    print("❌ risk_score supprimé (trop de valeurs manquantes)")
    train.drop(columns=['risk_score'], inplace=True)
    test.drop(columns=['risk_score'], inplace=True)
else:
    print("⚠️  risk_score gardé pour analyse")

# CORRECTION : Traitement de Geo_Code
print("\n🔄 Traitement de Geo_Code...")
# Convertir en numérique (gestion des erreurs)
train['Geo_Code'] = pd.to_numeric(train['Geo_Code'], errors='coerce')
test['Geo_Code'] = pd.to_numeric(test['Geo_Code'], errors='coerce')

# Remplacer les NaN par la médiane
train['Geo_Code'] = train['Geo_Code'].fillna(train['Geo_Code'].median())
test['Geo_Code'] = test['Geo_Code'].fillna(test['Geo_Code'].median())

# Discrétisation
try:
    enc = KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='quantile')
    train['Geo_Code'] = enc.fit_transform(train[['Geo_Code']])
    test['Geo_Code'] = enc.transform(test[['Geo_Code']])
    print("✅ Geo_Code discrétisé en 10 catégories")
except Exception as e:
    print(f"⚠️  Erreur lors de la discrétisation : {e}")

# ====================
# 6. ANALYSE DES VARIABLES NUMÉRIQUES
# ====================
print("\n" + "="*70)
print("6. ANALYSE DES VARIABLES NUMÉRIQUES")
print("="*70)

# Identifier les variables numériques
numerical_cols = train.select_dtypes(include=['int64', 'float64']).columns.tolist()
print(f"\n📊 Variables numériques : {numerical_cols}")

# Statistiques descriptives
print("\n📈 Statistiques descriptives des variables numériques :")
print(train[numerical_cols].describe())

# Visualisation des distributions
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for idx, col in enumerate(numerical_cols[:6]):
    sns.histplot(data=train, x=col, kde=True, ax=axes[idx], bins=30)
    axes[idx].set_title(f'Distribution de {col}', fontweight='bold')
    axes[idx].set_xlabel(col)
    axes[idx].set_ylabel('Fréquence')

plt.suptitle('Distributions des variables numériques', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

# ====================
# 7. DÉTECTION ET TRAITEMENT DES OUTLIERS
# ====================
print("\n" + "="*70)
print("7. DÉTECTION ET TRAITEMENT DES OUTLIERS")
print("="*70)

# Boxplots avant traitement
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for idx, col in enumerate(numerical_cols[:6]):
    sns.boxplot(data=train, y=col, ax=axes[idx])
    axes[idx].set_title(f'Boxplot de {col} (avant traitement)', fontweight='bold')
    axes[idx].set_ylabel(col)

plt.suptitle('Détection des outliers (avant traitement)', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

# Traitement des outliers pour area_m2
print("\n🔄 Traitement des outliers pour area_m2...")
train = boxplot_treatment(train, 'area_m2', min_threshold=10)
test = boxplot_treatment(test, 'area_m2', min_threshold=10)
print("✅ Outliers traités")

# Boxplots après traitement
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

sns.boxplot(data=train, y='area_m2', ax=axes[0])
axes[0].set_title('area_m2 après traitement', fontweight='bold')
axes[0].set_ylabel('Superficie (m²)')

sns.histplot(data=train, x='area_m2', kde=True, ax=axes[1], bins=30)
axes[1].set_title('Distribution de area_m2 après traitement', fontweight='bold')
axes[1].set_xlabel('Superficie (m²)')
axes[1].set_ylabel('Fréquence')

plt.suptitle('Variable area_m2 après traitement des outliers', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

# ====================
# 8. ANALYSE DES VARIABLES CATÉGORIELLES
# ====================
print("\n" + "="*70)
print("8. ANALYSE DES VARIABLES CATÉGORIELLES")
print("="*70)

# Identifier les variables catégorielles
categorical_cols = train.select_dtypes(include=['object']).columns.tolist()
print(f"\n📊 Variables catégorielles : {categorical_cols}")

# Analyser les principales variables catégorielles
key_categorical = ['structure_type', 'locality', 'is_finished_and_fenced', 'has_garden']

fig, axes = plt.subplots(2, 2, figsize=(15, 10))
axes = axes.flatten()

for idx, col in enumerate(key_categorical):
    value_counts = train[col].value_counts()
    axes[idx].bar(value_counts.index, value_counts.values)
    axes[idx].set_title(f'Distribution de {col}', fontweight='bold')
    axes[idx].set_xlabel(col)
    axes[idx].set_ylabel('Fréquence')
    axes[idx].tick_params(axis='x', rotation=45)

plt.suptitle('Distribution des variables catégorielles', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

# ====================
# 9. ANALYSE DES RELATIONS AVEC LA TARGET
# ====================
print("\n" + "="*70)
print("9. ANALYSE DES RELATIONS AVEC LA TARGET")
print("="*70)

# Variables catégorielles vs claim
print("\n📊 Taux de sinistre par variable catégorielle :")

fig, axes = plt.subplots(2, 2, figsize=(15, 10))
axes = axes.flatten()

for idx, col in enumerate(key_categorical):
    # Calculer les proportions
    cross_tab = pd.crosstab(train[col], train['claim'], normalize='index') * 100
    
    # Tracer
    cross_tab.plot(kind='bar', ax=axes[idx], color=['#3498db', '#e74c3c'])
    axes[idx].set_title(f'Taux de sinistre par {col}', fontweight='bold')
    axes[idx].set_xlabel(col)
    axes[idx].set_ylabel('Pourcentage (%)')
    axes[idx].legend(title='Claim')
    axes[idx].tick_params(axis='x', rotation=45)
    
    print(f"\n{col} :")
    print(cross_tab.round(1))

plt.suptitle('Relation entre variables catégorielles et sinistres', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

# Variables numériques vs claim
print("\n📊 Analyse des variables numériques par rapport à claim :")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
key_numerical = ['area_m2', 'window_count', 'year', 'Geo_Code']

for idx, col in enumerate(key_numerical):
    if col in train.columns:
        sns.boxplot(data=train, x='claim', y=col, ax=axes[idx//2, idx%2])
        axes[idx//2, idx%2].set_title(f'{col} vs Claim', fontweight='bold')
        axes[idx//2, idx%2].set_xlabel('Sinistre')
        axes[idx//2, idx%2].set_ylabel(col)

plt.suptitle('Variables numériques vs sinistres', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

# ====================
# 10. MATRICE DE CORRÉLATION
# ====================
print("\n" + "="*70)
print("10. MATRICE DE CORRÉLATION")
print("="*70)

# Sélectionner les variables numériques pertinentes
correlation_cols = [col for col in numerical_cols if col not in ['policy_id'] and train[col].nunique() > 1]

if len(correlation_cols) > 1:
    corr_matrix = train[correlation_cols].corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, fmt='.2f', 
                square=True, linewidths=0.5, cbar_kws={"shrink": 0.8})
    plt.title('Matrice de corrélation des variables numériques', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()
    
    print("\n🔍 Corrélations les plus fortes (absolue) :")
    corr_pairs = corr_matrix.unstack().sort_values(key=abs, ascending=False)
    # Filtrer les auto-corrélations et les doublons
    unique_corr_pairs = corr_pairs[~corr_pairs.index.duplicated(keep='first')]
    unique_corr_pairs = unique_corr_pairs[unique_corr_pairs != 1.0]
    print(unique_corr_pairs.head(10))
else:
    print("⚠️  Pas assez de variables numériques pour la matrice de corrélation")

# ====================
# 11. VÉRIFICATION FINALE
# ====================
print("\n" + "="*70)
print("11. VÉRIFICATION FINALE")
print("="*70)

print(f"\n✅ TRAITEMENT TERMINÉ AVEC SUCCÈS !")
print(f"\n📐 Dimensions finales :")
print(f"Train : {train.shape}")
print(f"Test  : {test.shape}")

print(f"\n✅ Valeurs manquantes finales :")
print("Train :", train.isnull().sum().sum(), "valeurs manquantes")
print("Test  :", test.isnull().sum().sum(), "valeurs manquantes")

print(f"\n📊 Aperçu des données traitées (5 premières lignes) :")
print(train.head())

print(f"\n📈 Statistiques finales des variables numériques :")
print(train[numerical_cols].describe().round(2))

print(f"\n🎯 Distribution finale de la target :")
final_claim_dist = train['claim'].value_counts(normalize=True) * 100
print(f"Non : {final_claim_dist.get('non', 0):.1f}%")
print(f"Oui : {final_claim_dist.get('oui', 0):.1f}%")

print("\n" + "="*70)
print("📋 RÉSUMÉ DES CORRECTIONS EFFECTUÉES :")
print("="*70)
print("1. ✅ Chargement avec decimal=\",\" pour les virgules décimales")
print("2. ✅ Traitement correct de window_count (conversion numérique)")
print("3. ✅ Analyse de risk_score avant suppression")
print("4. ✅ Gestion robuste de Geo_Code (valeurs non-numériques)")
print("5. ✅ Traitement des outliers pour area_m2")
print("6. ✅ Visualisations complètes et informatives")
print("7. ✅ Analyses statistiques détaillées")
print("\n🎉 Les données sont maintenant prêtes pour la modélisation !")

# Sauvegarde des données traitées
train.to_csv('train_traite.csv', index=False)
test.to_csv('test_traite.csv', index=False)
print(f"\n💾 Données sauvegardées : 'train_traite.csv' et 'test_traite.csv'")