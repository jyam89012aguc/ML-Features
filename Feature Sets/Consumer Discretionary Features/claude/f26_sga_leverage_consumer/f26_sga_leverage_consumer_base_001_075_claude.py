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
def _f26_sga_to_revenue(sgna, revenue):
    return sgna / revenue.replace(0, np.nan)


def _f26_sga_growth_gap(sgna, revenue, w):
    g_sga = sgna.pct_change(periods=w)
    g_rev = revenue.pct_change(periods=w)
    return g_sga - g_rev


def _f26_sga_leverage(sgna, revenue, w):
    ratio = sgna / revenue.replace(0, np.nan)
    return _mean(ratio, w) - _std(ratio, w)


# ===== features =====

def f26slc_f26_sga_leverage_consumer_sgarev_rawx_21d_base_v001_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarev_mean63d_base_v002_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = _mean(b, 63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarev_std126d_base_v003_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = _std(b, 126) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarev_z252d_base_v004_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = _z(b, 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarev_rank504d_base_v005_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.rolling(504, min_periods=max(5, 504//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarev_abs21d_base_v006_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.abs().rolling(21, min_periods=max(5, 21//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarev_sq63d_base_v007_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = (b * b.abs()).rolling(63, min_periods=max(5, 63//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarev_max126d_base_v008_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.rolling(126, min_periods=max(5, 126//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarev_min252d_base_v009_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.rolling(252, min_periods=max(5, 252//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarev_rng504d_base_v010_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = (b.rolling(504, min_periods=max(5, 504//4)).max() - b.rolling(504, min_periods=max(5, 504//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarev_med21d_base_v011_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.rolling(21, min_periods=max(5, 21//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarev_q7563d_base_v012_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.rolling(63, min_periods=max(5, 63//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarev_q25126d_base_v013_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.rolling(126, min_periods=max(5, 126//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarev_ema252d_base_v014_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.ewm(span=252, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarev_emastd504d_base_v015_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.ewm(span=504, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarev_diff21d_base_v016_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.diff(periods=21) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarev_pct63d_base_v017_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.pct_change(periods=63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarev_log126d_base_v018_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 126) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarev_sign252d_base_v019_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = np.sign(b) * _mean(b.abs(), 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarev_sum504d_base_v020_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.rolling(504, min_periods=max(5, 504//4)).sum() * closeadj / 504
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarev_zsq21d_base_v021_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = _z(b, 21) * _z(b, 21).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarev_centered63d_base_v022_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = (b - _mean(b, 63)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarev_ratio126d_base_v023_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = (b / _mean(b, 126).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarev_skew252d_base_v024_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.rolling(252, min_periods=max(5, 252//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarev_kurt504d_base_v025_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.rolling(504, min_periods=max(5, 504//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_rawx_21d_base_v026_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 21)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_mean63d_base_v027_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 63)
    out = _mean(b, 63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_std126d_base_v028_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 126)
    out = _std(b, 126) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_z252d_base_v029_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 252)
    out = _z(b, 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_rank504d_base_v030_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_abs21d_base_v031_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 21)
    out = b.abs().rolling(21, min_periods=max(5, 21//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_sq63d_base_v032_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 63)
    out = (b * b.abs()).rolling(63, min_periods=max(5, 63//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_max126d_base_v033_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_min252d_base_v034_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_rng504d_base_v035_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 504)
    out = (b.rolling(504, min_periods=max(5, 504//4)).max() - b.rolling(504, min_periods=max(5, 504//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_med21d_base_v036_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 21)
    out = b.rolling(21, min_periods=max(5, 21//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_q7563d_base_v037_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 63)
    out = b.rolling(63, min_periods=max(5, 63//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_q25126d_base_v038_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_ema252d_base_v039_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 252)
    out = b.ewm(span=252, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_emastd504d_base_v040_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 504)
    out = b.ewm(span=504, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_diff21d_base_v041_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 21)
    out = b.diff(periods=21) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_pct63d_base_v042_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 63)
    out = b.pct_change(periods=63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_log126d_base_v043_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 126)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 126) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_sign252d_base_v044_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 252)
    out = np.sign(b) * _mean(b.abs(), 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_sum504d_base_v045_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).sum() * closeadj / 504
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_zsq21d_base_v046_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 21)
    out = _z(b, 21) * _z(b, 21).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_centered63d_base_v047_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 63)
    out = (b - _mean(b, 63)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_ratio126d_base_v048_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 126)
    out = (b / _mean(b, 126).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_skew252d_base_v049_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gap_kurt504d_base_v050_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_rawx_21d_base_v051_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 21)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_mean63d_base_v052_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 63)
    out = _mean(b, 63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_std126d_base_v053_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 126)
    out = _std(b, 126) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_z252d_base_v054_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 252)
    out = _z(b, 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_rank504d_base_v055_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_abs21d_base_v056_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 21)
    out = b.abs().rolling(21, min_periods=max(5, 21//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_sq63d_base_v057_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 63)
    out = (b * b.abs()).rolling(63, min_periods=max(5, 63//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_max126d_base_v058_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_min252d_base_v059_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_rng504d_base_v060_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 504)
    out = (b.rolling(504, min_periods=max(5, 504//4)).max() - b.rolling(504, min_periods=max(5, 504//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_med21d_base_v061_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 21)
    out = b.rolling(21, min_periods=max(5, 21//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_q7563d_base_v062_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 63)
    out = b.rolling(63, min_periods=max(5, 63//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_q25126d_base_v063_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_ema252d_base_v064_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 252)
    out = b.ewm(span=252, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_emastd504d_base_v065_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 504)
    out = b.ewm(span=504, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_diff21d_base_v066_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 21)
    out = b.diff(periods=21) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_pct63d_base_v067_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 63)
    out = b.pct_change(periods=63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_log126d_base_v068_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 126)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 126) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_sign252d_base_v069_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 252)
    out = np.sign(b) * _mean(b.abs(), 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_sum504d_base_v070_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).sum() * closeadj / 504
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_zsq21d_base_v071_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 21)
    out = _z(b, 21) * _z(b, 21).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_centered63d_base_v072_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 63)
    out = (b - _mean(b, 63)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_ratio126d_base_v073_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 126)
    out = (b / _mean(b, 126).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_skew252d_base_v074_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_lev_kurt504d_base_v075_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f26slc_f26_sga_leverage_consumer_sgarev_rawx_21d_base_v001_signal,
    f26slc_f26_sga_leverage_consumer_sgarev_mean63d_base_v002_signal,
    f26slc_f26_sga_leverage_consumer_sgarev_std126d_base_v003_signal,
    f26slc_f26_sga_leverage_consumer_sgarev_z252d_base_v004_signal,
    f26slc_f26_sga_leverage_consumer_sgarev_rank504d_base_v005_signal,
    f26slc_f26_sga_leverage_consumer_sgarev_abs21d_base_v006_signal,
    f26slc_f26_sga_leverage_consumer_sgarev_sq63d_base_v007_signal,
    f26slc_f26_sga_leverage_consumer_sgarev_max126d_base_v008_signal,
    f26slc_f26_sga_leverage_consumer_sgarev_min252d_base_v009_signal,
    f26slc_f26_sga_leverage_consumer_sgarev_rng504d_base_v010_signal,
    f26slc_f26_sga_leverage_consumer_sgarev_med21d_base_v011_signal,
    f26slc_f26_sga_leverage_consumer_sgarev_q7563d_base_v012_signal,
    f26slc_f26_sga_leverage_consumer_sgarev_q25126d_base_v013_signal,
    f26slc_f26_sga_leverage_consumer_sgarev_ema252d_base_v014_signal,
    f26slc_f26_sga_leverage_consumer_sgarev_emastd504d_base_v015_signal,
    f26slc_f26_sga_leverage_consumer_sgarev_diff21d_base_v016_signal,
    f26slc_f26_sga_leverage_consumer_sgarev_pct63d_base_v017_signal,
    f26slc_f26_sga_leverage_consumer_sgarev_log126d_base_v018_signal,
    f26slc_f26_sga_leverage_consumer_sgarev_sign252d_base_v019_signal,
    f26slc_f26_sga_leverage_consumer_sgarev_sum504d_base_v020_signal,
    f26slc_f26_sga_leverage_consumer_sgarev_zsq21d_base_v021_signal,
    f26slc_f26_sga_leverage_consumer_sgarev_centered63d_base_v022_signal,
    f26slc_f26_sga_leverage_consumer_sgarev_ratio126d_base_v023_signal,
    f26slc_f26_sga_leverage_consumer_sgarev_skew252d_base_v024_signal,
    f26slc_f26_sga_leverage_consumer_sgarev_kurt504d_base_v025_signal,
    f26slc_f26_sga_leverage_consumer_gap_rawx_21d_base_v026_signal,
    f26slc_f26_sga_leverage_consumer_gap_mean63d_base_v027_signal,
    f26slc_f26_sga_leverage_consumer_gap_std126d_base_v028_signal,
    f26slc_f26_sga_leverage_consumer_gap_z252d_base_v029_signal,
    f26slc_f26_sga_leverage_consumer_gap_rank504d_base_v030_signal,
    f26slc_f26_sga_leverage_consumer_gap_abs21d_base_v031_signal,
    f26slc_f26_sga_leverage_consumer_gap_sq63d_base_v032_signal,
    f26slc_f26_sga_leverage_consumer_gap_max126d_base_v033_signal,
    f26slc_f26_sga_leverage_consumer_gap_min252d_base_v034_signal,
    f26slc_f26_sga_leverage_consumer_gap_rng504d_base_v035_signal,
    f26slc_f26_sga_leverage_consumer_gap_med21d_base_v036_signal,
    f26slc_f26_sga_leverage_consumer_gap_q7563d_base_v037_signal,
    f26slc_f26_sga_leverage_consumer_gap_q25126d_base_v038_signal,
    f26slc_f26_sga_leverage_consumer_gap_ema252d_base_v039_signal,
    f26slc_f26_sga_leverage_consumer_gap_emastd504d_base_v040_signal,
    f26slc_f26_sga_leverage_consumer_gap_diff21d_base_v041_signal,
    f26slc_f26_sga_leverage_consumer_gap_pct63d_base_v042_signal,
    f26slc_f26_sga_leverage_consumer_gap_log126d_base_v043_signal,
    f26slc_f26_sga_leverage_consumer_gap_sign252d_base_v044_signal,
    f26slc_f26_sga_leverage_consumer_gap_sum504d_base_v045_signal,
    f26slc_f26_sga_leverage_consumer_gap_zsq21d_base_v046_signal,
    f26slc_f26_sga_leverage_consumer_gap_centered63d_base_v047_signal,
    f26slc_f26_sga_leverage_consumer_gap_ratio126d_base_v048_signal,
    f26slc_f26_sga_leverage_consumer_gap_skew252d_base_v049_signal,
    f26slc_f26_sga_leverage_consumer_gap_kurt504d_base_v050_signal,
    f26slc_f26_sga_leverage_consumer_lev_rawx_21d_base_v051_signal,
    f26slc_f26_sga_leverage_consumer_lev_mean63d_base_v052_signal,
    f26slc_f26_sga_leverage_consumer_lev_std126d_base_v053_signal,
    f26slc_f26_sga_leverage_consumer_lev_z252d_base_v054_signal,
    f26slc_f26_sga_leverage_consumer_lev_rank504d_base_v055_signal,
    f26slc_f26_sga_leverage_consumer_lev_abs21d_base_v056_signal,
    f26slc_f26_sga_leverage_consumer_lev_sq63d_base_v057_signal,
    f26slc_f26_sga_leverage_consumer_lev_max126d_base_v058_signal,
    f26slc_f26_sga_leverage_consumer_lev_min252d_base_v059_signal,
    f26slc_f26_sga_leverage_consumer_lev_rng504d_base_v060_signal,
    f26slc_f26_sga_leverage_consumer_lev_med21d_base_v061_signal,
    f26slc_f26_sga_leverage_consumer_lev_q7563d_base_v062_signal,
    f26slc_f26_sga_leverage_consumer_lev_q25126d_base_v063_signal,
    f26slc_f26_sga_leverage_consumer_lev_ema252d_base_v064_signal,
    f26slc_f26_sga_leverage_consumer_lev_emastd504d_base_v065_signal,
    f26slc_f26_sga_leverage_consumer_lev_diff21d_base_v066_signal,
    f26slc_f26_sga_leverage_consumer_lev_pct63d_base_v067_signal,
    f26slc_f26_sga_leverage_consumer_lev_log126d_base_v068_signal,
    f26slc_f26_sga_leverage_consumer_lev_sign252d_base_v069_signal,
    f26slc_f26_sga_leverage_consumer_lev_sum504d_base_v070_signal,
    f26slc_f26_sga_leverage_consumer_lev_zsq21d_base_v071_signal,
    f26slc_f26_sga_leverage_consumer_lev_centered63d_base_v072_signal,
    f26slc_f26_sga_leverage_consumer_lev_ratio126d_base_v073_signal,
    f26slc_f26_sga_leverage_consumer_lev_skew252d_base_v074_signal,
    f26slc_f26_sga_leverage_consumer_lev_kurt504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values() if p.default is inspect.Parameter.empty]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_SGA_LEVERAGE_CONSUMER_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    cols = {"closeadj": closeadj, "sgna": sgna, "revenue": revenue, "opex": opex}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f26_sga_to_revenue", "_f26_sga_growth_gap", "_f26_sga_leverage",)
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
    print(f"OK f26_sga_leverage_consumer_base_001_075_claude: {n_features} features pass")
