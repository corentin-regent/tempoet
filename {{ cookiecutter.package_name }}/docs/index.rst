{%- set title_delimiter = '=' * (cookiecutter.project_name | length) -%}
{{ title_delimiter }}
{{ cookiecutter.project_name }}
{{ title_delimiter }}

*{{ cookiecutter.short_description }}*

Documentation index
-------------------

.. toctree::
   :caption: Documentation
   :maxdepth: 2

   reference/index

.. toctree::
   :caption: Project information
   :hidden:
   {% if cookiecutter.license != 'None' %}
   license
   {%- endif %}
   changelog
   contributing
