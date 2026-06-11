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
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f09_capex_to_ppe(capex, ppnenet):
    return capex / ppnenet.replace(0, np.nan)


def _f09_renewal_intensity(capex, ppnenet, depamor):
    return (capex - depamor) / ppnenet.replace(0, np.nan)


def _f09_capex_store_ratio(capex, ppnenet, w):
    ratio = capex / ppnenet.replace(0, np.nan)
    return ratio.rolling(w, min_periods=max(1, w // 2)).mean()

def f09rcs_f09_retail_capex_per_store_c2p_mean_5d_jerk_v001_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _mean(r, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_mean_10d_jerk_v002_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _mean(r, 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_mean_21d_jerk_v003_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _mean(r, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_mean_42d_jerk_v004_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _mean(r, 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_mean_63d_jerk_v005_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _mean(r, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_mean_126d_jerk_v006_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _mean(r, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_mean_189d_jerk_v007_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _mean(r, 189) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_mean_252d_jerk_v008_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _mean(r, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_mean_378d_jerk_v009_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _mean(r, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_mean_504d_jerk_v010_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _mean(r, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_std_5d_jerk_v011_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _std(r, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_std_10d_jerk_v012_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _std(r, 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_std_21d_jerk_v013_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _std(r, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_std_42d_jerk_v014_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _std(r, 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_std_63d_jerk_v015_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _std(r, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_std_126d_jerk_v016_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _std(r, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_std_189d_jerk_v017_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _std(r, 189) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_std_252d_jerk_v018_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _std(r, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_std_378d_jerk_v019_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _std(r, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_std_504d_jerk_v020_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _std(r, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_z_5d_jerk_v021_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _z(r, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_z_10d_jerk_v022_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _z(r, 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_z_21d_jerk_v023_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _z(r, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_z_42d_jerk_v024_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _z(r, 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_z_63d_jerk_v025_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _z(r, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_z_126d_jerk_v026_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _z(r, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_z_189d_jerk_v027_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _z(r, 189) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_z_252d_jerk_v028_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _z(r, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_z_378d_jerk_v029_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _z(r, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_z_504d_jerk_v030_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _z(r, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_ema_5d_jerk_v031_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _ema(r, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_ema_10d_jerk_v032_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _ema(r, 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_ema_21d_jerk_v033_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _ema(r, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_ema_42d_jerk_v034_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _ema(r, 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_ema_63d_jerk_v035_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _ema(r, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_ema_126d_jerk_v036_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _ema(r, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_ema_189d_jerk_v037_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _ema(r, 189) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_ema_252d_jerk_v038_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _ema(r, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_ema_378d_jerk_v039_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _ema(r, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_ema_504d_jerk_v040_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = _ema(r, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_diff_5d_jerk_v041_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = (r - r.shift(5)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_diff_10d_jerk_v042_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = (r - r.shift(10)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_diff_21d_jerk_v043_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = (r - r.shift(21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_diff_42d_jerk_v044_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = (r - r.shift(42)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_diff_63d_jerk_v045_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = (r - r.shift(63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_diff_126d_jerk_v046_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = (r - r.shift(126)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_diff_189d_jerk_v047_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = (r - r.shift(189)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_diff_252d_jerk_v048_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = (r - r.shift(252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_diff_378d_jerk_v049_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = (r - r.shift(378)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_c2p_diff_504d_jerk_v050_signal(capex, ppnenet, closeadj):
    r = _f09_capex_to_ppe(capex, ppnenet)
    base = (r - r.shift(504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_mean_5d_jerk_v051_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _mean(ri, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_mean_10d_jerk_v052_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _mean(ri, 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_mean_21d_jerk_v053_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _mean(ri, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_mean_42d_jerk_v054_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _mean(ri, 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_mean_63d_jerk_v055_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _mean(ri, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_mean_126d_jerk_v056_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _mean(ri, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_mean_189d_jerk_v057_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _mean(ri, 189) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_mean_252d_jerk_v058_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _mean(ri, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_mean_378d_jerk_v059_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _mean(ri, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_mean_504d_jerk_v060_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _mean(ri, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_std_5d_jerk_v061_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _std(ri, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_std_10d_jerk_v062_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _std(ri, 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_std_21d_jerk_v063_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _std(ri, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_std_42d_jerk_v064_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _std(ri, 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_std_63d_jerk_v065_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _std(ri, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_std_126d_jerk_v066_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _std(ri, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_std_189d_jerk_v067_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _std(ri, 189) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_std_252d_jerk_v068_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _std(ri, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_std_378d_jerk_v069_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _std(ri, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_std_504d_jerk_v070_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _std(ri, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_z_5d_jerk_v071_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _z(ri, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_z_10d_jerk_v072_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _z(ri, 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_z_21d_jerk_v073_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _z(ri, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_z_42d_jerk_v074_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _z(ri, 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_z_63d_jerk_v075_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _z(ri, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_z_126d_jerk_v076_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _z(ri, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_z_189d_jerk_v077_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _z(ri, 189) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_z_252d_jerk_v078_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _z(ri, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_z_378d_jerk_v079_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _z(ri, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_z_504d_jerk_v080_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _z(ri, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_ema_5d_jerk_v081_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _ema(ri, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_ema_10d_jerk_v082_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _ema(ri, 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_ema_21d_jerk_v083_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _ema(ri, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_ema_42d_jerk_v084_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _ema(ri, 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_ema_63d_jerk_v085_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _ema(ri, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_ema_126d_jerk_v086_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _ema(ri, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_ema_189d_jerk_v087_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _ema(ri, 189) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_ema_252d_jerk_v088_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _ema(ri, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_ema_378d_jerk_v089_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _ema(ri, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_ema_504d_jerk_v090_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = _ema(ri, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_diff_5d_jerk_v091_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = (ri - ri.shift(5)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_diff_10d_jerk_v092_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = (ri - ri.shift(10)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_diff_21d_jerk_v093_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = (ri - ri.shift(21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_diff_42d_jerk_v094_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = (ri - ri.shift(42)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_diff_63d_jerk_v095_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = (ri - ri.shift(63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_diff_126d_jerk_v096_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = (ri - ri.shift(126)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_diff_189d_jerk_v097_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = (ri - ri.shift(189)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_diff_252d_jerk_v098_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = (ri - ri.shift(252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_diff_378d_jerk_v099_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = (ri - ri.shift(378)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_diff_504d_jerk_v100_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    base = (ri - ri.shift(504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_5d_jerk_v101_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 5)
    base = r * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_10d_jerk_v102_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 10)
    base = r * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_21d_jerk_v103_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 21)
    base = r * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_42d_jerk_v104_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 42)
    base = r * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_63d_jerk_v105_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 63)
    base = r * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_126d_jerk_v106_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 126)
    base = r * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_189d_jerk_v107_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 189)
    base = r * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_252d_jerk_v108_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 252)
    base = r * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_378d_jerk_v109_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 378)
    base = r * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_504d_jerk_v110_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 504)
    base = r * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_std_5d_jerk_v111_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 5)
    base = _std(r, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_std_10d_jerk_v112_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 10)
    base = _std(r, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_std_21d_jerk_v113_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 21)
    base = _std(r, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_std_42d_jerk_v114_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 42)
    base = _std(r, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_std_63d_jerk_v115_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 63)
    base = _std(r, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_std_126d_jerk_v116_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 126)
    base = _std(r, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_std_189d_jerk_v117_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 189)
    base = _std(r, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_std_252d_jerk_v118_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 252)
    base = _std(r, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_std_378d_jerk_v119_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 378)
    base = _std(r, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_std_504d_jerk_v120_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 504)
    base = _std(r, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_z_5d_jerk_v121_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 5)
    base = _z(r, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_z_10d_jerk_v122_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 10)
    base = _z(r, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_z_21d_jerk_v123_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 21)
    base = _z(r, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_z_42d_jerk_v124_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 42)
    base = _z(r, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_z_63d_jerk_v125_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 63)
    base = _z(r, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_z_126d_jerk_v126_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 126)
    base = _z(r, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_z_189d_jerk_v127_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 189)
    base = _z(r, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_z_252d_jerk_v128_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 252)
    base = _z(r, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_z_378d_jerk_v129_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 378)
    base = _z(r, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_z_504d_jerk_v130_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 504)
    base = _z(r, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_xdep_5d_jerk_v131_signal(capex, ppnenet, depamor, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 5)
    base = r * (depamor / 1e7) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_xdep_10d_jerk_v132_signal(capex, ppnenet, depamor, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 10)
    base = r * (depamor / 1e7) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_xdep_21d_jerk_v133_signal(capex, ppnenet, depamor, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 21)
    base = r * (depamor / 1e7) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_xdep_42d_jerk_v134_signal(capex, ppnenet, depamor, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 42)
    base = r * (depamor / 1e7) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_xdep_63d_jerk_v135_signal(capex, ppnenet, depamor, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 63)
    base = r * (depamor / 1e7) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_xdep_126d_jerk_v136_signal(capex, ppnenet, depamor, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 126)
    base = r * (depamor / 1e7) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_xdep_189d_jerk_v137_signal(capex, ppnenet, depamor, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 189)
    base = r * (depamor / 1e7) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_xdep_252d_jerk_v138_signal(capex, ppnenet, depamor, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 252)
    base = r * (depamor / 1e7) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_xdep_378d_jerk_v139_signal(capex, ppnenet, depamor, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 378)
    base = r * (depamor / 1e7) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_xdep_504d_jerk_v140_signal(capex, ppnenet, depamor, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 504)
    base = r * (depamor / 1e7) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_diff_5d_jerk_v141_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 5)
    base = (r - r.shift(21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_diff_10d_jerk_v142_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 10)
    base = (r - r.shift(21)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_diff_21d_jerk_v143_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 21)
    base = (r - r.shift(21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_diff_42d_jerk_v144_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 42)
    base = (r - r.shift(21)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_diff_63d_jerk_v145_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 63)
    base = (r - r.shift(21)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_diff_126d_jerk_v146_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 126)
    base = (r - r.shift(21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_diff_189d_jerk_v147_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 189)
    base = (r - r.shift(21)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_diff_252d_jerk_v148_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 252)
    base = (r - r.shift(21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_diff_378d_jerk_v149_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 378)
    base = (r - r.shift(21)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_diff_504d_jerk_v150_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 504)
    base = (r - r.shift(21)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f09rcs_f09_retail_capex_per_store_c2p_mean_5d_jerk_v001_signal,
    f09rcs_f09_retail_capex_per_store_c2p_mean_10d_jerk_v002_signal,
    f09rcs_f09_retail_capex_per_store_c2p_mean_21d_jerk_v003_signal,
    f09rcs_f09_retail_capex_per_store_c2p_mean_42d_jerk_v004_signal,
    f09rcs_f09_retail_capex_per_store_c2p_mean_63d_jerk_v005_signal,
    f09rcs_f09_retail_capex_per_store_c2p_mean_126d_jerk_v006_signal,
    f09rcs_f09_retail_capex_per_store_c2p_mean_189d_jerk_v007_signal,
    f09rcs_f09_retail_capex_per_store_c2p_mean_252d_jerk_v008_signal,
    f09rcs_f09_retail_capex_per_store_c2p_mean_378d_jerk_v009_signal,
    f09rcs_f09_retail_capex_per_store_c2p_mean_504d_jerk_v010_signal,
    f09rcs_f09_retail_capex_per_store_c2p_std_5d_jerk_v011_signal,
    f09rcs_f09_retail_capex_per_store_c2p_std_10d_jerk_v012_signal,
    f09rcs_f09_retail_capex_per_store_c2p_std_21d_jerk_v013_signal,
    f09rcs_f09_retail_capex_per_store_c2p_std_42d_jerk_v014_signal,
    f09rcs_f09_retail_capex_per_store_c2p_std_63d_jerk_v015_signal,
    f09rcs_f09_retail_capex_per_store_c2p_std_126d_jerk_v016_signal,
    f09rcs_f09_retail_capex_per_store_c2p_std_189d_jerk_v017_signal,
    f09rcs_f09_retail_capex_per_store_c2p_std_252d_jerk_v018_signal,
    f09rcs_f09_retail_capex_per_store_c2p_std_378d_jerk_v019_signal,
    f09rcs_f09_retail_capex_per_store_c2p_std_504d_jerk_v020_signal,
    f09rcs_f09_retail_capex_per_store_c2p_z_5d_jerk_v021_signal,
    f09rcs_f09_retail_capex_per_store_c2p_z_10d_jerk_v022_signal,
    f09rcs_f09_retail_capex_per_store_c2p_z_21d_jerk_v023_signal,
    f09rcs_f09_retail_capex_per_store_c2p_z_42d_jerk_v024_signal,
    f09rcs_f09_retail_capex_per_store_c2p_z_63d_jerk_v025_signal,
    f09rcs_f09_retail_capex_per_store_c2p_z_126d_jerk_v026_signal,
    f09rcs_f09_retail_capex_per_store_c2p_z_189d_jerk_v027_signal,
    f09rcs_f09_retail_capex_per_store_c2p_z_252d_jerk_v028_signal,
    f09rcs_f09_retail_capex_per_store_c2p_z_378d_jerk_v029_signal,
    f09rcs_f09_retail_capex_per_store_c2p_z_504d_jerk_v030_signal,
    f09rcs_f09_retail_capex_per_store_c2p_ema_5d_jerk_v031_signal,
    f09rcs_f09_retail_capex_per_store_c2p_ema_10d_jerk_v032_signal,
    f09rcs_f09_retail_capex_per_store_c2p_ema_21d_jerk_v033_signal,
    f09rcs_f09_retail_capex_per_store_c2p_ema_42d_jerk_v034_signal,
    f09rcs_f09_retail_capex_per_store_c2p_ema_63d_jerk_v035_signal,
    f09rcs_f09_retail_capex_per_store_c2p_ema_126d_jerk_v036_signal,
    f09rcs_f09_retail_capex_per_store_c2p_ema_189d_jerk_v037_signal,
    f09rcs_f09_retail_capex_per_store_c2p_ema_252d_jerk_v038_signal,
    f09rcs_f09_retail_capex_per_store_c2p_ema_378d_jerk_v039_signal,
    f09rcs_f09_retail_capex_per_store_c2p_ema_504d_jerk_v040_signal,
    f09rcs_f09_retail_capex_per_store_c2p_diff_5d_jerk_v041_signal,
    f09rcs_f09_retail_capex_per_store_c2p_diff_10d_jerk_v042_signal,
    f09rcs_f09_retail_capex_per_store_c2p_diff_21d_jerk_v043_signal,
    f09rcs_f09_retail_capex_per_store_c2p_diff_42d_jerk_v044_signal,
    f09rcs_f09_retail_capex_per_store_c2p_diff_63d_jerk_v045_signal,
    f09rcs_f09_retail_capex_per_store_c2p_diff_126d_jerk_v046_signal,
    f09rcs_f09_retail_capex_per_store_c2p_diff_189d_jerk_v047_signal,
    f09rcs_f09_retail_capex_per_store_c2p_diff_252d_jerk_v048_signal,
    f09rcs_f09_retail_capex_per_store_c2p_diff_378d_jerk_v049_signal,
    f09rcs_f09_retail_capex_per_store_c2p_diff_504d_jerk_v050_signal,
    f09rcs_f09_retail_capex_per_store_renew_mean_5d_jerk_v051_signal,
    f09rcs_f09_retail_capex_per_store_renew_mean_10d_jerk_v052_signal,
    f09rcs_f09_retail_capex_per_store_renew_mean_21d_jerk_v053_signal,
    f09rcs_f09_retail_capex_per_store_renew_mean_42d_jerk_v054_signal,
    f09rcs_f09_retail_capex_per_store_renew_mean_63d_jerk_v055_signal,
    f09rcs_f09_retail_capex_per_store_renew_mean_126d_jerk_v056_signal,
    f09rcs_f09_retail_capex_per_store_renew_mean_189d_jerk_v057_signal,
    f09rcs_f09_retail_capex_per_store_renew_mean_252d_jerk_v058_signal,
    f09rcs_f09_retail_capex_per_store_renew_mean_378d_jerk_v059_signal,
    f09rcs_f09_retail_capex_per_store_renew_mean_504d_jerk_v060_signal,
    f09rcs_f09_retail_capex_per_store_renew_std_5d_jerk_v061_signal,
    f09rcs_f09_retail_capex_per_store_renew_std_10d_jerk_v062_signal,
    f09rcs_f09_retail_capex_per_store_renew_std_21d_jerk_v063_signal,
    f09rcs_f09_retail_capex_per_store_renew_std_42d_jerk_v064_signal,
    f09rcs_f09_retail_capex_per_store_renew_std_63d_jerk_v065_signal,
    f09rcs_f09_retail_capex_per_store_renew_std_126d_jerk_v066_signal,
    f09rcs_f09_retail_capex_per_store_renew_std_189d_jerk_v067_signal,
    f09rcs_f09_retail_capex_per_store_renew_std_252d_jerk_v068_signal,
    f09rcs_f09_retail_capex_per_store_renew_std_378d_jerk_v069_signal,
    f09rcs_f09_retail_capex_per_store_renew_std_504d_jerk_v070_signal,
    f09rcs_f09_retail_capex_per_store_renew_z_5d_jerk_v071_signal,
    f09rcs_f09_retail_capex_per_store_renew_z_10d_jerk_v072_signal,
    f09rcs_f09_retail_capex_per_store_renew_z_21d_jerk_v073_signal,
    f09rcs_f09_retail_capex_per_store_renew_z_42d_jerk_v074_signal,
    f09rcs_f09_retail_capex_per_store_renew_z_63d_jerk_v075_signal,
    f09rcs_f09_retail_capex_per_store_renew_z_126d_jerk_v076_signal,
    f09rcs_f09_retail_capex_per_store_renew_z_189d_jerk_v077_signal,
    f09rcs_f09_retail_capex_per_store_renew_z_252d_jerk_v078_signal,
    f09rcs_f09_retail_capex_per_store_renew_z_378d_jerk_v079_signal,
    f09rcs_f09_retail_capex_per_store_renew_z_504d_jerk_v080_signal,
    f09rcs_f09_retail_capex_per_store_renew_ema_5d_jerk_v081_signal,
    f09rcs_f09_retail_capex_per_store_renew_ema_10d_jerk_v082_signal,
    f09rcs_f09_retail_capex_per_store_renew_ema_21d_jerk_v083_signal,
    f09rcs_f09_retail_capex_per_store_renew_ema_42d_jerk_v084_signal,
    f09rcs_f09_retail_capex_per_store_renew_ema_63d_jerk_v085_signal,
    f09rcs_f09_retail_capex_per_store_renew_ema_126d_jerk_v086_signal,
    f09rcs_f09_retail_capex_per_store_renew_ema_189d_jerk_v087_signal,
    f09rcs_f09_retail_capex_per_store_renew_ema_252d_jerk_v088_signal,
    f09rcs_f09_retail_capex_per_store_renew_ema_378d_jerk_v089_signal,
    f09rcs_f09_retail_capex_per_store_renew_ema_504d_jerk_v090_signal,
    f09rcs_f09_retail_capex_per_store_renew_diff_5d_jerk_v091_signal,
    f09rcs_f09_retail_capex_per_store_renew_diff_10d_jerk_v092_signal,
    f09rcs_f09_retail_capex_per_store_renew_diff_21d_jerk_v093_signal,
    f09rcs_f09_retail_capex_per_store_renew_diff_42d_jerk_v094_signal,
    f09rcs_f09_retail_capex_per_store_renew_diff_63d_jerk_v095_signal,
    f09rcs_f09_retail_capex_per_store_renew_diff_126d_jerk_v096_signal,
    f09rcs_f09_retail_capex_per_store_renew_diff_189d_jerk_v097_signal,
    f09rcs_f09_retail_capex_per_store_renew_diff_252d_jerk_v098_signal,
    f09rcs_f09_retail_capex_per_store_renew_diff_378d_jerk_v099_signal,
    f09rcs_f09_retail_capex_per_store_renew_diff_504d_jerk_v100_signal,
    f09rcs_f09_retail_capex_per_store_csr_5d_jerk_v101_signal,
    f09rcs_f09_retail_capex_per_store_csr_10d_jerk_v102_signal,
    f09rcs_f09_retail_capex_per_store_csr_21d_jerk_v103_signal,
    f09rcs_f09_retail_capex_per_store_csr_42d_jerk_v104_signal,
    f09rcs_f09_retail_capex_per_store_csr_63d_jerk_v105_signal,
    f09rcs_f09_retail_capex_per_store_csr_126d_jerk_v106_signal,
    f09rcs_f09_retail_capex_per_store_csr_189d_jerk_v107_signal,
    f09rcs_f09_retail_capex_per_store_csr_252d_jerk_v108_signal,
    f09rcs_f09_retail_capex_per_store_csr_378d_jerk_v109_signal,
    f09rcs_f09_retail_capex_per_store_csr_504d_jerk_v110_signal,
    f09rcs_f09_retail_capex_per_store_csr_std_5d_jerk_v111_signal,
    f09rcs_f09_retail_capex_per_store_csr_std_10d_jerk_v112_signal,
    f09rcs_f09_retail_capex_per_store_csr_std_21d_jerk_v113_signal,
    f09rcs_f09_retail_capex_per_store_csr_std_42d_jerk_v114_signal,
    f09rcs_f09_retail_capex_per_store_csr_std_63d_jerk_v115_signal,
    f09rcs_f09_retail_capex_per_store_csr_std_126d_jerk_v116_signal,
    f09rcs_f09_retail_capex_per_store_csr_std_189d_jerk_v117_signal,
    f09rcs_f09_retail_capex_per_store_csr_std_252d_jerk_v118_signal,
    f09rcs_f09_retail_capex_per_store_csr_std_378d_jerk_v119_signal,
    f09rcs_f09_retail_capex_per_store_csr_std_504d_jerk_v120_signal,
    f09rcs_f09_retail_capex_per_store_csr_z_5d_jerk_v121_signal,
    f09rcs_f09_retail_capex_per_store_csr_z_10d_jerk_v122_signal,
    f09rcs_f09_retail_capex_per_store_csr_z_21d_jerk_v123_signal,
    f09rcs_f09_retail_capex_per_store_csr_z_42d_jerk_v124_signal,
    f09rcs_f09_retail_capex_per_store_csr_z_63d_jerk_v125_signal,
    f09rcs_f09_retail_capex_per_store_csr_z_126d_jerk_v126_signal,
    f09rcs_f09_retail_capex_per_store_csr_z_189d_jerk_v127_signal,
    f09rcs_f09_retail_capex_per_store_csr_z_252d_jerk_v128_signal,
    f09rcs_f09_retail_capex_per_store_csr_z_378d_jerk_v129_signal,
    f09rcs_f09_retail_capex_per_store_csr_z_504d_jerk_v130_signal,
    f09rcs_f09_retail_capex_per_store_csr_xdep_5d_jerk_v131_signal,
    f09rcs_f09_retail_capex_per_store_csr_xdep_10d_jerk_v132_signal,
    f09rcs_f09_retail_capex_per_store_csr_xdep_21d_jerk_v133_signal,
    f09rcs_f09_retail_capex_per_store_csr_xdep_42d_jerk_v134_signal,
    f09rcs_f09_retail_capex_per_store_csr_xdep_63d_jerk_v135_signal,
    f09rcs_f09_retail_capex_per_store_csr_xdep_126d_jerk_v136_signal,
    f09rcs_f09_retail_capex_per_store_csr_xdep_189d_jerk_v137_signal,
    f09rcs_f09_retail_capex_per_store_csr_xdep_252d_jerk_v138_signal,
    f09rcs_f09_retail_capex_per_store_csr_xdep_378d_jerk_v139_signal,
    f09rcs_f09_retail_capex_per_store_csr_xdep_504d_jerk_v140_signal,
    f09rcs_f09_retail_capex_per_store_csr_diff_5d_jerk_v141_signal,
    f09rcs_f09_retail_capex_per_store_csr_diff_10d_jerk_v142_signal,
    f09rcs_f09_retail_capex_per_store_csr_diff_21d_jerk_v143_signal,
    f09rcs_f09_retail_capex_per_store_csr_diff_42d_jerk_v144_signal,
    f09rcs_f09_retail_capex_per_store_csr_diff_63d_jerk_v145_signal,
    f09rcs_f09_retail_capex_per_store_csr_diff_126d_jerk_v146_signal,
    f09rcs_f09_retail_capex_per_store_csr_diff_189d_jerk_v147_signal,
    f09rcs_f09_retail_capex_per_store_csr_diff_252d_jerk_v148_signal,
    f09rcs_f09_retail_capex_per_store_csr_diff_378d_jerk_v149_signal,
    f09rcs_f09_retail_capex_per_store_csr_diff_504d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_RETAIL_CAPEX_PER_STORE_REGISTRY_JERK_001_150 = REGISTRY


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
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "inventory": inventory, "ppnenet": ppnenet,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f09_capex_to_ppe", "_f09_renewal_intensity", "_f09_capex_store_ratio")
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
    print(f"OK f09_retail_capex_per_store_jerk_001_150_claude: {n_features} features pass")
