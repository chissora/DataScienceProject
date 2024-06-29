from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads the requirements.txt file and returns a list of 
    requirements, excluding the '-e .' entry if it exists.
    
    Parameters:
    file_path (str): Path to the requirements file
    
    Returns:
    List[str]: List of requirements
    """
    requirements = []
    
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author='Dominik',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)