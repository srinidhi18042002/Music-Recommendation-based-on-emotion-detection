from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics.pairwise import euclidean_distances
from collections import defaultdict
import pandas as pd
import numpy as np

dataset=pd.read_csv("data.csv")

features = ['valence', 'year', 'acousticness',
            'danceability', 'duration_ms', 'energy',
            'explicit','instrumentalness', 'key', 
            'liveness', 'loudness', 'mode',
            'popularity','speechiness', 'tempo']

metadata_cols = ['year', 'name',  'artists']

song_cluster_pipeline = Pipeline([('scaler', StandardScaler()), 
                                  ('kmeans', KMeans(n_clusters=8, 
                                   verbose=2))],verbose=True)
X = dataset[features]
song_cluster_pipeline.fit(X)

def input_preprocessor(song_list, dataset):
   
    song_vectors = []
    
    for song in song_list:
        try:
            song_data = dataset[(dataset['name'] == song['name']) ].iloc[0]
       
        except IndexError:
            song_data = None
            
        if song_data is None:
            print('Warning: {} does not exist in our database'.format(song['name']))
            continue
            
        song_vectors.append(song_data[features].values)  

    return np.mean(np.array(list(song_vectors)), axis=0)

def Music_Recommender(song_list, dataset, n_songs=10):

    # groupby_input_tracks = tracks_groupby(song_list)
    song_center = input_preprocessor(song_list, dataset)
    
    
    scaler = song_cluster_pipeline.steps[0][1]
    scaled_data = scaler.transform(dataset[features])
    scaled_song_center = scaler.transform(song_center.reshape(1, -1))
    
    
    ed_dist = euclidean_distances(scaled_song_center, scaled_data)

    
    index = list(np.argsort(ed_dist)[:,:n_songs][0])
    rec_output = dataset.iloc[index]
  
    
    return rec_output[metadata_cols]
