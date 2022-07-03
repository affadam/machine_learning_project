##find packages will automatically call the libraries whiohc has the __init__.py resides
from setuptools import setup,find_packages
from typing import List

#Declaring varibles for setup functions
Project_name = "housing_predictor"
version="0.0.1"
author="Hari"
description = "first ML project for housing"
packages=["housing"]
requirements_file_name = "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function i goign to return the list of requiremnts
    mention in t=reuqiremnts.txt file
    return this function is going to return the a list which contain name of libraries mentioned in requirements.txt file
    """
    with open(requirements_file_name) as requiremnets_file:
        return requiremnets_file.readlines()

setup(

    name=Project_name,
    version=version,
    author = author,
    description=description,
    #Either we can call requiremnets.txt like line no 27 or 28
    #packages=packages,
    packages=find_packages(),
    install=get_requirements_list()
    
)



