from dash import html
import dash_mantine_components as dmc


def create_info_client():

    return html.Div([
        dmc.Text("Клиент: Кирпичный завод", fw="700", style={"font-size": "25px"}),
        dmc.Text("Сменный день: 2023-05-12"),
        dmc.Text("Точка учета: 2023-05-12"),
        dmc.Text("Начало периода: 08:00:00 (12.05)"),
        dmc.Text("Конец периода: 08:00:00 (05.05)", mb="20px")                    
    ])