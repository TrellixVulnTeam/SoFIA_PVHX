from setuptools import setup

setup(
    name='sofia',
    version='0.1',
    packages=['sofia'],
    url='https://github.com/pysofia/SoFIA',
    license='',
    author='Anabel del Val',
    author_email='',
    description='Sobol-based sensitivity analysis, Forward and Inverse uncertainty propagation with Application to high temperature gases.',
	install_requires=['matplotlib', 'numpy','scipy','sklearn','seaborn']
)
