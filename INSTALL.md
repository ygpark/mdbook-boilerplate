# Installation Guide

This guide will help you set up and install all necessary components for this mdBook project.

## Prerequisites

### 1. Rust and Cargo
mdBook and its plugins require Rust to be installed.

**Windows:**
```powershell
# Download and run rustup-init.exe from https://rustup.rs/
# Or use winget:
winget install Rustlang.Rustup
```

**macOS/Linux:**
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

## Required Components

### 1. mdBook
The main static site generator for creating books from Markdown files.

```bash
cargo install mdbook
```

### 2. mdbook-mermaid
Adds support for Mermaid diagrams in your book.

```bash
cargo install mdbook-mermaid
```

### 3. mdbook-autosummary
Automatically generates SUMMARY.md based on your file structure.

```bash
cargo install mdbook-autosummary
```

### 4. mdbook-toc
Generates table of contents for each chapter.

```bash
cargo install mdbook-toc
```

## Quick Installation

### Option 1: Using Make (Unix/Linux/macOS)
```bash
# Install all components at once
make install

# Or install individually
make install-mermaid
```

### Option 2: Using PowerShell Script (Windows)
```powershell
# Install all components
.\make.ps1 install

# Or install individually
.\make.ps1 install-mermaid
```

### Option 3: Manual Installation
```bash
# Install all components manually
cargo install mdbook
cargo install mdbook-mermaid
cargo install mdbook-autosummary
cargo install mdbook-toc

# Initialize mermaid support
mdbook-mermaid install
```

## Verify Installation

Check that all components are installed correctly:

```bash
mdbook --version
mdbook-mermaid --version
mdbook-autosummary --version
mdbook-toc --version
```

## Initialize the Project

After installation, initialize the mermaid support:

```bash
# Using Make
make init

# Using PowerShell
.\make.ps1 init

# Or manually
mdbook-mermaid install
```

## Build and Serve

### Build the book
```bash
# Using Make
make build

# Using PowerShell
.\make.ps1 build

# Or manually
mdbook build
```

### Serve with live reload
```bash
# Using Make
make serve

# Using PowerShell
.\make.ps1 serve

# Or manually
mdbook serve
```

The book will be available at `http://localhost:3000`

## Troubleshooting

### PowerShell Execution Policy (Windows)
If you encounter execution policy errors when running `make.ps1`:

```powershell
# Run with bypass flag
powershell -ExecutionPolicy Bypass -Command ".\make.ps1 [command]"

# Or change execution policy (requires admin)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Missing Dependencies
If any preprocessor is missing, you'll see warnings like:
```
[WARN] The command wasn't found, is the "xxx" preprocessor installed?
```

Install the missing component using:
```bash
cargo install mdbook-xxx
```

### Build Errors
If you encounter build errors:

1. Clean the build directory:
   ```bash
   mdbook clean
   # or
   make clean
   ```

2. Verify all files referenced in SUMMARY.md exist
3. Check `book.toml` configuration is valid

## Update Components

To update installed components to their latest versions:

```bash
cargo install --force mdbook
cargo install --force mdbook-mermaid
cargo install --force mdbook-autosummary
cargo install --force mdbook-toc
```

## Additional Resources

- [mdBook Documentation](https://rust-lang.github.io/mdBook/)
- [mdbook-mermaid](https://github.com/badboy/mdbook-mermaid)
- [mdbook-autosummary](https://github.com/daviddrysdale/mdbook-autosummary)
- [mdbook-toc](https://github.com/badboy/mdbook-toc)