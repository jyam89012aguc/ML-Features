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


# ===== folder domain primitives =====
def _f082_netinc_sign(netinc, w):
    # smoothed sign-like indicator using netinc relative to its rolling mean
    m = netinc.rolling(w, min_periods=max(1, w // 2)).mean()
    return (netinc - m) / (netinc.abs() + m.abs()).replace(0, np.nan)


def _f082_breakeven_cross(netinc, w):
    # breakeven proxy: distance of netinc from zero relative to its rolling std
    sd = netinc.rolling(w, min_periods=max(1, w // 2)).std()
    return netinc / sd.replace(0, np.nan)


def _f082_profitability_ignition(netinc, w):
    # profitability ignition proxy: smoothed positive-mass weighted by netinc growth
    base_m = netinc.rolling(w, min_periods=max(1, w // 2)).mean()
    gr = (netinc - base_m) / base_m.abs().replace(0, np.nan)
    return gr * netinc.abs()


def f082bcf_f082_breakeven_crossing_flag_bxce_21d_xclose_base_v076_signal(netinc, closeadj):
    base = _ema(_f082_breakeven_cross(netinc, 21), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_21d_xrev_base_v077_signal(netinc, closeadj, revenue):
    base = _ema(_f082_breakeven_cross(netinc, 21), 21)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_21d_xemac_base_v078_signal(netinc, closeadj):
    base = _ema(_f082_breakeven_cross(netinc, 21), 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_21d_xmean_base_v079_signal(netinc, closeadj):
    base = _ema(_f082_breakeven_cross(netinc, 21), 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_21d_xclose2_base_v080_signal(netinc, closeadj):
    base = _ema(_f082_breakeven_cross(netinc, 21), 21)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_63d_xclose_base_v081_signal(netinc, closeadj):
    base = _ema(_f082_breakeven_cross(netinc, 63), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_63d_xrev_base_v082_signal(netinc, closeadj, revenue):
    base = _ema(_f082_breakeven_cross(netinc, 63), 63)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_63d_xemac_base_v083_signal(netinc, closeadj):
    base = _ema(_f082_breakeven_cross(netinc, 63), 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_63d_xmean_base_v084_signal(netinc, closeadj):
    base = _ema(_f082_breakeven_cross(netinc, 63), 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_63d_xclose2_base_v085_signal(netinc, closeadj):
    base = _ema(_f082_breakeven_cross(netinc, 63), 63)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_252d_xclose_base_v086_signal(netinc, closeadj):
    base = _ema(_f082_breakeven_cross(netinc, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_252d_xrev_base_v087_signal(netinc, closeadj, revenue):
    base = _ema(_f082_breakeven_cross(netinc, 252), 252)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_252d_xemac_base_v088_signal(netinc, closeadj):
    base = _ema(_f082_breakeven_cross(netinc, 252), 252)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_252d_xmean_base_v089_signal(netinc, closeadj):
    base = _ema(_f082_breakeven_cross(netinc, 252), 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_252d_xclose2_base_v090_signal(netinc, closeadj):
    base = _ema(_f082_breakeven_cross(netinc, 252), 252)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_21d_xclose_base_v091_signal(netinc, closeadj):
    base = _f082_profitability_ignition(netinc, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_21d_xrev_base_v092_signal(netinc, closeadj, revenue):
    base = _f082_profitability_ignition(netinc, 21)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_21d_xemac_base_v093_signal(netinc, closeadj):
    base = _f082_profitability_ignition(netinc, 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_21d_xmean_base_v094_signal(netinc, closeadj):
    base = _f082_profitability_ignition(netinc, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_21d_xclose2_base_v095_signal(netinc, closeadj):
    base = _f082_profitability_ignition(netinc, 21)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_63d_xclose_base_v096_signal(netinc, closeadj):
    base = _f082_profitability_ignition(netinc, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_63d_xrev_base_v097_signal(netinc, closeadj, revenue):
    base = _f082_profitability_ignition(netinc, 63)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_63d_xemac_base_v098_signal(netinc, closeadj):
    base = _f082_profitability_ignition(netinc, 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_63d_xmean_base_v099_signal(netinc, closeadj):
    base = _f082_profitability_ignition(netinc, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_63d_xclose2_base_v100_signal(netinc, closeadj):
    base = _f082_profitability_ignition(netinc, 63)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_252d_xclose_base_v101_signal(netinc, closeadj):
    base = _f082_profitability_ignition(netinc, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_252d_xrev_base_v102_signal(netinc, closeadj, revenue):
    base = _f082_profitability_ignition(netinc, 252)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_252d_xemac_base_v103_signal(netinc, closeadj):
    base = _f082_profitability_ignition(netinc, 252)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_252d_xmean_base_v104_signal(netinc, closeadj):
    base = _f082_profitability_ignition(netinc, 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_252d_xclose2_base_v105_signal(netinc, closeadj):
    base = _f082_profitability_ignition(netinc, 252)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_21d_xclose_base_v106_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 21)
    base = raw / revenue.abs().replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_21d_xrev_base_v107_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 21)
    base = raw / revenue.abs().replace(0, np.nan)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_21d_xemac_base_v108_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 21)
    base = raw / revenue.abs().replace(0, np.nan)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_21d_xmean_base_v109_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 21)
    base = raw / revenue.abs().replace(0, np.nan)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_21d_xclose2_base_v110_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 21)
    base = raw / revenue.abs().replace(0, np.nan)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_63d_xclose_base_v111_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 63)
    base = raw / revenue.abs().replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_63d_xrev_base_v112_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 63)
    base = raw / revenue.abs().replace(0, np.nan)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_63d_xemac_base_v113_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 63)
    base = raw / revenue.abs().replace(0, np.nan)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_63d_xmean_base_v114_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 63)
    base = raw / revenue.abs().replace(0, np.nan)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_63d_xclose2_base_v115_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 63)
    base = raw / revenue.abs().replace(0, np.nan)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_252d_xclose_base_v116_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 252)
    base = raw / revenue.abs().replace(0, np.nan)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_252d_xrev_base_v117_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 252)
    base = raw / revenue.abs().replace(0, np.nan)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_252d_xemac_base_v118_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 252)
    base = raw / revenue.abs().replace(0, np.nan)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_252d_xmean_base_v119_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 252)
    base = raw / revenue.abs().replace(0, np.nan)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_252d_xclose2_base_v120_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 252)
    base = raw / revenue.abs().replace(0, np.nan)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_21d_xclose_base_v121_signal(netinc, closeadj):
    base = _ema(_f082_profitability_ignition(netinc, 21), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_21d_xrev_base_v122_signal(netinc, closeadj, revenue):
    base = _ema(_f082_profitability_ignition(netinc, 21), 21)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_21d_xemac_base_v123_signal(netinc, closeadj):
    base = _ema(_f082_profitability_ignition(netinc, 21), 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_21d_xmean_base_v124_signal(netinc, closeadj):
    base = _ema(_f082_profitability_ignition(netinc, 21), 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_21d_xclose2_base_v125_signal(netinc, closeadj):
    base = _ema(_f082_profitability_ignition(netinc, 21), 21)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_63d_xclose_base_v126_signal(netinc, closeadj):
    base = _ema(_f082_profitability_ignition(netinc, 63), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_63d_xrev_base_v127_signal(netinc, closeadj, revenue):
    base = _ema(_f082_profitability_ignition(netinc, 63), 63)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_63d_xemac_base_v128_signal(netinc, closeadj):
    base = _ema(_f082_profitability_ignition(netinc, 63), 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_63d_xmean_base_v129_signal(netinc, closeadj):
    base = _ema(_f082_profitability_ignition(netinc, 63), 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_63d_xclose2_base_v130_signal(netinc, closeadj):
    base = _ema(_f082_profitability_ignition(netinc, 63), 63)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_252d_xclose_base_v131_signal(netinc, closeadj):
    base = _ema(_f082_profitability_ignition(netinc, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_252d_xrev_base_v132_signal(netinc, closeadj, revenue):
    base = _ema(_f082_profitability_ignition(netinc, 252), 252)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_252d_xemac_base_v133_signal(netinc, closeadj):
    base = _ema(_f082_profitability_ignition(netinc, 252), 252)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_252d_xmean_base_v134_signal(netinc, closeadj):
    base = _ema(_f082_profitability_ignition(netinc, 252), 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_252d_xclose2_base_v135_signal(netinc, closeadj):
    base = _ema(_f082_profitability_ignition(netinc, 252), 252)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_21d_xclose_base_v136_signal(netinc, closeadj):
    base = _z(_f082_profitability_ignition(netinc, 21), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_21d_xrev_base_v137_signal(netinc, closeadj, revenue):
    base = _z(_f082_profitability_ignition(netinc, 21), 63)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_21d_xemac_base_v138_signal(netinc, closeadj):
    base = _z(_f082_profitability_ignition(netinc, 21), 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_21d_xmean_base_v139_signal(netinc, closeadj):
    base = _z(_f082_profitability_ignition(netinc, 21), 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_21d_xclose2_base_v140_signal(netinc, closeadj):
    base = _z(_f082_profitability_ignition(netinc, 21), 63)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_63d_xclose_base_v141_signal(netinc, closeadj):
    base = _z(_f082_profitability_ignition(netinc, 63), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_63d_xrev_base_v142_signal(netinc, closeadj, revenue):
    base = _z(_f082_profitability_ignition(netinc, 63), 126)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_63d_xemac_base_v143_signal(netinc, closeadj):
    base = _z(_f082_profitability_ignition(netinc, 63), 126)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_63d_xmean_base_v144_signal(netinc, closeadj):
    base = _z(_f082_profitability_ignition(netinc, 63), 126)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_63d_xclose2_base_v145_signal(netinc, closeadj):
    base = _z(_f082_profitability_ignition(netinc, 63), 126)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_252d_xclose_base_v146_signal(netinc, closeadj):
    base = _z(_f082_profitability_ignition(netinc, 252), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_252d_xrev_base_v147_signal(netinc, closeadj, revenue):
    base = _z(_f082_profitability_ignition(netinc, 252), 504)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_252d_xemac_base_v148_signal(netinc, closeadj):
    base = _z(_f082_profitability_ignition(netinc, 252), 504)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_252d_xmean_base_v149_signal(netinc, closeadj):
    base = _z(_f082_profitability_ignition(netinc, 252), 504)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_252d_xclose2_base_v150_signal(netinc, closeadj):
    base = _z(_f082_profitability_ignition(netinc, 252), 504)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f082bcf_f082_breakeven_crossing_flag_bxce_21d_xclose_base_v076_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_21d_xrev_base_v077_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_21d_xemac_base_v078_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_21d_xmean_base_v079_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_21d_xclose2_base_v080_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_63d_xclose_base_v081_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_63d_xrev_base_v082_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_63d_xemac_base_v083_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_63d_xmean_base_v084_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_63d_xclose2_base_v085_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_252d_xclose_base_v086_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_252d_xrev_base_v087_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_252d_xemac_base_v088_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_252d_xmean_base_v089_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_252d_xclose2_base_v090_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_21d_xclose_base_v091_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_21d_xrev_base_v092_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_21d_xemac_base_v093_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_21d_xmean_base_v094_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_21d_xclose2_base_v095_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_63d_xclose_base_v096_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_63d_xrev_base_v097_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_63d_xemac_base_v098_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_63d_xmean_base_v099_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_63d_xclose2_base_v100_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_252d_xclose_base_v101_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_252d_xrev_base_v102_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_252d_xemac_base_v103_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_252d_xmean_base_v104_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_252d_xclose2_base_v105_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_21d_xclose_base_v106_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_21d_xrev_base_v107_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_21d_xemac_base_v108_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_21d_xmean_base_v109_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_21d_xclose2_base_v110_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_63d_xclose_base_v111_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_63d_xrev_base_v112_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_63d_xemac_base_v113_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_63d_xmean_base_v114_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_63d_xclose2_base_v115_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_252d_xclose_base_v116_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_252d_xrev_base_v117_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_252d_xemac_base_v118_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_252d_xmean_base_v119_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_252d_xclose2_base_v120_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_21d_xclose_base_v121_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_21d_xrev_base_v122_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_21d_xemac_base_v123_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_21d_xmean_base_v124_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_21d_xclose2_base_v125_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_63d_xclose_base_v126_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_63d_xrev_base_v127_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_63d_xemac_base_v128_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_63d_xmean_base_v129_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_63d_xclose2_base_v130_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_252d_xclose_base_v131_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_252d_xrev_base_v132_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_252d_xemac_base_v133_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_252d_xmean_base_v134_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_252d_xclose2_base_v135_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_21d_xclose_base_v136_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_21d_xrev_base_v137_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_21d_xemac_base_v138_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_21d_xmean_base_v139_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_21d_xclose2_base_v140_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_63d_xclose_base_v141_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_63d_xrev_base_v142_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_63d_xemac_base_v143_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_63d_xmean_base_v144_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_63d_xclose2_base_v145_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_252d_xclose_base_v146_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_252d_xrev_base_v147_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_252d_xemac_base_v148_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_252d_xmean_base_v149_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_252d_xclose2_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F082_BREAKEVEN_CROSSING_FLAG_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f082_netinc_sign", "_f082_breakeven_cross", "_f082_profitability_ignition")
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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f082_breakeven_crossing_flag_base_076_150_claude: {n_features} features pass")
