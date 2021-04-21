import streamlit as st
import pandas as pd
import numpy as np
import models_app

    
df = pd.read_csv('https://raw.githubusercontent.com/susanqisun/test/main/movie_list_final.csv')

movie_title = st.selectbox(
    'Please scroll down to see the list of movies and Select a movie you like to get recommendations.',
     df['title'])

test = st.button('Search for recommended movies')





