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


def _ema(s, w):
    return s.ewm(span=max(2, w), adjust=False, min_periods=max(1, w // 2)).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)

# ===== folder domain primitives =====
def _f25_revenue_per_asset(revenue, assets):
    return revenue / assets.replace(0, np.nan)


def _f25_capital_efficiency(revenue, ppnenet, w):
    eff = revenue / ppnenet.replace(0, np.nan)
    return eff.rolling(w, min_periods=max(1, w // 2)).mean()


def _f25_efficiency_compound(revenue, assets, w):
    eff = revenue / assets.replace(0, np.nan)
    return eff * eff.pct_change(periods=w)



# ===== features =====

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_slope_pct_slope_v001_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p10s_slope_pct_slope_v002_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p21s_slope_pct_slope_v003_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p42s_slope_pct_slope_v004_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p63s_slope_pct_slope_v005_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p126s_slope_pct_slope_v006_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p189s_slope_pct_slope_v007_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p252s_slope_pct_slope_v008_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p378s_slope_pct_slope_v009_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p504s_slope_pct_slope_v010_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p7s_slope_pct_slope_v011_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p14s_slope_pct_slope_v012_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p30s_slope_pct_slope_v013_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p45s_slope_pct_slope_v014_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 45) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p90s_slope_pct_slope_v015_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p105s_slope_pct_slope_v016_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 105) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p168s_slope_pct_slope_v017_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p210s_slope_pct_slope_v018_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 210) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p315s_slope_pct_slope_v019_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p420s_slope_pct_slope_v020_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 420) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_slope_diff_slope_v021_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p10s_slope_diff_slope_v022_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p21s_slope_diff_slope_v023_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p42s_slope_diff_slope_v024_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p63s_slope_diff_slope_v025_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p126s_slope_diff_slope_v026_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p189s_slope_diff_slope_v027_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p252s_slope_diff_slope_v028_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p378s_slope_diff_slope_v029_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p504s_slope_diff_slope_v030_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p7s_slope_diff_slope_v031_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p14s_slope_diff_slope_v032_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p30s_slope_diff_slope_v033_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p45s_slope_diff_slope_v034_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 45) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p90s_slope_diff_slope_v035_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p105s_slope_diff_slope_v036_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 105) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p168s_slope_diff_slope_v037_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p210s_slope_diff_slope_v038_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 210) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p315s_slope_diff_slope_v039_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p420s_slope_diff_slope_v040_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 420) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_slope_pct_mean_slope_v041_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 5) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p10s_slope_pct_mean_slope_v042_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 10) * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p21s_slope_pct_mean_slope_v043_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p42s_slope_pct_mean_slope_v044_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 42) * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p63s_slope_pct_mean_slope_v045_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p126s_slope_pct_mean_slope_v046_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 126) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p189s_slope_pct_mean_slope_v047_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 189) * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p252s_slope_pct_mean_slope_v048_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 252) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p378s_slope_pct_mean_slope_v049_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 378) * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p504s_slope_pct_mean_slope_v050_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 504) * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p7s_slope_pct_mean_slope_v051_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 7) * _mean(closeadj, 7)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p14s_slope_pct_mean_slope_v052_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 14) * _mean(closeadj, 14)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p30s_slope_pct_mean_slope_v053_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 30) * _mean(closeadj, 30)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p45s_slope_pct_mean_slope_v054_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 45) * _mean(closeadj, 45)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p90s_slope_pct_mean_slope_v055_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 90) * _mean(closeadj, 90)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p105s_slope_pct_mean_slope_v056_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 105) * _mean(closeadj, 105)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p168s_slope_pct_mean_slope_v057_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 168) * _mean(closeadj, 168)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p210s_slope_pct_mean_slope_v058_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 210) * _mean(closeadj, 210)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p315s_slope_pct_mean_slope_v059_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 315) * _mean(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p420s_slope_pct_mean_slope_v060_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 420) * _mean(closeadj, 420)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_slope_diff_mean_slope_v061_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 5) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p10s_slope_diff_mean_slope_v062_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 10) * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p21s_slope_diff_mean_slope_v063_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p42s_slope_diff_mean_slope_v064_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 42) * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p63s_slope_diff_mean_slope_v065_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p126s_slope_diff_mean_slope_v066_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 126) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p189s_slope_diff_mean_slope_v067_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 189) * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p252s_slope_diff_mean_slope_v068_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 252) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p378s_slope_diff_mean_slope_v069_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 378) * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p504s_slope_diff_mean_slope_v070_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 504) * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p7s_slope_diff_mean_slope_v071_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 7) * _mean(closeadj, 7)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p14s_slope_diff_mean_slope_v072_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 14) * _mean(closeadj, 14)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p30s_slope_diff_mean_slope_v073_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 30) * _mean(closeadj, 30)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p45s_slope_diff_mean_slope_v074_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 45) * _mean(closeadj, 45)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p90s_slope_diff_mean_slope_v075_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 90) * _mean(closeadj, 90)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p105s_slope_diff_mean_slope_v076_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 105) * _mean(closeadj, 105)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p168s_slope_diff_mean_slope_v077_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 168) * _mean(closeadj, 168)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p210s_slope_diff_mean_slope_v078_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 210) * _mean(closeadj, 210)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p315s_slope_diff_mean_slope_v079_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 315) * _mean(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p420s_slope_diff_mean_slope_v080_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 420) * _mean(closeadj, 420)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_slope_pct_ema_slope_v081_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 5) * _ema(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p10s_slope_pct_ema_slope_v082_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 10) * _ema(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p21s_slope_pct_ema_slope_v083_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 21) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p42s_slope_pct_ema_slope_v084_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 42) * _ema(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p63s_slope_pct_ema_slope_v085_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 63) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p126s_slope_pct_ema_slope_v086_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 126) * _ema(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p189s_slope_pct_ema_slope_v087_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 189) * _ema(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p252s_slope_pct_ema_slope_v088_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 252) * _ema(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p378s_slope_pct_ema_slope_v089_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 378) * _ema(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p504s_slope_pct_ema_slope_v090_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 504) * _ema(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p7s_slope_pct_ema_slope_v091_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 7) * _ema(closeadj, 7)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p14s_slope_pct_ema_slope_v092_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 14) * _ema(closeadj, 14)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p30s_slope_pct_ema_slope_v093_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 30) * _ema(closeadj, 30)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p45s_slope_pct_ema_slope_v094_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 45) * _ema(closeadj, 45)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p90s_slope_pct_ema_slope_v095_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 90) * _ema(closeadj, 90)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p105s_slope_pct_ema_slope_v096_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 105) * _ema(closeadj, 105)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p168s_slope_pct_ema_slope_v097_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 168) * _ema(closeadj, 168)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p210s_slope_pct_ema_slope_v098_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 210) * _ema(closeadj, 210)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p315s_slope_pct_ema_slope_v099_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 315) * _ema(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p420s_slope_pct_ema_slope_v100_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 420) * _ema(closeadj, 420)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_slope_diff_ema_slope_v101_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 5) * _ema(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p10s_slope_diff_ema_slope_v102_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 10) * _ema(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p21s_slope_diff_ema_slope_v103_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 21) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p42s_slope_diff_ema_slope_v104_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 42) * _ema(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p63s_slope_diff_ema_slope_v105_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 63) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p126s_slope_diff_ema_slope_v106_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 126) * _ema(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p189s_slope_diff_ema_slope_v107_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 189) * _ema(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p252s_slope_diff_ema_slope_v108_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 252) * _ema(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p378s_slope_diff_ema_slope_v109_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 378) * _ema(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p504s_slope_diff_ema_slope_v110_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 504) * _ema(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p7s_slope_diff_ema_slope_v111_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 7) * _ema(closeadj, 7)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p14s_slope_diff_ema_slope_v112_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 14) * _ema(closeadj, 14)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p30s_slope_diff_ema_slope_v113_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 30) * _ema(closeadj, 30)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p45s_slope_diff_ema_slope_v114_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 45) * _ema(closeadj, 45)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p90s_slope_diff_ema_slope_v115_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 90) * _ema(closeadj, 90)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p105s_slope_diff_ema_slope_v116_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 105) * _ema(closeadj, 105)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p168s_slope_diff_ema_slope_v117_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 168) * _ema(closeadj, 168)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p210s_slope_diff_ema_slope_v118_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 210) * _ema(closeadj, 210)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p315s_slope_diff_ema_slope_v119_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 315) * _ema(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p420s_slope_diff_ema_slope_v120_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_diff_norm(base, 420) * _ema(closeadj, 420)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_slope_pct_std_slope_v121_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 5) * _std(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p10s_slope_pct_std_slope_v122_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 10) * _std(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p21s_slope_pct_std_slope_v123_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 21) * _std(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p42s_slope_pct_std_slope_v124_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 42) * _std(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p63s_slope_pct_std_slope_v125_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 63) * _std(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p126s_slope_pct_std_slope_v126_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 126) * _std(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p189s_slope_pct_std_slope_v127_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 189) * _std(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p252s_slope_pct_std_slope_v128_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 252) * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p378s_slope_pct_std_slope_v129_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 378) * _std(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p504s_slope_pct_std_slope_v130_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 504) * _std(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p7s_slope_pct_std_slope_v131_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 7) * _std(closeadj, 7)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p14s_slope_pct_std_slope_v132_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 14) * _std(closeadj, 14)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p30s_slope_pct_std_slope_v133_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 30) * _std(closeadj, 30)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p45s_slope_pct_std_slope_v134_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 45) * _std(closeadj, 45)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p90s_slope_pct_std_slope_v135_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 90) * _std(closeadj, 90)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p105s_slope_pct_std_slope_v136_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 105) * _std(closeadj, 105)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p168s_slope_pct_std_slope_v137_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 168) * _std(closeadj, 168)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p210s_slope_pct_std_slope_v138_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 210) * _std(closeadj, 210)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p315s_slope_pct_std_slope_v139_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 315) * _std(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p420s_slope_pct_std_slope_v140_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 420) * _std(closeadj, 420)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_slope_pct_z_slope_v141_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 5) * _z(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p10s_slope_pct_z_slope_v142_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 10) * _z(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p21s_slope_pct_z_slope_v143_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 21) * _z(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p42s_slope_pct_z_slope_v144_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 42) * _z(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p63s_slope_pct_z_slope_v145_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p126s_slope_pct_z_slope_v146_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 126) * _z(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p189s_slope_pct_z_slope_v147_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 189) * _z(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p252s_slope_pct_z_slope_v148_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 252) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p378s_slope_pct_z_slope_v149_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 378) * _z(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p504s_slope_pct_z_slope_v150_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _slope_pct(base, 504) * _z(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_slope_pct_slope_v001_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p10s_slope_pct_slope_v002_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p21s_slope_pct_slope_v003_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p42s_slope_pct_slope_v004_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p63s_slope_pct_slope_v005_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p126s_slope_pct_slope_v006_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p189s_slope_pct_slope_v007_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p252s_slope_pct_slope_v008_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p378s_slope_pct_slope_v009_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p504s_slope_pct_slope_v010_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p7s_slope_pct_slope_v011_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p14s_slope_pct_slope_v012_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p30s_slope_pct_slope_v013_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p45s_slope_pct_slope_v014_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p90s_slope_pct_slope_v015_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p105s_slope_pct_slope_v016_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p168s_slope_pct_slope_v017_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p210s_slope_pct_slope_v018_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p315s_slope_pct_slope_v019_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p420s_slope_pct_slope_v020_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_slope_diff_slope_v021_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p10s_slope_diff_slope_v022_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p21s_slope_diff_slope_v023_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p42s_slope_diff_slope_v024_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p63s_slope_diff_slope_v025_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p126s_slope_diff_slope_v026_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p189s_slope_diff_slope_v027_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p252s_slope_diff_slope_v028_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p378s_slope_diff_slope_v029_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p504s_slope_diff_slope_v030_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p7s_slope_diff_slope_v031_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p14s_slope_diff_slope_v032_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p30s_slope_diff_slope_v033_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p45s_slope_diff_slope_v034_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p90s_slope_diff_slope_v035_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p105s_slope_diff_slope_v036_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p168s_slope_diff_slope_v037_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p210s_slope_diff_slope_v038_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p315s_slope_diff_slope_v039_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p420s_slope_diff_slope_v040_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_slope_pct_mean_slope_v041_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p10s_slope_pct_mean_slope_v042_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p21s_slope_pct_mean_slope_v043_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p42s_slope_pct_mean_slope_v044_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p63s_slope_pct_mean_slope_v045_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p126s_slope_pct_mean_slope_v046_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p189s_slope_pct_mean_slope_v047_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p252s_slope_pct_mean_slope_v048_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p378s_slope_pct_mean_slope_v049_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p504s_slope_pct_mean_slope_v050_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p7s_slope_pct_mean_slope_v051_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p14s_slope_pct_mean_slope_v052_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p30s_slope_pct_mean_slope_v053_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p45s_slope_pct_mean_slope_v054_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p90s_slope_pct_mean_slope_v055_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p105s_slope_pct_mean_slope_v056_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p168s_slope_pct_mean_slope_v057_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p210s_slope_pct_mean_slope_v058_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p315s_slope_pct_mean_slope_v059_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p420s_slope_pct_mean_slope_v060_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_slope_diff_mean_slope_v061_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p10s_slope_diff_mean_slope_v062_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p21s_slope_diff_mean_slope_v063_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p42s_slope_diff_mean_slope_v064_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p63s_slope_diff_mean_slope_v065_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p126s_slope_diff_mean_slope_v066_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p189s_slope_diff_mean_slope_v067_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p252s_slope_diff_mean_slope_v068_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p378s_slope_diff_mean_slope_v069_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p504s_slope_diff_mean_slope_v070_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p7s_slope_diff_mean_slope_v071_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p14s_slope_diff_mean_slope_v072_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p30s_slope_diff_mean_slope_v073_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p45s_slope_diff_mean_slope_v074_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p90s_slope_diff_mean_slope_v075_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p105s_slope_diff_mean_slope_v076_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p168s_slope_diff_mean_slope_v077_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p210s_slope_diff_mean_slope_v078_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p315s_slope_diff_mean_slope_v079_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p420s_slope_diff_mean_slope_v080_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_slope_pct_ema_slope_v081_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p10s_slope_pct_ema_slope_v082_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p21s_slope_pct_ema_slope_v083_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p42s_slope_pct_ema_slope_v084_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p63s_slope_pct_ema_slope_v085_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p126s_slope_pct_ema_slope_v086_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p189s_slope_pct_ema_slope_v087_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p252s_slope_pct_ema_slope_v088_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p378s_slope_pct_ema_slope_v089_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p504s_slope_pct_ema_slope_v090_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p7s_slope_pct_ema_slope_v091_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p14s_slope_pct_ema_slope_v092_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p30s_slope_pct_ema_slope_v093_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p45s_slope_pct_ema_slope_v094_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p90s_slope_pct_ema_slope_v095_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p105s_slope_pct_ema_slope_v096_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p168s_slope_pct_ema_slope_v097_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p210s_slope_pct_ema_slope_v098_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p315s_slope_pct_ema_slope_v099_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p420s_slope_pct_ema_slope_v100_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_slope_diff_ema_slope_v101_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p10s_slope_diff_ema_slope_v102_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p21s_slope_diff_ema_slope_v103_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p42s_slope_diff_ema_slope_v104_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p63s_slope_diff_ema_slope_v105_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p126s_slope_diff_ema_slope_v106_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p189s_slope_diff_ema_slope_v107_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p252s_slope_diff_ema_slope_v108_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p378s_slope_diff_ema_slope_v109_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p504s_slope_diff_ema_slope_v110_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p7s_slope_diff_ema_slope_v111_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p14s_slope_diff_ema_slope_v112_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p30s_slope_diff_ema_slope_v113_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p45s_slope_diff_ema_slope_v114_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p90s_slope_diff_ema_slope_v115_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p105s_slope_diff_ema_slope_v116_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p168s_slope_diff_ema_slope_v117_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p210s_slope_diff_ema_slope_v118_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p315s_slope_diff_ema_slope_v119_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p420s_slope_diff_ema_slope_v120_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_slope_pct_std_slope_v121_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p10s_slope_pct_std_slope_v122_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p21s_slope_pct_std_slope_v123_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p42s_slope_pct_std_slope_v124_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p63s_slope_pct_std_slope_v125_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p126s_slope_pct_std_slope_v126_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p189s_slope_pct_std_slope_v127_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p252s_slope_pct_std_slope_v128_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p378s_slope_pct_std_slope_v129_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p504s_slope_pct_std_slope_v130_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p7s_slope_pct_std_slope_v131_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p14s_slope_pct_std_slope_v132_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p30s_slope_pct_std_slope_v133_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p45s_slope_pct_std_slope_v134_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p90s_slope_pct_std_slope_v135_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p105s_slope_pct_std_slope_v136_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p168s_slope_pct_std_slope_v137_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p210s_slope_pct_std_slope_v138_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p315s_slope_pct_std_slope_v139_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p420s_slope_pct_std_slope_v140_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_slope_pct_z_slope_v141_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p10s_slope_pct_z_slope_v142_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p21s_slope_pct_z_slope_v143_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p42s_slope_pct_z_slope_v144_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p63s_slope_pct_z_slope_v145_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p126s_slope_pct_z_slope_v146_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p189s_slope_pct_z_slope_v147_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p252s_slope_pct_z_slope_v148_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p378s_slope_pct_z_slope_v149_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p504s_slope_pct_z_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_TRANSMISSION_CAPITAL_EFFICIENCY_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    deferredrev = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")

    cols = {"closeadj": closeadj, "revenue": revenue, "ebitda": ebitda,
            "capex": capex, "assets": assets, "ppnenet": ppnenet,
            "deferredrev": deferredrev}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f25_revenue_per_asset', '_f25_capital_efficiency', '_f25_efficiency_compound')
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
    print(f"OK f25_transmission_capital_efficiency_slope_001_150_claude: {n_features} features pass")
