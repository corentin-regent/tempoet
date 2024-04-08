{%- set title_delimiter = '=' * (cookiecutter.project_name | length) -%}
{{ title_delimiter }}
{{ cookiecutter.project_name }}
{{ title_delimiter }}

*{{ cookiecutter.short_description }}*

======= ====================================================================
CI/CD   |ci| |cd|
Package |python-version| |package-version| |license|
Quality |coverage| |quality-gate| |maintainability| |reliability| |security|
Meta    |type-check| |code-style|
======= ====================================================================

Documentation
=============

Full documention can be found at
https://{{ cookiecutter.owner }}.github.io/{{ cookiecutter.package_name }}/

Credits
=======

This package was initialized with
`Cookiecutter <https://github.com/audreyr/cookiecutter>`_
and the `Tempoet <https://github.com/corentin-regent/tempoet>`_
project template.


.. CI/CD:

.. |ci| image:: https://github.com/{{ cookiecutter.owner }}/{{ cookiecutter.package_name }}/actions/workflows/ci.yml/badge.svg
  :alt: Continuous Integration
  :target: https://github.com/{{ cookiecutter.owner }}/{{ cookiecutter.package_name }}/actions/workflows/ci.yml

.. |cd| image:: https://github.com/{{ cookiecutter.owner }}/{{ cookiecutter.package_name }}/actions/workflows/cd.yml/badge.svg
  :alt: Continuous Deployment
  :target: https://github.com/{{ cookiecutter.owner }}/{{ cookiecutter.package_name }}/actions/workflows/cd.yml

.. Package:

.. |python-version| image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.package_name }}?logo=python
  :alt: Python Versions

.. |package-version| image:: https://img.shields.io/pypi/v/{{ cookiecutter.package_name }}?logo=python
  :alt: Package Version
  :target: https://pypi.org/project/{{ cookiecutter.package_name }}/

.. |license| image:: https://img.shields.io/pypi/l/{{ cookiecutter.package_name }}
  :alt: License
  :target: https://{{ cookiecutter.owner }}.github.io/{{ cookiecutter.package_name }}/license.html

.. Quality:

.. |coverage| image:: https://img.shields.io/sonar/coverage/{{ cookiecutter.owner }}_{{ cookiecutter.package_name }}?server=https%3A%2F%2Fsonarcloud.io&logo=sonarcloud
  :alt: Code Coverage
  :target: https://sonarcloud.io/summary/overall?id={{ cookiecutter.owner }}_{{ cookiecutter.package_name }}

.. |quality-gate| image:: https://sonarcloud.io/api/project_badges/measure?project={{ cookiecutter.owner }}_{{ cookiecutter.package_name }}&metric=alert_status
  :alt: Quality Gate
  :target: https://sonarcloud.io/summary/overall?id={{ cookiecutter.owner }}_{{ cookiecutter.package_name }}

.. |maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project={{ cookiecutter.owner }}_{{ cookiecutter.package_name }}&metric=sqale_rating
  :alt: Maintainability Rating
  :target: https://sonarcloud.io/summary/overall?id={{ cookiecutter.owner }}_{{ cookiecutter.package_name }}

.. |reliability| image:: https://sonarcloud.io/api/project_badges/measure?project={{ cookiecutter.owner }}_{{ cookiecutter.package_name }}&metric=reliability_rating
  :alt: Reliability Rating
  :target: https://sonarcloud.io/summary/overall?id={{ cookiecutter.owner }}_{{ cookiecutter.package_name }}

.. |security| image:: https://sonarcloud.io/api/project_badges/measure?project={{ cookiecutter.owner }}_{{ cookiecutter.package_name }}&metric=security_rating
  :alt: Security Rating
  :target: https://sonarcloud.io/summary/overall?id={{ cookiecutter.owner }}_{{ cookiecutter.package_name }}

.. Meta:

.. |type-check| image:: https://www.mypy-lang.org/static/mypy_badge.svg
  :alt: Type Checked
  :target: https://mypy-lang.org/

.. |code-style| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
  :alt: Code Style
  :target: https://github.com/astral-sh/ruff
