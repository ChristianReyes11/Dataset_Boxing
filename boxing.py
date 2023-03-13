import streamlit as st
import pandas as pd
import numpy as np
import codecs

st.sidebar.image("Logo.png")
st.title('COMBATES DE BOXEO BY CHRISTIAN REYES')
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
    filtered_data_genre = data[data['country'] == country]
    return filtered_data_country


data_load_state = st.text('Loading...')
data = load_data(500)
data_load_state.text("(using st.cache)")

if st.sidebar.checkbox('Mostrar Peleas'):
    st.subheader('Todas las peleas')
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
