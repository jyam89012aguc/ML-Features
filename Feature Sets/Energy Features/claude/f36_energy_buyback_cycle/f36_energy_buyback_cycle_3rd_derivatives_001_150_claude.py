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


def _f36_share_change(s, w):
    return (s.shift(0) - s.shift(w)) / s.abs().rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)



def _f36_buyback_intensity(s, close, w):
    delta = -(s - s.shift(w))
    base = s.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    return (delta / base) * close



def _f36_buyback_timing(s, close, w):
    delta = -(s - s.shift(w))
    base = s.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    pmean = close.rolling(w, min_periods=max(1, w // 2)).mean()
    return (delta / base) * (pmean - close)


# ===== features =====


def f36ebc_f36_energy_buyback_cycle_share_change_idxclose_5d_5d_jerk_v001_signal(sharesbas, closeadj):
    base = (_f36_share_change(sharesbas, 5)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_idxclose2_5d_10d_jerk_v002_signal(sharesbas, closeadj):
    base = (_f36_share_change(sharesbas, 5)) * closeadj * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_idxclosem_5d_21d_jerk_v003_signal(sharesbas, closeadj):
    base = (_f36_share_change(sharesbas, 5)) * _mean(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_idxclosem63_5d_42d_jerk_v004_signal(sharesbas, closeadj):
    base = (_f36_share_change(sharesbas, 5)) * _mean(closeadj, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_idxclosez_5d_63d_jerk_v005_signal(sharesbas, closeadj):
    base = (_f36_share_change(sharesbas, 5)) * _z(closeadj, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_idxclosechg_5d_126d_jerk_v006_signal(sharesbas, closeadj):
    base = (_f36_share_change(sharesbas, 5)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_idxclosediff_5d_189d_jerk_v007_signal(sharesbas, closeadj):
    base = (_f36_share_change(sharesbas, 5)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_meanxclose_5d_252d_jerk_v008_signal(sharesbas, closeadj):
    base = (_mean(_f36_share_change(sharesbas, 5), 5)) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_meanxclose2_5d_5d_jerk_v009_signal(sharesbas, closeadj):
    base = (_mean(_f36_share_change(sharesbas, 5), 5)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_meanxclosem_5d_10d_jerk_v010_signal(sharesbas, closeadj):
    base = (_mean(_f36_share_change(sharesbas, 5), 5)) * _mean(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_meanxclosem63_5d_21d_jerk_v011_signal(sharesbas, closeadj):
    base = (_mean(_f36_share_change(sharesbas, 5), 5)) * _mean(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_meanxclosez_5d_42d_jerk_v012_signal(sharesbas, closeadj):
    base = (_mean(_f36_share_change(sharesbas, 5), 5)) * _z(closeadj, 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_meanxclosechg_5d_63d_jerk_v013_signal(sharesbas, closeadj):
    base = (_mean(_f36_share_change(sharesbas, 5), 5)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_meanxclosediff_5d_126d_jerk_v014_signal(sharesbas, closeadj):
    base = (_mean(_f36_share_change(sharesbas, 5), 5)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_stdxclose_5d_189d_jerk_v015_signal(sharesbas, closeadj):
    base = (_std(_f36_share_change(sharesbas, 5), 5)) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_stdxclose2_5d_252d_jerk_v016_signal(sharesbas, closeadj):
    base = (_std(_f36_share_change(sharesbas, 5), 5)) * closeadj * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_stdxclosem_5d_5d_jerk_v017_signal(sharesbas, closeadj):
    base = (_std(_f36_share_change(sharesbas, 5), 5)) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_stdxclosem63_5d_10d_jerk_v018_signal(sharesbas, closeadj):
    base = (_std(_f36_share_change(sharesbas, 5), 5)) * _mean(closeadj, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_stdxclosez_5d_21d_jerk_v019_signal(sharesbas, closeadj):
    base = (_std(_f36_share_change(sharesbas, 5), 5)) * _z(closeadj, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_stdxclosechg_5d_42d_jerk_v020_signal(sharesbas, closeadj):
    base = (_std(_f36_share_change(sharesbas, 5), 5)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_stdxclosediff_5d_63d_jerk_v021_signal(sharesbas, closeadj):
    base = (_std(_f36_share_change(sharesbas, 5), 5)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_zxclose_5d_126d_jerk_v022_signal(sharesbas, closeadj):
    base = (_z(_f36_share_change(sharesbas, 5), 5)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_zxclose2_5d_189d_jerk_v023_signal(sharesbas, closeadj):
    base = (_z(_f36_share_change(sharesbas, 5), 5)) * closeadj * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_zxclosem_5d_252d_jerk_v024_signal(sharesbas, closeadj):
    base = (_z(_f36_share_change(sharesbas, 5), 5)) * _mean(closeadj, 21)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_zxclosem63_5d_5d_jerk_v025_signal(sharesbas, closeadj):
    base = (_z(_f36_share_change(sharesbas, 5), 5)) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_zxclosez_5d_10d_jerk_v026_signal(sharesbas, closeadj):
    base = (_z(_f36_share_change(sharesbas, 5), 5)) * _z(closeadj, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_zxclosechg_5d_21d_jerk_v027_signal(sharesbas, closeadj):
    base = (_z(_f36_share_change(sharesbas, 5), 5)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_zxclosediff_5d_42d_jerk_v028_signal(sharesbas, closeadj):
    base = (_z(_f36_share_change(sharesbas, 5), 5)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_emaxclose_5d_63d_jerk_v029_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_emaxclose2_5d_126d_jerk_v030_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * closeadj * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_emaxclosem_5d_189d_jerk_v031_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * _mean(closeadj, 21)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_emaxclosem63_5d_252d_jerk_v032_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * _mean(closeadj, 63)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_emaxclosez_5d_5d_jerk_v033_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * _z(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_emaxclosechg_5d_10d_jerk_v034_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_emaxclosediff_5d_21d_jerk_v035_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclose_5d_42d_jerk_v036_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclose2_5d_63d_jerk_v037_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclosem_5d_126d_jerk_v038_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * _mean(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclosem63_5d_189d_jerk_v039_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * _mean(closeadj, 63)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclosez_5d_252d_jerk_v040_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * _z(closeadj, 252)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclosechg_5d_5d_jerk_v041_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclosediff_5d_10d_jerk_v042_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclose_5d_21d_jerk_v043_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclose2_5d_42d_jerk_v044_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclosem_5d_63d_jerk_v045_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * _mean(closeadj, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclosem63_5d_126d_jerk_v046_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * _mean(closeadj, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclosez_5d_189d_jerk_v047_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * _z(closeadj, 252)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclosechg_5d_252d_jerk_v048_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclosediff_5d_5d_jerk_v049_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rminxclose_5d_10d_jerk_v050_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rminxclose2_5d_21d_jerk_v051_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rminxclosem_5d_42d_jerk_v052_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _mean(closeadj, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rminxclosem63_5d_63d_jerk_v053_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _mean(closeadj, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rminxclosez_5d_126d_jerk_v054_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _z(closeadj, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rminxclosechg_5d_189d_jerk_v055_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rminxclosediff_5d_252d_jerk_v056_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_skewxclose_5d_5d_jerk_v057_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_skewxclose2_5d_10d_jerk_v058_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * closeadj * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_skewxclosem_5d_21d_jerk_v059_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * _mean(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_skewxclosem63_5d_42d_jerk_v060_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * _mean(closeadj, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_skewxclosez_5d_63d_jerk_v061_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * _z(closeadj, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_skewxclosechg_5d_126d_jerk_v062_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_skewxclosediff_5d_189d_jerk_v063_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_kurtxclose_5d_252d_jerk_v064_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_kurtxclose2_5d_5d_jerk_v065_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_kurtxclosem_5d_10d_jerk_v066_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * _mean(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_kurtxclosem63_5d_21d_jerk_v067_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * _mean(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_kurtxclosez_5d_42d_jerk_v068_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * _z(closeadj, 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_kurtxclosechg_5d_63d_jerk_v069_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_kurtxclosediff_5d_126d_jerk_v070_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_qhixclose_5d_189d_jerk_v071_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_qhixclose2_5d_252d_jerk_v072_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * closeadj * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_qhixclosem_5d_5d_jerk_v073_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_qhixclosem63_5d_10d_jerk_v074_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * _mean(closeadj, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_qhixclosez_5d_21d_jerk_v075_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * _z(closeadj, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_qhixclosechg_5d_42d_jerk_v076_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_qhixclosediff_5d_63d_jerk_v077_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_qloxclose_5d_126d_jerk_v078_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_qloxclose2_5d_189d_jerk_v079_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * closeadj * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_qloxclosem_5d_252d_jerk_v080_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * _mean(closeadj, 21)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_qloxclosem63_5d_5d_jerk_v081_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_qloxclosez_5d_10d_jerk_v082_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * _z(closeadj, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_qloxclosechg_5d_21d_jerk_v083_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_qloxclosediff_5d_42d_jerk_v084_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rangexclose_5d_63d_jerk_v085_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rangexclose2_5d_126d_jerk_v086_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rangexclosem_5d_189d_jerk_v087_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _mean(closeadj, 21)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rangexclosem63_5d_252d_jerk_v088_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _mean(closeadj, 63)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rangexclosez_5d_5d_jerk_v089_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _z(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rangexclosechg_5d_10d_jerk_v090_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rangexclosediff_5d_21d_jerk_v091_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f36_share_change(sharesbas, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_squaredxclose_5d_42d_jerk_v092_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)) * (_f36_share_change(sharesbas, 5)).abs()) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_squaredxclose2_5d_63d_jerk_v093_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)) * (_f36_share_change(sharesbas, 5)).abs()) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_squaredxclosem_5d_126d_jerk_v094_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)) * (_f36_share_change(sharesbas, 5)).abs()) * _mean(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_squaredxclosem63_5d_189d_jerk_v095_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)) * (_f36_share_change(sharesbas, 5)).abs()) * _mean(closeadj, 63)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_squaredxclosez_5d_252d_jerk_v096_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)) * (_f36_share_change(sharesbas, 5)).abs()) * _z(closeadj, 252)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_squaredxclosechg_5d_5d_jerk_v097_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)) * (_f36_share_change(sharesbas, 5)).abs()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_squaredxclosediff_5d_10d_jerk_v098_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)) * (_f36_share_change(sharesbas, 5)).abs()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_diffxclose_5d_21d_jerk_v099_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)) - (_f36_share_change(sharesbas, 5)).shift(5)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_diffxclose2_5d_42d_jerk_v100_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)) - (_f36_share_change(sharesbas, 5)).shift(5)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_diffxclosem_5d_63d_jerk_v101_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)) - (_f36_share_change(sharesbas, 5)).shift(5)) * _mean(closeadj, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_diffxclosem63_5d_126d_jerk_v102_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)) - (_f36_share_change(sharesbas, 5)).shift(5)) * _mean(closeadj, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_diffxclosez_5d_189d_jerk_v103_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)) - (_f36_share_change(sharesbas, 5)).shift(5)) * _z(closeadj, 252)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_diffxclosechg_5d_252d_jerk_v104_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)) - (_f36_share_change(sharesbas, 5)).shift(5)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_diffxclosediff_5d_5d_jerk_v105_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)) - (_f36_share_change(sharesbas, 5)).shift(5)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_pctxclose_5d_10d_jerk_v106_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).pct_change(5)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_pctxclose2_5d_21d_jerk_v107_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).pct_change(5)) * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_pctxclosem_5d_42d_jerk_v108_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).pct_change(5)) * _mean(closeadj, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_pctxclosem63_5d_63d_jerk_v109_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).pct_change(5)) * _mean(closeadj, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_pctxclosez_5d_126d_jerk_v110_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).pct_change(5)) * _z(closeadj, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_pctxclosechg_5d_189d_jerk_v111_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).pct_change(5)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_pctxclosediff_5d_252d_jerk_v112_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).pct_change(5)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_signxclose_5d_5d_jerk_v113_signal(sharesbas, closeadj):
    base = (np.sign(_f36_share_change(sharesbas, 5))) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_signxclose2_5d_10d_jerk_v114_signal(sharesbas, closeadj):
    base = (np.sign(_f36_share_change(sharesbas, 5))) * closeadj * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_signxclosem_5d_21d_jerk_v115_signal(sharesbas, closeadj):
    base = (np.sign(_f36_share_change(sharesbas, 5))) * _mean(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_signxclosem63_5d_42d_jerk_v116_signal(sharesbas, closeadj):
    base = (np.sign(_f36_share_change(sharesbas, 5))) * _mean(closeadj, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_signxclosez_5d_63d_jerk_v117_signal(sharesbas, closeadj):
    base = (np.sign(_f36_share_change(sharesbas, 5))) * _z(closeadj, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_signxclosechg_5d_126d_jerk_v118_signal(sharesbas, closeadj):
    base = (np.sign(_f36_share_change(sharesbas, 5))) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_signxclosediff_5d_189d_jerk_v119_signal(sharesbas, closeadj):
    base = (np.sign(_f36_share_change(sharesbas, 5))) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_absxclose_5d_252d_jerk_v120_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).abs()) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_absxclose2_5d_5d_jerk_v121_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).abs()) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_absxclosem_5d_10d_jerk_v122_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).abs()) * _mean(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_absxclosem63_5d_21d_jerk_v123_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).abs()) * _mean(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_absxclosez_5d_42d_jerk_v124_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).abs()) * _z(closeadj, 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_absxclosechg_5d_63d_jerk_v125_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).abs()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_absxclosediff_5d_126d_jerk_v126_signal(sharesbas, closeadj):
    base = ((_f36_share_change(sharesbas, 5)).abs()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_idxclose_10d_189d_jerk_v127_signal(sharesbas, closeadj):
    base = (_f36_share_change(sharesbas, 10)) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_idxclose2_10d_252d_jerk_v128_signal(sharesbas, closeadj):
    base = (_f36_share_change(sharesbas, 10)) * closeadj * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_idxclosem_10d_5d_jerk_v129_signal(sharesbas, closeadj):
    base = (_f36_share_change(sharesbas, 10)) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_idxclosem63_10d_10d_jerk_v130_signal(sharesbas, closeadj):
    base = (_f36_share_change(sharesbas, 10)) * _mean(closeadj, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_idxclosez_10d_21d_jerk_v131_signal(sharesbas, closeadj):
    base = (_f36_share_change(sharesbas, 10)) * _z(closeadj, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_idxclosechg_10d_42d_jerk_v132_signal(sharesbas, closeadj):
    base = (_f36_share_change(sharesbas, 10)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_idxclosediff_10d_63d_jerk_v133_signal(sharesbas, closeadj):
    base = (_f36_share_change(sharesbas, 10)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_meanxclose_10d_126d_jerk_v134_signal(sharesbas, closeadj):
    base = (_mean(_f36_share_change(sharesbas, 10), 10)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_meanxclose2_10d_189d_jerk_v135_signal(sharesbas, closeadj):
    base = (_mean(_f36_share_change(sharesbas, 10), 10)) * closeadj * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_meanxclosem_10d_252d_jerk_v136_signal(sharesbas, closeadj):
    base = (_mean(_f36_share_change(sharesbas, 10), 10)) * _mean(closeadj, 21)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_meanxclosem63_10d_5d_jerk_v137_signal(sharesbas, closeadj):
    base = (_mean(_f36_share_change(sharesbas, 10), 10)) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_meanxclosez_10d_10d_jerk_v138_signal(sharesbas, closeadj):
    base = (_mean(_f36_share_change(sharesbas, 10), 10)) * _z(closeadj, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_meanxclosechg_10d_21d_jerk_v139_signal(sharesbas, closeadj):
    base = (_mean(_f36_share_change(sharesbas, 10), 10)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_meanxclosediff_10d_42d_jerk_v140_signal(sharesbas, closeadj):
    base = (_mean(_f36_share_change(sharesbas, 10), 10)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_stdxclose_10d_63d_jerk_v141_signal(sharesbas, closeadj):
    base = (_std(_f36_share_change(sharesbas, 10), 10)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_stdxclose2_10d_126d_jerk_v142_signal(sharesbas, closeadj):
    base = (_std(_f36_share_change(sharesbas, 10), 10)) * closeadj * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_stdxclosem_10d_189d_jerk_v143_signal(sharesbas, closeadj):
    base = (_std(_f36_share_change(sharesbas, 10), 10)) * _mean(closeadj, 21)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_stdxclosem63_10d_252d_jerk_v144_signal(sharesbas, closeadj):
    base = (_std(_f36_share_change(sharesbas, 10), 10)) * _mean(closeadj, 63)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_stdxclosez_10d_5d_jerk_v145_signal(sharesbas, closeadj):
    base = (_std(_f36_share_change(sharesbas, 10), 10)) * _z(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_stdxclosechg_10d_10d_jerk_v146_signal(sharesbas, closeadj):
    base = (_std(_f36_share_change(sharesbas, 10), 10)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_stdxclosediff_10d_21d_jerk_v147_signal(sharesbas, closeadj):
    base = (_std(_f36_share_change(sharesbas, 10), 10)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_zxclose_10d_42d_jerk_v148_signal(sharesbas, closeadj):
    base = (_z(_f36_share_change(sharesbas, 10), 10)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_zxclose2_10d_63d_jerk_v149_signal(sharesbas, closeadj):
    base = (_z(_f36_share_change(sharesbas, 10), 10)) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_zxclosem_10d_126d_jerk_v150_signal(sharesbas, closeadj):
    base = (_z(_f36_share_change(sharesbas, 10), 10)) * _mean(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f36ebc_f36_energy_buyback_cycle_share_change_idxclose_5d_5d_jerk_v001_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_idxclose2_5d_10d_jerk_v002_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_idxclosem_5d_21d_jerk_v003_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_idxclosem63_5d_42d_jerk_v004_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_idxclosez_5d_63d_jerk_v005_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_idxclosechg_5d_126d_jerk_v006_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_idxclosediff_5d_189d_jerk_v007_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_meanxclose_5d_252d_jerk_v008_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_meanxclose2_5d_5d_jerk_v009_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_meanxclosem_5d_10d_jerk_v010_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_meanxclosem63_5d_21d_jerk_v011_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_meanxclosez_5d_42d_jerk_v012_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_meanxclosechg_5d_63d_jerk_v013_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_meanxclosediff_5d_126d_jerk_v014_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_stdxclose_5d_189d_jerk_v015_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_stdxclose2_5d_252d_jerk_v016_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_stdxclosem_5d_5d_jerk_v017_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_stdxclosem63_5d_10d_jerk_v018_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_stdxclosez_5d_21d_jerk_v019_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_stdxclosechg_5d_42d_jerk_v020_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_stdxclosediff_5d_63d_jerk_v021_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_zxclose_5d_126d_jerk_v022_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_zxclose2_5d_189d_jerk_v023_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_zxclosem_5d_252d_jerk_v024_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_zxclosem63_5d_5d_jerk_v025_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_zxclosez_5d_10d_jerk_v026_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_zxclosechg_5d_21d_jerk_v027_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_zxclosediff_5d_42d_jerk_v028_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_emaxclose_5d_63d_jerk_v029_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_emaxclose2_5d_126d_jerk_v030_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_emaxclosem_5d_189d_jerk_v031_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_emaxclosem63_5d_252d_jerk_v032_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_emaxclosez_5d_5d_jerk_v033_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_emaxclosechg_5d_10d_jerk_v034_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_emaxclosediff_5d_21d_jerk_v035_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclose_5d_42d_jerk_v036_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclose2_5d_63d_jerk_v037_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclosem_5d_126d_jerk_v038_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclosem63_5d_189d_jerk_v039_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclosez_5d_252d_jerk_v040_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclosechg_5d_5d_jerk_v041_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclosediff_5d_10d_jerk_v042_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclose_5d_21d_jerk_v043_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclose2_5d_42d_jerk_v044_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclosem_5d_63d_jerk_v045_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclosem63_5d_126d_jerk_v046_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclosez_5d_189d_jerk_v047_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclosechg_5d_252d_jerk_v048_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclosediff_5d_5d_jerk_v049_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rminxclose_5d_10d_jerk_v050_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rminxclose2_5d_21d_jerk_v051_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rminxclosem_5d_42d_jerk_v052_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rminxclosem63_5d_63d_jerk_v053_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rminxclosez_5d_126d_jerk_v054_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rminxclosechg_5d_189d_jerk_v055_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rminxclosediff_5d_252d_jerk_v056_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_skewxclose_5d_5d_jerk_v057_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_skewxclose2_5d_10d_jerk_v058_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_skewxclosem_5d_21d_jerk_v059_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_skewxclosem63_5d_42d_jerk_v060_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_skewxclosez_5d_63d_jerk_v061_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_skewxclosechg_5d_126d_jerk_v062_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_skewxclosediff_5d_189d_jerk_v063_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_kurtxclose_5d_252d_jerk_v064_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_kurtxclose2_5d_5d_jerk_v065_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_kurtxclosem_5d_10d_jerk_v066_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_kurtxclosem63_5d_21d_jerk_v067_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_kurtxclosez_5d_42d_jerk_v068_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_kurtxclosechg_5d_63d_jerk_v069_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_kurtxclosediff_5d_126d_jerk_v070_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_qhixclose_5d_189d_jerk_v071_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_qhixclose2_5d_252d_jerk_v072_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_qhixclosem_5d_5d_jerk_v073_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_qhixclosem63_5d_10d_jerk_v074_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_qhixclosez_5d_21d_jerk_v075_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_qhixclosechg_5d_42d_jerk_v076_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_qhixclosediff_5d_63d_jerk_v077_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_qloxclose_5d_126d_jerk_v078_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_qloxclose2_5d_189d_jerk_v079_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_qloxclosem_5d_252d_jerk_v080_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_qloxclosem63_5d_5d_jerk_v081_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_qloxclosez_5d_10d_jerk_v082_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_qloxclosechg_5d_21d_jerk_v083_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_qloxclosediff_5d_42d_jerk_v084_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rangexclose_5d_63d_jerk_v085_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rangexclose2_5d_126d_jerk_v086_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rangexclosem_5d_189d_jerk_v087_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rangexclosem63_5d_252d_jerk_v088_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rangexclosez_5d_5d_jerk_v089_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rangexclosechg_5d_10d_jerk_v090_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rangexclosediff_5d_21d_jerk_v091_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_squaredxclose_5d_42d_jerk_v092_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_squaredxclose2_5d_63d_jerk_v093_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_squaredxclosem_5d_126d_jerk_v094_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_squaredxclosem63_5d_189d_jerk_v095_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_squaredxclosez_5d_252d_jerk_v096_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_squaredxclosechg_5d_5d_jerk_v097_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_squaredxclosediff_5d_10d_jerk_v098_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_diffxclose_5d_21d_jerk_v099_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_diffxclose2_5d_42d_jerk_v100_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_diffxclosem_5d_63d_jerk_v101_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_diffxclosem63_5d_126d_jerk_v102_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_diffxclosez_5d_189d_jerk_v103_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_diffxclosechg_5d_252d_jerk_v104_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_diffxclosediff_5d_5d_jerk_v105_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_pctxclose_5d_10d_jerk_v106_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_pctxclose2_5d_21d_jerk_v107_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_pctxclosem_5d_42d_jerk_v108_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_pctxclosem63_5d_63d_jerk_v109_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_pctxclosez_5d_126d_jerk_v110_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_pctxclosechg_5d_189d_jerk_v111_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_pctxclosediff_5d_252d_jerk_v112_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_signxclose_5d_5d_jerk_v113_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_signxclose2_5d_10d_jerk_v114_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_signxclosem_5d_21d_jerk_v115_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_signxclosem63_5d_42d_jerk_v116_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_signxclosez_5d_63d_jerk_v117_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_signxclosechg_5d_126d_jerk_v118_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_signxclosediff_5d_189d_jerk_v119_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_absxclose_5d_252d_jerk_v120_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_absxclose2_5d_5d_jerk_v121_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_absxclosem_5d_10d_jerk_v122_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_absxclosem63_5d_21d_jerk_v123_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_absxclosez_5d_42d_jerk_v124_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_absxclosechg_5d_63d_jerk_v125_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_absxclosediff_5d_126d_jerk_v126_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_idxclose_10d_189d_jerk_v127_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_idxclose2_10d_252d_jerk_v128_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_idxclosem_10d_5d_jerk_v129_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_idxclosem63_10d_10d_jerk_v130_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_idxclosez_10d_21d_jerk_v131_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_idxclosechg_10d_42d_jerk_v132_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_idxclosediff_10d_63d_jerk_v133_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_meanxclose_10d_126d_jerk_v134_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_meanxclose2_10d_189d_jerk_v135_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_meanxclosem_10d_252d_jerk_v136_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_meanxclosem63_10d_5d_jerk_v137_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_meanxclosez_10d_10d_jerk_v138_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_meanxclosechg_10d_21d_jerk_v139_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_meanxclosediff_10d_42d_jerk_v140_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_stdxclose_10d_63d_jerk_v141_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_stdxclose2_10d_126d_jerk_v142_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_stdxclosem_10d_189d_jerk_v143_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_stdxclosem63_10d_252d_jerk_v144_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_stdxclosez_10d_5d_jerk_v145_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_stdxclosechg_10d_10d_jerk_v146_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_stdxclosediff_10d_21d_jerk_v147_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_zxclose_10d_42d_jerk_v148_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_zxclose2_10d_63d_jerk_v149_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_zxclosem_10d_126d_jerk_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F36_ENERGY_BUYBACK_CYCLE_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue, "fcf": fcf, "capex": capex,
        "sharesbas": sharesbas, "shareswa": shareswa,
        "eps": eps, "fcfps": fcfps, "dps": dps,
        "payoutratio": payoutratio,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f36_share_change", "_f36_buyback_intensity", "_f36_buyback_timing",)
    import hashlib
    seen_bodies = set()
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
        body_lines = [l.strip() for l in src.splitlines()
                      if l.strip() and not l.strip().startswith("#") and not l.strip().startswith("def ")]
        body = "\n".join(body_lines)
        h = hashlib.sha1(body.encode()).hexdigest()
        assert h not in seen_bodies, f"DUP body in {name}"
        seen_bodies.add(h)
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f36_energy_buyback_cycle_3rd_derivatives_001_150_claude: {n_features} features pass")
