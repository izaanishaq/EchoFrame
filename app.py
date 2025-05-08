import streamlit as st
from PIL import Image
import tempfile
import os

from qa import generate_answer

st.set_page_config(page_title="Ask-the-Image: Multimodal QA App", layout="centered")

st.title("Ask-the-Image: Multimodal QA App")
st.markdown("Upload an image, type your question, and the app will answer.") # Modified

uploaded_image_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
question_text = st.text_input("Type your question here:") # Added

if st.button("Get Answer"):
    if uploaded_image_file is not None and question_text: # Modified
        # Process the image
        image = Image.open(uploaded_image_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

        with st.spinner("Processing your question..."):
            try:
                st.write(f"**Your Question:** {question_text}") # Modified

                answer = generate_answer(image, question_text) # Modified
                
                # Display results
                st.subheader("Answer:")
                st.write(answer)
                
            
            except Exception as e:
                st.error(f"An error occurred: {e}")
        
    elif uploaded_image_file is None:
        st.warning("Please upload an image.")
    # elif uploaded_audio_file is None: # Modified
    elif not question_text: # Modified
        st.warning("Please type your question.") # Modified

st.markdown("---")
st.markdown("Powered by Streamlit and BLIP-2.") # Modified