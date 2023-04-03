import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go        
import matplotlib.pyplot as plt
import altair as alt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from PIL import Image
import os


	
for seconds in range(5):
	
	SERVICE_ACCOUNT_FILE = os.path.abspath("key.json")
	SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
	creds=None
	creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
	SPREADSHEET_ID= '1bSihbRkViZF1-pGlX8GrtneDpY_FyASOucCf6IZ14V8'
	service=build("sheets", "v4", credentials=creds)
	result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range="Sheet1!A1:L100").execute()
	# Convert the result to a Pandas DataFrame
	data = result.get('values', [])
	df= pd.DataFrame(data[1:], columns=data[0])
time.sleep(1)	

# read csv from a github repo
#df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSEIbfyVxix6r_fDNU17bQZzNONVeZYSxPEW3waEve5GmbuSUS5CHKPgVlQkyQo3TQewL9gyodvBdsh/pub?output=csv")
	
st.set_page_config(
page_title = 'Lifelight Dashboard',
page_icon = '✅',
layout = 'wide' 
			)
	
# dashboard title
st.title("Real-Time Lifelight Dashboard")
sh=df.shape
if st.button('Check Updates'):
    	st.write('# The shape of datasets ', sh)
else:
    	st.write('No update of datasets yet')
# top-level filters 

st.sidebar.checkbox("Show Analysis by Gender", True, key=1)
select = st.sidebar.selectbox(" ", df['Gender'].unique())

#get the state selected in the selectbox
state_data = df[df['Ethnicity'] == select]
select_status = st.sidebar.radio("Ethnicity", ('Caucasian','Mogolian', 'Black', 'Others'))

values = df["Gender"].value_counts()
labels = ["Female", "Male"]

# Define colors for binary data values
colors = ["blue", "orange"]
fig, ax = plt.subplots()
# Create pie chart
plt.pie(values, labels=labels, colors=colors, autopct='%1.1f%%')

# Add title to the pie chart
plt.title("Gender")
# Display the pie chart
st.pyplot(fig)

grouped_data = df.groupby("Ethnicity").size()

# Create bar chart
fig, ax = plt.subplots()
ax.bar(grouped_data.index, grouped_data.values)
ax.set_xlabel("Ethnicity")
ax.set_ylabel("S/No")
ax.set_title("Categorical Data Bar Chart")

# Display the bar chart using Streamlit
st.pyplot(fig)

chart = alt.Chart(df).mark_line().encode(
    x="Porn (%)",
    y="Ethnicity"
)

# Display the chart using Streamlit
st.altair_chart(chart, use_container_width=True)




def get_total_dataframe(df):
    total_dataframe = pd.DataFrame({
    'Ethnicity':['Caucasian', 'Mogolian', 'Black','Others'],
    'Number of cases':(df.iloc[0]['Caucasian'],
    df.iloc[0]['Mogolian'], 
    df.iloc[0]['Black'],df.iloc[0]['Others'])})
    return total_dataframe

state_total = get_total_dataframe(state_data)

if st.sidebar.checkbox("Show Analysis by State", True, key=2):
	st.markdown("## **State level analysis**")
	st.markdown("### Overall Confirmed, Active, Recovered and " +"Deceased cases in %s yet" % (select))
if not st.checkbox('Hide Graph', False, key=1):
	state_total_graph = px.bar(state_total, x='Ethnicity',y='S/No',labels={'Number of cases':'Number of cases in %s' % (select)},color='Ethnicity')
st.plotly_chart(state_total_graph)
  
