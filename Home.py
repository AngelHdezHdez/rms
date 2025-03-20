import streamlit as st
from utils.database import check_credentials
from utils.auth import init_session_state

st.set_page_config(page_title="Login", page_icon="🔒")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
[data-testid="collapsedControl"] {display: none;}
div[data-testid="stSidebarNav"] {display: none;}
.css-1d391kg {display: none;}
section[data-testid="stSidebar"] {display: none;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def login_page():
    st.title("Inicio de Sesión 🔒")
    
    # Centrar el formulario de login
    col1, col2, col3 = st.columns([1,2,1])
    
    with col2:
        with st.form("login_form"):
            username = st.text_input("Usuario")
            password = st.text_input("Contraseña", type="password")
            submit_button = st.form_submit_button("Iniciar Sesión")
            
            if submit_button:
                if not username or not password:
                    st.error("Por favor, completa todos los campos")
                    return
                    
                user = check_credentials(username, password)
                if user:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success("¡Login exitoso!")
                    st.switch_page("pages/welcome.py")
                else:
                    st.error("Usuario o contraseña incorrectos")

def main():
    init_session_state()
    
    if st.session_state.logged_in:
        st.switch_page("pages/welcome.py")
    else:
        login_page()

if __name__ == "__main__":
    main()