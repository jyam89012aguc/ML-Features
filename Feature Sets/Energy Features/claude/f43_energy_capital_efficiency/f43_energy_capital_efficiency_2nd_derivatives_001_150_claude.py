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
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)

# ===== folder domain primitives =====
def _f43_asset_turnover(revenue, assets):
    return revenue / assets.replace(0, np.nan).abs()


def _f43_capital_efficiency(revenue, ppnenet, w):
    eff = revenue / ppnenet.replace(0, np.nan).abs()
    return eff.rolling(w, min_periods=max(1, w // 2)).mean()


def _f43_efficiency_compound(revenue, assets, w):
    turn = revenue / assets.replace(0, np.nan).abs()
    growth = turn.pct_change(periods=w)
    return turn * (1.0 + growth.fillna(0.0))

# ===== features =====
def f43ece_f43_energy_capital_efficiency_asset_turnover_x_raw_slope_v001_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_raw_slope_v002_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets))
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_raw_slope_v003_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_raw_slope_v004_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets))
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_raw_slope_v005_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_raw_slope_v006_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_xc_slope_v007_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets)) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_xc_slope_v008_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_xc_slope_v009_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_xc_slope_v010_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets)) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_xc_slope_v011_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_xc_slope_v012_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets)) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_xc2_slope_v013_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets)) * closeadj * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_xc2_slope_v014_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets)) * closeadj * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_xc2_slope_v015_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets)) * closeadj * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_xc2_slope_v016_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets)) * closeadj * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_xc2_slope_v017_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets)) * closeadj * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_xc2_slope_v018_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets)) * closeadj * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_mean21_slope_v019_signal(revenue, assets, closeadj):
    base = _mean((_f43_asset_turnover(revenue, assets)), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_mean21_slope_v020_signal(revenue, assets, closeadj):
    base = _mean((_f43_asset_turnover(revenue, assets)), 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_mean21_slope_v021_signal(revenue, assets, closeadj):
    base = _mean((_f43_asset_turnover(revenue, assets)), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_mean21_slope_v022_signal(revenue, assets, closeadj):
    base = _mean((_f43_asset_turnover(revenue, assets)), 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_mean21_slope_v023_signal(revenue, assets, closeadj):
    base = _mean((_f43_asset_turnover(revenue, assets)), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_mean21_slope_v024_signal(revenue, assets, closeadj):
    base = _mean((_f43_asset_turnover(revenue, assets)), 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_mean63_slope_v025_signal(revenue, assets, closeadj):
    base = _mean((_f43_asset_turnover(revenue, assets)), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_mean63_slope_v026_signal(revenue, assets, closeadj):
    base = _mean((_f43_asset_turnover(revenue, assets)), 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_mean63_slope_v027_signal(revenue, assets, closeadj):
    base = _mean((_f43_asset_turnover(revenue, assets)), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_mean63_slope_v028_signal(revenue, assets, closeadj):
    base = _mean((_f43_asset_turnover(revenue, assets)), 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_mean63_slope_v029_signal(revenue, assets, closeadj):
    base = _mean((_f43_asset_turnover(revenue, assets)), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_mean63_slope_v030_signal(revenue, assets, closeadj):
    base = _mean((_f43_asset_turnover(revenue, assets)), 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_ema21_slope_v031_signal(revenue, assets, closeadj):
    base = _ema((_f43_asset_turnover(revenue, assets)), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_ema21_slope_v032_signal(revenue, assets, closeadj):
    base = _ema((_f43_asset_turnover(revenue, assets)), 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_ema21_slope_v033_signal(revenue, assets, closeadj):
    base = _ema((_f43_asset_turnover(revenue, assets)), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_ema21_slope_v034_signal(revenue, assets, closeadj):
    base = _ema((_f43_asset_turnover(revenue, assets)), 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_ema21_slope_v035_signal(revenue, assets, closeadj):
    base = _ema((_f43_asset_turnover(revenue, assets)), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_ema21_slope_v036_signal(revenue, assets, closeadj):
    base = _ema((_f43_asset_turnover(revenue, assets)), 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_ema63_slope_v037_signal(revenue, assets, closeadj):
    base = _ema((_f43_asset_turnover(revenue, assets)), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_ema63_slope_v038_signal(revenue, assets, closeadj):
    base = _ema((_f43_asset_turnover(revenue, assets)), 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_ema63_slope_v039_signal(revenue, assets, closeadj):
    base = _ema((_f43_asset_turnover(revenue, assets)), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_ema63_slope_v040_signal(revenue, assets, closeadj):
    base = _ema((_f43_asset_turnover(revenue, assets)), 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_ema63_slope_v041_signal(revenue, assets, closeadj):
    base = _ema((_f43_asset_turnover(revenue, assets)), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_ema63_slope_v042_signal(revenue, assets, closeadj):
    base = _ema((_f43_asset_turnover(revenue, assets)), 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_std21_slope_v043_signal(revenue, assets, closeadj):
    base = _std((_f43_asset_turnover(revenue, assets)), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_std21_slope_v044_signal(revenue, assets, closeadj):
    base = _std((_f43_asset_turnover(revenue, assets)), 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_std21_slope_v045_signal(revenue, assets, closeadj):
    base = _std((_f43_asset_turnover(revenue, assets)), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_std21_slope_v046_signal(revenue, assets, closeadj):
    base = _std((_f43_asset_turnover(revenue, assets)), 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_std21_slope_v047_signal(revenue, assets, closeadj):
    base = _std((_f43_asset_turnover(revenue, assets)), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_std21_slope_v048_signal(revenue, assets, closeadj):
    base = _std((_f43_asset_turnover(revenue, assets)), 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_std63_slope_v049_signal(revenue, assets, closeadj):
    base = _std((_f43_asset_turnover(revenue, assets)), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_std63_slope_v050_signal(revenue, assets, closeadj):
    base = _std((_f43_asset_turnover(revenue, assets)), 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_std63_slope_v051_signal(revenue, assets, closeadj):
    base = _std((_f43_asset_turnover(revenue, assets)), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_std63_slope_v052_signal(revenue, assets, closeadj):
    base = _std((_f43_asset_turnover(revenue, assets)), 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_std63_slope_v053_signal(revenue, assets, closeadj):
    base = _std((_f43_asset_turnover(revenue, assets)), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_std63_slope_v054_signal(revenue, assets, closeadj):
    base = _std((_f43_asset_turnover(revenue, assets)), 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_z63_slope_v055_signal(revenue, assets, closeadj):
    base = _z((_f43_asset_turnover(revenue, assets)), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_z63_slope_v056_signal(revenue, assets, closeadj):
    base = _z((_f43_asset_turnover(revenue, assets)), 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_z63_slope_v057_signal(revenue, assets, closeadj):
    base = _z((_f43_asset_turnover(revenue, assets)), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_z63_slope_v058_signal(revenue, assets, closeadj):
    base = _z((_f43_asset_turnover(revenue, assets)), 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_z63_slope_v059_signal(revenue, assets, closeadj):
    base = _z((_f43_asset_turnover(revenue, assets)), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_z63_slope_v060_signal(revenue, assets, closeadj):
    base = _z((_f43_asset_turnover(revenue, assets)), 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_z126_slope_v061_signal(revenue, assets, closeadj):
    base = _z((_f43_asset_turnover(revenue, assets)), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_z126_slope_v062_signal(revenue, assets, closeadj):
    base = _z((_f43_asset_turnover(revenue, assets)), 126) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_z126_slope_v063_signal(revenue, assets, closeadj):
    base = _z((_f43_asset_turnover(revenue, assets)), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_z126_slope_v064_signal(revenue, assets, closeadj):
    base = _z((_f43_asset_turnover(revenue, assets)), 126) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_z126_slope_v065_signal(revenue, assets, closeadj):
    base = _z((_f43_asset_turnover(revenue, assets)), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_z126_slope_v066_signal(revenue, assets, closeadj):
    base = _z((_f43_asset_turnover(revenue, assets)), 126) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_abs_xc_slope_v067_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets)).abs() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_abs_xc_slope_v068_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets)).abs() * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_abs_xc_slope_v069_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets)).abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_abs_xc_slope_v070_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets)).abs() * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_abs_xc_slope_v071_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets)).abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_abs_xc_slope_v072_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_sq_xc_slope_v073_signal(revenue, assets, closeadj):
    base = ((_f43_asset_turnover(revenue, assets))**2) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_sq_xc_slope_v074_signal(revenue, assets, closeadj):
    base = ((_f43_asset_turnover(revenue, assets))**2) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_sq_xc_slope_v075_signal(revenue, assets, closeadj):
    base = ((_f43_asset_turnover(revenue, assets))**2) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_sq_xc_slope_v076_signal(revenue, assets, closeadj):
    base = ((_f43_asset_turnover(revenue, assets))**2) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_sq_xc_slope_v077_signal(revenue, assets, closeadj):
    base = ((_f43_asset_turnover(revenue, assets))**2) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_sq_xc_slope_v078_signal(revenue, assets, closeadj):
    base = ((_f43_asset_turnover(revenue, assets))**2) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_emamean21_slope_v079_signal(revenue, assets, closeadj):
    base = _ema(_mean((_f43_asset_turnover(revenue, assets)), 21), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_emamean21_slope_v080_signal(revenue, assets, closeadj):
    base = _ema(_mean((_f43_asset_turnover(revenue, assets)), 21), 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_emamean21_slope_v081_signal(revenue, assets, closeadj):
    base = _ema(_mean((_f43_asset_turnover(revenue, assets)), 21), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_emamean21_slope_v082_signal(revenue, assets, closeadj):
    base = _ema(_mean((_f43_asset_turnover(revenue, assets)), 21), 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_emamean21_slope_v083_signal(revenue, assets, closeadj):
    base = _ema(_mean((_f43_asset_turnover(revenue, assets)), 21), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_emamean21_slope_v084_signal(revenue, assets, closeadj):
    base = _ema(_mean((_f43_asset_turnover(revenue, assets)), 21), 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_logc_slope_v085_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets)) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_logc_slope_v086_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets)) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_logc_slope_v087_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets)) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_logc_slope_v088_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets)) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_logc_slope_v089_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets)) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_logc_slope_v090_signal(revenue, assets, closeadj):
    base = (_f43_asset_turnover(revenue, assets)) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_rngxc_slope_v091_signal(revenue, assets, closeadj):
    base = ((_f43_asset_turnover(revenue, assets)).rolling(21, min_periods=10).max() - (_f43_asset_turnover(revenue, assets)).rolling(21, min_periods=10).min()) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_rngxc_slope_v092_signal(revenue, assets, closeadj):
    base = ((_f43_asset_turnover(revenue, assets)).rolling(21, min_periods=10).max() - (_f43_asset_turnover(revenue, assets)).rolling(21, min_periods=10).min()) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_rngxc_slope_v093_signal(revenue, assets, closeadj):
    base = ((_f43_asset_turnover(revenue, assets)).rolling(21, min_periods=10).max() - (_f43_asset_turnover(revenue, assets)).rolling(21, min_periods=10).min()) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_rngxc_slope_v094_signal(revenue, assets, closeadj):
    base = ((_f43_asset_turnover(revenue, assets)).rolling(21, min_periods=10).max() - (_f43_asset_turnover(revenue, assets)).rolling(21, min_periods=10).min()) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_rngxc_slope_v095_signal(revenue, assets, closeadj):
    base = ((_f43_asset_turnover(revenue, assets)).rolling(21, min_periods=10).max() - (_f43_asset_turnover(revenue, assets)).rolling(21, min_periods=10).min()) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_asset_turnover_x_rngxc_slope_v096_signal(revenue, assets, closeadj):
    base = ((_f43_asset_turnover(revenue, assets)).rolling(21, min_periods=10).max() - (_f43_asset_turnover(revenue, assets)).rolling(21, min_periods=10).min()) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_raw_slope_v097_signal(revenue, ppnenet, closeadj):
    base = (_f43_capital_efficiency(revenue, ppnenet, 5))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_raw_slope_v098_signal(revenue, ppnenet, closeadj):
    base = (_f43_capital_efficiency(revenue, ppnenet, 5))
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_raw_slope_v099_signal(revenue, ppnenet, closeadj):
    base = (_f43_capital_efficiency(revenue, ppnenet, 5))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_raw_slope_v100_signal(revenue, ppnenet, closeadj):
    base = (_f43_capital_efficiency(revenue, ppnenet, 5))
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_raw_slope_v101_signal(revenue, ppnenet, closeadj):
    base = (_f43_capital_efficiency(revenue, ppnenet, 5))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_raw_slope_v102_signal(revenue, ppnenet, closeadj):
    base = (_f43_capital_efficiency(revenue, ppnenet, 5))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_xc_slope_v103_signal(revenue, ppnenet, closeadj):
    base = (_f43_capital_efficiency(revenue, ppnenet, 5)) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_xc_slope_v104_signal(revenue, ppnenet, closeadj):
    base = (_f43_capital_efficiency(revenue, ppnenet, 5)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_xc_slope_v105_signal(revenue, ppnenet, closeadj):
    base = (_f43_capital_efficiency(revenue, ppnenet, 5)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_xc_slope_v106_signal(revenue, ppnenet, closeadj):
    base = (_f43_capital_efficiency(revenue, ppnenet, 5)) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_xc_slope_v107_signal(revenue, ppnenet, closeadj):
    base = (_f43_capital_efficiency(revenue, ppnenet, 5)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_xc_slope_v108_signal(revenue, ppnenet, closeadj):
    base = (_f43_capital_efficiency(revenue, ppnenet, 5)) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_xc2_slope_v109_signal(revenue, ppnenet, closeadj):
    base = (_f43_capital_efficiency(revenue, ppnenet, 5)) * closeadj * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_xc2_slope_v110_signal(revenue, ppnenet, closeadj):
    base = (_f43_capital_efficiency(revenue, ppnenet, 5)) * closeadj * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_xc2_slope_v111_signal(revenue, ppnenet, closeadj):
    base = (_f43_capital_efficiency(revenue, ppnenet, 5)) * closeadj * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_xc2_slope_v112_signal(revenue, ppnenet, closeadj):
    base = (_f43_capital_efficiency(revenue, ppnenet, 5)) * closeadj * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_xc2_slope_v113_signal(revenue, ppnenet, closeadj):
    base = (_f43_capital_efficiency(revenue, ppnenet, 5)) * closeadj * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_xc2_slope_v114_signal(revenue, ppnenet, closeadj):
    base = (_f43_capital_efficiency(revenue, ppnenet, 5)) * closeadj * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_mean21_slope_v115_signal(revenue, ppnenet, closeadj):
    base = _mean((_f43_capital_efficiency(revenue, ppnenet, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_mean21_slope_v116_signal(revenue, ppnenet, closeadj):
    base = _mean((_f43_capital_efficiency(revenue, ppnenet, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_mean21_slope_v117_signal(revenue, ppnenet, closeadj):
    base = _mean((_f43_capital_efficiency(revenue, ppnenet, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_mean21_slope_v118_signal(revenue, ppnenet, closeadj):
    base = _mean((_f43_capital_efficiency(revenue, ppnenet, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_mean21_slope_v119_signal(revenue, ppnenet, closeadj):
    base = _mean((_f43_capital_efficiency(revenue, ppnenet, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_mean21_slope_v120_signal(revenue, ppnenet, closeadj):
    base = _mean((_f43_capital_efficiency(revenue, ppnenet, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_mean63_slope_v121_signal(revenue, ppnenet, closeadj):
    base = _mean((_f43_capital_efficiency(revenue, ppnenet, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_mean63_slope_v122_signal(revenue, ppnenet, closeadj):
    base = _mean((_f43_capital_efficiency(revenue, ppnenet, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_mean63_slope_v123_signal(revenue, ppnenet, closeadj):
    base = _mean((_f43_capital_efficiency(revenue, ppnenet, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_mean63_slope_v124_signal(revenue, ppnenet, closeadj):
    base = _mean((_f43_capital_efficiency(revenue, ppnenet, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_mean63_slope_v125_signal(revenue, ppnenet, closeadj):
    base = _mean((_f43_capital_efficiency(revenue, ppnenet, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_mean63_slope_v126_signal(revenue, ppnenet, closeadj):
    base = _mean((_f43_capital_efficiency(revenue, ppnenet, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_ema21_slope_v127_signal(revenue, ppnenet, closeadj):
    base = _ema((_f43_capital_efficiency(revenue, ppnenet, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_ema21_slope_v128_signal(revenue, ppnenet, closeadj):
    base = _ema((_f43_capital_efficiency(revenue, ppnenet, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_ema21_slope_v129_signal(revenue, ppnenet, closeadj):
    base = _ema((_f43_capital_efficiency(revenue, ppnenet, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_ema21_slope_v130_signal(revenue, ppnenet, closeadj):
    base = _ema((_f43_capital_efficiency(revenue, ppnenet, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_ema21_slope_v131_signal(revenue, ppnenet, closeadj):
    base = _ema((_f43_capital_efficiency(revenue, ppnenet, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_ema21_slope_v132_signal(revenue, ppnenet, closeadj):
    base = _ema((_f43_capital_efficiency(revenue, ppnenet, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_ema63_slope_v133_signal(revenue, ppnenet, closeadj):
    base = _ema((_f43_capital_efficiency(revenue, ppnenet, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_ema63_slope_v134_signal(revenue, ppnenet, closeadj):
    base = _ema((_f43_capital_efficiency(revenue, ppnenet, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_ema63_slope_v135_signal(revenue, ppnenet, closeadj):
    base = _ema((_f43_capital_efficiency(revenue, ppnenet, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_ema63_slope_v136_signal(revenue, ppnenet, closeadj):
    base = _ema((_f43_capital_efficiency(revenue, ppnenet, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_ema63_slope_v137_signal(revenue, ppnenet, closeadj):
    base = _ema((_f43_capital_efficiency(revenue, ppnenet, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_ema63_slope_v138_signal(revenue, ppnenet, closeadj):
    base = _ema((_f43_capital_efficiency(revenue, ppnenet, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_std21_slope_v139_signal(revenue, ppnenet, closeadj):
    base = _std((_f43_capital_efficiency(revenue, ppnenet, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_std21_slope_v140_signal(revenue, ppnenet, closeadj):
    base = _std((_f43_capital_efficiency(revenue, ppnenet, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_std21_slope_v141_signal(revenue, ppnenet, closeadj):
    base = _std((_f43_capital_efficiency(revenue, ppnenet, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_std21_slope_v142_signal(revenue, ppnenet, closeadj):
    base = _std((_f43_capital_efficiency(revenue, ppnenet, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_std21_slope_v143_signal(revenue, ppnenet, closeadj):
    base = _std((_f43_capital_efficiency(revenue, ppnenet, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_std21_slope_v144_signal(revenue, ppnenet, closeadj):
    base = _std((_f43_capital_efficiency(revenue, ppnenet, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_std63_slope_v145_signal(revenue, ppnenet, closeadj):
    base = _std((_f43_capital_efficiency(revenue, ppnenet, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_std63_slope_v146_signal(revenue, ppnenet, closeadj):
    base = _std((_f43_capital_efficiency(revenue, ppnenet, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_std63_slope_v147_signal(revenue, ppnenet, closeadj):
    base = _std((_f43_capital_efficiency(revenue, ppnenet, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_std63_slope_v148_signal(revenue, ppnenet, closeadj):
    base = _std((_f43_capital_efficiency(revenue, ppnenet, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_std63_slope_v149_signal(revenue, ppnenet, closeadj):
    base = _std((_f43_capital_efficiency(revenue, ppnenet, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_std63_slope_v150_signal(revenue, ppnenet, closeadj):
    base = _std((_f43_capital_efficiency(revenue, ppnenet, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_raw_slope_v001_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_raw_slope_v002_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_raw_slope_v003_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_raw_slope_v004_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_raw_slope_v005_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_raw_slope_v006_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_xc_slope_v007_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_xc_slope_v008_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_xc_slope_v009_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_xc_slope_v010_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_xc_slope_v011_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_xc_slope_v012_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_xc2_slope_v013_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_xc2_slope_v014_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_xc2_slope_v015_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_xc2_slope_v016_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_xc2_slope_v017_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_xc2_slope_v018_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_mean21_slope_v019_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_mean21_slope_v020_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_mean21_slope_v021_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_mean21_slope_v022_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_mean21_slope_v023_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_mean21_slope_v024_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_mean63_slope_v025_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_mean63_slope_v026_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_mean63_slope_v027_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_mean63_slope_v028_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_mean63_slope_v029_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_mean63_slope_v030_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_ema21_slope_v031_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_ema21_slope_v032_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_ema21_slope_v033_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_ema21_slope_v034_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_ema21_slope_v035_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_ema21_slope_v036_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_ema63_slope_v037_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_ema63_slope_v038_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_ema63_slope_v039_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_ema63_slope_v040_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_ema63_slope_v041_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_ema63_slope_v042_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_std21_slope_v043_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_std21_slope_v044_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_std21_slope_v045_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_std21_slope_v046_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_std21_slope_v047_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_std21_slope_v048_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_std63_slope_v049_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_std63_slope_v050_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_std63_slope_v051_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_std63_slope_v052_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_std63_slope_v053_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_std63_slope_v054_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_z63_slope_v055_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_z63_slope_v056_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_z63_slope_v057_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_z63_slope_v058_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_z63_slope_v059_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_z63_slope_v060_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_z126_slope_v061_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_z126_slope_v062_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_z126_slope_v063_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_z126_slope_v064_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_z126_slope_v065_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_z126_slope_v066_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_abs_xc_slope_v067_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_abs_xc_slope_v068_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_abs_xc_slope_v069_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_abs_xc_slope_v070_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_abs_xc_slope_v071_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_abs_xc_slope_v072_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_sq_xc_slope_v073_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_sq_xc_slope_v074_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_sq_xc_slope_v075_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_sq_xc_slope_v076_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_sq_xc_slope_v077_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_sq_xc_slope_v078_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_emamean21_slope_v079_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_emamean21_slope_v080_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_emamean21_slope_v081_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_emamean21_slope_v082_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_emamean21_slope_v083_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_emamean21_slope_v084_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_logc_slope_v085_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_logc_slope_v086_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_logc_slope_v087_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_logc_slope_v088_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_logc_slope_v089_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_logc_slope_v090_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_rngxc_slope_v091_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_rngxc_slope_v092_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_rngxc_slope_v093_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_rngxc_slope_v094_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_rngxc_slope_v095_signal,
    f43ece_f43_energy_capital_efficiency_asset_turnover_x_rngxc_slope_v096_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_raw_slope_v097_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_raw_slope_v098_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_raw_slope_v099_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_raw_slope_v100_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_raw_slope_v101_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_raw_slope_v102_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_xc_slope_v103_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_xc_slope_v104_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_xc_slope_v105_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_xc_slope_v106_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_xc_slope_v107_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_xc_slope_v108_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_xc2_slope_v109_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_xc2_slope_v110_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_xc2_slope_v111_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_xc2_slope_v112_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_xc2_slope_v113_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_xc2_slope_v114_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_mean21_slope_v115_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_mean21_slope_v116_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_mean21_slope_v117_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_mean21_slope_v118_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_mean21_slope_v119_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_mean21_slope_v120_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_mean63_slope_v121_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_mean63_slope_v122_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_mean63_slope_v123_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_mean63_slope_v124_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_mean63_slope_v125_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_mean63_slope_v126_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_ema21_slope_v127_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_ema21_slope_v128_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_ema21_slope_v129_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_ema21_slope_v130_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_ema21_slope_v131_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_ema21_slope_v132_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_ema63_slope_v133_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_ema63_slope_v134_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_ema63_slope_v135_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_ema63_slope_v136_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_ema63_slope_v137_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_ema63_slope_v138_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_std21_slope_v139_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_std21_slope_v140_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_std21_slope_v141_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_std21_slope_v142_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_std21_slope_v143_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_std21_slope_v144_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_std63_slope_v145_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_std63_slope_v146_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_std63_slope_v147_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_std63_slope_v148_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_std63_slope_v149_signal,
    f43ece_f43_energy_capital_efficiency_capital_efficiency_5d_std63_slope_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]

REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_ENERGY_CAPITAL_EFFICIENCY_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor,
        "assets": assets, "liabilities": liabilities, "equity": equity,
        "debt": debt, "cashneq": cashneq, "ppnenet": ppnenet,
        "marketcap": marketcap, "ev": ev,
        "roa": roa, "roe": roe, "roic": roic,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f43_asset_turnover", "_f43_capital_efficiency", "_f43_efficiency_compound")
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
    print(f"OK f43_energy_capital_efficiency_2nd_derivatives_001_150_claude: {n_features} features pass")
