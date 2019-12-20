import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data','census_bureau_international')


QUERY = """
        SELECT country_code,country_name,year,midyear_population
        FROM `bigquery-public-data.census_bureau_international.midyear_population`
        LIMIT 30
        """


df = bq_assistant.query_to_pandas(QUERY)

country_name = df[df['country_name']=="Aruba"]



trace1 = go.Scatter(
                x = country_name['year'].values,
                y = country_name['midyear_population'].values,
                mode = "lines",
                name = "Aruba"

                    )


trace2 = go.Pie(
                labels = country_name['year'],
                values = country_name['midyear_population'].values

                    )

trace3 = go.Bar(
                x = country_name['year'].values,
                y = country_name['midyear_population'].values


)

data = [trace1]

layout = dict(
              title = '',
              xaxis= dict(title= ''),
              yaxis=dict(title=''),
             )
fig = dict(data = [trace2], layout = layout)
plot(fig)
