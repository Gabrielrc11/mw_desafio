import pandas as pd
from questdb.ingress import Sender
import requests

#Criando tabela "dados" a partir de csv
tabela = pd.read_csv("questdb-usuarios-dataset.csv")
df = pd.DataFrame(data=tabela)
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

conf = f'http::addr=questdb:9000;'
with Sender.from_conf(conf) as sender:
    sender.dataframe(df, table_name='dados', at='timestamp')

#Executando comandos SQL e armazenando resultado em csv
url = "http://questdb:9000/exec"

#Clientes online por cidade
params = {
    "query": "SELECT cidadeCliente, COUNT(*) AS total_clientes FROM dados WHERE statusCliente = 1 ORDER BY total_clientes DESC;"
}
response = requests.get(url, params=params)
resultado = pd.DataFrame(response.json()['dataset'])
resultado.to_csv('./resultados/online.csv', index=False, header=False)

#Clientes offline por cidade
params = {
    "query": "SELECT cidadeCliente, COUNT(*) AS total_clientes FROM dados WHERE statusCliente = 0 ORDER BY total_clientes DESC;"
}
response = requests.get(url, params=params)
resultado = pd.DataFrame(response.json()['dataset'])
resultado.to_csv('./resultados/offline.csv', index=False, header=False)

#Clientes por plano
params = {
    "query": "SELECT planoContrato, COUNT(*) AS total_clientes FROM dados ORDER BY total_clientes DESC;"
}
response = requests.get(url, params=params)
resultado = pd.DataFrame(response.json()['dataset'])
resultado.to_csv('./resultados/plano.csv', index=False, header=False)

#Clientes por status
params = {
    "query": "SELECT statusCliente, COUNT(*) AS total_clientes FROM dados ORDER BY total_clientes DESC;"
}
response = requests.get(url, params=params)
resultado = pd.DataFrame(response.json()['dataset'])
resultado.to_csv('./resultados/status.csv', index=False, header=False)

#Clientes por valor do plano
params = {
    "query": "SELECT valorPlano, COUNT(*) AS total_clientes FROM dados ORDER BY total_clientes DESC;"
}
response = requests.get(url, params=params)
resultado = pd.DataFrame(response.json()['dataset'])
resultado.to_csv('./resultados/valor.csv', index=False, header=False)