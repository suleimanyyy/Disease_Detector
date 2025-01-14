from setuptools import find_packages, setup
from typing import List


Hyphen_e_dot ='-e .'
def get_requirements(filepath:str)-> List[str]:
    """ This function will return a list of requirements """
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n", "") for req in requirements]

        if Hyphen_e_dot in requirements:
            requirements.remove(Hyphen_e_dot)
            
    return requirements


setup(
name="DISEASE_DETECTOR",
version="0.0.1",
author="Suleiman",
description="Disease detection app",
long_description="Disease Detection",
long_description_content_type="text/markdown",
author_email="suleiman.onimi@gmail.com",
packages=find_packages(where="src"),
package_dir={"": "src"},
install_requires = get_requirements('requirements.txt')
)