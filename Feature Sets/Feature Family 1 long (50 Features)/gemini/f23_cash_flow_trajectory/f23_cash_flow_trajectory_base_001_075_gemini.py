import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
def _z(s, w): return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)

def _cft_ratio(num, den):
    return num / den.replace(0, np.nan)

def _cft_pct_chg(s, w):
    return s.pct_change(w)

def _cft_zscore(s, w):
    return _z(s, w)

# 63d average of FCF to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_rev_63d_base_v001_signal(fcf, revenue) -> pd.Series:
    res = _sma(_cft_ratio(fcf, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of FCF to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_rev_126d_base_v002_signal(fcf, revenue) -> pd.Series:
    res = _sma(_cft_ratio(fcf, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of FCF to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_rev_252d_base_v003_signal(fcf, revenue) -> pd.Series:
    res = _sma(_cft_ratio(fcf, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of FCF to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_rev_504d_base_v004_signal(fcf, revenue) -> pd.Series:
    res = _sma(_cft_ratio(fcf, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of FCF to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_rev_756d_base_v005_signal(fcf, revenue) -> pd.Series:
    res = _sma(_cft_ratio(fcf, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of FCF to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_rev_1260d_base_v006_signal(fcf, revenue) -> pd.Series:
    res = _sma(_cft_ratio(fcf, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of FCF to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_assets_63d_base_v007_signal(fcf, assets) -> pd.Series:
    res = _sma(_cft_ratio(fcf, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of FCF to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_assets_126d_base_v008_signal(fcf, assets) -> pd.Series:
    res = _sma(_cft_ratio(fcf, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of FCF to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_assets_252d_base_v009_signal(fcf, assets) -> pd.Series:
    res = _sma(_cft_ratio(fcf, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of FCF to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_assets_504d_base_v010_signal(fcf, assets) -> pd.Series:
    res = _sma(_cft_ratio(fcf, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of FCF to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_assets_756d_base_v011_signal(fcf, assets) -> pd.Series:
    res = _sma(_cft_ratio(fcf, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of FCF to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_assets_1260d_base_v012_signal(fcf, assets) -> pd.Series:
    res = _sma(_cft_ratio(fcf, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of NCFO to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_rev_63d_base_v013_signal(ncfo, revenue) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of NCFO to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_rev_126d_base_v014_signal(ncfo, revenue) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of NCFO to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_rev_252d_base_v015_signal(ncfo, revenue) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of NCFO to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_rev_504d_base_v016_signal(ncfo, revenue) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of NCFO to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_rev_756d_base_v017_signal(ncfo, revenue) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of NCFO to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_rev_1260d_base_v018_signal(ncfo, revenue) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of NCFO to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_assets_63d_base_v019_signal(ncfo, assets) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of NCFO to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_assets_126d_base_v020_signal(ncfo, assets) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of NCFO to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_assets_252d_base_v021_signal(ncfo, assets) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of NCFO to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_assets_504d_base_v022_signal(ncfo, assets) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of NCFO to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_assets_756d_base_v023_signal(ncfo, assets) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of NCFO to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_assets_1260d_base_v024_signal(ncfo, assets) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d percentage change of FCF for cash flow trajectory
def f23_cash_flow_trajectory_fcf_growth_63d_base_v025_signal(fcf) -> pd.Series:
    res = _cft_pct_chg(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d percentage change of FCF for cash flow trajectory
def f23_cash_flow_trajectory_fcf_growth_126d_base_v026_signal(fcf) -> pd.Series:
    res = _cft_pct_chg(fcf, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d percentage change of FCF for cash flow trajectory
def f23_cash_flow_trajectory_fcf_growth_252d_base_v027_signal(fcf) -> pd.Series:
    res = _cft_pct_chg(fcf, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d percentage change of FCF for cash flow trajectory
def f23_cash_flow_trajectory_fcf_growth_504d_base_v028_signal(fcf) -> pd.Series:
    res = _cft_pct_chg(fcf, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d percentage change of FCF for cash flow trajectory
def f23_cash_flow_trajectory_fcf_growth_756d_base_v029_signal(fcf) -> pd.Series:
    res = _cft_pct_chg(fcf, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d percentage change of FCF for cash flow trajectory
def f23_cash_flow_trajectory_fcf_growth_1260d_base_v030_signal(fcf) -> pd.Series:
    res = _cft_pct_chg(fcf, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d percentage change of NCFO for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_growth_63d_base_v031_signal(ncfo) -> pd.Series:
    res = _cft_pct_chg(ncfo, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d percentage change of NCFO for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_growth_126d_base_v032_signal(ncfo) -> pd.Series:
    res = _cft_pct_chg(ncfo, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d percentage change of NCFO for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_growth_252d_base_v033_signal(ncfo) -> pd.Series:
    res = _cft_pct_chg(ncfo, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d percentage change of NCFO for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_growth_504d_base_v034_signal(ncfo) -> pd.Series:
    res = _cft_pct_chg(ncfo, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d percentage change of NCFO for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_growth_756d_base_v035_signal(ncfo) -> pd.Series:
    res = _cft_pct_chg(ncfo, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d percentage change of NCFO for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_growth_1260d_base_v036_signal(ncfo) -> pd.Series:
    res = _cft_pct_chg(ncfo, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of Capex to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_capex_rev_63d_base_v037_signal(capex, revenue) -> pd.Series:
    res = _sma(_cft_ratio(capex, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of Capex to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_capex_rev_126d_base_v038_signal(capex, revenue) -> pd.Series:
    res = _sma(_cft_ratio(capex, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of Capex to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_capex_rev_252d_base_v039_signal(capex, revenue) -> pd.Series:
    res = _sma(_cft_ratio(capex, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of Capex to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_capex_rev_504d_base_v040_signal(capex, revenue) -> pd.Series:
    res = _sma(_cft_ratio(capex, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of Capex to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_capex_rev_756d_base_v041_signal(capex, revenue) -> pd.Series:
    res = _sma(_cft_ratio(capex, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of Capex to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_capex_rev_1260d_base_v042_signal(capex, revenue) -> pd.Series:
    res = _sma(_cft_ratio(capex, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of Capex to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_capex_assets_63d_base_v043_signal(capex, assets) -> pd.Series:
    res = _sma(_cft_ratio(capex, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of Capex to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_capex_assets_126d_base_v044_signal(capex, assets) -> pd.Series:
    res = _sma(_cft_ratio(capex, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of Capex to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_capex_assets_252d_base_v045_signal(capex, assets) -> pd.Series:
    res = _sma(_cft_ratio(capex, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of Capex to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_capex_assets_504d_base_v046_signal(capex, assets) -> pd.Series:
    res = _sma(_cft_ratio(capex, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of Capex to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_capex_assets_756d_base_v047_signal(capex, assets) -> pd.Series:
    res = _sma(_cft_ratio(capex, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of Capex to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_capex_assets_1260d_base_v048_signal(capex, assets) -> pd.Series:
    res = _sma(_cft_ratio(capex, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of FCF to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_netinc_63d_base_v049_signal(fcf, netinc) -> pd.Series:
    res = _sma(_cft_ratio(fcf, netinc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of FCF to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_netinc_126d_base_v050_signal(fcf, netinc) -> pd.Series:
    res = _sma(_cft_ratio(fcf, netinc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of FCF to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_netinc_252d_base_v051_signal(fcf, netinc) -> pd.Series:
    res = _sma(_cft_ratio(fcf, netinc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of FCF to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_netinc_504d_base_v052_signal(fcf, netinc) -> pd.Series:
    res = _sma(_cft_ratio(fcf, netinc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of FCF to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_netinc_756d_base_v053_signal(fcf, netinc) -> pd.Series:
    res = _sma(_cft_ratio(fcf, netinc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of FCF to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_netinc_1260d_base_v054_signal(fcf, netinc) -> pd.Series:
    res = _sma(_cft_ratio(fcf, netinc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of NCFO to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_netinc_63d_base_v055_signal(ncfo, netinc) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, netinc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of NCFO to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_netinc_126d_base_v056_signal(ncfo, netinc) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, netinc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of NCFO to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_netinc_252d_base_v057_signal(ncfo, netinc) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, netinc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of NCFO to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_netinc_504d_base_v058_signal(ncfo, netinc) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, netinc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of NCFO to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_netinc_756d_base_v059_signal(ncfo, netinc) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, netinc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of NCFO to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_netinc_1260d_base_v060_signal(ncfo, netinc) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, netinc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of (FCF - NCFI) to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_minus_ncfi_rev_63d_base_v061_signal(fcf, ncfi, revenue) -> pd.Series:
    res = _sma(_cft_ratio(fcf - ncfi, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of (FCF - NCFI) to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_minus_ncfi_rev_126d_base_v062_signal(fcf, ncfi, revenue) -> pd.Series:
    res = _sma(_cft_ratio(fcf - ncfi, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of (FCF - NCFI) to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_minus_ncfi_rev_252d_base_v063_signal(fcf, ncfi, revenue) -> pd.Series:
    res = _sma(_cft_ratio(fcf - ncfi, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of (FCF - NCFI) to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_minus_ncfi_rev_504d_base_v064_signal(fcf, ncfi, revenue) -> pd.Series:
    res = _sma(_cft_ratio(fcf - ncfi, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of (FCF - NCFI) to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_minus_ncfi_rev_756d_base_v065_signal(fcf, ncfi, revenue) -> pd.Series:
    res = _sma(_cft_ratio(fcf - ncfi, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of (FCF - NCFI) to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_minus_ncfi_rev_1260d_base_v066_signal(fcf, ncfi, revenue) -> pd.Series:
    res = _sma(_cft_ratio(fcf - ncfi, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of NCFO to Debt ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_debt_63d_base_v067_signal(ncfo, debt) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, debt), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of NCFO to Debt ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_debt_126d_base_v068_signal(ncfo, debt) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, debt), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of NCFO to Debt ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_debt_252d_base_v069_signal(ncfo, debt) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, debt), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of NCFO to Debt ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_debt_504d_base_v070_signal(ncfo, debt) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, debt), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of NCFO to Debt ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_debt_756d_base_v071_signal(ncfo, debt) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, debt), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of NCFO to Debt ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_debt_1260d_base_v072_signal(ncfo, debt) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, debt), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of FCF to Debt ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_debt_252d_base_v073_signal(fcf, debt) -> pd.Series:
    res = _sma(_cft_ratio(fcf, debt), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of FCF to Debt ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_debt_504d_base_v074_signal(fcf, debt) -> pd.Series:
    res = _sma(_cft_ratio(fcf, debt), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of FCF to Debt ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_debt_756d_base_v075_signal(fcf, debt) -> pd.Series:
    res = _sma(_cft_ratio(fcf, debt), 756)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "fcf": np.random.normal(10, 2, n),
        "revenue": np.random.normal(100, 10, n),
        "assets": np.random.normal(500, 50, n),
        "ncfo": np.random.normal(15, 3, n),
        "netinc": np.random.normal(8, 2, n),
        "capex": np.random.normal(5, 1, n),
        "ncfi": np.random.normal(-5, 1, n),
        "debt": np.random.normal(200, 20, n),
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f23_cash_flow_trajectory_"))]
    
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
        assert any(prim in source for prim in ["_cft_ratio", "_cft_pct_chg", "_cft_zscore"])

    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f23_cash_flow_trajectory_"))]}
F23_CASH_FLOW_TRAJECTORY_REGISTRY_001_075 = REGISTRY
