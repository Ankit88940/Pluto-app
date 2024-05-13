from dotenv import load_dotenv
load_dotenv() ##loading all the environment variables
import requests
from streamlit_lottie import st_lottie
import streamlit as st
import os
import google.generativeai as genai

def app():
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    # FUNCTION TO LOAD OPEN AI MODEL AND GET  RESPONSES
    model=genai.GenerativeModel("gemini-pro")
    def get_gemini_response(question):
        response=model.generate_content(question)
        return response.text

    # # INITIALIZE OUR STREAMLIT APP
    # Set page title and header
    st.title("PLUTO PROMT", anchor="custom_anchor")
    st.subheader("TEXT BASED AI",divider='rainbow') 
    

    # Add a text box above the input field
    st.text("SEARCH CODE, FETCH INFORMATION & OTHER")

    # Input field
    # input_text = st.text_input("So What's your Question Buddy? Don't worry I am here to help you!!!", key="input")
    # if input_text:
    #      response = get_gemini_response(input_text)
    #      st.subheader("ACCORDING TO THE PROCESSED INFORMATION:", divider='rainbow')
    #      st.write(response)
    # else:
    #      st.warning("Please enter a valid prompt.")

    # Submit button
    # submit = st.button("Click here!! ")

    # # After submit button is clicked
    # if submit:
    #    response = get_gemini_response(input_text)
        
    #    st.subheader("ACCORDING TO THE PROCESSED INFORMATION:THE RESPONSE IS",divider='rainbow')
    #    st.write(response)
    # else:
    #  response != get_gemini_response(input_text)
    #  st.warning("Please enter a valid prompt.")
    input_text = st.text_input("So What's your Question Buddy? Don't worry I am here to help you!!!", key="input")
    if st.button("Click here!"):

        with st.spinner("Concluding..."):
            if input_text:  # Check if input_text is not empty
                response = get_gemini_response(input_text)
                st.subheader("ACCORDING TO THE PROCESSED INFORMATION:", divider='rainbow')
                st.write(response)
            else:
                st.warning("Please enter a valid prompt.")
    
    #    st.text("Enter a valid promt")
    # if st.button("Submit"):
    # input_text = st.text_input("Enter your prompt:")

    

    def load_lottieurl(url:str):
            r=requests.get(url)
            if r.status_code!=200:
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
    # search history
    with st.sidebar:
        st.header("Search History", divider="rainbow")

        # Create an empty list to store search history
        search_history = []

        # If a previous search history exists in the session state, retrieve it
        if "search_history" in st.session_state:
            search_history = st.session_state["search_history"]

        # Display search history in the sidebar
        for question in search_history:
            st.write("**Question:**", question)

        # Add the current question and response to the search history if input is valid
        if input_text and response:
            search_history.append(input_text)
            st.session_state["search_history"] = search_history  # Update session state

if __name__ == "__main__":
        app()
        
         