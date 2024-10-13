import os,sys
import pandas as pd
import numpy as np
import pickle

import dask.dataframe as dd

from Logger import logging
from Custom_Exception import Custom_Exception
from abc import ABC,abstractmethod

import nltk
from nltk.stem.porter import PorterStemmer

from sklearn.feature_extraction.text import CountVectorizer

#global variable

root_directory_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_data_path=os.path.join(root_directory_path,"Data","processed","after_missing_values_data.pkl")
transformed_data_path=os.path.join(root_directory_path,"Data","processed","transformed_data_path.pkl")
vectors_data_path=os.path.join(root_directory_path,"Data","processed","vectors_data_path.pkl")

#load the data
if os.path.exists(input_data_path):
    with open(input_data_path ,"rb") as file:
        df =pickle.load(file)
else:
    raise Custom_Exception(FileNotFoundError,sys)


# This is the base class of Abstract class 
#------------------------------------------------------
# This class react as interface for the others strategies.
# The subclasses must have the abstract methods.

class Data_Transformation_Strategies(ABC):
    @abstractmethod
    def initiate_transformation(self,feature_name :str ):
        """
        Perform the feature engineering step to manipulate the data for model training.

        Parameters:
        df (pd.DataFrame) -> The dataset contains the data.
        feature_name -> One of the feature name in the dataset.

        Return : DataFrame that might have in well format structure for training model.
        
        """
        pass

    def get_main_names(self,obj):
        #spliting the cell data with comma 
        name_list=obj.split(",")[:3]
        return name_list
            
    
    def join_name(self,obj):
        l=[]
        #replace the " " with ""
        if " " in obj:
            obj=obj.replace(" ","")
            l.append(obj)
        else:
            l.append(obj)
        return l
    
    def remove_space(self,obj):
        l=[]
        for a in obj:
            if " " in a:
                name=a.replace(" ","")
                l.append(name)
            else:
                l.append(a)
        return l
    
    def convert_list_to_string(self,obj):
        obj=" ".join(obj)

        return obj


#Concrete class of Abstract class Data_Transformation_Strategies
#----------------------------------------------------------------
# This strategy must have a method name : initiate_transformation()
# This method helps to transform the data.

class Basic_Transformation_strategy(Data_Transformation_Strategies):
    def initiate_transformation(self,feature_name:str):
        #change the original language entries in the list 
        if feature_name=="original_language" or feature_name=="spoken_languages" or feature_name=="status" or feature_name=="original_title":
            print(f"the feature name is {feature_name}")
            df[feature_name]=df[feature_name].apply(lambda x: [x])
            #df[feature_name]=df[feature_name].astype("category")

        elif (feature_name =="overview" or feature_name =="tagline"):
            print(f"the feature name is {feature_name}")

            df[feature_name]=df[feature_name].apply(lambda x : x.split())

    
        elif (feature_name == "cast") or (feature_name =="director") or (feature_name =="writers") or (feature_name == "producers"):
            print(f"the feature name is {feature_name}")
            df[feature_name]=df[feature_name].apply(self.get_main_names)


            if (feature_name =="cast" or feature_name =="director" or feature_name =="writers" or feature_name =="producers"):
                print(f"the feature name is {feature_name}")
                df[feature_name]=df[feature_name].apply(self.remove_space)
        

        elif (feature_name=="production_companies" or feature_name=="genres" ):
            print(f"the feature name is {feature_name}")
            df[feature_name]=df[feature_name].apply(self.join_name)


        

        else:
            print(f"this column does not require or need these operations : {feature_name}")


        return df
    

    
class Tag_column_Strategy(Data_Transformation_Strategies):

    def initiate_transformation(self,feature_name : str):
        try:
            logging.info("tag columns is initialized")
            #make the tag feature

            df["tag"]=df["status"]+df["overview"]+df["tagline"]+df["original_language"]+df["original_title"]+df["genres"]+df["production_companies"]+df["spoken_languages"]+df["cast"]+df["director"]+df["writers"]+df["producers"]

            #delete the unecessary columns at the view of project
            df.drop(["status","overview","tagline","original_language","original_title","genres","production_companies","spoken_languages","cast","director","writers","producers"],axis=1,inplace=True)



            #convert the tag feature entries list -> string
            df["tag"]=df["tag"].apply(self.convert_list_to_string)
            df["tag"]=df["tag"].apply(lambda x : x.lower())
            print(df)


            with open(transformed_data_path,"wb") as file_ref:
                pickle.dump(df,file_ref)
            
            return df
        

        except Exception as e:
            raise Custom_Exception(e,sys)
        

#Concrete class of Data_Transformation_Strategies
#---------------------------------------------------------------------------------------------
#This strategy used to convert the text data to vectorization as nlp(natural language process)
#this strategy must impelement the initiate_transformation (abstract method of base class)
class Text_to_vectorization_Strategy(Data_Transformation_Strategies):

    # initializg the CounterVectorizer class with  cv object

    cv=CountVectorizer(max_features=5000,stop_words="english")
    def stemming_words(self,text):
        ps = PorterStemmer()
        words = [ps.stem(i) for i in text.split()]
        return " ".join(words)
    

    def process_partition(self,df):
        vectors=self.cv.fit_transform(df["tag"]).toarray()
        return vectors


    def initiate_transformation(self, feature_name:str):
        try:
            if feature_name=="tag":
                chunk_size=50000
                
                df[feature_name]=df[feature_name].apply(self.stemming_words)
                with open(vectors_data_path,"ab") as file_ref:
                    num_chunks=len(df) //chunk_size +1
                    for i in range(num_chunks):
                        #get chunk
                        chunk=df[i*chunk_size :(i+1)*chunk_size]
                        #the text column 
                        text_data=chunk["tag"].values
                        #vectorize the text data 
                        vectors=self.cv.fit_transform(text_data).toarray()
                        # save this chunk (vector) in pickle file
                        pickle.dump(vectors,file_ref)

            return vectors
        
        except Exception as e:
            raise Custom_Exception(e,sys)

# Context class to change the strategy of Data_Transformation_Strategies
#---------------------------------------------------------------------------------------------

class Data_Transformation:
    def __init__(self,strategy :Data_Transformation_Strategies):
        self._strategy=strategy

    def set_strategy(self,strategy:Data_Transformation_Strategies):

        self._strategy=strategy

    def execute_process(self,feature_name:str):
        

        df=self._strategy.initiate_transformation(feature_name)

        return df
