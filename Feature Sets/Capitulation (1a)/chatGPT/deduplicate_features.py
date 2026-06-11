import ast
import os
import sys
import copy

def get_logic_key(node):
    node_copy = copy.deepcopy(node)
    arg_map = {}
    for i, arg in enumerate(node_copy.args.args):
        arg_map[arg.arg] = f"arg_{i}"
        arg.arg = f"arg_{i}"
    for i, arg in enumerate(node_copy.args.posonlyargs):
        arg_map[arg.arg] = f"posarg_{i}"
        arg.arg = f"posarg_{i}"
    for i, arg in enumerate(node_copy.args.kwonlyargs):
        arg_map[arg.arg] = f"kwarg_{i}"
        arg.arg = f"kwarg_{i}"
    if node_copy.args.vararg:
        arg_map[node_copy.args.vararg.arg] = "vararg"
        node_copy.args.vararg.arg = "vararg"
    if node_copy.args.kwarg:
        arg_map[node_copy.args.kwarg.arg] = "kwarg"
        node_copy.args.kwarg.arg = "kwarg"
    for child in ast.walk(node_copy):
        if isinstance(child, ast.Name) and child.id in arg_map:
            child.id = arg_map[child.id]
    return (ast.dump(node_copy.args), "".join(ast.dump(n) for n in node_copy.body))

def deduplicate_tier(tier_files):
    if not tier_files:
        return
    
    tier_files.sort()
    all_functions = []
    file_trees = {}
    
    for file_path in tier_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            source = f.read()
        try:
            tree = ast.parse(source)
            file_trees[file_path] = (tree, source)
            for node in tree.body:
                if isinstance(node, ast.FunctionDef) and not node.name.startswith('_'):
                    all_functions.append({
                        'file': file_path,
                        'node': node,
                        'key': get_logic_key(node),
                        'name': node.name
                    })
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")

    seen_logic = {}
    to_delete_per_file = {f: set() for f in tier_files}
    any_to_delete = False
    
    for func in all_functions:
        if func['key'] in seen_logic:
            to_delete_per_file[func['file']].add(func['name'])
            any_to_delete = True
        else:
            seen_logic[func['key']] = func['name']
            
    if not any_to_delete:
        return

    for file_path in tier_files:
        names_to_delete = to_delete_per_file[file_path]
        tree, source = file_trees[file_path]
        
        print(f"Processing {file_path}: {len(names_to_delete)} duplicates to remove")
        
        functions = [n for n in tree.body if isinstance(n, ast.FunctionDef) and not n.name.startswith('_')]
        registries = []
        for node in tree.body:
            if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
                reg_id = node.targets[0].id
                if reg_id.endswith('_REGISTRY') or '_REGISTRY_' in reg_id or (reg_id.isupper() and 'REGISTRY' in reg_id):
                    registries.append(node)
                    
        lines = source.splitlines(keepends=True)
        to_remove_lines = set()
        for func in functions:
            if func.name in names_to_delete:
                for i in range(func.lineno - 1, func.end_lineno):
                    to_remove_lines.add(i)
        
        reg_blocks = []
        for reg in registries:
            reg_blocks.append(reg)
            for i in range(reg.lineno - 1, reg.end_lineno):
                to_remove_lines.add(i)

        new_source_parts = []
        for i, line in enumerate(lines):
            if i not in to_remove_lines:
                new_source_parts.append(line)
        
        for reg in reg_blocks:
            reg_name = reg.targets[0].id
            new_source_parts.append(f"\n{reg_name} = {{\n")
            dict_node = reg.value
            if isinstance(dict_node, ast.Dict):
                for key_node, val_node in zip(dict_node.keys, dict_node.values):
                    if isinstance(key_node, ast.Constant):
                        key_name = key_node.value
                    elif isinstance(key_node, (ast.Str, ast.Bytes)):
                        key_name = key_node.s
                    else: continue
                    if key_name not in names_to_delete:
                        inputs = []
                        if isinstance(val_node, ast.Dict):
                            for k, v in zip(val_node.keys, val_node.values):
                                k_val = k.value if hasattr(k, 'value') else k.s
                                if k_val == 'inputs' and isinstance(v, ast.List):
                                    for elt in v.elts:
                                        inputs.append(elt.value if hasattr(elt, 'value') else elt.s)
                        inputs_str = ", ".join([f"'{inp}'" for inp in inputs])
                        new_source_parts.append(f"    '{key_name}': {{'inputs': [{inputs_str}], 'func': {key_name}}},\n")
            new_source_parts.append("}\n")

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("".join(new_source_parts))

def process_family(family_path):
    family_files = [os.path.join(family_path, f) for f in os.listdir(family_path) if f.endswith('.py') and not f.startswith('__')]
    base_files = [f for f in family_files if 'base' in f.lower()]
    d2_files = [f for f in family_files if '2nd' in f.lower()]
    d3_files = [f for f in family_files if '3rd' in f.lower()]
    deduplicate_tier(base_files)
    deduplicate_tier(d2_files)
    deduplicate_tier(d3_files)

def main():
    root_dir = os.getcwd()
    targets = sys.argv[1:] if len(sys.argv) > 1 else [root_dir]
    
    for t in targets:
        if os.path.isfile(t):
            continue
        # Check if t is a family dir
        dirname = os.path.basename(t.rstrip(os.sep))
        if dirname[0].isdigit() or dirname == '100_listing_status_risk':
            process_family(t)
        else:
            # It's a root dir containing families
            items = sorted(os.listdir(t))
            for item in items:
                item_path = os.path.join(t, item)
                if os.path.isdir(item_path) and (item[0].isdigit() or item == '100_listing_status_risk'):
                    process_family(item_path)

if __name__ == "__main__":
    main()
