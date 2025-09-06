#!/usr/bin/env python3
"""
autosummary 토글 Python 스크립트
Usage: python scripts/toggle-autosummary.py [on|off|status]
"""

import sys
import re
from pathlib import Path


class AutosummaryToggler:
    def __init__(self, book_toml_path="book.toml"):
        self.book_toml_path = Path(book_toml_path)
        
    def read_config(self):
        if not self.book_toml_path.exists():
            raise FileNotFoundError(f"Error: {self.book_toml_path} not found!")
        return self.book_toml_path.read_text(encoding='utf-8')
    
    def write_config(self, content):
        self.book_toml_path.write_text(content, encoding='utf-8')
    
    def enable_autosummary(self):
        print("Enabling autosummary...")
        content = self.read_config()
        
        # Enable autosummary preprocessor
        content = re.sub(r'^#\[preprocessor\.autosummary\]', '[preprocessor.autosummary]', content, flags=re.MULTILINE)
        content = re.sub(r'^#index-name = ', 'index-name = ', content, flags=re.MULTILINE)
        content = re.sub(r'^#ignore-hidden = ', 'ignore-hidden = ', content, flags=re.MULTILINE)
        content = re.sub(r'^#after = \["autosummary"\]', 'after = ["autosummary"]', content, flags=re.MULTILINE)
        
        self.write_config(content)
        print("autosummary enabled ✓")
    
    def disable_autosummary(self):
        print("Disabling autosummary...")
        content = self.read_config()
        
        # Disable autosummary preprocessor
        content = re.sub(r'^\[preprocessor\.autosummary\]', '#[preprocessor.autosummary]', content, flags=re.MULTILINE)
        content = re.sub(r'^index-name = ', '#index-name = ', content, flags=re.MULTILINE)
        content = re.sub(r'^ignore-hidden = ', '#ignore-hidden = ', content, flags=re.MULTILINE)
        content = re.sub(r'^after = \["autosummary"\]', '#after = ["autosummary"]', content, flags=re.MULTILINE)
        
        self.write_config(content)
        print("autosummary disabled ✓")
    
    def get_status(self):
        content = self.read_config()
        if re.search(r'^#\[preprocessor\.autosummary\]', content, flags=re.MULTILINE):
            return "OFF"
        else:
            return "ON"
    
    def show_status(self):
        status = self.get_status()
        print(f"Current status:")
        print(f"  autosummary is {status}")


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ["on", "off", "status"]:
        print("Usage: python scripts/toggle-autosummary.py [on|off|status]")
        toggler = AutosummaryToggler()
        try:
            toggler.show_status()
        except FileNotFoundError as e:
            print(e)
        sys.exit(1)
    
    action = sys.argv[1]
    toggler = AutosummaryToggler()
    
    try:
        if action == "on":
            toggler.enable_autosummary()
        elif action == "off":
            toggler.disable_autosummary()
        elif action == "status":
            toggler.show_status()
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()