import streamlit as st
import pandas as pd
import plotly.express as px

online = pd.read_csv('./resultados/online.csv')
offline = pd.read_csv('./resultados/offline.csv')
plano = pd.read_csv('./resultados/plano.csv')
status = pd.read_csv('./resultados/status.csv')
valor = pd.read_csv('./resultados/valor.csv')

st.sidebar.title('Dashboard: Desafio MW Soluções')
opcao = st.sidebar.selectbox('Filtrar:', ('Clientes por cidade', 'Clientes por plano', 'Clientes por status'))

if opcao == 'Clientes por cidade':
    st.subheader('Clientes online por cidade:')
    st.dataframe(online, use_container_width=True)
    fig_online = px.bar(online, x='0', y='1', labels={'0': 'Cidades', '1': 'Total de Clientes Online'})
    st.plotly_chart(fig_online)
    st.subheader('Clientes offline por cidade:')
    st.dataframe(offline, use_container_width=True)
    fig_offline = px.bar(offline, x='0', y='1', labels={'0': 'Cidades', '1': 'Total de Clientes Offline'})
    st.plotly_chart(fig_offline)

if opcao == 'Clientes por plano':
    st.subheader('Clientes por plano:')
    st.dataframe(plano, use_container_width=True)
    fig_plano = px.bar(plano, x='0', y='1', labels={'0': 'Planos', '1': 'Total de Clientes'})
    st.plotly_chart(fig_plano)

if opcao == 'Clientes por status':
    st.subheader('Legenda: 0 = Offline; 1 = Online')
    st.dataframe(status, use_container_width=True)
    fig_status = px.pie(status, names='0', values='1', title='Distribuição de Clientes por Status',
                         labels={'0': 'Status', '1': 'Total de Clientes'})
    st.plotly_chart(fig_status)