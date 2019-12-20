import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data', 'census_bureau_international')


QUERY = """
        SELECT country_code,country_name,year,midyear_population
        FROM `bigquery-public-data.census_bureau_international.midyear_population`
        LIMIT 1000
        """


df = bq_assistant.query_to_pandas(QUERY)



serbia=df[df['country_name']=='Aruba']

trace1 = go.Scatter(
    x=serbia['year'],
    y=serbia['midyear_population']
    )


trace2 = go.Pie(
    labels=serbia['year'],
    values=serbia['midyear_population']

                    )



trace3 = go.Bar(
            x=serbia['year'],
            y=serbia['midyear_population']

)

data = [trace1]

layout = dict(
              title = 'Aruba',
              xaxis= dict(title= 'Population'),
              yaxis=dict(title='year'),
             )
fig = dict(data = [trace2], layout = layout)
plot(fig)
