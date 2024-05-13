import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie

def app():
    # st.title("Welcome to:red[ PLUTO ]")
    st.header("A multi web app for your multiple works", divider='rainbow')

    def load_lottieurl(url: str):
        """Loads Lottie animation from a URL."""
        response = requests.get(url)
        if response.status_code != 200:
            return None
        return response.json()

    lottie_hello = load_lottieurl("https://lottie.host/64f6ddb1-371f-4fd2-9a71-de27158d9fca/IMsHrmdMpB.json")
    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        quality="medium",
        height=600,
        width=700,
        key=None,
    )

    st.header("Unlock a comprehensive suite of AI tools ",divider="rainbow")

    st.write("PLUTO PROMT: Enhance your research with a cutting-edge AI assistant that seamlessly integrates into your search bar. Get instant answers, summaries, and insights for any query.")

    st.write("PLUTO VISION: Unleash the power of computer vision with an AI assistant that analyzes images . Perform image execution processing and provide effective output from uploaded images")

    st.write("Assistant: Elevate your experience with an AI assistant that assists you in fetching information,making blogs ,transcribing text and many more by just listening your voice commands")
    st.header("Other Key Features:",divider="rainbow")
    st.write("Intuitive multipage design for seamless navigation")
    # st.write("Detailed documentation for each tool")
    st.write("Customizable settings for a personalized experience")
    st.write("Powerful search functionality for quick access to AI capabilities")
    st.write("Continuous updates with new features and enhancements")
    st.write("Maximize your AI potential with PlutoAi, the ultimate destination for your AI needs. Supercharge your research, perform different tasks, and empower your innovation today!")

    # Contact Us sidebar
    with st.sidebar:
        st.header("Contact Us", divider="rainbow")
        st.write("Stay in touch!")

        
        contact_info = {
            "LinkedIn": "www.linkedin.com/in/",
            "Twitter": "https://x.com/ankit0339866430?t=Dhxz3pnecgZobFGSnLzULA&s=09",
            "WhatsApp": "+918894067365",  
            "Email": "anki88940@gmail.com",
        }

        for platform, link in contact_info.items():
            st.write(f"{platform}: {link}")

if __name__ == "__main__":
    app()
