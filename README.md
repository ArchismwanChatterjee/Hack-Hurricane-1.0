
![logo__1_-removebg-preview](https://github.com/ArchismwanChatterjee/Hack-Hurricane-1.0/assets/115975340/b1834188-dee7-44fa-b306-0cdb40fcb3e7)


# SoundSight Companion: Empowering Independence through Auditory Vision

![License](https://badgen.net/github/license/micromatch/micromatch)

SoundSight Companion aims to revolutionize the way visually impaired individuals perceive their surroundings. By leveraging advanced object detection algorithms and contextual image analysis, we enable users to explore the world by allowing them to upload images and receive detailed audio descriptions of objects detected, along with contextual information about the environment captured in the image.
Click [here](https://sound-sight-companion.streamlit.app/) to try out

This project is made under Hack-Hurricane 1.0 hackathon

## How to use:
1. Go through the disclaimer ⚠️ to understand more regarding what type of images will give best results.
2. Upload any image of your choice (upto 200MB)
3. Wait for the image to be uploaded, the dimesions of the image will be updated
4. Click on the button to detect the objects present
5. Wait for few seconds and See the ✨Magic ✨ Happen.
6. The users will be able to control the playback speed and download the audio output file.

## Installation:

- clone this repository

- SoundSight Companion requires [Python](https://www.python.org/) v3.9+ to run.

- Install the dependencies.

```python
pip install streamlit
pip install google-generativeai
pip install Pillow
pip install python-dotenv # for environment variable
pip install gtts
pip install ipython
pip install deep-translator
```
or simply

```python
pip install -r requirements.txt
```

- Make sure to create your own generative-ai api-key using Google Cloud Console or Google Makersuite and replace it.

```python
genai.configure(api_key=os.getenv("MY_SECRET_KEY")) # Replace with your own api-key by creating .env file
```
or 
```python
genai.configure(api_key="YOUR APIKEY")  # Replace YOUR APIKEY with the actual value of your apikey 
```

- To run the server
```python
streamlit run "your_file_name"
```

- For Deploying your application refer [Streamlit Community Cloud](https://docs.streamlit.io/streamlit-community-cloud/get-started)

## Deployment:

The website is deployed using streamlit community cloud ⬇️

[Link](https://sound-sight-companion.streamlit.app/) 
