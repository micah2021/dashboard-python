import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt

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
#for seconds in range(1):
#while True: 
    
   
        # create two columns for charts 

     
chart_visual = st.sidebar.selectbox('Select Charts/Plot type',('Line Chart', 'Bar Chart', 'Bubble Chart'))
st.sidebar.checkbox("Show Analysis by Users", True, key = 1)
selected_status = st.sidebar.selectbox('Select Users Status',options = ['Black','Caucasian', 'Mogolian','Others'])
fig = go.Figure()

if chart_visual == 'Line Chart':
	if selected_status == 'Black':
		fig.add_trace(go.Scatter(x = df.Ethnicity, y = data.Black,
								mode = 'lines',
								name = 'Black'))
	if selected_status == 'Caucasian':
		fig.add_trace(go.Scatter(x = df.Ethnicity, y = data.Caucasian,
								mode = 'lines', name = 'Caucasian'))
	if selected_status == 'Mogolian':
		fig.add_trace(go.Scatter(x = df.Ethnicity, y = data.Mogolian,
								mode = 'lines',
								name = 'Mogolian'))
	if selected_status == 'Others':   
		fig.add_trace(go.Scatter(x=df.Ethnicity, y=data.Others,
								mode='lines',
								name="Others"))

elif chart_visual == 'Bar Chart':
	if selected_status == 'Black':
		fig.add_trace(go.Bar(x=df.Ethnicity, y=df.Black,
							name='Black'))
	if selected_status == 'Caucasian':
		fig.add_trace(go.Bar(x=df.Ethnicity, y=df.Caucasian,
							name='Caucasian'))
	if selected_status == 'Mogolian':
		fig.add_trace(go.Bar(x=df.Ethnicity, y=df.Mogolian,
							name='Mogolian'))
	if selected_status == 'Others':
		fig.add_trace(go.Bar(x=df.Ethnicity, y=df.Others,
							name="Others"))

elif chart_visual == 'Bubble Chart':
	if selected_status == 'Black':
		fig.add_trace(go.Scatter(x=df.Person_Nudity,
								y=df.Black,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50],
								name='Black'))
		
	if selected_status == 'Smoked':
		fig.add_trace(go.Scatter(x=data.Person_Nudity, y=df.Caucasian,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50],
								name='Caucasian'))
		
	if selected_status == 'Mogolian':
		fig.add_trace(go.Scatter(x=df.Person_Nudity,
								y=df.Mogolian,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50],
								name = 'Mogolian'))
	if selected_status == 'Others':
		fig.add_trace(go.Scatter(x=df.Person_Nudity,
								y=df.Others,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50],
								name="Others"))

st.plotly_chart(fig, use_container_width=True)



        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(1)
    #placeholder.empty() 


       

# dataframe filter 
st.sidebar.checkbox("Show Analysis by Ethnicity", True, key=2)
select = st.sidebar.selectbox('Select a Ethnicity',pd.unique(df['Ethnicity']))  
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

