.PHONY: help build serve watch clean test install install-mermaid install-autosummary install-toc init dev open mdbook-init completions

# Default target
help:
	@echo "Available commands:"
	@echo "  make install        - Install all mdbook components"
	@echo "  make install-mermaid- Install only mdbook-mermaid preprocessor"
	@echo "  make install-autosummary - Install mdbook-autosummary preprocessor"
	@echo "  make install-toc    - Install mdbook-toc preprocessor"
	@echo "  make init           - Initialize mermaid support in book.toml"
	@echo "  make build          - Build the book"
	@echo "  make serve          - Serve the book locally with live reload"
	@echo "  make watch          - Watch for changes and rebuild automatically"
	@echo "  make dev            - Same as serve (alias)"
	@echo "  make clean          - Remove build artifacts"
	@echo "  make test           - Run mdbook tests"
	@echo "  make open           - Build and open the book in browser"
	@echo "  make mdbook-init    - Initialize a new mdbook project (with confirmation)"
	@echo "  make completions    - Show commands to generate shell completions"

# Install all mdbook components
install:
	@echo "Installing mdbook..."
	cargo install mdbook
	@echo "Installing mdbook-mermaid..."
	cargo install mdbook-mermaid
	@echo "Installing mdbook-autosummary..."
	cargo install mdbook-autosummary
	@echo "Installing mdbook-toc..."
	cargo install mdbook-toc

# Install only mdbook-mermaid
install-mermaid:
	@echo "Installing mdbook-mermaid..."
	cargo install mdbook-mermaid

# Install mdbook-autosummary
install-autosummary:
	@echo "Installing mdbook-autosummary..."
	cargo install mdbook-autosummary

# Install mdbook-toc
install-toc:
	@echo "Installing mdbook-toc..."
	cargo install mdbook-toc

# Initialize mermaid support in book.toml
init:
	@echo "Initializing mdbook-mermaid..."
	mdbook-mermaid install .

# Build the book
build:
ifeq ($(OS),Windows_NT)
	@powershell -Command "if (!(Test-Path 'src\SUMMARY.md')) { Write-Host 'Creating initial SUMMARY.md...'; Set-Content -Path 'src\SUMMARY.md' -Value '# Summary','','[Introduction](index.md)' }"
else
	@if [ ! -f src/SUMMARY.md ]; then \
		echo "Creating initial SUMMARY.md..."; \
		echo "# Summary\n\n[Introduction](index.md)" > src/SUMMARY.md; \
	fi
endif
	mdbook build

# Serve the book with live reload (default port 3000)
serve:
ifeq ($(OS),Windows_NT)
	@powershell -Command "if (!(Test-Path 'src\SUMMARY.md')) { Write-Host 'Creating initial SUMMARY.md...'; Set-Content -Path 'src\SUMMARY.md' -Value '# Summary','','[Introduction](index.md)' }"
else
	@if [ ! -f src/SUMMARY.md ]; then \
		echo "Creating initial SUMMARY.md..."; \
		echo "# Summary\n\n[Introduction](index.md)" > src/SUMMARY.md; \
	fi
endif
	mdbook serve

# Alias for serve
dev: serve

# Watch for changes and rebuild automatically
watch:
ifeq ($(OS),Windows_NT)
	@powershell -Command "if (!(Test-Path 'src\SUMMARY.md')) { Write-Host 'Creating initial SUMMARY.md...'; Set-Content -Path 'src\SUMMARY.md' -Value '# Summary','','[Introduction](index.md)' }"
else
	@if [ ! -f src/SUMMARY.md ]; then \
		echo "Creating initial SUMMARY.md..."; \
		echo "# Summary\n\n[Introduction](index.md)" > src/SUMMARY.md; \
	fi
endif
	mdbook watch

# Initialize a new mdbook project (use with caution in existing project)
mdbook-init:
	@echo "Warning: This will create a new mdbook project structure"
	@read -p "Are you sure? (y/N) " -n 1 -r; \
	echo; \
	if [[ $$REPLY =~ ^[Yy]$$ ]]; then \
		mdbook init .; \
	else \
		echo "Operation cancelled."; \
	fi

# Generate shell completions
completions:
	@echo "Generating shell completions..."
	@echo "Run: mdbook completions bash > ~/.bash_completion.d/mdbook"
	@echo "Run: mdbook completions zsh > ~/.zfunc/_mdbook"
	@echo "Run: mdbook completions fish > ~/.config/fish/completions/mdbook.fish"
	@echo "Run: mdbook completions powershell > mdbook.ps1"

# Clean build artifacts
clean:
	mdbook clean

# Run tests (disabled for documentation projects)
test:
	@echo "Tests are disabled for documentation projects"
	@echo "Use 'make build' to verify the book builds correctly"

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