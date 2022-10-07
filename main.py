import streamlit as st
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/labeconometria/MLxE/main/proyectos2do/datasets3.csv")


st.title("Proyecto 6")
st.write(" En la presente pagina, a partir de un dataset dentro del que se determina la potabilidad del agua \
    a partir de caracteristicas especificas como la cantidad de carbono organico o su condutividad, se realizan lo siguiente: ")
st.write("1. exploracion inicial: ")
st.table(df.head(5))

st.write("1. Una categorización de variables y conclusión acerca de la relación de estas con la variable objetivo")
st.write("2. Visualización de proporciones de las variables, relacion entre las variables sin la variable objetivo,\
     Boxplot entre las variables y la vraiable objetivo")
st.write("3. Pruebas de hipotesis sobre la normalidad de las variables, diferencia de medias y median si se divide \
    el dataset en 2, distribución normal multivariada del dataset sin la variable objetivo")