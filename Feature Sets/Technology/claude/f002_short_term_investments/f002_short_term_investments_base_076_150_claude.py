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
def _f002_sti(investmentsc):
    return investmentsc.fillna(0)


def _f002_liquid_pool(cashneq, investmentsc):
    return cashneq.fillna(0) + investmentsc.fillna(0)


def _f002_sti_to_total_inv(investmentsc, investments):
    return investmentsc / investments.replace(0, np.nan).abs()


# 63d z-score of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_z_63d_base_v076_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_z_126d_base_v077_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_z_252d_base_v078_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_z_504d_base_v079_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of liqpool
def f002sti_f002_short_term_investments_liqpool_z_63d_base_v080_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of liqpool
def f002sti_f002_short_term_investments_liqpool_z_126d_base_v081_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of liqpool
def f002sti_f002_short_term_investments_liqpool_z_252d_base_v082_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of liqpool
def f002sti_f002_short_term_investments_liqpool_z_504d_base_v083_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_z_63d_base_v084_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_z_126d_base_v085_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_z_252d_base_v086_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_z_504d_base_v087_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_z_63d_base_v088_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_z_126d_base_v089_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_z_252d_base_v090_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_z_504d_base_v091_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_z_63d_base_v092_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_z_126d_base_v093_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_z_252d_base_v094_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_z_504d_base_v095_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_z_63d_base_v096_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_z_126d_base_v097_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_z_252d_base_v098_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_z_504d_base_v099_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_z_63d_base_v100_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_z_126d_base_v101_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_z_252d_base_v102_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_z_504d_base_v103_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_distmax_252d_base_v104_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_distmax_504d_base_v105_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of liqpool
def f002sti_f002_short_term_investments_liqpool_distmax_252d_base_v106_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of liqpool
def f002sti_f002_short_term_investments_liqpool_distmax_504d_base_v107_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_distmax_252d_base_v108_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_distmax_504d_base_v109_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_distmax_252d_base_v110_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_distmax_504d_base_v111_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_distmax_252d_base_v112_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_distmax_504d_base_v113_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_distmax_252d_base_v114_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_distmax_504d_base_v115_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_distmax_252d_base_v116_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_distmax_504d_base_v117_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_distmed_126d_base_v118_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_distmed_252d_base_v119_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_distmed_504d_base_v120_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of liqpool
def f002sti_f002_short_term_investments_liqpool_distmed_126d_base_v121_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of liqpool
def f002sti_f002_short_term_investments_liqpool_distmed_252d_base_v122_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of liqpool
def f002sti_f002_short_term_investments_liqpool_distmed_504d_base_v123_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_distmed_126d_base_v124_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_distmed_252d_base_v125_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_distmed_504d_base_v126_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_distmed_126d_base_v127_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_distmed_252d_base_v128_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_distmed_504d_base_v129_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_distmed_126d_base_v130_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_distmed_252d_base_v131_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_distmed_504d_base_v132_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_distmed_126d_base_v133_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_distmed_252d_base_v134_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_distmed_504d_base_v135_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_distmed_126d_base_v136_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_distmed_252d_base_v137_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_distmed_504d_base_v138_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_chg_63d_base_v139_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_chg_252d_base_v140_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in liqpool
def f002sti_f002_short_term_investments_liqpool_chg_63d_base_v141_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in liqpool
def f002sti_f002_short_term_investments_liqpool_chg_252d_base_v142_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_chg_63d_base_v143_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_chg_252d_base_v144_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_chg_63d_base_v145_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_chg_252d_base_v146_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_chg_63d_base_v147_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_chg_252d_base_v148_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_chg_63d_base_v149_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_chg_252d_base_v150_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

