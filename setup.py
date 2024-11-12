from setuptools import setup, find_packages

setup(
    name="shared-config",
    version="0.1.0",
    description="Shared configuration module for microservices",
    author="mpielhoff",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "python-dotenv>=0.21.0",
    ],
)
