import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.express as plotexp

bq_assistant = BigQueryHelper( 'bigquery-public-data', 'census_bureau_international' )

QUERY = """
        SELECT country_name, year, infant_mortality, life_expectancy FROM `bigquery-public-data.census_bureau_international.mortality_life_expectancy`
        LIMIT 10000
        """

df = bq_assistant.query_to_pandas(QUERY)

Australia = df[ df.country_name == 'Australia']
bar = plotexp.bar( Australia, x = 'year', y = 'infant_mortality',
	labels = { 'year': 'Year', 'infant_mortality': 'Infant mortality' }, title = 'Australia' )

Year = df[ df.year == 1996 ]
scatter = plotexp.scatter( Year, x = 'infant_mortality', y = 'life_expectancy',
	labels = { 'infant_mortality': 'Infant mortality', 'life_expectancy': 'Life expectancy' },
	text = 'country_name', title = 'Infant mortality and life expectancy in 1996' )
scatter.update_traces( textposition = 'top center' )

scatter.show()