import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# Load the dataset
data_path = "data_enkn.csv"  # Updated to new dataset

df = pd.read_csv(data_path)

# Mapping of soil types and irrigation methods to Kannada translations
soil_translation = {
    "Alluvial": "ಮೆಕ್ಕಲು",
    "Black": "ಕಪ್ಪು ಮಣ್ಣು",
    "Red": "ಕೆಂಪು ಮಣ್ಣು",
    "Laterite": "ಲೇಟರೈಟ್",
    "Clay": "ಮಣ್ಣಿನ ಮಿಶ್ರಣ",
    "Sandy": "ಮರಳು ಮಣ್ಣು",
    "Loamy": "ಲೋಮಿ ಮಣ್ಣು"
}

irrigation_translation = {
    "Drip": "ತೊಟ್ಟು ನೀರಾವರಿ",
    "Sprinkler": "ಮಿಂಚು ನೀರಾವರಿ",
    "Flood": "ಪೊಕ್ಕಲಿ ನೀರಾವರಿ",
    "Canal": "ಕ್ಯಾನಲ್ ನೀರಾವರಿ",
    "Tube well": "ಟ್ಯೂಬ್ ವೆಲ್ ನೀರಾವರಿ",
    "Rain-fed": "ಮಳೆಯಾಧಾರಿತ"
}

# Custom CSS for a more attractive, app-like UI
st.markdown("""
    <style>
        body {background-color: #121212; color: white;}
        .stApp {background-color: #1E1E1E; padding: 20px; border-radius: 10px; color: white;}
        h1 {color: #4CAF50; text-align: center; font-size: 32px;}
        .header {background-color: #4CAF50; padding: 15px; border-radius: 10px; color: white; text-align: center;}
        .stButton>button {background-color: #4CAF50; color: white; font-size: 18px; border-radius: 8px; padding: 10px;}
        .stRadio>div {color: white;}
        .container {padding: 20px; border-radius: 15px; background: #222; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);}
        .result-box {background: #333; padding: 15px; border-radius: 10px; margin-top: 20px;}
    </style>
""", unsafe_allow_html=True)

# Streamlit App Title
st.markdown('<div class="header"><h1>ನಮ್ಮ ಕೃಷಿಕ - Namma Kisaan</h1></div>', unsafe_allow_html=True)

# Layout for Registration & Crop Recommendation
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("<div class='container'>", unsafe_allow_html=True)
    st.subheader("👤 Farmer Registration - ರೈತರ ನೋಂದಣಿ")
    name = st.text_input("🧑 Name / ಹೆಸರು")
    age = st.number_input("📅 Age / ವಯಸ್ಸು", min_value=18, max_value=100, step=1)
    aadhaar = st.text_input("🔢 Aadhaar Number / ಆಧಾರ್ ಸಂಖ್ಯೆ")
    ownership = st.radio("🏠 Ownership Type / ಮಾಲಿಕತ್ವ", ["Owner / ಮಾಲೀಕ", "Lessee / ಗುತ್ತಿಗೆದಾರ"], horizontal=True)
    location = st.text_input("📍 Location / ಸ್ಥಳ")
    plot_size = st.number_input("📏 Plot Size (Acres) / ಜಮೀನು ಗಾತ್ರ (ಎಕರೆ)", min_value=0.1, step=0.1)
    st.markdown("</div>", unsafe_allow_html=True)
    
with col2:
    st.markdown("<div class='container'>", unsafe_allow_html=True)
    st.subheader("🌱 Crop & Season Suggestion - ಬೆಳೆ ಮತ್ತು ಋತು ಶಿಫಾರಸು")
    soil_options = [f"{soil} / {soil_translation.get(soil, soil)}" for soil in df["Soil type"].dropna().unique()]
    irrigation_options = [f"{irrigation} / {irrigation_translation.get(irrigation, irrigation)}" for irrigation in df["Irrigation"].unique()]
    soil_type = st.selectbox("🌍 Select Soil Type / ಮಣ್ಣಿನ ಪ್ರಕಾರ", soil_options)
    irrigation = st.selectbox("💧 Select Irrigation Type / ನೀರಾವರಿ ಪ್ರಕಾರ", irrigation_options)
    
    # Extracting only English part for filtering
    soil_type_selected = soil_type.split(" / ")[0]
    irrigation_selected = irrigation.split(" / ")[0]
    
    # Filter dataset based on user input
    filtered_df = df[(df["Soil type"] == soil_type_selected) & (df["Irrigation"] == irrigation_selected)]
    
    if not filtered_df.empty:
        recommended_crop = filtered_df.iloc[0]["Crops"]
        recommended_season = filtered_df.iloc[0]["Season"]
        temperature = filtered_df.iloc[0]["Temperature"]
        rainfall = filtered_df.iloc[0]["Rainfall"]
        st.markdown("<div class='result-box'>", unsafe_allow_html=True)
        st.success(f"✅ **Recommended Crop:** {recommended_crop}\n🌦️ **Best Season:** {recommended_season}\n🌡️ **Optimal Temperature:** {temperature}°C\n🌧️ **Required Rainfall:** {rainfall} mm")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ No matching data found. Try a different selection.")
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <hr>
    <div style='text-align: center;'>
        <p style='color: white;'>🚀 Built with ❤️ by Namma Kisaan Team</p>
    </div>
""", unsafe_allow_html=True)
