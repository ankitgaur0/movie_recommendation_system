from setuptools import setup,find_packages
from typing import List
from pathlib import Path

HYPEN_e_DOT="-e ."

def get_packages(file_path:str) ->List[str]:
    Requirement=[]
    if file_path !="":
        file_path=Path(file_path)
        with open(file_path,"r") as requirements:
            Requirement=requirements.readlines()


            Requirement=[escape_line.replace("\n","") for escape_line in Requirement]

            if HYPEN_e_DOT  in Requirement:
                Requirement.remove(HYPEN_e_DOT)

    else:
        print("file is not exists")

    return Requirement







setup(
    name="Movie_Recommendation_System",
    version='0.0.01',
    author="Ankit Gaur",
    author_email="ankitparashar000@gmail.com",
    packages=find_packages(),
    install_requires=get_packages("Requirements.txt")

)