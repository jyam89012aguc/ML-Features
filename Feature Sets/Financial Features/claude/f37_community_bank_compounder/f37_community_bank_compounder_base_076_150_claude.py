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
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()

# ===== folder domain primitives =====
def _f37_size_score(marketcap, assets):
    # Smaller-bank emphasis: invert relative size, scale by marketcap to ensure variation.
    rel = _safe_div(assets, marketcap)
    return rel * marketcap / (rel + 1.0)


def _f37_steady_growth(revenue, w):
    g = revenue.pct_change(periods=w)
    sd = g.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return _safe_div(g, sd) * revenue


def _f37_community_score(marketcap, revenue, bvps, w):
    g = revenue.pct_change(periods=w)
    sd = g.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return (g / sd) * bvps * marketcap / (marketcap + 1.0)

def f37cbc_f37_community_bank_compounder_sizexag_21d_base_v076_signal(marketcap, assets, closeadj):
    base = _f37_size_score(marketcap, assets)
    ag = assets.pct_change(periods=21)
    result = base * ag * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizexag_63d_base_v077_signal(marketcap, assets, closeadj):
    base = _f37_size_score(marketcap, assets)
    ag = assets.pct_change(periods=63)
    result = base * ag * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizexag_126d_base_v078_signal(marketcap, assets, closeadj):
    base = _f37_size_score(marketcap, assets)
    ag = assets.pct_change(periods=126)
    result = base * ag * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizexag_252d_base_v079_signal(marketcap, assets, closeadj):
    base = _f37_size_score(marketcap, assets)
    ag = assets.pct_change(periods=252)
    result = base * ag * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyanom_21d_base_v080_signal(revenue, closeadj):
    base = _f37_steady_growth(revenue, 21)
    result = (base - _mean(base, 42)) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyanom_63d_base_v081_signal(revenue, closeadj):
    base = _f37_steady_growth(revenue, 63)
    result = (base - _mean(base, 126)) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyanom_126d_base_v082_signal(revenue, closeadj):
    base = _f37_steady_growth(revenue, 126)
    result = (base - _mean(base, 252)) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyanom_252d_base_v083_signal(revenue, closeadj):
    base = _f37_steady_growth(revenue, 252)
    result = (base - _mean(base, 504)) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commanom_21d_base_v084_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 21)
    result = (base - _mean(base, 42)) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commanom_63d_base_v085_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 63)
    result = (base - _mean(base, 126)) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commanom_126d_base_v086_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 126)
    result = (base - _mean(base, 252)) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commanom_252d_base_v087_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 252)
    result = (base - _mean(base, 504)) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizexrg_21d_base_v088_signal(marketcap, assets, revenue, closeadj):
    base = _f37_size_score(marketcap, assets)
    rg = revenue.pct_change(periods=21)
    result = base * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizexrg_63d_base_v089_signal(marketcap, assets, revenue, closeadj):
    base = _f37_size_score(marketcap, assets)
    rg = revenue.pct_change(periods=63)
    result = base * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizexrg_126d_base_v090_signal(marketcap, assets, revenue, closeadj):
    base = _f37_size_score(marketcap, assets)
    rg = revenue.pct_change(periods=126)
    result = base * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizexrg_252d_base_v091_signal(marketcap, assets, revenue, closeadj):
    base = _f37_size_score(marketcap, assets)
    rg = revenue.pct_change(periods=252)
    result = base * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyemb_21d_base_v092_signal(revenue, closeadj):
    base = _f37_steady_growth(revenue, 21)
    result = _ema(base, 21) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyemb_63d_base_v093_signal(revenue, closeadj):
    base = _f37_steady_growth(revenue, 63)
    result = _ema(base, 63) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyemb_126d_base_v094_signal(revenue, closeadj):
    base = _f37_steady_growth(revenue, 126)
    result = _ema(base, 126) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyemb_252d_base_v095_signal(revenue, closeadj):
    base = _f37_steady_growth(revenue, 252)
    result = _ema(base, 252) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commemb_21d_base_v096_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 21)
    result = _ema(base, 21) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commemb_63d_base_v097_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 63)
    result = _ema(base, 63) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commemb_126d_base_v098_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 126)
    result = _ema(base, 126) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commemb_252d_base_v099_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 252)
    result = _ema(base, 252) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizesteady_21d_base_v100_signal(marketcap, assets, revenue, closeadj):
    a = _f37_size_score(marketcap, assets)
    b = _f37_steady_growth(revenue, 21)
    result = a * b / 1e9 * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizesteady_63d_base_v101_signal(marketcap, assets, revenue, closeadj):
    a = _f37_size_score(marketcap, assets)
    b = _f37_steady_growth(revenue, 63)
    result = a * b / 1e9 * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizesteady_126d_base_v102_signal(marketcap, assets, revenue, closeadj):
    a = _f37_size_score(marketcap, assets)
    b = _f37_steady_growth(revenue, 126)
    result = a * b / 1e9 * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizesteady_252d_base_v103_signal(marketcap, assets, revenue, closeadj):
    a = _f37_size_score(marketcap, assets)
    b = _f37_steady_growth(revenue, 252)
    result = a * b / 1e9 * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizecomm_21d_base_v104_signal(marketcap, assets, revenue, bvps, closeadj):
    a = _f37_size_score(marketcap, assets)
    b = _f37_community_score(marketcap, revenue, bvps, 21)
    result = a * b / 1e10 * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizecomm_63d_base_v105_signal(marketcap, assets, revenue, bvps, closeadj):
    a = _f37_size_score(marketcap, assets)
    b = _f37_community_score(marketcap, revenue, bvps, 63)
    result = a * b / 1e10 * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizecomm_126d_base_v106_signal(marketcap, assets, revenue, bvps, closeadj):
    a = _f37_size_score(marketcap, assets)
    b = _f37_community_score(marketcap, revenue, bvps, 126)
    result = a * b / 1e10 * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizecomm_252d_base_v107_signal(marketcap, assets, revenue, bvps, closeadj):
    a = _f37_size_score(marketcap, assets)
    b = _f37_community_score(marketcap, revenue, bvps, 252)
    result = a * b / 1e10 * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commsqrt_21d_base_v108_signal(marketcap, revenue, bvps):
    base = _f37_community_score(marketcap, revenue, bvps, 21)
    result = base * np.sqrt(21) / np.sqrt(252.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commsqrt_63d_base_v109_signal(marketcap, revenue, bvps):
    base = _f37_community_score(marketcap, revenue, bvps, 63)
    result = base * np.sqrt(63) / np.sqrt(252.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commsqrt_126d_base_v110_signal(marketcap, revenue, bvps):
    base = _f37_community_score(marketcap, revenue, bvps, 126)
    result = base * np.sqrt(126) / np.sqrt(252.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commsqrt_252d_base_v111_signal(marketcap, revenue, bvps):
    base = _f37_community_score(marketcap, revenue, bvps, 252)
    result = base * np.sqrt(252) / np.sqrt(252.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadysqrt_21d_base_v112_signal(revenue):
    base = _f37_steady_growth(revenue, 21)
    result = base * np.sqrt(21) / np.sqrt(252.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadysqrt_63d_base_v113_signal(revenue):
    base = _f37_steady_growth(revenue, 63)
    result = base * np.sqrt(63) / np.sqrt(252.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadysqrt_126d_base_v114_signal(revenue):
    base = _f37_steady_growth(revenue, 126)
    result = base * np.sqrt(126) / np.sqrt(252.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadysqrt_252d_base_v115_signal(revenue):
    base = _f37_steady_growth(revenue, 252)
    result = base * np.sqrt(252) / np.sqrt(252.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizelog_k1_base_v116_signal(marketcap, assets, closeadj):
    base = _f37_size_score(marketcap, assets)
    result = np.log(base.abs() + 1.0) * closeadj * (1)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizelog_k2_base_v117_signal(marketcap, assets, closeadj):
    base = _f37_size_score(marketcap, assets)
    result = np.log(base.abs() + 1.0) * closeadj * (2)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizelog_k5_base_v118_signal(marketcap, assets, closeadj):
    base = _f37_size_score(marketcap, assets)
    result = np.log(base.abs() + 1.0) * closeadj * (5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sizelog_k10_base_v119_signal(marketcap, assets, closeadj):
    base = _f37_size_score(marketcap, assets)
    result = np.log(base.abs() + 1.0) * closeadj * (10)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commlog_21d_base_v120_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 21)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commlog_63d_base_v121_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 63)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commlog_126d_base_v122_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 126)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commlog_252d_base_v123_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 252)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadylog_21d_base_v124_signal(revenue, closeadj):
    base = _f37_steady_growth(revenue, 21)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadylog_63d_base_v125_signal(revenue, closeadj):
    base = _f37_steady_growth(revenue, 63)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadylog_126d_base_v126_signal(revenue, closeadj):
    base = _f37_steady_growth(revenue, 126)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadylog_252d_base_v127_signal(revenue, closeadj):
    base = _f37_steady_growth(revenue, 252)
    result = np.log(base.abs() + 1.0) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commdiff_21d_base_v128_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 21)
    result = (base - base.shift(21)) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commdiff_63d_base_v129_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 63)
    result = (base - base.shift(63)) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commdiff_126d_base_v130_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 126)
    result = (base - base.shift(126)) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commdiff_252d_base_v131_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 252)
    result = (base - base.shift(252)) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadydiff_21d_base_v132_signal(revenue, closeadj):
    base = _f37_steady_growth(revenue, 21)
    result = (base - base.shift(21)) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadydiff_63d_base_v133_signal(revenue, closeadj):
    base = _f37_steady_growth(revenue, 63)
    result = (base - base.shift(63)) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadydiff_126d_base_v134_signal(revenue, closeadj):
    base = _f37_steady_growth(revenue, 126)
    result = (base - base.shift(126)) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commxbvg_21d_base_v135_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 21)
    bg = bvps.pct_change(periods=21)
    result = base * (1.0 + bg) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commxbvg_63d_base_v136_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 63)
    bg = bvps.pct_change(periods=63)
    result = base * (1.0 + bg) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commxbvg_126d_base_v137_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 126)
    bg = bvps.pct_change(periods=126)
    result = base * (1.0 + bg) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commxbvg_252d_base_v138_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 252)
    bg = bvps.pct_change(periods=252)
    result = base * (1.0 + bg) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyxbvg_21d_base_v139_signal(revenue, bvps, closeadj):
    base = _f37_steady_growth(revenue, 21)
    bg = bvps.pct_change(periods=21)
    result = base * (1.0 + bg) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyxbvg_63d_base_v140_signal(revenue, bvps, closeadj):
    base = _f37_steady_growth(revenue, 63)
    bg = bvps.pct_change(periods=63)
    result = base * (1.0 + bg) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyxbvg_126d_base_v141_signal(revenue, bvps, closeadj):
    base = _f37_steady_growth(revenue, 126)
    bg = bvps.pct_change(periods=126)
    result = base * (1.0 + bg) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_steadyxbvg_252d_base_v142_signal(revenue, bvps, closeadj):
    base = _f37_steady_growth(revenue, 252)
    bg = bvps.pct_change(periods=252)
    result = base * (1.0 + bg) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commxrev2_21d_base_v143_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 21)
    result = base * (revenue / _mean(revenue, 42)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commxrev2_63d_base_v144_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 63)
    result = base * (revenue / _mean(revenue, 126)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commxrev2_126d_base_v145_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 126)
    result = base * (revenue / _mean(revenue, 252)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_commxrev2_252d_base_v146_signal(marketcap, revenue, bvps, closeadj):
    base = _f37_community_score(marketcap, revenue, bvps, 252)
    result = base * (revenue / _mean(revenue, 504)) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sxc_21d_base_v147_signal(marketcap, assets, revenue, bvps, closeadj):
    a = _f37_size_score(marketcap, assets)
    b = _f37_community_score(marketcap, revenue, bvps, 21)
    result = a * np.sign(b) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sxc_63d_base_v148_signal(marketcap, assets, revenue, bvps, closeadj):
    a = _f37_size_score(marketcap, assets)
    b = _f37_community_score(marketcap, revenue, bvps, 63)
    result = a * np.sign(b) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sxc_126d_base_v149_signal(marketcap, assets, revenue, bvps, closeadj):
    a = _f37_size_score(marketcap, assets)
    b = _f37_community_score(marketcap, revenue, bvps, 126)
    result = a * np.sign(b) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f37cbc_f37_community_bank_compounder_sxc_252d_base_v150_signal(marketcap, assets, revenue, bvps, closeadj):
    a = _f37_size_score(marketcap, assets)
    b = _f37_community_score(marketcap, revenue, bvps, 252)
    result = a * np.sign(b) * closeadj / _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f37cbc_f37_community_bank_compounder_sizexag_21d_base_v076_signal,
    f37cbc_f37_community_bank_compounder_sizexag_63d_base_v077_signal,
    f37cbc_f37_community_bank_compounder_sizexag_126d_base_v078_signal,
    f37cbc_f37_community_bank_compounder_sizexag_252d_base_v079_signal,
    f37cbc_f37_community_bank_compounder_steadyanom_21d_base_v080_signal,
    f37cbc_f37_community_bank_compounder_steadyanom_63d_base_v081_signal,
    f37cbc_f37_community_bank_compounder_steadyanom_126d_base_v082_signal,
    f37cbc_f37_community_bank_compounder_steadyanom_252d_base_v083_signal,
    f37cbc_f37_community_bank_compounder_commanom_21d_base_v084_signal,
    f37cbc_f37_community_bank_compounder_commanom_63d_base_v085_signal,
    f37cbc_f37_community_bank_compounder_commanom_126d_base_v086_signal,
    f37cbc_f37_community_bank_compounder_commanom_252d_base_v087_signal,
    f37cbc_f37_community_bank_compounder_sizexrg_21d_base_v088_signal,
    f37cbc_f37_community_bank_compounder_sizexrg_63d_base_v089_signal,
    f37cbc_f37_community_bank_compounder_sizexrg_126d_base_v090_signal,
    f37cbc_f37_community_bank_compounder_sizexrg_252d_base_v091_signal,
    f37cbc_f37_community_bank_compounder_steadyemb_21d_base_v092_signal,
    f37cbc_f37_community_bank_compounder_steadyemb_63d_base_v093_signal,
    f37cbc_f37_community_bank_compounder_steadyemb_126d_base_v094_signal,
    f37cbc_f37_community_bank_compounder_steadyemb_252d_base_v095_signal,
    f37cbc_f37_community_bank_compounder_commemb_21d_base_v096_signal,
    f37cbc_f37_community_bank_compounder_commemb_63d_base_v097_signal,
    f37cbc_f37_community_bank_compounder_commemb_126d_base_v098_signal,
    f37cbc_f37_community_bank_compounder_commemb_252d_base_v099_signal,
    f37cbc_f37_community_bank_compounder_sizesteady_21d_base_v100_signal,
    f37cbc_f37_community_bank_compounder_sizesteady_63d_base_v101_signal,
    f37cbc_f37_community_bank_compounder_sizesteady_126d_base_v102_signal,
    f37cbc_f37_community_bank_compounder_sizesteady_252d_base_v103_signal,
    f37cbc_f37_community_bank_compounder_sizecomm_21d_base_v104_signal,
    f37cbc_f37_community_bank_compounder_sizecomm_63d_base_v105_signal,
    f37cbc_f37_community_bank_compounder_sizecomm_126d_base_v106_signal,
    f37cbc_f37_community_bank_compounder_sizecomm_252d_base_v107_signal,
    f37cbc_f37_community_bank_compounder_commsqrt_21d_base_v108_signal,
    f37cbc_f37_community_bank_compounder_commsqrt_63d_base_v109_signal,
    f37cbc_f37_community_bank_compounder_commsqrt_126d_base_v110_signal,
    f37cbc_f37_community_bank_compounder_commsqrt_252d_base_v111_signal,
    f37cbc_f37_community_bank_compounder_steadysqrt_21d_base_v112_signal,
    f37cbc_f37_community_bank_compounder_steadysqrt_63d_base_v113_signal,
    f37cbc_f37_community_bank_compounder_steadysqrt_126d_base_v114_signal,
    f37cbc_f37_community_bank_compounder_steadysqrt_252d_base_v115_signal,
    f37cbc_f37_community_bank_compounder_sizelog_k1_base_v116_signal,
    f37cbc_f37_community_bank_compounder_sizelog_k2_base_v117_signal,
    f37cbc_f37_community_bank_compounder_sizelog_k5_base_v118_signal,
    f37cbc_f37_community_bank_compounder_sizelog_k10_base_v119_signal,
    f37cbc_f37_community_bank_compounder_commlog_21d_base_v120_signal,
    f37cbc_f37_community_bank_compounder_commlog_63d_base_v121_signal,
    f37cbc_f37_community_bank_compounder_commlog_126d_base_v122_signal,
    f37cbc_f37_community_bank_compounder_commlog_252d_base_v123_signal,
    f37cbc_f37_community_bank_compounder_steadylog_21d_base_v124_signal,
    f37cbc_f37_community_bank_compounder_steadylog_63d_base_v125_signal,
    f37cbc_f37_community_bank_compounder_steadylog_126d_base_v126_signal,
    f37cbc_f37_community_bank_compounder_steadylog_252d_base_v127_signal,
    f37cbc_f37_community_bank_compounder_commdiff_21d_base_v128_signal,
    f37cbc_f37_community_bank_compounder_commdiff_63d_base_v129_signal,
    f37cbc_f37_community_bank_compounder_commdiff_126d_base_v130_signal,
    f37cbc_f37_community_bank_compounder_commdiff_252d_base_v131_signal,
    f37cbc_f37_community_bank_compounder_steadydiff_21d_base_v132_signal,
    f37cbc_f37_community_bank_compounder_steadydiff_63d_base_v133_signal,
    f37cbc_f37_community_bank_compounder_steadydiff_126d_base_v134_signal,
    f37cbc_f37_community_bank_compounder_commxbvg_21d_base_v135_signal,
    f37cbc_f37_community_bank_compounder_commxbvg_63d_base_v136_signal,
    f37cbc_f37_community_bank_compounder_commxbvg_126d_base_v137_signal,
    f37cbc_f37_community_bank_compounder_commxbvg_252d_base_v138_signal,
    f37cbc_f37_community_bank_compounder_steadyxbvg_21d_base_v139_signal,
    f37cbc_f37_community_bank_compounder_steadyxbvg_63d_base_v140_signal,
    f37cbc_f37_community_bank_compounder_steadyxbvg_126d_base_v141_signal,
    f37cbc_f37_community_bank_compounder_steadyxbvg_252d_base_v142_signal,
    f37cbc_f37_community_bank_compounder_commxrev2_21d_base_v143_signal,
    f37cbc_f37_community_bank_compounder_commxrev2_63d_base_v144_signal,
    f37cbc_f37_community_bank_compounder_commxrev2_126d_base_v145_signal,
    f37cbc_f37_community_bank_compounder_commxrev2_252d_base_v146_signal,
    f37cbc_f37_community_bank_compounder_sxc_21d_base_v147_signal,
    f37cbc_f37_community_bank_compounder_sxc_63d_base_v148_signal,
    f37cbc_f37_community_bank_compounder_sxc_126d_base_v149_signal,
    f37cbc_f37_community_bank_compounder_sxc_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F37_COMMUNITY_BANK_COMPOUNDER_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f37_size_score", "_f37_steady_growth", "_f37_community_score")
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
    print(f"OK f37_community_bank_compounder_base_076_150_claude: {n_features} features pass")
