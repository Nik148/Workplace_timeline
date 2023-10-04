import plotly.express as px


def create_pie(df):
    pie = px.pie(df, values="duration_min", names="reason", color="color")
    return pie
