from setuptools import setup

setup(name='fixerpy',    
    version='0.1',
    description="A Python library for interacting with fixer.io.",
    url='https://github.com/rudimk/fixerpy',
    author='Rudraksh MK',
    author_email='rudraksh.mk@gmail.com',
    license='Apache',
    packages=['fixerpy'],
    install_requires=[
        'requests',
    ],
    zip_safe=False)