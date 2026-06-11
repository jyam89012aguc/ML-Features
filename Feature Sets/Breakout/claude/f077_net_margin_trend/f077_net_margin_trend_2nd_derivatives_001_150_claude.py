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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)

# ===== folder domain primitives =====
def _f077_nm_slope(nm, w):
    return (nm - nm.shift(w)) / w

def _f077_nm_smoothed(nm, w):
    return nm.rolling(w, min_periods=max(1, w // 2)).mean()

def _f077_nm_trend_quality(nm, w):
    sm = nm.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = nm.rolling(w, min_periods=max(1, w // 2)).std()
    return (sm - sm.shift(w)) / sd.replace(0, np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v001_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v002_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v003_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v004_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v005_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_mean(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v006_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v007_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_std(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v008_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=21, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v009_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=21, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v010_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v011_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v012_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v013_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_z(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v014_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_std(base, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v015_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=max(2, 21 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v016_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v017_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v018_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v019_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_mean(base.abs(), 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v020_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v021_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v022_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v023_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v024_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v025_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_mean(base, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v026_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v027_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_std(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v028_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=63, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v029_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=63, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v030_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v031_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v032_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v033_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_z(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v034_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_std(base, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v035_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=max(2, 63 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v036_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v037_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v038_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v039_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_mean(base.abs(), 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v040_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_126d_slope_v041_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_126d_slope_v042_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_126d_slope_v043_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_126d_slope_v044_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_126d_slope_v045_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(_mean(base, 126), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_126d_slope_v046_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 126), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_126d_slope_v047_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(_std(base, 126), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_126d_slope_v048_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=126, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_126d_slope_v049_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=126, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_slope_126d_slope_v050_signal(netmargin, closeadj):
    base = _mean(_f077_nm_slope(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v051_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v052_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v053_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v054_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v055_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_mean(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v056_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v057_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_std(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v058_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=21, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v059_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=21, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v060_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v061_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v062_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v063_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_z(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v064_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_std(base, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v065_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=max(2, 21 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v066_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v067_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v068_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v069_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_mean(base.abs(), 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v070_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v071_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v072_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v073_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v074_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v075_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_mean(base, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v076_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v077_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_std(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v078_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=63, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v079_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=63, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v080_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v081_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v082_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v083_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_z(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v084_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_std(base, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v085_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=max(2, 63 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v086_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v087_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v088_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v089_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_mean(base.abs(), 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v090_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_126d_slope_v091_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_126d_slope_v092_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_126d_slope_v093_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_126d_slope_v094_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_126d_slope_v095_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(_mean(base, 126), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_126d_slope_v096_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 126), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_126d_slope_v097_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(_std(base, 126), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_126d_slope_v098_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=126, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_126d_slope_v099_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=126, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_smoothed_126d_slope_v100_signal(netmargin, closeadj):
    base = _mean(_f077_nm_smoothed(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v101_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v102_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v103_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v104_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v105_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_mean(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v106_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v107_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_std(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v108_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=21, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v109_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=21, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v110_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v111_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v112_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v113_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_z(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v114_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_std(base, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v115_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=max(2, 21 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v116_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v117_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v118_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v119_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_mean(base.abs(), 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v120_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v121_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v122_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v123_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v124_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v125_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_mean(base, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v126_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v127_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_std(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v128_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=63, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v129_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=63, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v130_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v131_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v132_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v133_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_z(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v134_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_std(base, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v135_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=max(2, 63 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v136_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v137_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v138_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v139_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_mean(base.abs(), 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v140_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_126d_slope_v141_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_126d_slope_v142_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_126d_slope_v143_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_126d_slope_v144_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_126d_slope_v145_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(_mean(base, 126), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_126d_slope_v146_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 126), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_126d_slope_v147_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(_std(base, 126), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_126d_slope_v148_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=126, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_126d_slope_v149_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=126, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f077nmt_f077_net_margin_trend_nm_trend_quality_126d_slope_v150_signal(netmargin, closeadj):
    base = _mean(_f077_nm_trend_quality(netmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v001_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v002_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v003_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v004_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v005_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v006_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v007_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v008_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v009_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v010_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v011_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v012_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v013_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v014_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v015_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v016_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v017_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v018_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v019_signal,
    f077nmt_f077_net_margin_trend_nm_slope_21d_slope_v020_signal,
    f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v021_signal,
    f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v022_signal,
    f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v023_signal,
    f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v024_signal,
    f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v025_signal,
    f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v026_signal,
    f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v027_signal,
    f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v028_signal,
    f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v029_signal,
    f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v030_signal,
    f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v031_signal,
    f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v032_signal,
    f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v033_signal,
    f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v034_signal,
    f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v035_signal,
    f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v036_signal,
    f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v037_signal,
    f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v038_signal,
    f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v039_signal,
    f077nmt_f077_net_margin_trend_nm_slope_63d_slope_v040_signal,
    f077nmt_f077_net_margin_trend_nm_slope_126d_slope_v041_signal,
    f077nmt_f077_net_margin_trend_nm_slope_126d_slope_v042_signal,
    f077nmt_f077_net_margin_trend_nm_slope_126d_slope_v043_signal,
    f077nmt_f077_net_margin_trend_nm_slope_126d_slope_v044_signal,
    f077nmt_f077_net_margin_trend_nm_slope_126d_slope_v045_signal,
    f077nmt_f077_net_margin_trend_nm_slope_126d_slope_v046_signal,
    f077nmt_f077_net_margin_trend_nm_slope_126d_slope_v047_signal,
    f077nmt_f077_net_margin_trend_nm_slope_126d_slope_v048_signal,
    f077nmt_f077_net_margin_trend_nm_slope_126d_slope_v049_signal,
    f077nmt_f077_net_margin_trend_nm_slope_126d_slope_v050_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v051_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v052_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v053_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v054_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v055_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v056_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v057_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v058_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v059_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v060_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v061_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v062_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v063_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v064_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v065_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v066_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v067_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v068_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v069_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_21d_slope_v070_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v071_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v072_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v073_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v074_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v075_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v076_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v077_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v078_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v079_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v080_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v081_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v082_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v083_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v084_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v085_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v086_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v087_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v088_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v089_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_63d_slope_v090_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_126d_slope_v091_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_126d_slope_v092_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_126d_slope_v093_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_126d_slope_v094_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_126d_slope_v095_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_126d_slope_v096_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_126d_slope_v097_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_126d_slope_v098_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_126d_slope_v099_signal,
    f077nmt_f077_net_margin_trend_nm_smoothed_126d_slope_v100_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v101_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v102_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v103_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v104_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v105_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v106_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v107_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v108_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v109_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v110_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v111_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v112_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v113_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v114_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v115_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v116_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v117_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v118_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v119_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_21d_slope_v120_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v121_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v122_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v123_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v124_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v125_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v126_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v127_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v128_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v129_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v130_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v131_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v132_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v133_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v134_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v135_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v136_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v137_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v138_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v139_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_63d_slope_v140_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_126d_slope_v141_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_126d_slope_v142_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_126d_slope_v143_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_126d_slope_v144_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_126d_slope_v145_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_126d_slope_v146_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_126d_slope_v147_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_126d_slope_v148_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_126d_slope_v149_signal,
    f077nmt_f077_net_margin_trend_nm_trend_quality_126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F077_NET_MARGIN_TREND_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    netmargin = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    cols = {"netmargin": netmargin, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f077_nm_slope", "_f077_nm_smoothed", "_f077_nm_trend_quality",)
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
    print(f"OK f077_net_margin_trend_2nd_derivatives_001_150_claude: {n_features} features pass")
