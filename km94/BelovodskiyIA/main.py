import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data', 'census_bureau_international')

QUERY = """
        SELECT  country_name, year, midyear_population_male, midyear_population_female
        FROM `bigquery-public-data.census_bureau_international.midyear_population_5yr_age_sex`
        LIMIT 10
        """
df = bq_assistant.query_to_pandas(QUERY)

aruba_df = df[df['country_name'] == 'Aruba']

trace1 = go.Bar(x = aruba_df['year'], y = aruba_df['midyear_population_male'])
layout = dict(title = 'Riding',
              xaxis= dict(title= 'year'),
              yaxis=dict(title='midyear_population_male'),
             )
fig = dict(data = [trace1], layout = layout)
plot(fig)


trace2 = go.Scatter(x = aruba_df['year'],
                    y = aruba_df['midyear_population_male']
                    )

layout = dict(title = 'Riding',
              xaxis= dict(title= 'year'),
              yaxis=dict(title='midyear_population_male'),
             )
fig = dict(data = [trace2], layout = layout)
plot(fig)


trace3 = go.Pie(labels=aruba_df['year'], values=aruba_df['midyear_population_male'])

layout = dict(title = 'Riding',
              xaxis= dict(title= 'year'),
              yaxis=dict(title='midyear_population_male'),
             )
fig = dict(data = [trace3], layout = layout)
plot(fig)
