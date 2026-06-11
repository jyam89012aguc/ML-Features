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


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclose_5d_base_v001_signal(fcf, capex, closeadj):
    result = (_f38_capex_to_fcf(capex, fcf)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclose2_5d_base_v002_signal(fcf, capex, closeadj):
    result = (_f38_capex_to_fcf(capex, fcf)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosem_5d_base_v003_signal(fcf, capex, closeadj):
    result = (_f38_capex_to_fcf(capex, fcf)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosem63_5d_base_v004_signal(fcf, capex, closeadj):
    result = (_f38_capex_to_fcf(capex, fcf)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosez_5d_base_v005_signal(fcf, capex, closeadj):
    result = (_f38_capex_to_fcf(capex, fcf)) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosechg_5d_base_v006_signal(fcf, capex, closeadj):
    result = (_f38_capex_to_fcf(capex, fcf)) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosediff_5d_base_v007_signal(fcf, capex, closeadj):
    result = (_f38_capex_to_fcf(capex, fcf)) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclose_5d_base_v008_signal(fcf, capex, closeadj):
    result = (_mean(_f38_capex_to_fcf(capex, fcf), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclose2_5d_base_v009_signal(fcf, capex, closeadj):
    result = (_mean(_f38_capex_to_fcf(capex, fcf), 5)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosem_5d_base_v010_signal(fcf, capex, closeadj):
    result = (_mean(_f38_capex_to_fcf(capex, fcf), 5)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosem63_5d_base_v011_signal(fcf, capex, closeadj):
    result = (_mean(_f38_capex_to_fcf(capex, fcf), 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosez_5d_base_v012_signal(fcf, capex, closeadj):
    result = (_mean(_f38_capex_to_fcf(capex, fcf), 5)) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosechg_5d_base_v013_signal(fcf, capex, closeadj):
    result = (_mean(_f38_capex_to_fcf(capex, fcf), 5)) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosediff_5d_base_v014_signal(fcf, capex, closeadj):
    result = (_mean(_f38_capex_to_fcf(capex, fcf), 5)) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclose_5d_base_v015_signal(fcf, capex, closeadj):
    result = (_std(_f38_capex_to_fcf(capex, fcf), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclose2_5d_base_v016_signal(fcf, capex, closeadj):
    result = (_std(_f38_capex_to_fcf(capex, fcf), 5)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosem_5d_base_v017_signal(fcf, capex, closeadj):
    result = (_std(_f38_capex_to_fcf(capex, fcf), 5)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosem63_5d_base_v018_signal(fcf, capex, closeadj):
    result = (_std(_f38_capex_to_fcf(capex, fcf), 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosez_5d_base_v019_signal(fcf, capex, closeadj):
    result = (_std(_f38_capex_to_fcf(capex, fcf), 5)) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosechg_5d_base_v020_signal(fcf, capex, closeadj):
    result = (_std(_f38_capex_to_fcf(capex, fcf), 5)) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosediff_5d_base_v021_signal(fcf, capex, closeadj):
    result = (_std(_f38_capex_to_fcf(capex, fcf), 5)) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclose_5d_base_v022_signal(fcf, capex, closeadj):
    result = (_z(_f38_capex_to_fcf(capex, fcf), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclose2_5d_base_v023_signal(fcf, capex, closeadj):
    result = (_z(_f38_capex_to_fcf(capex, fcf), 5)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosem_5d_base_v024_signal(fcf, capex, closeadj):
    result = (_z(_f38_capex_to_fcf(capex, fcf), 5)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosem63_5d_base_v025_signal(fcf, capex, closeadj):
    result = (_z(_f38_capex_to_fcf(capex, fcf), 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosez_5d_base_v026_signal(fcf, capex, closeadj):
    result = (_z(_f38_capex_to_fcf(capex, fcf), 5)) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosechg_5d_base_v027_signal(fcf, capex, closeadj):
    result = (_z(_f38_capex_to_fcf(capex, fcf), 5)) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosediff_5d_base_v028_signal(fcf, capex, closeadj):
    result = (_z(_f38_capex_to_fcf(capex, fcf), 5)) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclose_5d_base_v029_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclose2_5d_base_v030_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosem_5d_base_v031_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosem63_5d_base_v032_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosez_5d_base_v033_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosechg_5d_base_v034_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosediff_5d_base_v035_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclose_5d_base_v036_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclose2_5d_base_v037_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).median()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosem_5d_base_v038_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).median()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosem63_5d_base_v039_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).median()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosez_5d_base_v040_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).median()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosechg_5d_base_v041_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).median()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosediff_5d_base_v042_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).median()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclose_5d_base_v043_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).max()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclose2_5d_base_v044_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).max()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosem_5d_base_v045_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).max()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosem63_5d_base_v046_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).max()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosez_5d_base_v047_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).max()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosechg_5d_base_v048_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).max()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosediff_5d_base_v049_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).max()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclose_5d_base_v050_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclose2_5d_base_v051_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosem_5d_base_v052_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosem63_5d_base_v053_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosez_5d_base_v054_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosechg_5d_base_v055_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosediff_5d_base_v056_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).min()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclose_5d_base_v057_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclose2_5d_base_v058_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosem_5d_base_v059_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosem63_5d_base_v060_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosez_5d_base_v061_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosechg_5d_base_v062_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosediff_5d_base_v063_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclose_5d_base_v064_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclose2_5d_base_v065_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosem_5d_base_v066_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosem63_5d_base_v067_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosez_5d_base_v068_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosechg_5d_base_v069_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosediff_5d_base_v070_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclose_5d_base_v071_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclose2_5d_base_v072_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclosem_5d_base_v073_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclosem63_5d_base_v074_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclosez_5d_base_v075_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclose_5d_base_v001_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclose2_5d_base_v002_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosem_5d_base_v003_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosem63_5d_base_v004_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosez_5d_base_v005_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosechg_5d_base_v006_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_idxclosediff_5d_base_v007_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclose_5d_base_v008_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclose2_5d_base_v009_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosem_5d_base_v010_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosem63_5d_base_v011_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosez_5d_base_v012_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosechg_5d_base_v013_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosediff_5d_base_v014_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclose_5d_base_v015_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclose2_5d_base_v016_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosem_5d_base_v017_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosem63_5d_base_v018_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosez_5d_base_v019_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosechg_5d_base_v020_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosediff_5d_base_v021_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclose_5d_base_v022_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclose2_5d_base_v023_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosem_5d_base_v024_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosem63_5d_base_v025_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosez_5d_base_v026_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosechg_5d_base_v027_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosediff_5d_base_v028_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclose_5d_base_v029_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclose2_5d_base_v030_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosem_5d_base_v031_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosem63_5d_base_v032_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosez_5d_base_v033_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosechg_5d_base_v034_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosediff_5d_base_v035_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclose_5d_base_v036_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclose2_5d_base_v037_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosem_5d_base_v038_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosem63_5d_base_v039_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosez_5d_base_v040_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosechg_5d_base_v041_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosediff_5d_base_v042_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclose_5d_base_v043_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclose2_5d_base_v044_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosem_5d_base_v045_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosem63_5d_base_v046_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosez_5d_base_v047_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosechg_5d_base_v048_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosediff_5d_base_v049_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclose_5d_base_v050_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclose2_5d_base_v051_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosem_5d_base_v052_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosem63_5d_base_v053_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosez_5d_base_v054_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosechg_5d_base_v055_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosediff_5d_base_v056_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclose_5d_base_v057_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclose2_5d_base_v058_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosem_5d_base_v059_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosem63_5d_base_v060_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosez_5d_base_v061_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosechg_5d_base_v062_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosediff_5d_base_v063_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclose_5d_base_v064_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclose2_5d_base_v065_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosem_5d_base_v066_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosem63_5d_base_v067_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosez_5d_base_v068_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosechg_5d_base_v069_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosediff_5d_base_v070_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclose_5d_base_v071_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclose2_5d_base_v072_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclosem_5d_base_v073_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclosem63_5d_base_v074_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclosez_5d_base_v075_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F38_ENERGY_CAPEX_DISCIPLINE_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f38_energy_capex_discipline_base_001_075_claude: {n_features} features pass")
