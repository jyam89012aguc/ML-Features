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


# ===== folder domain primitives =====
def _f26_rate_sensitivity_proxy(revenue, assets, w):
    nim = revenue / assets.replace(0, np.nan)
    return nim - nim.rolling(w, min_periods=max(1, w // 2)).mean()


def _f26_nim_volatility(revenue, assets, w):
    nim = revenue / assets.replace(0, np.nan)
    return nim.rolling(w, min_periods=max(1, w // 2)).std()


def _f26_rate_cycle_pos(revenue, w):
    g = revenue.pct_change(periods=w)
    return g - g.rolling(w, min_periods=max(1, w // 2)).mean()


def f26irs_f26_interest_rate_sensitivity_proxy_21d_base_v001_signal(revenue, assets, closeadj):
    result = _f26_rate_sensitivity_proxy(revenue, assets, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxy_42d_base_v002_signal(revenue, assets, closeadj):
    result = _f26_rate_sensitivity_proxy(revenue, assets, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxy_63d_base_v003_signal(revenue, assets, closeadj):
    result = _f26_rate_sensitivity_proxy(revenue, assets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxy_126d_base_v004_signal(revenue, assets, closeadj):
    result = _f26_rate_sensitivity_proxy(revenue, assets, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxy_189d_base_v005_signal(revenue, assets, closeadj):
    result = _f26_rate_sensitivity_proxy(revenue, assets, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxy_252d_base_v006_signal(revenue, assets, closeadj):
    result = _f26_rate_sensitivity_proxy(revenue, assets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxy_378d_base_v007_signal(revenue, assets, closeadj):
    result = _f26_rate_sensitivity_proxy(revenue, assets, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxy_504d_base_v008_signal(revenue, assets, closeadj):
    result = _f26_rate_sensitivity_proxy(revenue, assets, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxysm_21d_base_v009_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxysm_63d_base_v010_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxysm_126d_base_v011_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 126)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxysm_252d_base_v012_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxystd_21d_base_v013_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxystd_63d_base_v014_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxystd_126d_base_v015_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxystd_252d_base_v016_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxyz_21d_base_v017_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxyz_63d_base_v018_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxyz_126d_base_v019_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 126)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxyz_252d_base_v020_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxyabs_21d_base_v021_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxyabs_63d_base_v022_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxyabs_252d_base_v023_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxysign_21d_base_v024_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 21)
    result = np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxysign_63d_base_v025_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 63)
    result = np.sign(base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_nimvol_21d_base_v026_signal(revenue, assets, closeadj):
    result = _f26_nim_volatility(revenue, assets, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_nimvol_42d_base_v027_signal(revenue, assets, closeadj):
    result = _f26_nim_volatility(revenue, assets, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_nimvol_63d_base_v028_signal(revenue, assets, closeadj):
    result = _f26_nim_volatility(revenue, assets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_nimvol_126d_base_v029_signal(revenue, assets, closeadj):
    result = _f26_nim_volatility(revenue, assets, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_nimvol_189d_base_v030_signal(revenue, assets, closeadj):
    result = _f26_nim_volatility(revenue, assets, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_nimvol_252d_base_v031_signal(revenue, assets, closeadj):
    result = _f26_nim_volatility(revenue, assets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_nimvol_378d_base_v032_signal(revenue, assets, closeadj):
    result = _f26_nim_volatility(revenue, assets, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_nimvol_504d_base_v033_signal(revenue, assets, closeadj):
    result = _f26_nim_volatility(revenue, assets, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_nimvolsm_21d_base_v034_signal(revenue, assets, closeadj):
    base = _f26_nim_volatility(revenue, assets, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_nimvolsm_63d_base_v035_signal(revenue, assets, closeadj):
    base = _f26_nim_volatility(revenue, assets, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_nimvolsm_252d_base_v036_signal(revenue, assets, closeadj):
    base = _f26_nim_volatility(revenue, assets, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_nimvolstd_63d_base_v037_signal(revenue, assets, closeadj):
    base = _f26_nim_volatility(revenue, assets, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_nimvolstd_252d_base_v038_signal(revenue, assets, closeadj):
    base = _f26_nim_volatility(revenue, assets, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_nimvolz_63d_base_v039_signal(revenue, assets, closeadj):
    base = _f26_nim_volatility(revenue, assets, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_nimvolz_252d_base_v040_signal(revenue, assets, closeadj):
    base = _f26_nim_volatility(revenue, assets, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_cyclepos_21d_base_v041_signal(revenue, closeadj):
    result = _f26_rate_cycle_pos(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_cyclepos_42d_base_v042_signal(revenue, closeadj):
    result = _f26_rate_cycle_pos(revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_cyclepos_63d_base_v043_signal(revenue, closeadj):
    result = _f26_rate_cycle_pos(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_cyclepos_126d_base_v044_signal(revenue, closeadj):
    result = _f26_rate_cycle_pos(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_cyclepos_189d_base_v045_signal(revenue, closeadj):
    result = _f26_rate_cycle_pos(revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_cyclepos_252d_base_v046_signal(revenue, closeadj):
    result = _f26_rate_cycle_pos(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_cyclepos_378d_base_v047_signal(revenue, closeadj):
    result = _f26_rate_cycle_pos(revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_cyclepos_504d_base_v048_signal(revenue, closeadj):
    result = _f26_rate_cycle_pos(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_cycleposm_21d_base_v049_signal(revenue, closeadj):
    base = _f26_rate_cycle_pos(revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_cycleposm_63d_base_v050_signal(revenue, closeadj):
    base = _f26_rate_cycle_pos(revenue, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_cycleposm_252d_base_v051_signal(revenue, closeadj):
    base = _f26_rate_cycle_pos(revenue, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_cycleposstd_63d_base_v052_signal(revenue, closeadj):
    base = _f26_rate_cycle_pos(revenue, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_cycleposstd_252d_base_v053_signal(revenue, closeadj):
    base = _f26_rate_cycle_pos(revenue, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_cycleposz_63d_base_v054_signal(revenue, closeadj):
    base = _f26_rate_cycle_pos(revenue, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_cycleposz_252d_base_v055_signal(revenue, closeadj):
    base = _f26_rate_cycle_pos(revenue, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_cycleposabs_63d_base_v056_signal(revenue, closeadj):
    base = _f26_rate_cycle_pos(revenue, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_cycleposabs_252d_base_v057_signal(revenue, closeadj):
    base = _f26_rate_cycle_pos(revenue, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_cyclepossign_63d_base_v058_signal(revenue, closeadj):
    base = _f26_rate_cycle_pos(revenue, 63)
    result = np.sign(base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxydv_21d_base_v059_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxydv_63d_base_v060_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 63)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_nimvoldv_63d_base_v061_signal(revenue, assets, closeadj):
    base = _f26_nim_volatility(revenue, assets, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_nimvoldv_252d_base_v062_signal(revenue, assets, closeadj):
    base = _f26_nim_volatility(revenue, assets, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_cycleposdv_63d_base_v063_signal(revenue, closeadj):
    base = _f26_rate_cycle_pos(revenue, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_cycleposdv_252d_base_v064_signal(revenue, closeadj):
    base = _f26_rate_cycle_pos(revenue, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxypos_63d_base_v065_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 63)
    pos = (base > 0).astype(float)
    result = pos * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxyneg_63d_base_v066_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 63)
    neg = (base < 0).astype(float)
    result = neg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_nimvollog_63d_base_v067_signal(revenue, assets, closeadj):
    base = _f26_nim_volatility(revenue, assets, 63)
    result = np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_nimvollog_252d_base_v068_signal(revenue, assets, closeadj):
    base = _f26_nim_volatility(revenue, assets, 252)
    result = np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxyrng_63d_base_v069_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 63)
    rng = base.rolling(63, min_periods=21).max() - base.rolling(63, min_periods=21).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxyrng_252d_base_v070_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 252)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_cycleposrng_252d_base_v071_signal(revenue, closeadj):
    base = _f26_rate_cycle_pos(revenue, 252)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxysq_63d_base_v072_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_proxysq_252d_base_v073_signal(revenue, assets, closeadj):
    base = _f26_rate_sensitivity_proxy(revenue, assets, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_cycleposlog_63d_base_v074_signal(revenue, closeadj):
    base = _f26_rate_cycle_pos(revenue, 63)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26irs_f26_interest_rate_sensitivity_cycleposlog_252d_base_v075_signal(revenue, closeadj):
    base = _f26_rate_cycle_pos(revenue, 252)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f26irs_f26_interest_rate_sensitivity_proxy_21d_base_v001_signal,
    f26irs_f26_interest_rate_sensitivity_proxy_42d_base_v002_signal,
    f26irs_f26_interest_rate_sensitivity_proxy_63d_base_v003_signal,
    f26irs_f26_interest_rate_sensitivity_proxy_126d_base_v004_signal,
    f26irs_f26_interest_rate_sensitivity_proxy_189d_base_v005_signal,
    f26irs_f26_interest_rate_sensitivity_proxy_252d_base_v006_signal,
    f26irs_f26_interest_rate_sensitivity_proxy_378d_base_v007_signal,
    f26irs_f26_interest_rate_sensitivity_proxy_504d_base_v008_signal,
    f26irs_f26_interest_rate_sensitivity_proxysm_21d_base_v009_signal,
    f26irs_f26_interest_rate_sensitivity_proxysm_63d_base_v010_signal,
    f26irs_f26_interest_rate_sensitivity_proxysm_126d_base_v011_signal,
    f26irs_f26_interest_rate_sensitivity_proxysm_252d_base_v012_signal,
    f26irs_f26_interest_rate_sensitivity_proxystd_21d_base_v013_signal,
    f26irs_f26_interest_rate_sensitivity_proxystd_63d_base_v014_signal,
    f26irs_f26_interest_rate_sensitivity_proxystd_126d_base_v015_signal,
    f26irs_f26_interest_rate_sensitivity_proxystd_252d_base_v016_signal,
    f26irs_f26_interest_rate_sensitivity_proxyz_21d_base_v017_signal,
    f26irs_f26_interest_rate_sensitivity_proxyz_63d_base_v018_signal,
    f26irs_f26_interest_rate_sensitivity_proxyz_126d_base_v019_signal,
    f26irs_f26_interest_rate_sensitivity_proxyz_252d_base_v020_signal,
    f26irs_f26_interest_rate_sensitivity_proxyabs_21d_base_v021_signal,
    f26irs_f26_interest_rate_sensitivity_proxyabs_63d_base_v022_signal,
    f26irs_f26_interest_rate_sensitivity_proxyabs_252d_base_v023_signal,
    f26irs_f26_interest_rate_sensitivity_proxysign_21d_base_v024_signal,
    f26irs_f26_interest_rate_sensitivity_proxysign_63d_base_v025_signal,
    f26irs_f26_interest_rate_sensitivity_nimvol_21d_base_v026_signal,
    f26irs_f26_interest_rate_sensitivity_nimvol_42d_base_v027_signal,
    f26irs_f26_interest_rate_sensitivity_nimvol_63d_base_v028_signal,
    f26irs_f26_interest_rate_sensitivity_nimvol_126d_base_v029_signal,
    f26irs_f26_interest_rate_sensitivity_nimvol_189d_base_v030_signal,
    f26irs_f26_interest_rate_sensitivity_nimvol_252d_base_v031_signal,
    f26irs_f26_interest_rate_sensitivity_nimvol_378d_base_v032_signal,
    f26irs_f26_interest_rate_sensitivity_nimvol_504d_base_v033_signal,
    f26irs_f26_interest_rate_sensitivity_nimvolsm_21d_base_v034_signal,
    f26irs_f26_interest_rate_sensitivity_nimvolsm_63d_base_v035_signal,
    f26irs_f26_interest_rate_sensitivity_nimvolsm_252d_base_v036_signal,
    f26irs_f26_interest_rate_sensitivity_nimvolstd_63d_base_v037_signal,
    f26irs_f26_interest_rate_sensitivity_nimvolstd_252d_base_v038_signal,
    f26irs_f26_interest_rate_sensitivity_nimvolz_63d_base_v039_signal,
    f26irs_f26_interest_rate_sensitivity_nimvolz_252d_base_v040_signal,
    f26irs_f26_interest_rate_sensitivity_cyclepos_21d_base_v041_signal,
    f26irs_f26_interest_rate_sensitivity_cyclepos_42d_base_v042_signal,
    f26irs_f26_interest_rate_sensitivity_cyclepos_63d_base_v043_signal,
    f26irs_f26_interest_rate_sensitivity_cyclepos_126d_base_v044_signal,
    f26irs_f26_interest_rate_sensitivity_cyclepos_189d_base_v045_signal,
    f26irs_f26_interest_rate_sensitivity_cyclepos_252d_base_v046_signal,
    f26irs_f26_interest_rate_sensitivity_cyclepos_378d_base_v047_signal,
    f26irs_f26_interest_rate_sensitivity_cyclepos_504d_base_v048_signal,
    f26irs_f26_interest_rate_sensitivity_cycleposm_21d_base_v049_signal,
    f26irs_f26_interest_rate_sensitivity_cycleposm_63d_base_v050_signal,
    f26irs_f26_interest_rate_sensitivity_cycleposm_252d_base_v051_signal,
    f26irs_f26_interest_rate_sensitivity_cycleposstd_63d_base_v052_signal,
    f26irs_f26_interest_rate_sensitivity_cycleposstd_252d_base_v053_signal,
    f26irs_f26_interest_rate_sensitivity_cycleposz_63d_base_v054_signal,
    f26irs_f26_interest_rate_sensitivity_cycleposz_252d_base_v055_signal,
    f26irs_f26_interest_rate_sensitivity_cycleposabs_63d_base_v056_signal,
    f26irs_f26_interest_rate_sensitivity_cycleposabs_252d_base_v057_signal,
    f26irs_f26_interest_rate_sensitivity_cyclepossign_63d_base_v058_signal,
    f26irs_f26_interest_rate_sensitivity_proxydv_21d_base_v059_signal,
    f26irs_f26_interest_rate_sensitivity_proxydv_63d_base_v060_signal,
    f26irs_f26_interest_rate_sensitivity_nimvoldv_63d_base_v061_signal,
    f26irs_f26_interest_rate_sensitivity_nimvoldv_252d_base_v062_signal,
    f26irs_f26_interest_rate_sensitivity_cycleposdv_63d_base_v063_signal,
    f26irs_f26_interest_rate_sensitivity_cycleposdv_252d_base_v064_signal,
    f26irs_f26_interest_rate_sensitivity_proxypos_63d_base_v065_signal,
    f26irs_f26_interest_rate_sensitivity_proxyneg_63d_base_v066_signal,
    f26irs_f26_interest_rate_sensitivity_nimvollog_63d_base_v067_signal,
    f26irs_f26_interest_rate_sensitivity_nimvollog_252d_base_v068_signal,
    f26irs_f26_interest_rate_sensitivity_proxyrng_63d_base_v069_signal,
    f26irs_f26_interest_rate_sensitivity_proxyrng_252d_base_v070_signal,
    f26irs_f26_interest_rate_sensitivity_cycleposrng_252d_base_v071_signal,
    f26irs_f26_interest_rate_sensitivity_proxysq_63d_base_v072_signal,
    f26irs_f26_interest_rate_sensitivity_proxysq_252d_base_v073_signal,
    f26irs_f26_interest_rate_sensitivity_cycleposlog_63d_base_v074_signal,
    f26irs_f26_interest_rate_sensitivity_cycleposlog_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_INTEREST_RATE_SENSITIVITY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")

    cols = {"closeadj": closeadj, "revenue": revenue, "assets": assets}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f26_rate_sensitivity_proxy", "_f26_nim_volatility", "_f26_rate_cycle_pos")
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
    print(f"OK f26_interest_rate_sensitivity_base_001_075_claude: {n_features} features pass")
