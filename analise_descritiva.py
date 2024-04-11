import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import random
from IPython.display import display

import seaborn as sns

from pre_processamento_dos_dados import gera_amostragem


def estilo_tabela(val):
    return 'text-align: center;'


def plot_histogram(column, bins):
    # Set up the figure with two subplots
    plt.figure(figsize=(15, 6))
    plt.subplots_adjust(wspace=0.3)

    # Histogram of absolute frequencies
    plt.subplot(1, 2, 1)
    n, bins, patches = plt.hist(df[column], bins=bins, edgecolor='black', color='skyblue')
    plt.title(f'Histograma de Frequência Absoluta: {column}', fontsize=15)
    plt.xlabel(column, fontsize=12)
    plt.ylabel('Frequência Absoluta', fontsize=12)
    plt.grid(axis='y', alpha=0.9)

    # Histogram of relative frequencies
    plt.subplot(1, 2, 2)
    weights = (np.ones_like(df[column]) / len(df[column])) * 100  # Weights to convert counts to percentages
    n, bins, patches = plt.hist(df[column], bins=bins, weights=weights, edgecolor='black', color='coral')
    plt.title(f'Histograma de Frequência Relativa: {column}', fontsize=15)
    plt.xlabel(column, fontsize=12)
    plt.ylabel('Frequência Relativa (%)', fontsize=12)
    plt.grid(axis='y', alpha=0.9)

    # Display the plot
    plt.tight_layout()
    plt.show()


def frequencia(df, name_column, classe_lenght):
    classe_lenght = int(classe_lenght)
    dfcoluna = df[name_column].describe()
    var_min = int(dfcoluna['min'])
    var_max = int(dfcoluna['max'])
    amplitude = math.ceil((var_max - var_min) / classe_lenght)
    print(amplitude)
    max_limits = [var_min + amplitude * i for i in range(1, classe_lenght + 1)]
    min_limits = [var_min + amplitude * i for i in range(0, classe_lenght)]
    print(max_limits)
    print(min_limits)
    # criar uma nova coluna classificando os valores de ram com os novos rótulos
    bins = min_limits.copy()
    for n in range(1, len(bins)):
        bins[n] = int(bins[n])
    bins.append(int(max_limits[len(max_limits) - 1]))
    print(bins)

    df[name_column + '_class'] = pd.cut(df[name_column],
                             bins=bins, labels=list(range(1, classe_lenght + 1)))

    class_summary = df[name_column + '_class'].value_counts().sort_index().rename('frequency').to_frame()

    class_summary['lower_limit'] = min_limits
    class_summary['upper_limit'] = max_limits
    class_summary['relative_frequency'] = (class_summary['frequency'] / class_summary['frequency'].sum()) * 100
    class_summary['cumulative_frequency'] = class_summary['frequency'].cumsum()
    class_summary['cumulative_frequency_percentage'] = (class_summary['cumulative_frequency'] / class_summary[
        'frequency'].sum()) * 100
    print(class_summary.to_string())
    # Styling
    styled_df = class_summary.style.applymap(estilo_tabela) \
        .set_properties(**{'width': '100px'}) \
        .set_table_styles([{'selector': '', 'props': [('border', '1px solid black')]}])
    display(styled_df)
    plot_histogram(name_column + '_class', classe_lenght)




if __name__ == "__main__":
    df = gera_amostragem(data_inicial='2013-01-01', data_final='2013-12-31', gerar_csv=True, if_existente=True)

    target = 'Nivel_Popularidade'
    features = df.columns.values.tolist()

    print(df.describe().to_string())
    print(df.columns.values.tolist())
    columns = [' is_weekend']
    classes = [2]

    for i in range(len(columns)):
        frequencia(df, columns[i], classes[i])