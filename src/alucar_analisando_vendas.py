import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import funcoes_graficos as fg

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

# Cria colunas que serão utilizadas posteriormente.
# Adicionando uma coluna na qual fica registrado o aumento das vendas em relação ao mês anterior.
alucar['aumento'] = alucar['vendas'].diff()
# Adiciona a coluna que define a aceleração no crescimento das vendas
alucar['aceleracao'] = alucar['aumento'].diff()

# Salvando o arquivo com a coluna mes convertida para datetime.
alucar.to_csv('../data/alucar_convertido.csv', index=False)

# Código refatorado para utilizar a função plotar().
fg.plotar(alucar,'Vendas da Alucar no Período de 2017 a 2018','Meses',
          'Vendas (R$)','mes','vendas')
plt.show()
