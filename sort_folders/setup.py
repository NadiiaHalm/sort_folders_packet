from setuptools import setup, find_namespace_packages

setup(name='sort_folders',
      version='0.0.1',
      description='Very usefull code for sorting your folders',
      url='https://github.com/NadiiaHalm/sort_folders.git',
      author='NADIIA HALMANCHENKO',
      license='MIT',
      packages=['sort_folders'],
      install_requires=[
          'markdown',
      ],
      include_package_data=True,
      zip_safe=False)