import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from some_satellite_api import get_satellite_image, classify_image, detect_water_bodies, assess_water_quality

# Load dataset
data_path = "data_enkn.csv"
df = pd.read_csv(data_path)

# Custom CSS
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

# Layout
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("👤 Farmer Registration - ರೈತರ ನೋಂದಣಿ")
    name = st.text_input("🧑 Name / ಹೆಸರು")
    age = st.number_input("📅 Age / ವಯಸ್ಸು", min_value=18, max_value=100, step=1)
    aadhaar = st.text_input("🔢 Aadhaar Number / ಆಧಾರ್ ಸಂಖ್ಯೆ")
    ownership = st.radio("🏠 Ownership Type / ಮಾಲಿಕತ್ವ", ["Owner / ಮಾಲೀಕ", "Lessee / ಗುತ್ತಿಗೆದಾರ"], horizontal=True)
    location = st.text_input("📍 Location / ಸ್ಥಳ")
    plot_size = st.number_input("📏 Plot Size (Acres) / ಜಮೀನು ಗಾತ್ರ (ಎಕರೆ)", min_value=0.1, step=0.1)
    
    if location:
        st.subheader("🛰️ Satellite Data Analysis")
        sat_image = get_satellite_image(location)
        water_bodies = detect_water_bodies(sat_image)
        water_quality = assess_water_quality(water_bodies)
        classification = classify_image(sat_image)
        
        st.image(sat_image, caption="Satellite Image", use_column_width=True)
        st.write("🌊 Nearby Water Bodies:", water_bodies)
        st.write("💧 Water Quality:", water_quality)
        st.write("🏙️ Land Classification:", classification)
        
        # Show location on map
        map_ = folium.Map(location=[lat, lon], zoom_start=12)
        folium.Marker([lat, lon], popup="Selected Location").add_to(map_)
        folium_static(map_)

with col2:
    st.subheader("🌱 Crop & Season Suggestion - ಬೆಳೆ ಮತ್ತು ಋತು ಶಿಫಾರಸು")
    soil_type = st.selectbox("🌍 Select Soil Type / ಮಣ್ಣಿನ ಪ್ರಕಾರ", df["Soil type"].dropna().unique())
    irrigation = st.selectbox("💧 Select Irrigation Type / ನೀರಾವರಿ ಪ್ರಕಾರ", df["Irrigation"].unique())
    
    # Filter dataset
    filtered_df = df[(df["Soil type"] == soil_type) & (df["Irrigation"] == irrigation)]
    
    if not filtered_df.empty:
        recommended_crop = filtered_df.iloc[0]["Crops"]
        recommended_season = filtered_df.iloc[0]["Season"]
        temperature = filtered_df.iloc[0]["Temperature"]
        rainfall = filtered_df.iloc[0]["Rainfall"]
        st.success(f"✅ **Recommended Crop:** {recommended_crop}\n🌦️ **Best Season:** {recommended_season}\n🌡️ **Optimal Temperature:** {temperature}°C\n🌧️ **Required Rainfall:** {rainfall} mm")
    else:
        st.warning("⚠️ No matching data found. Try a different selection.")

# Footer
st.markdown("""
    <hr>
    <div style='text-align: center;'>
        <p style='color: white;'>🚀 Built with ❤️ by Namma Kisaan Team</p>
    </div>
""", unsafe_allow_html=True)
