import streamlit as st
import pandas as pd
from cria_imagens import *

st.set_page_config(layout='wide', page_title="Hoteis")

df=pd.read_json('dataset_booking-scraper_2024-04-04_22-54-18-439 (1).json')
all_address_data = []

# Iterar sobre cada linha do DataFrame
for index, row in df.iterrows():
    # Acessar o nome do hotel
    hotel_name = row['name']

    # Acessar o dicionário na coluna 'address'
    address_data = row['address']

    # Adicionar o nome do hotel ao dicionário de endereço
    address_data['hotel_name'] = hotel_name

    # Adicionar os dados do endereço à lista
    all_address_data.append(address_data)

# Criar um DataFrame com os dados de todos os endereços
df_address = pd.DataFrame(all_address_data)

all_rooms_data = []

# Iterar sobre cada linha do DataFrame
for index, row in df.iterrows():
    # Acessar o nome do hotel
    hotel_name = row['name']

    # Acessar cada dicionário na lista da coluna 'rooms'
    for room_data in row['rooms']:
        # Adicionar o nome do hotel aos dados da sala
        room_data['hotel_name'] = hotel_name

        # Adicionar os dados da sala à lista
        all_rooms_data.append(room_data)

# Criar um DataFrame com os dados de todas as salas, incluindo o nome do hotel
df_rooms = pd.DataFrame(all_rooms_data)

all_rating_data = []

# Iterar sobre cada linha do DataFrame
for index, row in df.iterrows():
    # Acessar o nome do hotel
    hotel_name = row['name']

    # Acessar cada dicionário na lista da coluna 'categoryReviews'
    for room_data in row['categoryReviews']:
        # Adicionar os dados da avaliação à lista
        all_rating_data.append({'name': hotel_name, 'title': room_data['title'], 'score': room_data['score']})

# Criar um DataFrame com os dados de todas as avaliações
df_rating = pd.DataFrame(all_rating_data)

# Agregar os scores das avaliações para cada hotel
df_rating = df_rating.pivot_table(index='name', columns='title', values='score', aggfunc='mean', fill_value=0)

# Resetar o índice para que 'name' se torne uma coluna novamente
df_rating = df_rating.reset_index()

import re
def extrair_bairro(endereco):
    # Expressão regular para tentar encontrar o bairro
    match = re.search(r',\s*([^,]+),[^,]*CEP', endereco)
    if match:
        return match.group(1).strip()
    else:
        # Se não for possível extrair o bairro usando a expressão regular,
        # tentaremos obter o último elemento após dividir o endereço por vírgulas
        parts = endereco.split(',')
        return parts[-2].strip() if len(parts) > 1 else ''

# Aplicar a função à coluna 'full' para extrair o bairro
df_address['bairro'] = df_address['full'].apply(extrair_bairro)



contagem_bairros = df_address['bairro'].value_counts().reset_index()
contagem_bairros = pd.DataFrame(contagem_bairros)

contagem_quartos_disponiveis = df_rooms['hotel_name'].value_counts().reset_index()
contagem_quartos_disponiveis = pd.DataFrame(contagem_quartos_disponiveis)

fig_bairros = criar_grafico_horizontal(contagem_bairros,'count','bairro','Contagem de hoteis por bairro')
fig_hoteis_quatos = criar_grafico_horizontal(contagem_quartos_disponiveis,'count','hotel_name','Contagem de quartos livres por hotel')

Contagem_hoteis = df.shape[0]
contagem_quatos = df_rooms.shape[0]

aux = pd.merge(df_address, df_rooms, how='inner', on='hotel_name')

quartos_livres_baiiro = aux['bairro'].value_counts().reset_index()
quartos_livres_baiiro = pd.DataFrame(quartos_livres_baiiro)

fig_bairros_quartos = criar_grafico_horizontal(quartos_livres_baiiro,'count','bairro','Contagem de hoteis por bairro')


col1, col2 = st.columns(2)
with col1:
    with st.container(height=100):
        st.metric("Numero de hoteis analizados", Contagem_hoteis)
with col2:
    with st.container(height=100):
        st.metric('Numero de quartos analizados', contagem_quatos)

col1, col2 = st.columns(2)
with col1:
    with st.container(height=400):
        st.altair_chart(fig_bairros, use_container_width=True)
with col2:
    with st.container(height=400):
        st.altair_chart(fig_hoteis_quatos, use_container_width=True)
with st.container(height=400):
    st.altair_chart(fig_bairros_quartos, use_container_width=True)