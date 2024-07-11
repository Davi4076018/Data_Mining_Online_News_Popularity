from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import pandas as pd
from sklearn.preprocessing import StandardScaler

from pre_processamento_dos_dados_1 import gera_amostragem

def main():

    df = gera_amostragem(data_inicial='2013-01-01', data_final='2014-12-31', gerar_csv=True, if_existente=True)
    features = df.columns.values.tolist()

    target = 'Nivel_Popularidade'
    # Separating out the features
    X = df.loc[:, features].values
    print(X.shape)

    # Separating out the target
    y = df.loc[:,[target]].values

    # Standardizing the features
    X = StandardScaler().fit_transform(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    print(X_train.shape)
    print(X_test.shape)

    clf = DecisionTreeClassifier(max_leaf_nodes=4)
    clf.fit(X_train, y_train)
    tree.plot_tree(clf)
    plt.show()
    
    predictions = clf.predict(X_test)
    print(predictions)
    
    result = clf.score(X_test, y_test)
    print('Acuraccy:')
    print(result)


if __name__ == "__main__":
    main()