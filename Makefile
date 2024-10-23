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
	pytest $(CURDIR)/tests/

.PHONY: test
test:
	pytest $(CURDIR)/test/ $(CURDIR)/tests/

.PHONY: coverage
coverage:
	pytest --junitxml=coverage.xml \
		--cov-report=term-missing:skip-covered \
		--cov=vulncheck_sdk \
		$(CURDIR)/tests/ \
		$(CURDIR)/test/ \
		| tee .coverage.txt
