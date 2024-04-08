=======
Tempoet
=======

*Cookiecutter template for modern Poetry projects*

|ci| |cd|

.. |ci| image:: https://github.com/corentin-regent/tempoet/actions/workflows/ci.yml/badge.svg
  :alt: Continuous Integration
  :target: https://github.com/corentin-regent/tempoet/actions/workflows/ci.yml

.. |cd| image:: https://github.com/corentin-regent/tempoet/actions/workflows/cd.yml/badge.svg
  :alt: Continuous Deployment
  :target: https://github.com/corentin-regent/tempoet/actions/workflows/cd.yml

Features
========

This Cookiecutter_ template will get you started quickly with the following utilities:

* Dependency management with Poetry_

* Testing with Pytest_ (unittest is also supported natively)

* Code formatting and linting with Ruff_

* Type checking with Mypy_

* Documentation built with Sphinx_, using the Furo_ theme (optional)

  * Initialized for the reStructuredText_ format

  * `Markdown (MyST)`_ format is also supported

* CI/CD implemented with `GitHub Actions`_

  * Automated testing, linting, formatting, type checking, and quality reporting

  * Automated `GitHub releases`_ and PyPI_ deployments with automatic `semantic versioning`_, using Poetrel_

  * Automated documentation build and deployment to `GitHub Pages`_ (optional)

* Static analysis and coverage reports with SonarCloud_

* Automatic dependency scanning and updates with Dependabot_

* A `Development Container`_ is offered,
  to install all tools automatically in an isolated, consistent environment

* A Makefile_ is offered, to store useful commands

Tutorial
========

Running the template
--------------------

First, you will need to execute Cookiecutter_ on this project, in order to
generate all the files. This will create a new folder under the current folder,
containing your generated project, named according to the provided
``package_name`` input.

Below are two ways you can achieve this.

Using Docker (recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^

A Docker_ image hosted `on GitHub Packages <https://github.com/corentin-regent/tempoet/pkgs/container/tempoet>`_
can help you generate your project in an isolated, tested and reproducible environment.

You only need to run the following command in order to generate your project::

  docker run --user $(id -u) -i --rm -v .:/output ghcr.io/corentin-regent/tempoet:main

On Windows you need to run this using bash.
A solution is to execute it in a `Git Bash`_ shell.

Manually
^^^^^^^^

You can setup and run Cookiecutter_ manually in your own local environment
using the following commands::

  pip install cookiecutter
  cookiecutter gh:corentin-regent/tempoet

Inputs
------

Here is the reference of the inputs that will be prompted to you when running
the template:

================= ================================================================
Input name        Purpose
================= ================================================================
project_name      The name of your project
package_name      The name of your Python package
short_description A short description for your project
owner             The owner of the GitHub repository (GitHub user or organization)
author            The author of the project
email             The email address of this author
license           The license for your project
docs              Whether to setup documentation generation and releases
================= ================================================================

Make sure to visit PyPI_ beforehand to check that your ``package_name``
is not used already.

Setting up the repository
-------------------------

Hosting on GitHub
^^^^^^^^^^^^^^^^^

After you created the project, you can manually push it to GitHub_::

  cd <package_name>
  git init
  git add .
  git commit -m "Initial commit."
  git branch -M main
  git remote add origin git@github.com:<owner>/<package_name>.git
  git push -u origin main

Setting Secrets
^^^^^^^^^^^^^^^

You need to set the following secrets in your GitHub repository
for the GitHub Actions to work:

* ``PAT``: A `personal access token`_, with ``contents: write`` permission.

* ``PYPI_TOKEN``: A token for PyPI_, which can be generated `here <https://pypi.org/manage/account/token/>`_.

* ``SONAR_TOKEN``: A token for SonarCloud_, to generate on `this page <https://sonarcloud.io/account/security>`_.
  It is needed in both the 'Actions' secrets and the 'Dependabot' secrets.

Activating GitHub Pages
^^^^^^^^^^^^^^^^^^^^^^^

If you chose to have a project documentation, hosted on `GitHub Pages`_,
then you need to setup GitHub Pages in your GitHub Repository by heading to
``Settings > Code and automation > Pages`` and choose ``GitHub Actions``
as the source.

Setting up SonarCloud
^^^^^^^^^^^^^^^^^^^^^

You simply have to register your new project by setting it up in
`this tab <https://sonarcloud.io/projects/create>`_.

Time to code!
-------------

You are now ready to go!

Development procedures are listed in the generated ``CONTRIBUTING.rst`` file,
to help you get started.


.. _`branch policies`: https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _Dependabot: https://github.blog/2020-06-01-keep-all-your-packages-up-to-date-with-dependabot/
.. _`Development Container`: https://code.visualstudio.com/docs/devcontainers/containers
.. _Docker: https://www.docker.com/
.. _Furo: https://pradyunsg.me/furo/
.. _`Git Bash`: https://gitforwindows.org/
.. _GitHub: https://github.com/
.. _`GitHub Actions`: https://github.com/features/actions
.. _`GitHub Pages`: https://pages.github.com/
.. _`GitHub releases`: https://docs.github.com/repositories/releasing-projects-on-github/about-releases
.. _Makefile: https://www.gnu.org/software/make/
.. _`Markdown (MyST)`: https://myst-parser.readthedocs.io/
.. _Mypy: https://www.mypy-lang.org/
.. _`personal access token`: https://docs.github.com/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
.. _Poetrel: https://github.com/corentin-regent/poetrel
.. _Poetry: https://python-poetry.org/
.. _PyPI: https://pypi.org/
.. _Pytest: https://pytest.org/
.. _reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _Ruff: https://docs.astral.sh/ruff/
.. _`semantic versioning`: http://semver.org/
.. _SonarCloud: https://sonarcloud.io
.. _Sphinx: https://www.sphinx-doc.org/
