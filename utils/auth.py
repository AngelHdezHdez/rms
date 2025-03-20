# Funciones de autenticación
import streamlit as st

def init_session_state():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = None

def validate_session():
    return st.session_state.logged_in

def logout():
    st.session_state.logged_in = False
    st.session_state.username = None