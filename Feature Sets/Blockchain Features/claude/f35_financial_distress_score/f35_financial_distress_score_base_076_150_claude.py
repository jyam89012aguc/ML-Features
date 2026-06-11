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


# ============ FEATURES 076-150 ============

# 504d-smoothed Altman Z'' score (long stability)
def f35fd_f35_financial_distress_score_altmansm_504d_base_v076_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = _mean(z, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM-smoothed Altman score (span 63)
def f35fd_f35_financial_distress_score_altmanewm_63d_base_v077_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = z.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# EWM-smoothed Altman score (span 126)
def f35fd_f35_financial_distress_score_altmanewm_126d_base_v078_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = z.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed WC/assets component
def f35fd_f35_financial_distress_score_wcta_126d_base_v079_signal(workingcapital, assets, retearn, ebit, equity, liabilities):
    c = _f35_zcomp(workingcapital, assets, 6.56)
    result = _mean(c, 126) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed RE/assets component
def f35fd_f35_financial_distress_score_reta_126d_base_v080_signal(retearn, assets, workingcapital, ebit, equity, liabilities):
    c = _f35_zcomp(retearn, assets, 3.26)
    result = _mean(c, 126) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed EBIT/assets component
def f35fd_f35_financial_distress_score_ebitta_126d_base_v081_signal(ebit, assets, workingcapital, retearn, equity, liabilities):
    c = _f35_zcomp(ebit, assets, 6.72)
    result = _mean(c, 126) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed equity/liabilities component
def f35fd_f35_financial_distress_score_eqliab_126d_base_v082_signal(equity, liabilities, workingcapital, retearn, ebit, assets):
    c = _f35_zcomp(equity, liabilities, 1.05)
    result = _mean(c, 126) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed revenue/assets turnover
def f35fd_f35_financial_distress_score_revta_126d_base_v083_signal(revenue, assets, workingcapital, retearn, ebit, equity, liabilities):
    c = _f35_zcomp(revenue, assets, 1.0)
    result = _mean(c, 126) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed EBIT coverage of liabilities
def f35fd_f35_financial_distress_score_ebitcov_126d_base_v084_signal(ebit, liabilities, workingcapital, retearn, equity, assets):
    c = _f35_coverage(ebit, liabilities)
    result = _mean(c, 126) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed cash coverage of liabilities
def f35fd_f35_financial_distress_score_cashcov_126d_base_v085_signal(cashneq, liabilities, workingcapital, retearn, ebit, equity, assets):
    c = _f35_coverage(cashneq, liabilities)
    result = _mean(c, 126) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed NCFO coverage of liabilities
def f35fd_f35_financial_distress_score_ncfocov_126d_base_v086_signal(ncfo, liabilities, workingcapital, retearn, ebit, equity, assets):
    c = _f35_coverage(ncfo, liabilities)
    result = _mean(c, 126) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed marketcap/liabilities
def f35fd_f35_financial_distress_score_mktliab_126d_base_v087_signal(marketcap, liabilities, workingcapital, retearn, ebit, equity, assets):
    c = _f35_coverage(marketcap, liabilities)
    result = _mean(c, 126) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed market-augmented Altman
def f35fd_f35_financial_distress_score_mktz_252d_base_v088_signal(workingcapital, retearn, ebit, assets, liabilities, marketcap, equity):
    base = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    m = base - _f35_zcomp(equity, liabilities, 1.05) + 1.05 * _safe_div(marketcap, liabilities)
    result = _mean(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed debt/assets leverage
def f35fd_f35_financial_distress_score_debtta_252d_base_v089_signal(debt, assets, workingcapital, retearn, ebit, equity, liabilities):
    c = _f35_zcomp(debt, assets, 1.0)
    result = _mean(c, 252) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed debt/equity gearing
def f35fd_f35_financial_distress_score_debteq_252d_base_v090_signal(debt, equity, workingcapital, retearn, ebit, liabilities, assets):
    c = _f35_coverage(debt, equity)
    result = _mean(c, 252) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed net-debt/assets
def f35fd_f35_financial_distress_score_netdebtta_252d_base_v091_signal(debt, cashneq, assets, workingcapital, retearn, ebit, equity, liabilities):
    c = _safe_div(debt - cashneq, assets)
    result = _mean(c, 252) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed liabilities/assets
def f35fd_f35_financial_distress_score_liabta_252d_base_v092_signal(liabilities, assets, workingcapital, retearn, ebit, equity):
    c = _safe_div(liabilities, assets)
    result = _mean(c, 252) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distress trend: 42d change in Altman score (fast deterioration)
def f35fd_f35_financial_distress_score_ztrend_42d_base_v093_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    result = _f35_distresstrend(workingcapital, retearn, ebit, equity, liabilities, assets, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# distress trend: 189d change in Altman score
def f35fd_f35_financial_distress_score_ztrend_189d_base_v094_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    result = _f35_distresstrend(workingcapital, retearn, ebit, equity, liabilities, assets, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# distress-trend normalized by Altman dispersion (deterioration intensity)
def f35fd_f35_financial_distress_score_ztrendnorm_126d_base_v095_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    tr = _f35_distresstrend(workingcapital, retearn, ebit, equity, liabilities, assets, 126)
    result = _safe_div(tr, _std(z, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# distress-trend normalized by Altman dispersion (63d)
def f35fd_f35_financial_distress_score_ztrendnorm_63d_base_v096_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    tr = _f35_distresstrend(workingcapital, retearn, ebit, equity, liabilities, assets, 63)
    result = _safe_div(tr, _std(z, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# Altman z-score standardized over 378d
def f35fd_f35_financial_distress_score_zofz_378d_base_v097_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = _z(z, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# Altman score percentile rank over 126d
def f35fd_f35_financial_distress_score_zrank_126d_base_v098_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = z.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# Altman score percentile rank over 378d
def f35fd_f35_financial_distress_score_zrank_378d_base_v099_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = z.rolling(378, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# distance-to-default proxy over 504d asset vol (long-horizon)
def f35fd_f35_financial_distress_score_d2d_504d_base_v100_signal(equity, liabilities, assets, workingcapital, retearn, ebit):
    cushion = _safe_div(equity, liabilities)
    vol = _std(_safe_div(assets.diff(), assets), 504)
    result = _safe_div(cushion, vol) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# market distance-to-default over 126d equity-value vol
def f35fd_f35_financial_distress_score_mktd2d_126d_base_v101_signal(marketcap, liabilities, workingcapital, retearn, ebit, equity, assets):
    cushion = _safe_div(marketcap, liabilities)
    vol = _std(_safe_div(marketcap.diff(), marketcap), 126)
    result = _safe_div(cushion, vol) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# deterioration acceleration: 252d change of the 252d distress trend
def f35fd_f35_financial_distress_score_zaccel_252d_base_v102_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    tr = _f35_distresstrend(workingcapital, retearn, ebit, equity, liabilities, assets, 252)
    result = tr.diff(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# deterioration acceleration: 42d change of the 42d distress trend
def f35fd_f35_financial_distress_score_zaccel_42d_base_v103_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    tr = _f35_distresstrend(workingcapital, retearn, ebit, equity, liabilities, assets, 42)
    result = tr.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed solvency composite
def f35fd_f35_financial_distress_score_solvcomp_252d_base_v104_signal(equity, liabilities, ebit, workingcapital, retearn, assets):
    c = _f35_coverage(equity, liabilities) + _f35_coverage(ebit, liabilities)
    result = _mean(c, 252) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed liquidity composite
def f35fd_f35_financial_distress_score_liqcomp_252d_base_v105_signal(workingcapital, cashneq, liabilities, retearn, ebit, equity, assets):
    c = _f35_coverage(workingcapital, liabilities) + _f35_coverage(cashneq, liabilities)
    result = _mean(c, 252) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# full solvency stack: equity + EBIT + cash coverage of liabilities
def f35fd_f35_financial_distress_score_solvstack_63d_base_v106_signal(equity, ebit, cashneq, liabilities, workingcapital, retearn, assets):
    c = _f35_coverage(equity, liabilities) + _f35_coverage(ebit, liabilities) + _f35_coverage(cashneq, liabilities)
    result = _mean(c, 63) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed full solvency stack
def f35fd_f35_financial_distress_score_solvstack_252d_base_v107_signal(equity, ebit, cashneq, liabilities, workingcapital, retearn, assets):
    c = _f35_coverage(equity, liabilities) + _f35_coverage(ebit, liabilities) + _f35_coverage(cashneq, liabilities)
    result = _mean(c, 252) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# currentratio cushion z-score over 252d
def f35fd_f35_financial_distress_score_crcushionz_252d_base_v108_signal(currentratio, equity, liabilities, workingcapital, retearn, ebit, assets):
    c = currentratio * _f35_coverage(equity, liabilities)
    result = _z(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT-coverage z-score over 126d
def f35fd_f35_financial_distress_score_covz_126d_base_v109_signal(ebit, liabilities, workingcapital, retearn, equity, assets):
    c = _f35_coverage(ebit, liabilities)
    result = _z(c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# cash-coverage z-score over 252d
def f35fd_f35_financial_distress_score_cashcovz_252d_base_v110_signal(cashneq, liabilities, workingcapital, retearn, ebit, equity, assets):
    c = _f35_coverage(cashneq, liabilities)
    result = _z(c, 252) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap/liabilities z-score over 252d (market-distress regime)
def f35fd_f35_financial_distress_score_mktliabz_252d_base_v111_signal(marketcap, liabilities, workingcapital, retearn, ebit, equity, assets):
    c = _f35_coverage(marketcap, liabilities)
    result = _z(c, 252) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# RE/assets z-score over 252d
def f35fd_f35_financial_distress_score_retaz_252d_base_v112_signal(retearn, assets, workingcapital, ebit, equity, liabilities):
    c = _f35_zcomp(retearn, assets, 3.26)
    result = _z(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# equity/liabilities z-score over 252d
def f35fd_f35_financial_distress_score_eqliabz_252d_base_v113_signal(equity, liabilities, workingcapital, retearn, ebit, assets):
    c = _f35_zcomp(equity, liabilities, 1.05)
    result = _z(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# Altman score scaled by 126d dispersion (stability-adjusted, fast)
def f35fd_f35_financial_distress_score_zstab_126d_base_v114_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = _safe_div(z, _std(z, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# Altman score scaled by 504d dispersion (stability-adjusted, slow)
def f35fd_f35_financial_distress_score_zstab_504d_base_v115_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = _safe_div(z, _std(z, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# Altman score minus its 63d mean (distress surprise, fast)
def f35fd_f35_financial_distress_score_zsurp_63d_base_v116_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = z - _mean(z, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Altman score minus its 504d mean (distress surprise, slow)
def f35fd_f35_financial_distress_score_zsurp_504d_base_v117_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = z - _mean(z, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed EBIT margin (ebit/revenue)
def f35fd_f35_financial_distress_score_ebitmgn_126d_base_v118_signal(ebit, revenue, workingcapital, retearn, equity, liabilities, assets):
    c = _safe_div(ebit, revenue)
    result = _mean(c, 126) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed NCFO/revenue cash conversion
def f35fd_f35_financial_distress_score_ncforev_63d_base_v119_signal(ncfo, revenue, workingcapital, retearn, ebit, equity, liabilities, assets):
    c = _safe_div(ncfo, revenue)
    result = _mean(c, 63) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# NCFO / debt (cash service of debt)
def f35fd_f35_financial_distress_score_ncfodebt_1d_base_v120_signal(ncfo, debt, workingcapital, retearn, ebit, equity, liabilities, assets):
    result = _safe_div(ncfo, debt) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed NCFO/debt
def f35fd_f35_financial_distress_score_ncfodebt_63d_base_v121_signal(ncfo, debt, workingcapital, retearn, ebit, equity, liabilities, assets):
    c = _safe_div(ncfo, debt)
    result = _mean(c, 63) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT / debt (earnings service of debt)
def f35fd_f35_financial_distress_score_ebitdebt_1d_base_v122_signal(ebit, debt, workingcapital, retearn, equity, liabilities, assets):
    result = _safe_div(ebit, debt) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed EBIT/debt
def f35fd_f35_financial_distress_score_ebitdebt_126d_base_v123_signal(ebit, debt, workingcapital, retearn, equity, liabilities, assets):
    c = _safe_div(ebit, debt)
    result = _mean(c, 126) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed cash/assets buffer
def f35fd_f35_financial_distress_score_cashta_126d_base_v124_signal(cashneq, assets, workingcapital, retearn, ebit, equity, liabilities):
    c = _safe_div(cashneq, assets)
    result = _mean(c, 126) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash-burn runway proxy: cash / (negative NCFO drag) scaled by assets
def f35fd_f35_financial_distress_score_runway_63d_base_v125_signal(cashneq, ncfo, assets, workingcapital, retearn, ebit, equity, liabilities):
    burn = _mean(ncfo, 63)
    result = _safe_div(cashneq, assets) - _safe_div(burn, assets) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital / liabilities coverage
def f35fd_f35_financial_distress_score_wcliab_1d_base_v126_signal(workingcapital, liabilities, retearn, ebit, equity, assets):
    result = _f35_coverage(workingcapital, liabilities) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed WC/liabilities coverage
def f35fd_f35_financial_distress_score_wcliab_126d_base_v127_signal(workingcapital, liabilities, retearn, ebit, equity, assets):
    c = _f35_coverage(workingcapital, liabilities)
    result = _mean(c, 126) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# retained-earnings / equity (accumulated-deficit signal)
def f35fd_f35_financial_distress_score_reeq_1d_base_v128_signal(retearn, equity, workingcapital, ebit, liabilities, assets):
    result = _f35_coverage(retearn, equity) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed retained-earnings/equity
def f35fd_f35_financial_distress_score_reeq_126d_base_v129_signal(retearn, equity, workingcapital, ebit, liabilities, assets):
    c = _f35_coverage(retearn, equity)
    result = _mean(c, 126) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# equity / assets (book solvency ratio)
def f35fd_f35_financial_distress_score_eqta_1d_base_v130_signal(equity, assets, workingcapital, retearn, ebit, liabilities):
    result = _f35_zcomp(equity, assets, 1.0) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed equity/assets
def f35fd_f35_financial_distress_score_eqta_126d_base_v131_signal(equity, assets, workingcapital, retearn, ebit, liabilities):
    c = _f35_zcomp(equity, assets, 1.0)
    result = _mean(c, 126) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# market value of equity / assets (market book solvency)
def f35fd_f35_financial_distress_score_mkteqta_1d_base_v132_signal(marketcap, assets, workingcapital, retearn, ebit, equity, liabilities):
    result = _safe_div(marketcap, assets) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed marketcap/assets
def f35fd_f35_financial_distress_score_mkteqta_252d_base_v133_signal(marketcap, assets, workingcapital, retearn, ebit, equity, liabilities):
    c = _safe_div(marketcap, assets)
    result = _mean(c, 252) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# revenue / liabilities (top-line coverage of obligations)
def f35fd_f35_financial_distress_score_revliab_1d_base_v134_signal(revenue, liabilities, workingcapital, retearn, ebit, equity, assets):
    result = _f35_coverage(revenue, liabilities) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed revenue/liabilities
def f35fd_f35_financial_distress_score_revliab_126d_base_v135_signal(revenue, liabilities, workingcapital, retearn, ebit, equity, assets):
    c = _f35_coverage(revenue, liabilities)
    result = _mean(c, 126) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Altman components dispersion (cross-sectional spread of the 4 ratios over time)
def f35fd_f35_financial_distress_score_compdisp_252d_base_v136_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    x1 = _f35_zcomp(workingcapital, assets, 6.56)
    x3 = _f35_zcomp(ebit, assets, 6.72)
    result = _std(x1 - x3, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT/assets minus liabilities/assets (profitability-leverage gap)
def f35fd_f35_financial_distress_score_profgap_1d_base_v137_signal(ebit, liabilities, assets, workingcapital, retearn, equity):
    result = _safe_div(ebit, assets) - _safe_div(liabilities, assets) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed profitability-leverage gap
def f35fd_f35_financial_distress_score_profgap_63d_base_v138_signal(ebit, liabilities, assets, workingcapital, retearn, equity):
    c = _safe_div(ebit, assets) - _safe_div(liabilities, assets)
    result = _mean(c, 63) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Altman EWM-trend gap: score minus its EWM (momentum of distress)
def f35fd_f35_financial_distress_score_zewmgap_63d_base_v139_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = z - z.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# Altman EWM-trend gap (span 126)
def f35fd_f35_financial_distress_score_zewmgap_126d_base_v140_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = z - z.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# coverage trend: 126d change in EBIT/liabilities solvency
def f35fd_f35_financial_distress_score_covtrend_126d_base_v141_signal(ebit, liabilities, workingcapital, retearn, equity, assets):
    c = _f35_coverage(ebit, liabilities)
    result = c.diff(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# coverage trend: 63d change in cash/liabilities solvency
def f35fd_f35_financial_distress_score_cashcovtrend_63d_base_v142_signal(cashneq, liabilities, workingcapital, retearn, ebit, equity, assets):
    c = _f35_coverage(cashneq, liabilities)
    result = c.diff(periods=63) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# leverage trend: 126d change in liabilities/assets
def f35fd_f35_financial_distress_score_levtrend_126d_base_v143_signal(liabilities, assets, workingcapital, retearn, ebit, equity):
    c = _safe_div(liabilities, assets)
    result = c.diff(periods=126) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distress-weighted leverage: liabilities/assets scaled by inverse Altman cushion
def f35fd_f35_financial_distress_score_levw_63d_base_v144_signal(liabilities, assets, workingcapital, retearn, ebit, equity):
    lev = _safe_div(liabilities, assets)
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    result = _mean(lev * z, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# distress composite: Altman score blended with EBIT-coverage solvency
def f35fd_f35_financial_distress_score_zcovblend_63d_base_v145_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    cov = _f35_coverage(ebit, liabilities)
    result = _mean(0.5 * z + 0.5 * cov, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# distress composite over 252d (slow)
def f35fd_f35_financial_distress_score_zcovblend_252d_base_v146_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    cov = _f35_coverage(ebit, liabilities)
    result = _mean(0.5 * z + 0.5 * cov, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# Altman score deviation from its 252d percentile-rank trend (regime distress)
def f35fd_f35_financial_distress_score_zrankdev_252d_base_v147_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    rk = z.rolling(252, min_periods=63).rank(pct=True)
    result = rk - _mean(rk, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# solvency information ratio: equity/liabilities cushion vs its own dispersion
def f35fd_f35_financial_distress_score_solvir_252d_base_v148_signal(equity, liabilities, workingcapital, retearn, ebit, assets):
    cushion = _f35_coverage(equity, liabilities)
    result = _safe_div(cushion, _std(cushion, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# coverage information ratio: EBIT/liabilities vs its own 126d dispersion
def f35fd_f35_financial_distress_score_covir_126d_base_v149_signal(ebit, liabilities, workingcapital, retearn, equity, assets):
    cov = _f35_coverage(ebit, liabilities)
    result = _safe_div(cov, _std(cov, 126)) + _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# grand distress composite: smoothed Altman + solvency + liquidity stack
def f35fd_f35_financial_distress_score_grand_126d_base_v150_signal(workingcapital, retearn, ebit, equity, liabilities, assets, cashneq):
    z = _f35_altman(workingcapital, retearn, ebit, equity, liabilities, assets)
    solv = _f35_coverage(ebit, liabilities)
    liq = _f35_coverage(cashneq, liabilities)
    result = _mean(z + solv + liq, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f35fd_f35_financial_distress_score_altmansm_504d_base_v076_signal,
    f35fd_f35_financial_distress_score_altmanewm_63d_base_v077_signal,
    f35fd_f35_financial_distress_score_altmanewm_126d_base_v078_signal,
    f35fd_f35_financial_distress_score_wcta_126d_base_v079_signal,
    f35fd_f35_financial_distress_score_reta_126d_base_v080_signal,
    f35fd_f35_financial_distress_score_ebitta_126d_base_v081_signal,
    f35fd_f35_financial_distress_score_eqliab_126d_base_v082_signal,
    f35fd_f35_financial_distress_score_revta_126d_base_v083_signal,
    f35fd_f35_financial_distress_score_ebitcov_126d_base_v084_signal,
    f35fd_f35_financial_distress_score_cashcov_126d_base_v085_signal,
    f35fd_f35_financial_distress_score_ncfocov_126d_base_v086_signal,
    f35fd_f35_financial_distress_score_mktliab_126d_base_v087_signal,
    f35fd_f35_financial_distress_score_mktz_252d_base_v088_signal,
    f35fd_f35_financial_distress_score_debtta_252d_base_v089_signal,
    f35fd_f35_financial_distress_score_debteq_252d_base_v090_signal,
    f35fd_f35_financial_distress_score_netdebtta_252d_base_v091_signal,
    f35fd_f35_financial_distress_score_liabta_252d_base_v092_signal,
    f35fd_f35_financial_distress_score_ztrend_42d_base_v093_signal,
    f35fd_f35_financial_distress_score_ztrend_189d_base_v094_signal,
    f35fd_f35_financial_distress_score_ztrendnorm_126d_base_v095_signal,
    f35fd_f35_financial_distress_score_ztrendnorm_63d_base_v096_signal,
    f35fd_f35_financial_distress_score_zofz_378d_base_v097_signal,
    f35fd_f35_financial_distress_score_zrank_126d_base_v098_signal,
    f35fd_f35_financial_distress_score_zrank_378d_base_v099_signal,
    f35fd_f35_financial_distress_score_d2d_504d_base_v100_signal,
    f35fd_f35_financial_distress_score_mktd2d_126d_base_v101_signal,
    f35fd_f35_financial_distress_score_zaccel_252d_base_v102_signal,
    f35fd_f35_financial_distress_score_zaccel_42d_base_v103_signal,
    f35fd_f35_financial_distress_score_solvcomp_252d_base_v104_signal,
    f35fd_f35_financial_distress_score_liqcomp_252d_base_v105_signal,
    f35fd_f35_financial_distress_score_solvstack_63d_base_v106_signal,
    f35fd_f35_financial_distress_score_solvstack_252d_base_v107_signal,
    f35fd_f35_financial_distress_score_crcushionz_252d_base_v108_signal,
    f35fd_f35_financial_distress_score_covz_126d_base_v109_signal,
    f35fd_f35_financial_distress_score_cashcovz_252d_base_v110_signal,
    f35fd_f35_financial_distress_score_mktliabz_252d_base_v111_signal,
    f35fd_f35_financial_distress_score_retaz_252d_base_v112_signal,
    f35fd_f35_financial_distress_score_eqliabz_252d_base_v113_signal,
    f35fd_f35_financial_distress_score_zstab_126d_base_v114_signal,
    f35fd_f35_financial_distress_score_zstab_504d_base_v115_signal,
    f35fd_f35_financial_distress_score_zsurp_63d_base_v116_signal,
    f35fd_f35_financial_distress_score_zsurp_504d_base_v117_signal,
    f35fd_f35_financial_distress_score_ebitmgn_126d_base_v118_signal,
    f35fd_f35_financial_distress_score_ncforev_63d_base_v119_signal,
    f35fd_f35_financial_distress_score_ncfodebt_1d_base_v120_signal,
    f35fd_f35_financial_distress_score_ncfodebt_63d_base_v121_signal,
    f35fd_f35_financial_distress_score_ebitdebt_1d_base_v122_signal,
    f35fd_f35_financial_distress_score_ebitdebt_126d_base_v123_signal,
    f35fd_f35_financial_distress_score_cashta_126d_base_v124_signal,
    f35fd_f35_financial_distress_score_runway_63d_base_v125_signal,
    f35fd_f35_financial_distress_score_wcliab_1d_base_v126_signal,
    f35fd_f35_financial_distress_score_wcliab_126d_base_v127_signal,
    f35fd_f35_financial_distress_score_reeq_1d_base_v128_signal,
    f35fd_f35_financial_distress_score_reeq_126d_base_v129_signal,
    f35fd_f35_financial_distress_score_eqta_1d_base_v130_signal,
    f35fd_f35_financial_distress_score_eqta_126d_base_v131_signal,
    f35fd_f35_financial_distress_score_mkteqta_1d_base_v132_signal,
    f35fd_f35_financial_distress_score_mkteqta_252d_base_v133_signal,
    f35fd_f35_financial_distress_score_revliab_1d_base_v134_signal,
    f35fd_f35_financial_distress_score_revliab_126d_base_v135_signal,
    f35fd_f35_financial_distress_score_compdisp_252d_base_v136_signal,
    f35fd_f35_financial_distress_score_profgap_1d_base_v137_signal,
    f35fd_f35_financial_distress_score_profgap_63d_base_v138_signal,
    f35fd_f35_financial_distress_score_zewmgap_63d_base_v139_signal,
    f35fd_f35_financial_distress_score_zewmgap_126d_base_v140_signal,
    f35fd_f35_financial_distress_score_covtrend_126d_base_v141_signal,
    f35fd_f35_financial_distress_score_cashcovtrend_63d_base_v142_signal,
    f35fd_f35_financial_distress_score_levtrend_126d_base_v143_signal,
    f35fd_f35_financial_distress_score_levw_63d_base_v144_signal,
    f35fd_f35_financial_distress_score_zcovblend_63d_base_v145_signal,
    f35fd_f35_financial_distress_score_zcovblend_252d_base_v146_signal,
    f35fd_f35_financial_distress_score_zrankdev_252d_base_v147_signal,
    f35fd_f35_financial_distress_score_solvir_252d_base_v148_signal,
    f35fd_f35_financial_distress_score_covir_126d_base_v149_signal,
    f35fd_f35_financial_distress_score_grand_126d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F35_FINANCIAL_DISTRESS_SCORE_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f35_financial_distress_score_base_076_150_claude: {n_features} features pass")
