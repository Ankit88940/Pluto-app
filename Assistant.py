from audio_recorder_streamlit import audio_recorder
import openai
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import requests
from streamlit_lottie import st_lottie
import base64

def app():
    def setup_openai_client(api_key):
        return openai.OpenAI(api_key=api_key)
    def transcribe_audio(client, audio_path):
        with open(audio_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
            return transcript.text

    #taking response
    def fetch_ai_response(client, input_text):
        messages = [{"role": "user", "content": input_text}]
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
        return response.choices[0].message.content

    #conert text to audio
    def text_to_audio(client, text, audio_path):
        response = client.audio.speech.create(model="tts-1", voice="echo", input=text)
        response.stream_to_file(audio_path)

    # #text cards functions
    # def create_text_card(text, title="Response"):
    #     card_html =f"""
    #     <style>
    #         .card{{
    #             box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    #             transition: 0.3s;
    #             border-radius: 5px;
    #             padding: 15px
    #         }}
    #         .card:hover{{
    #             box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    #         }}
    #         .container{{
    #             padding: 2px 16px;
    #         }}
    #         </style>
    #         <div class="card">
    #             <div class="container">
    #                <h4><b>{title}</b></h4>
    #                <p>{text}</p>
    #              </div>
    #      """
    #     st.markdown(card_html, unsafe_allow_html=True)

    #autoplay audio function

    def auto_play_audio(audio_file):

        # with open(audio_file, "rb") as audio_file:
        #     audio_bytes = audio_file.read()
        # base64_audio = base64.b64encode(audio_bytes).decode("utf-8")
        # audio_file = f'<audio scr="data:audio/mp3;base64,{base64_audio}" conrols autoplay>'
        # st.markdown(audio_file, unsafe_allow_html=True)
        with open(audio_file, "rb") as audio_file:
            audio_bytes = audio_file.read()
        base64_audio = base64.b64encode(audio_bytes).decode("utf-8")
        audio_html = f'<audio src="data:audio/mp3;base64,{base64_audio}" controls autoplay>'
        st.markdown(audio_html, unsafe_allow_html=True)

    def main():

        st.sidebar.header("API KEY CONFIGURATION",divider="rainbow")
        api_key = st.sidebar.text_input("Firstly enter your OpenAi API key & Click anywhere on the screen", type="password")
        st.sidebar.header("YOU CAN USE THIS API KEY FOR TESTING:",divider="rainbow")
        st.sidebar.write("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")
        st.sidebar.markdown("___")
        st.title("PLUTO VOICE")
        st.header("AI that listens you all the day", divider="rainbow")
        st.write("Hello Buddy!Click on the voice recorder to interact with me.How can i assist you today?")

        #check if api_key is there
        if api_key:
            client = setup_openai_client(api_key)
            recorded_audio = audio_recorder()
            #check
            with st.spinner("Concluding..."):
                if recorded_audio:
                    audio_file = "audio.mp3"
                    with open(audio_file, "wb") as f:
                        f.write(recorded_audio)

                    transcribed_text = transcribe_audio(client, audio_file)
                    st.header("USER'S TRANSCRIBED TEXT:",divider="rainbow")
                    st.write(transcribed_text)

                    ai_response = fetch_ai_response(client, transcribed_text)
                    response_audio_file = "audio_response.mp3"
                    text_to_audio(client, ai_response, response_audio_file)

                    st.header("PLUTO RESPONSE:", divider="rainbow")
                    st.write(ai_response)
                    auto_play_audio(response_audio_file)

        # Lottie animation (optional)
        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

        lottie_hello = load_lottieurl("https://lottie.host/64f6ddb1-371f-4fd2-9a71-de27158d9fca/IMsHrmdMpB.json")
        st_lottie(
            lottie_hello,
            speed=1,
            reverse=False,
            loop=True,
            quality="medium",
            # renderer='svg',
            height=300,
            width=700,
            key=None,
        )

    main()
