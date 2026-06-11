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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    denom = s.shift(w).abs().replace(0, np.nan)
    return s.diff(periods=w) / denom


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives (f13 aerospace_oem_cycle_position) =====
def _f13_revenue_inflection(revenue, w):
    sm = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    short = revenue.rolling(max(1, w // 3), min_periods=max(1, w // 6)).mean()
    return (short - sm) / sm.replace(0, np.nan).abs()


def _f13_cycle_trough_indicator(revenue, w):
    mn = revenue.rolling(w, min_periods=max(1, w // 2)).min()
    return (revenue - mn) / mn.replace(0, np.nan).abs()


def _f13_recovery_strength(revenue, ebitda, w):
    rg = revenue.pct_change(periods=max(1, w // 2))
    eg = ebitda.pct_change(periods=max(1, w // 2))
    return (rg + eg) * 0.5


def aoc_f13_aerospace_oem_cycle_position_revinfl_5d_rm_ca_sl5_v001_signal(closeadj, revenue):
    base = (_mean(_f13_revenue_inflection(revenue, 5), 5)) * (closeadj)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_5d_rm_lca_sl10_v002_signal(closeadj, revenue):
    base = (_mean(_f13_cycle_trough_indicator(revenue, 5), 5)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_5d_rm_mca_sl21_v003_signal(closeadj, ebitda, revenue):
    base = (_mean(_f13_recovery_strength(revenue, ebitda, 5), 5)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_10d_rm_rrn_sl63_v004_signal(closeadj, revenue):
    base = (_mean(_f13_revenue_inflection(revenue, 10), 10)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_10d_rm_ca_sl126_v005_signal(closeadj, revenue):
    base = (_mean(_f13_cycle_trough_indicator(revenue, 10), 10)) * (closeadj)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_10d_rm_lca_sl252_v006_signal(closeadj, ebitda, revenue):
    base = (_mean(_f13_recovery_strength(revenue, ebitda, 10), 10)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_21d_rm_mca_sl5_v007_signal(closeadj, revenue):
    base = (_mean(_f13_revenue_inflection(revenue, 21), 21)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_21d_rm_rrn_sl10_v008_signal(closeadj, revenue):
    base = (_mean(_f13_cycle_trough_indicator(revenue, 21), 21)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_21d_rm_ca_sl21_v009_signal(closeadj, ebitda, revenue):
    base = (_mean(_f13_recovery_strength(revenue, ebitda, 21), 21)) * (closeadj)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_42d_rm_lca_sl63_v010_signal(closeadj, revenue):
    base = (_mean(_f13_revenue_inflection(revenue, 42), 21)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_42d_rm_mca_sl126_v011_signal(closeadj, revenue):
    base = (_mean(_f13_cycle_trough_indicator(revenue, 42), 21)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_42d_rm_rrn_sl252_v012_signal(closeadj, ebitda, revenue):
    base = (_mean(_f13_recovery_strength(revenue, ebitda, 42), 21)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_63d_rm_ca_sl5_v013_signal(closeadj, revenue):
    base = (_mean(_f13_revenue_inflection(revenue, 63), 42)) * (closeadj)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_63d_rm_lca_sl10_v014_signal(closeadj, revenue):
    base = (_mean(_f13_cycle_trough_indicator(revenue, 63), 42)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_63d_rm_mca_sl21_v015_signal(closeadj, ebitda, revenue):
    base = (_mean(_f13_recovery_strength(revenue, ebitda, 63), 42)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_126d_rm_rrn_sl63_v016_signal(closeadj, revenue):
    base = (_mean(_f13_revenue_inflection(revenue, 126), 63)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_126d_rm_ca_sl126_v017_signal(closeadj, revenue):
    base = (_mean(_f13_cycle_trough_indicator(revenue, 126), 63)) * (closeadj)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_126d_rm_lca_sl252_v018_signal(closeadj, ebitda, revenue):
    base = (_mean(_f13_recovery_strength(revenue, ebitda, 126), 63)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_252d_rm_mca_sl5_v019_signal(closeadj, revenue):
    base = (_mean(_f13_revenue_inflection(revenue, 252), 126)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_252d_rm_rrn_sl10_v020_signal(closeadj, revenue):
    base = (_mean(_f13_cycle_trough_indicator(revenue, 252), 126)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_252d_rm_ca_sl21_v021_signal(closeadj, ebitda, revenue):
    base = (_mean(_f13_recovery_strength(revenue, ebitda, 252), 126)) * (closeadj)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_5d_rs_lca_sl63_v022_signal(closeadj, revenue):
    base = (_std(_f13_revenue_inflection(revenue, 5), 5)) * (np.log1p(closeadj.abs()))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_5d_rs_mca_sl126_v023_signal(closeadj, revenue):
    base = (_std(_f13_cycle_trough_indicator(revenue, 5), 5)) * (_mean(closeadj, 21))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_5d_rs_rrn_sl252_v024_signal(closeadj, ebitda, revenue):
    base = (_std(_f13_recovery_strength(revenue, ebitda, 5), 5)) * ((revenue / _mean(revenue, 63)))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_10d_rs_ca_sl5_v025_signal(closeadj, revenue):
    base = (_std(_f13_revenue_inflection(revenue, 10), 10)) * (closeadj)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_10d_rs_lca_sl10_v026_signal(closeadj, revenue):
    base = (_std(_f13_cycle_trough_indicator(revenue, 10), 10)) * (np.log1p(closeadj.abs()))
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_10d_rs_mca_sl21_v027_signal(closeadj, ebitda, revenue):
    base = (_std(_f13_recovery_strength(revenue, ebitda, 10), 10)) * (_mean(closeadj, 21))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_21d_rs_rrn_sl63_v028_signal(closeadj, revenue):
    base = (_std(_f13_revenue_inflection(revenue, 21), 21)) * ((revenue / _mean(revenue, 63)))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_21d_rs_ca_sl126_v029_signal(closeadj, revenue):
    base = (_std(_f13_cycle_trough_indicator(revenue, 21), 21)) * (closeadj)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_21d_rs_lca_sl252_v030_signal(closeadj, ebitda, revenue):
    base = (_std(_f13_recovery_strength(revenue, ebitda, 21), 21)) * (np.log1p(closeadj.abs()))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_42d_rs_mca_sl5_v031_signal(closeadj, revenue):
    base = (_std(_f13_revenue_inflection(revenue, 42), 21)) * (_mean(closeadj, 21))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_42d_rs_rrn_sl10_v032_signal(closeadj, revenue):
    base = (_std(_f13_cycle_trough_indicator(revenue, 42), 21)) * ((revenue / _mean(revenue, 63)))
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_42d_rs_ca_sl21_v033_signal(closeadj, ebitda, revenue):
    base = (_std(_f13_recovery_strength(revenue, ebitda, 42), 21)) * (closeadj)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_63d_rs_lca_sl63_v034_signal(closeadj, revenue):
    base = (_std(_f13_revenue_inflection(revenue, 63), 42)) * (np.log1p(closeadj.abs()))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_63d_rs_mca_sl126_v035_signal(closeadj, revenue):
    base = (_std(_f13_cycle_trough_indicator(revenue, 63), 42)) * (_mean(closeadj, 21))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_63d_rs_rrn_sl252_v036_signal(closeadj, ebitda, revenue):
    base = (_std(_f13_recovery_strength(revenue, ebitda, 63), 42)) * ((revenue / _mean(revenue, 63)))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_126d_rs_ca_sl5_v037_signal(closeadj, revenue):
    base = (_std(_f13_revenue_inflection(revenue, 126), 63)) * (closeadj)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_126d_rs_lca_sl10_v038_signal(closeadj, revenue):
    base = (_std(_f13_cycle_trough_indicator(revenue, 126), 63)) * (np.log1p(closeadj.abs()))
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_126d_rs_mca_sl21_v039_signal(closeadj, ebitda, revenue):
    base = (_std(_f13_recovery_strength(revenue, ebitda, 126), 63)) * (_mean(closeadj, 21))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_252d_rs_rrn_sl63_v040_signal(closeadj, revenue):
    base = (_std(_f13_revenue_inflection(revenue, 252), 126)) * ((revenue / _mean(revenue, 63)))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_252d_rs_ca_sl126_v041_signal(closeadj, revenue):
    base = (_std(_f13_cycle_trough_indicator(revenue, 252), 126)) * (closeadj)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_252d_rs_lca_sl252_v042_signal(closeadj, ebitda, revenue):
    base = (_std(_f13_recovery_strength(revenue, ebitda, 252), 126)) * (np.log1p(closeadj.abs()))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_5d_em_mca_sl5_v043_signal(closeadj, revenue):
    base = (_ema(_f13_revenue_inflection(revenue, 5), 5)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_5d_em_rrn_sl10_v044_signal(closeadj, revenue):
    base = (_ema(_f13_cycle_trough_indicator(revenue, 5), 5)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_5d_em_ca_sl21_v045_signal(closeadj, ebitda, revenue):
    base = (_ema(_f13_recovery_strength(revenue, ebitda, 5), 5)) * (closeadj)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_10d_em_lca_sl63_v046_signal(closeadj, revenue):
    base = (_ema(_f13_revenue_inflection(revenue, 10), 10)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_10d_em_mca_sl126_v047_signal(closeadj, revenue):
    base = (_ema(_f13_cycle_trough_indicator(revenue, 10), 10)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_10d_em_rrn_sl252_v048_signal(closeadj, ebitda, revenue):
    base = (_ema(_f13_recovery_strength(revenue, ebitda, 10), 10)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_21d_em_ca_sl5_v049_signal(closeadj, revenue):
    base = (_ema(_f13_revenue_inflection(revenue, 21), 21)) * (closeadj)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_21d_em_lca_sl10_v050_signal(closeadj, revenue):
    base = (_ema(_f13_cycle_trough_indicator(revenue, 21), 21)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_21d_em_mca_sl21_v051_signal(closeadj, ebitda, revenue):
    base = (_ema(_f13_recovery_strength(revenue, ebitda, 21), 21)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_42d_em_rrn_sl63_v052_signal(closeadj, revenue):
    base = (_ema(_f13_revenue_inflection(revenue, 42), 21)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_42d_em_ca_sl126_v053_signal(closeadj, revenue):
    base = (_ema(_f13_cycle_trough_indicator(revenue, 42), 21)) * (closeadj)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_42d_em_lca_sl252_v054_signal(closeadj, ebitda, revenue):
    base = (_ema(_f13_recovery_strength(revenue, ebitda, 42), 21)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_63d_em_mca_sl5_v055_signal(closeadj, revenue):
    base = (_ema(_f13_revenue_inflection(revenue, 63), 42)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_63d_em_rrn_sl10_v056_signal(closeadj, revenue):
    base = (_ema(_f13_cycle_trough_indicator(revenue, 63), 42)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_63d_em_ca_sl21_v057_signal(closeadj, ebitda, revenue):
    base = (_ema(_f13_recovery_strength(revenue, ebitda, 63), 42)) * (closeadj)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_126d_em_lca_sl63_v058_signal(closeadj, revenue):
    base = (_ema(_f13_revenue_inflection(revenue, 126), 63)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_126d_em_mca_sl126_v059_signal(closeadj, revenue):
    base = (_ema(_f13_cycle_trough_indicator(revenue, 126), 63)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_126d_em_rrn_sl252_v060_signal(closeadj, ebitda, revenue):
    base = (_ema(_f13_recovery_strength(revenue, ebitda, 126), 63)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_252d_em_ca_sl5_v061_signal(closeadj, revenue):
    base = (_ema(_f13_revenue_inflection(revenue, 252), 126)) * (closeadj)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_252d_em_lca_sl10_v062_signal(closeadj, revenue):
    base = (_ema(_f13_cycle_trough_indicator(revenue, 252), 126)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_252d_em_mca_sl21_v063_signal(closeadj, ebitda, revenue):
    base = (_ema(_f13_recovery_strength(revenue, ebitda, 252), 126)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_5d_zw_rrn_sl63_v064_signal(closeadj, revenue):
    base = (_z(_f13_revenue_inflection(revenue, 5), 5)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_5d_zw_ca_sl126_v065_signal(closeadj, revenue):
    base = (_z(_f13_cycle_trough_indicator(revenue, 5), 5)) * (closeadj)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_5d_zw_lca_sl252_v066_signal(closeadj, ebitda, revenue):
    base = (_z(_f13_recovery_strength(revenue, ebitda, 5), 5)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_10d_zw_mca_sl5_v067_signal(closeadj, revenue):
    base = (_z(_f13_revenue_inflection(revenue, 10), 10)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_10d_zw_rrn_sl10_v068_signal(closeadj, revenue):
    base = (_z(_f13_cycle_trough_indicator(revenue, 10), 10)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_10d_zw_ca_sl21_v069_signal(closeadj, ebitda, revenue):
    base = (_z(_f13_recovery_strength(revenue, ebitda, 10), 10)) * (closeadj)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_21d_zw_lca_sl63_v070_signal(closeadj, revenue):
    base = (_z(_f13_revenue_inflection(revenue, 21), 21)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_21d_zw_mca_sl126_v071_signal(closeadj, revenue):
    base = (_z(_f13_cycle_trough_indicator(revenue, 21), 21)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_21d_zw_rrn_sl252_v072_signal(closeadj, ebitda, revenue):
    base = (_z(_f13_recovery_strength(revenue, ebitda, 21), 21)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_42d_zw_ca_sl5_v073_signal(closeadj, revenue):
    base = (_z(_f13_revenue_inflection(revenue, 42), 21)) * (closeadj)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_42d_zw_lca_sl10_v074_signal(closeadj, revenue):
    base = (_z(_f13_cycle_trough_indicator(revenue, 42), 21)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_42d_zw_mca_sl21_v075_signal(closeadj, ebitda, revenue):
    base = (_z(_f13_recovery_strength(revenue, ebitda, 42), 21)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_63d_zw_rrn_sl63_v076_signal(closeadj, revenue):
    base = (_z(_f13_revenue_inflection(revenue, 63), 42)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_63d_zw_ca_sl126_v077_signal(closeadj, revenue):
    base = (_z(_f13_cycle_trough_indicator(revenue, 63), 42)) * (closeadj)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_63d_zw_lca_sl252_v078_signal(closeadj, ebitda, revenue):
    base = (_z(_f13_recovery_strength(revenue, ebitda, 63), 42)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_126d_zw_mca_sl5_v079_signal(closeadj, revenue):
    base = (_z(_f13_revenue_inflection(revenue, 126), 63)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_126d_zw_rrn_sl10_v080_signal(closeadj, revenue):
    base = (_z(_f13_cycle_trough_indicator(revenue, 126), 63)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_126d_zw_ca_sl21_v081_signal(closeadj, ebitda, revenue):
    base = (_z(_f13_recovery_strength(revenue, ebitda, 126), 63)) * (closeadj)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_252d_zw_lca_sl63_v082_signal(closeadj, revenue):
    base = (_z(_f13_revenue_inflection(revenue, 252), 126)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_252d_zw_mca_sl126_v083_signal(closeadj, revenue):
    base = (_z(_f13_cycle_trough_indicator(revenue, 252), 126)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_252d_zw_rrn_sl252_v084_signal(closeadj, ebitda, revenue):
    base = (_z(_f13_recovery_strength(revenue, ebitda, 252), 126)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_5d_lgm_ca_sl5_v085_signal(closeadj, revenue):
    base = (np.log1p(_mean(_f13_revenue_inflection(revenue, 5), 5).abs())) * (closeadj)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_5d_lgm_lca_sl10_v086_signal(closeadj, revenue):
    base = (np.log1p(_mean(_f13_cycle_trough_indicator(revenue, 5), 5).abs())) * (np.log1p(closeadj.abs()))
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_5d_lgm_mca_sl21_v087_signal(closeadj, ebitda, revenue):
    base = (np.log1p(_mean(_f13_recovery_strength(revenue, ebitda, 5), 5).abs())) * (_mean(closeadj, 21))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_10d_lgm_rrn_sl63_v088_signal(closeadj, revenue):
    base = (np.log1p(_mean(_f13_revenue_inflection(revenue, 10), 10).abs())) * ((revenue / _mean(revenue, 63)))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_10d_lgm_ca_sl126_v089_signal(closeadj, revenue):
    base = (np.log1p(_mean(_f13_cycle_trough_indicator(revenue, 10), 10).abs())) * (closeadj)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_10d_lgm_lca_sl252_v090_signal(closeadj, ebitda, revenue):
    base = (np.log1p(_mean(_f13_recovery_strength(revenue, ebitda, 10), 10).abs())) * (np.log1p(closeadj.abs()))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_21d_lgm_mca_sl5_v091_signal(closeadj, revenue):
    base = (np.log1p(_mean(_f13_revenue_inflection(revenue, 21), 21).abs())) * (_mean(closeadj, 21))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_21d_lgm_rrn_sl10_v092_signal(closeadj, revenue):
    base = (np.log1p(_mean(_f13_cycle_trough_indicator(revenue, 21), 21).abs())) * ((revenue / _mean(revenue, 63)))
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_21d_lgm_ca_sl21_v093_signal(closeadj, ebitda, revenue):
    base = (np.log1p(_mean(_f13_recovery_strength(revenue, ebitda, 21), 21).abs())) * (closeadj)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_42d_lgm_lca_sl63_v094_signal(closeadj, revenue):
    base = (np.log1p(_mean(_f13_revenue_inflection(revenue, 42), 21).abs())) * (np.log1p(closeadj.abs()))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_42d_lgm_mca_sl126_v095_signal(closeadj, revenue):
    base = (np.log1p(_mean(_f13_cycle_trough_indicator(revenue, 42), 21).abs())) * (_mean(closeadj, 21))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_42d_lgm_rrn_sl252_v096_signal(closeadj, ebitda, revenue):
    base = (np.log1p(_mean(_f13_recovery_strength(revenue, ebitda, 42), 21).abs())) * ((revenue / _mean(revenue, 63)))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_63d_lgm_ca_sl5_v097_signal(closeadj, revenue):
    base = (np.log1p(_mean(_f13_revenue_inflection(revenue, 63), 42).abs())) * (closeadj)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_63d_lgm_lca_sl10_v098_signal(closeadj, revenue):
    base = (np.log1p(_mean(_f13_cycle_trough_indicator(revenue, 63), 42).abs())) * (np.log1p(closeadj.abs()))
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_63d_lgm_mca_sl21_v099_signal(closeadj, ebitda, revenue):
    base = (np.log1p(_mean(_f13_recovery_strength(revenue, ebitda, 63), 42).abs())) * (_mean(closeadj, 21))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_126d_lgm_rrn_sl63_v100_signal(closeadj, revenue):
    base = (np.log1p(_mean(_f13_revenue_inflection(revenue, 126), 63).abs())) * ((revenue / _mean(revenue, 63)))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_126d_lgm_ca_sl126_v101_signal(closeadj, revenue):
    base = (np.log1p(_mean(_f13_cycle_trough_indicator(revenue, 126), 63).abs())) * (closeadj)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_126d_lgm_lca_sl252_v102_signal(closeadj, ebitda, revenue):
    base = (np.log1p(_mean(_f13_recovery_strength(revenue, ebitda, 126), 63).abs())) * (np.log1p(closeadj.abs()))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_252d_lgm_mca_sl5_v103_signal(closeadj, revenue):
    base = (np.log1p(_mean(_f13_revenue_inflection(revenue, 252), 126).abs())) * (_mean(closeadj, 21))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_252d_lgm_rrn_sl10_v104_signal(closeadj, revenue):
    base = (np.log1p(_mean(_f13_cycle_trough_indicator(revenue, 252), 126).abs())) * ((revenue / _mean(revenue, 63)))
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_252d_lgm_ca_sl21_v105_signal(closeadj, ebitda, revenue):
    base = (np.log1p(_mean(_f13_recovery_strength(revenue, ebitda, 252), 126).abs())) * (closeadj)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_5d_ssq_lca_sl63_v106_signal(closeadj, revenue):
    base = ((np.sign(_f13_revenue_inflection(revenue, 5)) * np.sqrt(_f13_revenue_inflection(revenue, 5).abs()))) * (np.log1p(closeadj.abs()))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_5d_ssq_mca_sl126_v107_signal(closeadj, revenue):
    base = ((np.sign(_f13_cycle_trough_indicator(revenue, 5)) * np.sqrt(_f13_cycle_trough_indicator(revenue, 5).abs()))) * (_mean(closeadj, 21))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_5d_ssq_rrn_sl252_v108_signal(closeadj, ebitda, revenue):
    base = ((np.sign(_f13_recovery_strength(revenue, ebitda, 5)) * np.sqrt(_f13_recovery_strength(revenue, ebitda, 5).abs()))) * ((revenue / _mean(revenue, 63)))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_10d_ssq_ca_sl5_v109_signal(closeadj, revenue):
    base = ((np.sign(_f13_revenue_inflection(revenue, 10)) * np.sqrt(_f13_revenue_inflection(revenue, 10).abs()))) * (closeadj)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_10d_ssq_lca_sl10_v110_signal(closeadj, revenue):
    base = ((np.sign(_f13_cycle_trough_indicator(revenue, 10)) * np.sqrt(_f13_cycle_trough_indicator(revenue, 10).abs()))) * (np.log1p(closeadj.abs()))
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_10d_ssq_mca_sl21_v111_signal(closeadj, ebitda, revenue):
    base = ((np.sign(_f13_recovery_strength(revenue, ebitda, 10)) * np.sqrt(_f13_recovery_strength(revenue, ebitda, 10).abs()))) * (_mean(closeadj, 21))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_21d_ssq_rrn_sl63_v112_signal(closeadj, revenue):
    base = ((np.sign(_f13_revenue_inflection(revenue, 21)) * np.sqrt(_f13_revenue_inflection(revenue, 21).abs()))) * ((revenue / _mean(revenue, 63)))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_21d_ssq_ca_sl126_v113_signal(closeadj, revenue):
    base = ((np.sign(_f13_cycle_trough_indicator(revenue, 21)) * np.sqrt(_f13_cycle_trough_indicator(revenue, 21).abs()))) * (closeadj)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_21d_ssq_lca_sl252_v114_signal(closeadj, ebitda, revenue):
    base = ((np.sign(_f13_recovery_strength(revenue, ebitda, 21)) * np.sqrt(_f13_recovery_strength(revenue, ebitda, 21).abs()))) * (np.log1p(closeadj.abs()))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_42d_ssq_mca_sl5_v115_signal(closeadj, revenue):
    base = ((np.sign(_f13_revenue_inflection(revenue, 42)) * np.sqrt(_f13_revenue_inflection(revenue, 42).abs()))) * (_mean(closeadj, 21))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_42d_ssq_rrn_sl10_v116_signal(closeadj, revenue):
    base = ((np.sign(_f13_cycle_trough_indicator(revenue, 42)) * np.sqrt(_f13_cycle_trough_indicator(revenue, 42).abs()))) * ((revenue / _mean(revenue, 63)))
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_42d_ssq_ca_sl21_v117_signal(closeadj, ebitda, revenue):
    base = ((np.sign(_f13_recovery_strength(revenue, ebitda, 42)) * np.sqrt(_f13_recovery_strength(revenue, ebitda, 42).abs()))) * (closeadj)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_63d_ssq_lca_sl63_v118_signal(closeadj, revenue):
    base = ((np.sign(_f13_revenue_inflection(revenue, 63)) * np.sqrt(_f13_revenue_inflection(revenue, 63).abs()))) * (np.log1p(closeadj.abs()))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_63d_ssq_mca_sl126_v119_signal(closeadj, revenue):
    base = ((np.sign(_f13_cycle_trough_indicator(revenue, 63)) * np.sqrt(_f13_cycle_trough_indicator(revenue, 63).abs()))) * (_mean(closeadj, 21))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_63d_ssq_rrn_sl252_v120_signal(closeadj, ebitda, revenue):
    base = ((np.sign(_f13_recovery_strength(revenue, ebitda, 63)) * np.sqrt(_f13_recovery_strength(revenue, ebitda, 63).abs()))) * ((revenue / _mean(revenue, 63)))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_126d_ssq_ca_sl5_v121_signal(closeadj, revenue):
    base = ((np.sign(_f13_revenue_inflection(revenue, 126)) * np.sqrt(_f13_revenue_inflection(revenue, 126).abs()))) * (closeadj)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_126d_ssq_lca_sl10_v122_signal(closeadj, revenue):
    base = ((np.sign(_f13_cycle_trough_indicator(revenue, 126)) * np.sqrt(_f13_cycle_trough_indicator(revenue, 126).abs()))) * (np.log1p(closeadj.abs()))
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_126d_ssq_mca_sl21_v123_signal(closeadj, ebitda, revenue):
    base = ((np.sign(_f13_recovery_strength(revenue, ebitda, 126)) * np.sqrt(_f13_recovery_strength(revenue, ebitda, 126).abs()))) * (_mean(closeadj, 21))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_252d_ssq_rrn_sl63_v124_signal(closeadj, revenue):
    base = ((np.sign(_f13_revenue_inflection(revenue, 252)) * np.sqrt(_f13_revenue_inflection(revenue, 252).abs()))) * ((revenue / _mean(revenue, 63)))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_252d_ssq_ca_sl126_v125_signal(closeadj, revenue):
    base = ((np.sign(_f13_cycle_trough_indicator(revenue, 252)) * np.sqrt(_f13_cycle_trough_indicator(revenue, 252).abs()))) * (closeadj)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_252d_ssq_lca_sl252_v126_signal(closeadj, ebitda, revenue):
    base = ((np.sign(_f13_recovery_strength(revenue, ebitda, 252)) * np.sqrt(_f13_recovery_strength(revenue, ebitda, 252).abs()))) * (np.log1p(closeadj.abs()))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_5d_dxc_mca_sl5_v127_signal(closeadj, revenue):
    base = ((_f13_revenue_inflection(revenue, 5).diff(5) * closeadj)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_5d_dxc_rrn_sl10_v128_signal(closeadj, revenue):
    base = ((_f13_cycle_trough_indicator(revenue, 5).diff(5) * closeadj)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_5d_dxc_ca_sl21_v129_signal(closeadj, ebitda, revenue):
    base = ((_f13_recovery_strength(revenue, ebitda, 5).diff(5) * closeadj)) * (closeadj)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_10d_dxc_lca_sl63_v130_signal(closeadj, revenue):
    base = ((_f13_revenue_inflection(revenue, 10).diff(10) * closeadj)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_10d_dxc_mca_sl126_v131_signal(closeadj, revenue):
    base = ((_f13_cycle_trough_indicator(revenue, 10).diff(10) * closeadj)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_10d_dxc_rrn_sl252_v132_signal(closeadj, ebitda, revenue):
    base = ((_f13_recovery_strength(revenue, ebitda, 10).diff(10) * closeadj)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_21d_dxc_ca_sl5_v133_signal(closeadj, revenue):
    base = ((_f13_revenue_inflection(revenue, 21).diff(21) * closeadj)) * (closeadj)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_21d_dxc_lca_sl10_v134_signal(closeadj, revenue):
    base = ((_f13_cycle_trough_indicator(revenue, 21).diff(21) * closeadj)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_21d_dxc_mca_sl21_v135_signal(closeadj, ebitda, revenue):
    base = ((_f13_recovery_strength(revenue, ebitda, 21).diff(21) * closeadj)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_42d_dxc_rrn_sl63_v136_signal(closeadj, revenue):
    base = ((_f13_revenue_inflection(revenue, 42).diff(21) * closeadj)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_42d_dxc_ca_sl126_v137_signal(closeadj, revenue):
    base = ((_f13_cycle_trough_indicator(revenue, 42).diff(21) * closeadj)) * (closeadj)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_42d_dxc_lca_sl252_v138_signal(closeadj, ebitda, revenue):
    base = ((_f13_recovery_strength(revenue, ebitda, 42).diff(21) * closeadj)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_63d_dxc_mca_sl5_v139_signal(closeadj, revenue):
    base = ((_f13_revenue_inflection(revenue, 63).diff(42) * closeadj)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_63d_dxc_rrn_sl10_v140_signal(closeadj, revenue):
    base = ((_f13_cycle_trough_indicator(revenue, 63).diff(42) * closeadj)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_63d_dxc_ca_sl21_v141_signal(closeadj, ebitda, revenue):
    base = ((_f13_recovery_strength(revenue, ebitda, 63).diff(42) * closeadj)) * (closeadj)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_126d_dxc_lca_sl63_v142_signal(closeadj, revenue):
    base = ((_f13_revenue_inflection(revenue, 126).diff(63) * closeadj)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_126d_dxc_mca_sl126_v143_signal(closeadj, revenue):
    base = ((_f13_cycle_trough_indicator(revenue, 126).diff(63) * closeadj)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_126d_dxc_rrn_sl252_v144_signal(closeadj, ebitda, revenue):
    base = ((_f13_recovery_strength(revenue, ebitda, 126).diff(63) * closeadj)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_252d_dxc_ca_sl5_v145_signal(closeadj, revenue):
    base = ((_f13_revenue_inflection(revenue, 252).diff(126) * closeadj)) * (closeadj)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_252d_dxc_lca_sl10_v146_signal(closeadj, revenue):
    base = ((_f13_cycle_trough_indicator(revenue, 252).diff(126) * closeadj)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_252d_dxc_mca_sl21_v147_signal(closeadj, ebitda, revenue):
    base = ((_f13_recovery_strength(revenue, ebitda, 252).diff(126) * closeadj)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_5d_rm_lca_sl5_v148_signal(closeadj, revenue):
    base = (_mean(_f13_revenue_inflection(revenue, 5), 5)) * (np.log1p(closeadj.abs()))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_5d_rm_mca_sl5_v149_signal(closeadj, revenue):
    base = (_mean(_f13_revenue_inflection(revenue, 5), 5)) * (_mean(closeadj, 21))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_5d_rm_rrn_sl5_v150_signal(closeadj, revenue):
    base = (_mean(_f13_revenue_inflection(revenue, 5), 5)) * ((revenue / _mean(revenue, 63)))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    aoc_f13_aerospace_oem_cycle_position_revinfl_5d_rm_ca_sl5_v001_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_5d_rm_lca_sl10_v002_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_5d_rm_mca_sl21_v003_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_10d_rm_rrn_sl63_v004_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_10d_rm_ca_sl126_v005_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_10d_rm_lca_sl252_v006_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_21d_rm_mca_sl5_v007_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_21d_rm_rrn_sl10_v008_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_21d_rm_ca_sl21_v009_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_42d_rm_lca_sl63_v010_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_42d_rm_mca_sl126_v011_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_42d_rm_rrn_sl252_v012_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_63d_rm_ca_sl5_v013_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_63d_rm_lca_sl10_v014_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_63d_rm_mca_sl21_v015_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_126d_rm_rrn_sl63_v016_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_126d_rm_ca_sl126_v017_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_126d_rm_lca_sl252_v018_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_252d_rm_mca_sl5_v019_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_252d_rm_rrn_sl10_v020_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_252d_rm_ca_sl21_v021_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_5d_rs_lca_sl63_v022_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_5d_rs_mca_sl126_v023_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_5d_rs_rrn_sl252_v024_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_10d_rs_ca_sl5_v025_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_10d_rs_lca_sl10_v026_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_10d_rs_mca_sl21_v027_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_21d_rs_rrn_sl63_v028_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_21d_rs_ca_sl126_v029_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_21d_rs_lca_sl252_v030_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_42d_rs_mca_sl5_v031_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_42d_rs_rrn_sl10_v032_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_42d_rs_ca_sl21_v033_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_63d_rs_lca_sl63_v034_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_63d_rs_mca_sl126_v035_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_63d_rs_rrn_sl252_v036_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_126d_rs_ca_sl5_v037_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_126d_rs_lca_sl10_v038_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_126d_rs_mca_sl21_v039_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_252d_rs_rrn_sl63_v040_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_252d_rs_ca_sl126_v041_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_252d_rs_lca_sl252_v042_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_5d_em_mca_sl5_v043_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_5d_em_rrn_sl10_v044_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_5d_em_ca_sl21_v045_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_10d_em_lca_sl63_v046_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_10d_em_mca_sl126_v047_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_10d_em_rrn_sl252_v048_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_21d_em_ca_sl5_v049_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_21d_em_lca_sl10_v050_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_21d_em_mca_sl21_v051_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_42d_em_rrn_sl63_v052_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_42d_em_ca_sl126_v053_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_42d_em_lca_sl252_v054_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_63d_em_mca_sl5_v055_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_63d_em_rrn_sl10_v056_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_63d_em_ca_sl21_v057_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_126d_em_lca_sl63_v058_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_126d_em_mca_sl126_v059_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_126d_em_rrn_sl252_v060_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_252d_em_ca_sl5_v061_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_252d_em_lca_sl10_v062_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_252d_em_mca_sl21_v063_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_5d_zw_rrn_sl63_v064_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_5d_zw_ca_sl126_v065_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_5d_zw_lca_sl252_v066_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_10d_zw_mca_sl5_v067_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_10d_zw_rrn_sl10_v068_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_10d_zw_ca_sl21_v069_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_21d_zw_lca_sl63_v070_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_21d_zw_mca_sl126_v071_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_21d_zw_rrn_sl252_v072_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_42d_zw_ca_sl5_v073_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_42d_zw_lca_sl10_v074_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_42d_zw_mca_sl21_v075_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_63d_zw_rrn_sl63_v076_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_63d_zw_ca_sl126_v077_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_63d_zw_lca_sl252_v078_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_126d_zw_mca_sl5_v079_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_126d_zw_rrn_sl10_v080_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_126d_zw_ca_sl21_v081_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_252d_zw_lca_sl63_v082_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_252d_zw_mca_sl126_v083_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_252d_zw_rrn_sl252_v084_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_5d_lgm_ca_sl5_v085_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_5d_lgm_lca_sl10_v086_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_5d_lgm_mca_sl21_v087_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_10d_lgm_rrn_sl63_v088_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_10d_lgm_ca_sl126_v089_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_10d_lgm_lca_sl252_v090_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_21d_lgm_mca_sl5_v091_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_21d_lgm_rrn_sl10_v092_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_21d_lgm_ca_sl21_v093_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_42d_lgm_lca_sl63_v094_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_42d_lgm_mca_sl126_v095_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_42d_lgm_rrn_sl252_v096_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_63d_lgm_ca_sl5_v097_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_63d_lgm_lca_sl10_v098_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_63d_lgm_mca_sl21_v099_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_126d_lgm_rrn_sl63_v100_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_126d_lgm_ca_sl126_v101_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_126d_lgm_lca_sl252_v102_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_252d_lgm_mca_sl5_v103_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_252d_lgm_rrn_sl10_v104_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_252d_lgm_ca_sl21_v105_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_5d_ssq_lca_sl63_v106_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_5d_ssq_mca_sl126_v107_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_5d_ssq_rrn_sl252_v108_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_10d_ssq_ca_sl5_v109_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_10d_ssq_lca_sl10_v110_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_10d_ssq_mca_sl21_v111_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_21d_ssq_rrn_sl63_v112_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_21d_ssq_ca_sl126_v113_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_21d_ssq_lca_sl252_v114_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_42d_ssq_mca_sl5_v115_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_42d_ssq_rrn_sl10_v116_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_42d_ssq_ca_sl21_v117_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_63d_ssq_lca_sl63_v118_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_63d_ssq_mca_sl126_v119_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_63d_ssq_rrn_sl252_v120_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_126d_ssq_ca_sl5_v121_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_126d_ssq_lca_sl10_v122_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_126d_ssq_mca_sl21_v123_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_252d_ssq_rrn_sl63_v124_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_252d_ssq_ca_sl126_v125_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_252d_ssq_lca_sl252_v126_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_5d_dxc_mca_sl5_v127_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_5d_dxc_rrn_sl10_v128_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_5d_dxc_ca_sl21_v129_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_10d_dxc_lca_sl63_v130_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_10d_dxc_mca_sl126_v131_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_10d_dxc_rrn_sl252_v132_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_21d_dxc_ca_sl5_v133_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_21d_dxc_lca_sl10_v134_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_21d_dxc_mca_sl21_v135_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_42d_dxc_rrn_sl63_v136_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_42d_dxc_ca_sl126_v137_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_42d_dxc_lca_sl252_v138_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_63d_dxc_mca_sl5_v139_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_63d_dxc_rrn_sl10_v140_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_63d_dxc_ca_sl21_v141_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_126d_dxc_lca_sl63_v142_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_126d_dxc_mca_sl126_v143_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_126d_dxc_rrn_sl252_v144_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_252d_dxc_ca_sl5_v145_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_252d_dxc_lca_sl10_v146_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_252d_dxc_mca_sl21_v147_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_5d_rm_lca_sl5_v148_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_5d_rm_mca_sl5_v149_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_5d_rm_rrn_sl5_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F13_AEROSPACE_OEM_CYCLE_POSITION_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    deferredrev = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "deferredrev": deferredrev,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f13_revenue_inflection", "_f13_cycle_trough_indicator", "_f13_recovery_strength",)
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
    print(f"OK f13_aerospace_oem_cycle_position_2nd_derivatives_001_150_claude: {n_features} features pass")
