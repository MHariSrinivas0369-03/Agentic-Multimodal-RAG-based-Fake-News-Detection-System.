import streamlit as st
from agent import verify_claim
from PIL import Image

st.set_page_config(page_title="Agentic Fake News Detection")

st.title("Agentic RAG Fake News Detection System")

st.write(
"""
This AI system verifies news claims using:

Retrieval Evidence based on RAG Wikipedia database
CLIP Model for Image-Text embedding   
LLM reasoning  
Image verification  
"""
)

claim = st.text_area("Enter News Claim")

image_file = st.file_uploader(
    "Upload an Image (optional)",
    type=["jpg","jpeg","png"]
)

if st.button("Verify Claim"):

    if claim.strip()=="":
        st.warning("Please enter a claim")

    else:

        with st.spinner("Analyzing claim..."):

            result = verify_claim(claim,image_file)

        st.subheader("Prediction")

        st.write(result["analysis"])

        st.subheader("Image Analysis")

        st.write(result["image_analysis"])

        st.subheader("Retrieved Evidence")

        for e in result["evidence"]:
            st.write("-",e)