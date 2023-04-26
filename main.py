import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

@st.cache_resource
def load_data():
    # df = pd.read_csv('/Users/nexus/Desktop/Benori Knowledge/electric_vehicle_charging_station_list.csv')
    df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")
    return df


st.header("CHARGING STATION LOCATOR")
df = load_data()

fig = px.choropleth(
    df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='state',
    color='active cases',
    color_continuous_scale='Reds'
)
fig.update_geos(fitbounds="locations", visible=False)


st.plotly_chart(fig, use_container_width=False)

