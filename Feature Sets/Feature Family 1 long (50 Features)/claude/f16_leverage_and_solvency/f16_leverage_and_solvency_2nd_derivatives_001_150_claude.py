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


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f16_leverage_ratio(debt, denom, w):
    d = _mean(debt, w)
    e = _mean(denom, w)
    return d / e.replace(0, np.nan).abs()


def _f16_solvency_coverage(numerator, expense, w):
    n = _mean(numerator, w)
    e = _mean(expense, w)
    return n / e.replace(0, np.nan).abs()


# 5d slope of 21d D/E x marketcap
def f16ls_f16_leverage_and_solvency_de_21d_slope_v001_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 21) * marketcap
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d D/E
def f16ls_f16_leverage_and_solvency_de_21d_slope_v002_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d D/E
def f16ls_f16_leverage_and_solvency_de_63d_slope_v003_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 63) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d D/E
def f16ls_f16_leverage_and_solvency_de_63d_slope_v004_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 63) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d D/E
def f16ls_f16_leverage_and_solvency_de_126d_slope_v005_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 126) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d D/E
def f16ls_f16_leverage_and_solvency_de_126d_slope_v006_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 126) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d D/E
def f16ls_f16_leverage_and_solvency_de_252d_slope_v007_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 252) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d D/E
def f16ls_f16_leverage_and_solvency_de_252d_slope_v008_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d D/E
def f16ls_f16_leverage_and_solvency_de_504d_slope_v009_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 504) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d D/E
def f16ls_f16_leverage_and_solvency_de_504d_slope_v010_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d D/A
def f16ls_f16_leverage_and_solvency_da_21d_slope_v011_signal(debt, assets, marketcap):
    base = _f16_leverage_ratio(debt, assets, 21) * marketcap
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d D/A
def f16ls_f16_leverage_and_solvency_da_21d_slope_v012_signal(debt, assets, marketcap):
    base = _f16_leverage_ratio(debt, assets, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d D/A
def f16ls_f16_leverage_and_solvency_da_63d_slope_v013_signal(debt, assets, marketcap):
    base = _f16_leverage_ratio(debt, assets, 63) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d D/A
def f16ls_f16_leverage_and_solvency_da_252d_slope_v014_signal(debt, assets, marketcap):
    base = _f16_leverage_ratio(debt, assets, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d D/A
def f16ls_f16_leverage_and_solvency_da_504d_slope_v015_signal(debt, assets, marketcap):
    base = _f16_leverage_ratio(debt, assets, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d L/A
def f16ls_f16_leverage_and_solvency_la_21d_slope_v016_signal(liabilities, assets, marketcap):
    base = _f16_leverage_ratio(liabilities, assets, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d L/A
def f16ls_f16_leverage_and_solvency_la_252d_slope_v017_signal(liabilities, assets, marketcap):
    base = _f16_leverage_ratio(liabilities, assets, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d L/A
def f16ls_f16_leverage_and_solvency_la_504d_slope_v018_signal(liabilities, assets, marketcap):
    base = _f16_leverage_ratio(liabilities, assets, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d L/E
def f16ls_f16_leverage_and_solvency_le_21d_slope_v019_signal(liabilities, equity, marketcap):
    base = _f16_leverage_ratio(liabilities, equity, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d L/E
def f16ls_f16_leverage_and_solvency_le_252d_slope_v020_signal(liabilities, equity, marketcap):
    base = _f16_leverage_ratio(liabilities, equity, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d L/E
def f16ls_f16_leverage_and_solvency_le_504d_slope_v021_signal(liabilities, equity, marketcap):
    base = _f16_leverage_ratio(liabilities, equity, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d debt/ebitda
def f16ls_f16_leverage_and_solvency_debtebitda_21d_slope_v022_signal(debt, ebitda, marketcap):
    base = _f16_leverage_ratio(debt, ebitda, 21) * marketcap
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d debt/ebitda
def f16ls_f16_leverage_and_solvency_debtebitda_63d_slope_v023_signal(debt, ebitda, marketcap):
    base = _f16_leverage_ratio(debt, ebitda, 63) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d debt/ebitda
def f16ls_f16_leverage_and_solvency_debtebitda_252d_slope_v024_signal(debt, ebitda, marketcap):
    base = _f16_leverage_ratio(debt, ebitda, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d debt/ebitda
def f16ls_f16_leverage_and_solvency_debtebitda_504d_slope_v025_signal(debt, ebitda, marketcap):
    base = _f16_leverage_ratio(debt, ebitda, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d debt/fcf
def f16ls_f16_leverage_and_solvency_debtfcf_21d_slope_v026_signal(debt, fcf, marketcap):
    base = _f16_leverage_ratio(debt, fcf, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d debt/fcf
def f16ls_f16_leverage_and_solvency_debtfcf_252d_slope_v027_signal(debt, fcf, marketcap):
    base = _f16_leverage_ratio(debt, fcf, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d debt/fcf
def f16ls_f16_leverage_and_solvency_debtfcf_504d_slope_v028_signal(debt, fcf, marketcap):
    base = _f16_leverage_ratio(debt, fcf, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d debt/ncfo
def f16ls_f16_leverage_and_solvency_debtncfo_21d_slope_v029_signal(debt, ncfo, marketcap):
    base = _f16_leverage_ratio(debt, ncfo, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d debt/ncfo
def f16ls_f16_leverage_and_solvency_debtncfo_252d_slope_v030_signal(debt, ncfo, marketcap):
    base = _f16_leverage_ratio(debt, ncfo, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d debt/opinc
def f16ls_f16_leverage_and_solvency_debtopinc_21d_slope_v031_signal(debt, opinc, marketcap):
    base = _f16_leverage_ratio(debt, opinc, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d debt/opinc
def f16ls_f16_leverage_and_solvency_debtopinc_252d_slope_v032_signal(debt, opinc, marketcap):
    base = _f16_leverage_ratio(debt, opinc, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d debt/revenue
def f16ls_f16_leverage_and_solvency_debtrev_21d_slope_v033_signal(debt, revenue, marketcap):
    base = _f16_leverage_ratio(debt, revenue, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d debt/revenue
def f16ls_f16_leverage_and_solvency_debtrev_252d_slope_v034_signal(debt, revenue, marketcap):
    base = _f16_leverage_ratio(debt, revenue, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d debt/revenue
def f16ls_f16_leverage_and_solvency_debtrev_504d_slope_v035_signal(debt, revenue, marketcap):
    base = _f16_leverage_ratio(debt, revenue, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d intcov
def f16ls_f16_leverage_and_solvency_intcov_21d_slope_v036_signal(ebitda, intexp, marketcap):
    base = _f16_solvency_coverage(ebitda, intexp, 21) * marketcap
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d intcov
def f16ls_f16_leverage_and_solvency_intcov_63d_slope_v037_signal(ebitda, intexp, marketcap):
    base = _f16_solvency_coverage(ebitda, intexp, 63) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d intcov
def f16ls_f16_leverage_and_solvency_intcov_252d_slope_v038_signal(ebitda, intexp, marketcap):
    base = _f16_solvency_coverage(ebitda, intexp, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d intcov
def f16ls_f16_leverage_and_solvency_intcov_504d_slope_v039_signal(ebitda, intexp, marketcap):
    base = _f16_solvency_coverage(ebitda, intexp, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d opinc/intexp
def f16ls_f16_leverage_and_solvency_intcovop_252d_slope_v040_signal(opinc, intexp, marketcap):
    base = _f16_solvency_coverage(opinc, intexp, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ncfo/intexp
def f16ls_f16_leverage_and_solvency_intcovncfo_252d_slope_v041_signal(ncfo, intexp, marketcap):
    base = _f16_solvency_coverage(ncfo, intexp, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d fcf/intexp
def f16ls_f16_leverage_and_solvency_intcovfcf_252d_slope_v042_signal(fcf, intexp, marketcap):
    base = _f16_solvency_coverage(fcf, intexp, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d (ebitda - capex)/intexp
def f16ls_f16_leverage_and_solvency_intcovrue_252d_slope_v043_signal(ebitda, capex, intexp, marketcap):
    num = ebitda - capex
    base = _f16_solvency_coverage(num, intexp, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d currentratio
def f16ls_f16_leverage_and_solvency_currentratio_21d_slope_v044_signal(currentratio, marketcap):
    base = _f16_solvency_coverage(currentratio * marketcap, marketcap, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d currentratio
def f16ls_f16_leverage_and_solvency_currentratio_252d_slope_v045_signal(currentratio, marketcap):
    base = _f16_solvency_coverage(currentratio * marketcap, marketcap, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d currentratio
def f16ls_f16_leverage_and_solvency_currentratio_504d_slope_v046_signal(currentratio, marketcap):
    base = _f16_solvency_coverage(currentratio * marketcap, marketcap, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d wc/liab
def f16ls_f16_leverage_and_solvency_wcliab_21d_slope_v047_signal(workingcapital, liabilities, marketcap):
    base = _f16_solvency_coverage(workingcapital, liabilities, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d wc/liab
def f16ls_f16_leverage_and_solvency_wcliab_252d_slope_v048_signal(workingcapital, liabilities, marketcap):
    base = _f16_solvency_coverage(workingcapital, liabilities, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d wc/debt
def f16ls_f16_leverage_and_solvency_wcdebt_21d_slope_v049_signal(workingcapital, debt, marketcap):
    base = _f16_solvency_coverage(workingcapital, debt, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d wc/debt
def f16ls_f16_leverage_and_solvency_wcdebt_252d_slope_v050_signal(workingcapital, debt, marketcap):
    base = _f16_solvency_coverage(workingcapital, debt, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d eq/assets
def f16ls_f16_leverage_and_solvency_eqassets_21d_slope_v051_signal(equity, assets, marketcap):
    base = _f16_solvency_coverage(equity, assets, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d eq/assets
def f16ls_f16_leverage_and_solvency_eqassets_252d_slope_v052_signal(equity, assets, marketcap):
    base = _f16_solvency_coverage(equity, assets, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d eq/assets
def f16ls_f16_leverage_and_solvency_eqassets_504d_slope_v053_signal(equity, assets, marketcap):
    base = _f16_solvency_coverage(equity, assets, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d retearn/debt
def f16ls_f16_leverage_and_solvency_retdebt_21d_slope_v054_signal(retearn, debt, marketcap):
    base = _f16_solvency_coverage(retearn, debt, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d retearn/debt
def f16ls_f16_leverage_and_solvency_retdebt_252d_slope_v055_signal(retearn, debt, marketcap):
    base = _f16_solvency_coverage(retearn, debt, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d retearn/debt
def f16ls_f16_leverage_and_solvency_retdebt_504d_slope_v056_signal(retearn, debt, marketcap):
    base = _f16_solvency_coverage(retearn, debt, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d retearn/liab
def f16ls_f16_leverage_and_solvency_retliab_21d_slope_v057_signal(retearn, liabilities, marketcap):
    base = _f16_solvency_coverage(retearn, liabilities, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d retearn/liab
def f16ls_f16_leverage_and_solvency_retliab_252d_slope_v058_signal(retearn, liabilities, marketcap):
    base = _f16_solvency_coverage(retearn, liabilities, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ebitda/debt
def f16ls_f16_leverage_and_solvency_ebitdadebt_21d_slope_v059_signal(ebitda, debt, marketcap):
    base = _f16_solvency_coverage(ebitda, debt, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ebitda/debt
def f16ls_f16_leverage_and_solvency_ebitdadebt_252d_slope_v060_signal(ebitda, debt, marketcap):
    base = _f16_solvency_coverage(ebitda, debt, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ncfo/debt
def f16ls_f16_leverage_and_solvency_ncfodebt_252d_slope_v061_signal(ncfo, debt, marketcap):
    base = _f16_solvency_coverage(ncfo, debt, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d fcf/debt
def f16ls_f16_leverage_and_solvency_fcfdebt_252d_slope_v062_signal(fcf, debt, marketcap):
    base = _f16_solvency_coverage(fcf, debt, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d networth ratio
def f16ls_f16_leverage_and_solvency_networth_21d_slope_v063_signal(assets, liabilities, marketcap):
    nw = assets - liabilities
    base = _f16_solvency_coverage(nw, assets, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d networth ratio
def f16ls_f16_leverage_and_solvency_networth_252d_slope_v064_signal(assets, liabilities, marketcap):
    nw = assets - liabilities
    base = _f16_solvency_coverage(nw, assets, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d networth ratio
def f16ls_f16_leverage_and_solvency_networth_504d_slope_v065_signal(assets, liabilities, marketcap):
    nw = assets - liabilities
    base = _f16_solvency_coverage(nw, assets, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d net leverage
def f16ls_f16_leverage_and_solvency_netlev_21d_slope_v066_signal(debt, workingcapital, equity, marketcap):
    nl = debt - workingcapital
    base = _f16_leverage_ratio(nl, equity, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d net leverage
def f16ls_f16_leverage_and_solvency_netlev_252d_slope_v067_signal(debt, workingcapital, equity, marketcap):
    nl = debt - workingcapital
    base = _f16_leverage_ratio(nl, equity, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d net leverage
def f16ls_f16_leverage_and_solvency_netlev_504d_slope_v068_signal(debt, workingcapital, equity, marketcap):
    nl = debt - workingcapital
    base = _f16_leverage_ratio(nl, equity, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d net lev / ebitda
def f16ls_f16_leverage_and_solvency_netlevebitda_21d_slope_v069_signal(debt, workingcapital, ebitda, marketcap):
    nl = debt - workingcapital
    base = _f16_leverage_ratio(nl, ebitda, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d net lev / ebitda
def f16ls_f16_leverage_and_solvency_netlevebitda_252d_slope_v070_signal(debt, workingcapital, ebitda, marketcap):
    nl = debt - workingcapital
    base = _f16_leverage_ratio(nl, ebitda, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of intexp/revenue
def f16ls_f16_leverage_and_solvency_intexprev_21d_slope_v071_signal(intexp, revenue, marketcap):
    base = _f16_leverage_ratio(intexp, revenue, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d intexp/revenue
def f16ls_f16_leverage_and_solvency_intexprev_252d_slope_v072_signal(intexp, revenue, marketcap):
    base = _f16_leverage_ratio(intexp, revenue, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of intexp/ebitda
def f16ls_f16_leverage_and_solvency_intexpebitda_21d_slope_v073_signal(intexp, ebitda, marketcap):
    base = _f16_leverage_ratio(intexp, ebitda, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d intexp/ebitda
def f16ls_f16_leverage_and_solvency_intexpebitda_252d_slope_v074_signal(intexp, ebitda, marketcap):
    base = _f16_leverage_ratio(intexp, ebitda, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of D/E z-score 252d
def f16ls_f16_leverage_and_solvency_dez_252d_slope_v075_signal(debt, equity, marketcap):
    p = _f16_leverage_ratio(debt, equity, 21)
    base = _z(p, 252) * marketcap / 1e9
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/E z-score 504d
def f16ls_f16_leverage_and_solvency_dez_504d_slope_v076_signal(debt, equity, marketcap):
    p = _f16_leverage_ratio(debt, equity, 63)
    base = _z(p, 504) * marketcap / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/A z-score 252d
def f16ls_f16_leverage_and_solvency_daz_252d_slope_v077_signal(debt, assets, marketcap):
    p = _f16_leverage_ratio(debt, assets, 21)
    base = _z(p, 252) * marketcap / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of debt/ebitda z-score 252d
def f16ls_f16_leverage_and_solvency_debtebitdaz_252d_slope_v078_signal(debt, ebitda, marketcap):
    p = _f16_leverage_ratio(debt, ebitda, 21)
    base = _z(p, 252) * marketcap / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of intcov z-score 252d
def f16ls_f16_leverage_and_solvency_intcovz_252d_slope_v079_signal(ebitda, intexp, marketcap):
    p = _f16_solvency_coverage(ebitda, intexp, 21)
    base = _z(p, 252) * marketcap / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/E deviation 252d
def f16ls_f16_leverage_and_solvency_dedev_252d_slope_v080_signal(debt, equity, marketcap):
    p = _f16_leverage_ratio(debt, equity, 21)
    avg = _mean(p, 252)
    base = (p - avg) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/A deviation 504d
def f16ls_f16_leverage_and_solvency_dadev_504d_slope_v081_signal(debt, assets, marketcap):
    p = _f16_leverage_ratio(debt, assets, 21)
    avg = _mean(p, 504)
    base = (p - avg) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of debt/ebitda deviation
def f16ls_f16_leverage_and_solvency_debtebitdadev_252d_slope_v082_signal(debt, ebitda, marketcap):
    p = _f16_leverage_ratio(debt, ebitda, 21)
    avg = _mean(p, 252)
    base = (p - avg) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of intcov deviation
def f16ls_f16_leverage_and_solvency_intcovdev_252d_slope_v083_signal(ebitda, intexp, marketcap):
    p = _f16_solvency_coverage(ebitda, intexp, 21)
    avg = _mean(p, 252)
    base = (p - avg) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/E relative to 504d hi
def f16ls_f16_leverage_and_solvency_derelhi_504d_slope_v084_signal(debt, equity, marketcap):
    p = _f16_leverage_ratio(debt, equity, 63)
    hi = p.rolling(504, min_periods=126).max()
    base = (p / hi.replace(0, np.nan)) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/A relative to 504d hi
def f16ls_f16_leverage_and_solvency_darelhi_504d_slope_v085_signal(debt, assets, marketcap):
    p = _f16_leverage_ratio(debt, assets, 63)
    hi = p.rolling(504, min_periods=126).max()
    base = (p / hi.replace(0, np.nan)) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of debt/ebitda relative to 504d hi
def f16ls_f16_leverage_and_solvency_debtebitdarelhi_504d_slope_v086_signal(debt, ebitda, marketcap):
    p = _f16_leverage_ratio(debt, ebitda, 63)
    hi = p.rolling(504, min_periods=126).max()
    base = (p / hi.replace(0, np.nan)) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/E position 504d
def f16ls_f16_leverage_and_solvency_depos_504d_slope_v087_signal(debt, equity, marketcap):
    p = _f16_leverage_ratio(debt, equity, 63)
    hi = p.rolling(504, min_periods=126).max()
    lo = p.rolling(504, min_periods=126).min()
    base = ((p - lo) / (hi - lo).replace(0, np.nan)) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of intcov position 504d
def f16ls_f16_leverage_and_solvency_intcovpos_504d_slope_v088_signal(ebitda, intexp, marketcap):
    p = _f16_solvency_coverage(ebitda, intexp, 63)
    hi = p.rolling(504, min_periods=126).max()
    lo = p.rolling(504, min_periods=126).min()
    base = ((p - lo) / (hi - lo).replace(0, np.nan)) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of high D/E count
def f16ls_f16_leverage_and_solvency_highde_count_252d_slope_v089_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 21)
    avg = _mean(base, 252)
    flag = (base > avg).astype(float)
    s = flag.rolling(252, min_periods=63).sum() * marketcap
    result = _slope_diff_norm(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of high debt/ebitda count
def f16ls_f16_leverage_and_solvency_highdebtebitda_count_252d_slope_v090_signal(debt, ebitda, marketcap):
    base = _f16_leverage_ratio(debt, ebitda, 21)
    avg = _mean(base, 252)
    flag = (base > avg).astype(float)
    s = flag.rolling(252, min_periods=63).sum() * marketcap
    result = _slope_diff_norm(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of low intcov count
def f16ls_f16_leverage_and_solvency_lowintcov_count_252d_slope_v091_signal(ebitda, intexp, marketcap):
    base = _f16_solvency_coverage(ebitda, intexp, 21)
    avg = _mean(base, 252)
    flag = (base < avg).astype(float)
    s = flag.rolling(252, min_periods=63).sum() * marketcap
    result = _slope_diff_norm(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of blended leverage 252d
def f16ls_f16_leverage_and_solvency_blendedlev_252d_slope_v092_signal(debt, equity, assets, liabilities, marketcap):
    a = _f16_leverage_ratio(debt, equity, 252)
    b = _f16_leverage_ratio(debt, assets, 252)
    c = _f16_leverage_ratio(liabilities, assets, 252)
    base = (a + b + c) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of blended solvency 252d
def f16ls_f16_leverage_and_solvency_blendedsolv_252d_slope_v093_signal(ebitda, intexp, currentratio, marketcap):
    a = _f16_solvency_coverage(ebitda, intexp, 252)
    b = _f16_solvency_coverage(currentratio * marketcap, marketcap, 252)
    base = (a + b) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of debt/cash flow proxy
def f16ls_f16_leverage_and_solvency_debtcfproxy_252d_slope_v094_signal(debt, ebitda, ncfo, marketcap):
    cf = ebitda + ncfo
    base = _f16_leverage_ratio(debt, cf, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of debt - retearn gap
def f16ls_f16_leverage_and_solvency_debtretgap_252d_slope_v095_signal(debt, retearn, equity, marketcap):
    gap = debt - retearn
    base = _f16_leverage_ratio(gap, equity, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of log D/E 21d
def f16ls_f16_leverage_and_solvency_logde_21d_slope_v096_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 21)
    s = np.log(base.replace(0, np.nan).abs() + 1.0) * marketcap
    result = _slope_diff_norm(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of log D/E 252d
def f16ls_f16_leverage_and_solvency_logde_252d_slope_v097_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 252)
    s = np.log(base.replace(0, np.nan).abs() + 1.0) * marketcap
    result = _slope_diff_norm(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of log debt/ebitda 252d
def f16ls_f16_leverage_and_solvency_logdebtebitda_252d_slope_v098_signal(debt, ebitda, marketcap):
    base = _f16_leverage_ratio(debt, ebitda, 252)
    s = np.log(base.replace(0, np.nan).abs() + 1.0) * marketcap
    result = _slope_diff_norm(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of log intcov 252d
def f16ls_f16_leverage_and_solvency_logintcov_252d_slope_v099_signal(ebitda, intexp, marketcap):
    base = _f16_solvency_coverage(ebitda, intexp, 252)
    s = np.log(base.replace(0, np.nan).abs() + 1.0) * marketcap
    result = _slope_diff_norm(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of leverage stress comp
def f16ls_f16_leverage_and_solvency_levstress_252d_slope_v100_signal(debt, equity, ebitda, marketcap):
    a = _f16_leverage_ratio(debt, equity, 252)
    b = _f16_leverage_ratio(debt, ebitda, 252)
    base = (a * b) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of solvency strength comp
def f16ls_f16_leverage_and_solvency_solvstrength_252d_slope_v101_signal(ebitda, intexp, currentratio, marketcap):
    a = _f16_solvency_coverage(ebitda, intexp, 252)
    b = _f16_solvency_coverage(currentratio * marketcap, marketcap, 252)
    base = (a * b) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of D/E squared
def f16ls_f16_leverage_and_solvency_desq_21d_slope_v102_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 21)
    s = base * base.abs() * marketcap
    result = _slope_diff_norm(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/E squared 252d
def f16ls_f16_leverage_and_solvency_desq_252d_slope_v103_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 252)
    s = base * base.abs() * marketcap
    result = _slope_diff_norm(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of debt/ebitda squared
def f16ls_f16_leverage_and_solvency_debtebitdasq_252d_slope_v104_signal(debt, ebitda, marketcap):
    base = _f16_leverage_ratio(debt, ebitda, 252)
    s = base * base.abs() * marketcap
    result = _slope_diff_norm(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of D/E EMA
def f16ls_f16_leverage_and_solvency_de_ema_21d_slope_v105_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 21).ewm(span=21, adjust=False).mean() * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/E EMA 252d
def f16ls_f16_leverage_and_solvency_de_ema_252d_slope_v106_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 252).ewm(span=252, adjust=False).mean() * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/A EMA 252d
def f16ls_f16_leverage_and_solvency_da_ema_252d_slope_v107_signal(debt, assets, marketcap):
    base = _f16_leverage_ratio(debt, assets, 252).ewm(span=252, adjust=False).mean() * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of intcov EMA 252d
def f16ls_f16_leverage_and_solvency_intcov_ema_252d_slope_v108_signal(ebitda, intexp, marketcap):
    base = _f16_solvency_coverage(ebitda, intexp, 252).ewm(span=252, adjust=False).mean() * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of debt/ev
def f16ls_f16_leverage_and_solvency_debtev_21d_slope_v109_signal(debt, ev, marketcap):
    base = _f16_leverage_ratio(debt, ev, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of debt/ev 252d
def f16ls_f16_leverage_and_solvency_debtev_252d_slope_v110_signal(debt, ev, marketcap):
    base = _f16_leverage_ratio(debt, ev, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of debt/ev 504d
def f16ls_f16_leverage_and_solvency_debtev_504d_slope_v111_signal(debt, ev, marketcap):
    base = _f16_leverage_ratio(debt, ev, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/E recent vs trend
def f16ls_f16_leverage_and_solvency_de_recent_vs_trend_slope_v112_signal(debt, equity, marketcap):
    a = _f16_leverage_ratio(debt, equity, 63)
    b = _f16_leverage_ratio(debt, equity, 252)
    base = (a / b.replace(0, np.nan)) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of debt/ebitda recent vs trend
def f16ls_f16_leverage_and_solvency_debtebitda_recent_vs_trend_slope_v113_signal(debt, ebitda, marketcap):
    a = _f16_leverage_ratio(debt, ebitda, 63)
    b = _f16_leverage_ratio(debt, ebitda, 252)
    base = (a / b.replace(0, np.nan)) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of intcov recent vs trend
def f16ls_f16_leverage_and_solvency_intcov_recent_vs_trend_slope_v114_signal(ebitda, intexp, marketcap):
    a = _f16_solvency_coverage(ebitda, intexp, 63)
    b = _f16_solvency_coverage(ebitda, intexp, 252)
    base = (a / b.replace(0, np.nan)) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/E x grossmargin
def f16ls_f16_leverage_and_solvency_de_x_gm_252d_slope_v115_signal(debt, equity, gp, revenue, marketcap):
    lev = _f16_leverage_ratio(debt, equity, 252)
    gm = _f16_solvency_coverage(gp, revenue, 252)
    base = (lev * gm) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of debt/(ebitda - capex)
def f16ls_f16_leverage_and_solvency_debtfcfproxy_252d_slope_v116_signal(debt, ebitda, capex, marketcap):
    fcf_p = ebitda - capex
    base = _f16_leverage_ratio(debt, fcf_p, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of retearn/equity
def f16ls_f16_leverage_and_solvency_retequity_21d_slope_v117_signal(retearn, equity, marketcap):
    base = _f16_solvency_coverage(retearn, equity, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retearn/equity 252d
def f16ls_f16_leverage_and_solvency_retequity_252d_slope_v118_signal(retearn, equity, marketcap):
    base = _f16_solvency_coverage(retearn, equity, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retearn/equity 504d
def f16ls_f16_leverage_and_solvency_retequity_504d_slope_v119_signal(retearn, equity, marketcap):
    base = _f16_solvency_coverage(retearn, equity, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retearn/assets 252d
def f16ls_f16_leverage_and_solvency_retassets_252d_slope_v120_signal(retearn, assets, marketcap):
    base = _f16_solvency_coverage(retearn, assets, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of buffer mult
def f16ls_f16_leverage_and_solvency_buffermult_21d_slope_v121_signal(assets, debt, marketcap):
    buf = assets - debt
    base = _f16_solvency_coverage(buf, debt, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of buffer mult 252d
def f16ls_f16_leverage_and_solvency_buffermult_252d_slope_v122_signal(assets, debt, marketcap):
    buf = assets - debt
    base = _f16_solvency_coverage(buf, debt, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of pay ability
def f16ls_f16_leverage_and_solvency_payabil_21d_slope_v123_signal(workingcapital, retearn, debt, marketcap):
    pay = workingcapital + retearn
    base = _f16_solvency_coverage(pay, debt, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of pay ability 252d
def f16ls_f16_leverage_and_solvency_payabil_252d_slope_v124_signal(workingcapital, retearn, debt, marketcap):
    pay = workingcapital + retearn
    base = _f16_solvency_coverage(pay, debt, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of cash buffer 252d
def f16ls_f16_leverage_and_solvency_cashbuf_252d_slope_v125_signal(ebitda, ncfo, fcf, debt, marketcap):
    cb = ebitda + ncfo + fcf
    base = _f16_solvency_coverage(cb, debt, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of intexp/fcf
def f16ls_f16_leverage_and_solvency_intexpfcf_21d_slope_v126_signal(intexp, fcf, marketcap):
    base = _f16_leverage_ratio(intexp, fcf, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of intexp/fcf 252d
def f16ls_f16_leverage_and_solvency_intexpfcf_252d_slope_v127_signal(intexp, fcf, marketcap):
    base = _f16_leverage_ratio(intexp, fcf, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of intexp/opinc
def f16ls_f16_leverage_and_solvency_intexpopinc_21d_slope_v128_signal(intexp, opinc, marketcap):
    base = _f16_leverage_ratio(intexp, opinc, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of intexp/opinc 252d
def f16ls_f16_leverage_and_solvency_intexpopinc_252d_slope_v129_signal(intexp, opinc, marketcap):
    base = _f16_leverage_ratio(intexp, opinc, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of intexp/netinc 252d
def f16ls_f16_leverage_and_solvency_intexpni_252d_slope_v130_signal(intexp, netinc, marketcap):
    base = _f16_leverage_ratio(intexp, netinc, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex/debt
def f16ls_f16_leverage_and_solvency_capexdebt_21d_slope_v131_signal(capex, debt, marketcap):
    base = _f16_leverage_ratio(capex, debt, 21) * marketcap
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex/debt 252d
def f16ls_f16_leverage_and_solvency_capexdebt_252d_slope_v132_signal(capex, debt, marketcap):
    base = _f16_leverage_ratio(capex, debt, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex/equity 252d
def f16ls_f16_leverage_and_solvency_capexequity_252d_slope_v133_signal(capex, equity, marketcap):
    base = _f16_leverage_ratio(capex, equity, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of intexp/liab 252d
def f16ls_f16_leverage_and_solvency_intexpliab_252d_slope_v134_signal(intexp, liabilities, marketcap):
    base = _f16_leverage_ratio(intexp, liabilities, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of intexp/debt 504d
def f16ls_f16_leverage_and_solvency_intexpdebt_504d_slope_v135_signal(intexp, debt, marketcap):
    base = _f16_leverage_ratio(intexp, debt, 504) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of full obligations / equity 252d
def f16ls_f16_leverage_and_solvency_fullob_eq_252d_slope_v136_signal(debt, liabilities, equity, marketcap):
    fl = debt + liabilities
    base = _f16_leverage_ratio(fl, equity, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of full obligations / assets 252d
def f16ls_f16_leverage_and_solvency_fullob_a_252d_slope_v137_signal(debt, liabilities, assets, marketcap):
    fl = debt + liabilities
    base = _f16_leverage_ratio(fl, assets, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of full obligations / ebitda 252d
def f16ls_f16_leverage_and_solvency_fullob_ebitda_252d_slope_v138_signal(debt, liabilities, ebitda, marketcap):
    fl = debt + liabilities
    base = _f16_leverage_ratio(fl, ebitda, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of distress comp 504d
def f16ls_f16_leverage_and_solvency_distresscomp_504d_slope_v139_signal(debt, equity, ebitda, intexp, marketcap):
    a = _f16_leverage_ratio(debt, equity, 504)
    b = _f16_leverage_ratio(debt, ebitda, 504)
    c = _f16_solvency_coverage(intexp, ebitda, 504)
    base = (a * b * c) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of health comp 252d
def f16ls_f16_leverage_and_solvency_healthcomp_252d_slope_v140_signal(debt, equity, ebitda, intexp, currentratio, marketcap):
    a = _f16_leverage_ratio(debt, equity, 252).replace(0, np.nan)
    b = _f16_solvency_coverage(ebitda, intexp, 252)
    c = _f16_solvency_coverage(currentratio * marketcap, marketcap, 252)
    base = (1.0 / a + b + c) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of (debt + intexp - ncfo) stress
def f16ls_f16_leverage_and_solvency_oblig_stress_252d_slope_v141_signal(debt, intexp, ncfo, marketcap):
    s = debt + intexp - ncfo
    base = _f16_leverage_ratio(s, ncfo, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of intexp / (ncfo - capex) free cash interest burden
def f16ls_f16_leverage_and_solvency_intexp_freeable_252d_slope_v142_signal(intexp, ncfo, capex, marketcap):
    fa = ncfo - capex
    base = _f16_leverage_ratio(intexp, fa, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of (assets - debt - liabilities)/equity
def f16ls_f16_leverage_and_solvency_solvbuffer_252d_slope_v143_signal(assets, debt, liabilities, equity, marketcap):
    sb = assets - debt - liabilities
    base = _f16_solvency_coverage(sb, equity, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of (currentratio * intcov) composite
def f16ls_f16_leverage_and_solvency_cr_x_intcov_252d_slope_v144_signal(currentratio, ebitda, intexp, marketcap):
    a = _f16_solvency_coverage(currentratio * marketcap, marketcap, 252)
    b = _f16_solvency_coverage(ebitda, intexp, 252)
    base = (a * b) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of (D/E + L/A) stress
def f16ls_f16_leverage_and_solvency_de_la_252d_slope_v145_signal(debt, equity, liabilities, assets, marketcap):
    a = _f16_leverage_ratio(debt, equity, 252)
    b = _f16_leverage_ratio(liabilities, assets, 252)
    base = (a + b) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of (debt/revenue + debt/ebitda)
def f16ls_f16_leverage_and_solvency_debtmult_252d_slope_v146_signal(debt, revenue, ebitda, marketcap):
    a = _f16_leverage_ratio(debt, revenue, 252)
    b = _f16_leverage_ratio(debt, ebitda, 252)
    base = (a + b) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of (intcov + ncfo/intexp)
def f16ls_f16_leverage_and_solvency_intcov_blend_252d_slope_v147_signal(ebitda, intexp, ncfo, marketcap):
    a = _f16_solvency_coverage(ebitda, intexp, 252)
    b = _f16_solvency_coverage(ncfo, intexp, 252)
    base = (a + b) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of (eq/assets * intcov)
def f16ls_f16_leverage_and_solvency_eqa_x_intcov_252d_slope_v148_signal(equity, assets, ebitda, intexp, marketcap):
    a = _f16_solvency_coverage(equity, assets, 252)
    b = _f16_solvency_coverage(ebitda, intexp, 252)
    base = (a * b) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of (debt/(ebitda + workingcapital)) stress
def f16ls_f16_leverage_and_solvency_debt_ebitdawc_252d_slope_v149_signal(debt, ebitda, workingcapital, marketcap):
    denom = ebitda + workingcapital
    base = _f16_leverage_ratio(debt, denom, 252) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of full leverage composite (D/E + D/A + L/E + debt/ebitda)
def f16ls_f16_leverage_and_solvency_fullcomp_252d_slope_v150_signal(debt, equity, assets, liabilities, ebitda, marketcap):
    a = _f16_leverage_ratio(debt, equity, 252)
    b = _f16_leverage_ratio(debt, assets, 252)
    c = _f16_leverage_ratio(liabilities, equity, 252)
    d = _f16_leverage_ratio(debt, ebitda, 252)
    base = (a + b + c + d) * marketcap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f16ls_f16_leverage_and_solvency_de_21d_slope_v001_signal,
    f16ls_f16_leverage_and_solvency_de_21d_slope_v002_signal,
    f16ls_f16_leverage_and_solvency_de_63d_slope_v003_signal,
    f16ls_f16_leverage_and_solvency_de_63d_slope_v004_signal,
    f16ls_f16_leverage_and_solvency_de_126d_slope_v005_signal,
    f16ls_f16_leverage_and_solvency_de_126d_slope_v006_signal,
    f16ls_f16_leverage_and_solvency_de_252d_slope_v007_signal,
    f16ls_f16_leverage_and_solvency_de_252d_slope_v008_signal,
    f16ls_f16_leverage_and_solvency_de_504d_slope_v009_signal,
    f16ls_f16_leverage_and_solvency_de_504d_slope_v010_signal,
    f16ls_f16_leverage_and_solvency_da_21d_slope_v011_signal,
    f16ls_f16_leverage_and_solvency_da_21d_slope_v012_signal,
    f16ls_f16_leverage_and_solvency_da_63d_slope_v013_signal,
    f16ls_f16_leverage_and_solvency_da_252d_slope_v014_signal,
    f16ls_f16_leverage_and_solvency_da_504d_slope_v015_signal,
    f16ls_f16_leverage_and_solvency_la_21d_slope_v016_signal,
    f16ls_f16_leverage_and_solvency_la_252d_slope_v017_signal,
    f16ls_f16_leverage_and_solvency_la_504d_slope_v018_signal,
    f16ls_f16_leverage_and_solvency_le_21d_slope_v019_signal,
    f16ls_f16_leverage_and_solvency_le_252d_slope_v020_signal,
    f16ls_f16_leverage_and_solvency_le_504d_slope_v021_signal,
    f16ls_f16_leverage_and_solvency_debtebitda_21d_slope_v022_signal,
    f16ls_f16_leverage_and_solvency_debtebitda_63d_slope_v023_signal,
    f16ls_f16_leverage_and_solvency_debtebitda_252d_slope_v024_signal,
    f16ls_f16_leverage_and_solvency_debtebitda_504d_slope_v025_signal,
    f16ls_f16_leverage_and_solvency_debtfcf_21d_slope_v026_signal,
    f16ls_f16_leverage_and_solvency_debtfcf_252d_slope_v027_signal,
    f16ls_f16_leverage_and_solvency_debtfcf_504d_slope_v028_signal,
    f16ls_f16_leverage_and_solvency_debtncfo_21d_slope_v029_signal,
    f16ls_f16_leverage_and_solvency_debtncfo_252d_slope_v030_signal,
    f16ls_f16_leverage_and_solvency_debtopinc_21d_slope_v031_signal,
    f16ls_f16_leverage_and_solvency_debtopinc_252d_slope_v032_signal,
    f16ls_f16_leverage_and_solvency_debtrev_21d_slope_v033_signal,
    f16ls_f16_leverage_and_solvency_debtrev_252d_slope_v034_signal,
    f16ls_f16_leverage_and_solvency_debtrev_504d_slope_v035_signal,
    f16ls_f16_leverage_and_solvency_intcov_21d_slope_v036_signal,
    f16ls_f16_leverage_and_solvency_intcov_63d_slope_v037_signal,
    f16ls_f16_leverage_and_solvency_intcov_252d_slope_v038_signal,
    f16ls_f16_leverage_and_solvency_intcov_504d_slope_v039_signal,
    f16ls_f16_leverage_and_solvency_intcovop_252d_slope_v040_signal,
    f16ls_f16_leverage_and_solvency_intcovncfo_252d_slope_v041_signal,
    f16ls_f16_leverage_and_solvency_intcovfcf_252d_slope_v042_signal,
    f16ls_f16_leverage_and_solvency_intcovrue_252d_slope_v043_signal,
    f16ls_f16_leverage_and_solvency_currentratio_21d_slope_v044_signal,
    f16ls_f16_leverage_and_solvency_currentratio_252d_slope_v045_signal,
    f16ls_f16_leverage_and_solvency_currentratio_504d_slope_v046_signal,
    f16ls_f16_leverage_and_solvency_wcliab_21d_slope_v047_signal,
    f16ls_f16_leverage_and_solvency_wcliab_252d_slope_v048_signal,
    f16ls_f16_leverage_and_solvency_wcdebt_21d_slope_v049_signal,
    f16ls_f16_leverage_and_solvency_wcdebt_252d_slope_v050_signal,
    f16ls_f16_leverage_and_solvency_eqassets_21d_slope_v051_signal,
    f16ls_f16_leverage_and_solvency_eqassets_252d_slope_v052_signal,
    f16ls_f16_leverage_and_solvency_eqassets_504d_slope_v053_signal,
    f16ls_f16_leverage_and_solvency_retdebt_21d_slope_v054_signal,
    f16ls_f16_leverage_and_solvency_retdebt_252d_slope_v055_signal,
    f16ls_f16_leverage_and_solvency_retdebt_504d_slope_v056_signal,
    f16ls_f16_leverage_and_solvency_retliab_21d_slope_v057_signal,
    f16ls_f16_leverage_and_solvency_retliab_252d_slope_v058_signal,
    f16ls_f16_leverage_and_solvency_ebitdadebt_21d_slope_v059_signal,
    f16ls_f16_leverage_and_solvency_ebitdadebt_252d_slope_v060_signal,
    f16ls_f16_leverage_and_solvency_ncfodebt_252d_slope_v061_signal,
    f16ls_f16_leverage_and_solvency_fcfdebt_252d_slope_v062_signal,
    f16ls_f16_leverage_and_solvency_networth_21d_slope_v063_signal,
    f16ls_f16_leverage_and_solvency_networth_252d_slope_v064_signal,
    f16ls_f16_leverage_and_solvency_networth_504d_slope_v065_signal,
    f16ls_f16_leverage_and_solvency_netlev_21d_slope_v066_signal,
    f16ls_f16_leverage_and_solvency_netlev_252d_slope_v067_signal,
    f16ls_f16_leverage_and_solvency_netlev_504d_slope_v068_signal,
    f16ls_f16_leverage_and_solvency_netlevebitda_21d_slope_v069_signal,
    f16ls_f16_leverage_and_solvency_netlevebitda_252d_slope_v070_signal,
    f16ls_f16_leverage_and_solvency_intexprev_21d_slope_v071_signal,
    f16ls_f16_leverage_and_solvency_intexprev_252d_slope_v072_signal,
    f16ls_f16_leverage_and_solvency_intexpebitda_21d_slope_v073_signal,
    f16ls_f16_leverage_and_solvency_intexpebitda_252d_slope_v074_signal,
    f16ls_f16_leverage_and_solvency_dez_252d_slope_v075_signal,
    f16ls_f16_leverage_and_solvency_dez_504d_slope_v076_signal,
    f16ls_f16_leverage_and_solvency_daz_252d_slope_v077_signal,
    f16ls_f16_leverage_and_solvency_debtebitdaz_252d_slope_v078_signal,
    f16ls_f16_leverage_and_solvency_intcovz_252d_slope_v079_signal,
    f16ls_f16_leverage_and_solvency_dedev_252d_slope_v080_signal,
    f16ls_f16_leverage_and_solvency_dadev_504d_slope_v081_signal,
    f16ls_f16_leverage_and_solvency_debtebitdadev_252d_slope_v082_signal,
    f16ls_f16_leverage_and_solvency_intcovdev_252d_slope_v083_signal,
    f16ls_f16_leverage_and_solvency_derelhi_504d_slope_v084_signal,
    f16ls_f16_leverage_and_solvency_darelhi_504d_slope_v085_signal,
    f16ls_f16_leverage_and_solvency_debtebitdarelhi_504d_slope_v086_signal,
    f16ls_f16_leverage_and_solvency_depos_504d_slope_v087_signal,
    f16ls_f16_leverage_and_solvency_intcovpos_504d_slope_v088_signal,
    f16ls_f16_leverage_and_solvency_highde_count_252d_slope_v089_signal,
    f16ls_f16_leverage_and_solvency_highdebtebitda_count_252d_slope_v090_signal,
    f16ls_f16_leverage_and_solvency_lowintcov_count_252d_slope_v091_signal,
    f16ls_f16_leverage_and_solvency_blendedlev_252d_slope_v092_signal,
    f16ls_f16_leverage_and_solvency_blendedsolv_252d_slope_v093_signal,
    f16ls_f16_leverage_and_solvency_debtcfproxy_252d_slope_v094_signal,
    f16ls_f16_leverage_and_solvency_debtretgap_252d_slope_v095_signal,
    f16ls_f16_leverage_and_solvency_logde_21d_slope_v096_signal,
    f16ls_f16_leverage_and_solvency_logde_252d_slope_v097_signal,
    f16ls_f16_leverage_and_solvency_logdebtebitda_252d_slope_v098_signal,
    f16ls_f16_leverage_and_solvency_logintcov_252d_slope_v099_signal,
    f16ls_f16_leverage_and_solvency_levstress_252d_slope_v100_signal,
    f16ls_f16_leverage_and_solvency_solvstrength_252d_slope_v101_signal,
    f16ls_f16_leverage_and_solvency_desq_21d_slope_v102_signal,
    f16ls_f16_leverage_and_solvency_desq_252d_slope_v103_signal,
    f16ls_f16_leverage_and_solvency_debtebitdasq_252d_slope_v104_signal,
    f16ls_f16_leverage_and_solvency_de_ema_21d_slope_v105_signal,
    f16ls_f16_leverage_and_solvency_de_ema_252d_slope_v106_signal,
    f16ls_f16_leverage_and_solvency_da_ema_252d_slope_v107_signal,
    f16ls_f16_leverage_and_solvency_intcov_ema_252d_slope_v108_signal,
    f16ls_f16_leverage_and_solvency_debtev_21d_slope_v109_signal,
    f16ls_f16_leverage_and_solvency_debtev_252d_slope_v110_signal,
    f16ls_f16_leverage_and_solvency_debtev_504d_slope_v111_signal,
    f16ls_f16_leverage_and_solvency_de_recent_vs_trend_slope_v112_signal,
    f16ls_f16_leverage_and_solvency_debtebitda_recent_vs_trend_slope_v113_signal,
    f16ls_f16_leverage_and_solvency_intcov_recent_vs_trend_slope_v114_signal,
    f16ls_f16_leverage_and_solvency_de_x_gm_252d_slope_v115_signal,
    f16ls_f16_leverage_and_solvency_debtfcfproxy_252d_slope_v116_signal,
    f16ls_f16_leverage_and_solvency_retequity_21d_slope_v117_signal,
    f16ls_f16_leverage_and_solvency_retequity_252d_slope_v118_signal,
    f16ls_f16_leverage_and_solvency_retequity_504d_slope_v119_signal,
    f16ls_f16_leverage_and_solvency_retassets_252d_slope_v120_signal,
    f16ls_f16_leverage_and_solvency_buffermult_21d_slope_v121_signal,
    f16ls_f16_leverage_and_solvency_buffermult_252d_slope_v122_signal,
    f16ls_f16_leverage_and_solvency_payabil_21d_slope_v123_signal,
    f16ls_f16_leverage_and_solvency_payabil_252d_slope_v124_signal,
    f16ls_f16_leverage_and_solvency_cashbuf_252d_slope_v125_signal,
    f16ls_f16_leverage_and_solvency_intexpfcf_21d_slope_v126_signal,
    f16ls_f16_leverage_and_solvency_intexpfcf_252d_slope_v127_signal,
    f16ls_f16_leverage_and_solvency_intexpopinc_21d_slope_v128_signal,
    f16ls_f16_leverage_and_solvency_intexpopinc_252d_slope_v129_signal,
    f16ls_f16_leverage_and_solvency_intexpni_252d_slope_v130_signal,
    f16ls_f16_leverage_and_solvency_capexdebt_21d_slope_v131_signal,
    f16ls_f16_leverage_and_solvency_capexdebt_252d_slope_v132_signal,
    f16ls_f16_leverage_and_solvency_capexequity_252d_slope_v133_signal,
    f16ls_f16_leverage_and_solvency_intexpliab_252d_slope_v134_signal,
    f16ls_f16_leverage_and_solvency_intexpdebt_504d_slope_v135_signal,
    f16ls_f16_leverage_and_solvency_fullob_eq_252d_slope_v136_signal,
    f16ls_f16_leverage_and_solvency_fullob_a_252d_slope_v137_signal,
    f16ls_f16_leverage_and_solvency_fullob_ebitda_252d_slope_v138_signal,
    f16ls_f16_leverage_and_solvency_distresscomp_504d_slope_v139_signal,
    f16ls_f16_leverage_and_solvency_healthcomp_252d_slope_v140_signal,
    f16ls_f16_leverage_and_solvency_oblig_stress_252d_slope_v141_signal,
    f16ls_f16_leverage_and_solvency_intexp_freeable_252d_slope_v142_signal,
    f16ls_f16_leverage_and_solvency_solvbuffer_252d_slope_v143_signal,
    f16ls_f16_leverage_and_solvency_cr_x_intcov_252d_slope_v144_signal,
    f16ls_f16_leverage_and_solvency_de_la_252d_slope_v145_signal,
    f16ls_f16_leverage_and_solvency_debtmult_252d_slope_v146_signal,
    f16ls_f16_leverage_and_solvency_intcov_blend_252d_slope_v147_signal,
    f16ls_f16_leverage_and_solvency_eqa_x_intcov_252d_slope_v148_signal,
    f16ls_f16_leverage_and_solvency_debt_ebitdawc_252d_slope_v149_signal,
    f16ls_f16_leverage_and_solvency_fullcomp_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F16_LEVERAGE_AND_SOLVENCY_REGISTRY_SLOPE = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
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
    eps = pd.Series(1.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="eps")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    gp = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="gp")
    workingcapital = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.006, n))), name="workingcapital")
    currentratio = pd.Series(1.8 * np.exp(np.cumsum(np.random.normal(0.0, 0.003, n))), name="currentratio")
    intexp = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.004, n))), name="intexp")
    liabilities = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.004, n))), name="liabilities")
    retearn = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="retearn")
    marketcap = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.015, n))), name="marketcap")
    ev = marketcap + debt - 0.3 * marketcap
    ev = pd.Series(ev.values, name="ev")
    evebit = ev / opinc.replace(0, np.nan)
    evebit = pd.Series(evebit.values, name="evebit")
    evebitda = ev / ebitda.replace(0, np.nan)
    evebitda = pd.Series(evebitda.values, name="evebitda")
    pe = marketcap / netinc.replace(0, np.nan)
    pe = pd.Series(pe.values, name="pe")
    pb = marketcap / equity.replace(0, np.nan)
    pb = pd.Series(pb.values, name="pb")
    ps = marketcap / revenue.replace(0, np.nan)
    ps = pd.Series(ps.values, name="ps")
    cols = {"closeadj": closeadj, "revenue": revenue, "netinc": netinc, "fcf": fcf, "ncfo": ncfo,
            "equity": equity, "debt": debt, "assets": assets, "ebitda": ebitda, "capex": capex,
            "eps": eps, "sharesbas": sharesbas, "opinc": opinc, "gp": gp, "workingcapital": workingcapital,
            "currentratio": currentratio, "intexp": intexp, "liabilities": liabilities, "retearn": retearn,
            "marketcap": marketcap, "ev": ev, "evebit": evebit, "evebitda": evebitda,
            "pe": pe, "pb": pb, "ps": ps}
    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f16_leverage", "_f16_solvency")
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
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f16_leverage_and_solvency_2nd_derivatives_001_150_claude: {n_features} features pass")
