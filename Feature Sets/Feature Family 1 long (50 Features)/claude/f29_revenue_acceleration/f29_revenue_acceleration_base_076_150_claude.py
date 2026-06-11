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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f29_revenue_accel(revenue, w):
    g = _diff(_mean(revenue, w), w) / _mean(revenue.abs(), w).replace(0, np.nan)
    return _diff(g, w)


def _f29_revenue_growth(revenue, w):
    return _diff(_mean(revenue, w), w) / _mean(revenue.abs(), w).replace(0, np.nan)


def _f29_revenue_jerk(revenue, w):
    g = _diff(_mean(revenue, w), w) / _mean(revenue.abs(), w).replace(0, np.nan)
    a = _diff(g, w)
    return _diff(a, w)


# 504d revenue acceleration × marketcap
def f29ra_f29_revenue_acceleration_accelxmcap_504d_base_v076_signal(revenue, marketcap, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    result = a * np.log(_mean(marketcap, 504).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel - growth dispersion
def f29ra_f29_revenue_acceleration_accelminusgrow_252d_base_v077_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g = _f29_revenue_growth(revenue, 252)
    result = (a - g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel - growth dispersion
def f29ra_f29_revenue_acceleration_accelminusgrow_504d_base_v078_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g = _f29_revenue_growth(revenue, 252)
    result = (a - g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue accel × revenue level
def f29ra_f29_revenue_acceleration_accelrevlvl_21d_base_v079_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    result = a * _mean(revenue, 21) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue accel × revenue level
def f29ra_f29_revenue_acceleration_accelrevlvl_63d_base_v080_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    result = a * _mean(revenue, 63) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel × revenue level
def f29ra_f29_revenue_acceleration_accelrevlvl_252d_base_v081_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    result = a * _mean(revenue, 252) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel × revenue level
def f29ra_f29_revenue_acceleration_accelrevlvl_504d_base_v082_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    result = a * _mean(revenue, 252) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel * revenue / netinc ratio
def f29ra_f29_revenue_acceleration_accelxratrev2ni_252d_base_v083_signal(revenue, netinc, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rat = _safe_div(_mean(revenue, 252), _mean(netinc, 252))
    result = a * rat * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel * revenue / netinc ratio
def f29ra_f29_revenue_acceleration_accelxratrev2ni_504d_base_v084_signal(revenue, netinc, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rat = _safe_div(_mean(revenue, 252), _mean(netinc, 504))
    result = a * rat * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel * (revenue/assets)
def f29ra_f29_revenue_acceleration_accelxat_252d_base_v085_signal(revenue, assets, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rat = _safe_div(_mean(revenue, 252), _mean(assets, 252))
    result = a * rat * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel * (revenue/assets)
def f29ra_f29_revenue_acceleration_accelxat_504d_base_v086_signal(revenue, assets, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rat = _safe_div(_mean(revenue, 252), _mean(assets, 504))
    result = a * rat * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel * (revenue/equity)
def f29ra_f29_revenue_acceleration_accelxeq_252d_base_v087_signal(revenue, equity, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rat = _safe_div(_mean(revenue, 252), _mean(equity, 252))
    result = a * rat * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel * (revenue/equity)
def f29ra_f29_revenue_acceleration_accelxeq_504d_base_v088_signal(revenue, equity, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rat = _safe_div(_mean(revenue, 252), _mean(equity, 504))
    result = a * rat * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite: 0.5 accel + 0.5 growth + 0.25 jerk
def f29ra_f29_revenue_acceleration_compaccel_252d_base_v089_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g = _f29_revenue_growth(revenue, 252)
    j = _f29_revenue_jerk(revenue, 252)
    result = (0.5 * a + 0.5 * g + 0.25 * j) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite: accel + growth + jerk
def f29ra_f29_revenue_acceleration_compaccel_504d_base_v090_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g = _f29_revenue_growth(revenue, 252)
    j = _f29_revenue_jerk(revenue, 126)
    result = (a + g + j) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue accel × volatility
def f29ra_f29_revenue_acceleration_accelxvol_21d_base_v091_signal(revenue, closeadj):
    sd = _std(closeadj.pct_change(), 21)
    result = _f29_revenue_accel(revenue, 21) * (1.0 + sd) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue accel × volatility
def f29ra_f29_revenue_acceleration_accelxvol_63d_base_v092_signal(revenue, closeadj):
    sd = _std(closeadj.pct_change(), 63)
    result = _f29_revenue_accel(revenue, 63) * (1.0 + sd) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel × volatility
def f29ra_f29_revenue_acceleration_accelxvol_252d_base_v093_signal(revenue, closeadj):
    sd = _std(closeadj.pct_change(), 252)
    result = _f29_revenue_accel(revenue, 252) * (1.0 + sd) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel × cumulative return
def f29ra_f29_revenue_acceleration_accelxretcum_252d_base_v094_signal(revenue, closeadj):
    cret = closeadj / closeadj.shift(252).replace(0, np.nan)
    result = _f29_revenue_accel(revenue, 252) * cret * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel × cumulative return
def f29ra_f29_revenue_acceleration_accelxretcum_504d_base_v095_signal(revenue, closeadj):
    cret = closeadj / closeadj.shift(504).replace(0, np.nan)
    result = _f29_revenue_accel(revenue, 252) * cret * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel × ebitda margin proxy
def f29ra_f29_revenue_acceleration_accelxebmargin_252d_base_v096_signal(revenue, ebitda, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    margin = _safe_div(_mean(ebitda, 252), _mean(revenue, 252))
    result = a * margin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel × ebitda margin proxy
def f29ra_f29_revenue_acceleration_accelxebmargin_504d_base_v097_signal(revenue, ebitda, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    margin = _safe_div(_mean(ebitda, 504), _mean(revenue, 252))
    result = a * margin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue accel × revenue/sharesbas
def f29ra_f29_revenue_acceleration_accelxrevpershare_21d_base_v098_signal(revenue, sharesbas, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    rps = _safe_div(_mean(revenue, 21), _mean(sharesbas, 21))
    result = a * rps * closeadj / 10.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel × revenue/sharesbas
def f29ra_f29_revenue_acceleration_accelxrevpershare_252d_base_v099_signal(revenue, sharesbas, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rps = _safe_div(_mean(revenue, 252), _mean(sharesbas, 252))
    result = a * rps * closeadj / 10.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel area / 252
def f29ra_f29_revenue_acceleration_accelarea_252d_base_v100_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    base = a.rolling(252, min_periods=63).sum() / 252.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel area / 504
def f29ra_f29_revenue_acceleration_accelarea_504d_base_v101_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    base = a.rolling(504, min_periods=126).sum() / 504.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel diff vs mean (anomaly)
def f29ra_f29_revenue_acceleration_accelvsmean_252d_base_v102_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    base = a - _mean(a, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel diff vs mean (anomaly)
def f29ra_f29_revenue_acceleration_accelvsmean_504d_base_v103_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    base = a - _mean(a, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel * netinc/revenue ratio
def f29ra_f29_revenue_acceleration_accelxnimargin_252d_base_v104_signal(revenue, netinc, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    margin = _safe_div(_mean(netinc, 252), _mean(revenue, 252))
    result = a * margin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel * netinc/revenue ratio
def f29ra_f29_revenue_acceleration_accelxnimargin_504d_base_v105_signal(revenue, netinc, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    margin = _safe_div(_mean(netinc, 504), _mean(revenue, 252))
    result = a * margin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo * revenue accel composite
def f29ra_f29_revenue_acceleration_accelxncfomargin_252d_base_v106_signal(revenue, ncfo, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    margin = _safe_div(_mean(ncfo, 252), _mean(revenue, 252))
    result = a * margin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncfo * revenue accel composite
def f29ra_f29_revenue_acceleration_accelxncfomargin_504d_base_v107_signal(revenue, ncfo, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    margin = _safe_div(_mean(ncfo, 504), _mean(revenue, 252))
    result = a * margin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel * (1 - debt/equity)
def f29ra_f29_revenue_acceleration_accelxleverage_252d_base_v108_signal(revenue, debt, equity, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    lev = _safe_div(_mean(debt, 252), _mean(equity, 252))
    result = a * (1.0 + lev) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel * leverage
def f29ra_f29_revenue_acceleration_accelxleverage_504d_base_v109_signal(revenue, debt, equity, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    lev = _safe_div(_mean(debt, 504), _mean(equity, 504))
    result = a * (1.0 + lev) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel × capex intensity
def f29ra_f29_revenue_acceleration_accelxcapint_252d_base_v110_signal(revenue, capex, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    intensity = _safe_div(_mean(capex, 252), _mean(revenue, 252))
    result = a * intensity * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel × capex intensity
def f29ra_f29_revenue_acceleration_accelxcapint_504d_base_v111_signal(revenue, capex, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    intensity = _safe_div(_mean(capex, 504), _mean(revenue, 252))
    result = a * intensity * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue accel sum × closeadj
def f29ra_f29_revenue_acceleration_accelsum_21d_base_v112_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    base = a.rolling(63, min_periods=21).sum()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue accel sum × closeadj
def f29ra_f29_revenue_acceleration_accelsum_63d_base_v113_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    base = a.rolling(126, min_periods=42).sum()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel sign sum × revenue level
def f29ra_f29_revenue_acceleration_accelsumxrev_252d_base_v114_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    sign = np.sign(a).fillna(0)
    base = sign.rolling(252, min_periods=63).sum()
    result = base * _mean(revenue, 252) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel sign sum × revenue level
def f29ra_f29_revenue_acceleration_accelsumxrev_504d_base_v115_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    sign = np.sign(a).fillna(0)
    base = sign.rolling(504, min_periods=126).sum()
    result = base * _mean(revenue, 252) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel × volume of growth std (variability proxy)
def f29ra_f29_revenue_acceleration_accelxgrowstd_252d_base_v116_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g_std = _std(_f29_revenue_growth(revenue, 21), 252)
    result = a * (1.0 + g_std) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel × growth std
def f29ra_f29_revenue_acceleration_accelxgrowstd_504d_base_v117_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g_std = _std(_f29_revenue_growth(revenue, 63), 504)
    result = a * (1.0 + g_std) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue accel × ncfo level
def f29ra_f29_revenue_acceleration_accelxncfolvl_21d_base_v118_signal(revenue, ncfo, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    result = a * _mean(ncfo, 21) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue accel × ncfo level
def f29ra_f29_revenue_acceleration_accelxncfolvl_63d_base_v119_signal(revenue, ncfo, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    result = a * _mean(ncfo, 63) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue accel × ebitda level
def f29ra_f29_revenue_acceleration_accelxebitdalvl_21d_base_v120_signal(revenue, ebitda, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    result = a * _mean(ebitda, 21) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue accel × ebitda level
def f29ra_f29_revenue_acceleration_accelxebitdalvl_63d_base_v121_signal(revenue, ebitda, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    result = a * _mean(ebitda, 63) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel × log(assets)
def f29ra_f29_revenue_acceleration_accelxlogassets_252d_base_v122_signal(revenue, assets, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    result = a * np.log(_mean(assets, 252).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel × log(assets)
def f29ra_f29_revenue_acceleration_accelxlogassets_504d_base_v123_signal(revenue, assets, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    result = a * np.log(_mean(assets, 504).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel × log(equity)
def f29ra_f29_revenue_acceleration_accelxlogeq_252d_base_v124_signal(revenue, equity, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    result = a * np.log(_mean(equity, 252).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel × log(equity)
def f29ra_f29_revenue_acceleration_accelxlogeq_504d_base_v125_signal(revenue, equity, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    result = a * np.log(_mean(equity, 504).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel × ratio of revenue to debt
def f29ra_f29_revenue_acceleration_accelxrev2debt_252d_base_v126_signal(revenue, debt, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rat = _safe_div(_mean(revenue, 252), _mean(debt, 252))
    result = a * rat * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel × ratio of revenue to debt
def f29ra_f29_revenue_acceleration_accelxrev2debt_504d_base_v127_signal(revenue, debt, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rat = _safe_div(_mean(revenue, 252), _mean(debt, 504))
    result = a * rat * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative revenue accel sign × revenue level
def f29ra_f29_revenue_acceleration_accelcumsign_252d_base_v128_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    sign = np.sign(a).fillna(0)
    base = sign.rolling(252, min_periods=63).sum()
    result = base * _mean(revenue, 252) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative revenue accel sign × revenue level
def f29ra_f29_revenue_acceleration_accelcumsign_504d_base_v129_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    sign = np.sign(a).fillna(0)
    base = sign.rolling(504, min_periods=126).sum()
    result = base * _mean(revenue, 252) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue accel volatility-of-vol
def f29ra_f29_revenue_acceleration_accelvolvol_21d_base_v130_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    base = _std(_std(a, 21), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue accel volatility-of-vol
def f29ra_f29_revenue_acceleration_accelvolvol_63d_base_v131_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    base = _std(_std(a, 63), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel × ratio (revenue/capex)
def f29ra_f29_revenue_acceleration_accelxrev2cap_252d_base_v132_signal(revenue, capex, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rat = _safe_div(_mean(revenue, 252), _mean(capex, 252))
    result = a * rat * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel × ratio (revenue/capex)
def f29ra_f29_revenue_acceleration_accelxrev2cap_504d_base_v133_signal(revenue, capex, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rat = _safe_div(_mean(revenue, 252), _mean(capex, 504))
    result = a * rat * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel exponential weighting
def f29ra_f29_revenue_acceleration_accelexp_252d_base_v134_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = np.sign(a) * np.log1p(a.abs())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel exponential weighting
def f29ra_f29_revenue_acceleration_accelexp_504d_base_v135_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    base = np.sign(a) * np.log1p(a.abs())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel × inverse netinc volatility
def f29ra_f29_revenue_acceleration_accelxnistab_252d_base_v136_signal(revenue, netinc, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    nistab = _safe_div(_mean(netinc.abs(), 252), _std(netinc, 252))
    result = a * nistab * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel × inverse netinc volatility
def f29ra_f29_revenue_acceleration_accelxnistab_504d_base_v137_signal(revenue, netinc, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    nistab = _safe_div(_mean(netinc.abs(), 504), _std(netinc, 504))
    result = a * nistab * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue accel × volume momentum (using capex as proxy for activity)
def f29ra_f29_revenue_acceleration_accelxactivity_21d_base_v138_signal(revenue, capex, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    activity = _diff(_mean(capex, 21), 21) / _mean(capex.abs(), 21).replace(0, np.nan)
    result = a * (1.0 + activity) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue accel × activity
def f29ra_f29_revenue_acceleration_accelxactivity_63d_base_v139_signal(revenue, capex, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    activity = _diff(_mean(capex, 63), 63) / _mean(capex.abs(), 63).replace(0, np.nan)
    result = a * (1.0 + activity) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel × asset turnover
def f29ra_f29_revenue_acceleration_accelxat_alt_252d_base_v140_signal(revenue, assets, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    at = _safe_div(_mean(revenue, 252), _mean(assets, 252))
    result = a * at * 100.0 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel × asset turnover
def f29ra_f29_revenue_acceleration_accelxat_alt_504d_base_v141_signal(revenue, assets, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    at = _safe_div(_mean(revenue, 252), _mean(assets, 504))
    result = a * at * 100.0 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel * capex level
def f29ra_f29_revenue_acceleration_accelxcaplvl_252d_base_v142_signal(revenue, capex, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    result = a * _mean(capex, 252) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel * capex level
def f29ra_f29_revenue_acceleration_accelxcaplvl_504d_base_v143_signal(revenue, capex, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    result = a * _mean(capex, 504) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel × revenue growth squared
def f29ra_f29_revenue_acceleration_accelxgrowsq_252d_base_v144_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g = _f29_revenue_growth(revenue, 252)
    result = a * g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel × revenue growth squared
def f29ra_f29_revenue_acceleration_accelxgrowsq_504d_base_v145_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g = _f29_revenue_growth(revenue, 252)
    result = a * g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue accel × short-term EMA of accel
def f29ra_f29_revenue_acceleration_accelxema_21d_base_v146_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    ema = a.ewm(span=10, adjust=False, min_periods=5).mean()
    result = a * ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue accel × ema accel
def f29ra_f29_revenue_acceleration_accelxema_63d_base_v147_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    ema = a.ewm(span=21, adjust=False, min_periods=10).mean()
    result = a * ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel × ema accel
def f29ra_f29_revenue_acceleration_accelxema_252d_base_v148_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    ema = a.ewm(span=63, adjust=False, min_periods=21).mean()
    result = a * ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel × ratio assets/equity (financial leverage proxy)
def f29ra_f29_revenue_acceleration_accelxalev_252d_base_v149_signal(revenue, assets, equity, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    alev = _safe_div(_mean(assets, 252), _mean(equity, 252))
    result = a * alev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel × ratio assets/equity
def f29ra_f29_revenue_acceleration_accelxalev_504d_base_v150_signal(revenue, assets, equity, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    alev = _safe_div(_mean(assets, 504), _mean(equity, 504))
    result = a * alev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f29ra_f29_revenue_acceleration_accelxmcap_504d_base_v076_signal,
    f29ra_f29_revenue_acceleration_accelminusgrow_252d_base_v077_signal,
    f29ra_f29_revenue_acceleration_accelminusgrow_504d_base_v078_signal,
    f29ra_f29_revenue_acceleration_accelrevlvl_21d_base_v079_signal,
    f29ra_f29_revenue_acceleration_accelrevlvl_63d_base_v080_signal,
    f29ra_f29_revenue_acceleration_accelrevlvl_252d_base_v081_signal,
    f29ra_f29_revenue_acceleration_accelrevlvl_504d_base_v082_signal,
    f29ra_f29_revenue_acceleration_accelxratrev2ni_252d_base_v083_signal,
    f29ra_f29_revenue_acceleration_accelxratrev2ni_504d_base_v084_signal,
    f29ra_f29_revenue_acceleration_accelxat_252d_base_v085_signal,
    f29ra_f29_revenue_acceleration_accelxat_504d_base_v086_signal,
    f29ra_f29_revenue_acceleration_accelxeq_252d_base_v087_signal,
    f29ra_f29_revenue_acceleration_accelxeq_504d_base_v088_signal,
    f29ra_f29_revenue_acceleration_compaccel_252d_base_v089_signal,
    f29ra_f29_revenue_acceleration_compaccel_504d_base_v090_signal,
    f29ra_f29_revenue_acceleration_accelxvol_21d_base_v091_signal,
    f29ra_f29_revenue_acceleration_accelxvol_63d_base_v092_signal,
    f29ra_f29_revenue_acceleration_accelxvol_252d_base_v093_signal,
    f29ra_f29_revenue_acceleration_accelxretcum_252d_base_v094_signal,
    f29ra_f29_revenue_acceleration_accelxretcum_504d_base_v095_signal,
    f29ra_f29_revenue_acceleration_accelxebmargin_252d_base_v096_signal,
    f29ra_f29_revenue_acceleration_accelxebmargin_504d_base_v097_signal,
    f29ra_f29_revenue_acceleration_accelxrevpershare_21d_base_v098_signal,
    f29ra_f29_revenue_acceleration_accelxrevpershare_252d_base_v099_signal,
    f29ra_f29_revenue_acceleration_accelarea_252d_base_v100_signal,
    f29ra_f29_revenue_acceleration_accelarea_504d_base_v101_signal,
    f29ra_f29_revenue_acceleration_accelvsmean_252d_base_v102_signal,
    f29ra_f29_revenue_acceleration_accelvsmean_504d_base_v103_signal,
    f29ra_f29_revenue_acceleration_accelxnimargin_252d_base_v104_signal,
    f29ra_f29_revenue_acceleration_accelxnimargin_504d_base_v105_signal,
    f29ra_f29_revenue_acceleration_accelxncfomargin_252d_base_v106_signal,
    f29ra_f29_revenue_acceleration_accelxncfomargin_504d_base_v107_signal,
    f29ra_f29_revenue_acceleration_accelxleverage_252d_base_v108_signal,
    f29ra_f29_revenue_acceleration_accelxleverage_504d_base_v109_signal,
    f29ra_f29_revenue_acceleration_accelxcapint_252d_base_v110_signal,
    f29ra_f29_revenue_acceleration_accelxcapint_504d_base_v111_signal,
    f29ra_f29_revenue_acceleration_accelsum_21d_base_v112_signal,
    f29ra_f29_revenue_acceleration_accelsum_63d_base_v113_signal,
    f29ra_f29_revenue_acceleration_accelsumxrev_252d_base_v114_signal,
    f29ra_f29_revenue_acceleration_accelsumxrev_504d_base_v115_signal,
    f29ra_f29_revenue_acceleration_accelxgrowstd_252d_base_v116_signal,
    f29ra_f29_revenue_acceleration_accelxgrowstd_504d_base_v117_signal,
    f29ra_f29_revenue_acceleration_accelxncfolvl_21d_base_v118_signal,
    f29ra_f29_revenue_acceleration_accelxncfolvl_63d_base_v119_signal,
    f29ra_f29_revenue_acceleration_accelxebitdalvl_21d_base_v120_signal,
    f29ra_f29_revenue_acceleration_accelxebitdalvl_63d_base_v121_signal,
    f29ra_f29_revenue_acceleration_accelxlogassets_252d_base_v122_signal,
    f29ra_f29_revenue_acceleration_accelxlogassets_504d_base_v123_signal,
    f29ra_f29_revenue_acceleration_accelxlogeq_252d_base_v124_signal,
    f29ra_f29_revenue_acceleration_accelxlogeq_504d_base_v125_signal,
    f29ra_f29_revenue_acceleration_accelxrev2debt_252d_base_v126_signal,
    f29ra_f29_revenue_acceleration_accelxrev2debt_504d_base_v127_signal,
    f29ra_f29_revenue_acceleration_accelcumsign_252d_base_v128_signal,
    f29ra_f29_revenue_acceleration_accelcumsign_504d_base_v129_signal,
    f29ra_f29_revenue_acceleration_accelvolvol_21d_base_v130_signal,
    f29ra_f29_revenue_acceleration_accelvolvol_63d_base_v131_signal,
    f29ra_f29_revenue_acceleration_accelxrev2cap_252d_base_v132_signal,
    f29ra_f29_revenue_acceleration_accelxrev2cap_504d_base_v133_signal,
    f29ra_f29_revenue_acceleration_accelexp_252d_base_v134_signal,
    f29ra_f29_revenue_acceleration_accelexp_504d_base_v135_signal,
    f29ra_f29_revenue_acceleration_accelxnistab_252d_base_v136_signal,
    f29ra_f29_revenue_acceleration_accelxnistab_504d_base_v137_signal,
    f29ra_f29_revenue_acceleration_accelxactivity_21d_base_v138_signal,
    f29ra_f29_revenue_acceleration_accelxactivity_63d_base_v139_signal,
    f29ra_f29_revenue_acceleration_accelxat_alt_252d_base_v140_signal,
    f29ra_f29_revenue_acceleration_accelxat_alt_504d_base_v141_signal,
    f29ra_f29_revenue_acceleration_accelxcaplvl_252d_base_v142_signal,
    f29ra_f29_revenue_acceleration_accelxcaplvl_504d_base_v143_signal,
    f29ra_f29_revenue_acceleration_accelxgrowsq_252d_base_v144_signal,
    f29ra_f29_revenue_acceleration_accelxgrowsq_504d_base_v145_signal,
    f29ra_f29_revenue_acceleration_accelxema_21d_base_v146_signal,
    f29ra_f29_revenue_acceleration_accelxema_63d_base_v147_signal,
    f29ra_f29_revenue_acceleration_accelxema_252d_base_v148_signal,
    f29ra_f29_revenue_acceleration_accelxalev_252d_base_v149_signal,
    f29ra_f29_revenue_acceleration_accelxalev_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_REVENUE_ACCELERATION_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 2500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    fcf = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcf")
    ncfo = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ncfo")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    capex = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="capex")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    gp = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="gp")
    marketcap = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.015, n))), name="marketcap")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "equity": equity, "debt": debt, "assets": assets,
        "ebitda": ebitda, "capex": capex, "sharesbas": sharesbas, "opinc": opinc,
        "gp": gp, "marketcap": marketcap,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f29_revenue_accel", "_f29_revenue_growth", "_f29_revenue_jerk")
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
    print(f"OK f29_revenue_acceleration_base_076_150_claude: {n_features} features pass")
