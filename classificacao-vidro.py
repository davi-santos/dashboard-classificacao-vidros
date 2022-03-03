from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
from dash_extensions import Lottie
import joblib


text = "industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged."

#Reading dataframe
df = pd.read_csv('./data/glass.csv')

#Config logo picture
logo_image = 'https://assets5.lottiefiles.com/packages/lf20_mkppywz7.json'
options_image = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

app = Dash(__name__, external_stylesheets=[dbc.themes.MATERIA],
            meta_tags=[{'name': 'viewport', 'content': 'width=device-width,initial-scale=1.0'}])
server = app.server
#FAVORITES: ZEPHYR VAPOR UNITED SPACELAB* SKETCHY**  PULSE MINTY LUX MATERIA***
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.Div([
                        html.H1('Classificador de Vidros',style={'text-align':'center'}),
                        Lottie(options=options_image, width="30%", height="30%", url=logo_image),
                    ],
                    className='border-0'
                )
                ]),
            ],
            className=''
            ),
             dbc.Card([
                dbc.CardHeader(
                    html.H4('Sobre a Base de Dados', className='card-title'),
                    className='bg-dark text-center text-light'
                ),

                dbc.CardBody([
                    html.H3('Classificação de vidros', className='ml-5 text-center'),
                    html.H3('214 amostras', className='ml-5 text-center'),
                    html.H3('9 atributos', className='ml-5 text-center'),

                    html.Div([
                        dbc.Button("Ver Atributos",color="secondary", id="left",className="me-1", n_clicks=0,),  
                        dbc.Button("Ver Tipos de Vidro",id="right",color="secondary",className="me-1",n_clicks=0,),
                        #dbc.Button("Ver todos os dados", color="secondary", id="both", n_clicks=0),
                        ],
                        className='d-grid gap-2 d-md-flex justify-content-md-center mb-2'
                    )],
                    className='bg-light'
                ),
                            dbc.Collapse(
                dbc.Card(
                    [
                        html.H5('Atributos:', className='font-weight-bold'),
                        dbc.Row([
                            dbc.Col([
                                html.Ul([
                html.Li('RI - Índice de Refração;'),
                            html.Li('Na - Sódio;'),
                            html.Li('Mg - Magnésio;'),
                            html.Li('Al - Alumínio;'),
                            html.Li('Si - Silício;'),
                                ]),
                            ]),
                            dbc.Col([html.Ul([
             html.Li('K - Potássio;'),
                            html.Li('Ca - Cálcio;'),
                            html.Li('Ba - Bário;'),
                            html.Li('Fe - Ferro.'),
                            ])])
                        ]),
                    ], 
                    body=True,
                    className='bg-light'
                ),
                id="left-collapse",
                is_open=False,
                className='bg-light'
            ),
            dbc.Collapse(
                dbc.Card([
                        html.H5('Tipos de Vidro:', className='font-weight-bold'),
                        html.Ul([
                            html.Li('Tipo 1 - Construção de Janela Flutuante Processado;'),
                            html.Li('Tipo 2 - Construção de Janela Não-flutuante processado;'),
                            html.Li('Tipo 3 - Janela de Veículo Flutuante Processado;'),
                            html.Li('Tipo 4 - Janela de Veículo Não-flutuante processado'),
                            html.Li('Tipo 5 - Vidros para recipientes'),
                            html.Li('Tipo 6 - Vidro de Louças;'),
                            html.Li('Tipo 7 - Vidro para Faróis'),
                        ],
                        className='ml-5 text-justify')                    
                ], body=True, className='bg-light',),
                    id="right-collapse",
                    is_open=False,
            ),                        
            dbc.Card([
                dbc.CardHeader(
                    html.H4('Links', className='card-title', style={'text-align':'center','color':'#FFFFFF'}),
                    className='bg-dark'
                ),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H5('Autor: '),
                        ], width=4),
                        dbc.Col([
                            html.A('Davi Santos', href='https://www.linkedin.com/in/davi-santos-datascientist/', target='_blank', style={'color':'green'}), 
                        ], width=4),
                    ], justify='center'),
                     dbc.Row([
                        dbc.Col([
                            html.H5('Artigo do trabalho: ')
                        ], width=4),
                        dbc.Col([
                            html.A('Medium', href='#', style={'color':'green'})
                        ], width=4)
                    ], justify='center'),
                    dbc.Row([
                        dbc.Col([
                           html.H5('Repositório: ') 
                        ], width=4),
                        dbc.Col([
                            html.A('Github', href='https://github.com/davi-santos/Glass-Classification', target='_blank', style={'color':'green'})
                        ], width=4,)
                    ], justify='center'),
                    dbc.Row([
                        dbc.Col([
                            html.H5('Fonte dos dados: ')
                        ], width=4),
                        dbc.Col([
                            html.A('Kaggle', href='https://www.kaggle.com/uciml/glass', target='_blank', style={'color':'green'})
                        ], width=4)
                    ], justify='center'),
                ], className='bg-light')
            ]),
           
            ]),
                ],
                align='top',
                xxl=5, xl=5, lg=5, md=12, sm=12, xs=12,
                className='mt-3',
            ),
            dbc.Col(
                [
                    #dbc.Card(
                    #    [
                            #dbc.CardBody(
                              #  [
                                    dbc.Card(
                                        dbc.CardHeader([
                                           html.H4('Opções Gráficas:', className=''),
                                            dbc.RadioItems(
                                                options=[
                                                    {"label": "Gráfico em Pizza", "value": 1},
                                                    {"label": "Gráfico de Barras", "value": 2},
                                                    {"label": "Mapa de Calor", "value": 3},
                                                    {"label": "Importância de Atributos do Modelo", "value": 4},
                                                ],
                                                value=1,
                                                id="graphic-option",
                                                inline=True,
                                            ),
                                        ],
                                        className='bg-dark text-light'
                                        )
                                    ),
                                    dcc.Graph(id='first-image', figure={}),
                                    dbc.Card([
                                        dbc.CardHeader([
                                            html.H4('Fazer Predições:'),
                                        ], className='bg-dark text-light'),
                                        dbc.CardBody([
                                          dbc.Row([
                                              dbc.Col([
                                                   dbc.Label("Índice de Refração", html_for="slider",),
                                                    dcc.Slider(id="RI", min=1.510, max=1.533, step=0.006, value=1.516),
                                              ], xxl=4, xl=4, lg=4, md=4, sm=6, xs=12,),
                                              dbc.Col([
                                                   dbc.Label("Sódio", html_for="slider"),
                                                    dcc.Slider(id="Na", min=10.7, max=17.4, step=1.4, value=12.1),
                                              ], xxl=4, xl=4, lg=4, md=4, sm=6, xs=12,),
                                              dbc.Col([
                                                   dbc.Label("Magnésio", html_for="slider"),
                                                    dcc.Slider(id="Mg", min=0, max=4.5, step=0.75, value=0.75),
                                              ], xxl=4, xl=4, lg=4, md=4, sm=6, xs=12,),
                                         #], className='text-center'),
                                          #dbc.Row([
                                              dbc.Col([
                                                   dbc.Label("Alumínio", html_for="slider"),
                                                    dcc.Slider(id="Al", min=0, max=4, step=0.7, value=0.7),
                                              ], xxl=4, xl=4, lg=4, md=4, sm=6, xs=12,),
                                              dbc.Col([
                                                   dbc.Label("Silício", html_for="slider"),
                                                    dcc.Slider(id="Si", min=68, max=76, step=1, value=69),
                                              ], xxl=4, xl=4, lg=4, md=4, sm=6, xs=12,),
                                              dbc.Col([
                                                   dbc.Label("Potássio", html_for="slider"),
                                                    dcc.Slider(id="K", min=0, max=6.5, step=1.25, value=1.25),
                                              ], xxl=4, xl=4, lg=4, md=4, sm=6, xs=12,),
                                          #], className='text-center'),
                                          #dbc.Row([
                                              dbc.Col([
                                                dbc.Label("Cálcio", html_for="slider"),
                                                dcc.Slider(id="Ca", min=5.4, max=16.2, step=2, value=7.4),
                                              ], xxl=4, xl=4, lg=4, md=4, sm=6, xs=12,),
                                              dbc.Col([
                                                   dbc.Label("Bário", html_for="slider"),
                                                    dcc.Slider(id="Ba", min=0, max=3.2, step=0.8, value=0.8),
                                              ], xxl=4, xl=4, lg=4, md=4, sm=6, xs=12,),
                                              dbc.Col([
                                                   dbc.Label("Ferro", html_for="slider"),
                                                    dcc.Slider(id="Fe", min=0, max=0.6, step=0.1, value=0.1),
                                              ], xxl=4, xl=4, lg=4, md=4, sm=6, xs=12,),
                                          ], className='text-center', justify='center'),
                                            dbc.Row([
                                                dbc.Col([
                                                    dbc.Button("Fazer Predição", id='result-button',color="secondary", n_clicks=0)
                                                ], xxl=4, xl=4, lg=4, md=4, sm=6, xs=6,),
                                                dbc.Col([
                                                    dbc.Card([
                                                        html.H4('Resultado: ', id='result')
                                                    ],
                                                    className='bg-dark text-light text-center font-weight-lighter',
                                                    ),
                                                ], xxl=4, xl=4, lg=4, md=4, sm=6, xs=6,),
                                            ], justify='center', align='center', className='mt-4'),
                                        ], className='')
                                    ]
                                    ),  
                             #   ]
                            #)
                    #    ]
                    #)
                ],
                className='justify-content-center mt-3',
                align='top',
                xxl=7, xl=7, lg=7, md=12, sm=12, xs=12,
                style={'color':'#000000'}
            ),
        ],
        justify='center',
    ),
],fluid=True)

@app.callback(
    Output('first-image', 'figure'),
    Input('graphic-option', 'value')
)
def image_top(option):
    
    fig = {}
    if option==1:
        fig = px.pie(df, values='Type',names='Type', title='Categorias de Vidro',)
    elif option==2:
        df_auxiliar = df['Type'].value_counts()
        fig = px.bar(df_auxiliar, y='Type', title='Quantidade de Vidro por Categoria', labels={'index':'Tipo de vidro', 'variable':'variável', 'Type':'Quantidade'})
    elif option==3:
        matrix_corr = df.drop('Type', axis=1).corr()
        matrix_corr = matrix_corr.apply(lambda x: round(x, 2))
        fig = px.imshow(matrix_corr, title='Correlação entre os atributos', aspect='auto', text_auto=True)
    elif option==4:
        dt = joblib.load('./models/DecisionTree.joblib')
        df_decisionTree = pd.DataFrame(dt.feature_importances_, index=df.columns.values[0:-1])

        fig = px.bar(df_decisionTree[0],  title='Importância dos atributos segundo o modelo', labels={'index':'Atributos', 'value':'Valor'})

    return fig

@app.callback(
    Output("left-collapse", "is_open"),
    [Input("left", "n_clicks")],
    [State("left-collapse", "is_open")],
)
def toggle_left(n_left, is_open):
    if n_left:
        return not is_open
    return is_open


@app.callback(
    Output("right-collapse", "is_open"),
    [Input("right", "n_clicks")],
    [State("right-collapse", "is_open")],
)
def toggle_left(n_right, is_open):
    if n_right:
        return not is_open
    return is_open


@app.callback(
    Output('result','children'),
    [Input('result-button', 'n_clicks')],
    [State('RI', 'value'), State('Na', 'value'),
    State('Mg', 'value'), State('Al', 'value'),
    State('Si', 'value'), State('K', 'value'), 
    State('Ca', 'value'), State('Ba', 'value'), 
    State('Fe', 'value')]
)
def result_prediction(n_clicks, RI, Na, Mg, Al, Si, K, Ca, Ba, Fe):
    load_model = joblib.load('./models/DecisionTree.joblib')
    resultado = 'Resultado: '

    if n_clicks==0:
        return resultado
    else:
        prediction = load_model.predict([[RI,Na,Mg,Al,Si,K,Ca,Ba,Fe]])[0]
        predict_proba = load_model.predict_proba([[RI,Na,Mg,Al,Si,K,Ca,Ba,Fe]])[0]
        print(predict_proba)
        resultado='Resultado: Classe '+str(prediction)
    return resultado


if __name__ == '__main__':
    app.run_server(debug=True)