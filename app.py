import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')
st.header("Análisis de anuncios de vehículos")
if st.button('Mostrar histograma de precios'):
    fig = px.histogram(df, x='price', nbins=50, title='Distribución de precios de los vehículos')
    st.plotly_chart(fig)