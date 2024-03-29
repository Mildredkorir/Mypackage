from setuptools import setup, find_packages

setup(
    name='myPackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Mildredkorir/Mypackage',
    author='<Mildred_Korir>',
    author_email='<mildredk.jebet@gmail.com>'
)