import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import models_app

    
components.html(
    """
    <!doctype html>
<title>Movie Recommendation </title>
<link rel=stylesheet type=text/css href="{{ url_for('static', filename='style.css') }}">
<body style="background-color:LavenderBlush;">
  <br>
  <h1 align="center">Movie Recommendation</h1>
  <h3 align="center">Content-Based Filtering based on MovieLens data </h3>
  <center><img src="https://raw.githubusercontent.com/susanqisun/DAV6300/main/recommender-system-for-movie-recommendation.jpeg" alt="movie" style="width:400px;height:300px;"></center>
    """,height=450,)

#style="background-color:powderblue;" 
#ask user for input
#climb_id = st.text_input('Enter movie ID:')

df = pd.read_csv('/Users/yangyang/Desktop/Desktop_Qi/capstone/data/movie_list_final.csv')

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
		st.dataframe(models_app.get_recommendations(title=movie_title))
		st.success('Finished')
		st.balloons()
		#RUN recommender
	else:
		st.error('Please select a movie')
		#ERROR please input a target climb


########################
st.write("#")

components.html(
    """
    <!doctype html>
<title>Movie Recommendation </title>
<link rel=stylesheet type=text/css href="{{ url_for('static', filename='style.css') }}">
<body style="background-color:AliceBlue;">
  <br>
  <hr width=100% align=left>
  <h3>There are 5 rating classes: 1, 2, 3, 4, 5 (5 being favorite, and 1 least)</h3>
  <h3>Please provide ratings for 10 different movies:</h3>
  {% block body %}
    <form name="passdata" action="." method="post">
      <fieldset>
        <legend>Rate some movies to begin!</legend>
        <p>
          <label for="shop1">Choose an movie</label>
          <select id = "shop1" name="shop1">
            {% for shop in list %}
              <option value = {{shop}}>{{movie}}</option>
            {% endfor %}
          </select>
          <br><label for="rate1">Rate it</label>
          <select id = "rate1" name="rate1">
            <option value = 1>1</option>
            <option value = 2>2</option>
            <option value = 3>3</option>
            <option value = 4>4</option>
            <option value = 5>5</option>
          </select>
          <br>
          <br>
          <label for="shop2">Choose an movie</label>
          <select id = "shop2" name="shop2">
            {% for shop in list %}
              <option value = {{shop}}>{{movie}}</option>
            {% endfor %}
          </select>
          <br><label for="rate2">Rate it</label>
          <select id = "rate2" name="rate2">
            <option value = 1>1</option>
            <option value = 2>2</option>
            <option value = 3>3</option>
            <option value = 4>4</option>
            <option value = 5>5</option>
          </select>
          <br>
          <br>
          <label for="shop3">Choose an movie</label>
          <select id = "shop3" name="shop3">
            {% for shop in list %}
              <option value = {{shop}}>{{movie}}</option>
            {% endfor %}
          </select>
          <br><label for="rate3">Rate it</label>
          <select id = "rate3" name="rate3">
            <option value = 1>1</option>
            <option value = 2>2</option>
            <option value = 3>3</option>
            <option value = 4>4</option>
            <option value = 5>5</option>
          </select>
          <br>
          <br>
          <label for="shop4">Choose an movie</label>
          <select id = "shop4" name="shop4">
            {% for shop in list %}
              <option value = {{shop}}>{{movie}}</option>
            {% endfor %}
          </select>
          <br><label for="rate4">Rate it</label>
          <select id = "rate4" name="rate4">
            <option value = 1>1</option>
            <option value = 2>2</option>
            <option value = 3>3</option>
            <option value = 4>4</option>
            <option value = 5>5</option>
          </select>
          <br>
          <br>
          <label for="shop5">Choose an movie</label>
          <select id = "shop5" name="shop5">
            {% for shop in list %}
              <option value = {{shop}}>{{movie}}</option>
            {% endfor %}
          </select>
          <br><label for="rate5">Rate it</label>
          <select id = "rate5" name="rate5">
            <option value = 1>1</option>
            <option value = 2>2</option>
            <option value = 3>3</option>
            <option value = 4>4</option>
            <option value = 5>5</option>
          </select>
          <br>
          <br>
          <label for="shop6">Choose an movie</label>
          <select id = "shop6" name="shop6">
            {% for shop in list %}
              <option value = {{shop}}>{{movie}}</option>
            {% endfor %}
          </select>
          <br><label for="rate6">Rate it</label>
          <select id = "rate6" name="rate6">
            <option value = 1>1</option>
            <option value = 2>2</option>
            <option value = 3>3</option>
            <option value = 4>4</option>
            <option value = 5>5</option>
          </select>
          <br>
          <br>
          <label for="shop7">Choose an movie</label>
          <select id = "shop7" name="shop7">
            {% for shop in list %}
              <option value = {{shop}}>{{movie}}</option>
            {% endfor %}
          </select>
          <br><label for="rate7">Rate it</label>
          <select id = "rate7" name="rate7">
            <option value = 1>1</option>
            <option value = 2>2</option>
            <option value = 3>3</option>
            <option value = 4>4</option>
            <option value = 5>5</option>
          </select>
          <br>
          <br>
          <label for="shop8">Choose an movie</label>
          <select id = "shop8" name="shop8">
            {% for shop in list %}
              <option value = {{shop}}>{{movie}}</option>
            {% endfor %}
          </select>
          <br><label for="rate8">Rate it</label>
          <select id = "rate8" name="rate8">
            <option value = 1>1</option>
            <option value = 2>2</option>
            <option value = 3>3</option>
            <option value = 4>4</option>
            <option value = 5>5</option>
          </select>
          <br>
          <br>
          <label for="shop9">Choose an movie</label>
          <select id = "shop9" name="shop9">
            {% for shop in list %}
              <option value = {{shop}}>{{movie}}</option>
            {% endfor %}
          </select>
          <br><label for="rate9">Rate it</label>
          <select id = "rate9" name="rate9">
            <option value = 1>1</option>
            <option value = 2>2</option>
            <option value = 3>3</option>
            <option value = 4>4</option>
            <option value = 5>5</option>
          </select>
          <br>
          <br>
          <label for="shop10">Choose an movie</label>
          <select id = "shop10" name="shop10">
            {% for shop in list %}
              <option value = {{shop}}>{{movie}}</option>
            {% endfor %}
          </select>
          <br><label for="rate10">Rate it</label>
          <select id = "rate10" name="rate10">
            <option value = 1>1</option>
            <option value = 2>2</option>
            <option value = 3>3</option>
            <option value = 4>4</option>
            <option value = 5>5</option>
          </select><br><br>
          <input type="submit" value="Submit">
        </p>
      </fieldset>
    </form>
    <body>
      <h3>Or you can check out the MovieLens pages of some of these movies before rating them!</h3>
      <table style="width:100%">
        <tr>
          <th>Moview Recommender System</th>
        </tr>
        {% for k, v in url_alias %}
          <tr>
            <td><a href={{k}} target="_blank">{{v}}</a></td>
          </tr>
        {% endfor %}
      </table>
    </body>
  {% endblock %}
</div>
    """,
    height=1100,
)
