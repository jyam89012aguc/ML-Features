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
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


# ===== folder domain primitives =====
def _f43_share_count_change(sharesbas, w):
    return sharesbas.pct_change(periods=w)


def _f43_buyback_intensity(sharesbas, closeadj, w):
    chg = -sharesbas.pct_change(periods=w)
    return chg * closeadj


def _f43_buyback_timing_quality(sharesbas, closeadj, w):
    chg = -sharesbas.pct_change(periods=w)
    pr_z = (closeadj - closeadj.rolling(w, min_periods=max(1, w // 2)).mean()) / closeadj.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return chg * (-pr_z)

# feature 76: bbq_126d_xc
def f43bct_f43_buyback_cycle_timing_bbq_126d_xc_base_v076_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 126)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 77: bbq_126d_xclog
def f43bct_f43_buyback_cycle_timing_bbq_126d_xclog_base_v077_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 126)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 78: bbq_126d_xcm21
def f43bct_f43_buyback_cycle_timing_bbq_126d_xcm21_base_v078_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 126)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 79: bbq_189d_xc
def f43bct_f43_buyback_cycle_timing_bbq_189d_xc_base_v079_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 189)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 80: bbq_189d_xclog
def f43bct_f43_buyback_cycle_timing_bbq_189d_xclog_base_v080_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 189)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 81: bbq_189d_xcm21
def f43bct_f43_buyback_cycle_timing_bbq_189d_xcm21_base_v081_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 189)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 82: bbq_252d_xc
def f43bct_f43_buyback_cycle_timing_bbq_252d_xc_base_v082_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 252)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 83: bbq_252d_xclog
def f43bct_f43_buyback_cycle_timing_bbq_252d_xclog_base_v083_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 252)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 84: bbq_252d_xcm21
def f43bct_f43_buyback_cycle_timing_bbq_252d_xcm21_base_v084_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 252)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 85: bbq_378d_xc
def f43bct_f43_buyback_cycle_timing_bbq_378d_xc_base_v085_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 378)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 86: bbq_378d_xclog
def f43bct_f43_buyback_cycle_timing_bbq_378d_xclog_base_v086_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 378)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 87: bbq_378d_xcm21
def f43bct_f43_buyback_cycle_timing_bbq_378d_xcm21_base_v087_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 378)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 88: bbq_504d_xc
def f43bct_f43_buyback_cycle_timing_bbq_504d_xc_base_v088_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 504)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 89: bbq_504d_xclog
def f43bct_f43_buyback_cycle_timing_bbq_504d_xclog_base_v089_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 504)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 90: bbq_504d_xcm21
def f43bct_f43_buyback_cycle_timing_bbq_504d_xcm21_base_v090_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 504)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 91: wasccchg_5d
def f43bct_f43_buyback_cycle_timing_wasccchg_5d_base_v091_signal(shareswa, closeadj):
    base = _f43_share_count_change(shareswa, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 92: wabbi_5d
def f43bct_f43_buyback_cycle_timing_wabbi_5d_base_v092_signal(shareswa, closeadj):
    base = _f43_buyback_intensity(shareswa, closeadj, 5)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# feature 93: wabbq_5d
def f43bct_f43_buyback_cycle_timing_wabbq_5d_base_v093_signal(shareswa, closeadj):
    base = _f43_buyback_timing_quality(shareswa, closeadj, 5)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# feature 94: wasccchg_10d
def f43bct_f43_buyback_cycle_timing_wasccchg_10d_base_v094_signal(shareswa, closeadj):
    base = _f43_share_count_change(shareswa, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 95: wabbi_10d
def f43bct_f43_buyback_cycle_timing_wabbi_10d_base_v095_signal(shareswa, closeadj):
    base = _f43_buyback_intensity(shareswa, closeadj, 10)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# feature 96: wabbq_10d
def f43bct_f43_buyback_cycle_timing_wabbq_10d_base_v096_signal(shareswa, closeadj):
    base = _f43_buyback_timing_quality(shareswa, closeadj, 10)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# feature 97: wasccchg_21d
def f43bct_f43_buyback_cycle_timing_wasccchg_21d_base_v097_signal(shareswa, closeadj):
    base = _f43_share_count_change(shareswa, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 98: wabbi_21d
def f43bct_f43_buyback_cycle_timing_wabbi_21d_base_v098_signal(shareswa, closeadj):
    base = _f43_buyback_intensity(shareswa, closeadj, 21)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# feature 99: wabbq_21d
def f43bct_f43_buyback_cycle_timing_wabbq_21d_base_v099_signal(shareswa, closeadj):
    base = _f43_buyback_timing_quality(shareswa, closeadj, 21)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# feature 100: wasccchg_42d
def f43bct_f43_buyback_cycle_timing_wasccchg_42d_base_v100_signal(shareswa, closeadj):
    base = _f43_share_count_change(shareswa, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 101: wabbi_42d
def f43bct_f43_buyback_cycle_timing_wabbi_42d_base_v101_signal(shareswa, closeadj):
    base = _f43_buyback_intensity(shareswa, closeadj, 42)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# feature 102: wabbq_42d
def f43bct_f43_buyback_cycle_timing_wabbq_42d_base_v102_signal(shareswa, closeadj):
    base = _f43_buyback_timing_quality(shareswa, closeadj, 42)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# feature 103: wasccchg_63d
def f43bct_f43_buyback_cycle_timing_wasccchg_63d_base_v103_signal(shareswa, closeadj):
    base = _f43_share_count_change(shareswa, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 104: wabbi_63d
def f43bct_f43_buyback_cycle_timing_wabbi_63d_base_v104_signal(shareswa, closeadj):
    base = _f43_buyback_intensity(shareswa, closeadj, 63)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# feature 105: wabbq_63d
def f43bct_f43_buyback_cycle_timing_wabbq_63d_base_v105_signal(shareswa, closeadj):
    base = _f43_buyback_timing_quality(shareswa, closeadj, 63)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# feature 106: wasccchg_126d
def f43bct_f43_buyback_cycle_timing_wasccchg_126d_base_v106_signal(shareswa, closeadj):
    base = _f43_share_count_change(shareswa, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 107: wabbi_126d
def f43bct_f43_buyback_cycle_timing_wabbi_126d_base_v107_signal(shareswa, closeadj):
    base = _f43_buyback_intensity(shareswa, closeadj, 126)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# feature 108: wabbq_126d
def f43bct_f43_buyback_cycle_timing_wabbq_126d_base_v108_signal(shareswa, closeadj):
    base = _f43_buyback_timing_quality(shareswa, closeadj, 126)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# feature 109: wasccchg_189d
def f43bct_f43_buyback_cycle_timing_wasccchg_189d_base_v109_signal(shareswa, closeadj):
    base = _f43_share_count_change(shareswa, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 110: wabbi_189d
def f43bct_f43_buyback_cycle_timing_wabbi_189d_base_v110_signal(shareswa, closeadj):
    base = _f43_buyback_intensity(shareswa, closeadj, 189)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# feature 111: wabbq_189d
def f43bct_f43_buyback_cycle_timing_wabbq_189d_base_v111_signal(shareswa, closeadj):
    base = _f43_buyback_timing_quality(shareswa, closeadj, 189)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# feature 112: wasccchg_252d
def f43bct_f43_buyback_cycle_timing_wasccchg_252d_base_v112_signal(shareswa, closeadj):
    base = _f43_share_count_change(shareswa, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 113: wabbi_252d
def f43bct_f43_buyback_cycle_timing_wabbi_252d_base_v113_signal(shareswa, closeadj):
    base = _f43_buyback_intensity(shareswa, closeadj, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# feature 114: wabbq_252d
def f43bct_f43_buyback_cycle_timing_wabbq_252d_base_v114_signal(shareswa, closeadj):
    base = _f43_buyback_timing_quality(shareswa, closeadj, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# feature 115: sccz_21d
def f43bct_f43_buyback_cycle_timing_sccz_21d_base_v115_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 116: bbiz_21d
def f43bct_f43_buyback_cycle_timing_bbiz_21d_base_v116_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 117: bbqz_21d
def f43bct_f43_buyback_cycle_timing_bbqz_21d_base_v117_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 118: scc_ema_21d
def f43bct_f43_buyback_cycle_timing_scc_ema_21d_base_v118_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 21)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 119: bbi_ema_21d
def f43bct_f43_buyback_cycle_timing_bbi_ema_21d_base_v119_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 21)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 120: bbq_ema_21d
def f43bct_f43_buyback_cycle_timing_bbq_ema_21d_base_v120_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 21)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 121: sccz_42d
def f43bct_f43_buyback_cycle_timing_sccz_42d_base_v121_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 42)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 122: bbiz_42d
def f43bct_f43_buyback_cycle_timing_bbiz_42d_base_v122_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 42)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 123: bbqz_42d
def f43bct_f43_buyback_cycle_timing_bbqz_42d_base_v123_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 42)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 124: scc_ema_42d
def f43bct_f43_buyback_cycle_timing_scc_ema_42d_base_v124_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 42)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 125: bbi_ema_42d
def f43bct_f43_buyback_cycle_timing_bbi_ema_42d_base_v125_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 42)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 126: bbq_ema_42d
def f43bct_f43_buyback_cycle_timing_bbq_ema_42d_base_v126_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 42)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 127: sccz_63d
def f43bct_f43_buyback_cycle_timing_sccz_63d_base_v127_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 128: bbiz_63d
def f43bct_f43_buyback_cycle_timing_bbiz_63d_base_v128_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 129: bbqz_63d
def f43bct_f43_buyback_cycle_timing_bbqz_63d_base_v129_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 130: scc_ema_63d
def f43bct_f43_buyback_cycle_timing_scc_ema_63d_base_v130_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 63)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 131: bbi_ema_63d
def f43bct_f43_buyback_cycle_timing_bbi_ema_63d_base_v131_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 63)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 132: bbq_ema_63d
def f43bct_f43_buyback_cycle_timing_bbq_ema_63d_base_v132_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 63)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 133: sccz_126d
def f43bct_f43_buyback_cycle_timing_sccz_126d_base_v133_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 126)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 134: bbiz_126d
def f43bct_f43_buyback_cycle_timing_bbiz_126d_base_v134_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 126)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 135: bbqz_126d
def f43bct_f43_buyback_cycle_timing_bbqz_126d_base_v135_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 126)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 136: scc_ema_126d
def f43bct_f43_buyback_cycle_timing_scc_ema_126d_base_v136_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 137: bbi_ema_126d
def f43bct_f43_buyback_cycle_timing_bbi_ema_126d_base_v137_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 138: bbq_ema_126d
def f43bct_f43_buyback_cycle_timing_bbq_ema_126d_base_v138_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 139: sccz_252d
def f43bct_f43_buyback_cycle_timing_sccz_252d_base_v139_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 140: bbiz_252d
def f43bct_f43_buyback_cycle_timing_bbiz_252d_base_v140_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 141: bbqz_252d
def f43bct_f43_buyback_cycle_timing_bbqz_252d_base_v141_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 142: scc_ema_252d
def f43bct_f43_buyback_cycle_timing_scc_ema_252d_base_v142_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 252)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 143: bbi_ema_252d
def f43bct_f43_buyback_cycle_timing_bbi_ema_252d_base_v143_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 252)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 144: bbq_ema_252d
def f43bct_f43_buyback_cycle_timing_bbq_ema_252d_base_v144_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 252)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 145: sccz_504d
def f43bct_f43_buyback_cycle_timing_sccz_504d_base_v145_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 504)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 146: bbiz_504d
def f43bct_f43_buyback_cycle_timing_bbiz_504d_base_v146_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 504)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 147: bbqz_504d
def f43bct_f43_buyback_cycle_timing_bbqz_504d_base_v147_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 504)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 148: scc_ema_504d
def f43bct_f43_buyback_cycle_timing_scc_ema_504d_base_v148_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 504)
    result = _ema(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 149: bbi_ema_504d
def f43bct_f43_buyback_cycle_timing_bbi_ema_504d_base_v149_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 504)
    result = _ema(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 150: bbq_ema_504d
def f43bct_f43_buyback_cycle_timing_bbq_ema_504d_base_v150_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 504)
    result = _ema(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f43bct_f43_buyback_cycle_timing_bbq_126d_xc_base_v076_signal,
    f43bct_f43_buyback_cycle_timing_bbq_126d_xclog_base_v077_signal,
    f43bct_f43_buyback_cycle_timing_bbq_126d_xcm21_base_v078_signal,
    f43bct_f43_buyback_cycle_timing_bbq_189d_xc_base_v079_signal,
    f43bct_f43_buyback_cycle_timing_bbq_189d_xclog_base_v080_signal,
    f43bct_f43_buyback_cycle_timing_bbq_189d_xcm21_base_v081_signal,
    f43bct_f43_buyback_cycle_timing_bbq_252d_xc_base_v082_signal,
    f43bct_f43_buyback_cycle_timing_bbq_252d_xclog_base_v083_signal,
    f43bct_f43_buyback_cycle_timing_bbq_252d_xcm21_base_v084_signal,
    f43bct_f43_buyback_cycle_timing_bbq_378d_xc_base_v085_signal,
    f43bct_f43_buyback_cycle_timing_bbq_378d_xclog_base_v086_signal,
    f43bct_f43_buyback_cycle_timing_bbq_378d_xcm21_base_v087_signal,
    f43bct_f43_buyback_cycle_timing_bbq_504d_xc_base_v088_signal,
    f43bct_f43_buyback_cycle_timing_bbq_504d_xclog_base_v089_signal,
    f43bct_f43_buyback_cycle_timing_bbq_504d_xcm21_base_v090_signal,
    f43bct_f43_buyback_cycle_timing_wasccchg_5d_base_v091_signal,
    f43bct_f43_buyback_cycle_timing_wabbi_5d_base_v092_signal,
    f43bct_f43_buyback_cycle_timing_wabbq_5d_base_v093_signal,
    f43bct_f43_buyback_cycle_timing_wasccchg_10d_base_v094_signal,
    f43bct_f43_buyback_cycle_timing_wabbi_10d_base_v095_signal,
    f43bct_f43_buyback_cycle_timing_wabbq_10d_base_v096_signal,
    f43bct_f43_buyback_cycle_timing_wasccchg_21d_base_v097_signal,
    f43bct_f43_buyback_cycle_timing_wabbi_21d_base_v098_signal,
    f43bct_f43_buyback_cycle_timing_wabbq_21d_base_v099_signal,
    f43bct_f43_buyback_cycle_timing_wasccchg_42d_base_v100_signal,
    f43bct_f43_buyback_cycle_timing_wabbi_42d_base_v101_signal,
    f43bct_f43_buyback_cycle_timing_wabbq_42d_base_v102_signal,
    f43bct_f43_buyback_cycle_timing_wasccchg_63d_base_v103_signal,
    f43bct_f43_buyback_cycle_timing_wabbi_63d_base_v104_signal,
    f43bct_f43_buyback_cycle_timing_wabbq_63d_base_v105_signal,
    f43bct_f43_buyback_cycle_timing_wasccchg_126d_base_v106_signal,
    f43bct_f43_buyback_cycle_timing_wabbi_126d_base_v107_signal,
    f43bct_f43_buyback_cycle_timing_wabbq_126d_base_v108_signal,
    f43bct_f43_buyback_cycle_timing_wasccchg_189d_base_v109_signal,
    f43bct_f43_buyback_cycle_timing_wabbi_189d_base_v110_signal,
    f43bct_f43_buyback_cycle_timing_wabbq_189d_base_v111_signal,
    f43bct_f43_buyback_cycle_timing_wasccchg_252d_base_v112_signal,
    f43bct_f43_buyback_cycle_timing_wabbi_252d_base_v113_signal,
    f43bct_f43_buyback_cycle_timing_wabbq_252d_base_v114_signal,
    f43bct_f43_buyback_cycle_timing_sccz_21d_base_v115_signal,
    f43bct_f43_buyback_cycle_timing_bbiz_21d_base_v116_signal,
    f43bct_f43_buyback_cycle_timing_bbqz_21d_base_v117_signal,
    f43bct_f43_buyback_cycle_timing_scc_ema_21d_base_v118_signal,
    f43bct_f43_buyback_cycle_timing_bbi_ema_21d_base_v119_signal,
    f43bct_f43_buyback_cycle_timing_bbq_ema_21d_base_v120_signal,
    f43bct_f43_buyback_cycle_timing_sccz_42d_base_v121_signal,
    f43bct_f43_buyback_cycle_timing_bbiz_42d_base_v122_signal,
    f43bct_f43_buyback_cycle_timing_bbqz_42d_base_v123_signal,
    f43bct_f43_buyback_cycle_timing_scc_ema_42d_base_v124_signal,
    f43bct_f43_buyback_cycle_timing_bbi_ema_42d_base_v125_signal,
    f43bct_f43_buyback_cycle_timing_bbq_ema_42d_base_v126_signal,
    f43bct_f43_buyback_cycle_timing_sccz_63d_base_v127_signal,
    f43bct_f43_buyback_cycle_timing_bbiz_63d_base_v128_signal,
    f43bct_f43_buyback_cycle_timing_bbqz_63d_base_v129_signal,
    f43bct_f43_buyback_cycle_timing_scc_ema_63d_base_v130_signal,
    f43bct_f43_buyback_cycle_timing_bbi_ema_63d_base_v131_signal,
    f43bct_f43_buyback_cycle_timing_bbq_ema_63d_base_v132_signal,
    f43bct_f43_buyback_cycle_timing_sccz_126d_base_v133_signal,
    f43bct_f43_buyback_cycle_timing_bbiz_126d_base_v134_signal,
    f43bct_f43_buyback_cycle_timing_bbqz_126d_base_v135_signal,
    f43bct_f43_buyback_cycle_timing_scc_ema_126d_base_v136_signal,
    f43bct_f43_buyback_cycle_timing_bbi_ema_126d_base_v137_signal,
    f43bct_f43_buyback_cycle_timing_bbq_ema_126d_base_v138_signal,
    f43bct_f43_buyback_cycle_timing_sccz_252d_base_v139_signal,
    f43bct_f43_buyback_cycle_timing_bbiz_252d_base_v140_signal,
    f43bct_f43_buyback_cycle_timing_bbqz_252d_base_v141_signal,
    f43bct_f43_buyback_cycle_timing_scc_ema_252d_base_v142_signal,
    f43bct_f43_buyback_cycle_timing_bbi_ema_252d_base_v143_signal,
    f43bct_f43_buyback_cycle_timing_bbq_ema_252d_base_v144_signal,
    f43bct_f43_buyback_cycle_timing_sccz_504d_base_v145_signal,
    f43bct_f43_buyback_cycle_timing_bbiz_504d_base_v146_signal,
    f43bct_f43_buyback_cycle_timing_bbqz_504d_base_v147_signal,
    f43bct_f43_buyback_cycle_timing_scc_ema_504d_base_v148_signal,
    f43bct_f43_buyback_cycle_timing_bbi_ema_504d_base_v149_signal,
    f43bct_f43_buyback_cycle_timing_bbq_ema_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_BUYBACK_CYCLE_TIMING_REGISTRY_076_150 = REGISTRY


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
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f43_share_count_change', '_f43_buyback_intensity', '_f43_buyback_timing_quality')
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
    print(f"OK f43_buyback_cycle_timing_base_076_150_claude: {n_features} features pass")
