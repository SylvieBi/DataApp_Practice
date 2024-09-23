pip install streamlit
pip install streamlit matplotlib WordCloud seabornpython
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Add title & Read csv file
st.title('California Housing Data (1990)')
df = pd.read_csv('housing.csv')

# Create a slider for median house price
price_filter = st.slider('Minimal median Housing Price', 0, 500001, 200000)

# Create a multi-select filter for location types
location_filter = st.sidebar.multiselect(
    'Choose the location type',
    df.ocean_proximity.unique(),
    df.ocean_proximity.unique()  # defaults
)

# Create a radio button for filtering by median income level
income_level = st.sidebar.radio(
    "Select income level",
    ('Low', 'Medium', 'High')
)

# Filter by income level
if income_level == 'Low (<=2.5)':
    filtered_df = df[df['median_income'] <= 2.5]
elif income_level == 'Medium (> 2.5 & <= 4.5)':
    filtered_df = df[(df['median_income'] > 2.5) & (df['median_income'] <= 4.5)]
else:
    filtered_df = df[df['median_income'] > 4.5]

# Filter by house value and location
filtered_df = filtered_df[(filtered_df['median_house_value'] >= price_filter) &
                         (filtered_df['ocean_proximity'].isin(location_filter))]

# Display map
st.map(filtered_df[['latitude', 'longitude']])

# Optional: You can add a histogram or other plots
st.write("Histogram of Median House Value")
fig, ax = plt.subplots()
filtered_df['median_house_value'].plot(kind='hist', bins=30, ax=ax)
st.pyplot(fig)
