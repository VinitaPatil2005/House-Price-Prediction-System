import streamlit as st
from predict import predict_price

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction System")

st.write("Enter the house details below to predict the estimated price.")

st.divider()

# ==========================================
# User Inputs
# ==========================================

area = st.number_input(
    "Area (sq. ft.)",
    min_value=500,
    max_value=20000,
    value=5000
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)

stories = st.number_input(
    "Stories",
    min_value=1,
    max_value=5,
    value=2
)

parking = st.number_input(
    "Parking Spaces",
    min_value=0,
    max_value=5,
    value=1
)

mainroad = st.selectbox(
    "Main Road",
    ["Yes", "No"]
)

guestroom = st.selectbox(
    "Guest Room",
    ["Yes", "No"]
)

basement = st.selectbox(
    "Basement",
    ["Yes", "No"]
)

hotwaterheating = st.selectbox(
    "Hot Water Heating",
    ["Yes", "No"]
)

airconditioning = st.selectbox(
    "Air Conditioning",
    ["Yes", "No"]
)

prefarea = st.selectbox(
    "Preferred Area",
    ["Yes", "No"]
)

furnishingstatus = st.selectbox(
    "Furnishing Status",
    [
        "Furnished",
        "Semi-Furnished",
        "Unfurnished"
    ]
)

# ==========================================
# Encoding
# ==========================================

mainroad = 1 if mainroad == "Yes" else 0
guestroom = 1 if guestroom == "Yes" else 0
basement = 1 if basement == "Yes" else 0
hotwaterheating = 1 if hotwaterheating == "Yes" else 0
airconditioning = 1 if airconditioning == "Yes" else 0
prefarea = 1 if prefarea == "Yes" else 0

if furnishingstatus == "Furnished":
    furnishingstatus = 2
elif furnishingstatus == "Semi-Furnished":
    furnishingstatus = 1
else:
    furnishingstatus = 0

# ==========================================
# Prediction
# ==========================================

if st.button("Predict House Price"):

    predicted_price = predict_price(
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
    )

    st.success(
        f"Estimated House Price: ₹ {predicted_price:,.2f}"
    )