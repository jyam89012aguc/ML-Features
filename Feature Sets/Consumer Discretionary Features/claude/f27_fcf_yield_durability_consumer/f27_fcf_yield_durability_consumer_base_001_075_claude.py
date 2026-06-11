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
def _f27_fcf_yield(fcf, ev):
    return fcf / ev.replace(0, np.nan)


def _f27_fcf_yield_stability(fcf, ev, w):
    y = fcf / ev.replace(0, np.nan)
    return _mean(y, w) / _std(y, w).replace(0, np.nan)


def _f27_fcf_compound_quality(fcf, marketcap, w):
    yld = fcf / marketcap.replace(0, np.nan)
    return _mean(yld, w) - _std(yld, w)


# ===== features =====

def f27fyd_f27_fcf_yield_durability_consumer_yld_rawx_21d_base_v001_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_mean63d_base_v002_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = _mean(b, 63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_std126d_base_v003_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = _std(b, 126) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_z252d_base_v004_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = _z(b, 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_rank504d_base_v005_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.rolling(504, min_periods=max(5, 504//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_abs21d_base_v006_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.abs().rolling(21, min_periods=max(5, 21//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_sq63d_base_v007_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = (b * b.abs()).rolling(63, min_periods=max(5, 63//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_max126d_base_v008_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.rolling(126, min_periods=max(5, 126//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_min252d_base_v009_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.rolling(252, min_periods=max(5, 252//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_rng504d_base_v010_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = (b.rolling(504, min_periods=max(5, 504//4)).max() - b.rolling(504, min_periods=max(5, 504//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_med21d_base_v011_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.rolling(21, min_periods=max(5, 21//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_q7563d_base_v012_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.rolling(63, min_periods=max(5, 63//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_q25126d_base_v013_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.rolling(126, min_periods=max(5, 126//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_ema252d_base_v014_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.ewm(span=252, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_emastd504d_base_v015_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.ewm(span=504, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_diff21d_base_v016_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.diff(periods=21) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_pct63d_base_v017_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.pct_change(periods=63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_log126d_base_v018_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 126) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_sign252d_base_v019_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = np.sign(b) * _mean(b.abs(), 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_sum504d_base_v020_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.rolling(504, min_periods=max(5, 504//4)).sum() * closeadj / 504
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_zsq21d_base_v021_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = _z(b, 21) * _z(b, 21).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_centered63d_base_v022_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = (b - _mean(b, 63)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_ratio126d_base_v023_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = (b / _mean(b, 126).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_skew252d_base_v024_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.rolling(252, min_periods=max(5, 252//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_kurt504d_base_v025_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.rolling(504, min_periods=max(5, 504//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_rawx_21d_base_v026_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 21)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_mean63d_base_v027_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 63)
    out = _mean(b, 63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_std126d_base_v028_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 126)
    out = _std(b, 126) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_z252d_base_v029_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 252)
    out = _z(b, 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_rank504d_base_v030_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_abs21d_base_v031_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 21)
    out = b.abs().rolling(21, min_periods=max(5, 21//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_sq63d_base_v032_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 63)
    out = (b * b.abs()).rolling(63, min_periods=max(5, 63//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_max126d_base_v033_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_min252d_base_v034_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_rng504d_base_v035_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 504)
    out = (b.rolling(504, min_periods=max(5, 504//4)).max() - b.rolling(504, min_periods=max(5, 504//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_med21d_base_v036_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 21)
    out = b.rolling(21, min_periods=max(5, 21//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_q7563d_base_v037_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 63)
    out = b.rolling(63, min_periods=max(5, 63//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_q25126d_base_v038_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_ema252d_base_v039_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 252)
    out = b.ewm(span=252, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_emastd504d_base_v040_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 504)
    out = b.ewm(span=504, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_diff21d_base_v041_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 21)
    out = b.diff(periods=21) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_pct63d_base_v042_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 63)
    out = b.pct_change(periods=63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_log126d_base_v043_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 126)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 126) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_sign252d_base_v044_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 252)
    out = np.sign(b) * _mean(b.abs(), 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_sum504d_base_v045_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).sum() * closeadj / 504
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_zsq21d_base_v046_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 21)
    out = _z(b, 21) * _z(b, 21).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_centered63d_base_v047_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 63)
    out = (b - _mean(b, 63)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_ratio126d_base_v048_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 126)
    out = (b / _mean(b, 126).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_skew252d_base_v049_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_kurt504d_base_v050_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_rawx_21d_base_v051_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 21)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_mean63d_base_v052_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 63)
    out = _mean(b, 63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_std126d_base_v053_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 126)
    out = _std(b, 126) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_z252d_base_v054_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 252)
    out = _z(b, 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_rank504d_base_v055_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_abs21d_base_v056_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 21)
    out = b.abs().rolling(21, min_periods=max(5, 21//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_sq63d_base_v057_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 63)
    out = (b * b.abs()).rolling(63, min_periods=max(5, 63//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_max126d_base_v058_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_min252d_base_v059_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_rng504d_base_v060_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 504)
    out = (b.rolling(504, min_periods=max(5, 504//4)).max() - b.rolling(504, min_periods=max(5, 504//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_med21d_base_v061_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 21)
    out = b.rolling(21, min_periods=max(5, 21//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_q7563d_base_v062_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 63)
    out = b.rolling(63, min_periods=max(5, 63//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_q25126d_base_v063_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_ema252d_base_v064_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 252)
    out = b.ewm(span=252, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_emastd504d_base_v065_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 504)
    out = b.ewm(span=504, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_diff21d_base_v066_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 21)
    out = b.diff(periods=21) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_pct63d_base_v067_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 63)
    out = b.pct_change(periods=63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_log126d_base_v068_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 126)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 126) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_sign252d_base_v069_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 252)
    out = np.sign(b) * _mean(b.abs(), 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_sum504d_base_v070_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).sum() * closeadj / 504
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_zsq21d_base_v071_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 21)
    out = _z(b, 21) * _z(b, 21).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_centered63d_base_v072_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 63)
    out = (b - _mean(b, 63)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_ratio126d_base_v073_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 126)
    out = (b / _mean(b, 126).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_skew252d_base_v074_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_kurt504d_base_v075_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f27fyd_f27_fcf_yield_durability_consumer_yld_rawx_21d_base_v001_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_mean63d_base_v002_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_std126d_base_v003_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_z252d_base_v004_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_rank504d_base_v005_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_abs21d_base_v006_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_sq63d_base_v007_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_max126d_base_v008_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_min252d_base_v009_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_rng504d_base_v010_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_med21d_base_v011_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_q7563d_base_v012_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_q25126d_base_v013_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_ema252d_base_v014_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_emastd504d_base_v015_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_diff21d_base_v016_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_pct63d_base_v017_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_log126d_base_v018_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_sign252d_base_v019_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_sum504d_base_v020_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_zsq21d_base_v021_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_centered63d_base_v022_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_ratio126d_base_v023_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_skew252d_base_v024_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_kurt504d_base_v025_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_rawx_21d_base_v026_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_mean63d_base_v027_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_std126d_base_v028_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_z252d_base_v029_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_rank504d_base_v030_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_abs21d_base_v031_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_sq63d_base_v032_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_max126d_base_v033_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_min252d_base_v034_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_rng504d_base_v035_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_med21d_base_v036_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_q7563d_base_v037_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_q25126d_base_v038_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_ema252d_base_v039_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_emastd504d_base_v040_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_diff21d_base_v041_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_pct63d_base_v042_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_log126d_base_v043_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_sign252d_base_v044_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_sum504d_base_v045_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_zsq21d_base_v046_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_centered63d_base_v047_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_ratio126d_base_v048_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_skew252d_base_v049_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_kurt504d_base_v050_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_rawx_21d_base_v051_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_mean63d_base_v052_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_std126d_base_v053_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_z252d_base_v054_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_rank504d_base_v055_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_abs21d_base_v056_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_sq63d_base_v057_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_max126d_base_v058_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_min252d_base_v059_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_rng504d_base_v060_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_med21d_base_v061_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_q7563d_base_v062_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_q25126d_base_v063_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_ema252d_base_v064_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_emastd504d_base_v065_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_diff21d_base_v066_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_pct63d_base_v067_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_log126d_base_v068_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_sign252d_base_v069_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_sum504d_base_v070_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_zsq21d_base_v071_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_centered63d_base_v072_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_ratio126d_base_v073_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_skew252d_base_v074_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_kurt504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values() if p.default is inspect.Parameter.empty]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_FCF_YIELD_DURABILITY_CONSUMER_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    fcf       = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    debt      = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    cashneq   = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    marketcap = pd.Series(closeadj * 1e8, name="marketcap")
    ev        = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    cols = {"closeadj": closeadj, "fcf": fcf, "ev": ev, "marketcap": marketcap}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f27_fcf_yield", "_f27_fcf_yield_stability", "_f27_fcf_compound_quality",)
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
    print(f"OK f27_fcf_yield_durability_consumer_base_001_075_claude: {n_features} features pass")
