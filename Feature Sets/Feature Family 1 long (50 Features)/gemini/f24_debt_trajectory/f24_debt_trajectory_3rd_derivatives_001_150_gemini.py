import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()

def _dt_ratio(num, den):
    return num / den.replace(0, np.nan)

def _dt_slope(s, w):
    return s.pct_change(w)

def _dt_jerk(s, w):
    return s.diff(w)

def _dt_zscore(s, w):
    return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)

# Jerk of 63d average Debt to Assets ratio for debt trajectory
def f24_debt_trajectory_debt_assets_63d_jerk_v001_signal(debt, assets) -> pd.Series:
    base = _sma(_dt_ratio(debt, assets), 63)
    slope = _dt_slope(base, 5)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 126d average Debt to Assets ratio for debt trajectory
def f24_debt_trajectory_debt_assets_126d_jerk_v002_signal(debt, assets) -> pd.Series:
    base = _sma(_dt_ratio(debt, assets), 126)
    slope = _dt_slope(base, 21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 252d average Debt to Assets ratio for debt trajectory
def f24_debt_trajectory_debt_assets_252d_jerk_v003_signal(debt, assets) -> pd.Series:
    base = _sma(_dt_ratio(debt, assets), 252)
    slope = _dt_slope(base, 21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 504d average Debt to Assets ratio for debt trajectory
def f24_debt_trajectory_debt_assets_504d_jerk_v004_signal(debt, assets) -> pd.Series:
    base = _sma(_dt_ratio(debt, assets), 504)
    slope = _dt_slope(base, 63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 756d average Debt to Assets ratio for debt trajectory
def f24_debt_trajectory_debt_assets_756d_jerk_v005_signal(debt, assets) -> pd.Series:
    base = _sma(_dt_ratio(debt, assets), 756)
    slope = _dt_slope(base, 63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 1260d average Debt to Assets ratio for debt trajectory
def f24_debt_trajectory_debt_assets_1260d_jerk_v006_signal(debt, assets) -> pd.Series:
    base = _sma(_dt_ratio(debt, assets), 1260)
    slope = _dt_slope(base, 126)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 63d average Debt to Equity ratio for debt trajectory
def f24_debt_trajectory_debt_equity_63d_jerk_v007_signal(debt, equity) -> pd.Series:
    base = _sma(_dt_ratio(debt, equity), 63)
    slope = _dt_slope(base, 5)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 126d average Debt to Equity ratio for debt trajectory
def f24_debt_trajectory_debt_equity_126d_jerk_v008_signal(debt, equity) -> pd.Series:
    base = _sma(_dt_ratio(debt, equity), 126)
    slope = _dt_slope(base, 21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 252d average Debt to Equity ratio for debt trajectory
def f24_debt_trajectory_debt_equity_252d_jerk_v009_signal(debt, equity) -> pd.Series:
    base = _sma(_dt_ratio(debt, equity), 252)
    slope = _dt_slope(base, 21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 504d average Debt to Equity ratio for debt trajectory
def f24_debt_trajectory_debt_equity_504d_jerk_v010_signal(debt, equity) -> pd.Series:
    base = _sma(_dt_ratio(debt, equity), 504)
    slope = _dt_slope(base, 63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 756d average Debt to Equity ratio for debt trajectory
def f24_debt_trajectory_debt_equity_756d_jerk_v011_signal(debt, equity) -> pd.Series:
    base = _sma(_dt_ratio(debt, equity), 756)
    slope = _dt_slope(base, 63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 1260d average Debt to Equity ratio for debt trajectory
def f24_debt_trajectory_debt_equity_1260d_jerk_v012_signal(debt, equity) -> pd.Series:
    base = _sma(_dt_ratio(debt, equity), 1260)
    slope = _dt_slope(base, 126)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 63d average Debt to EBITDA ratio for debt trajectory
def f24_debt_trajectory_debt_ebitda_63d_jerk_v013_signal(debt, ebitda) -> pd.Series:
    base = _sma(_dt_ratio(debt, ebitda), 63)
    slope = _dt_slope(base, 5)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 126d average Debt to EBITDA ratio for debt trajectory
def f24_debt_trajectory_debt_ebitda_126d_jerk_v014_signal(debt, ebitda) -> pd.Series:
    base = _sma(_dt_ratio(debt, ebitda), 126)
    slope = _dt_slope(base, 21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 252d average Debt to EBITDA ratio for debt trajectory
def f24_debt_trajectory_debt_ebitda_252d_jerk_v015_signal(debt, ebitda) -> pd.Series:
    base = _sma(_dt_ratio(debt, ebitda), 252)
    slope = _dt_slope(base, 21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 504d average Debt to EBITDA ratio for debt trajectory
def f24_debt_trajectory_debt_ebitda_504d_jerk_v016_signal(debt, ebitda) -> pd.Series:
    base = _sma(_dt_ratio(debt, ebitda), 504)
    slope = _dt_slope(base, 63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 756d average Debt to EBITDA ratio for debt trajectory
def f24_debt_trajectory_debt_ebitda_756d_jerk_v017_signal(debt, ebitda) -> pd.Series:
    base = _sma(_dt_ratio(debt, ebitda), 756)
    slope = _dt_slope(base, 63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 1260d average Debt to EBITDA ratio for debt trajectory
def f24_debt_trajectory_debt_ebitda_1260d_jerk_v018_signal(debt, ebitda) -> pd.Series:
    base = _sma(_dt_ratio(debt, ebitda), 1260)
    slope = _dt_slope(base, 126)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 63d Debt Growth for debt trajectory
def f24_debt_trajectory_debt_growth_63d_jerk_v019_signal(debt) -> pd.Series:
    slope = debt.pct_change(63).pct_change(5)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 126d Debt Growth for debt trajectory
def f24_debt_trajectory_debt_growth_126d_jerk_v020_signal(debt) -> pd.Series:
    slope = debt.pct_change(126).pct_change(21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 252d Debt Growth for debt trajectory
def f24_debt_trajectory_debt_growth_252d_jerk_v021_signal(debt) -> pd.Series:
    slope = debt.pct_change(252).pct_change(21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 504d Debt Growth for debt trajectory
def f24_debt_trajectory_debt_growth_504d_jerk_v022_signal(debt) -> pd.Series:
    slope = debt.pct_change(504).pct_change(63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 756d Debt Growth for debt trajectory
def f24_debt_trajectory_debt_growth_756d_jerk_v023_signal(debt) -> pd.Series:
    slope = debt.pct_change(756).pct_change(63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 1260d Debt Growth for debt trajectory
def f24_debt_trajectory_debt_growth_1260d_jerk_v024_signal(debt) -> pd.Series:
    slope = debt.pct_change(1260).pct_change(126)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 63d average Liabilities to Assets ratio for debt trajectory
def f24_debt_trajectory_liab_assets_63d_jerk_v025_signal(liabilities, assets) -> pd.Series:
    base = _sma(_dt_ratio(liabilities, assets), 63)
    slope = _dt_slope(base, 5)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 126d average Liabilities to Assets ratio for debt trajectory
def f24_debt_trajectory_liab_assets_126d_jerk_v026_signal(liabilities, assets) -> pd.Series:
    base = _sma(_dt_ratio(liabilities, assets), 126)
    slope = _dt_slope(base, 21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 252d average Liabilities to Assets ratio for debt trajectory
def f24_debt_trajectory_liab_assets_252d_jerk_v027_signal(liabilities, assets) -> pd.Series:
    base = _sma(_dt_ratio(liabilities, assets), 252)
    slope = _dt_slope(base, 21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 504d average Liabilities to Assets ratio for debt trajectory
def f24_debt_trajectory_liab_assets_504d_jerk_v028_signal(liabilities, assets) -> pd.Series:
    base = _sma(_dt_ratio(liabilities, assets), 504)
    slope = _dt_slope(base, 63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 756d average Liabilities to Assets ratio for debt trajectory
def f24_debt_trajectory_liab_assets_756d_jerk_v029_signal(liabilities, assets) -> pd.Series:
    base = _sma(_dt_ratio(liabilities, assets), 756)
    slope = _dt_slope(base, 63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 1260d average Liabilities to Assets ratio for debt trajectory
def f24_debt_trajectory_liab_assets_1260d_jerk_v030_signal(liabilities, assets) -> pd.Series:
    base = _sma(_dt_ratio(liabilities, assets), 1260)
    slope = _dt_slope(base, 126)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 63d Liabilities Growth for debt trajectory
def f24_debt_trajectory_liab_growth_63d_jerk_v031_signal(liabilities) -> pd.Series:
    slope = liabilities.pct_change(63).pct_change(5)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 126d Liabilities Growth for debt trajectory
def f24_debt_trajectory_liab_growth_126d_jerk_v032_signal(liabilities) -> pd.Series:
    slope = liabilities.pct_change(126).pct_change(21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 252d Liabilities Growth for debt trajectory
def f24_debt_trajectory_liab_growth_252d_jerk_v033_signal(liabilities) -> pd.Series:
    slope = liabilities.pct_change(252).pct_change(21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 504d Liabilities Growth for debt trajectory
def f24_debt_trajectory_liab_growth_504d_jerk_v034_signal(liabilities) -> pd.Series:
    slope = liabilities.pct_change(504).pct_change(63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 756d Liabilities Growth for debt trajectory
def f24_debt_trajectory_liab_growth_756d_jerk_v035_signal(liabilities) -> pd.Series:
    slope = liabilities.pct_change(756).pct_change(63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 1260d Liabilities Growth for debt trajectory
def f24_debt_trajectory_liab_growth_1260d_jerk_v036_signal(liabilities) -> pd.Series:
    slope = liabilities.pct_change(1260).pct_change(126)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 63d average Debt to Revenue ratio for debt trajectory
def f24_debt_trajectory_debt_rev_63d_jerk_v037_signal(debt, revenue) -> pd.Series:
    base = _sma(_dt_ratio(debt, revenue), 63)
    slope = _dt_slope(base, 5)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 126d average Debt to Revenue ratio for debt trajectory
def f24_debt_trajectory_debt_rev_126d_jerk_v038_signal(debt, revenue) -> pd.Series:
    base = _sma(_dt_ratio(debt, revenue), 126)
    slope = _dt_slope(base, 21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 252d average Debt to Revenue ratio for debt trajectory
def f24_debt_trajectory_debt_rev_252d_jerk_v039_signal(debt, revenue) -> pd.Series:
    base = _sma(_dt_ratio(debt, revenue), 252)
    slope = _dt_slope(base, 21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 504d average Debt to Revenue ratio for debt trajectory
def f24_debt_trajectory_debt_rev_504d_jerk_v040_signal(debt, revenue) -> pd.Series:
    base = _sma(_dt_ratio(debt, revenue), 504)
    slope = _dt_slope(base, 63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 756d average Debt to Revenue ratio for debt trajectory
def f24_debt_trajectory_debt_rev_756d_jerk_v041_signal(debt, revenue) -> pd.Series:
    base = _sma(_dt_ratio(debt, revenue), 756)
    slope = _dt_slope(base, 63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 1260d average Debt to Revenue ratio for debt trajectory
def f24_debt_trajectory_debt_rev_1260d_jerk_v042_signal(debt, revenue) -> pd.Series:
    base = _sma(_dt_ratio(debt, revenue), 1260)
    slope = _dt_slope(base, 126)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 63d average Working Capital to Debt ratio for debt trajectory
def f24_debt_trajectory_wc_debt_63d_jerk_v043_signal(workingcapital, debt) -> pd.Series:
    base = _sma(_dt_ratio(workingcapital, debt), 63)
    slope = _dt_slope(base, 5)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 126d average Working Capital to Debt ratio for debt trajectory
def f24_debt_trajectory_wc_debt_126d_jerk_v044_signal(workingcapital, debt) -> pd.Series:
    base = _sma(_dt_ratio(workingcapital, debt), 126)
    slope = _dt_slope(base, 21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 252d average Working Capital to Debt ratio for debt trajectory
def f24_debt_trajectory_wc_debt_252d_jerk_v045_signal(workingcapital, debt) -> pd.Series:
    base = _sma(_dt_ratio(workingcapital, debt), 252)
    slope = _dt_slope(base, 21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 504d average Working Capital to Debt ratio for debt trajectory
def f24_debt_trajectory_wc_debt_504d_jerk_v046_signal(workingcapital, debt) -> pd.Series:
    base = _sma(_dt_ratio(workingcapital, debt), 504)
    slope = _dt_slope(base, 63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 756d average Working Capital to Debt ratio for debt trajectory
def f24_debt_trajectory_wc_debt_756d_jerk_v047_signal(workingcapital, debt) -> pd.Series:
    base = _sma(_dt_ratio(workingcapital, debt), 756)
    slope = _dt_slope(base, 63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 1260d average Working Capital to Debt ratio for debt trajectory
def f24_debt_trajectory_wc_debt_1260d_jerk_v048_signal(workingcapital, debt) -> pd.Series:
    base = _sma(_dt_ratio(workingcapital, debt), 1260)
    slope = _dt_slope(base, 126)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 63d average Debt to Working Capital ratio for debt trajectory
def f24_debt_trajectory_debt_wc_63d_jerk_v049_signal(debt, workingcapital) -> pd.Series:
    base = _sma(_dt_ratio(debt, workingcapital), 63)
    slope = _dt_slope(base, 5)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 126d average Debt to Working Capital ratio for debt trajectory
def f24_debt_trajectory_debt_wc_126d_jerk_v050_signal(debt, workingcapital) -> pd.Series:
    base = _sma(_dt_ratio(debt, workingcapital), 126)
    slope = _dt_slope(base, 21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 252d average Debt to Working Capital ratio for debt trajectory
def f24_debt_trajectory_debt_wc_252d_jerk_v051_signal(debt, workingcapital) -> pd.Series:
    base = _sma(_dt_ratio(debt, workingcapital), 252)
    slope = _dt_slope(base, 21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 504d average Debt to Working Capital ratio for debt trajectory
def f24_debt_trajectory_debt_wc_504d_jerk_v052_signal(debt, workingcapital) -> pd.Series:
    base = _sma(_dt_ratio(debt, workingcapital), 504)
    slope = _dt_slope(base, 63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 756d average Debt to Working Capital ratio for debt trajectory
def f24_debt_trajectory_debt_wc_756d_jerk_v053_signal(debt, workingcapital) -> pd.Series:
    base = _sma(_dt_ratio(debt, workingcapital), 756)
    slope = _dt_slope(base, 63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 1260d average Debt to Working Capital ratio for debt trajectory
def f24_debt_trajectory_debt_wc_1260d_jerk_v054_signal(debt, workingcapital) -> pd.Series:
    base = _sma(_dt_ratio(debt, workingcapital), 1260)
    slope = _dt_slope(base, 126)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 63d average Liabilities to EBITDA ratio for debt trajectory
def f24_debt_trajectory_liab_ebitda_63d_jerk_v076_signal(liabilities, ebitda) -> pd.Series:
    base = _sma(_dt_ratio(liabilities, ebitda), 63)
    slope = _dt_slope(base, 5)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 126d average Liabilities to EBITDA ratio for debt trajectory
def f24_debt_trajectory_liab_ebitda_126d_jerk_v077_signal(liabilities, ebitda) -> pd.Series:
    base = _sma(_dt_ratio(liabilities, ebitda), 126)
    slope = _dt_slope(base, 21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 252d average Liabilities to EBITDA ratio for debt trajectory
def f24_debt_trajectory_liab_ebitda_252d_jerk_v078_signal(liabilities, ebitda) -> pd.Series:
    base = _sma(_dt_ratio(liabilities, ebitda), 252)
    slope = _dt_slope(base, 21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 504d average Liabilities to EBITDA ratio for debt trajectory
def f24_debt_trajectory_liab_ebitda_504d_jerk_v079_signal(liabilities, ebitda) -> pd.Series:
    base = _sma(_dt_ratio(liabilities, ebitda), 504)
    slope = _dt_slope(base, 63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 756d average Liabilities to EBITDA ratio for debt trajectory
def f24_debt_trajectory_liab_ebitda_756d_jerk_v080_signal(liabilities, ebitda) -> pd.Series:
    base = _sma(_dt_ratio(liabilities, ebitda), 756)
    slope = _dt_slope(base, 63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 1260d average Liabilities to EBITDA ratio for debt trajectory
def f24_debt_trajectory_liab_ebitda_1260d_jerk_v081_signal(liabilities, ebitda) -> pd.Series:
    base = _sma(_dt_ratio(liabilities, ebitda), 1260)
    slope = _dt_slope(base, 126)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 63d average Liabilities to Revenue ratio for debt trajectory
def f24_debt_trajectory_liab_rev_63d_jerk_v082_signal(liabilities, revenue) -> pd.Series:
    base = _sma(_dt_ratio(liabilities, revenue), 63)
    slope = _dt_slope(base, 5)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 126d average Liabilities to Revenue ratio for debt trajectory
def f24_debt_trajectory_liab_rev_126d_jerk_v083_signal(liabilities, revenue) -> pd.Series:
    base = _sma(_dt_ratio(liabilities, revenue), 126)
    slope = _dt_slope(base, 21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 252d average Liabilities to Revenue ratio for debt trajectory
def f24_debt_trajectory_liab_rev_252d_jerk_v084_signal(liabilities, revenue) -> pd.Series:
    base = _sma(_dt_ratio(liabilities, revenue), 252)
    slope = _dt_slope(base, 21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 504d average Liabilities to Revenue ratio for debt trajectory
def f24_debt_trajectory_liab_rev_504d_jerk_v085_signal(liabilities, revenue) -> pd.Series:
    base = _sma(_dt_ratio(liabilities, revenue), 504)
    slope = _dt_slope(base, 63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 756d average Liabilities to Revenue ratio for debt trajectory
def f24_debt_trajectory_liab_rev_756d_jerk_v086_signal(liabilities, revenue) -> pd.Series:
    base = _sma(_dt_ratio(liabilities, revenue), 756)
    slope = _dt_slope(base, 63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 1260d average Liabilities to Revenue ratio for debt trajectory
def f24_debt_trajectory_liab_rev_1260d_jerk_v087_signal(liabilities, revenue) -> pd.Series:
    base = _sma(_dt_ratio(liabilities, revenue), 1260)
    slope = _dt_slope(base, 126)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 63d average Liabilities to Equity ratio for debt trajectory
def f24_debt_trajectory_liab_equity_63d_jerk_v088_signal(liabilities, equity) -> pd.Series:
    base = _sma(_dt_ratio(liabilities, equity), 63)
    slope = _dt_slope(base, 5)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 126d average Liabilities to Equity ratio for debt trajectory
def f24_debt_trajectory_liab_equity_126d_jerk_v089_signal(liabilities, equity) -> pd.Series:
    base = _sma(_dt_ratio(liabilities, equity), 126)
    slope = _dt_slope(base, 21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 252d average Liabilities to Equity ratio for debt trajectory
def f24_debt_trajectory_liab_equity_252d_jerk_v090_signal(liabilities, equity) -> pd.Series:
    base = _sma(_dt_ratio(liabilities, equity), 252)
    slope = _dt_slope(base, 21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 504d average Liabilities to Equity ratio for debt trajectory
def f24_debt_trajectory_liab_equity_504d_jerk_v091_signal(liabilities, equity) -> pd.Series:
    base = _sma(_dt_ratio(liabilities, equity), 504)
    slope = _dt_slope(base, 63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 756d average Liabilities to Equity ratio for debt trajectory
def f24_debt_trajectory_liab_equity_756d_jerk_v092_signal(liabilities, equity) -> pd.Series:
    base = _sma(_dt_ratio(liabilities, equity), 756)
    slope = _dt_slope(base, 63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 1260d average Liabilities to Equity ratio for debt trajectory
def f24_debt_trajectory_liab_equity_1260d_jerk_v093_signal(liabilities, equity) -> pd.Series:
    base = _sma(_dt_ratio(liabilities, equity), 1260)
    slope = _dt_slope(base, 126)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 63d Debt CV for debt trajectory
def f24_debt_trajectory_debt_cv_63d_jerk_v094_signal(debt) -> pd.Series:
    base = _std(debt, 63) / _sma(debt, 63).abs().replace(0, np.nan)
    slope = base.pct_change(5)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 126d Debt CV for debt trajectory
def f24_debt_trajectory_debt_cv_126d_jerk_v095_signal(debt) -> pd.Series:
    base = _std(debt, 126) / _sma(debt, 126).abs().replace(0, np.nan)
    slope = base.pct_change(21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 252d Debt CV for debt trajectory
def f24_debt_trajectory_debt_cv_252d_jerk_v096_signal(debt) -> pd.Series:
    base = _std(debt, 252) / _sma(debt, 252).abs().replace(0, np.nan)
    slope = base.pct_change(21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 504d Debt CV for debt trajectory
def f24_debt_trajectory_debt_cv_504d_jerk_v097_signal(debt) -> pd.Series:
    base = _std(debt, 504) / _sma(debt, 504).abs().replace(0, np.nan)
    slope = base.pct_change(63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 756d Debt CV for debt trajectory
def f24_debt_trajectory_debt_cv_756d_jerk_v098_signal(debt) -> pd.Series:
    base = _std(debt, 756) / _sma(debt, 756).abs().replace(0, np.nan)
    slope = base.pct_change(63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 1260d Debt CV for debt trajectory
def f24_debt_trajectory_debt_cv_1260d_jerk_v099_signal(debt) -> pd.Series:
    base = _std(debt, 1260) / _sma(debt, 1260).abs().replace(0, np.nan)
    slope = base.pct_change(126)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 63d Liabilities CV for debt trajectory
def f24_debt_trajectory_liab_cv_63d_jerk_v100_signal(liabilities) -> pd.Series:
    base = _std(liabilities, 63) / _sma(liabilities, 63).abs().replace(0, np.nan)
    slope = base.pct_change(5)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 126d Liabilities CV for debt trajectory
def f24_debt_trajectory_liab_cv_126d_jerk_v101_signal(liabilities) -> pd.Series:
    base = _std(liabilities, 126) / _sma(liabilities, 126).abs().replace(0, np.nan)
    slope = base.pct_change(21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 252d Liabilities CV for debt trajectory
def f24_debt_trajectory_liab_cv_252d_jerk_v102_signal(liabilities) -> pd.Series:
    base = _std(liabilities, 252) / _sma(liabilities, 252).abs().replace(0, np.nan)
    slope = base.pct_change(21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 504d Liabilities CV for debt trajectory
def f24_debt_trajectory_liab_cv_504d_jerk_v103_signal(liabilities) -> pd.Series:
    base = _std(liabilities, 504) / _sma(liabilities, 504).abs().replace(0, np.nan)
    slope = base.pct_change(63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 756d Liabilities CV for debt trajectory
def f24_debt_trajectory_liab_cv_756d_jerk_v104_signal(liabilities) -> pd.Series:
    base = _std(liabilities, 756) / _sma(liabilities, 756).abs().replace(0, np.nan)
    slope = base.pct_change(63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 1260d Liabilities CV for debt trajectory
def f24_debt_trajectory_liab_cv_1260d_jerk_v105_signal(liabilities) -> pd.Series:
    base = _std(liabilities, 1260) / _sma(liabilities, 1260).abs().replace(0, np.nan)
    slope = base.pct_change(126)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 63d average Current Ratio for debt trajectory
def f24_debt_trajectory_current_ratio_63d_jerk_v112_signal(currentratio) -> pd.Series:
    base = _sma(currentratio, 63)
    slope = base.pct_change(5)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 126d average Current Ratio for debt trajectory
def f24_debt_trajectory_current_ratio_126d_jerk_v113_signal(currentratio) -> pd.Series:
    base = _sma(currentratio, 126)
    slope = base.pct_change(21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 252d average Current Ratio for debt trajectory
def f24_debt_trajectory_current_ratio_252d_jerk_v114_signal(currentratio) -> pd.Series:
    base = _sma(currentratio, 252)
    slope = base.pct_change(21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 504d average Current Ratio for debt trajectory
def f24_debt_trajectory_current_ratio_504d_jerk_v115_signal(currentratio) -> pd.Series:
    base = _sma(currentratio, 504)
    slope = base.pct_change(63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 756d average Current Ratio for debt trajectory
def f24_debt_trajectory_current_ratio_756d_jerk_v116_signal(currentratio) -> pd.Series:
    base = _sma(currentratio, 756)
    slope = base.pct_change(63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 1260d average Current Ratio for debt trajectory
def f24_debt_trajectory_current_ratio_1260d_jerk_v117_signal(currentratio) -> pd.Series:
    base = _sma(currentratio, 1260)
    slope = base.pct_change(126)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 63d average Assets/Liab for debt trajectory
def f24_debt_trajectory_assets_liab_63d_jerk_v136_signal(assets, liabilities) -> pd.Series:
    base = _sma(_dt_ratio(assets, liabilities), 63)
    slope = _dt_slope(base, 5)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 126d average Assets/Liab for debt trajectory
def f24_debt_trajectory_assets_liab_126d_jerk_v137_signal(assets, liabilities) -> pd.Series:
    base = _sma(_dt_ratio(assets, liabilities), 126)
    slope = _dt_slope(base, 21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 252d average Assets/Liab for debt trajectory
def f24_debt_trajectory_assets_liab_252d_jerk_v138_signal(assets, liabilities) -> pd.Series:
    base = _sma(_dt_ratio(assets, liabilities), 252)
    slope = _dt_slope(base, 21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 504d average Assets/Liab for debt trajectory
def f24_debt_trajectory_assets_liab_504d_jerk_v139_signal(assets, liabilities) -> pd.Series:
    base = _sma(_dt_ratio(assets, liabilities), 504)
    slope = _dt_slope(base, 63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 756d average Assets/Liab for debt trajectory
def f24_debt_trajectory_assets_liab_756d_jerk_v140_signal(assets, liabilities) -> pd.Series:
    base = _sma(_dt_ratio(assets, liabilities), 756)
    slope = _dt_slope(base, 63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 1260d average Assets/Liab for debt trajectory
def f24_debt_trajectory_assets_liab_1260d_jerk_v141_signal(assets, liabilities) -> pd.Series:
    base = _sma(_dt_ratio(assets, liabilities), 1260)
    slope = _dt_slope(base, 126)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 252d average OpInc/Liab for debt trajectory
def f24_debt_trajectory_opinc_liab_252d_jerk_v148_signal(opinc, liabilities) -> pd.Series:
    base = _sma(_dt_ratio(opinc, liabilities), 252)
    slope = _dt_slope(base, 21)
    res = _dt_jerk(slope, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 504d average OpInc/Liab for debt trajectory
def f24_debt_trajectory_opinc_liab_504d_jerk_v149_signal(opinc, liabilities) -> pd.Series:
    base = _sma(_dt_ratio(opinc, liabilities), 504)
    slope = _dt_slope(base, 63)
    res = _dt_jerk(slope, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 756d average OpInc/Liab for debt trajectory
def f24_debt_trajectory_opinc_liab_756d_jerk_v150_signal(opinc, liabilities) -> pd.Series:
    base = _sma(_dt_ratio(opinc, liabilities), 756)
    slope = _dt_slope(base, 63)
    res = _dt_jerk(slope, 21)
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
        "liabilities": np.random.normal(200, 40, n),
        "currentratio": np.random.normal(1.5, 0.3, n),
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
        assert any(prim in source for prim in ["_dt_ratio", "_dt_slope", "_dt_jerk"])

    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f24_debt_trajectory_"))]}
F24_DEBT_TRAJECTORY_REGISTRY_JERK = REGISTRY
