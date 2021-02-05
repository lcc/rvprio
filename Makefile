PYTHONPATH := .
VENV := venv
PYMODULE := rvprio
REQUIREMENTS := -r requirements.txt

BIN := $(VENV)/bin
PIP := $(BIN)/pip
PYTHON := $(BIN)/python
PYLINT := $(BIN)/pylint
PRE_COMMIT := $(BIN)/pre-commit

PLANTUML_JAR_URL = https://sourceforge.net/projects/plantuml/files/plantuml.jar/download
PLANTUML = plantuml.jar

bootstrap: venv \
	requirements \
	commit-hooks

venv:
	python3 -m venv $(VENV)

requirements:
	$(PIP) install $(REQUIREMENTS)

commit-hooks: pre-commit \
	commit-msg

pre-commit:
	$(PRE_COMMIT) install

commit-msg:
	ln -s -f ../../hooks/commit-msg.sh .git/hooks/commit-msg

lint:
	$(PYLINT) --verbose $(PYMODULE)

.PHONY: docs
docs: $(PLANTUML)
	java -jar $(PLANTUML) docs/systemcontext.puml
	java -jar $(PLANTUML) docs/rvprio.puml

.PHONY: plantuml
$(PLANTUML):
	wget $(PLANTUML_JAR_URL) -O $(PLANTUML)

clean:
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type f -name '*.py[co]' -exec rm -rf {} +
	@find . -type f -name '*.log' -exec rm -rf {} +

clean-all: clean
	@rm -r $(VENV)
	@rm .git/hooks/pre-commit
	@rm .git/hooks/pre-commit
