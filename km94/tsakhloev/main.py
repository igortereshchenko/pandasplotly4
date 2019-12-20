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

bar.show()