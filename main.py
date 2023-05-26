import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px


uploaded_file = st.file_uploader("Upload Files Here:", type = ['csv'])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    df = df[df['OPEN_INT'] > 0]
    df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
    #st.dataframe(df)
    
    option = st.sidebar.selectbox('Symbol', df['SYMBOL'].unique())
    option_exp = st.sidebar.selectbox('Expiry', df['EXPIRY_DT'].unique())

    option_inst = st.sidebar.selectbox('Instrument', df['INSTRUMENT'].unique())

    filterdata = df[(df['SYMBOL'] == option) & (df['EXPIRY_DT'] == option_exp) & (df['INSTRUMENT'] == option_inst)]

    oi_chart = px.bar(
            filterdata,
            x = 'STRIKE_PR',
            y = 'OPEN_INT', barmode = 'group', color = 'OPTION_TYP',
            height = 300, width = 1000
    ) 

    st.plotly_chart(oi_chart) 
    
    coi_chart = px.bar(
            filterdata,
            x = 'STRIKE_PR',
            y = 'CHG_IN_OI', barmode = 'group', color = 'OPTION_TYP',
            height = 300, width = 1000
    ) 

    st.plotly_chart(coi_chart) 


    #st.dataframe(filterdata)