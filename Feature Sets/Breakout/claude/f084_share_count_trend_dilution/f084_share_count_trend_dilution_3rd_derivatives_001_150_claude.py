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
    return s.ewm(span=max(2, w), adjust=False, min_periods=max(1, w // 2)).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f084_share_change(sharesbas, w):
    return sharesbas.pct_change(periods=w)


def _f084_dilution_intensity(sharesbas, w):
    chg = sharesbas.pct_change(periods=w)
    return chg.rolling(w, min_periods=max(1, w // 2)).std() + chg


def _f084_dilution_score(sharesbas, shareswa, w):
    gap = (sharesbas - shareswa) / shareswa.abs().replace(0, np.nan)
    return gap.rolling(w, min_periods=max(1, w // 2)).mean()


def f084sct_f084_share_count_trend_dilution_sch_21d_jerk_v001_signal(sharesbas, closeadj):
    base_pre = _f084_share_change(sharesbas, 21)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_21d_jerk_v002_signal(sharesbas, closeadj):
    base_pre = _f084_share_change(sharesbas, 21)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_21d_jerk_v003_signal(sharesbas, closeadj):
    base_pre = _f084_share_change(sharesbas, 21)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_21d_jerk_v004_signal(sharesbas, closeadj):
    base_pre = _f084_share_change(sharesbas, 21)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_21d_jerk_v005_signal(sharesbas, closeadj):
    base_pre = _f084_share_change(sharesbas, 21)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_63d_jerk_v006_signal(sharesbas, closeadj):
    base_pre = _f084_share_change(sharesbas, 63)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_63d_jerk_v007_signal(sharesbas, closeadj):
    base_pre = _f084_share_change(sharesbas, 63)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_63d_jerk_v008_signal(sharesbas, closeadj):
    base_pre = _f084_share_change(sharesbas, 63)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_63d_jerk_v009_signal(sharesbas, closeadj):
    base_pre = _f084_share_change(sharesbas, 63)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_63d_jerk_v010_signal(sharesbas, closeadj):
    base_pre = _f084_share_change(sharesbas, 63)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_252d_jerk_v011_signal(sharesbas, closeadj):
    base_pre = _f084_share_change(sharesbas, 252)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_252d_jerk_v012_signal(sharesbas, closeadj):
    base_pre = _f084_share_change(sharesbas, 252)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_252d_jerk_v013_signal(sharesbas, closeadj):
    base_pre = _f084_share_change(sharesbas, 252)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_252d_jerk_v014_signal(sharesbas, closeadj):
    base_pre = _f084_share_change(sharesbas, 252)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sch_252d_jerk_v015_signal(sharesbas, closeadj):
    base_pre = _f084_share_change(sharesbas, 252)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_21d_jerk_v016_signal(sharesbas, closeadj):
    base_pre = _z(_f084_share_change(sharesbas, 21), 63)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_21d_jerk_v017_signal(sharesbas, closeadj):
    base_pre = _z(_f084_share_change(sharesbas, 21), 63)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_21d_jerk_v018_signal(sharesbas, closeadj):
    base_pre = _z(_f084_share_change(sharesbas, 21), 63)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_21d_jerk_v019_signal(sharesbas, closeadj):
    base_pre = _z(_f084_share_change(sharesbas, 21), 63)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_21d_jerk_v020_signal(sharesbas, closeadj):
    base_pre = _z(_f084_share_change(sharesbas, 21), 63)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_63d_jerk_v021_signal(sharesbas, closeadj):
    base_pre = _z(_f084_share_change(sharesbas, 63), 126)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_63d_jerk_v022_signal(sharesbas, closeadj):
    base_pre = _z(_f084_share_change(sharesbas, 63), 126)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_63d_jerk_v023_signal(sharesbas, closeadj):
    base_pre = _z(_f084_share_change(sharesbas, 63), 126)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_63d_jerk_v024_signal(sharesbas, closeadj):
    base_pre = _z(_f084_share_change(sharesbas, 63), 126)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_63d_jerk_v025_signal(sharesbas, closeadj):
    base_pre = _z(_f084_share_change(sharesbas, 63), 126)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_252d_jerk_v026_signal(sharesbas, closeadj):
    base_pre = _z(_f084_share_change(sharesbas, 252), 504)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_252d_jerk_v027_signal(sharesbas, closeadj):
    base_pre = _z(_f084_share_change(sharesbas, 252), 504)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_252d_jerk_v028_signal(sharesbas, closeadj):
    base_pre = _z(_f084_share_change(sharesbas, 252), 504)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_252d_jerk_v029_signal(sharesbas, closeadj):
    base_pre = _z(_f084_share_change(sharesbas, 252), 504)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_schz_252d_jerk_v030_signal(sharesbas, closeadj):
    base_pre = _z(_f084_share_change(sharesbas, 252), 504)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_21d_jerk_v031_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_share_change(sharesbas, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_21d_jerk_v032_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_share_change(sharesbas, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_21d_jerk_v033_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_share_change(sharesbas, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_21d_jerk_v034_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_share_change(sharesbas, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_21d_jerk_v035_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_share_change(sharesbas, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_63d_jerk_v036_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_share_change(sharesbas, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_63d_jerk_v037_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_share_change(sharesbas, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_63d_jerk_v038_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_share_change(sharesbas, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_63d_jerk_v039_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_share_change(sharesbas, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_63d_jerk_v040_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_share_change(sharesbas, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_252d_jerk_v041_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_share_change(sharesbas, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_252d_jerk_v042_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_share_change(sharesbas, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_252d_jerk_v043_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_share_change(sharesbas, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_252d_jerk_v044_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_share_change(sharesbas, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_sche_252d_jerk_v045_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_share_change(sharesbas, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_21d_jerk_v046_signal(sharesbas, closeadj):
    base_pre = _f084_dilution_intensity(sharesbas, 21)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_21d_jerk_v047_signal(sharesbas, closeadj):
    base_pre = _f084_dilution_intensity(sharesbas, 21)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_21d_jerk_v048_signal(sharesbas, closeadj):
    base_pre = _f084_dilution_intensity(sharesbas, 21)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_21d_jerk_v049_signal(sharesbas, closeadj):
    base_pre = _f084_dilution_intensity(sharesbas, 21)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_21d_jerk_v050_signal(sharesbas, closeadj):
    base_pre = _f084_dilution_intensity(sharesbas, 21)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_63d_jerk_v051_signal(sharesbas, closeadj):
    base_pre = _f084_dilution_intensity(sharesbas, 63)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_63d_jerk_v052_signal(sharesbas, closeadj):
    base_pre = _f084_dilution_intensity(sharesbas, 63)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_63d_jerk_v053_signal(sharesbas, closeadj):
    base_pre = _f084_dilution_intensity(sharesbas, 63)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_63d_jerk_v054_signal(sharesbas, closeadj):
    base_pre = _f084_dilution_intensity(sharesbas, 63)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_63d_jerk_v055_signal(sharesbas, closeadj):
    base_pre = _f084_dilution_intensity(sharesbas, 63)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_252d_jerk_v056_signal(sharesbas, closeadj):
    base_pre = _f084_dilution_intensity(sharesbas, 252)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_252d_jerk_v057_signal(sharesbas, closeadj):
    base_pre = _f084_dilution_intensity(sharesbas, 252)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_252d_jerk_v058_signal(sharesbas, closeadj):
    base_pre = _f084_dilution_intensity(sharesbas, 252)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_252d_jerk_v059_signal(sharesbas, closeadj):
    base_pre = _f084_dilution_intensity(sharesbas, 252)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_din_252d_jerk_v060_signal(sharesbas, closeadj):
    base_pre = _f084_dilution_intensity(sharesbas, 252)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_21d_jerk_v061_signal(sharesbas, closeadj):
    base_pre = _mean(_f084_dilution_intensity(sharesbas, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_21d_jerk_v062_signal(sharesbas, closeadj):
    base_pre = _mean(_f084_dilution_intensity(sharesbas, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_21d_jerk_v063_signal(sharesbas, closeadj):
    base_pre = _mean(_f084_dilution_intensity(sharesbas, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_21d_jerk_v064_signal(sharesbas, closeadj):
    base_pre = _mean(_f084_dilution_intensity(sharesbas, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_21d_jerk_v065_signal(sharesbas, closeadj):
    base_pre = _mean(_f084_dilution_intensity(sharesbas, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_63d_jerk_v066_signal(sharesbas, closeadj):
    base_pre = _mean(_f084_dilution_intensity(sharesbas, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_63d_jerk_v067_signal(sharesbas, closeadj):
    base_pre = _mean(_f084_dilution_intensity(sharesbas, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_63d_jerk_v068_signal(sharesbas, closeadj):
    base_pre = _mean(_f084_dilution_intensity(sharesbas, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_63d_jerk_v069_signal(sharesbas, closeadj):
    base_pre = _mean(_f084_dilution_intensity(sharesbas, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_63d_jerk_v070_signal(sharesbas, closeadj):
    base_pre = _mean(_f084_dilution_intensity(sharesbas, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_252d_jerk_v071_signal(sharesbas, closeadj):
    base_pre = _mean(_f084_dilution_intensity(sharesbas, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_252d_jerk_v072_signal(sharesbas, closeadj):
    base_pre = _mean(_f084_dilution_intensity(sharesbas, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_252d_jerk_v073_signal(sharesbas, closeadj):
    base_pre = _mean(_f084_dilution_intensity(sharesbas, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_252d_jerk_v074_signal(sharesbas, closeadj):
    base_pre = _mean(_f084_dilution_intensity(sharesbas, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dinm_252d_jerk_v075_signal(sharesbas, closeadj):
    base_pre = _mean(_f084_dilution_intensity(sharesbas, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_21d_jerk_v076_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_dilution_intensity(sharesbas, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_21d_jerk_v077_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_dilution_intensity(sharesbas, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_21d_jerk_v078_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_dilution_intensity(sharesbas, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_21d_jerk_v079_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_dilution_intensity(sharesbas, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_21d_jerk_v080_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_dilution_intensity(sharesbas, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_63d_jerk_v081_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_dilution_intensity(sharesbas, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_63d_jerk_v082_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_dilution_intensity(sharesbas, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_63d_jerk_v083_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_dilution_intensity(sharesbas, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_63d_jerk_v084_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_dilution_intensity(sharesbas, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_63d_jerk_v085_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_dilution_intensity(sharesbas, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_252d_jerk_v086_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_dilution_intensity(sharesbas, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_252d_jerk_v087_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_dilution_intensity(sharesbas, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_252d_jerk_v088_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_dilution_intensity(sharesbas, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_252d_jerk_v089_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_dilution_intensity(sharesbas, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dine_252d_jerk_v090_signal(sharesbas, closeadj):
    base_pre = _ema(_f084_dilution_intensity(sharesbas, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_21d_jerk_v091_signal(sharesbas, shareswa, closeadj):
    base_pre = _f084_dilution_score(sharesbas, shareswa, 21)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_21d_jerk_v092_signal(sharesbas, shareswa, closeadj):
    base_pre = _f084_dilution_score(sharesbas, shareswa, 21)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_21d_jerk_v093_signal(sharesbas, shareswa, closeadj):
    base_pre = _f084_dilution_score(sharesbas, shareswa, 21)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_21d_jerk_v094_signal(sharesbas, shareswa, closeadj):
    base_pre = _f084_dilution_score(sharesbas, shareswa, 21)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_21d_jerk_v095_signal(sharesbas, shareswa, closeadj):
    base_pre = _f084_dilution_score(sharesbas, shareswa, 21)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_63d_jerk_v096_signal(sharesbas, shareswa, closeadj):
    base_pre = _f084_dilution_score(sharesbas, shareswa, 63)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_63d_jerk_v097_signal(sharesbas, shareswa, closeadj):
    base_pre = _f084_dilution_score(sharesbas, shareswa, 63)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_63d_jerk_v098_signal(sharesbas, shareswa, closeadj):
    base_pre = _f084_dilution_score(sharesbas, shareswa, 63)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_63d_jerk_v099_signal(sharesbas, shareswa, closeadj):
    base_pre = _f084_dilution_score(sharesbas, shareswa, 63)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_63d_jerk_v100_signal(sharesbas, shareswa, closeadj):
    base_pre = _f084_dilution_score(sharesbas, shareswa, 63)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_252d_jerk_v101_signal(sharesbas, shareswa, closeadj):
    base_pre = _f084_dilution_score(sharesbas, shareswa, 252)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_252d_jerk_v102_signal(sharesbas, shareswa, closeadj):
    base_pre = _f084_dilution_score(sharesbas, shareswa, 252)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_252d_jerk_v103_signal(sharesbas, shareswa, closeadj):
    base_pre = _f084_dilution_score(sharesbas, shareswa, 252)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_252d_jerk_v104_signal(sharesbas, shareswa, closeadj):
    base_pre = _f084_dilution_score(sharesbas, shareswa, 252)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsc_252d_jerk_v105_signal(sharesbas, shareswa, closeadj):
    base_pre = _f084_dilution_score(sharesbas, shareswa, 252)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_21d_jerk_v106_signal(sharesbas, shareswa, closeadj):
    base_pre = _z(_f084_dilution_score(sharesbas, shareswa, 21), 63)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_21d_jerk_v107_signal(sharesbas, shareswa, closeadj):
    base_pre = _z(_f084_dilution_score(sharesbas, shareswa, 21), 63)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_21d_jerk_v108_signal(sharesbas, shareswa, closeadj):
    base_pre = _z(_f084_dilution_score(sharesbas, shareswa, 21), 63)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_21d_jerk_v109_signal(sharesbas, shareswa, closeadj):
    base_pre = _z(_f084_dilution_score(sharesbas, shareswa, 21), 63)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_21d_jerk_v110_signal(sharesbas, shareswa, closeadj):
    base_pre = _z(_f084_dilution_score(sharesbas, shareswa, 21), 63)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_63d_jerk_v111_signal(sharesbas, shareswa, closeadj):
    base_pre = _z(_f084_dilution_score(sharesbas, shareswa, 63), 126)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_63d_jerk_v112_signal(sharesbas, shareswa, closeadj):
    base_pre = _z(_f084_dilution_score(sharesbas, shareswa, 63), 126)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_63d_jerk_v113_signal(sharesbas, shareswa, closeadj):
    base_pre = _z(_f084_dilution_score(sharesbas, shareswa, 63), 126)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_63d_jerk_v114_signal(sharesbas, shareswa, closeadj):
    base_pre = _z(_f084_dilution_score(sharesbas, shareswa, 63), 126)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_63d_jerk_v115_signal(sharesbas, shareswa, closeadj):
    base_pre = _z(_f084_dilution_score(sharesbas, shareswa, 63), 126)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_252d_jerk_v116_signal(sharesbas, shareswa, closeadj):
    base_pre = _z(_f084_dilution_score(sharesbas, shareswa, 252), 504)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_252d_jerk_v117_signal(sharesbas, shareswa, closeadj):
    base_pre = _z(_f084_dilution_score(sharesbas, shareswa, 252), 504)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_252d_jerk_v118_signal(sharesbas, shareswa, closeadj):
    base_pre = _z(_f084_dilution_score(sharesbas, shareswa, 252), 504)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_252d_jerk_v119_signal(sharesbas, shareswa, closeadj):
    base_pre = _z(_f084_dilution_score(sharesbas, shareswa, 252), 504)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscz_252d_jerk_v120_signal(sharesbas, shareswa, closeadj):
    base_pre = _z(_f084_dilution_score(sharesbas, shareswa, 252), 504)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_21d_jerk_v121_signal(sharesbas, shareswa, closeadj):
    base_pre = _ema(_f084_dilution_score(sharesbas, shareswa, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_21d_jerk_v122_signal(sharesbas, shareswa, closeadj):
    base_pre = _ema(_f084_dilution_score(sharesbas, shareswa, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_21d_jerk_v123_signal(sharesbas, shareswa, closeadj):
    base_pre = _ema(_f084_dilution_score(sharesbas, shareswa, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_21d_jerk_v124_signal(sharesbas, shareswa, closeadj):
    base_pre = _ema(_f084_dilution_score(sharesbas, shareswa, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_21d_jerk_v125_signal(sharesbas, shareswa, closeadj):
    base_pre = _ema(_f084_dilution_score(sharesbas, shareswa, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_63d_jerk_v126_signal(sharesbas, shareswa, closeadj):
    base_pre = _ema(_f084_dilution_score(sharesbas, shareswa, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_63d_jerk_v127_signal(sharesbas, shareswa, closeadj):
    base_pre = _ema(_f084_dilution_score(sharesbas, shareswa, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_63d_jerk_v128_signal(sharesbas, shareswa, closeadj):
    base_pre = _ema(_f084_dilution_score(sharesbas, shareswa, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_63d_jerk_v129_signal(sharesbas, shareswa, closeadj):
    base_pre = _ema(_f084_dilution_score(sharesbas, shareswa, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_63d_jerk_v130_signal(sharesbas, shareswa, closeadj):
    base_pre = _ema(_f084_dilution_score(sharesbas, shareswa, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_252d_jerk_v131_signal(sharesbas, shareswa, closeadj):
    base_pre = _ema(_f084_dilution_score(sharesbas, shareswa, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_252d_jerk_v132_signal(sharesbas, shareswa, closeadj):
    base_pre = _ema(_f084_dilution_score(sharesbas, shareswa, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_252d_jerk_v133_signal(sharesbas, shareswa, closeadj):
    base_pre = _ema(_f084_dilution_score(sharesbas, shareswa, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_252d_jerk_v134_signal(sharesbas, shareswa, closeadj):
    base_pre = _ema(_f084_dilution_score(sharesbas, shareswa, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dsce_252d_jerk_v135_signal(sharesbas, shareswa, closeadj):
    base_pre = _ema(_f084_dilution_score(sharesbas, shareswa, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_21d_jerk_v136_signal(sharesbas, shareswa, closeadj):
    base_pre = _std(_f084_dilution_score(sharesbas, shareswa, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_21d_jerk_v137_signal(sharesbas, shareswa, closeadj):
    base_pre = _std(_f084_dilution_score(sharesbas, shareswa, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_21d_jerk_v138_signal(sharesbas, shareswa, closeadj):
    base_pre = _std(_f084_dilution_score(sharesbas, shareswa, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_21d_jerk_v139_signal(sharesbas, shareswa, closeadj):
    base_pre = _std(_f084_dilution_score(sharesbas, shareswa, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_21d_jerk_v140_signal(sharesbas, shareswa, closeadj):
    base_pre = _std(_f084_dilution_score(sharesbas, shareswa, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_63d_jerk_v141_signal(sharesbas, shareswa, closeadj):
    base_pre = _std(_f084_dilution_score(sharesbas, shareswa, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_63d_jerk_v142_signal(sharesbas, shareswa, closeadj):
    base_pre = _std(_f084_dilution_score(sharesbas, shareswa, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_63d_jerk_v143_signal(sharesbas, shareswa, closeadj):
    base_pre = _std(_f084_dilution_score(sharesbas, shareswa, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_63d_jerk_v144_signal(sharesbas, shareswa, closeadj):
    base_pre = _std(_f084_dilution_score(sharesbas, shareswa, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_63d_jerk_v145_signal(sharesbas, shareswa, closeadj):
    base_pre = _std(_f084_dilution_score(sharesbas, shareswa, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_252d_jerk_v146_signal(sharesbas, shareswa, closeadj):
    base_pre = _std(_f084_dilution_score(sharesbas, shareswa, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_252d_jerk_v147_signal(sharesbas, shareswa, closeadj):
    base_pre = _std(_f084_dilution_score(sharesbas, shareswa, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_252d_jerk_v148_signal(sharesbas, shareswa, closeadj):
    base_pre = _std(_f084_dilution_score(sharesbas, shareswa, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_252d_jerk_v149_signal(sharesbas, shareswa, closeadj):
    base_pre = _std(_f084_dilution_score(sharesbas, shareswa, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f084sct_f084_share_count_trend_dilution_dscs_252d_jerk_v150_signal(sharesbas, shareswa, closeadj):
    base_pre = _std(_f084_dilution_score(sharesbas, shareswa, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f084sct_f084_share_count_trend_dilution_sch_21d_jerk_v001_signal,
    f084sct_f084_share_count_trend_dilution_sch_21d_jerk_v002_signal,
    f084sct_f084_share_count_trend_dilution_sch_21d_jerk_v003_signal,
    f084sct_f084_share_count_trend_dilution_sch_21d_jerk_v004_signal,
    f084sct_f084_share_count_trend_dilution_sch_21d_jerk_v005_signal,
    f084sct_f084_share_count_trend_dilution_sch_63d_jerk_v006_signal,
    f084sct_f084_share_count_trend_dilution_sch_63d_jerk_v007_signal,
    f084sct_f084_share_count_trend_dilution_sch_63d_jerk_v008_signal,
    f084sct_f084_share_count_trend_dilution_sch_63d_jerk_v009_signal,
    f084sct_f084_share_count_trend_dilution_sch_63d_jerk_v010_signal,
    f084sct_f084_share_count_trend_dilution_sch_252d_jerk_v011_signal,
    f084sct_f084_share_count_trend_dilution_sch_252d_jerk_v012_signal,
    f084sct_f084_share_count_trend_dilution_sch_252d_jerk_v013_signal,
    f084sct_f084_share_count_trend_dilution_sch_252d_jerk_v014_signal,
    f084sct_f084_share_count_trend_dilution_sch_252d_jerk_v015_signal,
    f084sct_f084_share_count_trend_dilution_schz_21d_jerk_v016_signal,
    f084sct_f084_share_count_trend_dilution_schz_21d_jerk_v017_signal,
    f084sct_f084_share_count_trend_dilution_schz_21d_jerk_v018_signal,
    f084sct_f084_share_count_trend_dilution_schz_21d_jerk_v019_signal,
    f084sct_f084_share_count_trend_dilution_schz_21d_jerk_v020_signal,
    f084sct_f084_share_count_trend_dilution_schz_63d_jerk_v021_signal,
    f084sct_f084_share_count_trend_dilution_schz_63d_jerk_v022_signal,
    f084sct_f084_share_count_trend_dilution_schz_63d_jerk_v023_signal,
    f084sct_f084_share_count_trend_dilution_schz_63d_jerk_v024_signal,
    f084sct_f084_share_count_trend_dilution_schz_63d_jerk_v025_signal,
    f084sct_f084_share_count_trend_dilution_schz_252d_jerk_v026_signal,
    f084sct_f084_share_count_trend_dilution_schz_252d_jerk_v027_signal,
    f084sct_f084_share_count_trend_dilution_schz_252d_jerk_v028_signal,
    f084sct_f084_share_count_trend_dilution_schz_252d_jerk_v029_signal,
    f084sct_f084_share_count_trend_dilution_schz_252d_jerk_v030_signal,
    f084sct_f084_share_count_trend_dilution_sche_21d_jerk_v031_signal,
    f084sct_f084_share_count_trend_dilution_sche_21d_jerk_v032_signal,
    f084sct_f084_share_count_trend_dilution_sche_21d_jerk_v033_signal,
    f084sct_f084_share_count_trend_dilution_sche_21d_jerk_v034_signal,
    f084sct_f084_share_count_trend_dilution_sche_21d_jerk_v035_signal,
    f084sct_f084_share_count_trend_dilution_sche_63d_jerk_v036_signal,
    f084sct_f084_share_count_trend_dilution_sche_63d_jerk_v037_signal,
    f084sct_f084_share_count_trend_dilution_sche_63d_jerk_v038_signal,
    f084sct_f084_share_count_trend_dilution_sche_63d_jerk_v039_signal,
    f084sct_f084_share_count_trend_dilution_sche_63d_jerk_v040_signal,
    f084sct_f084_share_count_trend_dilution_sche_252d_jerk_v041_signal,
    f084sct_f084_share_count_trend_dilution_sche_252d_jerk_v042_signal,
    f084sct_f084_share_count_trend_dilution_sche_252d_jerk_v043_signal,
    f084sct_f084_share_count_trend_dilution_sche_252d_jerk_v044_signal,
    f084sct_f084_share_count_trend_dilution_sche_252d_jerk_v045_signal,
    f084sct_f084_share_count_trend_dilution_din_21d_jerk_v046_signal,
    f084sct_f084_share_count_trend_dilution_din_21d_jerk_v047_signal,
    f084sct_f084_share_count_trend_dilution_din_21d_jerk_v048_signal,
    f084sct_f084_share_count_trend_dilution_din_21d_jerk_v049_signal,
    f084sct_f084_share_count_trend_dilution_din_21d_jerk_v050_signal,
    f084sct_f084_share_count_trend_dilution_din_63d_jerk_v051_signal,
    f084sct_f084_share_count_trend_dilution_din_63d_jerk_v052_signal,
    f084sct_f084_share_count_trend_dilution_din_63d_jerk_v053_signal,
    f084sct_f084_share_count_trend_dilution_din_63d_jerk_v054_signal,
    f084sct_f084_share_count_trend_dilution_din_63d_jerk_v055_signal,
    f084sct_f084_share_count_trend_dilution_din_252d_jerk_v056_signal,
    f084sct_f084_share_count_trend_dilution_din_252d_jerk_v057_signal,
    f084sct_f084_share_count_trend_dilution_din_252d_jerk_v058_signal,
    f084sct_f084_share_count_trend_dilution_din_252d_jerk_v059_signal,
    f084sct_f084_share_count_trend_dilution_din_252d_jerk_v060_signal,
    f084sct_f084_share_count_trend_dilution_dinm_21d_jerk_v061_signal,
    f084sct_f084_share_count_trend_dilution_dinm_21d_jerk_v062_signal,
    f084sct_f084_share_count_trend_dilution_dinm_21d_jerk_v063_signal,
    f084sct_f084_share_count_trend_dilution_dinm_21d_jerk_v064_signal,
    f084sct_f084_share_count_trend_dilution_dinm_21d_jerk_v065_signal,
    f084sct_f084_share_count_trend_dilution_dinm_63d_jerk_v066_signal,
    f084sct_f084_share_count_trend_dilution_dinm_63d_jerk_v067_signal,
    f084sct_f084_share_count_trend_dilution_dinm_63d_jerk_v068_signal,
    f084sct_f084_share_count_trend_dilution_dinm_63d_jerk_v069_signal,
    f084sct_f084_share_count_trend_dilution_dinm_63d_jerk_v070_signal,
    f084sct_f084_share_count_trend_dilution_dinm_252d_jerk_v071_signal,
    f084sct_f084_share_count_trend_dilution_dinm_252d_jerk_v072_signal,
    f084sct_f084_share_count_trend_dilution_dinm_252d_jerk_v073_signal,
    f084sct_f084_share_count_trend_dilution_dinm_252d_jerk_v074_signal,
    f084sct_f084_share_count_trend_dilution_dinm_252d_jerk_v075_signal,
    f084sct_f084_share_count_trend_dilution_dine_21d_jerk_v076_signal,
    f084sct_f084_share_count_trend_dilution_dine_21d_jerk_v077_signal,
    f084sct_f084_share_count_trend_dilution_dine_21d_jerk_v078_signal,
    f084sct_f084_share_count_trend_dilution_dine_21d_jerk_v079_signal,
    f084sct_f084_share_count_trend_dilution_dine_21d_jerk_v080_signal,
    f084sct_f084_share_count_trend_dilution_dine_63d_jerk_v081_signal,
    f084sct_f084_share_count_trend_dilution_dine_63d_jerk_v082_signal,
    f084sct_f084_share_count_trend_dilution_dine_63d_jerk_v083_signal,
    f084sct_f084_share_count_trend_dilution_dine_63d_jerk_v084_signal,
    f084sct_f084_share_count_trend_dilution_dine_63d_jerk_v085_signal,
    f084sct_f084_share_count_trend_dilution_dine_252d_jerk_v086_signal,
    f084sct_f084_share_count_trend_dilution_dine_252d_jerk_v087_signal,
    f084sct_f084_share_count_trend_dilution_dine_252d_jerk_v088_signal,
    f084sct_f084_share_count_trend_dilution_dine_252d_jerk_v089_signal,
    f084sct_f084_share_count_trend_dilution_dine_252d_jerk_v090_signal,
    f084sct_f084_share_count_trend_dilution_dsc_21d_jerk_v091_signal,
    f084sct_f084_share_count_trend_dilution_dsc_21d_jerk_v092_signal,
    f084sct_f084_share_count_trend_dilution_dsc_21d_jerk_v093_signal,
    f084sct_f084_share_count_trend_dilution_dsc_21d_jerk_v094_signal,
    f084sct_f084_share_count_trend_dilution_dsc_21d_jerk_v095_signal,
    f084sct_f084_share_count_trend_dilution_dsc_63d_jerk_v096_signal,
    f084sct_f084_share_count_trend_dilution_dsc_63d_jerk_v097_signal,
    f084sct_f084_share_count_trend_dilution_dsc_63d_jerk_v098_signal,
    f084sct_f084_share_count_trend_dilution_dsc_63d_jerk_v099_signal,
    f084sct_f084_share_count_trend_dilution_dsc_63d_jerk_v100_signal,
    f084sct_f084_share_count_trend_dilution_dsc_252d_jerk_v101_signal,
    f084sct_f084_share_count_trend_dilution_dsc_252d_jerk_v102_signal,
    f084sct_f084_share_count_trend_dilution_dsc_252d_jerk_v103_signal,
    f084sct_f084_share_count_trend_dilution_dsc_252d_jerk_v104_signal,
    f084sct_f084_share_count_trend_dilution_dsc_252d_jerk_v105_signal,
    f084sct_f084_share_count_trend_dilution_dscz_21d_jerk_v106_signal,
    f084sct_f084_share_count_trend_dilution_dscz_21d_jerk_v107_signal,
    f084sct_f084_share_count_trend_dilution_dscz_21d_jerk_v108_signal,
    f084sct_f084_share_count_trend_dilution_dscz_21d_jerk_v109_signal,
    f084sct_f084_share_count_trend_dilution_dscz_21d_jerk_v110_signal,
    f084sct_f084_share_count_trend_dilution_dscz_63d_jerk_v111_signal,
    f084sct_f084_share_count_trend_dilution_dscz_63d_jerk_v112_signal,
    f084sct_f084_share_count_trend_dilution_dscz_63d_jerk_v113_signal,
    f084sct_f084_share_count_trend_dilution_dscz_63d_jerk_v114_signal,
    f084sct_f084_share_count_trend_dilution_dscz_63d_jerk_v115_signal,
    f084sct_f084_share_count_trend_dilution_dscz_252d_jerk_v116_signal,
    f084sct_f084_share_count_trend_dilution_dscz_252d_jerk_v117_signal,
    f084sct_f084_share_count_trend_dilution_dscz_252d_jerk_v118_signal,
    f084sct_f084_share_count_trend_dilution_dscz_252d_jerk_v119_signal,
    f084sct_f084_share_count_trend_dilution_dscz_252d_jerk_v120_signal,
    f084sct_f084_share_count_trend_dilution_dsce_21d_jerk_v121_signal,
    f084sct_f084_share_count_trend_dilution_dsce_21d_jerk_v122_signal,
    f084sct_f084_share_count_trend_dilution_dsce_21d_jerk_v123_signal,
    f084sct_f084_share_count_trend_dilution_dsce_21d_jerk_v124_signal,
    f084sct_f084_share_count_trend_dilution_dsce_21d_jerk_v125_signal,
    f084sct_f084_share_count_trend_dilution_dsce_63d_jerk_v126_signal,
    f084sct_f084_share_count_trend_dilution_dsce_63d_jerk_v127_signal,
    f084sct_f084_share_count_trend_dilution_dsce_63d_jerk_v128_signal,
    f084sct_f084_share_count_trend_dilution_dsce_63d_jerk_v129_signal,
    f084sct_f084_share_count_trend_dilution_dsce_63d_jerk_v130_signal,
    f084sct_f084_share_count_trend_dilution_dsce_252d_jerk_v131_signal,
    f084sct_f084_share_count_trend_dilution_dsce_252d_jerk_v132_signal,
    f084sct_f084_share_count_trend_dilution_dsce_252d_jerk_v133_signal,
    f084sct_f084_share_count_trend_dilution_dsce_252d_jerk_v134_signal,
    f084sct_f084_share_count_trend_dilution_dsce_252d_jerk_v135_signal,
    f084sct_f084_share_count_trend_dilution_dscs_21d_jerk_v136_signal,
    f084sct_f084_share_count_trend_dilution_dscs_21d_jerk_v137_signal,
    f084sct_f084_share_count_trend_dilution_dscs_21d_jerk_v138_signal,
    f084sct_f084_share_count_trend_dilution_dscs_21d_jerk_v139_signal,
    f084sct_f084_share_count_trend_dilution_dscs_21d_jerk_v140_signal,
    f084sct_f084_share_count_trend_dilution_dscs_63d_jerk_v141_signal,
    f084sct_f084_share_count_trend_dilution_dscs_63d_jerk_v142_signal,
    f084sct_f084_share_count_trend_dilution_dscs_63d_jerk_v143_signal,
    f084sct_f084_share_count_trend_dilution_dscs_63d_jerk_v144_signal,
    f084sct_f084_share_count_trend_dilution_dscs_63d_jerk_v145_signal,
    f084sct_f084_share_count_trend_dilution_dscs_252d_jerk_v146_signal,
    f084sct_f084_share_count_trend_dilution_dscs_252d_jerk_v147_signal,
    f084sct_f084_share_count_trend_dilution_dscs_252d_jerk_v148_signal,
    f084sct_f084_share_count_trend_dilution_dscs_252d_jerk_v149_signal,
    f084sct_f084_share_count_trend_dilution_dscs_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F084_SHARE_COUNT_TREND_DILUTION_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    cashneq = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    debt    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    equity  = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    marketcap = pd.Series(closeadj * 1e8, name="marketcap")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "ebitda": ebitda, "netinc": netinc,
        "fcf": fcf, "ncfo": ncfo, "cashneq": cashneq, "debt": debt, "equity": equity,
        "sharesbas": sharesbas, "shareswa": shareswa, "marketcap": marketcap,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f084_share_change", "_f084_dilution_intensity", "_f084_dilution_score")
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
    print(f"OK f084_share_count_trend_dilution_3rd_derivatives_001_150_claude: {n_features} features pass")
