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


# ===== folder domain primitives =====

def _f12_capex_acceleration(capex, w):
    g = capex.pct_change(periods=w)
    return g - g.shift(w)


def _f12_revenue_capex_dynamics(revenue, capex, w):
    rg = revenue.pct_change(periods=w)
    cg = capex.pct_change(periods=w)
    return rg * cg


def _f12_rollout_signature(capex, revenue, w):
    cg = capex.pct_change(periods=w)
    rg = revenue.pct_change(periods=w)
    cap_acc = cg - cg.shift(w)
    return cap_acc + rg


# ===== features =====

def f12rov_f12_rollout_velocity_cap_xclose_5d_base_v001_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_zclose_5d_base_v002_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_mclose_5d_base_v003_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_sclose_5d_base_v004_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_xclose_10d_base_v005_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_zclose_10d_base_v006_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_mclose_10d_base_v007_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_sclose_10d_base_v008_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_xclose_21d_base_v009_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_zclose_21d_base_v010_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_mclose_21d_base_v011_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_sclose_21d_base_v012_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_xclose_42d_base_v013_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_zclose_42d_base_v014_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_mclose_42d_base_v015_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_sclose_42d_base_v016_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_xclose_63d_base_v017_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_zclose_63d_base_v018_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_mclose_63d_base_v019_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_sclose_63d_base_v020_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_xclose_126d_base_v021_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_zclose_126d_base_v022_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 126) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_mclose_126d_base_v023_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 126) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_sclose_126d_base_v024_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_xclose_189d_base_v025_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_zclose_189d_base_v026_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 189) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_mclose_189d_base_v027_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 189) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_sclose_189d_base_v028_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 189) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_xclose_252d_base_v029_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_zclose_252d_base_v030_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 252) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_mclose_252d_base_v031_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 252) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_sclose_252d_base_v032_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 252) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_xclose_378d_base_v033_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_zclose_378d_base_v034_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 378) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_mclose_378d_base_v035_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 378) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_sclose_378d_base_v036_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 378) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_xclose_504d_base_v037_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_zclose_504d_base_v038_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 504) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_mclose_504d_base_v039_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 504) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_sclose_504d_base_v040_signal(capex, closeadj):
    result = _f12_capex_acceleration(capex, 504) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_xclose_5d_base_v041_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_zclose_5d_base_v042_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_mclose_5d_base_v043_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_sclose_5d_base_v044_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_xclose_10d_base_v045_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_zclose_10d_base_v046_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_mclose_10d_base_v047_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_sclose_10d_base_v048_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_xclose_21d_base_v049_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_zclose_21d_base_v050_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_mclose_21d_base_v051_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_sclose_21d_base_v052_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_xclose_42d_base_v053_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_zclose_42d_base_v054_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_mclose_42d_base_v055_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_sclose_42d_base_v056_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_xclose_63d_base_v057_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_zclose_63d_base_v058_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_mclose_63d_base_v059_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_sclose_63d_base_v060_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_xclose_126d_base_v061_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_zclose_126d_base_v062_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 126) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_mclose_126d_base_v063_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 126) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_sclose_126d_base_v064_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_xclose_189d_base_v065_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_zclose_189d_base_v066_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 189) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_mclose_189d_base_v067_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 189) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_sclose_189d_base_v068_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 189) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_xclose_252d_base_v069_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_zclose_252d_base_v070_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 252) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_mclose_252d_base_v071_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 252) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_sclose_252d_base_v072_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 252) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_xclose_378d_base_v073_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_zclose_378d_base_v074_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 378) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_mclose_378d_base_v075_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 378) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f12rov_f12_rollout_velocity_cap_xclose_5d_base_v001_signal,
    f12rov_f12_rollout_velocity_cap_zclose_5d_base_v002_signal,
    f12rov_f12_rollout_velocity_cap_mclose_5d_base_v003_signal,
    f12rov_f12_rollout_velocity_cap_sclose_5d_base_v004_signal,
    f12rov_f12_rollout_velocity_cap_xclose_10d_base_v005_signal,
    f12rov_f12_rollout_velocity_cap_zclose_10d_base_v006_signal,
    f12rov_f12_rollout_velocity_cap_mclose_10d_base_v007_signal,
    f12rov_f12_rollout_velocity_cap_sclose_10d_base_v008_signal,
    f12rov_f12_rollout_velocity_cap_xclose_21d_base_v009_signal,
    f12rov_f12_rollout_velocity_cap_zclose_21d_base_v010_signal,
    f12rov_f12_rollout_velocity_cap_mclose_21d_base_v011_signal,
    f12rov_f12_rollout_velocity_cap_sclose_21d_base_v012_signal,
    f12rov_f12_rollout_velocity_cap_xclose_42d_base_v013_signal,
    f12rov_f12_rollout_velocity_cap_zclose_42d_base_v014_signal,
    f12rov_f12_rollout_velocity_cap_mclose_42d_base_v015_signal,
    f12rov_f12_rollout_velocity_cap_sclose_42d_base_v016_signal,
    f12rov_f12_rollout_velocity_cap_xclose_63d_base_v017_signal,
    f12rov_f12_rollout_velocity_cap_zclose_63d_base_v018_signal,
    f12rov_f12_rollout_velocity_cap_mclose_63d_base_v019_signal,
    f12rov_f12_rollout_velocity_cap_sclose_63d_base_v020_signal,
    f12rov_f12_rollout_velocity_cap_xclose_126d_base_v021_signal,
    f12rov_f12_rollout_velocity_cap_zclose_126d_base_v022_signal,
    f12rov_f12_rollout_velocity_cap_mclose_126d_base_v023_signal,
    f12rov_f12_rollout_velocity_cap_sclose_126d_base_v024_signal,
    f12rov_f12_rollout_velocity_cap_xclose_189d_base_v025_signal,
    f12rov_f12_rollout_velocity_cap_zclose_189d_base_v026_signal,
    f12rov_f12_rollout_velocity_cap_mclose_189d_base_v027_signal,
    f12rov_f12_rollout_velocity_cap_sclose_189d_base_v028_signal,
    f12rov_f12_rollout_velocity_cap_xclose_252d_base_v029_signal,
    f12rov_f12_rollout_velocity_cap_zclose_252d_base_v030_signal,
    f12rov_f12_rollout_velocity_cap_mclose_252d_base_v031_signal,
    f12rov_f12_rollout_velocity_cap_sclose_252d_base_v032_signal,
    f12rov_f12_rollout_velocity_cap_xclose_378d_base_v033_signal,
    f12rov_f12_rollout_velocity_cap_zclose_378d_base_v034_signal,
    f12rov_f12_rollout_velocity_cap_mclose_378d_base_v035_signal,
    f12rov_f12_rollout_velocity_cap_sclose_378d_base_v036_signal,
    f12rov_f12_rollout_velocity_cap_xclose_504d_base_v037_signal,
    f12rov_f12_rollout_velocity_cap_zclose_504d_base_v038_signal,
    f12rov_f12_rollout_velocity_cap_mclose_504d_base_v039_signal,
    f12rov_f12_rollout_velocity_cap_sclose_504d_base_v040_signal,
    f12rov_f12_rollout_velocity_rcd_xclose_5d_base_v041_signal,
    f12rov_f12_rollout_velocity_rcd_zclose_5d_base_v042_signal,
    f12rov_f12_rollout_velocity_rcd_mclose_5d_base_v043_signal,
    f12rov_f12_rollout_velocity_rcd_sclose_5d_base_v044_signal,
    f12rov_f12_rollout_velocity_rcd_xclose_10d_base_v045_signal,
    f12rov_f12_rollout_velocity_rcd_zclose_10d_base_v046_signal,
    f12rov_f12_rollout_velocity_rcd_mclose_10d_base_v047_signal,
    f12rov_f12_rollout_velocity_rcd_sclose_10d_base_v048_signal,
    f12rov_f12_rollout_velocity_rcd_xclose_21d_base_v049_signal,
    f12rov_f12_rollout_velocity_rcd_zclose_21d_base_v050_signal,
    f12rov_f12_rollout_velocity_rcd_mclose_21d_base_v051_signal,
    f12rov_f12_rollout_velocity_rcd_sclose_21d_base_v052_signal,
    f12rov_f12_rollout_velocity_rcd_xclose_42d_base_v053_signal,
    f12rov_f12_rollout_velocity_rcd_zclose_42d_base_v054_signal,
    f12rov_f12_rollout_velocity_rcd_mclose_42d_base_v055_signal,
    f12rov_f12_rollout_velocity_rcd_sclose_42d_base_v056_signal,
    f12rov_f12_rollout_velocity_rcd_xclose_63d_base_v057_signal,
    f12rov_f12_rollout_velocity_rcd_zclose_63d_base_v058_signal,
    f12rov_f12_rollout_velocity_rcd_mclose_63d_base_v059_signal,
    f12rov_f12_rollout_velocity_rcd_sclose_63d_base_v060_signal,
    f12rov_f12_rollout_velocity_rcd_xclose_126d_base_v061_signal,
    f12rov_f12_rollout_velocity_rcd_zclose_126d_base_v062_signal,
    f12rov_f12_rollout_velocity_rcd_mclose_126d_base_v063_signal,
    f12rov_f12_rollout_velocity_rcd_sclose_126d_base_v064_signal,
    f12rov_f12_rollout_velocity_rcd_xclose_189d_base_v065_signal,
    f12rov_f12_rollout_velocity_rcd_zclose_189d_base_v066_signal,
    f12rov_f12_rollout_velocity_rcd_mclose_189d_base_v067_signal,
    f12rov_f12_rollout_velocity_rcd_sclose_189d_base_v068_signal,
    f12rov_f12_rollout_velocity_rcd_xclose_252d_base_v069_signal,
    f12rov_f12_rollout_velocity_rcd_zclose_252d_base_v070_signal,
    f12rov_f12_rollout_velocity_rcd_mclose_252d_base_v071_signal,
    f12rov_f12_rollout_velocity_rcd_sclose_252d_base_v072_signal,
    f12rov_f12_rollout_velocity_rcd_xclose_378d_base_v073_signal,
    f12rov_f12_rollout_velocity_rcd_zclose_378d_base_v074_signal,
    f12rov_f12_rollout_velocity_rcd_mclose_378d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F12_ROLLOUT_VELOCITY_REGISTRY_001_075 = REGISTRY


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
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "ebitda": ebitda, "capex": capex,
        "assets": assets, "ppnenet": ppnenet,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f12_capex_acceleration", "_f12_revenue_capex_dynamics", "_f12_rollout_signature")
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
    print(f"OK f12_rollout_velocity_base_001_075_claude: {n_features} features pass")
