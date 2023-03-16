import streamlit as st
import pandas as pd
import numpy as np
import codecs
import matplotlib.pyplot as plt
import plotly.express as px


st.sidebar.image("Logo.png")
st.markdown("<h1 style='text-align: center; color: white;'>COMBATES DE BOXEO</h1>",
            unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>Christian Eduardo Amaro Reyes</h3>",
            unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>S19004895</h3>",
            unsafe_allow_html=True)

DATE_COLUMN = 'released'
DATA_URL = ('fighters.csv')
df = pd.read_csv(DATA_URL)


@st.cache
def load_data(nrows):
    doc = codecs.open('fighters.csv', 'rU', 'latin1')
    data = pd.read_csv(doc, nrows=nrows)
    def lowercase(x): return str(x).lower()
    return data


def filter_data_by_fighter(fighter):
    filtered_data_fighter = data[data['name'].str.upper(
    ).str.contains(fighter)]
    return filtered_data_fighter


def filter_data_by_country(country):
    filtered_data_country = data[data['country'] == country]
    return filtered_data_country


data_load_state = st.text('Loading...')
data = load_data(2500)
data_load_state.text("")
sidebar = st.sidebar

if st.sidebar.checkbox('Mostrar Peleadores'):
    st.subheader('Todos los peleadores')
    st.write(data)

namefighter = st.sidebar.text_input('Nombre del peleador :')
btnBuscar = st.sidebar.button('Buscar peleador')

if (btnBuscar):
    data_fighter = filter_data_by_fighter(namefighter.upper())
    count_row = data_fighter.shape[0]
    st.write(f"Total de peleadores : {count_row}")
    st.write(data_fighter)

selected_country = st.sidebar.selectbox(
    "Seleccionar País", data['country'].unique())
btnFilterbyCountry = st.sidebar.button('Filtrar País ')

if (btnFilterbyCountry):
    filterbycoun = filter_data_by_country(selected_country)
    count_row = filterbycoun.shape[0]
    st.write(f"Total de Peleadores : {count_row}")

    st.dataframe(filterbycoun)

wins = data['wins']
if st.sidebar.checkbox('Peleas ganadas'):
    st.markdown(
        "Grafica que muestra la frecuencia del total victorias en las peleas")
    fig, ax = plt.subplots()
    ax.hist(wins, bins=10, range=(0, 10))
    ax.set_xlabel('Peleas ganadas')
    ax.set_ylabel('Frecuencia')
    ax.set_title('Histograma del número de peleas ganadas')
    st.pyplot(fig)

wins = data['looses']
if st.sidebar.checkbox('Peleas perdidas'):
    st.markdown(
        "Grafica que muestra la frecuencia del total derrotas en las peleas")
    fig, ax = plt.subplots()
    ax.hist(wins, bins=10, range=(0, 10))
    ax.set_xlabel('Peleas perdidas')
    ax.set_ylabel('Frecuencia')
    ax.set_title('Histograma del número de peleas perdidas')
    st.pyplot(fig)

st.markdown("<h4 style='text-align: center; color: white;'>Este Histograma muestra desde que país son los peleadores</h4>", unsafe_allow_html=True)
country = data['country']
fig, ax = plt.subplots()
ax.hist(country, bins=4, range=(0, 3), color="red", ec="black")
ax.set_xlabel('Ciudades')
ax.set_ylabel('Frecuencia')
ax.set_title('Histograma de Los países de donde son los peleadores')
st.pyplot(fig)

columnas = ['Peleas']
columna_seleccionada = st.sidebar.multiselect(
    'Selecciona Peleas', columnas)
Victorias = data['wins'].sum()
Derrotas = data['looses'].sum()
Empates = data['draws'].sum()

if columna_seleccionada:
    st.markdown(
        "<h4 style='text-align: center; color: white;'>Muestra el Total de peleas</h4>", unsafe_allow_html=True)
    df = pd.DataFrame({
        'Peleas': ['Victorias', 'Derrotas', 'Empates'],
        'Total': [Victorias, Derrotas, Empates]
    })
    fig = px.bar(df, x='Peleas', y='Total')
    st.plotly_chart(fig, use_container_width=True)

# <Nueva implementación a probar>
# histograma por Peleadores por rango de edad
st.subheader("Gráficos")
st.write("Histograma que muestra la relacion entre la cantidad de Peleadores por rango de edad")

fig = px.histogram(df, x='age', nbins=10)
fig.update_layout(title='Numero de Peleadores por rango de edad',
                  xaxis_title='Edad',
                  yaxis_title='Frecuencia')
st.plotly_chart(fig)

st.write("\n\nGrafica de barras que muestra cuantas veces a perdido cada Peleador.\n Para el grafico se cargaron los primero 30 registros")

fig2 = px.bar(df[:30], x='looses', y='name', orientation='h', color='looses')
fig2.update_layout(title='¿Cuantas veces han perdido los peleadores?',
                   xaxis_title='Derrotas',
                   yaxis_title='Nombres')

st.plotly_chart(fig2)

datagrafica = load_data(1000)

st.write("\n\nGrafica de dispersion que muestra la relacion entre las Peleas ganadas y la edad de los peleadores.\n Para el grafico se cargaron los primero 1000 registros")
fig3 = px.scatter(datagrafica, x='age', y='wins')
fig3.update_layout(title='Grafica de Dispersión del Titanic',
                   xaxis_title='Edad',
                   yaxis_title='Victorias')
st.plotly_chart(fig3)

# st.sidebar.image("Uv Anverso.png")
