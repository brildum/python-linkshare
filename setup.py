
import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "python-linkshare",
    version = "0.0.1",
    author = "Chris Carroll",
    author_email = "brildum@gmail.com",
    description = ("Python client for LinkShare APIs"),
    license = "BSD",
    keywords = "linkshare affiliate",
    url = "https://github.com/brildum/python-linkshare",
    packages = find_packages(),
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
