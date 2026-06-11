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


def _f37_dps_growth(dps, w):
    base = dps.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    return (dps - dps.shift(w)) / base.abs()



def _f37_dividend_compound(dps, w):
    g = dps.pct_change(periods=w).fillna(0.0)
    return dps * (1.0 + g.rolling(w, min_periods=max(1, w // 2)).mean())



def _f37_dividend_coverage(dps, eps, w):
    base = dps.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    return (eps - dps) / base.abs()


# ===== features =====


def f37edg_f37_energy_dividend_growth_dps_growth_idxclose_5d_base_v001_signal(dps, closeadj):
    result = (_f37_dps_growth(dps, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_idxclose2_5d_base_v002_signal(dps, closeadj):
    result = (_f37_dps_growth(dps, 5)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_idxclosem_5d_base_v003_signal(dps, closeadj):
    result = (_f37_dps_growth(dps, 5)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_idxclosem63_5d_base_v004_signal(dps, closeadj):
    result = (_f37_dps_growth(dps, 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_idxclosez_5d_base_v005_signal(dps, closeadj):
    result = (_f37_dps_growth(dps, 5)) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_idxclosechg_5d_base_v006_signal(dps, closeadj):
    result = (_f37_dps_growth(dps, 5)) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_idxclosediff_5d_base_v007_signal(dps, closeadj):
    result = (_f37_dps_growth(dps, 5)) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_meanxclose_5d_base_v008_signal(dps, closeadj):
    result = (_mean(_f37_dps_growth(dps, 5), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_meanxclose2_5d_base_v009_signal(dps, closeadj):
    result = (_mean(_f37_dps_growth(dps, 5), 5)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_meanxclosem_5d_base_v010_signal(dps, closeadj):
    result = (_mean(_f37_dps_growth(dps, 5), 5)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_meanxclosem63_5d_base_v011_signal(dps, closeadj):
    result = (_mean(_f37_dps_growth(dps, 5), 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_meanxclosez_5d_base_v012_signal(dps, closeadj):
    result = (_mean(_f37_dps_growth(dps, 5), 5)) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_meanxclosechg_5d_base_v013_signal(dps, closeadj):
    result = (_mean(_f37_dps_growth(dps, 5), 5)) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_meanxclosediff_5d_base_v014_signal(dps, closeadj):
    result = (_mean(_f37_dps_growth(dps, 5), 5)) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_stdxclose_5d_base_v015_signal(dps, closeadj):
    result = (_std(_f37_dps_growth(dps, 5), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_stdxclose2_5d_base_v016_signal(dps, closeadj):
    result = (_std(_f37_dps_growth(dps, 5), 5)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_stdxclosem_5d_base_v017_signal(dps, closeadj):
    result = (_std(_f37_dps_growth(dps, 5), 5)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_stdxclosem63_5d_base_v018_signal(dps, closeadj):
    result = (_std(_f37_dps_growth(dps, 5), 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_stdxclosez_5d_base_v019_signal(dps, closeadj):
    result = (_std(_f37_dps_growth(dps, 5), 5)) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_stdxclosechg_5d_base_v020_signal(dps, closeadj):
    result = (_std(_f37_dps_growth(dps, 5), 5)) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_stdxclosediff_5d_base_v021_signal(dps, closeadj):
    result = (_std(_f37_dps_growth(dps, 5), 5)) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_zxclose_5d_base_v022_signal(dps, closeadj):
    result = (_z(_f37_dps_growth(dps, 5), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_zxclose2_5d_base_v023_signal(dps, closeadj):
    result = (_z(_f37_dps_growth(dps, 5), 5)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_zxclosem_5d_base_v024_signal(dps, closeadj):
    result = (_z(_f37_dps_growth(dps, 5), 5)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_zxclosem63_5d_base_v025_signal(dps, closeadj):
    result = (_z(_f37_dps_growth(dps, 5), 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_zxclosez_5d_base_v026_signal(dps, closeadj):
    result = (_z(_f37_dps_growth(dps, 5), 5)) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_zxclosechg_5d_base_v027_signal(dps, closeadj):
    result = (_z(_f37_dps_growth(dps, 5), 5)) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_zxclosediff_5d_base_v028_signal(dps, closeadj):
    result = (_z(_f37_dps_growth(dps, 5), 5)) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_emaxclose_5d_base_v029_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_emaxclose2_5d_base_v030_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_emaxclosem_5d_base_v031_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_emaxclosem63_5d_base_v032_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_emaxclosez_5d_base_v033_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_emaxclosechg_5d_base_v034_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_emaxclosediff_5d_base_v035_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_rmedianxclose_5d_base_v036_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_rmedianxclose2_5d_base_v037_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_rmedianxclosem_5d_base_v038_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_rmedianxclosem63_5d_base_v039_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_rmedianxclosez_5d_base_v040_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_rmedianxclosechg_5d_base_v041_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_rmedianxclosediff_5d_base_v042_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_rmaxxclose_5d_base_v043_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_rmaxxclose2_5d_base_v044_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_rmaxxclosem_5d_base_v045_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_rmaxxclosem63_5d_base_v046_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_rmaxxclosez_5d_base_v047_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_rmaxxclosechg_5d_base_v048_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_rmaxxclosediff_5d_base_v049_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_rminxclose_5d_base_v050_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_rminxclose2_5d_base_v051_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_rminxclosem_5d_base_v052_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_rminxclosem63_5d_base_v053_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_rminxclosez_5d_base_v054_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_rminxclosechg_5d_base_v055_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_rminxclosediff_5d_base_v056_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_skewxclose_5d_base_v057_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_skewxclose2_5d_base_v058_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_skewxclosem_5d_base_v059_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_skewxclosem63_5d_base_v060_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_skewxclosez_5d_base_v061_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_skewxclosechg_5d_base_v062_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_skewxclosediff_5d_base_v063_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_kurtxclose_5d_base_v064_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_kurtxclose2_5d_base_v065_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_kurtxclosem_5d_base_v066_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_kurtxclosem63_5d_base_v067_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_kurtxclosez_5d_base_v068_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_kurtxclosechg_5d_base_v069_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_kurtxclosediff_5d_base_v070_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_qhixclose_5d_base_v071_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_qhixclose2_5d_base_v072_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_qhixclosem_5d_base_v073_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_qhixclosem63_5d_base_v074_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f37edg_f37_energy_dividend_growth_dps_growth_qhixclosez_5d_base_v075_signal(dps, closeadj):
    result = ((_f37_dps_growth(dps, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f37edg_f37_energy_dividend_growth_dps_growth_idxclose_5d_base_v001_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_idxclose2_5d_base_v002_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_idxclosem_5d_base_v003_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_idxclosem63_5d_base_v004_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_idxclosez_5d_base_v005_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_idxclosechg_5d_base_v006_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_idxclosediff_5d_base_v007_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_meanxclose_5d_base_v008_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_meanxclose2_5d_base_v009_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_meanxclosem_5d_base_v010_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_meanxclosem63_5d_base_v011_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_meanxclosez_5d_base_v012_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_meanxclosechg_5d_base_v013_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_meanxclosediff_5d_base_v014_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_stdxclose_5d_base_v015_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_stdxclose2_5d_base_v016_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_stdxclosem_5d_base_v017_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_stdxclosem63_5d_base_v018_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_stdxclosez_5d_base_v019_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_stdxclosechg_5d_base_v020_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_stdxclosediff_5d_base_v021_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_zxclose_5d_base_v022_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_zxclose2_5d_base_v023_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_zxclosem_5d_base_v024_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_zxclosem63_5d_base_v025_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_zxclosez_5d_base_v026_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_zxclosechg_5d_base_v027_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_zxclosediff_5d_base_v028_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_emaxclose_5d_base_v029_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_emaxclose2_5d_base_v030_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_emaxclosem_5d_base_v031_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_emaxclosem63_5d_base_v032_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_emaxclosez_5d_base_v033_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_emaxclosechg_5d_base_v034_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_emaxclosediff_5d_base_v035_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_rmedianxclose_5d_base_v036_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_rmedianxclose2_5d_base_v037_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_rmedianxclosem_5d_base_v038_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_rmedianxclosem63_5d_base_v039_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_rmedianxclosez_5d_base_v040_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_rmedianxclosechg_5d_base_v041_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_rmedianxclosediff_5d_base_v042_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_rmaxxclose_5d_base_v043_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_rmaxxclose2_5d_base_v044_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_rmaxxclosem_5d_base_v045_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_rmaxxclosem63_5d_base_v046_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_rmaxxclosez_5d_base_v047_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_rmaxxclosechg_5d_base_v048_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_rmaxxclosediff_5d_base_v049_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_rminxclose_5d_base_v050_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_rminxclose2_5d_base_v051_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_rminxclosem_5d_base_v052_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_rminxclosem63_5d_base_v053_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_rminxclosez_5d_base_v054_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_rminxclosechg_5d_base_v055_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_rminxclosediff_5d_base_v056_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_skewxclose_5d_base_v057_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_skewxclose2_5d_base_v058_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_skewxclosem_5d_base_v059_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_skewxclosem63_5d_base_v060_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_skewxclosez_5d_base_v061_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_skewxclosechg_5d_base_v062_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_skewxclosediff_5d_base_v063_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_kurtxclose_5d_base_v064_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_kurtxclose2_5d_base_v065_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_kurtxclosem_5d_base_v066_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_kurtxclosem63_5d_base_v067_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_kurtxclosez_5d_base_v068_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_kurtxclosechg_5d_base_v069_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_kurtxclosediff_5d_base_v070_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_qhixclose_5d_base_v071_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_qhixclose2_5d_base_v072_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_qhixclosem_5d_base_v073_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_qhixclosem63_5d_base_v074_signal,
    f37edg_f37_energy_dividend_growth_dps_growth_qhixclosez_5d_base_v075_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F37_ENERGY_DIVIDEND_GROWTH_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f37_dps_growth", "_f37_dividend_compound", "_f37_dividend_coverage",)
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
    print(f"OK f37_energy_dividend_growth_base_001_075_claude: {n_features} features pass")
