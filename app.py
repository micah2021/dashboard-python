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


filter_sex = st.sidebar.radio('Filter By Sex', options=['Both', 'Female', 'Male'])
labels = ['Male', 'Female']
values = df['Gender'].value_counts()
is_highlighted = [True, False]
is_outlined = [False, True]
colors = {
    (True, False): 'yellow',
    (False, True): 'black',
    (True, True): 'red',
    (False, False): 'gray'
}
fig, ax = plt.subplots()

# Iterate over the data and plot each slice
for i in range(len(labels)):
    color = colors[(is_highlighted[i], is_outlined[i])]
    value = values[i]
    ax.pie([value, 100-value],
           colors=[color, 'white'],
           startangle=90, counterclock=False)

# Add a legend
handles = []
for is_highlighted, is_outlined in colors.keys():
    handles.append(plt.Rectangle((0,0), 1, 1, fc=colors[(is_highlighted, is_outlined)]))
plt.legend(handles, ['Highlighted and Outlined', 'Highlighted Only', 'Outlined Only', 'Not Highlighted or Outlined'], loc="best")

# Add a title
plt.title("My Pie Chart")

# Show the plot
plt.show()
if filter_sex == 'Both':
	pass
elif filter_sex == 'Male':
	dmale = df['Gender'].value_counts()

else:
	dfemale=df['Gender'].value_counts()



# Define the colors for each combination of binary values




