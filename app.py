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




chart_visual = st.sidebar.selectbox('Select Charts/Plot type',
									('Line Chart', 'Bar Chart', 'Bubble Chart'))

st.sidebar.checkbox("Show Analysis by Smoking Status", True, key = 1)
selected_status = st.sidebar.selectbox('Select Smoking Status',
									options = ['Formerly_Smoked',
												'Smoked', 'Never_Smoked',
												'Unknown'])

fig = go.Figure()

if chart_visual == 'Line Chart':
	if selected_status == 'Formerly_Smoked':
		fig.add_trace(go.Scatter(x = data.Country, y = data.formerly_smoked,
								mode = 'lines',
								name = 'Formerly_Smoked'))
	if selected_status == 'Smoked':
		fig.add_trace(go.Scatter(x = data.Country, y = data.Smokes,
								mode = 'lines', name = 'Smoked'))
	if selected_status == 'Never_Smoked':
		fig.add_trace(go.Scatter(x = data.Country, y = data.Never_Smoked,
								mode = 'lines',
								name = 'Never_Smoked'))
	if selected_status == 'Unknown':
		fig.add_trace(go.Scatter(x=data.Country, y=data.Unknown,
								mode='lines',
								name="Unknown"))

elif chart_visual == 'Bar Chart':
	if selected_status == 'Formerly_Smoked':
		fig.add_trace(go.Bar(x=data.Country, y=data.formerly_smoked,
							name='Formerly_Smoked'))
	if selected_status == 'Smoked':
		fig.add_trace(go.Bar(x=data.Country, y=data.Smokes,
							name='Smoked'))
	if selected_status == 'Never_Smoked':
		fig.add_trace(go.Bar(x=data.Country, y=data.Never_Smoked,
							name='Never_Smoked'))
	if selected_status == 'Unknown':
		fig.add_trace(go.Bar(x=data.Country, y=data.Unknown,
							name="Unknown"))

elif chart_visual == 'Bubble Chart':
	if selected_status == 'Formerly_Smoked':
		fig.add_trace(go.Scatter(x=data.Country,
								y=data.formerly_smoked,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50],
								name='Formerly_Smoked'))
		
	if selected_status == 'Smoked':
		fig.add_trace(go.Scatter(x=data.Country, y=data.Smokes,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50],
								name='Smoked'))
		
	if selected_status == 'Never_Smoked':
		fig.add_trace(go.Scatter(x=data.Country,
								y=data.Never_Smoked,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50],
								name = 'Never_Smoked'))
	if selected_status == 'Unknown':
		fig.add_trace(go.Scatter(x=data.Country,
								y=data.Unknown,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50],
								name="Unknown"))

st.plotly_chart(fig, use_container_width=True)


