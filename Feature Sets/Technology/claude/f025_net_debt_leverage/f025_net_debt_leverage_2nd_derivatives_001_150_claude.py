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


# 21d slope of net_debt
def f025nde_f025_net_debt_leverage_net_debt_slope_21d_2d_v001_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of net_debt
def f025nde_f025_net_debt_leverage_net_debt_slope_63d_2d_v002_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of net_debt
def f025nde_f025_net_debt_leverage_net_debt_slope_126d_2d_v003_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of net_debt
def f025nde_f025_net_debt_leverage_net_debt_slope_252d_2d_v004_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of net_debt
def f025nde_f025_net_debt_leverage_net_debt_slope_504d_2d_v005_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_slope_21d_2d_v006_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_slope_63d_2d_v007_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_slope_126d_2d_v008_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_slope_252d_2d_v009_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_slope_504d_2d_v010_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_slope_21d_2d_v011_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_slope_63d_2d_v012_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_slope_126d_2d_v013_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_slope_252d_2d_v014_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_slope_504d_2d_v015_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_slope_21d_2d_v016_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_slope_63d_2d_v017_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_slope_126d_2d_v018_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_slope_252d_2d_v019_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_slope_504d_2d_v020_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_slope_21d_2d_v021_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_slope_63d_2d_v022_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_slope_126d_2d_v023_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_slope_252d_2d_v024_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_slope_504d_2d_v025_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_slope_21d_2d_v026_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_slope_63d_2d_v027_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_slope_126d_2d_v028_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_slope_252d_2d_v029_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_slope_504d_2d_v030_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_slope_21d_2d_v031_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_slope_63d_2d_v032_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_slope_126d_2d_v033_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_slope_252d_2d_v034_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_slope_504d_2d_v035_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of net_debt
def f025nde_f025_net_debt_leverage_net_debt_sm21_sl21_2d_v036_signal(debt, cashneq, investmentsc, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of net_debt
def f025nde_f025_net_debt_leverage_net_debt_sm63_sl21_2d_v037_signal(debt, cashneq, investmentsc, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of net_debt
def f025nde_f025_net_debt_leverage_net_debt_sm63_sl63_2d_v038_signal(debt, cashneq, investmentsc, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of net_debt
def f025nde_f025_net_debt_leverage_net_debt_sm252_sl63_2d_v039_signal(debt, cashneq, investmentsc, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of net_debt
def f025nde_f025_net_debt_leverage_net_debt_sm252_sl126_2d_v040_signal(debt, cashneq, investmentsc, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_sm21_sl21_2d_v041_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_sm63_sl21_2d_v042_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_sm63_sl63_2d_v043_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_sm252_sl63_2d_v044_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_sm252_sl126_2d_v045_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_sm21_sl21_2d_v046_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_sm63_sl21_2d_v047_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_sm63_sl63_2d_v048_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_sm252_sl63_2d_v049_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_sm252_sl126_2d_v050_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_sm21_sl21_2d_v051_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_sm63_sl21_2d_v052_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_sm63_sl63_2d_v053_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_sm252_sl63_2d_v054_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_sm252_sl126_2d_v055_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_sm21_sl21_2d_v056_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_sm63_sl21_2d_v057_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_sm63_sl63_2d_v058_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_sm252_sl63_2d_v059_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_sm252_sl126_2d_v060_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_sm21_sl21_2d_v061_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_sm63_sl21_2d_v062_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_sm63_sl63_2d_v063_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_sm252_sl63_2d_v064_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_sm252_sl126_2d_v065_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_sm21_sl21_2d_v066_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_sm63_sl21_2d_v067_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_sm63_sl63_2d_v068_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_sm252_sl63_2d_v069_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_sm252_sl126_2d_v070_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _mean(_f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of net_debt
def f025nde_f025_net_debt_leverage_net_debt_pctslope_21d_2d_v071_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of net_debt
def f025nde_f025_net_debt_leverage_net_debt_pctslope_63d_2d_v072_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of net_debt
def f025nde_f025_net_debt_leverage_net_debt_pctslope_252d_2d_v073_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_pctslope_21d_2d_v074_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_pctslope_63d_2d_v075_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_pctslope_252d_2d_v076_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_pctslope_21d_2d_v077_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_pctslope_63d_2d_v078_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_pctslope_252d_2d_v079_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_pctslope_21d_2d_v080_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_pctslope_63d_2d_v081_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_pctslope_252d_2d_v082_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_pctslope_21d_2d_v083_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_pctslope_63d_2d_v084_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_pctslope_252d_2d_v085_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_pctslope_21d_2d_v086_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_pctslope_63d_2d_v087_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_pctslope_252d_2d_v088_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_pctslope_21d_2d_v089_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_pctslope_63d_2d_v090_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_pctslope_252d_2d_v091_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of net_debt
def f025nde_f025_net_debt_leverage_net_debt_sgnslope_21d_2d_v092_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of net_debt
def f025nde_f025_net_debt_leverage_net_debt_sgnslope_63d_2d_v093_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of net_debt
def f025nde_f025_net_debt_leverage_net_debt_sgnslope_252d_2d_v094_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_sgnslope_21d_2d_v095_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_sgnslope_63d_2d_v096_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_sgnslope_252d_2d_v097_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_sgnslope_21d_2d_v098_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_sgnslope_63d_2d_v099_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_sgnslope_252d_2d_v100_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_sgnslope_21d_2d_v101_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_sgnslope_63d_2d_v102_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_sgnslope_252d_2d_v103_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_sgnslope_21d_2d_v104_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_sgnslope_63d_2d_v105_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_sgnslope_252d_2d_v106_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_sgnslope_21d_2d_v107_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_sgnslope_63d_2d_v108_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_sgnslope_252d_2d_v109_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_sgnslope_21d_2d_v110_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_sgnslope_63d_2d_v111_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_sgnslope_252d_2d_v112_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of net_debt
def f025nde_f025_net_debt_leverage_net_debt_logmagslope_21d_2d_v113_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of net_debt
def f025nde_f025_net_debt_leverage_net_debt_logmagslope_63d_2d_v114_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of net_debt
def f025nde_f025_net_debt_leverage_net_debt_logmagslope_252d_2d_v115_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_logmagslope_21d_2d_v116_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_logmagslope_63d_2d_v117_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_logmagslope_252d_2d_v118_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_logmagslope_21d_2d_v119_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_logmagslope_63d_2d_v120_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_logmagslope_252d_2d_v121_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_logmagslope_21d_2d_v122_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_logmagslope_63d_2d_v123_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_logmagslope_252d_2d_v124_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_logmagslope_21d_2d_v125_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_logmagslope_63d_2d_v126_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_logmagslope_252d_2d_v127_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_logmagslope_21d_2d_v128_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_logmagslope_63d_2d_v129_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_logmagslope_252d_2d_v130_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_logmagslope_21d_2d_v131_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_logmagslope_63d_2d_v132_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_logmagslope_252d_2d_v133_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|net_debt|
def f025nde_f025_net_debt_leverage_net_debt_logslope_63d_2d_v134_signal(debt, cashneq, investmentsc, closeadj):
    base = np.log((_f025_net_debt(debt, cashneq, investmentsc)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|net_debt|
def f025nde_f025_net_debt_leverage_net_debt_logslope_252d_2d_v135_signal(debt, cashneq, investmentsc, closeadj):
    base = np.log((_f025_net_debt(debt, cashneq, investmentsc)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|netdebt_to_ebitda|
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_logslope_63d_2d_v136_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = np.log((_f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|netdebt_to_ebitda|
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_logslope_252d_2d_v137_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = np.log((_f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|netdebt_to_asset|
def f025nde_f025_net_debt_leverage_netdebt_to_asset_logslope_63d_2d_v138_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = np.log((_f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|netdebt_to_asset|
def f025nde_f025_net_debt_leverage_netdebt_to_asset_logslope_252d_2d_v139_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = np.log((_f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|netdebt_to_mcap|
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_logslope_63d_2d_v140_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = np.log((_f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|netdebt_to_mcap|
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_logslope_252d_2d_v141_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = np.log((_f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|netdebt_to_equity|
def f025nde_f025_net_debt_leverage_netdebt_to_equity_logslope_63d_2d_v142_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = np.log((_f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|netdebt_to_equity|
def f025nde_f025_net_debt_leverage_netdebt_to_equity_logslope_252d_2d_v143_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = np.log((_f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|netdebt_to_ocf|
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_logslope_63d_2d_v144_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = np.log((_f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|netdebt_to_ocf|
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_logslope_252d_2d_v145_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = np.log((_f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|netdebt_to_fcf|
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_logslope_63d_2d_v146_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = np.log((_f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|netdebt_to_fcf|
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_logslope_252d_2d_v147_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = np.log((_f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

