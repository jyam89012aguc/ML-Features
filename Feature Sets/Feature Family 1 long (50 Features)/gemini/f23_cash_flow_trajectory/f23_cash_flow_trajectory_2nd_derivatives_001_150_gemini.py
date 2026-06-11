import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()

def _cft_ratio(num, den):
    return num / den.replace(0, np.nan)

def _cft_slope(s, w):
    return s.pct_change(w)

def _cft_zscore(s, w):
    return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)

# Slope of 63d average FCF to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_rev_63d_slope_v001_signal(fcf, revenue) -> pd.Series:
    base = _sma(_cft_ratio(fcf, revenue), 63)
    res = _cft_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d average FCF to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_rev_126d_slope_v002_signal(fcf, revenue) -> pd.Series:
    base = _sma(_cft_ratio(fcf, revenue), 126)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d average FCF to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_rev_252d_slope_v003_signal(fcf, revenue) -> pd.Series:
    base = _sma(_cft_ratio(fcf, revenue), 252)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d average FCF to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_rev_504d_slope_v004_signal(fcf, revenue) -> pd.Series:
    base = _sma(_cft_ratio(fcf, revenue), 504)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d average FCF to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_rev_756d_slope_v005_signal(fcf, revenue) -> pd.Series:
    base = _sma(_cft_ratio(fcf, revenue), 756)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d average FCF to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_rev_1260d_slope_v006_signal(fcf, revenue) -> pd.Series:
    base = _sma(_cft_ratio(fcf, revenue), 1260)
    res = _cft_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 63d average FCF to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_assets_63d_slope_v007_signal(fcf, assets) -> pd.Series:
    base = _sma(_cft_ratio(fcf, assets), 63)
    res = _cft_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d average FCF to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_assets_126d_slope_v008_signal(fcf, assets) -> pd.Series:
    base = _sma(_cft_ratio(fcf, assets), 126)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d average FCF to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_assets_252d_slope_v009_signal(fcf, assets) -> pd.Series:
    base = _sma(_cft_ratio(fcf, assets), 252)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d average FCF to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_assets_504d_slope_v010_signal(fcf, assets) -> pd.Series:
    base = _sma(_cft_ratio(fcf, assets), 504)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d average FCF to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_assets_756d_slope_v011_signal(fcf, assets) -> pd.Series:
    base = _sma(_cft_ratio(fcf, assets), 756)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d average FCF to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_assets_1260d_slope_v012_signal(fcf, assets) -> pd.Series:
    base = _sma(_cft_ratio(fcf, assets), 1260)
    res = _cft_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 63d average NCFO to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_rev_63d_slope_v013_signal(ncfo, revenue) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, revenue), 63)
    res = _cft_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d average NCFO to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_rev_126d_slope_v014_signal(ncfo, revenue) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, revenue), 126)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d average NCFO to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_rev_252d_slope_v015_signal(ncfo, revenue) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, revenue), 252)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d average NCFO to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_rev_504d_slope_v016_signal(ncfo, revenue) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, revenue), 504)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d average NCFO to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_rev_756d_slope_v017_signal(ncfo, revenue) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, revenue), 756)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d average NCFO to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_rev_1260d_slope_v018_signal(ncfo, revenue) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, revenue), 1260)
    res = _cft_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 63d average NCFO to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_assets_63d_slope_v019_signal(ncfo, assets) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, assets), 63)
    res = _cft_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d average NCFO to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_assets_126d_slope_v020_signal(ncfo, assets) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, assets), 126)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d average NCFO to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_assets_252d_slope_v021_signal(ncfo, assets) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, assets), 252)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d average NCFO to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_assets_504d_slope_v022_signal(ncfo, assets) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, assets), 504)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d average NCFO to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_assets_756d_slope_v023_signal(ncfo, assets) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, assets), 756)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d average NCFO to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_assets_1260d_slope_v024_signal(ncfo, assets) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, assets), 1260)
    res = _cft_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 63d FCF Growth for cash flow trajectory
def f23_cash_flow_trajectory_fcf_growth_63d_slope_v025_signal(fcf) -> pd.Series:
    base = fcf.pct_change(63)
    res = _cft_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d FCF Growth for cash flow trajectory
def f23_cash_flow_trajectory_fcf_growth_126d_slope_v026_signal(fcf) -> pd.Series:
    base = fcf.pct_change(126)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d FCF Growth for cash flow trajectory
def f23_cash_flow_trajectory_fcf_growth_252d_slope_v027_signal(fcf) -> pd.Series:
    base = fcf.pct_change(252)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d FCF Growth for cash flow trajectory
def f23_cash_flow_trajectory_fcf_growth_504d_slope_v028_signal(fcf) -> pd.Series:
    base = fcf.pct_change(504)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d FCF Growth for cash flow trajectory
def f23_cash_flow_trajectory_fcf_growth_756d_slope_v029_signal(fcf) -> pd.Series:
    base = fcf.pct_change(756)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d FCF Growth for cash flow trajectory
def f23_cash_flow_trajectory_fcf_growth_1260d_slope_v030_signal(fcf) -> pd.Series:
    base = fcf.pct_change(1260)
    res = _cft_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 63d NCFO Growth for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_growth_63d_slope_v031_signal(ncfo) -> pd.Series:
    base = ncfo.pct_change(63)
    res = _cft_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d NCFO Growth for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_growth_126d_slope_v032_signal(ncfo) -> pd.Series:
    base = ncfo.pct_change(126)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d NCFO Growth for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_growth_252d_slope_v033_signal(ncfo) -> pd.Series:
    base = ncfo.pct_change(252)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d NCFO Growth for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_growth_504d_slope_v034_signal(ncfo) -> pd.Series:
    base = ncfo.pct_change(504)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d NCFO Growth for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_growth_756d_slope_v035_signal(ncfo) -> pd.Series:
    base = ncfo.pct_change(756)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d NCFO Growth for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_growth_1260d_slope_v036_signal(ncfo) -> pd.Series:
    base = ncfo.pct_change(1260)
    res = _cft_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 63d Capex to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_capex_rev_63d_slope_v037_signal(capex, revenue) -> pd.Series:
    base = _sma(_cft_ratio(capex, revenue), 63)
    res = _cft_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d Capex to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_capex_rev_126d_slope_v038_signal(capex, revenue) -> pd.Series:
    base = _sma(_cft_ratio(capex, revenue), 126)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d Capex to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_capex_rev_252d_slope_v039_signal(capex, revenue) -> pd.Series:
    base = _sma(_cft_ratio(capex, revenue), 252)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d Capex to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_capex_rev_504d_slope_v040_signal(capex, revenue) -> pd.Series:
    base = _sma(_cft_ratio(capex, revenue), 504)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d Capex to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_capex_rev_756d_slope_v041_signal(capex, revenue) -> pd.Series:
    base = _sma(_cft_ratio(capex, revenue), 756)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d Capex to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_capex_rev_1260d_slope_v042_signal(capex, revenue) -> pd.Series:
    base = _sma(_cft_ratio(capex, revenue), 1260)
    res = _cft_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 63d Capex to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_capex_assets_63d_slope_v043_signal(capex, assets) -> pd.Series:
    base = _sma(_cft_ratio(capex, assets), 63)
    res = _cft_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d Capex to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_capex_assets_126d_slope_v044_signal(capex, assets) -> pd.Series:
    base = _sma(_cft_ratio(capex, assets), 126)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d Capex to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_capex_assets_252d_slope_v045_signal(capex, assets) -> pd.Series:
    base = _sma(_cft_ratio(capex, assets), 252)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d Capex to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_capex_assets_504d_slope_v046_signal(capex, assets) -> pd.Series:
    base = _sma(_cft_ratio(capex, assets), 504)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d Capex to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_capex_assets_756d_slope_v047_signal(capex, assets) -> pd.Series:
    base = _sma(_cft_ratio(capex, assets), 756)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d Capex to Assets ratio for cash flow trajectory
def f23_cash_flow_trajectory_capex_assets_1260d_slope_v048_signal(capex, assets) -> pd.Series:
    base = _sma(_cft_ratio(capex, assets), 1260)
    res = _cft_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 63d FCF to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_netinc_63d_slope_v049_signal(fcf, netinc) -> pd.Series:
    base = _sma(_cft_ratio(fcf, netinc), 63)
    res = _cft_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d FCF to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_netinc_126d_slope_v050_signal(fcf, netinc) -> pd.Series:
    base = _sma(_cft_ratio(fcf, netinc), 126)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d FCF to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_netinc_252d_slope_v051_signal(fcf, netinc) -> pd.Series:
    base = _sma(_cft_ratio(fcf, netinc), 252)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d FCF to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_netinc_504d_slope_v052_signal(fcf, netinc) -> pd.Series:
    base = _sma(_cft_ratio(fcf, netinc), 504)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d FCF to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_netinc_756d_slope_v053_signal(fcf, netinc) -> pd.Series:
    base = _sma(_cft_ratio(fcf, netinc), 756)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d FCF to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_netinc_1260d_slope_v054_signal(fcf, netinc) -> pd.Series:
    base = _sma(_cft_ratio(fcf, netinc), 1260)
    res = _cft_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 63d NCFO to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_netinc_63d_slope_v055_signal(ncfo, netinc) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, netinc), 63)
    res = _cft_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d NCFO to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_netinc_126d_slope_v056_signal(ncfo, netinc) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, netinc), 126)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d NCFO to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_netinc_252d_slope_v057_signal(ncfo, netinc) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, netinc), 252)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d NCFO to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_netinc_504d_slope_v058_signal(ncfo, netinc) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, netinc), 504)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d NCFO to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_netinc_756d_slope_v059_signal(ncfo, netinc) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, netinc), 756)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d NCFO to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_netinc_1260d_slope_v060_signal(ncfo, netinc) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, netinc), 1260)
    res = _cft_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 63d FCF minus NCFI to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_minus_ncfi_rev_63d_slope_v061_signal(fcf, ncfi, revenue) -> pd.Series:
    base = _sma(_cft_ratio(fcf - ncfi, revenue), 63)
    res = _cft_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d FCF minus NCFI to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_minus_ncfi_rev_126d_slope_v062_signal(fcf, ncfi, revenue) -> pd.Series:
    base = _sma(_cft_ratio(fcf - ncfi, revenue), 126)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d FCF minus NCFI to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_minus_ncfi_rev_252d_slope_v063_signal(fcf, ncfi, revenue) -> pd.Series:
    base = _sma(_cft_ratio(fcf - ncfi, revenue), 252)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d FCF minus NCFI to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_minus_ncfi_rev_504d_slope_v064_signal(fcf, ncfi, revenue) -> pd.Series:
    base = _sma(_cft_ratio(fcf - ncfi, revenue), 504)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d FCF minus NCFI to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_minus_ncfi_rev_756d_slope_v065_signal(fcf, ncfi, revenue) -> pd.Series:
    base = _sma(_cft_ratio(fcf - ncfi, revenue), 756)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d FCF minus NCFI to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_minus_ncfi_rev_1260d_slope_v066_signal(fcf, ncfi, revenue) -> pd.Series:
    base = _sma(_cft_ratio(fcf - ncfi, revenue), 1260)
    res = _cft_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 63d NCFO to Debt ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_debt_63d_slope_v067_signal(ncfo, debt) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, debt), 63)
    res = _cft_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d NCFO to Debt ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_debt_126d_slope_v068_signal(ncfo, debt) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, debt), 126)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d NCFO to Debt ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_debt_252d_slope_v069_signal(ncfo, debt) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, debt), 252)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d NCFO to Debt ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_debt_504d_slope_v070_signal(ncfo, debt) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, debt), 504)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d NCFO to Debt ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_debt_756d_slope_v071_signal(ncfo, debt) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, debt), 756)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d NCFO to Debt ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_debt_1260d_slope_v072_signal(ncfo, debt) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, debt), 1260)
    res = _cft_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d FCF to Debt ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_debt_252d_slope_v073_signal(fcf, debt) -> pd.Series:
    base = _sma(_cft_ratio(fcf, debt), 252)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d FCF to Debt ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_debt_504d_slope_v074_signal(fcf, debt) -> pd.Series:
    base = _sma(_cft_ratio(fcf, debt), 504)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d FCF to Debt ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_debt_756d_slope_v075_signal(fcf, debt) -> pd.Series:
    base = _sma(_cft_ratio(fcf, debt), 756)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 63d FCF to Equity ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_equity_63d_slope_v076_signal(fcf, equity) -> pd.Series:
    base = _sma(_cft_ratio(fcf, equity), 63)
    res = _cft_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d FCF to Equity ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_equity_126d_slope_v077_signal(fcf, equity) -> pd.Series:
    base = _sma(_cft_ratio(fcf, equity), 126)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d FCF to Equity ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_equity_252d_slope_v078_signal(fcf, equity) -> pd.Series:
    base = _sma(_cft_ratio(fcf, equity), 252)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d FCF to Equity ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_equity_504d_slope_v079_signal(fcf, equity) -> pd.Series:
    base = _sma(_cft_ratio(fcf, equity), 504)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d FCF to Equity ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_equity_756d_slope_v080_signal(fcf, equity) -> pd.Series:
    base = _sma(_cft_ratio(fcf, equity), 756)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d FCF to Equity ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_equity_1260d_slope_v081_signal(fcf, equity) -> pd.Series:
    base = _sma(_cft_ratio(fcf, equity), 1260)
    res = _cft_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 63d NCFO to Equity ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_equity_63d_slope_v082_signal(ncfo, equity) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, equity), 63)
    res = _cft_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d NCFO to Equity ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_equity_126d_slope_v083_signal(ncfo, equity) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, equity), 126)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d NCFO to Equity ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_equity_252d_slope_v084_signal(ncfo, equity) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, equity), 252)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d NCFO to Equity ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_equity_504d_slope_v085_signal(ncfo, equity) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, equity), 504)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d NCFO to Equity ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_equity_756d_slope_v086_signal(ncfo, equity) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, equity), 756)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d NCFO to Equity ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_equity_1260d_slope_v087_signal(ncfo, equity) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, equity), 1260)
    res = _cft_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 63d FCF to Liabilities ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_liab_63d_slope_v088_signal(fcf, liabilities) -> pd.Series:
    base = _sma(_cft_ratio(fcf, liabilities), 63)
    res = _cft_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d FCF to Liabilities ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_liab_126d_slope_v089_signal(fcf, liabilities) -> pd.Series:
    base = _sma(_cft_ratio(fcf, liabilities), 126)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d FCF to Liabilities ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_liab_252d_slope_v090_signal(fcf, liabilities) -> pd.Series:
    base = _sma(_cft_ratio(fcf, liabilities), 252)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d FCF to Liabilities ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_liab_504d_slope_v091_signal(fcf, liabilities) -> pd.Series:
    base = _sma(_cft_ratio(fcf, liabilities), 504)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d FCF to Liabilities ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_liab_756d_slope_v092_signal(fcf, liabilities) -> pd.Series:
    base = _sma(_cft_ratio(fcf, liabilities), 756)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d FCF to Liabilities ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_liab_1260d_slope_v093_signal(fcf, liabilities) -> pd.Series:
    base = _sma(_cft_ratio(fcf, liabilities), 1260)
    res = _cft_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 63d NCFO to Liabilities ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_liab_63d_slope_v094_signal(ncfo, liabilities) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, liabilities), 63)
    res = _cft_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d NCFO to Liabilities ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_liab_126d_slope_v095_signal(ncfo, liabilities) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, liabilities), 126)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d NCFO to Liabilities ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_liab_252d_slope_v096_signal(ncfo, liabilities) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, liabilities), 252)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d NCFO to Liabilities ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_liab_504d_slope_v097_signal(ncfo, liabilities) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, liabilities), 504)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d NCFO to Liabilities ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_liab_756d_slope_v098_signal(ncfo, liabilities) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, liabilities), 756)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d NCFO to Liabilities ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_liab_1260d_slope_v099_signal(ncfo, liabilities) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, liabilities), 1260)
    res = _cft_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 63d FCF to Working Capital ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_wc_63d_slope_v100_signal(fcf, workingcapital) -> pd.Series:
    base = _sma(_cft_ratio(fcf, workingcapital), 63)
    res = _cft_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d FCF to Working Capital ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_wc_126d_slope_v101_signal(fcf, workingcapital) -> pd.Series:
    base = _sma(_cft_ratio(fcf, workingcapital), 126)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d FCF to Working Capital ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_wc_252d_slope_v102_signal(fcf, workingcapital) -> pd.Series:
    base = _sma(_cft_ratio(fcf, workingcapital), 252)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d FCF to Working Capital ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_wc_504d_slope_v103_signal(fcf, workingcapital) -> pd.Series:
    base = _sma(_cft_ratio(fcf, workingcapital), 504)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d FCF to Working Capital ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_wc_756d_slope_v104_signal(fcf, workingcapital) -> pd.Series:
    base = _sma(_cft_ratio(fcf, workingcapital), 756)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d FCF to Working Capital ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_wc_1260d_slope_v105_signal(fcf, workingcapital) -> pd.Series:
    base = _sma(_cft_ratio(fcf, workingcapital), 1260)
    res = _cft_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 63d NCFO to Working Capital ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_wc_63d_slope_v106_signal(ncfo, workingcapital) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, workingcapital), 63)
    res = _cft_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d NCFO to Working Capital ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_wc_126d_slope_v107_signal(ncfo, workingcapital) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, workingcapital), 126)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d NCFO to Working Capital ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_wc_252d_slope_v108_signal(ncfo, workingcapital) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, workingcapital), 252)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d NCFO to Working Capital ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_wc_504d_slope_v109_signal(ncfo, workingcapital) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, workingcapital), 504)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d NCFO to Working Capital ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_wc_756d_slope_v110_signal(ncfo, workingcapital) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, workingcapital), 756)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d NCFO to Working Capital ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_wc_1260d_slope_v111_signal(ncfo, workingcapital) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, workingcapital), 1260)
    res = _cft_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 63d FCF CV for cash flow trajectory
def f23_cash_flow_trajectory_fcf_cv_63d_slope_v112_signal(fcf) -> pd.Series:
    base = _std(fcf, 63) / _sma(fcf, 63).abs().replace(0, np.nan)
    res = _cft_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d FCF CV for cash flow trajectory
def f23_cash_flow_trajectory_fcf_cv_126d_slope_v113_signal(fcf) -> pd.Series:
    base = _std(fcf, 126) / _sma(fcf, 126).abs().replace(0, np.nan)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d FCF CV for cash flow trajectory
def f23_cash_flow_trajectory_fcf_cv_252d_slope_v114_signal(fcf) -> pd.Series:
    base = _std(fcf, 252) / _sma(fcf, 252).abs().replace(0, np.nan)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d FCF CV for cash flow trajectory
def f23_cash_flow_trajectory_fcf_cv_504d_slope_v115_signal(fcf) -> pd.Series:
    base = _std(fcf, 504) / _sma(fcf, 504).abs().replace(0, np.nan)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d FCF CV for cash flow trajectory
def f23_cash_flow_trajectory_fcf_cv_756d_slope_v116_signal(fcf) -> pd.Series:
    base = _std(fcf, 756) / _sma(fcf, 756).abs().replace(0, np.nan)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d FCF CV for cash flow trajectory
def f23_cash_flow_trajectory_fcf_cv_1260d_slope_v117_signal(fcf) -> pd.Series:
    base = _std(fcf, 1260) / _sma(fcf, 1260).abs().replace(0, np.nan)
    res = _cft_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 63d NCFO CV for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_cv_63d_slope_v118_signal(ncfo) -> pd.Series:
    base = _std(ncfo, 63) / _sma(ncfo, 63).abs().replace(0, np.nan)
    res = _cft_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d NCFO CV for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_cv_126d_slope_v119_signal(ncfo) -> pd.Series:
    base = _std(ncfo, 126) / _sma(ncfo, 126).abs().replace(0, np.nan)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d NCFO CV for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_cv_252d_slope_v120_signal(ncfo) -> pd.Series:
    base = _std(ncfo, 252) / _sma(ncfo, 252).abs().replace(0, np.nan)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d NCFO CV for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_cv_504d_slope_v121_signal(ncfo) -> pd.Series:
    base = _std(ncfo, 504) / _sma(ncfo, 504).abs().replace(0, np.nan)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d NCFO CV for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_cv_756d_slope_v122_signal(ncfo) -> pd.Series:
    base = _std(ncfo, 756) / _sma(ncfo, 756).abs().replace(0, np.nan)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d NCFO CV for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_cv_1260d_slope_v123_signal(ncfo) -> pd.Series:
    base = _std(ncfo, 1260) / _sma(ncfo, 1260).abs().replace(0, np.nan)
    res = _cft_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 63d z-score FCF/NetInc for cash flow trajectory
def f23_cash_flow_trajectory_fcf_netinc_zscore_63d_slope_v124_signal(fcf, netinc) -> pd.Series:
    base = _cft_zscore(_cft_ratio(fcf, netinc), 63)
    res = base.diff(5) / base.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d z-score FCF/NetInc for cash flow trajectory
def f23_cash_flow_trajectory_fcf_netinc_zscore_126d_slope_v125_signal(fcf, netinc) -> pd.Series:
    base = _cft_zscore(_cft_ratio(fcf, netinc), 126)
    res = base.diff(21) / base.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d z-score FCF/NetInc for cash flow trajectory
def f23_cash_flow_trajectory_fcf_netinc_zscore_252d_slope_v126_signal(fcf, netinc) -> pd.Series:
    base = _cft_zscore(_cft_ratio(fcf, netinc), 252)
    res = base.diff(21) / base.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d z-score FCF/NetInc for cash flow trajectory
def f23_cash_flow_trajectory_fcf_netinc_zscore_504d_slope_v127_signal(fcf, netinc) -> pd.Series:
    base = _cft_zscore(_cft_ratio(fcf, netinc), 504)
    res = base.diff(63) / base.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d z-score FCF/NetInc for cash flow trajectory
def f23_cash_flow_trajectory_fcf_netinc_zscore_756d_slope_v128_signal(fcf, netinc) -> pd.Series:
    base = _cft_zscore(_cft_ratio(fcf, netinc), 756)
    res = base.diff(63) / base.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d z-score FCF/NetInc for cash flow trajectory
def f23_cash_flow_trajectory_fcf_netinc_zscore_1260d_slope_v129_signal(fcf, netinc) -> pd.Series:
    base = _cft_zscore(_cft_ratio(fcf, netinc), 1260)
    res = base.diff(126) / base.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 63d z-score NCFO/Rev for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_rev_zscore_63d_slope_v130_signal(ncfo, revenue) -> pd.Series:
    base = _cft_zscore(_cft_ratio(ncfo, revenue), 63)
    res = base.diff(5) / base.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d z-score NCFO/Rev for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_rev_zscore_126d_slope_v131_signal(ncfo, revenue) -> pd.Series:
    base = _cft_zscore(_cft_ratio(ncfo, revenue), 126)
    res = base.diff(21) / base.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d z-score NCFO/Rev for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_rev_zscore_252d_slope_v132_signal(ncfo, revenue) -> pd.Series:
    base = _cft_zscore(_cft_ratio(ncfo, revenue), 252)
    res = base.diff(21) / base.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d z-score NCFO/Rev for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_rev_zscore_504d_slope_v133_signal(ncfo, revenue) -> pd.Series:
    base = _cft_zscore(_cft_ratio(ncfo, revenue), 504)
    res = base.diff(63) / base.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d z-score NCFO/Rev for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_rev_zscore_756d_slope_v134_signal(ncfo, revenue) -> pd.Series:
    base = _cft_zscore(_cft_ratio(ncfo, revenue), 756)
    res = base.diff(63) / base.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d z-score NCFO/Rev for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_rev_zscore_1260d_slope_v135_signal(ncfo, revenue) -> pd.Series:
    base = _cft_zscore(_cft_ratio(ncfo, revenue), 1260)
    res = base.diff(126) / base.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 63d average FCF to Capex ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_capex_63d_slope_v136_signal(fcf, capex) -> pd.Series:
    base = _sma(_cft_ratio(fcf, capex), 63)
    res = _cft_slope(base, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d average FCF to Capex ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_capex_126d_slope_v137_signal(fcf, capex) -> pd.Series:
    base = _sma(_cft_ratio(fcf, capex), 126)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d average FCF to Capex ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_capex_252d_slope_v138_signal(fcf, capex) -> pd.Series:
    base = _sma(_cft_ratio(fcf, capex), 252)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d average FCF to Capex ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_capex_504d_slope_v139_signal(fcf, capex) -> pd.Series:
    base = _sma(_cft_ratio(fcf, capex), 504)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d average FCF to Capex ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_capex_756d_slope_v140_signal(fcf, capex) -> pd.Series:
    base = _sma(_cft_ratio(fcf, capex), 756)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d average FCF to Capex ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_capex_1260d_slope_v141_signal(fcf, capex) -> pd.Series:
    base = _sma(_cft_ratio(fcf, capex), 1260)
    res = _cft_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d average OCF to Capex ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_capex_252d_slope_v142_signal(ncfo, capex) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, capex), 252)
    res = _cft_slope(base, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d average OCF to Capex ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_capex_504d_slope_v143_signal(ncfo, capex) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, capex), 504)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d average OCF to Capex ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_capex_756d_slope_v144_signal(ncfo, capex) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, capex), 756)
    res = _cft_slope(base, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d average OCF to Capex ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_capex_1260d_slope_v145_signal(ncfo, capex) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, capex), 1260)
    res = _cft_slope(base, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d z-score OCF/Capex for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_capex_zscore_252d_slope_v146_signal(ncfo, capex) -> pd.Series:
    base = _cft_zscore(_cft_ratio(ncfo, capex), 252)
    res = base.diff(21) / base.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d z-score OCF/Capex for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_capex_zscore_504d_slope_v147_signal(ncfo, capex) -> pd.Series:
    base = _cft_zscore(_cft_ratio(ncfo, capex), 504)
    res = base.diff(63) / base.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 756d z-score OCF/Capex for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_capex_zscore_756d_slope_v148_signal(ncfo, capex) -> pd.Series:
    base = _cft_zscore(_cft_ratio(ncfo, capex), 756)
    res = base.diff(63) / base.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 1260d z-score OCF/Capex for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_capex_zscore_1260d_slope_v149_signal(ncfo, capex) -> pd.Series:
    base = _cft_zscore(_cft_ratio(ncfo, capex), 1260)
    res = base.diff(126) / base.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d average NCFO to NCFI ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_ncfi_252d_slope_v150_signal(ncfo, ncfi) -> pd.Series:
    base = _sma(_cft_ratio(ncfo, ncfi), 252)
    res = _cft_slope(base, 21)
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
        "equity": np.random.normal(300, 30, n),
        "liabilities": np.random.normal(200, 20, n),
        "workingcapital": np.random.normal(50, 10, n),
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
        assert any(prim in source for prim in ["_cft_ratio", "_cft_slope", "_cft_zscore"])

    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f23_cash_flow_trajectory_"))]}
F23_CASH_FLOW_TRAJECTORY_REGISTRY_SLOPE = REGISTRY
