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


def _f39_total_return_yield(dps, sharesbas, close, w):
    div_yield = dps / close.replace(0, np.nan)
    buyback_yield = -(sharesbas - sharesbas.shift(w)) / sharesbas.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    return (div_yield + buyback_yield) * close



def _f39_return_consistency(dps, sharesbas, w):
    div_g = dps.pct_change(periods=w).fillna(0.0)
    share_chg = -(sharesbas - sharesbas.shift(w)) / sharesbas.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    combined = div_g + share_chg
    sd = combined.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return combined.rolling(w, min_periods=max(1, w // 2)).mean() / sd



def _f39_capital_return_score(dps, sharesbas, w):
    div_g = dps.pct_change(periods=w).fillna(0.0)
    share_chg = -(sharesbas - sharesbas.shift(w)) / sharesbas.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    return (div_g.rolling(w, min_periods=max(1, w // 2)).mean()
            + share_chg.rolling(w, min_periods=max(1, w // 2)).mean())


# ===== features =====


def f39crq_f39_energy_capital_return_quality_total_return_yield_idxclose_5d_5d_jerk_v001_signal(dps, sharesbas, closeadj):
    base = (_f39_total_return_yield(dps, sharesbas, closeadj, 5)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_idxclose2_5d_10d_jerk_v002_signal(dps, sharesbas, closeadj):
    base = (_f39_total_return_yield(dps, sharesbas, closeadj, 5)) * closeadj * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_idxclosem_5d_21d_jerk_v003_signal(dps, sharesbas, closeadj):
    base = (_f39_total_return_yield(dps, sharesbas, closeadj, 5)) * _mean(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_idxclosem63_5d_42d_jerk_v004_signal(dps, sharesbas, closeadj):
    base = (_f39_total_return_yield(dps, sharesbas, closeadj, 5)) * _mean(closeadj, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_idxclosez_5d_63d_jerk_v005_signal(dps, sharesbas, closeadj):
    base = (_f39_total_return_yield(dps, sharesbas, closeadj, 5)) * _z(closeadj, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_idxclosechg_5d_126d_jerk_v006_signal(dps, sharesbas, closeadj):
    base = (_f39_total_return_yield(dps, sharesbas, closeadj, 5)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_idxclosediff_5d_189d_jerk_v007_signal(dps, sharesbas, closeadj):
    base = (_f39_total_return_yield(dps, sharesbas, closeadj, 5)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclose_5d_252d_jerk_v008_signal(dps, sharesbas, closeadj):
    base = (_mean(_f39_total_return_yield(dps, sharesbas, closeadj, 5), 5)) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclose2_5d_5d_jerk_v009_signal(dps, sharesbas, closeadj):
    base = (_mean(_f39_total_return_yield(dps, sharesbas, closeadj, 5), 5)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclosem_5d_10d_jerk_v010_signal(dps, sharesbas, closeadj):
    base = (_mean(_f39_total_return_yield(dps, sharesbas, closeadj, 5), 5)) * _mean(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclosem63_5d_21d_jerk_v011_signal(dps, sharesbas, closeadj):
    base = (_mean(_f39_total_return_yield(dps, sharesbas, closeadj, 5), 5)) * _mean(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclosez_5d_42d_jerk_v012_signal(dps, sharesbas, closeadj):
    base = (_mean(_f39_total_return_yield(dps, sharesbas, closeadj, 5), 5)) * _z(closeadj, 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclosechg_5d_63d_jerk_v013_signal(dps, sharesbas, closeadj):
    base = (_mean(_f39_total_return_yield(dps, sharesbas, closeadj, 5), 5)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclosediff_5d_126d_jerk_v014_signal(dps, sharesbas, closeadj):
    base = (_mean(_f39_total_return_yield(dps, sharesbas, closeadj, 5), 5)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclose_5d_189d_jerk_v015_signal(dps, sharesbas, closeadj):
    base = (_std(_f39_total_return_yield(dps, sharesbas, closeadj, 5), 5)) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclose2_5d_252d_jerk_v016_signal(dps, sharesbas, closeadj):
    base = (_std(_f39_total_return_yield(dps, sharesbas, closeadj, 5), 5)) * closeadj * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclosem_5d_5d_jerk_v017_signal(dps, sharesbas, closeadj):
    base = (_std(_f39_total_return_yield(dps, sharesbas, closeadj, 5), 5)) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclosem63_5d_10d_jerk_v018_signal(dps, sharesbas, closeadj):
    base = (_std(_f39_total_return_yield(dps, sharesbas, closeadj, 5), 5)) * _mean(closeadj, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclosez_5d_21d_jerk_v019_signal(dps, sharesbas, closeadj):
    base = (_std(_f39_total_return_yield(dps, sharesbas, closeadj, 5), 5)) * _z(closeadj, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclosechg_5d_42d_jerk_v020_signal(dps, sharesbas, closeadj):
    base = (_std(_f39_total_return_yield(dps, sharesbas, closeadj, 5), 5)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclosediff_5d_63d_jerk_v021_signal(dps, sharesbas, closeadj):
    base = (_std(_f39_total_return_yield(dps, sharesbas, closeadj, 5), 5)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_zxclose_5d_126d_jerk_v022_signal(dps, sharesbas, closeadj):
    base = (_z(_f39_total_return_yield(dps, sharesbas, closeadj, 5), 5)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_zxclose2_5d_189d_jerk_v023_signal(dps, sharesbas, closeadj):
    base = (_z(_f39_total_return_yield(dps, sharesbas, closeadj, 5), 5)) * closeadj * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_zxclosem_5d_252d_jerk_v024_signal(dps, sharesbas, closeadj):
    base = (_z(_f39_total_return_yield(dps, sharesbas, closeadj, 5), 5)) * _mean(closeadj, 21)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_zxclosem63_5d_5d_jerk_v025_signal(dps, sharesbas, closeadj):
    base = (_z(_f39_total_return_yield(dps, sharesbas, closeadj, 5), 5)) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_zxclosez_5d_10d_jerk_v026_signal(dps, sharesbas, closeadj):
    base = (_z(_f39_total_return_yield(dps, sharesbas, closeadj, 5), 5)) * _z(closeadj, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_zxclosechg_5d_21d_jerk_v027_signal(dps, sharesbas, closeadj):
    base = (_z(_f39_total_return_yield(dps, sharesbas, closeadj, 5), 5)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_zxclosediff_5d_42d_jerk_v028_signal(dps, sharesbas, closeadj):
    base = (_z(_f39_total_return_yield(dps, sharesbas, closeadj, 5), 5)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_emaxclose_5d_63d_jerk_v029_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_emaxclose2_5d_126d_jerk_v030_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * closeadj * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_emaxclosem_5d_189d_jerk_v031_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * _mean(closeadj, 21)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_emaxclosem63_5d_252d_jerk_v032_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * _mean(closeadj, 63)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_emaxclosez_5d_5d_jerk_v033_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * _z(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_emaxclosechg_5d_10d_jerk_v034_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_emaxclosediff_5d_21d_jerk_v035_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).ewm(span=5, adjust=False, min_periods=max(1, 5 // 2)).mean()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rmedianxclose_5d_42d_jerk_v036_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rmedianxclose2_5d_63d_jerk_v037_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rmedianxclosem_5d_126d_jerk_v038_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * _mean(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rmedianxclosem63_5d_189d_jerk_v039_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * _mean(closeadj, 63)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rmedianxclosez_5d_252d_jerk_v040_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * _z(closeadj, 252)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rmedianxclosechg_5d_5d_jerk_v041_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rmedianxclosediff_5d_10d_jerk_v042_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).median()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rmaxxclose_5d_21d_jerk_v043_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rmaxxclose2_5d_42d_jerk_v044_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rmaxxclosem_5d_63d_jerk_v045_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * _mean(closeadj, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rmaxxclosem63_5d_126d_jerk_v046_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * _mean(closeadj, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rmaxxclosez_5d_189d_jerk_v047_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * _z(closeadj, 252)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rmaxxclosechg_5d_252d_jerk_v048_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rmaxxclosediff_5d_5d_jerk_v049_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).max()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rminxclose_5d_10d_jerk_v050_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rminxclose2_5d_21d_jerk_v051_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rminxclosem_5d_42d_jerk_v052_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _mean(closeadj, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rminxclosem63_5d_63d_jerk_v053_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _mean(closeadj, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rminxclosez_5d_126d_jerk_v054_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _z(closeadj, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rminxclosechg_5d_189d_jerk_v055_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rminxclosediff_5d_252d_jerk_v056_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_skewxclose_5d_5d_jerk_v057_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_skewxclose2_5d_10d_jerk_v058_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * closeadj * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_skewxclosem_5d_21d_jerk_v059_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * _mean(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_skewxclosem63_5d_42d_jerk_v060_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * _mean(closeadj, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_skewxclosez_5d_63d_jerk_v061_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * _z(closeadj, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_skewxclosechg_5d_126d_jerk_v062_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_skewxclosediff_5d_189d_jerk_v063_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).skew()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_kurtxclose_5d_252d_jerk_v064_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_kurtxclose2_5d_5d_jerk_v065_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_kurtxclosem_5d_10d_jerk_v066_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * _mean(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_kurtxclosem63_5d_21d_jerk_v067_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * _mean(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_kurtxclosez_5d_42d_jerk_v068_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * _z(closeadj, 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_kurtxclosechg_5d_63d_jerk_v069_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_kurtxclosediff_5d_126d_jerk_v070_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).kurt()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_qhixclose_5d_189d_jerk_v071_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_qhixclose2_5d_252d_jerk_v072_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * closeadj * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_qhixclosem_5d_5d_jerk_v073_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_qhixclosem63_5d_10d_jerk_v074_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * _mean(closeadj, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_qhixclosez_5d_21d_jerk_v075_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * _z(closeadj, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_qhixclosechg_5d_42d_jerk_v076_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_qhixclosediff_5d_63d_jerk_v077_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.75)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_qloxclose_5d_126d_jerk_v078_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_qloxclose2_5d_189d_jerk_v079_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * closeadj * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_qloxclosem_5d_252d_jerk_v080_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * _mean(closeadj, 21)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_qloxclosem63_5d_5d_jerk_v081_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_qloxclosez_5d_10d_jerk_v082_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * _z(closeadj, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_qloxclosechg_5d_21d_jerk_v083_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_qloxclosediff_5d_42d_jerk_v084_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).quantile(0.25)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rangexclose_5d_63d_jerk_v085_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rangexclose2_5d_126d_jerk_v086_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rangexclosem_5d_189d_jerk_v087_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _mean(closeadj, 21)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rangexclosem63_5d_252d_jerk_v088_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _mean(closeadj, 63)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rangexclosez_5d_5d_jerk_v089_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * _z(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rangexclosechg_5d_10d_jerk_v090_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_rangexclosediff_5d_21d_jerk_v091_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f39_total_return_yield(dps, sharesbas, closeadj, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_squaredxclose_5d_42d_jerk_v092_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)) * (_f39_total_return_yield(dps, sharesbas, closeadj, 5)).abs()) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_squaredxclose2_5d_63d_jerk_v093_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)) * (_f39_total_return_yield(dps, sharesbas, closeadj, 5)).abs()) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_squaredxclosem_5d_126d_jerk_v094_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)) * (_f39_total_return_yield(dps, sharesbas, closeadj, 5)).abs()) * _mean(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_squaredxclosem63_5d_189d_jerk_v095_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)) * (_f39_total_return_yield(dps, sharesbas, closeadj, 5)).abs()) * _mean(closeadj, 63)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_squaredxclosez_5d_252d_jerk_v096_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)) * (_f39_total_return_yield(dps, sharesbas, closeadj, 5)).abs()) * _z(closeadj, 252)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_squaredxclosechg_5d_5d_jerk_v097_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)) * (_f39_total_return_yield(dps, sharesbas, closeadj, 5)).abs()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_squaredxclosediff_5d_10d_jerk_v098_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)) * (_f39_total_return_yield(dps, sharesbas, closeadj, 5)).abs()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_diffxclose_5d_21d_jerk_v099_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)) - (_f39_total_return_yield(dps, sharesbas, closeadj, 5)).shift(5)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_diffxclose2_5d_42d_jerk_v100_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)) - (_f39_total_return_yield(dps, sharesbas, closeadj, 5)).shift(5)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_diffxclosem_5d_63d_jerk_v101_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)) - (_f39_total_return_yield(dps, sharesbas, closeadj, 5)).shift(5)) * _mean(closeadj, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_diffxclosem63_5d_126d_jerk_v102_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)) - (_f39_total_return_yield(dps, sharesbas, closeadj, 5)).shift(5)) * _mean(closeadj, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_diffxclosez_5d_189d_jerk_v103_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)) - (_f39_total_return_yield(dps, sharesbas, closeadj, 5)).shift(5)) * _z(closeadj, 252)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_diffxclosechg_5d_252d_jerk_v104_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)) - (_f39_total_return_yield(dps, sharesbas, closeadj, 5)).shift(5)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_diffxclosediff_5d_5d_jerk_v105_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)) - (_f39_total_return_yield(dps, sharesbas, closeadj, 5)).shift(5)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_pctxclose_5d_10d_jerk_v106_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).pct_change(5)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_pctxclose2_5d_21d_jerk_v107_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).pct_change(5)) * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_pctxclosem_5d_42d_jerk_v108_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).pct_change(5)) * _mean(closeadj, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_pctxclosem63_5d_63d_jerk_v109_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).pct_change(5)) * _mean(closeadj, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_pctxclosez_5d_126d_jerk_v110_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).pct_change(5)) * _z(closeadj, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_pctxclosechg_5d_189d_jerk_v111_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).pct_change(5)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_pctxclosediff_5d_252d_jerk_v112_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).pct_change(5)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_signxclose_5d_5d_jerk_v113_signal(dps, sharesbas, closeadj):
    base = (np.sign(_f39_total_return_yield(dps, sharesbas, closeadj, 5))) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_signxclose2_5d_10d_jerk_v114_signal(dps, sharesbas, closeadj):
    base = (np.sign(_f39_total_return_yield(dps, sharesbas, closeadj, 5))) * closeadj * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_signxclosem_5d_21d_jerk_v115_signal(dps, sharesbas, closeadj):
    base = (np.sign(_f39_total_return_yield(dps, sharesbas, closeadj, 5))) * _mean(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_signxclosem63_5d_42d_jerk_v116_signal(dps, sharesbas, closeadj):
    base = (np.sign(_f39_total_return_yield(dps, sharesbas, closeadj, 5))) * _mean(closeadj, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_signxclosez_5d_63d_jerk_v117_signal(dps, sharesbas, closeadj):
    base = (np.sign(_f39_total_return_yield(dps, sharesbas, closeadj, 5))) * _z(closeadj, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_signxclosechg_5d_126d_jerk_v118_signal(dps, sharesbas, closeadj):
    base = (np.sign(_f39_total_return_yield(dps, sharesbas, closeadj, 5))) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_signxclosediff_5d_189d_jerk_v119_signal(dps, sharesbas, closeadj):
    base = (np.sign(_f39_total_return_yield(dps, sharesbas, closeadj, 5))) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_absxclose_5d_252d_jerk_v120_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).abs()) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_absxclose2_5d_5d_jerk_v121_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).abs()) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_absxclosem_5d_10d_jerk_v122_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).abs()) * _mean(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_absxclosem63_5d_21d_jerk_v123_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).abs()) * _mean(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_absxclosez_5d_42d_jerk_v124_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).abs()) * _z(closeadj, 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_absxclosechg_5d_63d_jerk_v125_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).abs()) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_absxclosediff_5d_126d_jerk_v126_signal(dps, sharesbas, closeadj):
    base = ((_f39_total_return_yield(dps, sharesbas, closeadj, 5)).abs()) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_idxclose_10d_189d_jerk_v127_signal(dps, sharesbas, closeadj):
    base = (_f39_total_return_yield(dps, sharesbas, closeadj, 10)) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_idxclose2_10d_252d_jerk_v128_signal(dps, sharesbas, closeadj):
    base = (_f39_total_return_yield(dps, sharesbas, closeadj, 10)) * closeadj * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_idxclosem_10d_5d_jerk_v129_signal(dps, sharesbas, closeadj):
    base = (_f39_total_return_yield(dps, sharesbas, closeadj, 10)) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_idxclosem63_10d_10d_jerk_v130_signal(dps, sharesbas, closeadj):
    base = (_f39_total_return_yield(dps, sharesbas, closeadj, 10)) * _mean(closeadj, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_idxclosez_10d_21d_jerk_v131_signal(dps, sharesbas, closeadj):
    base = (_f39_total_return_yield(dps, sharesbas, closeadj, 10)) * _z(closeadj, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_idxclosechg_10d_42d_jerk_v132_signal(dps, sharesbas, closeadj):
    base = (_f39_total_return_yield(dps, sharesbas, closeadj, 10)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_idxclosediff_10d_63d_jerk_v133_signal(dps, sharesbas, closeadj):
    base = (_f39_total_return_yield(dps, sharesbas, closeadj, 10)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclose_10d_126d_jerk_v134_signal(dps, sharesbas, closeadj):
    base = (_mean(_f39_total_return_yield(dps, sharesbas, closeadj, 10), 10)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclose2_10d_189d_jerk_v135_signal(dps, sharesbas, closeadj):
    base = (_mean(_f39_total_return_yield(dps, sharesbas, closeadj, 10), 10)) * closeadj * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclosem_10d_252d_jerk_v136_signal(dps, sharesbas, closeadj):
    base = (_mean(_f39_total_return_yield(dps, sharesbas, closeadj, 10), 10)) * _mean(closeadj, 21)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclosem63_10d_5d_jerk_v137_signal(dps, sharesbas, closeadj):
    base = (_mean(_f39_total_return_yield(dps, sharesbas, closeadj, 10), 10)) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclosez_10d_10d_jerk_v138_signal(dps, sharesbas, closeadj):
    base = (_mean(_f39_total_return_yield(dps, sharesbas, closeadj, 10), 10)) * _z(closeadj, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclosechg_10d_21d_jerk_v139_signal(dps, sharesbas, closeadj):
    base = (_mean(_f39_total_return_yield(dps, sharesbas, closeadj, 10), 10)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclosediff_10d_42d_jerk_v140_signal(dps, sharesbas, closeadj):
    base = (_mean(_f39_total_return_yield(dps, sharesbas, closeadj, 10), 10)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclose_10d_63d_jerk_v141_signal(dps, sharesbas, closeadj):
    base = (_std(_f39_total_return_yield(dps, sharesbas, closeadj, 10), 10)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclose2_10d_126d_jerk_v142_signal(dps, sharesbas, closeadj):
    base = (_std(_f39_total_return_yield(dps, sharesbas, closeadj, 10), 10)) * closeadj * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclosem_10d_189d_jerk_v143_signal(dps, sharesbas, closeadj):
    base = (_std(_f39_total_return_yield(dps, sharesbas, closeadj, 10), 10)) * _mean(closeadj, 21)
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclosem63_10d_252d_jerk_v144_signal(dps, sharesbas, closeadj):
    base = (_std(_f39_total_return_yield(dps, sharesbas, closeadj, 10), 10)) * _mean(closeadj, 63)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclosez_10d_5d_jerk_v145_signal(dps, sharesbas, closeadj):
    base = (_std(_f39_total_return_yield(dps, sharesbas, closeadj, 10), 10)) * _z(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclosechg_10d_10d_jerk_v146_signal(dps, sharesbas, closeadj):
    base = (_std(_f39_total_return_yield(dps, sharesbas, closeadj, 10), 10)) * closeadj.pct_change(21).fillna(0.0)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclosediff_10d_21d_jerk_v147_signal(dps, sharesbas, closeadj):
    base = (_std(_f39_total_return_yield(dps, sharesbas, closeadj, 10), 10)) * (closeadj - _mean(closeadj, 63))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_zxclose_10d_42d_jerk_v148_signal(dps, sharesbas, closeadj):
    base = (_z(_f39_total_return_yield(dps, sharesbas, closeadj, 10), 10)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_zxclose2_10d_63d_jerk_v149_signal(dps, sharesbas, closeadj):
    base = (_z(_f39_total_return_yield(dps, sharesbas, closeadj, 10), 10)) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f39crq_f39_energy_capital_return_quality_total_return_yield_zxclosem_10d_126d_jerk_v150_signal(dps, sharesbas, closeadj):
    base = (_z(_f39_total_return_yield(dps, sharesbas, closeadj, 10), 10)) * _mean(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f39crq_f39_energy_capital_return_quality_total_return_yield_idxclose_5d_5d_jerk_v001_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_idxclose2_5d_10d_jerk_v002_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_idxclosem_5d_21d_jerk_v003_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_idxclosem63_5d_42d_jerk_v004_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_idxclosez_5d_63d_jerk_v005_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_idxclosechg_5d_126d_jerk_v006_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_idxclosediff_5d_189d_jerk_v007_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclose_5d_252d_jerk_v008_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclose2_5d_5d_jerk_v009_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclosem_5d_10d_jerk_v010_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclosem63_5d_21d_jerk_v011_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclosez_5d_42d_jerk_v012_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclosechg_5d_63d_jerk_v013_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclosediff_5d_126d_jerk_v014_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclose_5d_189d_jerk_v015_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclose2_5d_252d_jerk_v016_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclosem_5d_5d_jerk_v017_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclosem63_5d_10d_jerk_v018_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclosez_5d_21d_jerk_v019_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclosechg_5d_42d_jerk_v020_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclosediff_5d_63d_jerk_v021_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_zxclose_5d_126d_jerk_v022_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_zxclose2_5d_189d_jerk_v023_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_zxclosem_5d_252d_jerk_v024_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_zxclosem63_5d_5d_jerk_v025_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_zxclosez_5d_10d_jerk_v026_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_zxclosechg_5d_21d_jerk_v027_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_zxclosediff_5d_42d_jerk_v028_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_emaxclose_5d_63d_jerk_v029_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_emaxclose2_5d_126d_jerk_v030_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_emaxclosem_5d_189d_jerk_v031_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_emaxclosem63_5d_252d_jerk_v032_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_emaxclosez_5d_5d_jerk_v033_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_emaxclosechg_5d_10d_jerk_v034_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_emaxclosediff_5d_21d_jerk_v035_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rmedianxclose_5d_42d_jerk_v036_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rmedianxclose2_5d_63d_jerk_v037_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rmedianxclosem_5d_126d_jerk_v038_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rmedianxclosem63_5d_189d_jerk_v039_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rmedianxclosez_5d_252d_jerk_v040_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rmedianxclosechg_5d_5d_jerk_v041_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rmedianxclosediff_5d_10d_jerk_v042_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rmaxxclose_5d_21d_jerk_v043_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rmaxxclose2_5d_42d_jerk_v044_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rmaxxclosem_5d_63d_jerk_v045_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rmaxxclosem63_5d_126d_jerk_v046_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rmaxxclosez_5d_189d_jerk_v047_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rmaxxclosechg_5d_252d_jerk_v048_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rmaxxclosediff_5d_5d_jerk_v049_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rminxclose_5d_10d_jerk_v050_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rminxclose2_5d_21d_jerk_v051_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rminxclosem_5d_42d_jerk_v052_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rminxclosem63_5d_63d_jerk_v053_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rminxclosez_5d_126d_jerk_v054_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rminxclosechg_5d_189d_jerk_v055_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rminxclosediff_5d_252d_jerk_v056_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_skewxclose_5d_5d_jerk_v057_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_skewxclose2_5d_10d_jerk_v058_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_skewxclosem_5d_21d_jerk_v059_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_skewxclosem63_5d_42d_jerk_v060_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_skewxclosez_5d_63d_jerk_v061_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_skewxclosechg_5d_126d_jerk_v062_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_skewxclosediff_5d_189d_jerk_v063_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_kurtxclose_5d_252d_jerk_v064_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_kurtxclose2_5d_5d_jerk_v065_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_kurtxclosem_5d_10d_jerk_v066_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_kurtxclosem63_5d_21d_jerk_v067_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_kurtxclosez_5d_42d_jerk_v068_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_kurtxclosechg_5d_63d_jerk_v069_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_kurtxclosediff_5d_126d_jerk_v070_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_qhixclose_5d_189d_jerk_v071_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_qhixclose2_5d_252d_jerk_v072_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_qhixclosem_5d_5d_jerk_v073_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_qhixclosem63_5d_10d_jerk_v074_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_qhixclosez_5d_21d_jerk_v075_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_qhixclosechg_5d_42d_jerk_v076_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_qhixclosediff_5d_63d_jerk_v077_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_qloxclose_5d_126d_jerk_v078_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_qloxclose2_5d_189d_jerk_v079_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_qloxclosem_5d_252d_jerk_v080_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_qloxclosem63_5d_5d_jerk_v081_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_qloxclosez_5d_10d_jerk_v082_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_qloxclosechg_5d_21d_jerk_v083_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_qloxclosediff_5d_42d_jerk_v084_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rangexclose_5d_63d_jerk_v085_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rangexclose2_5d_126d_jerk_v086_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rangexclosem_5d_189d_jerk_v087_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rangexclosem63_5d_252d_jerk_v088_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rangexclosez_5d_5d_jerk_v089_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rangexclosechg_5d_10d_jerk_v090_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_rangexclosediff_5d_21d_jerk_v091_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_squaredxclose_5d_42d_jerk_v092_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_squaredxclose2_5d_63d_jerk_v093_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_squaredxclosem_5d_126d_jerk_v094_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_squaredxclosem63_5d_189d_jerk_v095_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_squaredxclosez_5d_252d_jerk_v096_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_squaredxclosechg_5d_5d_jerk_v097_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_squaredxclosediff_5d_10d_jerk_v098_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_diffxclose_5d_21d_jerk_v099_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_diffxclose2_5d_42d_jerk_v100_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_diffxclosem_5d_63d_jerk_v101_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_diffxclosem63_5d_126d_jerk_v102_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_diffxclosez_5d_189d_jerk_v103_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_diffxclosechg_5d_252d_jerk_v104_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_diffxclosediff_5d_5d_jerk_v105_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_pctxclose_5d_10d_jerk_v106_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_pctxclose2_5d_21d_jerk_v107_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_pctxclosem_5d_42d_jerk_v108_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_pctxclosem63_5d_63d_jerk_v109_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_pctxclosez_5d_126d_jerk_v110_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_pctxclosechg_5d_189d_jerk_v111_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_pctxclosediff_5d_252d_jerk_v112_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_signxclose_5d_5d_jerk_v113_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_signxclose2_5d_10d_jerk_v114_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_signxclosem_5d_21d_jerk_v115_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_signxclosem63_5d_42d_jerk_v116_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_signxclosez_5d_63d_jerk_v117_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_signxclosechg_5d_126d_jerk_v118_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_signxclosediff_5d_189d_jerk_v119_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_absxclose_5d_252d_jerk_v120_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_absxclose2_5d_5d_jerk_v121_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_absxclosem_5d_10d_jerk_v122_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_absxclosem63_5d_21d_jerk_v123_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_absxclosez_5d_42d_jerk_v124_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_absxclosechg_5d_63d_jerk_v125_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_absxclosediff_5d_126d_jerk_v126_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_idxclose_10d_189d_jerk_v127_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_idxclose2_10d_252d_jerk_v128_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_idxclosem_10d_5d_jerk_v129_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_idxclosem63_10d_10d_jerk_v130_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_idxclosez_10d_21d_jerk_v131_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_idxclosechg_10d_42d_jerk_v132_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_idxclosediff_10d_63d_jerk_v133_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclose_10d_126d_jerk_v134_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclose2_10d_189d_jerk_v135_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclosem_10d_252d_jerk_v136_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclosem63_10d_5d_jerk_v137_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclosez_10d_10d_jerk_v138_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclosechg_10d_21d_jerk_v139_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_meanxclosediff_10d_42d_jerk_v140_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclose_10d_63d_jerk_v141_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclose2_10d_126d_jerk_v142_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclosem_10d_189d_jerk_v143_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclosem63_10d_252d_jerk_v144_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclosez_10d_5d_jerk_v145_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclosechg_10d_10d_jerk_v146_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_stdxclosediff_10d_21d_jerk_v147_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_zxclose_10d_42d_jerk_v148_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_zxclose2_10d_63d_jerk_v149_signal,
    f39crq_f39_energy_capital_return_quality_total_return_yield_zxclosem_10d_126d_jerk_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F39_ENERGY_CAPITAL_RETURN_QUALITY_REGISTRY_JERK_001_150 = REGISTRY


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
    domain_primitives = ("_f39_total_return_yield", "_f39_return_consistency", "_f39_capital_return_score",)
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
    print(f"OK f39_energy_capital_return_quality_3rd_derivatives_001_150_claude: {n_features} features pass")
