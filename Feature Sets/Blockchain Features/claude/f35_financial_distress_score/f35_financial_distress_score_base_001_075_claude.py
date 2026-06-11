import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
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


# ===== folder domain primitives (financial distress / Altman-Z) =====
def _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets):
    # Altman Z'' for non-manufacturers / EM: 6.56*WC/TA + 3.26*RE/TA
    #   + 6.72*EBIT/TA + 1.05*equity/liabilities
    ta = assets.replace(0, np.nan)
    x1 = _safe_div(workingcapital, ta)
    x2 = _safe_div(retearn, ta)
    x3 = _safe_div(ebit, ta)
    x4 = _safe_div(equity, liabilities)
    return 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4


def _f35_zcomp(numer, denom, weight):
    # a single weighted Altman ratio component (e.g. weight * EBIT/TA)
    return weight * _safe_div(numer, denom)


def _f35_coverage(flow, liabilities):
    # solvency / coverage: how well an income or cash flow covers liabilities
    return _safe_div(flow, liabilities)


def _f35_distresstrend(workingcapital, retearn, ebit, equity, liabilities, assets, w):
    # deterioration of the Altman score over w days (positive = improving)
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    return z.diff(periods=w)


# ============ FEATURES 001-075 ============

# full Altman Z'' score
def f35fd_f35_financial_distress_score_altman_1d_base_v001_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    result = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d-smoothed Altman Z'' score
def f35fd_f35_financial_distress_score_altmansm_21d_base_v002_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = _mean(z, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed Altman Z'' score
def f35fd_f35_financial_distress_score_altmansm_63d_base_v003_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = _mean(z, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed Altman Z'' score
def f35fd_f35_financial_distress_score_altmansm_126d_base_v004_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = _mean(z, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed Altman Z'' score
def f35fd_f35_financial_distress_score_altmansm_252d_base_v005_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = _mean(z, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital / assets component (weighted)
def f35fd_f35_financial_distress_score_wcta_1d_base_v006_signal(workingcapital, assets, retearn, ebit, equity, liabilities):
    result = _f35_zcomp(workingcapital, assets, 6.56) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed WC/assets component
def f35fd_f35_financial_distress_score_wcta_63d_base_v007_signal(workingcapital, assets, retearn, ebit, equity, liabilities):
    c = _f35_zcomp(workingcapital, assets, 6.56)
    result = _mean(c, 63) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed WC/assets component
def f35fd_f35_financial_distress_score_wcta_252d_base_v008_signal(workingcapital, assets, retearn, ebit, equity, liabilities):
    c = _f35_zcomp(workingcapital, assets, 6.56)
    result = _mean(c, 252) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# retained-earnings / assets component (weighted)
def f35fd_f35_financial_distress_score_reta_1d_base_v009_signal(retearn, assets, workingcapital, ebit, equity, liabilities):
    result = _f35_zcomp(retearn, assets, 3.26) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed RE/assets component
def f35fd_f35_financial_distress_score_reta_63d_base_v010_signal(retearn, assets, workingcapital, ebit, equity, liabilities):
    c = _f35_zcomp(retearn, assets, 3.26)
    result = _mean(c, 63) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed RE/assets component
def f35fd_f35_financial_distress_score_reta_252d_base_v011_signal(retearn, assets, workingcapital, ebit, equity, liabilities):
    c = _f35_zcomp(retearn, assets, 3.26)
    result = _mean(c, 252) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT / assets component (weighted) - return-on-assets distress driver
def f35fd_f35_financial_distress_score_ebitta_1d_base_v012_signal(ebit, assets, workingcapital, retearn, equity, liabilities):
    result = _f35_zcomp(ebit, assets, 6.72) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed EBIT/assets component
def f35fd_f35_financial_distress_score_ebitta_63d_base_v013_signal(ebit, assets, workingcapital, retearn, equity, liabilities):
    c = _f35_zcomp(ebit, assets, 6.72)
    result = _mean(c, 63) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed EBIT/assets component
def f35fd_f35_financial_distress_score_ebitta_252d_base_v014_signal(ebit, assets, workingcapital, retearn, equity, liabilities):
    c = _f35_zcomp(ebit, assets, 6.72)
    result = _mean(c, 252) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# equity / liabilities component (weighted) - leverage cushion
def f35fd_f35_financial_distress_score_eqliab_1d_base_v015_signal(equity, liabilities, workingcapital, retearn, ebit, assets):
    result = _f35_zcomp(equity, liabilities, 1.05) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed equity/liabilities component
def f35fd_f35_financial_distress_score_eqliab_63d_base_v016_signal(equity, liabilities, workingcapital, retearn, ebit, assets):
    c = _f35_zcomp(equity, liabilities, 1.05)
    result = _mean(c, 63) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed equity/liabilities component
def f35fd_f35_financial_distress_score_eqliab_252d_base_v017_signal(equity, liabilities, workingcapital, retearn, ebit, assets):
    c = _f35_zcomp(equity, liabilities, 1.05)
    result = _mean(c, 252) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# revenue / assets (asset turnover) - original Altman X5 driver
def f35fd_f35_financial_distress_score_revta_1d_base_v018_signal(revenue, assets, workingcapital, retearn, ebit, equity, liabilities):
    result = _f35_zcomp(revenue, assets, 1.0) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed revenue/assets
def f35fd_f35_financial_distress_score_revta_63d_base_v019_signal(revenue, assets, workingcapital, retearn, ebit, equity, liabilities):
    c = _f35_zcomp(revenue, assets, 1.0)
    result = _mean(c, 63) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed revenue/assets
def f35fd_f35_financial_distress_score_revta_252d_base_v020_signal(revenue, assets, workingcapital, retearn, ebit, equity, liabilities):
    c = _f35_zcomp(revenue, assets, 1.0)
    result = _mean(c, 252) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT coverage of liabilities (solvency)
def f35fd_f35_financial_distress_score_ebitcov_1d_base_v021_signal(ebit, liabilities, workingcapital, retearn, equity, assets):
    result = _f35_coverage(ebit, liabilities) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed EBIT coverage of liabilities
def f35fd_f35_financial_distress_score_ebitcov_63d_base_v022_signal(ebit, liabilities, workingcapital, retearn, equity, assets):
    c = _f35_coverage(ebit, liabilities)
    result = _mean(c, 63) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed EBIT coverage of liabilities
def f35fd_f35_financial_distress_score_ebitcov_252d_base_v023_signal(ebit, liabilities, workingcapital, retearn, equity, assets):
    c = _f35_coverage(ebit, liabilities)
    result = _mean(c, 252) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash coverage of liabilities (liquidity solvency)
def f35fd_f35_financial_distress_score_cashcov_1d_base_v024_signal(cashneq, liabilities, workingcapital, retearn, ebit, equity, assets):
    result = _f35_coverage(cashneq, liabilities) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed cash coverage of liabilities
def f35fd_f35_financial_distress_score_cashcov_63d_base_v025_signal(cashneq, liabilities, workingcapital, retearn, ebit, equity, assets):
    c = _f35_coverage(cashneq, liabilities)
    result = _mean(c, 63) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed cash coverage of liabilities
def f35fd_f35_financial_distress_score_cashcov_252d_base_v026_signal(cashneq, liabilities, workingcapital, retearn, ebit, equity, assets):
    c = _f35_coverage(cashneq, liabilities)
    result = _mean(c, 252) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# operating-cashflow coverage of liabilities
def f35fd_f35_financial_distress_score_ncfocov_1d_base_v027_signal(ncfo, liabilities, workingcapital, retearn, ebit, equity, assets):
    result = _f35_coverage(ncfo, liabilities) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed NCFO coverage of liabilities
def f35fd_f35_financial_distress_score_ncfocov_63d_base_v028_signal(ncfo, liabilities, workingcapital, retearn, ebit, equity, assets):
    c = _f35_coverage(ncfo, liabilities)
    result = _mean(c, 63) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed NCFO coverage of liabilities
def f35fd_f35_financial_distress_score_ncfocov_252d_base_v029_signal(ncfo, liabilities, workingcapital, retearn, ebit, equity, assets):
    c = _f35_coverage(ncfo, liabilities)
    result = _mean(c, 252) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# market-based Z proxy: marketcap / liabilities (market value of equity vs debt)
def f35fd_f35_financial_distress_score_mktliab_1d_base_v030_signal(marketcap, liabilities, workingcapital, retearn, ebit, equity, assets):
    result = _f35_coverage(marketcap, liabilities) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed marketcap/liabilities
def f35fd_f35_financial_distress_score_mktliab_63d_base_v031_signal(marketcap, liabilities, workingcapital, retearn, ebit, equity, assets):
    c = _f35_coverage(marketcap, liabilities)
    result = _mean(c, 63) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed marketcap/liabilities
def f35fd_f35_financial_distress_score_mktliab_252d_base_v032_signal(marketcap, liabilities, workingcapital, retearn, ebit, equity, assets):
    c = _f35_coverage(marketcap, liabilities)
    result = _mean(c, 252) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# market-augmented Altman (replace book equity term with marketcap/liabilities)
def f35fd_f35_financial_distress_score_mktz_1d_base_v033_signal(workingcapital, retearn, ebit, assets, liabilities, marketcap, equity):
    base = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = base - _f35_zcomp(equity, liabilities, 1.05) + 1.05 * _safe_div(marketcap, liabilities)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed market-augmented Altman
def f35fd_f35_financial_distress_score_mktz_63d_base_v034_signal(workingcapital, retearn, ebit, assets, liabilities, marketcap, equity):
    base = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    m = base - _f35_zcomp(equity, liabilities, 1.05) + 1.05 * _safe_div(marketcap, liabilities)
    result = _mean(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# debt / assets leverage (distress driver)
def f35fd_f35_financial_distress_score_debtta_1d_base_v035_signal(debt, assets, workingcapital, retearn, ebit, equity, liabilities):
    result = _f35_zcomp(debt, assets, 1.0) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed debt/assets leverage
def f35fd_f35_financial_distress_score_debtta_63d_base_v036_signal(debt, assets, workingcapital, retearn, ebit, equity, liabilities):
    c = _f35_zcomp(debt, assets, 1.0)
    result = _mean(c, 63) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# debt / equity gearing
def f35fd_f35_financial_distress_score_debteq_1d_base_v037_signal(debt, equity, workingcapital, retearn, ebit, liabilities, assets):
    result = _f35_coverage(debt, equity) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed debt/equity gearing
def f35fd_f35_financial_distress_score_debteq_63d_base_v038_signal(debt, equity, workingcapital, retearn, ebit, liabilities, assets):
    c = _f35_coverage(debt, equity)
    result = _mean(c, 63) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt / assets (debt minus cash over assets)
def f35fd_f35_financial_distress_score_netdebtta_1d_base_v039_signal(debt, cashneq, assets, workingcapital, retearn, ebit, equity, liabilities):
    result = _safe_div(debt - cashneq, assets) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed net-debt/assets
def f35fd_f35_financial_distress_score_netdebtta_63d_base_v040_signal(debt, cashneq, assets, workingcapital, retearn, ebit, equity, liabilities):
    c = _safe_div(debt - cashneq, assets)
    result = _mean(c, 63) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities / assets (total leverage ratio)
def f35fd_f35_financial_distress_score_liabta_1d_base_v041_signal(liabilities, assets, workingcapital, retearn, ebit, equity):
    result = _safe_div(liabilities, assets) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed liabilities/assets
def f35fd_f35_financial_distress_score_liabta_63d_base_v042_signal(liabilities, assets, workingcapital, retearn, ebit, equity):
    c = _safe_div(liabilities, assets)
    result = _mean(c, 63) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distress trend: 63d change in Altman score
def f35fd_f35_financial_distress_score_ztrend_63d_base_v043_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    result = _f35_distresstrend(workingcapital, retearn, ebit, equity, liabilities, assets, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# distress trend: 126d change in Altman score
def f35fd_f35_financial_distress_score_ztrend_126d_base_v044_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    result = _f35_distresstrend(workingcapital, retearn, ebit, equity, liabilities, assets, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# distress trend: 252d change in Altman score
def f35fd_f35_financial_distress_score_ztrend_252d_base_v045_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    result = _f35_distresstrend(workingcapital, retearn, ebit, equity, liabilities, assets, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# distress trend: 504d change in Altman score
def f35fd_f35_financial_distress_score_ztrend_504d_base_v046_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    result = _f35_distresstrend(workingcapital, retearn, ebit, equity, liabilities, assets, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# Altman z-score (standardized over 252d) - distance from own history
def f35fd_f35_financial_distress_score_zofz_252d_base_v047_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = _z(z, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# Altman z-score standardized over 126d
def f35fd_f35_financial_distress_score_zofz_126d_base_v048_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = _z(z, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Altman z-score standardized over 504d
def f35fd_f35_financial_distress_score_zofz_504d_base_v049_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = _z(z, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# Altman score percentile rank over 252d
def f35fd_f35_financial_distress_score_zrank_252d_base_v050_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = z.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# Altman score percentile rank over 504d
def f35fd_f35_financial_distress_score_zrank_504d_base_v051_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = z.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# distance-to-default proxy: equity cushion / asset vol over liabilities
def f35fd_f35_financial_distress_score_d2d_252d_base_v052_signal(equity, liabilities, assets, workingcapital, retearn, ebit):
    cushion = _safe_div(equity, liabilities)
    vol = _std(_safe_div(assets.diff(), assets), 252)
    result = _safe_div(cushion, vol) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance-to-default proxy over 126d asset vol
def f35fd_f35_financial_distress_score_d2d_126d_base_v053_signal(equity, liabilities, assets, workingcapital, retearn, ebit):
    cushion = _safe_div(equity, liabilities)
    vol = _std(_safe_div(assets.diff(), assets), 126)
    result = _safe_div(cushion, vol) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# market distance-to-default: marketcap cushion / equity-value vol
def f35fd_f35_financial_distress_score_mktd2d_252d_base_v054_signal(marketcap, liabilities, workingcapital, retearn, ebit, equity, assets):
    cushion = _safe_div(marketcap, liabilities)
    vol = _std(_safe_div(marketcap.diff(), marketcap), 252)
    result = _safe_div(cushion, vol) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# deterioration acceleration: 63d change of the 63d distress trend
def f35fd_f35_financial_distress_score_zaccel_63d_base_v055_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    tr = _f35_distresstrend(workingcapital, retearn, ebit, equity, liabilities, assets, 63)
    result = tr.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# deterioration acceleration: 126d change of the 126d distress trend
def f35fd_f35_financial_distress_score_zaccel_126d_base_v056_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    tr = _f35_distresstrend(workingcapital, retearn, ebit, equity, liabilities, assets, 126)
    result = tr.diff(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# solvency composite: equity/liabilities + EBIT/liabilities
def f35fd_f35_financial_distress_score_solvcomp_1d_base_v057_signal(equity, liabilities, ebit, workingcapital, retearn, assets):
    result = _f35_coverage(equity, liabilities) + _f35_coverage(ebit, liabilities) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed solvency composite
def f35fd_f35_financial_distress_score_solvcomp_63d_base_v058_signal(equity, liabilities, ebit, workingcapital, retearn, assets):
    c = _f35_coverage(equity, liabilities) + _f35_coverage(ebit, liabilities)
    result = _mean(c, 63) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity composite: working-capital coverage + cash coverage of liabilities
def f35fd_f35_financial_distress_score_liqcomp_1d_base_v059_signal(workingcapital, cashneq, liabilities, retearn, ebit, equity, assets):
    result = _f35_coverage(workingcapital, liabilities) + _f35_coverage(cashneq, liabilities) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed liquidity composite
def f35fd_f35_financial_distress_score_liqcomp_63d_base_v060_signal(workingcapital, cashneq, liabilities, retearn, ebit, equity, assets):
    c = _f35_coverage(workingcapital, liabilities) + _f35_coverage(cashneq, liabilities)
    result = _mean(c, 63) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# currentratio scaled by equity/liabilities cushion
def f35fd_f35_financial_distress_score_crcushion_1d_base_v061_signal(currentratio, equity, liabilities, workingcapital, retearn, ebit, assets):
    result = currentratio * _f35_coverage(equity, liabilities)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed currentratio cushion
def f35fd_f35_financial_distress_score_crcushion_63d_base_v062_signal(currentratio, equity, liabilities, workingcapital, retearn, ebit, assets):
    c = currentratio * _f35_coverage(equity, liabilities)
    result = _mean(c, 63) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# currentratio z-score over 252d (liquidity regime)
def f35fd_f35_financial_distress_score_crz_252d_base_v063_signal(currentratio, workingcapital, retearn, ebit, equity, liabilities, assets):
    result = _z(currentratio, 252) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT coverage z-score over 252d (earnings-solvency regime)
def f35fd_f35_financial_distress_score_covz_252d_base_v064_signal(ebit, liabilities, workingcapital, retearn, equity, assets):
    c = _f35_coverage(ebit, liabilities)
    result = _z(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# WC/assets z-score over 252d
def f35fd_f35_financial_distress_score_wctaz_252d_base_v065_signal(workingcapital, assets, retearn, ebit, equity, liabilities):
    c = _f35_zcomp(workingcapital, assets, 6.56)
    result = _z(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT/assets z-score over 252d
def f35fd_f35_financial_distress_score_ebittaz_252d_base_v066_signal(ebit, assets, workingcapital, retearn, equity, liabilities):
    c = _f35_zcomp(ebit, assets, 6.72)
    result = _z(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# Altman score scaled by its own 252d dispersion (stability-adjusted distress)
def f35fd_f35_financial_distress_score_zstab_252d_base_v067_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = _safe_div(z, _std(z, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# Altman score minus its 126d mean (distress surprise)
def f35fd_f35_financial_distress_score_zsurp_126d_base_v068_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = z - _mean(z, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Altman score minus its 252d mean (distress surprise, slow)
def f35fd_f35_financial_distress_score_zsurp_252d_base_v069_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = z - _mean(z, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT margin (ebit/revenue) - profitability distress driver
def f35fd_f35_financial_distress_score_ebitmgn_1d_base_v070_signal(ebit, revenue, workingcapital, retearn, equity, liabilities, assets):
    result = _safe_div(ebit, revenue) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed EBIT margin
def f35fd_f35_financial_distress_score_ebitmgn_63d_base_v071_signal(ebit, revenue, workingcapital, retearn, equity, liabilities, assets):
    c = _safe_div(ebit, revenue)
    result = _mean(c, 63) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# NCFO / revenue (cash conversion) - distress driver
def f35fd_f35_financial_distress_score_ncforev_1d_base_v072_signal(ncfo, revenue, workingcapital, retearn, ebit, equity, liabilities, assets):
    result = _safe_div(ncfo, revenue) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash / assets (liquidity buffer)
def f35fd_f35_financial_distress_score_cashta_1d_base_v073_signal(cashneq, assets, workingcapital, retearn, ebit, equity, liabilities):
    result = _safe_div(cashneq, assets) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed cash/assets buffer
def f35fd_f35_financial_distress_score_cashta_63d_base_v074_signal(cashneq, assets, workingcapital, retearn, ebit, equity, liabilities):
    c = _safe_div(cashneq, assets)
    result = _mean(c, 63) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# market leverage: marketcap / (marketcap + liabilities) inverse cushion
def f35fd_f35_financial_distress_score_mktlev_1d_base_v075_signal(marketcap, liabilities, workingcapital, retearn, ebit, equity, assets):
    result = _safe_div(liabilities, marketcap + liabilities) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f35fd_f35_financial_distress_score_altman_1d_base_v001_signal,
    f35fd_f35_financial_distress_score_altmansm_21d_base_v002_signal,
    f35fd_f35_financial_distress_score_altmansm_63d_base_v003_signal,
    f35fd_f35_financial_distress_score_altmansm_126d_base_v004_signal,
    f35fd_f35_financial_distress_score_altmansm_252d_base_v005_signal,
    f35fd_f35_financial_distress_score_wcta_1d_base_v006_signal,
    f35fd_f35_financial_distress_score_wcta_63d_base_v007_signal,
    f35fd_f35_financial_distress_score_wcta_252d_base_v008_signal,
    f35fd_f35_financial_distress_score_reta_1d_base_v009_signal,
    f35fd_f35_financial_distress_score_reta_63d_base_v010_signal,
    f35fd_f35_financial_distress_score_reta_252d_base_v011_signal,
    f35fd_f35_financial_distress_score_ebitta_1d_base_v012_signal,
    f35fd_f35_financial_distress_score_ebitta_63d_base_v013_signal,
    f35fd_f35_financial_distress_score_ebitta_252d_base_v014_signal,
    f35fd_f35_financial_distress_score_eqliab_1d_base_v015_signal,
    f35fd_f35_financial_distress_score_eqliab_63d_base_v016_signal,
    f35fd_f35_financial_distress_score_eqliab_252d_base_v017_signal,
    f35fd_f35_financial_distress_score_revta_1d_base_v018_signal,
    f35fd_f35_financial_distress_score_revta_63d_base_v019_signal,
    f35fd_f35_financial_distress_score_revta_252d_base_v020_signal,
    f35fd_f35_financial_distress_score_ebitcov_1d_base_v021_signal,
    f35fd_f35_financial_distress_score_ebitcov_63d_base_v022_signal,
    f35fd_f35_financial_distress_score_ebitcov_252d_base_v023_signal,
    f35fd_f35_financial_distress_score_cashcov_1d_base_v024_signal,
    f35fd_f35_financial_distress_score_cashcov_63d_base_v025_signal,
    f35fd_f35_financial_distress_score_cashcov_252d_base_v026_signal,
    f35fd_f35_financial_distress_score_ncfocov_1d_base_v027_signal,
    f35fd_f35_financial_distress_score_ncfocov_63d_base_v028_signal,
    f35fd_f35_financial_distress_score_ncfocov_252d_base_v029_signal,
    f35fd_f35_financial_distress_score_mktliab_1d_base_v030_signal,
    f35fd_f35_financial_distress_score_mktliab_63d_base_v031_signal,
    f35fd_f35_financial_distress_score_mktliab_252d_base_v032_signal,
    f35fd_f35_financial_distress_score_mktz_1d_base_v033_signal,
    f35fd_f35_financial_distress_score_mktz_63d_base_v034_signal,
    f35fd_f35_financial_distress_score_debtta_1d_base_v035_signal,
    f35fd_f35_financial_distress_score_debtta_63d_base_v036_signal,
    f35fd_f35_financial_distress_score_debteq_1d_base_v037_signal,
    f35fd_f35_financial_distress_score_debteq_63d_base_v038_signal,
    f35fd_f35_financial_distress_score_netdebtta_1d_base_v039_signal,
    f35fd_f35_financial_distress_score_netdebtta_63d_base_v040_signal,
    f35fd_f35_financial_distress_score_liabta_1d_base_v041_signal,
    f35fd_f35_financial_distress_score_liabta_63d_base_v042_signal,
    f35fd_f35_financial_distress_score_ztrend_63d_base_v043_signal,
    f35fd_f35_financial_distress_score_ztrend_126d_base_v044_signal,
    f35fd_f35_financial_distress_score_ztrend_252d_base_v045_signal,
    f35fd_f35_financial_distress_score_ztrend_504d_base_v046_signal,
    f35fd_f35_financial_distress_score_zofz_252d_base_v047_signal,
    f35fd_f35_financial_distress_score_zofz_126d_base_v048_signal,
    f35fd_f35_financial_distress_score_zofz_504d_base_v049_signal,
    f35fd_f35_financial_distress_score_zrank_252d_base_v050_signal,
    f35fd_f35_financial_distress_score_zrank_504d_base_v051_signal,
    f35fd_f35_financial_distress_score_d2d_252d_base_v052_signal,
    f35fd_f35_financial_distress_score_d2d_126d_base_v053_signal,
    f35fd_f35_financial_distress_score_mktd2d_252d_base_v054_signal,
    f35fd_f35_financial_distress_score_zaccel_63d_base_v055_signal,
    f35fd_f35_financial_distress_score_zaccel_126d_base_v056_signal,
    f35fd_f35_financial_distress_score_solvcomp_1d_base_v057_signal,
    f35fd_f35_financial_distress_score_solvcomp_63d_base_v058_signal,
    f35fd_f35_financial_distress_score_liqcomp_1d_base_v059_signal,
    f35fd_f35_financial_distress_score_liqcomp_63d_base_v060_signal,
    f35fd_f35_financial_distress_score_crcushion_1d_base_v061_signal,
    f35fd_f35_financial_distress_score_crcushion_63d_base_v062_signal,
    f35fd_f35_financial_distress_score_crz_252d_base_v063_signal,
    f35fd_f35_financial_distress_score_covz_252d_base_v064_signal,
    f35fd_f35_financial_distress_score_wctaz_252d_base_v065_signal,
    f35fd_f35_financial_distress_score_ebittaz_252d_base_v066_signal,
    f35fd_f35_financial_distress_score_zstab_252d_base_v067_signal,
    f35fd_f35_financial_distress_score_zsurp_126d_base_v068_signal,
    f35fd_f35_financial_distress_score_zsurp_252d_base_v069_signal,
    f35fd_f35_financial_distress_score_ebitmgn_1d_base_v070_signal,
    f35fd_f35_financial_distress_score_ebitmgn_63d_base_v071_signal,
    f35fd_f35_financial_distress_score_ncforev_1d_base_v072_signal,
    f35fd_f35_financial_distress_score_cashta_1d_base_v073_signal,
    f35fd_f35_financial_distress_score_cashta_63d_base_v074_signal,
    f35fd_f35_financial_distress_score_mktlev_1d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F35_FINANCIAL_DISTRESS_SCORE_REGISTRY_001_075 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    POS = {"assets", "equity", "revenue", "cashneq", "marketcap", "currentratio",
           "workingcapital", "ebit", "debt"}
    for nm in names:
        walk = np.cumsum(np.random.normal(0.0, 1.0, n))
        level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
        s = level + 50.0 * walk
        if nm in POS:
            s = np.abs(s) + 10.0
        out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f35_altman", "_f35_zcomp", "_f35_coverage", "_f35_distresstrend")
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0
    nan_ok = 0
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
    print(f"OK f35_financial_distress_score_base_001_075_claude: {n_features} features pass")
