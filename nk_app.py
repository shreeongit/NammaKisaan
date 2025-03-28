import streamlit as st
import pandas as pd

# Load the dataset
data_path = "data_enkn.csv"  # Ensure this file is in your GitHub repo
df = pd.read_csv(data_path)

# Custom CSS for Styling
st.markdown("""
    <style>
        body {background-color: #121212; color: white;}
        .stApp {background-color: #1E1E1E; padding: 20px; border-radius: 10px; color: white;}
        h1 {color: #4CAF50; text-align: center;}
        .header {background-color: #4CAF50; padding: 10px; border-radius: 10px; color: white; text-align: center;}
        .stButton>button {background-color: #4CAF50; color: white; font-size: 18px; border-radius: 8px; padding: 10px;}
        .stRadio>div {color: white;}
    </style>
""", unsafe_allow_html=True)

# Streamlit App Title
st.markdown('<div class="header"><h1>ನಮ್ಮ ಕೃಷಿಕ - Namma Kisaan</h1></div>', unsafe_allow_html=True)

# Layout for Registration & Crop Recommendation
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("👤 Farmer Registration - ರೈತರ ನೋಂದಣಿ")
    name = st.text_input("🧑 Name / ಹೆಸರು")
    age = st.number_input("📅 Age / ವಯಸ್ಸು", min_value=18, max_value=100, step=1)
    aadhaar = st.text_input("🔢 Aadhaar Number / ಆಧಾರ್ ಸಂಖ್ಯೆ")
    ownership = st.radio("🏠 Ownership Type / ಮಾಲಿಕತ್ವ", ["Owner / ಮಾಲೀಕ", "Lessee / ಗುತ್ತಿಗೆದಾರ"], horizontal=True)
    location = st.text_input("📍 Enter Location / ಸ್ಥಳ")
    plot_size = st.number_input("📏 Plot Size (Acres) / ಜಮೀನು ಗಾತ್ರ (ಎಕರೆ)", min_value=0.1, step=0.1)
    
    # Get soil and irrigation type based on location
    location_data = df[df["Location"] == location]
    if not location_data.empty:
        soil_type = location_data.iloc[0]["Soil type"]
        irrigation = location_data.iloc[0]["Irrigation"]
        st.info(f"🌍 **Soil Type:** {soil_type}\n💧 **Irrigation Type:** {irrigation}")
    else:
        st.warning("⚠️ Location not found in database. Please enter a valid location.")
        soil_type, irrigation = None, None

with col2:
    st.subheader("🌱 Crop & Season Suggestion - ಬೆಳೆ ಮತ್ತು ಋತು ಶಿಫಾರಸು")
    
    if soil_type and irrigation:
        filtered_df = df[(df["Soil type"] == soil_type) & (df["Irrigation"] == irrigation)]
        
        if not filtered_df.empty:
            recommended_crop = filtered_df.iloc[0]["Crops"]
            recommended_season = filtered_df.iloc[0]["Season"]
            temperature = filtered_df.iloc[0]["Temperature"]
            rainfall = filtered_df.iloc[0]["Rainfall"]
            st.success(f"✅ **Recommended Crop:** {recommended_crop}\n🌦️ **Best Season:** {recommended_season}\n🌡️ **Optimal Temperature:** {temperature}°C\n🌧️ **Required Rainfall:** {rainfall} mm")
        else:
            st.warning("⚠️ No matching data found for this location.")
    else:
        st.warning("🔍 Enter a valid location to get soil and irrigation details.")

# Footer
st.markdown("""
    <hr>
    <div style='text-align: center;'>
        <p style='color: white;'>🚀 Built with ❤️ by Namma Kisaan Team</p>
    </div>
""", unsafe_allow_html=True)
