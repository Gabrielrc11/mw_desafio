import streamlit as st
import pandas as pd
import plotly.express as px

online = pd.read_csv('./resultados/online.csv')
offline = pd.read_csv('./resultados/offline.csv')
plano = pd.read_csv('./resultados/plano.csv')
status = pd.read_csv('./resultados/status.csv')

st.sidebar.title('Dashboard: Desafio MW Soluções')
opcao = st.sidebar.selectbox('Filtrar:', ('Clientes por cidade', 'Clientes por plano', 'Clientes por status'))

if opcao == 'Clientes por cidade':
    st.subheader('Clientes online por cidade:')
    st.dataframe(online, use_container_width=True)
    fig_online = px.bar(online, x='Cidade', y='Clientes')
    st.plotly_chart(fig_online)
    st.subheader('Clientes offline por cidade:')
    st.dataframe(offline, use_container_width=True)
    fig_offline = px.bar(offline, x='Cidade', y='Clientes')
    st.plotly_chart(fig_offline)

if opcao == 'Clientes por plano':
    st.subheader('Clientes por plano:')
    st.dataframe(plano, use_container_width=True)
    fig_plano = px.bar(plano, x='Plano', y='Clientes')
    st.plotly_chart(fig_plano)

if opcao == 'Clientes por status':
    st.subheader('Clientes por status:')
    st.dataframe(status, use_container_width=True)
    fig_status = px.pie(status, names='Status', values='Clientes', title='Distribuição de Clientes por Status')
    st.plotly_chart(fig_status)