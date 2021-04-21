import pandas as pd
import numpy as np
from ast import literal_eval
import warnings; warnings.simplefilter('ignore')

# movie data
df_movie = pd.read_csv('https://raw.githubusercontent.com/susanqisun/test/main/movies_metadata.csv')

df_movie['genres'] = df_movie['genres'].fillna('[]').apply(literal_eval).apply(lambda x: [i[
    'name'] for i in x] if isinstance(x, list) else [])

# Pre-processing step for getting year from date by splliting it using '-'
df_movie['year'] = pd.to_datetime(df_movie['release_date'], errors='coerce').apply(
    lambda x: str(x).split('-')[0] if x != np.nan else np.nan)


md = df_movie.copy()

s = md.apply(lambda x: pd.Series(x['genres']),axis=1).stack().reset_index(level=1, drop=True)
s.name = 'genre'
gen_md = md.drop('genres', axis=1).join(s)

links_small = pd.read_csv('https://raw.githubusercontent.com/susanqisun/DAV6300/main/data/links_small.csv')

links_small = links_small[links_small['tmdbId'].notnull()]['tmdbId'].astype('int')

## Pre-processing step
def convert_int(x):
    try:
        return int(x)
    except:
        return np.nan
    
md['id'] = md['id'].apply(convert_int)
md[md['id'].isnull()]

md = md.drop([19730, 29503, 35587])

md['id'] = md['id'].astype('int')
smd = md[md['id'].isin(links_small)]

smd['tagline'] = smd['tagline'].fillna('')
smd['description'] = smd['overview'] + smd['tagline']
smd['description'] = smd['description'].fillna('')

#initializing tfidf vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(smd['description'])

from sklearn.metrics.pairwise import cosine_similarity

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
