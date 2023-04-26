from setuptools import setup

setup(
    name='mypackage',
    version='0.1',
    packages=['mypackage'],
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'mypackage = mypackage.__main__:main'
        ]
    },
    author='Your Name',
    author_email='princee.studio45creations',
    description='A short description of your package',
    url='https://github.com/yourusername/mypackage',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
