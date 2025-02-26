import streamlit as st
import pandas as pd

# Load dataset
def load_data():
    file_path = "data_season.csv"  # Update if needed
    return pd.read_csv(file_path)

df = load_data()

# Registration form
st.title("Namma Kisaan - ನಮ್ಮ ಕೃಷಿ")

with st.form("registration_form"):
    name = st.text_input("Name (ನಾಮ)")
    age = st.number_input("Age (ವಯಸು)", min_value=18, max_value=100)
    aadhaar = st.text_input("Aadhaar Number (ಆಧಾರ ನಂ)")
    owner_type = st.radio("Ownership Type (ಮೂಲೆಕಾ)", ["Owner (ಮಾಲಿಕ)", "Lessee (ಭಾಗೆ)"])
    location = st.text_input("Location (ಸ್ಥಳ)")
    plot_size = st.number_input("Plot Size (Acres) (ಸೀಮೆ)", min_value=0.1)
    submit = st.form_submit_button("Register (ನಂದಾಣೀ)")

if submit:
    st.success("Registered Successfully! (ಅವರ ಜೀವಿಸಿ)")

# Display dataset
st.header("Dataset (ಡೇಟಾಸೆಟ್)")
st.dataframe(df.style.set_properties(**{"background-color": "#f9f9f9", "border": "1px solid black"}))
