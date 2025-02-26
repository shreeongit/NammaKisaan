import streamlit as st
import pandas as pd

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
    uploaded_file = st.file_uploader("Upload dataset (CSV) / ಡೇಟಾಸೆಟ್ ಅಪ್ಲೋಡ್ (CSV)", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("### 📊 Dataset Overview / ಡೇಟಾಸೆಟ್ ಅವಲೋಕನ")
        st.dataframe(df.style.set_properties(**{"background-color": "#f9f9f9", "color": "black"}))
    
if __name__ == "__main__":
    main()
