import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from abc import ABC,abstractmethod

# Abstract Class for the Bivariate Analysis Strategy
#---------------------------------------------------
#This class defines a comman interface for Bivariate Analysis Strategy
# Subclass must have or implement analze method.

class BivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self,df:pd.DataFrame,feature_name1:str,feature_name2:str):
        """
        Perform Bivariate Analysis on top of two feature/Column of dataset.

        Paramters:
        df (pd.DataFrame) -> df where contains data
        feature_name1 -> first feature name will be treated as x_axis,
        feature_name2 -> second feature name will be treated as y_axis.

        Returns:
        None -> This method visualize the relationship between two features
        """
        pass

#Concrete class of BivariateAnalysisStrategy
#--------------------------------------------
#This class defines the relationship between numerical or numerical type feature

class Numerical_Vs_Numerical_Analysis(BivariateAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, feature_name1: str, feature_name2: str):
        """
        Display a Scatter plot on top of two Columns (numerical,numerical type)

        Parameters:
        df (pd.DataFrame) -> this contain the data
        feature_name1 -> Treated as X-axis might be numerical type(int,float)
        feature_name2 -> Treated as Y-axis might be a numerical type(int float)

        Returns:
        None -> This method visualize the relationship between two features(numerical type)
        """
        plt.figure(figsize=(12,8))
        """sns.scatterplot(data=df,x=feature_name1,y=feature_name2)
        plt.title(f"Relationship between {feature_name1} and {feature_name2}")
        plt.xlabel(feature_name1)
        plt.ylabel(feature_name2)
        plt.legend()
        plt.show()"""
        #instread of using the scatterplot we use pair plot for all
        filter_data=df.sample(frac=0.04,random_state=42)
        sns.pairplot(filter_data)
        plt.legend()
        plt.show()
        print("="* 40)

# Concrete class of Bivariate Analysis Strategy
# ---------------------------------------------
# This class defines or Visualize the relationship b/w Numerical and Categorical type features

class Categorical_Vs_Numerical_Analysis(BivariateAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, feature_name1: str, feature_name2: str):
        """
        Display a Barplot on top of two categorical and numerical type features to get average

        Parameters:
        df (pd.DataFrame) -> this contains data
        feature_name1 -> Treated as x-axis , should be a Categorical type.
        freature_name2 -> Treated as y-axis, should be a Numerical type.

        Returns:
        None : Visualize the Relationship and getting the average 
        """
        #top categories in the categorical feature
        top_n=10
        top_categories=df[feature_name1].value_counts().head(top_n).index
        filtered_df=df[df[feature_name1].isin(top_categories)]
        #create a bar plot
        plt.figure(figsize=(12,8))
        sns.barplot(data=filtered_df,x=feature_name1,y=feature_name2)
        plt.xlabel(feature_name1)
        plt.ylabel(feature_name2)
        #rotate the x label for better readability
        plt.xticks(rotation=45)
        plt.show()
        print("\n")
        plt.figure(figsize=(12,6))
        sns.boxenplot(data=filtered_df,x=feature_name1,y=feature_name2)
        plt.xticks(rotation=45)
        plt.xlabel(feature_name1)
        plt.ylabel(feature_name2)
        plt.legend()
        plt.show()
        print("="* 40)


# Concrete Class of Bivariate Analysis Strategy
#----------------------------------------------
# This class defines and Visualize the relationship between two features(Categorical and categorical type)

class Categorical_Vs_Categorical_Analysis(BivariateAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, feature_name1: str, feature_name2: str):
        """
        Display the Heatmap and Clustermap between two features of the dataset
        
        Paramters:
        df (pd.DataFrame) -> The dataset contains the data in rows and features
        feature_name1 -> The categorical feature  of the dataset
        feature_name2 -> Another categorical feature of the dataset

        Returns:
        None -> Plot the Heatmap and Clustermap , Helps to find corelation between them
        """
        top_n=5
        top_categories_feature1=df[feature_name1].value_counts().head(top_n).index
        top_categories_feature2=df[feature_name2].value_counts().head(top_n).index
        
        # Filter the DataFrame based on the top categories for both features
        filter_df = df[(df[feature_name1].isin(top_categories_feature1)) & (df[feature_name2].isin(top_categories_feature2))]

        filtered_df=filter_df.sample(frac=0.1,random_state=42)

        #plot the graph
        plt.figure(figsize=(12,8))
        sns.heatmap(pd.crosstab(filtered_df[feature_name1],filtered_df[feature_name2]),annot=True,fmt=".2%",cmap="Blues",cbar=True)
        plt.xticks(rotation=45)
        plt.xlabel(feature_name1)
        plt.ylabel(feature_name2)
        plt.legend()
        plt.show()

        print("\n")
        print("tells the closeness between values")
        sns.clustermap(pd.crosstab(filter_df[feature_name1],filter_df[feature_name2]))

#Context class of BivariateAnalysisStrategy
#-------------------------------------------
# This class display a interface of abstract class to switches the strategy/subclasses



class Bivariate_Analysis:
    def __init__(self,strategy:BivariateAnalysisStrategy):

        self._strategy=strategy

    def set_strategy(self,strategy:BivariateAnalysisStrategy):
        self._strategy=strategy

    def execute_strategy(self,df :pd.DataFrame,feature_name1:str,feature_name2:str):
        self._strategy.analyze(df,feature_name1,feature_name2)

