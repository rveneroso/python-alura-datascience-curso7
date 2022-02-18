import pandas as pd
from pandas.plotting import autocorrelation_plot
import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
plt.suptitle('Correlação das Vendas', fontsize=18,x=0.26,y=0.95)
alucar = pd.read_csv('../data/alucar_convertido.csv')
autocorrelation_plot(alucar['vendas'])
plt.suptitle('Correlação do Aumento', fontsize=18,x=0.26,y=0.95)
autocorrelation_plot(alucar['aumento'][1:])
plt.suptitle('Correlação da Aceleração', fontsize=18,x=0.26,y=0.95)
autocorrelation_plot(alucar['aceleracao'][2:])
plt.show()
