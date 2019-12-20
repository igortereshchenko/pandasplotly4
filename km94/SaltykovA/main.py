import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('census_bureau_international', 'bigquery-public-data')

QUERY = """
        SELECT  `population`, `year`, `sex`, `age`
        FROM `bigquery-public-data.census_bureau_international.midyear_population_agespecific`
        LIMIT 1000
        """
df = bq_assistant.query_to_pandas(QUERY)

year_df = df[df['sex'] == 'Male']
year_df.head()

trace1 = go.Bar(x = year_df['year'], y = year_df['population'])
layout = dict(title = 'Population',
              xaxis= dict(title= "year"),
              yaxis=dict(title='population'),
             )
fig = dict(data = [trace1], layout = layout)
plot(fig)


trace2= go.Scatter(x = year_df['age'],
                    y = year_df['population']
                    )

layout = dict(title = 'population',
              xaxis= dict(title= 'age'),
              yaxis=dict(title='population'),
             )
fig = dict(data = [trace2], layout = layout)
plot(fig)

trace3 = go.Pie(labels=year_df['year'], values=year_df['population'])

layout = dict(title = 'population',
              xaxis= dict(title= 'year'),
              yaxis=dict(title='population'),
             )
fig = dict(data = [trace3], layout = layout)
plot(fig)
