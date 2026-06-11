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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


def _f039_price_progress(close, w):
    return close.pct_change(periods=w)


def _f039_volume_effort(volume, w):
    return volume.rolling(w, min_periods=max(1, w // 2)).sum()


def _f039_effort_result_ratio(close, volume, w):
    progress = close.pct_change(periods=w)
    effort = volume.rolling(w, min_periods=max(1, w // 2)).sum()
    return progress / (effort + 1.0).replace(0, np.nan)


def f039evr_f039_effort_vs_result_pprog_10d_jerk_v001_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_21d_jerk_v002_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_42d_jerk_v003_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_42d_jerk_v004_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_42d_jerk_v005_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_42d_jerk_v006_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 42) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_63d_jerk_v007_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_63d_jerk_v008_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_63d_jerk_v009_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_63d_jerk_v010_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_126d_jerk_v011_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_126d_jerk_v012_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_126d_jerk_v013_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_126d_jerk_v014_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_189d_jerk_v015_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_189d_jerk_v016_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_189d_jerk_v017_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_189d_jerk_v018_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 189) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_252d_jerk_v019_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_252d_jerk_v020_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_252d_jerk_v021_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_252d_jerk_v022_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_378d_jerk_v023_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_378d_jerk_v024_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_378d_jerk_v025_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_504d_jerk_v026_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_504d_jerk_v027_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprog_504d_jerk_v028_signal(closeadj, volume):
    base = _f039_price_progress(closeadj, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogsm_10d_jerk_v029_signal(closeadj, volume):
    base = _mean(_f039_price_progress(closeadj, 10), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogsm_21d_jerk_v030_signal(closeadj, volume):
    base = _mean(_f039_price_progress(closeadj, 21), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogsm_42d_jerk_v031_signal(closeadj, volume):
    base = _mean(_f039_price_progress(closeadj, 42), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogsm_42d_jerk_v032_signal(closeadj, volume):
    base = _mean(_f039_price_progress(closeadj, 42), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogsm_42d_jerk_v033_signal(closeadj, volume):
    base = _mean(_f039_price_progress(closeadj, 42), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogsm_42d_jerk_v034_signal(closeadj, volume):
    base = _mean(_f039_price_progress(closeadj, 42), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogsm_63d_jerk_v035_signal(closeadj, volume):
    base = _mean(_f039_price_progress(closeadj, 63), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogsm_63d_jerk_v036_signal(closeadj, volume):
    base = _mean(_f039_price_progress(closeadj, 63), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogsm_63d_jerk_v037_signal(closeadj, volume):
    base = _mean(_f039_price_progress(closeadj, 63), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogsm_63d_jerk_v038_signal(closeadj, volume):
    base = _mean(_f039_price_progress(closeadj, 63), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogsm_126d_jerk_v039_signal(closeadj, volume):
    base = _mean(_f039_price_progress(closeadj, 126), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogsm_126d_jerk_v040_signal(closeadj, volume):
    base = _mean(_f039_price_progress(closeadj, 126), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogsm_126d_jerk_v041_signal(closeadj, volume):
    base = _mean(_f039_price_progress(closeadj, 126), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogsm_126d_jerk_v042_signal(closeadj, volume):
    base = _mean(_f039_price_progress(closeadj, 126), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogsm_189d_jerk_v043_signal(closeadj, volume):
    base = _mean(_f039_price_progress(closeadj, 189), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogsm_189d_jerk_v044_signal(closeadj, volume):
    base = _mean(_f039_price_progress(closeadj, 189), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogsm_189d_jerk_v045_signal(closeadj, volume):
    base = _mean(_f039_price_progress(closeadj, 189), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogsm_189d_jerk_v046_signal(closeadj, volume):
    base = _mean(_f039_price_progress(closeadj, 189), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogsm_252d_jerk_v047_signal(closeadj, volume):
    base = _mean(_f039_price_progress(closeadj, 252), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogsm_252d_jerk_v048_signal(closeadj, volume):
    base = _mean(_f039_price_progress(closeadj, 252), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogsm_252d_jerk_v049_signal(closeadj, volume):
    base = _mean(_f039_price_progress(closeadj, 252), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogsm_252d_jerk_v050_signal(closeadj, volume):
    base = _mean(_f039_price_progress(closeadj, 252), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_10d_jerk_v051_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 10) * closeadj / 1e6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_21d_jerk_v052_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 21) * closeadj / 1e6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_42d_jerk_v053_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 42) * closeadj / 1e6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_42d_jerk_v054_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 42) * closeadj / 1e6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_42d_jerk_v055_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 42) * closeadj / 1e6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_42d_jerk_v056_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 42) * closeadj / 1e6
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_63d_jerk_v057_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 63) * closeadj / 1e6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_63d_jerk_v058_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 63) * closeadj / 1e6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_63d_jerk_v059_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 63) * closeadj / 1e6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_63d_jerk_v060_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 63) * closeadj / 1e6
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_126d_jerk_v061_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 126) * closeadj / 1e6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_126d_jerk_v062_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 126) * closeadj / 1e6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_126d_jerk_v063_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 126) * closeadj / 1e6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_126d_jerk_v064_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 126) * closeadj / 1e6
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_189d_jerk_v065_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 189) * closeadj / 1e6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_189d_jerk_v066_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 189) * closeadj / 1e6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_189d_jerk_v067_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 189) * closeadj / 1e6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_189d_jerk_v068_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 189) * closeadj / 1e6
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_252d_jerk_v069_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 252) * closeadj / 1e6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_252d_jerk_v070_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 252) * closeadj / 1e6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_252d_jerk_v071_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 252) * closeadj / 1e6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_252d_jerk_v072_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 252) * closeadj / 1e6
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_378d_jerk_v073_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 378) * closeadj / 1e6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_378d_jerk_v074_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 378) * closeadj / 1e6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_378d_jerk_v075_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 378) * closeadj / 1e6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_504d_jerk_v076_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 504) * closeadj / 1e6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_504d_jerk_v077_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 504) * closeadj / 1e6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veff_504d_jerk_v078_signal(closeadj, volume):
    base = _f039_volume_effort(volume, 504) * closeadj / 1e6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffsm_10d_jerk_v079_signal(closeadj, volume):
    base = _mean(_f039_volume_effort(volume, 10), 21) * closeadj / 1e6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffsm_21d_jerk_v080_signal(closeadj, volume):
    base = _mean(_f039_volume_effort(volume, 21), 21) * closeadj / 1e6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffsm_42d_jerk_v081_signal(closeadj, volume):
    base = _mean(_f039_volume_effort(volume, 42), 21) * closeadj / 1e6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffsm_42d_jerk_v082_signal(closeadj, volume):
    base = _mean(_f039_volume_effort(volume, 42), 21) * closeadj / 1e6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffsm_42d_jerk_v083_signal(closeadj, volume):
    base = _mean(_f039_volume_effort(volume, 42), 21) * closeadj / 1e6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffsm_42d_jerk_v084_signal(closeadj, volume):
    base = _mean(_f039_volume_effort(volume, 42), 21) * closeadj / 1e6
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffsm_63d_jerk_v085_signal(closeadj, volume):
    base = _mean(_f039_volume_effort(volume, 63), 21) * closeadj / 1e6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffsm_63d_jerk_v086_signal(closeadj, volume):
    base = _mean(_f039_volume_effort(volume, 63), 21) * closeadj / 1e6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffsm_63d_jerk_v087_signal(closeadj, volume):
    base = _mean(_f039_volume_effort(volume, 63), 21) * closeadj / 1e6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffsm_63d_jerk_v088_signal(closeadj, volume):
    base = _mean(_f039_volume_effort(volume, 63), 21) * closeadj / 1e6
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffsm_126d_jerk_v089_signal(closeadj, volume):
    base = _mean(_f039_volume_effort(volume, 126), 21) * closeadj / 1e6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffsm_126d_jerk_v090_signal(closeadj, volume):
    base = _mean(_f039_volume_effort(volume, 126), 21) * closeadj / 1e6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffsm_126d_jerk_v091_signal(closeadj, volume):
    base = _mean(_f039_volume_effort(volume, 126), 21) * closeadj / 1e6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffsm_126d_jerk_v092_signal(closeadj, volume):
    base = _mean(_f039_volume_effort(volume, 126), 21) * closeadj / 1e6
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffsm_189d_jerk_v093_signal(closeadj, volume):
    base = _mean(_f039_volume_effort(volume, 189), 21) * closeadj / 1e6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffsm_189d_jerk_v094_signal(closeadj, volume):
    base = _mean(_f039_volume_effort(volume, 189), 21) * closeadj / 1e6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffsm_189d_jerk_v095_signal(closeadj, volume):
    base = _mean(_f039_volume_effort(volume, 189), 21) * closeadj / 1e6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffsm_189d_jerk_v096_signal(closeadj, volume):
    base = _mean(_f039_volume_effort(volume, 189), 21) * closeadj / 1e6
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffsm_252d_jerk_v097_signal(closeadj, volume):
    base = _mean(_f039_volume_effort(volume, 252), 21) * closeadj / 1e6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffsm_252d_jerk_v098_signal(closeadj, volume):
    base = _mean(_f039_volume_effort(volume, 252), 21) * closeadj / 1e6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffsm_252d_jerk_v099_signal(closeadj, volume):
    base = _mean(_f039_volume_effort(volume, 252), 21) * closeadj / 1e6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffsm_252d_jerk_v100_signal(closeadj, volume):
    base = _mean(_f039_volume_effort(volume, 252), 21) * closeadj / 1e6
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_10d_jerk_v101_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_21d_jerk_v102_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_42d_jerk_v103_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_42d_jerk_v104_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_42d_jerk_v105_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_42d_jerk_v106_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 42) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_63d_jerk_v107_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_63d_jerk_v108_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_63d_jerk_v109_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_63d_jerk_v110_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_126d_jerk_v111_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_126d_jerk_v112_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_126d_jerk_v113_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_126d_jerk_v114_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_189d_jerk_v115_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_189d_jerk_v116_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_189d_jerk_v117_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_189d_jerk_v118_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 189) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_252d_jerk_v119_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_252d_jerk_v120_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_252d_jerk_v121_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_252d_jerk_v122_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_378d_jerk_v123_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_378d_jerk_v124_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_378d_jerk_v125_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_504d_jerk_v126_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_504d_jerk_v127_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evr_504d_jerk_v128_signal(closeadj, volume):
    base = _f039_effort_result_ratio(closeadj, volume, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrsm_10d_jerk_v129_signal(closeadj, volume):
    base = _mean(_f039_effort_result_ratio(closeadj, volume, 10), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrsm_21d_jerk_v130_signal(closeadj, volume):
    base = _mean(_f039_effort_result_ratio(closeadj, volume, 21), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrsm_42d_jerk_v131_signal(closeadj, volume):
    base = _mean(_f039_effort_result_ratio(closeadj, volume, 42), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrsm_42d_jerk_v132_signal(closeadj, volume):
    base = _mean(_f039_effort_result_ratio(closeadj, volume, 42), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrsm_42d_jerk_v133_signal(closeadj, volume):
    base = _mean(_f039_effort_result_ratio(closeadj, volume, 42), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrsm_42d_jerk_v134_signal(closeadj, volume):
    base = _mean(_f039_effort_result_ratio(closeadj, volume, 42), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrsm_63d_jerk_v135_signal(closeadj, volume):
    base = _mean(_f039_effort_result_ratio(closeadj, volume, 63), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrsm_63d_jerk_v136_signal(closeadj, volume):
    base = _mean(_f039_effort_result_ratio(closeadj, volume, 63), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrsm_63d_jerk_v137_signal(closeadj, volume):
    base = _mean(_f039_effort_result_ratio(closeadj, volume, 63), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrsm_63d_jerk_v138_signal(closeadj, volume):
    base = _mean(_f039_effort_result_ratio(closeadj, volume, 63), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrsm_126d_jerk_v139_signal(closeadj, volume):
    base = _mean(_f039_effort_result_ratio(closeadj, volume, 126), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrsm_126d_jerk_v140_signal(closeadj, volume):
    base = _mean(_f039_effort_result_ratio(closeadj, volume, 126), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrsm_126d_jerk_v141_signal(closeadj, volume):
    base = _mean(_f039_effort_result_ratio(closeadj, volume, 126), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrsm_126d_jerk_v142_signal(closeadj, volume):
    base = _mean(_f039_effort_result_ratio(closeadj, volume, 126), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrsm_189d_jerk_v143_signal(closeadj, volume):
    base = _mean(_f039_effort_result_ratio(closeadj, volume, 189), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrsm_189d_jerk_v144_signal(closeadj, volume):
    base = _mean(_f039_effort_result_ratio(closeadj, volume, 189), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrsm_189d_jerk_v145_signal(closeadj, volume):
    base = _mean(_f039_effort_result_ratio(closeadj, volume, 189), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrsm_189d_jerk_v146_signal(closeadj, volume):
    base = _mean(_f039_effort_result_ratio(closeadj, volume, 189), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrsm_252d_jerk_v147_signal(closeadj, volume):
    base = _mean(_f039_effort_result_ratio(closeadj, volume, 252), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrsm_252d_jerk_v148_signal(closeadj, volume):
    base = _mean(_f039_effort_result_ratio(closeadj, volume, 252), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrsm_252d_jerk_v149_signal(closeadj, volume):
    base = _mean(_f039_effort_result_ratio(closeadj, volume, 252), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrsm_252d_jerk_v150_signal(closeadj, volume):
    base = _mean(_f039_effort_result_ratio(closeadj, volume, 252), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f039evr_f039_effort_vs_result_pprog_10d_jerk_v001_signal,
    f039evr_f039_effort_vs_result_pprog_21d_jerk_v002_signal,
    f039evr_f039_effort_vs_result_pprog_42d_jerk_v003_signal,
    f039evr_f039_effort_vs_result_pprog_42d_jerk_v004_signal,
    f039evr_f039_effort_vs_result_pprog_42d_jerk_v005_signal,
    f039evr_f039_effort_vs_result_pprog_42d_jerk_v006_signal,
    f039evr_f039_effort_vs_result_pprog_63d_jerk_v007_signal,
    f039evr_f039_effort_vs_result_pprog_63d_jerk_v008_signal,
    f039evr_f039_effort_vs_result_pprog_63d_jerk_v009_signal,
    f039evr_f039_effort_vs_result_pprog_63d_jerk_v010_signal,
    f039evr_f039_effort_vs_result_pprog_126d_jerk_v011_signal,
    f039evr_f039_effort_vs_result_pprog_126d_jerk_v012_signal,
    f039evr_f039_effort_vs_result_pprog_126d_jerk_v013_signal,
    f039evr_f039_effort_vs_result_pprog_126d_jerk_v014_signal,
    f039evr_f039_effort_vs_result_pprog_189d_jerk_v015_signal,
    f039evr_f039_effort_vs_result_pprog_189d_jerk_v016_signal,
    f039evr_f039_effort_vs_result_pprog_189d_jerk_v017_signal,
    f039evr_f039_effort_vs_result_pprog_189d_jerk_v018_signal,
    f039evr_f039_effort_vs_result_pprog_252d_jerk_v019_signal,
    f039evr_f039_effort_vs_result_pprog_252d_jerk_v020_signal,
    f039evr_f039_effort_vs_result_pprog_252d_jerk_v021_signal,
    f039evr_f039_effort_vs_result_pprog_252d_jerk_v022_signal,
    f039evr_f039_effort_vs_result_pprog_378d_jerk_v023_signal,
    f039evr_f039_effort_vs_result_pprog_378d_jerk_v024_signal,
    f039evr_f039_effort_vs_result_pprog_378d_jerk_v025_signal,
    f039evr_f039_effort_vs_result_pprog_504d_jerk_v026_signal,
    f039evr_f039_effort_vs_result_pprog_504d_jerk_v027_signal,
    f039evr_f039_effort_vs_result_pprog_504d_jerk_v028_signal,
    f039evr_f039_effort_vs_result_pprogsm_10d_jerk_v029_signal,
    f039evr_f039_effort_vs_result_pprogsm_21d_jerk_v030_signal,
    f039evr_f039_effort_vs_result_pprogsm_42d_jerk_v031_signal,
    f039evr_f039_effort_vs_result_pprogsm_42d_jerk_v032_signal,
    f039evr_f039_effort_vs_result_pprogsm_42d_jerk_v033_signal,
    f039evr_f039_effort_vs_result_pprogsm_42d_jerk_v034_signal,
    f039evr_f039_effort_vs_result_pprogsm_63d_jerk_v035_signal,
    f039evr_f039_effort_vs_result_pprogsm_63d_jerk_v036_signal,
    f039evr_f039_effort_vs_result_pprogsm_63d_jerk_v037_signal,
    f039evr_f039_effort_vs_result_pprogsm_63d_jerk_v038_signal,
    f039evr_f039_effort_vs_result_pprogsm_126d_jerk_v039_signal,
    f039evr_f039_effort_vs_result_pprogsm_126d_jerk_v040_signal,
    f039evr_f039_effort_vs_result_pprogsm_126d_jerk_v041_signal,
    f039evr_f039_effort_vs_result_pprogsm_126d_jerk_v042_signal,
    f039evr_f039_effort_vs_result_pprogsm_189d_jerk_v043_signal,
    f039evr_f039_effort_vs_result_pprogsm_189d_jerk_v044_signal,
    f039evr_f039_effort_vs_result_pprogsm_189d_jerk_v045_signal,
    f039evr_f039_effort_vs_result_pprogsm_189d_jerk_v046_signal,
    f039evr_f039_effort_vs_result_pprogsm_252d_jerk_v047_signal,
    f039evr_f039_effort_vs_result_pprogsm_252d_jerk_v048_signal,
    f039evr_f039_effort_vs_result_pprogsm_252d_jerk_v049_signal,
    f039evr_f039_effort_vs_result_pprogsm_252d_jerk_v050_signal,
    f039evr_f039_effort_vs_result_veff_10d_jerk_v051_signal,
    f039evr_f039_effort_vs_result_veff_21d_jerk_v052_signal,
    f039evr_f039_effort_vs_result_veff_42d_jerk_v053_signal,
    f039evr_f039_effort_vs_result_veff_42d_jerk_v054_signal,
    f039evr_f039_effort_vs_result_veff_42d_jerk_v055_signal,
    f039evr_f039_effort_vs_result_veff_42d_jerk_v056_signal,
    f039evr_f039_effort_vs_result_veff_63d_jerk_v057_signal,
    f039evr_f039_effort_vs_result_veff_63d_jerk_v058_signal,
    f039evr_f039_effort_vs_result_veff_63d_jerk_v059_signal,
    f039evr_f039_effort_vs_result_veff_63d_jerk_v060_signal,
    f039evr_f039_effort_vs_result_veff_126d_jerk_v061_signal,
    f039evr_f039_effort_vs_result_veff_126d_jerk_v062_signal,
    f039evr_f039_effort_vs_result_veff_126d_jerk_v063_signal,
    f039evr_f039_effort_vs_result_veff_126d_jerk_v064_signal,
    f039evr_f039_effort_vs_result_veff_189d_jerk_v065_signal,
    f039evr_f039_effort_vs_result_veff_189d_jerk_v066_signal,
    f039evr_f039_effort_vs_result_veff_189d_jerk_v067_signal,
    f039evr_f039_effort_vs_result_veff_189d_jerk_v068_signal,
    f039evr_f039_effort_vs_result_veff_252d_jerk_v069_signal,
    f039evr_f039_effort_vs_result_veff_252d_jerk_v070_signal,
    f039evr_f039_effort_vs_result_veff_252d_jerk_v071_signal,
    f039evr_f039_effort_vs_result_veff_252d_jerk_v072_signal,
    f039evr_f039_effort_vs_result_veff_378d_jerk_v073_signal,
    f039evr_f039_effort_vs_result_veff_378d_jerk_v074_signal,
    f039evr_f039_effort_vs_result_veff_378d_jerk_v075_signal,
    f039evr_f039_effort_vs_result_veff_504d_jerk_v076_signal,
    f039evr_f039_effort_vs_result_veff_504d_jerk_v077_signal,
    f039evr_f039_effort_vs_result_veff_504d_jerk_v078_signal,
    f039evr_f039_effort_vs_result_veffsm_10d_jerk_v079_signal,
    f039evr_f039_effort_vs_result_veffsm_21d_jerk_v080_signal,
    f039evr_f039_effort_vs_result_veffsm_42d_jerk_v081_signal,
    f039evr_f039_effort_vs_result_veffsm_42d_jerk_v082_signal,
    f039evr_f039_effort_vs_result_veffsm_42d_jerk_v083_signal,
    f039evr_f039_effort_vs_result_veffsm_42d_jerk_v084_signal,
    f039evr_f039_effort_vs_result_veffsm_63d_jerk_v085_signal,
    f039evr_f039_effort_vs_result_veffsm_63d_jerk_v086_signal,
    f039evr_f039_effort_vs_result_veffsm_63d_jerk_v087_signal,
    f039evr_f039_effort_vs_result_veffsm_63d_jerk_v088_signal,
    f039evr_f039_effort_vs_result_veffsm_126d_jerk_v089_signal,
    f039evr_f039_effort_vs_result_veffsm_126d_jerk_v090_signal,
    f039evr_f039_effort_vs_result_veffsm_126d_jerk_v091_signal,
    f039evr_f039_effort_vs_result_veffsm_126d_jerk_v092_signal,
    f039evr_f039_effort_vs_result_veffsm_189d_jerk_v093_signal,
    f039evr_f039_effort_vs_result_veffsm_189d_jerk_v094_signal,
    f039evr_f039_effort_vs_result_veffsm_189d_jerk_v095_signal,
    f039evr_f039_effort_vs_result_veffsm_189d_jerk_v096_signal,
    f039evr_f039_effort_vs_result_veffsm_252d_jerk_v097_signal,
    f039evr_f039_effort_vs_result_veffsm_252d_jerk_v098_signal,
    f039evr_f039_effort_vs_result_veffsm_252d_jerk_v099_signal,
    f039evr_f039_effort_vs_result_veffsm_252d_jerk_v100_signal,
    f039evr_f039_effort_vs_result_evr_10d_jerk_v101_signal,
    f039evr_f039_effort_vs_result_evr_21d_jerk_v102_signal,
    f039evr_f039_effort_vs_result_evr_42d_jerk_v103_signal,
    f039evr_f039_effort_vs_result_evr_42d_jerk_v104_signal,
    f039evr_f039_effort_vs_result_evr_42d_jerk_v105_signal,
    f039evr_f039_effort_vs_result_evr_42d_jerk_v106_signal,
    f039evr_f039_effort_vs_result_evr_63d_jerk_v107_signal,
    f039evr_f039_effort_vs_result_evr_63d_jerk_v108_signal,
    f039evr_f039_effort_vs_result_evr_63d_jerk_v109_signal,
    f039evr_f039_effort_vs_result_evr_63d_jerk_v110_signal,
    f039evr_f039_effort_vs_result_evr_126d_jerk_v111_signal,
    f039evr_f039_effort_vs_result_evr_126d_jerk_v112_signal,
    f039evr_f039_effort_vs_result_evr_126d_jerk_v113_signal,
    f039evr_f039_effort_vs_result_evr_126d_jerk_v114_signal,
    f039evr_f039_effort_vs_result_evr_189d_jerk_v115_signal,
    f039evr_f039_effort_vs_result_evr_189d_jerk_v116_signal,
    f039evr_f039_effort_vs_result_evr_189d_jerk_v117_signal,
    f039evr_f039_effort_vs_result_evr_189d_jerk_v118_signal,
    f039evr_f039_effort_vs_result_evr_252d_jerk_v119_signal,
    f039evr_f039_effort_vs_result_evr_252d_jerk_v120_signal,
    f039evr_f039_effort_vs_result_evr_252d_jerk_v121_signal,
    f039evr_f039_effort_vs_result_evr_252d_jerk_v122_signal,
    f039evr_f039_effort_vs_result_evr_378d_jerk_v123_signal,
    f039evr_f039_effort_vs_result_evr_378d_jerk_v124_signal,
    f039evr_f039_effort_vs_result_evr_378d_jerk_v125_signal,
    f039evr_f039_effort_vs_result_evr_504d_jerk_v126_signal,
    f039evr_f039_effort_vs_result_evr_504d_jerk_v127_signal,
    f039evr_f039_effort_vs_result_evr_504d_jerk_v128_signal,
    f039evr_f039_effort_vs_result_evrsm_10d_jerk_v129_signal,
    f039evr_f039_effort_vs_result_evrsm_21d_jerk_v130_signal,
    f039evr_f039_effort_vs_result_evrsm_42d_jerk_v131_signal,
    f039evr_f039_effort_vs_result_evrsm_42d_jerk_v132_signal,
    f039evr_f039_effort_vs_result_evrsm_42d_jerk_v133_signal,
    f039evr_f039_effort_vs_result_evrsm_42d_jerk_v134_signal,
    f039evr_f039_effort_vs_result_evrsm_63d_jerk_v135_signal,
    f039evr_f039_effort_vs_result_evrsm_63d_jerk_v136_signal,
    f039evr_f039_effort_vs_result_evrsm_63d_jerk_v137_signal,
    f039evr_f039_effort_vs_result_evrsm_63d_jerk_v138_signal,
    f039evr_f039_effort_vs_result_evrsm_126d_jerk_v139_signal,
    f039evr_f039_effort_vs_result_evrsm_126d_jerk_v140_signal,
    f039evr_f039_effort_vs_result_evrsm_126d_jerk_v141_signal,
    f039evr_f039_effort_vs_result_evrsm_126d_jerk_v142_signal,
    f039evr_f039_effort_vs_result_evrsm_189d_jerk_v143_signal,
    f039evr_f039_effort_vs_result_evrsm_189d_jerk_v144_signal,
    f039evr_f039_effort_vs_result_evrsm_189d_jerk_v145_signal,
    f039evr_f039_effort_vs_result_evrsm_189d_jerk_v146_signal,
    f039evr_f039_effort_vs_result_evrsm_252d_jerk_v147_signal,
    f039evr_f039_effort_vs_result_evrsm_252d_jerk_v148_signal,
    f039evr_f039_effort_vs_result_evrsm_252d_jerk_v149_signal,
    f039evr_f039_effort_vs_result_evrsm_252d_jerk_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F039_EFFORT_VS_RESULT_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f039_price_progress", "_f039_volume_effort", "_f039_effort_result_ratio")
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
    print(f"OK f039_effort_vs_result_3rd_derivatives_001_150_claude: {n_features} features pass")
