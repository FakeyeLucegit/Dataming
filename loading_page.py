import streamlit as st 
import numpy as np
import pandas as pd

# Titre de l'application
st.title('Data analyst')
df = pd.read_csv("DataAnalyst.csv")
df.drop(['Unnamed: 0'], axis=1, inplace=True)

data=pd.DataFrame(df)
st.write(data)