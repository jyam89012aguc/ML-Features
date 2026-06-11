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
def _f25_revenue_per_asset(revenue, assets):
    return revenue / assets.replace(0, np.nan)


def _f25_capital_efficiency(revenue, ppnenet, w):
    eff = revenue / ppnenet.replace(0, np.nan)
    return eff.rolling(w, min_periods=max(1, w // 2)).mean()


def _f25_efficiency_compound(revenue, assets, w):
    eff = revenue / assets.replace(0, np.nan)
    return eff * eff.pct_change(periods=w)



# ===== features =====

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p90s_ema_w_base_v076_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _ema(base, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p105s_ema_w_base_v077_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _ema(base, 105) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p168s_ema_w_base_v078_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _ema(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p210s_ema_w_base_v079_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _ema(base, 210) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p315s_ema_w_base_v080_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _ema(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p420s_ema_w_base_v081_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = _ema(base, 420) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_logabs_base_v082_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_signxclose_base_v083_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = np.sign(base) * closeadj * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p10s_signxclose_base_v084_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = np.sign(base) * closeadj * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p21s_signxclose_base_v085_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = np.sign(base) * closeadj * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p42s_signxclose_base_v086_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = np.sign(base) * closeadj * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p63s_signxclose_base_v087_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = np.sign(base) * closeadj * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p126s_signxclose_base_v088_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = np.sign(base) * closeadj * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p189s_signxclose_base_v089_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = np.sign(base) * closeadj * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p252s_signxclose_base_v090_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = np.sign(base) * closeadj * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p378s_signxclose_base_v091_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = np.sign(base) * closeadj * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p504s_signxclose_base_v092_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = np.sign(base) * closeadj * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p7s_signxclose_base_v093_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = np.sign(base) * closeadj * _mean(closeadj, 7)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p14s_signxclose_base_v094_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = np.sign(base) * closeadj * _mean(closeadj, 14)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p30s_signxclose_base_v095_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = np.sign(base) * closeadj * _mean(closeadj, 30)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p45s_signxclose_base_v096_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = np.sign(base) * closeadj * _mean(closeadj, 45)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p90s_signxclose_base_v097_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = np.sign(base) * closeadj * _mean(closeadj, 90)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p105s_signxclose_base_v098_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = np.sign(base) * closeadj * _mean(closeadj, 105)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p168s_signxclose_base_v099_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = np.sign(base) * closeadj * _mean(closeadj, 168)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p210s_signxclose_base_v100_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = np.sign(base) * closeadj * _mean(closeadj, 210)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p315s_signxclose_base_v101_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = np.sign(base) * closeadj * _mean(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p420s_signxclose_base_v102_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = np.sign(base) * closeadj * _mean(closeadj, 420)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_diff_w_base_v103_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base.diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p10s_diff_w_base_v104_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base.diff(periods=10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p21s_diff_w_base_v105_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base.diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p42s_diff_w_base_v106_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base.diff(periods=42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p63s_diff_w_base_v107_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base.diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p126s_diff_w_base_v108_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base.diff(periods=126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p189s_diff_w_base_v109_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base.diff(periods=189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p252s_diff_w_base_v110_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base.diff(periods=252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p378s_diff_w_base_v111_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base.diff(periods=378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p504s_diff_w_base_v112_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base.diff(periods=504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p7s_diff_w_base_v113_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base.diff(periods=7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p14s_diff_w_base_v114_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base.diff(periods=14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p30s_diff_w_base_v115_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base.diff(periods=30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p45s_diff_w_base_v116_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base.diff(periods=45) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p90s_diff_w_base_v117_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base.diff(periods=90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p105s_diff_w_base_v118_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base.diff(periods=105) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p168s_diff_w_base_v119_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base.diff(periods=168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p210s_diff_w_base_v120_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base.diff(periods=210) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p315s_diff_w_base_v121_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base.diff(periods=315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p420s_diff_w_base_v122_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base.diff(periods=420) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_ratio_mean_base_v123_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = (base / _mean(base, 5).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p10s_ratio_mean_base_v124_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = (base / _mean(base, 10).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p21s_ratio_mean_base_v125_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = (base / _mean(base, 21).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p42s_ratio_mean_base_v126_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = (base / _mean(base, 42).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p63s_ratio_mean_base_v127_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = (base / _mean(base, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p126s_ratio_mean_base_v128_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = (base / _mean(base, 126).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p189s_ratio_mean_base_v129_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = (base / _mean(base, 189).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p252s_ratio_mean_base_v130_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = (base / _mean(base, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p378s_ratio_mean_base_v131_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = (base / _mean(base, 378).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p504s_ratio_mean_base_v132_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = (base / _mean(base, 504).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p7s_ratio_mean_base_v133_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = (base / _mean(base, 7).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p14s_ratio_mean_base_v134_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = (base / _mean(base, 14).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p30s_ratio_mean_base_v135_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = (base / _mean(base, 30).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p45s_ratio_mean_base_v136_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = (base / _mean(base, 45).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p90s_ratio_mean_base_v137_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = (base / _mean(base, 90).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p105s_ratio_mean_base_v138_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = (base / _mean(base, 105).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p168s_ratio_mean_base_v139_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = (base / _mean(base, 168).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p210s_ratio_mean_base_v140_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = (base / _mean(base, 210).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p315s_ratio_mean_base_v141_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = (base / _mean(base, 315).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p420s_ratio_mean_base_v142_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = (base / _mean(base, 420).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_xclose_mean_base_v143_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p10s_xclose_mean_base_v144_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p21s_xclose_mean_base_v145_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p42s_xclose_mean_base_v146_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p63s_xclose_mean_base_v147_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p126s_xclose_mean_base_v148_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p189s_xclose_mean_base_v149_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p252s_xclose_mean_base_v150_signal(assets, revenue, closeadj):
    base = _f25_revenue_per_asset(revenue, assets)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p90s_ema_w_base_v076_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p105s_ema_w_base_v077_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p168s_ema_w_base_v078_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p210s_ema_w_base_v079_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p315s_ema_w_base_v080_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p420s_ema_w_base_v081_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_logabs_base_v082_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_signxclose_base_v083_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p10s_signxclose_base_v084_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p21s_signxclose_base_v085_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p42s_signxclose_base_v086_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p63s_signxclose_base_v087_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p126s_signxclose_base_v088_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p189s_signxclose_base_v089_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p252s_signxclose_base_v090_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p378s_signxclose_base_v091_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p504s_signxclose_base_v092_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p7s_signxclose_base_v093_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p14s_signxclose_base_v094_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p30s_signxclose_base_v095_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p45s_signxclose_base_v096_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p90s_signxclose_base_v097_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p105s_signxclose_base_v098_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p168s_signxclose_base_v099_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p210s_signxclose_base_v100_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p315s_signxclose_base_v101_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p420s_signxclose_base_v102_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_diff_w_base_v103_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p10s_diff_w_base_v104_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p21s_diff_w_base_v105_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p42s_diff_w_base_v106_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p63s_diff_w_base_v107_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p126s_diff_w_base_v108_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p189s_diff_w_base_v109_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p252s_diff_w_base_v110_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p378s_diff_w_base_v111_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p504s_diff_w_base_v112_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p7s_diff_w_base_v113_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p14s_diff_w_base_v114_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p30s_diff_w_base_v115_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p45s_diff_w_base_v116_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p90s_diff_w_base_v117_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p105s_diff_w_base_v118_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p168s_diff_w_base_v119_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p210s_diff_w_base_v120_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p315s_diff_w_base_v121_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p420s_diff_w_base_v122_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_ratio_mean_base_v123_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p10s_ratio_mean_base_v124_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p21s_ratio_mean_base_v125_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p42s_ratio_mean_base_v126_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p63s_ratio_mean_base_v127_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p126s_ratio_mean_base_v128_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p189s_ratio_mean_base_v129_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p252s_ratio_mean_base_v130_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p378s_ratio_mean_base_v131_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p504s_ratio_mean_base_v132_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p7s_ratio_mean_base_v133_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p14s_ratio_mean_base_v134_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p30s_ratio_mean_base_v135_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p45s_ratio_mean_base_v136_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p90s_ratio_mean_base_v137_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p105s_ratio_mean_base_v138_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p168s_ratio_mean_base_v139_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p210s_ratio_mean_base_v140_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p315s_ratio_mean_base_v141_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p420s_ratio_mean_base_v142_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p5s_xclose_mean_base_v143_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p10s_xclose_mean_base_v144_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p21s_xclose_mean_base_v145_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p42s_xclose_mean_base_v146_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p63s_xclose_mean_base_v147_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p126s_xclose_mean_base_v148_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p189s_xclose_mean_base_v149_signal,
    f25tce_f25_transmission_capital_efficiency_revenue_per_asset_63p252s_xclose_mean_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_TRANSMISSION_CAPITAL_EFFICIENCY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    deferredrev = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")

    cols = {"closeadj": closeadj, "revenue": revenue, "ebitda": ebitda,
            "capex": capex, "assets": assets, "ppnenet": ppnenet,
            "deferredrev": deferredrev}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f25_revenue_per_asset', '_f25_capital_efficiency', '_f25_efficiency_compound')
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
    print(f"OK f25_transmission_capital_efficiency_076_150_claude: {n_features} features pass")
