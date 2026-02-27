# streamlit_app.py
import streamlit as st
import requests

st.title("Medical Claim PDF Extractor")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    if st.button("Extract Data"):
        with st.spinner("Extracting..."):
            try:
                # Call FastAPI endpoint
                response = requests.post(
                    "http://127.0.0.1:8000/upload",
                    files={"file": open("temp.pdf", "rb")}
                )

                if response.status_code == 200:
                    data = response.json()
                    st.success("Extraction Complete!")
                    st.json(data)
                else:
                    st.error(f"API Error: {response.json()}")
            except Exception as e:
                st.error(f"Error: {str(e)}")
