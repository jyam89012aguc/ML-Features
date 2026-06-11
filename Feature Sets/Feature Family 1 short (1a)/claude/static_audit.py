import ast
import collections
import hashlib
import json
import pathlib
import re

root = pathlib.Path(".")
body = collections.defaultdict(list)
shift = []
nan_series = []
pct = []

for path in root.glob("*/*.py"):
    text = path.read_text(encoding="utf-8", errors="replace")
    for lineno, line in enumerate(text.splitlines(), 1):
        if re.search(r"\.shift\(\s*-\d+", line):
            shift.append((str(path), lineno, line.strip()))
        if "pd.Series(np.nan)" in line:
            nan_series.append((str(path), lineno, line.strip()))
        if ".pct_change(" in line and "fill_method" not in line:
            pct.append((str(path), lineno, line.strip()))
    tree = ast.parse(text)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and re.match(r"^f\d+_", node.name):
            normalized = ast.FunctionDef(
                name="FN",
                args=node.args,
                body=node.body,
                decorator_list=[],
                returns=None,
                type_comment=None,
            )
            ast.fix_missing_locations(normalized)
            digest = hashlib.sha256(ast.dump(normalized, include_attributes=False).encode()).hexdigest()
            body[digest].append((str(path), node.lineno, node.name))

body_dups = [group for group in body.values() if len(group) > 1]
body_dups.sort(key=len, reverse=True)

report = {
    "shift_negative": shift,
    "pd_series_nan": nan_series,
    "pct_change_no_fill_method_count": len(pct),
    "pct_change_no_fill_method_sample": pct[:200],
    "body_dup_groups": body_dups[:500],
    "body_dup_group_count": len(body_dups),
}

out = root / "static_audit_report.json"
out.write_text(json.dumps(report, indent=2), encoding="utf-8")

print(json.dumps({
    "shift_negative": len(shift),
    "pd_series_nan": len(nan_series),
    "pct_change_no_fill_method_count": len(pct),
    "body_dup_group_count": len(body_dups),
}, indent=2))
print("largest_body_dup_groups")
for group in body_dups[:20]:
    print(len(group), " | ".join(f"{path}:{line}:{name}" for path, line, name in group[:6]))
print(f"report={out}")
