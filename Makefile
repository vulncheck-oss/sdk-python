.PHONY: deps
deps:
	poetry install

.PHONY: lint
lint:
	# stop the build if there are Python syntax errors or undefined names
	poetry run flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	poetry run flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

#### Build Commands ####

.PHONY: generate
generate:
	$(CURDIR)/scripts/generate.sh $(CURDIR)

.PHONY: build
build:
	poetry build

#### Test Commands ####

.PHONY: test-integration
test-integration:
	poetry run pytest $(CURDIR)/tests/

.PHONY: test
test:
	poetry run pytest $(CURDIR)/test/ $(CURDIR)/tests/

.PHONY: coverage
coverage:
	poetry run pytest --junitxml=coverage.xml \
		--cov-report=term-missing:skip-covered \
		--cov=vulncheck_sdk \
		$(CURDIR)/tests/ \
		$(CURDIR)/test/ \
		| tee .coverage.txt
