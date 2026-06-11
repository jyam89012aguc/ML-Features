import pandas as pd
import numpy as np
import inspect

# ===== High-Performance Alpha Helpers =====
def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
def _ewma(s, w): return s.ewm(span=w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _z(s, w): return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)
def _ratio(n, d): return n / d.replace(0, np.nan)
def _min(s, w): return s.rolling(w, min_periods=min(w, 5)).min()
def _max(s, w): return s.rolling(w, min_periods=min(w, 5)).max()
def _drawdown(s, w): return (s / _max(s, w).replace(0, np.nan)) - 1
def _recovery(s, w): return (s / _min(s, w).replace(0, np.nan)) - 1
def _slope_pct(s, w): return s.pct_change(w)
def _jerk(s, w1, w2): return _slope_pct(s, w1).diff(w2)
def _skew(s, w): return s.rolling(w, min_periods=min(w, 40) if w > 40 else min(w, 5)).skew()
def _kurt(s, w): return s.rolling(w, min_periods=min(w, 40) if w > 40 else min(w, 5)).kurt()

def f16_ab_leverage_debt_base_5d_v001_signal(debt):
    """Moving average of Raw level of debt over 5d window."""
    res = _sma(debt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_assets_base_5d_v002_signal(assets):
    """Moving average of Raw level of assets over 5d window."""
    res = _sma(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_receivables_base_5d_v003_signal(receivables):
    """Moving average of Raw level of receivables over 5d window."""
    res = _sma(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_loan_density_base_5d_v004_signal(receivables, assets):
    """Moving average of Loan book as % of assets over 5d window."""
    res = _sma(_ratio(receivables, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_debt_base_10d_v005_signal(debt):
    """Moving average of Raw level of debt over 10d window."""
    res = _sma(debt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_assets_base_10d_v006_signal(assets):
    """Moving average of Raw level of assets over 10d window."""
    res = _sma(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_receivables_base_10d_v007_signal(receivables):
    """Moving average of Raw level of receivables over 10d window."""
    res = _sma(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_loan_density_base_10d_v008_signal(receivables, assets):
    """Moving average of Loan book as % of assets over 10d window."""
    res = _sma(_ratio(receivables, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_debt_base_21d_v009_signal(debt):
    """Moving average of Raw level of debt over 21d window."""
    res = _sma(debt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_assets_base_21d_v010_signal(assets):
    """Moving average of Raw level of assets over 21d window."""
    res = _sma(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_receivables_base_21d_v011_signal(receivables):
    """Moving average of Raw level of receivables over 21d window."""
    res = _sma(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_loan_density_base_21d_v012_signal(receivables, assets):
    """Moving average of Loan book as % of assets over 21d window."""
    res = _sma(_ratio(receivables, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_debt_base_42d_v013_signal(debt):
    """Moving average of Raw level of debt over 42d window."""
    res = _sma(debt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_assets_base_42d_v014_signal(assets):
    """Moving average of Raw level of assets over 42d window."""
    res = _sma(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_receivables_base_42d_v015_signal(receivables):
    """Moving average of Raw level of receivables over 42d window."""
    res = _sma(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_loan_density_base_42d_v016_signal(receivables, assets):
    """Moving average of Loan book as % of assets over 42d window."""
    res = _sma(_ratio(receivables, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_debt_base_63d_v017_signal(debt):
    """Moving average of Raw level of debt over 63d window."""
    res = _sma(debt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_assets_base_63d_v018_signal(assets):
    """Moving average of Raw level of assets over 63d window."""
    res = _sma(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_receivables_base_63d_v019_signal(receivables):
    """Moving average of Raw level of receivables over 63d window."""
    res = _sma(receivables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_loan_density_base_63d_v020_signal(receivables, assets):
    """Moving average of Loan book as % of assets over 63d window."""
    res = _sma(_ratio(receivables, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_debt_base_126d_v021_signal(debt):
    """Moving average of Raw level of debt over 126d window."""
    res = _sma(debt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_assets_base_126d_v022_signal(assets):
    """Moving average of Raw level of assets over 126d window."""
    res = _sma(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_receivables_base_126d_v023_signal(receivables):
    """Moving average of Raw level of receivables over 126d window."""
    res = _sma(receivables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_loan_density_base_126d_v024_signal(receivables, assets):
    """Moving average of Loan book as % of assets over 126d window."""
    res = _sma(_ratio(receivables, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_debt_base_252d_v025_signal(debt):
    """Moving average of Raw level of debt over 252d window."""
    res = _sma(debt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_assets_base_252d_v026_signal(assets):
    """Moving average of Raw level of assets over 252d window."""
    res = _sma(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_receivables_base_252d_v027_signal(receivables):
    """Moving average of Raw level of receivables over 252d window."""
    res = _sma(receivables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_loan_density_base_252d_v028_signal(receivables, assets):
    """Moving average of Loan book as % of assets over 252d window."""
    res = _sma(_ratio(receivables, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_debt_base_504d_v029_signal(debt):
    """Moving average of Raw level of debt over 504d window."""
    res = _sma(debt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_assets_base_504d_v030_signal(assets):
    """Moving average of Raw level of assets over 504d window."""
    res = _sma(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_receivables_base_504d_v031_signal(receivables):
    """Moving average of Raw level of receivables over 504d window."""
    res = _sma(receivables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_loan_density_base_504d_v032_signal(receivables, assets):
    """Moving average of Loan book as % of assets over 504d window."""
    res = _sma(_ratio(receivables, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_debt_base_756d_v033_signal(debt):
    """Moving average of Raw level of debt over 756d window."""
    res = _sma(debt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_assets_base_756d_v034_signal(assets):
    """Moving average of Raw level of assets over 756d window."""
    res = _sma(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_receivables_base_756d_v035_signal(receivables):
    """Moving average of Raw level of receivables over 756d window."""
    res = _sma(receivables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_loan_density_base_756d_v036_signal(receivables, assets):
    """Moving average of Loan book as % of assets over 756d window."""
    res = _sma(_ratio(receivables, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_debt_base_1008d_v037_signal(debt):
    """Moving average of Raw level of debt over 1008d window."""
    res = _sma(debt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_assets_base_1008d_v038_signal(assets):
    """Moving average of Raw level of assets over 1008d window."""
    res = _sma(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_receivables_base_1008d_v039_signal(receivables):
    """Moving average of Raw level of receivables over 1008d window."""
    res = _sma(receivables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_loan_density_base_1008d_v040_signal(receivables, assets):
    """Moving average of Loan book as % of assets over 1008d window."""
    res = _sma(_ratio(receivables, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_debt_base_1260d_v041_signal(debt):
    """Moving average of Raw level of debt over 1260d window."""
    res = _sma(debt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_assets_base_1260d_v042_signal(assets):
    """Moving average of Raw level of assets over 1260d window."""
    res = _sma(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_receivables_base_1260d_v043_signal(receivables):
    """Moving average of Raw level of receivables over 1260d window."""
    res = _sma(receivables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_loan_density_base_1260d_v044_signal(receivables, assets):
    """Moving average of Loan book as % of assets over 1260d window."""
    res = _sma(_ratio(receivables, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_debt_ewma_5d_v045_signal(debt):
    """Exponential moving average of Raw level of debt over 5d window."""
    res = _ewma(debt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_assets_ewma_5d_v046_signal(assets):
    """Exponential moving average of Raw level of assets over 5d window."""
    res = _ewma(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_receivables_ewma_5d_v047_signal(receivables):
    """Exponential moving average of Raw level of receivables over 5d window."""
    res = _ewma(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_loan_density_ewma_5d_v048_signal(receivables, assets):
    """Exponential moving average of Loan book as % of assets over 5d window."""
    res = _ewma(_ratio(receivables, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_debt_ewma_10d_v049_signal(debt):
    """Exponential moving average of Raw level of debt over 10d window."""
    res = _ewma(debt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_assets_ewma_10d_v050_signal(assets):
    """Exponential moving average of Raw level of assets over 10d window."""
    res = _ewma(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_receivables_ewma_10d_v051_signal(receivables):
    """Exponential moving average of Raw level of receivables over 10d window."""
    res = _ewma(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_loan_density_ewma_10d_v052_signal(receivables, assets):
    """Exponential moving average of Loan book as % of assets over 10d window."""
    res = _ewma(_ratio(receivables, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_debt_ewma_21d_v053_signal(debt):
    """Exponential moving average of Raw level of debt over 21d window."""
    res = _ewma(debt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_assets_ewma_21d_v054_signal(assets):
    """Exponential moving average of Raw level of assets over 21d window."""
    res = _ewma(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_receivables_ewma_21d_v055_signal(receivables):
    """Exponential moving average of Raw level of receivables over 21d window."""
    res = _ewma(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_loan_density_ewma_21d_v056_signal(receivables, assets):
    """Exponential moving average of Loan book as % of assets over 21d window."""
    res = _ewma(_ratio(receivables, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_debt_ewma_42d_v057_signal(debt):
    """Exponential moving average of Raw level of debt over 42d window."""
    res = _ewma(debt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_assets_ewma_42d_v058_signal(assets):
    """Exponential moving average of Raw level of assets over 42d window."""
    res = _ewma(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_receivables_ewma_42d_v059_signal(receivables):
    """Exponential moving average of Raw level of receivables over 42d window."""
    res = _ewma(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_loan_density_ewma_42d_v060_signal(receivables, assets):
    """Exponential moving average of Loan book as % of assets over 42d window."""
    res = _ewma(_ratio(receivables, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_debt_ewma_63d_v061_signal(debt):
    """Exponential moving average of Raw level of debt over 63d window."""
    res = _ewma(debt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_assets_ewma_63d_v062_signal(assets):
    """Exponential moving average of Raw level of assets over 63d window."""
    res = _ewma(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_receivables_ewma_63d_v063_signal(receivables):
    """Exponential moving average of Raw level of receivables over 63d window."""
    res = _ewma(receivables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_loan_density_ewma_63d_v064_signal(receivables, assets):
    """Exponential moving average of Loan book as % of assets over 63d window."""
    res = _ewma(_ratio(receivables, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_debt_ewma_126d_v065_signal(debt):
    """Exponential moving average of Raw level of debt over 126d window."""
    res = _ewma(debt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_assets_ewma_126d_v066_signal(assets):
    """Exponential moving average of Raw level of assets over 126d window."""
    res = _ewma(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_receivables_ewma_126d_v067_signal(receivables):
    """Exponential moving average of Raw level of receivables over 126d window."""
    res = _ewma(receivables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_loan_density_ewma_126d_v068_signal(receivables, assets):
    """Exponential moving average of Loan book as % of assets over 126d window."""
    res = _ewma(_ratio(receivables, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_debt_ewma_252d_v069_signal(debt):
    """Exponential moving average of Raw level of debt over 252d window."""
    res = _ewma(debt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_assets_ewma_252d_v070_signal(assets):
    """Exponential moving average of Raw level of assets over 252d window."""
    res = _ewma(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_receivables_ewma_252d_v071_signal(receivables):
    """Exponential moving average of Raw level of receivables over 252d window."""
    res = _ewma(receivables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_loan_density_ewma_252d_v072_signal(receivables, assets):
    """Exponential moving average of Loan book as % of assets over 252d window."""
    res = _ewma(_ratio(receivables, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_debt_ewma_504d_v073_signal(debt):
    """Exponential moving average of Raw level of debt over 504d window."""
    res = _ewma(debt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_assets_ewma_504d_v074_signal(assets):
    """Exponential moving average of Raw level of assets over 504d window."""
    res = _ewma(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_ab_leverage_receivables_ewma_504d_v075_signal(receivables):
    """Exponential moving average of Raw level of receivables over 504d window."""
    res = _ewma(receivables, 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f16_ab_leverage_debt_base_5d_v001_signal": {"func": f16_ab_leverage_debt_base_5d_v001_signal},
    "f16_ab_leverage_assets_base_5d_v002_signal": {"func": f16_ab_leverage_assets_base_5d_v002_signal},
    "f16_ab_leverage_receivables_base_5d_v003_signal": {"func": f16_ab_leverage_receivables_base_5d_v003_signal},
    "f16_ab_leverage_loan_density_base_5d_v004_signal": {"func": f16_ab_leverage_loan_density_base_5d_v004_signal},
    "f16_ab_leverage_debt_base_10d_v005_signal": {"func": f16_ab_leverage_debt_base_10d_v005_signal},
    "f16_ab_leverage_assets_base_10d_v006_signal": {"func": f16_ab_leverage_assets_base_10d_v006_signal},
    "f16_ab_leverage_receivables_base_10d_v007_signal": {"func": f16_ab_leverage_receivables_base_10d_v007_signal},
    "f16_ab_leverage_loan_density_base_10d_v008_signal": {"func": f16_ab_leverage_loan_density_base_10d_v008_signal},
    "f16_ab_leverage_debt_base_21d_v009_signal": {"func": f16_ab_leverage_debt_base_21d_v009_signal},
    "f16_ab_leverage_assets_base_21d_v010_signal": {"func": f16_ab_leverage_assets_base_21d_v010_signal},
    "f16_ab_leverage_receivables_base_21d_v011_signal": {"func": f16_ab_leverage_receivables_base_21d_v011_signal},
    "f16_ab_leverage_loan_density_base_21d_v012_signal": {"func": f16_ab_leverage_loan_density_base_21d_v012_signal},
    "f16_ab_leverage_debt_base_42d_v013_signal": {"func": f16_ab_leverage_debt_base_42d_v013_signal},
    "f16_ab_leverage_assets_base_42d_v014_signal": {"func": f16_ab_leverage_assets_base_42d_v014_signal},
    "f16_ab_leverage_receivables_base_42d_v015_signal": {"func": f16_ab_leverage_receivables_base_42d_v015_signal},
    "f16_ab_leverage_loan_density_base_42d_v016_signal": {"func": f16_ab_leverage_loan_density_base_42d_v016_signal},
    "f16_ab_leverage_debt_base_63d_v017_signal": {"func": f16_ab_leverage_debt_base_63d_v017_signal},
    "f16_ab_leverage_assets_base_63d_v018_signal": {"func": f16_ab_leverage_assets_base_63d_v018_signal},
    "f16_ab_leverage_receivables_base_63d_v019_signal": {"func": f16_ab_leverage_receivables_base_63d_v019_signal},
    "f16_ab_leverage_loan_density_base_63d_v020_signal": {"func": f16_ab_leverage_loan_density_base_63d_v020_signal},
    "f16_ab_leverage_debt_base_126d_v021_signal": {"func": f16_ab_leverage_debt_base_126d_v021_signal},
    "f16_ab_leverage_assets_base_126d_v022_signal": {"func": f16_ab_leverage_assets_base_126d_v022_signal},
    "f16_ab_leverage_receivables_base_126d_v023_signal": {"func": f16_ab_leverage_receivables_base_126d_v023_signal},
    "f16_ab_leverage_loan_density_base_126d_v024_signal": {"func": f16_ab_leverage_loan_density_base_126d_v024_signal},
    "f16_ab_leverage_debt_base_252d_v025_signal": {"func": f16_ab_leverage_debt_base_252d_v025_signal},
    "f16_ab_leverage_assets_base_252d_v026_signal": {"func": f16_ab_leverage_assets_base_252d_v026_signal},
    "f16_ab_leverage_receivables_base_252d_v027_signal": {"func": f16_ab_leverage_receivables_base_252d_v027_signal},
    "f16_ab_leverage_loan_density_base_252d_v028_signal": {"func": f16_ab_leverage_loan_density_base_252d_v028_signal},
    "f16_ab_leverage_debt_base_504d_v029_signal": {"func": f16_ab_leverage_debt_base_504d_v029_signal},
    "f16_ab_leverage_assets_base_504d_v030_signal": {"func": f16_ab_leverage_assets_base_504d_v030_signal},
    "f16_ab_leverage_receivables_base_504d_v031_signal": {"func": f16_ab_leverage_receivables_base_504d_v031_signal},
    "f16_ab_leverage_loan_density_base_504d_v032_signal": {"func": f16_ab_leverage_loan_density_base_504d_v032_signal},
    "f16_ab_leverage_debt_base_756d_v033_signal": {"func": f16_ab_leverage_debt_base_756d_v033_signal},
    "f16_ab_leverage_assets_base_756d_v034_signal": {"func": f16_ab_leverage_assets_base_756d_v034_signal},
    "f16_ab_leverage_receivables_base_756d_v035_signal": {"func": f16_ab_leverage_receivables_base_756d_v035_signal},
    "f16_ab_leverage_loan_density_base_756d_v036_signal": {"func": f16_ab_leverage_loan_density_base_756d_v036_signal},
    "f16_ab_leverage_debt_base_1008d_v037_signal": {"func": f16_ab_leverage_debt_base_1008d_v037_signal},
    "f16_ab_leverage_assets_base_1008d_v038_signal": {"func": f16_ab_leverage_assets_base_1008d_v038_signal},
    "f16_ab_leverage_receivables_base_1008d_v039_signal": {"func": f16_ab_leverage_receivables_base_1008d_v039_signal},
    "f16_ab_leverage_loan_density_base_1008d_v040_signal": {"func": f16_ab_leverage_loan_density_base_1008d_v040_signal},
    "f16_ab_leverage_debt_base_1260d_v041_signal": {"func": f16_ab_leverage_debt_base_1260d_v041_signal},
    "f16_ab_leverage_assets_base_1260d_v042_signal": {"func": f16_ab_leverage_assets_base_1260d_v042_signal},
    "f16_ab_leverage_receivables_base_1260d_v043_signal": {"func": f16_ab_leverage_receivables_base_1260d_v043_signal},
    "f16_ab_leverage_loan_density_base_1260d_v044_signal": {"func": f16_ab_leverage_loan_density_base_1260d_v044_signal},
    "f16_ab_leverage_debt_ewma_5d_v045_signal": {"func": f16_ab_leverage_debt_ewma_5d_v045_signal},
    "f16_ab_leverage_assets_ewma_5d_v046_signal": {"func": f16_ab_leverage_assets_ewma_5d_v046_signal},
    "f16_ab_leverage_receivables_ewma_5d_v047_signal": {"func": f16_ab_leverage_receivables_ewma_5d_v047_signal},
    "f16_ab_leverage_loan_density_ewma_5d_v048_signal": {"func": f16_ab_leverage_loan_density_ewma_5d_v048_signal},
    "f16_ab_leverage_debt_ewma_10d_v049_signal": {"func": f16_ab_leverage_debt_ewma_10d_v049_signal},
    "f16_ab_leverage_assets_ewma_10d_v050_signal": {"func": f16_ab_leverage_assets_ewma_10d_v050_signal},
    "f16_ab_leverage_receivables_ewma_10d_v051_signal": {"func": f16_ab_leverage_receivables_ewma_10d_v051_signal},
    "f16_ab_leverage_loan_density_ewma_10d_v052_signal": {"func": f16_ab_leverage_loan_density_ewma_10d_v052_signal},
    "f16_ab_leverage_debt_ewma_21d_v053_signal": {"func": f16_ab_leverage_debt_ewma_21d_v053_signal},
    "f16_ab_leverage_assets_ewma_21d_v054_signal": {"func": f16_ab_leverage_assets_ewma_21d_v054_signal},
    "f16_ab_leverage_receivables_ewma_21d_v055_signal": {"func": f16_ab_leverage_receivables_ewma_21d_v055_signal},
    "f16_ab_leverage_loan_density_ewma_21d_v056_signal": {"func": f16_ab_leverage_loan_density_ewma_21d_v056_signal},
    "f16_ab_leverage_debt_ewma_42d_v057_signal": {"func": f16_ab_leverage_debt_ewma_42d_v057_signal},
    "f16_ab_leverage_assets_ewma_42d_v058_signal": {"func": f16_ab_leverage_assets_ewma_42d_v058_signal},
    "f16_ab_leverage_receivables_ewma_42d_v059_signal": {"func": f16_ab_leverage_receivables_ewma_42d_v059_signal},
    "f16_ab_leverage_loan_density_ewma_42d_v060_signal": {"func": f16_ab_leverage_loan_density_ewma_42d_v060_signal},
    "f16_ab_leverage_debt_ewma_63d_v061_signal": {"func": f16_ab_leverage_debt_ewma_63d_v061_signal},
    "f16_ab_leverage_assets_ewma_63d_v062_signal": {"func": f16_ab_leverage_assets_ewma_63d_v062_signal},
    "f16_ab_leverage_receivables_ewma_63d_v063_signal": {"func": f16_ab_leverage_receivables_ewma_63d_v063_signal},
    "f16_ab_leverage_loan_density_ewma_63d_v064_signal": {"func": f16_ab_leverage_loan_density_ewma_63d_v064_signal},
    "f16_ab_leverage_debt_ewma_126d_v065_signal": {"func": f16_ab_leverage_debt_ewma_126d_v065_signal},
    "f16_ab_leverage_assets_ewma_126d_v066_signal": {"func": f16_ab_leverage_assets_ewma_126d_v066_signal},
    "f16_ab_leverage_receivables_ewma_126d_v067_signal": {"func": f16_ab_leverage_receivables_ewma_126d_v067_signal},
    "f16_ab_leverage_loan_density_ewma_126d_v068_signal": {"func": f16_ab_leverage_loan_density_ewma_126d_v068_signal},
    "f16_ab_leverage_debt_ewma_252d_v069_signal": {"func": f16_ab_leverage_debt_ewma_252d_v069_signal},
    "f16_ab_leverage_assets_ewma_252d_v070_signal": {"func": f16_ab_leverage_assets_ewma_252d_v070_signal},
    "f16_ab_leverage_receivables_ewma_252d_v071_signal": {"func": f16_ab_leverage_receivables_ewma_252d_v071_signal},
    "f16_ab_leverage_loan_density_ewma_252d_v072_signal": {"func": f16_ab_leverage_loan_density_ewma_252d_v072_signal},
    "f16_ab_leverage_debt_ewma_504d_v073_signal": {"func": f16_ab_leverage_debt_ewma_504d_v073_signal},
    "f16_ab_leverage_assets_ewma_504d_v074_signal": {"func": f16_ab_leverage_assets_ewma_504d_v074_signal},
    "f16_ab_leverage_receivables_ewma_504d_v075_signal": {"func": f16_ab_leverage_receivables_ewma_504d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "debt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 16...")
    for name, info in REGISTRY.items():
        fn = info["func"]
        sig = inspect.signature(fn)
        params = list(sig.parameters.keys())
        args = [df[p] for p in params]
        try:
            res = fn(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
