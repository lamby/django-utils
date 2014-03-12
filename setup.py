from setuptools import setup, find_packages

version = '0.0.5.4'
install_requires = ['pytest', 'django-model-utils', 'requests', ]
dependency_links = []

setup(name='django-utils',
      version=version,
      description='Django utilities',
      author="The Motley Fool",
      author_email="github@fool.com",
      url="http://www.fool.com/",
      packages=find_packages(),
      include_package_data=True,
      install_requires=install_requires,
      dependency_links=dependency_links,
      zip_safe=False,
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Topic :: Software Development'
      ],
      )
