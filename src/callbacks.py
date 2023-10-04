from dash import Output, Input, State
from .main import app, df
from .components.timeline import create_timeline

@app.callback(
    Output('timeline', 'figure'),
    Input('filter_button', 'n_clicks'),
    State('multiselect', 'value'))
def filter_state(n_clicks, value):
    if value:
        dff = df[df["state"].isin(value)]
        return create_timeline(dff)
    
    return create_timeline(df)