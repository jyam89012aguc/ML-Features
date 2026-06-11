from __future__ import annotations

import importlib
import os
import re
import sys
from pathlib import Path


TARGET = Path(r"C:\Users\jyama\Desktop\active_non audited features per AI\Capitulation Feature Build SEP 01-59")
sys.path.insert(0, str(TARGET))


D2_MARKER = "Base-universe derivative extensions for repaired first-base features"
D3_MARKER = "Third-derivative extensions for repaired first-base features"


def clean_ident(value: str) -> str:
    value = re.sub(r"\W+", "_", value)
    if value and value[0].isdigit():
        value = "_" + value
    return value


def family_prefix(feature_names: list[str]) -> str:
    for name in feature_names:
        match = re.match(r"([a-z]+)_", name)
        if match:
            return match.group(1)
    raise ValueError("could not infer feature prefix")


def registries(module) -> list[dict]:
    return [v for k, v in module.__dict__.items() if "REGISTRY" in k and isinstance(v, dict)]


def base_features(family: str) -> list[str]:
    base_file = next((TARGET / family).glob("*base_001_075.py"))
    module = importlib.import_module(f"{family}.{base_file.stem}")
    merged = {}
    for registry in registries(module):
        merged.update(registry)
    return list(merged.keys())


def derivative_inputs(family: str, kind: str) -> set[str]:
    suffix = "2nd_derivatives.py" if kind == "d2" else "3rd_derivatives.py"
    path = next((TARGET / family).glob(f"*{suffix}"))
    module = importlib.import_module(f"{family}.{path.stem}")
    inputs: set[str] = set()
    for registry in registries(module):
        for info in registry.values():
            for inp in info.get("inputs", []):
                inputs.add(inp)
    return inputs


def append_d2(path: Path, prefix: str, missing_base: list[str]) -> list[str]:
    text = path.read_text(encoding="utf-8")
    if D2_MARKER in text:
        return []
    if not missing_base:
        return []

    registry = f"{prefix.upper()}_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY"
    d2_names = []
    lines = [
        f"\n\n# {D2_MARKER}.\n",
        f"{registry} = {{}}\n",
        "\n\ndef _base_universe_d2(feature, idx):\n",
        "    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)\n",
        "    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]\n",
        "    lag = windows[idx % len(windows)]\n",
        "    smooth = windows[(idx * 3 + 1) % len(windows)]\n",
        "    delta = feature.diff(lag)\n",
        "    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()\n",
        "    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))\n",
        "    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)\n",
    ]

    for idx, base in enumerate(missing_base, start=1):
        d2_name = f"{prefix}_base_universe_d2_{idx:03d}_{clean_ident(base)}"
        d2_names.append(d2_name)
        lines.append(f"\n\ndef {d2_name}({base}):\n    return _base_universe_d2({base}, {idx})\n")
        lines.append(f"{registry}['{d2_name}'] = {{'inputs': ['{base}'], 'func': {d2_name}}}\n")

    path.write_text(text.rstrip() + "\n" + "".join(lines), encoding="utf-8")
    return d2_names


def append_d3(path: Path, prefix: str, d2_names: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    if D3_MARKER in text:
        return
    if not d2_names:
        return

    registry = f"{prefix.upper()}_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY"
    lines = [
        f"\n\n# {D3_MARKER}.\n",
        f"{registry} = {{}}\n",
        "\n\ndef _base_universe_d3(feature, idx):\n",
        "    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)\n",
        "    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]\n",
        "    lag = windows[(idx * 2) % len(windows)]\n",
        "    smooth = windows[(idx * 5 + 2) % len(windows)]\n",
        "    accel = feature.diff(lag)\n",
        "    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()\n",
        "    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))\n",
        "    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)\n",
    ]

    for idx, d2_name in enumerate(d2_names, start=1):
        d3_name = d2_name.replace("_d2_", "_d3_", 1)
        if d3_name == d2_name:
            d3_name = f"{prefix}_base_universe_d3_{idx:03d}_{clean_ident(d2_name)}"
        lines.append(f"\n\ndef {d3_name}({d2_name}):\n    return _base_universe_d3({d2_name}, {idx})\n")
        lines.append(f"{registry}['{d3_name}'] = {{'inputs': ['{d2_name}'], 'func': {d3_name}}}\n")

    path.write_text(text.rstrip() + "\n" + "".join(lines), encoding="utf-8")


def main() -> None:
    changed_d2 = 0
    changed_d3 = 0
    added_d2 = 0
    added_d3 = 0

    for family in sorted(d for d in os.listdir(TARGET) if (TARGET / d).is_dir() and d[0].isdigit()):
        bases = base_features(family)
        prefix = family_prefix(bases)
        existing_d2_inputs = derivative_inputs(family, "d2")
        missing = [name for name in bases if name not in existing_d2_inputs]

        d2_path = next((TARGET / family).glob("*2nd_derivatives.py"))
        d3_path = next((TARGET / family).glob("*3rd_derivatives.py"))
        d2_names = append_d2(d2_path, prefix, missing)
        if d2_names:
            changed_d2 += 1
            added_d2 += len(d2_names)
            append_d3(d3_path, prefix, d2_names)
            changed_d3 += 1
            added_d3 += len(d2_names)
            print(f"{family}: added {len(d2_names)} d2 + {len(d2_names)} d3 repaired-base derivatives")

    print(f"changed_d2_files={changed_d2} added_d2={added_d2} changed_d3_files={changed_d3} added_d3={added_d3}")


if __name__ == "__main__":
    main()
