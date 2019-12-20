import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
from google.cloud import bigquery
import plotly.graph_objs as go
from plotly.offline import plot

client = bigquery.Client()
bq_assistant = BigQueryHelper('bigquery-public-data', 'census_bureau_international')

QUERY = """
        SELECT `country_name`, `year`, `rate_natural_increase`, `growth_rate` 
        FROM `bigquery-public-data.census_bureau_international.birth_death_growth_rates`
        LIMIT 10000
        """

df = bq_assistant.query_to_pandas(QUERY)


labels= df['year']
values = df['growth_rate']
fig2 = go.Figure(data=[go.Pie(labels=labels, values=values)])
plot(fig2)


trace3 = go.Bar(x = df['country_name'], y = df['growth_rate'])
layout3 = go.Layout(
    title='Швидкість росту населення',
    xaxis = dict(title='Country'),
    yaxis = dict(title='Grown Rate')
)

fig1 = go.Figure(data=[trace3], layout=layout3)
plot(fig1)
