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


# 21d mean of net_debt scaled by closeadj
def f025nde_f025_net_debt_leverage_net_debt_mean_21d_base_v001_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of net_debt scaled by closeadj
def f025nde_f025_net_debt_leverage_net_debt_mean_63d_base_v002_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of net_debt scaled by closeadj
def f025nde_f025_net_debt_leverage_net_debt_mean_126d_base_v003_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of net_debt scaled by closeadj
def f025nde_f025_net_debt_leverage_net_debt_mean_252d_base_v004_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of net_debt scaled by closeadj
def f025nde_f025_net_debt_leverage_net_debt_mean_504d_base_v005_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of netdebt_to_ebitda scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_mean_21d_base_v006_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of netdebt_to_ebitda scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_mean_63d_base_v007_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of netdebt_to_ebitda scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_mean_126d_base_v008_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of netdebt_to_ebitda scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_mean_252d_base_v009_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of netdebt_to_ebitda scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_mean_504d_base_v010_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of netdebt_to_asset scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_asset_mean_21d_base_v011_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of netdebt_to_asset scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_asset_mean_63d_base_v012_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of netdebt_to_asset scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_asset_mean_126d_base_v013_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of netdebt_to_asset scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_asset_mean_252d_base_v014_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of netdebt_to_asset scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_asset_mean_504d_base_v015_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of netdebt_to_mcap scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_mean_21d_base_v016_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of netdebt_to_mcap scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_mean_63d_base_v017_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of netdebt_to_mcap scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_mean_126d_base_v018_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of netdebt_to_mcap scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_mean_252d_base_v019_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of netdebt_to_mcap scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_mean_504d_base_v020_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of netdebt_to_equity scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_equity_mean_21d_base_v021_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of netdebt_to_equity scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_equity_mean_63d_base_v022_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of netdebt_to_equity scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_equity_mean_126d_base_v023_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of netdebt_to_equity scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_equity_mean_252d_base_v024_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of netdebt_to_equity scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_equity_mean_504d_base_v025_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of netdebt_to_ocf scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_mean_21d_base_v026_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of netdebt_to_ocf scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_mean_63d_base_v027_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of netdebt_to_ocf scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_mean_126d_base_v028_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of netdebt_to_ocf scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_mean_252d_base_v029_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of netdebt_to_ocf scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_mean_504d_base_v030_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of netdebt_to_fcf scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_mean_21d_base_v031_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of netdebt_to_fcf scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_mean_63d_base_v032_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of netdebt_to_fcf scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_mean_126d_base_v033_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of netdebt_to_fcf scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_mean_252d_base_v034_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of netdebt_to_fcf scaled by closeadj
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_mean_504d_base_v035_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of net_debt
def f025nde_f025_net_debt_leverage_net_debt_median_63d_base_v036_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of net_debt
def f025nde_f025_net_debt_leverage_net_debt_median_252d_base_v037_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of net_debt
def f025nde_f025_net_debt_leverage_net_debt_median_504d_base_v038_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_median_63d_base_v039_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_median_252d_base_v040_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_median_504d_base_v041_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_median_63d_base_v042_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_median_252d_base_v043_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_median_504d_base_v044_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_median_63d_base_v045_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_median_252d_base_v046_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_median_504d_base_v047_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_median_63d_base_v048_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_median_252d_base_v049_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_median_504d_base_v050_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_median_63d_base_v051_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_median_252d_base_v052_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_median_504d_base_v053_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_median_63d_base_v054_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_median_252d_base_v055_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_median_504d_base_v056_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of net_debt
def f025nde_f025_net_debt_leverage_net_debt_rmax_252d_base_v057_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of net_debt
def f025nde_f025_net_debt_leverage_net_debt_rmax_504d_base_v058_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_rmax_252d_base_v059_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_rmax_504d_base_v060_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_rmax_252d_base_v061_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_rmax_504d_base_v062_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_rmax_252d_base_v063_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of netdebt_to_mcap
def f025nde_f025_net_debt_leverage_netdebt_to_mcap_rmax_504d_base_v064_signal(debt, cashneq, investmentsc, marketcap, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_rmax_252d_base_v065_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of netdebt_to_equity
def f025nde_f025_net_debt_leverage_netdebt_to_equity_rmax_504d_base_v066_signal(debt, cashneq, investmentsc, equity, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / equity.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_rmax_252d_base_v067_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of netdebt_to_ocf
def f025nde_f025_net_debt_leverage_netdebt_to_ocf_rmax_504d_base_v068_signal(debt, cashneq, investmentsc, ncfo, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ncfo.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_rmax_252d_base_v069_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of netdebt_to_fcf
def f025nde_f025_net_debt_leverage_netdebt_to_fcf_rmax_504d_base_v070_signal(debt, cashneq, investmentsc, fcf, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / fcf.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of net_debt
def f025nde_f025_net_debt_leverage_net_debt_rmin_252d_base_v071_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of net_debt
def f025nde_f025_net_debt_leverage_net_debt_rmin_504d_base_v072_signal(debt, cashneq, investmentsc, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_rmin_252d_base_v073_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of netdebt_to_ebitda
def f025nde_f025_net_debt_leverage_netdebt_to_ebitda_rmin_504d_base_v074_signal(debt, cashneq, investmentsc, ebitda, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / ebitda.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of netdebt_to_asset
def f025nde_f025_net_debt_leverage_netdebt_to_asset_rmin_252d_base_v075_signal(debt, cashneq, investmentsc, assets, closeadj):
    base = _f025_net_debt(debt, cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

