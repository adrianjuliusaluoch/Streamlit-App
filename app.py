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

left, middle, right = st.columns(3)
if left.button("Download button", use_container_width=True):
    left.markdown("You clicked the plain button.")
    @st.cache_data
    def get_data():
        df = pd.DataFrame(
            np.random.randn(50, 20), columns=("col %d" % i for i in range(20))
        )
        return df

    @st.cache_data
    def convert_for_download(df):
        return df.to_csv().encode("utf-8")

    df = get_data()
    csv = convert_for_download(df)

    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="data.csv",
        mime="text/csv",
        icon=":material/download:",
    )

    with open("flower.png", "rb") as file:
        st.download_button(
            label="Download image",
            data=file,
            file_name="flower.png",
            mime="image/png",
        )

if middle.button("Emoji button", icon="😃", use_container_width=True):
    middle.markdown("You clicked the emoji button.")


if right.button("Material button", icon=":material/mood:", use_container_width=True):
    right.markdown("You clicked the Material button.")

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