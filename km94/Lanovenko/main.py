import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data', 'census_bureau_international')


QUERY = """
        SELECT `year`, `midyear_population`, `midyear_population_male`, `midyear_population_female`
        FROM `bigquery-public-data.census_bureau_international.midyear_population_5yr_age_sex`
        LIMIT 1000
        """


df = bq_assistant.query_to_pandas(QUERY)

trace1 = go.Scatter(
    x=df['year'],
    y=df['midyear_population_male'],
    mode='lines',
)

trace3 = go.Bar(
    x=df['year'],
    y=df['midyear_population'],
)


layout_scatter = dict(
              title='Середня популяція чоловіків відносно року',
              xaxis=dict(title= 'Рік'),
              yaxis=dict(title='Популяція чоловіків'),
)

layout_bar = dict(
              title='Популяція населення відносно',
              xaxis=dict(title= 'Рік'),
              yaxis=dict(title='Загальна популяція'),
)

fig_scatter = dict(data=[trace1], layout=layout_scatter)
fig_bar = dict(data=[trace3], layout=layout_bar)

plot(fig_scatter)
plot(fig_bar)
