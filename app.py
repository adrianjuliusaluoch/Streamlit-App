import datetime
import streamlit as st
import pandas as pd
import numpy as np
from vega_datasets import data
import plotly.express as px

# Set Page Layout
st.set_page_config(page_title='Streamlit',layout='wide')

# Set Padding
st.markdown('<style>div.block-container{padding-top:2.0rem}</style>',unsafe_allow_html=True)

# Set Page Header
title = """
<style>
    .header{
        font-size : 2.5rem;
        font-family : Roboto Condensed;
    }
</style>
<b><center class='header'>Welcome to Streamlit:sunglasses:</center></b>
"""
st.markdown(title,unsafe_allow_html=True)

# Streamlit Plotly
df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

tab1, tab2, tab3 = st.tabs(["Streamlit theme (default)", "Date input", "Atair Charts"])
with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with tab2:
    d = st.date_input("When's your birthday", 
                  value='today',
                  min_value=datetime.date(1900, 1, 1),
                  max_value=datetime.date.today())
    st.write("Your birthday is:", d)

with tab3:
    source = data.unemployment_across_industries()
    st.area_chart(source, x="date", y="count", color="series", stack="center")