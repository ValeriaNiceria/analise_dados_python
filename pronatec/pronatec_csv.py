# importando a biblioteca pandas
import pandas as pd

# Informa para o pandas mostrar o gráfico no jupyter notebook
# %matplotlib inline

# Lendo o arquivo CSV e atribuindo a variável
# O pandas vai converter o arquivo em um DataFrame
df = pd.read_csv('pronatec.csv', sep=';', encoding='latin1')

# Mostra as 5 primeiras linhas do DataFrame
df.head()

# Quantas linhas tem o arquivo
df.count()

# Seleciona no DataFrame somente a coluna especificada
# Retorna a quantidade de unidades em cada região do Brasil
valores_regiao_unidade = df['NOME_REGIAO_UNIDADE'].value_counts()

# Contando o número de unidades em cada estado
valores_uf_unidade = df['SIGLA_UF_UNIDADE'].value_counts()

# Mostrando os dados em um gráfico
valores_uf_unidade.plot.bar()
