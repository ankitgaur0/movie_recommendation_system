#this file is used to make objects of the classes and passes necessary data and info that they needs 
import os,sys


from Logger import logging
from Custom_Exception import Custom_Exception
from src.Data_Ingestion import Data_Ingestion


try:
    Project_directory=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    zip_file_path=os.path.join(Project_directory,"Data","archive.zip")
    #make the object of the Data_Ingestion class and pass the zip file path
    data_ingestion=Data_Ingestion(zip_file_path)
    logging.info("zip file path is passed to data_ingestion class")
    pkl_data_file_path=data_ingestion.initiate_data()
    logging.info("pickle data file path got for futher use")

    



except Exception as e:
    raise Custom_Exception(e,sys)