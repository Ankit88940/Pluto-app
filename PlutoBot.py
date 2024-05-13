import streamlit as st
import requests
from streamlit_lottie import st_lottie
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
def app():
    # app config

    st.title("PLUTO BOT")
    st.subheader("YOUR OWN PERSONAL CHATBOT ", divider='rainbow')

    # Initialize ChatOpenAI with correct API key
    apikey = "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"
    llm = ChatOpenAI(api_key=apikey)

    def get_response(user_query, chat_history):
        template = """
        You are a helpful assistant. Answer the following questions considering the history of the conversation:
    
        Chat history: {chat_history}
    
        User question: {user_question}
        """

        prompt = ChatPromptTemplate.from_template(template)

        chain = prompt | llm | StrOutputParser()

        return chain.invoke({
            "chat_history": chat_history,
            "user_question": user_query,
        })


    # session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage(content="Hey buddy,I am a PLUTO. How can I help you?"),
        ]

    # conversation
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)

    # user input
    user_query = st.chat_input("Type your message here...")
    if user_query is not None and user_query != "":
        st.session_state.chat_history.append(HumanMessage(content=user_query))

        with st.chat_message("Human"):
            st.markdown(user_query)

        with st.chat_message("AI"):
            response = get_response(user_query, st.session_state.chat_history)
            st.write(response)

        st.session_state.chat_history.append(AIMessage(content=response))

    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_hello = load_lottieurl("https://lottie.host/64f6ddb1-371f-4fd2-9a71-de27158d9fca/IMsHrmdMpB.json")
    with st.sidebar:
     st_lottie(
             lottie_hello,
            speed=1,
            reverse=False,
            loop=True,
            quality="medium",
            # renderer='svg',
            height=300,
            width=300,
            key=None,
        )
app()