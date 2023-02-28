import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image



st.title(":red[Innomatics] Data APP :+1:")
st.header("Task for the program")
st.subheader("Feb 2023")



st.subheader("we can add code to the app")

CODE = '''print("Hello world")'''
st.code(CODE,language="python")




# BELOW CODE IS ADDING AND DISPLAYING THE DATA SET IN THE STERAMLIT

st.header('We can add data frames and read them')
st.subheader('Example')



df =pd.DataFrame(
    np.random.randn(50,20),
    columns=('col %d' % i for i in range(20)))


st.dataframe(df) #this is same as st.write(df)






# the below code is related to adding the iris data set

st.header("Iris Data Set")
st.subheader("This table contains the data related to the Iris data set")


image = Image.open(r'C:\Users\YESWANTH SAI YADLA\Desktop\DS_INTERN_23\proj_1\iris.jpg')
st.image(image, caption='iris dataset')

dff = pd.read_csv(r'C:\Users\YESWANTH SAI YADLA\Desktop\DS_INTERN_23\proj_1\iris.csv')
st.dataframe(dff)




# the below code is related to adding the titanic data set

st.header("Titanic Data Set")
st.subheader("This table contains the data related to the Titanic data set")


image = Image.open(r'C:\Users\YESWANTH SAI YADLA\Desktop\DS_INTERN_23\proj_1\titanic.jpg')
st.image(image, caption='titanic dataset')

dfff = pd.read_csv(r'C:\Users\YESWANTH SAI YADLA\Desktop\DS_INTERN_23\proj_1\titanic.csv')
st.dataframe(dfff)


st.header("we can display the data sets as shown above or we can make dashboards and show them individually")

st.header("Thanks for scrolling till the end :blush:")




