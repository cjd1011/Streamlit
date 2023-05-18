import streamlit as st
import pandas as pd
#from openpyxl import Workbook
import pip
pip.main(["install", "openpyxl"])# esta linea y la de arriba me ayudaron a poder ejecutarlo en streamlit, casi que no!

st.write("Hello world")

st.title(':clipboard: Análisis de la Bolsa de Valores Australiana') #Titulo del Dash
st.subheader('Realizado por: Camilo Diaz')
st.markdown('##')

df = pd.read_excel("Portafolio Australia.xlsx")

#st.dataframe(df)

st.sidebar.header("Activos a filtrar:") #sidebar lo que nos va a hacer es crear en la parte izquierda un cuadro para agregar los filtros que queremos tener
    Activo = st.sidebar.multiselect(
        "Seleccione el Activo:",
        options = df['Asset'].unique(),
        default = df['Asset'].unique() #Aqui podría por default dejar un filtro especifico pero vamos a dejarlos todos puestos por default
    )
    
    df_seleccion = df.query("Asset == @Activo " ) #el primero es la columna y el segundo es el selector

    st.dataframe(df_seleccion)
    
    line = alt.Chart(df_seleccion).mark_line().encode(
        alt.X("Date",title = "Date"),
        alt.Y("Close", title = "Closing Price",scale=alt.Scale(zero=False)),
        color = 'Asset'
    )
    line