import os
import streamlit as st
import requests
from openrouter import ask_openrouter


def get_api_key():
    try:
        return st.secrets["OPENROUTER_API_KEY"]
    except:
        return os.getenv("OPENROUTER_API_KEY") or ""


st.title("OpenAI")
st.write("Чатбот з іішкою")

with st.sidebar:
    st.header("Параметри")
    model = st.selectbox("Модель", ["tencent/hy3:free"])
    temperature = st.slider("Temperature", 0.0, 1.5,0.7, 0.1)

    system_promt = st.text_area("System promt",value= "Ти навчальний асистент для студентів.Відповідай українською, коротко і структуровано")

if "messages" not  in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])



user_message = st.chat_input("напишіть повідомлення")

if user_message:
    st.session_state.messages.append({"role":"user","content":user_message})

    with st.chat_message("user"):
        st.markdown(user_message)

    with st.chat_message("assistant"):
        try:
            api_messages = [{"role":"system","content":system_promt}]
            api_messages.extend(st.session_state.messages)
            with st.spinner("..."):
                answer = ask_openrouter(get_api_key(), api_messages,model,temperature)
        except requests.HTTPError as error:
            st.error(f"HTTPError: {error}")
            st.stop()
        except Exception as error:
            st.error(f"Exception: {error}")
            st.stop()

        st.markdown(answer)

    st.session_state.messages.append({"role":"assistant","content":answer})