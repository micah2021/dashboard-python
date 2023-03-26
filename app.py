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


labels = ['Female', 'Male']

sizes =df['Gender'].value_counts()

# Create the pie chart using matplotlib
fig, ax3 = plt.subplots()
ax3.pie(sizes, labels=labels, autopct='%1.1f%%')
ax3.axis('equal')

# Display the chart using Streamlit
st.pyplot(fig)



subset = df.loc[df['Ethnicity']=="Black"]
fig1, ax4 = plt.subplots()

sns.distplot(subset["Porn (%)"], color='red')
ax4.set_title('Distribution of Total Porns')

# Display the plot using Streamlit
st.pyplot(fig1)



sh=df.shape
st.write("The shape of datasets", sh)
cross=pd.crosstab(df['Ethnicity'], df['Porn (%)'])
st.write("The is the cross table for Ethnicity with Porn", cross)

select1 = st.sidebar.selectbox("Select the Gender", pd.unique(df['Gender']))







st.set_option('deprecation.showPyplotGlobalUse', False)
fig, ax = plt.subplots()

# Plot a histogram
ax.hist(df['Gender'], bins=5)
# Label
ax.set(title='A Histogram of Gender Count',
       xlabel='Gender',
       ylabel='Count')
plt.show();
st.pyplot()
fig1, ax1 = plt.subplots()
ax1.hist(df['Ethnicity'], bins=5)
# Label
ax1.set(title='A Histogram of Ethnicity Count',
       xlabel='Ethnicity',
       ylabel='Count')
plt.show();
st.pyplot()





# Create a sample data frame with a string column



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
fig = go.Figure()

if chart_visual == 'Line Chart':
	if selected_status == 'Black':
		fig.add_trace(go.Scatter(x = df.Porn, y = df.Ethnicity,
								mode = 'lines',
								name = 'Black'))
	if selected_status == 'Caucasian':
		fig.add_trace(go.Scatter(x = df.Porn, y = df.Ethnicity,
								mode = 'lines', name = 'Caucasian'))
	if selected_status == 'Mogolian':
		fig.add_trace(go.Scatter(x = df.Porn, y = df.Ethnicity,
								mode = 'lines',
								name = 'Mogolian'))
	if selected_status == 'Others':   
		fig.add_trace(go.Scatter(x=df.Porn, y=df.Ethnicity,
								mode='lines',
								name="Others"))

elif chart_visual == 'Bar Chart':
	if selected_status == 'Black':
		fig.add_trace(go.Bar(x=df.Porn, y=df.Ethnicity,
							name='Black'))
	if selected_status == 'Caucasian':
		fig.add_trace(go.Bar(x=df.Porn, y=df.Ethnicity,
							name='Caucasian'))
	if selected_status == 'Mogolian':
		fig.add_trace(go.Bar(x=df.Porn, y=df.Ethnicity,
							name='Mogolian'))
	if selected_status == 'Others':
		fig.add_trace(go.Bar(x=df.Porn, y=df.Ethnicity,
							name="Others"))

elif chart_visual == 'Bubble Chart':
	if selected_status == 'Black':
		fig.add_trace(go.Scatter(x=df.Person_Nudity,
								y=df.Ethnicity,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50],
								name='Black'))
		
	if selected_status == 'Smoked':
		fig.add_trace(go.Scatter(x=data.Person_Nudity, y=df.Ethnicity,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50],
								name='Caucasian'))
		
	if selected_status == 'Mogolian':
		fig.add_trace(go.Scatter(x=df.Person_Nudity,
								y=df.Ethnicity,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50],
								name = 'Mogolian'))
	if selected_status == 'Others':
		fig.add_trace(go.Scatter(x=df.Person_Nudity,
								y=df.Ethnicity,
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



