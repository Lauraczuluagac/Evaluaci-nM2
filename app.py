import pandas as pd
import streamlit as st

data = pd.read_csv('historico_resultados_pruebas_saber_11.csv')

st.header("Tablas resultados pruebas saber pro 11")
data
data = data.dropna()
st.header("Tabla con limpieza de datos")
data

#filtro 1 

st.header("filtro1")
st.write("Mostrar puntaje naturales mayor que 50")
filtro1 = data[data['puntaje_naturales'] > 50]
st.dataframe(filtro1)

#filtro 2 

st.header("filtro2")
st.write("Mostrar puntaje global menor a 250 en manrique")
filtro2 = data[(data['puntaje_global'] < 250) & (data['comuna'] == 'manrique')] 
st.dataframe(filtro2)

#filtro 3 

st.header("filtro3")
st.write("Mostrar puntajes de institucion  santa teresa")
filtro3 = data[(data['establecimiento'] =='inst educ santa teresa')] 
st.dataframe(filtro3)


#filtro 4

st.header("filtro4")
st.write("Mostrar prestacion de servicios privado en comuna aranjuezr")
filtro4 = data[(data['prestacion_servicio'] == 'privado') & (data['comuna'] == 'aranjuez')] 
st.dataframe(filtro4)

#filtro 5

st.header("filtro5")
st.write("Mostrar prestacion de servicios contratacion en establecimiento col gente unida jovenes por la paz - luz de oriente")
filtro5 = data[(data['prestacion_servicio'] == 'contratacion') & (data['establecimiento'] == 'col gente unida jovenes por la paz - luz de oriente')] 
st.dataframe(filtro5)
