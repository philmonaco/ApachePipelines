from setuptools import setup, find_packages

setup(
    name='apache-spaceflight-pipeline-demo',
    version='1.0.0',
    author='Your Name',
    author_email='your_email@example.com',
    description='Description of your project',
    packages=find_packages(),
    install_requires=[
        'pykafka',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'spaceflight = src.spaceflight.cli:cli',
        ],
    },
)