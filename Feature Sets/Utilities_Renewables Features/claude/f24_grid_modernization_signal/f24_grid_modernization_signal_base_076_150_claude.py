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
def _f24_asset_growth(assets, w):
    return assets.pct_change(periods=w)


def _f24_capex_pulse(capex, w):
    m = capex.rolling(w, min_periods=max(1, w // 2)).mean()
    return (capex - m) / m.replace(0, np.nan)


def _f24_modernization_score(assets, capex, ppnenet, w):
    ag = assets.pct_change(periods=w)
    cp = capex / ppnenet.replace(0, np.nan)
    return ag * cp



# ===== features =====

def f24gms_f24_grid_modernization_signal_asset_growth_5p90s_ema_w_base_v076_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = _ema(base, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p105s_ema_w_base_v077_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = _ema(base, 105) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p168s_ema_w_base_v078_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = _ema(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p210s_ema_w_base_v079_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = _ema(base, 210) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p315s_ema_w_base_v080_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = _ema(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p420s_ema_w_base_v081_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = _ema(base, 420) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p5s_logabs_base_v082_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p5s_signxclose_base_v083_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = np.sign(base) * closeadj * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p10s_signxclose_base_v084_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = np.sign(base) * closeadj * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p21s_signxclose_base_v085_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = np.sign(base) * closeadj * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p42s_signxclose_base_v086_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = np.sign(base) * closeadj * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p63s_signxclose_base_v087_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = np.sign(base) * closeadj * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p126s_signxclose_base_v088_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = np.sign(base) * closeadj * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p189s_signxclose_base_v089_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = np.sign(base) * closeadj * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p252s_signxclose_base_v090_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = np.sign(base) * closeadj * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p378s_signxclose_base_v091_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = np.sign(base) * closeadj * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p504s_signxclose_base_v092_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = np.sign(base) * closeadj * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p7s_signxclose_base_v093_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = np.sign(base) * closeadj * _mean(closeadj, 7)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p14s_signxclose_base_v094_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = np.sign(base) * closeadj * _mean(closeadj, 14)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p30s_signxclose_base_v095_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = np.sign(base) * closeadj * _mean(closeadj, 30)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p45s_signxclose_base_v096_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = np.sign(base) * closeadj * _mean(closeadj, 45)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p90s_signxclose_base_v097_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = np.sign(base) * closeadj * _mean(closeadj, 90)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p105s_signxclose_base_v098_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = np.sign(base) * closeadj * _mean(closeadj, 105)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p168s_signxclose_base_v099_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = np.sign(base) * closeadj * _mean(closeadj, 168)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p210s_signxclose_base_v100_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = np.sign(base) * closeadj * _mean(closeadj, 210)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p315s_signxclose_base_v101_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = np.sign(base) * closeadj * _mean(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p420s_signxclose_base_v102_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = np.sign(base) * closeadj * _mean(closeadj, 420)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p5s_diff_w_base_v103_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base.diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p10s_diff_w_base_v104_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base.diff(periods=10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p21s_diff_w_base_v105_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base.diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p42s_diff_w_base_v106_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base.diff(periods=42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p63s_diff_w_base_v107_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base.diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p126s_diff_w_base_v108_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base.diff(periods=126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p189s_diff_w_base_v109_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base.diff(periods=189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p252s_diff_w_base_v110_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base.diff(periods=252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p378s_diff_w_base_v111_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base.diff(periods=378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p504s_diff_w_base_v112_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base.diff(periods=504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p7s_diff_w_base_v113_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base.diff(periods=7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p14s_diff_w_base_v114_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base.diff(periods=14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p30s_diff_w_base_v115_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base.diff(periods=30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p45s_diff_w_base_v116_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base.diff(periods=45) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p90s_diff_w_base_v117_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base.diff(periods=90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p105s_diff_w_base_v118_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base.diff(periods=105) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p168s_diff_w_base_v119_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base.diff(periods=168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p210s_diff_w_base_v120_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base.diff(periods=210) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p315s_diff_w_base_v121_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base.diff(periods=315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p420s_diff_w_base_v122_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base.diff(periods=420) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p5s_ratio_mean_base_v123_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = (base / _mean(base, 5).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p10s_ratio_mean_base_v124_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = (base / _mean(base, 10).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p21s_ratio_mean_base_v125_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = (base / _mean(base, 21).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p42s_ratio_mean_base_v126_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = (base / _mean(base, 42).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p63s_ratio_mean_base_v127_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = (base / _mean(base, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p126s_ratio_mean_base_v128_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = (base / _mean(base, 126).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p189s_ratio_mean_base_v129_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = (base / _mean(base, 189).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p252s_ratio_mean_base_v130_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = (base / _mean(base, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p378s_ratio_mean_base_v131_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = (base / _mean(base, 378).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p504s_ratio_mean_base_v132_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = (base / _mean(base, 504).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p7s_ratio_mean_base_v133_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = (base / _mean(base, 7).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p14s_ratio_mean_base_v134_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = (base / _mean(base, 14).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p30s_ratio_mean_base_v135_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = (base / _mean(base, 30).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p45s_ratio_mean_base_v136_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = (base / _mean(base, 45).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p90s_ratio_mean_base_v137_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = (base / _mean(base, 90).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p105s_ratio_mean_base_v138_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = (base / _mean(base, 105).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p168s_ratio_mean_base_v139_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = (base / _mean(base, 168).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p210s_ratio_mean_base_v140_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = (base / _mean(base, 210).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p315s_ratio_mean_base_v141_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = (base / _mean(base, 315).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p420s_ratio_mean_base_v142_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = (base / _mean(base, 420).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p5s_xclose_mean_base_v143_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p10s_xclose_mean_base_v144_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p21s_xclose_mean_base_v145_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p42s_xclose_mean_base_v146_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p63s_xclose_mean_base_v147_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p126s_xclose_mean_base_v148_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p189s_xclose_mean_base_v149_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f24gms_f24_grid_modernization_signal_asset_growth_5p252s_xclose_mean_base_v150_signal(assets, closeadj):
    base = _f24_asset_growth(assets, 5)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f24gms_f24_grid_modernization_signal_asset_growth_5p90s_ema_w_base_v076_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p105s_ema_w_base_v077_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p168s_ema_w_base_v078_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p210s_ema_w_base_v079_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p315s_ema_w_base_v080_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p420s_ema_w_base_v081_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p5s_logabs_base_v082_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p5s_signxclose_base_v083_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p10s_signxclose_base_v084_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p21s_signxclose_base_v085_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p42s_signxclose_base_v086_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p63s_signxclose_base_v087_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p126s_signxclose_base_v088_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p189s_signxclose_base_v089_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p252s_signxclose_base_v090_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p378s_signxclose_base_v091_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p504s_signxclose_base_v092_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p7s_signxclose_base_v093_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p14s_signxclose_base_v094_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p30s_signxclose_base_v095_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p45s_signxclose_base_v096_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p90s_signxclose_base_v097_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p105s_signxclose_base_v098_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p168s_signxclose_base_v099_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p210s_signxclose_base_v100_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p315s_signxclose_base_v101_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p420s_signxclose_base_v102_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p5s_diff_w_base_v103_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p10s_diff_w_base_v104_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p21s_diff_w_base_v105_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p42s_diff_w_base_v106_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p63s_diff_w_base_v107_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p126s_diff_w_base_v108_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p189s_diff_w_base_v109_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p252s_diff_w_base_v110_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p378s_diff_w_base_v111_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p504s_diff_w_base_v112_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p7s_diff_w_base_v113_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p14s_diff_w_base_v114_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p30s_diff_w_base_v115_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p45s_diff_w_base_v116_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p90s_diff_w_base_v117_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p105s_diff_w_base_v118_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p168s_diff_w_base_v119_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p210s_diff_w_base_v120_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p315s_diff_w_base_v121_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p420s_diff_w_base_v122_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p5s_ratio_mean_base_v123_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p10s_ratio_mean_base_v124_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p21s_ratio_mean_base_v125_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p42s_ratio_mean_base_v126_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p63s_ratio_mean_base_v127_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p126s_ratio_mean_base_v128_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p189s_ratio_mean_base_v129_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p252s_ratio_mean_base_v130_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p378s_ratio_mean_base_v131_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p504s_ratio_mean_base_v132_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p7s_ratio_mean_base_v133_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p14s_ratio_mean_base_v134_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p30s_ratio_mean_base_v135_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p45s_ratio_mean_base_v136_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p90s_ratio_mean_base_v137_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p105s_ratio_mean_base_v138_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p168s_ratio_mean_base_v139_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p210s_ratio_mean_base_v140_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p315s_ratio_mean_base_v141_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p420s_ratio_mean_base_v142_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p5s_xclose_mean_base_v143_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p10s_xclose_mean_base_v144_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p21s_xclose_mean_base_v145_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p42s_xclose_mean_base_v146_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p63s_xclose_mean_base_v147_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p126s_xclose_mean_base_v148_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p189s_xclose_mean_base_v149_signal,
    f24gms_f24_grid_modernization_signal_asset_growth_5p252s_xclose_mean_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F24_GRID_MODERNIZATION_SIGNAL_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ('_f24_asset_growth', '_f24_capex_pulse', '_f24_modernization_score')
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
    print(f"OK f24_grid_modernization_signal_076_150_claude: {n_features} features pass")
