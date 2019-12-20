import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data', 'census_bureau_international')


QUERY = """
        SELECT `year`, `infant_mortality`, `country_name`, `life_expectancy`
        FROM `bigquery-public-data.census_bureau_international.mortality_life_expectancy`
        LIMIT 10000
        """

df = bq_assistant.query_to_pandas(QUERY)

Infant_mortality = df[df.infant_mortality >= 150]

trace1 = go.Bar(
                x=Infant_mortality.year,
                y=Infant_mortality.infant_mortality,
                name="Infant_mortality",
                marker=dict(color = 'rgba(255, 174, 255, 0.5)',
                             line=dict(color='rgb(0,0,0)',width=1.5)),
                text=Infant_mortality.country_name
                )


Armenia = df[df.country_name == 'Armenia']

trace2 = go.Scatter(
                    x=Armenia.year,
                    y=Armenia.life_expectancy,
                    mode="lines",
                    name="Life expectancy",
                    marker=dict(color = 'rgba(16, 112, 2, 0.8)'),
                    text=Armenia.country_name)


data = [trace1]

layout = dict(
              title='',
              xaxis= dict(title= ''),
              yaxis=dict(title=''),
             )
fig = dict(data = [trace1], layout = layout)
plot(fig)

layout = dict(
              title='',
              xaxis= dict(title= ''),
              yaxis=dict(title=''),
             )
fig = go.Figure(data=[trace2], layout=layout)
plot(fig)

df1 = df[df['year'] == 1991]
labels = df1['country_name']
values = df1['infant_mortality']


trace3 = go.Figure(data=[go.Pie(labels=labels, values=values)])
plot(trace3)


