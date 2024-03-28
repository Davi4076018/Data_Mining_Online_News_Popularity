import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns

from pre_processamento_dos_dados import gera_amostragem

def z_score_nomalization(df, target, features):
    x = df.loc[:, features].values
    x_zscore = StandardScaler().fit_transform(x)
    normalized_zscore = pd.DataFrame(x_zscore, columns=features)
    normalized_zscore = pd.concat([normalized_zscore, df[[target]]], axis=1)
    return normalized_zscore

def min_max_nomalization(df, target, features):
    x = df.loc[:, features].values
    x_minmax = MinMaxScaler().fit_transform(x)
    normalized_minmax = pd.DataFrame(x_minmax, columns=features)
    normalized_minmax = pd.concat([normalized_minmax, df[[target]]], axis=1)
    return normalized_minmax

def plot_matriz_correlacao(normalized_minmax):
    plt.figure(figsize=(20, 12))
    sns.heatmap(normalized_minmax.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=2)
    plt.title('Correlation Matrix')
    plt.show()


def VisualizePcaProjection(finalDf, targetColumn):
    colunas_nomes = finalDf.columns.values.tolist()
    fig = plt.figure(figsize=(20, 12))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel(colunas_nomes[0], fontsize=15)
    ax.set_ylabel(colunas_nomes[1], fontsize=15)
    ax.set_title('4 component PCA', fontsize=20)
    targets = [1, 2, 3, 4, 5]
    colors = ['r', 'g', 'b', 'y', 'purple']
    for target, color in zip(targets, colors):
        indicesToKeep = finalDf[targetColumn] == target
        ax.scatter(finalDf.loc[indicesToKeep, colunas_nomes[0]],
                   finalDf.loc[indicesToKeep, colunas_nomes[1]],
                   c=color, s=50)
    ax.legend(targets)
    ax.grid()
    plt.show()


def VisualizePca3dProjection(finalDf, targetColumn):
    colunas_nomes = finalDf.columns.values.tolist()
    fig = plt.figure(figsize=(20, 12))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel(colunas_nomes[0], fontsize=15)
    ax.set_ylabel(colunas_nomes[1], fontsize=15)
    ax.set_zlabel(colunas_nomes[2], fontsize=15)
    ax.set_title('4 component PCA', fontsize=20)
    targets = [1, 2, 3, 4, 5]
    colors = ['r', 'g', 'b', 'y', 'purple']
    for target, color in zip(targets, colors):
        indicesToKeep = finalDf[targetColumn] == target
        ax.scatter(finalDf.loc[indicesToKeep, colunas_nomes[0]],
                   finalDf.loc[indicesToKeep, colunas_nomes[1]],
                   finalDf.loc[indicesToKeep, colunas_nomes[2]],
                   c=color, s=50)
    ax.legend(targets)
    ax.grid()
    plt.show()


if __name__ == "__main__":
    df = gera_amostragem(data_inicial='2013-01-01', data_final='2014-12-31', gerar_csv=True, if_existente=True)
    print(df.describe().to_string())
    target = 'Nivel_Popularidade'
    features = df.drop(['Link', 'Nivel_Popularidade', 'Data_Publicado'], axis=1).columns.values.tolist()
    zscore_norm = z_score_nomalization(df, target, features)
    min_max_norm = min_max_nomalization(df, target, features)
    print(zscore_norm.describe().to_string())
    print(min_max_norm.describe().to_string())
    plot_matriz_correlacao(min_max_norm)

    # PCA
    x_zscorePCA = StandardScaler().fit_transform(df.loc[:, ['Publicado_fim_semana', 'Num_links_gerais', 'Num_imagens']].values)

    pca = PCA()
    pca3d = PCA(n_components=3)
    principalComponents = pca.fit_transform(x_zscorePCA)


    principalDf = pd.DataFrame(data=principalComponents[:, 0:2],
                               columns=['Publicado_fim_semana', 'Num_links_gerais'])
    principalDf3d = pd.DataFrame(data=principalComponents[:, 0:3],
                                 columns=['Publicado_fim_semana', 'Num_links_gerais', 'Num_imagens'])

    finalDf = pd.concat([principalDf, df[[target]]], axis=1)
    finalDf3 = pd.concat([principalDf3d, df[[target]]], axis=1)

    print(finalDf)
    print(finalDf3)
    VisualizePcaProjection(finalDf, target)
    VisualizePca3dProjection(finalDf3, target)


