import os
from shutil import rmtree

if '{{ cookiecutter.license }}' == 'None':
    os.remove('LICENSE')
    os.remove('docs/license.rst')

if '{{ cookiecutter.docs }}' == 'False':
    rmtree('docs')
