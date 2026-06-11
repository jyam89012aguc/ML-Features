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
def _f004_net_cash(cashneq, investmentsc, debt):
    return cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)


def _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap):
    nc = cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)
    return nc / marketcap.replace(0, np.nan).abs()


def _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas):
    nc = cashneq.fillna(0) + investmentsc.fillna(0) - debt.fillna(0)
    return nc / sharesbas.replace(0, np.nan).abs()


# 21d slope of netcash_lvl
def f004ncp_f004_net_cash_position_netcash_lvl_slope_21d_2d_v001_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of netcash_lvl
def f004ncp_f004_net_cash_position_netcash_lvl_slope_63d_2d_v002_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of netcash_lvl
def f004ncp_f004_net_cash_position_netcash_lvl_slope_126d_2d_v003_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of netcash_lvl
def f004ncp_f004_net_cash_position_netcash_lvl_slope_252d_2d_v004_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of netcash_lvl
def f004ncp_f004_net_cash_position_netcash_lvl_slope_504d_2d_v005_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of netcash_per_mcap
def f004ncp_f004_net_cash_position_netcash_per_mcap_slope_21d_2d_v006_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of netcash_per_mcap
def f004ncp_f004_net_cash_position_netcash_per_mcap_slope_63d_2d_v007_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of netcash_per_mcap
def f004ncp_f004_net_cash_position_netcash_per_mcap_slope_126d_2d_v008_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of netcash_per_mcap
def f004ncp_f004_net_cash_position_netcash_per_mcap_slope_252d_2d_v009_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of netcash_per_mcap
def f004ncp_f004_net_cash_position_netcash_per_mcap_slope_504d_2d_v010_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of netcash_per_share
def f004ncp_f004_net_cash_position_netcash_per_share_slope_21d_2d_v011_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of netcash_per_share
def f004ncp_f004_net_cash_position_netcash_per_share_slope_63d_2d_v012_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of netcash_per_share
def f004ncp_f004_net_cash_position_netcash_per_share_slope_126d_2d_v013_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of netcash_per_share
def f004ncp_f004_net_cash_position_netcash_per_share_slope_252d_2d_v014_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of netcash_per_share
def f004ncp_f004_net_cash_position_netcash_per_share_slope_504d_2d_v015_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of netcash_per_asset
def f004ncp_f004_net_cash_position_netcash_per_asset_slope_21d_2d_v016_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of netcash_per_asset
def f004ncp_f004_net_cash_position_netcash_per_asset_slope_63d_2d_v017_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of netcash_per_asset
def f004ncp_f004_net_cash_position_netcash_per_asset_slope_126d_2d_v018_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of netcash_per_asset
def f004ncp_f004_net_cash_position_netcash_per_asset_slope_252d_2d_v019_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of netcash_per_asset
def f004ncp_f004_net_cash_position_netcash_per_asset_slope_504d_2d_v020_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of netcash_per_equity
def f004ncp_f004_net_cash_position_netcash_per_equity_slope_21d_2d_v021_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of netcash_per_equity
def f004ncp_f004_net_cash_position_netcash_per_equity_slope_63d_2d_v022_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of netcash_per_equity
def f004ncp_f004_net_cash_position_netcash_per_equity_slope_126d_2d_v023_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of netcash_per_equity
def f004ncp_f004_net_cash_position_netcash_per_equity_slope_252d_2d_v024_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of netcash_per_equity
def f004ncp_f004_net_cash_position_netcash_per_equity_slope_504d_2d_v025_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of netcash_per_ev
def f004ncp_f004_net_cash_position_netcash_per_ev_slope_21d_2d_v026_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of netcash_per_ev
def f004ncp_f004_net_cash_position_netcash_per_ev_slope_63d_2d_v027_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of netcash_per_ev
def f004ncp_f004_net_cash_position_netcash_per_ev_slope_126d_2d_v028_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of netcash_per_ev
def f004ncp_f004_net_cash_position_netcash_per_ev_slope_252d_2d_v029_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of netcash_per_ev
def f004ncp_f004_net_cash_position_netcash_per_ev_slope_504d_2d_v030_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of netcash_to_rnd
def f004ncp_f004_net_cash_position_netcash_to_rnd_slope_21d_2d_v031_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of netcash_to_rnd
def f004ncp_f004_net_cash_position_netcash_to_rnd_slope_63d_2d_v032_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of netcash_to_rnd
def f004ncp_f004_net_cash_position_netcash_to_rnd_slope_126d_2d_v033_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of netcash_to_rnd
def f004ncp_f004_net_cash_position_netcash_to_rnd_slope_252d_2d_v034_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of netcash_to_rnd
def f004ncp_f004_net_cash_position_netcash_to_rnd_slope_504d_2d_v035_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of netcash_lvl
def f004ncp_f004_net_cash_position_netcash_lvl_sm21_sl21_2d_v036_signal(cashneq, investmentsc, debt, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of netcash_lvl
def f004ncp_f004_net_cash_position_netcash_lvl_sm63_sl21_2d_v037_signal(cashneq, investmentsc, debt, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of netcash_lvl
def f004ncp_f004_net_cash_position_netcash_lvl_sm63_sl63_2d_v038_signal(cashneq, investmentsc, debt, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of netcash_lvl
def f004ncp_f004_net_cash_position_netcash_lvl_sm252_sl63_2d_v039_signal(cashneq, investmentsc, debt, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of netcash_lvl
def f004ncp_f004_net_cash_position_netcash_lvl_sm252_sl126_2d_v040_signal(cashneq, investmentsc, debt, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of netcash_per_mcap
def f004ncp_f004_net_cash_position_netcash_per_mcap_sm21_sl21_2d_v041_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _mean(_f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of netcash_per_mcap
def f004ncp_f004_net_cash_position_netcash_per_mcap_sm63_sl21_2d_v042_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _mean(_f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of netcash_per_mcap
def f004ncp_f004_net_cash_position_netcash_per_mcap_sm63_sl63_2d_v043_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _mean(_f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of netcash_per_mcap
def f004ncp_f004_net_cash_position_netcash_per_mcap_sm252_sl63_2d_v044_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _mean(_f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of netcash_per_mcap
def f004ncp_f004_net_cash_position_netcash_per_mcap_sm252_sl126_2d_v045_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _mean(_f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of netcash_per_share
def f004ncp_f004_net_cash_position_netcash_per_share_sm21_sl21_2d_v046_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _mean(_f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of netcash_per_share
def f004ncp_f004_net_cash_position_netcash_per_share_sm63_sl21_2d_v047_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _mean(_f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of netcash_per_share
def f004ncp_f004_net_cash_position_netcash_per_share_sm63_sl63_2d_v048_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _mean(_f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of netcash_per_share
def f004ncp_f004_net_cash_position_netcash_per_share_sm252_sl63_2d_v049_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _mean(_f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of netcash_per_share
def f004ncp_f004_net_cash_position_netcash_per_share_sm252_sl126_2d_v050_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _mean(_f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of netcash_per_asset
def f004ncp_f004_net_cash_position_netcash_per_asset_sm21_sl21_2d_v051_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of netcash_per_asset
def f004ncp_f004_net_cash_position_netcash_per_asset_sm63_sl21_2d_v052_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of netcash_per_asset
def f004ncp_f004_net_cash_position_netcash_per_asset_sm63_sl63_2d_v053_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of netcash_per_asset
def f004ncp_f004_net_cash_position_netcash_per_asset_sm252_sl63_2d_v054_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of netcash_per_asset
def f004ncp_f004_net_cash_position_netcash_per_asset_sm252_sl126_2d_v055_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of netcash_per_equity
def f004ncp_f004_net_cash_position_netcash_per_equity_sm21_sl21_2d_v056_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of netcash_per_equity
def f004ncp_f004_net_cash_position_netcash_per_equity_sm63_sl21_2d_v057_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of netcash_per_equity
def f004ncp_f004_net_cash_position_netcash_per_equity_sm63_sl63_2d_v058_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of netcash_per_equity
def f004ncp_f004_net_cash_position_netcash_per_equity_sm252_sl63_2d_v059_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of netcash_per_equity
def f004ncp_f004_net_cash_position_netcash_per_equity_sm252_sl126_2d_v060_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of netcash_per_ev
def f004ncp_f004_net_cash_position_netcash_per_ev_sm21_sl21_2d_v061_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of netcash_per_ev
def f004ncp_f004_net_cash_position_netcash_per_ev_sm63_sl21_2d_v062_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of netcash_per_ev
def f004ncp_f004_net_cash_position_netcash_per_ev_sm63_sl63_2d_v063_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of netcash_per_ev
def f004ncp_f004_net_cash_position_netcash_per_ev_sm252_sl63_2d_v064_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of netcash_per_ev
def f004ncp_f004_net_cash_position_netcash_per_ev_sm252_sl126_2d_v065_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of netcash_to_rnd
def f004ncp_f004_net_cash_position_netcash_to_rnd_sm21_sl21_2d_v066_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of netcash_to_rnd
def f004ncp_f004_net_cash_position_netcash_to_rnd_sm63_sl21_2d_v067_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of netcash_to_rnd
def f004ncp_f004_net_cash_position_netcash_to_rnd_sm63_sl63_2d_v068_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of netcash_to_rnd
def f004ncp_f004_net_cash_position_netcash_to_rnd_sm252_sl63_2d_v069_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of netcash_to_rnd
def f004ncp_f004_net_cash_position_netcash_to_rnd_sm252_sl126_2d_v070_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _mean(_f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of netcash_lvl
def f004ncp_f004_net_cash_position_netcash_lvl_pctslope_21d_2d_v071_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of netcash_lvl
def f004ncp_f004_net_cash_position_netcash_lvl_pctslope_63d_2d_v072_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of netcash_lvl
def f004ncp_f004_net_cash_position_netcash_lvl_pctslope_252d_2d_v073_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of netcash_per_mcap
def f004ncp_f004_net_cash_position_netcash_per_mcap_pctslope_21d_2d_v074_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of netcash_per_mcap
def f004ncp_f004_net_cash_position_netcash_per_mcap_pctslope_63d_2d_v075_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of netcash_per_mcap
def f004ncp_f004_net_cash_position_netcash_per_mcap_pctslope_252d_2d_v076_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of netcash_per_share
def f004ncp_f004_net_cash_position_netcash_per_share_pctslope_21d_2d_v077_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of netcash_per_share
def f004ncp_f004_net_cash_position_netcash_per_share_pctslope_63d_2d_v078_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of netcash_per_share
def f004ncp_f004_net_cash_position_netcash_per_share_pctslope_252d_2d_v079_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of netcash_per_asset
def f004ncp_f004_net_cash_position_netcash_per_asset_pctslope_21d_2d_v080_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of netcash_per_asset
def f004ncp_f004_net_cash_position_netcash_per_asset_pctslope_63d_2d_v081_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of netcash_per_asset
def f004ncp_f004_net_cash_position_netcash_per_asset_pctslope_252d_2d_v082_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of netcash_per_equity
def f004ncp_f004_net_cash_position_netcash_per_equity_pctslope_21d_2d_v083_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of netcash_per_equity
def f004ncp_f004_net_cash_position_netcash_per_equity_pctslope_63d_2d_v084_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of netcash_per_equity
def f004ncp_f004_net_cash_position_netcash_per_equity_pctslope_252d_2d_v085_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of netcash_per_ev
def f004ncp_f004_net_cash_position_netcash_per_ev_pctslope_21d_2d_v086_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of netcash_per_ev
def f004ncp_f004_net_cash_position_netcash_per_ev_pctslope_63d_2d_v087_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of netcash_per_ev
def f004ncp_f004_net_cash_position_netcash_per_ev_pctslope_252d_2d_v088_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of netcash_to_rnd
def f004ncp_f004_net_cash_position_netcash_to_rnd_pctslope_21d_2d_v089_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of netcash_to_rnd
def f004ncp_f004_net_cash_position_netcash_to_rnd_pctslope_63d_2d_v090_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of netcash_to_rnd
def f004ncp_f004_net_cash_position_netcash_to_rnd_pctslope_252d_2d_v091_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of netcash_lvl
def f004ncp_f004_net_cash_position_netcash_lvl_sgnslope_21d_2d_v092_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of netcash_lvl
def f004ncp_f004_net_cash_position_netcash_lvl_sgnslope_63d_2d_v093_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of netcash_lvl
def f004ncp_f004_net_cash_position_netcash_lvl_sgnslope_252d_2d_v094_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of netcash_per_mcap
def f004ncp_f004_net_cash_position_netcash_per_mcap_sgnslope_21d_2d_v095_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of netcash_per_mcap
def f004ncp_f004_net_cash_position_netcash_per_mcap_sgnslope_63d_2d_v096_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of netcash_per_mcap
def f004ncp_f004_net_cash_position_netcash_per_mcap_sgnslope_252d_2d_v097_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of netcash_per_share
def f004ncp_f004_net_cash_position_netcash_per_share_sgnslope_21d_2d_v098_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of netcash_per_share
def f004ncp_f004_net_cash_position_netcash_per_share_sgnslope_63d_2d_v099_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of netcash_per_share
def f004ncp_f004_net_cash_position_netcash_per_share_sgnslope_252d_2d_v100_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of netcash_per_asset
def f004ncp_f004_net_cash_position_netcash_per_asset_sgnslope_21d_2d_v101_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of netcash_per_asset
def f004ncp_f004_net_cash_position_netcash_per_asset_sgnslope_63d_2d_v102_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of netcash_per_asset
def f004ncp_f004_net_cash_position_netcash_per_asset_sgnslope_252d_2d_v103_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of netcash_per_equity
def f004ncp_f004_net_cash_position_netcash_per_equity_sgnslope_21d_2d_v104_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of netcash_per_equity
def f004ncp_f004_net_cash_position_netcash_per_equity_sgnslope_63d_2d_v105_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of netcash_per_equity
def f004ncp_f004_net_cash_position_netcash_per_equity_sgnslope_252d_2d_v106_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of netcash_per_ev
def f004ncp_f004_net_cash_position_netcash_per_ev_sgnslope_21d_2d_v107_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of netcash_per_ev
def f004ncp_f004_net_cash_position_netcash_per_ev_sgnslope_63d_2d_v108_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of netcash_per_ev
def f004ncp_f004_net_cash_position_netcash_per_ev_sgnslope_252d_2d_v109_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of netcash_to_rnd
def f004ncp_f004_net_cash_position_netcash_to_rnd_sgnslope_21d_2d_v110_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of netcash_to_rnd
def f004ncp_f004_net_cash_position_netcash_to_rnd_sgnslope_63d_2d_v111_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of netcash_to_rnd
def f004ncp_f004_net_cash_position_netcash_to_rnd_sgnslope_252d_2d_v112_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of netcash_lvl
def f004ncp_f004_net_cash_position_netcash_lvl_logmagslope_21d_2d_v113_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of netcash_lvl
def f004ncp_f004_net_cash_position_netcash_lvl_logmagslope_63d_2d_v114_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of netcash_lvl
def f004ncp_f004_net_cash_position_netcash_lvl_logmagslope_252d_2d_v115_signal(cashneq, investmentsc, debt, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of netcash_per_mcap
def f004ncp_f004_net_cash_position_netcash_per_mcap_logmagslope_21d_2d_v116_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of netcash_per_mcap
def f004ncp_f004_net_cash_position_netcash_per_mcap_logmagslope_63d_2d_v117_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of netcash_per_mcap
def f004ncp_f004_net_cash_position_netcash_per_mcap_logmagslope_252d_2d_v118_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = _f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of netcash_per_share
def f004ncp_f004_net_cash_position_netcash_per_share_logmagslope_21d_2d_v119_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of netcash_per_share
def f004ncp_f004_net_cash_position_netcash_per_share_logmagslope_63d_2d_v120_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of netcash_per_share
def f004ncp_f004_net_cash_position_netcash_per_share_logmagslope_252d_2d_v121_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = _f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of netcash_per_asset
def f004ncp_f004_net_cash_position_netcash_per_asset_logmagslope_21d_2d_v122_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of netcash_per_asset
def f004ncp_f004_net_cash_position_netcash_per_asset_logmagslope_63d_2d_v123_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of netcash_per_asset
def f004ncp_f004_net_cash_position_netcash_per_asset_logmagslope_252d_2d_v124_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of netcash_per_equity
def f004ncp_f004_net_cash_position_netcash_per_equity_logmagslope_21d_2d_v125_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of netcash_per_equity
def f004ncp_f004_net_cash_position_netcash_per_equity_logmagslope_63d_2d_v126_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of netcash_per_equity
def f004ncp_f004_net_cash_position_netcash_per_equity_logmagslope_252d_2d_v127_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of netcash_per_ev
def f004ncp_f004_net_cash_position_netcash_per_ev_logmagslope_21d_2d_v128_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of netcash_per_ev
def f004ncp_f004_net_cash_position_netcash_per_ev_logmagslope_63d_2d_v129_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of netcash_per_ev
def f004ncp_f004_net_cash_position_netcash_per_ev_logmagslope_252d_2d_v130_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of netcash_to_rnd
def f004ncp_f004_net_cash_position_netcash_to_rnd_logmagslope_21d_2d_v131_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of netcash_to_rnd
def f004ncp_f004_net_cash_position_netcash_to_rnd_logmagslope_63d_2d_v132_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of netcash_to_rnd
def f004ncp_f004_net_cash_position_netcash_to_rnd_logmagslope_252d_2d_v133_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = _f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|netcash_lvl|
def f004ncp_f004_net_cash_position_netcash_lvl_logslope_63d_2d_v134_signal(cashneq, investmentsc, debt, closeadj):
    base = np.log((_f004_net_cash(cashneq, investmentsc, debt)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|netcash_lvl|
def f004ncp_f004_net_cash_position_netcash_lvl_logslope_252d_2d_v135_signal(cashneq, investmentsc, debt, closeadj):
    base = np.log((_f004_net_cash(cashneq, investmentsc, debt)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|netcash_per_mcap|
def f004ncp_f004_net_cash_position_netcash_per_mcap_logslope_63d_2d_v136_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = np.log((_f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|netcash_per_mcap|
def f004ncp_f004_net_cash_position_netcash_per_mcap_logslope_252d_2d_v137_signal(cashneq, investmentsc, debt, marketcap, closeadj):
    base = np.log((_f004_net_cash_per_mcap(cashneq, investmentsc, debt, marketcap)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|netcash_per_share|
def f004ncp_f004_net_cash_position_netcash_per_share_logslope_63d_2d_v138_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = np.log((_f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|netcash_per_share|
def f004ncp_f004_net_cash_position_netcash_per_share_logslope_252d_2d_v139_signal(cashneq, investmentsc, debt, sharesbas, closeadj):
    base = np.log((_f004_net_cash_per_share(cashneq, investmentsc, debt, sharesbas)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|netcash_per_asset|
def f004ncp_f004_net_cash_position_netcash_per_asset_logslope_63d_2d_v140_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = np.log((_f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|netcash_per_asset|
def f004ncp_f004_net_cash_position_netcash_per_asset_logslope_252d_2d_v141_signal(cashneq, investmentsc, debt, assets, closeadj):
    base = np.log((_f004_net_cash(cashneq, investmentsc, debt) / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|netcash_per_equity|
def f004ncp_f004_net_cash_position_netcash_per_equity_logslope_63d_2d_v142_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = np.log((_f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|netcash_per_equity|
def f004ncp_f004_net_cash_position_netcash_per_equity_logslope_252d_2d_v143_signal(cashneq, investmentsc, debt, equity, closeadj):
    base = np.log((_f004_net_cash(cashneq, investmentsc, debt) / equity.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|netcash_per_ev|
def f004ncp_f004_net_cash_position_netcash_per_ev_logslope_63d_2d_v144_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = np.log((_f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|netcash_per_ev|
def f004ncp_f004_net_cash_position_netcash_per_ev_logslope_252d_2d_v145_signal(cashneq, investmentsc, debt, ev, closeadj):
    base = np.log((_f004_net_cash(cashneq, investmentsc, debt) / ev.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|netcash_to_rnd|
def f004ncp_f004_net_cash_position_netcash_to_rnd_logslope_63d_2d_v146_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = np.log((_f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|netcash_to_rnd|
def f004ncp_f004_net_cash_position_netcash_to_rnd_logslope_252d_2d_v147_signal(cashneq, investmentsc, debt, rnd, closeadj):
    base = np.log((_f004_net_cash(cashneq, investmentsc, debt) / rnd.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

