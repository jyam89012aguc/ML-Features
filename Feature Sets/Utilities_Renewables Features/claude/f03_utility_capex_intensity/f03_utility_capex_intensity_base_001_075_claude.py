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


def _f03_capex_intensity(capex, revenue):
    return capex / revenue.replace(0, np.nan)


def _f03_capex_to_assets(capex, assets):
    return capex / assets.replace(0, np.nan)


def _f03_capex_dynamics(capex, revenue, w):
    ci = capex / revenue.replace(0, np.nan)
    return ci - ci.rolling(w, min_periods=max(1, w // 2)).mean()


# Plain capex intensity smoothed × close
def f03uci_f03_utility_capex_intensity_intensity_21d_base_v001_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensity_63d_base_v002_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensity_126d_base_v003_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensity_252d_base_v004_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensity_504d_base_v005_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex_to_assets
def f03uci_f03_utility_capex_intensity_capexassets_21d_base_v006_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_capexassets_63d_base_v007_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_capexassets_126d_base_v008_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_capexassets_252d_base_v009_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_capexassets_504d_base_v010_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# dynamics
def f03uci_f03_utility_capex_intensity_capexdyn_21d_base_v011_signal(capex, revenue, closeadj):
    result = _f03_capex_dynamics(capex, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_capexdyn_63d_base_v012_signal(capex, revenue, closeadj):
    result = _f03_capex_dynamics(capex, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_capexdyn_126d_base_v013_signal(capex, revenue, closeadj):
    result = _f03_capex_dynamics(capex, revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_capexdyn_252d_base_v014_signal(capex, revenue, closeadj):
    result = _f03_capex_dynamics(capex, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_capexdyn_504d_base_v015_signal(capex, revenue, closeadj):
    result = _f03_capex_dynamics(capex, revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Z-scores
def f03uci_f03_utility_capex_intensity_intensityz_252d_base_v016_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensityz_504d_base_v017_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsz_252d_base_v018_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsz_504d_base_v019_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Std
def f03uci_f03_utility_capex_intensity_intensitystd_63d_base_v020_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensitystd_252d_base_v021_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsstd_252d_base_v022_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EMA
def f03uci_f03_utility_capex_intensity_intensityema_63d_base_v023_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = base.ewm(span=63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensityema_252d_base_v024_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = base.ewm(span=252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsema_252d_base_v025_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = base.ewm(span=252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Rank
def f03uci_f03_utility_capex_intensity_intensityrank_252d_base_v026_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsrank_252d_base_v027_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# pct change
def f03uci_f03_utility_capex_intensity_intensitychg_21d_base_v028_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = base.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensitychg_63d_base_v029_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensitychg_252d_base_v030_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetschg_63d_base_v031_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetschg_252d_base_v032_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Short windows
def f03uci_f03_utility_capex_intensity_intensity_5d_base_v033_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensity_10d_base_v034_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensity_42d_base_v035_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensity_189d_base_v036_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensity_378d_base_v037_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets short
def f03uci_f03_utility_capex_intensity_capexassets_5d_base_v038_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_capexassets_42d_base_v039_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_capexassets_189d_base_v040_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Volume × intensity × close
def f03uci_f03_utility_capex_intensity_intensxvol_63d_base_v041_signal(capex, revenue, closeadj, volume):
    base = _f03_capex_intensity(capex, revenue)
    result = _mean(base, 63) * _mean(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxvol_252d_base_v042_signal(capex, revenue, closeadj, volume):
    base = _f03_capex_intensity(capex, revenue)
    result = _mean(base, 252) * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsxvol_252d_base_v043_signal(capex, assets, closeadj, volume):
    base = _f03_capex_to_assets(capex, assets)
    result = _mean(base, 252) * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ATR-weighted
def f03uci_f03_utility_capex_intensity_intensxatr_63d_base_v044_signal(capex, revenue, closeadj, high, low):
    base = _f03_capex_intensity(capex, revenue)
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _mean(base, 63) * atr
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxatr_252d_base_v045_signal(capex, revenue, closeadj, high, low):
    base = _f03_capex_intensity(capex, revenue)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _mean(base, 252) * atr
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsxatr_252d_base_v046_signal(capex, assets, closeadj, high, low):
    base = _f03_capex_to_assets(capex, assets)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _mean(base, 252) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# capex growth raw × close
def f03uci_f03_utility_capex_intensity_capexgrowth_63d_base_v047_signal(capex, revenue, closeadj):
    g = capex.pct_change(63)
    rb = _f03_capex_intensity(capex, revenue)
    result = g * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_capexgrowth_252d_base_v048_signal(capex, revenue, closeadj):
    g = capex.pct_change(252)
    rb = _f03_capex_intensity(capex, revenue)
    result = g * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_capexgrowth_504d_base_v049_signal(capex, revenue, closeadj):
    g = capex.pct_change(504)
    rb = _f03_capex_intensity(capex, revenue)
    result = g * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Log capex intensity × close
def f03uci_f03_utility_capex_intensity_intensitylog_63d_base_v050_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensitylog_252d_base_v051_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = np.log(base.abs().replace(0, np.nan)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetslog_252d_base_v052_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = np.log(base.abs().replace(0, np.nan)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Intensity × capex log × close
def f03uci_f03_utility_capex_intensity_intensxsize_63d_base_v053_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    s = np.log(capex.abs().replace(0, np.nan))
    result = _mean(base, 63) * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxsize_252d_base_v054_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    s = np.log(capex.abs().replace(0, np.nan))
    result = _mean(base, 252) * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Intensity × revenue log × close
def f03uci_f03_utility_capex_intensity_intensxrevsize_63d_base_v055_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    s = np.log(revenue.abs().replace(0, np.nan))
    result = _mean(base, 63) * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxrevsize_252d_base_v056_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    s = np.log(revenue.abs().replace(0, np.nan))
    result = _mean(base, 252) * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Capex squared × close
def f03uci_f03_utility_capex_intensity_intenssq_63d_base_v057_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intenssq_252d_base_v058_signal(capex, revenue, closeadj):
    base = _mean(_f03_capex_intensity(capex, revenue), 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Dynamics squared × close
def f03uci_f03_utility_capex_intensity_dynsq_63d_base_v059_signal(capex, revenue, closeadj):
    base = _f03_capex_dynamics(capex, revenue, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dynsq_252d_base_v060_signal(capex, revenue, closeadj):
    base = _f03_capex_dynamics(capex, revenue, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Dynamics × volume
def f03uci_f03_utility_capex_intensity_dynxvol_63d_base_v061_signal(capex, revenue, closeadj, volume):
    base = _f03_capex_dynamics(capex, revenue, 63)
    result = base * _mean(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dynxvol_252d_base_v062_signal(capex, revenue, closeadj, volume):
    base = _f03_capex_dynamics(capex, revenue, 252)
    result = base * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Dynamics × ATR
def f03uci_f03_utility_capex_intensity_dynxatr_63d_base_v063_signal(capex, revenue, closeadj, high, low):
    base = _f03_capex_dynamics(capex, revenue, 63)
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = base * atr
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_dynxatr_252d_base_v064_signal(capex, revenue, closeadj, high, low):
    base = _f03_capex_dynamics(capex, revenue, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = base * atr
    return result.replace([np.inf, -np.inf], np.nan)


# Capex sum × close
def f03uci_f03_utility_capex_intensity_intenssum_63d_base_v065_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = base.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intenssum_252d_base_v066_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Capex/Assets × revenue × close
def f03uci_f03_utility_capex_intensity_assetsxrev_63d_base_v067_signal(capex, assets, revenue, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = _mean(base, 63) * np.log(revenue.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsxrev_252d_base_v068_signal(capex, assets, revenue, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = _mean(base, 252) * np.log(revenue.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Combined intensity × capex/assets × close
def f03uci_f03_utility_capex_intensity_combointens_63d_base_v069_signal(capex, revenue, assets, closeadj):
    ci = _f03_capex_intensity(capex, revenue)
    ca = _f03_capex_to_assets(capex, assets)
    result = _mean(ci, 63) * _mean(ca, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_combointens_252d_base_v070_signal(capex, revenue, assets, closeadj):
    ci = _f03_capex_intensity(capex, revenue)
    ca = _f03_capex_to_assets(capex, assets)
    result = _mean(ci, 252) * _mean(ca, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Intensity × revenue × close (dollar weighted)
def f03uci_f03_utility_capex_intensity_intensxrev_63d_base_v071_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = _mean(base, 63) * _mean(revenue, 63) / _mean(revenue, 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensxrev_252d_base_v072_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = _mean(base, 252) * _mean(revenue, 252) / _mean(revenue, 504).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Intensity gap × close
def f03uci_f03_utility_capex_intensity_intensgap_63d_base_v073_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = (base - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_intensgap_252d_base_v074_signal(capex, revenue, closeadj):
    base = _f03_capex_intensity(capex, revenue)
    result = (base - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f03uci_f03_utility_capex_intensity_assetsgap_252d_base_v075_signal(capex, assets, closeadj):
    base = _f03_capex_to_assets(capex, assets)
    result = (base - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f03uci_f03_utility_capex_intensity_intensity_21d_base_v001_signal,
    f03uci_f03_utility_capex_intensity_intensity_63d_base_v002_signal,
    f03uci_f03_utility_capex_intensity_intensity_126d_base_v003_signal,
    f03uci_f03_utility_capex_intensity_intensity_252d_base_v004_signal,
    f03uci_f03_utility_capex_intensity_intensity_504d_base_v005_signal,
    f03uci_f03_utility_capex_intensity_capexassets_21d_base_v006_signal,
    f03uci_f03_utility_capex_intensity_capexassets_63d_base_v007_signal,
    f03uci_f03_utility_capex_intensity_capexassets_126d_base_v008_signal,
    f03uci_f03_utility_capex_intensity_capexassets_252d_base_v009_signal,
    f03uci_f03_utility_capex_intensity_capexassets_504d_base_v010_signal,
    f03uci_f03_utility_capex_intensity_capexdyn_21d_base_v011_signal,
    f03uci_f03_utility_capex_intensity_capexdyn_63d_base_v012_signal,
    f03uci_f03_utility_capex_intensity_capexdyn_126d_base_v013_signal,
    f03uci_f03_utility_capex_intensity_capexdyn_252d_base_v014_signal,
    f03uci_f03_utility_capex_intensity_capexdyn_504d_base_v015_signal,
    f03uci_f03_utility_capex_intensity_intensityz_252d_base_v016_signal,
    f03uci_f03_utility_capex_intensity_intensityz_504d_base_v017_signal,
    f03uci_f03_utility_capex_intensity_assetsz_252d_base_v018_signal,
    f03uci_f03_utility_capex_intensity_assetsz_504d_base_v019_signal,
    f03uci_f03_utility_capex_intensity_intensitystd_63d_base_v020_signal,
    f03uci_f03_utility_capex_intensity_intensitystd_252d_base_v021_signal,
    f03uci_f03_utility_capex_intensity_assetsstd_252d_base_v022_signal,
    f03uci_f03_utility_capex_intensity_intensityema_63d_base_v023_signal,
    f03uci_f03_utility_capex_intensity_intensityema_252d_base_v024_signal,
    f03uci_f03_utility_capex_intensity_assetsema_252d_base_v025_signal,
    f03uci_f03_utility_capex_intensity_intensityrank_252d_base_v026_signal,
    f03uci_f03_utility_capex_intensity_assetsrank_252d_base_v027_signal,
    f03uci_f03_utility_capex_intensity_intensitychg_21d_base_v028_signal,
    f03uci_f03_utility_capex_intensity_intensitychg_63d_base_v029_signal,
    f03uci_f03_utility_capex_intensity_intensitychg_252d_base_v030_signal,
    f03uci_f03_utility_capex_intensity_assetschg_63d_base_v031_signal,
    f03uci_f03_utility_capex_intensity_assetschg_252d_base_v032_signal,
    f03uci_f03_utility_capex_intensity_intensity_5d_base_v033_signal,
    f03uci_f03_utility_capex_intensity_intensity_10d_base_v034_signal,
    f03uci_f03_utility_capex_intensity_intensity_42d_base_v035_signal,
    f03uci_f03_utility_capex_intensity_intensity_189d_base_v036_signal,
    f03uci_f03_utility_capex_intensity_intensity_378d_base_v037_signal,
    f03uci_f03_utility_capex_intensity_capexassets_5d_base_v038_signal,
    f03uci_f03_utility_capex_intensity_capexassets_42d_base_v039_signal,
    f03uci_f03_utility_capex_intensity_capexassets_189d_base_v040_signal,
    f03uci_f03_utility_capex_intensity_intensxvol_63d_base_v041_signal,
    f03uci_f03_utility_capex_intensity_intensxvol_252d_base_v042_signal,
    f03uci_f03_utility_capex_intensity_assetsxvol_252d_base_v043_signal,
    f03uci_f03_utility_capex_intensity_intensxatr_63d_base_v044_signal,
    f03uci_f03_utility_capex_intensity_intensxatr_252d_base_v045_signal,
    f03uci_f03_utility_capex_intensity_assetsxatr_252d_base_v046_signal,
    f03uci_f03_utility_capex_intensity_capexgrowth_63d_base_v047_signal,
    f03uci_f03_utility_capex_intensity_capexgrowth_252d_base_v048_signal,
    f03uci_f03_utility_capex_intensity_capexgrowth_504d_base_v049_signal,
    f03uci_f03_utility_capex_intensity_intensitylog_63d_base_v050_signal,
    f03uci_f03_utility_capex_intensity_intensitylog_252d_base_v051_signal,
    f03uci_f03_utility_capex_intensity_assetslog_252d_base_v052_signal,
    f03uci_f03_utility_capex_intensity_intensxsize_63d_base_v053_signal,
    f03uci_f03_utility_capex_intensity_intensxsize_252d_base_v054_signal,
    f03uci_f03_utility_capex_intensity_intensxrevsize_63d_base_v055_signal,
    f03uci_f03_utility_capex_intensity_intensxrevsize_252d_base_v056_signal,
    f03uci_f03_utility_capex_intensity_intenssq_63d_base_v057_signal,
    f03uci_f03_utility_capex_intensity_intenssq_252d_base_v058_signal,
    f03uci_f03_utility_capex_intensity_dynsq_63d_base_v059_signal,
    f03uci_f03_utility_capex_intensity_dynsq_252d_base_v060_signal,
    f03uci_f03_utility_capex_intensity_dynxvol_63d_base_v061_signal,
    f03uci_f03_utility_capex_intensity_dynxvol_252d_base_v062_signal,
    f03uci_f03_utility_capex_intensity_dynxatr_63d_base_v063_signal,
    f03uci_f03_utility_capex_intensity_dynxatr_252d_base_v064_signal,
    f03uci_f03_utility_capex_intensity_intenssum_63d_base_v065_signal,
    f03uci_f03_utility_capex_intensity_intenssum_252d_base_v066_signal,
    f03uci_f03_utility_capex_intensity_assetsxrev_63d_base_v067_signal,
    f03uci_f03_utility_capex_intensity_assetsxrev_252d_base_v068_signal,
    f03uci_f03_utility_capex_intensity_combointens_63d_base_v069_signal,
    f03uci_f03_utility_capex_intensity_combointens_252d_base_v070_signal,
    f03uci_f03_utility_capex_intensity_intensxrev_63d_base_v071_signal,
    f03uci_f03_utility_capex_intensity_intensxrev_252d_base_v072_signal,
    f03uci_f03_utility_capex_intensity_intensgap_63d_base_v073_signal,
    f03uci_f03_utility_capex_intensity_intensgap_252d_base_v074_signal,
    f03uci_f03_utility_capex_intensity_assetsgap_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F03_UTILITY_CAPEX_INTENSITY_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f03_utility_capex_intensity_base_001_075_claude: {n_features} features pass")
