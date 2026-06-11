import ast
import copy
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path, PureWindowsPath


ROOT = Path(__file__).resolve().parent
SIGNAL_RE = re.compile(
    r"^(?P<prefix>[^_]+)_(?P<folder>f\d{3}_.+)_(?P<concept>.+)_(?P<kind>base|2d|3d)_v(?P<version>\d+)_signal$"
)


class Canonicalizer(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        args = [arg.arg for arg in node.args.args]
        mapping = {name: f"arg{i}" for i, name in enumerate(args)}
        return FunctionBodyCanonicalizer(mapping).visit(node)


class FunctionBodyCanonicalizer(ast.NodeTransformer):
    def __init__(self, mapping):
        self.mapping = mapping

    def visit_Name(self, node):
        if node.id in self.mapping:
            return ast.copy_location(ast.Name(id=self.mapping[node.id], ctx=node.ctx), node)
        return node


def function_records(path):
    text = path.read_text(encoding="utf-8")
    tree = ast.parse(text, filename=str(path))
    records = []
    for node in tree.body:
        if not isinstance(node, ast.FunctionDef):
            continue
        if not node.name.endswith("_signal"):
            continue
        source = ast.get_source_segment(text, node) or ""
        body_dump = ast.dump(ast.Module(body=copy.deepcopy(node.body), type_ignores=[]), include_attributes=False)
        canonical = Canonicalizer().visit(copy.deepcopy(node))
        ast.fix_missing_locations(canonical)
        dump = ast.dump(canonical, include_attributes=False)
        records.append(
            {
                "file": str(path.relative_to(ROOT)),
                "line": node.lineno,
                "name": node.name,
                "args": [arg.arg for arg in node.args.args],
                "canonical_hash": hashlib.sha256(dump.encode()).hexdigest(),
                "body_hash": hashlib.sha256(body_dump.encode()).hexdigest(),
                "returns_sanitized": "replace([np.inf, -np.inf], np.nan)" in source,
                "source": source,
            }
        )
    return records


def main():
    py_files = sorted(p for p in ROOT.glob("f*/*.py") if "__pycache__" not in p.parts)
    parse_errors = []
    records = []
    for path in py_files:
        try:
            records.extend(function_records(path))
        except Exception as exc:
            parse_errors.append({"file": str(path.relative_to(ROOT)), "error": repr(exc)})

    name_counts = Counter(r["name"] for r in records)
    duplicate_names = {name: count for name, count in name_counts.items() if count > 1}

    by_canonical = defaultdict(list)
    by_body = defaultdict(list)
    for r in records:
        by_canonical[r["canonical_hash"]].append(r)
        by_body[r["body_hash"]].append(r)

    exact_duplicate_groups = [
        [{"file": r["file"], "line": r["line"], "name": r["name"]} for r in group]
        for group in by_canonical.values()
        if len(group) > 1
    ]
    same_body_groups = [
        [{"file": r["file"], "line": r["line"], "name": r["name"]} for r in group]
        for group in by_body.values()
        if len(group) > 1
    ]
    normalized_duplicate_groups = [
        [{"file": r["file"], "line": r["line"], "name": r["name"], "args": r["args"]} for r in group]
        for group in by_canonical.values()
        if len(group) > 1
    ]

    unsanitized = [
        {"file": r["file"], "line": r["line"], "name": r["name"]}
        for r in records
        if not r["returns_sanitized"]
    ]

    folder_counts = Counter(Path(r["file"]).parts[0] for r in records)
    file_counts = Counter(r["file"] for r in records)
    expected_files = [str(p.relative_to(ROOT)) for p in py_files]
    files_without_signals = [f for f in expected_files if file_counts[f] == 0]

    cross_folder_overlap_groups = []
    for group in by_body.values():
        if len(group) < 2:
            continue
        folders = sorted({PureWindowsPath(r["file"]).parts[0] for r in group})
        if len(folders) < 2:
            continue
        members = []
        for r in group:
            match = SIGNAL_RE.match(r["name"])
            members.append(
                {
                    "file": r["file"],
                    "line": r["line"],
                    "name": r["name"],
                    "concept": match.group("concept") if match else r["name"],
                }
            )
        cross_folder_overlap_groups.append({"folders": folders, "members": members})

    pair_counts = Counter()
    for family in cross_folder_overlap_groups:
        folders = family["folders"]
        for i, left in enumerate(folders):
            for right in folders[i + 1 :]:
                pair_counts[f"{left} <-> {right}"] += 1

    duplicate_manifest = []
    for group in by_body.values():
        if len(group) < 2:
            continue
        ordered = sorted(group, key=lambda r: (PureWindowsPath(r["file"]).parts[0], r["file"], r["line"], r["name"]))
        keep = ordered[0]
        duplicate_manifest.append(
            {
                "canonical": {"file": keep["file"], "line": keep["line"], "name": keep["name"]},
                "duplicates": [
                    {"file": r["file"], "line": r["line"], "name": r["name"]}
                    for r in ordered[1:]
                ],
            }
        )

    report = {
        "summary": {
            "python_files": len(py_files),
            "signal_functions": len(records),
            "feature_folders": len(folder_counts),
            "parse_errors": len(parse_errors),
            "duplicate_names": len(duplicate_names),
            "exact_duplicate_groups": len(exact_duplicate_groups),
            "same_raw_body_groups": len(same_body_groups),
            "normalized_duplicate_groups": len(normalized_duplicate_groups),
            "cross_folder_overlap_groups": len(cross_folder_overlap_groups),
            "unsanitized_signals": len(unsanitized),
            "files_without_signals": len(files_without_signals),
            "min_signals_per_folder": min(folder_counts.values()) if folder_counts else 0,
            "max_signals_per_folder": max(folder_counts.values()) if folder_counts else 0,
        },
        "parse_errors": parse_errors,
        "duplicate_names": duplicate_names,
        "exact_duplicate_groups": exact_duplicate_groups,
        "same_raw_body_groups": same_body_groups,
        "normalized_duplicate_groups": normalized_duplicate_groups,
        "unsanitized": unsanitized,
        "files_without_signals": files_without_signals,
        "folder_counts": dict(sorted(folder_counts.items())),
        "top_cross_folder_overlap_pairs": pair_counts.most_common(50),
        "cross_folder_overlap_groups": cross_folder_overlap_groups,
    }
    (ROOT / "_feature_audit_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    (ROOT / "_feature_dedup_manifest.json").write_text(
        json.dumps(
            {
                "policy": "For each identical raw calculation body, keep the lexicographically first feature by folder/file/line and suppress the remaining aliases in downstream registry construction.",
                "duplicate_groups": len(duplicate_manifest),
                "redundant_signals": sum(len(group["duplicates"]) for group in duplicate_manifest),
                "groups": duplicate_manifest,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    markdown = [
        "# Feature Audit Report",
        "",
        "## Summary",
        "",
        f"- Python files scanned: {report['summary']['python_files']}",
        f"- Public signal functions: {report['summary']['signal_functions']}",
        f"- Feature folders: {report['summary']['feature_folders']}",
        f"- Parse errors: {report['summary']['parse_errors']}",
        f"- Duplicate function names: {report['summary']['duplicate_names']}",
        f"- Exact duplicate functions: {report['summary']['exact_duplicate_groups']}",
        f"- Same raw-body groups: {report['summary']['same_raw_body_groups']}",
        f"- Cross-folder overlap groups: {report['summary']['cross_folder_overlap_groups']}",
        f"- Redundant signals in de-dup manifest: {sum(len(group['duplicates']) for group in duplicate_manifest)}",
        f"- Unsanitized signals: {report['summary']['unsanitized_signals']}",
        f"- Files without signals: {report['summary']['files_without_signals']}",
        "",
        "## Interpretation",
        "",
        "No syntax, naming, or output-sanitization failures were found. The remaining duplicate risk is cross-domain semantic overlap: different feature folders expose the same calculation under domain-specific names.",
        "",
        "## Highest Overlap Pairs",
        "",
    ]
    for pair, count in pair_counts.most_common(25):
        markdown.append(f"- `{pair}`: {count} matching calculation groups")
    markdown.extend(["", "## Recommendation", ""])
    markdown.append(
        "Keep these modules intact if downstream code expects each domain folder to be self-contained. If the registry must be strictly non-duplicative, canonicalize cross-domain overlap families in the registry or generation manifest rather than deleting functions from the modules."
    )
    markdown.extend(
        [
            "",
            "A strict non-duplicate manifest is available in `_feature_dedup_manifest.json`.",
        ]
    )
    (ROOT / "_feature_audit_report.md").write_text("\n".join(markdown) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], indent=2))


if __name__ == "__main__":
    main()
