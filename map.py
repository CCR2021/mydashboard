import streamlit as st
import pandas as pd
import plotly.express as px

# Sample geographical data
data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Latitude': [40.7128, 34.0522, 41.8781, 29.7604, 33.4484],
    'Longitude': [-74.0060, -118.2437, -87.6298, -95.3698, -112.0740],
    'Population (millions)': [8.4, 3.9, 2.7, 2.3, 1.7],
}

df = pd.DataFrame(data)

# Streamlit app
st.title('Sample Map Dashboard')

# Create a scatter map using Plotly Express
fig = px.scatter_geo(
    df,
    lat='Latitude',
    lon='Longitude',
    text='City',
    size='Population (millions)',
    projection='natural earth',
    title='Population Distribution in Major US Cities',
)

# Customize the map
fig.update_geos(
    resolution=110,
    showcoastlines=True,
    coastlinecolor="Black",
    showland=True,
    landcolor="LightGray",
)

# Display the map using Streamlit
st.plotly_chart(fig)

# Run the app
if __name__ == '__main__':
    st.write("To run this app, use the following command:")
    st.write("`streamlit run map_dashboard.py`")
