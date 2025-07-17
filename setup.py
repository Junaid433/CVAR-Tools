from setuptools import setup, find_packages

setup(
    name='pubg-cvar-tools',
    version='1.0',
    author='Junaid Rahman',
    description='Encrypt and decrypt PUBG Mobile CVAR strings with GUI',
    packages=find_packages(),
    install_requires=[
        'PySide6>=6.0.0',
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'pubg-cvar-tools=main:main',
        ],
    },
    python_requires='>=3.8',
)
