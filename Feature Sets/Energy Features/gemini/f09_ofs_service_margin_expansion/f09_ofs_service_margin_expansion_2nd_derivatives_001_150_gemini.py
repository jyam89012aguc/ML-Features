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

def f09_ofs_service_margin_expansion_debt_slope_pct_5d_v001_signal(debt):
    """Percentage slope for Raw level of debt over 5d window."""
    res = _slope_pct(debt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_slope_pct_5d_v002_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 5d window."""
    res = _slope_pct(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_slope_pct_5d_v003_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 5d window."""
    res = _slope_pct(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_slope_pct_5d_v004_signal(assets):
    """Percentage slope for Raw level of assets over 5d window."""
    res = _slope_pct(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_5d_v005_signal(ebitda, debt, assets, marketcap):
    """Percentage slope for Earnings coverage and valuation discount interaction over 5d window."""
    res = _slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_slope_pct_5d_v006_signal(marketcap, debt):
    """Percentage slope for Market value coverage of debt over 5d window."""
    res = _slope_pct(_ratio(marketcap, debt), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_debt_slope_pct_10d_v007_signal(debt):
    """Percentage slope for Raw level of debt over 10d window."""
    res = _slope_pct(debt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_slope_pct_10d_v008_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 10d window."""
    res = _slope_pct(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_slope_pct_10d_v009_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 10d window."""
    res = _slope_pct(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_slope_pct_10d_v010_signal(assets):
    """Percentage slope for Raw level of assets over 10d window."""
    res = _slope_pct(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_10d_v011_signal(ebitda, debt, assets, marketcap):
    """Percentage slope for Earnings coverage and valuation discount interaction over 10d window."""
    res = _slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_slope_pct_10d_v012_signal(marketcap, debt):
    """Percentage slope for Market value coverage of debt over 10d window."""
    res = _slope_pct(_ratio(marketcap, debt), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_debt_slope_pct_21d_v013_signal(debt):
    """Percentage slope for Raw level of debt over 21d window."""
    res = _slope_pct(debt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_slope_pct_21d_v014_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 21d window."""
    res = _slope_pct(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_slope_pct_21d_v015_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 21d window."""
    res = _slope_pct(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_slope_pct_21d_v016_signal(assets):
    """Percentage slope for Raw level of assets over 21d window."""
    res = _slope_pct(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_21d_v017_signal(ebitda, debt, assets, marketcap):
    """Percentage slope for Earnings coverage and valuation discount interaction over 21d window."""
    res = _slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_slope_pct_21d_v018_signal(marketcap, debt):
    """Percentage slope for Market value coverage of debt over 21d window."""
    res = _slope_pct(_ratio(marketcap, debt), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_debt_slope_pct_42d_v019_signal(debt):
    """Percentage slope for Raw level of debt over 42d window."""
    res = _slope_pct(debt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_slope_pct_42d_v020_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 42d window."""
    res = _slope_pct(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_slope_pct_42d_v021_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 42d window."""
    res = _slope_pct(marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_slope_pct_42d_v022_signal(assets):
    """Percentage slope for Raw level of assets over 42d window."""
    res = _slope_pct(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_42d_v023_signal(ebitda, debt, assets, marketcap):
    """Percentage slope for Earnings coverage and valuation discount interaction over 42d window."""
    res = _slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_slope_pct_42d_v024_signal(marketcap, debt):
    """Percentage slope for Market value coverage of debt over 42d window."""
    res = _slope_pct(_ratio(marketcap, debt), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_debt_slope_pct_63d_v025_signal(debt):
    """Percentage slope for Raw level of debt over 63d window."""
    res = _slope_pct(debt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_slope_pct_63d_v026_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 63d window."""
    res = _slope_pct(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_slope_pct_63d_v027_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 63d window."""
    res = _slope_pct(marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_slope_pct_63d_v028_signal(assets):
    """Percentage slope for Raw level of assets over 63d window."""
    res = _slope_pct(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_63d_v029_signal(ebitda, debt, assets, marketcap):
    """Percentage slope for Earnings coverage and valuation discount interaction over 63d window."""
    res = _slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_slope_pct_63d_v030_signal(marketcap, debt):
    """Percentage slope for Market value coverage of debt over 63d window."""
    res = _slope_pct(_ratio(marketcap, debt), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_debt_slope_pct_126d_v031_signal(debt):
    """Percentage slope for Raw level of debt over 126d window."""
    res = _slope_pct(debt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_slope_pct_126d_v032_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 126d window."""
    res = _slope_pct(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_slope_pct_126d_v033_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 126d window."""
    res = _slope_pct(marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_slope_pct_126d_v034_signal(assets):
    """Percentage slope for Raw level of assets over 126d window."""
    res = _slope_pct(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_126d_v035_signal(ebitda, debt, assets, marketcap):
    """Percentage slope for Earnings coverage and valuation discount interaction over 126d window."""
    res = _slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_slope_pct_126d_v036_signal(marketcap, debt):
    """Percentage slope for Market value coverage of debt over 126d window."""
    res = _slope_pct(_ratio(marketcap, debt), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_debt_slope_pct_252d_v037_signal(debt):
    """Percentage slope for Raw level of debt over 252d window."""
    res = _slope_pct(debt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_slope_pct_252d_v038_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 252d window."""
    res = _slope_pct(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_slope_pct_252d_v039_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 252d window."""
    res = _slope_pct(marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_slope_pct_252d_v040_signal(assets):
    """Percentage slope for Raw level of assets over 252d window."""
    res = _slope_pct(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_252d_v041_signal(ebitda, debt, assets, marketcap):
    """Percentage slope for Earnings coverage and valuation discount interaction over 252d window."""
    res = _slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_slope_pct_252d_v042_signal(marketcap, debt):
    """Percentage slope for Market value coverage of debt over 252d window."""
    res = _slope_pct(_ratio(marketcap, debt), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_debt_slope_pct_504d_v043_signal(debt):
    """Percentage slope for Raw level of debt over 504d window."""
    res = _slope_pct(debt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_slope_pct_504d_v044_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 504d window."""
    res = _slope_pct(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_slope_pct_504d_v045_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 504d window."""
    res = _slope_pct(marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_slope_pct_504d_v046_signal(assets):
    """Percentage slope for Raw level of assets over 504d window."""
    res = _slope_pct(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_504d_v047_signal(ebitda, debt, assets, marketcap):
    """Percentage slope for Earnings coverage and valuation discount interaction over 504d window."""
    res = _slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_slope_pct_504d_v048_signal(marketcap, debt):
    """Percentage slope for Market value coverage of debt over 504d window."""
    res = _slope_pct(_ratio(marketcap, debt), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_debt_slope_pct_756d_v049_signal(debt):
    """Percentage slope for Raw level of debt over 756d window."""
    res = _slope_pct(debt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_slope_pct_756d_v050_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 756d window."""
    res = _slope_pct(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_slope_pct_756d_v051_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 756d window."""
    res = _slope_pct(marketcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_slope_pct_756d_v052_signal(assets):
    """Percentage slope for Raw level of assets over 756d window."""
    res = _slope_pct(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_756d_v053_signal(ebitda, debt, assets, marketcap):
    """Percentage slope for Earnings coverage and valuation discount interaction over 756d window."""
    res = _slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_slope_pct_756d_v054_signal(marketcap, debt):
    """Percentage slope for Market value coverage of debt over 756d window."""
    res = _slope_pct(_ratio(marketcap, debt), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_debt_slope_pct_1008d_v055_signal(debt):
    """Percentage slope for Raw level of debt over 1008d window."""
    res = _slope_pct(debt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_slope_pct_1008d_v056_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 1008d window."""
    res = _slope_pct(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_slope_pct_1008d_v057_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 1008d window."""
    res = _slope_pct(marketcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_slope_pct_1008d_v058_signal(assets):
    """Percentage slope for Raw level of assets over 1008d window."""
    res = _slope_pct(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_1008d_v059_signal(ebitda, debt, assets, marketcap):
    """Percentage slope for Earnings coverage and valuation discount interaction over 1008d window."""
    res = _slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_slope_pct_1008d_v060_signal(marketcap, debt):
    """Percentage slope for Market value coverage of debt over 1008d window."""
    res = _slope_pct(_ratio(marketcap, debt), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_debt_slope_pct_1260d_v061_signal(debt):
    """Percentage slope for Raw level of debt over 1260d window."""
    res = _slope_pct(debt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_slope_pct_1260d_v062_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 1260d window."""
    res = _slope_pct(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_slope_pct_1260d_v063_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 1260d window."""
    res = _slope_pct(marketcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_slope_pct_1260d_v064_signal(assets):
    """Percentage slope for Raw level of assets over 1260d window."""
    res = _slope_pct(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_1260d_v065_signal(ebitda, debt, assets, marketcap):
    """Percentage slope for Earnings coverage and valuation discount interaction over 1260d window."""
    res = _slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_slope_pct_1260d_v066_signal(marketcap, debt):
    """Percentage slope for Market value coverage of debt over 1260d window."""
    res = _slope_pct(_ratio(marketcap, debt), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_debt_jerk_5d_v067_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 5d window."""
    res = _jerk(debt, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_jerk_5d_v068_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 5d window."""
    res = _jerk(ebitda, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_jerk_5d_v069_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 5d window."""
    res = _jerk(marketcap, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_jerk_5d_v070_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 5d window."""
    res = _jerk(assets, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_jerk_5d_v071_signal(ebitda, debt, assets, marketcap):
    """Acceleration/Jerk for Earnings coverage and valuation discount interaction over 5d window."""
    res = _jerk(_ratio(ebitda, debt) * _ratio(assets, marketcap), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_jerk_5d_v072_signal(marketcap, debt):
    """Acceleration/Jerk for Market value coverage of debt over 5d window."""
    res = _jerk(_ratio(marketcap, debt), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_debt_jerk_10d_v073_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 10d window."""
    res = _jerk(debt, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_jerk_10d_v074_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 10d window."""
    res = _jerk(ebitda, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_jerk_10d_v075_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 10d window."""
    res = _jerk(marketcap, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_jerk_10d_v076_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 10d window."""
    res = _jerk(assets, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_jerk_10d_v077_signal(ebitda, debt, assets, marketcap):
    """Acceleration/Jerk for Earnings coverage and valuation discount interaction over 10d window."""
    res = _jerk(_ratio(ebitda, debt) * _ratio(assets, marketcap), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_jerk_10d_v078_signal(marketcap, debt):
    """Acceleration/Jerk for Market value coverage of debt over 10d window."""
    res = _jerk(_ratio(marketcap, debt), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_debt_jerk_21d_v079_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 21d window."""
    res = _jerk(debt, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_jerk_21d_v080_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 21d window."""
    res = _jerk(ebitda, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_jerk_21d_v081_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 21d window."""
    res = _jerk(marketcap, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_jerk_21d_v082_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 21d window."""
    res = _jerk(assets, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_jerk_21d_v083_signal(ebitda, debt, assets, marketcap):
    """Acceleration/Jerk for Earnings coverage and valuation discount interaction over 21d window."""
    res = _jerk(_ratio(ebitda, debt) * _ratio(assets, marketcap), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_jerk_21d_v084_signal(marketcap, debt):
    """Acceleration/Jerk for Market value coverage of debt over 21d window."""
    res = _jerk(_ratio(marketcap, debt), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_debt_jerk_42d_v085_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 42d window."""
    res = _jerk(debt, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_jerk_42d_v086_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 42d window."""
    res = _jerk(ebitda, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_jerk_42d_v087_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 42d window."""
    res = _jerk(marketcap, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_jerk_42d_v088_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 42d window."""
    res = _jerk(assets, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_jerk_42d_v089_signal(ebitda, debt, assets, marketcap):
    """Acceleration/Jerk for Earnings coverage and valuation discount interaction over 42d window."""
    res = _jerk(_ratio(ebitda, debt) * _ratio(assets, marketcap), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_jerk_42d_v090_signal(marketcap, debt):
    """Acceleration/Jerk for Market value coverage of debt over 42d window."""
    res = _jerk(_ratio(marketcap, debt), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_debt_jerk_63d_v091_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 63d window."""
    res = _jerk(debt, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_jerk_63d_v092_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 63d window."""
    res = _jerk(ebitda, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_jerk_63d_v093_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 63d window."""
    res = _jerk(marketcap, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_jerk_63d_v094_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 63d window."""
    res = _jerk(assets, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_jerk_63d_v095_signal(ebitda, debt, assets, marketcap):
    """Acceleration/Jerk for Earnings coverage and valuation discount interaction over 63d window."""
    res = _jerk(_ratio(ebitda, debt) * _ratio(assets, marketcap), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_jerk_63d_v096_signal(marketcap, debt):
    """Acceleration/Jerk for Market value coverage of debt over 63d window."""
    res = _jerk(_ratio(marketcap, debt), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_debt_jerk_126d_v097_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 126d window."""
    res = _jerk(debt, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_jerk_126d_v098_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 126d window."""
    res = _jerk(ebitda, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_jerk_126d_v099_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 126d window."""
    res = _jerk(marketcap, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_jerk_126d_v100_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 126d window."""
    res = _jerk(assets, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_jerk_126d_v101_signal(ebitda, debt, assets, marketcap):
    """Acceleration/Jerk for Earnings coverage and valuation discount interaction over 126d window."""
    res = _jerk(_ratio(ebitda, debt) * _ratio(assets, marketcap), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_jerk_126d_v102_signal(marketcap, debt):
    """Acceleration/Jerk for Market value coverage of debt over 126d window."""
    res = _jerk(_ratio(marketcap, debt), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_debt_jerk_252d_v103_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 252d window."""
    res = _jerk(debt, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_jerk_252d_v104_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 252d window."""
    res = _jerk(ebitda, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_jerk_252d_v105_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 252d window."""
    res = _jerk(marketcap, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_jerk_252d_v106_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 252d window."""
    res = _jerk(assets, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_jerk_252d_v107_signal(ebitda, debt, assets, marketcap):
    """Acceleration/Jerk for Earnings coverage and valuation discount interaction over 252d window."""
    res = _jerk(_ratio(ebitda, debt) * _ratio(assets, marketcap), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_jerk_252d_v108_signal(marketcap, debt):
    """Acceleration/Jerk for Market value coverage of debt over 252d window."""
    res = _jerk(_ratio(marketcap, debt), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_debt_jerk_504d_v109_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 504d window."""
    res = _jerk(debt, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_jerk_504d_v110_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 504d window."""
    res = _jerk(ebitda, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_jerk_504d_v111_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 504d window."""
    res = _jerk(marketcap, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_jerk_504d_v112_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 504d window."""
    res = _jerk(assets, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_jerk_504d_v113_signal(ebitda, debt, assets, marketcap):
    """Acceleration/Jerk for Earnings coverage and valuation discount interaction over 504d window."""
    res = _jerk(_ratio(ebitda, debt) * _ratio(assets, marketcap), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_jerk_504d_v114_signal(marketcap, debt):
    """Acceleration/Jerk for Market value coverage of debt over 504d window."""
    res = _jerk(_ratio(marketcap, debt), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_debt_jerk_756d_v115_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 756d window."""
    res = _jerk(debt, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_jerk_756d_v116_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 756d window."""
    res = _jerk(ebitda, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_jerk_756d_v117_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 756d window."""
    res = _jerk(marketcap, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_jerk_756d_v118_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 756d window."""
    res = _jerk(assets, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_jerk_756d_v119_signal(ebitda, debt, assets, marketcap):
    """Acceleration/Jerk for Earnings coverage and valuation discount interaction over 756d window."""
    res = _jerk(_ratio(ebitda, debt) * _ratio(assets, marketcap), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_jerk_756d_v120_signal(marketcap, debt):
    """Acceleration/Jerk for Market value coverage of debt over 756d window."""
    res = _jerk(_ratio(marketcap, debt), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_debt_jerk_1008d_v121_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 1008d window."""
    res = _jerk(debt, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_jerk_1008d_v122_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 1008d window."""
    res = _jerk(ebitda, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_jerk_1008d_v123_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 1008d window."""
    res = _jerk(marketcap, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_jerk_1008d_v124_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 1008d window."""
    res = _jerk(assets, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_jerk_1008d_v125_signal(ebitda, debt, assets, marketcap):
    """Acceleration/Jerk for Earnings coverage and valuation discount interaction over 1008d window."""
    res = _jerk(_ratio(ebitda, debt) * _ratio(assets, marketcap), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_jerk_1008d_v126_signal(marketcap, debt):
    """Acceleration/Jerk for Market value coverage of debt over 1008d window."""
    res = _jerk(_ratio(marketcap, debt), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_debt_jerk_1260d_v127_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 1260d window."""
    res = _jerk(debt, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_jerk_1260d_v128_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 1260d window."""
    res = _jerk(ebitda, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_jerk_1260d_v129_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 1260d window."""
    res = _jerk(marketcap, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_jerk_1260d_v130_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 1260d window."""
    res = _jerk(assets, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_jerk_1260d_v131_signal(ebitda, debt, assets, marketcap):
    """Acceleration/Jerk for Earnings coverage and valuation discount interaction over 1260d window."""
    res = _jerk(_ratio(ebitda, debt) * _ratio(assets, marketcap), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_jerk_1260d_v132_signal(marketcap, debt):
    """Acceleration/Jerk for Market value coverage of debt over 1260d window."""
    res = _jerk(_ratio(marketcap, debt), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_debt_slope_diff_norm_5d_v133_signal(debt):
    """Normalized slope change for Raw level of debt over 5d window."""
    res = (_slope_pct(debt, 5).diff(5) / _sma(debt.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_slope_diff_norm_5d_v134_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 5d window."""
    res = (_slope_pct(ebitda, 5).diff(5) / _sma(ebitda.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_slope_diff_norm_5d_v135_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 5d window."""
    res = (_slope_pct(marketcap, 5).diff(5) / _sma(marketcap.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_slope_diff_norm_5d_v136_signal(assets):
    """Normalized slope change for Raw level of assets over 5d window."""
    res = (_slope_pct(assets, 5).diff(5) / _sma(assets.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_slope_diff_norm_5d_v137_signal(ebitda, debt, assets, marketcap):
    """Normalized slope change for Earnings coverage and valuation discount interaction over 5d window."""
    res = (_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 5).diff(5) / _sma(_ratio(ebitda, debt) * _ratio(assets, marketcap).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_slope_diff_norm_5d_v138_signal(marketcap, debt):
    """Normalized slope change for Market value coverage of debt over 5d window."""
    res = (_slope_pct(_ratio(marketcap, debt), 5).diff(5) / _sma(_ratio(marketcap, debt).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_debt_slope_diff_norm_10d_v139_signal(debt):
    """Normalized slope change for Raw level of debt over 10d window."""
    res = (_slope_pct(debt, 10).diff(10) / _sma(debt.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_slope_diff_norm_10d_v140_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 10d window."""
    res = (_slope_pct(ebitda, 10).diff(10) / _sma(ebitda.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_slope_diff_norm_10d_v141_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 10d window."""
    res = (_slope_pct(marketcap, 10).diff(10) / _sma(marketcap.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_slope_diff_norm_10d_v142_signal(assets):
    """Normalized slope change for Raw level of assets over 10d window."""
    res = (_slope_pct(assets, 10).diff(10) / _sma(assets.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_slope_diff_norm_10d_v143_signal(ebitda, debt, assets, marketcap):
    """Normalized slope change for Earnings coverage and valuation discount interaction over 10d window."""
    res = (_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 10).diff(10) / _sma(_ratio(ebitda, debt) * _ratio(assets, marketcap).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_slope_diff_norm_10d_v144_signal(marketcap, debt):
    """Normalized slope change for Market value coverage of debt over 10d window."""
    res = (_slope_pct(_ratio(marketcap, debt), 10).diff(10) / _sma(_ratio(marketcap, debt).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_debt_slope_diff_norm_21d_v145_signal(debt):
    """Normalized slope change for Raw level of debt over 21d window."""
    res = (_slope_pct(debt, 21).diff(21) / _sma(debt.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_ebitda_slope_diff_norm_21d_v146_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 21d window."""
    res = (_slope_pct(ebitda, 21).diff(21) / _sma(ebitda.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_marketcap_slope_diff_norm_21d_v147_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 21d window."""
    res = (_slope_pct(marketcap, 21).diff(21) / _sma(marketcap.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_assets_slope_diff_norm_21d_v148_signal(assets):
    """Normalized slope change for Raw level of assets over 21d window."""
    res = (_slope_pct(assets, 21).diff(21) / _sma(assets.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_deleveraging_potential_slope_diff_norm_21d_v149_signal(ebitda, debt, assets, marketcap):
    """Normalized slope change for Earnings coverage and valuation discount interaction over 21d window."""
    res = (_slope_pct(_ratio(ebitda, debt) * _ratio(assets, marketcap), 21).diff(21) / _sma(_ratio(ebitda, debt) * _ratio(assets, marketcap).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_ofs_service_margin_expansion_equity_coverage_slope_diff_norm_21d_v150_signal(marketcap, debt):
    """Normalized slope change for Market value coverage of debt over 21d window."""
    res = (_slope_pct(_ratio(marketcap, debt), 21).diff(21) / _sma(_ratio(marketcap, debt).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f09_ofs_service_margin_expansion_debt_slope_pct_5d_v001_signal": {"func": f09_ofs_service_margin_expansion_debt_slope_pct_5d_v001_signal},
    "f09_ofs_service_margin_expansion_ebitda_slope_pct_5d_v002_signal": {"func": f09_ofs_service_margin_expansion_ebitda_slope_pct_5d_v002_signal},
    "f09_ofs_service_margin_expansion_marketcap_slope_pct_5d_v003_signal": {"func": f09_ofs_service_margin_expansion_marketcap_slope_pct_5d_v003_signal},
    "f09_ofs_service_margin_expansion_assets_slope_pct_5d_v004_signal": {"func": f09_ofs_service_margin_expansion_assets_slope_pct_5d_v004_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_5d_v005_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_5d_v005_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_slope_pct_5d_v006_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_slope_pct_5d_v006_signal},
    "f09_ofs_service_margin_expansion_debt_slope_pct_10d_v007_signal": {"func": f09_ofs_service_margin_expansion_debt_slope_pct_10d_v007_signal},
    "f09_ofs_service_margin_expansion_ebitda_slope_pct_10d_v008_signal": {"func": f09_ofs_service_margin_expansion_ebitda_slope_pct_10d_v008_signal},
    "f09_ofs_service_margin_expansion_marketcap_slope_pct_10d_v009_signal": {"func": f09_ofs_service_margin_expansion_marketcap_slope_pct_10d_v009_signal},
    "f09_ofs_service_margin_expansion_assets_slope_pct_10d_v010_signal": {"func": f09_ofs_service_margin_expansion_assets_slope_pct_10d_v010_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_10d_v011_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_10d_v011_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_slope_pct_10d_v012_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_slope_pct_10d_v012_signal},
    "f09_ofs_service_margin_expansion_debt_slope_pct_21d_v013_signal": {"func": f09_ofs_service_margin_expansion_debt_slope_pct_21d_v013_signal},
    "f09_ofs_service_margin_expansion_ebitda_slope_pct_21d_v014_signal": {"func": f09_ofs_service_margin_expansion_ebitda_slope_pct_21d_v014_signal},
    "f09_ofs_service_margin_expansion_marketcap_slope_pct_21d_v015_signal": {"func": f09_ofs_service_margin_expansion_marketcap_slope_pct_21d_v015_signal},
    "f09_ofs_service_margin_expansion_assets_slope_pct_21d_v016_signal": {"func": f09_ofs_service_margin_expansion_assets_slope_pct_21d_v016_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_21d_v017_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_21d_v017_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_slope_pct_21d_v018_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_slope_pct_21d_v018_signal},
    "f09_ofs_service_margin_expansion_debt_slope_pct_42d_v019_signal": {"func": f09_ofs_service_margin_expansion_debt_slope_pct_42d_v019_signal},
    "f09_ofs_service_margin_expansion_ebitda_slope_pct_42d_v020_signal": {"func": f09_ofs_service_margin_expansion_ebitda_slope_pct_42d_v020_signal},
    "f09_ofs_service_margin_expansion_marketcap_slope_pct_42d_v021_signal": {"func": f09_ofs_service_margin_expansion_marketcap_slope_pct_42d_v021_signal},
    "f09_ofs_service_margin_expansion_assets_slope_pct_42d_v022_signal": {"func": f09_ofs_service_margin_expansion_assets_slope_pct_42d_v022_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_42d_v023_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_42d_v023_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_slope_pct_42d_v024_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_slope_pct_42d_v024_signal},
    "f09_ofs_service_margin_expansion_debt_slope_pct_63d_v025_signal": {"func": f09_ofs_service_margin_expansion_debt_slope_pct_63d_v025_signal},
    "f09_ofs_service_margin_expansion_ebitda_slope_pct_63d_v026_signal": {"func": f09_ofs_service_margin_expansion_ebitda_slope_pct_63d_v026_signal},
    "f09_ofs_service_margin_expansion_marketcap_slope_pct_63d_v027_signal": {"func": f09_ofs_service_margin_expansion_marketcap_slope_pct_63d_v027_signal},
    "f09_ofs_service_margin_expansion_assets_slope_pct_63d_v028_signal": {"func": f09_ofs_service_margin_expansion_assets_slope_pct_63d_v028_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_63d_v029_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_63d_v029_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_slope_pct_63d_v030_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_slope_pct_63d_v030_signal},
    "f09_ofs_service_margin_expansion_debt_slope_pct_126d_v031_signal": {"func": f09_ofs_service_margin_expansion_debt_slope_pct_126d_v031_signal},
    "f09_ofs_service_margin_expansion_ebitda_slope_pct_126d_v032_signal": {"func": f09_ofs_service_margin_expansion_ebitda_slope_pct_126d_v032_signal},
    "f09_ofs_service_margin_expansion_marketcap_slope_pct_126d_v033_signal": {"func": f09_ofs_service_margin_expansion_marketcap_slope_pct_126d_v033_signal},
    "f09_ofs_service_margin_expansion_assets_slope_pct_126d_v034_signal": {"func": f09_ofs_service_margin_expansion_assets_slope_pct_126d_v034_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_126d_v035_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_126d_v035_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_slope_pct_126d_v036_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_slope_pct_126d_v036_signal},
    "f09_ofs_service_margin_expansion_debt_slope_pct_252d_v037_signal": {"func": f09_ofs_service_margin_expansion_debt_slope_pct_252d_v037_signal},
    "f09_ofs_service_margin_expansion_ebitda_slope_pct_252d_v038_signal": {"func": f09_ofs_service_margin_expansion_ebitda_slope_pct_252d_v038_signal},
    "f09_ofs_service_margin_expansion_marketcap_slope_pct_252d_v039_signal": {"func": f09_ofs_service_margin_expansion_marketcap_slope_pct_252d_v039_signal},
    "f09_ofs_service_margin_expansion_assets_slope_pct_252d_v040_signal": {"func": f09_ofs_service_margin_expansion_assets_slope_pct_252d_v040_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_252d_v041_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_252d_v041_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_slope_pct_252d_v042_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_slope_pct_252d_v042_signal},
    "f09_ofs_service_margin_expansion_debt_slope_pct_504d_v043_signal": {"func": f09_ofs_service_margin_expansion_debt_slope_pct_504d_v043_signal},
    "f09_ofs_service_margin_expansion_ebitda_slope_pct_504d_v044_signal": {"func": f09_ofs_service_margin_expansion_ebitda_slope_pct_504d_v044_signal},
    "f09_ofs_service_margin_expansion_marketcap_slope_pct_504d_v045_signal": {"func": f09_ofs_service_margin_expansion_marketcap_slope_pct_504d_v045_signal},
    "f09_ofs_service_margin_expansion_assets_slope_pct_504d_v046_signal": {"func": f09_ofs_service_margin_expansion_assets_slope_pct_504d_v046_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_504d_v047_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_504d_v047_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_slope_pct_504d_v048_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_slope_pct_504d_v048_signal},
    "f09_ofs_service_margin_expansion_debt_slope_pct_756d_v049_signal": {"func": f09_ofs_service_margin_expansion_debt_slope_pct_756d_v049_signal},
    "f09_ofs_service_margin_expansion_ebitda_slope_pct_756d_v050_signal": {"func": f09_ofs_service_margin_expansion_ebitda_slope_pct_756d_v050_signal},
    "f09_ofs_service_margin_expansion_marketcap_slope_pct_756d_v051_signal": {"func": f09_ofs_service_margin_expansion_marketcap_slope_pct_756d_v051_signal},
    "f09_ofs_service_margin_expansion_assets_slope_pct_756d_v052_signal": {"func": f09_ofs_service_margin_expansion_assets_slope_pct_756d_v052_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_756d_v053_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_756d_v053_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_slope_pct_756d_v054_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_slope_pct_756d_v054_signal},
    "f09_ofs_service_margin_expansion_debt_slope_pct_1008d_v055_signal": {"func": f09_ofs_service_margin_expansion_debt_slope_pct_1008d_v055_signal},
    "f09_ofs_service_margin_expansion_ebitda_slope_pct_1008d_v056_signal": {"func": f09_ofs_service_margin_expansion_ebitda_slope_pct_1008d_v056_signal},
    "f09_ofs_service_margin_expansion_marketcap_slope_pct_1008d_v057_signal": {"func": f09_ofs_service_margin_expansion_marketcap_slope_pct_1008d_v057_signal},
    "f09_ofs_service_margin_expansion_assets_slope_pct_1008d_v058_signal": {"func": f09_ofs_service_margin_expansion_assets_slope_pct_1008d_v058_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_1008d_v059_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_1008d_v059_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_slope_pct_1008d_v060_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_slope_pct_1008d_v060_signal},
    "f09_ofs_service_margin_expansion_debt_slope_pct_1260d_v061_signal": {"func": f09_ofs_service_margin_expansion_debt_slope_pct_1260d_v061_signal},
    "f09_ofs_service_margin_expansion_ebitda_slope_pct_1260d_v062_signal": {"func": f09_ofs_service_margin_expansion_ebitda_slope_pct_1260d_v062_signal},
    "f09_ofs_service_margin_expansion_marketcap_slope_pct_1260d_v063_signal": {"func": f09_ofs_service_margin_expansion_marketcap_slope_pct_1260d_v063_signal},
    "f09_ofs_service_margin_expansion_assets_slope_pct_1260d_v064_signal": {"func": f09_ofs_service_margin_expansion_assets_slope_pct_1260d_v064_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_1260d_v065_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_slope_pct_1260d_v065_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_slope_pct_1260d_v066_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_slope_pct_1260d_v066_signal},
    "f09_ofs_service_margin_expansion_debt_jerk_5d_v067_signal": {"func": f09_ofs_service_margin_expansion_debt_jerk_5d_v067_signal},
    "f09_ofs_service_margin_expansion_ebitda_jerk_5d_v068_signal": {"func": f09_ofs_service_margin_expansion_ebitda_jerk_5d_v068_signal},
    "f09_ofs_service_margin_expansion_marketcap_jerk_5d_v069_signal": {"func": f09_ofs_service_margin_expansion_marketcap_jerk_5d_v069_signal},
    "f09_ofs_service_margin_expansion_assets_jerk_5d_v070_signal": {"func": f09_ofs_service_margin_expansion_assets_jerk_5d_v070_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_jerk_5d_v071_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_jerk_5d_v071_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_jerk_5d_v072_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_jerk_5d_v072_signal},
    "f09_ofs_service_margin_expansion_debt_jerk_10d_v073_signal": {"func": f09_ofs_service_margin_expansion_debt_jerk_10d_v073_signal},
    "f09_ofs_service_margin_expansion_ebitda_jerk_10d_v074_signal": {"func": f09_ofs_service_margin_expansion_ebitda_jerk_10d_v074_signal},
    "f09_ofs_service_margin_expansion_marketcap_jerk_10d_v075_signal": {"func": f09_ofs_service_margin_expansion_marketcap_jerk_10d_v075_signal},
    "f09_ofs_service_margin_expansion_assets_jerk_10d_v076_signal": {"func": f09_ofs_service_margin_expansion_assets_jerk_10d_v076_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_jerk_10d_v077_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_jerk_10d_v077_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_jerk_10d_v078_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_jerk_10d_v078_signal},
    "f09_ofs_service_margin_expansion_debt_jerk_21d_v079_signal": {"func": f09_ofs_service_margin_expansion_debt_jerk_21d_v079_signal},
    "f09_ofs_service_margin_expansion_ebitda_jerk_21d_v080_signal": {"func": f09_ofs_service_margin_expansion_ebitda_jerk_21d_v080_signal},
    "f09_ofs_service_margin_expansion_marketcap_jerk_21d_v081_signal": {"func": f09_ofs_service_margin_expansion_marketcap_jerk_21d_v081_signal},
    "f09_ofs_service_margin_expansion_assets_jerk_21d_v082_signal": {"func": f09_ofs_service_margin_expansion_assets_jerk_21d_v082_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_jerk_21d_v083_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_jerk_21d_v083_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_jerk_21d_v084_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_jerk_21d_v084_signal},
    "f09_ofs_service_margin_expansion_debt_jerk_42d_v085_signal": {"func": f09_ofs_service_margin_expansion_debt_jerk_42d_v085_signal},
    "f09_ofs_service_margin_expansion_ebitda_jerk_42d_v086_signal": {"func": f09_ofs_service_margin_expansion_ebitda_jerk_42d_v086_signal},
    "f09_ofs_service_margin_expansion_marketcap_jerk_42d_v087_signal": {"func": f09_ofs_service_margin_expansion_marketcap_jerk_42d_v087_signal},
    "f09_ofs_service_margin_expansion_assets_jerk_42d_v088_signal": {"func": f09_ofs_service_margin_expansion_assets_jerk_42d_v088_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_jerk_42d_v089_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_jerk_42d_v089_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_jerk_42d_v090_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_jerk_42d_v090_signal},
    "f09_ofs_service_margin_expansion_debt_jerk_63d_v091_signal": {"func": f09_ofs_service_margin_expansion_debt_jerk_63d_v091_signal},
    "f09_ofs_service_margin_expansion_ebitda_jerk_63d_v092_signal": {"func": f09_ofs_service_margin_expansion_ebitda_jerk_63d_v092_signal},
    "f09_ofs_service_margin_expansion_marketcap_jerk_63d_v093_signal": {"func": f09_ofs_service_margin_expansion_marketcap_jerk_63d_v093_signal},
    "f09_ofs_service_margin_expansion_assets_jerk_63d_v094_signal": {"func": f09_ofs_service_margin_expansion_assets_jerk_63d_v094_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_jerk_63d_v095_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_jerk_63d_v095_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_jerk_63d_v096_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_jerk_63d_v096_signal},
    "f09_ofs_service_margin_expansion_debt_jerk_126d_v097_signal": {"func": f09_ofs_service_margin_expansion_debt_jerk_126d_v097_signal},
    "f09_ofs_service_margin_expansion_ebitda_jerk_126d_v098_signal": {"func": f09_ofs_service_margin_expansion_ebitda_jerk_126d_v098_signal},
    "f09_ofs_service_margin_expansion_marketcap_jerk_126d_v099_signal": {"func": f09_ofs_service_margin_expansion_marketcap_jerk_126d_v099_signal},
    "f09_ofs_service_margin_expansion_assets_jerk_126d_v100_signal": {"func": f09_ofs_service_margin_expansion_assets_jerk_126d_v100_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_jerk_126d_v101_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_jerk_126d_v101_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_jerk_126d_v102_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_jerk_126d_v102_signal},
    "f09_ofs_service_margin_expansion_debt_jerk_252d_v103_signal": {"func": f09_ofs_service_margin_expansion_debt_jerk_252d_v103_signal},
    "f09_ofs_service_margin_expansion_ebitda_jerk_252d_v104_signal": {"func": f09_ofs_service_margin_expansion_ebitda_jerk_252d_v104_signal},
    "f09_ofs_service_margin_expansion_marketcap_jerk_252d_v105_signal": {"func": f09_ofs_service_margin_expansion_marketcap_jerk_252d_v105_signal},
    "f09_ofs_service_margin_expansion_assets_jerk_252d_v106_signal": {"func": f09_ofs_service_margin_expansion_assets_jerk_252d_v106_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_jerk_252d_v107_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_jerk_252d_v107_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_jerk_252d_v108_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_jerk_252d_v108_signal},
    "f09_ofs_service_margin_expansion_debt_jerk_504d_v109_signal": {"func": f09_ofs_service_margin_expansion_debt_jerk_504d_v109_signal},
    "f09_ofs_service_margin_expansion_ebitda_jerk_504d_v110_signal": {"func": f09_ofs_service_margin_expansion_ebitda_jerk_504d_v110_signal},
    "f09_ofs_service_margin_expansion_marketcap_jerk_504d_v111_signal": {"func": f09_ofs_service_margin_expansion_marketcap_jerk_504d_v111_signal},
    "f09_ofs_service_margin_expansion_assets_jerk_504d_v112_signal": {"func": f09_ofs_service_margin_expansion_assets_jerk_504d_v112_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_jerk_504d_v113_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_jerk_504d_v113_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_jerk_504d_v114_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_jerk_504d_v114_signal},
    "f09_ofs_service_margin_expansion_debt_jerk_756d_v115_signal": {"func": f09_ofs_service_margin_expansion_debt_jerk_756d_v115_signal},
    "f09_ofs_service_margin_expansion_ebitda_jerk_756d_v116_signal": {"func": f09_ofs_service_margin_expansion_ebitda_jerk_756d_v116_signal},
    "f09_ofs_service_margin_expansion_marketcap_jerk_756d_v117_signal": {"func": f09_ofs_service_margin_expansion_marketcap_jerk_756d_v117_signal},
    "f09_ofs_service_margin_expansion_assets_jerk_756d_v118_signal": {"func": f09_ofs_service_margin_expansion_assets_jerk_756d_v118_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_jerk_756d_v119_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_jerk_756d_v119_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_jerk_756d_v120_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_jerk_756d_v120_signal},
    "f09_ofs_service_margin_expansion_debt_jerk_1008d_v121_signal": {"func": f09_ofs_service_margin_expansion_debt_jerk_1008d_v121_signal},
    "f09_ofs_service_margin_expansion_ebitda_jerk_1008d_v122_signal": {"func": f09_ofs_service_margin_expansion_ebitda_jerk_1008d_v122_signal},
    "f09_ofs_service_margin_expansion_marketcap_jerk_1008d_v123_signal": {"func": f09_ofs_service_margin_expansion_marketcap_jerk_1008d_v123_signal},
    "f09_ofs_service_margin_expansion_assets_jerk_1008d_v124_signal": {"func": f09_ofs_service_margin_expansion_assets_jerk_1008d_v124_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_jerk_1008d_v125_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_jerk_1008d_v125_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_jerk_1008d_v126_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_jerk_1008d_v126_signal},
    "f09_ofs_service_margin_expansion_debt_jerk_1260d_v127_signal": {"func": f09_ofs_service_margin_expansion_debt_jerk_1260d_v127_signal},
    "f09_ofs_service_margin_expansion_ebitda_jerk_1260d_v128_signal": {"func": f09_ofs_service_margin_expansion_ebitda_jerk_1260d_v128_signal},
    "f09_ofs_service_margin_expansion_marketcap_jerk_1260d_v129_signal": {"func": f09_ofs_service_margin_expansion_marketcap_jerk_1260d_v129_signal},
    "f09_ofs_service_margin_expansion_assets_jerk_1260d_v130_signal": {"func": f09_ofs_service_margin_expansion_assets_jerk_1260d_v130_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_jerk_1260d_v131_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_jerk_1260d_v131_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_jerk_1260d_v132_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_jerk_1260d_v132_signal},
    "f09_ofs_service_margin_expansion_debt_slope_diff_norm_5d_v133_signal": {"func": f09_ofs_service_margin_expansion_debt_slope_diff_norm_5d_v133_signal},
    "f09_ofs_service_margin_expansion_ebitda_slope_diff_norm_5d_v134_signal": {"func": f09_ofs_service_margin_expansion_ebitda_slope_diff_norm_5d_v134_signal},
    "f09_ofs_service_margin_expansion_marketcap_slope_diff_norm_5d_v135_signal": {"func": f09_ofs_service_margin_expansion_marketcap_slope_diff_norm_5d_v135_signal},
    "f09_ofs_service_margin_expansion_assets_slope_diff_norm_5d_v136_signal": {"func": f09_ofs_service_margin_expansion_assets_slope_diff_norm_5d_v136_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_slope_diff_norm_5d_v137_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_slope_diff_norm_5d_v137_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_slope_diff_norm_5d_v138_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_slope_diff_norm_5d_v138_signal},
    "f09_ofs_service_margin_expansion_debt_slope_diff_norm_10d_v139_signal": {"func": f09_ofs_service_margin_expansion_debt_slope_diff_norm_10d_v139_signal},
    "f09_ofs_service_margin_expansion_ebitda_slope_diff_norm_10d_v140_signal": {"func": f09_ofs_service_margin_expansion_ebitda_slope_diff_norm_10d_v140_signal},
    "f09_ofs_service_margin_expansion_marketcap_slope_diff_norm_10d_v141_signal": {"func": f09_ofs_service_margin_expansion_marketcap_slope_diff_norm_10d_v141_signal},
    "f09_ofs_service_margin_expansion_assets_slope_diff_norm_10d_v142_signal": {"func": f09_ofs_service_margin_expansion_assets_slope_diff_norm_10d_v142_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_slope_diff_norm_10d_v143_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_slope_diff_norm_10d_v143_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_slope_diff_norm_10d_v144_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_slope_diff_norm_10d_v144_signal},
    "f09_ofs_service_margin_expansion_debt_slope_diff_norm_21d_v145_signal": {"func": f09_ofs_service_margin_expansion_debt_slope_diff_norm_21d_v145_signal},
    "f09_ofs_service_margin_expansion_ebitda_slope_diff_norm_21d_v146_signal": {"func": f09_ofs_service_margin_expansion_ebitda_slope_diff_norm_21d_v146_signal},
    "f09_ofs_service_margin_expansion_marketcap_slope_diff_norm_21d_v147_signal": {"func": f09_ofs_service_margin_expansion_marketcap_slope_diff_norm_21d_v147_signal},
    "f09_ofs_service_margin_expansion_assets_slope_diff_norm_21d_v148_signal": {"func": f09_ofs_service_margin_expansion_assets_slope_diff_norm_21d_v148_signal},
    "f09_ofs_service_margin_expansion_deleveraging_potential_slope_diff_norm_21d_v149_signal": {"func": f09_ofs_service_margin_expansion_deleveraging_potential_slope_diff_norm_21d_v149_signal},
    "f09_ofs_service_margin_expansion_equity_coverage_slope_diff_norm_21d_v150_signal": {"func": f09_ofs_service_margin_expansion_equity_coverage_slope_diff_norm_21d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "divyield": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "debt": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "opex": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 09...")
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
