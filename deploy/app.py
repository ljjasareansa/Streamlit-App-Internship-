import streamlit as st
import time
from groq import Groq
import base64

GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)
def encode_image(image):
    return base64.b64encode(image.read()).decode()


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
    st.image(Image, caption="Uploaded Image", use_column_width=True)
    st.info("Uploading image... Please wait ")
    progress_text = st.empty()
    progress_bar = st.progress(0)
        
    st.header("Prediction Score")
    gender = st.radio("Enter your gender:", ['Male', 'Female'])
    parent_education = st.selectbox("Select your Parent Education Level", [
    'some high school',
    'high school',
    'some college',
    "associate's degree",
    "bachelor's degree",
    "master's degree"
    ])
    test_prep = st.selectbox("Did student complete a test prep course?", ['Completed', 'None'])

    user_prompt = st.text_area("Enter any additional information for prediction:")

    if st.button("Make Prediction"):
        base64_image = encode_image(Image)
        
        messages = [
            {
        "role": "user",
        "content": [
            {"type": "text", "text": (
                f"Patient Info:\n"
                f"Name: {name}\n"
                f"Age: {age}\n"
                f"Location: {area}\n"
                f"Gender: {gender}\n"
                f"Parent Education: {parent_education}\n"
                f"Test Prep: {test_prep}\n"
                f"User Prompt: {user_prompt}"
            )},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
        ]
    }
        ]
        
        with st.spinner("Generating prediction..."):
            try:
                response = client.chat.completions.create(
                    model="meta-llama/llama-4-scout-17b-16e-instruct",  
                    messages=messages,
                    
                )
                output = response.choices[0].message.content
                st.success("Prediction Submitted!")
                st.markdown(f"*AI Output:*\n\n{output}")
                              
            except Exception as e:
                st.error(f"An error occurred during prediction: {e}"
            )
        
else:
    st.info("Please upload an image before the prediction form will appear.")
    
