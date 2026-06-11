import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives: range-based volatility estimators =====
def _f11_log_hl(high, low):
    return np.log(high.replace(0, np.nan) / low.replace(0, np.nan))


def _f11_parkinson(high, low, w):
    r2 = _f11_log_hl(high, low) ** 2
    c = 1.0 / (4.0 * np.log(2.0))
    return np.sqrt((c * r2).rolling(w, min_periods=max(2, w // 2)).mean())


def _f11_gk_term(open, high, low, close):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    co = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    return 0.5 * hl ** 2 - (2.0 * np.log(2.0) - 1.0) * co ** 2


def _f11_garman_klass(open, high, low, close, w):
    t = _f11_gk_term(open, high, low, close)
    return np.sqrt(t.rolling(w, min_periods=max(2, w // 2)).mean().clip(lower=0))


def _f11_rs_term(open, high, low, close):
    hc = np.log(high.replace(0, np.nan) / close.replace(0, np.nan))
    ho = np.log(high.replace(0, np.nan) / open.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / close.replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / open.replace(0, np.nan))
    return hc * ho + lc * lo


def _f11_rogers_satchell(open, high, low, close, w):
    t = _f11_rs_term(open, high, low, close)
    return np.sqrt(t.rolling(w, min_periods=max(2, w // 2)).mean().clip(lower=0))


def _f11_true_range(high, low, close):
    pc = close.shift(1)
    a = (high - low).abs()
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


def _f11_atr(high, low, close, w):
    return _f11_true_range(high, low, close).rolling(
        w, min_periods=max(2, w // 2)).mean()


def _f11_hl_range_close(high, low, close):
    return (high - low) / close.replace(0, np.nan)


def _f11_overnight(open, close):
    return np.log(open.replace(0, np.nan) / close.shift(1).replace(0, np.nan))


# park 5d jerk(2nd deriv) roc=3d
def f11re_f11_range_vol_estimators_park_5d_jerk_v001_signal(high, low):
    base = _f11_parkinson(high, low, 5)
    result = (base - 2.0 * base.shift(3) + base.shift(6)) / 9.0
    return result.replace([np.inf, -np.inf], np.nan)

# park 10d jerk(2nd deriv) roc=7d
def f11re_f11_range_vol_estimators_park_10d_jerk_v002_signal(high, low):
    base = _f11_parkinson(high, low, 10)
    result = (base - 2.0 * base.shift(7) + base.shift(14)) / 49.0
    return result.replace([np.inf, -np.inf], np.nan)

# park 21d jerk(2nd deriv) roc=13d
def f11re_f11_range_vol_estimators_park_21d_jerk_v003_signal(high, low):
    base = _f11_parkinson(high, low, 21)
    result = (base - 2.0 * base.shift(13) + base.shift(26)) / 169.0
    return result.replace([np.inf, -np.inf], np.nan)

# park 42d jerk(2nd deriv) roc=26d
def f11re_f11_range_vol_estimators_park_42d_jerk_v004_signal(high, low):
    base = _f11_parkinson(high, low, 42)
    result = (base - 2.0 * base.shift(26) + base.shift(52)) / 676.0
    return result.replace([np.inf, -np.inf], np.nan)

# park 63d jerk(2nd deriv) roc=34d
def f11re_f11_range_vol_estimators_park_63d_jerk_v005_signal(high, low):
    base = _f11_parkinson(high, low, 63)
    result = (base - 2.0 * base.shift(34) + base.shift(68)) / 1156.0
    return result.replace([np.inf, -np.inf], np.nan)

# park 126d jerk(2nd deriv) roc=55d
def f11re_f11_range_vol_estimators_park_126d_jerk_v006_signal(high, low):
    base = _f11_parkinson(high, low, 126)
    result = (base - 2.0 * base.shift(55) + base.shift(110)) / 3025.0
    return result.replace([np.inf, -np.inf], np.nan)

# park 252d jerk(2nd deriv) roc=80d
def f11re_f11_range_vol_estimators_park_252d_jerk_v007_signal(high, low):
    base = _f11_parkinson(high, low, 252)
    result = (base - 2.0 * base.shift(80) + base.shift(160)) / 6400.0
    return result.replace([np.inf, -np.inf], np.nan)

# gk 5d jerk(2nd deriv) roc=5d
def f11re_f11_range_vol_estimators_gk_5d_jerk_v008_signal(open, high, low, close):
    base = _f11_garman_klass(open, high, low, close, 5)
    result = (base - 2.0 * base.shift(5) + base.shift(10)) / 25.0
    return result.replace([np.inf, -np.inf], np.nan)

# gk 10d jerk(2nd deriv) roc=9d
def f11re_f11_range_vol_estimators_gk_10d_jerk_v009_signal(open, high, low, close):
    base = _f11_garman_klass(open, high, low, close, 10)
    result = (base - 2.0 * base.shift(9) + base.shift(18)) / 81.0
    return result.replace([np.inf, -np.inf], np.nan)

# gk 21d jerk(2nd deriv) roc=17d
def f11re_f11_range_vol_estimators_gk_21d_jerk_v010_signal(open, high, low, close):
    base = _f11_garman_klass(open, high, low, close, 21)
    result = (base - 2.0 * base.shift(17) + base.shift(34)) / 289.0
    return result.replace([np.inf, -np.inf], np.nan)

# gk 42d jerk(2nd deriv) roc=21d
def f11re_f11_range_vol_estimators_gk_42d_jerk_v011_signal(open, high, low, close):
    base = _f11_garman_klass(open, high, low, close, 42)
    result = (base - 2.0 * base.shift(21) + base.shift(42)) / 441.0
    return result.replace([np.inf, -np.inf], np.nan)

# gk 63d jerk(2nd deriv) roc=42d
def f11re_f11_range_vol_estimators_gk_63d_jerk_v012_signal(open, high, low, close):
    base = _f11_garman_klass(open, high, low, close, 63)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    return result.replace([np.inf, -np.inf], np.nan)

# gk 126d jerk(2nd deriv) roc=47d
def f11re_f11_range_vol_estimators_gk_126d_jerk_v013_signal(open, high, low, close):
    base = _f11_garman_klass(open, high, low, close, 126)
    result = (base - 2.0 * base.shift(47) + base.shift(94)) / 2209.0
    return result.replace([np.inf, -np.inf], np.nan)

# gk 252d jerk(2nd deriv) roc=63d
def f11re_f11_range_vol_estimators_gk_252d_jerk_v014_signal(open, high, low, close):
    base = _f11_garman_klass(open, high, low, close, 252)
    result = (base - 2.0 * base.shift(63) + base.shift(126)) / 3969.0
    return result.replace([np.inf, -np.inf], np.nan)

# rs 5d jerk(2nd deriv) roc=9d
def f11re_f11_range_vol_estimators_rs_5d_jerk_v015_signal(open, high, low, close):
    base = _f11_rogers_satchell(open, high, low, close, 5)
    result = (base - 2.0 * base.shift(9) + base.shift(18)) / 81.0
    return result.replace([np.inf, -np.inf], np.nan)

# rs 10d jerk(2nd deriv) roc=5d
def f11re_f11_range_vol_estimators_rs_10d_jerk_v016_signal(open, high, low, close):
    base = _f11_rogers_satchell(open, high, low, close, 10)
    result = (base - 2.0 * base.shift(5) + base.shift(10)) / 25.0
    return result.replace([np.inf, -np.inf], np.nan)

# rs 21d jerk(2nd deriv) roc=26d
def f11re_f11_range_vol_estimators_rs_21d_jerk_v017_signal(open, high, low, close):
    base = _f11_rogers_satchell(open, high, low, close, 21)
    result = (base - 2.0 * base.shift(26) + base.shift(52)) / 676.0
    return result.replace([np.inf, -np.inf], np.nan)

# rs 42d jerk(2nd deriv) roc=13d
def f11re_f11_range_vol_estimators_rs_42d_jerk_v018_signal(open, high, low, close):
    base = _f11_rogers_satchell(open, high, low, close, 42)
    result = (base - 2.0 * base.shift(13) + base.shift(26)) / 169.0
    return result.replace([np.inf, -np.inf], np.nan)

# rs 63d jerk(2nd deriv) roc=21d
def f11re_f11_range_vol_estimators_rs_63d_jerk_v019_signal(open, high, low, close):
    base = _f11_rogers_satchell(open, high, low, close, 63)
    result = (base - 2.0 * base.shift(21) + base.shift(42)) / 441.0
    return result.replace([np.inf, -np.inf], np.nan)

# rs 126d jerk(2nd deriv) roc=80d
def f11re_f11_range_vol_estimators_rs_126d_jerk_v020_signal(open, high, low, close):
    base = _f11_rogers_satchell(open, high, low, close, 126)
    result = (base - 2.0 * base.shift(80) + base.shift(160)) / 6400.0
    return result.replace([np.inf, -np.inf], np.nan)

# rs 252d jerk(2nd deriv) roc=47d
def f11re_f11_range_vol_estimators_rs_252d_jerk_v021_signal(open, high, low, close):
    base = _f11_rogers_satchell(open, high, low, close, 252)
    result = (base - 2.0 * base.shift(47) + base.shift(94)) / 2209.0
    return result.replace([np.inf, -np.inf], np.nan)

# atrp 5d jerk(2nd deriv) roc=5d
def f11re_f11_range_vol_estimators_atrp_5d_jerk_v022_signal(high, low, close):
    base = _f11_atr(high, low, close, 5) / close.replace(0, np.nan)
    result = (base - 2.0 * base.shift(5) + base.shift(10)) / 25.0
    return result.replace([np.inf, -np.inf], np.nan)

# atrp 14d jerk(2nd deriv) roc=9d
def f11re_f11_range_vol_estimators_atrp_14d_jerk_v023_signal(high, low, close):
    base = _f11_atr(high, low, close, 14) / close.replace(0, np.nan)
    result = (base - 2.0 * base.shift(9) + base.shift(18)) / 81.0
    return result.replace([np.inf, -np.inf], np.nan)

# atrp 21d jerk(2nd deriv) roc=13d
def f11re_f11_range_vol_estimators_atrp_21d_jerk_v024_signal(high, low, close):
    base = _f11_atr(high, low, close, 21) / close.replace(0, np.nan)
    result = (base - 2.0 * base.shift(13) + base.shift(26)) / 169.0
    return result.replace([np.inf, -np.inf], np.nan)

# atrp 42d jerk(2nd deriv) roc=26d
def f11re_f11_range_vol_estimators_atrp_42d_jerk_v025_signal(high, low, close):
    base = _f11_atr(high, low, close, 42) / close.replace(0, np.nan)
    result = (base - 2.0 * base.shift(26) + base.shift(52)) / 676.0
    return result.replace([np.inf, -np.inf], np.nan)

# atrp 63d jerk(2nd deriv) roc=34d
def f11re_f11_range_vol_estimators_atrp_63d_jerk_v026_signal(high, low, close):
    base = _f11_atr(high, low, close, 63) / close.replace(0, np.nan)
    result = (base - 2.0 * base.shift(34) + base.shift(68)) / 1156.0
    return result.replace([np.inf, -np.inf], np.nan)

# atrp 126d jerk(2nd deriv) roc=55d
def f11re_f11_range_vol_estimators_atrp_126d_jerk_v027_signal(high, low, close):
    base = _f11_atr(high, low, close, 126) / close.replace(0, np.nan)
    result = (base - 2.0 * base.shift(55) + base.shift(110)) / 3025.0
    return result.replace([np.inf, -np.inf], np.nan)

# atrp 252d jerk(2nd deriv) roc=80d
def f11re_f11_range_vol_estimators_atrp_252d_jerk_v028_signal(high, low, close):
    base = _f11_atr(high, low, close, 252) / close.replace(0, np.nan)
    result = (base - 2.0 * base.shift(80) + base.shift(160)) / 6400.0
    return result.replace([np.inf, -np.inf], np.nan)

# hlrng 5d jerk(2nd deriv) roc=7d
def f11re_f11_range_vol_estimators_hlrng_5d_jerk_v029_signal(high, low, close):
    base = _mean(_f11_hl_range_close(high, low, close), 5)
    result = (base - 2.0 * base.shift(7) + base.shift(14)) / 49.0
    return result.replace([np.inf, -np.inf], np.nan)

# hlrng 21d jerk(2nd deriv) roc=17d
def f11re_f11_range_vol_estimators_hlrng_21d_jerk_v030_signal(high, low, close):
    base = _mean(_f11_hl_range_close(high, low, close), 21)
    result = (base - 2.0 * base.shift(17) + base.shift(34)) / 289.0
    return result.replace([np.inf, -np.inf], np.nan)

# hlrng 42d jerk(2nd deriv) roc=21d
def f11re_f11_range_vol_estimators_hlrng_42d_jerk_v031_signal(high, low, close):
    base = _mean(_f11_hl_range_close(high, low, close), 42)
    result = (base - 2.0 * base.shift(21) + base.shift(42)) / 441.0
    return result.replace([np.inf, -np.inf], np.nan)

# hlrng 63d jerk(2nd deriv) roc=42d
def f11re_f11_range_vol_estimators_hlrng_63d_jerk_v032_signal(high, low, close):
    base = _mean(_f11_hl_range_close(high, low, close), 63)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    return result.replace([np.inf, -np.inf], np.nan)

# hlrng 126d jerk(2nd deriv) roc=47d
def f11re_f11_range_vol_estimators_hlrng_126d_jerk_v033_signal(high, low, close):
    base = _mean(_f11_hl_range_close(high, low, close), 126)
    result = (base - 2.0 * base.shift(47) + base.shift(94)) / 2209.0
    return result.replace([np.inf, -np.inf], np.nan)

# trz 21d jerk(2nd deriv) roc=11d
def f11re_f11_range_vol_estimators_trz_21d_jerk_v034_signal(high, low, close):
    tr = _f11_true_range(high, low, close)
    base = _z(tr, 21)
    result = (base - 2.0 * base.shift(11) + base.shift(22)) / 121.0
    return result.replace([np.inf, -np.inf], np.nan)

# trz 42d jerk(2nd deriv) roc=23d
def f11re_f11_range_vol_estimators_trz_42d_jerk_v035_signal(high, low, close):
    tr = _f11_true_range(high, low, close)
    base = _z(tr, 42)
    result = (base - 2.0 * base.shift(23) + base.shift(46)) / 529.0
    return result.replace([np.inf, -np.inf], np.nan)

# trz 63d jerk(2nd deriv) roc=31d
def f11re_f11_range_vol_estimators_trz_63d_jerk_v036_signal(high, low, close):
    tr = _f11_true_range(high, low, close)
    base = _z(tr, 63)
    result = (base - 2.0 * base.shift(31) + base.shift(62)) / 961.0
    return result.replace([np.inf, -np.inf], np.nan)

# trz 126d jerk(2nd deriv) roc=51d
def f11re_f11_range_vol_estimators_trz_126d_jerk_v037_signal(high, low, close):
    tr = _f11_true_range(high, low, close)
    base = _z(tr, 126)
    result = (base - 2.0 * base.shift(51) + base.shift(102)) / 2601.0
    return result.replace([np.inf, -np.inf], np.nan)

# parkterm 5v21d jerk(2nd deriv) roc=11d
def f11re_f11_range_vol_estimators_parkterm_5v21d_jerk_v038_signal(high, low):
    s = _f11_parkinson(high, low, 5)
    l = _f11_parkinson(high, low, 21)
    base = s / l.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(11) + base.shift(22)) / 121.0
    return result.replace([np.inf, -np.inf], np.nan)

# parkterm 10v42d jerk(2nd deriv) roc=23d
def f11re_f11_range_vol_estimators_parkterm_10v42d_jerk_v039_signal(high, low):
    s = _f11_parkinson(high, low, 10)
    l = _f11_parkinson(high, low, 42)
    base = s / l.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(23) + base.shift(46)) / 529.0
    return result.replace([np.inf, -np.inf], np.nan)

# parkterm 21v63d jerk(2nd deriv) roc=31d
def f11re_f11_range_vol_estimators_parkterm_21v63d_jerk_v040_signal(high, low):
    s = _f11_parkinson(high, low, 21)
    l = _f11_parkinson(high, low, 63)
    base = s / l.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(31) + base.shift(62)) / 961.0
    return result.replace([np.inf, -np.inf], np.nan)

# parkterm 21v126d jerk(2nd deriv) roc=44d
def f11re_f11_range_vol_estimators_parkterm_21v126d_jerk_v041_signal(high, low):
    s = _f11_parkinson(high, low, 21)
    l = _f11_parkinson(high, low, 126)
    base = s / l.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(44) + base.shift(88)) / 1936.0
    return result.replace([np.inf, -np.inf], np.nan)

# parkterm 63v252d jerk(2nd deriv) roc=66d
def f11re_f11_range_vol_estimators_parkterm_63v252d_jerk_v042_signal(high, low):
    s = _f11_parkinson(high, low, 63)
    l = _f11_parkinson(high, low, 252)
    base = s / l.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(66) + base.shift(132)) / 4356.0
    return result.replace([np.inf, -np.inf], np.nan)

# gkterm 5v21d jerk(2nd deriv) roc=13d
def f11re_f11_range_vol_estimators_gkterm_5v21d_jerk_v043_signal(open, high, low, close):
    s = _f11_garman_klass(open, high, low, close, 5)
    l = _f11_garman_klass(open, high, low, close, 21)
    base = s / l.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(13) + base.shift(26)) / 169.0
    return result.replace([np.inf, -np.inf], np.nan)

# gkterm 21v63d jerk(2nd deriv) roc=26d
def f11re_f11_range_vol_estimators_gkterm_21v63d_jerk_v044_signal(open, high, low, close):
    s = _f11_garman_klass(open, high, low, close, 21)
    l = _f11_garman_klass(open, high, low, close, 63)
    base = s / l.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(26) + base.shift(52)) / 676.0
    return result.replace([np.inf, -np.inf], np.nan)

# gkterm 21v126d jerk(2nd deriv) roc=47d
def f11re_f11_range_vol_estimators_gkterm_21v126d_jerk_v045_signal(open, high, low, close):
    s = _f11_garman_klass(open, high, low, close, 21)
    l = _f11_garman_klass(open, high, low, close, 126)
    base = s / l.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(47) + base.shift(94)) / 2209.0
    return result.replace([np.inf, -np.inf], np.nan)

# gkterm 63v252d jerk(2nd deriv) roc=63d
def f11re_f11_range_vol_estimators_gkterm_63v252d_jerk_v046_signal(open, high, low, close):
    s = _f11_garman_klass(open, high, low, close, 63)
    l = _f11_garman_klass(open, high, low, close, 252)
    base = s / l.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(63) + base.shift(126)) / 3969.0
    return result.replace([np.inf, -np.inf], np.nan)

# rsterm 10v42d jerk(2nd deriv) roc=21d
def f11re_f11_range_vol_estimators_rsterm_10v42d_jerk_v047_signal(open, high, low, close):
    s = _f11_rogers_satchell(open, high, low, close, 10)
    l = _f11_rogers_satchell(open, high, low, close, 42)
    base = s / l.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(21) + base.shift(42)) / 441.0
    return result.replace([np.inf, -np.inf], np.nan)

# rsterm 21v63d jerk(2nd deriv) roc=37d
def f11re_f11_range_vol_estimators_rsterm_21v63d_jerk_v048_signal(open, high, low, close):
    s = _f11_rogers_satchell(open, high, low, close, 21)
    l = _f11_rogers_satchell(open, high, low, close, 63)
    base = s / l.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(37) + base.shift(74)) / 1369.0
    return result.replace([np.inf, -np.inf], np.nan)

# rsterm 63v252d jerk(2nd deriv) roc=55d
def f11re_f11_range_vol_estimators_rsterm_63v252d_jerk_v049_signal(open, high, low, close):
    s = _f11_rogers_satchell(open, high, low, close, 63)
    l = _f11_rogers_satchell(open, high, low, close, 252)
    base = s / l.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(55) + base.shift(110)) / 3025.0
    return result.replace([np.inf, -np.inf], np.nan)

# atrterm 5v21d jerk(2nd deriv) roc=11d
def f11re_f11_range_vol_estimators_atrterm_5v21d_jerk_v050_signal(high, low, close):
    s = _f11_atr(high, low, close, 5) / close.replace(0, np.nan)
    l = _f11_atr(high, low, close, 21) / close.replace(0, np.nan)
    base = s / l.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(11) + base.shift(22)) / 121.0
    return result.replace([np.inf, -np.inf], np.nan)

# atrterm 14v63d jerk(2nd deriv) roc=26d
def f11re_f11_range_vol_estimators_atrterm_14v63d_jerk_v051_signal(high, low, close):
    s = _f11_atr(high, low, close, 14) / close.replace(0, np.nan)
    l = _f11_atr(high, low, close, 63) / close.replace(0, np.nan)
    base = s / l.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(26) + base.shift(52)) / 676.0
    return result.replace([np.inf, -np.inf], np.nan)

# atrterm 21v126d jerk(2nd deriv) roc=44d
def f11re_f11_range_vol_estimators_atrterm_21v126d_jerk_v052_signal(high, low, close):
    s = _f11_atr(high, low, close, 21) / close.replace(0, np.nan)
    l = _f11_atr(high, low, close, 126) / close.replace(0, np.nan)
    base = s / l.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(44) + base.shift(88)) / 1936.0
    return result.replace([np.inf, -np.inf], np.nan)

# pkgkspr 21d jerk(2nd deriv) roc=13d
def f11re_f11_range_vol_estimators_pkgkspr_21d_jerk_v053_signal(open, high, low, close):
    pk = _f11_parkinson(high, low, 21)
    gk = _f11_garman_klass(open, high, low, close, 21)
    base = (pk - gk) / (pk + gk).replace(0, np.nan)
    result = (base - 2.0 * base.shift(13) + base.shift(26)) / 169.0
    return result.replace([np.inf, -np.inf], np.nan)

# pkgkspr 63d jerk(2nd deriv) roc=31d
def f11re_f11_range_vol_estimators_pkgkspr_63d_jerk_v054_signal(open, high, low, close):
    pk = _f11_parkinson(high, low, 63)
    gk = _f11_garman_klass(open, high, low, close, 63)
    base = (pk - gk) / (pk + gk).replace(0, np.nan)
    result = (base - 2.0 * base.shift(31) + base.shift(62)) / 961.0
    return result.replace([np.inf, -np.inf], np.nan)

# pkgkspr 126d jerk(2nd deriv) roc=51d
def f11re_f11_range_vol_estimators_pkgkspr_126d_jerk_v055_signal(open, high, low, close):
    pk = _f11_parkinson(high, low, 126)
    gk = _f11_garman_klass(open, high, low, close, 126)
    base = (pk - gk) / (pk + gk).replace(0, np.nan)
    result = (base - 2.0 * base.shift(51) + base.shift(102)) / 2601.0
    return result.replace([np.inf, -np.inf], np.nan)

# pkrsspr 21d jerk(2nd deriv) roc=17d
def f11re_f11_range_vol_estimators_pkrsspr_21d_jerk_v056_signal(open, high, low, close):
    pk = _f11_parkinson(high, low, 21)
    rs = _f11_rogers_satchell(open, high, low, close, 21)
    base = (pk - rs) / (pk + rs).replace(0, np.nan)
    result = (base - 2.0 * base.shift(17) + base.shift(34)) / 289.0
    return result.replace([np.inf, -np.inf], np.nan)

# pkrsspr 63d jerk(2nd deriv) roc=37d
def f11re_f11_range_vol_estimators_pkrsspr_63d_jerk_v057_signal(open, high, low, close):
    pk = _f11_parkinson(high, low, 63)
    rs = _f11_rogers_satchell(open, high, low, close, 63)
    base = (pk - rs) / (pk + rs).replace(0, np.nan)
    result = (base - 2.0 * base.shift(37) + base.shift(74)) / 1369.0
    return result.replace([np.inf, -np.inf], np.nan)

# pkrsspr 126d jerk(2nd deriv) roc=44d
def f11re_f11_range_vol_estimators_pkrsspr_126d_jerk_v058_signal(open, high, low, close):
    pk = _f11_parkinson(high, low, 126)
    rs = _f11_rogers_satchell(open, high, low, close, 126)
    base = (pk - rs) / (pk + rs).replace(0, np.nan)
    result = (base - 2.0 * base.shift(44) + base.shift(88)) / 1936.0
    return result.replace([np.inf, -np.inf], np.nan)

# gkrsspr 21d jerk(2nd deriv) roc=23d
def f11re_f11_range_vol_estimators_gkrsspr_21d_jerk_v059_signal(open, high, low, close):
    gk = _f11_garman_klass(open, high, low, close, 21)
    rs = _f11_rogers_satchell(open, high, low, close, 21)
    base = (gk - rs) / (gk + rs).replace(0, np.nan)
    result = (base - 2.0 * base.shift(23) + base.shift(46)) / 529.0
    return result.replace([np.inf, -np.inf], np.nan)

# gkrsspr 63d jerk(2nd deriv) roc=42d
def f11re_f11_range_vol_estimators_gkrsspr_63d_jerk_v060_signal(open, high, low, close):
    gk = _f11_garman_klass(open, high, low, close, 63)
    rs = _f11_rogers_satchell(open, high, low, close, 63)
    base = (gk - rs) / (gk + rs).replace(0, np.nan)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    return result.replace([np.inf, -np.inf], np.nan)

# parkvov 63d jerk(2nd deriv) roc=31d
def f11re_f11_range_vol_estimators_parkvov_63d_jerk_v061_signal(high, low):
    pk = _f11_parkinson(high, low, 21)
    base = _std(pk, 63) / _mean(pk, 63).replace(0, np.nan)
    result = (base - 2.0 * base.shift(31) + base.shift(62)) / 961.0
    return result.replace([np.inf, -np.inf], np.nan)

# parkvov 126d jerk(2nd deriv) roc=51d
def f11re_f11_range_vol_estimators_parkvov_126d_jerk_v062_signal(high, low):
    pk = _f11_parkinson(high, low, 21)
    base = _std(pk, 126) / _mean(pk, 126).replace(0, np.nan)
    result = (base - 2.0 * base.shift(51) + base.shift(102)) / 2601.0
    return result.replace([np.inf, -np.inf], np.nan)

# gkvov 63d jerk(2nd deriv) roc=37d
def f11re_f11_range_vol_estimators_gkvov_63d_jerk_v063_signal(open, high, low, close):
    gk = _f11_garman_klass(open, high, low, close, 21)
    base = _std(gk, 63) / _mean(gk, 63).replace(0, np.nan)
    result = (base - 2.0 * base.shift(37) + base.shift(74)) / 1369.0
    return result.replace([np.inf, -np.inf], np.nan)

# gkvov 126d jerk(2nd deriv) roc=44d
def f11re_f11_range_vol_estimators_gkvov_126d_jerk_v064_signal(open, high, low, close):
    gk = _f11_garman_klass(open, high, low, close, 21)
    base = _std(gk, 126) / _mean(gk, 126).replace(0, np.nan)
    result = (base - 2.0 * base.shift(44) + base.shift(88)) / 1936.0
    return result.replace([np.inf, -np.inf], np.nan)

# atrvov 63d jerk(2nd deriv) roc=34d
def f11re_f11_range_vol_estimators_atrvov_63d_jerk_v065_signal(high, low, close):
    atrp = _f11_atr(high, low, close, 14) / close.replace(0, np.nan)
    base = _std(atrp, 63) / _mean(atrp, 63).replace(0, np.nan)
    result = (base - 2.0 * base.shift(34) + base.shift(68)) / 1156.0
    return result.replace([np.inf, -np.inf], np.nan)

# overnightvol 21d jerk(2nd deriv) roc=11d
def f11re_f11_range_vol_estimators_overnightvol_21d_jerk_v066_signal(open, close):
    o = _f11_overnight(open, close)
    base = _std(o, 21)
    result = (base - 2.0 * base.shift(11) + base.shift(22)) / 121.0
    return result.replace([np.inf, -np.inf], np.nan)

# overnightvol 63d jerk(2nd deriv) roc=34d
def f11re_f11_range_vol_estimators_overnightvol_63d_jerk_v067_signal(open, close):
    o = _f11_overnight(open, close)
    base = _std(o, 63)
    result = (base - 2.0 * base.shift(34) + base.shift(68)) / 1156.0
    return result.replace([np.inf, -np.inf], np.nan)

# overnightvol 126d jerk(2nd deriv) roc=55d
def f11re_f11_range_vol_estimators_overnightvol_126d_jerk_v068_signal(open, close):
    o = _f11_overnight(open, close)
    base = _std(o, 126)
    result = (base - 2.0 * base.shift(55) + base.shift(110)) / 3025.0
    return result.replace([np.inf, -np.inf], np.nan)

# intravol 21d jerk(2nd deriv) roc=13d
def f11re_f11_range_vol_estimators_intravol_21d_jerk_v069_signal(open, close):
    c = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    base = _std(c, 21)
    result = (base - 2.0 * base.shift(13) + base.shift(26)) / 169.0
    return result.replace([np.inf, -np.inf], np.nan)

# intravol 63d jerk(2nd deriv) roc=42d
def f11re_f11_range_vol_estimators_intravol_63d_jerk_v070_signal(open, close):
    c = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    base = _std(c, 63)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    return result.replace([np.inf, -np.inf], np.nan)

# upsemi 21d jerk(2nd deriv) roc=13d
def f11re_f11_range_vol_estimators_upsemi_21d_jerk_v071_signal(high, open):
    up = np.log(high.replace(0, np.nan) / open.replace(0, np.nan)).clip(lower=0)
    base = np.sqrt((up ** 2).rolling(21, min_periods=max(2, 21 // 2)).mean())
    result = (base - 2.0 * base.shift(13) + base.shift(26)) / 169.0
    return result.replace([np.inf, -np.inf], np.nan)

# upsemi 63d jerk(2nd deriv) roc=34d
def f11re_f11_range_vol_estimators_upsemi_63d_jerk_v072_signal(high, open):
    up = np.log(high.replace(0, np.nan) / open.replace(0, np.nan)).clip(lower=0)
    base = np.sqrt((up ** 2).rolling(63, min_periods=max(2, 63 // 2)).mean())
    result = (base - 2.0 * base.shift(34) + base.shift(68)) / 1156.0
    return result.replace([np.inf, -np.inf], np.nan)

# downsemi 21d jerk(2nd deriv) roc=17d
def f11re_f11_range_vol_estimators_downsemi_21d_jerk_v073_signal(open, low):
    dn = np.log(open.replace(0, np.nan) / low.replace(0, np.nan)).clip(lower=0)
    base = np.sqrt((dn ** 2).rolling(21, min_periods=max(2, 21 // 2)).mean())
    result = (base - 2.0 * base.shift(17) + base.shift(34)) / 289.0
    return result.replace([np.inf, -np.inf], np.nan)

# downsemi 63d jerk(2nd deriv) roc=42d
def f11re_f11_range_vol_estimators_downsemi_63d_jerk_v074_signal(open, low):
    dn = np.log(open.replace(0, np.nan) / low.replace(0, np.nan)).clip(lower=0)
    base = np.sqrt((dn ** 2).rolling(63, min_periods=max(2, 63 // 2)).mean())
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    return result.replace([np.inf, -np.inf], np.nan)

# semiskew 63d jerk(2nd deriv) roc=34d
def f11re_f11_range_vol_estimators_semiskew_63d_jerk_v075_signal(open, high, low):
    up = np.log(high.replace(0, np.nan) / open.replace(0, np.nan)).clip(lower=0)
    dn = np.log(open.replace(0, np.nan) / low.replace(0, np.nan)).clip(lower=0)
    uv = np.sqrt((up ** 2).rolling(63, min_periods=max(2, 63 // 2)).mean())
    dv = np.sqrt((dn ** 2).rolling(63, min_periods=max(2, 63 // 2)).mean())
    base = (uv - dv) / (uv + dv).replace(0, np.nan)
    result = (base - 2.0 * base.shift(34) + base.shift(68)) / 1156.0
    return result.replace([np.inf, -np.inf], np.nan)

# semiskew 126d jerk(2nd deriv) roc=51d
def f11re_f11_range_vol_estimators_semiskew_126d_jerk_v076_signal(open, high, low):
    up = np.log(high.replace(0, np.nan) / open.replace(0, np.nan)).clip(lower=0)
    dn = np.log(open.replace(0, np.nan) / low.replace(0, np.nan)).clip(lower=0)
    uv = np.sqrt((up ** 2).rolling(126, min_periods=max(2, 126 // 2)).mean())
    dv = np.sqrt((dn ** 2).rolling(126, min_periods=max(2, 126 // 2)).mean())
    base = (uv - dv) / (uv + dv).replace(0, np.nan)
    result = (base - 2.0 * base.shift(51) + base.shift(102)) / 2601.0
    return result.replace([np.inf, -np.inf], np.nan)

# parkadj 63d jerk(2nd deriv) roc=31d
def f11re_f11_range_vol_estimators_parkadj_63d_jerk_v077_signal(high, low, closeadj):
    base = _f11_parkinson(high, low, 63) / closeadj.replace(0, np.nan)
    result = (base - 2.0 * base.shift(31) + base.shift(62)) / 961.0
    return result.replace([np.inf, -np.inf], np.nan)

# parkadj 126d jerk(2nd deriv) roc=47d
def f11re_f11_range_vol_estimators_parkadj_126d_jerk_v078_signal(high, low, closeadj):
    base = _f11_parkinson(high, low, 126) / closeadj.replace(0, np.nan)
    result = (base - 2.0 * base.shift(47) + base.shift(94)) / 2209.0
    return result.replace([np.inf, -np.inf], np.nan)

# parkadj 252d jerk(2nd deriv) roc=66d
def f11re_f11_range_vol_estimators_parkadj_252d_jerk_v079_signal(high, low, closeadj):
    base = _f11_parkinson(high, low, 252) / closeadj.replace(0, np.nan)
    result = (base - 2.0 * base.shift(66) + base.shift(132)) / 4356.0
    return result.replace([np.inf, -np.inf], np.nan)

# hlrngadjz 63d jerk(2nd deriv) roc=31d
def f11re_f11_range_vol_estimators_hlrngadjz_63d_jerk_v080_signal(high, low, closeadj):
    hl = ((high - low) / closeadj.replace(0, np.nan)).rolling(63, min_periods=max(2, 63 // 2)).mean()
    base = _z(hl, 252)
    result = (base - 2.0 * base.shift(31) + base.shift(62)) / 961.0
    return result.replace([np.inf, -np.inf], np.nan)

# hlrngadjz 126d jerk(2nd deriv) roc=47d
def f11re_f11_range_vol_estimators_hlrngadjz_126d_jerk_v081_signal(high, low, closeadj):
    hl = ((high - low) / closeadj.replace(0, np.nan)).rolling(126, min_periods=max(2, 126 // 2)).mean()
    base = _z(hl, 252)
    result = (base - 2.0 * base.shift(47) + base.shift(94)) / 2209.0
    return result.replace([np.inf, -np.inf], np.nan)

# hlrngadjz 252d jerk(2nd deriv) roc=66d
def f11re_f11_range_vol_estimators_hlrngadjz_252d_jerk_v082_signal(high, low, closeadj):
    hl = ((high - low) / closeadj.replace(0, np.nan)).rolling(252, min_periods=max(2, 252 // 2)).mean()
    base = _z(hl, 252)
    result = (base - 2.0 * base.shift(66) + base.shift(132)) / 4356.0
    return result.replace([np.inf, -np.inf], np.nan)

# rangeff 21d jerk(2nd deriv) roc=13d
def f11re_f11_range_vol_estimators_rangeff_21d_jerk_v083_signal(high, low, close):
    net = (close - close.shift(21)).abs()
    path = (high - low).rolling(21, min_periods=max(2, 21 // 2)).sum()
    base = net / path.replace(0, np.nan)
    result = (base - 2.0 * base.shift(13) + base.shift(26)) / 169.0
    return result.replace([np.inf, -np.inf], np.nan)

# rangeff 63d jerk(2nd deriv) roc=34d
def f11re_f11_range_vol_estimators_rangeff_63d_jerk_v084_signal(high, low, close):
    net = (close - close.shift(63)).abs()
    path = (high - low).rolling(63, min_periods=max(2, 63 // 2)).sum()
    base = net / path.replace(0, np.nan)
    result = (base - 2.0 * base.shift(34) + base.shift(68)) / 1156.0
    return result.replace([np.inf, -np.inf], np.nan)

# bodyrange 21d jerk(2nd deriv) roc=13d
def f11re_f11_range_vol_estimators_bodyrange_21d_jerk_v085_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low)
    base = _mean(body / rng.replace(0, np.nan), 21)
    result = (base - 2.0 * base.shift(13) + base.shift(26)) / 169.0
    return result.replace([np.inf, -np.inf], np.nan)

# bodyrange 63d jerk(2nd deriv) roc=34d
def f11re_f11_range_vol_estimators_bodyrange_63d_jerk_v086_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low)
    base = _mean(body / rng.replace(0, np.nan), 63)
    result = (base - 2.0 * base.shift(34) + base.shift(68)) / 1156.0
    return result.replace([np.inf, -np.inf], np.nan)

# uppershadow 21d jerk(2nd deriv) roc=17d
def f11re_f11_range_vol_estimators_uppershadow_21d_jerk_v087_signal(open, high, close):
    body_hi = pd.concat([open, close], axis=1).max(axis=1)
    base = _mean((high - body_hi) / close.replace(0, np.nan), 21)
    result = (base - 2.0 * base.shift(17) + base.shift(34)) / 289.0
    return result.replace([np.inf, -np.inf], np.nan)

# uppershadow 63d jerk(2nd deriv) roc=42d
def f11re_f11_range_vol_estimators_uppershadow_63d_jerk_v088_signal(open, high, close):
    body_hi = pd.concat([open, close], axis=1).max(axis=1)
    base = _mean((high - body_hi) / close.replace(0, np.nan), 63)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    return result.replace([np.inf, -np.inf], np.nan)

# lowershadow 21d jerk(2nd deriv) roc=23d
def f11re_f11_range_vol_estimators_lowershadow_21d_jerk_v089_signal(open, low, close):
    body_lo = pd.concat([open, close], axis=1).min(axis=1)
    base = _mean((body_lo - low) / close.replace(0, np.nan), 21)
    result = (base - 2.0 * base.shift(23) + base.shift(46)) / 529.0
    return result.replace([np.inf, -np.inf], np.nan)

# lowershadow 63d jerk(2nd deriv) roc=37d
def f11re_f11_range_vol_estimators_lowershadow_63d_jerk_v090_signal(open, low, close):
    body_lo = pd.concat([open, close], axis=1).min(axis=1)
    base = _mean((body_lo - low) / close.replace(0, np.nan), 63)
    result = (base - 2.0 * base.shift(37) + base.shift(74)) / 1369.0
    return result.replace([np.inf, -np.inf], np.nan)

# trgap 21d jerk(2nd deriv) roc=13d
def f11re_f11_range_vol_estimators_trgap_21d_jerk_v091_signal(high, low, close):
    tr = _f11_true_range(high, low, close)
    base = _mean((tr - (high - low)) / close.replace(0, np.nan), 21)
    result = (base - 2.0 * base.shift(13) + base.shift(26)) / 169.0
    return result.replace([np.inf, -np.inf], np.nan)

# trgap 63d jerk(2nd deriv) roc=34d
def f11re_f11_range_vol_estimators_trgap_63d_jerk_v092_signal(high, low, close):
    tr = _f11_true_range(high, low, close)
    base = _mean((tr - (high - low)) / close.replace(0, np.nan), 63)
    result = (base - 2.0 * base.shift(34) + base.shift(68)) / 1156.0
    return result.replace([np.inf, -np.inf], np.nan)

# closeloc 21d jerk(2nd deriv) roc=17d
def f11re_f11_range_vol_estimators_closeloc_21d_jerk_v093_signal(high, low, close):
    loc = (close - low) / (high - low).replace(0, np.nan)
    base = _mean(loc, 21) - 0.5
    result = (base - 2.0 * base.shift(17) + base.shift(34)) / 289.0
    return result.replace([np.inf, -np.inf], np.nan)

# closeloc 63d jerk(2nd deriv) roc=42d
def f11re_f11_range_vol_estimators_closeloc_63d_jerk_v094_signal(high, low, close):
    loc = (close - low) / (high - low).replace(0, np.nan)
    base = _mean(loc, 63) - 0.5
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    return result.replace([np.inf, -np.inf], np.nan)

# parkrank 5d jerk(2nd deriv) roc=5d
def f11re_f11_range_vol_estimators_parkrank_5d_jerk_v095_signal(high, low):
    pk = _f11_parkinson(high, low, 5)
    base = pk.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = (base - 2.0 * base.shift(5) + base.shift(10)) / 25.0
    return result.replace([np.inf, -np.inf], np.nan)

# parkrank 21d jerk(2nd deriv) roc=13d
def f11re_f11_range_vol_estimators_parkrank_21d_jerk_v096_signal(high, low):
    pk = _f11_parkinson(high, low, 21)
    base = pk.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = (base - 2.0 * base.shift(13) + base.shift(26)) / 169.0
    return result.replace([np.inf, -np.inf], np.nan)

# parkrank 63d jerk(2nd deriv) roc=34d
def f11re_f11_range_vol_estimators_parkrank_63d_jerk_v097_signal(high, low):
    pk = _f11_parkinson(high, low, 63)
    base = pk.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = (base - 2.0 * base.shift(34) + base.shift(68)) / 1156.0
    return result.replace([np.inf, -np.inf], np.nan)

# atrprank 21d jerk(2nd deriv) roc=17d
def f11re_f11_range_vol_estimators_atrprank_21d_jerk_v098_signal(high, low, close):
    atrp = _f11_atr(high, low, close, 21) / close.replace(0, np.nan)
    base = atrp.rolling(252, min_periods=max(2, 252 // 2)).rank(pct=True) - 0.5
    result = (base - 2.0 * base.shift(17) + base.shift(34)) / 289.0
    return result.replace([np.inf, -np.inf], np.nan)

# atrprank 63d jerk(2nd deriv) roc=42d
def f11re_f11_range_vol_estimators_atrprank_63d_jerk_v099_signal(high, low, close):
    atrp = _f11_atr(high, low, close, 63) / close.replace(0, np.nan)
    base = atrp.rolling(504, min_periods=max(2, 504 // 2)).rank(pct=True) - 0.5
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    return result.replace([np.inf, -np.inf], np.nan)

# parkdisp ewm42d jerk(2nd deriv) roc=21d
def f11re_f11_range_vol_estimators_parkdisp_ewm42d_jerk_v100_signal(high, low):
    pk = _f11_parkinson(high, low, 21)
    base = pk - pk.ewm(span=42, min_periods=21).mean()
    result = (base - 2.0 * base.shift(21) + base.shift(42)) / 441.0
    return result.replace([np.inf, -np.inf], np.nan)

# gkdisp ewm42d jerk(2nd deriv) roc=21d
def f11re_f11_range_vol_estimators_gkdisp_ewm42d_jerk_v101_signal(open, high, low, close):
    gk = _f11_garman_klass(open, high, low, close, 21)
    base = gk - gk.ewm(span=42, min_periods=21).mean()
    result = (base - 2.0 * base.shift(21) + base.shift(42)) / 441.0
    return result.replace([np.inf, -np.inf], np.nan)

# rangecv 63d jerk(2nd deriv) roc=31d
def f11re_f11_range_vol_estimators_rangecv_63d_jerk_v102_signal(high, low, close):
    hl = _f11_hl_range_close(high, low, close)
    base = _std(hl, 63) / _mean(hl, 63).replace(0, np.nan)
    result = (base - 2.0 * base.shift(31) + base.shift(62)) / 961.0
    return result.replace([np.inf, -np.inf], np.nan)

# rangecv 126d jerk(2nd deriv) roc=51d
def f11re_f11_range_vol_estimators_rangecv_126d_jerk_v103_signal(high, low, close):
    hl = _f11_hl_range_close(high, low, close)
    base = _std(hl, 126) / _mean(hl, 126).replace(0, np.nan)
    result = (base - 2.0 * base.shift(51) + base.shift(102)) / 2601.0
    return result.replace([np.inf, -np.inf], np.nan)

# trcv 63d jerk(2nd deriv) roc=37d
def f11re_f11_range_vol_estimators_trcv_63d_jerk_v104_signal(high, low, close):
    tr = _f11_true_range(high, low, close)
    base = _std(tr, 63) / _mean(tr, 63).replace(0, np.nan)
    result = (base - 2.0 * base.shift(37) + base.shift(74)) / 1369.0
    return result.replace([np.inf, -np.inf], np.nan)

# gkyzprem 63d jerk(2nd deriv) roc=31d
def f11re_f11_range_vol_estimators_gkyzprem_63d_jerk_v105_signal(open, high, low, close):
    o = _f11_overnight(open, close)
    t = o ** 2 + _f11_gk_term(open, high, low, close)
    gkyz = np.sqrt(t.rolling(63, min_periods=32).mean().clip(lower=0))
    gk = _f11_garman_klass(open, high, low, close, 63)
    base = gkyz / gk.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(31) + base.shift(62)) / 961.0
    return result.replace([np.inf, -np.inf], np.nan)

# gapshare 63d jerk(2nd deriv) roc=34d
def f11re_f11_range_vol_estimators_gapshare_63d_jerk_v106_signal(open, high, low, close):
    o = _f11_overnight(open, close) ** 2
    tot = o + _f11_gk_term(open, high, low, close)
    base = o.rolling(63, min_periods=max(2, 63 // 2)).mean() / tot.rolling(63, min_periods=max(2, 63 // 2)).mean().replace(0, np.nan)
    result = (base - 2.0 * base.shift(34) + base.shift(68)) / 1156.0
    return result.replace([np.inf, -np.inf], np.nan)

# gapshare 126d jerk(2nd deriv) roc=51d
def f11re_f11_range_vol_estimators_gapshare_126d_jerk_v107_signal(open, high, low, close):
    o = _f11_overnight(open, close) ** 2
    tot = o + _f11_gk_term(open, high, low, close)
    base = o.rolling(126, min_periods=max(2, 126 // 2)).mean() / tot.rolling(126, min_periods=max(2, 126 // 2)).mean().replace(0, np.nan)
    result = (base - 2.0 * base.shift(51) + base.shift(102)) / 2601.0
    return result.replace([np.inf, -np.inf], np.nan)

# parkrvdiv 63d jerk(2nd deriv) roc=31d
def f11re_f11_range_vol_estimators_parkrvdiv_63d_jerk_v108_signal(high, low, closeadj):
    pk = _f11_parkinson(high, low, 63)
    rv = closeadj.pct_change().rolling(63, min_periods=max(2, 63 // 2)).std()
    base = pk / rv.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(31) + base.shift(62)) / 961.0
    return result.replace([np.inf, -np.inf], np.nan)

# parkrvdiv 126d jerk(2nd deriv) roc=47d
def f11re_f11_range_vol_estimators_parkrvdiv_126d_jerk_v109_signal(high, low, closeadj):
    pk = _f11_parkinson(high, low, 126)
    rv = closeadj.pct_change().rolling(126, min_periods=max(2, 126 // 2)).std()
    base = pk / rv.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(47) + base.shift(94)) / 2209.0
    return result.replace([np.inf, -np.inf], np.nan)

# rsrvdiv 63d jerk(2nd deriv) roc=37d
def f11re_f11_range_vol_estimators_rsrvdiv_63d_jerk_v110_signal(open, high, low, close, closeadj):
    rs = _f11_rogers_satchell(open, high, low, close, 63)
    rv = closeadj.pct_change().rolling(63, min_periods=max(2, 63 // 2)).std()
    base = rs / rv.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(37) + base.shift(74)) / 1369.0
    return result.replace([np.inf, -np.inf], np.nan)

# rsrvdiv 126d jerk(2nd deriv) roc=55d
def f11re_f11_range_vol_estimators_rsrvdiv_126d_jerk_v111_signal(open, high, low, close, closeadj):
    rs = _f11_rogers_satchell(open, high, low, close, 126)
    rv = closeadj.pct_change().rolling(126, min_periods=max(2, 126 // 2)).std()
    base = rs / rv.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(55) + base.shift(110)) / 3025.0
    return result.replace([np.inf, -np.inf], np.nan)

# rangeffz 63d jerk(2nd deriv) roc=34d
def f11re_f11_range_vol_estimators_rangeffz_63d_jerk_v112_signal(high, low, closeadj):
    net = (closeadj - closeadj.shift(63)).abs()
    path = (high - low).rolling(63, min_periods=max(2, 63 // 2)).sum()
    eff = net / path.replace(0, np.nan)
    base = _z(eff, 252)
    result = (base - 2.0 * base.shift(34) + base.shift(68)) / 1156.0
    return result.replace([np.inf, -np.inf], np.nan)

# rangeffz 126d jerk(2nd deriv) roc=55d
def f11re_f11_range_vol_estimators_rangeffz_126d_jerk_v113_signal(high, low, closeadj):
    net = (closeadj - closeadj.shift(126)).abs()
    path = (high - low).rolling(126, min_periods=max(2, 126 // 2)).sum()
    eff = net / path.replace(0, np.nan)
    base = _z(eff, 252)
    result = (base - 2.0 * base.shift(55) + base.shift(110)) / 3025.0
    return result.replace([np.inf, -np.inf], np.nan)

# trtail 63d jerk(2nd deriv) roc=34d
def f11re_f11_range_vol_estimators_trtail_63d_jerk_v114_signal(high, low, close):
    tr = _f11_true_range(high, low, close) / close.replace(0, np.nan)
    q90 = tr.rolling(63, min_periods=max(2, 63 // 2)).quantile(0.9)
    med = tr.rolling(63, min_periods=max(2, 63 // 2)).median()
    base = q90 / med.replace(0, np.nan)
    result = (base - 2.0 * base.shift(34) + base.shift(68)) / 1156.0
    return result.replace([np.inf, -np.inf], np.nan)

# trtail 126d jerk(2nd deriv) roc=51d
def f11re_f11_range_vol_estimators_trtail_126d_jerk_v115_signal(high, low, close):
    tr = _f11_true_range(high, low, close) / close.replace(0, np.nan)
    q90 = tr.rolling(126, min_periods=max(2, 126 // 2)).quantile(0.9)
    med = tr.rolling(126, min_periods=max(2, 126 // 2)).median()
    base = q90 / med.replace(0, np.nan)
    result = (base - 2.0 * base.shift(51) + base.shift(102)) / 2601.0
    return result.replace([np.inf, -np.inf], np.nan)

# updownrange 63d jerk(2nd deriv) roc=34d
def f11re_f11_range_vol_estimators_updownrange_63d_jerk_v116_signal(high, low, close):
    hl = _f11_hl_range_close(high, low, close)
    up = (close > close.shift(1))
    up_r = hl.where(up).rolling(63, min_periods=20).mean()
    dn_r = hl.where(~up).rolling(63, min_periods=20).mean()
    base = (dn_r - up_r) / (dn_r + up_r).replace(0, np.nan)
    result = (base - 2.0 * base.shift(34) + base.shift(68)) / 1156.0
    return result.replace([np.inf, -np.inf], np.nan)

# updownrange 126d jerk(2nd deriv) roc=51d
def f11re_f11_range_vol_estimators_updownrange_126d_jerk_v117_signal(high, low, close):
    hl = _f11_hl_range_close(high, low, close)
    up = (close > close.shift(1))
    up_r = hl.where(up).rolling(126, min_periods=20).mean()
    dn_r = hl.where(~up).rolling(126, min_periods=20).mean()
    base = (dn_r - up_r) / (dn_r + up_r).replace(0, np.nan)
    result = (base - 2.0 * base.shift(51) + base.shift(102)) / 2601.0
    return result.replace([np.inf, -np.inf], np.nan)

# parkatrratio 63d jerk(2nd deriv) roc=34d
def f11re_f11_range_vol_estimators_parkatrratio_63d_jerk_v118_signal(high, low, close):
    pk = _f11_parkinson(high, low, 63) * close
    atr = _f11_atr(high, low, close, 63)
    base = pk / atr.replace(0, np.nan)
    result = (base - 2.0 * base.shift(34) + base.shift(68)) / 1156.0
    return result.replace([np.inf, -np.inf], np.nan)

# parkatrratio 126d jerk(2nd deriv) roc=51d
def f11re_f11_range_vol_estimators_parkatrratio_126d_jerk_v119_signal(high, low, close):
    pk = _f11_parkinson(high, low, 126) * close
    atr = _f11_atr(high, low, close, 126)
    base = pk / atr.replace(0, np.nan)
    result = (base - 2.0 * base.shift(51) + base.shift(102)) / 2601.0
    return result.replace([np.inf, -np.inf], np.nan)

# ccparkvr 63d jerk(2nd deriv) roc=34d
def f11re_f11_range_vol_estimators_ccparkvr_63d_jerk_v120_signal(high, low, closeadj):
    cc = closeadj.pct_change().rolling(63, min_periods=max(2, 63 // 2)).std()
    pk = _f11_parkinson(high, low, 63)
    base = (cc / pk.replace(0, np.nan)) ** 2 - 1.0
    result = (base - 2.0 * base.shift(34) + base.shift(68)) / 1156.0
    return result.replace([np.inf, -np.inf], np.nan)

# ccparkvr 126d jerk(2nd deriv) roc=51d
def f11re_f11_range_vol_estimators_ccparkvr_126d_jerk_v121_signal(high, low, closeadj):
    cc = closeadj.pct_change().rolling(126, min_periods=max(2, 126 // 2)).std()
    pk = _f11_parkinson(high, low, 126)
    base = (cc / pk.replace(0, np.nan)) ** 2 - 1.0
    result = (base - 2.0 * base.shift(51) + base.shift(102)) / 2601.0
    return result.replace([np.inf, -np.inf], np.nan)

# intravsover 63d jerk(2nd deriv) roc=34d
def f11re_f11_range_vol_estimators_intravsover_63d_jerk_v122_signal(open, high, low, close):
    intraday = (high - low) / close.replace(0, np.nan)
    overnight = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    base = _mean(intraday, 63) / _mean(overnight, 63).replace(0, np.nan)
    result = (base - 2.0 * base.shift(34) + base.shift(68)) / 1156.0
    return result.replace([np.inf, -np.inf], np.nan)

# atrgapdiv 63d jerk(2nd deriv) roc=31d
def f11re_f11_range_vol_estimators_atrgapdiv_63d_jerk_v123_signal(high, low, close):
    atr = _f11_atr(high, low, close, 63)
    simple = _mean(high - low, 63)
    base = atr / simple.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(31) + base.shift(62)) / 961.0
    return result.replace([np.inf, -np.inf], np.nan)

# rngbody 21d jerk(2nd deriv) roc=13d
def f11re_f11_range_vol_estimators_rngbody_21d_jerk_v124_signal(open, high, low, close):
    rng = (high - low)
    body = (close - open).abs()
    base = _mean(rng / body.replace(0, np.nan), 21)
    result = (base - 2.0 * base.shift(13) + base.shift(26)) / 169.0
    return result.replace([np.inf, -np.inf], np.nan)

# trconc 63d jerk(2nd deriv) roc=34d
def f11re_f11_range_vol_estimators_trconc_63d_jerk_v125_signal(high, low, close):
    tr = _f11_true_range(high, low, close) / close.replace(0, np.nan)
    s = tr.rolling(63, min_periods=32).sum()
    mx = tr.rolling(63, min_periods=32).max()
    base = mx / s.replace(0, np.nan)
    result = (base - 2.0 * base.shift(34) + base.shift(68)) / 1156.0
    return result.replace([np.inf, -np.inf], np.nan)

# triqr 63d jerk(2nd deriv) roc=34d
def f11re_f11_range_vol_estimators_triqr_63d_jerk_v126_signal(high, low, close):
    tr = _f11_true_range(high, low, close) / close.replace(0, np.nan)
    q75 = tr.rolling(63, min_periods=32).quantile(0.75)
    q25 = tr.rolling(63, min_periods=32).quantile(0.25)
    base = q75 - q25
    result = (base - 2.0 * base.shift(34) + base.shift(68)) / 1156.0
    return result.replace([np.inf, -np.inf], np.nan)

# yzvol 63d jerk(2nd deriv) roc=47d
def f11re_f11_range_vol_estimators_yzvol_63d_jerk_v127_signal(open, high, low, close):
    o = _f11_overnight(open, close)
    c = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    vo = ((o - o.rolling(63, min_periods=32).mean()) ** 2).rolling(63, min_periods=32).mean()
    vc = ((c - c.rolling(63, min_periods=32).mean()) ** 2).rolling(63, min_periods=32).mean()
    rsg = _f11_rs_term(open, high, low, close).rolling(63, min_periods=32).mean()
    k = 0.34 / (1.34 + 64.0 / 62.0)
    yz = np.sqrt((vo + k * vc + (1.0 - k) * rsg).clip(lower=0))
    base = _z(yz, 252)
    result = (base - 2.0 * base.shift(47) + base.shift(94)) / 2209.0
    return result.replace([np.inf, -np.inf], np.nan)

# gkpkcross 21v63d jerk(2nd deriv) roc=13d
def f11re_f11_range_vol_estimators_gkpkcross_21v63d_jerk_v128_signal(open, high, low, close):
    gk = _f11_garman_klass(open, high, low, close, 21)
    pk = _f11_parkinson(high, low, 63)
    base = gk / pk.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(13) + base.shift(26)) / 169.0
    return result.replace([np.inf, -np.inf], np.nan)

# gkpkcross 63v126d jerk(2nd deriv) roc=31d
def f11re_f11_range_vol_estimators_gkpkcross_63v126d_jerk_v129_signal(open, high, low, close):
    gk = _f11_garman_klass(open, high, low, close, 63)
    pk = _f11_parkinson(high, low, 126)
    base = gk / pk.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(31) + base.shift(62)) / 961.0
    return result.replace([np.inf, -np.inf], np.nan)

# gkpkcross 126v252d jerk(2nd deriv) roc=47d
def f11re_f11_range_vol_estimators_gkpkcross_126v252d_jerk_v130_signal(open, high, low, close):
    gk = _f11_garman_klass(open, high, low, close, 126)
    pk = _f11_parkinson(high, low, 252)
    base = gk / pk.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(47) + base.shift(94)) / 2209.0
    return result.replace([np.inf, -np.inf], np.nan)

# rsgkcross 21v63d jerk(2nd deriv) roc=17d
def f11re_f11_range_vol_estimators_rsgkcross_21v63d_jerk_v131_signal(open, high, low, close):
    rs = _f11_rogers_satchell(open, high, low, close, 21)
    gk = _f11_garman_klass(open, high, low, close, 63)
    base = rs / gk.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(17) + base.shift(34)) / 289.0
    return result.replace([np.inf, -np.inf], np.nan)

# rsgkcross 63v126d jerk(2nd deriv) roc=37d
def f11re_f11_range_vol_estimators_rsgkcross_63v126d_jerk_v132_signal(open, high, low, close):
    rs = _f11_rogers_satchell(open, high, low, close, 63)
    gk = _f11_garman_klass(open, high, low, close, 126)
    base = rs / gk.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(37) + base.shift(74)) / 1369.0
    return result.replace([np.inf, -np.inf], np.nan)

# rsgkcross 126v252d jerk(2nd deriv) roc=55d
def f11re_f11_range_vol_estimators_rsgkcross_126v252d_jerk_v133_signal(open, high, low, close):
    rs = _f11_rogers_satchell(open, high, low, close, 126)
    gk = _f11_garman_klass(open, high, low, close, 252)
    base = rs / gk.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(55) + base.shift(110)) / 3025.0
    return result.replace([np.inf, -np.inf], np.nan)

# trq10 63d jerk(2nd deriv) roc=34d
def f11re_f11_range_vol_estimators_trq10_63d_jerk_v134_signal(high, low, close):
    tr = _f11_true_range(high, low, close) / close.replace(0, np.nan)
    base = tr.rolling(63, min_periods=max(2, 63 // 2)).quantile(0.1)
    result = (base - 2.0 * base.shift(34) + base.shift(68)) / 1156.0
    return result.replace([np.inf, -np.inf], np.nan)

# trq10 126d jerk(2nd deriv) roc=51d
def f11re_f11_range_vol_estimators_trq10_126d_jerk_v135_signal(high, low, close):
    tr = _f11_true_range(high, low, close) / close.replace(0, np.nan)
    base = tr.rolling(126, min_periods=max(2, 126 // 2)).quantile(0.1)
    result = (base - 2.0 * base.shift(51) + base.shift(102)) / 2601.0
    return result.replace([np.inf, -np.inf], np.nan)

# parkdayskew 126d jerk(2nd deriv) roc=44d
def f11re_f11_range_vol_estimators_parkdayskew_126d_jerk_v136_signal(high, low):
    r2 = _f11_log_hl(high, low) ** 2
    base = r2.rolling(126, min_periods=63).skew()
    result = (base - 2.0 * base.shift(44) + base.shift(88)) / 1936.0
    return result.replace([np.inf, -np.inf], np.nan)

# trkurt 126d jerk(2nd deriv) roc=44d
def f11re_f11_range_vol_estimators_trkurt_126d_jerk_v137_signal(high, low, close):
    tr = _f11_true_range(high, low, close) / close.replace(0, np.nan)
    base = tr.rolling(126, min_periods=63).kurt()
    result = (base - 2.0 * base.shift(44) + base.shift(88)) / 1936.0
    return result.replace([np.inf, -np.inf], np.nan)

# rangeac 63d jerk(2nd deriv) roc=31d
def f11re_f11_range_vol_estimators_rangeac_63d_jerk_v138_signal(high, low, close):
    hl = _f11_hl_range_close(high, low, close)
    def _ac(a):
        x = a[:-1]; y = a[1:]
        if np.std(x) == 0 or np.std(y) == 0:
            return np.nan
        return np.corrcoef(x, y)[0, 1]
    base = hl.rolling(63, min_periods=40).apply(_ac, raw=True)
    result = (base - 2.0 * base.shift(31) + base.shift(62)) / 961.0
    return result.replace([np.inf, -np.inf], np.nan)

# gkrvdivz 63d jerk(2nd deriv) roc=42d
def f11re_f11_range_vol_estimators_gkrvdivz_63d_jerk_v139_signal(open, high, low, close, closeadj):
    gk = _f11_garman_klass(open, high, low, close, 63)
    rv = closeadj.pct_change().rolling(63, min_periods=max(2, 63 // 2)).std()
    ratio = gk / rv.replace(0, np.nan)
    base = _z(ratio, 252)
    result = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    return result.replace([np.inf, -np.inf], np.nan)

# gkrvdivz 126d jerk(2nd deriv) roc=47d
def f11re_f11_range_vol_estimators_gkrvdivz_126d_jerk_v140_signal(open, high, low, close, closeadj):
    gk = _f11_garman_klass(open, high, low, close, 126)
    rv = closeadj.pct_change().rolling(126, min_periods=max(2, 126 // 2)).std()
    ratio = gk / rv.replace(0, np.nan)
    base = _z(ratio, 252)
    result = (base - 2.0 * base.shift(47) + base.shift(94)) / 2209.0
    return result.replace([np.inf, -np.inf], np.nan)

# atrpewma ewm63d jerk(2nd deriv) roc=31d
def f11re_f11_range_vol_estimators_atrpewma_ewm63d_jerk_v141_signal(high, low, close):
    tr = _f11_true_range(high, low, close) / close.replace(0, np.nan)
    base = tr.ewm(span=63, min_periods=21).mean()
    result = (base - 2.0 * base.shift(31) + base.shift(62)) / 961.0
    return result.replace([np.inf, -np.inf], np.nan)

# rsewma ewm42d jerk(2nd deriv) roc=21d
def f11re_f11_range_vol_estimators_rsewma_ewm42d_jerk_v142_signal(open, high, low, close):
    t = _f11_rs_term(open, high, low, close).clip(lower=0)
    base = np.sqrt(t.ewm(span=42, min_periods=21).mean())
    result = (base - 2.0 * base.shift(21) + base.shift(42)) / 441.0
    return result.replace([np.inf, -np.inf], np.nan)

# gappkmix 63d jerk(2nd deriv) roc=37d
def f11re_f11_range_vol_estimators_gappkmix_63d_jerk_v143_signal(open, high, low, close):
    gapv = _std(_f11_overnight(open, close), 63)
    pk = _f11_parkinson(high, low, 63)
    base = _z(gapv / pk.replace(0, np.nan), 252)
    result = (base - 2.0 * base.shift(37) + base.shift(74)) / 1369.0
    return result.replace([np.inf, -np.inf], np.nan)

# overintravol 63d jerk(2nd deriv) roc=37d
def f11re_f11_range_vol_estimators_overintravol_63d_jerk_v144_signal(open, close):
    o = _std(_f11_overnight(open, close), 63)
    c = _std(np.log(close.replace(0, np.nan) / open.replace(0, np.nan)), 63)
    base = o / c.replace(0, np.nan)
    result = (base - 2.0 * base.shift(37) + base.shift(74)) / 1369.0
    return result.replace([np.inf, -np.inf], np.nan)

# overintravol 126d jerk(2nd deriv) roc=55d
def f11re_f11_range_vol_estimators_overintravol_126d_jerk_v145_signal(open, close):
    o = _std(_f11_overnight(open, close), 126)
    c = _std(np.log(close.replace(0, np.nan) / open.replace(0, np.nan)), 126)
    base = o / c.replace(0, np.nan)
    result = (base - 2.0 * base.shift(55) + base.shift(110)) / 3025.0
    return result.replace([np.inf, -np.inf], np.nan)

# rngccratio 126d jerk(2nd deriv) roc=44d
def f11re_f11_range_vol_estimators_rngccratio_126d_jerk_v146_signal(high, low, closeadj):
    hl = _mean((high - low) / closeadj.replace(0, np.nan), 126)
    cc = closeadj.pct_change().abs().rolling(126, min_periods=63).mean()
    base = hl / cc.replace(0, np.nan)
    result = (base - 2.0 * base.shift(44) + base.shift(88)) / 1936.0
    return result.replace([np.inf, -np.inf], np.nan)

# parkcurveshape multi jerk(2nd deriv) roc=21d
def f11re_f11_range_vol_estimators_parkcurveshape_multi_jerk_v147_signal(high, low):
    p5 = _f11_parkinson(high, low, 5)
    p21 = _f11_parkinson(high, low, 21)
    p63 = _f11_parkinson(high, low, 63)
    base = (p5 - 2.0 * p21 + p63) / p21.replace(0, np.nan)
    result = (base - 2.0 * base.shift(21) + base.shift(42)) / 441.0
    return result.replace([np.inf, -np.inf], np.nan)

# estdisp 63d jerk(2nd deriv) roc=34d
def f11re_f11_range_vol_estimators_estdisp_63d_jerk_v148_signal(open, high, low, close):
    pk = _f11_parkinson(high, low, 63)
    gk = _f11_garman_klass(open, high, low, close, 63)
    rs = _f11_rogers_satchell(open, high, low, close, 63)
    st = pd.concat([pk, gk, rs], axis=1)
    base = (st.max(axis=1) - st.min(axis=1)) / st.mean(axis=1).replace(0, np.nan)
    result = (base - 2.0 * base.shift(34) + base.shift(68)) / 1156.0
    return result.replace([np.inf, -np.inf], np.nan)

# parkdd 21d jerk(2nd deriv) roc=17d
def f11re_f11_range_vol_estimators_parkdd_21d_jerk_v149_signal(high, low):
    pk = _f11_parkinson(high, low, 21)
    pk_peak = pk.rolling(126, min_periods=63).max()
    base = pk / pk_peak.replace(0, np.nan) - 1.0
    result = (base - 2.0 * base.shift(17) + base.shift(34)) / 289.0
    return result.replace([np.inf, -np.inf], np.nan)

# volqual 21d jerk(2nd deriv) roc=13d
def f11re_f11_range_vol_estimators_volqual_21d_jerk_v150_signal(high, low, close):
    atrp = _f11_atr(high, low, close, 21) / close.replace(0, np.nan)
    net = (close - close.shift(21)).abs()
    path = (high - low).rolling(21, min_periods=11).sum()
    eff = net / path.replace(0, np.nan)
    base = atrp * (1.0 - eff)
    result = (base - 2.0 * base.shift(13) + base.shift(26)) / 169.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f11re_f11_range_vol_estimators_park_5d_jerk_v001_signal,
    f11re_f11_range_vol_estimators_park_10d_jerk_v002_signal,
    f11re_f11_range_vol_estimators_park_21d_jerk_v003_signal,
    f11re_f11_range_vol_estimators_park_42d_jerk_v004_signal,
    f11re_f11_range_vol_estimators_park_63d_jerk_v005_signal,
    f11re_f11_range_vol_estimators_park_126d_jerk_v006_signal,
    f11re_f11_range_vol_estimators_park_252d_jerk_v007_signal,
    f11re_f11_range_vol_estimators_gk_5d_jerk_v008_signal,
    f11re_f11_range_vol_estimators_gk_10d_jerk_v009_signal,
    f11re_f11_range_vol_estimators_gk_21d_jerk_v010_signal,
    f11re_f11_range_vol_estimators_gk_42d_jerk_v011_signal,
    f11re_f11_range_vol_estimators_gk_63d_jerk_v012_signal,
    f11re_f11_range_vol_estimators_gk_126d_jerk_v013_signal,
    f11re_f11_range_vol_estimators_gk_252d_jerk_v014_signal,
    f11re_f11_range_vol_estimators_rs_5d_jerk_v015_signal,
    f11re_f11_range_vol_estimators_rs_10d_jerk_v016_signal,
    f11re_f11_range_vol_estimators_rs_21d_jerk_v017_signal,
    f11re_f11_range_vol_estimators_rs_42d_jerk_v018_signal,
    f11re_f11_range_vol_estimators_rs_63d_jerk_v019_signal,
    f11re_f11_range_vol_estimators_rs_126d_jerk_v020_signal,
    f11re_f11_range_vol_estimators_rs_252d_jerk_v021_signal,
    f11re_f11_range_vol_estimators_atrp_5d_jerk_v022_signal,
    f11re_f11_range_vol_estimators_atrp_14d_jerk_v023_signal,
    f11re_f11_range_vol_estimators_atrp_21d_jerk_v024_signal,
    f11re_f11_range_vol_estimators_atrp_42d_jerk_v025_signal,
    f11re_f11_range_vol_estimators_atrp_63d_jerk_v026_signal,
    f11re_f11_range_vol_estimators_atrp_126d_jerk_v027_signal,
    f11re_f11_range_vol_estimators_atrp_252d_jerk_v028_signal,
    f11re_f11_range_vol_estimators_hlrng_5d_jerk_v029_signal,
    f11re_f11_range_vol_estimators_hlrng_21d_jerk_v030_signal,
    f11re_f11_range_vol_estimators_hlrng_42d_jerk_v031_signal,
    f11re_f11_range_vol_estimators_hlrng_63d_jerk_v032_signal,
    f11re_f11_range_vol_estimators_hlrng_126d_jerk_v033_signal,
    f11re_f11_range_vol_estimators_trz_21d_jerk_v034_signal,
    f11re_f11_range_vol_estimators_trz_42d_jerk_v035_signal,
    f11re_f11_range_vol_estimators_trz_63d_jerk_v036_signal,
    f11re_f11_range_vol_estimators_trz_126d_jerk_v037_signal,
    f11re_f11_range_vol_estimators_parkterm_5v21d_jerk_v038_signal,
    f11re_f11_range_vol_estimators_parkterm_10v42d_jerk_v039_signal,
    f11re_f11_range_vol_estimators_parkterm_21v63d_jerk_v040_signal,
    f11re_f11_range_vol_estimators_parkterm_21v126d_jerk_v041_signal,
    f11re_f11_range_vol_estimators_parkterm_63v252d_jerk_v042_signal,
    f11re_f11_range_vol_estimators_gkterm_5v21d_jerk_v043_signal,
    f11re_f11_range_vol_estimators_gkterm_21v63d_jerk_v044_signal,
    f11re_f11_range_vol_estimators_gkterm_21v126d_jerk_v045_signal,
    f11re_f11_range_vol_estimators_gkterm_63v252d_jerk_v046_signal,
    f11re_f11_range_vol_estimators_rsterm_10v42d_jerk_v047_signal,
    f11re_f11_range_vol_estimators_rsterm_21v63d_jerk_v048_signal,
    f11re_f11_range_vol_estimators_rsterm_63v252d_jerk_v049_signal,
    f11re_f11_range_vol_estimators_atrterm_5v21d_jerk_v050_signal,
    f11re_f11_range_vol_estimators_atrterm_14v63d_jerk_v051_signal,
    f11re_f11_range_vol_estimators_atrterm_21v126d_jerk_v052_signal,
    f11re_f11_range_vol_estimators_pkgkspr_21d_jerk_v053_signal,
    f11re_f11_range_vol_estimators_pkgkspr_63d_jerk_v054_signal,
    f11re_f11_range_vol_estimators_pkgkspr_126d_jerk_v055_signal,
    f11re_f11_range_vol_estimators_pkrsspr_21d_jerk_v056_signal,
    f11re_f11_range_vol_estimators_pkrsspr_63d_jerk_v057_signal,
    f11re_f11_range_vol_estimators_pkrsspr_126d_jerk_v058_signal,
    f11re_f11_range_vol_estimators_gkrsspr_21d_jerk_v059_signal,
    f11re_f11_range_vol_estimators_gkrsspr_63d_jerk_v060_signal,
    f11re_f11_range_vol_estimators_parkvov_63d_jerk_v061_signal,
    f11re_f11_range_vol_estimators_parkvov_126d_jerk_v062_signal,
    f11re_f11_range_vol_estimators_gkvov_63d_jerk_v063_signal,
    f11re_f11_range_vol_estimators_gkvov_126d_jerk_v064_signal,
    f11re_f11_range_vol_estimators_atrvov_63d_jerk_v065_signal,
    f11re_f11_range_vol_estimators_overnightvol_21d_jerk_v066_signal,
    f11re_f11_range_vol_estimators_overnightvol_63d_jerk_v067_signal,
    f11re_f11_range_vol_estimators_overnightvol_126d_jerk_v068_signal,
    f11re_f11_range_vol_estimators_intravol_21d_jerk_v069_signal,
    f11re_f11_range_vol_estimators_intravol_63d_jerk_v070_signal,
    f11re_f11_range_vol_estimators_upsemi_21d_jerk_v071_signal,
    f11re_f11_range_vol_estimators_upsemi_63d_jerk_v072_signal,
    f11re_f11_range_vol_estimators_downsemi_21d_jerk_v073_signal,
    f11re_f11_range_vol_estimators_downsemi_63d_jerk_v074_signal,
    f11re_f11_range_vol_estimators_semiskew_63d_jerk_v075_signal,
    f11re_f11_range_vol_estimators_semiskew_126d_jerk_v076_signal,
    f11re_f11_range_vol_estimators_parkadj_63d_jerk_v077_signal,
    f11re_f11_range_vol_estimators_parkadj_126d_jerk_v078_signal,
    f11re_f11_range_vol_estimators_parkadj_252d_jerk_v079_signal,
    f11re_f11_range_vol_estimators_hlrngadjz_63d_jerk_v080_signal,
    f11re_f11_range_vol_estimators_hlrngadjz_126d_jerk_v081_signal,
    f11re_f11_range_vol_estimators_hlrngadjz_252d_jerk_v082_signal,
    f11re_f11_range_vol_estimators_rangeff_21d_jerk_v083_signal,
    f11re_f11_range_vol_estimators_rangeff_63d_jerk_v084_signal,
    f11re_f11_range_vol_estimators_bodyrange_21d_jerk_v085_signal,
    f11re_f11_range_vol_estimators_bodyrange_63d_jerk_v086_signal,
    f11re_f11_range_vol_estimators_uppershadow_21d_jerk_v087_signal,
    f11re_f11_range_vol_estimators_uppershadow_63d_jerk_v088_signal,
    f11re_f11_range_vol_estimators_lowershadow_21d_jerk_v089_signal,
    f11re_f11_range_vol_estimators_lowershadow_63d_jerk_v090_signal,
    f11re_f11_range_vol_estimators_trgap_21d_jerk_v091_signal,
    f11re_f11_range_vol_estimators_trgap_63d_jerk_v092_signal,
    f11re_f11_range_vol_estimators_closeloc_21d_jerk_v093_signal,
    f11re_f11_range_vol_estimators_closeloc_63d_jerk_v094_signal,
    f11re_f11_range_vol_estimators_parkrank_5d_jerk_v095_signal,
    f11re_f11_range_vol_estimators_parkrank_21d_jerk_v096_signal,
    f11re_f11_range_vol_estimators_parkrank_63d_jerk_v097_signal,
    f11re_f11_range_vol_estimators_atrprank_21d_jerk_v098_signal,
    f11re_f11_range_vol_estimators_atrprank_63d_jerk_v099_signal,
    f11re_f11_range_vol_estimators_parkdisp_ewm42d_jerk_v100_signal,
    f11re_f11_range_vol_estimators_gkdisp_ewm42d_jerk_v101_signal,
    f11re_f11_range_vol_estimators_rangecv_63d_jerk_v102_signal,
    f11re_f11_range_vol_estimators_rangecv_126d_jerk_v103_signal,
    f11re_f11_range_vol_estimators_trcv_63d_jerk_v104_signal,
    f11re_f11_range_vol_estimators_gkyzprem_63d_jerk_v105_signal,
    f11re_f11_range_vol_estimators_gapshare_63d_jerk_v106_signal,
    f11re_f11_range_vol_estimators_gapshare_126d_jerk_v107_signal,
    f11re_f11_range_vol_estimators_parkrvdiv_63d_jerk_v108_signal,
    f11re_f11_range_vol_estimators_parkrvdiv_126d_jerk_v109_signal,
    f11re_f11_range_vol_estimators_rsrvdiv_63d_jerk_v110_signal,
    f11re_f11_range_vol_estimators_rsrvdiv_126d_jerk_v111_signal,
    f11re_f11_range_vol_estimators_rangeffz_63d_jerk_v112_signal,
    f11re_f11_range_vol_estimators_rangeffz_126d_jerk_v113_signal,
    f11re_f11_range_vol_estimators_trtail_63d_jerk_v114_signal,
    f11re_f11_range_vol_estimators_trtail_126d_jerk_v115_signal,
    f11re_f11_range_vol_estimators_updownrange_63d_jerk_v116_signal,
    f11re_f11_range_vol_estimators_updownrange_126d_jerk_v117_signal,
    f11re_f11_range_vol_estimators_parkatrratio_63d_jerk_v118_signal,
    f11re_f11_range_vol_estimators_parkatrratio_126d_jerk_v119_signal,
    f11re_f11_range_vol_estimators_ccparkvr_63d_jerk_v120_signal,
    f11re_f11_range_vol_estimators_ccparkvr_126d_jerk_v121_signal,
    f11re_f11_range_vol_estimators_intravsover_63d_jerk_v122_signal,
    f11re_f11_range_vol_estimators_atrgapdiv_63d_jerk_v123_signal,
    f11re_f11_range_vol_estimators_rngbody_21d_jerk_v124_signal,
    f11re_f11_range_vol_estimators_trconc_63d_jerk_v125_signal,
    f11re_f11_range_vol_estimators_triqr_63d_jerk_v126_signal,
    f11re_f11_range_vol_estimators_yzvol_63d_jerk_v127_signal,
    f11re_f11_range_vol_estimators_gkpkcross_21v63d_jerk_v128_signal,
    f11re_f11_range_vol_estimators_gkpkcross_63v126d_jerk_v129_signal,
    f11re_f11_range_vol_estimators_gkpkcross_126v252d_jerk_v130_signal,
    f11re_f11_range_vol_estimators_rsgkcross_21v63d_jerk_v131_signal,
    f11re_f11_range_vol_estimators_rsgkcross_63v126d_jerk_v132_signal,
    f11re_f11_range_vol_estimators_rsgkcross_126v252d_jerk_v133_signal,
    f11re_f11_range_vol_estimators_trq10_63d_jerk_v134_signal,
    f11re_f11_range_vol_estimators_trq10_126d_jerk_v135_signal,
    f11re_f11_range_vol_estimators_parkdayskew_126d_jerk_v136_signal,
    f11re_f11_range_vol_estimators_trkurt_126d_jerk_v137_signal,
    f11re_f11_range_vol_estimators_rangeac_63d_jerk_v138_signal,
    f11re_f11_range_vol_estimators_gkrvdivz_63d_jerk_v139_signal,
    f11re_f11_range_vol_estimators_gkrvdivz_126d_jerk_v140_signal,
    f11re_f11_range_vol_estimators_atrpewma_ewm63d_jerk_v141_signal,
    f11re_f11_range_vol_estimators_rsewma_ewm42d_jerk_v142_signal,
    f11re_f11_range_vol_estimators_gappkmix_63d_jerk_v143_signal,
    f11re_f11_range_vol_estimators_overintravol_63d_jerk_v144_signal,
    f11re_f11_range_vol_estimators_overintravol_126d_jerk_v145_signal,
    f11re_f11_range_vol_estimators_rngccratio_126d_jerk_v146_signal,
    f11re_f11_range_vol_estimators_parkcurveshape_multi_jerk_v147_signal,
    f11re_f11_range_vol_estimators_estdisp_63d_jerk_v148_signal,
    f11re_f11_range_vol_estimators_parkdd_21d_jerk_v149_signal,
    f11re_f11_range_vol_estimators_volqual_21d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F11_RANGE_VOL_ESTIMATORS_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.012, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1.2e6, 7e5, n)) + 5e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    ALLOW = {"open", "high", "low", "close", "closeadj", "volume"}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f11_range_vol_estimators_3rd_derivatives_001_150_claude: %d features pass" % n_features)
