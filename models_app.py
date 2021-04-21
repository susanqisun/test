import pandas as pd
import numpy as np
from ast import literal_eval
import warnings; warnings.simplefilter('ignore')
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommendations (title):
    smd = pd.read_csv('https://raw.githubusercontent.com/susanqisun/test/main/movies_new.csv')
    tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
    tfidf_matrix = tf.fit_transform(smd['description'])
    
    cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)
    smd = smd.reset_index()
    indices = pd.Series(smd.index, index=smd['title'])
    
    def get_recommendations(title):
        idx = indices[title]
        sim_scores = list(enumerate(cosine_similarities[idx]))    
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:31]
        movie_indices = [i[0] for i in sim_scores]
        smd02 = smd.iloc[movie_indices][['title', 'year','overview']]
        return smd02.head(10)
    
    rec = get_recommendations(title)
    return rec
