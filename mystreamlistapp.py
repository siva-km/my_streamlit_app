import streamlit as slit
import pandas as pd

slit.title("TITLE :: My Test App ")

slit.header("Header :: My Header")
slit.text("Line 1")
slit.text("Line 2")
slit.text("Line 3")
slit.text("Few emojis :: 🥣 🥗 🐔 🥑 🍞")

fruits_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_list = fruits_list.set_index('Fruit')
slit.dataframe(fruits_list)

slit.multiselect("Pick fruits :: ", list(fruits_list.index))
slit.dataframe(fruits_list)

c_fruits_list = slit.multiselect("Pick fruits :: ", list(fruits_list.index),['Lemon','Lime'])
display_fruits = fruits_list.loc[c_fruits_list]
