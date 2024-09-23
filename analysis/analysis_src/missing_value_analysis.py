import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from abc import ABC,abstractmethod

class MissingValueAnalysisTemplate(ABC):
    def analyze(self,df:pd.DataFrame):
        """
        Performs a complete missing values analysis by identifying the missing values in individual Features

        Parameters:
        df(pd.DataFrame) ->this dataframe to be analyzed

        Returns:
        None: This method performs the analysis and visualize on the dataframe and print them
        """
        self.identify_missing_values(df)
        self.visualize_missing_values(df)

    @abstractmethod
    def identify_missing_values(self,df:pd.DataFrame):
        """
        Perform to identify the missing values in the dataframe.

        Parameters:
        df(pd.DataFrame)->the dataframe to be analyzed.

        Returns:
        None: This method should print the count of missing values with respect to Features of the dataframe

        """
        pass

    @abstractmethod
    def visualize_missing_values(self,df:pd.DataFrame):
        """
        Visualize the missing values in the dataframe.

        Parameters:
        df (pd.DataFrame)-> this dataframe to be visualized.

        Returns:
        None: this method should plot a graph of missing values
        """
        pass

#Concrete class for missing values indentification and visualization


class Missing_Values(MissingValueAnalysisTemplate):

    def identify_missing_values(self,df: pd.DataFrame):
        """
        Perform a operation to identify the missing values in the features

        Parameters:
        df (pd.DataFrame)-> this dataframe to be analyzed.

        Returns:
        None :Print the missing values count to console.
        """
        print("\n Missing values Count by Columns")
        missing_values=df.isnull().sum()
        print(missing_values[missing_values>0])


    def visualize_missing_values(self,df:pd.DataFrame):
        """
        Create a heat map to visualize the missing values in the dataframe

        Parameters:
        df (pd.DataFrame) -> this datframe null values to be visualized

        Returns:
        None : Displays a heatmap for missing values
        """
        print("\nVisualize the missing valies in DataFrame.....")
        plt.figure(figsize=(12,8))
        sns.heatmap(df.isnull(),cbar=False,cmap="viridis")
        plt.title("Missing values Heatmap")
        plt.show()