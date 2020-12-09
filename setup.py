from setuptools import setup

setup(
    name='flask-adapter',
    version='0.4',
    py_modules=['main'],
    entry_points={
        'console_scripts': ['flask-adapter = main:run']
    },
)
