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

from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://docs.google.com/spreadsheets/d/e/2PACX-1vSEIbfyVxix6r_fDNU17bQZzNONVeZYSxPEW3waEve5GmbuSUS5CHKPgVlQkyQo3TQewL9gyodvBdsh/pub?output=csv']
SERVICE_ACCOUNT_FILE = 'path/to/service_account.json'

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)


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
sh=df.shape
st.write("# The shape of datasets ", sh)


labels = ['Female', 'Male']

sizes =df['Gender'].value_counts()
# Create the pie chart using matplotlib
fig, ax3 = plt.subplots()
ax3.pie(sizes, labels=labels, autopct='%1.1f%%')
ax3.axis('equal')

# Display the chart using Streamlit



fig1, ax1 = plt.subplots()
ax1.hist(df['Ethnicity'], bins=5)
# Label
ax1.set(title='A Histogram of Ethnicity Count',
       xlabel='Ethnicity',
       ylabel='Count')
plt.show();





subset = df.loc[df['Ethnicity']=="Others"]
fig2, ax4 = plt.subplots()

sns.distplot(subset["Porn (%)"], color='red')
ax4.set_title('Distribution of Total Others Races with Porn')

# Display the plot using Streamlit


col1, col2, col3= st.columns(3)
col1.pyplot(fig)
col2.pyplot(fig1)
col3.pyplot(fig2)




g = sns.FacetGrid(data=df, col='Ethnicity', col_wrap=2, height=5)

# Map a bar plot of the 'total_bill' column to each subplot
g.map(sns.barplot, 'Porn (%)', 'Drawing (%)')

# Set the title of each subplot
for ax in g.axes.flat:
    ax.set_title(f"Porn by Gender and Ethnicity({ax.get_title()})")

# Display the plot using Streamlit
st.pyplot(g.fig)



cross=pd.crosstab(df['Ethnicity'], df['Porn (%)'])
st.write("## The is the cross table for Ethnicity with Porn", cross)

select1 = st.sidebar.selectbox("Select the Gender", pd.unique(df['Gender']))


st.set_option('deprecation.showPyplotGlobalUse', False)
fig, ax = plt.subplots()

# Plot a histogram

# creating a single-element container.
select1 = st.empty()
#for seconds in range(1):
#while True: 
st.header("The is summary of the datasets")
desc=df.describe(include=["bool","object"])
desc1=df.describe(include="number")
desc
desc1
     
chart_visual = st.sidebar.selectbox('Select Charts/Plot type',('Line Chart', 'Bar Chart', 'Bubble Chart'))
st.sidebar.checkbox("Show Analysis by Users", True, key = 1)
selected_status = st.sidebar.selectbox('Select Users Status',options = ['Black','Caucasian', 'Mogolian','Others'])
fig5 = go.Figure()

if chart_visual == 'Line Chart':
	if selected_status == 'Black':
		fig5.add_trace(go.Scatter(x = df["Porn (%)"], y = df.Ethnicity,
								mode = 'markers',
								name = 'Black'))
	if selected_status == 'Caucasian':
		fig5.add_trace(go.Scatter(x = df["Porn (%)"], y = df.Ethnicity,
								mode = 'markers', name = 'Caucasian'))
	if selected_status == 'Mogolian':
		fig5.add_trace(go.Scatter(x = df["Porn (%)"], y = df.Ethnicity,
								mode = 'markers',
								name = 'Mogolian'))
	if selected_status == 'Others':   
		fig5.add_trace(go.Scatter(x=df["Porn (%)"], y=df.Ethnicity,
								mode='markers',
								name="Others"))


	
	
	
elif chart_visual == 'Bubble Chart':
	if selected_status == 'Black':
		fig5.add_trace(go.Scatter(x=df.Person_Nudity,
								y=df.Ethnicity,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50],
								name='Black'))
		
	if selected_status == 'Smoked':
		fig5.add_trace(go.Scatter(x=data.Person_Nudity, y=df.Ethnicity,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50],
								name='Caucasian'))
		
	if selected_status == 'Mogolian':
		fig5.add_trace(go.Scatter(x=df.Person_Nudity,
								y=df.Ethnicity,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50],
								name = 'Mogolian'))
	if selected_status == 'Others':
		fig5.add_trace(go.Scatter(x=df.Person_Nudity,
								y=df.Ethnicity,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50],
								name="Others"))

st.plotly_chart(fig5, use_container_width=True)
st.markdown("### Detailed Data View")
st.dataframe(df)
time.sleep(1)
    #placeholder.empty() 


       

# dataframe filter 




