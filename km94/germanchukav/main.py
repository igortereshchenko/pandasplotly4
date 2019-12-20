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




)

data = [trace1]

layout1 = dict(
              title = 'Gross reproduction',
              xaxis= dict(title= 'Year'),
              yaxis=dict(title='Gross reproduction'),
             )

fig1 = dict(data = [trace1], layout = layout1)

plot(fig1)

