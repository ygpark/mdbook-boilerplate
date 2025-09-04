.PHONY: help build serve clean test install install-mermaid init watch open

# Default target
help:
	@echo "Available commands:"
	@echo "  make install        - Install mdbook and mdbook-mermaid"
	@echo "  make install-mermaid- Install only mdbook-mermaid preprocessor"
	@echo "  make init           - Initialize mermaid support in book.toml"
	@echo "  make build          - Build the book"
	@echo "  make serve          - Serve the book locally with live reload"
	@echo "  make watch          - Same as serve (alias)"
	@echo "  make clean          - Remove build artifacts"
	@echo "  make test           - Run mdbook tests"
	@echo "  make open           - Build and open the book in browser"

# Install mdbook and mdbook-mermaid
install:
	@echo "Installing mdbook..."
	cargo install mdbook
	@echo "Installing mdbook-mermaid..."
	cargo install mdbook-mermaid

# Install only mdbook-mermaid
install-mermaid:
	@echo "Installing mdbook-mermaid..."
	cargo install mdbook-mermaid

# Initialize mermaid support in book.toml
init:
	@echo "Initializing mdbook-mermaid..."
	mdbook-mermaid install .

# Build the book
build:
	mdbook build

# Serve the book with live reload (default port 3000)
serve:
	mdbook serve

# Alias for serve
watch: serve

# Clean build artifacts
clean:
	mdbook clean

# Run tests
test:
	mdbook test

# Build and open in browser
open: build
	@echo "Opening book in browser..."
ifeq ($(OS),Windows_NT)
	@powershell -Command "if (Test-Path 'book\index.html') { Start-Process 'book\index.html' } else { Write-Host 'Error: book\index.html not found. Build may have failed.' }"
else
	@if [ -f book/index.html ]; then \
		open book/index.html 2>/dev/null || xdg-open book/index.html 2>/dev/null || start book/index.html; \
	else \
		echo "Error: book/index.html not found. Build may have failed."; \
	fi
endif