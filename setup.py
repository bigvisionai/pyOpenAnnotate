from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Automated single class image annotation tool.'
LONG_DESCRIPTION = 'An automated single class image annotation tool using OpenCV.'

# Setting up
setup(
    name="open-Annotate",
    version=VERSION,
    author="Kukil [LearnOpenCV]",
    author_email="<kukilp213@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['opencv-python'],
    keywords=['opencv', 'python', 'annotation tool', 'assisted annotation'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)