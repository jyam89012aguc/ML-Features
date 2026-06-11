"""
Deep-quality review of folders 51-75 (temp QA script, not part of the build).
Builds a realistic synthetic capitulation dataset so features genuinely vary,
runs all 5,000 features, and analyzes:
  - dead features  : all-NaN, constant, near-constant (<=5 distinct values)
  - mostly-NaN     : >90% NaN
  - redundancy     : within-folder feature pairs with |corr| >= 0.95 / 0.999
  - cross-folder duplication (domain bleed)
Does not touch any database.
"""
import os
import zlib
import warnings
import importlib.util
import numpy as np
import pandas as pd

warnings.simplefilter("ignore")
ROOT = os.path.dirname(os.path.abspath(__file__))

SF1_INPUTS = [
    "revenue", "cor", "gp", "opex", "sgna", "rnd", "opinc", "ebit",
    "ebitda", "ebt", "netinc", "netinccmn", "prefdivis", "eps", "epsdil",
    "intexp", "taxexp", "depamor", "sbcomp", "assets", "assetsc",
    "assetsnc", "cashnequiv", "receivables", "inventory", "investmentsc",
    "investmentsnc", "intangibles", "ppnenet", "tangibles", "liabilities",
    "liabilitiesc", "liabilitiesnc", "debt", "debtc", "debtnc", "payables",
    "deferredrev", "equity", "retearn", "accoci", "workingcapital",
    "invcap", "ncfo", "ncfi", "ncff", "ncf", "capex", "fcf", "ncfdebt",
    "ncfcommon", "ncfdiv", "sharesbas", "shareswa", "shareswadil",
]


def build_data():
    """Realistic capitulation path: 10x run-up -> crash to multi-year low ->
    grinding sub-$5 bottom (incl. zero-volume days) -> weak bounce. Plus a
    distressed quarterly SF1 set forward-filled to the daily index."""
    n = 1400
    idx = pd.date_range("2016-01-01", periods=n, freq="B")
    rng = np.random.default_rng(20240520)

    # --- price path with explicit phases -----------------------------------
    drift = np.empty(n)
    vol = np.empty(n)
    drift[:500] = 0.0050;  vol[:500] = 0.018          # 10x run-up
    drift[500:900] = -0.0090; vol[500:900] = 0.055    # crash / capitulation
    drift[900:1150] = -0.0005; vol[900:1150] = 0.030  # grinding bottom
    drift[1150:] = 0.0035; vol[1150:] = 0.035         # weak bounce
    steps = rng.normal(drift, vol)
    close = pd.Series(5.0 * np.exp(np.cumsum(steps)), index=idx)

    op = (close.shift(1).fillna(close.iloc[0])
          * (1 + rng.normal(0, 0.008, n)))
    rng_mult = np.where(np.arange(n) < 900,
                        np.abs(rng.normal(0, 0.018, n)),
                        np.abs(rng.normal(0, 0.010, n)))
    hi = np.maximum(close.values, op) * (1 + rng_mult)
    lo = np.minimum(close.values, op) * (1 - rng_mult)

    # --- volume: blowoff in the crash, dry-up at the bottom ----------------
    base_v = np.full(n, 1.0e6)
    base_v[500:760] *= np.linspace(1, 6, 260)        # blowoff
    base_v[760:1150] *= np.linspace(6, 0.25, 390)    # dry-up / exhaustion
    base_v[1150:] *= 0.6
    volume = pd.Series(np.abs(rng.normal(base_v, base_v * 0.3)) + 1.0,
                       index=idx)
    zero_days = rng.choice(np.arange(950, 1140), size=18, replace=False)
    volume.iloc[zero_days] = 0.0                      # genuine no-trade days

    data = {"close": close,
            "open": pd.Series(op, index=idx),
            "high": pd.Series(hi, index=idx),
            "low": pd.Series(lo, index=idx),
            "volume": volume}

    # --- distressed quarterly SF1, forward-filled to daily -----------------
    # Each field is an INDEPENDENT noisy geometric/arithmetic walk (per-field
    # seed) so QoQ changes carry genuine, decorrelated variation. A monotonic
    # linspace would make every level/change/derivative feature collinear and
    # produce a falsely-inflated redundancy report.
    qidx = idx[::63]
    q = len(qidx)
    cost_like = {"cor", "opex", "sgna", "rnd"}
    margin_like = {"netinc", "netinccmn", "opinc", "ebit", "ebitda", "ebt",
                   "gp", "fcf", "ncfo", "ncf"}
    bs_pos = {"cashnequiv", "assets", "assetsc", "assetsnc", "receivables",
              "inventory", "payables", "deferredrev", "workingcapital",
              "debtc", "debtnc", "liabilities", "liabilitiesc",
              "liabilitiesnc", "investmentsc", "investmentsnc",
              "intangibles", "ppnenet", "tangibles", "invcap"}
    signed_cum = {"retearn", "accoci"}
    signed_flow = {"ncfdebt", "ncfcommon", "ncfdiv"}
    neg_flow = {"capex", "ncfi", "ncff"}

    def fseed(name):
        # deterministic per-field seed (Python's hash() is per-process random)
        return np.random.default_rng(zlib.crc32(name.encode()) & 0xFFFFFFFF)

    def gwalk(name, start, drift, vol):
        """Independent geometric walk with a downward distress drift."""
        r = fseed(name)
        return start * np.cumprod(1 + drift + r.normal(0, vol, q))

    rev = gwalk("revenue", 5e8, -0.045, 0.07)
    for f in SF1_INPUTS:
        if f == "revenue":
            s = rev
        elif f in cost_like:
            ratio = fseed(f + "_r").uniform(0.15, 0.55) \
                * (1 + fseed(f).normal(0, 0.12, q))
            s = np.abs(rev * ratio)
        elif f in margin_like:
            mr = fseed(f).normal(0, 0.10, q)            # noisy margin walk
            margin = np.linspace(0.10, -0.18, q) + np.cumsum(mr) * 0.20
            s = rev * margin
        elif f in ("eps", "epsdil"):
            s = (np.linspace(1.3, -1.0, q)
                 + np.cumsum(fseed(f).normal(0, 0.12, q)))
        elif f in ("shareswa", "shareswadil", "sharesbas"):
            s = gwalk(f, 1e8, 0.012, 0.015)             # distinct per field
        elif f in neg_flow:
            s = -np.abs(gwalk(f, 3e7, 0.01, 0.20))
        elif f in signed_cum:
            s = (np.linspace(2e8, -3e8, q)
                 + np.cumsum(fseed(f).normal(0, 4e7, q)))
        elif f in signed_flow:
            s = fseed(f).normal(0, 2e7, q)
        elif f == "debt":
            s = gwalk("debt", 2e8, 0.030, 0.05)         # leverage escalation
        elif f == "equity":
            s = gwalk("equity", 4e8, -0.055, 0.06)      # equity erosion
        elif f in bs_pos:
            s = gwalk(f, 2e8, -0.020, 0.06)
        else:
            s = np.abs(gwalk(f, 2e7, -0.01, 0.10))
        data[f] = pd.Series(np.asarray(s, float), index=qidx
                            ).reindex(idx).ffill().bfill()
    return data


def load_folder(fdir):
    """Return {feature_name: pd.Series} for a folder's 4 canonical files plus
    any {folder}_extended_*.py tier files. Files are addressed by name/glob so
    a stray *.py cannot inject extra registries; a broken file is skipped."""
    feats = {}
    data = DATA
    folder = os.path.basename(fdir)
    canon = [f"{folder}_{t}.py" for t in
             ("base_001_075", "base_076_150",
              "2nd_derivatives", "3rd_derivatives")]
    ext = sorted(f for f in os.listdir(fdir)
                 if f.startswith(f"{folder}_extended_") and f.endswith(".py"))
    for fn in canon + ext:
        path = os.path.join(fdir, fn)
        if not os.path.isfile(path):
            continue
        spec = importlib.util.spec_from_file_location("q_" + fn[:-3], path)
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
        except Exception:
            continue
        for k, v in list(vars(mod).items()):
            if not (isinstance(v, dict) and (k.endswith(
                    ("_001_075", "_076_150", "_DERIVATIVES")) or "REGISTRY" in k)):
                continue
            for name, meta in v.items():
                try:
                    out = meta["func"](*[data[i] for i in meta["inputs"]])
                    feats[name] = pd.Series(out).astype(float)
                except Exception:
                    feats[name] = pd.Series(np.nan, index=data["close"].index)
    return feats


DATA = build_data()
folders = sorted(d for d in os.listdir(ROOT)
                 if os.path.isdir(os.path.join(ROOT, d))
                 and d.split("_")[0].isdigit()
                 and 51 <= int(d.split("_")[0]) <= 75)

print(f"{'folder':<30}{'feat':>5}{'NaN':>5}{'const':>6}{'near':>6}"
      f"{'mNaN':>6}{'dup95':>7}{'dup999':>8}{'maxclu':>7}")
print("-" * 86)

summary = []
folder_frames = {}
for folder in folders:
    feats = load_folder(os.path.join(ROOT, folder))
    df = pd.DataFrame(feats)
    folder_frames[folder] = df
    n_feat = df.shape[1]
    allnan = const = near = mostly = 0
    live_cols = []
    for c in df.columns:
        s = df[c]
        nn = s.dropna()
        if len(nn) == 0:
            allnan += 1
            continue
        if s.isna().mean() > 0.90:
            mostly += 1
        u = nn.round(10).nunique()
        if u <= 1:
            const += 1
            continue
        if u <= 5:
            near += 1
        live_cols.append(c)
    # within-folder redundancy on live (non-constant) features
    dup95 = dup999 = maxclu = 0
    if len(live_cols) > 1:
        corr = df[live_cols].corr().abs()
        np.fill_diagonal(corr.values, 0.0)
        cv = corr.values
        iu = np.triu_indices_from(cv, k=1)
        pair = cv[iu]
        dup95 = int((pair >= 0.95).sum())
        dup999 = int((pair >= 0.999).sum())
        # largest cluster of mutually >=0.95 features (greedy connected comp)
        adj = cv >= 0.95
        seen = set()
        for i in range(len(live_cols)):
            if i in seen:
                continue
            stack, comp = [i], []
            while stack:
                j = stack.pop()
                if j in seen:
                    continue
                seen.add(j)
                comp.append(j)
                stack.extend(np.where(adj[j])[0])
            maxclu = max(maxclu, len(comp))
    summary.append((folder, n_feat, allnan, const, near, mostly,
                    dup95, dup999, maxclu))
    print(f"{folder:<30}{n_feat:>5}{allnan:>5}{const:>6}{near:>6}"
          f"{mostly:>6}{dup95:>7}{dup999:>8}{maxclu:>7}")

print("-" * 86)
tot = [sum(r[i] for r in summary) for i in range(1, 9)]
print(f"{'TOTAL 51-75':<30}{tot[0]:>5}{tot[1]:>5}{tot[2]:>6}{tot[3]:>6}"
      f"{tot[4]:>6}{tot[5]:>7}{tot[6]:>8}{'-':>7}")

# --- worst-offender detail: top folders by exact-duplicate count -----------
print("\n=== EXACT/NEAR-EXACT DUPLICATE PAIRS (|corr| >= 0.999) ===")
worst = sorted(summary, key=lambda r: -r[7])[:6]
for folder, *_rest in worst:
    if _rest[6] == 0:
        continue
    df = folder_frames[folder]
    live = [c for c in df.columns
            if df[c].dropna().round(10).nunique() > 1]
    corr = df[live].corr().abs()
    np.fill_diagonal(corr.values, 0.0)
    pairs = []
    cv = corr.values
    for i in range(len(live)):
        for j in range(i + 1, len(live)):
            if cv[i, j] >= 0.999:
                pairs.append((live[i], live[j], cv[i, j]))
    print(f"\n  {folder}  ({len(pairs)} pairs):")
    for a, b, r in pairs[:12]:
        print(f"    {r:.4f}  {a}  <->  {b}")
    if len(pairs) > 12:
        print(f"    ... +{len(pairs) - 12} more")

# --- base <-> derivative file collision (schema defect) --------------------
# The schema says base files = features, derivative files = rate-of-change OF
# base features. If a base file already contains a "change/accel/diff" feature
# it collides exactly with the derivative file -> wasted feature slots.
print("\n=== BASE <-> DERIVATIVE FILE COLLISION (base feat with |corr|>=0.999"
      " to a derivative feat) ===")
coll_tot = 0
for folder in folders:
    df = folder_frames[folder]
    deriv = [c for c in df.columns if "_drv2_" in c or "_drv3_" in c]
    base = [c for c in df.columns if c not in deriv]
    live_b = [c for c in base if df[c].dropna().round(10).nunique() > 1]
    live_d = [c for c in deriv if df[c].dropna().round(10).nunique() > 1]
    if not live_b or not live_d:
        continue
    cc = df[live_b + live_d].corr().abs()
    block = cc.loc[live_b, live_d]
    collided = [b for b in live_b if (block.loc[b] >= 0.999).any()]
    coll_tot += len(collided)
    if collided:
        print(f"  {folder:<30} {len(collided):>3} base features duplicated "
              f"in the derivative files")
        for b in collided:
            row = block.loc[b]
            d = row.idxmax()
            print(f"        {b:<46} == {d:<46} ({row.max():.4f})")
print(f"  {'TOTAL base features wasted on derivative-collisions':<30} "
      f"= {coll_tot}")

# --- cross-folder domain-bleed check ---------------------------------------
print("\n=== CROSS-FOLDER DUPLICATION (adjacent folders, |corr| >= 0.97) ===")
for a, b in zip(folders[:-1], folders[1:]):
    da, db = folder_frames[a], folder_frames[b]
    la = [c for c in da.columns if da[c].dropna().round(10).nunique() > 1]
    lb = [c for c in db.columns if db[c].dropna().round(10).nunique() > 1]
    if not la or not lb:
        continue
    cc = pd.concat([da[la], db[lb]], axis=1).corr().abs()
    block = cc.loc[la, lb].values
    hits = int((block >= 0.97).sum())
    if hits:
        print(f"  {a:<28} x {b:<28} {hits} cross-pairs >=0.97")
print("\n(done)")
