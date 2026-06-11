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


# ===== folder domain primitives =====


def _f40_payout_floor(payoutratio, w):
    return payoutratio.rolling(w, min_periods=max(1, w // 2)).min()



def _f40_payout_durability(payoutratio, eps, w):
    cap = 1.0 - payoutratio
    eps_g = eps.pct_change(periods=w).fillna(0.0)
    return cap.rolling(w, min_periods=max(1, w // 2)).mean() + eps_g



def _f40_payout_sustainability(payoutratio, fcfps, w):
    cover = fcfps / payoutratio.replace(0, np.nan).abs()
    return cover.rolling(w, min_periods=max(1, w // 2)).mean()


# ===== features =====


def f40epd_f40_energy_payout_durability_payout_floor_idxclose_5d_5d_slope_v001_signal(payoutratio, closeadj):
    base = (_f40_payout_floor(payoutratio, 5)) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_idxclose2_5d_10d_slope_v002_signal(payoutratio, closeadj):
    base = (_f40_payout_floor(payoutratio, 5)) * closeadj * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_idxclosem_5d_21d_slope_v003_signal(payoutratio, closeadj):
    base = (_f40_payout_floor(payoutratio, 5)) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_idxclosem63_5d_42d_slope_v004_signal(payoutratio, closeadj):
    base = (_f40_payout_floor(payoutratio, 5)) * _mean(closeadj, 63)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_idxclosez_5d_63d_slope_v005_signal(payoutratio, closeadj):
    base = (_f40_payout_floor(payoutratio, 5)) * _z(closeadj, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_idxclosechg_5d_126d_slope_v006_signal(payoutratio, closeadj):
    base = (_f40_payout_floor(payoutratio, 5)) * closeadj.pct_change(21).fillna(0.0)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_idxclosediff_5d_189d_slope_v007_signal(payoutratio, closeadj):
    base = (_f40_payout_floor(payoutratio, 5)) * (closeadj - _mean(closeadj, 63))
    result = _slope_diff_norm(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_meanxclose_5d_252d_slope_v008_signal(payoutratio, closeadj):
    base = (_mean(_f40_payout_floor(payoutratio, 5), 5)) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_meanxclose2_5d_5d_slope_v009_signal(payoutratio, closeadj):
    base = (_mean(_f40_payout_floor(payoutratio, 5), 5)) * closeadj * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_meanxclosem_5d_10d_slope_v010_signal(payoutratio, closeadj):
    base = (_mean(_f40_payout_floor(payoutratio, 5), 5)) * _mean(closeadj, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_meanxclosem63_5d_21d_slope_v011_signal(payoutratio, closeadj):
    base = (_mean(_f40_payout_floor(payoutratio, 5), 5)) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_meanxclosez_5d_42d_slope_v012_signal(payoutratio, closeadj):
    base = (_mean(_f40_payout_floor(payoutratio, 5), 5)) * _z(closeadj, 252)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_meanxclosechg_5d_63d_slope_v013_signal(payoutratio, closeadj):
    base = (_mean(_f40_payout_floor(payoutratio, 5), 5)) * closeadj.pct_change(21).fillna(0.0)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_meanxclosediff_5d_126d_slope_v014_signal(payoutratio, closeadj):
    base = (_mean(_f40_payout_floor(payoutratio, 5), 5)) * (closeadj - _mean(closeadj, 63))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_stdxclose_5d_189d_slope_v015_signal(payoutratio, closeadj):
    base = (_std(_f40_payout_floor(payoutratio, 5), 5)) * closeadj
    result = _slope_diff_norm(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_stdxclose2_5d_252d_slope_v016_signal(payoutratio, closeadj):
    base = (_std(_f40_payout_floor(payoutratio, 5), 5)) * closeadj * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_stdxclosem_5d_5d_slope_v017_signal(payoutratio, closeadj):
    base = (_std(_f40_payout_floor(payoutratio, 5), 5)) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_stdxclosem63_5d_10d_slope_v018_signal(payoutratio, closeadj):
    base = (_std(_f40_payout_floor(payoutratio, 5), 5)) * _mean(closeadj, 63)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_stdxclosez_5d_21d_slope_v019_signal(payoutratio, closeadj):
    base = (_std(_f40_payout_floor(payoutratio, 5), 5)) * _z(closeadj, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_stdxclosechg_5d_42d_slope_v020_signal(payoutratio, closeadj):
    base = (_std(_f40_payout_floor(payoutratio, 5), 5)) * closeadj.pct_change(21).fillna(0.0)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_stdxclosediff_5d_63d_slope_v021_signal(payoutratio, closeadj):
    base = (_std(_f40_payout_floor(payoutratio, 5), 5)) * (closeadj - _mean(closeadj, 63))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_zxclose_5d_126d_slope_v022_signal(payoutratio, closeadj):
    base = (_z(_f40_payout_floor(payoutratio, 5), 5)) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_zxclose2_5d_189d_slope_v023_signal(payoutratio, closeadj):
    base = (_z(_f40_payout_floor(payoutratio, 5), 5)) * closeadj * closeadj
    result = _slope_diff_norm(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_zxclosem_5d_252d_slope_v024_signal(payoutratio, closeadj):
    base = (_z(_f40_payout_floor(payoutratio, 5), 5)) * _mean(closeadj, 21)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_zxclosem63_5d_5d_slope_v025_signal(payoutratio, closeadj):
    base = (_z(_f40_payout_floor(payoutratio, 5), 5)) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_zxclosez_5d_10d_slope_v026_signal(payoutratio, closeadj):
    base = (_z(_f40_payout_floor(payoutratio, 5), 5)) * _z(closeadj, 252)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_zxclosechg_5d_21d_slope_v027_signal(payoutratio, closeadj):
    base = (_z(_f40_payout_floor(payoutratio, 5), 5)) * closeadj.pct_change(21).fillna(0.0)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_zxclosediff_5d_42d_slope_v028_signal(payoutratio, closeadj):
    base = (_z(_f40_payout_floor(payoutratio, 5), 5)) * (closeadj - _mean(closeadj, 63))
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_emaxclose_5d_63d_slope_v029_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_emaxclose2_5d_126d_slope_v030_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * closeadj * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_emaxclosem_5d_189d_slope_v031_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_emaxclosem63_5d_252d_slope_v032_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * _mean(closeadj, 63)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_emaxclosez_5d_5d_slope_v033_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * _z(closeadj, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_emaxclosechg_5d_10d_slope_v034_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * closeadj.pct_change(21).fillna(0.0)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_emaxclosediff_5d_21d_slope_v035_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * (closeadj - _mean(closeadj, 63))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmedianxclose_5d_42d_slope_v036_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmedianxclose2_5d_63d_slope_v037_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * closeadj * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmedianxclosem_5d_126d_slope_v038_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * _mean(closeadj, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmedianxclosem63_5d_189d_slope_v039_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmedianxclosez_5d_252d_slope_v040_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * _z(closeadj, 252)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmedianxclosechg_5d_5d_slope_v041_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * closeadj.pct_change(21).fillna(0.0)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmedianxclosediff_5d_10d_slope_v042_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * (closeadj - _mean(closeadj, 63))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmaxxclose_5d_21d_slope_v043_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmaxxclose2_5d_42d_slope_v044_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * closeadj * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmaxxclosem_5d_63d_slope_v045_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmaxxclosem63_5d_126d_slope_v046_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * _mean(closeadj, 63)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmaxxclosez_5d_189d_slope_v047_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * _z(closeadj, 252)
    result = _slope_diff_norm(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmaxxclosechg_5d_252d_slope_v048_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * closeadj.pct_change(21).fillna(0.0)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmaxxclosediff_5d_5d_slope_v049_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * (closeadj - _mean(closeadj, 63))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rminxclose_5d_10d_slope_v050_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rminxclose2_5d_21d_slope_v051_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rminxclosem_5d_42d_slope_v052_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _mean(closeadj, 21)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rminxclosem63_5d_63d_slope_v053_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rminxclosez_5d_126d_slope_v054_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _z(closeadj, 252)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rminxclosechg_5d_189d_slope_v055_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj.pct_change(21).fillna(0.0)
    result = _slope_diff_norm(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rminxclosediff_5d_252d_slope_v056_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * (closeadj - _mean(closeadj, 63))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_skewxclose_5d_5d_slope_v057_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_skewxclose2_5d_10d_slope_v058_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * closeadj * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_skewxclosem_5d_21d_slope_v059_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_skewxclosem63_5d_42d_slope_v060_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * _mean(closeadj, 63)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_skewxclosez_5d_63d_slope_v061_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * _z(closeadj, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_skewxclosechg_5d_126d_slope_v062_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * closeadj.pct_change(21).fillna(0.0)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_skewxclosediff_5d_189d_slope_v063_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * (closeadj - _mean(closeadj, 63))
    result = _slope_diff_norm(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_kurtxclose_5d_252d_slope_v064_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_kurtxclose2_5d_5d_slope_v065_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * closeadj * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_kurtxclosem_5d_10d_slope_v066_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * _mean(closeadj, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_kurtxclosem63_5d_21d_slope_v067_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_kurtxclosez_5d_42d_slope_v068_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * _z(closeadj, 252)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_kurtxclosechg_5d_63d_slope_v069_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * closeadj.pct_change(21).fillna(0.0)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_kurtxclosediff_5d_126d_slope_v070_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * (closeadj - _mean(closeadj, 63))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_qhixclose_5d_189d_slope_v071_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * closeadj
    result = _slope_diff_norm(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_qhixclose2_5d_252d_slope_v072_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * closeadj * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_qhixclosem_5d_5d_slope_v073_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_qhixclosem63_5d_10d_slope_v074_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * _mean(closeadj, 63)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_qhixclosez_5d_21d_slope_v075_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * _z(closeadj, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_qhixclosechg_5d_42d_slope_v076_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * closeadj.pct_change(21).fillna(0.0)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_qhixclosediff_5d_63d_slope_v077_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * (closeadj - _mean(closeadj, 63))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_qloxclose_5d_126d_slope_v078_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_qloxclose2_5d_189d_slope_v079_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * closeadj * closeadj
    result = _slope_diff_norm(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_qloxclosem_5d_252d_slope_v080_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * _mean(closeadj, 21)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_qloxclosem63_5d_5d_slope_v081_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_qloxclosez_5d_10d_slope_v082_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * _z(closeadj, 252)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_qloxclosechg_5d_21d_slope_v083_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * closeadj.pct_change(21).fillna(0.0)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_qloxclosediff_5d_42d_slope_v084_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * (closeadj - _mean(closeadj, 63))
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rangexclose_5d_63d_slope_v085_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rangexclose2_5d_126d_slope_v086_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rangexclosem_5d_189d_slope_v087_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rangexclosem63_5d_252d_slope_v088_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _mean(closeadj, 63)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rangexclosez_5d_5d_slope_v089_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _z(closeadj, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rangexclosechg_5d_10d_slope_v090_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj.pct_change(21).fillna(0.0)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rangexclosediff_5d_21d_slope_v091_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f40_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * (closeadj - _mean(closeadj, 63))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_squaredxclose_5d_42d_slope_v092_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)) * (_f40_payout_floor(payoutratio, 5)).abs()) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_squaredxclose2_5d_63d_slope_v093_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)) * (_f40_payout_floor(payoutratio, 5)).abs()) * closeadj * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_squaredxclosem_5d_126d_slope_v094_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)) * (_f40_payout_floor(payoutratio, 5)).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_squaredxclosem63_5d_189d_slope_v095_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)) * (_f40_payout_floor(payoutratio, 5)).abs()) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_squaredxclosez_5d_252d_slope_v096_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)) * (_f40_payout_floor(payoutratio, 5)).abs()) * _z(closeadj, 252)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_squaredxclosechg_5d_5d_slope_v097_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)) * (_f40_payout_floor(payoutratio, 5)).abs()) * closeadj.pct_change(21).fillna(0.0)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_squaredxclosediff_5d_10d_slope_v098_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)) * (_f40_payout_floor(payoutratio, 5)).abs()) * (closeadj - _mean(closeadj, 63))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_diffxclose_5d_21d_slope_v099_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)) - (_f40_payout_floor(payoutratio, 5)).shift(5)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_diffxclose2_5d_42d_slope_v100_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)) - (_f40_payout_floor(payoutratio, 5)).shift(5)) * closeadj * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_diffxclosem_5d_63d_slope_v101_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)) - (_f40_payout_floor(payoutratio, 5)).shift(5)) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_diffxclosem63_5d_126d_slope_v102_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)) - (_f40_payout_floor(payoutratio, 5)).shift(5)) * _mean(closeadj, 63)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_diffxclosez_5d_189d_slope_v103_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)) - (_f40_payout_floor(payoutratio, 5)).shift(5)) * _z(closeadj, 252)
    result = _slope_diff_norm(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_diffxclosechg_5d_252d_slope_v104_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)) - (_f40_payout_floor(payoutratio, 5)).shift(5)) * closeadj.pct_change(21).fillna(0.0)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_diffxclosediff_5d_5d_slope_v105_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)) - (_f40_payout_floor(payoutratio, 5)).shift(5)) * (closeadj - _mean(closeadj, 63))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_pctxclose_5d_10d_slope_v106_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).pct_change(5)) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_pctxclose2_5d_21d_slope_v107_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).pct_change(5)) * closeadj * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_pctxclosem_5d_42d_slope_v108_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).pct_change(5)) * _mean(closeadj, 21)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_pctxclosem63_5d_63d_slope_v109_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).pct_change(5)) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_pctxclosez_5d_126d_slope_v110_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).pct_change(5)) * _z(closeadj, 252)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_pctxclosechg_5d_189d_slope_v111_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).pct_change(5)) * closeadj.pct_change(21).fillna(0.0)
    result = _slope_diff_norm(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_pctxclosediff_5d_252d_slope_v112_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).pct_change(5)) * (closeadj - _mean(closeadj, 63))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_signxclose_5d_5d_slope_v113_signal(payoutratio, closeadj):
    base = (np.sign(_f40_payout_floor(payoutratio, 5))) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_signxclose2_5d_10d_slope_v114_signal(payoutratio, closeadj):
    base = (np.sign(_f40_payout_floor(payoutratio, 5))) * closeadj * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_signxclosem_5d_21d_slope_v115_signal(payoutratio, closeadj):
    base = (np.sign(_f40_payout_floor(payoutratio, 5))) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_signxclosem63_5d_42d_slope_v116_signal(payoutratio, closeadj):
    base = (np.sign(_f40_payout_floor(payoutratio, 5))) * _mean(closeadj, 63)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_signxclosez_5d_63d_slope_v117_signal(payoutratio, closeadj):
    base = (np.sign(_f40_payout_floor(payoutratio, 5))) * _z(closeadj, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_signxclosechg_5d_126d_slope_v118_signal(payoutratio, closeadj):
    base = (np.sign(_f40_payout_floor(payoutratio, 5))) * closeadj.pct_change(21).fillna(0.0)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_signxclosediff_5d_189d_slope_v119_signal(payoutratio, closeadj):
    base = (np.sign(_f40_payout_floor(payoutratio, 5))) * (closeadj - _mean(closeadj, 63))
    result = _slope_diff_norm(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_absxclose_5d_252d_slope_v120_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).abs()) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_absxclose2_5d_5d_slope_v121_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).abs()) * closeadj * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_absxclosem_5d_10d_slope_v122_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_absxclosem63_5d_21d_slope_v123_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).abs()) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_absxclosez_5d_42d_slope_v124_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).abs()) * _z(closeadj, 252)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_absxclosechg_5d_63d_slope_v125_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).abs()) * closeadj.pct_change(21).fillna(0.0)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_absxclosediff_5d_126d_slope_v126_signal(payoutratio, closeadj):
    base = ((_f40_payout_floor(payoutratio, 5)).abs()) * (closeadj - _mean(closeadj, 63))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_idxclose_10d_189d_slope_v127_signal(payoutratio, closeadj):
    base = (_f40_payout_floor(payoutratio, 10)) * closeadj
    result = _slope_diff_norm(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_idxclose2_10d_252d_slope_v128_signal(payoutratio, closeadj):
    base = (_f40_payout_floor(payoutratio, 10)) * closeadj * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_idxclosem_10d_5d_slope_v129_signal(payoutratio, closeadj):
    base = (_f40_payout_floor(payoutratio, 10)) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_idxclosem63_10d_10d_slope_v130_signal(payoutratio, closeadj):
    base = (_f40_payout_floor(payoutratio, 10)) * _mean(closeadj, 63)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_idxclosez_10d_21d_slope_v131_signal(payoutratio, closeadj):
    base = (_f40_payout_floor(payoutratio, 10)) * _z(closeadj, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_idxclosechg_10d_42d_slope_v132_signal(payoutratio, closeadj):
    base = (_f40_payout_floor(payoutratio, 10)) * closeadj.pct_change(21).fillna(0.0)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_idxclosediff_10d_63d_slope_v133_signal(payoutratio, closeadj):
    base = (_f40_payout_floor(payoutratio, 10)) * (closeadj - _mean(closeadj, 63))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_meanxclose_10d_126d_slope_v134_signal(payoutratio, closeadj):
    base = (_mean(_f40_payout_floor(payoutratio, 10), 10)) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_meanxclose2_10d_189d_slope_v135_signal(payoutratio, closeadj):
    base = (_mean(_f40_payout_floor(payoutratio, 10), 10)) * closeadj * closeadj
    result = _slope_diff_norm(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_meanxclosem_10d_252d_slope_v136_signal(payoutratio, closeadj):
    base = (_mean(_f40_payout_floor(payoutratio, 10), 10)) * _mean(closeadj, 21)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_meanxclosem63_10d_5d_slope_v137_signal(payoutratio, closeadj):
    base = (_mean(_f40_payout_floor(payoutratio, 10), 10)) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_meanxclosez_10d_10d_slope_v138_signal(payoutratio, closeadj):
    base = (_mean(_f40_payout_floor(payoutratio, 10), 10)) * _z(closeadj, 252)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_meanxclosechg_10d_21d_slope_v139_signal(payoutratio, closeadj):
    base = (_mean(_f40_payout_floor(payoutratio, 10), 10)) * closeadj.pct_change(21).fillna(0.0)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_meanxclosediff_10d_42d_slope_v140_signal(payoutratio, closeadj):
    base = (_mean(_f40_payout_floor(payoutratio, 10), 10)) * (closeadj - _mean(closeadj, 63))
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_stdxclose_10d_63d_slope_v141_signal(payoutratio, closeadj):
    base = (_std(_f40_payout_floor(payoutratio, 10), 10)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_stdxclose2_10d_126d_slope_v142_signal(payoutratio, closeadj):
    base = (_std(_f40_payout_floor(payoutratio, 10), 10)) * closeadj * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_stdxclosem_10d_189d_slope_v143_signal(payoutratio, closeadj):
    base = (_std(_f40_payout_floor(payoutratio, 10), 10)) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_stdxclosem63_10d_252d_slope_v144_signal(payoutratio, closeadj):
    base = (_std(_f40_payout_floor(payoutratio, 10), 10)) * _mean(closeadj, 63)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_stdxclosez_10d_5d_slope_v145_signal(payoutratio, closeadj):
    base = (_std(_f40_payout_floor(payoutratio, 10), 10)) * _z(closeadj, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_stdxclosechg_10d_10d_slope_v146_signal(payoutratio, closeadj):
    base = (_std(_f40_payout_floor(payoutratio, 10), 10)) * closeadj.pct_change(21).fillna(0.0)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_stdxclosediff_10d_21d_slope_v147_signal(payoutratio, closeadj):
    base = (_std(_f40_payout_floor(payoutratio, 10), 10)) * (closeadj - _mean(closeadj, 63))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_zxclose_10d_42d_slope_v148_signal(payoutratio, closeadj):
    base = (_z(_f40_payout_floor(payoutratio, 10), 10)) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_zxclose2_10d_63d_slope_v149_signal(payoutratio, closeadj):
    base = (_z(_f40_payout_floor(payoutratio, 10), 10)) * closeadj * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_zxclosem_10d_126d_slope_v150_signal(payoutratio, closeadj):
    base = (_z(_f40_payout_floor(payoutratio, 10), 10)) * _mean(closeadj, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f40epd_f40_energy_payout_durability_payout_floor_idxclose_5d_5d_slope_v001_signal,
    f40epd_f40_energy_payout_durability_payout_floor_idxclose2_5d_10d_slope_v002_signal,
    f40epd_f40_energy_payout_durability_payout_floor_idxclosem_5d_21d_slope_v003_signal,
    f40epd_f40_energy_payout_durability_payout_floor_idxclosem63_5d_42d_slope_v004_signal,
    f40epd_f40_energy_payout_durability_payout_floor_idxclosez_5d_63d_slope_v005_signal,
    f40epd_f40_energy_payout_durability_payout_floor_idxclosechg_5d_126d_slope_v006_signal,
    f40epd_f40_energy_payout_durability_payout_floor_idxclosediff_5d_189d_slope_v007_signal,
    f40epd_f40_energy_payout_durability_payout_floor_meanxclose_5d_252d_slope_v008_signal,
    f40epd_f40_energy_payout_durability_payout_floor_meanxclose2_5d_5d_slope_v009_signal,
    f40epd_f40_energy_payout_durability_payout_floor_meanxclosem_5d_10d_slope_v010_signal,
    f40epd_f40_energy_payout_durability_payout_floor_meanxclosem63_5d_21d_slope_v011_signal,
    f40epd_f40_energy_payout_durability_payout_floor_meanxclosez_5d_42d_slope_v012_signal,
    f40epd_f40_energy_payout_durability_payout_floor_meanxclosechg_5d_63d_slope_v013_signal,
    f40epd_f40_energy_payout_durability_payout_floor_meanxclosediff_5d_126d_slope_v014_signal,
    f40epd_f40_energy_payout_durability_payout_floor_stdxclose_5d_189d_slope_v015_signal,
    f40epd_f40_energy_payout_durability_payout_floor_stdxclose2_5d_252d_slope_v016_signal,
    f40epd_f40_energy_payout_durability_payout_floor_stdxclosem_5d_5d_slope_v017_signal,
    f40epd_f40_energy_payout_durability_payout_floor_stdxclosem63_5d_10d_slope_v018_signal,
    f40epd_f40_energy_payout_durability_payout_floor_stdxclosez_5d_21d_slope_v019_signal,
    f40epd_f40_energy_payout_durability_payout_floor_stdxclosechg_5d_42d_slope_v020_signal,
    f40epd_f40_energy_payout_durability_payout_floor_stdxclosediff_5d_63d_slope_v021_signal,
    f40epd_f40_energy_payout_durability_payout_floor_zxclose_5d_126d_slope_v022_signal,
    f40epd_f40_energy_payout_durability_payout_floor_zxclose2_5d_189d_slope_v023_signal,
    f40epd_f40_energy_payout_durability_payout_floor_zxclosem_5d_252d_slope_v024_signal,
    f40epd_f40_energy_payout_durability_payout_floor_zxclosem63_5d_5d_slope_v025_signal,
    f40epd_f40_energy_payout_durability_payout_floor_zxclosez_5d_10d_slope_v026_signal,
    f40epd_f40_energy_payout_durability_payout_floor_zxclosechg_5d_21d_slope_v027_signal,
    f40epd_f40_energy_payout_durability_payout_floor_zxclosediff_5d_42d_slope_v028_signal,
    f40epd_f40_energy_payout_durability_payout_floor_emaxclose_5d_63d_slope_v029_signal,
    f40epd_f40_energy_payout_durability_payout_floor_emaxclose2_5d_126d_slope_v030_signal,
    f40epd_f40_energy_payout_durability_payout_floor_emaxclosem_5d_189d_slope_v031_signal,
    f40epd_f40_energy_payout_durability_payout_floor_emaxclosem63_5d_252d_slope_v032_signal,
    f40epd_f40_energy_payout_durability_payout_floor_emaxclosez_5d_5d_slope_v033_signal,
    f40epd_f40_energy_payout_durability_payout_floor_emaxclosechg_5d_10d_slope_v034_signal,
    f40epd_f40_energy_payout_durability_payout_floor_emaxclosediff_5d_21d_slope_v035_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmedianxclose_5d_42d_slope_v036_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmedianxclose2_5d_63d_slope_v037_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmedianxclosem_5d_126d_slope_v038_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmedianxclosem63_5d_189d_slope_v039_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmedianxclosez_5d_252d_slope_v040_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmedianxclosechg_5d_5d_slope_v041_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmedianxclosediff_5d_10d_slope_v042_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmaxxclose_5d_21d_slope_v043_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmaxxclose2_5d_42d_slope_v044_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmaxxclosem_5d_63d_slope_v045_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmaxxclosem63_5d_126d_slope_v046_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmaxxclosez_5d_189d_slope_v047_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmaxxclosechg_5d_252d_slope_v048_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmaxxclosediff_5d_5d_slope_v049_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rminxclose_5d_10d_slope_v050_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rminxclose2_5d_21d_slope_v051_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rminxclosem_5d_42d_slope_v052_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rminxclosem63_5d_63d_slope_v053_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rminxclosez_5d_126d_slope_v054_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rminxclosechg_5d_189d_slope_v055_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rminxclosediff_5d_252d_slope_v056_signal,
    f40epd_f40_energy_payout_durability_payout_floor_skewxclose_5d_5d_slope_v057_signal,
    f40epd_f40_energy_payout_durability_payout_floor_skewxclose2_5d_10d_slope_v058_signal,
    f40epd_f40_energy_payout_durability_payout_floor_skewxclosem_5d_21d_slope_v059_signal,
    f40epd_f40_energy_payout_durability_payout_floor_skewxclosem63_5d_42d_slope_v060_signal,
    f40epd_f40_energy_payout_durability_payout_floor_skewxclosez_5d_63d_slope_v061_signal,
    f40epd_f40_energy_payout_durability_payout_floor_skewxclosechg_5d_126d_slope_v062_signal,
    f40epd_f40_energy_payout_durability_payout_floor_skewxclosediff_5d_189d_slope_v063_signal,
    f40epd_f40_energy_payout_durability_payout_floor_kurtxclose_5d_252d_slope_v064_signal,
    f40epd_f40_energy_payout_durability_payout_floor_kurtxclose2_5d_5d_slope_v065_signal,
    f40epd_f40_energy_payout_durability_payout_floor_kurtxclosem_5d_10d_slope_v066_signal,
    f40epd_f40_energy_payout_durability_payout_floor_kurtxclosem63_5d_21d_slope_v067_signal,
    f40epd_f40_energy_payout_durability_payout_floor_kurtxclosez_5d_42d_slope_v068_signal,
    f40epd_f40_energy_payout_durability_payout_floor_kurtxclosechg_5d_63d_slope_v069_signal,
    f40epd_f40_energy_payout_durability_payout_floor_kurtxclosediff_5d_126d_slope_v070_signal,
    f40epd_f40_energy_payout_durability_payout_floor_qhixclose_5d_189d_slope_v071_signal,
    f40epd_f40_energy_payout_durability_payout_floor_qhixclose2_5d_252d_slope_v072_signal,
    f40epd_f40_energy_payout_durability_payout_floor_qhixclosem_5d_5d_slope_v073_signal,
    f40epd_f40_energy_payout_durability_payout_floor_qhixclosem63_5d_10d_slope_v074_signal,
    f40epd_f40_energy_payout_durability_payout_floor_qhixclosez_5d_21d_slope_v075_signal,
    f40epd_f40_energy_payout_durability_payout_floor_qhixclosechg_5d_42d_slope_v076_signal,
    f40epd_f40_energy_payout_durability_payout_floor_qhixclosediff_5d_63d_slope_v077_signal,
    f40epd_f40_energy_payout_durability_payout_floor_qloxclose_5d_126d_slope_v078_signal,
    f40epd_f40_energy_payout_durability_payout_floor_qloxclose2_5d_189d_slope_v079_signal,
    f40epd_f40_energy_payout_durability_payout_floor_qloxclosem_5d_252d_slope_v080_signal,
    f40epd_f40_energy_payout_durability_payout_floor_qloxclosem63_5d_5d_slope_v081_signal,
    f40epd_f40_energy_payout_durability_payout_floor_qloxclosez_5d_10d_slope_v082_signal,
    f40epd_f40_energy_payout_durability_payout_floor_qloxclosechg_5d_21d_slope_v083_signal,
    f40epd_f40_energy_payout_durability_payout_floor_qloxclosediff_5d_42d_slope_v084_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rangexclose_5d_63d_slope_v085_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rangexclose2_5d_126d_slope_v086_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rangexclosem_5d_189d_slope_v087_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rangexclosem63_5d_252d_slope_v088_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rangexclosez_5d_5d_slope_v089_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rangexclosechg_5d_10d_slope_v090_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rangexclosediff_5d_21d_slope_v091_signal,
    f40epd_f40_energy_payout_durability_payout_floor_squaredxclose_5d_42d_slope_v092_signal,
    f40epd_f40_energy_payout_durability_payout_floor_squaredxclose2_5d_63d_slope_v093_signal,
    f40epd_f40_energy_payout_durability_payout_floor_squaredxclosem_5d_126d_slope_v094_signal,
    f40epd_f40_energy_payout_durability_payout_floor_squaredxclosem63_5d_189d_slope_v095_signal,
    f40epd_f40_energy_payout_durability_payout_floor_squaredxclosez_5d_252d_slope_v096_signal,
    f40epd_f40_energy_payout_durability_payout_floor_squaredxclosechg_5d_5d_slope_v097_signal,
    f40epd_f40_energy_payout_durability_payout_floor_squaredxclosediff_5d_10d_slope_v098_signal,
    f40epd_f40_energy_payout_durability_payout_floor_diffxclose_5d_21d_slope_v099_signal,
    f40epd_f40_energy_payout_durability_payout_floor_diffxclose2_5d_42d_slope_v100_signal,
    f40epd_f40_energy_payout_durability_payout_floor_diffxclosem_5d_63d_slope_v101_signal,
    f40epd_f40_energy_payout_durability_payout_floor_diffxclosem63_5d_126d_slope_v102_signal,
    f40epd_f40_energy_payout_durability_payout_floor_diffxclosez_5d_189d_slope_v103_signal,
    f40epd_f40_energy_payout_durability_payout_floor_diffxclosechg_5d_252d_slope_v104_signal,
    f40epd_f40_energy_payout_durability_payout_floor_diffxclosediff_5d_5d_slope_v105_signal,
    f40epd_f40_energy_payout_durability_payout_floor_pctxclose_5d_10d_slope_v106_signal,
    f40epd_f40_energy_payout_durability_payout_floor_pctxclose2_5d_21d_slope_v107_signal,
    f40epd_f40_energy_payout_durability_payout_floor_pctxclosem_5d_42d_slope_v108_signal,
    f40epd_f40_energy_payout_durability_payout_floor_pctxclosem63_5d_63d_slope_v109_signal,
    f40epd_f40_energy_payout_durability_payout_floor_pctxclosez_5d_126d_slope_v110_signal,
    f40epd_f40_energy_payout_durability_payout_floor_pctxclosechg_5d_189d_slope_v111_signal,
    f40epd_f40_energy_payout_durability_payout_floor_pctxclosediff_5d_252d_slope_v112_signal,
    f40epd_f40_energy_payout_durability_payout_floor_signxclose_5d_5d_slope_v113_signal,
    f40epd_f40_energy_payout_durability_payout_floor_signxclose2_5d_10d_slope_v114_signal,
    f40epd_f40_energy_payout_durability_payout_floor_signxclosem_5d_21d_slope_v115_signal,
    f40epd_f40_energy_payout_durability_payout_floor_signxclosem63_5d_42d_slope_v116_signal,
    f40epd_f40_energy_payout_durability_payout_floor_signxclosez_5d_63d_slope_v117_signal,
    f40epd_f40_energy_payout_durability_payout_floor_signxclosechg_5d_126d_slope_v118_signal,
    f40epd_f40_energy_payout_durability_payout_floor_signxclosediff_5d_189d_slope_v119_signal,
    f40epd_f40_energy_payout_durability_payout_floor_absxclose_5d_252d_slope_v120_signal,
    f40epd_f40_energy_payout_durability_payout_floor_absxclose2_5d_5d_slope_v121_signal,
    f40epd_f40_energy_payout_durability_payout_floor_absxclosem_5d_10d_slope_v122_signal,
    f40epd_f40_energy_payout_durability_payout_floor_absxclosem63_5d_21d_slope_v123_signal,
    f40epd_f40_energy_payout_durability_payout_floor_absxclosez_5d_42d_slope_v124_signal,
    f40epd_f40_energy_payout_durability_payout_floor_absxclosechg_5d_63d_slope_v125_signal,
    f40epd_f40_energy_payout_durability_payout_floor_absxclosediff_5d_126d_slope_v126_signal,
    f40epd_f40_energy_payout_durability_payout_floor_idxclose_10d_189d_slope_v127_signal,
    f40epd_f40_energy_payout_durability_payout_floor_idxclose2_10d_252d_slope_v128_signal,
    f40epd_f40_energy_payout_durability_payout_floor_idxclosem_10d_5d_slope_v129_signal,
    f40epd_f40_energy_payout_durability_payout_floor_idxclosem63_10d_10d_slope_v130_signal,
    f40epd_f40_energy_payout_durability_payout_floor_idxclosez_10d_21d_slope_v131_signal,
    f40epd_f40_energy_payout_durability_payout_floor_idxclosechg_10d_42d_slope_v132_signal,
    f40epd_f40_energy_payout_durability_payout_floor_idxclosediff_10d_63d_slope_v133_signal,
    f40epd_f40_energy_payout_durability_payout_floor_meanxclose_10d_126d_slope_v134_signal,
    f40epd_f40_energy_payout_durability_payout_floor_meanxclose2_10d_189d_slope_v135_signal,
    f40epd_f40_energy_payout_durability_payout_floor_meanxclosem_10d_252d_slope_v136_signal,
    f40epd_f40_energy_payout_durability_payout_floor_meanxclosem63_10d_5d_slope_v137_signal,
    f40epd_f40_energy_payout_durability_payout_floor_meanxclosez_10d_10d_slope_v138_signal,
    f40epd_f40_energy_payout_durability_payout_floor_meanxclosechg_10d_21d_slope_v139_signal,
    f40epd_f40_energy_payout_durability_payout_floor_meanxclosediff_10d_42d_slope_v140_signal,
    f40epd_f40_energy_payout_durability_payout_floor_stdxclose_10d_63d_slope_v141_signal,
    f40epd_f40_energy_payout_durability_payout_floor_stdxclose2_10d_126d_slope_v142_signal,
    f40epd_f40_energy_payout_durability_payout_floor_stdxclosem_10d_189d_slope_v143_signal,
    f40epd_f40_energy_payout_durability_payout_floor_stdxclosem63_10d_252d_slope_v144_signal,
    f40epd_f40_energy_payout_durability_payout_floor_stdxclosez_10d_5d_slope_v145_signal,
    f40epd_f40_energy_payout_durability_payout_floor_stdxclosechg_10d_10d_slope_v146_signal,
    f40epd_f40_energy_payout_durability_payout_floor_stdxclosediff_10d_21d_slope_v147_signal,
    f40epd_f40_energy_payout_durability_payout_floor_zxclose_10d_42d_slope_v148_signal,
    f40epd_f40_energy_payout_durability_payout_floor_zxclose2_10d_63d_slope_v149_signal,
    f40epd_f40_energy_payout_durability_payout_floor_zxclosem_10d_126d_slope_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F40_ENERGY_PAYOUT_DURABILITY_REGISTRY_SLOPE_001_150 = REGISTRY


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
    domain_primitives = ("_f40_payout_floor", "_f40_payout_durability", "_f40_payout_sustainability",)
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
    print(f"OK f40_energy_payout_durability_2nd_derivatives_001_150_claude: {n_features} features pass")
