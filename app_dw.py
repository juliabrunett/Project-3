import pandas as pd
import numpy as np

#To set up similarity matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Could perform train_test_split and metrics.accuracy_score test if needed.   
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC 
from sklearn import metrics

#import csv
df = pd.read_csv("../data_cleaning/export/movie_db.csv")

#set up new dataframe
features = df[['index','title','release_date','cast','total_top_5_female_led','total_female_actors','percentage_female_cast','international','original_language','languages','genres','budget','budget_bins','popularity','tagline','keywords','production_companies','production_company_origin_country']]

#create combined_features row for similarity matrix
def combine_features(row):
    return row['cast']+" "+row['keywords']+" "+row['genres']+" "+row['tagline']+" "+row['production_companies']+" "+row['production_company_origin_country']

for feature in features:
    features = features.fillna('')
    features['combined_features'] = features.apply(combine_features, axis=1)

#create new CountVectorizer matrix
cv = CountVectorizer()
count_matrix = cv.fit_transform(features['combined_features'])

#obtain cosine similarity matrix from the count matrix
cosine_sim = cosine_similarity(count_matrix)

#get movie title from movie index and vice-versa
def get_title_from_index(index):
    return features[features.index == index]["title"].values[0]
def get_index_from_title(title):
    return features[features.title == title]["index"].values[0]

#find similarity scores for given movie and then enmerate over it.
movie_user_likes = "Toy Story 3"
movie_index = get_index_from_title(movie_user_likes)
similar_movies = list(enumerate(cosine_sim[movie_index])) 
similar_movies

#Sort the list similar_movies accroding to similarity scores in descending order. Since the most similar movie to a given movie is itself, discard the first elements after sorting movies.
sorted_similar_movies = sorted(similar_movies, key=lambda
                              x:x[1], reverse=True)[1:]

#run a loop to print first 50 entries from sorted_similar_movies list
i=0
print("Top 50 Similar movies to "+movie_user_likes+" are:\n")
for movie in sorted_similar_movies:
    print(get_title_from_index(movie[0]))
    i=i+1
    if i>49:
        break

