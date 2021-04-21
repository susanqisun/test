import streamlit as st
import pandas as pd
import numpy as np
import models_app

    
df = pd.read_csv('https://raw.githubusercontent.com/susanqisun/test/main/movie_list_final.csv')

movie_title = st.selectbox(
    'Please scroll down to see the list of movies and Select a movie you like to get recommendations.',
     df['title'])

test = st.button('Search for recommended movies')

#run recommender
if test:
	if movie_title:
		#spinner
		#below lines show we are done
		#if len(climb_id)>10:
			#climb_id = climb_id.split('/')[-2]
		#else we have climb id lets look it up
		#st.success('Searching for similar climbs in that area')
		#call function and pass id, city, state, zip and radius
		#fxn returns df of 10 most similar climbs in search range
		st.dataframe(models_app.recommendations(title=movie_title))
		st.success('Finished')
		st.balloons()
		#RUN recommender
	else:
		st.error('Please select a movie')



