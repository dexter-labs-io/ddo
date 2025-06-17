from setuptools import setup, find_packages

setup(
    name="ddo",
    version="0.1",
    description="Domain-Driven Orchestration framework",
    author="DexterLabs",
    author_email="opensource@dexter-labs.io",
    url="https://github.com/dexter-labs-io/ddo",
    packages=find_packages(include=["ddo_core*", "ddo_runtime*", "ddo_plugins*", "ddo_gov*", "ddo_ui*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.7',
)
