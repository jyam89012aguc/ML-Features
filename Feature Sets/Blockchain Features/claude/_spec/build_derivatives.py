"""
Authoring tool (NOT one of the 4 output files).

Reads a family's two base files (base_001_075 + base_076_150) and emits the two
derivative files with FULLY-EXPANDED, literal `def` blocks:
  - {FAM}_2nd_derivatives_001_150_claude.py   (slope  = 1st math derivative of base)
  - {FAM}_3rd_derivatives_001_150_claude.py   (jerk   = 2nd math derivative of base)

Each derivative function inlines its base computation, then applies a window-
appropriate discrete derivative. The OUTPUT files contain no generators, no
_core(), no importlib/exec/globals/setattr, no formula-list indexing -- every
function is a literal expanded def. This script merely authors that text.

Usage:
    python build_derivatives.py <family_folder>
e.g. python build_derivatives.py "D:/Features/claude/f01_crypto_beta_momentum"
"""
import importlib.util
import inspect
import os
import re
import sys


# ---- synthetic series generators for the self-test (universal across families) ----
SYNTH = r'''
def _synth_cols(names):
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    closeadj = pd.Series(base_price, name="closeadj")
    noise_h = np.abs(np.random.normal(0, 0.02, n))
    noise_l = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open", "high", "low", "close", "closeadj", "price", "volume",
           "vwap", "marketcap", "ev", "assets", "assetsc", "assetsnc", "equity",
           "revenue", "revenueusd", "gp", "ebitda", "ebit", "ppnenet", "sharesbas",
           "shareswa", "cashneq", "cor", "opex", "sgna", "rnd", "inventory",
           "receivables", "payables", "intangibles", "evebitda", "evebit",
           "pe", "pb", "ps", "currentratio", "bvps", "sps", "divyield", "dps",
           "shrvalue", "shrunits", "totalvalue", "percentoftotal", "value",
           "units", "shares", "sf3a_shares", "sf3a_value", "sf3b_shares",
           "sf3b_value", "grossmargin", "ebitdamargin", "netmargin", "roe",
           "roa", "roic", "deposits", "invcap",
           "sector_index", "bellwether_coin", "bellwether_mstr", "nholders",
           "newholders", "exitholders", "hhi", "totalunits", "avgposition",
           "buyval", "sellval", "buyshares", "sellshares", "buycount", "sellcount",
           "officerbuyval", "dirbuyval", "tenpctbuyval", "officerbuycount",
           "optionexval", "tenpctsellval", "receivables", "workingcapital"}
    for nm in names:
        if nm == "closeadj" or nm == "close" or nm == "price":
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price * (1 + np.random.normal(0, 0.01, n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price * (1 + noise_h), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price * (1 - noise_l), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            series = level + 50.0 * walk
            if nm in POS:
                series = np.abs(series) + 10.0
            out[nm] = pd.Series(series, name=nm)
    return out
'''

SLOPE_HELPERS = '''
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)
'''


def _load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _preamble(base_src):
    marker = "# ============ FEATURES"
    idx = base_src.index(marker)
    return base_src[:idx].rstrip() + "\n"


def _max_window(fn_name):
    nums = [int(x) for x in re.findall(r"_(\d+)d", fn_name)]
    if not nums:
        nums = [int(x) for x in re.findall(r"(\d+)", fn_name.split("_v")[0])]
    return max(nums) if nums else 21


def _slope_window(bw):
    if bw <= 5:
        return 5
    if bw <= 21:
        return 5
    if bw <= 63:
        return 21
    if bw <= 189:
        return 21
    return 63


def _body_lines(fn):
    src = inspect.getsource(fn)
    lines = src.split("\n")
    # drop the def line (first non-empty) and the trailing return line
    start = 0
    while not lines[start].lstrip().startswith("def "):
        start += 1
    body = lines[start + 1:]
    # strip trailing empties
    while body and body[-1].strip() == "":
        body.pop()
    assert body[-1].lstrip().startswith("return "), fn.__name__
    body = body[:-1]
    return body


def _emit(fn, kind):
    # kind in {"slope","jerk"}
    name = fn.__name__
    params = ", ".join(p.name for p in inspect.signature(fn).parameters.values())
    bw = _max_window(name)
    w = _slope_window(bw)
    new_name = name.replace("_base_v", "_%s_v" % kind)
    body = _body_lines(fn)
    lines = ["def %s(%s):" % (new_name, params)]
    lines.extend(body)
    if kind == "slope":
        lines.append("    result = _slope_norm(result, %d)" % w)
    else:
        lines.append("    result = _slope_norm(_slope_norm(result, %d), %d)" % (w, w))
    lines.append("    return result.replace([np.inf, -np.inf], np.nan)")
    return new_name, "\n".join(lines)


def build(folder):
    folder = folder.rstrip("/\\")
    fam = os.path.basename(folder)            # e.g. f01_crypto_beta_momentum
    files = sorted(os.listdir(folder))
    b1 = [f for f in files if f.endswith("_base_001_075_claude.py")][0]
    b2 = [f for f in files if f.endswith("_base_076_150_claude.py")][0]
    m1 = _load_module(os.path.join(folder, b1), fam + "_b1")
    m2 = _load_module(os.path.join(folder, b2), fam + "_b2")
    base_src = open(os.path.join(folder, b1), encoding="utf-8").read()
    pre = _preamble(base_src)

    feats = list(m1._FEATURES) + list(m2._FEATURES)
    assert len(feats) == 150, "expected 150 base feats, got %d" % len(feats)

    prims = tuple(re.findall(r"def (_%s[a-z0-9_]*?)\(" % fam[:3], base_src))
    # domain primitives are the _fNN_* helpers
    prim_names = tuple(re.findall(r"def (_f\d\d_[a-z0-9_]+)\(", base_src))
    prim_tuple = repr(prim_names)

    reg_const = fam.upper()

    for kind, suffix, reg in (
        ("slope", "2nd_derivatives", "SLOPE"),
        ("jerk", "3rd_derivatives", "JERK"),
    ):
        defs = []
        names = []
        for fn in feats:
            nm, code = _emit(fn, kind)
            names.append(nm)
            defs.append(code)
        out = []
        out.append(pre.rstrip() + "\n")
        out.append(SLOPE_HELPERS.strip() + "\n")
        out.append("\n# ============ %s FEATURES 001-150 ============\n" % kind.upper())
        out.append("\n\n".join(defs) + "\n")
        out.append("\n_FEATURES = [")
        for nm in names:
            out.append("    %s," % nm)
        out.append("]\n")
        out.append('''

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
%s_REGISTRY_%s = REGISTRY
''' % (reg_const, reg))
        out.append(SYNTH)
        out.append('''

if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    domain_primitives = %s
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0
    nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print("OK %s_" + "%s" + "_001_150_claude: " + str(n_features) + " features pass")
''' % (prim_tuple, fam, suffix))
        text = "".join(out)
        outpath = os.path.join(folder, "%s_%s_001_150_claude.py" % (fam, suffix))
        with open(outpath, "w", encoding="utf-8") as fh:
            fh.write(text)
        print("wrote", outpath, "%.1fKB" % (len(text) / 1024.0))


if __name__ == "__main__":
    build(sys.argv[1])
