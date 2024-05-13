import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

import Home
import Assistant
import PlutoVision
import PlutoPrompt
import PlutoBot
import About
import requests

st.set_page_config(page_title="Puto", page_icon="🤖")
def creds_entered():
    if st.session_state["user"].strip() == "ankit" and st.session_state["passwd"].strip() == "ankit":
        st.session_state["authenticated"] = True
    else:
        st.session_state["authenticated"] = False
        if not st.session_state["passwd"]:
            st.warning("Please enter the password")
        elif not st.session_state["user"]:
            st.warning("Please enter the username")
        else:
            st.error("Invalid Username/Password:face_with_raised_eyebrow:")


def authenticate_user():
    if "authenticated" not in st.session_state:
        st.header("LOGIN", divider="rainbow")

        st.text_input(label="Username:", value="", key="user", on_change=creds_entered)
        st.text_input(label="Password:", value="", key="passwd", type="password", on_change=creds_entered)
        st.success("Press enter after filling Credentials")

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
        return False
    else:
        if st.session_state["authenticated"]:
            return True
        else:
            st.header("LOGIN", divider="rainbow")
            st.text_input(label="Username:", value="", key="user", on_change=creds_entered)
            st.text_input(label="Password:", value="", key="passwd", type="password", on_change=creds_entered)
            st.success("Press enter after filling Credentials")

            def load_lottieurl(url: str):
                r = requests.get(url)
                if r.status_code != 200:
                    return None
                return r.json()

            lottie_hello = load_lottieurl(
                "https://lottie.host/64f6ddb1-371f-4fd2-9a71-de27158d9fca/IMsHrmdMpB.json")
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
            return False


if authenticate_user():
    # Set page title and header
    # st.set_page_config(page_title="PLUTO AI", layout="centered")
    class MultiApp:

        def __init__(self):
            self.apps = []

        def add_app(self, title, function):
            self.apps.append({
                "title": title,
                "function": function
            })

        @staticmethod
        def run():
            with st.sidebar:
                app = option_menu(
                    menu_title="PLUTO ",
                    options=['Home', 'PlutoVision', 'PlutoPrompt', 'Assistant','PlutoBot', 'About'],
                    icons=['house-fill', 'camera-fill', 'chat-text-fill', 'person-circle','person-circle', 'info-circle-fill'],
                    menu_icon='clipboard-data',
                    default_index=0,
                    styles={
                        "container": {"padding": "5!important", "background-color": '#262730', "color": "white"},
                        # Set background & text color
                        "icon": {"color": "white", "font-size": "10px"},
                        "nav-link": {"font-size": "13px", "text-align": "left", "margin": "0px"},
                        "nav-link-selected": {"background-color": "#4E525A"}
                    })
            if app == 'Assistant':
                Assistant.app()
            if app == 'Home':
                Home.app()
            if app == 'PlutoVision':
                PlutoVision.app()
            if app == 'PlutoPrompt':
                PlutoPrompt.app()
            if app == 'PlutoBot':
                PlutoBot.app()
            if app == 'About':
                About.app()

        run()
