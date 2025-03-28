import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim

# Load the dataset
data_path = "data_enkn.csv"  # Ensure this file is in your directory
df = pd.read_csv(data_path)

# Function to get coordinates
def get_coordinates(location):
    geolocator = Nominatim(user_agent="namma_kisaan")
    try:
        loc = geolocator.geocode(location)
        return loc.latitude, loc.longitude if loc else (None, None)
    except:
        return None, None

# Streamlit App Title
st.markdown('<h1 style="text-align: center; color: #4CAF50;">ನಮ್ಮ ಕಿಸಾನ್ - Namma Kisaan</h1>', unsafe_allow_html=True)

# Layout for Registration & Crop Recommendation
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("👤 Farmer Registration - ರೈತರ ನೋಂದಣಿ")
    name = st.text_input("🧑 Name / ಹೆಸರು")
    age = st.number_input("📅 Age / ವಯಸ್ಸು", min_value=18, max_value=100, step=1)
    aadhaar = st.text_input("🔢 Aadhaar Number / ಆಧಾರ್ ಸಂಖ್ಯೆ")
    ownership = st.radio("🏠 Ownership Type / ಮಾಲಿಕತ್ವ", ["Owner / ಮಾಲೀಕ", "Lessee / ಗುತ್ತಿಗೆದಾರ"], horizontal=True)
    location = st.text_input("📍 Location / ಸ್ಥಳ")
    plot_size = st.number_input("📏 Plot Size (Acres) / ಜಮೀನು ಗಾತ್ರ (ಎಕರೆ)", min_value=0.1, step=0.1)

with col2:
    st.subheader("🌱 Crop & Season Suggestion - ಬೆಳೆ ಮತ್ತು ಋತು ಶಿಫಾರಸು")
    soil_type = st.selectbox("🌍 Select Soil Type / ಮಣ್ಣಿನ ಪ್ರಕಾರ", df["Soil type"].dropna().unique())
    irrigation = st.selectbox("💧 Select Irrigation Type / ನೀರಾವರಿ ಪ್ರಕಾರ", df["Irrigation"].unique())
    
    # Filter dataset based on user input
    filtered_df = df[(df["Soil type"] == soil_type) & (df["Irrigation"] == irrigation)]
    
    if not filtered_df.empty:
        recommended_crop = filtered_df.iloc[0]["Crops"]
        recommended_season = filtered_df.iloc[0]["Season"]
        temperature = filtered_df.iloc[0]["Temperature"]
        rainfall = filtered_df.iloc[0]["Rainfall"]
        st.success(f"✅ **Recommended Crop:** {recommended_crop}\n🌦️ **Best Season:** {recommended_season}\n🌡️ **Optimal Temperature:** {temperature}°C\n🌧️ **Required Rainfall:** {rainfall} mm")
    else:
        st.warning("⚠️ No matching data found. Try a different selection.")

# Satellite View Feature
st.subheader("📡 Satellite View of Your Location")
user_location = st.text_input("📍 Enter a location (e.g., city, village, landmark)")

if user_location:
    lat, lon = get_coordinates(user_location)
    if lat and lon:
        st.success(f"Location found: {lat}, {lon}")
        
        # Create a map centered at the given coordinates
        m = folium.Map(location=[lat, lon], zoom_start=15, tiles="Stamen Terrain")
        folium.Marker([lat, lon], popup=user_location, tooltip="📍 Your Location").add_to(m)
        
        # Display the map
        folium_static(m)
    else:
        st.error("Could not retrieve coordinates. Try a different location.")

# Footer
st.markdown("""
    <hr>
    <div style='text-align: center;'>
        <p style='color: white;'>🚀 Built with ❤️ by Namma Kisaan Team</p>
    </div>
""", unsafe_allow_html=True)
