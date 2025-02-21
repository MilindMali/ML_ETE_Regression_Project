from setuptools import setup , find_packages
from typing import List


PROJECT_NAME='ML Regression ETE Project Pipeline'
VERSION='0.0.1'
DESCRIPTION='This is end to end ML regression project to understand modular coding and complete ML life cycle'
AUTHOR_NAME='Milind Mali'
AUTHOR_EMAIL='milindmali108@gmail.com'

REQUIREMENTS_FILE_NAME='requirements.txt'

HYPHONE_E_DOT="-e ."

#to open requirements file--> read
def get_requirements_list()->list[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list=requirement_file.readlines()
        requirement_list=[requirement.replace("\n","") for requirement in requirement_list]

        if HYPHONE_E_DOT in requirement_list:
            requirement_list.remove(HYPHONE_E_DOT)

        return requirement_list


setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requires=get_requirements_list()
     )