import streamlit as st
import pandas as pd
import numpy as np
import codecs
import matplotlib.pyplot as plt
import plotly.express as px


st.sidebar.image("Logo.png")
st.title('COMBATES DE BOXEO BY CHRISTIAN REYES!!')
st.text("Christian Eduardo Amaro Reyes - S19004895")

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

if st.sidebar.checkbox('Mostrar Peleadores'):
    st.subheader('Todos los peleadores')
    st.write(data)

namefighter = st.sidebar.text_input('Nombre del peleador :')
btnBuscar = st.sidebar.button('Buscar peleador')

if (btnBuscar):
    data_fighter = filter_data_by_fighter(namefighter.upper())
    count_row = data_fighter.shape[0]
    st.write(f"Total mostrados : {count_row}")
    st.write(data_fighter)

selected_country = st.sidebar.selectbox(
    "Seleccionar País", data['country'].unique())
btnFilterbyCountry = st.sidebar.button('Filtrar País ')

if (btnFilterbyCountry):
    filterbycoun = filter_data_by_country(selected_country)
    count_row = filterbycoun.shape[0]
    st.write(f"Total Peleas : {count_row}")

    st.dataframe(filterbycoun)

wins = data['wins']
if st.sidebar.checkbox('Peleas ganadas'):
    st.markdown("Grafica que muestra la frecuencia del total victorias en las peleas siendo 0 el numero mas bajo y siendo la frecuencia el numero de peleas")
    fig, ax = plt.subplots()
    ax.hist(wins, bins=10, range=(0, 10))
    ax.set_xlabel('Peleas ganadas')
    ax.set_ylabel('Frecuencia')
    ax.set_title('Histograma del número de peleas ganadas')
    st.pyplot(fig)

wins = data['looses']
if st.sidebar.checkbox('Peleas perdidas'):
    st.markdown("Grafica que muestra la frecuencia del total derrotas en las peleas siendo 0 el numero mas bajo y siendo la frecuencia el numero de peleas")
    fig, ax = plt.subplots()
    ax.hist(wins, bins=10, range=(0, 10))
    ax.set_xlabel('Peleas perdidas')
    ax.set_ylabel('Frecuencia')
    ax.set_title('Histograma del número de peleas perdidas')
    st.pyplot(fig)


# away = st.sidebar.multiselect("Peleas ganadas", sorted(data["wins"].unique()))
# home = st.sidebar.multiselect(
#    "Peleas perdidas", sorted(data["looses"].unique()))

# if st.sidebar.button("Filtrar Peleas"):
#    st.markdown("Se selecciona el numero de Peleas ganadas y Perdidas y muesta los resultados de peleas con ese numero de wins o loses")
#    mask = (data["wins"].isin(home)) & (data["looses"].isin(away))
#    peleas_seleccionadas = data[mask]
#    st.write("Peleas seleccionadas")
#    st.write(Peleas_seleccionadas)

# columnas = ['wins', 'loses']
# columna_seleccionada = st.sidebar.multiselect(
#    'Selecciona si gano o perdio', columnas)
# wins = data['wins'].sum()
# loses = data['loses'].sum()
