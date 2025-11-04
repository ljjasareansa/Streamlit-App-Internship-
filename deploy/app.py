import streamlit as st
import time

st.title("Maths Score Prediction")


with st.form("data_form"):
    st.header("Data Collection Section")

    name = st.text_input("Enter your name:")
    age = st.slider("Select your age", 15, 30)
    area = st.selectbox("Where do you stay?", ['Ayeduase', 'New Site', 'Boadi', 'Appiadu', 'On Campus'])

    submitted = st.form_submit_button("Submit Data")

if submitted:
    message = st.info("Submitting data... Please wait")
    time.sleep(2)   
    message.empty()
    st.success(f"Data submitted successfully!")
    st.balloons()

    st.header("Image Upload Section")
    Image = st.file_uploader("Upload image file(JPG, JPEG, PNG)")
    if Image is not None:
        st.Image(Image, caption="Uploaded Image", use_column_width=True)
        st.info("Uploading image... Please wait ")
        progress_text = st.empty()
        progress_bar = st.progress(0)
        st.header("Prediction Score")
    
    
