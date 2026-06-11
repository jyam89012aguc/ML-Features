import ast
import os

def deduplicate_file(file_path):
    with open(file_path, 'r') as f:
        source = f.read()
    
    tree = ast.parse(source)
    
    functions = []
    registries = []
    other_nodes = []
    
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            if not node.name.startswith('_'):
                functions.append(node)
            else:
                other_nodes.append(node)
        elif isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name) and (node.targets[0].id.endswith('_REGISTRY') or '_REGISTRY_' in node.targets[0].id):
            registries.append(node)
        else:
            other_nodes.append(node)

    if not functions:
        return # Nothing to do
    
    # Group functions by logic
    def get_logic_key(node):
        # Args + Body
        return (ast.dump(node.args), "".join(ast.dump(n) for n in node.body))

    seen_logic = {}
    to_delete = set()
    master_map = {} # duplicate_name -> master_name

    for func in functions:
        key = get_logic_key(func)
        if key in seen_logic:
            to_delete.add(func.name)
            master_map[func.name] = seen_logic[key]
        else:
            seen_logic[key] = func.name

    if not to_delete:
        print(f"No duplicates found in {file_path}")
        return

    print(f"Found {len(to_delete)} duplicates in {file_path}")

    # Now we need to remove them from the source.
    # We'll rebuild the file content.
    # 1. Keep imports and helper functions.
    # 2. Keep master functions.
    # 3. Update registries.
    
    # To preserve formatting as much as possible, let's use a more surgical approach.
    # But for 100 families, maybe a clean rewrite is okay if it's syntactically correct.
    # Actually, the user says "Keep ONLY the first occurrence and delete the redundant slots".
    
    # Let's try to find the line ranges of functions to delete.
    lines = source.splitlines()
    new_lines = []
    
    # We'll use a simple approach:
    # 1. Iterate through nodes.
    # 2. If it's a FunctionDef to delete, skip it.
    # 3. If it's a registry, filter its entries.
    
    # Wait, ast nodes have lineno and end_lineno.
    
    segments_to_keep = []
    last_pos = 0
    
    # Sort nodes by position
    all_nodes = sorted(tree.body, key=lambda n: n.lineno)
    
    new_source = ""
    
    # This is tricky because we want to modify the registry Dict node.
    # Let's just use ast.unparse if available, or rebuild the registry manually.
    
    # Let's try a different approach:
    # Identify function names to keep.
    keep_names = [f.name for f in functions if f.name not in to_delete]
    
    # Rewrite the file:
    # - Helper functions (start with _)
    # - Masters
    # - Updated Registry
    
    import astunparse # If available, but let's assume it's not and use ast.unparse (Py 3.9+)
    
    # Check Python version
    import sys
    can_unparse = hasattr(ast, 'unparse')

    # If I can't use unparse, I'll have to be more clever.
    # Let's use string manipulation for the registry.
    
    final_source_parts = []
    
    # Get all lines
    lines = source.splitlines(keepends=True)
    
    # Mark lines to remove
    to_remove_lines = set()
    for func in functions:
        if func.name in to_delete:
            for i in range(func.lineno - 1, func.end_lineno):
                to_remove_lines.add(i)
    
    # Handle registry
    for reg in registries:
        # A registry is an Assign(targets=[Name(id=...)], value=Dict(keys=[Constant(value=...)], values=[Dict(...)]))
        # The structure is: 'name': {'inputs': [...], 'func': name}
        # We want to remove entries where key is in to_delete.
        
        # Mark registry lines for replacement
        for i in range(reg.lineno - 1, reg.end_lineno):
            to_remove_lines.add(i)
            
    # Now build the file
    for i, line in enumerate(lines):
        if i not in to_remove_lines:
            final_source_parts.append(line)
            
    # Add back the updated registries at the end
    for reg in registries:
        reg_name = reg.targets[0].id
        new_reg_lines = [f"{reg_name} = {{\n"]
        
        # Original entries
        dict_node = reg.value
        for key_node, val_node in zip(dict_node.keys, dict_node.values):
            key_name = key_node.value if hasattr(key_node, 'value') else key_node.s
            if key_name not in to_delete:
                # We want to keep the original text of the value if possible, 
                # but it's simpler to just reconstruct it.
                # Entries look like: 'name': {'inputs': ['close'], 'func': name}
                
                # Get inputs from val_node
                inputs = []
                for k, v in zip(val_node.keys, val_node.values):
                    if (hasattr(k, 'value') and k.value == 'inputs') or (hasattr(k, 's') and k.s == 'inputs'):
                        if isinstance(v, ast.List):
                            inputs = [elt.value if hasattr(elt, 'value') else elt.s for elt in v.elts]
                
                inputs_str = ", ".join([f"'{inp}'" for inp in inputs])
                new_reg_lines.append(f"    '{key_name}': {{'inputs': [{inputs_str}], 'func': {key_name}}},\n")
        
        new_reg_lines.append("}\n")
        final_source_parts.extend(new_reg_lines)
        
    new_source = "".join(final_source_parts)
    
    with open(file_path, 'w') as f:
        f.write(new_source)
    print(f"Successfully deduplicated {file_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        deduplicate_file(sys.argv[1])
