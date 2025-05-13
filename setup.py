'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''

from setuptools import find_packages,setup
### find_packages: go through all folders and consider any folder with an __init__.py file as a package


from typing import List 

def get_requirements() -> List[str]: ### returns list of requirments
    requirement_lst:List[str]=[]
    try:
        with open ('requirements.txt','r') as file:
            # read lines from file
            lines=file.readlines()
            # process each line:
            for line in lines:
                requirement=line.strip()
                ##  ignore the empty lines and -e . (-e stands for editable. It’s a pip option that tells Python to install a package in editable mode.)
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file doesnt exist")
    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Samah EDDAOUDI",
    author_email="samaheddaoudi@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
                






