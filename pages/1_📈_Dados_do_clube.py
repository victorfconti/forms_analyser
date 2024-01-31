import streamlit as st
from services.forms_service import FormsService

forms_service = FormsService()

st.set_page_config(
    page_title="Dados do clube",
    page_icon="📈",
    layout='wide'
)

st.title("Dados do clube")

"Bem vindo leitor, aqui nós iremos exibir as informações estatísticas sobre os nossos leitores"
st.write("Caso ainda não tenha preenchido, por favor, preencha o formulário em: "
         " [formulário]"
         "(https://docs.google.com/forms/d/e/1FAIpQLSe1DtkjH9lkcNXqrjN2YlrGma21NN_U7UMZ-fQBfxO3UuC3uQ/viewform)")


