from setuptools import setup, find_packages

setup(
    name='aflaskapp',
    version='0.2.0',
    packages=['aflaskapp'],
    platforms='any',
    install_requires=[
        'Flask>=0.11.1',
        'gunicorn>=19.6'
    ]
)
