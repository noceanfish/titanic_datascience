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
	  packages=['Titanic']
	)