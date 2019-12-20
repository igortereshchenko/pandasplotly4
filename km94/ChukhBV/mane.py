
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"
from google.cloud import bigquery

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot


bq_assistant = BigQueryHelper('bigquery-public-data','census_bureau_international')


QUERY = """
        SELECT country_name, sex, population_age_34, population_age_38
        FROM `bigquery-public-data.census_bureau_international.midyear_population_age_sex`
        LIMIT 500
        """


df = bq_assistant.query_to_pandas(QUERY)
print(df)




gender_df_groupby = df.groupby(['sex'])['population_age_34'].count()

trace1 = go.Scatter(
                        x=gender_df_groupby.index,
                        y=gender_df_groupby.values,
                        mode="lines",
                        name="count_of_people_by_age_34"

                    )
data = [trace1]

layout = dict(
              title = ' Count of males and females in age of 34 ',
              xaxis= dict(title= ''),
              yaxis=dict(title=''),
             )
fig = dict(data = [trace1], layout = layout)
plot(fig)

start_new_point_groupby = df.groupby(['sex'])['population_age_38'].count()
labels = start_new_point_groupby.index
values = start_new_point_groupby.values
layout = dict(
              title = 'Males and females in age of 38 ')


pie=go.Figure(data=[go.Pie(labels=labels,values=values)],layout=layout)
plot(pie)

start_point_groupby = df.groupby(['country_name'])['country_name'].count()

fig3 = {
    "data":[
        {
            "y":start_point_groupby.values,
            "x":start_point_groupby.index,
            "name":"Countries",
            "type":"bar"
        },
    ],
    "layout":{
        "title":"Countries",
    }
}
plot(fig3)
