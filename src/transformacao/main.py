import pandas as pd
import sqlite3
from datetime import datetime

# Lendo os dados coletados pelo webscraping e coloando em um Dataframe
df = pd.read_json('data/data.jsonl', lines=True)

# Criando colunas _source e _hora_coleta
df['_source'] = 'https://lista.mercadolivre.com.br/smartphone-8gb-ram'
df['_data_coleta'] = datetime.now()

# Transformando preços e rating em float
df['preco_antigo'] = df['preco_antigo'].fillna(0).astype(float)
df['preco_novo'] = df['preco_novo'].fillna(0).astype(float)
df['rating'] = df['rating'].fillna(0).astype(float)

# Removendo parenteses da coluna qtd_review e transformando em inteiros
df['qtd_review'] = df['qtd_review'].str.replace('[(,)]', '', regex=True)
df['qtd_review'] = df['qtd_review'].fillna(0).astype(int)

# Conectando ao banco de dados SQLite
conn = sqlite3.connect('data/data.db')

# Salvando o Dataframe no banco de dados SQLite
df.to_sql('mercadolivre', conn, if_exists='replace', index=False)

# Fechando conexao banco de dados
conn.close()