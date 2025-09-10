import streamlit as st
import os

# Configura a página para usar o layout "wide" (largo) e remove
# o preenchimento padrão ao redor do conteúdo principal.
st.set_page_config(layout="wide")

# Remove o espaço em branco no topo e nas laterais da página
st.markdown("""
    <style>
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
    }
    .main > div:first-child {
        padding-top: 0rem;
    }
    iframe {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)


# --- Carrega e exibe o HTML de um arquivo, ocupando a tela ---
try:
    # Obtém o caminho para o diretório atual do script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_file_path = os.path.join(current_dir, 'html.html')

    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_code_from_file = f.read()

    # Para simular "tela inteira", removemos outros elementos do Streamlit
    # e definimos uma altura grande para o componente HTML.
    # O valor 1080 é um exemplo para preencher uma tela Full HD; ajuste conforme necessário.
    st.components.v1.html(html_code_from_file, height=1080, scrolling=True)

except FileNotFoundError:
    st.error("O arquivo 'meu_codigo.html' não foi encontrado. Certifique-se de que ele está no mesmo diretório que o 'app.py'.")
