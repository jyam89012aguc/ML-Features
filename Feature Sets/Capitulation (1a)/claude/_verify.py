"""Verification + smoke test for capitulation 1a claude folders.
QA harness — not part of the feature build. Does not touch any database.

Folder-aware input discipline:
  - folders 01-59  : SEP folders, inputs must be price/volume only
  - folders 60-76  : SF1 fundamental folders, inputs must be SF1 fields
  - folders 77+    : not yet covered here; inputs accepted if known
"""
import ast
import io
import os
import re
import tokenize
import importlib.util
import warnings
import numpy as np
import pandas as pd


def _code_only(src):
    """Strip comments and string literals so FWD-LOOK regex only sees code."""
    out = []
    try:
        for tok in tokenize.generate_tokens(io.StringIO(src).readline):
            if tok.type in (tokenize.COMMENT, tokenize.STRING):
                continue
            out.append(tok.string)
    except (tokenize.TokenError, IndentationError, SyntaxError):
        return src
    return " ".join(out)

warnings.simplefilter("ignore")
ROOT = os.path.dirname(os.path.abspath(__file__))
SEP_INPUTS = {"close", "high", "low", "open", "volume"}
SF1_INPUTS = {
    "revenue", "cor", "gp", "opex", "sgna", "rnd", "opinc", "ebit",
    "ebitda", "ebt", "netinc", "netinccmn", "prefdivis", "eps", "epsdil",
    "intexp", "taxexp", "depamor", "sbcomp", "assets", "assetsc",
    "assetsnc", "cashnequiv", "receivables", "inventory", "investmentsc",
    "investmentsnc", "intangibles", "ppnenet", "tangibles", "liabilities",
    "liabilitiesc", "liabilitiesnc", "debt", "debtc", "debtnc", "payables",
    "deferredrev", "equity", "retearn", "accoci", "workingcapital",
    "invcap", "ncfo", "ncfi", "ncff", "ncf", "capex", "fcf", "ncfdebt",
    "ncfcommon", "ncfdiv", "sharesbas", "shareswa", "shareswadil",
}
VAL_INPUTS = {"marketcap", "ev", "pe", "pb", "ps", "evebit", "evebitda",
              "divyield"}
PEER_INPUTS = {"peer_median_" + m for m in VAL_INPUTS}
SF2_INPUTS = {
    "insider_buy_count", "insider_sell_count", "insider_buy_shares",
    "insider_sell_shares", "insider_buy_value", "insider_sell_value",
    "insider_buyers", "insider_sellers", "officer_buy_count",
    "officer_buy_value", "officer_sell_value", "director_buy_count",
    "director_buy_value", "director_sell_value", "ceo_buy_value",
    "cfo_buy_value", "tenpct_buy_count", "tenpct_buy_value",
    "insider_shares_held",
}
EVENT_INPUTS = {
    "closeunadj", "exchange_tier", "delist_notice", "dividends", "dps",
    "split_factor", "event_count", "audit_warning", "going_concern",
}
SF3_INPUTS = {
    "inst_holders", "inst_shares", "inst_value", "inst_pct", "new_positions",
    "closed_positions", "increased_positions", "decreased_positions",
    "avg_position", "hhi", "top1_shares", "top5_shares", "top10_shares",
}
SF3_PEER_INPUTS = {"peer_median_" + m for m in (
    "inst_holders", "inst_shares", "inst_pct", "new_positions",
    "closed_positions")}
FWD = [r"shift\(\s*-", r"\.iloc\[\s*\w+\s*\+", r"diff\(\s*-"]
N = 1300


def synth_price(n=N):
    rng = np.random.default_rng(7)
    idx = pd.date_range("2018-01-01", periods=n, freq="B")
    steps = rng.normal(-0.001, 0.03, n)
    close = pd.Series(100 * np.exp(np.cumsum(steps)), index=idx)
    op = close.shift(1).fillna(close.iloc[0]) * (1 + rng.normal(0, 0.01, n))
    hi = np.maximum(close, op) * (1 + np.abs(rng.normal(0, 0.012, n)))
    lo = np.minimum(close, op) * (1 - np.abs(rng.normal(0, 0.012, n)))
    vol = pd.Series(np.abs(rng.normal(1e6, 3e5, n)), index=idx)
    return idx, {"close": close, "open": pd.Series(op, index=idx),
                 "high": pd.Series(hi, index=idx), "low": pd.Series(lo, index=idx),
                 "volume": vol}


def synth_fundamentals(idx):
    """Synthetic quarterly SF1 fields forward-filled onto the daily index."""
    rng = np.random.default_rng(13)
    qidx = idx[::63]
    n = len(qidx)
    rev = np.abs(rng.normal(5e8, 1e8, n)).cumsum() / 3 + 1e8
    cost_like = {"cor", "opex", "sgna", "rnd"}
    margin_like = {"netinc", "netinccmn", "opinc", "ebit", "ebitda", "ebt",
                   "gp", "fcf", "ncfo", "ncf"}
    bs_pos = {"cashnequiv", "assets", "assetsc", "assetsnc", "receivables",
              "inventory", "payables", "deferredrev", "workingcapital",
              "debt", "debtc", "debtnc", "liabilities", "liabilitiesc",
              "liabilitiesnc", "investmentsc", "investmentsnc", "intangibles",
              "ppnenet", "tangibles", "invcap", "equity"}
    signed_cum = {"retearn", "accoci"}
    signed_flow = {"ncfdebt", "ncfcommon", "ncfdiv"}
    neg_flow = {"capex", "ncfi", "ncff"}
    out = {}
    for f in SF1_INPUTS:
        if f == "revenue":
            q = pd.Series(rev, index=qidx)
        elif f in cost_like:
            q = pd.Series(rev * rng.uniform(0.1, 0.6, n), index=qidx)
        elif f in margin_like:
            q = pd.Series(rev * rng.normal(0.05, 0.15, n), index=qidx)
        elif f in ("eps", "epsdil"):
            q = pd.Series(rng.normal(0.5, 1.5, n), index=qidx)
        elif f in ("shareswa", "shareswadil", "sharesbas"):
            q = pd.Series(np.abs(rng.normal(1e8, 1e6, n)), index=qidx)
        elif f in neg_flow:
            q = pd.Series(-np.abs(rng.normal(3e7, 1e7, n)), index=qidx)
        elif f in signed_cum:
            q = pd.Series(rng.normal(0, 5e7, n).cumsum(), index=qidx)
        elif f in signed_flow:
            q = pd.Series(rng.normal(0, 2e7, n), index=qidx)
        elif f in bs_pos:
            q = pd.Series(np.abs(rng.normal(2e8, 5e7, n)), index=qidx)
        else:  # depamor, sbcomp, taxexp, intexp, prefdivis
            q = pd.Series(np.abs(rng.normal(2e7, 5e6, n)), index=qidx)
        out[f] = q.reindex(idx).ffill().bfill()
    return out


def synth_valuation(idx):
    """Synthetic daily Sharadar DAILY valuation metrics + peer medians."""
    rng = np.random.default_rng(29)
    n = len(idx)
    mc = pd.Series(1e9 * np.exp(np.cumsum(rng.normal(-0.001, 0.03, n))),
                   index=idx)
    out = {}
    out["marketcap"] = mc
    out["ev"] = mc * pd.Series(rng.uniform(1.0, 2.5, n), index=idx)
    out["pe"] = pd.Series(rng.normal(15, 12, n), index=idx)
    out["pb"] = pd.Series(np.abs(rng.normal(2.2, 1.4, n)), index=idx)
    out["ps"] = pd.Series(np.abs(rng.normal(3.0, 2.0, n)), index=idx)
    out["evebit"] = pd.Series(rng.normal(13, 10, n), index=idx)
    out["evebitda"] = pd.Series(rng.normal(9, 6, n), index=idx)
    out["divyield"] = pd.Series(np.abs(rng.normal(0.02, 0.025, n)), index=idx)
    for m in list(out):
        base = out[m]
        out["peer_median_" + m] = base.rolling(21, min_periods=1).mean() * \
            pd.Series(rng.uniform(0.85, 1.15, n), index=idx)
    return out


def synth_insider(idx):
    """Synthetic sparse daily event-aggregated SF2 insider series (~95% zero)."""
    rng = np.random.default_rng(41)
    n = len(idx)

    def sparse(scale, integer=False):
        mask = rng.random(n) < 0.05
        vals = np.abs(rng.normal(scale, scale * 0.6, n))
        if integer:
            vals = np.maximum(1.0, np.round(vals))
        return pd.Series(np.where(mask, vals, 0.0), index=idx)

    count_fields = {"insider_buy_count", "insider_sell_count",
                    "insider_buyers", "insider_sellers", "officer_buy_count",
                    "director_buy_count", "tenpct_buy_count"}
    share_fields = {"insider_buy_shares", "insider_sell_shares"}
    out = {}
    for f in SF2_INPUTS:
        if f == "insider_shares_held":
            out[f] = pd.Series(
                np.abs(5e6 + np.cumsum(rng.normal(0, 2e4, n))), index=idx)
        elif f in count_fields:
            out[f] = sparse(2.0, integer=True)
        elif f in share_fields:
            out[f] = sparse(5e4)
        else:  # *_value fields
            out[f] = sparse(5e5)
    return out


def synth_events(idx):
    """Synthetic daily corporate-action / listing-event series (ACTIONS/EVENTS,
    families 96-100). Status fields are forward-filled onto the daily index."""
    rng = np.random.default_rng(53)
    n = len(idx)
    out = {}
    # raw unadjusted close: positive random-walk price that drifts toward
    # delisting-relevant sub-$5 / sub-$1 territory
    out["closeunadj"] = pd.Series(
        8.0 * np.exp(np.cumsum(rng.normal(-0.001, 0.03, n))), index=idx)
    # exchange tier: ordinal 1-5, forward-filled, occasional downgrades
    tier = np.ones(n)
    t = 1
    for i in range(n):
        if t < 5 and rng.random() < 0.004:
            t += 1
        tier[i] = t
    out["exchange_tier"] = pd.Series(tier, index=idx)
    # delisting / deficiency notice: binary, clustered multi-week spells
    notice = np.zeros(n)
    i = 0
    while i < n:
        if rng.random() < 0.01:
            span = int(rng.integers(20, 120))
            notice[i:i + span] = 1.0
            i += span
        else:
            i += 1
    out["delist_notice"] = pd.Series(notice, index=idx)
    # going-concern flag: rare, long spells
    gc = np.zeros(n)
    i = 0
    while i < n:
        if rng.random() < 0.003:
            span = int(rng.integers(60, 250))
            gc[i:i + span] = 1.0
            i += span
        else:
            i += 1
    out["going_concern"] = pd.Series(gc, index=idx)
    # audit warning: sparse binary events
    out["audit_warning"] = pd.Series((rng.random(n) < 0.01).astype(float), index=idx)
    # dividends paid on ~quarterly ex-dates, else 0
    div = np.zeros(n)
    div[::63] = np.abs(rng.normal(0.15, 0.05, len(div[::63])))
    out["dividends"] = pd.Series(div, index=idx)
    # trailing dividend-per-share: forward-filled annualised step series
    out["dps"] = (pd.Series(div, index=idx).replace(0.0, np.nan)
                  .ffill().fillna(0.0) * 4.0)
    # split factor: 1.0 normally, occasional reverse split (<1) or split (>1)
    sf = np.ones(n)
    for i in range(n):
        if rng.random() < 0.002:
            sf[i] = float(rng.choice([0.1, 0.2, 0.5, 2.0]))
    out["split_factor"] = pd.Series(sf, index=idx)
    # corporate-event filing count: mostly 0, occasional small bursts
    out["event_count"] = pd.Series(
        np.where(rng.random(n) < 0.06, rng.integers(1, 5, n), 0).astype(float),
        index=idx)
    return out


def synth_sf3(idx):
    """Synthetic quarterly SF3 institutional-ownership fields, forward-filled
    onto the daily index (families 91-95). Includes peer-median series for the
    cross-sectional family 94 (holder_count_dynamics)."""
    rng = np.random.default_rng(67)
    qidx = idx[::63]
    nq = len(qidx)

    def q(vals):
        return pd.Series(vals, index=qidx).reindex(idx).ffill().bfill()

    # institutional holder count: declining trend (institutional exit)
    holders = np.clip(300 + np.cumsum(rng.normal(-3.0, 25.0, nq)), 5, None)
    inst_shares = np.abs(rng.normal(5e7, 1.5e7, nq)) + holders * 1e4
    out = {}
    out["inst_holders"] = q(np.round(holders))
    out["inst_shares"] = q(inst_shares)
    out["inst_pct"] = q(np.clip(rng.normal(0.6, 0.15, nq), 0.02, 0.98))
    out["inst_value"] = q(inst_shares * np.abs(rng.normal(40.0, 12.0, nq)))
    out["new_positions"] = q(np.round(np.abs(rng.normal(20.0, 12.0, nq))))
    out["closed_positions"] = q(np.round(np.abs(rng.normal(25.0, 14.0, nq))))
    out["increased_positions"] = q(np.round(np.abs(rng.normal(40.0, 18.0, nq))))
    out["decreased_positions"] = q(np.round(np.abs(rng.normal(45.0, 20.0, nq))))
    out["avg_position"] = q(inst_shares / np.maximum(holders, 1.0))
    out["hhi"] = q(np.clip(rng.normal(0.12, 0.06, nq), 0.01, 0.9))
    top1 = inst_shares * np.clip(rng.uniform(0.05, 0.20, nq), 0, 1)
    top5 = inst_shares * np.clip(rng.uniform(0.25, 0.50, nq), 0, 1)
    top10 = inst_shares * np.clip(rng.uniform(0.45, 0.75, nq), 0, 1)
    out["top1_shares"] = q(top1)
    out["top5_shares"] = q(np.maximum(top5, top1))
    out["top10_shares"] = q(np.maximum(top10, np.maximum(top5, top1)))
    # peer-median series (cross-sectional inputs for family 94)
    for f in ("inst_holders", "inst_shares", "inst_pct",
              "new_positions", "closed_positions"):
        base = out[f]
        out["peer_median_" + f] = base.rolling(21, min_periods=1).mean() * \
            pd.Series(rng.uniform(0.85, 1.15, len(idx)), index=idx)
    return out


IDX, DATA = synth_price()
DATA.update(synth_fundamentals(IDX))
DATA.update(synth_valuation(IDX))
DATA.update(synth_insider(IDX))
DATA.update(synth_events(IDX))
DATA.update(synth_sf3(IDX))
folders = sorted(d for d in os.listdir(ROOT)
                 if os.path.isdir(os.path.join(ROOT, d)) and d[:2].isdigit())

tot_feat = tot_pass = tot_fail = tot_nan = tot_const = 0
print(f"{'file':<48}{'parse':<7}{'KB':<7}{'count':<7}{'run ok':<8}{'allNaN':<8}{'const'}")
print("-" * 92)

for folder in folders:
    fdir = os.path.join(ROOT, folder)
    try:
        fnum = int(folder.split("_")[0])
    except ValueError:
        continue
    if fnum <= 59:
        allowed = SEP_INPUTS
    elif fnum <= 76:
        allowed = SF1_INPUTS
    elif fnum == 82:
        allowed = VAL_INPUTS | PEER_INPUTS
    elif fnum <= 81:
        allowed = VAL_INPUTS
    elif fnum == 87:
        allowed = SF2_INPUTS | {"close"}
    elif fnum <= 90:
        allowed = SF2_INPUTS
    elif fnum == 94:
        allowed = SF3_INPUTS | SF3_PEER_INPUTS | {"close"}
    elif 91 <= fnum <= 95:
        allowed = SF3_INPUTS | {"close"}
    elif 96 <= fnum <= 100:
        allowed = SEP_INPUTS | EVENT_INPUTS
    else:
        allowed = set(DATA)
    # Audit the 4 canonical files per folder (mandatory, addressed by name)
    # plus every {folder}_extended_*.py file (the optional "extended" tier:
    # extended_001_075 / extended_076_150 / extended_2nd_derivatives /
    # extended_3rd_derivatives). Any other *.py is flagged STRAY so a
    # backup/scratch file cannot inject its own registry into the tally.
    canon_files = [f"{folder}_{t}.py" for t in
                   ("base_001_075", "base_076_150",
                    "2nd_derivatives", "3rd_derivatives")]
    ext_files = sorted(f for f in os.listdir(fdir)
                       if f.startswith(f"{folder}_extended_")
                       and f.endswith(".py"))
    audit_files = canon_files + ext_files
    audit_set = set(audit_files)
    for stray in sorted(f for f in os.listdir(fdir)
                        if f.endswith(".py") and f not in audit_set):
        print(f"{stray:<48}-- STRAY non-canonical file (not audited)")
    for fn in audit_files:
        path = os.path.join(fdir, fn)
        if not os.path.isfile(path):
            print(f"{fn:<48}MISSING")
            continue
        src = open(path, encoding="utf-8").read()
        kb = len(src.encode("utf-8")) / 1024
        try:
            ast.parse(src)
        except SyntaxError as e:
            print(f"{fn:<48}FAIL  {e}")
            continue
        fwd_hits = [p for p in FWD if re.search(p, _code_only(src))]
        spec = importlib.util.spec_from_file_location(fn[:-3], path)
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
        except Exception as e:
            print(f"{fn:<48}FAIL  import error: {type(e).__name__}: {e}")
            continue
        reg = {k: v for k, v in vars(mod).items()
               if k.endswith(("_001_075", "_076_150", "_DERIVATIVES")) and isinstance(v, dict)}
        if len(reg) != 1:
            print(f"{fn:<48}-- registry dicts found: {list(reg)}")
            continue
        rname, rdict = next(iter(reg.items()))
        cnt = len(rdict)
        tot_feat += cnt
        ok = nan = const = 0
        bad_inputs, undef, errs = [], [], []
        for name, meta in rdict.items():
            ins = meta.get("inputs", [])
            if not set(ins) <= allowed:
                bad_inputs.append((name, [i for i in ins if i not in allowed]))
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
        print(f"{fn:<48}{'OK':<7}{kb:<7.1f}{cnt:<7}{ok:<8}{nan:<8}{const}{size_flag}")
        for nm, ins in bad_inputs:
            print(f"    DISALLOWED INPUT: {nm} -> {ins}")
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
