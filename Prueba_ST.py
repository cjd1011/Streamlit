import streamlit as st
import pandas as pd
from openpyxl import Workbook

st.write("Hello world")

st.title(':clipboard: Análisis de la Bolsa de Valores Australiana') #Titulo del Dash
st.subheader('Realizado por: Camilo Diaz')
st.markdown('##')

df = pd.read_excel("Portafolio Australia.xlsx")

st.dataframe(df)