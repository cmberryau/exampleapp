from setuptools import setup, find_packages

setup(name='exampleapp',
      version='2019.1',
      description='An example of packaging up a django app',
      packages=find_packages(),
      install_requires=[
        'django==2.2.27',
        'unittest-xml-reporting==2.5.1',
      ],
      include_package_data=True,
      zip_safe=False)
