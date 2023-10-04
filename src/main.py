from dash import html, Output, Input, State, dcc
import dash_mantine_components as dmc
from dash.exceptions import PreventUpdate
from sqlalchemy import create_engine, text, select
from sqlalchemy.orm import sessionmaker, scoped_session
import pandas as pd
from .components.main_layout import create_main_layout
from .components.timeline import create_timeline
from config import Config
from .app_conf import EncostDash
from .query import get_shift_day


engine = create_engine(Config.DB_URL)

# df = pd.read_sql(text("SELECT * FROM sources WHERE client_name='Кирпичный Завод'"), engine)
df = pd.read_sql(get_shift_day("Кирпичный Завод", "2023-05-12", 2007), engine)


app = EncostDash(name=__name__)

app.layout = create_main_layout(df)

