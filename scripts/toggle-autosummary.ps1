# autosummary 토글 PowerShell 스크립트
# Usage: .\scripts\toggle-autosummary.ps1 [on|off]

param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("on", "off")]
    [string]$Action
)

$BookToml = "book.toml"

if (!(Test-Path $BookToml)) {
    Write-Error "Error: book.toml not found!"
    exit 1
}

$content = Get-Content $BookToml

switch ($Action) {
    "on" {
        Write-Host "Enabling autosummary..." -ForegroundColor Green
        $content = $content -replace '^#\[preprocessor\.autosummary\]', '[preprocessor.autosummary]'
        $content = $content -replace '^#index-name = ', 'index-name = '
        $content = $content -replace '^#ignore-hidden = ', 'ignore-hidden = '
        $content = $content -replace '^#after = \["autosummary"\]', 'after = ["autosummary"]'
        Write-Host "autosummary enabled ✓" -ForegroundColor Green
    }
    "off" {
        Write-Host "Disabling autosummary..." -ForegroundColor Yellow
        $content = $content -replace '^\[preprocessor\.autosummary\]', '#[preprocessor.autosummary]'
        $content = $content -replace '^index-name = ', '#index-name = '
        $content = $content -replace '^ignore-hidden = ', '#ignore-hidden = '
        $content = $content -replace '^after = \["autosummary"\]', '#after = ["autosummary"]'
        Write-Host "autosummary disabled ✓" -ForegroundColor Yellow
    }
}

$content | Set-Content $BookToml -Encoding UTF8