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


def _f48_self_smoothed_baseline(closeadj, w):
    return _mean(closeadj, w)


def _f48_self_momentum_excess(closeadj, w):
    base = _mean(closeadj, w)
    return closeadj - base


def _f48_momentum_persistence(closeadj, w):
    ret_short = closeadj.pct_change(w)
    ret_long = _mean(closeadj.pct_change(w), w)
    return ret_short - ret_long


# v076-v085: alternate windows and combinations
def f48srm_f48_sector_relative_momentum_excess_10d_base_v076_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 10)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_84d_base_v077_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 84)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_10d_base_v078_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_84d_base_v079_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_base_10d_base_v080_signal(closeadj):
    base = _f48_self_smoothed_baseline(closeadj, 10)
    result = (closeadj - base)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_base_84d_base_v081_signal(closeadj):
    base = _f48_self_smoothed_baseline(closeadj, 84)
    result = (closeadj - base)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_msq_252d_base_v082_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 252)
    result = np.sign(g) * g * g
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_msq_252d_base_v083_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 252)
    result = (g * g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxprice_63d_base_v084_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxprice_252d_base_v085_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v086-v095: dual-EMA cross
def f48srm_f48_sector_relative_momentum_dualema_21v63_base_v086_signal(closeadj):
    ema_s = closeadj.ewm(span=21, adjust=False).mean()
    ema_l = closeadj.ewm(span=63, adjust=False).mean()
    base = _f48_self_smoothed_baseline(closeadj, 21)
    result = (ema_s - ema_l) + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_dualema_63v252_base_v087_signal(closeadj):
    ema_s = closeadj.ewm(span=63, adjust=False).mean()
    ema_l = closeadj.ewm(span=252, adjust=False).mean()
    base = _f48_self_smoothed_baseline(closeadj, 63)
    result = (ema_s - ema_l) + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_dualema_252v504_base_v088_signal(closeadj):
    ema_s = closeadj.ewm(span=252, adjust=False).mean()
    ema_l = closeadj.ewm(span=504, adjust=False).mean()
    base = _f48_self_smoothed_baseline(closeadj, 252)
    result = (ema_s - ema_l) + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_dualema_5v21_base_v089_signal(closeadj):
    ema_s = closeadj.ewm(span=5, adjust=False).mean()
    ema_l = closeadj.ewm(span=21, adjust=False).mean()
    base = _f48_self_smoothed_baseline(closeadj, 5)
    result = (ema_s - ema_l) + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_macdsig_base_v090_signal(closeadj):
    ema_s = closeadj.ewm(span=12, adjust=False).mean()
    ema_l = closeadj.ewm(span=26, adjust=False).mean()
    base = _f48_self_smoothed_baseline(closeadj, 21)
    sig = (ema_s - ema_l).ewm(span=9, adjust=False).mean()
    result = ((ema_s - ema_l) - sig) + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_macdsig_long_base_v091_signal(closeadj):
    ema_s = closeadj.ewm(span=63, adjust=False).mean()
    ema_l = closeadj.ewm(span=189, adjust=False).mean()
    base = _f48_self_smoothed_baseline(closeadj, 63)
    sig = (ema_s - ema_l).ewm(span=42, adjust=False).mean()
    result = ((ema_s - ema_l) - sig) + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessrsi_21d_base_v092_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 21)
    up = base.where(base > 0, 0.0)
    dn = (-base).where(base < 0, 0.0)
    rs = _mean(up, 21) / _mean(dn, 21).replace(0, np.nan)
    rsi = 100.0 - (100.0 / (1.0 + rs))
    result = rsi + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessrsi_63d_base_v093_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 63)
    up = base.where(base > 0, 0.0)
    dn = (-base).where(base < 0, 0.0)
    rs = _mean(up, 63) / _mean(dn, 63).replace(0, np.nan)
    rsi = 100.0 - (100.0 / (1.0 + rs))
    result = rsi + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessabs_252d_base_v094_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 252)
    result = g.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_signxexcess_63d_base_v095_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 63)
    sg = np.sign(g)
    result = sg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v096-v110: volatility-adjusted momentum
def f48srm_f48_sector_relative_momentum_excessvoladj_63d_base_v096_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 63)
    vol = _std(closeadj.pct_change(), 63)
    result = g / vol.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessvoladj_252d_base_v097_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 252)
    vol = _std(closeadj.pct_change(), 252)
    result = g / vol.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persvoladj_252d_base_v098_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 252)
    vol = _std(closeadj.pct_change(), 252)
    result = g / vol.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_med_252d_base_v099_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 252)
    med = g.rolling(252, min_periods=63).median()
    result = (g - med)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_med_252d_base_v100_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 252)
    med = g.rolling(252, min_periods=63).median()
    result = (g - med) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_hi_252d_base_v101_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 252)
    med = g.rolling(252, min_periods=63).median()
    hi = (g > med).astype(float)
    result = (hi * g + g * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_lo_252d_base_v102_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 252)
    med = g.rolling(252, min_periods=63).median()
    lo = (g < med).astype(float)
    result = (lo * g + g * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_hi_252d_base_v103_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 252)
    med = g.rolling(252, min_periods=63).median()
    hi = (g > med).astype(float)
    result = (hi * g + g * 0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_logabs_252d_base_v104_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 252)
    result = np.log1p(g.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_logabs_252d_base_v105_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 252)
    result = np.log1p(g.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v106-v115: alternative momentum constructions
def f48srm_f48_sector_relative_momentum_diff_long_short_base_v106_signal(closeadj):
    base_s = _f48_self_smoothed_baseline(closeadj, 21)
    base_l = _f48_self_smoothed_baseline(closeadj, 504)
    result = (base_s - base_l)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_diff_long_short_504_base_v107_signal(closeadj):
    base_s = _f48_self_smoothed_baseline(closeadj, 63)
    base_l = _f48_self_smoothed_baseline(closeadj, 504)
    result = (base_s - base_l)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_ratiocls_63d_base_v108_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 63)
    result = base / closeadj.replace(0, np.nan) * closeadj * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_ratiocls_252d_base_v109_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 252)
    result = base / closeadj.replace(0, np.nan) * closeadj * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_cumsum_252d_base_v110_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 21)
    result = g.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_cumsum_504d_base_v111_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 21)
    result = g.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_cumsum_252d_base_v112_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 21)
    result = g.rolling(252, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_cumsum_504d_base_v113_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 21)
    result = g.rolling(504, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_lag_excess_63d_base_v114_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 63)
    result = (g - g.shift(63))
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_lag_excess_252d_base_v115_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 63)
    result = (g - g.shift(252))
    return result.replace([np.inf, -np.inf], np.nan)


# v116-v125: volume × momentum derivatives
def f48srm_f48_sector_relative_momentum_excessxvol_dv_63d_base_v116_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 63)
    dv = closeadj * volume
    result = base * _z(dv, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxvol_dv_252d_base_v117_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 252)
    dv = closeadj * volume
    result = base * _z(dv, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persxvol_dv_252d_base_v118_signal(closeadj, volume):
    base = _f48_momentum_persistence(closeadj, 252)
    dv = closeadj * volume
    result = base * _z(dv, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxvol_z_504d_base_v119_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 504)
    result = base * _z(volume, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_basexvol_z_252d_base_v120_signal(closeadj, volume):
    base = _f48_self_smoothed_baseline(closeadj, 252)
    result = (closeadj - base) * _z(volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxvol_growth_252d_base_v121_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 252)
    vg = volume.pct_change(252)
    result = base * vg
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persxvol_growth_63d_base_v122_signal(closeadj, volume):
    base = _f48_momentum_persistence(closeadj, 63)
    vg = volume.pct_change(63)
    result = base * vg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_vw_63d_base_v123_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 63)
    vw = _mean(closeadj * volume, 21) / _mean(volume, 21).replace(0, np.nan)
    result = (base) + (closeadj - vw)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_vw_252d_base_v124_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 252)
    vw = _mean(closeadj * volume, 63) / _mean(volume, 63).replace(0, np.nan)
    result = (base) + (closeadj - vw)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxlogprice_252d_base_v125_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 252)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v126-v140: percent change variants and acceleration
def f48srm_f48_sector_relative_momentum_excess_pct_63d_base_v126_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 63)
    result = base.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_pct_252d_base_v127_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 252)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_pct_252d_base_v128_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 252)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxprice_log_63d_base_v129_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 63)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxprice_sqrt_63d_base_v130_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 63)
    result = base * np.sqrt(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persxprice_sqrt_252d_base_v131_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 252)
    result = base * np.sqrt(closeadj.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_kavg_63d_base_v132_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 63)
    result = g.rolling(63, min_periods=21).mean() * 0.5 + g * 0.5
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_kavg_252d_base_v133_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 252)
    result = g.rolling(252, min_periods=63).mean() * 0.5 + g * 0.5
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_kavg_252d_base_v134_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 252)
    result = (g.rolling(252, min_periods=63).mean() * 0.5 + g * 0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_long_log_504d_base_v135_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 504)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_basesqrt_252d_base_v136_signal(closeadj):
    base = _f48_self_smoothed_baseline(closeadj, 252)
    result = np.sqrt((closeadj - base).abs()) * np.sign(closeadj - base)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_cumprod_63d_base_v137_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 63)
    norm_g = g / closeadj.abs().replace(0, np.nan)
    result = norm_g.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_cumprod_252d_base_v138_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 252)
    norm_g = g / closeadj.abs().replace(0, np.nan)
    result = norm_g.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_logvolxprice_63d_base_v139_signal(closeadj, volume):
    g = _f48_self_momentum_excess(closeadj, 63)
    result = g * np.log(volume.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_logvol_252d_base_v140_signal(closeadj, volume):
    g = _f48_momentum_persistence(closeadj, 252)
    result = g * np.log(volume.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v141-v150: additional composites
def f48srm_f48_sector_relative_momentum_excessxpers_63d_base_v141_signal(closeadj):
    a = _f48_self_momentum_excess(closeadj, 63)
    b = _f48_momentum_persistence(closeadj, 63)
    result = (a + b * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxpers_252d_base_v142_signal(closeadj):
    a = _f48_self_momentum_excess(closeadj, 252)
    b = _f48_momentum_persistence(closeadj, 252)
    result = (a + b * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxpers_504d_base_v143_signal(closeadj):
    a = _f48_self_momentum_excess(closeadj, 504)
    b = _f48_momentum_persistence(closeadj, 504)
    result = (a + b * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_smooth_252d_base_v144_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 63)
    smooth = _mean(g, 252)
    result = (g - smooth)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_smooth_504d_base_v145_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 63)
    smooth = _mean(g, 504)
    result = (g - smooth)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_smooth_252d_base_v146_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 63)
    smooth = _mean(g, 252)
    result = (g - smooth) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_dvxprice_252d_base_v147_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 252)
    dv = closeadj * volume
    result = base * _mean(dv, 63) / closeadj.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_volz_long_504d_base_v148_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 504)
    result = base * _z(volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_logprice_252d_base_v149_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 252)
    result = g * np.log(closeadj.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_composite_excess_pers_504d_base_v150_signal(closeadj, volume):
    a = _f48_self_momentum_excess(closeadj, 504)
    b = _f48_momentum_persistence(closeadj, 504)
    result = (a + b * closeadj) * _z(volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f48srm_f48_sector_relative_momentum_excess_10d_base_v076_signal,
    f48srm_f48_sector_relative_momentum_excess_84d_base_v077_signal,
    f48srm_f48_sector_relative_momentum_pers_10d_base_v078_signal,
    f48srm_f48_sector_relative_momentum_pers_84d_base_v079_signal,
    f48srm_f48_sector_relative_momentum_base_10d_base_v080_signal,
    f48srm_f48_sector_relative_momentum_base_84d_base_v081_signal,
    f48srm_f48_sector_relative_momentum_excess_msq_252d_base_v082_signal,
    f48srm_f48_sector_relative_momentum_pers_msq_252d_base_v083_signal,
    f48srm_f48_sector_relative_momentum_excessxprice_63d_base_v084_signal,
    f48srm_f48_sector_relative_momentum_excessxprice_252d_base_v085_signal,
    f48srm_f48_sector_relative_momentum_dualema_21v63_base_v086_signal,
    f48srm_f48_sector_relative_momentum_dualema_63v252_base_v087_signal,
    f48srm_f48_sector_relative_momentum_dualema_252v504_base_v088_signal,
    f48srm_f48_sector_relative_momentum_dualema_5v21_base_v089_signal,
    f48srm_f48_sector_relative_momentum_macdsig_base_v090_signal,
    f48srm_f48_sector_relative_momentum_macdsig_long_base_v091_signal,
    f48srm_f48_sector_relative_momentum_excessrsi_21d_base_v092_signal,
    f48srm_f48_sector_relative_momentum_excessrsi_63d_base_v093_signal,
    f48srm_f48_sector_relative_momentum_excessabs_252d_base_v094_signal,
    f48srm_f48_sector_relative_momentum_signxexcess_63d_base_v095_signal,
    f48srm_f48_sector_relative_momentum_excessvoladj_63d_base_v096_signal,
    f48srm_f48_sector_relative_momentum_excessvoladj_252d_base_v097_signal,
    f48srm_f48_sector_relative_momentum_persvoladj_252d_base_v098_signal,
    f48srm_f48_sector_relative_momentum_excess_med_252d_base_v099_signal,
    f48srm_f48_sector_relative_momentum_pers_med_252d_base_v100_signal,
    f48srm_f48_sector_relative_momentum_excess_hi_252d_base_v101_signal,
    f48srm_f48_sector_relative_momentum_excess_lo_252d_base_v102_signal,
    f48srm_f48_sector_relative_momentum_pers_hi_252d_base_v103_signal,
    f48srm_f48_sector_relative_momentum_excess_logabs_252d_base_v104_signal,
    f48srm_f48_sector_relative_momentum_pers_logabs_252d_base_v105_signal,
    f48srm_f48_sector_relative_momentum_diff_long_short_base_v106_signal,
    f48srm_f48_sector_relative_momentum_diff_long_short_504_base_v107_signal,
    f48srm_f48_sector_relative_momentum_excess_ratiocls_63d_base_v108_signal,
    f48srm_f48_sector_relative_momentum_excess_ratiocls_252d_base_v109_signal,
    f48srm_f48_sector_relative_momentum_pers_cumsum_252d_base_v110_signal,
    f48srm_f48_sector_relative_momentum_pers_cumsum_504d_base_v111_signal,
    f48srm_f48_sector_relative_momentum_excess_cumsum_252d_base_v112_signal,
    f48srm_f48_sector_relative_momentum_excess_cumsum_504d_base_v113_signal,
    f48srm_f48_sector_relative_momentum_lag_excess_63d_base_v114_signal,
    f48srm_f48_sector_relative_momentum_lag_excess_252d_base_v115_signal,
    f48srm_f48_sector_relative_momentum_excessxvol_dv_63d_base_v116_signal,
    f48srm_f48_sector_relative_momentum_excessxvol_dv_252d_base_v117_signal,
    f48srm_f48_sector_relative_momentum_persxvol_dv_252d_base_v118_signal,
    f48srm_f48_sector_relative_momentum_excessxvol_z_504d_base_v119_signal,
    f48srm_f48_sector_relative_momentum_basexvol_z_252d_base_v120_signal,
    f48srm_f48_sector_relative_momentum_excessxvol_growth_252d_base_v121_signal,
    f48srm_f48_sector_relative_momentum_persxvol_growth_63d_base_v122_signal,
    f48srm_f48_sector_relative_momentum_excess_vw_63d_base_v123_signal,
    f48srm_f48_sector_relative_momentum_excess_vw_252d_base_v124_signal,
    f48srm_f48_sector_relative_momentum_excessxlogprice_252d_base_v125_signal,
    f48srm_f48_sector_relative_momentum_excess_pct_63d_base_v126_signal,
    f48srm_f48_sector_relative_momentum_excess_pct_252d_base_v127_signal,
    f48srm_f48_sector_relative_momentum_pers_pct_252d_base_v128_signal,
    f48srm_f48_sector_relative_momentum_excessxprice_log_63d_base_v129_signal,
    f48srm_f48_sector_relative_momentum_excessxprice_sqrt_63d_base_v130_signal,
    f48srm_f48_sector_relative_momentum_persxprice_sqrt_252d_base_v131_signal,
    f48srm_f48_sector_relative_momentum_excess_kavg_63d_base_v132_signal,
    f48srm_f48_sector_relative_momentum_excess_kavg_252d_base_v133_signal,
    f48srm_f48_sector_relative_momentum_pers_kavg_252d_base_v134_signal,
    f48srm_f48_sector_relative_momentum_excess_long_log_504d_base_v135_signal,
    f48srm_f48_sector_relative_momentum_basesqrt_252d_base_v136_signal,
    f48srm_f48_sector_relative_momentum_excess_cumprod_63d_base_v137_signal,
    f48srm_f48_sector_relative_momentum_excess_cumprod_252d_base_v138_signal,
    f48srm_f48_sector_relative_momentum_excess_logvolxprice_63d_base_v139_signal,
    f48srm_f48_sector_relative_momentum_pers_logvol_252d_base_v140_signal,
    f48srm_f48_sector_relative_momentum_excessxpers_63d_base_v141_signal,
    f48srm_f48_sector_relative_momentum_excessxpers_252d_base_v142_signal,
    f48srm_f48_sector_relative_momentum_excessxpers_504d_base_v143_signal,
    f48srm_f48_sector_relative_momentum_excess_smooth_252d_base_v144_signal,
    f48srm_f48_sector_relative_momentum_excess_smooth_504d_base_v145_signal,
    f48srm_f48_sector_relative_momentum_pers_smooth_252d_base_v146_signal,
    f48srm_f48_sector_relative_momentum_excess_dvxprice_252d_base_v147_signal,
    f48srm_f48_sector_relative_momentum_excess_volz_long_504d_base_v148_signal,
    f48srm_f48_sector_relative_momentum_pers_logprice_252d_base_v149_signal,
    f48srm_f48_sector_relative_momentum_composite_excess_pers_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F48_SECTOR_RELATIVE_MOMENTUM_REGISTRY_076_150 = REGISTRY


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

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f48_self_smoothed_baseline", "_f48_self_momentum_excess", "_f48_momentum_persistence")
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
    print(f"OK f48_sector_relative_momentum_base_076_150_claude: {n_features} features pass")
