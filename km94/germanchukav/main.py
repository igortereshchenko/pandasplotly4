import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('biqquery-public-data','census_bureau_international')


QUERY = """
        SELECT `year`,`sex_ratio_at_birth`,`total_fertility_rate`,`gross_reproduction_rate`
        FROM `bigquery-public-data.census_bureau_international.age_specific_fertility_rates`
        LIMIT 10000
        """


df = bq_assistant.query_to_pandas(QUERY)





trace1 = go.Scatter(
    x = df['year'],
    y = df['gross_reproduction_rate']

                    )
trace2 = go.Pie(
    values=df['sex_ratio_at_birth'],
    labels=df['year']

                    )


trace3 = go.Bar(
    x = df['year'],
    y = df['total_fertility_rate']
)

data = [trace1]

layout1 = dict(
              title = 'Gross reproduction',
              xaxis= dict(title= 'Year'),
              yaxis=dict(title='Gross reproduction'),
             )
layout2 = dict(
              title = 'sex ratio at birth',
              xaxis= dict(title= 'Year'),
              yaxis=dict(title='sex_ratio_at_birth'),
             )
layout3 = dict(
              title = 'total fertility rate',
              xaxis= dict(title= 'Year'),
              yaxis=dict(title='total_fertility_rate'),
             )

fig1 = dict(data = [trace1], layout = layout1)
fig2 = dict(data = [trace2], layout = layout2)
fig3 = dict(data = [trace3], layout = layout3)
plot(fig1)
plot(fig2)
plot(fig3)

