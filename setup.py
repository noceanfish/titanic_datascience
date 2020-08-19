#! /use/bin/env python

from distutils.core import setup


def readme():
	"""import the readme.md markdown file, try to convert it to RST format"""
	try:
		import pypandoc
		return pypandoc.convert_file('README.md', 'rst')
	except(IOError, ImportError):
		with open('README.md', 'rb') as f:
			return f.read()


setup(name='Distutils',
	  version='1.0',
	  description='Analysis of the Titanic dataset',
	  long_description=readme(),
	  classifiers=['Programming Language :: python :: 3',],
	  url='https://github.com/<github_account>/titanic_datascience',
	  author='JW',
	  author_email='pipi$!@163.com',
	  license='MIT',
	  packages=['Titanic'],
	  install_requires=[
        'pypandoc>=1.4',
        'watermark>=1.8.1',
        'pandas>=0.24.2',
        'scikit-learn>=0.20.3',
        'scipy>=1.2.1',
        'matplotlib>=3.0.3',
        'pytest>=4.3.1',
        'pytest-runner>=4.4',
        'click>=7.0'
	 ],
	setup_requires=['pytest-runner'],
	tests_require=['pytest'],
	entry_points='''
        [console_scripts]
        titanic_analysis=titanic.command_line:titanic_analysis
    '''
	)