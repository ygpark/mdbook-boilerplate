#!/usr/bin/env python3
import sys
import re
from pathlib import Path

def number_h2_headings(file_path):
    """
    Read markdown file and add sequential numbering to headings.
    Level 2 headings (##): 1., 2., 3., ...
    Level 3 headings (###): 1.1., 1.2., 2.1., 2.2., ...
    Skip headings inside code blocks.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Patterns for level 2 and 3 headings
        h2_pattern = r'^##\s+(.*)$'
        h3_pattern = r'^###\s+(.*)$'
        lines = content.split('\n')
        h2_counter = 1
        h3_counter = 1
        in_code_block = False
        
        for i, line in enumerate(lines):
            # Check if we're entering or exiting a code block
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                continue
            
            # Skip processing if we're inside a code block
            if in_code_block:
                continue
            
            if re.match(h2_pattern, line):
                # Remove existing numbering if present
                heading_text = re.sub(r'^##\s*\d+\.\s*', '## ', line)
                # Add new numbering
                lines[i] = re.sub(r'^##\s+', f'## {h2_counter}. ', heading_text)
                h2_counter += 1
                h3_counter = 1  # Reset h3 counter for new h2 section
            
            elif re.match(h3_pattern, line):
                # Remove existing numbering if present
                heading_text = re.sub(r'^###\s*\d+\.\d+\.\s*', '### ', line)
                # Add new numbering
                lines[i] = re.sub(r'^###\s+', f'### {h2_counter-1}.{h3_counter}. ', heading_text)
                h3_counter += 1
        
        # Write back to file
        updated_content = '\n'.join(lines)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
            
        print(f"Successfully numbered {h2_counter-1} level 2 headings and level 3 headings in {file_path}")
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python number_headings.py <markdown_file>")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    
    if not file_path.exists():
        print(f"Error: File '{file_path}' does not exist")
        sys.exit(1)
    
    if not file_path.suffix.lower() in ['.md', '.markdown']:
        print(f"Warning: '{file_path}' does not appear to be a markdown file")
    
    number_h2_headings(file_path)

if __name__ == "__main__":
    main()