
from IPython import get_ipython
get_ipython().magic('reset -sf')
import requests
import json
from json import loads
import pandas as pd
from pandas.io.json import json_normalize
import streamlit as st
import altair as alt



url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

querystring = {"country":"US"}

headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "2d81c24244mshffe53b231648b51p1450f7jsn88b6e0713f7e"
    }


response= requests.get(url,headers=headers, params=querystring)

response.json()

json_res= response.json()


df = json_normalize(json_res,['data','covid19Stats'])


st.title('COVID19 Data via API')
if st.checkbox('Show Data'):
    st.write(df,height=1000, length =1000)


if st.checkbox('deaths'):
     c = alt.Chart(df, width=800, height=800).mark_bar(clip=True).encode(x='province', y='deaths')
     st.altair_chart(c)

if st.checkbox('recovered'):
     c = alt.Chart(df, width=800, height=800).mark_bar(clip=True).encode(x='province', y='recovered')
     st.altair_chart(c)

if st.checkbox('confirmed'):
     c = alt.Chart(df, width=800, height=800).mark_bar(clip=True).encode(x='province', y='confirmed')
     st.altair_chart(c)
