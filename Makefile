.PHONY: help docs run test

help:
	@echo "This project assumes an active Python virtualev is present."
	@echo "The following Make targets are available:"
	@echo "		help		display this help and exit"
	@echo "		docs		create pydocs for all relevant modules"
	@echo "		run		run the flask application
	@echo "		test		run all tests with coverage"

docs:
	./scripts/make_docs

run:
	export FLASK_APP=run.py && \
	export FLASK_DEBUG=true && \
	flask run --host=0.0.0.0

shell:
	export FLASK_APP=run.py && \
	flask shell

test:
	export FLASK_CONFIG=testing && \
	set -e && coverage run tests/main.py