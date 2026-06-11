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


def _f38_capex_to_fcf(capex, fcf):
    base = fcf.abs().rolling(21, min_periods=5).mean().replace(0, np.nan)
    return capex / base



def _f38_capex_discipline(capex, fcf, w):
    ratio = capex / fcf.abs().rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    return -ratio.rolling(w, min_periods=max(1, w // 2)).mean()



def _f38_discipline_score(capex, fcf, revenue, w):
    ratio = capex / fcf.abs().rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    rev_g = revenue.pct_change(periods=w).fillna(0.0)
    return (-ratio + rev_g).rolling(w, min_periods=max(1, w // 2)).mean()


# ===== features =====


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclose_5d_5d_jerk_v001_signal(fcf, capex, closeadj):
    base = (_f38_capex_to_fcf(capex, fcf)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclose2_5d_10d_jerk_v002_signal(fcf, capex, closeadj):
    base = (_f38_capex_to_fcf(capex, fcf)) * closeadj * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosem_5d_21d_jerk_v003_signal(fcf, capex, closeadj):
    base = (_f38_capex_to_fcf(capex, fcf)) * _mean(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosem63_5d_42d_jerk_v004_signal(fcf, capex, closeadj):
    base = (_f38_capex_to_fcf(capex, fcf)) * _mean(closeadj, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosez_5d_63d_jerk_v005_signal(fcf, capex, closeadj):
    base = (_f38_capex_to_fcf(capex, fcf)) * _z(closeadj, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosechg_5d_126d_jerk_v006_signal(fcf, capex, closeadj):
    base = (_f38_capex_to_fcf(capex, fcf)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosediff_5d_189d_jerk_v007_signal(fcf, capex, closeadj):
    base = (_f38_capex_to_fcf(capex, fcf)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclose_5d_252d_jerk_v008_signal(fcf, capex, closeadj):
    base = (_mean(_f38_capex_to_fcf(capex, fcf), 5)) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclose2_5d_5d_jerk_v009_signal(fcf, capex, closeadj):
    base = (_mean(_f38_capex_to_fcf(capex, fcf), 5)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosem_5d_10d_jerk_v010_signal(fcf, capex, closeadj):
    base = (_mean(_f38_capex_to_fcf(capex, fcf), 5)) * _mean(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosem63_5d_21d_jerk_v011_signal(fcf, capex, closeadj):
    base = (_mean(_f38_capex_to_fcf(capex, fcf), 5)) * _mean(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosez_5d_42d_jerk_v012_signal(fcf, capex, closeadj):
    base = (_mean(_f38_capex_to_fcf(capex, fcf), 5)) * _z(closeadj, 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosechg_5d_63d_jerk_v013_signal(fcf, capex, closeadj):
    base = (_mean(_f38_capex_to_fcf(capex, fcf), 5)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosediff_5d_126d_jerk_v014_signal(fcf, capex, closeadj):
    base = (_mean(_f38_capex_to_fcf(capex, fcf), 5)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclose_5d_189d_jerk_v015_signal(fcf, capex, closeadj):
    base = (_std(_f38_capex_to_fcf(capex, fcf), 5)) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclose2_5d_252d_jerk_v016_signal(fcf, capex, closeadj):
    base = (_std(_f38_capex_to_fcf(capex, fcf), 5)) * closeadj * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosem_5d_5d_jerk_v017_signal(fcf, capex, closeadj):
    base = (_std(_f38_capex_to_fcf(capex, fcf), 5)) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosem63_5d_10d_jerk_v018_signal(fcf, capex, closeadj):
    base = (_std(_f38_capex_to_fcf(capex, fcf), 5)) * _mean(closeadj, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosez_5d_21d_jerk_v019_signal(fcf, capex, closeadj):
    base = (_std(_f38_capex_to_fcf(capex, fcf), 5)) * _z(closeadj, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosechg_5d_42d_jerk_v020_signal(fcf, capex, closeadj):
    base = (_std(_f38_capex_to_fcf(capex, fcf), 5)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosediff_5d_63d_jerk_v021_signal(fcf, capex, closeadj):
    base = (_std(_f38_capex_to_fcf(capex, fcf), 5)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclose_5d_126d_jerk_v022_signal(fcf, capex, closeadj):
    base = (_z(_f38_capex_to_fcf(capex, fcf), 5)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclose2_5d_189d_jerk_v023_signal(fcf, capex, closeadj):
    base = (_z(_f38_capex_to_fcf(capex, fcf), 5)) * closeadj * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosem_5d_252d_jerk_v024_signal(fcf, capex, closeadj):
    base = (_z(_f38_capex_to_fcf(capex, fcf), 5)) * _mean(closeadj, 21)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosem63_5d_5d_jerk_v025_signal(fcf, capex, closeadj):
    base = (_z(_f38_capex_to_fcf(capex, fcf), 5)) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosez_5d_10d_jerk_v026_signal(fcf, capex, closeadj):
    base = (_z(_f38_capex_to_fcf(capex, fcf), 5)) * _z(closeadj, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosechg_5d_21d_jerk_v027_signal(fcf, capex, closeadj):
    base = (_z(_f38_capex_to_fcf(capex, fcf), 5)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosediff_5d_42d_jerk_v028_signal(fcf, capex, closeadj):
    base = (_z(_f38_capex_to_fcf(capex, fcf), 5)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclose_5d_63d_jerk_v029_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclose2_5d_126d_jerk_v030_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * closeadj * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosem_5d_189d_jerk_v031_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * _mean(closeadj, 21)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosem63_5d_252d_jerk_v032_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * _mean(closeadj, 63)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosez_5d_5d_jerk_v033_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * _z(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosechg_5d_10d_jerk_v034_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosediff_5d_21d_jerk_v035_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclose_5d_42d_jerk_v036_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).median()) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclose2_5d_63d_jerk_v037_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).median()) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosem_5d_126d_jerk_v038_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).median()) * _mean(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosem63_5d_189d_jerk_v039_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).median()) * _mean(closeadj, 63)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosez_5d_252d_jerk_v040_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).median()) * _z(closeadj, 252)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosechg_5d_5d_jerk_v041_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).median()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosediff_5d_10d_jerk_v042_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).median()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclose_5d_21d_jerk_v043_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).max()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclose2_5d_42d_jerk_v044_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).max()) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosem_5d_63d_jerk_v045_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).max()) * _mean(closeadj, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosem63_5d_126d_jerk_v046_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).max()) * _mean(closeadj, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosez_5d_189d_jerk_v047_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).max()) * _z(closeadj, 252)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosechg_5d_252d_jerk_v048_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).max()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosediff_5d_5d_jerk_v049_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).max()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclose_5d_10d_jerk_v050_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclose2_5d_21d_jerk_v051_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosem_5d_42d_jerk_v052_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _mean(closeadj, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosem63_5d_63d_jerk_v053_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _mean(closeadj, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosez_5d_126d_jerk_v054_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _z(closeadj, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosechg_5d_189d_jerk_v055_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosediff_5d_252d_jerk_v056_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).min()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclose_5d_5d_jerk_v057_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclose2_5d_10d_jerk_v058_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * closeadj * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosem_5d_21d_jerk_v059_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * _mean(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosem63_5d_42d_jerk_v060_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * _mean(closeadj, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosez_5d_63d_jerk_v061_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * _z(closeadj, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosechg_5d_126d_jerk_v062_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosediff_5d_189d_jerk_v063_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclose_5d_252d_jerk_v064_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclose2_5d_5d_jerk_v065_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosem_5d_10d_jerk_v066_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * _mean(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosem63_5d_21d_jerk_v067_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * _mean(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosez_5d_42d_jerk_v068_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * _z(closeadj, 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosechg_5d_63d_jerk_v069_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosediff_5d_126d_jerk_v070_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclose_5d_189d_jerk_v071_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclose2_5d_252d_jerk_v072_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * closeadj * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclosem_5d_5d_jerk_v073_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclosem63_5d_10d_jerk_v074_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * _mean(closeadj, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclosez_5d_21d_jerk_v075_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * _z(closeadj, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclosechg_5d_42d_jerk_v076_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclosediff_5d_63d_jerk_v077_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_qloxclose_5d_126d_jerk_v078_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_qloxclose2_5d_189d_jerk_v079_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * closeadj * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_qloxclosem_5d_252d_jerk_v080_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * _mean(closeadj, 21)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_qloxclosem63_5d_5d_jerk_v081_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_qloxclosez_5d_10d_jerk_v082_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * _z(closeadj, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_qloxclosechg_5d_21d_jerk_v083_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_qloxclosediff_5d_42d_jerk_v084_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rangexclose_5d_63d_jerk_v085_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rangexclose2_5d_126d_jerk_v086_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rangexclosem_5d_189d_jerk_v087_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _mean(closeadj, 21)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rangexclosem63_5d_252d_jerk_v088_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _mean(closeadj, 63)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rangexclosez_5d_5d_jerk_v089_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _z(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rangexclosechg_5d_10d_jerk_v090_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rangexclosediff_5d_21d_jerk_v091_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).min()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_squaredxclose_5d_42d_jerk_v092_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)) * (_f38_capex_to_fcf(capex, fcf)).abs()) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_squaredxclose2_5d_63d_jerk_v093_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)) * (_f38_capex_to_fcf(capex, fcf)).abs()) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_squaredxclosem_5d_126d_jerk_v094_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)) * (_f38_capex_to_fcf(capex, fcf)).abs()) * _mean(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_squaredxclosem63_5d_189d_jerk_v095_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)) * (_f38_capex_to_fcf(capex, fcf)).abs()) * _mean(closeadj, 63)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_squaredxclosez_5d_252d_jerk_v096_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)) * (_f38_capex_to_fcf(capex, fcf)).abs()) * _z(closeadj, 252)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_squaredxclosechg_5d_5d_jerk_v097_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)) * (_f38_capex_to_fcf(capex, fcf)).abs()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_squaredxclosediff_5d_10d_jerk_v098_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)) * (_f38_capex_to_fcf(capex, fcf)).abs()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_diffxclose_5d_21d_jerk_v099_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)) - (_f38_capex_to_fcf(capex, fcf)).shift(5)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_diffxclose2_5d_42d_jerk_v100_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)) - (_f38_capex_to_fcf(capex, fcf)).shift(5)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_diffxclosem_5d_63d_jerk_v101_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)) - (_f38_capex_to_fcf(capex, fcf)).shift(5)) * _mean(closeadj, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_diffxclosem63_5d_126d_jerk_v102_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)) - (_f38_capex_to_fcf(capex, fcf)).shift(5)) * _mean(closeadj, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_diffxclosez_5d_189d_jerk_v103_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)) - (_f38_capex_to_fcf(capex, fcf)).shift(5)) * _z(closeadj, 252)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_diffxclosechg_5d_252d_jerk_v104_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)) - (_f38_capex_to_fcf(capex, fcf)).shift(5)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_diffxclosediff_5d_5d_jerk_v105_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)) - (_f38_capex_to_fcf(capex, fcf)).shift(5)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_pctxclose_5d_10d_jerk_v106_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).pct_change(5)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_pctxclose2_5d_21d_jerk_v107_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).pct_change(5)) * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_pctxclosem_5d_42d_jerk_v108_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).pct_change(5)) * _mean(closeadj, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_pctxclosem63_5d_63d_jerk_v109_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).pct_change(5)) * _mean(closeadj, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_pctxclosez_5d_126d_jerk_v110_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).pct_change(5)) * _z(closeadj, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_pctxclosechg_5d_189d_jerk_v111_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).pct_change(5)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_pctxclosediff_5d_252d_jerk_v112_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).pct_change(5)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_signxclose_5d_5d_jerk_v113_signal(fcf, capex, closeadj):
    base = (np.sign(_f38_capex_to_fcf(capex, fcf))) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_signxclose2_5d_10d_jerk_v114_signal(fcf, capex, closeadj):
    base = (np.sign(_f38_capex_to_fcf(capex, fcf))) * closeadj * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_signxclosem_5d_21d_jerk_v115_signal(fcf, capex, closeadj):
    base = (np.sign(_f38_capex_to_fcf(capex, fcf))) * _mean(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_signxclosem63_5d_42d_jerk_v116_signal(fcf, capex, closeadj):
    base = (np.sign(_f38_capex_to_fcf(capex, fcf))) * _mean(closeadj, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_signxclosez_5d_63d_jerk_v117_signal(fcf, capex, closeadj):
    base = (np.sign(_f38_capex_to_fcf(capex, fcf))) * _z(closeadj, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_signxclosechg_5d_126d_jerk_v118_signal(fcf, capex, closeadj):
    base = (np.sign(_f38_capex_to_fcf(capex, fcf))) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_signxclosediff_5d_189d_jerk_v119_signal(fcf, capex, closeadj):
    base = (np.sign(_f38_capex_to_fcf(capex, fcf))) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclose_5d_252d_jerk_v120_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).abs()) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclose2_5d_5d_jerk_v121_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).abs()) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclosem_5d_10d_jerk_v122_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).abs()) * _mean(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclosem63_5d_21d_jerk_v123_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).abs()) * _mean(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclosez_5d_42d_jerk_v124_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).abs()) * _z(closeadj, 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclosechg_5d_63d_jerk_v125_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).abs()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclosediff_5d_126d_jerk_v126_signal(fcf, capex, closeadj):
    base = ((_f38_capex_to_fcf(capex, fcf)).abs()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclose_10d_189d_jerk_v127_signal(fcf, capex, closeadj):
    base = (_f38_capex_to_fcf(capex, fcf)) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclose2_10d_252d_jerk_v128_signal(fcf, capex, closeadj):
    base = (_f38_capex_to_fcf(capex, fcf)) * closeadj * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosem_10d_5d_jerk_v129_signal(fcf, capex, closeadj):
    base = (_f38_capex_to_fcf(capex, fcf)) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosem63_10d_10d_jerk_v130_signal(fcf, capex, closeadj):
    base = (_f38_capex_to_fcf(capex, fcf)) * _mean(closeadj, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosez_10d_21d_jerk_v131_signal(fcf, capex, closeadj):
    base = (_f38_capex_to_fcf(capex, fcf)) * _z(closeadj, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosechg_10d_42d_jerk_v132_signal(fcf, capex, closeadj):
    base = (_f38_capex_to_fcf(capex, fcf)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosediff_10d_63d_jerk_v133_signal(fcf, capex, closeadj):
    base = (_f38_capex_to_fcf(capex, fcf)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclose_10d_126d_jerk_v134_signal(fcf, capex, closeadj):
    base = (_mean(_f38_capex_to_fcf(capex, fcf), 10)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclose2_10d_189d_jerk_v135_signal(fcf, capex, closeadj):
    base = (_mean(_f38_capex_to_fcf(capex, fcf), 10)) * closeadj * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosem_10d_252d_jerk_v136_signal(fcf, capex, closeadj):
    base = (_mean(_f38_capex_to_fcf(capex, fcf), 10)) * _mean(closeadj, 21)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosem63_10d_5d_jerk_v137_signal(fcf, capex, closeadj):
    base = (_mean(_f38_capex_to_fcf(capex, fcf), 10)) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosez_10d_10d_jerk_v138_signal(fcf, capex, closeadj):
    base = (_mean(_f38_capex_to_fcf(capex, fcf), 10)) * _z(closeadj, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosechg_10d_21d_jerk_v139_signal(fcf, capex, closeadj):
    base = (_mean(_f38_capex_to_fcf(capex, fcf), 10)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosediff_10d_42d_jerk_v140_signal(fcf, capex, closeadj):
    base = (_mean(_f38_capex_to_fcf(capex, fcf), 10)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclose_10d_63d_jerk_v141_signal(fcf, capex, closeadj):
    base = (_std(_f38_capex_to_fcf(capex, fcf), 10)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclose2_10d_126d_jerk_v142_signal(fcf, capex, closeadj):
    base = (_std(_f38_capex_to_fcf(capex, fcf), 10)) * closeadj * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosem_10d_189d_jerk_v143_signal(fcf, capex, closeadj):
    base = (_std(_f38_capex_to_fcf(capex, fcf), 10)) * _mean(closeadj, 21)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosem63_10d_252d_jerk_v144_signal(fcf, capex, closeadj):
    base = (_std(_f38_capex_to_fcf(capex, fcf), 10)) * _mean(closeadj, 63)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosez_10d_5d_jerk_v145_signal(fcf, capex, closeadj):
    base = (_std(_f38_capex_to_fcf(capex, fcf), 10)) * _z(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosechg_10d_10d_jerk_v146_signal(fcf, capex, closeadj):
    base = (_std(_f38_capex_to_fcf(capex, fcf), 10)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosediff_10d_21d_jerk_v147_signal(fcf, capex, closeadj):
    base = (_std(_f38_capex_to_fcf(capex, fcf), 10)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclose_10d_42d_jerk_v148_signal(fcf, capex, closeadj):
    base = (_z(_f38_capex_to_fcf(capex, fcf), 10)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclose2_10d_63d_jerk_v149_signal(fcf, capex, closeadj):
    base = (_z(_f38_capex_to_fcf(capex, fcf), 10)) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosem_10d_126d_jerk_v150_signal(fcf, capex, closeadj):
    base = (_z(_f38_capex_to_fcf(capex, fcf), 10)) * _mean(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclose_5d_5d_jerk_v001_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclose2_5d_10d_jerk_v002_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosem_5d_21d_jerk_v003_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosem63_5d_42d_jerk_v004_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosez_5d_63d_jerk_v005_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosechg_5d_126d_jerk_v006_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosediff_5d_189d_jerk_v007_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclose_5d_252d_jerk_v008_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclose2_5d_5d_jerk_v009_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosem_5d_10d_jerk_v010_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosem63_5d_21d_jerk_v011_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosez_5d_42d_jerk_v012_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosechg_5d_63d_jerk_v013_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosediff_5d_126d_jerk_v014_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclose_5d_189d_jerk_v015_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclose2_5d_252d_jerk_v016_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosem_5d_5d_jerk_v017_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosem63_5d_10d_jerk_v018_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosez_5d_21d_jerk_v019_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosechg_5d_42d_jerk_v020_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosediff_5d_63d_jerk_v021_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclose_5d_126d_jerk_v022_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclose2_5d_189d_jerk_v023_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosem_5d_252d_jerk_v024_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosem63_5d_5d_jerk_v025_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosez_5d_10d_jerk_v026_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosechg_5d_21d_jerk_v027_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosediff_5d_42d_jerk_v028_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclose_5d_63d_jerk_v029_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclose2_5d_126d_jerk_v030_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosem_5d_189d_jerk_v031_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosem63_5d_252d_jerk_v032_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosez_5d_5d_jerk_v033_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosechg_5d_10d_jerk_v034_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosediff_5d_21d_jerk_v035_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclose_5d_42d_jerk_v036_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclose2_5d_63d_jerk_v037_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosem_5d_126d_jerk_v038_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosem63_5d_189d_jerk_v039_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosez_5d_252d_jerk_v040_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosechg_5d_5d_jerk_v041_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosediff_5d_10d_jerk_v042_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclose_5d_21d_jerk_v043_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclose2_5d_42d_jerk_v044_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosem_5d_63d_jerk_v045_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosem63_5d_126d_jerk_v046_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosez_5d_189d_jerk_v047_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosechg_5d_252d_jerk_v048_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosediff_5d_5d_jerk_v049_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclose_5d_10d_jerk_v050_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclose2_5d_21d_jerk_v051_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosem_5d_42d_jerk_v052_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosem63_5d_63d_jerk_v053_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosez_5d_126d_jerk_v054_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosechg_5d_189d_jerk_v055_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosediff_5d_252d_jerk_v056_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclose_5d_5d_jerk_v057_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclose2_5d_10d_jerk_v058_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosem_5d_21d_jerk_v059_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosem63_5d_42d_jerk_v060_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosez_5d_63d_jerk_v061_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosechg_5d_126d_jerk_v062_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosediff_5d_189d_jerk_v063_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclose_5d_252d_jerk_v064_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclose2_5d_5d_jerk_v065_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosem_5d_10d_jerk_v066_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosem63_5d_21d_jerk_v067_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosez_5d_42d_jerk_v068_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosechg_5d_63d_jerk_v069_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosediff_5d_126d_jerk_v070_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclose_5d_189d_jerk_v071_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclose2_5d_252d_jerk_v072_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclosem_5d_5d_jerk_v073_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclosem63_5d_10d_jerk_v074_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclosez_5d_21d_jerk_v075_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclosechg_5d_42d_jerk_v076_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclosediff_5d_63d_jerk_v077_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_qloxclose_5d_126d_jerk_v078_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_qloxclose2_5d_189d_jerk_v079_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_qloxclosem_5d_252d_jerk_v080_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_qloxclosem63_5d_5d_jerk_v081_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_qloxclosez_5d_10d_jerk_v082_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_qloxclosechg_5d_21d_jerk_v083_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_qloxclosediff_5d_42d_jerk_v084_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rangexclose_5d_63d_jerk_v085_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rangexclose2_5d_126d_jerk_v086_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rangexclosem_5d_189d_jerk_v087_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rangexclosem63_5d_252d_jerk_v088_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rangexclosez_5d_5d_jerk_v089_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rangexclosechg_5d_10d_jerk_v090_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rangexclosediff_5d_21d_jerk_v091_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_squaredxclose_5d_42d_jerk_v092_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_squaredxclose2_5d_63d_jerk_v093_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_squaredxclosem_5d_126d_jerk_v094_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_squaredxclosem63_5d_189d_jerk_v095_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_squaredxclosez_5d_252d_jerk_v096_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_squaredxclosechg_5d_5d_jerk_v097_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_squaredxclosediff_5d_10d_jerk_v098_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_diffxclose_5d_21d_jerk_v099_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_diffxclose2_5d_42d_jerk_v100_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_diffxclosem_5d_63d_jerk_v101_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_diffxclosem63_5d_126d_jerk_v102_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_diffxclosez_5d_189d_jerk_v103_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_diffxclosechg_5d_252d_jerk_v104_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_diffxclosediff_5d_5d_jerk_v105_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_pctxclose_5d_10d_jerk_v106_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_pctxclose2_5d_21d_jerk_v107_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_pctxclosem_5d_42d_jerk_v108_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_pctxclosem63_5d_63d_jerk_v109_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_pctxclosez_5d_126d_jerk_v110_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_pctxclosechg_5d_189d_jerk_v111_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_pctxclosediff_5d_252d_jerk_v112_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_signxclose_5d_5d_jerk_v113_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_signxclose2_5d_10d_jerk_v114_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_signxclosem_5d_21d_jerk_v115_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_signxclosem63_5d_42d_jerk_v116_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_signxclosez_5d_63d_jerk_v117_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_signxclosechg_5d_126d_jerk_v118_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_signxclosediff_5d_189d_jerk_v119_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclose_5d_252d_jerk_v120_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclose2_5d_5d_jerk_v121_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclosem_5d_10d_jerk_v122_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclosem63_5d_21d_jerk_v123_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclosez_5d_42d_jerk_v124_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclosechg_5d_63d_jerk_v125_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclosediff_5d_126d_jerk_v126_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclose_10d_189d_jerk_v127_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclose2_10d_252d_jerk_v128_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosem_10d_5d_jerk_v129_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosem63_10d_10d_jerk_v130_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosez_10d_21d_jerk_v131_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosechg_10d_42d_jerk_v132_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosediff_10d_63d_jerk_v133_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclose_10d_126d_jerk_v134_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclose2_10d_189d_jerk_v135_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosem_10d_252d_jerk_v136_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosem63_10d_5d_jerk_v137_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosez_10d_10d_jerk_v138_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosechg_10d_21d_jerk_v139_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosediff_10d_42d_jerk_v140_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclose_10d_63d_jerk_v141_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclose2_10d_126d_jerk_v142_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosem_10d_189d_jerk_v143_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosem63_10d_252d_jerk_v144_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosez_10d_5d_jerk_v145_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosechg_10d_10d_jerk_v146_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosediff_10d_21d_jerk_v147_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclose_10d_42d_jerk_v148_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclose2_10d_63d_jerk_v149_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosem_10d_126d_jerk_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F38_ENERGY_CAPEX_DISCIPLINE_REGISTRY_JERK_001_150 = REGISTRY


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
    domain_primitives = ("_f38_capex_to_fcf", "_f38_capex_discipline", "_f38_discipline_score",)
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
    print(f"OK f38_energy_capex_discipline_3rd_derivatives_001_150_claude: {n_features} features pass")
