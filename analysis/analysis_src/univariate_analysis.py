# using to anlysis and getting insights from individual features
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from abc import ABC,abstractmethod

#Abstract Base class for Unviariate Analysis Strategy
#----------------------------------------------------
#this class defines a comman interface for univariate analysis
#Subclass must implement the analyze method.


class UnivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self,df :pd.DataFrame,feature_name :str):
        """
        Perform the Univarite analysis on a specific feature of the df dataset

        Parameters:
        df(pd.DataFrame) ->The dataframe contains the data
        feature_name :str ->It is column name of the df data set that going to be analyzed

        Returns:
        None -> This method visualize the distribution of the specific features of the dataset
        """
        pass

#Concrete Strategy for Numerical Features
#-----------------------------------------
#This Strategy analyzes the Numerical features by plotting their distribution

class NumericalUnivariateAnalysis(UnivariateAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, feature_name: str):
        """
        Plots the distribution of a numerical feature using a histogram and KDE.

        Parameters:
        df (pd.DataFrame) -> This dataframe contains the data.
        feature_name (str) -> The name of the numerical feature/column in the df data set that to be analyzed.

        Returns:
        None: Display the historgrame with a KDE plot.
        """

        filter_df=df.sample(frac=0.1,random_state=42)
        plt.figure(figsize=(10,6))
        sns.distplot(data=filter_df[feature_name])
        plt.title(f"Distribution of {feature_name}")
        plt.xlabel(feature_name)
        plt.ylabel("Frequency")
        plt.show()
            
#Concrete Strategy for Categorical Features of UnivariateAnalysisStrategy Abstract class
#-------------------------------------------------------------------------------------------------
#This Strategy analyzes categorical features by plotting their frequency distribution.

class CategoricalUnivariateAnalysis(UnivariateAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, feature_name: str):
        """
        Plot the distribution of the Categorical features by using bar plot

        Parameters:
        df (pd.DataFrame) -> the dataframe contains the data (with features)
        feature_name :str -> the name of the feature or columns used in ploting and findign the pattern of distribution

        Returns:
        None -> Display a bar plot showing the frequency of each category
        """
        #top category in categories column
        top_n=5
        top_categories=df[feature_name].value_counts().head(top_n).index
        filtered_df=df[df[feature_name].isin(top_categories)]
        filtered_df=filtered_df.sample(frac=0.1,random_state=42)
        plt.figure(figsize=(10,6))
        sns.countplot(x=feature_name,data=filtered_df,palette="muted")
        plt.title(f"Distribution of {feature_name}")
        #plt.xlabel(feature_name)
        plt.ylabel("Count")
        plt.xticks(rotation=90)
        plt.show()


#Context class that uses a UnivariateAnalysisStrategy
#----------------------------------------------------
#set_strategy method is used to switch the strategy
class Univaritate_Analysis:
    def __init__(self,strategy:UnivariateAnalysisStrategy):
        """
        Initializes the Univariate_Analysis with special analyzed method of UnivariateAnalysisStrategy class

        Parameters:
        strategy ->strategy(UnivariateAnalysisStrategy) to be use for switching the different strategy.

        Retuns:
        None ->set the new strategy of the Unvivariate_Analysis class
        """

        self._strategy=strategy

    def set_strategy(self,strategy:UnivariateAnalysisStrategy):
        """
        Set the deseried strategy for the UnivariateAnalysisStrategy Class

        """
        self._strategy=strategy

    def execute_analysis(self,df:pd.DataFrame,feature_name:str):
        """
        Executes the analyze using the current strategy

        Parameters:
        df (pd.DataFrame) -> this dataframe contains the data
        freature_name -> One Feature/column name in the df dataset

        Returns:
        None -> Executes the selected strategy analyze method 
        """

        self._strategy.analyze(df,feature_name)

    