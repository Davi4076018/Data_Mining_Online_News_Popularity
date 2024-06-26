import pandas as pd
from datetime import datetime

dfcond_nv_popu = pd.DataFrame()

def Reducao_drop_columns(df):
    dropcoluns = [' timedelta', 'Data_Publicado', 'url', ' shares']
    #dropcoluns = [' timedelta', ' n_non_stop_unique_tokens', ' LDA_00', ' LDA_01', ' LDA_02', ' LDA_03', ' LDA_04',
    #              ' global_sentiment_polarity', ' rate_positive_words', ' rate_negative_words']
    colunas = df.columns.values.tolist()
    #dropcoluns.extend(colunas[19:31].copy())
    #dropcoluns.extend(colunas[50:60].copy())
    df.drop(dropcoluns, axis=1, inplace=True)
    return df

def Criacao_data_column(df):
    df['Data_Publicado'] = df['url'].str[20:30]
    df['Data_Publicado'] = pd.to_datetime(df['Data_Publicado'])
    return df

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

def categorias(row):
    val = 'Nenhuma'
    colunas = [' data_channel_is_lifestyle', ' data_channel_is_entertainment', ' data_channel_is_bus',
               ' data_channel_is_socmed', ' data_channel_is_tech', ' data_channel_is_world']
    saidas = ['Estilo de vida', 'Entretenimento', 'Negocios',
              'Midia Social', 'Tecnologia', 'Mundo']
    for n in range(len(colunas)):
        if row[colunas[n]] == 1:
            val = saidas[n]
            break
    return val

def Agrupamento_Categoria(df):
    colunas = [' data_channel_is_lifestyle', ' data_channel_is_entertainment', ' data_channel_is_bus', ' data_channel_is_socmed',
               ' data_channel_is_tech', ' data_channel_is_world']
    for coluna in colunas:
        df[coluna] = df[coluna].astype(int)
    df['Categoria_Noticia'] = df.apply(categorias, axis=1)
    df.drop(colunas, axis=1, inplace=True)
    return df

def Renomeando_columns_int(df):
    nomeColunaAnt = ['url', ' n_tokens_title', ' n_tokens_content', ' num_hrefs', ' num_self_hrefs',
            ' num_imgs', ' num_videos', ' num_keywords', ' is_weekend', ' shares']
    nomeColunaNew = nomeColunaAnt.copy()
    #nomeColunaNew = ['Link', 'Num_palavras_titulo', 'Num_palavras_conteudo', 'Num_links_gerais', 'Num_links_noticias',
    #          'Num_imagens', 'Num_videos', 'Num_palavras-chaves', 'Publicado_fim_semana', 'Compartilhamentos']
    dictionary = dict(zip(nomeColunaAnt, nomeColunaNew))
    df.rename(columns=dictionary, inplace=True)
    for coluna in nomeColunaNew:
        try:
            df[coluna] = df[coluna].astype(int)
        except:
            pass
    return df

def Renomeando_columns_float(df):
    nomeColunaAnt = [' average_token_length', ' n_unique_tokens', ' n_non_stop_words',
                     ' global_subjectivity', ' global_rate_positive_words', ' global_rate_negative_words']
    nomeColunaNew = nomeColunaAnt.copy()
    #nomeColunaNew = ['Comprimento_medio_palavras', 'Taxa_palavras_unicas', 'Taxa_palavras_Continuas',
    #                 'Subjetividade_texto', 'Taxa_palavras_positivas', 'Taxa_palavras_negativas']
    dictionary = dict(zip(nomeColunaAnt, nomeColunaNew))
    df.rename(columns=dictionary, inplace=True)
    return df

def Conversao_columns_int(df):
    colunas = df.columns.values.tolist()
    for coluna in colunas:
        try:
            df[coluna] = df[coluna].astype(int)
        except:
            pass
    return df

def cria_amostragem_data(inicial, final, df):
    mask = (df['Data_Publicado'] >= inicial) & (df['Data_Publicado'] <= final)
    return df.loc[mask]

def Numerizacao_Categoria(row):
    val = '0'
    entradas = ['Nenhuma', 'Estilo de vida', 'Entretenimento',
                'Negocios', 'Midia Social', 'Tecnologia', 'Mundo']
    saidas = ['0', '1', '2',
              '3', '4', '5', '6']
    for n in range(len(entradas)):
        if row['Categoria_Noticia'] == entradas[n]:
            val = saidas[n]
            break
    return val

def Numerizacao_Dias_Semana(row):
    val = '0'
    entradas = ['Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo']
    saidas = ['2', '3', '4', '5', '6', '7', '1']
    for n in range(len(entradas)):
        if row['Dia_Publicado'] == entradas[n]:
            val = saidas[n]
            break
    return val

def classifica_niv_popularidade(row):
    val = '0'
    entradas = [dfcond_nv_popu['20%'], dfcond_nv_popu['40%'], dfcond_nv_popu['60%'], dfcond_nv_popu['80%'], dfcond_nv_popu['max']]
    saidas = ['1', '2', '3', '4', '5']
    for n in range(len(entradas)):
        if int(row[' shares']) <= int(entradas[n]):
            val = saidas[n]
            break
    return val

def gera_amostragem(data_inicial='2013-01-01', data_final='2014-12-31', gerar_csv=True, if_existente=False):
    global dfcond_nv_popu
    if not if_existente:
        df = pd.read_csv('bases/OnlineNewsPopularity.csv')  # leitura da base
        df = Criacao_data_column(df)
        df = Agrupamento_Dias_Semana(df)
        df = Agrupamento_Categoria(df)
        df = Renomeando_columns_int(df)
        df = Renomeando_columns_float(df)
        df['Dia_Publicado'] = df.apply(Numerizacao_Dias_Semana, axis=1)
        df['Categoria_Noticia'] = df.apply(Numerizacao_Categoria, axis=1)
        dfcond_nv_popu = df[' shares'].describe(percentiles=[.20, .40, .60, .80])
        dfcond_nv_popu = df['Compartilhamentos'].describe(percentiles=[.20, .40, .60, .80])
        print(dfcond_nv_popu)
        df['Nivel_Popularidade'] = df.apply(classifica_niv_popularidade, axis=1)
        df = cria_amostragem_data(data_inicial, data_final, df)
        df = Reducao_drop_columns(df)
        if gerar_csv:
            df.to_csv('bases/OnlineNewsPopularity_pre-processamento_' + data_inicial + '_to_' + data_final + '.csv', sep=',', index=False)
        return df
    else:
        try:
            return pd.read_csv('bases/OnlineNewsPopularity_pre-processamento_' + data_inicial + '_to_' + data_final + '.csv')
        except:
            gera_amostragem(data_inicial=data_inicial, data_final=data_final, gerar_csv=True, if_existente=False)



if __name__ == "__main__":
    gera_amostragem(data_inicial='2013-01-01', data_final='2013-12-31')
