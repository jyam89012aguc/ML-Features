"""Helper: produce a new SPEC list referencing functions directly."""
import re, sys

path = sys.argv[1]
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Extract current SPEC entries: list of (short_name, args_tag) preserving order
m = re.search(r'_SPEC = \[\n(.*?)\n\]', text, flags=re.S)
spec_block = m.group(1)
entries = re.findall(r'\("(\w+)", (\w+)\),', spec_block)
print(f"# entries: {len(entries)}", file=sys.stderr)

# Build mapping short_name -> full func name
funcs = re.findall(r'^def (f28pd_\w+)\(', text, flags=re.M)
prefix = "f28pd_f28_price_volume_divergence_"
func_by_short = {fn[len(prefix):]: fn for fn in funcs}

# Generate new SPEC list lines
out = []
for short, tag in entries:
    full = func_by_short[short]
    out.append(f"    ({full}, {tag}),")
new_spec_body = "\n".join(out)
print(new_spec_body)
