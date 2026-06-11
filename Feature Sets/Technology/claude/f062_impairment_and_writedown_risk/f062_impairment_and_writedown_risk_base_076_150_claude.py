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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f062_intang_burden(intangibles, assets):
    return intangibles / assets.replace(0, np.nan).abs()


# 63d z-score of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_z_63d_base_v076_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_z_126d_base_v077_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_z_252d_base_v078_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_z_504d_base_v079_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_z_63d_base_v080_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_z_126d_base_v081_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_z_252d_base_v082_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_z_504d_base_v083_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_z_63d_base_v084_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_z_126d_base_v085_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_z_252d_base_v086_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_z_504d_base_v087_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_z_63d_base_v088_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_z_126d_base_v089_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_z_252d_base_v090_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_z_504d_base_v091_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_z_63d_base_v092_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_z_126d_base_v093_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_z_252d_base_v094_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_z_504d_base_v095_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_z_63d_base_v096_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_z_126d_base_v097_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_z_252d_base_v098_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_z_504d_base_v099_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_z_63d_base_v100_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_z_126d_base_v101_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_z_252d_base_v102_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_z_504d_base_v103_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_distmax_252d_base_v104_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_distmax_504d_base_v105_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_distmax_252d_base_v106_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_distmax_504d_base_v107_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_distmax_252d_base_v108_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_distmax_504d_base_v109_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_distmax_252d_base_v110_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_distmax_504d_base_v111_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_distmax_252d_base_v112_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_distmax_504d_base_v113_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_distmax_252d_base_v114_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_distmax_504d_base_v115_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_distmax_252d_base_v116_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_distmax_504d_base_v117_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_distmed_126d_base_v118_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_distmed_252d_base_v119_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_distmed_504d_base_v120_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_distmed_126d_base_v121_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_distmed_252d_base_v122_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_distmed_504d_base_v123_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_distmed_126d_base_v124_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_distmed_252d_base_v125_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_distmed_504d_base_v126_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_distmed_126d_base_v127_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_distmed_252d_base_v128_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_distmed_504d_base_v129_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_distmed_126d_base_v130_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_distmed_252d_base_v131_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_distmed_504d_base_v132_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_distmed_126d_base_v133_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_distmed_252d_base_v134_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_distmed_504d_base_v135_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_distmed_126d_base_v136_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_distmed_252d_base_v137_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_distmed_504d_base_v138_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_chg_63d_base_v139_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_chg_252d_base_v140_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_chg_63d_base_v141_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_chg_252d_base_v142_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_chg_63d_base_v143_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_chg_252d_base_v144_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_chg_63d_base_v145_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_chg_252d_base_v146_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_chg_63d_base_v147_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_chg_252d_base_v148_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_chg_63d_base_v149_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_chg_252d_base_v150_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

