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
def _f30_quality_composite(roic, fcf, revenue, w):
    fcfm = fcf / revenue.replace(0, np.nan)
    return _mean(roic, w) + _mean(fcfm, w) + _mean(revenue.pct_change(periods=w), w)


def _f30_terminal_score(roic, ebitdamargin, w):
    return _mean(roic, w) * _mean(ebitdamargin, w)


def _f30_terminal_quality(fcf, revenue, roic, w):
    fcfm = fcf / revenue.replace(0, np.nan)
    return _mean(fcfm, w) * _mean(roic, w)


# ===== features =====

def f30ctc_f30_consumer_terminal_compounder_qcomp_5d_jerk_v001_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 5)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_5d_jerk_v002_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 5)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_5d_jerk_v003_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 5)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_5d_jerk_v004_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 5)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_5d_jerk_v005_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 5)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_10d_jerk_v006_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 10)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_10d_jerk_v007_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 10)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_10d_jerk_v008_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 10)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_10d_jerk_v009_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 10)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_10d_jerk_v010_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 10)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_21d_jerk_v011_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 21)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_21d_jerk_v012_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 21)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_21d_jerk_v013_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 21)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_21d_jerk_v014_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 21)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_21d_jerk_v015_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 21)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_42d_jerk_v016_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 42)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_42d_jerk_v017_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 42)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_42d_jerk_v018_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 42)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_42d_jerk_v019_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 42)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_42d_jerk_v020_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 42)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_63d_jerk_v021_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 63)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_63d_jerk_v022_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 63)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_63d_jerk_v023_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 63)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_63d_jerk_v024_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 63)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_63d_jerk_v025_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 63)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_126d_jerk_v026_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 126)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_126d_jerk_v027_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 126)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_126d_jerk_v028_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 126)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_126d_jerk_v029_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 126)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_126d_jerk_v030_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 126)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_189d_jerk_v031_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 189)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_189d_jerk_v032_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 189)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_189d_jerk_v033_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 189)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_189d_jerk_v034_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 189)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_189d_jerk_v035_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 189)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_252d_jerk_v036_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 252)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_252d_jerk_v037_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 252)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_252d_jerk_v038_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 252)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_252d_jerk_v039_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 252)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_252d_jerk_v040_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 252)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_378d_jerk_v041_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 378)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_378d_jerk_v042_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 378)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_378d_jerk_v043_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 378)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_378d_jerk_v044_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 378)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_378d_jerk_v045_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 378)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_504d_jerk_v046_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 504)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_504d_jerk_v047_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 504)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_504d_jerk_v048_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 504)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_504d_jerk_v049_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 504)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcomp_504d_jerk_v050_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 504)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_5d_jerk_v051_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 5)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_5d_jerk_v052_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 5)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_5d_jerk_v053_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 5)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_5d_jerk_v054_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 5)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_5d_jerk_v055_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 5)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_10d_jerk_v056_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 10)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_10d_jerk_v057_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 10)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_10d_jerk_v058_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 10)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_10d_jerk_v059_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 10)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_10d_jerk_v060_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 10)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_21d_jerk_v061_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 21)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_21d_jerk_v062_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 21)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_21d_jerk_v063_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 21)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_21d_jerk_v064_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 21)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_21d_jerk_v065_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 21)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_42d_jerk_v066_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 42)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_42d_jerk_v067_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 42)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_42d_jerk_v068_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 42)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_42d_jerk_v069_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 42)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_42d_jerk_v070_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 42)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_63d_jerk_v071_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 63)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_63d_jerk_v072_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 63)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_63d_jerk_v073_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 63)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_63d_jerk_v074_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 63)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_63d_jerk_v075_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 63)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_126d_jerk_v076_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 126)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_126d_jerk_v077_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 126)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_126d_jerk_v078_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 126)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_126d_jerk_v079_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 126)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_126d_jerk_v080_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 126)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_189d_jerk_v081_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 189)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_189d_jerk_v082_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 189)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_189d_jerk_v083_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 189)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_189d_jerk_v084_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 189)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_189d_jerk_v085_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 189)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_252d_jerk_v086_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 252)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_252d_jerk_v087_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 252)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_252d_jerk_v088_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 252)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_252d_jerk_v089_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 252)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_252d_jerk_v090_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 252)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_378d_jerk_v091_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 378)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_378d_jerk_v092_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 378)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_378d_jerk_v093_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 378)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_378d_jerk_v094_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 378)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_378d_jerk_v095_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 378)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_504d_jerk_v096_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 504)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_504d_jerk_v097_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 504)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_504d_jerk_v098_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 504)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_504d_jerk_v099_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 504)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscr_504d_jerk_v100_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 504)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_5d_jerk_v101_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 5)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_5d_jerk_v102_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 5)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_5d_jerk_v103_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 5)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_5d_jerk_v104_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 5)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_5d_jerk_v105_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 5)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_10d_jerk_v106_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 10)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_10d_jerk_v107_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 10)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_10d_jerk_v108_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 10)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_10d_jerk_v109_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 10)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_10d_jerk_v110_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 10)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_21d_jerk_v111_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 21)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_21d_jerk_v112_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 21)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_21d_jerk_v113_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 21)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_21d_jerk_v114_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 21)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_21d_jerk_v115_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 21)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_42d_jerk_v116_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 42)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_42d_jerk_v117_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 42)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_42d_jerk_v118_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 42)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_42d_jerk_v119_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 42)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_42d_jerk_v120_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 42)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_63d_jerk_v121_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 63)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_63d_jerk_v122_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 63)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_63d_jerk_v123_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 63)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_63d_jerk_v124_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 63)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_63d_jerk_v125_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 63)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_126d_jerk_v126_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 126)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_126d_jerk_v127_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 126)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_126d_jerk_v128_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 126)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_126d_jerk_v129_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 126)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_126d_jerk_v130_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 126)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_189d_jerk_v131_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 189)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_189d_jerk_v132_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 189)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_189d_jerk_v133_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 189)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_189d_jerk_v134_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 189)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_189d_jerk_v135_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 189)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_252d_jerk_v136_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 252)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_252d_jerk_v137_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 252)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_252d_jerk_v138_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 252)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_252d_jerk_v139_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 252)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_252d_jerk_v140_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 252)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_378d_jerk_v141_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 378)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_378d_jerk_v142_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 378)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_378d_jerk_v143_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 378)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_378d_jerk_v144_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 378)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_378d_jerk_v145_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 378)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_504d_jerk_v146_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 504)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_504d_jerk_v147_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 504)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_504d_jerk_v148_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 504)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_504d_jerk_v149_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 504)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqual_504d_jerk_v150_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 504)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f30ctc_f30_consumer_terminal_compounder_qcomp_5d_jerk_v001_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_5d_jerk_v002_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_5d_jerk_v003_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_5d_jerk_v004_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_5d_jerk_v005_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_10d_jerk_v006_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_10d_jerk_v007_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_10d_jerk_v008_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_10d_jerk_v009_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_10d_jerk_v010_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_21d_jerk_v011_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_21d_jerk_v012_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_21d_jerk_v013_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_21d_jerk_v014_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_21d_jerk_v015_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_42d_jerk_v016_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_42d_jerk_v017_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_42d_jerk_v018_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_42d_jerk_v019_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_42d_jerk_v020_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_63d_jerk_v021_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_63d_jerk_v022_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_63d_jerk_v023_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_63d_jerk_v024_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_63d_jerk_v025_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_126d_jerk_v026_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_126d_jerk_v027_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_126d_jerk_v028_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_126d_jerk_v029_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_126d_jerk_v030_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_189d_jerk_v031_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_189d_jerk_v032_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_189d_jerk_v033_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_189d_jerk_v034_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_189d_jerk_v035_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_252d_jerk_v036_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_252d_jerk_v037_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_252d_jerk_v038_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_252d_jerk_v039_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_252d_jerk_v040_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_378d_jerk_v041_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_378d_jerk_v042_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_378d_jerk_v043_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_378d_jerk_v044_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_378d_jerk_v045_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_504d_jerk_v046_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_504d_jerk_v047_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_504d_jerk_v048_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_504d_jerk_v049_signal,
    f30ctc_f30_consumer_terminal_compounder_qcomp_504d_jerk_v050_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_5d_jerk_v051_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_5d_jerk_v052_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_5d_jerk_v053_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_5d_jerk_v054_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_5d_jerk_v055_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_10d_jerk_v056_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_10d_jerk_v057_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_10d_jerk_v058_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_10d_jerk_v059_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_10d_jerk_v060_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_21d_jerk_v061_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_21d_jerk_v062_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_21d_jerk_v063_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_21d_jerk_v064_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_21d_jerk_v065_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_42d_jerk_v066_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_42d_jerk_v067_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_42d_jerk_v068_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_42d_jerk_v069_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_42d_jerk_v070_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_63d_jerk_v071_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_63d_jerk_v072_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_63d_jerk_v073_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_63d_jerk_v074_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_63d_jerk_v075_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_126d_jerk_v076_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_126d_jerk_v077_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_126d_jerk_v078_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_126d_jerk_v079_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_126d_jerk_v080_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_189d_jerk_v081_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_189d_jerk_v082_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_189d_jerk_v083_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_189d_jerk_v084_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_189d_jerk_v085_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_252d_jerk_v086_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_252d_jerk_v087_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_252d_jerk_v088_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_252d_jerk_v089_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_252d_jerk_v090_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_378d_jerk_v091_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_378d_jerk_v092_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_378d_jerk_v093_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_378d_jerk_v094_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_378d_jerk_v095_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_504d_jerk_v096_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_504d_jerk_v097_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_504d_jerk_v098_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_504d_jerk_v099_signal,
    f30ctc_f30_consumer_terminal_compounder_tscr_504d_jerk_v100_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_5d_jerk_v101_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_5d_jerk_v102_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_5d_jerk_v103_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_5d_jerk_v104_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_5d_jerk_v105_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_10d_jerk_v106_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_10d_jerk_v107_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_10d_jerk_v108_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_10d_jerk_v109_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_10d_jerk_v110_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_21d_jerk_v111_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_21d_jerk_v112_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_21d_jerk_v113_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_21d_jerk_v114_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_21d_jerk_v115_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_42d_jerk_v116_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_42d_jerk_v117_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_42d_jerk_v118_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_42d_jerk_v119_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_42d_jerk_v120_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_63d_jerk_v121_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_63d_jerk_v122_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_63d_jerk_v123_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_63d_jerk_v124_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_63d_jerk_v125_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_126d_jerk_v126_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_126d_jerk_v127_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_126d_jerk_v128_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_126d_jerk_v129_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_126d_jerk_v130_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_189d_jerk_v131_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_189d_jerk_v132_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_189d_jerk_v133_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_189d_jerk_v134_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_189d_jerk_v135_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_252d_jerk_v136_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_252d_jerk_v137_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_252d_jerk_v138_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_252d_jerk_v139_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_252d_jerk_v140_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_378d_jerk_v141_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_378d_jerk_v142_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_378d_jerk_v143_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_378d_jerk_v144_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_378d_jerk_v145_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_504d_jerk_v146_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_504d_jerk_v147_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_504d_jerk_v148_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_504d_jerk_v149_signal,
    f30ctc_f30_consumer_terminal_compounder_tqual_504d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values() if p.default is inspect.Parameter.empty]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_CONSUMER_TERMINAL_COMPOUNDER_REGISTRY_JERK_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f30_consumer_terminal_compounder_3rd_derivatives_001_150_claude: {n_features} features pass")
