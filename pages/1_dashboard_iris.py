import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px
import os




# the below code is related to adding the iris data set

st.header("Iris Data Set")
st.subheader("This table contains the data related to the Iris data set")


image = Image.open(r'C:\Users\YESWANTH SAI YADLA\Desktop\DS_INTERN_23\proj_1\iris.jpg')
st.image(image, caption='iris dataset')

dff = pd.read_csv(r'C:\Users\YESWANTH SAI YADLA\Desktop\DS_INTERN_23\proj_1\iris.csv')
st.dataframe(dff)


species = st.selectbox("Select the Species:",dff['Species'].unique())
col1,col2 = st.columns(2)

fig_1 = px.histogram(dff[dff['Species'] == species], x = "SepalLengthCm")
col1.plotly_chart(fig_1, use_container_width = True)

fig_2 = px.box(dff[dff['Species']== species], y ="SepalLenghtCm")
col2.plotly_chart(fig_2, use_container_width = True)