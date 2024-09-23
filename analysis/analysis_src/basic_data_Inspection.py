import os,sys
import pickle
import pandas as pd

from Logger import logging
from Custom_Exception import Custom_Exception
from abc import ABC,abstractmethod

#Abstract Base class for Data Inspection Strategies
#this class defines a command interface  for data inspection strategies
# Subclasss must impelment the inspect method which is regrading the data inspection


class Data_Inspection_Strategies(ABC):
    def inspect(self,df :pd.DataFrame):
        """
        Perform a specific type of data inspection

        Parameters:
        df(pd.DataFrame): The dataframe on which inspection will performed

        Returns:
        None: this method prints the inspection result directory
        """
        pass

#Concrete class with Data_Inspection_Strategies class
#----------------------------------------------------
# This strategy print some(5 rows) data in the form of DataFrame and its shape,columns name
class ShowDataInspectionStrategy(Data_Inspection_Strategies):
    def inspect(self, df: pd.DataFrame):
        #print the dataframe and its shape
        print("\nShow dataframe")
        print(df.head())

        print("\nShape of the DataFrame")
        print(df.shape)
        print("\nColumns names")
        df.columns



#Concrete Strategy for Summary Statistics Inspection
#----------------------------------------------------
# This strategy provides the statistics summary for both numerical and categorical Features of DataFrame
class SummaryStatisticsInspectionStrategy(Data_Inspection_Strategies):
    def inspect(self, df: pd.DataFrame):
        # it will print the data statistical summary for both numerical and categorical type data

        print("\nSummary Statistics for Numerical Features")
        print(df.describe())
        print("\nSummary Statistics for Categorical Features")
        print(df.describe(include=["O"]))


#Concrete class with Data_Inspection_Strategies class
#----------------------------------------------------
#this strategy provides the info of the data 
class InformationInspectionStrategy(Data_Inspection_Strategies):
    def inspect(self, df: pd.DataFrame):
        #this will print data information (int,float,object,Feature type) and another also

        print("\n Information of the dataframe is:")
        print(df.info())  

#Concrete class with Data_Inspection_Strategies class
#----------------------------------------------------
#This strategy provides the sum duplicate data and show the duplicate data
class DuplicateInspectionStrategy(Data_Inspection_Strategies):
    def inspect(self, df: pd.DataFrame):
        # this will provides the total sum of duplicate data and duplicate data

        print("\nTotal number of duplicate rows in the DataFrame")
        n=df.duplicated().sum()
        print("total =",n)
        if n > 0:
            print("\nDuplicate data in the DataFrame")
            print(df[df.duplicated()])
        else:
            print("\nThere is no duplicate values in the Data Frame")

#Context Class that user a Data_Inspection_Strategies
#----------------------------------------------------
#This class allows you to switch between different data inspect methods
class Data_Inspector:
    def __init__(self,strategy:Data_Inspection_Strategies):
        """
        Initializes the Data_Inspector with specific inspection method of Data_Inspection_Strategies class

        Parameters:
        strategy(Data_Inspection_Strategies): The strategy to be use for switch the diferent methods

        Returns:
        None

        """
        self._strategy=strategy

    def set_strategy(self,strategy:Data_Inspection_Strategies):
        """
        Sets a new strategy for the Data_Inspector class
        """

        self._strategy=strategy

    def execute_inspection(self,df:pd.DataFrame):
        """
        Executes the  inpsection using the current strategy

        Parameters:
        df(pd.DataFrame):the data frame to be inspected

        Returns:
        None: executes the strategy's inspection method
        """
        self._strategy.inspect(df)

"""
#Expamle usages
if __name__=="__main__":
    try:
        Project_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pkl_file_path=os.path.join(Project_dir,"Data","processed","raw_data.pkl")

        with open(pkl_file_path,"rb") as file:
            df=pickle.load(file)

        #making the object of Data_Inspector class
        #initialize Data_Inspector with a strategy(ShowDataInspectionStrategy)
        inspector=Data_Inspector(ShowDataInspectionStrategy())
        #Execute the inspection
        inspector.execute_inspection(df)

        #Switch the another strategy dynamically(SummaryStatisticsInspectionStrategy)
        inspector.set_strategy(SummaryStatisticsInspectionStrategy())
        inspector.execute_inspection(df)

        #Switch the another strategy dynamically (InformationInspectionStrategy)
        inspector.set_strategy(InformationInspectionStrategy())
        inspector.execute_inspection(df)

        #Switch the another strategy dynamically (DuplicateInspectionStrategy())
        inspector.set_strategy(DuplicateInspectionStrategy())
        inspector.execute_inspection(df)


    except Exception as e:
        Custom_Exception(e,sys)

    


"""  