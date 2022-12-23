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
slit.dataframe(display_fruits)

#Chapter 8
import requests as req
fruityvoice_resp1 = req.get("https://fruityvice.com/api/fruit/"+"watermelon")
#slit.text(fruityvoice_resp)
#slit.text(fruityvoice_resp.json())

fruityvoice_norm1 = pd.json_normalize(fruityvoice_resp1.json())
slit.dataframe(fruityvoice_norm1)

fruityvoice_resp2 = req.get("https://fruityvice.com/api/fruit/"+"kiwi")

fruityvoice_norm2 = pd.json_normalize(fruityvoice_resp2.json())
slit.dataframe(fruityvoice_norm2)

slit.header("::FruityVice - Selector::")
fruit_choice = slit.text_input('What fruit would you like information about?','Kiwi')
slit.write('The user entered ', fruit_choice)

fruityvoice_resp_var = req.get("https://fruityvice.com/api/fruit/"+fruit_choice)

fruityvoice_norm_var = pd.json_normalize(fruityvoice_resp_var.json())
slit.dataframe(fruityvoice_norm_var)

#testing with python module
import snowflake.connector
my_cnx = snowflake.connector.connect(**slit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
slit.text("Hello from Snowflake:")
#slit.text(my_data_row)

#my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchone()
slit.text("Fruit load list:")
slit.text(my_data_row)

slit.header("::::Fruit list contains only this::::")
slit.dataframe(my_data_row)

my_data_set = my_cur.fetchall()
slit.header("::::Fruit list contains::::")
slit.dataframe(my_data_set)
