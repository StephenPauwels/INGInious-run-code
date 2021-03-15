from setuptools import setup, find_packages

setup(
    name="inginious-run-code",
    version="0.1",
    description="Plugin to allow students to run python code and get the output back without getting graded",
    packages=find_packages(),
    install_requires=["inginious"],
    test_require=[],
    extras_require={},
    scripts=[],
    include_package_data=True,
    author="Stephen Pauwels - UAntwerpen",
    author_email="stephen.pauwels@uantwerpen.be",
    license="AGPL 3",
    url=""
)