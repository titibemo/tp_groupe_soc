from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

PROJECT_PATH = Path(__file__).parent.parent.resolve()
DATA_PATH = PROJECT_PATH / "data"
OUTPUT_PATH = PROJECT_PATH / "output"
DATA_TRAINING_SET_PATH = DATA_PATH / "UNSW_NB15_training-set.csv"
PIPELINE_FILE = OUTPUT_PATH / "preprocessing_pipeline.pkl"
DATA_REDUCED_FILE = OUTPUT_PATH / "X_reduced_5.npy"

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)


print("Chargement des données...")
df_train = pd.read_csv(DATA_TRAINING_SET_PATH)
print(f"Forme initiale des données : {df_train.shape}")

num_features = df_train.select_dtypes(include=np.number).columns.to_list()
cat_features = df_train.select_dtypes(include=["object", str]).columns.to_list()

numeric_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", MinMaxScaler()),
    ]
)

categorical_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
        ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, num_features),
        ("cat", categorical_transformer, cat_features),
    ]
)

n_components = 6

final_pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("pca", PCA(n_components=n_components)),
    ]
)

print(f"Exécution de la Pipeline (Preprocessing + ACP {n_components})...")
X_reduced = final_pipeline.fit_transform(df_train)

joblib.dump(final_pipeline, PIPELINE_FILE)
np.save(DATA_REDUCED_FILE, X_reduced)

print("Terminé avec succès")
print(f"Pipeline sauvegardée dans : {PIPELINE_FILE}")
print(f"Données réduites sauvegardées dans : {DATA_REDUCED_FILE}")
print(f"Forme finale des données : {X_reduced.shape}")
