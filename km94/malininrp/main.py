import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('mortality_life_expectancy', 'census_bureau_international')


QUERY = """
         SELECT  `country_name`, `year`, `infant_mortality`, `life_expectancy`
        FROM `bigquery-public-data.census_bureau_international.mortality_life_expectancy`
        LIMIT 10
        """


df = bq_assistant.query_to_pandas(QUERY)

aruba_df = df[df['country_name'] == 'Aruba']
aruba_df.head()






trace1 = go.Bar(x = aruba_df['year'], y = aruba_df['infant_mortality'])
layout = dict(title = 'Mortality',
              xaxis= dict(title= 'year'),
              yaxis=dict(title='infant_mortality'),
             )
fig = dict(data = [trace1], layout = layout)
plot(fig)


