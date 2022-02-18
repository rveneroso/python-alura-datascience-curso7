import seaborn as sns

def plotar(origem_dados, titulo, label_eixox, label_eixoy, x, y):
    # Definindo a palheta de cores
    sns.set_palette('Accent')
    # Adicionando um grid ao gráfico
    sns.set_style('darkgrid')
    # Gera um gráfico para verificar se as vendas aumentaram com o passar do tempo.
    ax = sns.lineplot(x=x, y=y, data=origem_dados)
    # Aumentando o tamanho da imagem para 12 x 6 polegadas
    ax.figure.set_size_inches(12, 6)
    # Configurando um título para o gráfico. O título será alinhado à esquerda e terá o tamanho da fonte igual a 18.
    ax.set_title(titulo, loc='left', fontsize=18)
    # Definindo o label a ser exibido para o eixo x
    ax.set_xlabel(label_eixox, fontsize=14)
    ax.set_ylabel(label_eixoy, fontsize=14)

    return ax