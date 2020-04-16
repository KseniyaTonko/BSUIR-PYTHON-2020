from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='lab_2',
    version="",
    packages=find_packages(),
    url="",
    author="Kseniya Tonko",
    author_email="kseniya.tonko@gmail.com",
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    test_suite='tests',
    include_package_data=True,
)
