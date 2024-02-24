import os
#from runpy import run_path

from setuptools import find_packages, setup

# read the program version from version.py (without loading the module)
#__version__ = run_path('src/yose/version.py')['__version__']
from src.yose import __version__

def read(fname):
    """Utility function to read the README file."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="yose",
    version=__version__,
    author="Alejandro Gil",
    author_email="alejandrogilelias940711@gmail.com",
    description="Your Own Search Engine that can be completely customized.",
    license="proprietary",
    url="",
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={'yose': ['res/*']},
    long_description=read('README.md'),
    install_requires=[],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pre-commit',
    ],
    platforms='any',
    python_requires='>=3.8',
)
