"""
This module used for extract the main feature and fill or remove the missing values in the main features.

"""
import os,sys
import pickle
import pandas as pd
import numpy as np

from Logger import logging
from Custom_Exception import Custom_Exception

from abc import ABC, abstractmethod


#global variables:
Project_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Output_saved_path=os.path.join(Project_dir,"Data","processed","after_missing_values_data.pkl")

class Fill_missing_value_Strategy(ABC):
    # This functioin is used for remove the missing values.
    @abstractmethod
    def fill_null_values(self,df :pd.DataFrame, selected_columns):
        """
        Performs the operations in which it will remove, and fill with Unknown and mode value at the place of missing value.

        Parameters:
        df (pd.DataFrame) -> This dataset contains the data.
        selected_columns -> this is the list of selected or desired columns names.

        Returns: return the dataframe in which comman missing values have removed.
        
        """
        pass

    # Concrete class of the Fill_missing_value_Strategy class.
    #-----------------------------------------------------------
    # This strategy remove the missing values that have comman in the selected columns names.
    # This might have a functioin name fill_null_values().

class Comman_remove_null_values(Fill_missing_value_Strategy):
    def fill_null_values(self, df: pd.DataFrame, selected_columns):
        logging.info(f"comman missing values in the selected columns {df[df[selected_columns].isna().all(axis=1)]}")
        logging.info(f"total number of missing values {df[selected_columns].isna().all(axis=1).sum()}")
        # remove the comman missing values and return the dataframe
        df=df[~df[selected_columns].isna().all(axis=1)]

        return df
    
# Concrete class of the Fill_missing_value_Strategy class.
#-----------------------------------------------------------
# This strategy fill the Unknown paramter as place of missing values in the selected columns.
# This might have a functioin name fill_null_values().
class Unknown_parameter_Strategy(Fill_missing_value_Strategy):
    def fill_null_values(self, df: pd.DataFrame, selected_columns):
        for column in selected_columns:
            logging.info(f" column name {column} ,total missing value in this colums : {df[column].isnull().sum()}")
            df[column]=df[column].fillna("Unknown")

        return df

# Concrete class of the Fill_missing_value_Strategy class.
#-----------------------------------------------------------
# This strategy fill the mode values of a features in the same feature.
# This might have a functioin name remove_comman_null().
class Mode_value_Strategy(Fill_missing_value_Strategy):
    def fill_null_values(self, df: pd.DataFrame, selected_columns):
        logging.info(f"columns list that has to be fill with mode values in missing values")
        for column in selected_columns:
            mode_value=df[column].mode()[0]
            logging.info(f"the mode value {mode_value} in the column name{column}")

            df[column]=df[column].fillna(mode_value)

        return df
    


# context class that is user of the Fill_missing_value_Strategy class.
#---------------------------------------------------------------------
# This class allows you to switch between different Strategy.

class Missing_values_handler:
    def __init__(self,strategy :Fill_missing_value_Strategy):
        """
        Initialzing the Missing_values_handler class with specific mothod fill_null_values  of Fill_missing_value_Strategy class strategy.

        Parameters:
        strategy -> This variable is used to switches different strategy of the base class.

        Returns:
         -> executes the selected stratgey and save the dataframe in pickle format.
         -> return the path  after missing value data pickle file. 
        """
        self._strategy=strategy

    def set_strategy(self,strategy :Fill_missing_value_Strategy):
        #Sets the desired strategy.
        self._strategy=strategy

    def execute_strategy(self,df:pd.DataFrame , selected_columns):
        df=self._strategy.fill_null_values(df,selected_columns)

        logging.info(f"{self._strategy} is executed ")


        #save the dataframe in the form of artifacts.
        with open(Output_saved_path,"wb") as file_ref:
            pickle.dump(df,file_ref)


        return Output_saved_path
        