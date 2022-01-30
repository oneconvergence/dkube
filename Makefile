.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT


VERSION=2.3
help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr docs/build/website
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

docs: ## generate Sphinx HTML documentation, including API docs
	cd docs && ./build.sh

release: dist launcher## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	python setup.py bdist_wheel
	ls -l dist

image:
	docker build -t ocdr/dkube_pylauncher:$(VERSION) .;
	docker push ocdr/dkube_pylauncher:$(VERSION)

install: clean ## install the package to the active Python's site-packages
	python setup.py install

update: ## update version to given version
	sed  -i '' -e 's/$(VERSION)/$(version)/g' Makefile setup.py dkube/pipelines/components/op.py
