# MOVIE RECOMMENDATION SYSTEM & MLOPS
[Ankit Gaur](https://github.com/ankitgaur0)
[Rohit Jangra](https://github.com/rohit-jangra-dx)

<p align="center">  
    <br>
	<a href="#">
	    <img src="https://raw.githubusercontent.com/Thomas-George-T/Thomas-George-T/master/assets/python.svg" alt="Python" title="Python" width ="120" />
        <img height=100 src="https://cdn.svgporn.com/logos/tensorflow.svg" alt="Tensorflow" title="Tensorflow" hspace=20  /> 
        <img height=100 src="https://cdn.svgporn.com/logos/docker-icon.svg" alt="Docker" title="Docker" hspace=20 />
        <img height=100 src="https://github.com/user-attachments/assets/0a69c092-41e6-44b8-b3a0-92befc7c2f8c" alt="Amazon Web Servies" title="Amazon Web Servies" hspace=20  />
        <img height=100 src="https://cdn.svgporn.com/logos/flask.svg" alt="Flask" title="Flask" hspace=20 /> 
  </a>	
</p>
<br>

# Introduction
In the modern era of streaming platforms and personalized content, providing users with tailored recommendations has become a key factor in enhancing user engagement, satisfaction, and platform success. The ability to offer content that aligns with user preferences is achieved through advanced techniques like recommendation systems, which leverage vast amounts of data to understand and predict user behavior. In this project, we focus on the development of a movie recommendation system that harnesses the power of data analytics, unsupervised learning, and collaborative filtering methods to deliver personalized movie suggestions to users.
At the heart of our project lies the challenge of dealing with incomplete and sparse data, as our dataset contains significant missing values across several key attributes such as movie descriptions, genres, and director information. These missing data points pose challenges but also offer opportunities to explore advanced imputation techniques and model-based approaches for filling the gaps. Additionally, analyzing missing values helps us understand potential biases in data collection and usage patterns, which could impact the recommendation system’s performance.
The process begins with exploratory data analysis (EDA) to gain insights into the distribution and characteristics of the data. EDA helps us uncover hidden patterns in viewing behaviors, genre preferences, and movie ratings, and provides a foundation for building robust recommendation models. Handling missing data is a critical step in this phase, and we utilize techniques such as mean/mode imputation, k-nearest neighbor (KNN) imputation, or matrix factorization to reconstruct incomplete information.
Once the data is prepared, we proceed to develop the recommendation system using techniques item-based methods. These approaches rely on the similarities of items to make predictions . To enhance accuracy, matrix factorization techniques like Singular Value Decomposition (SVD) are employed to capture latent factors that influence user preferences but are not explicitly available in the dataset.
Moreover, this project includes the development of a data pipeline to ensure seamless data ingestion, preprocessing, and model_Trainer.
Future directions for this project include the integration of deep learning models, such as autoencoders or neural collaborative filtering (NCF), to further refine predictions and capture more complex user behaviors. Additionally, we aim to incorporate real-time feedback loops, enabling the recommendation engine to adapt on-the-fly to user interactions and provide even more personalized movie suggestions.
Ultimately, this project simulates the real-world application of recommendation systems in today’s competitive streaming industry, demonstrating how data-driven insights can enhance user experiences, improve retention, and drive overall business growth.

# Dataset Information
This a movie information data set which contains the names of the movies ,ratings,votes,genres names,languages ,budgets, revenues, runtime ,release_data of the movie also have many others thigs about the movies from different companies and nations.

## Data Card
- Size: 992715 rows * 27 columns
- Datatypes


| Variable Name | Role | Type | Description |
|:--------------|:-----|:-----|:------------|
|Title | name of movies|object | this feature contains the names of the movies|
|imdb_id| Unique id | categorical | each imdb_id represent the information of movies on imdb platform | 
|budget |investment in $| int64 | represent the investment in movies|
|revenue|total prrfilt in $| int64|total earning from the movie|



# Installation
This project uses 'python >=3.9'.Please ensure that the correct version is installed in your device.This project also works on Mac,Windows and Linux.

# Prerequisities 
1. git
2. python >=3.9
3. docker daemon/desktop is running

# User Installation 
The steps for User installtion are as follows:

1. Clone repository on the local machine 
'''
git clone https://github.com/ankitgaur0/movie_recommendation_system.git
'''
2. Check your python version
'''python
python --version
'''
3. Check if you have enough space
'''docker
docker run --rm "debian:bullseye-slim" bash -c 'numfmt --to iec $(echo $(($(getconf _PHYS_PAGES) * $(getconf PAGE_SIZE))))'
'''

<hr>
