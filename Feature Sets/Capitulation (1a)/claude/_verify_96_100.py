"""Verification + smoke test for capitulation folders 96-100 (ACTIONS/EVENTS).

QA harness — not part of the feature build. Does not touch any database.
The shipped _verify.py only knows SEP/SF1 inputs and cannot exercise the
event-driven inputs used by families 96-100; this file fills that gap with
synthetic corporate-action / event Series matching each folder's documented
input contract.

Checks per .py file: ast.parse, size < 75KB, registry present with the
expected entry count, every func reference defined, every feature runs and
returns a same-length pandas Series, plus all-NaN / constant-output counts
and a backward-looking-pattern scan.
"""
import ast
import os
import re
import importlib.util
import warnings
import numpy as np
import pandas as pd

warnings.simplefilter("ignore")
ROOT = os.path.dirname(os.path.abspath(__file__))
FOLDERS = [
    "96_dividend_distress",
    "97_reverse_split_signal",
    "98_corporate_event_density",
    "99_going_concern_flags",
    "100_listing_status_risk",
]
FWD = [r"shift\(\s*-", r"\.iloc\[\s*\w+\s*\+", r"diff\(\s*-"]
N = 1300


def synth_inputs(n=N):
    """Synthetic daily Series covering the input contracts of folders 96-100."""
    rng = np.random.default_rng(101)
    idx = pd.date_range("2018-01-01", periods=n, freq="B")

    # adjusted close: declining random walk (a distressed name into its low)
    steps = rng.normal(-0.0012, 0.032, n)
    close = pd.Series(40.0 * np.exp(np.cumsum(steps)), index=idx)

    # reverse splits: factor 1.0 normally; two reverse splits + one forward
    split_factor = pd.Series(np.ones(n), index=idx)
    split_factor.iloc[400] = 0.1     # 1-for-10 reverse split
    split_factor.iloc[900] = 0.2     # 1-for-5 reverse split
    split_factor.iloc[650] = 2.0     # forward 2-for-1

    # unadjusted close: nominal price drifting toward sub-$1, lifted on RS dates
    raw = pd.Series(12.0 * np.exp(np.cumsum(rng.normal(-0.0018, 0.03, n))), index=idx)
    cum = split_factor.iloc[::-1].cumprod().iloc[::-1].shift(-1).fillna(1.0)
    closeunadj = (raw / cum).clip(lower=0.05)

    # dividends per share: paid, then cut, then omitted
    dps = pd.Series(np.zeros(n), index=idx)
    qidx = np.arange(0, n, 63)
    dps_path = [0.20, 0.20, 0.22, 0.22, 0.15, 0.15, 0.05, 0.0, 0.0, 0.0,
                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    for k, q in enumerate(qidx):
        dps.iloc[q:] = dps_path[min(k, len(dps_path) - 1)]
    dividends = dps * 1.0e8  # total cash dividends proxy

    # corporate-event count: mostly zero, Poisson bursts, a distress cluster
    event_count = pd.Series(rng.poisson(0.04, n).astype(float), index=idx)
    event_count.iloc[700:760] += rng.poisson(0.8, 60).astype(float)

    # going-concern / audit-warning flags (forward-filled step functions)
    audit_warning = pd.Series(np.zeros(n), index=idx)
    audit_warning.iloc[520:] = 1.0
    going_concern = pd.Series(np.zeros(n), index=idx)
    going_concern.iloc[760:] = 1.0

    # exchange tier: steps down (1 -> 2 -> 3 -> 4) as distress deepens
    exchange_tier = pd.Series(np.ones(n), index=idx)
    exchange_tier.iloc[300:] = 2.0
    exchange_tier.iloc[640:] = 3.0
    exchange_tier.iloc[980:] = 4.0

    # delisting-deficiency notice: two spells in effect
    delist_notice = pd.Series(np.zeros(n), index=idx)
    delist_notice.iloc[560:620] = 1.0
    delist_notice.iloc[860:] = 1.0

    return idx, {
        "close": close, "closeunadj": closeunadj, "split_factor": split_factor,
        "dps": dps, "dividends": dividends, "event_count": event_count,
        "going_concern": going_concern, "audit_warning": audit_warning,
        "exchange_tier": exchange_tier, "delist_notice": delist_notice,
    }


IDX, DATA = synth_inputs()
ALLOWED = set(DATA)
EXPECTED = {"_001_075": 75, "_076_150": 75,
            "_2ND_DERIVATIVES": 25, "_3RD_DERIVATIVES": 25}

tot_feat = tot_pass = tot_fail = tot_nan = tot_const = 0
print(f"{'file':<46}{'parse':<7}{'KB':<7}{'count':<7}{'run ok':<8}{'allNaN':<8}{'const'}")
print("-" * 92)

for folder in FOLDERS:
    fdir = os.path.join(ROOT, folder)
    if not os.path.isdir(fdir):
        print(f"{folder:<46}MISSING FOLDER")
        continue
    for fn in sorted(f for f in os.listdir(fdir) if f.endswith(".py")):
        path = os.path.join(fdir, fn)
        src = open(path, encoding="utf-8").read()
        kb = len(src.encode("utf-8")) / 1024
        try:
            ast.parse(src)
        except SyntaxError as e:
            print(f"{fn:<46}FAIL  {e}")
            continue
        fwd_hits = [p for p in FWD if re.search(p, src)]
        spec = importlib.util.spec_from_file_location(fn[:-3], path)
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
        except Exception as e:
            print(f"{fn:<46}IMPORT FAIL  {repr(e)[:60]}")
            continue
        reg = {k: v for k, v in vars(mod).items()
               if k.endswith(("_001_075", "_076_150", "_DERIVATIVES"))
               and isinstance(v, dict)}
        if len(reg) != 1:
            print(f"{fn:<46}-- registry dicts found: {list(reg)}")
            continue
        rname, rdict = next(iter(reg.items()))
        cnt = len(rdict)
        exp = next((v for k, v in EXPECTED.items() if rname.endswith(k)), None)
        cnt_flag = "" if exp is None or cnt == exp else f" !expected {exp}"
        tot_feat += cnt
        ok = nan = const = 0
        bad_inputs, undef, errs = [], [], []
        for name, meta in rdict.items():
            ins = meta.get("inputs", [])
            if not set(ins) <= ALLOWED:
                bad_inputs.append((name, [i for i in ins if i not in ALLOWED]))
            f = meta.get("func")
            if not callable(f):
                undef.append(name)
                continue
            try:
                args = [DATA[i] for i in ins if i in DATA]
                if len(args) != len(ins):
                    raise KeyError([i for i in ins if i not in DATA])
                out = f(*args)
                assert isinstance(out, pd.Series), "not a Series"
                assert len(out) == len(DATA["close"]), "length mismatch"
                ok += 1
                if out.isna().all():
                    nan += 1
                elif out.nunique(dropna=True) <= 1:
                    const += 1
            except Exception as e:
                errs.append((name, repr(e)[:90]))
        tot_pass += ok
        tot_fail += len(errs) + len(undef)
        tot_nan += nan
        tot_const += const
        size_flag = "" if kb < 75 else " !>75KB"
        print(f"{fn:<46}{'OK':<7}{kb:<7.1f}{str(cnt) + cnt_flag:<7}"
              f"{ok:<8}{nan:<8}{const}{size_flag}")
        for nm, ii in bad_inputs:
            print(f"    DISALLOWED INPUT: {nm} -> {ii}")
        for nm in undef:
            print(f"    UNDEFINED FUNC: {nm}")
        for nm, e in errs:
            print(f"    RUNTIME ERROR: {nm}: {e}")
        if fwd_hits:
            print(f"    FWD-LOOK PATTERN(S): {fwd_hits}")

print("-" * 92)
print(f"TOTAL features registered : {tot_feat}")
print(f"  ran OK                   : {tot_pass}")
print(f"  failed (error/undefined) : {tot_fail}")
print(f"  all-NaN output           : {tot_nan}")
print(f"  constant output          : {tot_const}")
