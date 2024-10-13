import os,sys
import pickle
import pandas as pd
import numpy as np

from Logger import logging
from Custom_Exception import Custom_Exception
from sklearn.metrics.pairwise import cosine_similarity

project_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_dataframe_path=os.path.join(project_dir,"Data","processed","transformed_data_path.pkl")
input_vectors_data_path=os.path.join(project_dir,"Data","processed","vector_data_path.pkl")

if os.path.exists(input_dataframe_path):
    with open(input_dataframe_path,"rb") as file:
        df=pickle.load(file)

    with open(input_vectors_data_path,"rb") as file:
        vectors=pickle.load(file)
else:
    raise Custom_Exception(FileNotFoundError,sys)





class Recommend_moives:
    def __init__(self) -> None:
        pass


    def similarity_movies_vector(self,vectors):
        similarity=cosine_similarity(vectors)

        return similarity


    def initiate_prediction(self,moive):
        similarity=self.similarity_movies_vector(vectors)
        movie_index=df[df["title"]== moive].index[0]

        distances=similarity[movie_index]

        movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

        return movies_list

    
    