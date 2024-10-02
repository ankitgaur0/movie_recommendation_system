#this file is used to make objects of the classes and passes necessary data and info that they needs 
import os,sys
import pickle

from Logger import logging
from Custom_Exception import Custom_Exception
from src.Data_Ingestion import Data_Ingestion
from src.missing_value_handler import Missing_values_handler,Fill_missing_value_Strategy,Comman_remove_null_values,Unknown_parameter_Strategy,Mode_value_Strategy




def load_pickle_file(pickle_file_path):
    with open(pickle_file_path ,"rb") as data:
        df=pickle.load(data)
        return df

try:
    Project_directory=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    zip_file_path=os.path.join(Project_directory,"Data","archive.zip")

    # Data Ingestion.
    #make the object of the Data_Ingestion class and pass the zip file path
    data_ingestion=Data_Ingestion(zip_file_path)
    logging.info("zip file path is passed to data_ingestion class")
    pkl_data_file_path=data_ingestion.initiate_data()
    logging.info("pickle data file path got for futher use")


    # Missing Value Handler 
    
    df=load_pickle_file(pkl_data_file_path)
    #extract the main features in the dataframe
    df.drop(columns=["id","vote_average","vote_count","revenue","runtime","budget","popularity","production_countries","director_of_photography","music_composer","imdb_rating","imdb_votes"],axis=1,inplace=True)
    columns=df.columns
    logging.info(f"the columns in the dataframe is {columns}")
    missing_handler=Missing_values_handler(Comman_remove_null_values())
    # select the columns for comman remove missing values
    selected_columns=["release_date","overview","tagline","production_companies","spoken_languages","genres","cast","director","writers","producers"]
    df_path=missing_handler.execute_strategy(df,selected_columns)

    #change the missing values handler strategy
    missing_handler.set_strategy(Unknown_parameter_Strategy())
    #new_data path after execute first strategy
    df=load_pickle_file(df_path)
    #select the features names for filling Unknown paramter
    selected_columns=["title","release_date","overview","tagline",'cast',"director","writers","producers"]
    df_path=missing_handler.execute_strategy(df,selected_columns)

    #change the strategy to fill the mode values
    missing_handler.set_strategy(Mode_value_Strategy())
    #load the pickle file
    df=load_pickle_file(df_path)
    df_path=missing_handler.execute_strategy(df,selected_columns)

    df=load_pickle_file(df_path)
    logging.info("missing_value handler is complete")
    logging.info(f"dataframe after missing value {df.head(2)}")





except Exception as e:
    raise Custom_Exception(e,sys)