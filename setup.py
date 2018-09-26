from setuptools import setup
from setuptools import find_packages

setup(
    name='zadacha',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask-migrate',
        'flask-wtf',
        'psycopg2-binary',
        'ldclient-py',
        'flask-security'
    ]
)