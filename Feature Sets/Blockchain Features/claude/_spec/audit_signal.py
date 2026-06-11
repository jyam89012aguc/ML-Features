"""
Crash-resistant real-data signal audit (per-family subprocess isolation).

The feature code uses pandas rolling().rank(), which can trigger a fatal
GIL/threading abort on this CPython3.12+pandas3 build. Mitigations:
  - force single-threaded numpy/pandas (env vars set BEFORE numpy import),
  - run each family in its own subprocess so any residual hard-crash is isolated.

Modes:
  python audit_signal.py panel           -> build panel cache (panel.pkl)
  python audit_signal.py one <family>    -> audit one family -> audit_parts/<fam>.json
  python audit_signal.py summary         -> aggregate -> audit_results.csv + printout
"""
import os
for _v in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS",
           "NUMEXPR_NUM_THREADS","VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
import sys, re, json, importlib.util, warnings
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")

DB = r"C:/Users/remoteuser/Downloads/trading.duckdb"
ROOT = r"D:/Features/claude"
PARTS = os.path.join(ROOT, "_spec", "audit_parts")
PKL = os.path.join(ROOT, "_spec", "panel.pkl")
START = pd.Timestamp("2019-01-01")
UNI = ['MARA','RIOT','CLSK','HUT','BITF','CIFR','WULF','HIVE','IREN','BTDR','CORZ',
       'BTBT','COIN','MSTR','CAN','BKKT','GREE','ARBK','SDIG','BTM','APLD']
FCOLS = ['revenue','revenueusd','netinc','ncfo','ncfi','ncff','ncfcommon','fcf','equity',
         'debt','assets','assetsc','liabilities','ebitda','ebit','gp','grossmargin','cor',
         'opex','opinc','sgna','rnd','capex','ppnenet','depamor','sharesbas','shareswa',
         'sbcomp','cashneq','currentratio','de','workingcapital','retearn','intangibles',
         'marketcap','ev','evebit','evebitda','pe','pb','ps']
OCOLS = ['shrvalue','shrunits','totalvalue','percentoftotal']


def build_panel():
    import duckdb, pickle
    con = duckdb.connect(DB, read_only=True)
    panel = {}
    for t in UNI:
        px = con.execute("SELECT date,open,high,low,close,closeadj,volume FROM sep_validated "
                         "WHERE ticker=? ORDER BY date", [t]).df()
        if len(px) < 300:
            continue
        px['date'] = pd.to_datetime(px['date']); px = px.set_index('date'); idx = px.index
        f = con.execute(f"SELECT datekey,{','.join(FCOLS)} FROM fundamentals_validated "
                        "WHERE ticker=? AND dimension='ARQ' ORDER BY datekey", [t]).df()
        if len(f):
            f['datekey'] = pd.to_datetime(f['datekey']); f = f.set_index('datekey')
            f = f[~f.index.duplicated(keep='last')]
            fd = f.reindex(idx.union(f.index)).sort_index().ffill().reindex(idx)
        else:
            fd = pd.DataFrame(index=idx, columns=FCOLS, dtype=float)
        o = con.execute(f"SELECT calendardate,{','.join(OCOLS)} FROM sf3a "
                        "WHERE ticker=? ORDER BY calendardate", [t]).df()
        if len(o):
            o['calendardate'] = pd.to_datetime(o['calendardate']) + pd.Timedelta(days=45)
            o = o.set_index('calendardate'); o = o[~o.index.duplicated(keep='last')]
            od = o.reindex(idx.union(o.index)).sort_index().ffill().reindex(idx)
        else:
            od = pd.DataFrame(index=idx, columns=OCOLS, dtype=float)
        df = pd.DataFrame(index=idx)
        for c in ['open','high','low','close','closeadj','volume']: df[c] = px[c].astype(float)
        for c in FCOLS: df[c] = fd[c].astype(float).values
        for c in OCOLS: df[c] = od[c].astype(float).values
        panel[t] = df
    con.close()
    with open(PKL, "wb") as fh:
        pickle.dump(panel, fh)
    print("panel built:", list(panel.keys()))


def load_panel():
    import pickle
    with open(PKL, "rb") as fh:
        return pickle.load(fh)


def family_base_files(fam):
    folder = os.path.join(ROOT, fam)
    return [os.path.join(folder, f) for f in sorted(os.listdir(folder))
            if f.endswith('claude.py') and '_base_' in f]


def load_registry(path):
    fam = os.path.basename(os.path.dirname(path))
    spec = importlib.util.spec_from_file_location(fam+os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.REGISTRY


def audit_one(fam):
    panel = load_panel()
    tickers = list(panel.keys())
    feats = {}
    for path in family_base_files(fam):
        feats.update(load_registry(path))
    names = list(feats.keys())
    contam = {n: [] for n in names}
    nanfrac = {n: [] for n in names}
    ic_store = {n: [] for n in names}     # rows: date, val, fwd252
    pooled = {n: [] for n in names}
    for t in tickers:
        df = panel[t]; idx = df.index
        cols = {c: df[c] for c in df.columns}
        ca = df['closeadj']; logp = np.log(ca.replace(0, np.nan))
        fwd252 = ca.shift(-252)/ca - 1.0
        mser = pd.Series(idx, index=idx)
        post = mser[idx >= START]
        if len(post) < 60:
            continue
        sample_idx = post.groupby(post.dt.to_period('M')).last()
        pos = idx.get_indexer(pd.DatetimeIndex(sample_idx.values))
        for n in names:
            meta = feats[n]
            try:
                y = meta['func'](*[cols[c] for c in meta['inputs']]).replace([np.inf,-np.inf], np.nan)
            except Exception:
                continue
            ywin = y[idx >= START]
            nanfrac[n].append(float(ywin.isna().mean()))
            m = y.notna() & logp.notna()
            if m.sum() > 100 and y[m].std() > 0:
                contam[n].append(abs(np.corrcoef(y[m].values, logp[m].values)[0, 1]))
            v = y.iloc[pos].values; r = fwd252.iloc[pos].values
            ic_store[n].append(pd.DataFrame({'d': sample_idx.index.values, 'v': v, 'r': r}))
            if ywin.notna().sum() > 50 and ywin.std() > 0:
                pooled[n].append(((ywin - ywin.mean())/ywin.std()).reset_index(drop=True))
    # aggregate
    res = {}
    for n in names:
        ic_mean = ic_ir = np.nan
        if ic_store[n]:
            d = pd.concat(ic_store[n]).dropna()
            ics = []
            for dd, g in d.groupby('d'):
                if len(g) >= 4 and g['v'].nunique() >= 4 and g['r'].nunique() >= 4:
                    ics.append(g['v'].rank().corr(g['r'].rank()))
            ics = [x for x in ics if pd.notna(x)]
            if len(ics) >= 6:
                a = np.array(ics); ic_mean = float(a.mean()); ic_ir = float(a.mean()/(a.std()+1e-9)*np.sqrt(len(a)))
        res[n] = dict(contam=(float(np.mean(contam[n])) if contam[n] else None),
                      nan=(float(np.mean(nanfrac[n])) if nanfrac[n] else None),
                      ic=ic_mean if ic_mean==ic_mean else None,
                      icir=ic_ir if ic_ir==ic_ir else None)
    # redundancy
    red = pct95 = None
    try:
        M = pd.DataFrame({n: pd.concat(pooled[n], ignore_index=True) for n in names if pooled[n]})
        C = M.corr().abs().values
        iu = np.triu_indices_from(C, 1); offs = C[iu]; offs = offs[~np.isnan(offs)]
        red = float(np.mean(offs)); pct95 = float(np.mean(offs > 0.95))
    except Exception:
        pass
    os.makedirs(PARTS, exist_ok=True)
    out = dict(family=fam, n=len(names), redund=red, pct_dup95=pct95, feats=res)
    with open(os.path.join(PARTS, fam + ".json"), "w") as fh:
        json.dump(out, fh)
    # one-line summary
    cont = np.array([res[n]['contam'] for n in names if res[n]['contam'] is not None])
    nn = np.array([res[n]['nan'] for n in names if res[n]['nan'] is not None])
    icir = np.array([res[n]['icir'] for n in names if res[n]['icir'] is not None])
    icv = np.array([res[n]['ic'] for n in names if res[n]['ic'] is not None])
    print(f"{fam:34} contam(med|>.9)={np.median(cont):.2f}|{np.mean(cont>0.9):.0%}  "
          f"redund={red:.2f} dup95={pct95:.0%}  nan={np.median(nn):.0%}  "
          f"|ic|med={np.median(np.abs(icv)):.3f} strong(|IR|>2)={np.mean(np.abs(icir)>2):.0%} "
          f"best|ic|={np.max(np.abs(icv)) if len(icv) else float('nan'):.3f}")


def summary():
    rows = []
    for fn in sorted(os.listdir(PARTS)):
        if not fn.endswith(".json"): continue
        d = json.load(open(os.path.join(PARTS, fn)))
        res = d['feats']; names = list(res)
        cont = np.array([res[n]['contam'] for n in names if res[n]['contam'] is not None])
        nn = np.array([res[n]['nan'] for n in names if res[n]['nan'] is not None])
        icir = np.array([res[n]['icir'] for n in names if res[n]['icir'] is not None])
        icv = np.array([res[n]['ic'] for n in names if res[n]['ic'] is not None])
        rows.append(dict(family=d['family'], n=d['n'],
            contam_med=float(np.median(cont)) if len(cont) else np.nan,
            contam_hi=float(np.mean(cont>0.9)) if len(cont) else np.nan,
            redund=d['redund'], dup95=d['pct_dup95'],
            nan_med=float(np.median(nn)) if len(nn) else np.nan,
            ic_absmed=float(np.median(np.abs(icv))) if len(icv) else np.nan,
            ic_strong=float(np.mean(np.abs(icir)>2)) if len(icir) else np.nan,
            best_ic=float(np.max(np.abs(icv))) if len(icv) else np.nan))
    df = pd.DataFrame(rows).sort_values('family')
    df.to_csv(os.path.join(ROOT, "_spec", "audit_results.csv"), index=False)
    pd.set_option('display.width', 200); pd.set_option('display.max_rows', 40)
    print(df.to_string(index=False, float_format=lambda x: f"{x:.3f}"))
    print("\n==== OVERALL (30 families) ====")
    print(f"families audited: {len(df)}")
    print(f"median price-contamination: {df['contam_med'].median():.2f}")
    print(f"families >50% feats contaminated(>.9): {(df['contam_hi']>0.5).sum()}/{len(df)}")
    print(f"median within-family redundancy |corr|: {df['redund'].median():.2f}")
    print(f"median %% near-dup pairs (>.95): {df['dup95'].median():.0%}")
    print(f"median NaN fraction: {df['nan_med'].median():.0%}")
    print(f"median share strong-IC feats (|IR|>2) vs fwd252: {df['ic_strong'].median():.0%}")
    print(f"families with >=15%% strong-IC feats: {(df['ic_strong']>=0.15).sum()}/{len(df)}")


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "panel": build_panel()
    elif mode == "one": audit_one(sys.argv[2])
    elif mode == "summary": summary()
