.PHONY: test lint typecheck format format-check ci install clean
SHELL := /bin/bash

test:
	@echo "Running tests..."
	@uv run pytest tests/ --cov=src --cov-report=term --cov-report=html

lint:
	@echo "Running linter..."
	@uv run ruff check src/ tests/

typecheck:
	@echo "Running type checker..."
	@uv run mypy --package src

format:
	@echo "Formatting code..."
	@uv run ruff format src/ tests/

format-check:
	@echo "Checking code formatting..."
	@uv run ruff format --check src/ tests/

ci: format-check lint typecheck test
	@echo "✓ All CI checks passed!"

install:
	@echo "Installing uv if not present..."
	@if ! command -v uv >/dev/null 2>&1; then \
		echo "uv is not installed. Installing..."; \
		curl -LsSf https://astral.sh/uv/install.sh | sh; \
	else \
		echo "✓ uv is already installed."; \
	fi
	@echo "Installing Python dependencies..."
	@uv sync --locked --all-groups
	@echo "Installing git hooks..."
	@uv run --no-project pre-commit install
	@echo "✓ Setup complete!"

clean:
	@echo "Cleaning up..."
	@rm -rf __pycache__ .pytest_cache .coverage htmlcov
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete
