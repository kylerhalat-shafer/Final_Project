from setuptools import setup, find_packages

setup(
    name='montecarlo',
    version='1.0.0',
    url='https://github.com/kylerhalat-shafer/Final_Project.git',
    author='Kyler Halat-Shafer',
    author_email='uxt5qb@virginia.edu',
    description='This package includes a montecarlo file that has three distinct classes in it to create a probabality object, use it and analyze the results. \n It also includes a testing file and demonstration file on how to use each of the classes',
    packages=find_packages(),   
    license = 'LICENSE.txt', 
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1', 'pandas >= 1.4.3'],
)
