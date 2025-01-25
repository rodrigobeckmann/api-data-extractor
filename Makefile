# Virtual environment configuration
VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
IPYTHON = $(VENV)/bin/ipython

# Default target: displays available commands
help:
	@echo "Available commands:"
	@echo "  make setup         - Set up the virtual environment and install dependencies"
	@echo "  make run-script SCRIPT=<script_name> - Run a specified script using IPython"

# Set up the virtual environment and install dependencies
setup:
	@echo "Setting up the virtual environment..."
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "Environment setup complete!"

# Run the specified script
run-script:
	@if [ -z "$(SCRIPT)" ]; then \
		echo "Error: You need to specify a script path. Example: make run-script SCRIPT=example_extraction"; \
		exit 1; \
	fi
	@echo "Running script: $(SCRIPT)"
	$(IPYTHON) ./scripts/$(SCRIPT).py
