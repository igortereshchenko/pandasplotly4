import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.express as px

bq_assistant = BigQueryHelper('bigquery-public-data', 'census_bureau_international')


QUERY = """
        SELECT country_name, year, population, age 
        FROM `bigquery-public-data.census_bureau_international.midyear_population_agespecific`
        LIMIT 10000
        """


df = bq_assistant.query_to_pandas(QUERY)

print(df)

Nauru = df[df.country_name == 'Nauru']
bar = px.bar(Nauru, x = 'year', y = 'population', labels = {'year': 'Рік', 'population': 'Популяція'}, title = 'Популяція Nauru')
bar.show()

Population = df[df.population == 19]
scatter = px.scatter(Population, y = 'country_name', x = 'year', labels = {'country_name': 'Країна', 'year': 'Рік'}, title = 'Країна|Рік, де популяція = 19')
scatter.show()

Age = df[df.age >= 90]
pie = px.pie(Age, values = 'year', names = 'country_name', labels = {'year': 'Рік', 'country_name': 'Назви'}, title = 'Країни з жителями, віком > 90 по населенню')
pie.show()
