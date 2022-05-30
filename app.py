from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.graph_objs import Figure

app = Dash(__name__)

captacao_liq_df = pd.read_excel("captacao_liq_2.xltx")

activies_df = pd.read_excel("activities.xltx")

most_done_19 = pd.read_excel("most_done_2019.xltx")

most_done_20 = pd.read_excel("most_done_2020.xltx")

df_ic = pd.read_excel("2019_2020.xltx")


adv_id_unique = list(captacao_liq_df['adv_id'].unique())

opcoes = list(captacao_liq_df['Data'].unique())

opcoes.sort()

acessores = captacao_liq_df['adv_id'].unique()

acessores.sort()

df = pd.read_excel("most_done_activities.xltx")

fig = px.bar(captacao_liq_df, x="adv_id", y="Captação", color="adv_id", barmode="relative")

fig2 = px.bar(captacao_liq_df, x="adv_id", y="Captação", color="adv_id", barmode="stack")

fig3 = px.bar(df, x='type', y='total', title='Qual atividade mais feita no período: um infográfico de evolução do atendimento ',color = 'type', barmode='group')

fig4 = px.bar(df_ic, x='ano', y='quantidade', title='INTENSIDADE COMERCIAL 2019-2020',color = 'ano', barmode='group')






# INFORMAÇÕES EXTRAÍDAS

how_many_calls = activies_df['activitie_type'].value_counts()
print("Which was the most done activitie?\n")
print(how_many_calls)
print('\n')

call, r1, r2, meeting, r2x1 = list(how_many_calls)
int_comercial = (call*1 + r2x1*2 + (r2 + r1 + meeting)*3)/6
print('A intensidade comercial média da assesoria no período inteiro foi de '+ str(int_comercial))
print('\n')

how_many_calls_2019 = most_done_19['activitie_type'].value_counts()
call_1, meeting_1 = list(how_many_calls_2019)
r1_1, r2_1, r2x1_1 = 0, 0, 0
int_comercial_1 = (call_1*1 + r2x1_1*2 + (r2_1 + r1_1 + meeting_1)*3)/6
print('HOW MANY CALLS IN 2019\n')
print(how_many_calls_2019)
print('\n')
print('A INTENSIDADE COMERCIAL DO PERÍODO DE 2019 FOI :'+str(int_comercial_1)+ '\n')
how_many_calls_2020 = most_done_20['activitie_type'].value_counts()
call_2, r1_2, r2_2, meeting_2, r2x1_2 = list(how_many_calls_2020)
int_comercial_2 = (call_2*1 + r2x1_2*2 + (r2_2 + r1_2 + meeting_2)*3)/6
print('HOW MANY CALLS IN 2020\n')
print(how_many_calls_2020)
print('\n')
print('A INTENSIDADE COMERCIAL DO PERÍODO DE 2020 FOI :'+str(int_comercial_2)+ '\n')

#---------

actv_adv = activies_df['adv_id'].value_counts()
print("Which adv made the most activities?")
print(actv_adv)


app.layout = html.Div(children=[

    html.H1(children='Relatório dos Colaboradores( Atividade 1 )'),

    html.H2(children='Gráfico com a captação líquida somada de todos os colaboradores separados por mês durante 2020'),

    html.Div(children='''

        Obs: Esse gráfico mostra a quantidade de variação da captação, não do último registro de sua captação líquida no final do mês.

    '''),

    dcc.Dropdown(opcoes, value=1, id='data_mes'),

    html.Div(id='texto'),


    dcc.Graph(

        id='grafico1',

        figure=fig






    ),
    html.Div(children='''

        GRÁFICO NO ANO DE 2020

    '''),
    dcc.Graph(

            id='grafico2',

            figure=fig2






        ),
    dcc.Graph(

                id='grafico3',

                figure=fig3






            ),
dcc.Graph(

                id='grafico4',

                figure=fig4






            )

])



@app.callback(

    Output('grafico1', 'figure'),
    Input('data_mes', 'value')

)
def update_output(value):

    tabela_filtrada = captacao_liq_df.loc[captacao_liq_df['Data'] == value, :]

    fig = px.bar(tabela_filtrada, x="adv_id", y="Captação", color="adv_id", barmode="group")

    return fig


if __name__ == '__main__':
   app.run_server(debug=True)
