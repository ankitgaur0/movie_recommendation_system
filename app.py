import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

root_dir=os.path.dirname(os.path.abspath(__file__))
dataframe_input_files=os.path.join(root_dir)


st.title("Movies-Recommender System")


st.selectbox("Search moives")