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
import altair as alt


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
gender = st.sidebar.selectbox(" ", df['Gender'].unique())

#get the state selected in the selectbox
state_data = df[df['Ethnicity'] == gender]
Ethnic = st.sidebar.radio("Ethnicity", ('Caucasian','Mogolian', 'Black', 'Others'))

values = df["Gender"].value_counts()
labels = ["Female", "Male"]

# Define colors for binary data values
colors = ["blue", "orange"]
fig1, ax = plt.subplots()
# Create pie chart
plt.pie(values, labels=labels, colors=colors, autopct='%1.1f%%')

# Add title to the pie chart
plt.title("Gender by Count")
# Display the pie chart

st.pyplot(fig1)
grouped_data = df.groupby("Ethnicity").size()

# Create bar chart
fig2, ax = plt.subplots() 
ax.bar(grouped_data.index, grouped_data.values)
ax.set_xlabel("Ethnicity")
ax.set_ylabel("Porn (%)")
ax.set_title("Categorical Data Bar Chart")

# Display the bar chart using Streamlit


fig3 = px.bar(df, x='Gender', y='Model')

col2, col3 = st.beta_columns(2)

with col2:
    st.plotly_chart(fig2)
with col3:
    st.plotly_chart(fig3)

def create_plot(df["Ethnicity", "Porn (%)"]):
    fig, ax = plt.subplots()
    ax = sns.histplot(["Ethnicity", "Porn (%)"])
    return fig
fig = create_plot(["Ethnicity", "Porn (%)"])

# Display your plot with Streamlit
st.pyplot(fig)

