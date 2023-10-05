from dash import html
import dash_mantine_components as dmc


def create_info_client(df):

    return html.Div([
        dmc.Text(f"Клиент: {df['client_name'][0]}", fw="700", style={"font-size": "25px"}),
        dmc.Text(f"Сменный день: {df['shift_day'][0]}"),
        dmc.Text(f"Точка учета: {df['endpoint_name'][0]}"),
        dmc.Text(f"Начало периода: {df['shift_begin'][0]} {df['calendar_day'][0]}"),
        dmc.Text(f"Конец периода: {df['shift_end'][df.index[-1]]} {df['calendar_day'][df.index[-1]]}", mb="20px")                      
    ])