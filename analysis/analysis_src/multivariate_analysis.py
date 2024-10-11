#uses the more than two features to analysis and get insights
import pandas as pd
from abc import ABC,abstractmethod


# Impelement a Abstract class of MulitvariateAnalysisStrategy
#------------------------------------------------------------
#defines a analyze method as an abstract method 
# Sub class might be impletement the analyze method

class MultivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self,df:pd.DataFrame,feature_name1 :str,feature_name2:str,feature_name_3 :str=None):
        """
        An abstract method, here does not defines but in Subclass analyze method defines and display some graph

        Parameters:
        df (pd.DataFrame): the dataset which contains the data.
        feature_name1:first feature name of dataset treated as x-axis
        feature_name2:Second feature name of dataset treated as y-axis
        feature_name3:Third feature name of dataset treated as hue parameter 

        Returns:
        None: Plot different types of graph based on feature type and number of paramters.

        """
        pass

#Conrete class of MultivariateAnalysisStrategy(Abstract class)
#--------------------------------------------------------------
# This strategy is for Numerical and Nuerical columns and third is also for Categorical columns(top category)
class Numerical