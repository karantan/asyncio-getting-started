# convenience makefile to run buildout and tests

.DEFAULT_GOAL := build


run-blocking:
	@env/bin/python3 -m src.blocking_asyncio

run-non-blocking:
	@env/bin/python3 -m src.nonblocking_asyncio

build:
	virtualenv -p python3 env
	@env/bin/pip install -r requirements.txt
	@if [ -f requirements-dev.txt ]; then env/bin/pip install -r requirements-dev.txt; fi;

package: pip-compile pipdeptree

pip-compile:
	@env/bin/pip-compile --output-file requirements.txt setup.py requirements-dev.in

pip-upgrade:
	@env/bin/pip-compile --upgrade --output-file requirements.txt setup.py requirements-dev.in

pipdeptree:
	@env/bin/pipdeptree > requirements-tree.txt

pip-sync:
	@env/bin/pip-sync

clean:
	@rm -rf env
	@rm -rf __pycache__
	@rm -rf .cache

sort:
	@env/bin/isort -rc -fas -sl src

tests:
	@env/bin/pytest --cov=src --cov-report=html --cov-fail-under=100 tests/* -v

.PHONY: all tests clean