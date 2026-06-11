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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f025_net_debt(debt, cashneq, investmentsc):
    return debt.fillna(0) - cashneq.fillna(0) - investmentsc.fillna(0)


# 21d acceleration of net_debt
def f025nde_f025_net_debt_leverage_net_debt_accel_21d_3d_v001_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of net_debt
def f025nde_f025_net_debt_leverage_net_debt_accel_63d_3d_v002_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of net_debt
def f025nde_f025_net_debt_leverage_net_debt_accel_126d_3d_v003_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of net_debt
def f025nde_f025_net_debt_leverage_net_debt_accel_252d_3d_v004_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_accel_21d_3d_v005_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_accel_63d_3d_v006_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_accel_126d_3d_v007_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_accel_252d_3d_v008_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_accel_21d_3d_v009_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_accel_63d_3d_v010_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_accel_126d_3d_v011_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_accel_252d_3d_v012_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_accel_21d_3d_v013_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_accel_63d_3d_v014_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_accel_126d_3d_v015_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_accel_252d_3d_v016_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_accel_21d_3d_v017_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_accel_63d_3d_v018_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_accel_126d_3d_v019_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_accel_252d_3d_v020_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_accel_21d_3d_v021_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_accel_63d_3d_v022_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_accel_126d_3d_v023_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_accel_252d_3d_v024_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_accel_21d_3d_v025_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_accel_63d_3d_v026_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_accel_126d_3d_v027_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_accel_252d_3d_v028_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of net_debt
def f025nde_f025_net_debt_leverage_net_debt_slopez_21d_z126_3d_v029_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of net_debt
def f025nde_f025_net_debt_leverage_net_debt_slopez_63d_z252_3d_v030_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of net_debt
def f025nde_f025_net_debt_leverage_net_debt_slopez_126d_z252_3d_v031_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of net_debt
def f025nde_f025_net_debt_leverage_net_debt_slopez_252d_z504_3d_v032_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_slopez_21d_z126_3d_v033_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_slopez_63d_z252_3d_v034_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_slopez_126d_z252_3d_v035_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_slopez_252d_z504_3d_v036_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_slopez_21d_z126_3d_v037_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_slopez_63d_z252_3d_v038_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_slopez_126d_z252_3d_v039_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_slopez_252d_z504_3d_v040_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_slopez_21d_z126_3d_v041_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_slopez_63d_z252_3d_v042_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_slopez_126d_z252_3d_v043_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_slopez_252d_z504_3d_v044_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_slopez_21d_z126_3d_v045_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_slopez_63d_z252_3d_v046_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_slopez_126d_z252_3d_v047_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_slopez_252d_z504_3d_v048_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_slopez_21d_z126_3d_v049_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_slopez_63d_z252_3d_v050_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_slopez_126d_z252_3d_v051_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_slopez_252d_z504_3d_v052_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_slopez_21d_z126_3d_v053_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_slopez_63d_z252_3d_v054_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_slopez_126d_z252_3d_v055_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_slopez_252d_z504_3d_v056_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of net_debt
def f025nde_f025_net_debt_leverage_net_debt_jerk_21d_3d_v057_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of net_debt
def f025nde_f025_net_debt_leverage_net_debt_jerk_63d_3d_v058_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of net_debt
def f025nde_f025_net_debt_leverage_net_debt_jerk_126d_3d_v059_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_jerk_21d_3d_v060_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_jerk_63d_3d_v061_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_jerk_126d_3d_v062_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_jerk_21d_3d_v063_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_jerk_63d_3d_v064_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_jerk_126d_3d_v065_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_jerk_21d_3d_v066_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_jerk_63d_3d_v067_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_jerk_126d_3d_v068_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_jerk_21d_3d_v069_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_jerk_63d_3d_v070_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_jerk_126d_3d_v071_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_jerk_21d_3d_v072_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_jerk_63d_3d_v073_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_jerk_126d_3d_v074_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_jerk_21d_3d_v075_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_jerk_63d_3d_v076_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_jerk_126d_3d_v077_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of net_debt smoothed over 252d
def f025nde_f025_net_debt_leverage_net_debt_smoothaccel_63d_sm252_3d_v078_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of net_debt smoothed over 504d
def f025nde_f025_net_debt_leverage_net_debt_smoothaccel_252d_sm504_3d_v079_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of netdebt_to_ebitda smoothed over 252d
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_smoothaccel_63d_sm252_3d_v080_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of netdebt_to_ebitda smoothed over 504d
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_smoothaccel_252d_sm504_3d_v081_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of netdebt_to_asset smoothed over 252d
def f025nde_f025_net_debt_leverage_netdebt_to_asset_smoothaccel_63d_sm252_3d_v082_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of netdebt_to_asset smoothed over 504d
def f025nde_f025_net_debt_leverage_netdebt_to_asset_smoothaccel_252d_sm504_3d_v083_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of netdebt_to_mcap smoothed over 252d
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_smoothaccel_63d_sm252_3d_v084_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of netdebt_to_mcap smoothed over 504d
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_smoothaccel_252d_sm504_3d_v085_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of netdebt_to_equity smoothed over 252d
def f025nde_f025_net_debt_leverage_netdebt_to_equity_smoothaccel_63d_sm252_3d_v086_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of netdebt_to_equity smoothed over 504d
def f025nde_f025_net_debt_leverage_netdebt_to_equity_smoothaccel_252d_sm504_3d_v087_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of netdebt_to_ocf smoothed over 252d
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_smoothaccel_63d_sm252_3d_v088_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of netdebt_to_ocf smoothed over 504d
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_smoothaccel_252d_sm504_3d_v089_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of netdebt_to_fcf smoothed over 252d
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_smoothaccel_63d_sm252_3d_v090_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of netdebt_to_fcf smoothed over 504d
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_smoothaccel_252d_sm504_3d_v091_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of net_debt
def f025nde_f025_net_debt_leverage_net_debt_accelz_21d_z252_3d_v092_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of net_debt
def f025nde_f025_net_debt_leverage_net_debt_accelz_63d_z504_3d_v093_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_accelz_21d_z252_3d_v094_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_accelz_63d_z504_3d_v095_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_accelz_21d_z252_3d_v096_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_accelz_63d_z504_3d_v097_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_accelz_21d_z252_3d_v098_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_accelz_63d_z504_3d_v099_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_accelz_21d_z252_3d_v100_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_accelz_63d_z504_3d_v101_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_accelz_21d_z252_3d_v102_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_accelz_63d_z504_3d_v103_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_accelz_21d_z252_3d_v104_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_accelz_63d_z504_3d_v105_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in net_debt (raw count, no price scaling)
def f025nde_f025_net_debt_leverage_net_debt_signflip_63d_3d_v106_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in net_debt (raw count, no price scaling)
def f025nde_f025_net_debt_leverage_net_debt_signflip_252d_3d_v107_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in netdebt_to_ebitda (raw count, no price scaling)
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_signflip_63d_3d_v108_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in netdebt_to_ebitda (raw count, no price scaling)
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_signflip_252d_3d_v109_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in netdebt_to_asset (raw count, no price scaling)
def f025nde_f025_net_debt_leverage_netdebt_to_asset_signflip_63d_3d_v110_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in netdebt_to_asset (raw count, no price scaling)
def f025nde_f025_net_debt_leverage_netdebt_to_asset_signflip_252d_3d_v111_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in netdebt_to_mcap (raw count, no price scaling)
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_signflip_63d_3d_v112_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in netdebt_to_mcap (raw count, no price scaling)
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_signflip_252d_3d_v113_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in netdebt_to_equity (raw count, no price scaling)
def f025nde_f025_net_debt_leverage_netdebt_to_equity_signflip_63d_3d_v114_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in netdebt_to_equity (raw count, no price scaling)
def f025nde_f025_net_debt_leverage_netdebt_to_equity_signflip_252d_3d_v115_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in netdebt_to_ocf (raw count, no price scaling)
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_signflip_63d_3d_v116_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in netdebt_to_ocf (raw count, no price scaling)
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_signflip_252d_3d_v117_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in netdebt_to_fcf (raw count, no price scaling)
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_signflip_63d_3d_v118_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in netdebt_to_fcf (raw count, no price scaling)
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_signflip_252d_3d_v119_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of net_debt normalized by 252d range
def f025nde_f025_net_debt_leverage_net_debt_rngaccel_63d_r252_3d_v120_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of net_debt normalized by 504d range
def f025nde_f025_net_debt_leverage_net_debt_rngaccel_252d_r504_3d_v121_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of netdebt_to_ebitda normalized by 252d range
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_rngaccel_63d_r252_3d_v122_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of netdebt_to_ebitda normalized by 504d range
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_rngaccel_252d_r504_3d_v123_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of netdebt_to_asset normalized by 252d range
def f025nde_f025_net_debt_leverage_netdebt_to_asset_rngaccel_63d_r252_3d_v124_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of netdebt_to_asset normalized by 504d range
def f025nde_f025_net_debt_leverage_netdebt_to_asset_rngaccel_252d_r504_3d_v125_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of netdebt_to_mcap normalized by 252d range
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_rngaccel_63d_r252_3d_v126_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of netdebt_to_mcap normalized by 504d range
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_rngaccel_252d_r504_3d_v127_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of netdebt_to_equity normalized by 252d range
def f025nde_f025_net_debt_leverage_netdebt_to_equity_rngaccel_63d_r252_3d_v128_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of netdebt_to_equity normalized by 504d range
def f025nde_f025_net_debt_leverage_netdebt_to_equity_rngaccel_252d_r504_3d_v129_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of netdebt_to_ocf normalized by 252d range
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_rngaccel_63d_r252_3d_v130_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of netdebt_to_ocf normalized by 504d range
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_rngaccel_252d_r504_3d_v131_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of netdebt_to_fcf normalized by 252d range
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_rngaccel_63d_r252_3d_v132_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of netdebt_to_fcf normalized by 504d range
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_rngaccel_252d_r504_3d_v133_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of net_debt
def f025nde_f025_net_debt_leverage_net_debt_cumslope_21d_3d_v134_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of net_debt
def f025nde_f025_net_debt_leverage_net_debt_cumslope_63d_3d_v135_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of net_debt
def f025nde_f025_net_debt_leverage_net_debt_cumslope_252d_3d_v136_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_cumslope_21d_3d_v137_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_cumslope_63d_3d_v138_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_cumslope_252d_3d_v139_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_cumslope_21d_3d_v140_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_cumslope_63d_3d_v141_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_cumslope_252d_3d_v142_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_cumslope_21d_3d_v143_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_cumslope_63d_3d_v144_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_cumslope_252d_3d_v145_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_cumslope_21d_3d_v146_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_cumslope_63d_3d_v147_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_cumslope_252d_3d_v148_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_cumslope_21d_3d_v149_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_cumslope_63d_3d_v150_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

