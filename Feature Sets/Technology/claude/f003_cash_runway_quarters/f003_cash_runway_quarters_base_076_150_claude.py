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
def _f003_burn(ncfo):
    return (-ncfo).clip(lower=0)


def _f003_runway(cashneq, investmentsc, ncfo):
    burn = (-ncfo).clip(lower=0)
    return (cashneq.fillna(0) + investmentsc.fillna(0)) / burn.replace(0, np.nan)


def _f003_fcf_runway(cashneq, investmentsc, fcf):
    burn = (-fcf).clip(lower=0)
    return (cashneq.fillna(0) + investmentsc.fillna(0)) / burn.replace(0, np.nan)


# 63d z-score of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_z_63d_base_v076_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_z_126d_base_v077_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_z_252d_base_v078_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_z_504d_base_v079_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of runway
def f003cr_f003_cash_runway_quarters_runway_z_63d_base_v080_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of runway
def f003cr_f003_cash_runway_quarters_runway_z_126d_base_v081_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of runway
def f003cr_f003_cash_runway_quarters_runway_z_252d_base_v082_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of runway
def f003cr_f003_cash_runway_quarters_runway_z_504d_base_v083_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_z_63d_base_v084_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_z_126d_base_v085_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_z_252d_base_v086_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_z_504d_base_v087_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_z_63d_base_v088_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_z_126d_base_v089_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_z_252d_base_v090_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_z_504d_base_v091_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_z_63d_base_v092_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_z_126d_base_v093_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_z_252d_base_v094_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_z_504d_base_v095_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_z_63d_base_v096_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_z_126d_base_v097_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_z_252d_base_v098_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_z_504d_base_v099_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_z_63d_base_v100_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_z_126d_base_v101_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_z_252d_base_v102_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_z_504d_base_v103_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_distmax_252d_base_v104_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_distmax_504d_base_v105_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of runway
def f003cr_f003_cash_runway_quarters_runway_distmax_252d_base_v106_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of runway
def f003cr_f003_cash_runway_quarters_runway_distmax_504d_base_v107_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_distmax_252d_base_v108_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_distmax_504d_base_v109_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_distmax_252d_base_v110_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_distmax_504d_base_v111_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_distmax_252d_base_v112_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_distmax_504d_base_v113_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_distmax_252d_base_v114_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_distmax_504d_base_v115_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_distmax_252d_base_v116_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_distmax_504d_base_v117_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_distmed_126d_base_v118_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_distmed_252d_base_v119_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_distmed_504d_base_v120_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of runway
def f003cr_f003_cash_runway_quarters_runway_distmed_126d_base_v121_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of runway
def f003cr_f003_cash_runway_quarters_runway_distmed_252d_base_v122_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of runway
def f003cr_f003_cash_runway_quarters_runway_distmed_504d_base_v123_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_distmed_126d_base_v124_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_distmed_252d_base_v125_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_distmed_504d_base_v126_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_distmed_126d_base_v127_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_distmed_252d_base_v128_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_distmed_504d_base_v129_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_distmed_126d_base_v130_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_distmed_252d_base_v131_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_distmed_504d_base_v132_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_distmed_126d_base_v133_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_distmed_252d_base_v134_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_distmed_504d_base_v135_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_distmed_126d_base_v136_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_distmed_252d_base_v137_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_distmed_504d_base_v138_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_chg_63d_base_v139_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_chg_252d_base_v140_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in runway
def f003cr_f003_cash_runway_quarters_runway_chg_63d_base_v141_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in runway
def f003cr_f003_cash_runway_quarters_runway_chg_252d_base_v142_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_chg_63d_base_v143_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_chg_252d_base_v144_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_chg_63d_base_v145_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_chg_252d_base_v146_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_chg_63d_base_v147_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_chg_252d_base_v148_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_chg_63d_base_v149_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_chg_252d_base_v150_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

