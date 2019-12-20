import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquerty-public-data', 'census_bureau_international')

QWERY = """
SELECT country_name, year, sex, max_age FROM 'bigquerty-public-data.census_bureau_international.midyear_population_age_sex'
LIMIT 10000
"""

df = bq_assistant.query_to_pandas(QWERY)

Aruba = df[df.country_name == 'Aruba']
bar = plot.bar(Aruba, x = 'year', y = 'max_age',
               labels = {'year': 'Year', 'max_age': 'Max age'}, title = 'Aruba')
bar.show()

Year = df[df.year == 1981]
scatter = plot.scatter(Year, x = 'sex', y = 'max_age',
                       labels = {'year': 'Year', 'max_age': 'Max age'},
                       text = 'country_name', title = 'Max age in 1981')
scatter.update_traces(textposition = 'top senter')
scatter.show()