import os,glob
from setuptools import  setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

datadir = os.path.join('mfiles','wtc')
datafiles = [(datadir, [f for f in glob.glob(os.path.join(datadir, '*'))])]


setup(
    name = "apibdtsent",
    version = "0.1.0",
    author = "Eduardo dos Santos Pereira",
    author_email = "pereira.somoza@gmail.com",
    description = ("Api de analise de sentimentos de pt-BR"),
    license = "GNU v3",
    keywords = "computacao cognitiva",
    url = "http://twipiniquim.com",
    packages= find_packages(),
    install_requires=['requests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: GNU V3",
    ],
)
