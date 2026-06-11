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
    return s.ewm(span=w, adjust=False, min_periods=max(1, w // 2)).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f39_margin_range(ebitdamargin, w):
    """Cyclical margin range: max-min over window."""
    mx = ebitdamargin.rolling(w, min_periods=max(2, w // 2)).max()
    mn = ebitdamargin.rolling(w, min_periods=max(2, w // 2)).min()
    return mx - mn


def _f39_margin_trough_position(grossmargin, w):
    """Where current margin sits in trough-to-peak range (0-1)."""
    mx = grossmargin.rolling(w, min_periods=max(2, w // 2)).max()
    mn = grossmargin.rolling(w, min_periods=max(2, w // 2)).min()
    rng = (mx - mn).replace(0, np.nan)
    return (grossmargin - mn) / rng


def _f39_margin_recovery_strength(ebitdamargin, w):
    """Recovery: current minus trough scaled by range."""
    mx = ebitdamargin.rolling(w, min_periods=max(2, w // 2)).max()
    mn = ebitdamargin.rolling(w, min_periods=max(2, w // 2)).min()
    rng = (mx - mn).replace(0, np.nan)
    return (ebitdamargin - mn) / rng - 0.5


def f39mtp_f39_margin_trough_to_peak_range_grossmargin_5d_5d_slope_v001_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 5)
    base_ = r * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_grossmargin_10d_21d_slope_v002_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 10)
    base_ = r * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_grossmargin_21d_63d_slope_v003_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 21)
    base_ = r * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_grossmargin_42d_126d_slope_v004_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 42)
    base_ = r * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_grossmargin_63d_252d_slope_v005_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 63)
    base_ = r * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_grossmargin_126d_5d_slope_v006_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 126)
    base_ = r * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_grossmargin_189d_21d_slope_v007_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 189)
    base_ = r * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_grossmargin_252d_63d_slope_v008_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 252)
    base_ = r * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_grossmargin_378d_126d_slope_v009_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 378)
    base_ = r * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_grossmargin_504d_252d_slope_v010_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 504)
    base_ = r * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_ebitdamargin_5d_5d_slope_v011_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 5)
    base_ = r * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_ebitdamargin_10d_21d_slope_v012_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 10)
    base_ = r * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_ebitdamargin_21d_63d_slope_v013_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 21)
    base_ = r * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_ebitdamargin_42d_126d_slope_v014_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 42)
    base_ = r * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_ebitdamargin_63d_252d_slope_v015_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 63)
    base_ = r * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_ebitdamargin_126d_5d_slope_v016_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 126)
    base_ = r * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_ebitdamargin_189d_21d_slope_v017_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 189)
    base_ = r * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_ebitdamargin_252d_63d_slope_v018_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 252)
    base_ = r * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_ebitdamargin_378d_126d_slope_v019_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 378)
    base_ = r * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_ebitdamargin_504d_252d_slope_v020_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 504)
    base_ = r * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_netmargin_5d_5d_slope_v021_signal(netmargin, closeadj):
    r = _f39_margin_range(netmargin, 5)
    base_ = r * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_netmargin_10d_21d_slope_v022_signal(netmargin, closeadj):
    r = _f39_margin_range(netmargin, 10)
    base_ = r * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_netmargin_21d_63d_slope_v023_signal(netmargin, closeadj):
    r = _f39_margin_range(netmargin, 21)
    base_ = r * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_netmargin_42d_126d_slope_v024_signal(netmargin, closeadj):
    r = _f39_margin_range(netmargin, 42)
    base_ = r * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_netmargin_63d_252d_slope_v025_signal(netmargin, closeadj):
    r = _f39_margin_range(netmargin, 63)
    base_ = r * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_netmargin_126d_5d_slope_v026_signal(netmargin, closeadj):
    r = _f39_margin_range(netmargin, 126)
    base_ = r * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_netmargin_189d_21d_slope_v027_signal(netmargin, closeadj):
    r = _f39_margin_range(netmargin, 189)
    base_ = r * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_netmargin_252d_63d_slope_v028_signal(netmargin, closeadj):
    r = _f39_margin_range(netmargin, 252)
    base_ = r * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_netmargin_378d_126d_slope_v029_signal(netmargin, closeadj):
    r = _f39_margin_range(netmargin, 378)
    base_ = r * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_range_netmargin_504d_252d_slope_v030_signal(netmargin, closeadj):
    r = _f39_margin_range(netmargin, 504)
    base_ = r * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_grossmargin_5d_5d_slope_v031_signal(grossmargin, closeadj):
    t = _f39_margin_trough_position(grossmargin, 5)
    base_ = t * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_grossmargin_10d_21d_slope_v032_signal(grossmargin, closeadj):
    t = _f39_margin_trough_position(grossmargin, 10)
    base_ = t * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_grossmargin_21d_63d_slope_v033_signal(grossmargin, closeadj):
    t = _f39_margin_trough_position(grossmargin, 21)
    base_ = t * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_grossmargin_42d_126d_slope_v034_signal(grossmargin, closeadj):
    t = _f39_margin_trough_position(grossmargin, 42)
    base_ = t * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_grossmargin_63d_252d_slope_v035_signal(grossmargin, closeadj):
    t = _f39_margin_trough_position(grossmargin, 63)
    base_ = t * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_grossmargin_126d_5d_slope_v036_signal(grossmargin, closeadj):
    t = _f39_margin_trough_position(grossmargin, 126)
    base_ = t * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_grossmargin_189d_21d_slope_v037_signal(grossmargin, closeadj):
    t = _f39_margin_trough_position(grossmargin, 189)
    base_ = t * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_grossmargin_252d_63d_slope_v038_signal(grossmargin, closeadj):
    t = _f39_margin_trough_position(grossmargin, 252)
    base_ = t * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_grossmargin_378d_126d_slope_v039_signal(grossmargin, closeadj):
    t = _f39_margin_trough_position(grossmargin, 378)
    base_ = t * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_grossmargin_504d_252d_slope_v040_signal(grossmargin, closeadj):
    t = _f39_margin_trough_position(grossmargin, 504)
    base_ = t * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_ebitdamargin_5d_5d_slope_v041_signal(ebitdamargin, closeadj):
    t = _f39_margin_trough_position(ebitdamargin, 5)
    base_ = t * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_ebitdamargin_10d_21d_slope_v042_signal(ebitdamargin, closeadj):
    t = _f39_margin_trough_position(ebitdamargin, 10)
    base_ = t * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_ebitdamargin_21d_63d_slope_v043_signal(ebitdamargin, closeadj):
    t = _f39_margin_trough_position(ebitdamargin, 21)
    base_ = t * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_ebitdamargin_42d_126d_slope_v044_signal(ebitdamargin, closeadj):
    t = _f39_margin_trough_position(ebitdamargin, 42)
    base_ = t * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_ebitdamargin_63d_252d_slope_v045_signal(ebitdamargin, closeadj):
    t = _f39_margin_trough_position(ebitdamargin, 63)
    base_ = t * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_ebitdamargin_126d_5d_slope_v046_signal(ebitdamargin, closeadj):
    t = _f39_margin_trough_position(ebitdamargin, 126)
    base_ = t * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_ebitdamargin_189d_21d_slope_v047_signal(ebitdamargin, closeadj):
    t = _f39_margin_trough_position(ebitdamargin, 189)
    base_ = t * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_ebitdamargin_252d_63d_slope_v048_signal(ebitdamargin, closeadj):
    t = _f39_margin_trough_position(ebitdamargin, 252)
    base_ = t * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_ebitdamargin_378d_126d_slope_v049_signal(ebitdamargin, closeadj):
    t = _f39_margin_trough_position(ebitdamargin, 378)
    base_ = t * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_ebitdamargin_504d_252d_slope_v050_signal(ebitdamargin, closeadj):
    t = _f39_margin_trough_position(ebitdamargin, 504)
    base_ = t * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_netmargin_5d_5d_slope_v051_signal(netmargin, closeadj):
    t = _f39_margin_trough_position(netmargin, 5)
    base_ = t * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_netmargin_10d_21d_slope_v052_signal(netmargin, closeadj):
    t = _f39_margin_trough_position(netmargin, 10)
    base_ = t * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_netmargin_21d_63d_slope_v053_signal(netmargin, closeadj):
    t = _f39_margin_trough_position(netmargin, 21)
    base_ = t * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_netmargin_42d_126d_slope_v054_signal(netmargin, closeadj):
    t = _f39_margin_trough_position(netmargin, 42)
    base_ = t * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_netmargin_63d_252d_slope_v055_signal(netmargin, closeadj):
    t = _f39_margin_trough_position(netmargin, 63)
    base_ = t * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_netmargin_126d_5d_slope_v056_signal(netmargin, closeadj):
    t = _f39_margin_trough_position(netmargin, 126)
    base_ = t * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_netmargin_189d_21d_slope_v057_signal(netmargin, closeadj):
    t = _f39_margin_trough_position(netmargin, 189)
    base_ = t * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_netmargin_252d_63d_slope_v058_signal(netmargin, closeadj):
    t = _f39_margin_trough_position(netmargin, 252)
    base_ = t * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_netmargin_378d_126d_slope_v059_signal(netmargin, closeadj):
    t = _f39_margin_trough_position(netmargin, 378)
    base_ = t * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_trough_netmargin_504d_252d_slope_v060_signal(netmargin, closeadj):
    t = _f39_margin_trough_position(netmargin, 504)
    base_ = t * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_grossmargin_5d_5d_slope_v061_signal(grossmargin, closeadj):
    rec = _f39_margin_recovery_strength(grossmargin, 5)
    base_ = rec * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_grossmargin_10d_21d_slope_v062_signal(grossmargin, closeadj):
    rec = _f39_margin_recovery_strength(grossmargin, 10)
    base_ = rec * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_grossmargin_21d_63d_slope_v063_signal(grossmargin, closeadj):
    rec = _f39_margin_recovery_strength(grossmargin, 21)
    base_ = rec * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_grossmargin_42d_126d_slope_v064_signal(grossmargin, closeadj):
    rec = _f39_margin_recovery_strength(grossmargin, 42)
    base_ = rec * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_grossmargin_63d_252d_slope_v065_signal(grossmargin, closeadj):
    rec = _f39_margin_recovery_strength(grossmargin, 63)
    base_ = rec * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_grossmargin_126d_5d_slope_v066_signal(grossmargin, closeadj):
    rec = _f39_margin_recovery_strength(grossmargin, 126)
    base_ = rec * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_grossmargin_189d_21d_slope_v067_signal(grossmargin, closeadj):
    rec = _f39_margin_recovery_strength(grossmargin, 189)
    base_ = rec * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_grossmargin_252d_63d_slope_v068_signal(grossmargin, closeadj):
    rec = _f39_margin_recovery_strength(grossmargin, 252)
    base_ = rec * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_grossmargin_378d_126d_slope_v069_signal(grossmargin, closeadj):
    rec = _f39_margin_recovery_strength(grossmargin, 378)
    base_ = rec * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_grossmargin_504d_252d_slope_v070_signal(grossmargin, closeadj):
    rec = _f39_margin_recovery_strength(grossmargin, 504)
    base_ = rec * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_ebitdamargin_5d_5d_slope_v071_signal(ebitdamargin, closeadj):
    rec = _f39_margin_recovery_strength(ebitdamargin, 5)
    base_ = rec * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_ebitdamargin_10d_21d_slope_v072_signal(ebitdamargin, closeadj):
    rec = _f39_margin_recovery_strength(ebitdamargin, 10)
    base_ = rec * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_ebitdamargin_21d_63d_slope_v073_signal(ebitdamargin, closeadj):
    rec = _f39_margin_recovery_strength(ebitdamargin, 21)
    base_ = rec * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_ebitdamargin_42d_126d_slope_v074_signal(ebitdamargin, closeadj):
    rec = _f39_margin_recovery_strength(ebitdamargin, 42)
    base_ = rec * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_ebitdamargin_63d_252d_slope_v075_signal(ebitdamargin, closeadj):
    rec = _f39_margin_recovery_strength(ebitdamargin, 63)
    base_ = rec * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_ebitdamargin_126d_5d_slope_v076_signal(ebitdamargin, closeadj):
    rec = _f39_margin_recovery_strength(ebitdamargin, 126)
    base_ = rec * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_ebitdamargin_189d_21d_slope_v077_signal(ebitdamargin, closeadj):
    rec = _f39_margin_recovery_strength(ebitdamargin, 189)
    base_ = rec * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_ebitdamargin_252d_63d_slope_v078_signal(ebitdamargin, closeadj):
    rec = _f39_margin_recovery_strength(ebitdamargin, 252)
    base_ = rec * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_ebitdamargin_378d_126d_slope_v079_signal(ebitdamargin, closeadj):
    rec = _f39_margin_recovery_strength(ebitdamargin, 378)
    base_ = rec * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_ebitdamargin_504d_252d_slope_v080_signal(ebitdamargin, closeadj):
    rec = _f39_margin_recovery_strength(ebitdamargin, 504)
    base_ = rec * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_netmargin_5d_5d_slope_v081_signal(netmargin, closeadj):
    rec = _f39_margin_recovery_strength(netmargin, 5)
    base_ = rec * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_netmargin_10d_21d_slope_v082_signal(netmargin, closeadj):
    rec = _f39_margin_recovery_strength(netmargin, 10)
    base_ = rec * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_netmargin_21d_63d_slope_v083_signal(netmargin, closeadj):
    rec = _f39_margin_recovery_strength(netmargin, 21)
    base_ = rec * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_netmargin_42d_126d_slope_v084_signal(netmargin, closeadj):
    rec = _f39_margin_recovery_strength(netmargin, 42)
    base_ = rec * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_netmargin_63d_252d_slope_v085_signal(netmargin, closeadj):
    rec = _f39_margin_recovery_strength(netmargin, 63)
    base_ = rec * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_netmargin_126d_5d_slope_v086_signal(netmargin, closeadj):
    rec = _f39_margin_recovery_strength(netmargin, 126)
    base_ = rec * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_netmargin_189d_21d_slope_v087_signal(netmargin, closeadj):
    rec = _f39_margin_recovery_strength(netmargin, 189)
    base_ = rec * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_netmargin_252d_63d_slope_v088_signal(netmargin, closeadj):
    rec = _f39_margin_recovery_strength(netmargin, 252)
    base_ = rec * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_netmargin_378d_126d_slope_v089_signal(netmargin, closeadj):
    rec = _f39_margin_recovery_strength(netmargin, 378)
    base_ = rec * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recovery_netmargin_504d_252d_slope_v090_signal(netmargin, closeadj):
    rec = _f39_margin_recovery_strength(netmargin, 504)
    base_ = rec * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngxrec_grossmargin_63d_5d_slope_v091_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 63)
    rec = _f39_margin_recovery_strength(grossmargin, 63)
    base_ = (r * rec) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngxrec_grossmargin_126d_21d_slope_v092_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 126)
    rec = _f39_margin_recovery_strength(grossmargin, 126)
    base_ = (r * rec) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngxrec_grossmargin_252d_63d_slope_v093_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 252)
    rec = _f39_margin_recovery_strength(grossmargin, 252)
    base_ = (r * rec) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngxrec_grossmargin_504d_126d_slope_v094_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 504)
    rec = _f39_margin_recovery_strength(grossmargin, 504)
    base_ = (r * rec) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngxrec_ebitdamargin_63d_252d_slope_v095_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 63)
    rec = _f39_margin_recovery_strength(ebitdamargin, 63)
    base_ = (r * rec) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngxrec_ebitdamargin_126d_5d_slope_v096_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 126)
    rec = _f39_margin_recovery_strength(ebitdamargin, 126)
    base_ = (r * rec) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngxrec_ebitdamargin_252d_21d_slope_v097_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 252)
    rec = _f39_margin_recovery_strength(ebitdamargin, 252)
    base_ = (r * rec) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngxrec_ebitdamargin_504d_63d_slope_v098_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 504)
    rec = _f39_margin_recovery_strength(ebitdamargin, 504)
    base_ = (r * rec) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_troughz_grossmargin_63_252_126d_slope_v099_signal(grossmargin, closeadj):
    t = _f39_margin_trough_position(grossmargin, 63)
    base_ = _z(t, 252) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_troughz_grossmargin_126_252_252d_slope_v100_signal(grossmargin, closeadj):
    t = _f39_margin_trough_position(grossmargin, 126)
    base_ = _z(t, 252) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_troughz_grossmargin_63_504_5d_slope_v101_signal(grossmargin, closeadj):
    t = _f39_margin_trough_position(grossmargin, 63)
    base_ = _z(t, 504) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_troughz_grossmargin_126_504_21d_slope_v102_signal(grossmargin, closeadj):
    t = _f39_margin_trough_position(grossmargin, 126)
    base_ = _z(t, 504) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_troughz_ebitdamargin_63_252_63d_slope_v103_signal(ebitdamargin, closeadj):
    t = _f39_margin_trough_position(ebitdamargin, 63)
    base_ = _z(t, 252) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_troughz_ebitdamargin_126_252_126d_slope_v104_signal(ebitdamargin, closeadj):
    t = _f39_margin_trough_position(ebitdamargin, 126)
    base_ = _z(t, 252) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_troughz_ebitdamargin_63_504_252d_slope_v105_signal(ebitdamargin, closeadj):
    t = _f39_margin_trough_position(ebitdamargin, 63)
    base_ = _z(t, 504) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_troughz_ebitdamargin_126_504_5d_slope_v106_signal(ebitdamargin, closeadj):
    t = _f39_margin_trough_position(ebitdamargin, 126)
    base_ = _z(t, 504) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngsm_grossmargin_126d_21d_slope_v107_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 126)
    base_ = _mean(r, 21) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngsm_grossmargin_252d_63d_slope_v108_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 252)
    base_ = _mean(r, 21) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngsm_grossmargin_378d_126d_slope_v109_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 378)
    base_ = _mean(r, 21) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngsm_grossmargin_504d_252d_slope_v110_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 504)
    base_ = _mean(r, 21) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngsm_ebitdamargin_126d_5d_slope_v111_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 126)
    base_ = _mean(r, 21) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngsm_ebitdamargin_252d_21d_slope_v112_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 252)
    base_ = _mean(r, 21) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngsm_ebitdamargin_378d_63d_slope_v113_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 378)
    base_ = _mean(r, 21) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngsm_ebitdamargin_504d_126d_slope_v114_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 504)
    base_ = _mean(r, 21) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recdiff_grossmargin_63d_252d_slope_v115_signal(grossmargin, closeadj):
    rec = _f39_margin_recovery_strength(grossmargin, 63)
    base_ = rec.diff(21) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recdiff_grossmargin_126d_5d_slope_v116_signal(grossmargin, closeadj):
    rec = _f39_margin_recovery_strength(grossmargin, 126)
    base_ = rec.diff(21) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recdiff_grossmargin_252d_21d_slope_v117_signal(grossmargin, closeadj):
    rec = _f39_margin_recovery_strength(grossmargin, 252)
    base_ = rec.diff(21) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recdiff_grossmargin_504d_63d_slope_v118_signal(grossmargin, closeadj):
    rec = _f39_margin_recovery_strength(grossmargin, 504)
    base_ = rec.diff(21) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recdiff_ebitdamargin_63d_126d_slope_v119_signal(ebitdamargin, closeadj):
    rec = _f39_margin_recovery_strength(ebitdamargin, 63)
    base_ = rec.diff(21) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recdiff_ebitdamargin_126d_252d_slope_v120_signal(ebitdamargin, closeadj):
    rec = _f39_margin_recovery_strength(ebitdamargin, 126)
    base_ = rec.diff(21) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recdiff_ebitdamargin_252d_5d_slope_v121_signal(ebitdamargin, closeadj):
    rec = _f39_margin_recovery_strength(ebitdamargin, 252)
    base_ = rec.diff(21) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_recdiff_ebitdamargin_504d_21d_slope_v122_signal(ebitdamargin, closeadj):
    rec = _f39_margin_recovery_strength(ebitdamargin, 504)
    base_ = rec.diff(21) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngxtrough_grossmargin_63d_63d_slope_v123_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 63)
    t = _f39_margin_trough_position(grossmargin, 63)
    base_ = (r * t) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngxtrough_grossmargin_126d_126d_slope_v124_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 126)
    t = _f39_margin_trough_position(grossmargin, 126)
    base_ = (r * t) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngxtrough_grossmargin_252d_252d_slope_v125_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 252)
    t = _f39_margin_trough_position(grossmargin, 252)
    base_ = (r * t) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngxtrough_grossmargin_504d_5d_slope_v126_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 504)
    t = _f39_margin_trough_position(grossmargin, 504)
    base_ = (r * t) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngxtrough_ebitdamargin_63d_21d_slope_v127_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 63)
    t = _f39_margin_trough_position(ebitdamargin, 63)
    base_ = (r * t) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngxtrough_ebitdamargin_126d_63d_slope_v128_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 126)
    t = _f39_margin_trough_position(ebitdamargin, 126)
    base_ = (r * t) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngxtrough_ebitdamargin_252d_126d_slope_v129_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 252)
    t = _f39_margin_trough_position(ebitdamargin, 252)
    base_ = (r * t) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngxtrough_ebitdamargin_504d_252d_slope_v130_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 504)
    t = _f39_margin_trough_position(ebitdamargin, 504)
    base_ = (r * t) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_crossrec_63d_5d_slope_v131_signal(grossmargin, ebitdamargin, closeadj):
    rec1 = _f39_margin_recovery_strength(grossmargin, 63)
    rec2 = _f39_margin_recovery_strength(ebitdamargin, 63)
    base_ = (rec1 + rec2) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_crossrec_126d_21d_slope_v132_signal(grossmargin, ebitdamargin, closeadj):
    rec1 = _f39_margin_recovery_strength(grossmargin, 126)
    rec2 = _f39_margin_recovery_strength(ebitdamargin, 126)
    base_ = (rec1 + rec2) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_crossrec_252d_63d_slope_v133_signal(grossmargin, ebitdamargin, closeadj):
    rec1 = _f39_margin_recovery_strength(grossmargin, 252)
    rec2 = _f39_margin_recovery_strength(ebitdamargin, 252)
    base_ = (rec1 + rec2) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngema_grossmargin_63d_126d_slope_v134_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 63)
    base_ = _ema(r, 21) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngema_grossmargin_126d_252d_slope_v135_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 126)
    base_ = _ema(r, 21) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngema_grossmargin_252d_5d_slope_v136_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 252)
    base_ = _ema(r, 21) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngema_grossmargin_504d_21d_slope_v137_signal(grossmargin, closeadj):
    r = _f39_margin_range(grossmargin, 504)
    base_ = _ema(r, 21) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngema_ebitdamargin_63d_63d_slope_v138_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 63)
    base_ = _ema(r, 21) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngema_ebitdamargin_126d_126d_slope_v139_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 126)
    base_ = _ema(r, 21) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngema_ebitdamargin_252d_252d_slope_v140_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 252)
    base_ = _ema(r, 21) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngema_ebitdamargin_504d_5d_slope_v141_signal(ebitdamargin, closeadj):
    r = _f39_margin_range(ebitdamargin, 504)
    base_ = _ema(r, 21) * closeadj
    result = _slope_pct(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngema_netmargin_63d_21d_slope_v142_signal(netmargin, closeadj):
    r = _f39_margin_range(netmargin, 63)
    base_ = _ema(r, 21) * closeadj
    result = _slope_diff_norm(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngema_netmargin_126d_63d_slope_v143_signal(netmargin, closeadj):
    r = _f39_margin_range(netmargin, 126)
    base_ = _ema(r, 21) * closeadj
    result = _slope_pct(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngema_netmargin_252d_126d_slope_v144_signal(netmargin, closeadj):
    r = _f39_margin_range(netmargin, 252)
    base_ = _ema(r, 21) * closeadj
    result = _slope_diff_norm(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_rngema_netmargin_504d_252d_slope_v145_signal(netmargin, closeadj):
    r = _f39_margin_range(netmargin, 504)
    base_ = _ema(r, 21) * closeadj
    result = _slope_pct(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_troughdiff_grossmargin_63d_5d_slope_v146_signal(grossmargin, closeadj):
    t = _f39_margin_trough_position(grossmargin, 63)
    base_ = t.diff(21) * closeadj
    result = _slope_diff_norm(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_troughdiff_grossmargin_126d_21d_slope_v147_signal(grossmargin, closeadj):
    t = _f39_margin_trough_position(grossmargin, 126)
    base_ = t.diff(21) * closeadj
    result = _slope_pct(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_troughdiff_grossmargin_252d_63d_slope_v148_signal(grossmargin, closeadj):
    t = _f39_margin_trough_position(grossmargin, 252)
    base_ = t.diff(21) * closeadj
    result = _slope_diff_norm(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_troughdiff_grossmargin_504d_126d_slope_v149_signal(grossmargin, closeadj):
    t = _f39_margin_trough_position(grossmargin, 504)
    base_ = t.diff(21) * closeadj
    result = _slope_pct(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f39mtp_f39_margin_trough_to_peak_troughdiff_ebitdamargin_63d_252d_slope_v150_signal(ebitdamargin, closeadj):
    t = _f39_margin_trough_position(ebitdamargin, 63)
    base_ = t.diff(21) * closeadj
    result = _slope_diff_norm(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f39mtp_f39_margin_trough_to_peak_range_grossmargin_5d_5d_slope_v001_signal,
    f39mtp_f39_margin_trough_to_peak_range_grossmargin_10d_21d_slope_v002_signal,
    f39mtp_f39_margin_trough_to_peak_range_grossmargin_21d_63d_slope_v003_signal,
    f39mtp_f39_margin_trough_to_peak_range_grossmargin_42d_126d_slope_v004_signal,
    f39mtp_f39_margin_trough_to_peak_range_grossmargin_63d_252d_slope_v005_signal,
    f39mtp_f39_margin_trough_to_peak_range_grossmargin_126d_5d_slope_v006_signal,
    f39mtp_f39_margin_trough_to_peak_range_grossmargin_189d_21d_slope_v007_signal,
    f39mtp_f39_margin_trough_to_peak_range_grossmargin_252d_63d_slope_v008_signal,
    f39mtp_f39_margin_trough_to_peak_range_grossmargin_378d_126d_slope_v009_signal,
    f39mtp_f39_margin_trough_to_peak_range_grossmargin_504d_252d_slope_v010_signal,
    f39mtp_f39_margin_trough_to_peak_range_ebitdamargin_5d_5d_slope_v011_signal,
    f39mtp_f39_margin_trough_to_peak_range_ebitdamargin_10d_21d_slope_v012_signal,
    f39mtp_f39_margin_trough_to_peak_range_ebitdamargin_21d_63d_slope_v013_signal,
    f39mtp_f39_margin_trough_to_peak_range_ebitdamargin_42d_126d_slope_v014_signal,
    f39mtp_f39_margin_trough_to_peak_range_ebitdamargin_63d_252d_slope_v015_signal,
    f39mtp_f39_margin_trough_to_peak_range_ebitdamargin_126d_5d_slope_v016_signal,
    f39mtp_f39_margin_trough_to_peak_range_ebitdamargin_189d_21d_slope_v017_signal,
    f39mtp_f39_margin_trough_to_peak_range_ebitdamargin_252d_63d_slope_v018_signal,
    f39mtp_f39_margin_trough_to_peak_range_ebitdamargin_378d_126d_slope_v019_signal,
    f39mtp_f39_margin_trough_to_peak_range_ebitdamargin_504d_252d_slope_v020_signal,
    f39mtp_f39_margin_trough_to_peak_range_netmargin_5d_5d_slope_v021_signal,
    f39mtp_f39_margin_trough_to_peak_range_netmargin_10d_21d_slope_v022_signal,
    f39mtp_f39_margin_trough_to_peak_range_netmargin_21d_63d_slope_v023_signal,
    f39mtp_f39_margin_trough_to_peak_range_netmargin_42d_126d_slope_v024_signal,
    f39mtp_f39_margin_trough_to_peak_range_netmargin_63d_252d_slope_v025_signal,
    f39mtp_f39_margin_trough_to_peak_range_netmargin_126d_5d_slope_v026_signal,
    f39mtp_f39_margin_trough_to_peak_range_netmargin_189d_21d_slope_v027_signal,
    f39mtp_f39_margin_trough_to_peak_range_netmargin_252d_63d_slope_v028_signal,
    f39mtp_f39_margin_trough_to_peak_range_netmargin_378d_126d_slope_v029_signal,
    f39mtp_f39_margin_trough_to_peak_range_netmargin_504d_252d_slope_v030_signal,
    f39mtp_f39_margin_trough_to_peak_trough_grossmargin_5d_5d_slope_v031_signal,
    f39mtp_f39_margin_trough_to_peak_trough_grossmargin_10d_21d_slope_v032_signal,
    f39mtp_f39_margin_trough_to_peak_trough_grossmargin_21d_63d_slope_v033_signal,
    f39mtp_f39_margin_trough_to_peak_trough_grossmargin_42d_126d_slope_v034_signal,
    f39mtp_f39_margin_trough_to_peak_trough_grossmargin_63d_252d_slope_v035_signal,
    f39mtp_f39_margin_trough_to_peak_trough_grossmargin_126d_5d_slope_v036_signal,
    f39mtp_f39_margin_trough_to_peak_trough_grossmargin_189d_21d_slope_v037_signal,
    f39mtp_f39_margin_trough_to_peak_trough_grossmargin_252d_63d_slope_v038_signal,
    f39mtp_f39_margin_trough_to_peak_trough_grossmargin_378d_126d_slope_v039_signal,
    f39mtp_f39_margin_trough_to_peak_trough_grossmargin_504d_252d_slope_v040_signal,
    f39mtp_f39_margin_trough_to_peak_trough_ebitdamargin_5d_5d_slope_v041_signal,
    f39mtp_f39_margin_trough_to_peak_trough_ebitdamargin_10d_21d_slope_v042_signal,
    f39mtp_f39_margin_trough_to_peak_trough_ebitdamargin_21d_63d_slope_v043_signal,
    f39mtp_f39_margin_trough_to_peak_trough_ebitdamargin_42d_126d_slope_v044_signal,
    f39mtp_f39_margin_trough_to_peak_trough_ebitdamargin_63d_252d_slope_v045_signal,
    f39mtp_f39_margin_trough_to_peak_trough_ebitdamargin_126d_5d_slope_v046_signal,
    f39mtp_f39_margin_trough_to_peak_trough_ebitdamargin_189d_21d_slope_v047_signal,
    f39mtp_f39_margin_trough_to_peak_trough_ebitdamargin_252d_63d_slope_v048_signal,
    f39mtp_f39_margin_trough_to_peak_trough_ebitdamargin_378d_126d_slope_v049_signal,
    f39mtp_f39_margin_trough_to_peak_trough_ebitdamargin_504d_252d_slope_v050_signal,
    f39mtp_f39_margin_trough_to_peak_trough_netmargin_5d_5d_slope_v051_signal,
    f39mtp_f39_margin_trough_to_peak_trough_netmargin_10d_21d_slope_v052_signal,
    f39mtp_f39_margin_trough_to_peak_trough_netmargin_21d_63d_slope_v053_signal,
    f39mtp_f39_margin_trough_to_peak_trough_netmargin_42d_126d_slope_v054_signal,
    f39mtp_f39_margin_trough_to_peak_trough_netmargin_63d_252d_slope_v055_signal,
    f39mtp_f39_margin_trough_to_peak_trough_netmargin_126d_5d_slope_v056_signal,
    f39mtp_f39_margin_trough_to_peak_trough_netmargin_189d_21d_slope_v057_signal,
    f39mtp_f39_margin_trough_to_peak_trough_netmargin_252d_63d_slope_v058_signal,
    f39mtp_f39_margin_trough_to_peak_trough_netmargin_378d_126d_slope_v059_signal,
    f39mtp_f39_margin_trough_to_peak_trough_netmargin_504d_252d_slope_v060_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_grossmargin_5d_5d_slope_v061_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_grossmargin_10d_21d_slope_v062_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_grossmargin_21d_63d_slope_v063_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_grossmargin_42d_126d_slope_v064_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_grossmargin_63d_252d_slope_v065_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_grossmargin_126d_5d_slope_v066_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_grossmargin_189d_21d_slope_v067_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_grossmargin_252d_63d_slope_v068_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_grossmargin_378d_126d_slope_v069_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_grossmargin_504d_252d_slope_v070_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_ebitdamargin_5d_5d_slope_v071_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_ebitdamargin_10d_21d_slope_v072_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_ebitdamargin_21d_63d_slope_v073_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_ebitdamargin_42d_126d_slope_v074_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_ebitdamargin_63d_252d_slope_v075_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_ebitdamargin_126d_5d_slope_v076_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_ebitdamargin_189d_21d_slope_v077_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_ebitdamargin_252d_63d_slope_v078_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_ebitdamargin_378d_126d_slope_v079_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_ebitdamargin_504d_252d_slope_v080_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_netmargin_5d_5d_slope_v081_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_netmargin_10d_21d_slope_v082_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_netmargin_21d_63d_slope_v083_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_netmargin_42d_126d_slope_v084_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_netmargin_63d_252d_slope_v085_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_netmargin_126d_5d_slope_v086_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_netmargin_189d_21d_slope_v087_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_netmargin_252d_63d_slope_v088_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_netmargin_378d_126d_slope_v089_signal,
    f39mtp_f39_margin_trough_to_peak_recovery_netmargin_504d_252d_slope_v090_signal,
    f39mtp_f39_margin_trough_to_peak_rngxrec_grossmargin_63d_5d_slope_v091_signal,
    f39mtp_f39_margin_trough_to_peak_rngxrec_grossmargin_126d_21d_slope_v092_signal,
    f39mtp_f39_margin_trough_to_peak_rngxrec_grossmargin_252d_63d_slope_v093_signal,
    f39mtp_f39_margin_trough_to_peak_rngxrec_grossmargin_504d_126d_slope_v094_signal,
    f39mtp_f39_margin_trough_to_peak_rngxrec_ebitdamargin_63d_252d_slope_v095_signal,
    f39mtp_f39_margin_trough_to_peak_rngxrec_ebitdamargin_126d_5d_slope_v096_signal,
    f39mtp_f39_margin_trough_to_peak_rngxrec_ebitdamargin_252d_21d_slope_v097_signal,
    f39mtp_f39_margin_trough_to_peak_rngxrec_ebitdamargin_504d_63d_slope_v098_signal,
    f39mtp_f39_margin_trough_to_peak_troughz_grossmargin_63_252_126d_slope_v099_signal,
    f39mtp_f39_margin_trough_to_peak_troughz_grossmargin_126_252_252d_slope_v100_signal,
    f39mtp_f39_margin_trough_to_peak_troughz_grossmargin_63_504_5d_slope_v101_signal,
    f39mtp_f39_margin_trough_to_peak_troughz_grossmargin_126_504_21d_slope_v102_signal,
    f39mtp_f39_margin_trough_to_peak_troughz_ebitdamargin_63_252_63d_slope_v103_signal,
    f39mtp_f39_margin_trough_to_peak_troughz_ebitdamargin_126_252_126d_slope_v104_signal,
    f39mtp_f39_margin_trough_to_peak_troughz_ebitdamargin_63_504_252d_slope_v105_signal,
    f39mtp_f39_margin_trough_to_peak_troughz_ebitdamargin_126_504_5d_slope_v106_signal,
    f39mtp_f39_margin_trough_to_peak_rngsm_grossmargin_126d_21d_slope_v107_signal,
    f39mtp_f39_margin_trough_to_peak_rngsm_grossmargin_252d_63d_slope_v108_signal,
    f39mtp_f39_margin_trough_to_peak_rngsm_grossmargin_378d_126d_slope_v109_signal,
    f39mtp_f39_margin_trough_to_peak_rngsm_grossmargin_504d_252d_slope_v110_signal,
    f39mtp_f39_margin_trough_to_peak_rngsm_ebitdamargin_126d_5d_slope_v111_signal,
    f39mtp_f39_margin_trough_to_peak_rngsm_ebitdamargin_252d_21d_slope_v112_signal,
    f39mtp_f39_margin_trough_to_peak_rngsm_ebitdamargin_378d_63d_slope_v113_signal,
    f39mtp_f39_margin_trough_to_peak_rngsm_ebitdamargin_504d_126d_slope_v114_signal,
    f39mtp_f39_margin_trough_to_peak_recdiff_grossmargin_63d_252d_slope_v115_signal,
    f39mtp_f39_margin_trough_to_peak_recdiff_grossmargin_126d_5d_slope_v116_signal,
    f39mtp_f39_margin_trough_to_peak_recdiff_grossmargin_252d_21d_slope_v117_signal,
    f39mtp_f39_margin_trough_to_peak_recdiff_grossmargin_504d_63d_slope_v118_signal,
    f39mtp_f39_margin_trough_to_peak_recdiff_ebitdamargin_63d_126d_slope_v119_signal,
    f39mtp_f39_margin_trough_to_peak_recdiff_ebitdamargin_126d_252d_slope_v120_signal,
    f39mtp_f39_margin_trough_to_peak_recdiff_ebitdamargin_252d_5d_slope_v121_signal,
    f39mtp_f39_margin_trough_to_peak_recdiff_ebitdamargin_504d_21d_slope_v122_signal,
    f39mtp_f39_margin_trough_to_peak_rngxtrough_grossmargin_63d_63d_slope_v123_signal,
    f39mtp_f39_margin_trough_to_peak_rngxtrough_grossmargin_126d_126d_slope_v124_signal,
    f39mtp_f39_margin_trough_to_peak_rngxtrough_grossmargin_252d_252d_slope_v125_signal,
    f39mtp_f39_margin_trough_to_peak_rngxtrough_grossmargin_504d_5d_slope_v126_signal,
    f39mtp_f39_margin_trough_to_peak_rngxtrough_ebitdamargin_63d_21d_slope_v127_signal,
    f39mtp_f39_margin_trough_to_peak_rngxtrough_ebitdamargin_126d_63d_slope_v128_signal,
    f39mtp_f39_margin_trough_to_peak_rngxtrough_ebitdamargin_252d_126d_slope_v129_signal,
    f39mtp_f39_margin_trough_to_peak_rngxtrough_ebitdamargin_504d_252d_slope_v130_signal,
    f39mtp_f39_margin_trough_to_peak_crossrec_63d_5d_slope_v131_signal,
    f39mtp_f39_margin_trough_to_peak_crossrec_126d_21d_slope_v132_signal,
    f39mtp_f39_margin_trough_to_peak_crossrec_252d_63d_slope_v133_signal,
    f39mtp_f39_margin_trough_to_peak_rngema_grossmargin_63d_126d_slope_v134_signal,
    f39mtp_f39_margin_trough_to_peak_rngema_grossmargin_126d_252d_slope_v135_signal,
    f39mtp_f39_margin_trough_to_peak_rngema_grossmargin_252d_5d_slope_v136_signal,
    f39mtp_f39_margin_trough_to_peak_rngema_grossmargin_504d_21d_slope_v137_signal,
    f39mtp_f39_margin_trough_to_peak_rngema_ebitdamargin_63d_63d_slope_v138_signal,
    f39mtp_f39_margin_trough_to_peak_rngema_ebitdamargin_126d_126d_slope_v139_signal,
    f39mtp_f39_margin_trough_to_peak_rngema_ebitdamargin_252d_252d_slope_v140_signal,
    f39mtp_f39_margin_trough_to_peak_rngema_ebitdamargin_504d_5d_slope_v141_signal,
    f39mtp_f39_margin_trough_to_peak_rngema_netmargin_63d_21d_slope_v142_signal,
    f39mtp_f39_margin_trough_to_peak_rngema_netmargin_126d_63d_slope_v143_signal,
    f39mtp_f39_margin_trough_to_peak_rngema_netmargin_252d_126d_slope_v144_signal,
    f39mtp_f39_margin_trough_to_peak_rngema_netmargin_504d_252d_slope_v145_signal,
    f39mtp_f39_margin_trough_to_peak_troughdiff_grossmargin_63d_5d_slope_v146_signal,
    f39mtp_f39_margin_trough_to_peak_troughdiff_grossmargin_126d_21d_slope_v147_signal,
    f39mtp_f39_margin_trough_to_peak_troughdiff_grossmargin_252d_63d_slope_v148_signal,
    f39mtp_f39_margin_trough_to_peak_troughdiff_grossmargin_504d_126d_slope_v149_signal,
    f39mtp_f39_margin_trough_to_peak_troughdiff_ebitdamargin_63d_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F39_MARGIN_TROUGH_TO_PEAK_REGISTRY_SLOPE_001_150 = REGISTRY


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
    domain_primitives = ("_f39_margin_range", "_f39_margin_trough_position", "_f39_margin_recovery_strength")
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
    print(f"OK f39_margin_trough_to_peak_2nd_derivatives_001_150_claude: {n_features} features pass")
