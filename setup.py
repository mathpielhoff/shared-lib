from setuptools import setup, find_packages

setup(
    name="shared_lib",
    version="0.1.0",
    description="Shared configuration module for microservices",
    author="mpielhoff",
    packages=find_packages(),
    install_requires=[
        "python-dotenv>=0.21.0",
    ],
)
