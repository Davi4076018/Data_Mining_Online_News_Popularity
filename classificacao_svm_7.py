import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import random
from IPython.display import display

import seaborn as sns

from pre_processamento_dos_dados_1 import gera_amostragem





if __name__ == "__main__":
    df = gera_amostragem(data_inicial='2013-01-01', data_final='2013-12-31', gerar_csv=True, if_existente=True)
