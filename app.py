import streamlit as st
import pandas as pd 

default_range =20

#sidebars
# st.sidebar.header('Info')
# st.sidebar.text('subsection')

#test/title
st.title("Climb Recommender")

#header
st.header('Input the reference climb using Mountain Project ID')
st.subheader('You can include search area(using zip or city & state) and radius range in miles, \n https://www.mountainproject.com/area/classics <- link to climbs')

#ask user for input
climb_id = st.text_input('Enter target climb ID (or mountain project url for target climb):')

zip_code = st.text_input('Enter zip code to search for similar climbs in that area:', '92008')
st.info('Or search by city and state')
city = st.text_input('Enter city to search in that area:', '')
state = st.text_input('Enter state to search in that area:', '')

st.text('Lastly, enter the search radius (defaults to 20 miles)')
radius_range = st.number_input('Enter radius to search in specified area:', default_range)


#once button pressed we check for input errors and start search
test = st.button('Search for recommended climbs')
# pd.set_option('max_colwidth', 100)
