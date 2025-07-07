from setuptools import setup, find_packages

setup(
    name='CurrencyConverter',
    version='1.0.0',
    description='A simple Tkinter-based Currency Converter using real-time exchange rates.',
    author='Yugank',
    author_email='your_email@example.com',
    packages=find_packages(),
    py_modules=['Currency_converter'],
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'currency-converter = Currency_converter:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
