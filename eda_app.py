import streamlit as st

# Exploratory Data Analysis packages
import pandas as pd

def run_eda_app():
    st.subheader("Exploratory Data Analysis")
    df = pd.read_csv("data/diabetes_Data_upload.csv")
    st.dataframe(df)
    
    