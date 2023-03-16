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

# peleador = data['name']
# ganadas = data['wins']
# racha = data['ko_rate']
# edad = data['age']

follow = data['name']
friends = data['wins']
fav = data['ko_rate']
dis = data['age']

fig_perf_work = px.scatter(data,
                           x=dis,
                           y=friends,
                           size=fav,
                           color=follow,
                           title="Muestra la cantidad de segudiores  ",
                           labels=dict(Date="Fecha de Tweet",
                                       source="Dispositivo", favo="Fvaoritos"),
                           template="plotly_white")
fig_perf_work.update_layout(plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig_perf_work)

# fig_perf_work = px.scatter(data,
#                           x=edad,
#                           y=ganadas,
#                           size=racha,
#                           color=peleador,
#                           title="Muestra datos del peleador  ",
#                           labels=dict(Date="Fecha de Tweet",
#                                       age="Edad", racha="Racha KO"),
#                           template="plotly_white")
# fig_perf_work.update_layout(plot_bgcolor="rgba(0,0,0,0)")
# st.plotly_chart(fig_perf_work)
