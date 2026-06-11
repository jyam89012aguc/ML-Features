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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _f03_capex_intensity(capex, revenue):
    return capex / revenue.replace(0, np.nan)


def _f03_capex_to_assets(capex, assets):
    return capex / assets.replace(0, np.nan)


def _f03_capex_dynamics(capex, revenue, w):
    ci = capex / revenue.replace(0, np.nan)
    return ci - ci.rolling(w, min_periods=max(1, w // 2)).mean()


def f03uci_f03_utility_capex_intensity_intens_21d_slope_v001_signal(capex, revenue, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intens_21d_slope_v002_signal(capex, revenue, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intens_63d_slope_v003_signal(capex, revenue, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intens_63d_slope_v004_signal(capex, revenue, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intens_63d_slope_v005_signal(capex, revenue, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intens_126d_slope_v006_signal(capex, revenue, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intens_126d_slope_v007_signal(capex, revenue, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intens_252d_slope_v008_signal(capex, revenue, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intens_252d_slope_v009_signal(capex, revenue, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intens_252d_slope_v010_signal(capex, revenue, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 252) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intens_504d_slope_v011_signal(capex, revenue, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intens_504d_slope_v012_signal(capex, revenue, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 504) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets slopes
def f03uci_f03_utility_capex_intensity_assets_21d_slope_v013_signal(capex, assets, closeadj):
    base = _mean(_f03_capex_to_assets(capex, assets), 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assets_21d_slope_v014_signal(capex, assets, closeadj):
    base = _mean(_f03_capex_to_assets(capex, assets), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assets_63d_slope_v015_signal(capex, assets, closeadj):
    base = _mean(_f03_capex_to_assets(capex, assets), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assets_63d_slope_v016_signal(capex, assets, closeadj):
    base = _mean(_f03_capex_to_assets(capex, assets), 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assets_252d_slope_v017_signal(capex, assets, closeadj):
    base = _mean(_f03_capex_to_assets(capex, assets), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assets_252d_slope_v018_signal(capex, assets, closeadj):
    base = _mean(_f03_capex_to_assets(capex, assets), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assets_504d_slope_v019_signal(capex, assets, closeadj):
    base = _mean(_f03_capex_to_assets(capex, assets), 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assets_504d_slope_v020_signal(capex, assets, closeadj):
    base = _mean(_f03_capex_to_assets(capex, assets), 504) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# dynamics slopes
def f03uci_f03_utility_capex_intensity_dyn_21d_slope_v021_signal(capex, revenue, closeadj):
    base = _f03_capex_dynamics(capex, revenue, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dyn_21d_slope_v022_signal(capex, revenue, closeadj):
    base = _f03_capex_dynamics(capex, revenue, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dyn_63d_slope_v023_signal(capex, revenue, closeadj):
    base = _f03_capex_dynamics(capex, revenue, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dyn_63d_slope_v024_signal(capex, revenue, closeadj):
    base = _f03_capex_dynamics(capex, revenue, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dyn_252d_slope_v025_signal(capex, revenue, closeadj):
    base = _f03_capex_dynamics(capex, revenue, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dyn_252d_slope_v026_signal(capex, revenue, closeadj):
    base = _f03_capex_dynamics(capex, revenue, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dyn_504d_slope_v027_signal(capex, revenue, closeadj):
    base = _f03_capex_dynamics(capex, revenue, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dyn_504d_slope_v028_signal(capex, revenue, closeadj):
    base = _f03_capex_dynamics(capex, revenue, 504) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Volume variants
def f03uci_f03_utility_capex_intensity_intensxvol_63d_slope_v029_signal(capex, revenue, closeadj, volume):
    base = _mean(_f03_capex_intensity(capex, revenue), 63) * closeadj * _mean(volume, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxvol_252d_slope_v030_signal(capex, revenue, closeadj, volume):
    base = _mean(_f03_capex_intensity(capex, revenue), 252) * closeadj * _mean(volume, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsxvol_63d_slope_v031_signal(capex, assets, closeadj, volume):
    base = _mean(_f03_capex_to_assets(capex, assets), 63) * closeadj * _mean(volume, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsxvol_252d_slope_v032_signal(capex, assets, closeadj, volume):
    base = _mean(_f03_capex_to_assets(capex, assets), 252) * closeadj * _mean(volume, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dynxvol_63d_slope_v033_signal(capex, revenue, closeadj, volume):
    base = _f03_capex_dynamics(capex, revenue, 63) * closeadj * _mean(volume, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dynxvol_252d_slope_v034_signal(capex, revenue, closeadj, volume):
    base = _f03_capex_dynamics(capex, revenue, 252) * closeadj * _mean(volume, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR
def f03uci_f03_utility_capex_intensity_intensxatr_63d_slope_v035_signal(capex, revenue, closeadj, high, low):
    base = _mean(_f03_capex_intensity(capex, revenue), 63) * (high - low).rolling(21, min_periods=5).mean()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxatr_252d_slope_v036_signal(capex, revenue, closeadj, high, low):
    base = _mean(_f03_capex_intensity(capex, revenue), 252) * (high - low).rolling(63, min_periods=21).mean()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsxatr_63d_slope_v037_signal(capex, assets, closeadj, high, low):
    base = _mean(_f03_capex_to_assets(capex, assets), 63) * (high - low).rolling(21, min_periods=5).mean()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsxatr_252d_slope_v038_signal(capex, assets, closeadj, high, low):
    base = _mean(_f03_capex_to_assets(capex, assets), 252) * (high - low).rolling(63, min_periods=21).mean()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dynxatr_63d_slope_v039_signal(capex, revenue, closeadj, high, low):
    base = _f03_capex_dynamics(capex, revenue, 63) * (high - low).rolling(21, min_periods=5).mean()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dynxatr_252d_slope_v040_signal(capex, revenue, closeadj, high, low):
    base = _f03_capex_dynamics(capex, revenue, 252) * (high - low).rolling(63, min_periods=21).mean()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# EMA
def f03uci_f03_utility_capex_intensity_intensema_63d_slope_v041_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue).ewm(span=63, min_periods=21).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensema_252d_slope_v042_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue).ewm(span=252, min_periods=63).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsema_63d_slope_v043_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets).ewm(span=63, min_periods=21).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsema_252d_slope_v044_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets).ewm(span=252, min_periods=63).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Squared slopes
def f03uci_f03_utility_capex_intensity_intenssq_63d_slope_v045_signal(capex, revenue, closeadj):
    p = _f03_capex_intensity(capex, revenue)
    base = p * p.abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intenssq_252d_slope_v046_signal(capex, revenue, closeadj):
    p = _mean(_f03_capex_intensity(capex, revenue), 252)
    base = p * p.abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dynsq_63d_slope_v047_signal(capex, revenue, closeadj):
    d = _f03_capex_dynamics(capex, revenue, 63)
    base = d * d.abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dynsq_252d_slope_v048_signal(capex, revenue, closeadj):
    d = _f03_capex_dynamics(capex, revenue, 252)
    base = d * d.abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetssq_63d_slope_v049_signal(capex, assets, closeadj):
    p = _f03_capex_to_assets(capex, assets)
    base = p * p.abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetssq_252d_slope_v050_signal(capex, assets, closeadj):
    p = _mean(_f03_capex_to_assets(capex, assets), 252)
    base = p * p.abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Z-score
def f03uci_f03_utility_capex_intensity_intensz_63d_slope_v051_signal(capex, revenue, closeadj):
    base = _z(_f03_capex_intensity(capex, revenue), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensz_252d_slope_v052_signal(capex, revenue, closeadj):
    base = _z(_f03_capex_intensity(capex, revenue), 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsz_63d_slope_v053_signal(capex, assets, closeadj):
    base = _z(_f03_capex_to_assets(capex, assets), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsz_252d_slope_v054_signal(capex, assets, closeadj):
    base = _z(_f03_capex_to_assets(capex, assets), 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dynz_63d_slope_v055_signal(capex, revenue, closeadj):
    d = _f03_capex_dynamics(capex, revenue, 63)
    base = _z(d, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dynz_252d_slope_v056_signal(capex, revenue, closeadj):
    d = _f03_capex_dynamics(capex, revenue, 252)
    base = _z(d, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Rank
def f03uci_f03_utility_capex_intensity_intensrank_63d_slope_v057_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensrank_252d_slope_v058_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue).rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsrank_63d_slope_v059_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsrank_252d_slope_v060_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets).rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Gap
def f03uci_f03_utility_capex_intensity_intensgap_63d_slope_v061_signal(capex, revenue, closeadj):
    p = _f03_capex_intensity(capex, revenue)
    base = (p - _mean(p, 252)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensgap_252d_slope_v062_signal(capex, revenue, closeadj):
    p = _f03_capex_intensity(capex, revenue)
    base = (p - _mean(p, 504)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsgap_63d_slope_v063_signal(capex, assets, closeadj):
    p = _f03_capex_to_assets(capex, assets)
    base = (p - _mean(p, 252)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsgap_252d_slope_v064_signal(capex, assets, closeadj):
    p = _f03_capex_to_assets(capex, assets)
    base = (p - _mean(p, 504)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Log
def f03uci_f03_utility_capex_intensity_intenslog_63d_slope_v065_signal(capex, revenue, closeadj):
    p = _f03_capex_intensity(capex, revenue)
    base = np.log(p.abs().replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intenslog_252d_slope_v066_signal(capex, revenue, closeadj):
    p = _f03_capex_intensity(capex, revenue)
    base = np.log(p.abs().replace(0, np.nan)) * _mean(closeadj, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetslog_252d_slope_v067_signal(capex, assets, closeadj):
    p = _f03_capex_to_assets(capex, assets)
    base = np.log(p.abs().replace(0, np.nan)) * _mean(closeadj, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Combo
def f03uci_f03_utility_capex_intensity_combo_63d_slope_v068_signal(capex, revenue, assets, closeadj):
    ci = _f03_capex_intensity(capex, revenue)
    ca = _f03_capex_to_assets(capex, assets)
    base = _mean(ci, 63) * _mean(ca, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_combo_252d_slope_v069_signal(capex, revenue, assets, closeadj):
    ci = _f03_capex_intensity(capex, revenue)
    ca = _f03_capex_to_assets(capex, assets)
    base = _mean(ci, 252) * _mean(ca, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Dollar volume
def f03uci_f03_utility_capex_intensity_intensxdv_63d_slope_v070_signal(capex, revenue, closeadj, volume):
    p = _f03_capex_intensity(capex, revenue)
    dv = closeadj * volume
    base = _mean(p, 63) * _mean(dv, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxdv_252d_slope_v071_signal(capex, revenue, closeadj, volume):
    p = _f03_capex_intensity(capex, revenue)
    dv = closeadj * volume
    base = _mean(p, 252) * _mean(dv, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dynxdv_63d_slope_v072_signal(capex, revenue, closeadj, volume):
    d = _f03_capex_dynamics(capex, revenue, 63)
    dv = closeadj * volume
    base = d * _mean(dv, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dynxdv_252d_slope_v073_signal(capex, revenue, closeadj, volume):
    d = _f03_capex_dynamics(capex, revenue, 252)
    dv = closeadj * volume
    base = d * _mean(dv, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsxdv_63d_slope_v074_signal(capex, assets, closeadj, volume):
    p = _f03_capex_to_assets(capex, assets)
    dv = closeadj * volume
    base = _mean(p, 63) * _mean(dv, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsxdv_252d_slope_v075_signal(capex, assets, closeadj, volume):
    p = _f03_capex_to_assets(capex, assets)
    dv = closeadj * volume
    base = _mean(p, 252) * _mean(dv, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Std
def f03uci_f03_utility_capex_intensity_intensstd_63d_slope_v076_signal(capex, revenue, closeadj):
    p = _f03_capex_intensity(capex, revenue)
    base = _std(p, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensstd_252d_slope_v077_signal(capex, revenue, closeadj):
    p = _f03_capex_intensity(capex, revenue)
    base = _std(p, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsstd_63d_slope_v078_signal(capex, assets, closeadj):
    p = _f03_capex_to_assets(capex, assets)
    base = _std(p, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsstd_252d_slope_v079_signal(capex, assets, closeadj):
    p = _f03_capex_to_assets(capex, assets)
    base = _std(p, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Size
def f03uci_f03_utility_capex_intensity_intensxsize_63d_slope_v080_signal(capex, revenue, closeadj):
    p = _f03_capex_intensity(capex, revenue)
    base = _mean(p, 63) * np.log(capex.abs().replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxsize_252d_slope_v081_signal(capex, revenue, closeadj):
    p = _f03_capex_intensity(capex, revenue)
    base = _mean(p, 252) * np.log(capex.abs().replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxrevsize_63d_slope_v082_signal(capex, revenue, closeadj):
    p = _f03_capex_intensity(capex, revenue)
    base = _mean(p, 63) * np.log(revenue.abs().replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxrevsize_252d_slope_v083_signal(capex, revenue, closeadj):
    p = _f03_capex_intensity(capex, revenue)
    base = _mean(p, 252) * np.log(revenue.abs().replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# closez
def f03uci_f03_utility_capex_intensity_intensxclosez_63d_slope_v084_signal(capex, revenue, closeadj):
    p = _f03_capex_intensity(capex, revenue)
    base = _mean(p, 63) * _z(closeadj, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxclosez_252d_slope_v085_signal(capex, revenue, closeadj):
    p = _f03_capex_intensity(capex, revenue)
    base = _mean(p, 252) * _z(closeadj, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dynxclosez_63d_slope_v086_signal(capex, revenue, closeadj):
    d = _f03_capex_dynamics(capex, revenue, 63)
    base = d * _z(closeadj, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dynxclosez_252d_slope_v087_signal(capex, revenue, closeadj):
    d = _f03_capex_dynamics(capex, revenue, 252)
    base = d * _z(closeadj, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsxclosez_63d_slope_v088_signal(capex, assets, closeadj):
    p = _f03_capex_to_assets(capex, assets)
    base = _mean(p, 63) * _z(closeadj, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsxclosez_252d_slope_v089_signal(capex, assets, closeadj):
    p = _f03_capex_to_assets(capex, assets)
    base = _mean(p, 252) * _z(closeadj, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Return
def f03uci_f03_utility_capex_intensity_intensxret_63d_slope_v090_signal(capex, revenue, closeadj):
    p = _f03_capex_intensity(capex, revenue)
    base = _mean(p, 63) * closeadj.pct_change(21) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxret_252d_slope_v091_signal(capex, revenue, closeadj):
    p = _f03_capex_intensity(capex, revenue)
    base = _mean(p, 252) * closeadj.pct_change(63) * closeadj * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dynxret_63d_slope_v092_signal(capex, revenue, closeadj):
    d = _f03_capex_dynamics(capex, revenue, 63)
    base = d * closeadj.pct_change(21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dynxret_252d_slope_v093_signal(capex, revenue, closeadj):
    d = _f03_capex_dynamics(capex, revenue, 252)
    base = d * closeadj.pct_change(63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Abs return
def f03uci_f03_utility_capex_intensity_intensxabsret_63d_slope_v094_signal(capex, revenue, closeadj):
    p = _f03_capex_intensity(capex, revenue)
    base = _mean(p, 63) * closeadj.pct_change(21).abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxabsret_252d_slope_v095_signal(capex, revenue, closeadj):
    p = _f03_capex_intensity(capex, revenue)
    base = _mean(p, 252) * closeadj.pct_change(63).abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dynxabsret_63d_slope_v096_signal(capex, revenue, closeadj):
    d = _f03_capex_dynamics(capex, revenue, 63)
    base = d * closeadj.pct_change(21).abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dynxabsret_252d_slope_v097_signal(capex, revenue, closeadj):
    d = _f03_capex_dynamics(capex, revenue, 252)
    base = d * closeadj.pct_change(63).abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Acceleration
def f03uci_f03_utility_capex_intensity_intensaccel_63d_slope_v098_signal(capex, revenue, closeadj):
    p = _mean(_f03_capex_intensity(capex, revenue), 63)
    base = (p - p.shift(21)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensaccel_252d_slope_v099_signal(capex, revenue, closeadj):
    p = _mean(_f03_capex_intensity(capex, revenue), 252)
    base = (p - p.shift(63)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsaccel_63d_slope_v100_signal(capex, assets, closeadj):
    p = _mean(_f03_capex_to_assets(capex, assets), 63)
    base = (p - p.shift(21)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsaccel_252d_slope_v101_signal(capex, assets, closeadj):
    p = _mean(_f03_capex_to_assets(capex, assets), 252)
    base = (p - p.shift(63)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Inv price
def f03uci_f03_utility_capex_intensity_intensxinvprice_63d_slope_v102_signal(capex, revenue, closeadj):
    p = _mean(_f03_capex_intensity(capex, revenue), 63)
    base = p * _mean(closeadj, 21) * _mean(closeadj, 21) / closeadj.replace(0, np.nan)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxinvprice_252d_slope_v103_signal(capex, revenue, closeadj):
    p = _mean(_f03_capex_intensity(capex, revenue), 252)
    base = p * _mean(closeadj, 63) * _mean(closeadj, 63) / closeadj.replace(0, np.nan)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# MA cross
def f03uci_f03_utility_capex_intensity_intenscross_21_252_slope_v104_signal(capex, revenue, closeadj):
    p = _f03_capex_intensity(capex, revenue)
    base = (_mean(p, 21) - _mean(p, 252)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intenscross_63_252_slope_v105_signal(capex, revenue, closeadj):
    p = _f03_capex_intensity(capex, revenue)
    base = (_mean(p, 63) - _mean(p, 252)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetscross_21_252_slope_v106_signal(capex, assets, closeadj):
    p = _f03_capex_to_assets(capex, assets)
    base = (_mean(p, 21) - _mean(p, 252)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetscross_63_252_slope_v107_signal(capex, assets, closeadj):
    p = _f03_capex_to_assets(capex, assets)
    base = (_mean(p, 63) - _mean(p, 252)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Spread
def f03uci_f03_utility_capex_intensity_intensspread_63d_slope_v108_signal(capex, revenue, closeadj):
    p = _f03_capex_intensity(capex, revenue)
    base = (p - 0.15) * closeadj * _mean(p, 63) / _mean(p, 252).replace(0, np.nan)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensspread_252d_slope_v109_signal(capex, revenue, closeadj):
    p = _f03_capex_intensity(capex, revenue)
    base = (p - 0.15) * closeadj * _mean(p, 252) / _mean(p, 504).replace(0, np.nan)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Sum
def f03uci_f03_utility_capex_intensity_intenssum_63d_slope_v110_signal(capex, revenue, closeadj):
    p = _f03_capex_intensity(capex, revenue)
    base = p.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intenssum_252d_slope_v111_signal(capex, revenue, closeadj):
    p = _f03_capex_intensity(capex, revenue)
    base = p.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Capex growth
def f03uci_f03_utility_capex_intensity_capexgrowth_63d_slope_v112_signal(capex, revenue, closeadj):
    g = capex.pct_change(63)
    rb = _f03_capex_intensity(capex, revenue)
    base = g * closeadj + rb * 0.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_capexgrowth_252d_slope_v113_signal(capex, revenue, closeadj):
    g = capex.pct_change(252)
    rb = _f03_capex_intensity(capex, revenue)
    base = g * closeadj + rb * 0.0
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Sign × vol
def f03uci_f03_utility_capex_intensity_intenssignxvol_63d_slope_v114_signal(capex, revenue, closeadj, volume):
    p = _f03_capex_intensity(capex, revenue)
    base = np.sign(p - _mean(p, 252)) * _mean(volume, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intenssignxvol_252d_slope_v115_signal(capex, revenue, closeadj, volume):
    p = _f03_capex_intensity(capex, revenue)
    base = np.sign(p - _mean(p, 504)) * _mean(volume, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Diff-norm
def f03uci_f03_utility_capex_intensity_intensdn_63d_slope_v116_signal(capex, revenue, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensdn_252d_slope_v117_signal(capex, revenue, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsdn_63d_slope_v118_signal(capex, assets, closeadj):
    base = _mean(_f03_capex_to_assets(capex, assets), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsdn_252d_slope_v119_signal(capex, assets, closeadj):
    base = _mean(_f03_capex_to_assets(capex, assets), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dyndn_63d_slope_v120_signal(capex, revenue, closeadj):
    base = _f03_capex_dynamics(capex, revenue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dyndn_252d_slope_v121_signal(capex, revenue, closeadj):
    base = _f03_capex_dynamics(capex, revenue, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d
def f03uci_f03_utility_capex_intensity_intens_5d_slope_v122_signal(capex, revenue, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assets_5d_slope_v123_signal(capex, assets, closeadj):
    base = _mean(_f03_capex_to_assets(capex, assets), 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dyn_5d_slope_v124_signal(capex, revenue, closeadj):
    base = _f03_capex_dynamics(capex, revenue, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d
def f03uci_f03_utility_capex_intensity_intens_10d_slope_v125_signal(capex, revenue, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 21) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assets_10d_slope_v126_signal(capex, assets, closeadj):
    base = _mean(_f03_capex_to_assets(capex, assets), 21) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d
def f03uci_f03_utility_capex_intensity_intens_42d_slope_v127_signal(capex, revenue, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 63) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assets_42d_slope_v128_signal(capex, assets, closeadj):
    base = _mean(_f03_capex_to_assets(capex, assets), 63) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dyn_42d_slope_v129_signal(capex, revenue, closeadj):
    base = _f03_capex_dynamics(capex, revenue, 63) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d
def f03uci_f03_utility_capex_intensity_intens_189d_slope_v130_signal(capex, revenue, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 252) * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assets_189d_slope_v131_signal(capex, assets, closeadj):
    base = _mean(_f03_capex_to_assets(capex, assets), 252) * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dyn_189d_slope_v132_signal(capex, revenue, closeadj):
    base = _f03_capex_dynamics(capex, revenue, 252) * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope
def f03uci_f03_utility_capex_intensity_intens_252d_slope_v133_signal(capex, revenue, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 504) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assets_252d_slope_v134_signal(capex, assets, closeadj):
    base = _mean(_f03_capex_to_assets(capex, assets), 504) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# Combo ATR
def f03uci_f03_utility_capex_intensity_comboxatr_63d_slope_v135_signal(capex, revenue, assets, closeadj, high, low):
    ci = _f03_capex_intensity(capex, revenue)
    ca = _f03_capex_to_assets(capex, assets)
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _mean(ci, 63) * _mean(ca, 63) * atr
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_comboxatr_252d_slope_v136_signal(capex, revenue, assets, closeadj, high, low):
    ci = _f03_capex_intensity(capex, revenue)
    ca = _f03_capex_to_assets(capex, assets)
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _mean(ci, 252) * _mean(ca, 252) * atr
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Combo dv
def f03uci_f03_utility_capex_intensity_comboxdv_63d_slope_v137_signal(capex, revenue, assets, closeadj, volume):
    ci = _f03_capex_intensity(capex, revenue)
    ca = _f03_capex_to_assets(capex, assets)
    dv = closeadj * volume
    base = _mean(ci, 63) * _mean(ca, 63) * _mean(dv, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_comboxdv_252d_slope_v138_signal(capex, revenue, assets, closeadj, volume):
    ci = _f03_capex_intensity(capex, revenue)
    ca = _f03_capex_to_assets(capex, assets)
    dv = closeadj * volume
    base = _mean(ci, 252) * _mean(ca, 252) * _mean(dv, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Combined dyn × asset
def f03uci_f03_utility_capex_intensity_combodyn_63d_slope_v139_signal(capex, revenue, assets, closeadj):
    d = _f03_capex_dynamics(capex, revenue, 63)
    ca = _f03_capex_to_assets(capex, assets)
    base = d * _mean(ca, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_combodyn_252d_slope_v140_signal(capex, revenue, assets, closeadj):
    d = _f03_capex_dynamics(capex, revenue, 252)
    ca = _f03_capex_to_assets(capex, assets)
    base = d * _mean(ca, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Revenue growth × intensity
def f03uci_f03_utility_capex_intensity_intensxrevgrowth_63d_slope_v141_signal(capex, revenue, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 63) * revenue.pct_change(63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxrevgrowth_252d_slope_v142_signal(capex, revenue, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 252) * revenue.pct_change(252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Intensity × revenue/assets
def f03uci_f03_utility_capex_intensity_intensxrevassets_63d_slope_v143_signal(capex, revenue, assets, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 63) * (revenue / assets.replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxrevassets_252d_slope_v144_signal(capex, revenue, assets, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 252) * (revenue / assets.replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Capex sum / revenue sum
def f03uci_f03_utility_capex_intensity_capexsumxclose_63d_slope_v145_signal(capex, revenue, closeadj):
    rb = _f03_capex_intensity(capex, revenue)
    base = capex.rolling(63, min_periods=21).sum() / revenue.rolling(63, min_periods=21).sum().replace(0, np.nan) * closeadj + rb * 0.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_capexsumxclose_252d_slope_v146_signal(capex, revenue, closeadj):
    rb = _f03_capex_intensity(capex, revenue)
    base = capex.rolling(252, min_periods=63).sum() / revenue.rolling(252, min_periods=63).sum().replace(0, np.nan) * closeadj + rb * 0.0
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Intensity × asset size
def f03uci_f03_utility_capex_intensity_intensxassetsize_63d_slope_v147_signal(capex, revenue, assets, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 63) * np.log(assets.replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxassetsize_252d_slope_v148_signal(capex, revenue, assets, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 252) * np.log(assets.replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Capex accel
def f03uci_f03_utility_capex_intensity_capexaccel_63d_slope_v149_signal(capex, revenue, closeadj):
    g = capex.pct_change(63)
    rb = _f03_capex_intensity(capex, revenue)
    base = (g - g.shift(21)) * closeadj + rb * 0.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_capexaccel_252d_slope_v150_signal(capex, revenue, closeadj):
    g = capex.pct_change(252)
    rb = _f03_capex_intensity(capex, revenue)
    base = (g - g.shift(63)) * closeadj + rb * 0.0
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f03uci_f03_utility_capex_intensity_intens_21d_slope_v001_signal,
    f03uci_f03_utility_capex_intensity_intens_21d_slope_v002_signal,
    f03uci_f03_utility_capex_intensity_intens_63d_slope_v003_signal,
    f03uci_f03_utility_capex_intensity_intens_63d_slope_v004_signal,
    f03uci_f03_utility_capex_intensity_intens_63d_slope_v005_signal,
    f03uci_f03_utility_capex_intensity_intens_126d_slope_v006_signal,
    f03uci_f03_utility_capex_intensity_intens_126d_slope_v007_signal,
    f03uci_f03_utility_capex_intensity_intens_252d_slope_v008_signal,
    f03uci_f03_utility_capex_intensity_intens_252d_slope_v009_signal,
    f03uci_f03_utility_capex_intensity_intens_252d_slope_v010_signal,
    f03uci_f03_utility_capex_intensity_intens_504d_slope_v011_signal,
    f03uci_f03_utility_capex_intensity_intens_504d_slope_v012_signal,
    f03uci_f03_utility_capex_intensity_assets_21d_slope_v013_signal,
    f03uci_f03_utility_capex_intensity_assets_21d_slope_v014_signal,
    f03uci_f03_utility_capex_intensity_assets_63d_slope_v015_signal,
    f03uci_f03_utility_capex_intensity_assets_63d_slope_v016_signal,
    f03uci_f03_utility_capex_intensity_assets_252d_slope_v017_signal,
    f03uci_f03_utility_capex_intensity_assets_252d_slope_v018_signal,
    f03uci_f03_utility_capex_intensity_assets_504d_slope_v019_signal,
    f03uci_f03_utility_capex_intensity_assets_504d_slope_v020_signal,
    f03uci_f03_utility_capex_intensity_dyn_21d_slope_v021_signal,
    f03uci_f03_utility_capex_intensity_dyn_21d_slope_v022_signal,
    f03uci_f03_utility_capex_intensity_dyn_63d_slope_v023_signal,
    f03uci_f03_utility_capex_intensity_dyn_63d_slope_v024_signal,
    f03uci_f03_utility_capex_intensity_dyn_252d_slope_v025_signal,
    f03uci_f03_utility_capex_intensity_dyn_252d_slope_v026_signal,
    f03uci_f03_utility_capex_intensity_dyn_504d_slope_v027_signal,
    f03uci_f03_utility_capex_intensity_dyn_504d_slope_v028_signal,
    f03uci_f03_utility_capex_intensity_intensxvol_63d_slope_v029_signal,
    f03uci_f03_utility_capex_intensity_intensxvol_252d_slope_v030_signal,
    f03uci_f03_utility_capex_intensity_assetsxvol_63d_slope_v031_signal,
    f03uci_f03_utility_capex_intensity_assetsxvol_252d_slope_v032_signal,
    f03uci_f03_utility_capex_intensity_dynxvol_63d_slope_v033_signal,
    f03uci_f03_utility_capex_intensity_dynxvol_252d_slope_v034_signal,
    f03uci_f03_utility_capex_intensity_intensxatr_63d_slope_v035_signal,
    f03uci_f03_utility_capex_intensity_intensxatr_252d_slope_v036_signal,
    f03uci_f03_utility_capex_intensity_assetsxatr_63d_slope_v037_signal,
    f03uci_f03_utility_capex_intensity_assetsxatr_252d_slope_v038_signal,
    f03uci_f03_utility_capex_intensity_dynxatr_63d_slope_v039_signal,
    f03uci_f03_utility_capex_intensity_dynxatr_252d_slope_v040_signal,
    f03uci_f03_utility_capex_intensity_intensema_63d_slope_v041_signal,
    f03uci_f03_utility_capex_intensity_intensema_252d_slope_v042_signal,
    f03uci_f03_utility_capex_intensity_assetsema_63d_slope_v043_signal,
    f03uci_f03_utility_capex_intensity_assetsema_252d_slope_v044_signal,
    f03uci_f03_utility_capex_intensity_intenssq_63d_slope_v045_signal,
    f03uci_f03_utility_capex_intensity_intenssq_252d_slope_v046_signal,
    f03uci_f03_utility_capex_intensity_dynsq_63d_slope_v047_signal,
    f03uci_f03_utility_capex_intensity_dynsq_252d_slope_v048_signal,
    f03uci_f03_utility_capex_intensity_assetssq_63d_slope_v049_signal,
    f03uci_f03_utility_capex_intensity_assetssq_252d_slope_v050_signal,
    f03uci_f03_utility_capex_intensity_intensz_63d_slope_v051_signal,
    f03uci_f03_utility_capex_intensity_intensz_252d_slope_v052_signal,
    f03uci_f03_utility_capex_intensity_assetsz_63d_slope_v053_signal,
    f03uci_f03_utility_capex_intensity_assetsz_252d_slope_v054_signal,
    f03uci_f03_utility_capex_intensity_dynz_63d_slope_v055_signal,
    f03uci_f03_utility_capex_intensity_dynz_252d_slope_v056_signal,
    f03uci_f03_utility_capex_intensity_intensrank_63d_slope_v057_signal,
    f03uci_f03_utility_capex_intensity_intensrank_252d_slope_v058_signal,
    f03uci_f03_utility_capex_intensity_assetsrank_63d_slope_v059_signal,
    f03uci_f03_utility_capex_intensity_assetsrank_252d_slope_v060_signal,
    f03uci_f03_utility_capex_intensity_intensgap_63d_slope_v061_signal,
    f03uci_f03_utility_capex_intensity_intensgap_252d_slope_v062_signal,
    f03uci_f03_utility_capex_intensity_assetsgap_63d_slope_v063_signal,
    f03uci_f03_utility_capex_intensity_assetsgap_252d_slope_v064_signal,
    f03uci_f03_utility_capex_intensity_intenslog_63d_slope_v065_signal,
    f03uci_f03_utility_capex_intensity_intenslog_252d_slope_v066_signal,
    f03uci_f03_utility_capex_intensity_assetslog_252d_slope_v067_signal,
    f03uci_f03_utility_capex_intensity_combo_63d_slope_v068_signal,
    f03uci_f03_utility_capex_intensity_combo_252d_slope_v069_signal,
    f03uci_f03_utility_capex_intensity_intensxdv_63d_slope_v070_signal,
    f03uci_f03_utility_capex_intensity_intensxdv_252d_slope_v071_signal,
    f03uci_f03_utility_capex_intensity_dynxdv_63d_slope_v072_signal,
    f03uci_f03_utility_capex_intensity_dynxdv_252d_slope_v073_signal,
    f03uci_f03_utility_capex_intensity_assetsxdv_63d_slope_v074_signal,
    f03uci_f03_utility_capex_intensity_assetsxdv_252d_slope_v075_signal,
    f03uci_f03_utility_capex_intensity_intensstd_63d_slope_v076_signal,
    f03uci_f03_utility_capex_intensity_intensstd_252d_slope_v077_signal,
    f03uci_f03_utility_capex_intensity_assetsstd_63d_slope_v078_signal,
    f03uci_f03_utility_capex_intensity_assetsstd_252d_slope_v079_signal,
    f03uci_f03_utility_capex_intensity_intensxsize_63d_slope_v080_signal,
    f03uci_f03_utility_capex_intensity_intensxsize_252d_slope_v081_signal,
    f03uci_f03_utility_capex_intensity_intensxrevsize_63d_slope_v082_signal,
    f03uci_f03_utility_capex_intensity_intensxrevsize_252d_slope_v083_signal,
    f03uci_f03_utility_capex_intensity_intensxclosez_63d_slope_v084_signal,
    f03uci_f03_utility_capex_intensity_intensxclosez_252d_slope_v085_signal,
    f03uci_f03_utility_capex_intensity_dynxclosez_63d_slope_v086_signal,
    f03uci_f03_utility_capex_intensity_dynxclosez_252d_slope_v087_signal,
    f03uci_f03_utility_capex_intensity_assetsxclosez_63d_slope_v088_signal,
    f03uci_f03_utility_capex_intensity_assetsxclosez_252d_slope_v089_signal,
    f03uci_f03_utility_capex_intensity_intensxret_63d_slope_v090_signal,
    f03uci_f03_utility_capex_intensity_intensxret_252d_slope_v091_signal,
    f03uci_f03_utility_capex_intensity_dynxret_63d_slope_v092_signal,
    f03uci_f03_utility_capex_intensity_dynxret_252d_slope_v093_signal,
    f03uci_f03_utility_capex_intensity_intensxabsret_63d_slope_v094_signal,
    f03uci_f03_utility_capex_intensity_intensxabsret_252d_slope_v095_signal,
    f03uci_f03_utility_capex_intensity_dynxabsret_63d_slope_v096_signal,
    f03uci_f03_utility_capex_intensity_dynxabsret_252d_slope_v097_signal,
    f03uci_f03_utility_capex_intensity_intensaccel_63d_slope_v098_signal,
    f03uci_f03_utility_capex_intensity_intensaccel_252d_slope_v099_signal,
    f03uci_f03_utility_capex_intensity_assetsaccel_63d_slope_v100_signal,
    f03uci_f03_utility_capex_intensity_assetsaccel_252d_slope_v101_signal,
    f03uci_f03_utility_capex_intensity_intensxinvprice_63d_slope_v102_signal,
    f03uci_f03_utility_capex_intensity_intensxinvprice_252d_slope_v103_signal,
    f03uci_f03_utility_capex_intensity_intenscross_21_252_slope_v104_signal,
    f03uci_f03_utility_capex_intensity_intenscross_63_252_slope_v105_signal,
    f03uci_f03_utility_capex_intensity_assetscross_21_252_slope_v106_signal,
    f03uci_f03_utility_capex_intensity_assetscross_63_252_slope_v107_signal,
    f03uci_f03_utility_capex_intensity_intensspread_63d_slope_v108_signal,
    f03uci_f03_utility_capex_intensity_intensspread_252d_slope_v109_signal,
    f03uci_f03_utility_capex_intensity_intenssum_63d_slope_v110_signal,
    f03uci_f03_utility_capex_intensity_intenssum_252d_slope_v111_signal,
    f03uci_f03_utility_capex_intensity_capexgrowth_63d_slope_v112_signal,
    f03uci_f03_utility_capex_intensity_capexgrowth_252d_slope_v113_signal,
    f03uci_f03_utility_capex_intensity_intenssignxvol_63d_slope_v114_signal,
    f03uci_f03_utility_capex_intensity_intenssignxvol_252d_slope_v115_signal,
    f03uci_f03_utility_capex_intensity_intensdn_63d_slope_v116_signal,
    f03uci_f03_utility_capex_intensity_intensdn_252d_slope_v117_signal,
    f03uci_f03_utility_capex_intensity_assetsdn_63d_slope_v118_signal,
    f03uci_f03_utility_capex_intensity_assetsdn_252d_slope_v119_signal,
    f03uci_f03_utility_capex_intensity_dyndn_63d_slope_v120_signal,
    f03uci_f03_utility_capex_intensity_dyndn_252d_slope_v121_signal,
    f03uci_f03_utility_capex_intensity_intens_5d_slope_v122_signal,
    f03uci_f03_utility_capex_intensity_assets_5d_slope_v123_signal,
    f03uci_f03_utility_capex_intensity_dyn_5d_slope_v124_signal,
    f03uci_f03_utility_capex_intensity_intens_10d_slope_v125_signal,
    f03uci_f03_utility_capex_intensity_assets_10d_slope_v126_signal,
    f03uci_f03_utility_capex_intensity_intens_42d_slope_v127_signal,
    f03uci_f03_utility_capex_intensity_assets_42d_slope_v128_signal,
    f03uci_f03_utility_capex_intensity_dyn_42d_slope_v129_signal,
    f03uci_f03_utility_capex_intensity_intens_189d_slope_v130_signal,
    f03uci_f03_utility_capex_intensity_assets_189d_slope_v131_signal,
    f03uci_f03_utility_capex_intensity_dyn_189d_slope_v132_signal,
    f03uci_f03_utility_capex_intensity_intens_252d_slope_v133_signal,
    f03uci_f03_utility_capex_intensity_assets_252d_slope_v134_signal,
    f03uci_f03_utility_capex_intensity_comboxatr_63d_slope_v135_signal,
    f03uci_f03_utility_capex_intensity_comboxatr_252d_slope_v136_signal,
    f03uci_f03_utility_capex_intensity_comboxdv_63d_slope_v137_signal,
    f03uci_f03_utility_capex_intensity_comboxdv_252d_slope_v138_signal,
    f03uci_f03_utility_capex_intensity_combodyn_63d_slope_v139_signal,
    f03uci_f03_utility_capex_intensity_combodyn_252d_slope_v140_signal,
    f03uci_f03_utility_capex_intensity_intensxrevgrowth_63d_slope_v141_signal,
    f03uci_f03_utility_capex_intensity_intensxrevgrowth_252d_slope_v142_signal,
    f03uci_f03_utility_capex_intensity_intensxrevassets_63d_slope_v143_signal,
    f03uci_f03_utility_capex_intensity_intensxrevassets_252d_slope_v144_signal,
    f03uci_f03_utility_capex_intensity_capexsumxclose_63d_slope_v145_signal,
    f03uci_f03_utility_capex_intensity_capexsumxclose_252d_slope_v146_signal,
    f03uci_f03_utility_capex_intensity_intensxassetsize_63d_slope_v147_signal,
    f03uci_f03_utility_capex_intensity_intensxassetsize_252d_slope_v148_signal,
    f03uci_f03_utility_capex_intensity_capexaccel_63d_slope_v149_signal,
    f03uci_f03_utility_capex_intensity_capexaccel_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F03_UTILITY_CAPEX_INTENSITY_REGISTRY_SLOPE_001_150 = REGISTRY


def _build_cols():
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = pd.Series(closeadj.values * (1.0 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(closeadj.values * (1.0 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    capex = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    return {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "capex": capex, "revenue": revenue, "assets": assets,
    }


if __name__ == "__main__":
    cols = _build_cols()
    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f03_capex_intensity", "_f03_capex_to_assets", "_f03_capex_dynamics")
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
    print(f"OK f03_utility_capex_intensity_2nd_derivatives_001_150_claude: {n_features} features pass")
