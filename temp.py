import pandas as pd
import plotly.express as px

df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

data = {'state': ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 
                  'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 
                  'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 
                  'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 
                  'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 
                  'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Andaman and Nicobar Islands', 'Chandigarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Lakshadweep', 'Delhi', 'Puducherry', 'Jammu & Kashmir','Ladakh'],
  
        'value': [266, 0, 25, 37, 25, 
                  0, 288, 50, 10, 0,
                  172, 131, 159, 317, 0, 
                  40, 0, 0, 18, 0, 
                  205, 29, 256, 138, 0, 
                  207, 10, 141, 10, 70, 
                  0, 0, 72, 10, 25, 25]}


fig = px.choropleth(
    data,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='state',
    color='value',
    color_continuous_scale='Blues'
)


fig.update_geos(fitbounds="locations", visible=False)

fig.show()

