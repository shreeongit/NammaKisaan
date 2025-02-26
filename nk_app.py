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
    
        # Load dataset
        df = load_data()
        
        if location:
            filtered_df = df[df['Location'].str.contains(location, case=False, na=False)]
            if not filtered_df.empty:
                st.write("### 📊 Information for Location / ಸ್ಥಳಕ್ಕಾಗಿ ಮಾಹಿತಿಗಳು")
                st.dataframe(filtered_df.style.set_properties(**{"background-color": "#f9f9f9", "color": "black"}))
            else:
                st.write("❌ No data available for the given location / ನೀಡಿದ ಸ್ಥಳಕ್ಕಾಗಿ ಡೇಟಾ ಲಭ್ಯವಿಲ್ಲ")
        else:
            st.write("⚠️ Please enter a location to view data / ಡೇಟಾ ವೀಕ್ಷಿಸಲು ಸ್ಥಳವನ್ನು ನಮೂದಿಸಿ")
    
if __name__ == "__main__":
    main()
