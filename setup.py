import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PPool",
    version="0.0.1",
    author="Ahmad Alobaid",
    author_email="aalobaid@fi.upm.es",
    description="A Pool for Processes in Python with locks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oeg-upm/PPool",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: System :: Operating System"
    ),
)