# importando a bibliteca pandas
import pandas as pd

# Importando somente algumas colunas do arquivo
'''
3 - hospital
6 - município
7 - complexidade
8 - carater atendimento
12 - sub grupo de procedimento
14 - procedimento
'''
df = pd.read_csv('sih-janeiro-2017-cirurgias-eletiva-e-emergencia.csv', sep=';', encoding='latin1', usecols=[3, 6, 7, 8, 12, 14])

# Exibir as 3 primeiras linhas do DataFrame
df.head(3)

# Alterando o nome das colunas
df.columns = ['Hospital', 'Municipio', 'Complexidade', 'Carater Atendimento', 'Sub Grupo Procedimento', 'Procedimento']

# Exibindo as primeiras linhas do DataFrame com o cabeçalho alterado
df.head()

# Descrevendo as colunas
df.describe()

# Listando os hospital presentes nos dados
df['Hospital'].unique()

# Listando os hospitais e número de cirurgias realizadas
df['Hospital'].value_counts()

# Listando o número de cirurgias por sub grupo procedimentos
sub_grupo_procedimento = df['Sub Grupo Procedimento'].value_counts()

# Plotando o gráfico por sub grupo procedimento
sub_grupo_procedimento.plot.bar()

# Criando um novo DataFrame onde somente terá os dados do hospital tratado
df_hosp_base = df[df['Hospital'] == '0010456 HBDF HOSPITAL DE BASE DO DISTRITO FEDERAL']

# Listando os dados iniciais do novo DataFrame
df_hosp_base.head()

# Listando os dados finais do DataFrame
df_hosp_base.tail()

# Listando linhas aleatórias do DataFrame
df_hosp_base.sample(5)

# Listando a quantidade de procedimentos realizados no Hospital de Base
df_hosp_base['Procedimento'].value_counts()

# Fatiando o DataFrame com base em um pedaço de palavra
df_hosp_base[df_hosp_base['Procedimento'].str.contains('AMPUTA')]

# Criando um novo DataFrame apartir do original onde terá apenas procedimentos de 'Parto Cesariano'
df_parto_cesariano = df[df['Procedimento'] == 'PARTO CESARIANO']

# Listando as primeiras linhas do DataFrame criado
df_parto_cesariano.head()

# Verificando a quantidade de partos cesarianos por hospital
df_parto_cesariano['Hospital'].value_counts()

# Verificando a quantidade de partos por 'Carater Atendimento'
df_parto_cesariano['Carater Atendimento'].value_counts()

# Plotando os hospitais no gráfico de barras horizontal
df_parto_cesariano['Hospital'].value_counts().plot.barh()

# Melhorando o gráfico de barras horizontal
# Invertendo a ordem e colocando título
df_parto_cesariano['Hospital'].value_counts(ascending=True).plot.barh(title='Quantidade de Partos Cesarianos por Hospital')