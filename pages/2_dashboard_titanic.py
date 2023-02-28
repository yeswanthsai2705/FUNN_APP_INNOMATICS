import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px
import os



# the below code is related to adding the titanic data set

st.header("Titanic Data Set")
st.subheader("This table contains the data related to the Titanic data set")


image = Image.open(r'C:\Users\YESWANTH SAI YADLA\Desktop\DS_INTERN_23\proj_1\titanic.jpg')
st.image(image, caption='titanic dataset')

dfff = pd.read_csv(r'C:\Users\YESWANTH SAI YADLA\Desktop\DS_INTERN_23\proj_1\titanic.csv')
st.dataframe(dfff)