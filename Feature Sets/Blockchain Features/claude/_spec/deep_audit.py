"""
DEEP signal audit — robust statistics, honest about a small/young universe.

Adds over audit_signal.py:
  - Newey-West (HAC) t-stats on the monthly cross-sectional IC series (corrects the
    overlap inflation that made the first pass's IR>2 counts optimistic).
  - Out-of-sample temporal stability (IC sign agreement across time halves).
  - Quantile long-short spread (top-minus-bottom tercile forward return) + its HAC t.
  - Horizon profile: fwd 126d / 252d / 504d (504d ~ the closest proxy to the 5y/10x target).
  - PERMUTATION NULL: shuffle ticker labels of forward returns within each month, breaking
    the feature->return link; re-measure the 'robust' share. Observed vs null is the headline
    multiple-testing honesty check (16,650 features on ~21 names will manufacture chance signal).
  - Effective dimensionality (PCA) of the base-feature set.

Audits BASE features (150/family). Single-threaded subprocess per family (pandas
rolling().rank() GIL-crashes multithreaded on this box).

Modes:
  python deep_audit.py one <family>
  python deep_audit.py summary
  python deep_audit.py pca
"""
import os
for _v in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import sys, re, json, importlib.util, warnings
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")

ROOT = r"D:/Features/claude"
PARTS = os.path.join(ROOT, "_spec", "deep_parts")
PKL = os.path.join(ROOT, "_spec", "panel.pkl")
START = pd.Timestamp("2019-01-01")
HORIZONS = [126, 252, 504]
PRIMARY = 252
NWLAG = 12  # months, ~ overlap length for 252d at monthly sampling


def load_panel():
    import pickle
    return pickle.load(open(PKL, "rb"))


def base_files(fam):
    folder = os.path.join(ROOT, fam)
    return [os.path.join(folder, f) for f in sorted(os.listdir(folder))
            if f.endswith('claude.py') and '_base_' in f]


def load_registry(path):
    fam = os.path.basename(os.path.dirname(path))
    spec = importlib.util.spec_from_file_location(fam+os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.REGISTRY


def nw_tstat(x, lag=NWLAG):
    x = np.asarray(x, float); x = x[~np.isnan(x)]
    T = len(x)
    if T < 8: return np.nan
    mu = x.mean(); e = x - mu
    g0 = np.dot(e, e) / T
    s = g0
    for l in range(1, min(lag, T-1)+1):
        gl = np.dot(e[l:], e[:-l]) / T
        s += 2.0 * (1.0 - l/(lag+1.0)) * gl
    if s <= 0: return np.nan
    se = np.sqrt(s / T)
    return mu / se if se > 0 else np.nan


def monthly_ic(feat_panel, fwd_panel):
    # feat_panel, fwd_panel: DataFrame date(month) x ticker
    ics = []
    for d in feat_panel.index:
        v = feat_panel.loc[d]; r = fwd_panel.loc[d]
        ok = v.notna() & r.notna()
        if ok.sum() >= 5 and v[ok].nunique() >= 5 and r[ok].nunique() >= 5:
            ics.append((d, v[ok].rank().corr(r[ok].rank())))
    if not ics: return pd.Series(dtype=float)
    return pd.Series([c for _, c in ics], index=[d for d, _ in ics]).dropna()


def ls_spread(feat_panel, fwd_panel):
    sp = []
    for d in feat_panel.index:
        v = feat_panel.loc[d]; r = fwd_panel.loc[d]
        ok = v.notna() & r.notna()
        if ok.sum() >= 6 and v[ok].nunique() >= 4:
            vv = v[ok]; rr = r[ok]
            q = vv.rank(pct=True)
            top = rr[q >= 2/3.0]; bot = rr[q <= 1/3.0]
            if len(top) and len(bot):
                sp.append(top.mean() - bot.mean())
    return pd.Series(sp, dtype=float)


def audit_one(fam, permute=False, seed=0):
    panel = load_panel()
    tickers = list(panel.keys())
    feats = {}
    for p in base_files(fam): feats.update(load_registry(p))
    names = list(feats.keys())
    # build per-feature monthly cross-sectional matrices
    # first, monthly sample index per ticker + forward returns
    rng = np.random.RandomState(seed)
    fvals = {n: {} for n in names}      # ticker -> Series(month->val)
    fwd = {h: {} for h in HORIZONS}     # ticker -> Series(month->fwdret)
    months_all = set()
    for t in tickers:
        df = panel[t]; idx = df.index
        ca = df['closeadj']
        post = pd.Series(idx, index=idx); post = post[idx >= START]
        if len(post) < 60: continue
        samp = post.groupby(post.dt.to_period('M')).last()
        pos = idx.get_indexer(pd.DatetimeIndex(samp.values))
        mlabels = samp.index  # PeriodIndex
        for h in HORIZONS:
            fr = (ca.shift(-h)/ca - 1.0).iloc[pos]
            fwd[h][t] = pd.Series(fr.values, index=mlabels)
        cols = {c: df[c] for c in df.columns}
        for n in names:
            try:
                y = feats[n]['func'](*[cols[c] for c in feats[n]['inputs']]).replace([np.inf,-np.inf], np.nan)
            except Exception:
                continue
            fvals[n][t] = pd.Series(y.iloc[pos].values, index=mlabels)
        months_all |= set(mlabels)
    months = pd.PeriodIndex(sorted(months_all))
    fwdM = {h: pd.DataFrame({t: fwd[h][t] for t in fwd[h]}).reindex(months) for h in HORIZONS}
    if permute:
        for h in HORIZONS:
            M = fwdM[h].copy()
            for d in M.index:
                row = M.loc[d].values.copy(); rng.shuffle(row); M.loc[d] = row
            fwdM[h] = M

    res = {}
    for n in names:
        if not fvals[n]:
            continue
        fp = pd.DataFrame({t: fvals[n][t] for t in fvals[n]}).reindex(months)
        rec = {}
        ic_primary = None
        for h in HORIZONS:
            ic = monthly_ic(fp, fwdM[h])
            rec[f'ic{h}'] = float(ic.mean()) if len(ic) else np.nan
            if h == PRIMARY: ic_primary = ic
        # HAC t on primary IC series
        hac = nw_tstat(ic_primary.values) if ic_primary is not None and len(ic_primary) else np.nan
        # OOS sign stability on primary
        oos = False
        if ic_primary is not None and len(ic_primary) >= 12:
            h1 = ic_primary.iloc[:len(ic_primary)//2]; h2 = ic_primary.iloc[len(ic_primary)//2:]
            if abs(h1.mean()) > 0.02 and abs(h2.mean()) > 0.02 and np.sign(h1.mean()) == np.sign(h2.mean()):
                oos = True
        sp = ls_spread(fp, fwdM[PRIMARY])
        sp_mean = float(sp.mean()) if len(sp) else np.nan
        sp_t = nw_tstat(sp.values) if len(sp) else np.nan
        robust = bool((abs(hac) >= 2.0 if hac==hac else False) and oos
                      and (sp_t==sp_t and abs(sp_t) >= 2.0)
                      and (np.sign(sp_mean) == np.sign(rec[f'ic{PRIMARY}']) if (sp_mean==sp_mean and rec[f'ic{PRIMARY}']==rec[f'ic{PRIMARY}']) else False))
        res[n] = dict(ic126=rec['ic126'], ic252=rec['ic252'], ic504=rec['ic504'],
                      hac=float(hac) if hac==hac else None, oos=oos,
                      ls=sp_mean if sp_mean==sp_mean else None,
                      lst=float(sp_t) if sp_t==sp_t else None, robust=robust)
    return res


def run_family(fam):
    obs = audit_one(fam, permute=False)
    nul = audit_one(fam, permute=True, seed=12345)
    os.makedirs(PARTS, exist_ok=True)
    out = dict(family=fam, obs=obs,
               null_robust=float(np.mean([v['robust'] for v in nul.values()])) if nul else None,
               null_strong_hac=float(np.mean([abs(v['hac'])>=2 for v in nul.values() if v['hac'] is not None])) if nul else None)
    json.dump(out, open(os.path.join(PARTS, fam+".json"), "w"))
    o = list(obs.values())
    ic252 = np.array([x['ic252'] for x in o if x['ic252'] is not None])
    hac = np.array([abs(x['hac']) for x in o if x['hac'] is not None])
    ic504 = np.array([x['ic504'] for x in o if x['ic504'] is not None])
    robust = np.mean([x['robust'] for x in o])
    # horizon consistency: sign agreement ic252 vs ic504
    pair = [(x['ic252'], x['ic504']) for x in o if x['ic252'] is not None and x['ic504'] is not None]
    hcons = np.mean([np.sign(a)==np.sign(b) for a,b in pair]) if pair else np.nan
    print(f"{fam:36} |ic252|med={np.median(np.abs(ic252)):.3f} hac|t|>2={np.mean(hac>=2):.0%} "
          f"robust={robust:.0%} (null={out['null_robust']:.0%})  ls&ic252signOK in robust  "
          f"horizonsignagree={hcons:.0%} |ic504|med={np.median(np.abs(ic504)):.3f}")


def summary():
    rows = []
    for fn in sorted(os.listdir(PARTS)):
        if not fn.endswith(".json"): continue
        d = json.load(open(os.path.join(PARTS, fn)))
        o = list(d['obs'].values())
        ic252 = np.array([x['ic252'] for x in o if x['ic252'] is not None])
        ic504 = np.array([x['ic504'] for x in o if x['ic504'] is not None])
        hac = np.array([abs(x['hac']) for x in o if x['hac'] is not None])
        rows.append(dict(family=d['family'], n=len(o),
            ic252_absmed=np.median(np.abs(ic252)) if len(ic252) else np.nan,
            ic504_absmed=np.median(np.abs(ic504)) if len(ic504) else np.nan,
            hac_strong=np.mean(hac>=2) if len(hac) else np.nan,
            robust=np.mean([x['robust'] for x in o]),
            null_robust=d['null_robust'], null_hac=d['null_strong_hac']))
    df = pd.DataFrame(rows).sort_values('robust', ascending=False)
    df.to_csv(os.path.join(ROOT, "_spec", "deep_audit_results.csv"), index=False)
    pd.set_option('display.width', 220); pd.set_option('display.max_rows', 50)
    print(df.to_string(index=False, float_format=lambda x: f"{x:.3f}"))
    print("\n==== OVERALL (deep) ====")
    print(f"families: {len(df)}")
    print(f"median |IC| (252d): {df['ic252_absmed'].median():.3f}   median |IC| (504d): {df['ic504_absmed'].median():.3f}")
    print(f"OBSERVED robust-feature share: {df['robust'].mean():.1%}")
    print(f"NULL (permuted) robust share : {df['null_robust'].mean():.1%}   <- false-positive floor")
    print(f"observed HAC|t|>2 share: {df['hac_strong'].mean():.1%}   null HAC|t|>2 share: {df['null_hac'].mean():.1%}")
    lift = df['robust'].mean() / max(df['null_robust'].mean(), 1e-9)
    print(f"signal lift over chance (robust): {lift:.1f}x")
    print(f"families clearly above null (robust > 3x null): {(df['robust'] > 3*df['null_robust'].clip(lower=0.01)).sum()}/{len(df)}")
    # leaderboard
    best = []
    for fn in sorted(os.listdir(PARTS)):
        if not fn.endswith('.json'): continue
        d = json.load(open(os.path.join(PARTS, fn)))
        for nm, x in d['obs'].items():
            if x['robust'] and x['hac'] is not None:
                best.append((abs(x['hac']), x['ic252'], x['ic504'], nm))
    best.sort(reverse=True)
    print("\nTop 20 robust features (by HAC |t|):")
    for h, i2, i5, nm in best[:20]:
        print(f"  |t|={h:4.1f} ic252={i2:+.3f} ic504={(i5 if i5 is not None else float('nan')):+.3f}  {nm}")
    print(f"\ntotal robust base features: {len(best)} of ~{df['n'].sum()}")


def pca():
    panel = load_panel(); tickers = list(panel.keys())
    fams = sorted([d for d in os.listdir(ROOT) if re.match(r'f\d\d_', d)])
    cols = {}
    rng = np.random.RandomState(7)
    for fam in fams:
        feats = {}
        for p in base_files(fam): feats.update(load_registry(p))
        pick = rng.choice(list(feats), size=min(40, len(feats)), replace=False)
        for n in pick:
            series = []
            for t in tickers:
                df = panel[t]; cmap = {c: df[c] for c in df.columns}
                try:
                    y = feats[n]['func'](*[cmap[c] for c in feats[n]['inputs']]).replace([np.inf,-np.inf], np.nan)
                except Exception:
                    series = []; break
                yy = y[df.index >= START]
                z = (yy - yy.mean())/yy.std() if yy.std() and yy.notna().sum() > 50 else yy*np.nan
                series.append(z.reset_index(drop=True))
            if series:
                cols[fam[:3]+"_"+n[-12:]] = pd.concat(series, ignore_index=True)
    M = pd.DataFrame(cols).dropna(axis=0, how='any')
    if len(M) < 50:
        M = pd.DataFrame(cols).fillna(0.0)
    X = M.values
    X = X - X.mean(0)
    X = X[:, X.std(0) > 0]
    C = np.corrcoef(X, rowvar=False)
    w = np.linalg.eigvalsh(C)[::-1]; w = w[w > 0]
    cum = np.cumsum(w)/w.sum()
    def ncomp(th): return int(np.searchsorted(cum, th)+1)
    print(f"PCA on {X.shape[1]} sampled base features, {X.shape[0]} obs")
    print(f"effective dimensionality: {ncomp(0.80)} PCs -> 80% var | {ncomp(0.90)} -> 90% | {ncomp(0.95)} -> 95%")
    print(f"top PC explains {w[0]/w.sum():.1%}; top 5 PCs explain {cum[4]:.1%}; top 10 {cum[9]:.1%}")


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "one": run_family(sys.argv[2])
    elif mode == "summary": summary()
    elif mode == "pca": pca()
