# Pagina de energia_generada_por_tipo_tecnologia
import pandas as pd
import plotly.express as px
import streamlit as st
from utils.database import check_energia_generada_por_tipo_tecnologia_bd

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

def show_engenportec_page(username):
     
    st.markdown("""
        <style>
        .title {
            margin-top: -200px;
        }
        </style>
        """, unsafe_allow_html=True)
    
    if st.button("Volver a Inicio", key="return_button"):
        st.session_state.logged_in = True
        st.switch_page("pages/welcome.py")

datos = check_energia_generada_por_tipo_tecnologia_bd()

def crear_grafica_energia(datos):
    st.markdown(f'<h1 class="title">Grafico por tipo de tecnología</h1>', unsafe_allow_html=True)
    
    if not datos:
        st.error("No hay datos disponibles")
        return

    if datos:
        df = pd.DataFrame(datos)
        df['Hora'] = df['Hora'].replace(25, 1)
        df['Hora'] = (df['Hora'] - 1) % 24
        
        df['DateTime'] = pd.to_datetime(df['Fecha'].dt.date.astype(str) + ' ' + df['Hora'].astype(str) + ':00')
        
        liquidacion_opciones = df['Liquidacion'].unique()
        liquidacion_seleccionada = st.selectbox(
            "Seleccionar Liquidación",
            options=liquidacion_opciones,
            key="liquidacion_select"
        )
        
        tecnologias = df.columns[-12:-1].tolist()
        
        col_fecha1, col_fecha2 = st.columns(2)
        with col_fecha1:
            fecha_inicio = st.date_input(
                "Fecha inicial",
                min_value=df['Fecha'].min().date(),
                max_value=df['Fecha'].max().date(),
                value=df['Fecha'].min().date(),
                key="fecha_inicio_input"
            )
        with col_fecha2:
            fecha_fin = st.date_input(
                "Fecha final",
                min_value=df['Fecha'].min().date(),
                max_value=df['Fecha'].max().date(),
                value=df['Fecha'].max().date(),
                key="fecha_fin_input"
            )
        
        tecnologias_seleccionadas = st.multiselect(
            "Selecciona las tecnologías a mostrar",
            options=tecnologias,
            default=tecnologias,
            key="tecnologias_multiselect"
        )

        if st.button('Generar Gráfico', key='generar_grafico'):
            if fecha_fin < fecha_inicio:
                st.error("La fecha final debe ser posterior a la fecha inicial")
                return
                
            with st.spinner('Generando gráfico...'):
                mask = (
                    (df['Fecha'].dt.date >= fecha_inicio) & 
                    (df['Fecha'].dt.date <= fecha_fin) &
                    (df['Liquidacion'] == liquidacion_seleccionada)
                )
                df_filtrado = df.loc[mask]
                
                if tecnologias_seleccionadas:
                    fig = px.scatter(
                        df_filtrado,
                        x='DateTime',
                        y=tecnologias_seleccionadas,
                        title='Energía Generada por Tipo de Tecnología',
                        opacity=0.7,
                        size_max=10,
                        render_mode='svg'
                    )

                    fig.update_layout(
                    xaxis_title="Fecha y Hora",
                    yaxis_title="Energía Generada",
                    legend_title="Tecnologías",
                    height=500,
                    
                    legend=dict(
                        orientation="h",
                        yanchor="bottom",
                        y=-0.3,
                        xanchor="center",
                        x=0.5
                    ))
                    
                    fig.update_xaxes(tickformat="%Y-%m-%d %H:%M")
                    
                    st.plotly_chart(fig, use_container_width=True)
                    
                    if len(df_filtrado) > 0:
                        csv = df_filtrado.to_csv(index=False)
                        st.download_button(
                            label="Descargar CSV",
                            data=csv,
                            file_name="energia_por_tecnologia.csv",
                            mime="text/csv",
                            key="download_csv"
                        )

                    return fig, df_filtrado['DateTime'].max().strftime('%d/%m/%Y %H:%M')

resultado = crear_grafica_energia(datos)

if resultado:
    figura, fecha_actualizacion = resultado

if st.session_state.logged_in:
    show_engenportec_page(st.session_state.username)