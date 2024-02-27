#pip install streamlit gtts
#pip install ipython

import streamlit as st
from PIL import Image

import os

import google.generativeai as genai
from gtts import gTTS
import IPython.display as ipd
from deep_translator import GoogleTranslator

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("MY_SECRET_KEY")) 

generation_config = {
  "temperature": 0.9,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 1024,
}

st.image("logo.png", width=200)

def main():
    # Initialize session state
    if "objects_detected_text" not in st.session_state:
        st.session_state.objects_detected_text = ""

    # Add elements to the sidebar
    st.sidebar.header("Select the operation")
    selected_page = st.sidebar.radio("Choose", ["Detect", "Translate"])

    # Display different content based on the selected page
    if selected_page == "Detect":
        st.title("SoundSight Companion")
        disclaimer_message = """This is an object detector model so preferably use images containing different objects, tools... for best results 🙂."""

        st.write("")
        with st.expander("Disclaimer ⚠️", expanded=False):
            st.markdown(disclaimer_message)

        uploaded_image = st.file_uploader("Choose an image ...", type=["jpg", "jpeg", "png"])

        if uploaded_image is not None:
            st.image(uploaded_image, caption="Uploaded Image.", use_column_width=True)

            image = Image.open(uploaded_image)
            width, height = image.size
            st.write("Image Dimensions:", f"{width}x{height}")

            if st.button("Identify the objects"):
                st.success("Detecting...")
                vision_model = genai.GenerativeModel('gemini-pro-vision')
                response = vision_model.generate_content(["Extract the objects in the provided image and output them in a list along with their description, do not use an asterisk. Also, detect the environment of the image. Suppose the image contains famous personalities then try to identify them too.", image])

                st.session_state.objects_detected_text = response.text

                st.write("The objects detected are \n")
                st.write(st.session_state.objects_detected_text)

                tts = gTTS(text=st.session_state.objects_detected_text, lang='en')
                tts.save("output.mp3")
                audio_player = ipd.Audio("output.mp3", autoplay=True)
                st.write(audio_player)

                st.text("")
                
                st.text("Go to Translate page from sidebar for translating the output")

                st.text("")
                
                st.success("Thanks for visiting 🤩!!")
                st.info("For trying out with another image just click on browse files, enjoy 😄!!!")
    
    elif selected_page == "Translate":
        if (st.session_state.objects_detected_text):
        
            st.write("The text to be translated : ")
            st.text("")
            st.write(st.session_state.objects_detected_text)
            target_language = st.selectbox("Select target language:", ["Gujrati(gu)", "Kannada(kn)", "Malayalam(ml)", "Marathi(mr)", "Urdu(ur)", "Hindi(hi)", "Bengali(bn)", "Tamil(ta)", "Telegu(te)"])
            language=target_language[-3:-1]

    # Translate text on button click
            if st.button("Translate"):
                    translated_text = translate_text(st.session_state.objects_detected_text, language)
                    st.success(f"Translation: {translated_text}")
                
                    tts = gTTS(text=translated_text, lang=language)

                    tts.save("output2.mp3")
                    audio_player2 = ipd.Audio("output2.mp3", autoplay=True)
                    st.write(audio_player2)
                    st.text("")
        else:
            st.warning("No objects are detected please use any image to detect the objects in the detect page")


if __name__ == "__main__":
    main()



