import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


# read csv from a github repo
df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSEIbfyVxix6r_fDNU17bQZzNONVeZYSxPEW3waEve5GmbuSUS5CHKPgVlQkyQo3TQewL9gyodvBdsh/pub?output=csv")


st.set_page_config(
    page_title = 'Lifelight Dashboard',
    page_icon = '✅',
    layout = 'wide'
)

# dashboard title

st.title("Real-Time Lifelight Dashboard")

# top-level filters 

select1 = st.sidebar.selectbox("Select the Gender", pd.unique(df['Gender']))


# creating a single-element container.
select1 = st.empty()
for seconds in range(1):
#while True: 
    
   
        # create two columns for charts 

        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### First Chart")
            fig1 = px.histogram(data_frame = df, x = 'Gender')
            st.write(fig1)
       
        with fig_col2:
            st.markdown("### Second Chart")
            fig = px.density_heatmap(data_frame=df, y = 'Porn', x = 'Ethnicity')
            st.write(fig)
            st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(1)
    #placeholder.empty() 


       

# dataframe filter 
st.sidebar.checkbox("Show Analysis by Ethnicity", True, key=1)
select = st.sidebar.selectbox('Select a Ethnicity',pd.unique(df['Ethnicity']))  

#get the state selected in the selectbox
state_data = df[df['Ethnicity'] == select]
select_status = st.sidebar.radio("Users status", ('Black', 'Caucasian', 'Mogolian','Others'))

def get_total_dataframe(df):
    total_dataframe = pd.DataFrame({
    'Ethnicity':['Black', 'Caucasian', 'Mogolian','Others'],
    'Number of Users':
    (df.iloc[0]['Porn'],
    df.iloc[0]['Neutral'], 
    df.iloc[0]['Sexy'],
    df.iloc[0]['Drawing'])})
    return total_dataframe

state_total = get_total_dataframe(state_data)



# dataframe filter 


# near real-time / live feed simulation 

