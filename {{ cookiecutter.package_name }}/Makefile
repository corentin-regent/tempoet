.PHONY: setup
setup:
{%- if cookiecutter.docs %}
	@poetry install --with dev,test,docs
{%- else %}
	@poetry install --with dev,test
{%- endif %}

.PHONY: lint
lint:
	@poetry run ruff check

.PHONY: format
format:
	@poetry run ruff format

.PHONY: type-check
type-check:
	@poetry run mypy .

.PHONY: test
test:
	@poetry run pytest -v tests/

.PHONY: coverage
coverage:
	@poetry run coverage run -m pytest -v tests/
	@poetry run coverage html
{%- if cookiecutter.docs %}

.PHONY: docs
docs:
	@poetry run sphinx-build docs docs/_build
{%- endif %}

.PHONY: clean
clean:
	@find . -name '__pycache__' -exec rm -rf {} +
	@rm -rf dist .coverage htmlcov .mypy_cache .pytest_cache .ruff_cache
{%- if cookiecutter.docs %}
	@rm -rf docs/_build
{%- endif %}
