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
def _f38_share_issuance(sharesbas, w):
    return sharesbas.pct_change(periods=w)


def _f38_capital_raise_proxy(sharesbas, equity, w):
    g_shares = sharesbas.pct_change(periods=w)
    g_eq = equity.pct_change(periods=w)
    return g_shares - g_eq


def _f38_dilution_signal(sharesbas, shareswa, w):
    ratio = sharesbas / shareswa.replace(0, np.nan).abs()
    return ratio.rolling(w, min_periods=max(1, w // 2)).mean() - 1.0

# ===== features =====

# p0_xclose window=5 ow=5
def f38ucr_f38_utility_capital_raise_p0_xclose_5d_jerk_v001_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 5)) * _mean(closeadj, 5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=5 ow=10
def f38ucr_f38_utility_capital_raise_p0_xclose_5d_jerk_v002_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 5)) * _mean(closeadj, 5)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=5 ow=21
def f38ucr_f38_utility_capital_raise_p0_xclose_5d_jerk_v003_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 5)) * _mean(closeadj, 5)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=5 ow=42
def f38ucr_f38_utility_capital_raise_p0_xclose_5d_jerk_v004_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 5)) * _mean(closeadj, 5)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=5 ow=63
def f38ucr_f38_utility_capital_raise_p0_xclose_5d_jerk_v005_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 5)) * _mean(closeadj, 5)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=5 ow=126
def f38ucr_f38_utility_capital_raise_p0_xclose_5d_jerk_v006_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 5)) * _mean(closeadj, 5)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=10 ow=5
def f38ucr_f38_utility_capital_raise_p0_xclose_10d_jerk_v007_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 10)) * _mean(closeadj, 10)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=10 ow=10
def f38ucr_f38_utility_capital_raise_p0_xclose_10d_jerk_v008_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 10)) * _mean(closeadj, 10)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=10 ow=21
def f38ucr_f38_utility_capital_raise_p0_xclose_10d_jerk_v009_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 10)) * _mean(closeadj, 10)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=10 ow=42
def f38ucr_f38_utility_capital_raise_p0_xclose_10d_jerk_v010_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 10)) * _mean(closeadj, 10)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=10 ow=63
def f38ucr_f38_utility_capital_raise_p0_xclose_10d_jerk_v011_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 10)) * _mean(closeadj, 10)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=10 ow=126
def f38ucr_f38_utility_capital_raise_p0_xclose_10d_jerk_v012_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 10)) * _mean(closeadj, 10)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=21 ow=5
def f38ucr_f38_utility_capital_raise_p0_xclose_21d_jerk_v013_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 21)) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=21 ow=10
def f38ucr_f38_utility_capital_raise_p0_xclose_21d_jerk_v014_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 21)) * _mean(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=21 ow=21
def f38ucr_f38_utility_capital_raise_p0_xclose_21d_jerk_v015_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 21)) * _mean(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=21 ow=42
def f38ucr_f38_utility_capital_raise_p0_xclose_21d_jerk_v016_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 21)) * _mean(closeadj, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=21 ow=63
def f38ucr_f38_utility_capital_raise_p0_xclose_21d_jerk_v017_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 21)) * _mean(closeadj, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=21 ow=126
def f38ucr_f38_utility_capital_raise_p0_xclose_21d_jerk_v018_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 21)) * _mean(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=42 ow=5
def f38ucr_f38_utility_capital_raise_p0_xclose_42d_jerk_v019_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 42)) * _mean(closeadj, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=42 ow=10
def f38ucr_f38_utility_capital_raise_p0_xclose_42d_jerk_v020_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 42)) * _mean(closeadj, 42)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=42 ow=21
def f38ucr_f38_utility_capital_raise_p0_xclose_42d_jerk_v021_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 42)) * _mean(closeadj, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=42 ow=42
def f38ucr_f38_utility_capital_raise_p0_xclose_42d_jerk_v022_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 42)) * _mean(closeadj, 42)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=42 ow=63
def f38ucr_f38_utility_capital_raise_p0_xclose_42d_jerk_v023_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 42)) * _mean(closeadj, 42)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=42 ow=126
def f38ucr_f38_utility_capital_raise_p0_xclose_42d_jerk_v024_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 42)) * _mean(closeadj, 42)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=63 ow=5
def f38ucr_f38_utility_capital_raise_p0_xclose_63d_jerk_v025_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 63)) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=63 ow=10
def f38ucr_f38_utility_capital_raise_p0_xclose_63d_jerk_v026_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 63)) * _mean(closeadj, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=63 ow=21
def f38ucr_f38_utility_capital_raise_p0_xclose_63d_jerk_v027_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 63)) * _mean(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=63 ow=42
def f38ucr_f38_utility_capital_raise_p0_xclose_63d_jerk_v028_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 63)) * _mean(closeadj, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=63 ow=63
def f38ucr_f38_utility_capital_raise_p0_xclose_63d_jerk_v029_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 63)) * _mean(closeadj, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=63 ow=126
def f38ucr_f38_utility_capital_raise_p0_xclose_63d_jerk_v030_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 63)) * _mean(closeadj, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=126 ow=5
def f38ucr_f38_utility_capital_raise_p0_xclose_126d_jerk_v031_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 126)) * _mean(closeadj, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=126 ow=10
def f38ucr_f38_utility_capital_raise_p0_xclose_126d_jerk_v032_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 126)) * _mean(closeadj, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=126 ow=21
def f38ucr_f38_utility_capital_raise_p0_xclose_126d_jerk_v033_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 126)) * _mean(closeadj, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=126 ow=42
def f38ucr_f38_utility_capital_raise_p0_xclose_126d_jerk_v034_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 126)) * _mean(closeadj, 126)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=126 ow=63
def f38ucr_f38_utility_capital_raise_p0_xclose_126d_jerk_v035_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 126)) * _mean(closeadj, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=126 ow=126
def f38ucr_f38_utility_capital_raise_p0_xclose_126d_jerk_v036_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 126)) * _mean(closeadj, 126)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=189 ow=5
def f38ucr_f38_utility_capital_raise_p0_xclose_189d_jerk_v037_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 189)) * _mean(closeadj, 189)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=189 ow=10
def f38ucr_f38_utility_capital_raise_p0_xclose_189d_jerk_v038_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 189)) * _mean(closeadj, 189)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=189 ow=21
def f38ucr_f38_utility_capital_raise_p0_xclose_189d_jerk_v039_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 189)) * _mean(closeadj, 189)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=189 ow=42
def f38ucr_f38_utility_capital_raise_p0_xclose_189d_jerk_v040_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 189)) * _mean(closeadj, 189)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=189 ow=63
def f38ucr_f38_utility_capital_raise_p0_xclose_189d_jerk_v041_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 189)) * _mean(closeadj, 189)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=189 ow=126
def f38ucr_f38_utility_capital_raise_p0_xclose_189d_jerk_v042_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 189)) * _mean(closeadj, 189)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=252 ow=5
def f38ucr_f38_utility_capital_raise_p0_xclose_252d_jerk_v043_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 252)) * _mean(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=252 ow=10
def f38ucr_f38_utility_capital_raise_p0_xclose_252d_jerk_v044_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 252)) * _mean(closeadj, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=252 ow=21
def f38ucr_f38_utility_capital_raise_p0_xclose_252d_jerk_v045_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 252)) * _mean(closeadj, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=252 ow=42
def f38ucr_f38_utility_capital_raise_p0_xclose_252d_jerk_v046_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 252)) * _mean(closeadj, 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=252 ow=63
def f38ucr_f38_utility_capital_raise_p0_xclose_252d_jerk_v047_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 252)) * _mean(closeadj, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=252 ow=126
def f38ucr_f38_utility_capital_raise_p0_xclose_252d_jerk_v048_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 252)) * _mean(closeadj, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=378 ow=5
def f38ucr_f38_utility_capital_raise_p0_xclose_378d_jerk_v049_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 378)) * _mean(closeadj, 378)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=378 ow=10
def f38ucr_f38_utility_capital_raise_p0_xclose_378d_jerk_v050_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 378)) * _mean(closeadj, 378)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=378 ow=21
def f38ucr_f38_utility_capital_raise_p0_xclose_378d_jerk_v051_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 378)) * _mean(closeadj, 378)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=378 ow=42
def f38ucr_f38_utility_capital_raise_p0_xclose_378d_jerk_v052_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 378)) * _mean(closeadj, 378)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=378 ow=63
def f38ucr_f38_utility_capital_raise_p0_xclose_378d_jerk_v053_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 378)) * _mean(closeadj, 378)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=378 ow=126
def f38ucr_f38_utility_capital_raise_p0_xclose_378d_jerk_v054_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 378)) * _mean(closeadj, 378)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=504 ow=5
def f38ucr_f38_utility_capital_raise_p0_xclose_504d_jerk_v055_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 504)) * _mean(closeadj, 504)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=504 ow=10
def f38ucr_f38_utility_capital_raise_p0_xclose_504d_jerk_v056_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 504)) * _mean(closeadj, 504)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=504 ow=21
def f38ucr_f38_utility_capital_raise_p0_xclose_504d_jerk_v057_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 504)) * _mean(closeadj, 504)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=504 ow=42
def f38ucr_f38_utility_capital_raise_p0_xclose_504d_jerk_v058_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 504)) * _mean(closeadj, 504)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=504 ow=63
def f38ucr_f38_utility_capital_raise_p0_xclose_504d_jerk_v059_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 504)) * _mean(closeadj, 504)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=504 ow=126
def f38ucr_f38_utility_capital_raise_p0_xclose_504d_jerk_v060_signal(closeadj, sharesbas):
    base = (_f38_share_issuance(sharesbas, 504)) * _mean(closeadj, 504)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=5 ow=5
def f38ucr_f38_utility_capital_raise_p0_meanw_5d_jerk_v061_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 5), 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=5 ow=10
def f38ucr_f38_utility_capital_raise_p0_meanw_5d_jerk_v062_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 5), 5) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=5 ow=21
def f38ucr_f38_utility_capital_raise_p0_meanw_5d_jerk_v063_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 5), 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=5 ow=42
def f38ucr_f38_utility_capital_raise_p0_meanw_5d_jerk_v064_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 5), 5) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=5 ow=63
def f38ucr_f38_utility_capital_raise_p0_meanw_5d_jerk_v065_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 5), 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=5 ow=126
def f38ucr_f38_utility_capital_raise_p0_meanw_5d_jerk_v066_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 5), 5) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=10 ow=5
def f38ucr_f38_utility_capital_raise_p0_meanw_10d_jerk_v067_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 10), 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=10 ow=10
def f38ucr_f38_utility_capital_raise_p0_meanw_10d_jerk_v068_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 10), 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=10 ow=21
def f38ucr_f38_utility_capital_raise_p0_meanw_10d_jerk_v069_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 10), 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=10 ow=42
def f38ucr_f38_utility_capital_raise_p0_meanw_10d_jerk_v070_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 10), 10) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=10 ow=63
def f38ucr_f38_utility_capital_raise_p0_meanw_10d_jerk_v071_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 10), 10) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=10 ow=126
def f38ucr_f38_utility_capital_raise_p0_meanw_10d_jerk_v072_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 10), 10) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=21 ow=5
def f38ucr_f38_utility_capital_raise_p0_meanw_21d_jerk_v073_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 21), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=21 ow=10
def f38ucr_f38_utility_capital_raise_p0_meanw_21d_jerk_v074_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 21), 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=21 ow=21
def f38ucr_f38_utility_capital_raise_p0_meanw_21d_jerk_v075_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 21), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=21 ow=42
def f38ucr_f38_utility_capital_raise_p0_meanw_21d_jerk_v076_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 21), 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=21 ow=63
def f38ucr_f38_utility_capital_raise_p0_meanw_21d_jerk_v077_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 21), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=21 ow=126
def f38ucr_f38_utility_capital_raise_p0_meanw_21d_jerk_v078_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 21), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=42 ow=5
def f38ucr_f38_utility_capital_raise_p0_meanw_42d_jerk_v079_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 42), 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=42 ow=10
def f38ucr_f38_utility_capital_raise_p0_meanw_42d_jerk_v080_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 42), 42) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=42 ow=21
def f38ucr_f38_utility_capital_raise_p0_meanw_42d_jerk_v081_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 42), 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=42 ow=42
def f38ucr_f38_utility_capital_raise_p0_meanw_42d_jerk_v082_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 42), 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=42 ow=63
def f38ucr_f38_utility_capital_raise_p0_meanw_42d_jerk_v083_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 42), 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=42 ow=126
def f38ucr_f38_utility_capital_raise_p0_meanw_42d_jerk_v084_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 42), 42) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=63 ow=5
def f38ucr_f38_utility_capital_raise_p0_meanw_63d_jerk_v085_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 63), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=63 ow=10
def f38ucr_f38_utility_capital_raise_p0_meanw_63d_jerk_v086_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 63), 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=63 ow=21
def f38ucr_f38_utility_capital_raise_p0_meanw_63d_jerk_v087_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 63), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=63 ow=42
def f38ucr_f38_utility_capital_raise_p0_meanw_63d_jerk_v088_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 63), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=63 ow=63
def f38ucr_f38_utility_capital_raise_p0_meanw_63d_jerk_v089_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 63), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=63 ow=126
def f38ucr_f38_utility_capital_raise_p0_meanw_63d_jerk_v090_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 63), 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=126 ow=5
def f38ucr_f38_utility_capital_raise_p0_meanw_126d_jerk_v091_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 126), 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=126 ow=10
def f38ucr_f38_utility_capital_raise_p0_meanw_126d_jerk_v092_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 126), 126) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=126 ow=21
def f38ucr_f38_utility_capital_raise_p0_meanw_126d_jerk_v093_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 126), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=126 ow=42
def f38ucr_f38_utility_capital_raise_p0_meanw_126d_jerk_v094_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 126), 126) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=126 ow=63
def f38ucr_f38_utility_capital_raise_p0_meanw_126d_jerk_v095_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 126), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=126 ow=126
def f38ucr_f38_utility_capital_raise_p0_meanw_126d_jerk_v096_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 126), 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=189 ow=5
def f38ucr_f38_utility_capital_raise_p0_meanw_189d_jerk_v097_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 189), 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=189 ow=10
def f38ucr_f38_utility_capital_raise_p0_meanw_189d_jerk_v098_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 189), 189) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=189 ow=21
def f38ucr_f38_utility_capital_raise_p0_meanw_189d_jerk_v099_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 189), 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=189 ow=42
def f38ucr_f38_utility_capital_raise_p0_meanw_189d_jerk_v100_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 189), 189) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=189 ow=63
def f38ucr_f38_utility_capital_raise_p0_meanw_189d_jerk_v101_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 189), 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=189 ow=126
def f38ucr_f38_utility_capital_raise_p0_meanw_189d_jerk_v102_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 189), 189) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=252 ow=5
def f38ucr_f38_utility_capital_raise_p0_meanw_252d_jerk_v103_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 252), 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=252 ow=10
def f38ucr_f38_utility_capital_raise_p0_meanw_252d_jerk_v104_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 252), 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=252 ow=21
def f38ucr_f38_utility_capital_raise_p0_meanw_252d_jerk_v105_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 252), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=252 ow=42
def f38ucr_f38_utility_capital_raise_p0_meanw_252d_jerk_v106_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 252), 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=252 ow=63
def f38ucr_f38_utility_capital_raise_p0_meanw_252d_jerk_v107_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 252), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=252 ow=126
def f38ucr_f38_utility_capital_raise_p0_meanw_252d_jerk_v108_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 252), 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=378 ow=5
def f38ucr_f38_utility_capital_raise_p0_meanw_378d_jerk_v109_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 378), 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=378 ow=10
def f38ucr_f38_utility_capital_raise_p0_meanw_378d_jerk_v110_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 378), 378) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=378 ow=21
def f38ucr_f38_utility_capital_raise_p0_meanw_378d_jerk_v111_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 378), 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=378 ow=42
def f38ucr_f38_utility_capital_raise_p0_meanw_378d_jerk_v112_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 378), 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=378 ow=63
def f38ucr_f38_utility_capital_raise_p0_meanw_378d_jerk_v113_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 378), 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=378 ow=126
def f38ucr_f38_utility_capital_raise_p0_meanw_378d_jerk_v114_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 378), 378) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=504 ow=5
def f38ucr_f38_utility_capital_raise_p0_meanw_504d_jerk_v115_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 504), 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=504 ow=10
def f38ucr_f38_utility_capital_raise_p0_meanw_504d_jerk_v116_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 504), 504) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=504 ow=21
def f38ucr_f38_utility_capital_raise_p0_meanw_504d_jerk_v117_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 504), 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=504 ow=42
def f38ucr_f38_utility_capital_raise_p0_meanw_504d_jerk_v118_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 504), 504) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=504 ow=63
def f38ucr_f38_utility_capital_raise_p0_meanw_504d_jerk_v119_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 504), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=504 ow=126
def f38ucr_f38_utility_capital_raise_p0_meanw_504d_jerk_v120_signal(closeadj, sharesbas):
    base = _mean(_f38_share_issuance(sharesbas, 504), 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=5 ow=5
def f38ucr_f38_utility_capital_raise_p0_stdw_5d_jerk_v121_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 5), 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=5 ow=10
def f38ucr_f38_utility_capital_raise_p0_stdw_5d_jerk_v122_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 5), 5) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=5 ow=21
def f38ucr_f38_utility_capital_raise_p0_stdw_5d_jerk_v123_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 5), 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=5 ow=42
def f38ucr_f38_utility_capital_raise_p0_stdw_5d_jerk_v124_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 5), 5) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=5 ow=63
def f38ucr_f38_utility_capital_raise_p0_stdw_5d_jerk_v125_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 5), 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=5 ow=126
def f38ucr_f38_utility_capital_raise_p0_stdw_5d_jerk_v126_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 5), 5) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=10 ow=5
def f38ucr_f38_utility_capital_raise_p0_stdw_10d_jerk_v127_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 10), 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=10 ow=10
def f38ucr_f38_utility_capital_raise_p0_stdw_10d_jerk_v128_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 10), 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=10 ow=21
def f38ucr_f38_utility_capital_raise_p0_stdw_10d_jerk_v129_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 10), 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=10 ow=42
def f38ucr_f38_utility_capital_raise_p0_stdw_10d_jerk_v130_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 10), 10) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=10 ow=63
def f38ucr_f38_utility_capital_raise_p0_stdw_10d_jerk_v131_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 10), 10) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=10 ow=126
def f38ucr_f38_utility_capital_raise_p0_stdw_10d_jerk_v132_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 10), 10) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=21 ow=5
def f38ucr_f38_utility_capital_raise_p0_stdw_21d_jerk_v133_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 21), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=21 ow=10
def f38ucr_f38_utility_capital_raise_p0_stdw_21d_jerk_v134_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 21), 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=21 ow=21
def f38ucr_f38_utility_capital_raise_p0_stdw_21d_jerk_v135_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 21), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=21 ow=42
def f38ucr_f38_utility_capital_raise_p0_stdw_21d_jerk_v136_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 21), 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=21 ow=63
def f38ucr_f38_utility_capital_raise_p0_stdw_21d_jerk_v137_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 21), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=21 ow=126
def f38ucr_f38_utility_capital_raise_p0_stdw_21d_jerk_v138_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 21), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=42 ow=5
def f38ucr_f38_utility_capital_raise_p0_stdw_42d_jerk_v139_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 42), 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=42 ow=10
def f38ucr_f38_utility_capital_raise_p0_stdw_42d_jerk_v140_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 42), 42) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=42 ow=21
def f38ucr_f38_utility_capital_raise_p0_stdw_42d_jerk_v141_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 42), 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=42 ow=42
def f38ucr_f38_utility_capital_raise_p0_stdw_42d_jerk_v142_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 42), 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=42 ow=63
def f38ucr_f38_utility_capital_raise_p0_stdw_42d_jerk_v143_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 42), 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=42 ow=126
def f38ucr_f38_utility_capital_raise_p0_stdw_42d_jerk_v144_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 42), 42) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=63 ow=5
def f38ucr_f38_utility_capital_raise_p0_stdw_63d_jerk_v145_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 63), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=63 ow=10
def f38ucr_f38_utility_capital_raise_p0_stdw_63d_jerk_v146_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 63), 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=63 ow=21
def f38ucr_f38_utility_capital_raise_p0_stdw_63d_jerk_v147_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 63), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=63 ow=42
def f38ucr_f38_utility_capital_raise_p0_stdw_63d_jerk_v148_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 63), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=63 ow=63
def f38ucr_f38_utility_capital_raise_p0_stdw_63d_jerk_v149_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 63), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=63 ow=126
def f38ucr_f38_utility_capital_raise_p0_stdw_63d_jerk_v150_signal(closeadj, sharesbas):
    base = _std(_f38_share_issuance(sharesbas, 63), 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f38ucr_f38_utility_capital_raise_p0_xclose_5d_jerk_v001_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_5d_jerk_v002_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_5d_jerk_v003_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_5d_jerk_v004_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_5d_jerk_v005_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_5d_jerk_v006_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_10d_jerk_v007_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_10d_jerk_v008_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_10d_jerk_v009_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_10d_jerk_v010_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_10d_jerk_v011_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_10d_jerk_v012_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_21d_jerk_v013_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_21d_jerk_v014_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_21d_jerk_v015_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_21d_jerk_v016_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_21d_jerk_v017_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_21d_jerk_v018_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_42d_jerk_v019_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_42d_jerk_v020_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_42d_jerk_v021_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_42d_jerk_v022_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_42d_jerk_v023_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_42d_jerk_v024_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_63d_jerk_v025_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_63d_jerk_v026_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_63d_jerk_v027_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_63d_jerk_v028_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_63d_jerk_v029_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_63d_jerk_v030_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_126d_jerk_v031_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_126d_jerk_v032_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_126d_jerk_v033_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_126d_jerk_v034_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_126d_jerk_v035_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_126d_jerk_v036_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_189d_jerk_v037_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_189d_jerk_v038_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_189d_jerk_v039_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_189d_jerk_v040_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_189d_jerk_v041_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_189d_jerk_v042_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_252d_jerk_v043_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_252d_jerk_v044_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_252d_jerk_v045_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_252d_jerk_v046_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_252d_jerk_v047_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_252d_jerk_v048_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_378d_jerk_v049_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_378d_jerk_v050_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_378d_jerk_v051_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_378d_jerk_v052_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_378d_jerk_v053_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_378d_jerk_v054_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_504d_jerk_v055_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_504d_jerk_v056_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_504d_jerk_v057_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_504d_jerk_v058_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_504d_jerk_v059_signal,
    f38ucr_f38_utility_capital_raise_p0_xclose_504d_jerk_v060_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_5d_jerk_v061_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_5d_jerk_v062_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_5d_jerk_v063_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_5d_jerk_v064_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_5d_jerk_v065_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_5d_jerk_v066_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_10d_jerk_v067_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_10d_jerk_v068_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_10d_jerk_v069_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_10d_jerk_v070_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_10d_jerk_v071_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_10d_jerk_v072_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_21d_jerk_v073_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_21d_jerk_v074_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_21d_jerk_v075_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_21d_jerk_v076_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_21d_jerk_v077_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_21d_jerk_v078_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_42d_jerk_v079_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_42d_jerk_v080_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_42d_jerk_v081_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_42d_jerk_v082_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_42d_jerk_v083_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_42d_jerk_v084_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_63d_jerk_v085_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_63d_jerk_v086_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_63d_jerk_v087_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_63d_jerk_v088_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_63d_jerk_v089_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_63d_jerk_v090_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_126d_jerk_v091_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_126d_jerk_v092_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_126d_jerk_v093_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_126d_jerk_v094_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_126d_jerk_v095_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_126d_jerk_v096_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_189d_jerk_v097_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_189d_jerk_v098_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_189d_jerk_v099_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_189d_jerk_v100_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_189d_jerk_v101_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_189d_jerk_v102_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_252d_jerk_v103_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_252d_jerk_v104_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_252d_jerk_v105_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_252d_jerk_v106_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_252d_jerk_v107_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_252d_jerk_v108_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_378d_jerk_v109_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_378d_jerk_v110_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_378d_jerk_v111_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_378d_jerk_v112_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_378d_jerk_v113_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_378d_jerk_v114_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_504d_jerk_v115_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_504d_jerk_v116_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_504d_jerk_v117_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_504d_jerk_v118_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_504d_jerk_v119_signal,
    f38ucr_f38_utility_capital_raise_p0_meanw_504d_jerk_v120_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_5d_jerk_v121_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_5d_jerk_v122_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_5d_jerk_v123_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_5d_jerk_v124_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_5d_jerk_v125_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_5d_jerk_v126_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_10d_jerk_v127_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_10d_jerk_v128_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_10d_jerk_v129_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_10d_jerk_v130_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_10d_jerk_v131_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_10d_jerk_v132_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_21d_jerk_v133_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_21d_jerk_v134_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_21d_jerk_v135_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_21d_jerk_v136_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_21d_jerk_v137_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_21d_jerk_v138_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_42d_jerk_v139_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_42d_jerk_v140_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_42d_jerk_v141_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_42d_jerk_v142_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_42d_jerk_v143_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_42d_jerk_v144_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_63d_jerk_v145_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_63d_jerk_v146_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_63d_jerk_v147_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_63d_jerk_v148_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_63d_jerk_v149_signal,
    f38ucr_f38_utility_capital_raise_p0_stdw_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F38_UTILITY_CAPITAL_RAISE_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    debt    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    equity  = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    de        = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")

    cols = {
        "closeadj": closeadj,
        "debt": debt, "equity": equity, "ebitda": ebitda, "fcf": fcf,
        "capex": capex, "sharesbas": sharesbas, "shareswa": shareswa, "de": de,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f38_share_issuance", "_f38_capital_raise_proxy", "_f38_dilution_signal")
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
    print(f"OK f38_utility_capital_raise_3rd_derivatives_001_150_claude: {n_features} features pass")
