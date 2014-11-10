from setuptools import setup, find_packages

version = '1.0.0.1.dev0'
install_requires = ['pytest', 'django-model-utils >= 2.0.2', 'requests', ]
dependency_links = ["http://localshop.foolhq.com/simple"]

setup(name='tmf-django-utils',
      version=version,
      description='Django utilities',
      author="The Motley Fool",
      author_email="github@fool.com",
      url="https://github.com/themotleyfool/django-utils",
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
