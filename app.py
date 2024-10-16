import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the app, my apologies but I didn't recall any of this in any of the past lessons, so i found examples online to use for this specific page
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

# Visualization
st.subheader("Price Distribution for Selected Paint Color")
fig, ax = plt.subplots()
sns.boxplot(x='paint_color', y='price', data=filtered_data, ax=ax)
plt.title(f'Price Distribution for {color_option}')
st.pyplot(fig)

# Count of vehicles by paint color
paint_color_counts = data['paint_color'].value_counts()
st.subheader("Vehicle Count by Paint Color")
fig2, ax2 = plt.subplots()
sns.barplot(x=paint_color_counts.index, y=paint_color_counts.values, palette='Set2', ax=ax2)
plt.title('Distribution of Vehicles by Paint Color')
plt.xlabel('Paint Color')
plt.ylabel('Count')
plt.xticks(rotation=45)
st.pyplot(fig2)

# Conclusion
st.subheader("Conclusion")
st.write("This app allows you to explore how the paint color of vehicles relates to their prices.")
