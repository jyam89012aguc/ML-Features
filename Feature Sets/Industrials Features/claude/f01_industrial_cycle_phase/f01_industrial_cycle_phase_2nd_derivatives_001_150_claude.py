import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)

# ===== folder domain primitives =====
def _f01_cycle_earnings_strength(netinc, revenue, w):
    margin = netinc / revenue.replace(0, np.nan).abs()
    return margin.rolling(w, min_periods=max(1, w // 2)).mean()


def _f01_price_breadth(closeadj, w):
    above = (closeadj > closeadj.rolling(w, min_periods=max(1, w // 2)).mean()).astype(float)
    return above.rolling(w, min_periods=max(1, w // 2)).mean()


def _f01_asset_growth_signature(assets, w):
    return assets.pct_change(periods=w)

def f01icp_f01_industrial_cycle_phase_ces_5d_slope_v001_signal(netinc, revenue, closeadj):
    base = _f01_cycle_earnings_strength(netinc, revenue, 5)
    _b = base * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_ces_10d_slope_v002_signal(netinc, revenue, closeadj):
    base = _f01_cycle_earnings_strength(netinc, revenue, 10)
    _b = base * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_ces_21d_slope_v003_signal(netinc, revenue, closeadj):
    base = _f01_cycle_earnings_strength(netinc, revenue, 21)
    _b = base * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_ces_42d_slope_v004_signal(netinc, revenue, closeadj):
    base = _f01_cycle_earnings_strength(netinc, revenue, 42)
    _b = base * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_ces_63d_slope_v005_signal(netinc, revenue, closeadj):
    base = _f01_cycle_earnings_strength(netinc, revenue, 63)
    _b = base * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_ces_126d_slope_v006_signal(netinc, revenue, closeadj):
    base = _f01_cycle_earnings_strength(netinc, revenue, 126)
    _b = base * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_ces_189d_slope_v007_signal(netinc, revenue, closeadj):
    base = _f01_cycle_earnings_strength(netinc, revenue, 189)
    _b = base * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_ces_252d_slope_v008_signal(netinc, revenue, closeadj):
    base = _f01_cycle_earnings_strength(netinc, revenue, 252)
    _b = base * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbr_5d_slope_v009_signal(closeadj):
    base = _f01_price_breadth(closeadj, 5)
    _b = base * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbr_10d_slope_v010_signal(closeadj):
    base = _f01_price_breadth(closeadj, 10)
    _b = base * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbr_21d_slope_v011_signal(closeadj):
    base = _f01_price_breadth(closeadj, 21)
    _b = base * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbr_42d_slope_v012_signal(closeadj):
    base = _f01_price_breadth(closeadj, 42)
    _b = base * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbr_63d_slope_v013_signal(closeadj):
    base = _f01_price_breadth(closeadj, 63)
    _b = base * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbr_126d_slope_v014_signal(closeadj):
    base = _f01_price_breadth(closeadj, 126)
    _b = base * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbr_189d_slope_v015_signal(closeadj):
    base = _f01_price_breadth(closeadj, 189)
    _b = base * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbr_252d_slope_v016_signal(closeadj):
    base = _f01_price_breadth(closeadj, 252)
    _b = base * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agr_5d_slope_v017_signal(assets, closeadj):
    base = _f01_asset_growth_signature(assets, 5)
    _b = base * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agr_10d_slope_v018_signal(assets, closeadj):
    base = _f01_asset_growth_signature(assets, 10)
    _b = base * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agr_21d_slope_v019_signal(assets, closeadj):
    base = _f01_asset_growth_signature(assets, 21)
    _b = base * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agr_42d_slope_v020_signal(assets, closeadj):
    base = _f01_asset_growth_signature(assets, 42)
    _b = base * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agr_63d_slope_v021_signal(assets, closeadj):
    base = _f01_asset_growth_signature(assets, 63)
    _b = base * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agr_126d_slope_v022_signal(assets, closeadj):
    base = _f01_asset_growth_signature(assets, 126)
    _b = base * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agr_189d_slope_v023_signal(assets, closeadj):
    base = _f01_asset_growth_signature(assets, 189)
    _b = base * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agr_252d_slope_v024_signal(assets, closeadj):
    base = _f01_asset_growth_signature(assets, 252)
    _b = base * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxpbr_5d_slope_v025_signal(netinc, revenue, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 5)
    b = _f01_price_breadth(closeadj, 5)
    _b = a * b * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxpbr_10d_slope_v026_signal(netinc, revenue, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 10)
    b = _f01_price_breadth(closeadj, 10)
    _b = a * b * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxpbr_21d_slope_v027_signal(netinc, revenue, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 21)
    b = _f01_price_breadth(closeadj, 21)
    _b = a * b * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxpbr_42d_slope_v028_signal(netinc, revenue, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 42)
    b = _f01_price_breadth(closeadj, 42)
    _b = a * b * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxpbr_63d_slope_v029_signal(netinc, revenue, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 63)
    b = _f01_price_breadth(closeadj, 63)
    _b = a * b * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxpbr_126d_slope_v030_signal(netinc, revenue, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 126)
    b = _f01_price_breadth(closeadj, 126)
    _b = a * b * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxpbr_189d_slope_v031_signal(netinc, revenue, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 189)
    b = _f01_price_breadth(closeadj, 189)
    _b = a * b * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxpbr_252d_slope_v032_signal(netinc, revenue, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 252)
    b = _f01_price_breadth(closeadj, 252)
    _b = a * b * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxagr_5d_slope_v033_signal(netinc, revenue, assets, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 5)
    b = _f01_asset_growth_signature(assets, 5)
    _b = a * b * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxagr_10d_slope_v034_signal(netinc, revenue, assets, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 10)
    b = _f01_asset_growth_signature(assets, 10)
    _b = a * b * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxagr_21d_slope_v035_signal(netinc, revenue, assets, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 21)
    b = _f01_asset_growth_signature(assets, 21)
    _b = a * b * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxagr_42d_slope_v036_signal(netinc, revenue, assets, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 42)
    b = _f01_asset_growth_signature(assets, 42)
    _b = a * b * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxagr_63d_slope_v037_signal(netinc, revenue, assets, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 63)
    b = _f01_asset_growth_signature(assets, 63)
    _b = a * b * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxagr_126d_slope_v038_signal(netinc, revenue, assets, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 126)
    b = _f01_asset_growth_signature(assets, 126)
    _b = a * b * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxagr_189d_slope_v039_signal(netinc, revenue, assets, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 189)
    b = _f01_asset_growth_signature(assets, 189)
    _b = a * b * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxagr_252d_slope_v040_signal(netinc, revenue, assets, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 252)
    b = _f01_asset_growth_signature(assets, 252)
    _b = a * b * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrxagr_5d_slope_v041_signal(closeadj, assets):
    a = _f01_price_breadth(closeadj, 5)
    b = _f01_asset_growth_signature(assets, 5)
    _b = a * b * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrxagr_10d_slope_v042_signal(closeadj, assets):
    a = _f01_price_breadth(closeadj, 10)
    b = _f01_asset_growth_signature(assets, 10)
    _b = a * b * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrxagr_21d_slope_v043_signal(closeadj, assets):
    a = _f01_price_breadth(closeadj, 21)
    b = _f01_asset_growth_signature(assets, 21)
    _b = a * b * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrxagr_42d_slope_v044_signal(closeadj, assets):
    a = _f01_price_breadth(closeadj, 42)
    b = _f01_asset_growth_signature(assets, 42)
    _b = a * b * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrxagr_63d_slope_v045_signal(closeadj, assets):
    a = _f01_price_breadth(closeadj, 63)
    b = _f01_asset_growth_signature(assets, 63)
    _b = a * b * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrxagr_126d_slope_v046_signal(closeadj, assets):
    a = _f01_price_breadth(closeadj, 126)
    b = _f01_asset_growth_signature(assets, 126)
    _b = a * b * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrxagr_189d_slope_v047_signal(closeadj, assets):
    a = _f01_price_breadth(closeadj, 189)
    b = _f01_asset_growth_signature(assets, 189)
    _b = a * b * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrxagr_252d_slope_v048_signal(closeadj, assets):
    a = _f01_price_breadth(closeadj, 252)
    b = _f01_asset_growth_signature(assets, 252)
    _b = a * b * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesebit_5d_slope_v049_signal(ebit, revenue, closeadj):
    base = _f01_cycle_earnings_strength(ebit, revenue, 5)
    _b = base * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesebit_10d_slope_v050_signal(ebit, revenue, closeadj):
    base = _f01_cycle_earnings_strength(ebit, revenue, 10)
    _b = base * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesebit_21d_slope_v051_signal(ebit, revenue, closeadj):
    base = _f01_cycle_earnings_strength(ebit, revenue, 21)
    _b = base * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesebit_42d_slope_v052_signal(ebit, revenue, closeadj):
    base = _f01_cycle_earnings_strength(ebit, revenue, 42)
    _b = base * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesebit_63d_slope_v053_signal(ebit, revenue, closeadj):
    base = _f01_cycle_earnings_strength(ebit, revenue, 63)
    _b = base * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesebit_126d_slope_v054_signal(ebit, revenue, closeadj):
    base = _f01_cycle_earnings_strength(ebit, revenue, 126)
    _b = base * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesebit_189d_slope_v055_signal(ebit, revenue, closeadj):
    base = _f01_cycle_earnings_strength(ebit, revenue, 189)
    _b = base * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesebit_252d_slope_v056_signal(ebit, revenue, closeadj):
    base = _f01_cycle_earnings_strength(ebit, revenue, 252)
    _b = base * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesebitda_5d_slope_v057_signal(ebitda, revenue, closeadj):
    base = _f01_cycle_earnings_strength(ebitda, revenue, 5)
    _b = base * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesebitda_10d_slope_v058_signal(ebitda, revenue, closeadj):
    base = _f01_cycle_earnings_strength(ebitda, revenue, 10)
    _b = base * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesebitda_21d_slope_v059_signal(ebitda, revenue, closeadj):
    base = _f01_cycle_earnings_strength(ebitda, revenue, 21)
    _b = base * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesebitda_42d_slope_v060_signal(ebitda, revenue, closeadj):
    base = _f01_cycle_earnings_strength(ebitda, revenue, 42)
    _b = base * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesebitda_63d_slope_v061_signal(ebitda, revenue, closeadj):
    base = _f01_cycle_earnings_strength(ebitda, revenue, 63)
    _b = base * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesebitda_126d_slope_v062_signal(ebitda, revenue, closeadj):
    base = _f01_cycle_earnings_strength(ebitda, revenue, 126)
    _b = base * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesebitda_189d_slope_v063_signal(ebitda, revenue, closeadj):
    base = _f01_cycle_earnings_strength(ebitda, revenue, 189)
    _b = base * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesebitda_252d_slope_v064_signal(ebitda, revenue, closeadj):
    base = _f01_cycle_earnings_strength(ebitda, revenue, 252)
    _b = base * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesz_21d_slope_v065_signal(netinc, revenue, closeadj):
    base = _f01_cycle_earnings_strength(netinc, revenue, 21)
    _b = _z(base, 42) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesz_63d_slope_v066_signal(netinc, revenue, closeadj):
    base = _f01_cycle_earnings_strength(netinc, revenue, 63)
    _b = _z(base, 126) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesz_126d_slope_v067_signal(netinc, revenue, closeadj):
    base = _f01_cycle_earnings_strength(netinc, revenue, 126)
    _b = _z(base, 252) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesz_252d_slope_v068_signal(netinc, revenue, closeadj):
    base = _f01_cycle_earnings_strength(netinc, revenue, 252)
    _b = _z(base, 504) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrz_21d_slope_v069_signal(closeadj):
    base = _f01_price_breadth(closeadj, 21)
    _b = _z(base, 42) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrz_63d_slope_v070_signal(closeadj):
    base = _f01_price_breadth(closeadj, 63)
    _b = _z(base, 126) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrz_126d_slope_v071_signal(closeadj):
    base = _f01_price_breadth(closeadj, 126)
    _b = _z(base, 252) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrz_252d_slope_v072_signal(closeadj):
    base = _f01_price_breadth(closeadj, 252)
    _b = _z(base, 504) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrz_21d_slope_v073_signal(assets, closeadj):
    base = _f01_asset_growth_signature(assets, 21)
    _b = _z(base, 42) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrz_63d_slope_v074_signal(assets, closeadj):
    base = _f01_asset_growth_signature(assets, 63)
    _b = _z(base, 126) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrz_126d_slope_v075_signal(assets, closeadj):
    base = _f01_asset_growth_signature(assets, 126)
    _b = _z(base, 252) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrz_252d_slope_v076_signal(assets, closeadj):
    base = _f01_asset_growth_signature(assets, 252)
    _b = _z(base, 504) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesmean_21d_slope_v077_signal(netinc, revenue, closeadj):
    base = _f01_cycle_earnings_strength(netinc, revenue, 21)
    _b = _mean(base, 21) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesmean_63d_slope_v078_signal(netinc, revenue, closeadj):
    base = _f01_cycle_earnings_strength(netinc, revenue, 63)
    _b = _mean(base, 63) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesmean_126d_slope_v079_signal(netinc, revenue, closeadj):
    base = _f01_cycle_earnings_strength(netinc, revenue, 126)
    _b = _mean(base, 126) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesmean_252d_slope_v080_signal(netinc, revenue, closeadj):
    base = _f01_cycle_earnings_strength(netinc, revenue, 252)
    _b = _mean(base, 252) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrmean_21d_slope_v081_signal(closeadj):
    base = _f01_price_breadth(closeadj, 21)
    _b = _mean(base, 21) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrmean_63d_slope_v082_signal(closeadj):
    base = _f01_price_breadth(closeadj, 63)
    _b = _mean(base, 63) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrmean_126d_slope_v083_signal(closeadj):
    base = _f01_price_breadth(closeadj, 126)
    _b = _mean(base, 126) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrmean_252d_slope_v084_signal(closeadj):
    base = _f01_price_breadth(closeadj, 252)
    _b = _mean(base, 252) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrmean_21d_slope_v085_signal(assets, closeadj):
    base = _f01_asset_growth_signature(assets, 21)
    _b = _mean(base, 21) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrmean_63d_slope_v086_signal(assets, closeadj):
    base = _f01_asset_growth_signature(assets, 63)
    _b = _mean(base, 63) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrmean_126d_slope_v087_signal(assets, closeadj):
    base = _f01_asset_growth_signature(assets, 126)
    _b = _mean(base, 126) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrmean_252d_slope_v088_signal(assets, closeadj):
    base = _f01_asset_growth_signature(assets, 252)
    _b = _mean(base, 252) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesstd_21d_slope_v089_signal(netinc, revenue, closeadj):
    base = _f01_cycle_earnings_strength(netinc, revenue, 21)
    _b = _std(base, 21) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesstd_63d_slope_v090_signal(netinc, revenue, closeadj):
    base = _f01_cycle_earnings_strength(netinc, revenue, 63)
    _b = _std(base, 63) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesstd_126d_slope_v091_signal(netinc, revenue, closeadj):
    base = _f01_cycle_earnings_strength(netinc, revenue, 126)
    _b = _std(base, 126) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesstd_252d_slope_v092_signal(netinc, revenue, closeadj):
    base = _f01_cycle_earnings_strength(netinc, revenue, 252)
    _b = _std(base, 252) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrstd_21d_slope_v093_signal(closeadj):
    base = _f01_price_breadth(closeadj, 21)
    _b = _std(base, 21) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrstd_63d_slope_v094_signal(closeadj):
    base = _f01_price_breadth(closeadj, 63)
    _b = _std(base, 63) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrstd_126d_slope_v095_signal(closeadj):
    base = _f01_price_breadth(closeadj, 126)
    _b = _std(base, 126) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrstd_252d_slope_v096_signal(closeadj):
    base = _f01_price_breadth(closeadj, 252)
    _b = _std(base, 252) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrstd_21d_slope_v097_signal(assets, closeadj):
    base = _f01_asset_growth_signature(assets, 21)
    _b = _std(base, 21) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrstd_63d_slope_v098_signal(assets, closeadj):
    base = _f01_asset_growth_signature(assets, 63)
    _b = _std(base, 63) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrstd_126d_slope_v099_signal(assets, closeadj):
    base = _f01_asset_growth_signature(assets, 126)
    _b = _std(base, 126) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrstd_252d_slope_v100_signal(assets, closeadj):
    base = _f01_asset_growth_signature(assets, 252)
    _b = _std(base, 252) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxcapex_21d_slope_v101_signal(netinc, revenue, capex, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 21)
    _b = a * (capex / 1e7) + _f01_price_breadth(closeadj, 21) * 0.0
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxcapex_63d_slope_v102_signal(netinc, revenue, capex, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 63)
    _b = a * (capex / 1e7) + _f01_price_breadth(closeadj, 63) * 0.0
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxcapex_126d_slope_v103_signal(netinc, revenue, capex, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 126)
    _b = a * (capex / 1e7) + _f01_price_breadth(closeadj, 126) * 0.0
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxcapex_252d_slope_v104_signal(netinc, revenue, capex, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 252)
    _b = a * (capex / 1e7) + _f01_price_breadth(closeadj, 252) * 0.0
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrxppne_21d_slope_v105_signal(closeadj, ppnenet):
    a = _f01_price_breadth(closeadj, 21)
    _b = a * (ppnenet / 1e8) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrxppne_63d_slope_v106_signal(closeadj, ppnenet):
    a = _f01_price_breadth(closeadj, 63)
    _b = a * (ppnenet / 1e8) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrxppne_126d_slope_v107_signal(closeadj, ppnenet):
    a = _f01_price_breadth(closeadj, 126)
    _b = a * (ppnenet / 1e8) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrxppne_252d_slope_v108_signal(closeadj, ppnenet):
    a = _f01_price_breadth(closeadj, 252)
    _b = a * (ppnenet / 1e8) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrxmcap_21d_slope_v109_signal(assets, marketcap, closeadj):
    a = _f01_asset_growth_signature(assets, 21)
    _b = a * (marketcap / 1e8) + _f01_price_breadth(closeadj, 21) * 0.0
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrxmcap_63d_slope_v110_signal(assets, marketcap, closeadj):
    a = _f01_asset_growth_signature(assets, 63)
    _b = a * (marketcap / 1e8) + _f01_price_breadth(closeadj, 63) * 0.0
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrxmcap_126d_slope_v111_signal(assets, marketcap, closeadj):
    a = _f01_asset_growth_signature(assets, 126)
    _b = a * (marketcap / 1e8) + _f01_price_breadth(closeadj, 126) * 0.0
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrxmcap_252d_slope_v112_signal(assets, marketcap, closeadj):
    a = _f01_asset_growth_signature(assets, 252)
    _b = a * (marketcap / 1e8) + _f01_price_breadth(closeadj, 252) * 0.0
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_compsig_21d_slope_v113_signal(netinc, revenue, assets, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 21)
    b = _f01_asset_growth_signature(assets, 21)
    c = _f01_price_breadth(closeadj, 21)
    _b = (a + b + c) * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_compsig_63d_slope_v114_signal(netinc, revenue, assets, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 63)
    b = _f01_asset_growth_signature(assets, 63)
    c = _f01_price_breadth(closeadj, 63)
    _b = (a + b + c) * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_compsig_126d_slope_v115_signal(netinc, revenue, assets, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 126)
    b = _f01_asset_growth_signature(assets, 126)
    c = _f01_price_breadth(closeadj, 126)
    _b = (a + b + c) * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_compsig_252d_slope_v116_signal(netinc, revenue, assets, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 252)
    b = _f01_asset_growth_signature(assets, 252)
    c = _f01_price_breadth(closeadj, 252)
    _b = (a + b + c) * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxret_21d_slope_v117_signal(netinc, revenue, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 21)
    ret = closeadj.pct_change(21)
    _b = a * ret * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxret_63d_slope_v118_signal(netinc, revenue, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 63)
    ret = closeadj.pct_change(63)
    _b = a * ret * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxret_126d_slope_v119_signal(netinc, revenue, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 126)
    ret = closeadj.pct_change(126)
    _b = a * ret * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrxvol_21d_slope_v120_signal(closeadj, volume):
    a = _f01_price_breadth(closeadj, 21)
    _b = a * _mean(closeadj * volume, 21)
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrxvol_63d_slope_v121_signal(closeadj, volume):
    a = _f01_price_breadth(closeadj, 63)
    _b = a * _mean(closeadj * volume, 63)
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrxvol_126d_slope_v122_signal(closeadj, volume):
    a = _f01_price_breadth(closeadj, 126)
    _b = a * _mean(closeadj * volume, 126)
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrxvol_21d_slope_v123_signal(assets, closeadj, volume):
    a = _f01_asset_growth_signature(assets, 21)
    _b = a * _mean(closeadj * volume, 21)
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrxvol_63d_slope_v124_signal(assets, closeadj, volume):
    a = _f01_asset_growth_signature(assets, 63)
    _b = a * _mean(closeadj * volume, 63)
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrxvol_126d_slope_v125_signal(assets, closeadj, volume):
    a = _f01_asset_growth_signature(assets, 126)
    _b = a * _mean(closeadj * volume, 126)
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxgm_21d_slope_v126_signal(netinc, revenue, grossmargin, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 21)
    _b = a * grossmargin * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxgm_63d_slope_v127_signal(netinc, revenue, grossmargin, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 63)
    _b = a * grossmargin * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxgm_126d_slope_v128_signal(netinc, revenue, grossmargin, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 126)
    _b = a * grossmargin * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxgm_252d_slope_v129_signal(netinc, revenue, grossmargin, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 252)
    _b = a * grossmargin * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrxgm_21d_slope_v130_signal(closeadj, grossmargin):
    a = _f01_price_breadth(closeadj, 21)
    _b = a * grossmargin * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrxgm_63d_slope_v131_signal(closeadj, grossmargin):
    a = _f01_price_breadth(closeadj, 63)
    _b = a * grossmargin * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrxgm_126d_slope_v132_signal(closeadj, grossmargin):
    a = _f01_price_breadth(closeadj, 126)
    _b = a * grossmargin * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrxgm_252d_slope_v133_signal(closeadj, grossmargin):
    a = _f01_price_breadth(closeadj, 252)
    _b = a * grossmargin * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrxgm_21d_slope_v134_signal(assets, grossmargin, closeadj):
    a = _f01_asset_growth_signature(assets, 21)
    _b = a * grossmargin * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrxgm_63d_slope_v135_signal(assets, grossmargin, closeadj):
    a = _f01_asset_growth_signature(assets, 63)
    _b = a * grossmargin * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrxgm_126d_slope_v136_signal(assets, grossmargin, closeadj):
    a = _f01_asset_growth_signature(assets, 126)
    _b = a * grossmargin * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrxgm_252d_slope_v137_signal(assets, grossmargin, closeadj):
    a = _f01_asset_growth_signature(assets, 252)
    _b = a * grossmargin * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesema_21d_slope_v138_signal(netinc, revenue, closeadj):
    base = _f01_cycle_earnings_strength(netinc, revenue, 21)
    _b = base.ewm(span=21, min_periods=10).mean() * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesema_63d_slope_v139_signal(netinc, revenue, closeadj):
    base = _f01_cycle_earnings_strength(netinc, revenue, 63)
    _b = base.ewm(span=63, min_periods=31).mean() * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesema_126d_slope_v140_signal(netinc, revenue, closeadj):
    base = _f01_cycle_earnings_strength(netinc, revenue, 126)
    _b = base.ewm(span=126, min_periods=63).mean() * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrema_21d_slope_v141_signal(closeadj):
    base = _f01_price_breadth(closeadj, 21)
    _b = base.ewm(span=21, min_periods=10).mean() * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrema_63d_slope_v142_signal(closeadj):
    base = _f01_price_breadth(closeadj, 63)
    _b = base.ewm(span=63, min_periods=31).mean() * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_pbrema_126d_slope_v143_signal(closeadj):
    base = _f01_price_breadth(closeadj, 126)
    _b = base.ewm(span=126, min_periods=63).mean() * closeadj
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrema_21d_slope_v144_signal(assets, closeadj):
    base = _f01_asset_growth_signature(assets, 21)
    _b = base.ewm(span=21, min_periods=10).mean() * closeadj
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrema_63d_slope_v145_signal(assets, closeadj):
    base = _f01_asset_growth_signature(assets, 63)
    _b = base.ewm(span=63, min_periods=31).mean() * closeadj
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_agrema_126d_slope_v146_signal(assets, closeadj):
    base = _f01_asset_growth_signature(assets, 126)
    _b = base.ewm(span=126, min_periods=63).mean() * closeadj
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxev_21d_slope_v147_signal(netinc, revenue, ev, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 21)
    _b = a * (ev / 1e8) + _f01_price_breadth(closeadj, 21) * 0.0
    result = _slope_pct(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxev_63d_slope_v148_signal(netinc, revenue, ev, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 63)
    _b = a * (ev / 1e8) + _f01_price_breadth(closeadj, 63) * 0.0
    result = _slope_diff_norm(_b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxev_126d_slope_v149_signal(netinc, revenue, ev, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 126)
    _b = a * (ev / 1e8) + _f01_price_breadth(closeadj, 126) * 0.0
    result = _slope_pct(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01icp_f01_industrial_cycle_phase_cesxev_252d_slope_v150_signal(netinc, revenue, ev, closeadj):
    a = _f01_cycle_earnings_strength(netinc, revenue, 252)
    _b = a * (ev / 1e8) + _f01_price_breadth(closeadj, 252) * 0.0
    result = _slope_diff_norm(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f01icp_f01_industrial_cycle_phase_ces_5d_slope_v001_signal,
    f01icp_f01_industrial_cycle_phase_ces_10d_slope_v002_signal,
    f01icp_f01_industrial_cycle_phase_ces_21d_slope_v003_signal,
    f01icp_f01_industrial_cycle_phase_ces_42d_slope_v004_signal,
    f01icp_f01_industrial_cycle_phase_ces_63d_slope_v005_signal,
    f01icp_f01_industrial_cycle_phase_ces_126d_slope_v006_signal,
    f01icp_f01_industrial_cycle_phase_ces_189d_slope_v007_signal,
    f01icp_f01_industrial_cycle_phase_ces_252d_slope_v008_signal,
    f01icp_f01_industrial_cycle_phase_pbr_5d_slope_v009_signal,
    f01icp_f01_industrial_cycle_phase_pbr_10d_slope_v010_signal,
    f01icp_f01_industrial_cycle_phase_pbr_21d_slope_v011_signal,
    f01icp_f01_industrial_cycle_phase_pbr_42d_slope_v012_signal,
    f01icp_f01_industrial_cycle_phase_pbr_63d_slope_v013_signal,
    f01icp_f01_industrial_cycle_phase_pbr_126d_slope_v014_signal,
    f01icp_f01_industrial_cycle_phase_pbr_189d_slope_v015_signal,
    f01icp_f01_industrial_cycle_phase_pbr_252d_slope_v016_signal,
    f01icp_f01_industrial_cycle_phase_agr_5d_slope_v017_signal,
    f01icp_f01_industrial_cycle_phase_agr_10d_slope_v018_signal,
    f01icp_f01_industrial_cycle_phase_agr_21d_slope_v019_signal,
    f01icp_f01_industrial_cycle_phase_agr_42d_slope_v020_signal,
    f01icp_f01_industrial_cycle_phase_agr_63d_slope_v021_signal,
    f01icp_f01_industrial_cycle_phase_agr_126d_slope_v022_signal,
    f01icp_f01_industrial_cycle_phase_agr_189d_slope_v023_signal,
    f01icp_f01_industrial_cycle_phase_agr_252d_slope_v024_signal,
    f01icp_f01_industrial_cycle_phase_cesxpbr_5d_slope_v025_signal,
    f01icp_f01_industrial_cycle_phase_cesxpbr_10d_slope_v026_signal,
    f01icp_f01_industrial_cycle_phase_cesxpbr_21d_slope_v027_signal,
    f01icp_f01_industrial_cycle_phase_cesxpbr_42d_slope_v028_signal,
    f01icp_f01_industrial_cycle_phase_cesxpbr_63d_slope_v029_signal,
    f01icp_f01_industrial_cycle_phase_cesxpbr_126d_slope_v030_signal,
    f01icp_f01_industrial_cycle_phase_cesxpbr_189d_slope_v031_signal,
    f01icp_f01_industrial_cycle_phase_cesxpbr_252d_slope_v032_signal,
    f01icp_f01_industrial_cycle_phase_cesxagr_5d_slope_v033_signal,
    f01icp_f01_industrial_cycle_phase_cesxagr_10d_slope_v034_signal,
    f01icp_f01_industrial_cycle_phase_cesxagr_21d_slope_v035_signal,
    f01icp_f01_industrial_cycle_phase_cesxagr_42d_slope_v036_signal,
    f01icp_f01_industrial_cycle_phase_cesxagr_63d_slope_v037_signal,
    f01icp_f01_industrial_cycle_phase_cesxagr_126d_slope_v038_signal,
    f01icp_f01_industrial_cycle_phase_cesxagr_189d_slope_v039_signal,
    f01icp_f01_industrial_cycle_phase_cesxagr_252d_slope_v040_signal,
    f01icp_f01_industrial_cycle_phase_pbrxagr_5d_slope_v041_signal,
    f01icp_f01_industrial_cycle_phase_pbrxagr_10d_slope_v042_signal,
    f01icp_f01_industrial_cycle_phase_pbrxagr_21d_slope_v043_signal,
    f01icp_f01_industrial_cycle_phase_pbrxagr_42d_slope_v044_signal,
    f01icp_f01_industrial_cycle_phase_pbrxagr_63d_slope_v045_signal,
    f01icp_f01_industrial_cycle_phase_pbrxagr_126d_slope_v046_signal,
    f01icp_f01_industrial_cycle_phase_pbrxagr_189d_slope_v047_signal,
    f01icp_f01_industrial_cycle_phase_pbrxagr_252d_slope_v048_signal,
    f01icp_f01_industrial_cycle_phase_cesebit_5d_slope_v049_signal,
    f01icp_f01_industrial_cycle_phase_cesebit_10d_slope_v050_signal,
    f01icp_f01_industrial_cycle_phase_cesebit_21d_slope_v051_signal,
    f01icp_f01_industrial_cycle_phase_cesebit_42d_slope_v052_signal,
    f01icp_f01_industrial_cycle_phase_cesebit_63d_slope_v053_signal,
    f01icp_f01_industrial_cycle_phase_cesebit_126d_slope_v054_signal,
    f01icp_f01_industrial_cycle_phase_cesebit_189d_slope_v055_signal,
    f01icp_f01_industrial_cycle_phase_cesebit_252d_slope_v056_signal,
    f01icp_f01_industrial_cycle_phase_cesebitda_5d_slope_v057_signal,
    f01icp_f01_industrial_cycle_phase_cesebitda_10d_slope_v058_signal,
    f01icp_f01_industrial_cycle_phase_cesebitda_21d_slope_v059_signal,
    f01icp_f01_industrial_cycle_phase_cesebitda_42d_slope_v060_signal,
    f01icp_f01_industrial_cycle_phase_cesebitda_63d_slope_v061_signal,
    f01icp_f01_industrial_cycle_phase_cesebitda_126d_slope_v062_signal,
    f01icp_f01_industrial_cycle_phase_cesebitda_189d_slope_v063_signal,
    f01icp_f01_industrial_cycle_phase_cesebitda_252d_slope_v064_signal,
    f01icp_f01_industrial_cycle_phase_cesz_21d_slope_v065_signal,
    f01icp_f01_industrial_cycle_phase_cesz_63d_slope_v066_signal,
    f01icp_f01_industrial_cycle_phase_cesz_126d_slope_v067_signal,
    f01icp_f01_industrial_cycle_phase_cesz_252d_slope_v068_signal,
    f01icp_f01_industrial_cycle_phase_pbrz_21d_slope_v069_signal,
    f01icp_f01_industrial_cycle_phase_pbrz_63d_slope_v070_signal,
    f01icp_f01_industrial_cycle_phase_pbrz_126d_slope_v071_signal,
    f01icp_f01_industrial_cycle_phase_pbrz_252d_slope_v072_signal,
    f01icp_f01_industrial_cycle_phase_agrz_21d_slope_v073_signal,
    f01icp_f01_industrial_cycle_phase_agrz_63d_slope_v074_signal,
    f01icp_f01_industrial_cycle_phase_agrz_126d_slope_v075_signal,
    f01icp_f01_industrial_cycle_phase_agrz_252d_slope_v076_signal,
    f01icp_f01_industrial_cycle_phase_cesmean_21d_slope_v077_signal,
    f01icp_f01_industrial_cycle_phase_cesmean_63d_slope_v078_signal,
    f01icp_f01_industrial_cycle_phase_cesmean_126d_slope_v079_signal,
    f01icp_f01_industrial_cycle_phase_cesmean_252d_slope_v080_signal,
    f01icp_f01_industrial_cycle_phase_pbrmean_21d_slope_v081_signal,
    f01icp_f01_industrial_cycle_phase_pbrmean_63d_slope_v082_signal,
    f01icp_f01_industrial_cycle_phase_pbrmean_126d_slope_v083_signal,
    f01icp_f01_industrial_cycle_phase_pbrmean_252d_slope_v084_signal,
    f01icp_f01_industrial_cycle_phase_agrmean_21d_slope_v085_signal,
    f01icp_f01_industrial_cycle_phase_agrmean_63d_slope_v086_signal,
    f01icp_f01_industrial_cycle_phase_agrmean_126d_slope_v087_signal,
    f01icp_f01_industrial_cycle_phase_agrmean_252d_slope_v088_signal,
    f01icp_f01_industrial_cycle_phase_cesstd_21d_slope_v089_signal,
    f01icp_f01_industrial_cycle_phase_cesstd_63d_slope_v090_signal,
    f01icp_f01_industrial_cycle_phase_cesstd_126d_slope_v091_signal,
    f01icp_f01_industrial_cycle_phase_cesstd_252d_slope_v092_signal,
    f01icp_f01_industrial_cycle_phase_pbrstd_21d_slope_v093_signal,
    f01icp_f01_industrial_cycle_phase_pbrstd_63d_slope_v094_signal,
    f01icp_f01_industrial_cycle_phase_pbrstd_126d_slope_v095_signal,
    f01icp_f01_industrial_cycle_phase_pbrstd_252d_slope_v096_signal,
    f01icp_f01_industrial_cycle_phase_agrstd_21d_slope_v097_signal,
    f01icp_f01_industrial_cycle_phase_agrstd_63d_slope_v098_signal,
    f01icp_f01_industrial_cycle_phase_agrstd_126d_slope_v099_signal,
    f01icp_f01_industrial_cycle_phase_agrstd_252d_slope_v100_signal,
    f01icp_f01_industrial_cycle_phase_cesxcapex_21d_slope_v101_signal,
    f01icp_f01_industrial_cycle_phase_cesxcapex_63d_slope_v102_signal,
    f01icp_f01_industrial_cycle_phase_cesxcapex_126d_slope_v103_signal,
    f01icp_f01_industrial_cycle_phase_cesxcapex_252d_slope_v104_signal,
    f01icp_f01_industrial_cycle_phase_pbrxppne_21d_slope_v105_signal,
    f01icp_f01_industrial_cycle_phase_pbrxppne_63d_slope_v106_signal,
    f01icp_f01_industrial_cycle_phase_pbrxppne_126d_slope_v107_signal,
    f01icp_f01_industrial_cycle_phase_pbrxppne_252d_slope_v108_signal,
    f01icp_f01_industrial_cycle_phase_agrxmcap_21d_slope_v109_signal,
    f01icp_f01_industrial_cycle_phase_agrxmcap_63d_slope_v110_signal,
    f01icp_f01_industrial_cycle_phase_agrxmcap_126d_slope_v111_signal,
    f01icp_f01_industrial_cycle_phase_agrxmcap_252d_slope_v112_signal,
    f01icp_f01_industrial_cycle_phase_compsig_21d_slope_v113_signal,
    f01icp_f01_industrial_cycle_phase_compsig_63d_slope_v114_signal,
    f01icp_f01_industrial_cycle_phase_compsig_126d_slope_v115_signal,
    f01icp_f01_industrial_cycle_phase_compsig_252d_slope_v116_signal,
    f01icp_f01_industrial_cycle_phase_cesxret_21d_slope_v117_signal,
    f01icp_f01_industrial_cycle_phase_cesxret_63d_slope_v118_signal,
    f01icp_f01_industrial_cycle_phase_cesxret_126d_slope_v119_signal,
    f01icp_f01_industrial_cycle_phase_pbrxvol_21d_slope_v120_signal,
    f01icp_f01_industrial_cycle_phase_pbrxvol_63d_slope_v121_signal,
    f01icp_f01_industrial_cycle_phase_pbrxvol_126d_slope_v122_signal,
    f01icp_f01_industrial_cycle_phase_agrxvol_21d_slope_v123_signal,
    f01icp_f01_industrial_cycle_phase_agrxvol_63d_slope_v124_signal,
    f01icp_f01_industrial_cycle_phase_agrxvol_126d_slope_v125_signal,
    f01icp_f01_industrial_cycle_phase_cesxgm_21d_slope_v126_signal,
    f01icp_f01_industrial_cycle_phase_cesxgm_63d_slope_v127_signal,
    f01icp_f01_industrial_cycle_phase_cesxgm_126d_slope_v128_signal,
    f01icp_f01_industrial_cycle_phase_cesxgm_252d_slope_v129_signal,
    f01icp_f01_industrial_cycle_phase_pbrxgm_21d_slope_v130_signal,
    f01icp_f01_industrial_cycle_phase_pbrxgm_63d_slope_v131_signal,
    f01icp_f01_industrial_cycle_phase_pbrxgm_126d_slope_v132_signal,
    f01icp_f01_industrial_cycle_phase_pbrxgm_252d_slope_v133_signal,
    f01icp_f01_industrial_cycle_phase_agrxgm_21d_slope_v134_signal,
    f01icp_f01_industrial_cycle_phase_agrxgm_63d_slope_v135_signal,
    f01icp_f01_industrial_cycle_phase_agrxgm_126d_slope_v136_signal,
    f01icp_f01_industrial_cycle_phase_agrxgm_252d_slope_v137_signal,
    f01icp_f01_industrial_cycle_phase_cesema_21d_slope_v138_signal,
    f01icp_f01_industrial_cycle_phase_cesema_63d_slope_v139_signal,
    f01icp_f01_industrial_cycle_phase_cesema_126d_slope_v140_signal,
    f01icp_f01_industrial_cycle_phase_pbrema_21d_slope_v141_signal,
    f01icp_f01_industrial_cycle_phase_pbrema_63d_slope_v142_signal,
    f01icp_f01_industrial_cycle_phase_pbrema_126d_slope_v143_signal,
    f01icp_f01_industrial_cycle_phase_agrema_21d_slope_v144_signal,
    f01icp_f01_industrial_cycle_phase_agrema_63d_slope_v145_signal,
    f01icp_f01_industrial_cycle_phase_agrema_126d_slope_v146_signal,
    f01icp_f01_industrial_cycle_phase_cesxev_21d_slope_v147_signal,
    f01icp_f01_industrial_cycle_phase_cesxev_63d_slope_v148_signal,
    f01icp_f01_industrial_cycle_phase_cesxev_126d_slope_v149_signal,
    f01icp_f01_industrial_cycle_phase_cesxev_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F01_INDUSTRIAL_CYCLE_PHASE_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f01_cycle_earnings_strength', '_f01_price_breadth', '_f01_asset_growth_signature')
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f01_industrial_cycle_phase_2nd_derivatives_001_150_claude: {n_features} features pass")
