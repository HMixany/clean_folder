from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='1',
      description='Sorts files',
      url='https://github.com/HMixany/clean_folder.git',
      author='Mykhailo Hrytsan',
      author_email='hmixany@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']})