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
def _f30_quality_composite(roic, fcf, revenue, w):
    fcfm = fcf / revenue.replace(0, np.nan)
    return _mean(roic, w) + _mean(fcfm, w) + _mean(revenue.pct_change(periods=w), w)


def _f30_terminal_score(roic, ebitdamargin, w):
    return _mean(roic, w) * _mean(ebitdamargin, w)


def _f30_terminal_quality(fcf, revenue, roic, w):
    fcfm = fcf / revenue.replace(0, np.nan)
    return _mean(fcfm, w) * _mean(roic, w)


# ===== features =====

def f30ctc_f30_consumer_terminal_compounder_qcomp_rawx_21d_base_v001_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 21)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_mean63d_base_v002_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 63)
    out = _mean(b, 63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_std126d_base_v003_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 126)
    out = _std(b, 126) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_z252d_base_v004_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 252)
    out = _z(b, 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_rank504d_base_v005_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_abs21d_base_v006_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 21)
    out = b.abs().rolling(21, min_periods=max(5, 21//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_sq63d_base_v007_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 63)
    out = (b * b.abs()).rolling(63, min_periods=max(5, 63//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_max126d_base_v008_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_min252d_base_v009_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_rng504d_base_v010_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 504)
    out = (b.rolling(504, min_periods=max(5, 504//4)).max() - b.rolling(504, min_periods=max(5, 504//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_med21d_base_v011_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 21)
    out = b.rolling(21, min_periods=max(5, 21//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_q7563d_base_v012_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 63)
    out = b.rolling(63, min_periods=max(5, 63//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_q25126d_base_v013_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_ema252d_base_v014_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 252)
    out = b.ewm(span=252, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_emastd504d_base_v015_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 504)
    out = b.ewm(span=504, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_diff21d_base_v016_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 21)
    out = b.diff(periods=21) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_pct63d_base_v017_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 63)
    out = b.pct_change(periods=63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_log126d_base_v018_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 126)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 126) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_sign252d_base_v019_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 252)
    out = np.sign(b) * _mean(b.abs(), 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_sum504d_base_v020_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).sum() * closeadj / 504
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_zsq21d_base_v021_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 21)
    out = _z(b, 21) * _z(b, 21).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_centered63d_base_v022_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 63)
    out = (b - _mean(b, 63)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_ratio126d_base_v023_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 126)
    out = (b / _mean(b, 126).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_skew252d_base_v024_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_kurt504d_base_v025_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_rawx_21d_base_v026_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 21)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_mean63d_base_v027_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 63)
    out = _mean(b, 63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_std126d_base_v028_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 126)
    out = _std(b, 126) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_z252d_base_v029_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 252)
    out = _z(b, 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_rank504d_base_v030_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_abs21d_base_v031_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 21)
    out = b.abs().rolling(21, min_periods=max(5, 21//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_sq63d_base_v032_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 63)
    out = (b * b.abs()).rolling(63, min_periods=max(5, 63//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_max126d_base_v033_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_min252d_base_v034_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_rng504d_base_v035_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 504)
    out = (b.rolling(504, min_periods=max(5, 504//4)).max() - b.rolling(504, min_periods=max(5, 504//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_med21d_base_v036_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 21)
    out = b.rolling(21, min_periods=max(5, 21//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_q7563d_base_v037_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 63)
    out = b.rolling(63, min_periods=max(5, 63//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_q25126d_base_v038_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_ema252d_base_v039_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 252)
    out = b.ewm(span=252, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_emastd504d_base_v040_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 504)
    out = b.ewm(span=504, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_diff21d_base_v041_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 21)
    out = b.diff(periods=21) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_pct63d_base_v042_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 63)
    out = b.pct_change(periods=63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_log126d_base_v043_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 126)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 126) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_sign252d_base_v044_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 252)
    out = np.sign(b) * _mean(b.abs(), 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_sum504d_base_v045_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).sum() * closeadj / 504
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_zsq21d_base_v046_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 21)
    out = _z(b, 21) * _z(b, 21).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_centered63d_base_v047_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 63)
    out = (b - _mean(b, 63)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_ratio126d_base_v048_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 126)
    out = (b / _mean(b, 126).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_skew252d_base_v049_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_kurt504d_base_v050_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_rawx_21d_base_v051_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 21)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_mean63d_base_v052_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 63)
    out = _mean(b, 63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_std126d_base_v053_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 126)
    out = _std(b, 126) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_z252d_base_v054_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 252)
    out = _z(b, 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_rank504d_base_v055_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_abs21d_base_v056_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 21)
    out = b.abs().rolling(21, min_periods=max(5, 21//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_sq63d_base_v057_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 63)
    out = (b * b.abs()).rolling(63, min_periods=max(5, 63//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_max126d_base_v058_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_min252d_base_v059_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_rng504d_base_v060_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 504)
    out = (b.rolling(504, min_periods=max(5, 504//4)).max() - b.rolling(504, min_periods=max(5, 504//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_med21d_base_v061_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 21)
    out = b.rolling(21, min_periods=max(5, 21//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_q7563d_base_v062_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 63)
    out = b.rolling(63, min_periods=max(5, 63//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_q25126d_base_v063_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 126)
    out = b.rolling(126, min_periods=max(5, 126//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_ema252d_base_v064_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 252)
    out = b.ewm(span=252, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_emastd504d_base_v065_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 504)
    out = b.ewm(span=504, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_diff21d_base_v066_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 21)
    out = b.diff(periods=21) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_pct63d_base_v067_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 63)
    out = b.pct_change(periods=63) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_log126d_base_v068_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 126)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 126) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_sign252d_base_v069_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 252)
    out = np.sign(b) * _mean(b.abs(), 252) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_sum504d_base_v070_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).sum() * closeadj / 504
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_zsq21d_base_v071_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 21)
    out = _z(b, 21) * _z(b, 21).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_centered63d_base_v072_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 63)
    out = (b - _mean(b, 63)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_ratio126d_base_v073_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 126)
    out = (b / _mean(b, 126).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_skew252d_base_v074_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_kurt504d_base_v075_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 504)
    out = b.rolling(504, min_periods=max(5, 504//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f30ctc_f30_consumer_terminal_compounder_qcomp_rawx_21d_base_v001_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_mean63d_base_v002_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_std126d_base_v003_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_z252d_base_v004_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_rank504d_base_v005_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_abs21d_base_v006_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_sq63d_base_v007_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_max126d_base_v008_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_min252d_base_v009_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_rng504d_base_v010_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_med21d_base_v011_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_q7563d_base_v012_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_q25126d_base_v013_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_ema252d_base_v014_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_emastd504d_base_v015_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_diff21d_base_v016_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_pct63d_base_v017_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_log126d_base_v018_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_sign252d_base_v019_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_sum504d_base_v020_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_zsq21d_base_v021_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_centered63d_base_v022_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_ratio126d_base_v023_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_skew252d_base_v024_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_kurt504d_base_v025_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_rawx_21d_base_v026_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_mean63d_base_v027_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_std126d_base_v028_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_z252d_base_v029_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_rank504d_base_v030_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_abs21d_base_v031_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_sq63d_base_v032_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_max126d_base_v033_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_min252d_base_v034_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_rng504d_base_v035_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_med21d_base_v036_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_q7563d_base_v037_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_q25126d_base_v038_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_ema252d_base_v039_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_emastd504d_base_v040_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_diff21d_base_v041_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_pct63d_base_v042_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_log126d_base_v043_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_sign252d_base_v044_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_sum504d_base_v045_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_zsq21d_base_v046_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_centered63d_base_v047_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_ratio126d_base_v048_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_skew252d_base_v049_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_kurt504d_base_v050_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_rawx_21d_base_v051_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_mean63d_base_v052_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_std126d_base_v053_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_z252d_base_v054_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_rank504d_base_v055_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_abs21d_base_v056_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_sq63d_base_v057_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_max126d_base_v058_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_min252d_base_v059_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_rng504d_base_v060_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_med21d_base_v061_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_q7563d_base_v062_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_q25126d_base_v063_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_ema252d_base_v064_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_emastd504d_base_v065_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_diff21d_base_v066_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_pct63d_base_v067_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_log126d_base_v068_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_sign252d_base_v069_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_sum504d_base_v070_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_zsq21d_base_v071_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_centered63d_base_v072_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_ratio126d_base_v073_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_skew252d_base_v074_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_kurt504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values() if p.default is inspect.Parameter.empty]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_CONSUMER_TERMINAL_COMPOUNDER_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue      = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    fcf          = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ebitda       = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    cols = {"closeadj": closeadj, "revenue": revenue, "fcf": fcf, "ebitda": ebitda, "roic": roic, "ebitdamargin": ebitdamargin}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f30_quality_composite", "_f30_terminal_score", "_f30_terminal_quality",)
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
    print(f"OK f30_consumer_terminal_compounder_base_001_075_claude: {n_features} features pass")
