import pandas as pd
import numpy as np

def _rg_growth(s, w): return s.pct_change(w)
def _rg_zscore(s, w): return (s - s.rolling(w, min_periods=1).mean()) / s.rolling(w, min_periods=1).std().replace(0, np.nan)
def _rg_sma(s, w): return s.rolling(w, min_periods=1).mean()
def _rg_vol(s, w): return s.rolling(w, min_periods=1).std()

def f21_revenue_growth_revenue_growth_63d_base_v001_signal(arg_revenue) -> pd.Series:
    res = _rg_growth(arg_revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_revenue_growth_126d_base_v002_signal(arg_revenue) -> pd.Series:
    res = _rg_growth(arg_revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_revenue_growth_252d_base_v003_signal(arg_revenue) -> pd.Series:
    res = _rg_growth(arg_revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_revenue_growth_504d_base_v004_signal(arg_revenue) -> pd.Series:
    res = _rg_growth(arg_revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_revenue_growth_756d_base_v005_signal(arg_revenue) -> pd.Series:
    res = _rg_growth(arg_revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_revenue_growth_1260d_base_v006_signal(arg_revenue) -> pd.Series:
    res = _rg_growth(arg_revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_assets_growth_63d_base_v007_signal(arg_assets) -> pd.Series:
    res = _rg_growth(arg_assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_assets_growth_126d_base_v008_signal(arg_assets) -> pd.Series:
    res = _rg_growth(arg_assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_assets_growth_252d_base_v009_signal(arg_assets) -> pd.Series:
    res = _rg_growth(arg_assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_assets_growth_504d_base_v010_signal(arg_assets) -> pd.Series:
    res = _rg_growth(arg_assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_assets_growth_756d_base_v011_signal(arg_assets) -> pd.Series:
    res = _rg_growth(arg_assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_assets_growth_1260d_base_v012_signal(arg_assets) -> pd.Series:
    res = _rg_growth(arg_assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_growth_63d_base_v013_signal(arg_netinc) -> pd.Series:
    res = _rg_growth(arg_netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_growth_126d_base_v014_signal(arg_netinc) -> pd.Series:
    res = _rg_growth(arg_netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_growth_252d_base_v015_signal(arg_netinc) -> pd.Series:
    res = _rg_growth(arg_netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_growth_504d_base_v016_signal(arg_netinc) -> pd.Series:
    res = _rg_growth(arg_netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_growth_756d_base_v017_signal(arg_netinc) -> pd.Series:
    res = _rg_growth(arg_netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_growth_1260d_base_v018_signal(arg_netinc) -> pd.Series:
    res = _rg_growth(arg_netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_per_share_growth_63d_base_v019_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_per_share_growth_126d_base_v020_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_per_share_growth_252d_base_v021_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_per_share_growth_504d_base_v022_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_per_share_growth_756d_base_v023_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_per_share_growth_1260d_base_v024_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_assets_growth_63d_base_v025_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rg_growth(arg_revenue / arg_assets.replace(0, np.nan), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_assets_growth_126d_base_v026_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rg_growth(arg_revenue / arg_assets.replace(0, np.nan), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_assets_growth_252d_base_v027_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rg_growth(arg_revenue / arg_assets.replace(0, np.nan), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_assets_growth_504d_base_v028_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rg_growth(arg_revenue / arg_assets.replace(0, np.nan), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_assets_growth_756d_base_v029_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rg_growth(arg_revenue / arg_assets.replace(0, np.nan), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_assets_growth_1260d_base_v030_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rg_growth(arg_revenue / arg_assets.replace(0, np.nan), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_roa_growth_63d_base_v031_signal(arg_netinc, arg_assets) -> pd.Series:
    res = _rg_growth(arg_netinc / arg_assets.replace(0, np.nan), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_roa_growth_126d_base_v032_signal(arg_netinc, arg_assets) -> pd.Series:
    res = _rg_growth(arg_netinc / arg_assets.replace(0, np.nan), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_roa_growth_252d_base_v033_signal(arg_netinc, arg_assets) -> pd.Series:
    res = _rg_growth(arg_netinc / arg_assets.replace(0, np.nan), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_roa_growth_504d_base_v034_signal(arg_netinc, arg_assets) -> pd.Series:
    res = _rg_growth(arg_netinc / arg_assets.replace(0, np.nan), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_roa_growth_756d_base_v035_signal(arg_netinc, arg_assets) -> pd.Series:
    res = _rg_growth(arg_netinc / arg_assets.replace(0, np.nan), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_roa_growth_1260d_base_v036_signal(arg_netinc, arg_assets) -> pd.Series:
    res = _rg_growth(arg_netinc / arg_assets.replace(0, np.nan), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_net_margin_growth_63d_base_v037_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _rg_growth(arg_netinc / arg_revenue.replace(0, np.nan), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_net_margin_growth_126d_base_v038_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _rg_growth(arg_netinc / arg_revenue.replace(0, np.nan), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_net_margin_growth_252d_base_v039_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _rg_growth(arg_netinc / arg_revenue.replace(0, np.nan), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_net_margin_growth_504d_base_v040_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _rg_growth(arg_netinc / arg_revenue.replace(0, np.nan), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_net_margin_growth_756d_base_v041_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _rg_growth(arg_netinc / arg_revenue.replace(0, np.nan), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_net_margin_growth_1260d_base_v042_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _rg_growth(arg_netinc / arg_revenue.replace(0, np.nan), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_rev_growth_63d_base_v043_signal(arg_revenue) -> pd.Series:
    res = _rg_zscore(_rg_growth(arg_revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_rev_growth_126d_base_v044_signal(arg_revenue) -> pd.Series:
    res = _rg_zscore(_rg_growth(arg_revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_rev_growth_252d_base_v045_signal(arg_revenue) -> pd.Series:
    res = _rg_zscore(_rg_growth(arg_revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_rev_growth_504d_base_v046_signal(arg_revenue) -> pd.Series:
    res = _rg_zscore(_rg_growth(arg_revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_rev_growth_756d_base_v047_signal(arg_revenue) -> pd.Series:
    res = _rg_zscore(_rg_growth(arg_revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_rev_growth_1260d_base_v048_signal(arg_revenue) -> pd.Series:
    res = _rg_zscore(_rg_growth(arg_revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_assets_growth_63d_base_v049_signal(arg_assets) -> pd.Series:
    res = _rg_zscore(_rg_growth(arg_assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_assets_growth_126d_base_v050_signal(arg_assets) -> pd.Series:
    res = _rg_zscore(_rg_growth(arg_assets, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_assets_growth_252d_base_v051_signal(arg_assets) -> pd.Series:
    res = _rg_zscore(_rg_growth(arg_assets, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_assets_growth_504d_base_v052_signal(arg_assets) -> pd.Series:
    res = _rg_zscore(_rg_growth(arg_assets, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_assets_growth_756d_base_v053_signal(arg_assets) -> pd.Series:
    res = _rg_zscore(_rg_growth(arg_assets, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_assets_growth_1260d_base_v054_signal(arg_assets) -> pd.Series:
    res = _rg_zscore(_rg_growth(arg_assets, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_netinc_growth_63d_base_v055_signal(arg_netinc) -> pd.Series:
    res = _rg_zscore(_rg_growth(arg_netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_netinc_growth_126d_base_v056_signal(arg_netinc) -> pd.Series:
    res = _rg_zscore(_rg_growth(arg_netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_netinc_growth_252d_base_v057_signal(arg_netinc) -> pd.Series:
    res = _rg_zscore(_rg_growth(arg_netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_netinc_growth_504d_base_v058_signal(arg_netinc) -> pd.Series:
    res = _rg_zscore(_rg_growth(arg_netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_netinc_growth_756d_base_v059_signal(arg_netinc) -> pd.Series:
    res = _rg_zscore(_rg_growth(arg_netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_netinc_growth_1260d_base_v060_signal(arg_netinc) -> pd.Series:
    res = _rg_zscore(_rg_growth(arg_netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_rev_shares_growth_63d_base_v061_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _rg_zscore(_rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_rev_shares_growth_126d_base_v062_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _rg_zscore(_rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_rev_shares_growth_252d_base_v063_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _rg_zscore(_rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_rev_shares_growth_504d_base_v064_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _rg_zscore(_rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_rev_shares_growth_756d_base_v065_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _rg_zscore(_rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_rev_shares_growth_1260d_base_v066_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _rg_zscore(_rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_rev_growth_63d_base_v067_signal(arg_revenue) -> pd.Series:
    res = _rg_sma(_rg_growth(arg_revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_rev_growth_126d_base_v068_signal(arg_revenue) -> pd.Series:
    res = _rg_sma(_rg_growth(arg_revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_rev_growth_252d_base_v069_signal(arg_revenue) -> pd.Series:
    res = _rg_sma(_rg_growth(arg_revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_rev_growth_504d_base_v070_signal(arg_revenue) -> pd.Series:
    res = _rg_sma(_rg_growth(arg_revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_rev_growth_756d_base_v071_signal(arg_revenue) -> pd.Series:
    res = _rg_sma(_rg_growth(arg_revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_rev_growth_1260d_base_v072_signal(arg_revenue) -> pd.Series:
    res = _rg_sma(_rg_growth(arg_revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_assets_growth_63d_base_v073_signal(arg_assets) -> pd.Series:
    res = _rg_sma(_rg_growth(arg_assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_assets_growth_126d_base_v074_signal(arg_assets) -> pd.Series:
    res = _rg_sma(_rg_growth(arg_assets, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_assets_growth_252d_base_v075_signal(arg_assets) -> pd.Series:
    res = _rg_sma(_rg_growth(arg_assets, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c.replace('arg_', '')}" for c in ["arg_revenue", "arg_assets", "arg_netinc", "arg_shareswa"]}

F21_REVENUE_GROWTH_BASE_REGISTRY_001_075 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted([f for f in globals() if f.startswith('f21_revenue_growth_') and f.endswith('_signal')])
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 5000
    np.random.seed(42)
    steps = 20
    step_size = sz // steps
    base_rev = np.repeat(np.random.lognormal(10, 1, steps), step_size)
    if len(base_rev) < sz:
        base_rev = np.concatenate([base_rev, [base_rev[-1]] * (sz - len(base_rev))])
    
    d = pd.DataFrame({
        "arg_revenue": pd.Series(base_rev * (1 + np.random.normal(0, 0.05, sz))),
        "arg_assets": pd.Series(base_rev * np.random.uniform(0.5, 2.0, sz)),
        "arg_netinc": pd.Series(base_rev * np.random.uniform(-0.1, 0.2, sz)),
        "arg_shareswa": pd.Series(np.ones(sz) * 1e6),
        "ticker": ["T"]*sz,
        "date": pd.date_range("2010-01-01", periods=sz)
    })
    for n, c in F21_REVENUE_GROWTH_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert len(r) > 0, f"{n} failed len"
        assert r.nunique() > 2, f"{n} failed nunique: {r.nunique()}"
        assert r.std() > 0, f"{n} failed std: {r.std()}"
    print(f"OK")
