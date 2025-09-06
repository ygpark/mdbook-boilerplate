#!/bin/bash

# autosummary 토글 스크립트
# Usage: ./scripts/toggle-autosummary.sh [on|off]

BOOK_TOML="book.toml"

if [ ! -f "$BOOK_TOML" ]; then
    echo "Error: book.toml not found!"
    exit 1
fi

case "$1" in
    "on")
        echo "Enabling autosummary..."
        sed -i.bak 's/^#\[preprocessor\.autosummary\]/[preprocessor.autosummary]/' "$BOOK_TOML"
        sed -i.bak 's/^#index-name = /index-name = /' "$BOOK_TOML"
        sed -i.bak 's/^#ignore-hidden = /ignore-hidden = /' "$BOOK_TOML"
        sed -i.bak 's/^#after = \["autosummary"\]/after = ["autosummary"]/' "$BOOK_TOML"
        echo "autosummary enabled ✓"
        ;;
    "off")
        echo "Disabling autosummary..."
        sed -i.bak 's/^\[preprocessor\.autosummary\]/#[preprocessor.autosummary]/' "$BOOK_TOML"
        sed -i.bak 's/^index-name = /#index-name = /' "$BOOK_TOML"
        sed -i.bak 's/^ignore-hidden = /#ignore-hidden = /' "$BOOK_TOML"
        sed -i.bak 's/^after = \["autosummary"\]/#after = ["autosummary"]/' "$BOOK_TOML"
        echo "autosummary disabled ✓"
        ;;
    *)
        echo "Usage: $0 [on|off]"
        echo "Current status:"
        if grep -q "^#\[preprocessor\.autosummary\]" "$BOOK_TOML"; then
            echo "  autosummary is OFF"
        else
            echo "  autosummary is ON"
        fi
        exit 1
        ;;
esac

# 백업 파일 정리
rm -f "${BOOK_TOML}.bak"