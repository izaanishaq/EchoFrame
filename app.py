import streamlit as st
from PIL import Image
import tempfile
import os

# Assuming your existing modules are in the same directory or accessible in PYTHONPATH
from asr import transcribe
from qa import generate_answer
from tts import text_to_speech

st.set_page_config(page_title="Ask-the-Image: Multimodal QA App", layout="centered")

st.title("Ask-the-Image: Multimodal QA App")
st.markdown("Upload an image and ask a question by uploading an audio file. The app answers and speaks it back.")

uploaded_image_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
uploaded_audio_file = st.file_uploader("Upload your Question (audio file)", type=["wav", "mp3", "flac", "ogg"])

if st.button("Get Answer"):
    if uploaded_image_file is not None and uploaded_audio_file is not None:
        # Process the image
        image = Image.open(uploaded_image_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

        # Process the audio
        # Save uploaded audio to a temporary file because `transcribe` expects a filepath
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_audio_file.name)[1]) as tmp_audio_file:
            tmp_audio_file.write(uploaded_audio_file.getvalue())
            audio_path = tmp_audio_file.name
        
        with st.spinner("Processing your question..."):
            try:
                # 1. Transcribe audio to text
                question = transcribe(audio_path)
                st.write(f"**Your Question:** {question}")

                # 2. Generate answer from image and question
                answer = generate_answer(image, question)
                
                # 3. Convert answer to speech
                spoken_audio_path = text_to_speech(answer)

                # Display results
                st.subheader("Answer:")
                st.write(answer)
                
                st.subheader("Spoken Answer:")
                st.audio(spoken_audio_path)
            
            except Exception as e:
                st.error(f"An error occurred: {e}")
            finally:
                # Clean up the temporary audio file created for transcription
                if os.path.exists(audio_path):
                    os.remove(audio_path)
                # Note: The temporary file from text_to_speech is not deleted here
                # as st.audio needs access to it. gTTS creates it with delete=False.
                # For long-running apps, a more robust temp file management strategy might be needed.

    elif uploaded_image_file is None:
        st.warning("Please upload an image.")
    elif uploaded_audio_file is None:
        st.warning("Please upload an audio file for your question.")

st.markdown("---")
st.markdown("Powered by Streamlit, Whisper, BLIP-2, and gTTS.")