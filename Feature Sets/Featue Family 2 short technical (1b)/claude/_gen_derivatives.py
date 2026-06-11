"""Generate d1/d2/d3 sibling files from a base feature file by AST rewriting.

Usage:
    python _gen_derivatives.py <family_dir> <abbrev> <chunk_001_075|076_150>

For each feature function `{abbrev}_NNN_name` in the base file we:
  - copy the function
  - rename to `{abbrev}_NNN_name_d{1,2,3}`
  - wrap the value of the outermost Return statement with .diff() applied 1/2/3 times

Preamble (imports + private helpers) is copied verbatim from the base file. Registry
dicts are rebuilt with the renamed function refs.
"""
from __future__ import annotations

import ast
import re
import sys
from pathlib import Path


def split_preamble_and_features(tree, abbrev):
    feat_pat = re.compile(rf"{re.escape(abbrev)}_\d{{3}}_")
    preamble = []
    feats = []
    registries = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and feat_pat.search(node.name):
            feats.append(node)
        elif isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and "REGISTRY" in t.id for t in node.targets
        ):
            registries.append(node)
        else:
            preamble.append(node)
    return preamble, feats, registries


def wrap_return_with_diff(fn, n_diff):
    fn = ast.parse(ast.unparse(fn)).body[0]
    last_ret_idx = None
    for i, stmt in enumerate(fn.body):
        if isinstance(stmt, ast.Return):
            last_ret_idx = i
    if last_ret_idx is None:
        raise ValueError(f"function {fn.name} has no top-level Return")
    ret = fn.body[last_ret_idx]
    val = ret.value
    for _ in range(n_diff):
        val = ast.Call(
            func=ast.Attribute(value=val, attr="diff", ctx=ast.Load()),
            args=[],
            keywords=[],
        )
    ret.value = val
    return fn


def build_registry_assign(orig_assign, abbrev, suffix, order_tag):
    new_assign = ast.parse(ast.unparse(orig_assign)).body[0]
    for t in new_assign.targets:
        if isinstance(t, ast.Name):
            t.id = t.id.replace("_BASE_REGISTRY_", f"_{order_tag}_REGISTRY_")
    dct = new_assign.value
    new_keys = []
    new_values = []
    feat_key_pat = re.compile(rf"{re.escape(abbrev)}_\d{{3}}_")
    for k, v in zip(dct.keys, dct.values):
        if isinstance(k, ast.Constant) and isinstance(k.value, str) and feat_key_pat.search(k.value):
            new_keys.append(ast.Constant(value=k.value + suffix))
            new_inner_keys = []
            new_inner_values = []
            for ik, iv in zip(v.keys, v.values):
                if isinstance(ik, ast.Constant) and ik.value == "func" and isinstance(iv, ast.Name):
                    new_inner_keys.append(ik)
                    new_inner_values.append(ast.Name(id=iv.id + suffix, ctx=ast.Load()))
                else:
                    new_inner_keys.append(ik)
                    new_inner_values.append(iv)
            new_values.append(ast.Dict(keys=new_inner_keys, values=new_inner_values))
        else:
            new_keys.append(k)
            new_values.append(v)
    new_assign.value = ast.Dict(keys=new_keys, values=new_values)
    return new_assign


def generate(family_dir, abbrev, chunk):
    base_path = family_dir / f"{family_dir.name}__base__{chunk}.py"
    src = base_path.read_text(encoding="utf-8")
    tree = ast.parse(src)
    preamble, feats, registries = split_preamble_and_features(tree, abbrev)
    assert len(registries) == 1, f"expected exactly one registry in {base_path}, got {len(registries)}"

    for n_diff, tag, suffix in [(1, "D1", "_d1"), (2, "D2", "_d2"), (3, "D3", "_d3")]:
        out_path = family_dir / f"{family_dir.name}__{tag.lower()}__{chunk}.py"
        new_feats = [wrap_return_with_diff(fn, n_diff) for fn in feats]
        for fn in new_feats:
            fn.name = fn.name + suffix
        new_registry = build_registry_assign(registries[0], abbrev, suffix, tag)

        new_preamble = list(preamble)
        if new_preamble and isinstance(new_preamble[0], ast.Expr) and isinstance(new_preamble[0].value, ast.Constant):
            doc = (
                f"{family_dir.name} {tag.lower()} features {chunk.replace('_', '-')} — "
                f"order-{n_diff} difference of corresponding base features.\n\n"
                f"Each function inlines the base body and wraps the return value with "
                f"{'.diff()' * n_diff}. Self-contained; helpers redefined locally per HANDOFF."
            )
            new_preamble[0] = ast.Expr(value=ast.Constant(value=doc))

        new_module = ast.Module(body=new_preamble + new_feats + [new_registry], type_ignores=[])
        ast.fix_missing_locations(new_module)
        out_src = ast.unparse(new_module)
        out_path.write_text(out_src, encoding="utf-8")
        print(f"wrote {out_path.name} ({len(out_src)} bytes, {len(new_feats)} feats)")


if __name__ == "__main__":
    family_dir = Path(sys.argv[1])
    abbrev = sys.argv[2]
    chunk = sys.argv[3]
    generate(family_dir, abbrev, chunk)
