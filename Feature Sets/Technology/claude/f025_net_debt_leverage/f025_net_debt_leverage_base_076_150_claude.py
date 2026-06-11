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
def _f025_net_debt(debt, cashneq, investmentsc):
    return debt.fillna(0) - cashneq.fillna(0) - investmentsc.fillna(0)


# 63d z-score of net_debt
def f025nde_f025_net_debt_leverage_net_debt_z_63d_base_v076_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of net_debt
def f025nde_f025_net_debt_leverage_net_debt_z_126d_base_v077_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of net_debt
def f025nde_f025_net_debt_leverage_net_debt_z_252d_base_v078_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of net_debt
def f025nde_f025_net_debt_leverage_net_debt_z_504d_base_v079_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_z_63d_base_v080_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_z_126d_base_v081_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_z_252d_base_v082_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_z_504d_base_v083_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_z_63d_base_v084_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_z_126d_base_v085_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_z_252d_base_v086_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_z_504d_base_v087_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_z_63d_base_v088_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_z_126d_base_v089_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_z_252d_base_v090_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_z_504d_base_v091_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_z_63d_base_v092_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_z_126d_base_v093_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_z_252d_base_v094_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_z_504d_base_v095_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_z_63d_base_v096_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_z_126d_base_v097_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_z_252d_base_v098_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_z_504d_base_v099_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_z_63d_base_v100_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_z_126d_base_v101_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_z_252d_base_v102_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_z_504d_base_v103_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of net_debt
def f025nde_f025_net_debt_leverage_net_debt_distmax_252d_base_v104_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of net_debt
def f025nde_f025_net_debt_leverage_net_debt_distmax_504d_base_v105_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_distmax_252d_base_v106_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_distmax_504d_base_v107_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_distmax_252d_base_v108_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_distmax_504d_base_v109_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_distmax_252d_base_v110_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_distmax_504d_base_v111_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_distmax_252d_base_v112_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_distmax_504d_base_v113_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_distmax_252d_base_v114_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_distmax_504d_base_v115_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_distmax_252d_base_v116_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_distmax_504d_base_v117_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of net_debt
def f025nde_f025_net_debt_leverage_net_debt_distmed_126d_base_v118_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of net_debt
def f025nde_f025_net_debt_leverage_net_debt_distmed_252d_base_v119_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of net_debt
def f025nde_f025_net_debt_leverage_net_debt_distmed_504d_base_v120_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_distmed_126d_base_v121_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_distmed_252d_base_v122_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_distmed_504d_base_v123_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_distmed_126d_base_v124_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_distmed_252d_base_v125_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_distmed_504d_base_v126_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_distmed_126d_base_v127_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_distmed_252d_base_v128_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_distmed_504d_base_v129_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_distmed_126d_base_v130_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_distmed_252d_base_v131_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_distmed_504d_base_v132_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_distmed_126d_base_v133_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_distmed_252d_base_v134_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_distmed_504d_base_v135_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_distmed_126d_base_v136_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_distmed_252d_base_v137_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_distmed_504d_base_v138_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in net_debt
def f025nde_f025_net_debt_leverage_net_debt_chg_63d_base_v139_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in net_debt
def f025nde_f025_net_debt_leverage_net_debt_chg_252d_base_v140_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_chg_63d_base_v141_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_chg_252d_base_v142_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_chg_63d_base_v143_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_chg_252d_base_v144_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_chg_63d_base_v145_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_chg_252d_base_v146_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_chg_63d_base_v147_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_chg_252d_base_v148_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_chg_63d_base_v149_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_chg_252d_base_v150_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

