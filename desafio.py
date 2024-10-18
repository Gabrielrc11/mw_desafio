import pandas as pd
from questdb.ingress import Sender

tabela = pd.read_csv("questdb-usuarios-dataset.csv")
df = pd.DataFrame(data=tabela)
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

conf = f'http::addr=localhost:9000;'
with Sender.from_conf(conf) as sender:
    sender.dataframe(df, table_name='questdb-usuarios-dataset', at='timestamp')