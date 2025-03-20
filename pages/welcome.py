# Pagina de bienvenida
import streamlit as st
from utils.database import check_gender, check_energia_generada_por_tipo_tecnologia_bd

# Ocultar todos los elementos
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

if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.warning("Por favor, inicia sesión primero")
    st.stop()

def show_welcome_page(username):
    saludo = check_gender(username)
    
    st.markdown("""
        <style>
        .title {
            margin-top: 10px;
        }
        </style>
        """, unsafe_allow_html=True)

    container1 = st.container()
    with container1:
        st.markdown(f'<h1 class="title">¡{saludo}, {username}! 👋</h1>', unsafe_allow_html=True)
        col1, col2 = st.columns([2,1])
        with col1:
            st.write(f'<h3>¿Que planes tienes para hoy? 👀</h4>',unsafe_allow_html=True)
        with col2:
            if st.button("Cerrar sesion", key="btnx1"):
                st.session_state.logged_in = False
                st.switch_page("Home.py")
    
    container2 = st.container()
    with container2:
        st.header("Energia Generada por tipo de tecnologia")
        st.write(f'Actualizado hasta el: ')

        col1, col2, col3, col4 = st.columns([1,1,1,1])
        with col1:
            if st.button("Visualización de BD", key="btn1"):
                st.session_state.logged_in = True
                st.switch_page("pages/egxt.py")
        with col2:
            if st.button("Actualización de BD", key="btn2"):
                st.session_state.logged_in = True
                st.switch_page("pages/energia_generada_por_tipo_tecnologia.py")
        with col3:
            if st.button("Exportar pronóstico", key="btn3"):
                st.session_state.logged_in = True
                st.switch_page("pages/energia_generada_por_tipo_tecnologia.py")
        with col4:
            if st.button("Reportar falla", key="btn4"):
                st.session_state.logged_in = True
                st.switch_page("pages/energia_generada_por_tipo_tecnologia.py")

    container3 = st.container()
    with container3:
        st.header("Estimación Demanda Real")
        st.write("Actualizado hasta el: ")
        
        col1, col2, col3, col4 = st.columns([1,1,1,1])
        with col1:
            if st.button("Visualización de BD", key="btn5"):
                st.session_state.logged_in = True
                st.switch_page("pages/energia_generada_por_tipo_tecnologia.py")
        with col2:
            if st.button("Actualización de BD", key="btn6"):
                st.session_state.logged_in = True
                st.switch_page("pages/energia_generada_por_tipo_tecnologia.py")
        with col3:
            if st.button("Exportar pronóstico", key="btn7"):
                st.session_state.logged_in = True
                st.switch_page("pages/energia_generada_por_tipo_tecnologia.py")
        with col4:
            if st.button("Reportar falla", key="btn8"):
                st.session_state.logged_in = True
                st.switch_page("pages/energia_generada_por_tipo_tecnologia.py")
    
    container4 = st.container()
    with container4:
        st.header("Pronóstico de Demanda")
        st.write("Actualizado hasta el: ")
        
        col1, col2, col3, col4 = st.columns([1,1,1,1])
        with col1:
            if st.button("Visualización de BD", key="btn9"):
                st.session_state.logged_in = True
                st.switch_page("pages/energia_generada_por_tipo_tecnologia.py")
        with col2:
            if st.button("Actualización de BD", key="btn10"):
                st.session_state.logged_in = True
                st.switch_page("pages/energia_generada_por_tipo_tecnologia.py")
        with col3:
            if st.button("Exportar pronóstico", key="btn11"):
                st.session_state.logged_in = True
                st.switch_page("pages/energia_generada_por_tipo_tecnologia.py")
        with col4:
            if st.button("Reportar falla", key="btn12"):
                st.session_state.logged_in = True
                st.switch_page("pages/energia_generada_por_tipo_tecnologia.py")

if st.session_state.logged_in:
    show_welcome_page(st.session_state.username)