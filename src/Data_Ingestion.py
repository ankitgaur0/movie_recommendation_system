import os,sys
import numpy as np
import pandas as pd
import zipfile
import pickle
from Logger import logging
from Custom_Exception import Custom_Exception


from abc import ABC,abstractmethod

#global variable
Project_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pickle_path=os.path.join(Project_dir,"Data","processed","raw_data.pkl")


class Data(ABC):
    
    @abstractmethod
    def unzip_file(self):
        pass

    def initiate_data(self):
        try:
            data_path=self.unzip_file()
            logging.info(f"list of files the extracted folder {list(os.listdir(data_path))}")
            extracted_files=os.listdir(data_path)
            #check there having csv files or not
            csv_files=[f for f in extracted_files if f.endswith(".csv")]
            if len(csv_files) >1:
                print("there are more than one file \n please enter the number respect to select the csv file:")
                num=int(input("enter the number :"))
            elif len(csv_files) ==0:
                print("there is no file")
                raise Custom_Exception(FileNotFoundError,sys)
            else:
                number=0

            #read the csv file
            csv_file=os.path.join(data_path,csv_files[number])
            df=pd.read_csv(csv_file)
            logging.info(f"the csv file named {csv_files[number]} is loaded")
            #now store the data in the form of pickle so that can be used for future
            os.makedirs(os.path.dirname(pickle_path),exist_ok=True)
            with open(pickle_path,"wb") as file:
                pickle.dump(df,file)
            logging.info("Data saved to {pickle_path} for future use")

            return pickle_path
        except Exception as e:
            raise Custom_Exception(e,sys)

class Data_Ingestion(Data):
    def __init__(self,zip_file_path :str):
        self.zip_file_path=zip_file_path
    def unzip_file(self):
        try:

            #getting root diretoy
            root_dir=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
            extracted_data_path =os.path.join(root_dir,"Data/extracted_data")
            with zipfile.ZipFile(self.zip_file_path,"r") as zip_ref:
                zip_ref.extractall(extracted_data_path)
            logging.info(f"File {self.zip_file_path} successfully unzipped to {extracted_data_path}")

            return extracted_data_path
        except Exception as e:
            raise Custom_Exception(e,sys)
    

zip_file_path=os.path.join(Project_dir,"Data","archive.zip")
if __name__=="__main__":
    if os.path.exists(zip_file_path):
        data_ing=Data_Ingestion(zip_file_path)
        pickle_path=data_ing.initiate_data()

        print(pickle_path)
    else:
        print("there is no such zip file")