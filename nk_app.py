import streamlit as st
import pandas as pd

def load_data():
    # Load the pre-existing dataset
    file_path = "data_enkn.xlsx"  # Ensure this file is in the same directory or adjust the path accordingly
    df = pd.read_excel(file_path)
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
    
    # Load dataset
    df = load_data()
    
    # User input for soil type and irrigation
    st.write("### 🌱 Select Your Soil Type and Irrigation / ನಿಮ್ಮ ಮಣ್ಣು ಪ್ರಕಾರ ಮತ್ತು ನೀರಾವರಿ ಆಯ್ಕೆ ಮಾಡಿ")
    soil_types = df['Soil type'].dropna().unique().tolist()
    irrigation_types = df['Irrigation'].dropna().unique().tolist()
    
    selected_soil = st.selectbox("Soil Type / ಮಣ್ಣು ಪ್ರಕಾರ", soil_types)
    selected_irrigation = st.selectbox("Irrigation Type / ನೀರಾವರಿ ಪ್ರಕಾರ", irrigation_types)
    
    if st.button("Get Crop Recommendation / ಬೆಳೆ ಶಿಫಾರಸು ಪಡೆಯಿರಿ"):
        filtered_df = df[(df['Soil type'] == selected_soil) & (df['Irrigation'] == selected_irrigation)]
        
        if not filtered_df.empty:
            selected_entry = filtered_df.iloc[0]  # Pick the first matching entry
            st.write("### 🌾 Recommended Crop and Season / ಶಿಫಾರಸು ಮಾಡಿದ ಬೆಳೆ ಮತ್ತು ಹಂಗಾಮು")
            st.write(f"**Season / ಹಂಗಾಮು:** {selected_entry['Season']}")
            st.write(f"**Crop / ಬೆಳೆ:** {selected_entry['Crops']}")
        else:
            st.write("❌ No matching data found. Please try different inputs. / ಯಾವುದೇ ಹೊಂದಾಣಿಕೆಯ ಡೇಟಾ ಲಭ್ಯವಿಲ್ಲ. ದಯವಿಟ್ಟು ಬೇರೆ ಆಯ್ಕೆಗಳನ್ನು ಪ್ರಯತ್ನಿಸಿ.")
    
if __name__ == "__main__":
    main()
