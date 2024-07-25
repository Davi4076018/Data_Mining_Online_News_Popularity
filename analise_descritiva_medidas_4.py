import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import random
from IPython.display import display

import seaborn as sns

from pre_processamento_dos_dados_1 import gera_amostragem


def medida_tendencia_central(df_clean):
    measures = {
        'Feature': [],
        'Mean': [],
        'Mode': [],
        'Median': [],
        'Ponto Médio': []
    }

    for column in df_clean.columns:
        if df_clean[column].dtype in [int, float]:
            measures['Feature'].append(column)
            measures['Mean'].append(df_clean[column].mean())
            measures['Mode'].append(df_clean[column].mode().values[0])
            measures['Median'].append(df_clean[column].median())
            measures['Ponto Médio'].append((df_clean[column].max() + df_clean[column].min()) / 2)

    table_measures = pd.DataFrame({
        'Feature': measures['Feature'],
        'Mean': measures['Mean'],
        'Mode': measures['Mode'],
        'Median': measures['Median'],
        'Ponto Médio': measures['Ponto Médio']
    })

    display(table_measures)

def medida_dispersao(df_clean):
    measures = {
        'Feature': [],
        'Range': [],
        'Standard Deviation': [],
    }

    for column in df_clean.columns:
        if df_clean[column].dtype in [int, float]:
            measures['Feature'].append(column)
            measures['Range'].append(df_clean[column].max() - df_clean[column].min())
            measures['Standard Deviation'].append(df_clean[column].std())

    table_measures = pd.DataFrame({
        'Feature': measures['Feature'],
        'Range': measures['Range'],
        'Standard Deviation': measures['Standard Deviation']
    })

    display(table_measures)

def medida_posicao_relativa(df_clean):
    measures = {
        'Feature': [],
        'Z-Score': [],
        '25th Percentile': [],
        '50th Percentile': [],
        '75th Percentile': []
    }

    for column in df_clean.columns:
        if df_clean[column].dtype in [int, float]:
            measures['Feature'].append(column)

            # Z-Score
            z_score = (df_clean[column] - df_clean[column].mean()) / df_clean[column].std()
            measures['Z-Score'].append(z_score.iloc[0])

            # Quantiles
            q25 = np.percentile(df_clean[column], 25)
            q50 = np.percentile(df_clean[column], 50)
            q75 = np.percentile(df_clean[column], 75)
            measures['25th Percentile'].append(q25)
            measures['50th Percentile'].append(q50)
            measures['75th Percentile'].append(q75)

    table_measures = pd.DataFrame({
        'Feature': measures['Feature'],
        'Z-Score': measures['Z-Score'],
        '25th Percentile': measures['25th Percentile'],
        '50th Percentile': measures['50th Percentile'],
        '75th Percentile': measures['75th Percentile']
    })

    display(table_measures)

def medida_associacao(df_clean):
    measures = {
        'Feature': [],
        'Covariance': [],
        'Correlation': []
    }

    for column in df_clean.columns:
        if df_clean[column].dtype in [int, float]:
            measures['Feature'].append(column)

            # Covariance
            cov_value = df_clean[column].cov(df_clean['Nivel_Popularidade'])
            measures['Covariance'].append(cov_value)

            # Correlation
            corr_value = df_clean[column].corr(df_clean['Nivel_Popularidade'])
            measures['Correlation'].append(corr_value)

    table_measures = pd.DataFrame({
        'Feature': measures['Feature'],
        'Covariance': measures['Covariance'],
        'Correlation': measures['Correlation']
    })

    display(table_measures)

if __name__ == "__main__":
    df = gera_amostragem(data_inicial='2013-01-01', data_final='2013-12-31', gerar_csv=True, if_existente=True)
    medida_tendencia_central(df)
    medida_dispersao(df)
    medida_posicao_relativa(df)
    medida_associacao(df)
