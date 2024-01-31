import streamlit as st

from services.forms_service import FormsService

st.set_page_config(
    page_title="Boas vindas",
    page_icon="👋",
    layout='wide'
)

st.title("Boas vindas leitor")
forms_service = FormsService()
