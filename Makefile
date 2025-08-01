.PHONY: help install lint format check test clean

# Default target
help:
	@echo "Available commands:"
	@echo "  install    Install dependencies"
	@echo "  lint       Run linting with ruff"
	@echo "  format     Format code with ruff"
	@echo "  check      Run both linting and format check"
	@echo "  fix        Fix linting issues and format code"
	@echo "  test       Run tests"
	@echo "  clean      Clean up cache files"

# Install dependencies
install:
	pip install -e .
	pip install ruff pytest

# Run linting
lint:
	ruff check .

# Format code
format:
	ruff format .

# Check formatting without modifying files
check:
	ruff check .
	ruff format --check .

# Fix linting issues and format code
fix:
	ruff check --fix .
	ruff format .

# Run tests
test:
	python -m pytest tests/ -v

# Clean up cache files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -name "*.pyc" -delete 