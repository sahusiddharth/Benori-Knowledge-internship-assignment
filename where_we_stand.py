import pandas as pd
import plotly.express as px

data = {'state': ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 
                  'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 
                  'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 
                  'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 
                  'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 
                  'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Andaman & Nicobar Islands', 'Chandigarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Lakshadweep', 'Delhi', 'Puducherry', 'Jammu & Kashmir','Ladakh'],
  
        'value': [60, 0, 10, 9, 18, 
                  8, 78, 62, 6, 22,
                  134, 94, 20, 265, 0, 
                  0, 0, 0, 39, 24, 
                  69, 2, 183, 82, 1, 
                  87, 24, 56, 1, 2, 
                  0, 0, 179, 3, 7, 7]}


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

