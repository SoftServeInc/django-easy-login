import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

files_to_exclude = ['.gitignore']

name = "django-easy-login"
version = "0.1.dev2"
release = "0.0.1"

setup(
    name=name,
    version=version,
    packages=find_packages(exclude=files_to_exclude),
    include_package_data=True,
    install_requires=['Django==2.2.24', 'pytz==2019.1'],

    license='MIT License',  # example license
    description='A simple Django app to switch between users without authentication.',
    long_description=README,
    url='https://django-easy-login.herokuapp.com/',
    author='SoftServe inc.',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
