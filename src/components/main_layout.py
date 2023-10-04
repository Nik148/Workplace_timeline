from dash import html, Output, Input, State, dcc
from dash_extensions.enrich import (DashProxy,
                                    ServersideOutputTransform,
                                    MultiplexerTransform)
import dash_mantine_components as dmc
from dash.exceptions import PreventUpdate
from .timeline import create_timeline
from .pie import create_pie

CARD_STYLE = dict(withBorder=True,
                  shadow="sm",
                  radius="md",
                  style={'height': '500px'})

def create_main_layout(df):
    return html.Div([
        dmc.Paper([
            dmc.Grid([
                dmc.Col([
                    dmc.Card([
                        html.Div([
                            dmc.Text(f"Клиент: {df['client_name'][0]}", fw="700", style={"font-size": "25px"}),
                            dmc.Text(f"Сменный день: {df['shift_day'][0]}"),
                            dmc.Text(f"Точка учета: {df['endpoint_name'][0]}"),
                            dmc.Text(f"Начало периода: {df['shift_begin'][0]} {df['calendar_day'][0]}"),
                            dmc.Text(f"Конец периода: {df['shift_end'][df.index[-1]]} {df['calendar_day'][df.index[-1]]}", mb="20px")                    
                        ]),
                        dmc.MultiSelect(
                            data=df["state"].unique(),
                            id="multiselect",
                            mb="20px"
                        ),
                        dmc.Button(
                            "Фильтровать",
                            id="filter_button"
                        )
                            ],
                        **CARD_STYLE)
                ], span=6),
                dmc.Col([
                    dmc.Card([
                        dcc.Graph(id="pie", figure=create_pie(df))],
                        **CARD_STYLE)
                ], span=6),
                dmc.Col([
                    dmc.Card([
                        dcc.Graph(id="timeline", figure=create_timeline(df)),
                        # html.Div([
                        #     dcc.Markdown(),
                        #     html.Pre(id='hover-data')
                        # ])
                        ],
                        **CARD_STYLE)
                ], span=12),
            ], gutter="xl",)
        ])
    ])