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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)

# ===== folder domain primitives =====
def _f28_low_vol_signal(closeadj, w):
    rets = closeadj.pct_change()
    return -_std(rets, w)


def _f28_steady_earnings_growth(netinc, w):
    g = netinc.pct_change(periods=w)
    return _mean(g, w) - _std(g, w)


def _f28_compounder_composite(closeadj, netinc, w):
    rets = closeadj.pct_change()
    vol = _std(rets, w)
    g = netinc.pct_change(periods=w)
    return _mean(g, w) / vol.replace(0, np.nan)


# ===== features =====

def f28qcc_f28_quiet_consumer_compounder_lowvol_5d_jerk_v001_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 5)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_5d_jerk_v002_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 5)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_5d_jerk_v003_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 5)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_5d_jerk_v004_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 5)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_5d_jerk_v005_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 5)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_10d_jerk_v006_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 10)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_10d_jerk_v007_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 10)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_10d_jerk_v008_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 10)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_10d_jerk_v009_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 10)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_10d_jerk_v010_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 10)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_21d_jerk_v011_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 21)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_21d_jerk_v012_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 21)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_21d_jerk_v013_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 21)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_21d_jerk_v014_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 21)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_21d_jerk_v015_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 21)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_42d_jerk_v016_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 42)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_42d_jerk_v017_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 42)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_42d_jerk_v018_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 42)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_42d_jerk_v019_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 42)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_42d_jerk_v020_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 42)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_63d_jerk_v021_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 63)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_63d_jerk_v022_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 63)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_63d_jerk_v023_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 63)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_63d_jerk_v024_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 63)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_63d_jerk_v025_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 63)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_126d_jerk_v026_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 126)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_126d_jerk_v027_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 126)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_126d_jerk_v028_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 126)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_126d_jerk_v029_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 126)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_126d_jerk_v030_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 126)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_189d_jerk_v031_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 189)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_189d_jerk_v032_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 189)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_189d_jerk_v033_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 189)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_189d_jerk_v034_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 189)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_189d_jerk_v035_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 189)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_252d_jerk_v036_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 252)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_252d_jerk_v037_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 252)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_252d_jerk_v038_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 252)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_252d_jerk_v039_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 252)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_252d_jerk_v040_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 252)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_378d_jerk_v041_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 378)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_378d_jerk_v042_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 378)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_378d_jerk_v043_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 378)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_378d_jerk_v044_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 378)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_378d_jerk_v045_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 378)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_504d_jerk_v046_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 504)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_504d_jerk_v047_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 504)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_504d_jerk_v048_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 504)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_504d_jerk_v049_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 504)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvol_504d_jerk_v050_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 504)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_5d_jerk_v051_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 5)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_5d_jerk_v052_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 5)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_5d_jerk_v053_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 5)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_5d_jerk_v054_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 5)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_5d_jerk_v055_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 5)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_10d_jerk_v056_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 10)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_10d_jerk_v057_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 10)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_10d_jerk_v058_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 10)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_10d_jerk_v059_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 10)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_10d_jerk_v060_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 10)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_21d_jerk_v061_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 21)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_21d_jerk_v062_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 21)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_21d_jerk_v063_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 21)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_21d_jerk_v064_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 21)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_21d_jerk_v065_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 21)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_42d_jerk_v066_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 42)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_42d_jerk_v067_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 42)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_42d_jerk_v068_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 42)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_42d_jerk_v069_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 42)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_42d_jerk_v070_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 42)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_63d_jerk_v071_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 63)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_63d_jerk_v072_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 63)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_63d_jerk_v073_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 63)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_63d_jerk_v074_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 63)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_63d_jerk_v075_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 63)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_126d_jerk_v076_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 126)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_126d_jerk_v077_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 126)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_126d_jerk_v078_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 126)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_126d_jerk_v079_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 126)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_126d_jerk_v080_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 126)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_189d_jerk_v081_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 189)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_189d_jerk_v082_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 189)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_189d_jerk_v083_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 189)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_189d_jerk_v084_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 189)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_189d_jerk_v085_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 189)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_252d_jerk_v086_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 252)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_252d_jerk_v087_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 252)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_252d_jerk_v088_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 252)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_252d_jerk_v089_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 252)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_252d_jerk_v090_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 252)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_378d_jerk_v091_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 378)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_378d_jerk_v092_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 378)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_378d_jerk_v093_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 378)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_378d_jerk_v094_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 378)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_378d_jerk_v095_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 378)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_504d_jerk_v096_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 504)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_504d_jerk_v097_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 504)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_504d_jerk_v098_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 504)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_504d_jerk_v099_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 504)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_eg_504d_jerk_v100_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 504)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_5d_jerk_v101_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 5)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_5d_jerk_v102_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 5)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_5d_jerk_v103_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 5)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_5d_jerk_v104_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 5)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_5d_jerk_v105_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 5)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_10d_jerk_v106_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 10)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_10d_jerk_v107_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 10)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_10d_jerk_v108_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 10)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_10d_jerk_v109_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 10)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_10d_jerk_v110_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 10)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_21d_jerk_v111_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 21)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_21d_jerk_v112_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 21)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_21d_jerk_v113_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 21)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_21d_jerk_v114_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 21)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_21d_jerk_v115_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 21)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_42d_jerk_v116_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 42)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_42d_jerk_v117_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 42)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_42d_jerk_v118_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 42)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_42d_jerk_v119_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 42)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_42d_jerk_v120_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 42)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_63d_jerk_v121_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 63)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_63d_jerk_v122_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 63)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_63d_jerk_v123_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 63)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_63d_jerk_v124_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 63)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_63d_jerk_v125_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 63)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_126d_jerk_v126_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 126)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_126d_jerk_v127_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 126)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_126d_jerk_v128_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 126)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_126d_jerk_v129_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 126)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_126d_jerk_v130_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 126)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_189d_jerk_v131_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 189)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_189d_jerk_v132_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 189)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_189d_jerk_v133_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 189)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_189d_jerk_v134_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 189)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_189d_jerk_v135_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 189)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_252d_jerk_v136_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 252)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_252d_jerk_v137_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 252)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_252d_jerk_v138_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 252)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_252d_jerk_v139_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 252)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_252d_jerk_v140_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 252)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_378d_jerk_v141_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 378)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_378d_jerk_v142_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 378)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_378d_jerk_v143_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 378)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_378d_jerk_v144_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 378)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_378d_jerk_v145_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 378)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_504d_jerk_v146_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 504)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_504d_jerk_v147_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 504)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_504d_jerk_v148_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 504)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_504d_jerk_v149_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 504)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_comp_504d_jerk_v150_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 504)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f28qcc_f28_quiet_consumer_compounder_lowvol_5d_jerk_v001_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_5d_jerk_v002_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_5d_jerk_v003_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_5d_jerk_v004_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_5d_jerk_v005_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_10d_jerk_v006_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_10d_jerk_v007_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_10d_jerk_v008_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_10d_jerk_v009_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_10d_jerk_v010_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_21d_jerk_v011_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_21d_jerk_v012_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_21d_jerk_v013_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_21d_jerk_v014_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_21d_jerk_v015_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_42d_jerk_v016_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_42d_jerk_v017_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_42d_jerk_v018_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_42d_jerk_v019_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_42d_jerk_v020_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_63d_jerk_v021_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_63d_jerk_v022_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_63d_jerk_v023_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_63d_jerk_v024_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_63d_jerk_v025_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_126d_jerk_v026_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_126d_jerk_v027_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_126d_jerk_v028_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_126d_jerk_v029_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_126d_jerk_v030_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_189d_jerk_v031_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_189d_jerk_v032_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_189d_jerk_v033_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_189d_jerk_v034_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_189d_jerk_v035_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_252d_jerk_v036_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_252d_jerk_v037_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_252d_jerk_v038_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_252d_jerk_v039_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_252d_jerk_v040_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_378d_jerk_v041_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_378d_jerk_v042_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_378d_jerk_v043_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_378d_jerk_v044_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_378d_jerk_v045_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_504d_jerk_v046_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_504d_jerk_v047_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_504d_jerk_v048_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_504d_jerk_v049_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvol_504d_jerk_v050_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_5d_jerk_v051_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_5d_jerk_v052_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_5d_jerk_v053_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_5d_jerk_v054_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_5d_jerk_v055_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_10d_jerk_v056_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_10d_jerk_v057_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_10d_jerk_v058_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_10d_jerk_v059_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_10d_jerk_v060_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_21d_jerk_v061_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_21d_jerk_v062_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_21d_jerk_v063_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_21d_jerk_v064_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_21d_jerk_v065_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_42d_jerk_v066_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_42d_jerk_v067_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_42d_jerk_v068_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_42d_jerk_v069_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_42d_jerk_v070_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_63d_jerk_v071_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_63d_jerk_v072_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_63d_jerk_v073_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_63d_jerk_v074_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_63d_jerk_v075_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_126d_jerk_v076_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_126d_jerk_v077_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_126d_jerk_v078_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_126d_jerk_v079_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_126d_jerk_v080_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_189d_jerk_v081_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_189d_jerk_v082_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_189d_jerk_v083_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_189d_jerk_v084_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_189d_jerk_v085_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_252d_jerk_v086_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_252d_jerk_v087_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_252d_jerk_v088_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_252d_jerk_v089_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_252d_jerk_v090_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_378d_jerk_v091_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_378d_jerk_v092_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_378d_jerk_v093_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_378d_jerk_v094_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_378d_jerk_v095_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_504d_jerk_v096_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_504d_jerk_v097_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_504d_jerk_v098_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_504d_jerk_v099_signal,
    f28qcc_f28_quiet_consumer_compounder_eg_504d_jerk_v100_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_5d_jerk_v101_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_5d_jerk_v102_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_5d_jerk_v103_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_5d_jerk_v104_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_5d_jerk_v105_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_10d_jerk_v106_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_10d_jerk_v107_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_10d_jerk_v108_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_10d_jerk_v109_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_10d_jerk_v110_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_21d_jerk_v111_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_21d_jerk_v112_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_21d_jerk_v113_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_21d_jerk_v114_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_21d_jerk_v115_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_42d_jerk_v116_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_42d_jerk_v117_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_42d_jerk_v118_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_42d_jerk_v119_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_42d_jerk_v120_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_63d_jerk_v121_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_63d_jerk_v122_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_63d_jerk_v123_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_63d_jerk_v124_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_63d_jerk_v125_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_126d_jerk_v126_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_126d_jerk_v127_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_126d_jerk_v128_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_126d_jerk_v129_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_126d_jerk_v130_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_189d_jerk_v131_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_189d_jerk_v132_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_189d_jerk_v133_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_189d_jerk_v134_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_189d_jerk_v135_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_252d_jerk_v136_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_252d_jerk_v137_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_252d_jerk_v138_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_252d_jerk_v139_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_252d_jerk_v140_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_378d_jerk_v141_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_378d_jerk_v142_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_378d_jerk_v143_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_378d_jerk_v144_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_378d_jerk_v145_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_504d_jerk_v146_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_504d_jerk_v147_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_504d_jerk_v148_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_504d_jerk_v149_signal,
    f28qcc_f28_quiet_consumer_compounder_comp_504d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values() if p.default is inspect.Parameter.empty]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_QUIET_CONSUMER_COMPOUNDER_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    netinc = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    ebitda = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    eps    = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1, n+1), name="eps")
    cols = {"closeadj": closeadj, "netinc": netinc, "ebitda": ebitda, "eps": eps}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f28_low_vol_signal", "_f28_steady_earnings_growth", "_f28_compounder_composite",)
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
    print(f"OK f28_quiet_consumer_compounder_3rd_derivatives_001_150_claude: {n_features} features pass")
