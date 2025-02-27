import streamlit as st
import pandas as pd

# Load the dataset
data_path = "data_enkn.csv"  # Ensure this file is in your GitHub repo
df = pd.read_csv(data_path)

# Streamlit App Title
st.title("Namma Kisaan - ನಮ್ಮ ಕೃಷಿಕ")

# Layout for Registration & Crop Recommendation
col1, col2 = st.columns(2)

with col1:
    st.header("👤 Farmer Registration - ರೈತರ ನೋಂದಣಿ")
    name = st.text_input("Name / ಹೆಸರು")
    age = st.number_input("Age / ವಯಸ್ಸು", min_value=18, max_value=100, step=1)
    aadhaar = st.text_input("Aadhaar Number / ಆಧಾರ್ ಸಂಖ್ಯೆ")
    ownership = st.radio("Ownership Type / ಮಾಲಿಕತ್ವ", ["Owner / ಮಾಲೀಕ", "Lessee / ಗುತ್ತಿಗೆದಾರ"])
    location = st.text_input("Location / ಸ್ಥಳ")
    plot_size = st.number_input("Plot Size (Acres) / ಜಮೀನು ಗಾತ್ರ (ಎಕರೆ)", min_value=0.1, step=0.1)

with col2:
    st.header("🌱 Crop & Season Suggestion - ಬೆಳೆ ಮತ್ತು ಋತು ಶಿಫಾರಸು")
    soil_type = st.selectbox("Select Soil Type / ಮಣ್ಣಿನ ಪ್ರಕಾರ", df["Soil type"].dropna().unique())
    irrigation = st.selectbox("Select Irrigation Type / ನೀರಾವರಿ ಪ್ರಕಾರ", df["Irrigation"].unique())
    
    # Filter dataset based on user input
    filtered_df = df[(df["Soil type"] == soil_type) & (df["Irrigation"] == irrigation)]
    
    if not filtered_df.empty:
        recommended_crop = filtered_df.iloc[0]["Crops"]
        recommended_season = filtered_df.iloc[0]["Season"]
        st.success(f"✅ Recommended Crop: {recommended_crop}\n🌦️ Best Season: {recommended_season}")
    else:
        st.warning("No matching data found. Try a different selection.")
