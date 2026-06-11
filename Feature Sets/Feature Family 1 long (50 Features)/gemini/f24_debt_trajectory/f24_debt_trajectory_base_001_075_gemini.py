import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
def _z(s, w): return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)

def _dt_ratio(num, den):
    return num / den.replace(0, np.nan)

def _dt_pct_chg(s, w):
    return s.pct_change(w)

def _dt_zscore(s, w):
    return _z(s, w)

# 63d average of Debt to Assets ratio for debt trajectory
def f24_debt_trajectory_debt_assets_63d_base_v001_signal(debt, assets) -> pd.Series:
    res = _sma(_dt_ratio(debt, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of Debt to Assets ratio for debt trajectory
def f24_debt_trajectory_debt_assets_126d_base_v002_signal(debt, assets) -> pd.Series:
    res = _sma(_dt_ratio(debt, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of Debt to Assets ratio for debt trajectory
def f24_debt_trajectory_debt_assets_252d_base_v003_signal(debt, assets) -> pd.Series:
    res = _sma(_dt_ratio(debt, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of Debt to Assets ratio for debt trajectory
def f24_debt_trajectory_debt_assets_504d_base_v004_signal(debt, assets) -> pd.Series:
    res = _sma(_dt_ratio(debt, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of Debt to Assets ratio for debt trajectory
def f24_debt_trajectory_debt_assets_756d_base_v005_signal(debt, assets) -> pd.Series:
    res = _sma(_dt_ratio(debt, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of Debt to Assets ratio for debt trajectory
def f24_debt_trajectory_debt_assets_1260d_base_v006_signal(debt, assets) -> pd.Series:
    res = _sma(_dt_ratio(debt, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of Debt to Equity ratio for debt trajectory
def f24_debt_trajectory_debt_equity_63d_base_v007_signal(debt, equity) -> pd.Series:
    res = _sma(_dt_ratio(debt, equity), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of Debt to Equity ratio for debt trajectory
def f24_debt_trajectory_debt_equity_126d_base_v008_signal(debt, equity) -> pd.Series:
    res = _sma(_dt_ratio(debt, equity), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of Debt to Equity ratio for debt trajectory
def f24_debt_trajectory_debt_equity_252d_base_v009_signal(debt, equity) -> pd.Series:
    res = _sma(_dt_ratio(debt, equity), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of Debt to Equity ratio for debt trajectory
def f24_debt_trajectory_debt_equity_504d_base_v010_signal(debt, equity) -> pd.Series:
    res = _sma(_dt_ratio(debt, equity), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of Debt to Equity ratio for debt trajectory
def f24_debt_trajectory_debt_equity_756d_base_v011_signal(debt, equity) -> pd.Series:
    res = _sma(_dt_ratio(debt, equity), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of Debt to Equity ratio for debt trajectory
def f24_debt_trajectory_debt_equity_1260d_base_v012_signal(debt, equity) -> pd.Series:
    res = _sma(_dt_ratio(debt, equity), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of Debt to EBITDA ratio for debt trajectory
def f24_debt_trajectory_debt_ebitda_63d_base_v013_signal(debt, ebitda) -> pd.Series:
    res = _sma(_dt_ratio(debt, ebitda), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of Debt to EBITDA ratio for debt trajectory
def f24_debt_trajectory_debt_ebitda_126d_base_v014_signal(debt, ebitda) -> pd.Series:
    res = _sma(_dt_ratio(debt, ebitda), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of Debt to EBITDA ratio for debt trajectory
def f24_debt_trajectory_debt_ebitda_252d_base_v015_signal(debt, ebitda) -> pd.Series:
    res = _sma(_dt_ratio(debt, ebitda), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of Debt to EBITDA ratio for debt trajectory
def f24_debt_trajectory_debt_ebitda_504d_base_v016_signal(debt, ebitda) -> pd.Series:
    res = _sma(_dt_ratio(debt, ebitda), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of Debt to EBITDA ratio for debt trajectory
def f24_debt_trajectory_debt_ebitda_756d_base_v017_signal(debt, ebitda) -> pd.Series:
    res = _sma(_dt_ratio(debt, ebitda), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of Debt to EBITDA ratio for debt trajectory
def f24_debt_trajectory_debt_ebitda_1260d_base_v018_signal(debt, ebitda) -> pd.Series:
    res = _sma(_dt_ratio(debt, ebitda), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d percentage change of Debt for debt trajectory
def f24_debt_trajectory_debt_growth_63d_base_v019_signal(debt) -> pd.Series:
    res = _dt_pct_chg(debt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d percentage change of Debt for debt trajectory
def f24_debt_trajectory_debt_growth_126d_base_v020_signal(debt) -> pd.Series:
    res = _dt_pct_chg(debt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d percentage change of Debt for debt trajectory
def f24_debt_trajectory_debt_growth_252d_base_v021_signal(debt) -> pd.Series:
    res = _dt_pct_chg(debt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d percentage change of Debt for debt trajectory
def f24_debt_trajectory_debt_growth_504d_base_v022_signal(debt) -> pd.Series:
    res = _dt_pct_chg(debt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d percentage change of Debt for debt trajectory
def f24_debt_trajectory_debt_growth_756d_base_v023_signal(debt) -> pd.Series:
    res = _dt_pct_chg(debt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d percentage change of Debt for debt trajectory
def f24_debt_trajectory_debt_growth_1260d_base_v024_signal(debt) -> pd.Series:
    res = _dt_pct_chg(debt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of Liabilities to Assets ratio for debt trajectory
def f24_debt_trajectory_liab_assets_63d_base_v025_signal(liabilities, assets) -> pd.Series:
    res = _sma(_dt_ratio(liabilities, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of Liabilities to Assets ratio for debt trajectory
def f24_debt_trajectory_liab_assets_126d_base_v026_signal(liabilities, assets) -> pd.Series:
    res = _sma(_dt_ratio(liabilities, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of Liabilities to Assets ratio for debt trajectory
def f24_debt_trajectory_liab_assets_252d_base_v027_signal(liabilities, assets) -> pd.Series:
    res = _sma(_dt_ratio(liabilities, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of Liabilities to Assets ratio for debt trajectory
def f24_debt_trajectory_liab_assets_504d_base_v028_signal(liabilities, assets) -> pd.Series:
    res = _sma(_dt_ratio(liabilities, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of Liabilities to Assets ratio for debt trajectory
def f24_debt_trajectory_liab_assets_756d_base_v029_signal(liabilities, assets) -> pd.Series:
    res = _sma(_dt_ratio(liabilities, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of Liabilities to Assets ratio for debt trajectory
def f24_debt_trajectory_liab_assets_1260d_base_v030_signal(liabilities, assets) -> pd.Series:
    res = _sma(_dt_ratio(liabilities, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d percentage change of Liabilities for debt trajectory
def f24_debt_trajectory_liab_growth_63d_base_v031_signal(liabilities) -> pd.Series:
    res = _dt_pct_chg(liabilities, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d percentage change of Liabilities for debt trajectory
def f24_debt_trajectory_liab_growth_126d_base_v032_signal(liabilities) -> pd.Series:
    res = _dt_pct_chg(liabilities, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d percentage change of Liabilities for debt trajectory
def f24_debt_trajectory_liab_growth_252d_base_v033_signal(liabilities) -> pd.Series:
    res = _dt_pct_chg(liabilities, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d percentage change of Liabilities for debt trajectory
def f24_debt_trajectory_liab_growth_504d_base_v034_signal(liabilities) -> pd.Series:
    res = _dt_pct_chg(liabilities, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d percentage change of Liabilities for debt trajectory
def f24_debt_trajectory_liab_growth_756d_base_v035_signal(liabilities) -> pd.Series:
    res = _dt_pct_chg(liabilities, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d percentage change of Liabilities for debt trajectory
def f24_debt_trajectory_liab_growth_1260d_base_v036_signal(liabilities) -> pd.Series:
    res = _dt_pct_chg(liabilities, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of Debt to Revenue ratio for debt trajectory
def f24_debt_trajectory_debt_rev_63d_base_v037_signal(debt, revenue) -> pd.Series:
    res = _sma(_dt_ratio(debt, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of Debt to Revenue ratio for debt trajectory
def f24_debt_trajectory_debt_rev_126d_base_v038_signal(debt, revenue) -> pd.Series:
    res = _sma(_dt_ratio(debt, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of Debt to Revenue ratio for debt trajectory
def f24_debt_trajectory_debt_rev_252d_base_v039_signal(debt, revenue) -> pd.Series:
    res = _sma(_dt_ratio(debt, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of Debt to Revenue ratio for debt trajectory
def f24_debt_trajectory_debt_rev_504d_base_v040_signal(debt, revenue) -> pd.Series:
    res = _sma(_dt_ratio(debt, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of Debt to Revenue ratio for debt trajectory
def f24_debt_trajectory_debt_rev_756d_base_v041_signal(debt, revenue) -> pd.Series:
    res = _sma(_dt_ratio(debt, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of Debt to Revenue ratio for debt trajectory
def f24_debt_trajectory_debt_rev_1260d_base_v042_signal(debt, revenue) -> pd.Series:
    res = _sma(_dt_ratio(debt, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of Working Capital to Debt ratio for debt trajectory
def f24_debt_trajectory_wc_debt_63d_base_v043_signal(workingcapital, debt) -> pd.Series:
    res = _sma(_dt_ratio(workingcapital, debt), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of Working Capital to Debt ratio for debt trajectory
def f24_debt_trajectory_wc_debt_126d_base_v044_signal(workingcapital, debt) -> pd.Series:
    res = _sma(_dt_ratio(workingcapital, debt), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of Working Capital to Debt ratio for debt trajectory
def f24_debt_trajectory_wc_debt_252d_base_v045_signal(workingcapital, debt) -> pd.Series:
    res = _sma(_dt_ratio(workingcapital, debt), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of Working Capital to Debt ratio for debt trajectory
def f24_debt_trajectory_wc_debt_504d_base_v046_signal(workingcapital, debt) -> pd.Series:
    res = _sma(_dt_ratio(workingcapital, debt), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of Working Capital to Debt ratio for debt trajectory
def f24_debt_trajectory_wc_debt_756d_base_v047_signal(workingcapital, debt) -> pd.Series:
    res = _sma(_dt_ratio(workingcapital, debt), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of Working Capital to Debt ratio for debt trajectory
def f24_debt_trajectory_wc_debt_1260d_base_v048_signal(workingcapital, debt) -> pd.Series:
    res = _sma(_dt_ratio(workingcapital, debt), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of Debt to Working Capital ratio for debt trajectory
def f24_debt_trajectory_debt_wc_63d_base_v049_signal(debt, workingcapital) -> pd.Series:
    res = _sma(_dt_ratio(debt, workingcapital), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of Debt to Working Capital ratio for debt trajectory
def f24_debt_trajectory_debt_wc_126d_base_v050_signal(debt, workingcapital) -> pd.Series:
    res = _sma(_dt_ratio(debt, workingcapital), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of Debt to Working Capital ratio for debt trajectory
def f24_debt_trajectory_debt_wc_252d_base_v051_signal(debt, workingcapital) -> pd.Series:
    res = _sma(_dt_ratio(debt, workingcapital), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of Debt to Working Capital ratio for debt trajectory
def f24_debt_trajectory_debt_wc_504d_base_v052_signal(debt, workingcapital) -> pd.Series:
    res = _sma(_dt_ratio(debt, workingcapital), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of Debt to Working Capital ratio for debt trajectory
def f24_debt_trajectory_debt_wc_756d_base_v053_signal(debt, workingcapital) -> pd.Series:
    res = _sma(_dt_ratio(debt, workingcapital), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of Debt to Working Capital ratio for debt trajectory
def f24_debt_trajectory_debt_wc_1260d_base_v054_signal(debt, workingcapital) -> pd.Series:
    res = _sma(_dt_ratio(debt, workingcapital), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d z-score of Debt to Assets ratio for debt trajectory
def f24_debt_trajectory_debt_assets_zscore_63d_base_v055_signal(debt, assets) -> pd.Series:
    res = _dt_zscore(_dt_ratio(debt, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d z-score of Debt to Assets ratio for debt trajectory
def f24_debt_trajectory_debt_assets_zscore_126d_base_v056_signal(debt, assets) -> pd.Series:
    res = _dt_zscore(_dt_ratio(debt, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d z-score of Debt to Assets ratio for debt trajectory
def f24_debt_trajectory_debt_assets_zscore_252d_base_v057_signal(debt, assets) -> pd.Series:
    res = _dt_zscore(_dt_ratio(debt, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d z-score of Debt to Assets ratio for debt trajectory
def f24_debt_trajectory_debt_assets_zscore_504d_base_v058_signal(debt, assets) -> pd.Series:
    res = _dt_zscore(_dt_ratio(debt, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d z-score of Debt to Assets ratio for debt trajectory
def f24_debt_trajectory_debt_assets_zscore_756d_base_v059_signal(debt, assets) -> pd.Series:
    res = _dt_zscore(_dt_ratio(debt, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d z-score of Debt to Assets ratio for debt trajectory
def f24_debt_trajectory_debt_assets_zscore_1260d_base_v060_signal(debt, assets) -> pd.Series:
    res = _dt_zscore(_dt_ratio(debt, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of Debt to Operating Income ratio for debt trajectory
def f24_debt_trajectory_debt_opinc_63d_base_v061_signal(debt, opinc) -> pd.Series:
    res = _sma(_dt_ratio(debt, opinc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of Debt to Operating Income ratio for debt trajectory
def f24_debt_trajectory_debt_opinc_126d_base_v062_signal(debt, opinc) -> pd.Series:
    res = _sma(_dt_ratio(debt, opinc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of Debt to Operating Income ratio for debt trajectory
def f24_debt_trajectory_debt_opinc_252d_base_v063_signal(debt, opinc) -> pd.Series:
    res = _sma(_dt_ratio(debt, opinc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of Debt to Operating Income ratio for debt trajectory
def f24_debt_trajectory_debt_opinc_504d_base_v064_signal(debt, opinc) -> pd.Series:
    res = _sma(_dt_ratio(debt, opinc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of Debt to Operating Income ratio for debt trajectory
def f24_debt_trajectory_debt_opinc_756d_base_v065_signal(debt, opinc) -> pd.Series:
    res = _sma(_dt_ratio(debt, opinc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of Debt to Operating Income ratio for debt trajectory
def f24_debt_trajectory_debt_opinc_1260d_base_v066_signal(debt, opinc) -> pd.Series:
    res = _sma(_dt_ratio(debt, opinc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d z-score of Debt for debt trajectory
def f24_debt_trajectory_debt_zscore_63d_base_v067_signal(debt) -> pd.Series:
    res = _dt_zscore(debt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d z-score of Debt for debt trajectory
def f24_debt_trajectory_debt_zscore_126d_base_v068_signal(debt) -> pd.Series:
    res = _dt_zscore(debt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d z-score of Debt for debt trajectory
def f24_debt_trajectory_debt_zscore_252d_base_v069_signal(debt) -> pd.Series:
    res = _dt_zscore(debt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d z-score of Debt for debt trajectory
def f24_debt_trajectory_debt_zscore_504d_base_v070_signal(debt) -> pd.Series:
    res = _dt_zscore(debt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d z-score of Debt for debt trajectory
def f24_debt_trajectory_debt_zscore_756d_base_v071_signal(debt) -> pd.Series:
    res = _dt_zscore(debt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d z-score of Debt for debt trajectory
def f24_debt_trajectory_debt_zscore_1260d_base_v072_signal(debt) -> pd.Series:
    res = _dt_zscore(debt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of Debt to Net Income ratio for debt trajectory
def f24_debt_trajectory_debt_netinc_252d_base_v073_signal(debt, netinc) -> pd.Series:
    res = _sma(_dt_ratio(debt, netinc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of Debt to Net Income ratio for debt trajectory
def f24_debt_trajectory_debt_netinc_504d_base_v074_signal(debt, netinc) -> pd.Series:
    res = _sma(_dt_ratio(debt, netinc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of Debt to Net Income ratio for debt trajectory
def f24_debt_trajectory_debt_netinc_756d_base_v075_signal(debt, netinc) -> pd.Series:
    res = _sma(_dt_ratio(debt, netinc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "debt": np.random.normal(100, 20, n),
        "assets": np.random.normal(500, 50, n),
        "equity": np.random.normal(300, 30, n),
        "ebitda": np.random.normal(50, 10, n),
        "revenue": np.random.normal(400, 40, n),
        "workingcapital": np.random.normal(100, 20, n),
        "opinc": np.random.normal(40, 8, n),
        "netinc": np.random.normal(30, 6, n),
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f24_debt_trajectory_"))]
    
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        y2 = func(*args)
        pd.testing.assert_series_equal(y1, y2)
        
        q = y1.iloc[504:].dropna()
        assert len(q) > 0
        assert q.nunique() > 50
        assert q.std() > 0
        assert not q.isna().all()
        
        source = inspect.getsource(func)
        assert any(prim in source for prim in ["_dt_ratio", "_dt_pct_chg", "_dt_zscore"])

    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f24_debt_trajectory_"))]}
F24_DEBT_TRAJECTORY_REGISTRY_001_075 = REGISTRY
