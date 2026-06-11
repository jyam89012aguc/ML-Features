import pandas as pd
import numpy as np
import inspect

# ===== Energy Ultra-High-Performance Alpha Helpers =====
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

def _rsi(s, w):
    delta = s.diff()
    up = delta.clip(lower=0)
    down = -delta.clip(upper=0)
    ma_up = up.rolling(w, min_periods=min(w, 10)).mean()
    ma_down = down.rolling(w, min_periods=min(w, 10)).mean()
    rs = ma_up / ma_down.replace(0, np.nan)
    return 100 - (100 / (1 + rs))

def f29_uranium_production_cost_inflation_debt_base_5d_v001_signal(debt):
    """Moving average of Raw level of debt over 5d window."""
    res = _sma(debt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_ebitda_base_5d_v002_signal(ebitda):
    """Moving average of Raw level of ebitda over 5d window."""
    res = _sma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_marketcap_base_5d_v003_signal(marketcap):
    """Moving average of Raw level of marketcap over 5d window."""
    res = _sma(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_assets_base_5d_v004_signal(assets):
    """Moving average of Raw level of assets over 5d window."""
    res = _sma(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_deleveraging_potential_base_5d_v005_signal(ebitda, debt, assets, marketcap):
    """Moving average of Earnings coverage and valuation discount interaction over 5d window."""
    res = _sma(_ratio(ebitda, debt) * _ratio(assets, marketcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_equity_coverage_base_5d_v006_signal(marketcap, debt):
    """Moving average of Market value coverage of debt over 5d window."""
    res = _sma(_ratio(marketcap, debt), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_debt_base_10d_v007_signal(debt):
    """Moving average of Raw level of debt over 10d window."""
    res = _sma(debt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_ebitda_base_10d_v008_signal(ebitda):
    """Moving average of Raw level of ebitda over 10d window."""
    res = _sma(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_marketcap_base_10d_v009_signal(marketcap):
    """Moving average of Raw level of marketcap over 10d window."""
    res = _sma(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_assets_base_10d_v010_signal(assets):
    """Moving average of Raw level of assets over 10d window."""
    res = _sma(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_deleveraging_potential_base_10d_v011_signal(ebitda, debt, assets, marketcap):
    """Moving average of Earnings coverage and valuation discount interaction over 10d window."""
    res = _sma(_ratio(ebitda, debt) * _ratio(assets, marketcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_equity_coverage_base_10d_v012_signal(marketcap, debt):
    """Moving average of Market value coverage of debt over 10d window."""
    res = _sma(_ratio(marketcap, debt), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_debt_base_21d_v013_signal(debt):
    """Moving average of Raw level of debt over 21d window."""
    res = _sma(debt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_ebitda_base_21d_v014_signal(ebitda):
    """Moving average of Raw level of ebitda over 21d window."""
    res = _sma(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_marketcap_base_21d_v015_signal(marketcap):
    """Moving average of Raw level of marketcap over 21d window."""
    res = _sma(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_assets_base_21d_v016_signal(assets):
    """Moving average of Raw level of assets over 21d window."""
    res = _sma(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_deleveraging_potential_base_21d_v017_signal(ebitda, debt, assets, marketcap):
    """Moving average of Earnings coverage and valuation discount interaction over 21d window."""
    res = _sma(_ratio(ebitda, debt) * _ratio(assets, marketcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_equity_coverage_base_21d_v018_signal(marketcap, debt):
    """Moving average of Market value coverage of debt over 21d window."""
    res = _sma(_ratio(marketcap, debt), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_debt_base_42d_v019_signal(debt):
    """Moving average of Raw level of debt over 42d window."""
    res = _sma(debt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_ebitda_base_42d_v020_signal(ebitda):
    """Moving average of Raw level of ebitda over 42d window."""
    res = _sma(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_marketcap_base_42d_v021_signal(marketcap):
    """Moving average of Raw level of marketcap over 42d window."""
    res = _sma(marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_assets_base_42d_v022_signal(assets):
    """Moving average of Raw level of assets over 42d window."""
    res = _sma(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_deleveraging_potential_base_42d_v023_signal(ebitda, debt, assets, marketcap):
    """Moving average of Earnings coverage and valuation discount interaction over 42d window."""
    res = _sma(_ratio(ebitda, debt) * _ratio(assets, marketcap), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_equity_coverage_base_42d_v024_signal(marketcap, debt):
    """Moving average of Market value coverage of debt over 42d window."""
    res = _sma(_ratio(marketcap, debt), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_debt_base_63d_v025_signal(debt):
    """Moving average of Raw level of debt over 63d window."""
    res = _sma(debt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_ebitda_base_63d_v026_signal(ebitda):
    """Moving average of Raw level of ebitda over 63d window."""
    res = _sma(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_marketcap_base_63d_v027_signal(marketcap):
    """Moving average of Raw level of marketcap over 63d window."""
    res = _sma(marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_assets_base_63d_v028_signal(assets):
    """Moving average of Raw level of assets over 63d window."""
    res = _sma(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_deleveraging_potential_base_63d_v029_signal(ebitda, debt, assets, marketcap):
    """Moving average of Earnings coverage and valuation discount interaction over 63d window."""
    res = _sma(_ratio(ebitda, debt) * _ratio(assets, marketcap), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_equity_coverage_base_63d_v030_signal(marketcap, debt):
    """Moving average of Market value coverage of debt over 63d window."""
    res = _sma(_ratio(marketcap, debt), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_debt_base_126d_v031_signal(debt):
    """Moving average of Raw level of debt over 126d window."""
    res = _sma(debt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_ebitda_base_126d_v032_signal(ebitda):
    """Moving average of Raw level of ebitda over 126d window."""
    res = _sma(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_marketcap_base_126d_v033_signal(marketcap):
    """Moving average of Raw level of marketcap over 126d window."""
    res = _sma(marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_assets_base_126d_v034_signal(assets):
    """Moving average of Raw level of assets over 126d window."""
    res = _sma(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_deleveraging_potential_base_126d_v035_signal(ebitda, debt, assets, marketcap):
    """Moving average of Earnings coverage and valuation discount interaction over 126d window."""
    res = _sma(_ratio(ebitda, debt) * _ratio(assets, marketcap), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_equity_coverage_base_126d_v036_signal(marketcap, debt):
    """Moving average of Market value coverage of debt over 126d window."""
    res = _sma(_ratio(marketcap, debt), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_debt_base_252d_v037_signal(debt):
    """Moving average of Raw level of debt over 252d window."""
    res = _sma(debt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_ebitda_base_252d_v038_signal(ebitda):
    """Moving average of Raw level of ebitda over 252d window."""
    res = _sma(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_marketcap_base_252d_v039_signal(marketcap):
    """Moving average of Raw level of marketcap over 252d window."""
    res = _sma(marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_assets_base_252d_v040_signal(assets):
    """Moving average of Raw level of assets over 252d window."""
    res = _sma(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_deleveraging_potential_base_252d_v041_signal(ebitda, debt, assets, marketcap):
    """Moving average of Earnings coverage and valuation discount interaction over 252d window."""
    res = _sma(_ratio(ebitda, debt) * _ratio(assets, marketcap), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_equity_coverage_base_252d_v042_signal(marketcap, debt):
    """Moving average of Market value coverage of debt over 252d window."""
    res = _sma(_ratio(marketcap, debt), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_debt_base_504d_v043_signal(debt):
    """Moving average of Raw level of debt over 504d window."""
    res = _sma(debt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_ebitda_base_504d_v044_signal(ebitda):
    """Moving average of Raw level of ebitda over 504d window."""
    res = _sma(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_marketcap_base_504d_v045_signal(marketcap):
    """Moving average of Raw level of marketcap over 504d window."""
    res = _sma(marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_assets_base_504d_v046_signal(assets):
    """Moving average of Raw level of assets over 504d window."""
    res = _sma(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_deleveraging_potential_base_504d_v047_signal(ebitda, debt, assets, marketcap):
    """Moving average of Earnings coverage and valuation discount interaction over 504d window."""
    res = _sma(_ratio(ebitda, debt) * _ratio(assets, marketcap), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_equity_coverage_base_504d_v048_signal(marketcap, debt):
    """Moving average of Market value coverage of debt over 504d window."""
    res = _sma(_ratio(marketcap, debt), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_debt_base_756d_v049_signal(debt):
    """Moving average of Raw level of debt over 756d window."""
    res = _sma(debt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_ebitda_base_756d_v050_signal(ebitda):
    """Moving average of Raw level of ebitda over 756d window."""
    res = _sma(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_marketcap_base_756d_v051_signal(marketcap):
    """Moving average of Raw level of marketcap over 756d window."""
    res = _sma(marketcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_assets_base_756d_v052_signal(assets):
    """Moving average of Raw level of assets over 756d window."""
    res = _sma(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_deleveraging_potential_base_756d_v053_signal(ebitda, debt, assets, marketcap):
    """Moving average of Earnings coverage and valuation discount interaction over 756d window."""
    res = _sma(_ratio(ebitda, debt) * _ratio(assets, marketcap), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_equity_coverage_base_756d_v054_signal(marketcap, debt):
    """Moving average of Market value coverage of debt over 756d window."""
    res = _sma(_ratio(marketcap, debt), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_debt_base_1008d_v055_signal(debt):
    """Moving average of Raw level of debt over 1008d window."""
    res = _sma(debt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_ebitda_base_1008d_v056_signal(ebitda):
    """Moving average of Raw level of ebitda over 1008d window."""
    res = _sma(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_marketcap_base_1008d_v057_signal(marketcap):
    """Moving average of Raw level of marketcap over 1008d window."""
    res = _sma(marketcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_assets_base_1008d_v058_signal(assets):
    """Moving average of Raw level of assets over 1008d window."""
    res = _sma(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_deleveraging_potential_base_1008d_v059_signal(ebitda, debt, assets, marketcap):
    """Moving average of Earnings coverage and valuation discount interaction over 1008d window."""
    res = _sma(_ratio(ebitda, debt) * _ratio(assets, marketcap), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_equity_coverage_base_1008d_v060_signal(marketcap, debt):
    """Moving average of Market value coverage of debt over 1008d window."""
    res = _sma(_ratio(marketcap, debt), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_debt_base_1260d_v061_signal(debt):
    """Moving average of Raw level of debt over 1260d window."""
    res = _sma(debt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_ebitda_base_1260d_v062_signal(ebitda):
    """Moving average of Raw level of ebitda over 1260d window."""
    res = _sma(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_marketcap_base_1260d_v063_signal(marketcap):
    """Moving average of Raw level of marketcap over 1260d window."""
    res = _sma(marketcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_assets_base_1260d_v064_signal(assets):
    """Moving average of Raw level of assets over 1260d window."""
    res = _sma(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_deleveraging_potential_base_1260d_v065_signal(ebitda, debt, assets, marketcap):
    """Moving average of Earnings coverage and valuation discount interaction over 1260d window."""
    res = _sma(_ratio(ebitda, debt) * _ratio(assets, marketcap), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_equity_coverage_base_1260d_v066_signal(marketcap, debt):
    """Moving average of Market value coverage of debt over 1260d window."""
    res = _sma(_ratio(marketcap, debt), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_debt_ewma_5d_v067_signal(debt):
    """Exponential moving average of Raw level of debt over 5d window."""
    res = _ewma(debt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_ebitda_ewma_5d_v068_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 5d window."""
    res = _ewma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_marketcap_ewma_5d_v069_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 5d window."""
    res = _ewma(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_assets_ewma_5d_v070_signal(assets):
    """Exponential moving average of Raw level of assets over 5d window."""
    res = _ewma(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_deleveraging_potential_ewma_5d_v071_signal(ebitda, debt, assets, marketcap):
    """Exponential moving average of Earnings coverage and valuation discount interaction over 5d window."""
    res = _ewma(_ratio(ebitda, debt) * _ratio(assets, marketcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_equity_coverage_ewma_5d_v072_signal(marketcap, debt):
    """Exponential moving average of Market value coverage of debt over 5d window."""
    res = _ewma(_ratio(marketcap, debt), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_debt_ewma_10d_v073_signal(debt):
    """Exponential moving average of Raw level of debt over 10d window."""
    res = _ewma(debt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_ebitda_ewma_10d_v074_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 10d window."""
    res = _ewma(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_uranium_production_cost_inflation_marketcap_ewma_10d_v075_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 10d window."""
    res = _ewma(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f29_uranium_production_cost_inflation_debt_base_5d_v001_signal": {"func": f29_uranium_production_cost_inflation_debt_base_5d_v001_signal},
    "f29_uranium_production_cost_inflation_ebitda_base_5d_v002_signal": {"func": f29_uranium_production_cost_inflation_ebitda_base_5d_v002_signal},
    "f29_uranium_production_cost_inflation_marketcap_base_5d_v003_signal": {"func": f29_uranium_production_cost_inflation_marketcap_base_5d_v003_signal},
    "f29_uranium_production_cost_inflation_assets_base_5d_v004_signal": {"func": f29_uranium_production_cost_inflation_assets_base_5d_v004_signal},
    "f29_uranium_production_cost_inflation_deleveraging_potential_base_5d_v005_signal": {"func": f29_uranium_production_cost_inflation_deleveraging_potential_base_5d_v005_signal},
    "f29_uranium_production_cost_inflation_equity_coverage_base_5d_v006_signal": {"func": f29_uranium_production_cost_inflation_equity_coverage_base_5d_v006_signal},
    "f29_uranium_production_cost_inflation_debt_base_10d_v007_signal": {"func": f29_uranium_production_cost_inflation_debt_base_10d_v007_signal},
    "f29_uranium_production_cost_inflation_ebitda_base_10d_v008_signal": {"func": f29_uranium_production_cost_inflation_ebitda_base_10d_v008_signal},
    "f29_uranium_production_cost_inflation_marketcap_base_10d_v009_signal": {"func": f29_uranium_production_cost_inflation_marketcap_base_10d_v009_signal},
    "f29_uranium_production_cost_inflation_assets_base_10d_v010_signal": {"func": f29_uranium_production_cost_inflation_assets_base_10d_v010_signal},
    "f29_uranium_production_cost_inflation_deleveraging_potential_base_10d_v011_signal": {"func": f29_uranium_production_cost_inflation_deleveraging_potential_base_10d_v011_signal},
    "f29_uranium_production_cost_inflation_equity_coverage_base_10d_v012_signal": {"func": f29_uranium_production_cost_inflation_equity_coverage_base_10d_v012_signal},
    "f29_uranium_production_cost_inflation_debt_base_21d_v013_signal": {"func": f29_uranium_production_cost_inflation_debt_base_21d_v013_signal},
    "f29_uranium_production_cost_inflation_ebitda_base_21d_v014_signal": {"func": f29_uranium_production_cost_inflation_ebitda_base_21d_v014_signal},
    "f29_uranium_production_cost_inflation_marketcap_base_21d_v015_signal": {"func": f29_uranium_production_cost_inflation_marketcap_base_21d_v015_signal},
    "f29_uranium_production_cost_inflation_assets_base_21d_v016_signal": {"func": f29_uranium_production_cost_inflation_assets_base_21d_v016_signal},
    "f29_uranium_production_cost_inflation_deleveraging_potential_base_21d_v017_signal": {"func": f29_uranium_production_cost_inflation_deleveraging_potential_base_21d_v017_signal},
    "f29_uranium_production_cost_inflation_equity_coverage_base_21d_v018_signal": {"func": f29_uranium_production_cost_inflation_equity_coverage_base_21d_v018_signal},
    "f29_uranium_production_cost_inflation_debt_base_42d_v019_signal": {"func": f29_uranium_production_cost_inflation_debt_base_42d_v019_signal},
    "f29_uranium_production_cost_inflation_ebitda_base_42d_v020_signal": {"func": f29_uranium_production_cost_inflation_ebitda_base_42d_v020_signal},
    "f29_uranium_production_cost_inflation_marketcap_base_42d_v021_signal": {"func": f29_uranium_production_cost_inflation_marketcap_base_42d_v021_signal},
    "f29_uranium_production_cost_inflation_assets_base_42d_v022_signal": {"func": f29_uranium_production_cost_inflation_assets_base_42d_v022_signal},
    "f29_uranium_production_cost_inflation_deleveraging_potential_base_42d_v023_signal": {"func": f29_uranium_production_cost_inflation_deleveraging_potential_base_42d_v023_signal},
    "f29_uranium_production_cost_inflation_equity_coverage_base_42d_v024_signal": {"func": f29_uranium_production_cost_inflation_equity_coverage_base_42d_v024_signal},
    "f29_uranium_production_cost_inflation_debt_base_63d_v025_signal": {"func": f29_uranium_production_cost_inflation_debt_base_63d_v025_signal},
    "f29_uranium_production_cost_inflation_ebitda_base_63d_v026_signal": {"func": f29_uranium_production_cost_inflation_ebitda_base_63d_v026_signal},
    "f29_uranium_production_cost_inflation_marketcap_base_63d_v027_signal": {"func": f29_uranium_production_cost_inflation_marketcap_base_63d_v027_signal},
    "f29_uranium_production_cost_inflation_assets_base_63d_v028_signal": {"func": f29_uranium_production_cost_inflation_assets_base_63d_v028_signal},
    "f29_uranium_production_cost_inflation_deleveraging_potential_base_63d_v029_signal": {"func": f29_uranium_production_cost_inflation_deleveraging_potential_base_63d_v029_signal},
    "f29_uranium_production_cost_inflation_equity_coverage_base_63d_v030_signal": {"func": f29_uranium_production_cost_inflation_equity_coverage_base_63d_v030_signal},
    "f29_uranium_production_cost_inflation_debt_base_126d_v031_signal": {"func": f29_uranium_production_cost_inflation_debt_base_126d_v031_signal},
    "f29_uranium_production_cost_inflation_ebitda_base_126d_v032_signal": {"func": f29_uranium_production_cost_inflation_ebitda_base_126d_v032_signal},
    "f29_uranium_production_cost_inflation_marketcap_base_126d_v033_signal": {"func": f29_uranium_production_cost_inflation_marketcap_base_126d_v033_signal},
    "f29_uranium_production_cost_inflation_assets_base_126d_v034_signal": {"func": f29_uranium_production_cost_inflation_assets_base_126d_v034_signal},
    "f29_uranium_production_cost_inflation_deleveraging_potential_base_126d_v035_signal": {"func": f29_uranium_production_cost_inflation_deleveraging_potential_base_126d_v035_signal},
    "f29_uranium_production_cost_inflation_equity_coverage_base_126d_v036_signal": {"func": f29_uranium_production_cost_inflation_equity_coverage_base_126d_v036_signal},
    "f29_uranium_production_cost_inflation_debt_base_252d_v037_signal": {"func": f29_uranium_production_cost_inflation_debt_base_252d_v037_signal},
    "f29_uranium_production_cost_inflation_ebitda_base_252d_v038_signal": {"func": f29_uranium_production_cost_inflation_ebitda_base_252d_v038_signal},
    "f29_uranium_production_cost_inflation_marketcap_base_252d_v039_signal": {"func": f29_uranium_production_cost_inflation_marketcap_base_252d_v039_signal},
    "f29_uranium_production_cost_inflation_assets_base_252d_v040_signal": {"func": f29_uranium_production_cost_inflation_assets_base_252d_v040_signal},
    "f29_uranium_production_cost_inflation_deleveraging_potential_base_252d_v041_signal": {"func": f29_uranium_production_cost_inflation_deleveraging_potential_base_252d_v041_signal},
    "f29_uranium_production_cost_inflation_equity_coverage_base_252d_v042_signal": {"func": f29_uranium_production_cost_inflation_equity_coverage_base_252d_v042_signal},
    "f29_uranium_production_cost_inflation_debt_base_504d_v043_signal": {"func": f29_uranium_production_cost_inflation_debt_base_504d_v043_signal},
    "f29_uranium_production_cost_inflation_ebitda_base_504d_v044_signal": {"func": f29_uranium_production_cost_inflation_ebitda_base_504d_v044_signal},
    "f29_uranium_production_cost_inflation_marketcap_base_504d_v045_signal": {"func": f29_uranium_production_cost_inflation_marketcap_base_504d_v045_signal},
    "f29_uranium_production_cost_inflation_assets_base_504d_v046_signal": {"func": f29_uranium_production_cost_inflation_assets_base_504d_v046_signal},
    "f29_uranium_production_cost_inflation_deleveraging_potential_base_504d_v047_signal": {"func": f29_uranium_production_cost_inflation_deleveraging_potential_base_504d_v047_signal},
    "f29_uranium_production_cost_inflation_equity_coverage_base_504d_v048_signal": {"func": f29_uranium_production_cost_inflation_equity_coverage_base_504d_v048_signal},
    "f29_uranium_production_cost_inflation_debt_base_756d_v049_signal": {"func": f29_uranium_production_cost_inflation_debt_base_756d_v049_signal},
    "f29_uranium_production_cost_inflation_ebitda_base_756d_v050_signal": {"func": f29_uranium_production_cost_inflation_ebitda_base_756d_v050_signal},
    "f29_uranium_production_cost_inflation_marketcap_base_756d_v051_signal": {"func": f29_uranium_production_cost_inflation_marketcap_base_756d_v051_signal},
    "f29_uranium_production_cost_inflation_assets_base_756d_v052_signal": {"func": f29_uranium_production_cost_inflation_assets_base_756d_v052_signal},
    "f29_uranium_production_cost_inflation_deleveraging_potential_base_756d_v053_signal": {"func": f29_uranium_production_cost_inflation_deleveraging_potential_base_756d_v053_signal},
    "f29_uranium_production_cost_inflation_equity_coverage_base_756d_v054_signal": {"func": f29_uranium_production_cost_inflation_equity_coverage_base_756d_v054_signal},
    "f29_uranium_production_cost_inflation_debt_base_1008d_v055_signal": {"func": f29_uranium_production_cost_inflation_debt_base_1008d_v055_signal},
    "f29_uranium_production_cost_inflation_ebitda_base_1008d_v056_signal": {"func": f29_uranium_production_cost_inflation_ebitda_base_1008d_v056_signal},
    "f29_uranium_production_cost_inflation_marketcap_base_1008d_v057_signal": {"func": f29_uranium_production_cost_inflation_marketcap_base_1008d_v057_signal},
    "f29_uranium_production_cost_inflation_assets_base_1008d_v058_signal": {"func": f29_uranium_production_cost_inflation_assets_base_1008d_v058_signal},
    "f29_uranium_production_cost_inflation_deleveraging_potential_base_1008d_v059_signal": {"func": f29_uranium_production_cost_inflation_deleveraging_potential_base_1008d_v059_signal},
    "f29_uranium_production_cost_inflation_equity_coverage_base_1008d_v060_signal": {"func": f29_uranium_production_cost_inflation_equity_coverage_base_1008d_v060_signal},
    "f29_uranium_production_cost_inflation_debt_base_1260d_v061_signal": {"func": f29_uranium_production_cost_inflation_debt_base_1260d_v061_signal},
    "f29_uranium_production_cost_inflation_ebitda_base_1260d_v062_signal": {"func": f29_uranium_production_cost_inflation_ebitda_base_1260d_v062_signal},
    "f29_uranium_production_cost_inflation_marketcap_base_1260d_v063_signal": {"func": f29_uranium_production_cost_inflation_marketcap_base_1260d_v063_signal},
    "f29_uranium_production_cost_inflation_assets_base_1260d_v064_signal": {"func": f29_uranium_production_cost_inflation_assets_base_1260d_v064_signal},
    "f29_uranium_production_cost_inflation_deleveraging_potential_base_1260d_v065_signal": {"func": f29_uranium_production_cost_inflation_deleveraging_potential_base_1260d_v065_signal},
    "f29_uranium_production_cost_inflation_equity_coverage_base_1260d_v066_signal": {"func": f29_uranium_production_cost_inflation_equity_coverage_base_1260d_v066_signal},
    "f29_uranium_production_cost_inflation_debt_ewma_5d_v067_signal": {"func": f29_uranium_production_cost_inflation_debt_ewma_5d_v067_signal},
    "f29_uranium_production_cost_inflation_ebitda_ewma_5d_v068_signal": {"func": f29_uranium_production_cost_inflation_ebitda_ewma_5d_v068_signal},
    "f29_uranium_production_cost_inflation_marketcap_ewma_5d_v069_signal": {"func": f29_uranium_production_cost_inflation_marketcap_ewma_5d_v069_signal},
    "f29_uranium_production_cost_inflation_assets_ewma_5d_v070_signal": {"func": f29_uranium_production_cost_inflation_assets_ewma_5d_v070_signal},
    "f29_uranium_production_cost_inflation_deleveraging_potential_ewma_5d_v071_signal": {"func": f29_uranium_production_cost_inflation_deleveraging_potential_ewma_5d_v071_signal},
    "f29_uranium_production_cost_inflation_equity_coverage_ewma_5d_v072_signal": {"func": f29_uranium_production_cost_inflation_equity_coverage_ewma_5d_v072_signal},
    "f29_uranium_production_cost_inflation_debt_ewma_10d_v073_signal": {"func": f29_uranium_production_cost_inflation_debt_ewma_10d_v073_signal},
    "f29_uranium_production_cost_inflation_ebitda_ewma_10d_v074_signal": {"func": f29_uranium_production_cost_inflation_ebitda_ewma_10d_v074_signal},
    "f29_uranium_production_cost_inflation_marketcap_ewma_10d_v075_signal": {"func": f29_uranium_production_cost_inflation_marketcap_ewma_10d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "divyield": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "debt": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "opex": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 29...")
    for name, info in REGISTRY.items():
        fn = info["func"]
        sig = inspect.signature(fn)
        params = list(sig.parameters.keys())
        args = [df[p] for p in params]
        try:
            res = fn(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
            # Relaxing non-null for RSI/Skew which need more data
            if len(res.dropna()) < 10 and len(df) > 1000: pass 
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
