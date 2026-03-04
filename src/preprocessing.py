import pandas as pd
import numpy as np
import joblib
from pathlib import Path
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.decomposition import PCA 

# --- 0. Configuration des Chemins ---
PROJECT_PATH = Path("../").resolve()
DATA_PATH = PROJECT_PATH / "data"
OUTPUT_PATH = PROJECT_PATH / "output"
# Création du dossier output s'il n'existe pas
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

DATA_TRAINING_SET_PATH = DATA_PATH / "UNSW_NB15_training-set.csv"

# --- 1. Chargement ---
print("⏳ Chargement des données...")
df_train = pd.read_csv(DATA_TRAINING_SET_PATH)

# --- 2. Sélection des features ---
num_features = ['dur', 'spkts', 'dpkts', 'sbytes', 'dbytes', 'rate', 'sttl', 'dttl']
cat_features = ['proto', 'service', 'state']

# --- 3. Construction de la Pipeline finale ---

# Branche Numérique
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# Branche Catégorielle
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

# Assemblage du preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, num_features),
        ('cat', categorical_transformer, cat_features)
    ]
)

# Pipeline complète avec fixation à 5 composantes
final_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('pca', PCA(n_components=5)) 
])

# --- 4. Entraînement et Transformation ---
print("⏳ Exécution de la Pipeline (Preprocessing + ACP 5)...")
X_reduced = final_pipeline.fit_transform(df_train)

# --- 5. Exportation ---
# On exporte la pipeline (l'objet qui sait transformer les données)
PIPELINE_FILE = OUTPUT_PATH / "preprocessing_pipeline.pkl"
joblib.dump(final_pipeline, PIPELINE_FILE)

# On exporte aussi les données transformées (pour le clustering direct)
DATA_REDUCED_FILE = OUTPUT_PATH / "X_reduced_5.npy"
np.save(DATA_REDUCED_FILE, X_reduced)

print(f"\n✅ Terminé avec succès !")
print(f"📂 Pipeline sauvegardée dans : {PIPELINE_FILE}")
print(f"📊 Données réduites sauvegardées dans : {DATA_REDUCED_FILE}")
print(f"🚀 Forme finale des données : {X_reduced.shape}")