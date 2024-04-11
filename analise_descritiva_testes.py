import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import random
from IPython.display import display

import seaborn as sns

from pre_processamento_dos_dados import gera_amostragem





if __name__ == "__main__":
    df = gera_amostragem(data_inicial='2013-01-01', data_final='2013-12-31', gerar_csv=True, if_existente=True)

    target = 'Nivel_Popularidade'
    features = df.columns.values.tolist()

    # Criando o ambiente do gráfico
    sns.set(font_scale=1.5)
    sns.set_style("dark")
    plt.figure(figsize=(10, 10))
    for n in range(1, 6):
        dfnivel = df.loc[df['Nivel_Popularidade'] == n]
        dfnivel_0 = dfnivel.loc[dfnivel[' is_weekend'] == 0]
        dfnivel_1 = dfnivel.loc[dfnivel[' is_weekend'] == 1]
        plt.pie([len(dfnivel_0), len(dfnivel_1)], labels= ['Publicado Durante a Semana', 'Publicado Fim de Semana'], autopct='%1.1f%%')
        plt.title("Nivel de Popularidade " + str(n))

        plt.show()

