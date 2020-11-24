.PHONY: install poetry-install build package-install check

install:
	poetry install

poetry-install:
	poetry run brain-games

build:
	poetry build

package-install:
	pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games