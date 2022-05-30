
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import numpy as np
 
 
st.title('Welcome to EDA web app! 👋')
st.write('This web app was created to facilitate a quick EDA of your data!')

global dataframe
dataframe = pd.DataFrame()
file  = st.file_uploader(label= 'Upload your csv file', type = ['csv'])

if file is not None:
    dataframe = pd.read_csv(file)
    st.title('Here is your file 📈')
    st.write(dataframe)
    st.title('Descriptive Statistics')
    st.write(dataframe.describe())
     # Can be used wherever a "file-like" object is accepted:
else:
    st.info('Awaiting for CSV file to be uploaded.')
#estatísticas descritivas

st.title('Kurtosis and Skewness')
col1, col2 = st.columns(2)
col1.write(pd.DataFrame(dataframe.kurt(),columns=['kurtosis']))
col2.write(pd.DataFrame(dataframe.skew(),columns=['skewness']))

st.title('Graphs 📶')
chart_select =  st.selectbox(label='graphs', 
options=['boxplot', 'violinplot', 'distribution-Skewness'])
values = dataframe.columns
chosen_columns = []
for i, value in enumerate(values):
    v= st.checkbox(label=f'{value}', key=i)
    if v==True:
        chosen_columns.append(value)

if chart_select == 'boxplot':
    try:
        d = dataframe[chosen_columns]
        fig = px.box(d)
        st.plotly_chart(fig)
    except Exception as e:
        print(e)

if chart_select == 'violinplot':
    try:
        d = dataframe[chosen_columns]
        fig = px.violin(d)
        st.plotly_chart(fig)
    except Exception as e:
        print(e)

#Correlations heatmap
st.title('Correlations heatmap')
chart_select2 =  st.selectbox(label='Select the Correlation coefficient you would like to compute', 
options=['Pearson', 'Kendall-Tau', 'Spearman'])

if chart_select2 == 'Pearson':
    try:
        df = dataframe.corr()

        fig = go.Figure()
        fig.add_trace(
        go.Heatmap(
        x = df.columns,
        y = df.index,
        z = np.array(df),
        colorscale='Viridis'
    )
)
        st.plotly_chart(fig, use_container_width=True)
    except:
        print('e')
if chart_select2 == 'Spearman':
    try:
        df = dataframe.corr('spearman')
        fig = go.Figure()
        fig.add_trace(
        go.Heatmap(
        x = df.columns,
        y = df.index,
        z = np.array(df),
        colorscale='Viridis'
    ))

        st.plotly_chart(fig, use_container_width=True)
    except:
        print('e')
if chart_select2 == 'Kendall-Tau':
    try:
        df = dataframe.corr('kendall')
        fig = go.Figure()
        fig.add_trace(
        go.Heatmap(
        x = df.columns,
        y = df.index,
        z = np.array(df),
        colorscale='Viridis'
    ))
        st.plotly_chart(fig, use_container_width=True)
    except:
        print('e')


