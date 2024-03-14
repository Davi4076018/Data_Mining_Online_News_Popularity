import pandas as pd
import datetime
def Reducao_drop_columns(df):
    dropcoluns = [' timedelta']
    colunas = df.columns.values.tolist()
    dropcoluns.extend(colunas[19:31].copy())
    dropcoluns.extend(colunas[39:60].copy())
    df.drop(dropcoluns, axis=1, inplace=True)
    return df

df = pd.read_csv('atividades/base/OnlineNewsPopularity.csv') # leitura da base

def dias_semana(row):
    val = ''
    colunas = [' weekday_is_monday', ' weekday_is_tuesday', ' weekday_is_wednesday', ' weekday_is_thursday',
                 ' weekday_is_friday', ' weekday_is_saturday', ' weekday_is_sunday']
    saidas = ['Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo']
    for n in range(len(colunas)):
        if row[colunas[n]] == 1:
            val = saidas[n]
            break
    return val
def Agrupamento_Dias_Semana(df):
    colunas = [' weekday_is_monday', ' weekday_is_tuesday', ' weekday_is_wednesday', ' weekday_is_thursday',
               ' weekday_is_friday', ' weekday_is_saturday', ' weekday_is_sunday']
    for coluna in colunas:
        df[coluna] = df[coluna].astype(int)
    df['Dia_Publicado'] = df.apply(dias_semana, axis=1)
    df.drop(colunas, axis=1, inplace=True)
    return df
    #print(df)
    #print(colunas[19:31]) # ver o nome das colunas
#print(colunas[39:60])
#subdf_colunas = ['url', ' n_tokens_title', ' shares'] # subset que irá filtrar
#subdf = df[subdf_colunas] # criação do subset
#subdf.rename(columns={' n_tokens_title': 'num_palavras_titulo', ' shares': 'compartilhamentos'}, inplace=True)
#subdf['num_palavras_titulo'] = subdf['num_palavras_titulo'].astype(int)
#subdf.sort_values(by=['compartilhamentos'], inplace=True, ascending=False)
#subdf.reset_index(drop = True, inplace = True)



if __name__ == "__main__":
    df = pd.read_csv('base/OnlineNewsPopularity.csv')  # leitura da base
    df = Reducao_drop_columns(df)
    df = Criacao_data_column(df)
    print(df.columns.values.tolist())
    df = Agrupamento_Dias_Semana(df)
    df.to_csv('base/OnlineNewsPopularity_atividade_1.csv', sep=',')