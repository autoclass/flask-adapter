from setuptools import setup

setup(
    name='flask-adapter',
    version='0.1',
    py_modules=['main'],
    entry_points={
        'console_scripts': ['main = main:run']
    },
)
