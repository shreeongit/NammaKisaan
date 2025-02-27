import streamlit as st
import pandas as pd

def load_data():
    # Load the pre-existing dataset
    file_path = "data_season.csv"  # Ensure this file is in the same directory or adjust the path accordingly
    df = pd.read_csv(file_path)
    return df

def main():
    st.set_page_config(page_title="Namma Kisaan", layout="wide")
    
    st.title("🌾 Namma Kisaan - ನಮ್ಮ ಕಿಸಾನ್ 🌾")
    
    # Sidebar for registration
    st.sidebar.header("👤 Farmer Registration / ರೈತ ನೋಂದಣಿ")
    name = st.sidebar.text_input("Name / ಹೆಸರು")
    age = st.sidebar.number_input("Age / ವಯಸ್ಸು", min_value=18, max_value=100, step=1)
    aadhaar = st.sidebar.text_input("Aadhaar Number / ಆದಾರ್ ಸಂಖ್ಯೆ")
    owner_type = st.sidebar.radio("Ownership Type / ಮಾಲಕತ್ವ ಪ್ರಕಾರ", ["Owner / ಮಾಲೀಕ", "Lessee / ಬಾಡಿಗೆ"])
    location = st.sidebar.text_input("Location / ಸ್ಥಳ")
    plot_size = st.sidebar.number_input("Plot Size (acres) / ಪ್ಲಾಟ್ ಗಾತ್ರ (ಎಕರೆ)", min_value=0.1, step=0.1)
    
    if st.sidebar.button("Register / ನೋಂದಾಯಿಸಿ"):
        st.sidebar.success(f"Registered {name} successfully! / {name} ಯಶಸ್ವಿಯಾಗಿ ನೋಂದಾಯಿಸಲಾಗಿದೆ!")
        
        # Ask for soil type and irrigation type
        st.sidebar.subheader("🌱 Soil and Irrigation Details / ಮಣ್ಣು ಮತ್ತು ನೀರಾವರಿ ವಿವರಗಳು")
        soil_type = st.sidebar.selectbox("Select Soil Type / ಮಣ್ಣಿನ ಪ್ರಕಾರ ಆಯ್ಕೆ ಮಾಡಿ", ["Red Soil", "Black Soil", "Sandy Soil", "Clayey Soil"])
        irrigation_type = st.sidebar.selectbox("Select Irrigation Type / ನೀರಾವರಿ ವಿಧಾನ ಆಯ್ಕೆ ಮಾಡಿ", ["Canal", "Drip", "Sprinkler", "Rainfed"])
        
        # Load dataset
        df = load_data()
        
        # Filter based on soil type and irrigation type
        recommendation = df[(df['Soil type'].str.contains(soil_type, case=False, na=False)) &
                            (df['Irrigation'].str.contains(irrigation_type, case=False, na=False))]
        
        if not recommendation.empty:
            season = recommendation.iloc[0]['Season']
            crop = recommendation.iloc[0]['Crops']
            st.sidebar.write(f"🌾 Recommended Season: {season} / ಶಿಫಾರಸು ಮಾಡಿದ ಹಂಗಾಮು")
            st.sidebar.write(f"🌿 Recommended Crop: {crop} / ಶಿಫಾರಸು ಮಾಡಿದ ಬೆಳೆ")
        else:
            st.sidebar.write("❌ No recommendations available for the selected inputs / ಆಯ್ಕೆ ಮಾಡಿದ ಮಾಹಿತಿಗೆ ಶಿಫಾರಸು ಲಭ್ಯವಿಲ್ಲ")
    
if __name__ == "__main__":
    main()
