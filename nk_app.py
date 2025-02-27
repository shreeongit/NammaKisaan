import streamlit as st
import pandas as pd

# Load dataset
data_path = "data_season.csv"  # Update path if necessary
df = pd.read_csv(data_path)

# Bilingual labels
labels = {
    "en": {"name": "Name", "age": "Age", "aadhar": "Aadhaar Number", "owner": "Ownership Type", "location": "Location", "size": "Plot Size (Acres)", "register": "Register"},
    "kn": {"name": "ಹೆಸರು", "age": "ವಯಸ್ಸು", "aadhar": "ಆಧಾರ್ ಸಂಖ್ಯೆ", "owner": "ಮಾಲಕತ್ವದ ಪ್ರಕಾರ", "location": "ಸ್ಥಳ", "size": "ಜಮೀನಿನ ಗಾತ್ರ (ಏಕರೆ)", "register": "ನೋಂದಾಯಿಸಿ"}
}

# User language selection
lang = st.sidebar.radio("Select Language / ಭಾಷೆ ಆಯ್ಕೆಮಾಡಿ", ("en", "kn"))

st.title("Namma Kisaan / ನಮ್ಮ ಕೃಷಿಕ")

# Registration form
st.header("Farmer Registration / ಕೃಷಿಕ ನೋಂದಣಿ")
name = st.text_input(labels[lang]["name"])
age = st.number_input(labels[lang]["age"], min_value=18, max_value=100)
aadhar = st.text_input(labels[lang]["aadhar"], max_chars=12)
owner = st.selectbox(labels[lang]["owner"], ["Owner", "Lessee"] if lang == "en" else ["ಮಾಲೀಕ", "ಭಾಡಿಗೆದಾರ"])
location = st.text_input(labels[lang]["location"])
size = st.number_input(labels[lang]["size"], min_value=0.1)

if st.button(labels[lang]["register"]):
    st.success("Registered Successfully! / ಯಶಸ್ವಿಯಾಗಿ ನೋಂದಾಯಿಸಲಾಗಿದೆ!")

# Filter dataset based on location
st.header("Agricultural Data / ಕೃಷಿ ಡೇಟಾ")
filtered_data = df[df["Location"].str.contains(location, case=False, na=False)]
if not filtered_data.empty:
    st.dataframe(filtered_data[["Soil type", "yeilds", "Irrigation", "Season", "Crops"]])
else:
    st.warning("No matching data found / ಹೊಂದಾಣಿಕೆಯ ಡೇಟಾ ಲಭ್ಯವಿಲ್ಲ")

# Crop recommendation
st.header("Crop Recommendation / ಬೆಳೆ ಶಿಫಾರಸು")
soil_type = st.selectbox("Select Soil Type / ಮಣ್ಣಿನ ಪ್ರಕಾರ ಆಯ್ಕೆಮಾಡಿ", df["Soil type"].dropna().unique())
irrigation = st.selectbox("Select Irrigation Type / ನೀರಾವರಿ ಪ್ರಕಾರ ಆಯ್ಕೆಮಾಡಿ", df["Irrigation"].unique())
recommendation = df[(df["Soil type"] == soil_type) & (df["Irrigation"] == irrigation)][["Season", "Crops"]].drop_duplicates()
if not recommendation.empty:
    st.write(recommendation.to_dict(orient="records"))
else:
    st.warning("No recommendations available / ಶಿಫಾರಸುಗಳು ಲಭ್ಯವಿಲ್ಲ")
