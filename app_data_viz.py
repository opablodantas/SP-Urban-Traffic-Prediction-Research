# Imports

import streamlit as st
import numpy as np
import pandas as pd 
import plotly
import plotly.express as px
import seaborn as sns

# Adicionando titulo para a visualizaçao
st.markdown("<h1 style='text-align: center; '><strong><u>Visualização de Dados Interativo sobre o Comportamento do Transito de São Paulo</u></strong></h1>", unsafe_allow_html = True)
    
# Funçao para carregar os dados 
def carrega_dados():
	dados = pd.read_csv('behavior_of_the_urban_traffic.csv', sep = ';', decimal = ',')
	return dados 

# Carrega os dados 
df = carrega_dados()
st.write('')

# Como a hora está em numeros, vamos dividi-lo em periodos 
def HoraDoDia(num):
    if num <= 11:        
        return 'Manha'
    elif num >= 11 and num <= 22 :
        return 'Tarde'
    elif num >= 22:
        return 'Noite'

# Criando as classes
df['HoraDoDia'] = df['Hour (Coded)'].map(HoraDoDia)


# Substituindo os numeros pela hora correspodente 

df.loc[df['Hour (Coded)'] == 1,'Hour (Coded)']='7:00'
df.loc[df['Hour (Coded)'] == 2,'Hour (Coded)']='7:30'
df.loc[df['Hour (Coded)'] == 3,'Hour (Coded)']='8:00'
df.loc[df['Hour (Coded)'] == 4,'Hour (Coded)']='8:30'
df.loc[df['Hour (Coded)'] == 5,'Hour (Coded)']='9:00'
df.loc[df['Hour (Coded)'] == 6,'Hour (Coded)']='9:30'
df.loc[df['Hour (Coded)'] == 7,'Hour (Coded)']='10:00'
df.loc[df['Hour (Coded)'] == 8,'Hour (Coded)']='10:30'
df.loc[df['Hour (Coded)'] == 9,'Hour (Coded)']='11:00'
df.loc[df['Hour (Coded)'] == 10,'Hour (Coded)']='11:30'
df.loc[df['Hour (Coded)'] == 11,'Hour (Coded)']='12:00'
df.loc[df['Hour (Coded)'] == 12,'Hour (Coded)']='12:30'
df.loc[df['Hour (Coded)'] == 13,'Hour (Coded)']='13:00'
df.loc[df['Hour (Coded)'] == 14,'Hour (Coded)']='13:30'
df.loc[df['Hour (Coded)'] == 15,'Hour (Coded)']='14:00'
df.loc[df['Hour (Coded)'] == 16,'Hour (Coded)']='14:30'
df.loc[df['Hour (Coded)'] == 17,'Hour (Coded)']='15:00'
df.loc[df['Hour (Coded)'] == 18,'Hour (Coded)']='15:30'
df.loc[df['Hour (Coded)'] == 19,'Hour (Coded)']='16:00'
df.loc[df['Hour (Coded)'] == 20,'Hour (Coded)']='16:30'
df.loc[df['Hour (Coded)'] == 21,'Hour (Coded)']='17:00'
df.loc[df['Hour (Coded)'] == 22,'Hour (Coded)']='17:30'
df.loc[df['Hour (Coded)'] == 23,'Hour (Coded)']='18:00'
df.loc[df['Hour (Coded)'] == 24,'Hour (Coded)']='18:30'
df.loc[df['Hour (Coded)'] == 25,'Hour (Coded)']='19:00'
df.loc[df['Hour (Coded)'] == 26,'Hour (Coded)']='19:30'
df.loc[df['Hour (Coded)'] == 27,'Hour (Coded)']='20:00'

# Criando uma função para criar a variavel classe que vai conter os labels das classes 

def Class(num):
    if num < 9:        
        return 'Baixo'
    elif num >= 9 and num < 18 :
        return 'Medio'
    elif num >= 18:
        return 'Alto'

# Criando as classes
df['Class'] = df['Slowness in traffic (%)'].map(Class)

























st.write('Visualizando Dados Brutos')
st.write(df)

# Usando crosstap para uma melhor visualização
st.write('Tabela Cruzada para Observar a Hora e a Classe de Transito')
cross_date = pd.crosstab(df['Class'], df['Hour (Coded)'])
st.write(cross_date)

#st.selectbox('Selecione a coluna que deseja ver:', df.columns)


# Menu lateral
# Título do menu lateral
st.sidebar.markdown("<h1 style='text-align: center; color: #baccee;'><strong><u></u></strong></h1>", unsafe_allow_html = True)

st.sidebar.subheader('Análises Graficas')
template = 'plotly_dark'

# Caixa de seleção
select = st.sidebar.selectbox('Escolha o Tipo de Acidente a ser visto', df.columns, key = '1')


# Opções da Caixa de Seleção 
if select == 'Hour (Coded)':
	fig = px.scatter(df, x = 'Hour (Coded)', y = 'Slowness in traffic (%)', )
	fig.update_layout(title = 'Dispersão entre A Hora e a Porcentagem de Lentidão',
		xaxis_title = 'Hora',
        yaxis_title = 'Lentidão (em %)',
        template = template)
	st.plotly_chart(fig)
	st.write('O gráfico acima mostra que conforme o tempo vai passando, a lentidão do trafego de veiculos tem uma tendencia a aumentar')


if select == 'Immobilized bus':
	
	# Grafico de barras
	fig = px.histogram(df, x='Immobilized bus', color= 'Class')
	fig.update_layout(title = 'Análise de Variabilidade do Acidente',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Quantidade de Ocorrências',
        template = template)


	# Grafico de Dispersão
	fig2 = px.scatter(df, x="Immobilized bus", y="Slowness in traffic (%)") 
	fig2.update_layout(title = 'Comparação entre o Número de Ocorrências e a Porcentagem de Lentidão',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Porcentagem de Lentidão',)
	st.plotly_chart(fig)
	st.plotly_chart(fig2)

	st.subheader('Conclusão:')


if select == 'Broken Truck':
	
	# Grafico de barras
	fig = px.histogram(df, x='Broken Truck', barmode='group')
	fig.update_layout(title = 'Análise de Variabilidade do Acidente',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Quantidade de Ocorrências',
        template = template)


	# Grafico de Dispersão
	fig2 = px.scatter(df, x="Broken Truck", y="Slowness in traffic (%)") 
	fig2.update_layout(title = 'Comparação entre o Número de Ocorrências e a Porcentagem de Lentidão',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Porcentagem de Lentidão',)
	st.plotly_chart(fig)
	st.plotly_chart(fig2)

	st.subheader('Conclusão:')


if select == 'Vehicle excess':
	
	# Grafico de barras
	fig = px.histogram(df, x='Vehicle excess', barmode='group')
	fig.update_layout(title = 'Análise de Variabilidade do Acidente',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Quantidade de Ocorrências',
        template = template)


	# Grafico de Dispersão
	fig2 = px.scatter(df, x="Vehicle excess", y="Slowness in traffic (%)") 
	fig2.update_layout(title = 'Comparação entre o Número de Ocorrências e a Porcentagem de Lentidão',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Porcentagem de Lentidão',)
	st.plotly_chart(fig)
	st.plotly_chart(fig2)

	st.subheader('Conclusão:')


if select == 'Accident victim':
	
	# Grafico de barras
	fig = px.histogram(df, x='Accident victim', barmode='group')
	fig.update_layout(title = 'Análise de Variabilidade do Acidente',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Quantidade de Ocorrências',
        template = template)


	# Grafico de Dispersão
	fig2 = px.scatter(df, x="Accident victim", y="Slowness in traffic (%)") 
	fig2.update_layout(title = 'Comparação entre o Número de Ocorrências e a Porcentagem de Lentidão',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Porcentagem de Lentidão',)
	st.plotly_chart(fig)
	st.plotly_chart(fig2)

	st.subheader('Conclusão:')


if select == 'Running over':
	
	# Grafico de barras
	fig = px.histogram(df, x='Running over', color= 'Class')
	fig.update_layout(title = 'Análise de Variabilidade do Acidente',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Quantidade de Ocorrências',
        template = template)


	# Grafico de Dispersão
	fig2 = px.scatter(df, x="Running over", y="Slowness in traffic (%)") 
	fig2.update_layout(title = 'Comparação entre o Número de Ocorrências e a Porcentagem de Lentidão',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Porcentagem de Lentidão',)
	st.plotly_chart(fig)
	st.plotly_chart(fig2)

	st.subheader('Conclusão:')


if select == 'Fire vehicles':
	
	# Grafico de barras
	fig = px.histogram(df, x='Fire vehicles', barmode='group')
	fig.update_layout(title = 'Análise de Variabilidade do Acidente',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Quantidade de Ocorrências',
        template = template)


	# Grafico de Dispersão
	fig2 = px.scatter(df, x="Fire vehicles", y="Slowness in traffic (%)") 
	fig2.update_layout(title = 'Comparação entre o Número de Ocorrências e a Porcentagem de Lentidão',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Porcentagem de Lentidão',)
	st.plotly_chart(fig)
	st.plotly_chart(fig2)

	st.subheader('Conclusão:')


if select == 'Occurrence involving freight':
	
	# Grafico de barras
	fig = px.histogram(df, x='Occurrence involving freight', barmode='group')
	fig.update_layout(title = 'Análise de Variabilidade do Acidente',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Quantidade de Ocorrências',
        template = template)


	# Grafico de Dispersão
	fig2 = px.scatter(df, x="Occurrence involving freight", y="Slowness in traffic (%)") 
	fig2.update_layout(title = 'Comparação entre o Número de Ocorrências e a Porcentagem de Lentidão',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Porcentagem de Lentidão',)
	st.plotly_chart(fig)
	st.plotly_chart(fig2)

	st.subheader('Conclusão:')


if select == 'Incident involving dangerous freight':
	
	# Grafico de barras
	fig = px.histogram(df, x='Incident involving dangerous freight', barmode='group')
	fig.update_layout(title = 'Análise de Variabilidade do Acidente',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Quantidade de Ocorrências',
        template = template)


	# Grafico de Dispersão
	fig2 = px.scatter(df, x="Incident involving dangerous freight", y="Slowness in traffic (%)") 
	fig2.update_layout(title = 'Comparação entre o Número de Ocorrências e a Porcentagem de Lentidão',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Porcentagem de Lentidão',)
	st.plotly_chart(fig)
	st.plotly_chart(fig2)

	st.subheader('Conclusão:')


if select == 'Lack of electricity':
	
	# Grafico de barras
	fig = px.histogram(df, x='Lack of electricity', barmode='group')
	fig.update_layout(title = 'Análise de Variabilidade do Acidente',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Quantidade de Ocorrências',
        template = template)


	# Grafico de Dispersão
	fig2 = px.scatter(df, x="Lack of electricity", y="Slowness in traffic (%)") 
	fig2.update_layout(title = 'Comparação entre o Número de Ocorrências e a Porcentagem de Lentidão',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Porcentagem de Lentidão',)
	st.plotly_chart(fig)
	st.plotly_chart(fig2)

	st.subheader('Conclusão:')


if select == 'Fire':
	
	# Grafico de barras
	fig = px.histogram(df, x='Fire', barmode='group')
	fig.update_layout(title = 'Análise de Variabilidade do Acidente',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Quantidade de Ocorrências',
        template = template)


	# Grafico de Dispersão
	fig2 = px.scatter(df, x="Fire", y="Slowness in traffic (%)") 
	fig2.update_layout(title = 'Comparação entre o Número de Ocorrências e a Porcentagem de Lentidão',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Porcentagem de Lentidão',)
	st.plotly_chart(fig)
	st.plotly_chart(fig2)

	st.subheader('Conclusão:')


if select == 'Point of flooding':
	
	# Grafico de barras
	fig = px.histogram(df, x='Point of flooding', barmode='group')
	fig.update_layout(title = 'Análise de Variabilidade do Acidente',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Quantidade de Ocorrências',
        template = template)


	# Grafico de Dispersão
	fig2 = px.scatter(df, x="Point of flooding", y="Slowness in traffic (%)") 
	fig2.update_layout(title = 'Comparação entre o Número de Ocorrências e a Porcentagem de Lentidão',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Porcentagem de Lentidão',)
	st.plotly_chart(fig)
	st.plotly_chart(fig2)

	st.subheader('Conclusão:')


if select == 'Manifestations':
	
	# Grafico de barras
	fig = px.histogram(df, x='Manifestations', barmode='group')
	fig.update_layout(title = 'Análise de Variabilidade do Acidente',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Quantidade de Ocorrências',
        template = template)


	# Grafico de Dispersão
	fig2 = px.scatter(df, x="Manifestations", y="Slowness in traffic (%)") 
	fig2.update_layout(title = 'Comparação entre o Número de Ocorrências e a Porcentagem de Lentidão',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Porcentagem de Lentidão',)
	st.plotly_chart(fig)
	st.plotly_chart(fig2)

	st.subheader('Conclusão:')


if select == 'Defect in the network of trolleybuses':
	
	# Grafico de barras
	fig = px.histogram(df, x='Defect in the network of trolleybuses', barmode='group')
	fig.update_layout(title = 'Análise de Variabilidade do Acidente',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Quantidade de Ocorrências',
        template = template)


	# Grafico de Dispersão
	fig2 = px.scatter(df, x="Defect in the network of trolleybuses", y="Slowness in traffic (%)") 
	fig2.update_layout(title = 'Comparação entre o Número de Ocorrências e a Porcentagem de Lentidão',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Porcentagem de Lentidão',)
	st.plotly_chart(fig)
	st.plotly_chart(fig2)

	st.subheader('Conclusão:')


if select == 'Tree on the road':
	
	# Grafico de barras
	fig = px.histogram(df, x='Tree on the road', barmode='group')
	fig.update_layout(title = 'Análise de Variabilidade do Acidente',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Quantidade de Ocorrências',
        template = template)


	# Grafico de Dispersão
	fig2 = px.scatter(df, x="Tree on the road", y="Slowness in traffic (%)") 
	fig2.update_layout(title = 'Comparação entre o Número de Ocorrências e a Porcentagem de Lentidão',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Porcentagem de Lentidão',)
	st.plotly_chart(fig)
	st.plotly_chart(fig2)

	st.subheader('Conclusão:')


if select == 'Semaphore off':
	
	# Grafico de barras
	fig = px.histogram(df, x='Semaphore off', barmode='group')
	fig.update_layout(title = 'Análise de Variabilidade do Acidente',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Quantidade de Ocorrências',
        template = template)


	# Grafico de Dispersão
	fig2 = px.scatter(df, x="Semaphore off", y="Slowness in traffic (%)") 
	fig2.update_layout(title = 'Comparação entre o Número de Ocorrências e a Porcentagem de Lentidão',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Porcentagem de Lentidão',)
	st.plotly_chart(fig)
	st.plotly_chart(fig2)

	st.subheader('Conclusão:')


if select == 'Intermittent Semaphore':
	
	# Grafico de barras
	fig = px.histogram(df, x='Intermittent Semaphore', barmode='group')
	fig.update_layout(title = 'Análise de Variabilidade do Acidente',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Quantidade de Ocorrências',
        template = template)


	# Grafico de Dispersão
	fig2 = px.scatter(df, x="Intermittent Semaphore", y="Slowness in traffic (%)") 
	fig2.update_layout(title = 'Comparação entre o Número de Ocorrências e a Porcentagem de Lentidão',
		xaxis_title = 'Número de Ocorrências',
        yaxis_title = 'Porcentagem de Lentidão',)
	st.plotly_chart(fig)
	st.plotly_chart(fig2)

	st.subheader('Conclusão:')


if select == 'HoraDoDia':

	# Grafico de Barras
	fig = px.bar(df, x='HoraDoDia', color = 'Class')
	fig.update_layout(title = 'Quantidade de Registros e o Periodo do dia',
		xaxis_title = 'Periodo do Dia',
        yaxis_title = 'Quantidade de Registros',
        template = template)

	st.plotly_chart(fig)
	st.write('Como é observado acima, a maior parte dos dados são registros durante o período da manhã e há uma boa diferença entre a quantidade do período matutino e diurno, mas isso se deve pois esse conjunto de dados cobre a maior parte do período da manhã enquanto no período diurno só tem registros até às 20h e a cidade de São Paulo normalmente tem mais movimentação após esse horário')


if select == 'Class':

	# Grafico de Barras
	fig = px.bar(df, x='Class', color = 'HoraDoDia')
	fig.update_layout(title = 'Quantidade de Registros e o Periodo do dia',
		xaxis_title = 'Nível de Transito',
        yaxis_title = 'Quantidade de Registros',
        template = template)

	st.plotly_chart(fig)
	st.write('E acima nos é informado que em sua maioria, o nível de transito esta de Baixo para Médio, com poucos horários tendo o transito Alto')





st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('Copyright © 2022 de Pablo')
st.write('Versão 1.0')