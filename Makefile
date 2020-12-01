.PHONY: install poetry-install build package-install check test

install:
	poetry install

build:
	poetry build

package-install: build
	pip install --user --no-build-isolation dist/*.whl

lint:
	poetry run flake8 brain_games

test:
	poetry run pytest

update_pip:
	python -m pip install --upgrade pip