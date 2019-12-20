import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data', 'census_bureau_international')


QUERY = """
        SELECT country_code,country_name, year, midyear_population 
         FROM `bigquery-public-data.census_bureau_international.midyear_population_5yr_age_sex`
        LIMIT 10000
        """


df = bq_assistant.query_to_pandas(QUERY)

df1 = df[df['country_name']=='Aruba']
x = df1['year']
y = df1['midyear_population']

trace1 = go.Scatter( x=x,
                     y=y,
                     mode = "lines")

fig1 = dict(data = [trace1])
plot(fig1)


df2 = df[df['year']==1981]
labels = df2['country_name']
values = df2['midyear_population']
trace2 = go.Pie(labels = labels, values = values)
fig = go.Figure(trace2)
plot(fig)

df3 = df[df['country_name']=='Aruba']

trace3 = go.Bar(x = df3['year'], y = df3['midyear_population'])
fig = go.Figure(data = [trace3])
plot(fig)


