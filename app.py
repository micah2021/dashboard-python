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


	
for seconds in range(200):
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
if filter_sex == 'Both':
    pass
else:
    df = df.query('sex == @filter_sex')

counts = df['Gender'].value_counts()




