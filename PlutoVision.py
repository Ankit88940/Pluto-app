import streamlit as st
from dotenv import load_dotenv
load_dotenv() ##loading all the environment variables
import requests
from streamlit_lottie import st_lottie
import os
import google.generativeai as genai
from PIL import Image


# st.set_page_config(page_title="Q&A Demo")
def app():
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    # FUNCTION TO LOAD OPEN AI MODEL AND GET RESPONSES
    model = genai.GenerativeModel("gemini-pro-vision")
    def get_gemini_response(input, image):
        if input and image:  # Check both input and image are not empty
            return model.generate_content([input, image]).text
        elif not input:
            return "Please enter a valid prompt."
        elif not image:
            return "Please upload an image."
        else:
            return "An unexpected error occurred."  # Handle other potential issues

    # Set page title and header
    st.title("PLUTO VISION", anchor="custom_anchor")
    st.subheader("IMAGE BASED AI", divider='rainbow')
    

    # Add a text box above the input field
    st.text("IMAGE BASED TASKS , FETCH INFORMATION & OTHER")

    # Input field
    input = st.text_input("Enter your prompt:", key="input")
    st.expander("Enter your prompt here")
    submit = st.button("Click here!")

    uploaded_file = st.file_uploader("choose an image___", type=["jpg", "jpeg", "png"])
    image = None  # Initialize image variable outside the if condition

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image ", use_column_width=True)

    #   # After submit button is clicked
    #   if submit:
    #       response = get_gemini_response(input, image)
    #       # st.subheader("ACCORDING TO THE PROCESSED INFORMATION:THE RESPONSE IS", divider='rainbow')
    #       if isinstance(response, str):  # Check if response is an error message
    #           st.warning(response)  # Display warning for error messages
    #       else:
    #           st.subheader("ACCORDING TO THE PROCESSED INFORMATION:THE RESPONSE IS", divider='rainbow')
    #           st.write(response)
        # After submit button is clicked
        if submit:
            # Check for both input and image (combine conditions)
            with st.spinner("Concluding..."):
                if input or uploaded_file:
                    response = get_gemini_response(input, image)  # Call function with input and image
                    st.subheader("ACCORDING TO THE PROCESSED INFORMATION:", divider='rainbow')
                    st.write(response)
                else:
                    st.warning("Please enter a prompt or upload an image.")  # Combined error message


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

    # Contact Us sidebar
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
        if input and response:
            search_history.append(input)
            st.session_state["search_history"] = search_history  # Update session state

if __name__ == "__main__":
 app()
    
