import pickle
from pathlib import Path

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# =====================================================
# Project Paths
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "Housing.csv"
MODEL_PATH = BASE_DIR / "models" / "house_price_model.pkl"

# =====================================================
# Load Dataset
# =====================================================

print("Loading dataset...")

df = pd.read_csv(DATA_PATH)

# =====================================================
# Data Preprocessing
# =====================================================

yes_no_columns = [
    "mainroad",
    "guestroom",
    "basement",
    "hotwaterheating",
    "airconditioning",
    "prefarea"
]

for column in yes_no_columns:
    df[column] = df[column].map({
        "yes": 1,
        "no": 0
    })

df["furnishingstatus"] = df["furnishingstatus"].map({
    "furnished": 2,
    "semi-furnished": 1,
    "unfurnished": 0
})

# =====================================================
# Features & Target
# =====================================================

X = df.drop("price", axis=1)
y = df["price"]

# =====================================================
# Train-Test Split
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =====================================================
# Train Model
# =====================================================

print("Training Random Forest Regressor...")

model = RandomForestRegressor(
    random_state=42
)

model.fit(X_train, y_train)

# =====================================================
# Save Model
# =====================================================

with open(MODEL_PATH, "wb") as file:
    pickle.dump(model, file)

print("\nModel trained successfully!")
print(f"Model saved at:\n{MODEL_PATH}")