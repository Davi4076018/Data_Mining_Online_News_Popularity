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

    fig = plt.figure(figsize=(30, 18))
    for i, col in enumerate(df):
        if i == 15:
            break
        ax = fig.add_subplot(5, 3, (i + 1))
        sns.scatterplot(x='ram', y=col, hue='price_range', data=df, palette="tab10")
