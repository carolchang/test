try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'Carol Chang',
	'url': 'URL to get it at.',
	'download_url': 'Where to downlaod it',
	'author_email': 'homelover@gmail.com',
	'version':'0.1',
	'install_requires':['nose'],
	'packages':['ex47'],
	'scripts':[],
	'name':'ex47'
}

setup(**config)