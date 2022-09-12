install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

packadge-install:
	python3 -m pip install --user dist/*.whl

.PHONY: install test lint selfcheck check build