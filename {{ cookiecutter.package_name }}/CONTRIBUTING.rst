Contributing
============

Setting up
----------

Using a Dev Container (recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open the project in the provided development container to get
all tools and dependencies up and running automatically.

If it is your first time using a dev container, you can follow
`this guide <https://code.visualstudio.com/docs/devcontainers/containers#_installation>`_
to set it up.

Manual installation
^^^^^^^^^^^^^^^^^^^

See `this page <https://python-poetry.org/docs/>`_
to install poetry if you don't have it already.

All the commands that you may use are grouped in the root Makefile.
So make sure that you have `Make <https://www.gnu.org/software/make/>`_
available in your environment, otherwise you can just copy the commands
from the Makefile and paste them in your terminal.

In order to install the project and required dependencies, you can run ``make setup``.

Testing
-------

Running tests
^^^^^^^^^^^^^

Tests can be run with `pytest <https://docs.pytest.org/>`_ using ``make test``.

Test coverage
^^^^^^^^^^^^^

You can check your test coverage locally by using the
`coverage <https://coverage.readthedocs.io/>`_
package through ``make coverage``.

An HTML report will be generated in the ``htmlcov`` directory
at the root of the project, highlighting which lines
of code were not covered by the tests.

Linting and code formatting
---------------------------

`Ruff <https://docs.astral.sh/ruff/>`_ is used for linting and formatting our code.
It can be run using the ``make lint`` and ``make format`` commands.

Type checking
-------------

This project ensures strict type checking using `mypy <https://github.com/python/mypy>`_.
In order to check whether your changes are correctly typed,
you can run ``make type-check``.
{%- if cookiecutter.docs %}

Documentation
-------------

All user-exposed classes, methods and functions you add must be documented, following the
`Google style guide <https://google.github.io/styleguide/pyguide.html>`_.

The documentation is built using `Sphinx <https://sphinx-doc.org>`_.
You can generate it locally using ``make docs``.
{%- endif %}

Deployment
----------
{%- if cookiecutter.docs %}

Project
^^^^^^^
{%- endif %}

The project is released automatically to PyPI using
`Poetrel <https://github.com/corentin-regent/poetrel>`_,
each time a pull request with a ``poetrel:`` label is merged on the main branch.
See the documentation there for details.
{%- if cookiecutter.docs %}

Documentation
^^^^^^^^^^^^^

The documentation is built and deployed automatically to
`GitHub Pages <https://{{ cookiecutter.owner }}.github.io/{{ cookiecutter.package_name }}/>`_
after each release of the project.
{%- endif %}
