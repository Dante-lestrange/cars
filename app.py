import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos solo una vez
df = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación (sin duplicaciones)
st.title("Análisis de anuncios de vehículos")

# Controles para los botones usando `st.checkbox()`
mostrar_histograma = st.checkbox("Mostrar histograma de precios")
mostrar_dispersion = st.checkbox("Mostrar gráfica de dispersión")

# Si el usuario marca el checkbox, se muestra la gráfica correspondiente
if mostrar_histograma:
    fig = px.histogram(df, x="price", nbins=50, title="Distribución de precios de los vehículos")
    st.plotly_chart(fig)

if mostrar_dispersion:
    fig = px.scatter(df, x="odometer", y="price", title="Dispersión: Precio vs Kilometraje")
    st.plotly_chart(fig)