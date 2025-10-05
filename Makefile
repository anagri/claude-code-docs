.PHONY: help setup clean run run-html run-md run-full serve archive-status

# Default target - show help
help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'
	@echo ''
	@echo 'Examples:'
	@echo '  make setup       # First-time setup'
	@echo '  make run-full    # Download and convert to Markdown'
	@echo '  make serve       # Start local web server'

setup: ## Install dependencies using uv (first-time setup)
	@echo "Setting up project with uv..."
	@if ! command -v uv &> /dev/null; then \
		echo "Error: uv is not installed. Install it from https://docs.astral.sh/uv/"; \
		exit 1; \
	fi
	uv venv
	uv sync
	@echo "Setup complete! Virtual environment created at .venv"
	@echo "Run 'make run-full' to download and convert documentation"

clean: ## Remove downloads
	@echo "Removing downloads directory..."
	rm -rf downloads/
	@echo "Clean complete!"

clean-all: ## Remove downloads, archive, and virtual environment
	@echo "Removing downloads, archive, and .venv..."
	rm -rf downloads/ archive/ .venv/
	@echo "Clean complete! Run 'make setup' to start fresh"

run: run-full ## Alias for run-full (download and convert)

run-html: ## Download HTML documentation from Claude Code docs
	@echo "Downloading HTML documentation..."
	uv run python main.py --html
	@echo "HTML download complete! Files saved to downloads/html/"

run-md: ## Convert downloaded HTML to Markdown
	@echo "Converting HTML to Markdown..."
	uv run python main.py --md
	@echo "Markdown conversion complete! Files saved to downloads/md/"

run-full: ## Download HTML and convert to Markdown (recommended)
	@echo "Running full download and conversion..."
	uv run python main.py --html --md
	@echo "Complete! Documentation available in downloads/"

serve: ## Start local web server to browse downloaded docs (port 8000)
	@echo "Starting local web server on http://localhost:8000"
	@echo "Press Ctrl+C to stop..."
	uv run python main.py --serve

serve-port: ## Start local web server on custom port (usage: make serve-port PORT=8080)
	@echo "Starting local web server on http://localhost:$(PORT)"
	@echo "Press Ctrl+C to stop..."
	uv run python main.py --serve --port $(PORT)

archive-status: ## Show current download date and archive history
	@echo "Current download date:"
	@if [ -f downloads/meta.json ]; then \
		cat downloads/meta.json; \
	else \
		echo "  No active download (run 'make run-html' first)"; \
	fi
	@echo ""
	@echo "Archived downloads:"
	@if [ -d archive ]; then \
		ls -1 archive/ | sed 's/^/  /'; \
	else \
		echo "  No archives yet"; \
	fi

info: ## Show project information and current state
	@echo "Claude Code Documentation Scraper"
	@echo "=================================="
	@echo ""
	@echo "Python version:"
	@uv run python --version
	@echo ""
	@echo "Current download status:"
	@if [ -f downloads/meta.json ]; then \
		echo "  Date: $$(cat downloads/meta.json | grep download_date | cut -d'"' -f4)"; \
		echo "  HTML files: $$(find downloads/html -name '*.html' 2>/dev/null | wc -l | tr -d ' ')"; \
		echo "  MD files: $$(find downloads/md -name '*.md' 2>/dev/null | wc -l | tr -d ' ')"; \
	else \
		echo "  No active download"; \
	fi
	@echo ""
	@echo "Archives:"
	@if [ -d archive ]; then \
		for dir in archive/*/; do \
			date=$$(basename $$dir); \
			count=$$(find $$dir/html -name '*.html' 2>/dev/null | wc -l | tr -d ' '); \
			echo "  $$date: $$count HTML files"; \
		done; \
	else \
		echo "  No archives"; \
	fi

check: ## Verify uv and dependencies are installed
	@echo "Checking dependencies..."
	@if command -v uv &> /dev/null; then \
		echo "✓ uv is installed ($$(uv --version))"; \
	else \
		echo "✗ uv is not installed"; \
		echo "  Install from: https://docs.astral.sh/uv/"; \
		exit 1; \
	fi
	@if [ -d .venv ]; then \
		echo "✓ Virtual environment exists"; \
	else \
		echo "✗ Virtual environment not found"; \
		echo "  Run 'make setup' to create it"; \
		exit 1; \
	fi
	@echo "All checks passed!"
