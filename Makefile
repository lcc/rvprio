PYTHONPATH := .
VENV := venv
PYMODULE := rvprio
REQUIREMENTS := -r requirements.txt

BIN := $(VENV)/bin
PIP := $(BIN)/pip
PYTHON := $(BIN)/python
PRE_COMMIT := $(BIN)/pre-commit

bootstrap: venv \
	requirements \
	commit-hooks

venv:
	python3 -m venv $(VENV)

requirements:
	$(PIP) install $(REQUIREMENTS)

commit-hooks:
	$(PRE_COMMIT) install

clean:
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type f -name '*.py[co]' -exec rm -rf {} +
	@find . -type f -name '*.log' -exec rm -rf {} +

clean-all: clean
	@rm -r $(VENV)
	@rm .git/hooks/pre-commit
