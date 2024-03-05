from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace('\n',"") for req in requirements]
        
        return requirements
setup(
    name="Diamond_Price_Prediction",
    version="0.0.1",
    description="ML project for diamond price prediction",
    author="Sumit_Panwar",
    author_email="sumitgurjar2373@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages()
)