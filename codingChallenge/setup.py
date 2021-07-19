from setuptools import setup

packages = []
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="codingChallenge",
    version="0.1.0",
    description="coding challegene",
    url="https://github.com/vas610/trav/tree/main/codingChallenge",
    author="vas610",
    author_email="github.com/vas610",
    license="Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International",
    include_package_data=True,
    install_requires=requirements,
    packages=packages,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
    ],
)
