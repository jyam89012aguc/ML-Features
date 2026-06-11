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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)

# ===== folder domain primitives =====
def _f076_op_margin_change(em, w):
    return em - em.shift(w)

def _f076_op_inflection(em, w):
    d1 = em - em.shift(w)
    d2 = d1 - d1.shift(w)
    return d2

def _f076_profitability_turn(em, nm, w):
    em_ch = em - em.shift(w)
    nm_ch = nm - nm.shift(w)
    return em_ch + nm_ch


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v001_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v002_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v003_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v004_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v005_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v006_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v007_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v008_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.ewm(span=21, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v009_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.ewm(span=21, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v010_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v011_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v012_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v013_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_z(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v014_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v015_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 21 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v016_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v017_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v018_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v019_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v020_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v021_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v022_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v023_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v024_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v025_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v026_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v027_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_std(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v028_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=63, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v029_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=63, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v030_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v031_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v032_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v033_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_z(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v034_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_std(base, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v035_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 63 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v036_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v037_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v038_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v039_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v040_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_126d_jerk_v041_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_126d_jerk_v042_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_126d_jerk_v043_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_126d_jerk_v044_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_126d_jerk_v045_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 126), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_126d_jerk_v046_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 126), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_126d_jerk_v047_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_std(base, 126), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_126d_jerk_v048_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_126d_jerk_v049_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_margin_change_126d_jerk_v050_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_margin_change(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v051_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v052_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v053_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v054_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v055_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v056_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v057_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v058_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.ewm(span=21, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v059_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.ewm(span=21, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v060_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v061_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v062_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v063_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_z(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v064_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v065_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 21 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v066_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v067_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v068_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v069_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v070_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v071_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v072_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v073_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v074_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v075_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v076_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v077_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_std(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v078_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=63, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v079_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=63, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v080_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v081_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v082_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v083_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_z(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v084_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_std(base, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v085_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 63 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v086_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v087_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v088_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v089_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v090_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_126d_jerk_v091_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_126d_jerk_v092_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_126d_jerk_v093_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_126d_jerk_v094_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_126d_jerk_v095_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 126), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_126d_jerk_v096_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 126), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_126d_jerk_v097_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_std(base, 126), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_126d_jerk_v098_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_126d_jerk_v099_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_op_inflection_126d_jerk_v100_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_op_inflection(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v101_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v102_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v103_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v104_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v105_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v106_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v107_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v108_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.ewm(span=21, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v109_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.ewm(span=21, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v110_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v111_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v112_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v113_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_z(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v114_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v115_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 21 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v116_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v117_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v118_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v119_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v120_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v121_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v122_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v123_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v124_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v125_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v126_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v127_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_std(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v128_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=63, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v129_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=63, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v130_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v131_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v132_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v133_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_z(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v134_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_std(base, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v135_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 63 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v136_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v137_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v138_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v139_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v140_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_126d_jerk_v141_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_126d_jerk_v142_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_126d_jerk_v143_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_126d_jerk_v144_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_126d_jerk_v145_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 126), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_126d_jerk_v146_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 126), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_126d_jerk_v147_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_std(base, 126), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_126d_jerk_v148_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_126d_jerk_v149_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f076omi_f076_operating_margin_inflection_profitability_turn_126d_jerk_v150_signal(ebitdamargin, netmargin, closeadj):
    base = _mean(_f076_profitability_turn(ebitdamargin, netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v001_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v002_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v003_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v004_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v005_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v006_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v007_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v008_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v009_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v010_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v011_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v012_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v013_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v014_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v015_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v016_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v017_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v018_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v019_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_21d_jerk_v020_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v021_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v022_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v023_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v024_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v025_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v026_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v027_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v028_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v029_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v030_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v031_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v032_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v033_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v034_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v035_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v036_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v037_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v038_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v039_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_63d_jerk_v040_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_126d_jerk_v041_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_126d_jerk_v042_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_126d_jerk_v043_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_126d_jerk_v044_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_126d_jerk_v045_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_126d_jerk_v046_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_126d_jerk_v047_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_126d_jerk_v048_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_126d_jerk_v049_signal,
    f076omi_f076_operating_margin_inflection_op_margin_change_126d_jerk_v050_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v051_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v052_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v053_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v054_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v055_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v056_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v057_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v058_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v059_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v060_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v061_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v062_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v063_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v064_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v065_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v066_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v067_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v068_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v069_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_21d_jerk_v070_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v071_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v072_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v073_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v074_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v075_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v076_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v077_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v078_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v079_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v080_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v081_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v082_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v083_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v084_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v085_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v086_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v087_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v088_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v089_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_63d_jerk_v090_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_126d_jerk_v091_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_126d_jerk_v092_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_126d_jerk_v093_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_126d_jerk_v094_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_126d_jerk_v095_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_126d_jerk_v096_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_126d_jerk_v097_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_126d_jerk_v098_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_126d_jerk_v099_signal,
    f076omi_f076_operating_margin_inflection_op_inflection_126d_jerk_v100_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v101_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v102_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v103_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v104_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v105_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v106_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v107_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v108_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v109_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v110_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v111_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v112_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v113_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v114_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v115_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v116_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v117_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v118_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v119_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_21d_jerk_v120_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v121_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v122_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v123_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v124_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v125_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v126_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v127_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v128_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v129_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v130_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v131_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v132_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v133_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v134_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v135_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v136_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v137_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v138_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v139_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_63d_jerk_v140_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_126d_jerk_v141_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_126d_jerk_v142_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_126d_jerk_v143_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_126d_jerk_v144_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_126d_jerk_v145_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_126d_jerk_v146_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_126d_jerk_v147_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_126d_jerk_v148_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_126d_jerk_v149_signal,
    f076omi_f076_operating_margin_inflection_profitability_turn_126d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F076_OPERATING_MARGIN_INFLECTION_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    cols = {"ebitdamargin": ebitdamargin, "netmargin": netmargin, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f076_op_margin_change", "_f076_op_inflection", "_f076_profitability_turn",)
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
    print(f"OK f076_operating_margin_inflection_3rd_derivatives_001_150_claude: {n_features} features pass")
