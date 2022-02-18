import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

alucar = pd.read_csv('../data/alucar.csv')

# Exibindo o tamanho do DataFrame
print('Quantidade de linhas e colunas presentes no arquivo: ', alucar.shape)

# Exibindo a quantidade de dados nulos. São feitas duas chamadas ao método sum() para que o resultado seja um só,
# totalizando dados nulos da coluna mes com dados nulos da coluna vendas.
print('Quantidade de dados nulos no arquivo: ', alucar.isna().sum().sum())

# Identificando os tipos de dados das colunas do arquivo alucar.csv
print(alucar.dtypes)
'''
mes       object
vendas     int64
dtype: object
'''

# Para se trabalhar com Time Series é importante que o dado na coluna mes seja do tipo datetime.
alucar['mes'] = pd.to_datetime(alucar['mes'])
print(alucar.dtypes)
'''
mes       datetime64[ns]
vendas             int64
dtype: object
'''
# Realizando ajustes no gráfico. Observação: esses ajustes precisam ser feitos antes da linha onde o lineplot é
# chamado. Caso contrário, as configurações não serão aplicadas.

# Definindo a palheta de cores
sns.set_palette('Accent')
# Adicionando um grid ao gráfico
sns.set_style('darkgrid')
# Gera um gráfico para verificar se as vendas aumentaram com o passar do tempo.
ax = sns.lineplot(x='mes',y='vendas',data=alucar)
# Aumentando o tamanho da imagem para 12 x 6 polegadas
ax.figure.set_size_inches(12,6)
# Configurando um título para o gráfico. O título será alinhado à esquerda e terá o tamanho da fonte igual a 18.
ax.set_title('Vendas da Alucar no Período de 2017 a 2018', loc='left', fontsize=18)
# Definindo o label a ser exibido para o eixo x
ax.set_xlabel('Meses', fontsize=14)
ax.set_ylabel('Vendas (R$)', fontsize=14)
plt.show()
# Salvando o arquivo com a coluna mes convertida para datetime.
alucar.to_csv('../data/alucar_convertido.csv')
