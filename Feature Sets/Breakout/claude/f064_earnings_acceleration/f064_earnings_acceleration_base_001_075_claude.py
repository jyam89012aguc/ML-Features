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
def _f064_eps_growth(eps, w):
    return eps.diff(periods=w) / eps.shift(w).abs().replace(0, np.nan)


def _f064_eps_accel(eps, w):
    g = eps.diff(periods=w) / eps.shift(w).abs().replace(0, np.nan)
    return g - g.shift(w)


def _f064_earnings_inflection(eps, netinc, w):
    g_eps = eps.diff(periods=w) / eps.shift(w).abs().replace(0, np.nan)
    g_ni = netinc.pct_change(periods=w)
    return (g_eps + g_ni) * 0.5


# ===== features =====

def f064eac_f064_earnings_acceleration_raw_5d_base_v001_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 5)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_m21_10d_base_v002_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 10)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_m63_21d_base_v003_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_s21_42d_base_v004_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 42)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_s63_63d_base_v005_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_z21_126d_base_v006_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 126)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_z63_189d_base_v007_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 189)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_z252_252d_base_v008_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_e21_378d_base_v009_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 378)
    result = (base).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_e63_504d_base_v010_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 504)
    result = (base).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_e126_5d_base_v011_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 5)
    result = (base).ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_cum_10d_base_v012_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 10)
    result = (base).fillna(0).cumsum() / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_log_21d_base_v013_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 21)
    result = np.log1p((base).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_sgn_42d_base_v014_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 42)
    result = np.sign(base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_r63_63d_base_v015_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 63)
    result = (base).rolling(63, min_periods=21).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_r252_126d_base_v016_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 126)
    result = (base).rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_mc_189d_base_v017_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 189)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_dc_252d_base_v018_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 252)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_pc5_378d_base_v019_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 378)
    result = (base).pct_change(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_pc21_504d_base_v020_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 504)
    result = (base).pct_change(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_d21_5d_base_v021_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 5)
    result = (base).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_sq_10d_base_v022_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 10)
    result = (base) * (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_cb_21d_base_v023_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 21)
    result = (base) ** 3 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_sqr_42d_base_v024_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 42)
    result = np.sqrt((base).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_m126_63d_base_v025_signal(eps, netinc, closeadj):
    base = _f064_eps_growth(eps, 63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_raw_126d_base_v026_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 126)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_m21_189d_base_v027_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 189)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_m63_252d_base_v028_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_s21_378d_base_v029_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 378)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_s63_504d_base_v030_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 504)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_z21_5d_base_v031_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 5)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_z63_10d_base_v032_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 10)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_z252_21d_base_v033_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_e21_42d_base_v034_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 42)
    result = (base).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_e63_63d_base_v035_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 63)
    result = (base).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_e126_126d_base_v036_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 126)
    result = (base).ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_cum_189d_base_v037_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 189)
    result = (base).fillna(0).cumsum() / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_log_252d_base_v038_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 252)
    result = np.log1p((base).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_sgn_378d_base_v039_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 378)
    result = np.sign(base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_r63_504d_base_v040_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 504)
    result = (base).rolling(63, min_periods=21).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_r252_5d_base_v041_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 5)
    result = (base).rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_mc_10d_base_v042_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 10)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_dc_21d_base_v043_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 21)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_pc5_42d_base_v044_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 42)
    result = (base).pct_change(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_pc21_63d_base_v045_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 63)
    result = (base).pct_change(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_d21_126d_base_v046_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 126)
    result = (base).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_sq_189d_base_v047_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 189)
    result = (base) * (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_cb_252d_base_v048_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 252)
    result = (base) ** 3 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_sqr_378d_base_v049_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 378)
    result = np.sqrt((base).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_m126_504d_base_v050_signal(eps, netinc, closeadj):
    base = _f064_eps_accel(eps, 504)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_raw_5d_base_v051_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 5)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_m21_10d_base_v052_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 10)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_m63_21d_base_v053_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_s21_42d_base_v054_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 42)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_s63_63d_base_v055_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_z21_126d_base_v056_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 126)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_z63_189d_base_v057_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 189)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_z252_252d_base_v058_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_e21_378d_base_v059_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 378)
    result = (base).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_e63_504d_base_v060_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 504)
    result = (base).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_e126_5d_base_v061_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 5)
    result = (base).ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_cum_10d_base_v062_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 10)
    result = (base).fillna(0).cumsum() / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_log_21d_base_v063_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 21)
    result = np.log1p((base).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_sgn_42d_base_v064_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 42)
    result = np.sign(base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_r63_63d_base_v065_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 63)
    result = (base).rolling(63, min_periods=21).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_r252_126d_base_v066_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 126)
    result = (base).rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_mc_189d_base_v067_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 189)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_dc_252d_base_v068_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 252)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_pc5_378d_base_v069_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 378)
    result = (base).pct_change(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_pc21_504d_base_v070_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 504)
    result = (base).pct_change(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_d21_5d_base_v071_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 5)
    result = (base).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_sq_10d_base_v072_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 10)
    result = (base) * (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_cb_21d_base_v073_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 21)
    result = (base) ** 3 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_sqr_42d_base_v074_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 42)
    result = np.sqrt((base).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f064eac_f064_earnings_acceleration_m126_63d_base_v075_signal(eps, netinc, closeadj):
    base = _f064_earnings_inflection(eps, netinc, 63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f064eac_f064_earnings_acceleration_raw_5d_base_v001_signal,
    f064eac_f064_earnings_acceleration_m21_10d_base_v002_signal,
    f064eac_f064_earnings_acceleration_m63_21d_base_v003_signal,
    f064eac_f064_earnings_acceleration_s21_42d_base_v004_signal,
    f064eac_f064_earnings_acceleration_s63_63d_base_v005_signal,
    f064eac_f064_earnings_acceleration_z21_126d_base_v006_signal,
    f064eac_f064_earnings_acceleration_z63_189d_base_v007_signal,
    f064eac_f064_earnings_acceleration_z252_252d_base_v008_signal,
    f064eac_f064_earnings_acceleration_e21_378d_base_v009_signal,
    f064eac_f064_earnings_acceleration_e63_504d_base_v010_signal,
    f064eac_f064_earnings_acceleration_e126_5d_base_v011_signal,
    f064eac_f064_earnings_acceleration_cum_10d_base_v012_signal,
    f064eac_f064_earnings_acceleration_log_21d_base_v013_signal,
    f064eac_f064_earnings_acceleration_sgn_42d_base_v014_signal,
    f064eac_f064_earnings_acceleration_r63_63d_base_v015_signal,
    f064eac_f064_earnings_acceleration_r252_126d_base_v016_signal,
    f064eac_f064_earnings_acceleration_mc_189d_base_v017_signal,
    f064eac_f064_earnings_acceleration_dc_252d_base_v018_signal,
    f064eac_f064_earnings_acceleration_pc5_378d_base_v019_signal,
    f064eac_f064_earnings_acceleration_pc21_504d_base_v020_signal,
    f064eac_f064_earnings_acceleration_d21_5d_base_v021_signal,
    f064eac_f064_earnings_acceleration_sq_10d_base_v022_signal,
    f064eac_f064_earnings_acceleration_cb_21d_base_v023_signal,
    f064eac_f064_earnings_acceleration_sqr_42d_base_v024_signal,
    f064eac_f064_earnings_acceleration_m126_63d_base_v025_signal,
    f064eac_f064_earnings_acceleration_raw_126d_base_v026_signal,
    f064eac_f064_earnings_acceleration_m21_189d_base_v027_signal,
    f064eac_f064_earnings_acceleration_m63_252d_base_v028_signal,
    f064eac_f064_earnings_acceleration_s21_378d_base_v029_signal,
    f064eac_f064_earnings_acceleration_s63_504d_base_v030_signal,
    f064eac_f064_earnings_acceleration_z21_5d_base_v031_signal,
    f064eac_f064_earnings_acceleration_z63_10d_base_v032_signal,
    f064eac_f064_earnings_acceleration_z252_21d_base_v033_signal,
    f064eac_f064_earnings_acceleration_e21_42d_base_v034_signal,
    f064eac_f064_earnings_acceleration_e63_63d_base_v035_signal,
    f064eac_f064_earnings_acceleration_e126_126d_base_v036_signal,
    f064eac_f064_earnings_acceleration_cum_189d_base_v037_signal,
    f064eac_f064_earnings_acceleration_log_252d_base_v038_signal,
    f064eac_f064_earnings_acceleration_sgn_378d_base_v039_signal,
    f064eac_f064_earnings_acceleration_r63_504d_base_v040_signal,
    f064eac_f064_earnings_acceleration_r252_5d_base_v041_signal,
    f064eac_f064_earnings_acceleration_mc_10d_base_v042_signal,
    f064eac_f064_earnings_acceleration_dc_21d_base_v043_signal,
    f064eac_f064_earnings_acceleration_pc5_42d_base_v044_signal,
    f064eac_f064_earnings_acceleration_pc21_63d_base_v045_signal,
    f064eac_f064_earnings_acceleration_d21_126d_base_v046_signal,
    f064eac_f064_earnings_acceleration_sq_189d_base_v047_signal,
    f064eac_f064_earnings_acceleration_cb_252d_base_v048_signal,
    f064eac_f064_earnings_acceleration_sqr_378d_base_v049_signal,
    f064eac_f064_earnings_acceleration_m126_504d_base_v050_signal,
    f064eac_f064_earnings_acceleration_raw_5d_base_v051_signal,
    f064eac_f064_earnings_acceleration_m21_10d_base_v052_signal,
    f064eac_f064_earnings_acceleration_m63_21d_base_v053_signal,
    f064eac_f064_earnings_acceleration_s21_42d_base_v054_signal,
    f064eac_f064_earnings_acceleration_s63_63d_base_v055_signal,
    f064eac_f064_earnings_acceleration_z21_126d_base_v056_signal,
    f064eac_f064_earnings_acceleration_z63_189d_base_v057_signal,
    f064eac_f064_earnings_acceleration_z252_252d_base_v058_signal,
    f064eac_f064_earnings_acceleration_e21_378d_base_v059_signal,
    f064eac_f064_earnings_acceleration_e63_504d_base_v060_signal,
    f064eac_f064_earnings_acceleration_e126_5d_base_v061_signal,
    f064eac_f064_earnings_acceleration_cum_10d_base_v062_signal,
    f064eac_f064_earnings_acceleration_log_21d_base_v063_signal,
    f064eac_f064_earnings_acceleration_sgn_42d_base_v064_signal,
    f064eac_f064_earnings_acceleration_r63_63d_base_v065_signal,
    f064eac_f064_earnings_acceleration_r252_126d_base_v066_signal,
    f064eac_f064_earnings_acceleration_mc_189d_base_v067_signal,
    f064eac_f064_earnings_acceleration_dc_252d_base_v068_signal,
    f064eac_f064_earnings_acceleration_pc5_378d_base_v069_signal,
    f064eac_f064_earnings_acceleration_pc21_504d_base_v070_signal,
    f064eac_f064_earnings_acceleration_d21_5d_base_v071_signal,
    f064eac_f064_earnings_acceleration_sq_10d_base_v072_signal,
    f064eac_f064_earnings_acceleration_cb_21d_base_v073_signal,
    f064eac_f064_earnings_acceleration_sqr_42d_base_v074_signal,
    f064eac_f064_earnings_acceleration_m126_63d_base_v075_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F064_EARNINGS_ACCELERATION_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f064_eps_growth", "_f064_eps_accel", "_f064_earnings_inflection")
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
    print(f"OK f064_earnings_acceleration_001_075_claude: {n_features} features pass")
