import streamlit as st
import pandas as pd

def load_data():
    # Load the pre-existing dataset
    file_path = "data_enkn.xlsx"  # Ensure this file is in the same directory or adjust the path accordingly
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
            filtered_df = df[df['Location'].str.contains(location, case=False, na=False)][['Soil type', 'Yeilds', 'Irrigation', 'Season', 'Crops']]
            if not filtered_df.empty:
                selected_entry = filtered_df.iloc[0]  # Select only one matching entry
                st.write("### 📊 Information for Location / ಸ್ಥಳಕ್ಕಾಗಿ ಮಾಹಿತಿಗಳು")
                st.write(f"🟢 **Soil Type / ಮಣ್ಣಿನ ಪ್ರಕಾರ**: {selected_entry['Soil type']}")
                st.write(f"🌾 **Yield / ಬೆಳೆ ಉತ್ಪಾದನೆ**: {selected_entry['Yeilds']}")
                st.write(f"💧 **Irrigation / ನೀರಾವರಿ**: {selected_entry['Irrigation']}")
                st.write(f"📅 **Season / ಋತು**: {selected_entry['Season']}")
                st.write(f"🌱 **Crop / ಬೆಳೆ**: {selected_entry['Crops']}")
            else:
                st.write("❌ No data available for the given location / ನೀಡಿದ ಸ್ಥಳಕ್ಕಾಗಿ ಡೇಟಾ ಲಭ್ಯವಿಲ್ಲ")
        else:
            st.write("⚠️ Please enter a location to view data / ಡೇಟಾ ವೀಕ್ಷಿಸಲು ಸ್ಥಳವನ್ನು ನಮೂದಿಸಿ")
        
        # User input for soil type and irrigation method
        st.write("### 🌿 Get Crop Recommendation / ಬೆಳೆ ಶಿಫಾರಸು ಪಡೆಯಿರಿ")
        soil_type_input = st.selectbox("Select Soil Type / ಮಣ್ಣಿನ ಪ್ರಕಾರವನ್ನು ಆಯ್ಕೆಮಾಡಿ", df['Soil type'].dropna().unique())
        irrigation_input = st.selectbox("Select Irrigation Method / ನೀರಾವರಿ ವಿಧಾನವನ್ನು ಆಯ್ಕೆಮಾಡಿ", df['Irrigation'].dropna().unique())
        
        recommendation_df = df[(df['Soil type'] == soil_type_input) & (df['Irrigation'] == irrigation_input)][['Season', 'Crops']]
        if not recommendation_df.empty:
            recommended_entry = recommendation_df.iloc[0]
            st.write(f"🌾 **Recommended Season / ಶಿಫಾರಸು ಮಾಡಿದ ಋತು**: {recommended_entry['Season']}")
            st.write(f"🌱 **Recommended Crop / ಶಿಫಾರಸು ಮಾಡಿದ ಬೆಳೆ**: {recommended_entry['Crops']}")
        else:
            st.write("❌ No recommendation available for the selected soil and irrigation / ಆಯ್ಕೆಮಾಡಿದ ಮಣ್ಣು ಮತ್ತು ನೀರಾವರಿಗಾಗಿ ಶಿಫಾರಸು ಲಭ್ಯವಿಲ್ಲ")
    
if __name__ == "__main__":
    main()
