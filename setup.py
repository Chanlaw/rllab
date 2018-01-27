# setup.py
from setuptools import setup,find_packages

setup(
    name='rllab',
    install_requires=['theano', 'cached-property', 'python-dateutil', 
'path.py', 'joblib', 'pyprind', 'dill'],
    packages=[package for package in find_packages()
                if package.startswith('rllab')],
    version='0.1.0',
)
