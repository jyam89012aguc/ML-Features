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
    return s.ewm(span=w, adjust=False, min_periods=max(1, w // 2)).mean()


# ===== folder domain primitives =====
def _f36_inv_days(inventory, cor):
    # Inventory days = inventory / (annualized cogs / 365)
    daily_cor = _mean(cor, 63) / 365.0
    return inventory / daily_cor.replace(0, np.nan)


def _f36_inv_revenue_divergence(inventory, revenue, w):
    # Inventory growth minus revenue growth over window
    inv_g = inventory.pct_change(w)
    rev_g = revenue.pct_change(w)
    return inv_g - rev_g


def _f36_markdown_risk_signal(inventory, revenue, grossmargin, w):
    # High inventory growth + falling margins => markdown risk
    inv_g = inventory.pct_change(w)
    rev_g = revenue.pct_change(w)
    gm_chg = grossmargin.diff(w)
    return (inv_g - rev_g) - gm_chg


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxrev_5d_base_v076_signal(inventory, cor, revenue, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 5) * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxrev_10d_base_v077_signal(inventory, cor, revenue, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 10) * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxrev_21d_base_v078_signal(inventory, cor, revenue, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 21) * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxrev_42d_base_v079_signal(inventory, cor, revenue, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 42) * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxrev_63d_base_v080_signal(inventory, cor, revenue, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 63) * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxrev_126d_base_v081_signal(inventory, cor, revenue, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 126) * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxrev_189d_base_v082_signal(inventory, cor, revenue, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 189) * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxrev_252d_base_v083_signal(inventory, cor, revenue, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 252) * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxrev_378d_base_v084_signal(inventory, cor, revenue, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 378) * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxrev_504d_base_v085_signal(inventory, cor, revenue, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 504) * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysrnk_21d_base_v086_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = d.rolling(21, min_periods=max(1, 21//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysrnk_63d_base_v087_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = d.rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysrnk_126d_base_v088_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = d.rolling(126, min_periods=max(1, 126//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysrnk_252d_base_v089_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = d.rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysrnk_378d_base_v090_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = d.rolling(378, min_periods=max(1, 378//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysrnk_504d_base_v091_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = d.rolling(504, min_periods=max(1, 504//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysrnk_189d_base_v092_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = d.rolling(189, min_periods=max(1, 189//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivsq_10d_base_v093_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 10)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivsq_21d_base_v094_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 21)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivsq_42d_base_v095_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 42)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivsq_63d_base_v096_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 63)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivsq_126d_base_v097_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 126)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivsq_252d_base_v098_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 252)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivsq_378d_base_v099_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 378)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxrev_21d_base_v100_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxrev_42d_base_v101_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 42)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxrev_63d_base_v102_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 63)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxrev_126d_base_v103_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 126)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxrev_189d_base_v104_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 189)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxrev_252d_base_v105_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 252)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxrev_378d_base_v106_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 378)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxrev_504d_base_v107_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 504)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysdev_21d_base_v108_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = (d - _mean(d, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysdev_63d_base_v109_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = (d - _mean(d, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysdev_126d_base_v110_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = (d - _mean(d, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysdev_189d_base_v111_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = (d - _mean(d, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysdev_252d_base_v112_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = (d - _mean(d, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysdev_378d_base_v113_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = (d - _mean(d, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysdev_504d_base_v114_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = (d - _mean(d, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivxgmd_21d_base_v115_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 21)
    result = d * grossmargin.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivxgmd_42d_base_v116_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 42)
    result = d * grossmargin.diff(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivxgmd_63d_base_v117_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 63)
    result = d * grossmargin.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivxgmd_126d_base_v118_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 126)
    result = d * grossmargin.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivxgmd_189d_base_v119_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 189)
    result = d * grossmargin.diff(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivxgmd_252d_base_v120_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 252)
    result = d * grossmargin.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivxgmd_378d_base_v121_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 378)
    result = d * grossmargin.diff(378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskema_10d_base_v122_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21)
    result = _ema(d, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskema_21d_base_v123_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21)
    result = _ema(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskema_42d_base_v124_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21)
    result = _ema(d, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskema_63d_base_v125_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21)
    result = _ema(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskema_126d_base_v126_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21)
    result = _ema(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskema_252d_base_v127_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21)
    result = _ema(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskema_378d_base_v128_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21)
    result = _ema(d, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxcor_21d_base_v129_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 21) * cor.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxcor_63d_base_v130_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 63) * cor.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxcor_126d_base_v131_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 126) * cor.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxcor_189d_base_v132_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 189) * cor.pct_change(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxcor_252d_base_v133_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 252) * cor.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxcor_378d_base_v134_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 378) * cor.pct_change(378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxcor_504d_base_v135_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 504) * cor.pct_change(504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivmax_21d_base_v136_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 21)
    result = d.rolling(21, min_periods=max(1, 21//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivmax_63d_base_v137_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 21)
    result = d.rolling(63, min_periods=max(1, 63//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivmax_126d_base_v138_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 21)
    result = d.rolling(126, min_periods=max(1, 126//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivmax_189d_base_v139_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 21)
    result = d.rolling(189, min_periods=max(1, 189//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivmax_252d_base_v140_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 21)
    result = d.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivmax_378d_base_v141_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 21)
    result = d.rolling(378, min_periods=max(1, 378//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivmax_504d_base_v142_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 21)
    result = d.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskstd_63d_base_v143_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21)
    result = _std(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskstd_252d_base_v144_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21)
    result = _std(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgmchg_63d_base_v145_signal(inventory, cor, grossmargin, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = d * grossmargin.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgmchg_252d_base_v146_signal(inventory, cor, grossmargin, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = d * grossmargin.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivmean_189d_base_v147_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 21)
    result = _mean(d, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivmean_378d_base_v148_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 21)
    result = _mean(d, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxcor_126d_base_v149_signal(inventory, revenue, grossmargin, cor, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 63)
    result = d * cor.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxcor_252d_base_v150_signal(inventory, revenue, grossmargin, cor, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 63)
    result = d * cor.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxrev_5d_base_v076_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxrev_10d_base_v077_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxrev_21d_base_v078_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxrev_42d_base_v079_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxrev_63d_base_v080_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxrev_126d_base_v081_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxrev_189d_base_v082_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxrev_252d_base_v083_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxrev_378d_base_v084_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxrev_504d_base_v085_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysrnk_21d_base_v086_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysrnk_63d_base_v087_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysrnk_126d_base_v088_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysrnk_252d_base_v089_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysrnk_378d_base_v090_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysrnk_504d_base_v091_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysrnk_189d_base_v092_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivsq_10d_base_v093_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivsq_21d_base_v094_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivsq_42d_base_v095_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivsq_63d_base_v096_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivsq_126d_base_v097_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivsq_252d_base_v098_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivsq_378d_base_v099_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxrev_21d_base_v100_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxrev_42d_base_v101_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxrev_63d_base_v102_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxrev_126d_base_v103_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxrev_189d_base_v104_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxrev_252d_base_v105_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxrev_378d_base_v106_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxrev_504d_base_v107_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysdev_21d_base_v108_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysdev_63d_base_v109_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysdev_126d_base_v110_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysdev_189d_base_v111_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysdev_252d_base_v112_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysdev_378d_base_v113_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysdev_504d_base_v114_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivxgmd_21d_base_v115_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivxgmd_42d_base_v116_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivxgmd_63d_base_v117_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivxgmd_126d_base_v118_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivxgmd_189d_base_v119_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivxgmd_252d_base_v120_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivxgmd_378d_base_v121_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskema_10d_base_v122_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskema_21d_base_v123_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskema_42d_base_v124_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskema_63d_base_v125_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskema_126d_base_v126_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskema_252d_base_v127_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskema_378d_base_v128_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxcor_21d_base_v129_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxcor_63d_base_v130_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxcor_126d_base_v131_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxcor_189d_base_v132_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxcor_252d_base_v133_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxcor_378d_base_v134_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxcor_504d_base_v135_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivmax_21d_base_v136_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivmax_63d_base_v137_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivmax_126d_base_v138_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivmax_189d_base_v139_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivmax_252d_base_v140_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivmax_378d_base_v141_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivmax_504d_base_v142_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskstd_63d_base_v143_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskstd_252d_base_v144_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgmchg_63d_base_v145_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgmchg_252d_base_v146_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivmean_189d_base_v147_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivmean_378d_base_v148_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxcor_126d_base_v149_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxcor_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F36_APPAREL_INVENTORY_MARKDOWN_RISK_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj, "volume": volume,
        "revenue": revenue, "cor": cor, "inventory": inventory,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }


    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f36_inv_days", "_f36_inv_revenue_divergence", "_f36_markdown_risk_signal",)
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
    print(f"OK f36_apparel_inventory_markdown_risk_076_150_claude: {n_features} features pass")
