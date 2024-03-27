import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns

def z_score_nomalization(df, target, features):
    x = df.loc[:, features].values
    y = df.loc[:, [target]].values
    x_zscore = StandardScaler().fit_transform(x)
    y_zscore = StandardScaler().fit_transform(y)
    normalized_zscore_x = pd.DataFrame(x_zscore, columns=features)
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
    fig = plt.figure(figsize=(20, 12))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('Principal Component 1', fontsize=15)
    ax.set_ylabel('Principal Component 2', fontsize=15)
    ax.set_title('4 component PCA', fontsize=20)
    targets = [0, 1, 2, 3]
    colors = ['r', 'g', 'b', 'y']
    for target, color in zip(targets, colors):
        print('target = ', target)
        print('targetColumn = ', targetColumn)
        indicesToKeep = finalDf[targetColumn] == target
        #print(indicesToKeep.to_string())
        ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'],
                   finalDf.loc[indicesToKeep, 'principal component 2'],
                   c=color, s=50)
        print('a')
    ax.legend(targets)
    ax.grid()
    plt.show()


def VisualizePca3dProjection(finalDf, targetColumn):
    fig = plt.figure(figsize=(20, 12))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('Principal Component 1', fontsize=15)
    ax.set_ylabel('Principal Component 2', fontsize=15)
    ax.set_zlabel('Principal Component 3', fontsize=15)
    ax.set_title('4 component PCA', fontsize=20)
    targets = [0, 1, 2, 3]
    colors = ['r', 'g', 'b', 'y']
    for target, color in zip(targets, colors):
        indicesToKeep = finalDf[targetColumn] == target
        ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'],
                   finalDf.loc[indicesToKeep, 'principal component 2'],
                   finalDf.loc[indicesToKeep, 'principal component 3'],
                   c=color, s=50)
    ax.legend(targets)
    ax.grid()
    plt.show()


if __name__ == "__main__":
    df = pd.read_csv('bases/OnlineNewsPopularity_pre-processamento_1.csv')
    #df = pd.read_csv('bases/OnlineNewsPopularity_pre-processamento_1_2013.csv')
    #df = pd.read_csv('bases/OnlineNewsPopularity_pre-processamento_1_2014.csv')
    print(df.describe().to_string())
    target = 'Compartilhamentos'
    features = df.drop(['Link', 'Compartilhamentos', 'Data_Publicado'], axis=1).columns.values.tolist()
    zscore_norm = z_score_nomalization(df, target, features)
    min_max_norm = min_max_nomalization(df, target, features)
    print(zscore_norm.describe().to_string())
    print(min_max_norm.describe().to_string())
    #plot_matriz_correlacao(min_max_norm)

    # PCA
    # pca = PCA(n_components=2)
    x_zscore = StandardScaler().fit_transform(df.loc[:, features].values)

    pca = PCA()
    pca3d = PCA(n_components=3)
    principalComponents = pca.fit_transform(x_zscore)
    print(principalComponents)
    print(principalComponents[:, 6:8])
    # print('Explained variance ratio:')
    # print(pca.explained_variance_ratio_.tolist())
    # print(x_minmax)

    # Create a DataFrame with the two principal components = memory intern and ram

    principalDf = pd.DataFrame(data=principalComponents[:, 0:2],
                               columns=['principal component 1', 'principal component 2'])
    principalDf3d = pd.DataFrame(data=principalComponents[:, 0:3],
                                 columns=['principal component 1', 'principal component 2', 'principal component 3'])

    finalDf = pd.concat([principalDf, df[[target]]], axis=1)
    finalDf3 = pd.concat([principalDf3d, df[[target]]], axis=1)
    # finalDf.describe()
    print(finalDf)
    print(finalDf3)
    VisualizePcaProjection(finalDf, target)
   # VisualizePca3dProjection(finalDf3, target)
    # VisualizePca3dProjection(finalDf, target)


