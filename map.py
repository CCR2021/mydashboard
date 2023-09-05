import streamlit as st
import pandas as pd
import plotly.express as px
14.47
# Sample geographical data
data = {
    'City': ['Kadapa', 'Badvel', 'Jammalamadugu', 'Pulivendla', 'vempalle'],
    'Latitude': [14.4734, 14.7318, 14.8519, 14.4214, 14.3665],
    'Longitude': [78.8284, 79.0581, 78.3699, 78.1983, 78.4581],
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
    title='Population Distribution in Major  Cities',
)

# Customize the map
fig.update_geos(
    resolution=1080,
    showcoastlines=True,
    coastlinecolor="Black",
    showland=True,
    landcolor="LightGreen",
)

# Display the map using Streamlit
st.plotly_chart(fig)

# Run the app
if __name__ == '__main__':
    st.write("To run this app, use the following command:")
    st.write("`streamlit run map_dashboard.py`")
