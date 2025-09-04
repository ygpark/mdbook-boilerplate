# PowerShell build script for mdBook project
# Usage: .\make.ps1 [command]

param(
    [Parameter(Position=0)]
    [string]$Command = "help"
)

function Show-Help {
    Write-Host "Available commands:" -ForegroundColor Green
    Write-Host "  .\make.ps1 install         - Install mdbook and mdbook-mermaid"
    Write-Host "  .\make.ps1 install-mermaid - Install only mdbook-mermaid preprocessor"
    Write-Host "  .\make.ps1 init            - Initialize mermaid support in book.toml"
    Write-Host "  .\make.ps1 build           - Build the book"
    Write-Host "  .\make.ps1 serve           - Serve the book locally with live reload"
    Write-Host "  .\make.ps1 watch           - Same as serve (alias)"
    Write-Host "  .\make.ps1 clean           - Remove build artifacts"
    Write-Host "  .\make.ps1 test            - Run mdbook tests"
    Write-Host "  .\make.ps1 open            - Build and open the book in browser"
    Write-Host "  .\make.ps1 help            - Show this help message"
}

function Install-MdBook {
    Write-Host "Installing mdbook..." -ForegroundColor Yellow
    cargo install mdbook
    Write-Host "Installing mdbook-mermaid..." -ForegroundColor Yellow
    cargo install mdbook-mermaid
    Write-Host "Installation complete!" -ForegroundColor Green
}

function Install-MermaidOnly {
    Write-Host "Installing mdbook-mermaid..." -ForegroundColor Yellow
    cargo install mdbook-mermaid
    Write-Host "Installation complete!" -ForegroundColor Green
}

function Initialize-Mermaid {
    Write-Host "Initializing mdbook-mermaid..." -ForegroundColor Yellow
    mdbook-mermaid install .
    Write-Host "Initialization complete!" -ForegroundColor Green
}

function Build-Book {
    Write-Host "Building the book..." -ForegroundColor Yellow
    mdbook build
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Build complete!" -ForegroundColor Green
    } else {
        Write-Host "Build failed!" -ForegroundColor Red
        exit 1
    }
}

function Start-Server {
    Write-Host "Starting development server on http://localhost:3000" -ForegroundColor Yellow
    Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Cyan
    mdbook serve
}

function Clear-Build {
    Write-Host "Cleaning build artifacts..." -ForegroundColor Yellow
    mdbook clean
    Write-Host "Clean complete!" -ForegroundColor Green
}

function Test-Book {
    Write-Host "Running tests..." -ForegroundColor Yellow
    mdbook test
    if ($LASTEXITCODE -eq 0) {
        Write-Host "All tests passed!" -ForegroundColor Green
    } else {
        Write-Host "Tests failed!" -ForegroundColor Red
        exit 1
    }
}

function Open-Book {
    Build-Book
    Write-Host "Opening book in browser..." -ForegroundColor Yellow
    $indexPath = Join-Path $PSScriptRoot "book\index.html"
    if (Test-Path $indexPath) {
        Start-Process $indexPath
        Write-Host "Book opened in browser!" -ForegroundColor Green
    } else {
        Write-Host "Error: book\index.html not found. Build may have failed." -ForegroundColor Red
        exit 1
    }
}

# Check if required tools are installed
function Test-Requirements {
    $missing = @()
    
    if (-not (Get-Command "cargo" -ErrorAction SilentlyContinue)) {
        $missing += "cargo (Rust)"
    }
    
    if ($missing.Count -gt 0) {
        Write-Host "Missing required tools:" -ForegroundColor Red
        foreach ($tool in $missing) {
            Write-Host "  - $tool" -ForegroundColor Red
        }
        Write-Host "`nPlease install Rust from: https://www.rust-lang.org/tools/install" -ForegroundColor Yellow
        exit 1
    }
}

# Main execution
Test-Requirements

switch ($Command.ToLower()) {
    "help"           { Show-Help }
    "install"        { Install-MdBook }
    "install-mermaid" { Install-MermaidOnly }
    "init"           { Initialize-Mermaid }
    "build"          { Build-Book }
    "serve"          { Start-Server }
    "watch"          { Start-Server }
    "clean"          { Clear-Build }
    "test"           { Test-Book }
    "open"           { Open-Book }
    default {
        Write-Host "Unknown command: $Command" -ForegroundColor Red
        Write-Host ""
        Show-Help
        exit 1
    }
}