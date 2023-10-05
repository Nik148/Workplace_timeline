import plotly.express as px


def create_timeline(df):
    timeline = px.timeline(df, x_start="state_begin", 
                       x_end="state_end", 
                       y="endpoint_name", 
                       color="color",
                       title="График состояний",
                       custom_data=['state', 'reason', 'duration_min', "shift_day", "shift_name",
                                    "operator"])

    timeline.update_traces(
        showlegend=False, # Скрывает легенду цвета
        hovertemplate="<br>".join([
            "Состояние: %{customdata[0]}",
            "Причина: %{customdata[1]}",
            "Начало: %{base}", # x_start
            "Длительность: %{customdata[2]}",
            "",
            "Сменный день: %{customdata[3]}",
            "Смена: %{customdata[4]}",
            "Оператор: %{customdata[5]}",
            "<extra></extra>" # Удаляет ненужную информацию справа от hovertemplate
        ])
    )
    timeline.update_layout(
        title_x=0.5,
    )
    timeline.update_yaxes(visible=False, showticklabels=False)
    return timeline