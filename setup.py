import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name='django-jsoneditor',
    version='0.0.1',
    url='https://github.com/inmagik/django-jsoneditor',
    install_requires=[
        'Django >=1.8',
    ],
    description="JSON editor fields and widgets",
    long_description=README,
    license="MIT",
    author="Mauro Bianchi",
    author_email="bianchimro@gmail.com",
    packages=['jsoneditor'],
    #package_dir={'jsoneditor': 'jsoneditor'},
    include_package_data = True,    # include everything in source control
    #package_data={'jsoneditor': ['*.py','contrib/*.py','tests/*.py','tests/templates/*.html']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python']
)
