import pandas as pd
import streamlit as st
import plotly.express as px

# Title of the app
st.title("Vehicle Price Analysis by Color")

# Load the dataset
data = pd.read_csv('vehicles_us.csv')

# Data Cleaning
data = data.drop_duplicates()
data['paint_color'] = data['paint_color'].fillna('Unknown')
data['is_4wd'] = data['is_4wd'].fillna(0)
data['model_year'] = data['model_year'].fillna(data['model_year'].median())
data['odometer'] = data['odometer'].fillna(data['odometer'].median())
data['cylinders'] = data['cylinders'].fillna(data['cylinders'].mode()[0])

# Sidebar for user input
st.sidebar.header("User Input Features")
color_option = st.sidebar.selectbox("Select Paint Color", data['paint_color'].unique())

# Filter data based on user input
filtered_data = data[data['paint_color'] == color_option]

# Visualization: Price Distribution for Selected Paint Color
st.subheader("Price Distribution for Selected Paint Color")
fig = px.box(filtered_data, x='paint_color', y='price', title=f'Price Distribution for {color_option}')
st.plotly_chart(fig)

# Count of vehicles by paint color
paint_color_counts = data['paint_color'].value_counts().reset_index()
paint_color_counts.columns = ['paint_color', 'count']

st.subheader("Vehicle Count by Paint Color")
fig2 = px.bar(paint_color_counts, x='paint_color', y='count', title='Distribution of Vehicles by Paint Color', 
               color='paint_color', color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(fig2)

# Conclusion
st.subheader("Conclusion")
st.write("This app allows you to explore how the paint color of vehicles relates to their prices.")