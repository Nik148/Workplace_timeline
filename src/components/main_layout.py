from dash import html, Output, Input, State, dcc
from dash_extensions.enrich import (DashProxy,
                                    ServersideOutputTransform,
                                    MultiplexerTransform)
import dash_mantine_components as dmc
from dash.exceptions import PreventUpdate
from .timeline import create_timeline
from .pie import create_pie
from .info_client import create_info_client

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
                        create_info_client(df),
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