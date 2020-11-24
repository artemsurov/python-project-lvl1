.PHONY: install

install:
	poetry install

poetry-install:
	poetry run brain-games

build:
	poetry build

package-install:
	pip install --user dist/*.whl