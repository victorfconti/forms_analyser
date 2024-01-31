import streamlit as st

from st_pages import Page, show_pages
from services.forms_service import FormsService

st.set_page_config(
    page_title="Boas vindas",
    page_icon="👋",
    layout='wide'
)

show_pages(
    [
        Page("main.py", "Boas vindas", "🏠"),
        Page("pages/dados_do_clube.py", "Dados do clube", "📈"),
        Page("pages/recomendacoes.py", "Recomendações", "📖"),
    ]
)

st.title("Boas vindas leitor")
forms_service = FormsService()
