import pickle
from pathlib import Path
import numpy as np

# ==========================================
# Project Paths
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "house_price_model.pkl"

# ==========================================
# Load Model
# ==========================================

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


# ==========================================
# Prediction Function
# ==========================================

def predict_price(
    area,
    bedrooms,
    bathrooms,
    stories,
    mainroad,
    guestroom,
    basement,
    hotwaterheating,
    airconditioning,
    parking,
    prefarea,
    furnishingstatus
):

    features = np.array([[
        area,
        bedrooms,
        bathrooms,
        stories,
        mainroad,
        guestroom,
        basement,
        hotwaterheating,
        airconditioning,
        parking,
        prefarea,
        furnishingstatus
    ]])

    prediction = model.predict(features)

    return prediction[0]