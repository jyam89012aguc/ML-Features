import sys
import re
import os

def compress_python_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    new_lines = []
    in_docstring = False
    
    for line in lines:
        stripped = line.strip()
        
        # Keep imports and helpers as is
        if stripped.startswith('import ') or stripped.startswith('from '):
            new_lines.append(line)
            continue
            
        if stripped.startswith('def _'):
            new_lines.append(line)
            continue

        # Handle docstrings for signal functions
        if '"""' in line:
            if stripped.startswith('"""') and stripped.endswith('"""') and len(stripped) > 6:
                # Single line docstring - shorten it
                content = stripped.strip('" ')
                new_lines.append(line.split('"""')[0] + '"""' + content.split('\n')[0] + '"""\n')
                continue
            elif not in_docstring:
                in_docstring = True
                doc_start = line.split('"""')[0]
                new_lines.append(doc_start + '"""Shortened docstring."""\n')
                continue
            else:
                in_docstring = False
                continue
        
        if in_docstring:
            continue

        # Remove comments that start with # Step
        if stripped.startswith('# Step'):
            continue
            
        # Remove empty lines if multiple
        if not stripped and new_lines and not new_lines[-1].strip():
            continue
            
        new_lines.append(line)

    with open(file_path, 'w') as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    for path in sys.argv[1:]:
        if os.path.exists(path):
            print(f"Compressing {path}...")
            compress_python_file(path)
            print(f"New size: {os.path.getsize(path)} bytes")
