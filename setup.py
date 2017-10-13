from setuptools import setup, find_packages
import glob

setup(name='loki',
      version='0.1',
      packages=find_packages(),
      scripts=glob.glob("scripts/*.py")
      )
