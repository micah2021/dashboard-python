import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 


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

job_filter = st.selectbox("Select the Gender", pd.unique(df['Gender']))


# creating a single-element container.
placeholder = st.empty()

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

if st.sidebar.checkbox("Show Analysis by Ethnicity", True, key=2):
    st.markdown("## **Ethnic level analysis**")
    st.markdown("### Overall Black,Caucasian, Mogolian and " +
    "Others %s " % (select))
    if not st.checkbox('Hide Graph', False, key=1):
        state_total_graph = px.bar(
        state_total, 
        x='Ethnicity',
        y='S/No',
        labels={'Number of Users':'Number of Users in %s' % (select)},
        color='Ethnicity')
        st.plotly_chart(state_total_graph)

# dataframe filter 


# near real-time / live feed simulation 

for seconds in range(200):
#while True: 
    
   
        # create two columns for charts 

        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### First Chart")
            fig = px.density_heatmap(data_frame=df, y = 'Porn', x = 'Ethnicity')
            st.write(fig)
        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(data_frame = df, x = 'Porn')
            st.write(fig2)
        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(1)
    #placeholder.empty() 


       
