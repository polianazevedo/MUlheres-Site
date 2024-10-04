import streamlit as st
from PIL import Image

# Definindo o CSS para remover funções de adm - customização da interface do site
customizando_site = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {
        background: radial-gradient(circle, violet, pink); /* Gradiente rosa-roxo */
    }
    </style>
    """

# Aplicando o CSS
st.markdown(customizando_site, unsafe_allow_html=True)

# Definição do título
st.header(" A Influência das Mulheres Gonçalenses na Construção Identitária da Sociedade", divider="gray")

# Colunas

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Aline")
    st.image("IMAGES.SITE/Aline.jpg")
    st.caption("Minha professora que me ensinou que sempre devemos acreditar em nós mesmos, e também não desistir do que almejamos. - PH 3004")

with col2:
    st.subheader("Elaine")
    st.image("IMAGES.SITE/Elaine.jpg")
    st.caption("Me formou como pessoa e me ensinou que amor não é só falando mas também pode ser demonstrado com ações. - PH 3004 ")

with col3:
    st.subheader("Maria José")
    st.image("IMAGES.SITE/Maria José.jpg")
    st.caption("me ensinou que podem tirar tudo da gente menos o conhecimento. - Ana Clara Souza 2003")