from setuptools import setup, find_packages

setup(
    name="shared_lib",
    version="0.1.0",
    description="Shared librairies module for microservices",
    author="mpielhoff",
    packages=find_packages(include=["shared_lib", "shared_lib.*"]),
    install_requires=[
        "python-dotenv>=0.21.0",
    ],
)
