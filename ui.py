import streamlit as st
import requests

st.set_page_config(page_title="Langgraph Agent UI", page_icon="😎")

API_URL = "http://127.0.0.1:8000/chat"

# Define model names
MODEL_NAMES = [
    "mixtral-8x7b-32768",
    "llama-3.1-70b-versatile",
    "gemma2-9b-it",
]

st.title("LangGraph Chatbot Agent")
st.write("Your Go to Pattner")

given_system_promt = st.text_area("Define Your Agent:",placeholder="Tpye your system prompt here.....")
select_model=st.selectbox("Select Your Model:", MODEL_NAMES)
user_input = st.text_area("Enter your message:",placeholder="Type your message here.....")

def send_api_req(playload):
    try:
        response= requests.post(API_URL, json=playload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f'An error in backend:{e}')
        return None
    except ValueError:
        st.error("The API returned an invalid JSON response.")
        return None

def display_ai_respone(response_data):
    if "error" in response_data:
        st.error(response_data['error'])
    else:
        ai_response=[
            message.get("content","")
            for message in response_data.get("messages",[])
            if message.get('type')=='ai'
            ]
        if ai_response:
            st.subheader("Agent Response:")
            st.markdown(f'**Final Response** {ai_response[-1]}')
        else: st.warning("No AI respose found.")
        
if st.button("Submit"):
    if user_input.strip():
        payload={"messages":[user_input],"model_name":select_model,"system_prompt":given_system_promt}
        with st.spinner("Sending Request to the agent...."):
            response_data = send_api_req(payload)
            if response_data:
                display_ai_respone(response_data)
    else:
        st.warning("Pls Enter a Valid Message befor sending query.")
        
if not given_system_promt.strip():
    st.warning("It's recommended to provide a system prompt to guide the agent's behavior.")
    