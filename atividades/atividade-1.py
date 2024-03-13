import pandas as pd

df = pd.read_csv('base/OnlineNewsPopularity.csv') # leitura da base

print(df.columns.to_list) # ver o nome das colunas
subdf_colunas = ['url', ' n_tokens_title', ' shares'] # subset que irá filtrar
subdf = df[subdf_colunas] # criação do subset
subdf.rename(columns={' n_tokens_title': 'num_palavras_titulo', ' shares': 'compartilhamentos'}, inplace=True)
subdf['num_palavras_titulo'] = subdf['num_palavras_titulo'].astype(int)
subdf.sort_values(by=['compartilhamentos'], inplace=True, ascending=False)
subdf.reset_index(drop = True, inplace = True)
