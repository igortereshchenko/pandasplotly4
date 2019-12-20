import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot
import plotly.express as pe

bq_assistant = BigQueryHelper("census-bureau-international","birth_death_growth_rates")


QUERY = """
        SELECT  country_code, year, crude_birth_rate, crude_death_rate FROM `bigquery-public-data.census_bureau_international.birth_death_growth_rates`
        LIMIT 10000
        """


df = bq_assistant.query_to_pandas(QUERY)


bar = pe.bar(df[df.crude_birth_rate>=30], x= "year", y="crude_birth_rate", labels = {"year": "Year","crude_birth_rate": "crude birth rate"}, title = "crude birth rate>=30")
bar.show()

scatter = pe.scatter(df[df.crude_death_rate<10], x= "year", y="crude_death_rate", labels = {"year": "Year","crude_death_rate":"Crude death rate <10"})
scatter.show()

pie = pe.pie(df[df.crude_death_rate>13],values="crude_death_rate", names = "country_code", labels= {"crude_death_rate":"crude death rate","country_code":"country code"}, title = "Country, where crude_death_rate>13")
pie.show()