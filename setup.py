from setuptools import setup, find_packages
setup(
    name='habitaclia',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'psycopg2',
        'sqlalchemy',
        'scrapy-slackbot'
    ],
    entry_points={'scrapy': ['settings = habitaclia.settings']}
)