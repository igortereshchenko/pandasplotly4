import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('census_bureau_international', 'age_specific_fertility_rates')


QUERY = """
        SELECT *
        FROM `bigquery-public-data.census_bureau_international.age_specific_fertility_rates`
        
        """


df = bq_assistant.query_to_pandas(QUERY)

country=df['country_name']
year=df['year']
total_fertility_rate=df['total_fertility_rate']




trace1 = go.Scatter(
    y=country.values,
    x=total_fertility_rate,
    mode="lines",
    name="Total fertility rate",
 )



trace2 = go.Pie(
    labels=country,
    values=total_fertility_rate,


   )

trace3 = go.Bar(
    x=country.values,
    y=total_fertility_rate.values,
    name="Total fertilyty rate"


)

data = [trace1]

layout = dict(
              title = 'Total fertility rate',
              xaxis= dict(title= 'Contry'),
              yaxis=dict(title='Fertilyty rate'),
             )
fig = dict(data = [trace1], layout = layout)
plot(fig)


data=[trace3]
layout = dict(
              title = 'Total fertility rate',
              xaxis= dict(title= 'Contry'),
              yaxis=dict(title='Fertilyty rate'),
             )
fig = dict(data = [trace3], layout = layout)

data=[trace2]

layout = dict(
              title = 'Total fertility rate',
             )
fig = dict(data = [trace2], layout = layout)