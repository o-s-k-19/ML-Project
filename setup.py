from setuptools import find_packages,setup
from typing import List

HYPHEN_E_="-e."
def get_requirements(file_path:str)->List[str]:
    '''
    cette fonction renvoie les librairies requis pour le projet
    '''
    
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[line.replace("\n","") for line in requirements]
    
    if HYPHEN_E_ in requirements:
        requirements.remove(HYPHEN_E_)
    
    return requirements



setup(
name='ml-generic-project',
version='0.0.1',
description='a generic ml project',
author='ousseini',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)