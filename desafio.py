import pandas as pd
from questdb.ingress import Sender
import requests as rq

tabela = pd.read_csv("questdb-usuarios-dataset.csv")
df = pd.DataFrame(data=tabela)
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

conf = f'http::addr=questdb:9000;'
with Sender.from_conf(conf) as sender:
    sender.dataframe(df, table_name='dados', at='timestamp')

url = "http://questdb:9000/exec"

params = {
    "query": "SELECT cidadeCliente, COUNT(*) AS total_clientes FROM dados WHERE statusCliente = 1 ORDER BY total_clientes DESC;"
}
response = rq.get(url, params=params)
resultado = pd.DataFrame(response.json()['dataset'], columns=['Cidade', 'Clientes'])
resultado.to_csv('./resultados/online.csv', index=False, header=True)

params = {
    "query": "SELECT cidadeCliente, COUNT(*) AS total_clientes FROM dados WHERE statusCliente = 0 ORDER BY total_clientes DESC;"
}
response = rq.get(url, params=params)
resultado = pd.DataFrame(response.json()['dataset'], columns=['Cidade', 'Clientes'])
resultado.to_csv('./resultados/offline.csv', index=False, header=True)

params = {
    "query": "SELECT planoContrato, COUNT(*) AS total_clientes FROM dados ORDER BY total_clientes DESC LIMIT 10;"
}
response = rq.get(url, params=params)
resultado = pd.DataFrame(response.json()['dataset'], columns=['Plano', 'Clientes'])
resultado.to_csv('./resultados/plano.csv', index=False, header=True)

params = {
    "query": "SELECT statusCliente, COUNT(*) AS total_clientes FROM dados ORDER BY total_clientes DESC;"
}
response = rq.get(url, params=params)
resultado = pd.DataFrame(response.json()['dataset'], columns=['Status', 'Clientes'])
resultado['Status'] = resultado['Status'].replace({0: 'Offline', 1: 'Online'})
resultado.to_csv('./resultados/status.csv', index=False, header=True)

params = {
    "query": "SELECT valorPlano, COUNT(*) AS total_clientes FROM dados ORDER BY total_clientes DESC;"
}
response = rq.get(url, params=params)
resultado = pd.DataFrame(response.json()['dataset'], columns=['Valor', 'Clientes'])
resultado.to_csv('./resultados/valor.csv', index=False, header=True)