from setuptools import setup, find_packages
import os

os.system('set DJANGO_SETTINGS_MODULE=scraperUi.settings')

setup(name='scraperProject', version='1.0', packages=find_packages())