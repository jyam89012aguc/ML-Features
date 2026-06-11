import os
import re
import glob

def process_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    forbidden_operators = ['_roc(', '.diff(', '.pct_change(']
    
    # 1. Identify functions to remove
    functions_to_remove = set()
    current_func = None
    current_func_lines = []
    
    # We'll also identify helper functions like _roc that are purely wrappers
    # In these files, _roc is defined as:
    # def _roc(x, periods=1):
    #     return _s(x).pct_change(periods)
    
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('def '):
            func_name = line.split('(')[0].split('def ')[1].strip()
            
            # Read the whole function
            func_lines = [line]
            j = i + 1
            is_forbidden = False
            while j < len(lines) and (lines[j].startswith('    ') or lines[j].strip() == ''):
                func_lines.append(lines[j])
                if any(op in lines[j] for op in forbidden_operators):
                    is_forbidden = True
                j += 1
            
            # Check if it's a "purely a wrapper" helper function
            # e.g., def _roc(x, periods=1): \n return _s(x).pct_change(periods)
            if func_name.startswith('_'):
                # If it uses a forbidden operator, it's a polluted helper
                if is_forbidden:
                     functions_to_remove.add(func_name)
                     i = j
                     continue

            if is_forbidden:
                functions_to_remove.add(func_name)
                i = j
                continue
            else:
                new_lines.extend(func_lines)
                i = j
        else:
            new_lines.append(line)
            i += 1

    # 2. Identify registry and remove entries
    final_lines = []
    in_registry = False
    registry_name = None
    
    # First, let's find the registry name if any
    for line in new_lines:
        if '_REGISTRY_' in line and ' = {' in line:
            registry_name = line.split('=')[0].strip()
            break

    for line in new_lines:
        if registry_name and registry_name in line and ' = {' in line:
            in_registry = True
            final_lines.append(line)
            continue
        
        if in_registry:
            if '}' in line and ':' not in line: # End of registry
                in_registry = False
                # Ensure no trailing comma on the previous line if we want to be strict,
                # but Python is fine with it. The user asked for "no trailing commas in registries, etc."
                # which might mean if the registry becomes empty or just to avoid comma at the end of the last entry.
                if final_lines and final_lines[-1].strip().endswith(','):
                    # Clean up the last entry's comma if it's now the last one
                    # This is complex with just lines. Let's do a post-process on the registry block.
                    pass
                final_lines.append(line)
                continue
            
            should_remove_registry_entry = False
            for func in functions_to_remove:
                # Match 'func': func_name or 'func':func_name
                if re.search(fr"['\"]func['\"]\s*:\s*{func}\b", line):
                    should_remove_registry_entry = True
                    break
            
            if should_remove_registry_entry:
                continue
            else:
                final_lines.append(line)
        else:
            final_lines.append(line)

    # 3. Post-process registry to fix trailing commas and empty registries
    # (Actually, let's just make sure we don't leave a comma before the closing brace)
    content = "".join(final_lines)
    
    def fix_registry(match):
        reg_content = match.group(2)
        # Remove empty lines and fix commas
        entries = [e.strip() for e in reg_content.split('\n') if e.strip()]
        if not entries:
            return f"{match.group(1)}{{\n}}"
        
        # Rebuild registry content
        new_reg_content = ""
        for i, entry in enumerate(entries):
            entry = entry.rstrip(',')
            if i < len(entries) - 1:
                new_reg_content += f"    {entry},\n"
            else:
                new_reg_content += f"    {entry}\n"
        return f"{match.group(1)}{{\n{new_reg_content}}}"

    if registry_name:
        content = re.sub(fr"({registry_name}\s*=\s*)\{{(.*?)\}}", fix_registry, content, flags=re.DOTALL)

    # Cleanup multiple newlines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    return functions_to_remove

def main():
    base_files = glob.glob('**/[0-9]*_base_*.py', recursive=True)
    print(f"Found {len(base_files)} base files.")
    total_removed = 0
    for f in base_files:
        removed = process_file(f)
        if removed:
            print(f"Processed {f}: removed {len(removed)} functions: {', '.join(removed)}")
            total_removed += len(removed)
    print(f"Total functions removed: {total_removed}")

if __name__ == "__main__":
    main()
