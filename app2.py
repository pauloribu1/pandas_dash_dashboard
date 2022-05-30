from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.graph_objs import Figure

app = Dash(__name__)

captacao_liq_df = pd.read_excel("captacao_liq_2.xltx")






opcoes = list(captacao_liq_df['Data'].unique())

opcoes.sort()

acessores = captacao_liq_df['adv_id'].unique()

acessores.sort()

df = pd.read_excel("assessores.xltx")

fig = px.bar(captacao_liq_df, x="Data", y="Captação", color="Data", barmode="group")

fig2 = px.bar(captacao_liq_df, x="Data", y="Captação", color="Data", barmode="group")

fig3= px.bar(df, x= "Inicio", y="captacao_total", color="adv_id",title="Data de Início x Captação Total de 10 assesores (jan2020 contempla períodos de 2019)", barmode="group")







app.layout = html.Div(children=[

    html.H1(children='Relatório dos Colaboradores  Atividade 2 '),

    html.H2(children='Gráfico com a variação de captação líquida de todos os colaboradores separados por mês durante 2020'),

    html.Div(children='''

        Obs: Esse gráfico mostra a quantidade de variação da captação, não do último registro de sua captação líquida no final do mês.

    '''),

    dcc.Dropdown(acessores, value='Assessor_1', id='data_mes'),

    html.Div(id='texto'),


    dcc.Graph(

        id='grafico1',

        figure=fig






    ),
    html.Div(children='''

        GRÁFICO DE TODOS ASSESSORES X DATA X CAPTAÇÃO : UMA ANÁLISE DO AUMENTO DA CAPTAÇÃO ENTRE OS MESES DE TODOS ADV

    '''),
    dcc.Graph(

            id='grafico2',

            figure=fig2






        ),
    dcc.Graph(

            id='grafico3',

            figure=fig3






        ),

])



@app.callback(

    Output('grafico1', 'figure'),
    Input('data_mes', 'value')

)
def update_output(value):

    tabela_filtrada = captacao_liq_df.loc[captacao_liq_df['adv_id'] == value, :]

    fig = px.bar(tabela_filtrada, x="Data", y="Captação", color="Data", barmode="stack")

    return fig


if __name__ == '__main__':
   app.run_server(debug=True)
