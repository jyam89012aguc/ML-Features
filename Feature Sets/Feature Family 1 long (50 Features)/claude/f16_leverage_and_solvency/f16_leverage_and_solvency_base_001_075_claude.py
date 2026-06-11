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


# ===== folder domain primitives =====
def _f16_leverage_ratio(debt, denom, w):
    d = _mean(debt, w)
    e = _mean(denom, w)
    return d / e.replace(0, np.nan).abs()


def _f16_solvency_coverage(numerator, expense, w):
    n = _mean(numerator, w)
    e = _mean(expense, w)
    return n / e.replace(0, np.nan).abs()


# 21d debt / equity leverage
def f16ls_f16_leverage_and_solvency_de_21d_base_v001_signal(debt, equity, marketcap):
    result = _f16_leverage_ratio(debt, equity, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt / equity leverage
def f16ls_f16_leverage_and_solvency_de_63d_base_v002_signal(debt, equity, marketcap):
    result = _f16_leverage_ratio(debt, equity, 63) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 126d debt / equity leverage
def f16ls_f16_leverage_and_solvency_de_126d_base_v003_signal(debt, equity, marketcap):
    result = _f16_leverage_ratio(debt, equity, 126) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt / equity leverage
def f16ls_f16_leverage_and_solvency_de_252d_base_v004_signal(debt, equity, marketcap):
    result = _f16_leverage_ratio(debt, equity, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d debt / equity leverage
def f16ls_f16_leverage_and_solvency_de_504d_base_v005_signal(debt, equity, marketcap):
    result = _f16_leverage_ratio(debt, equity, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt / assets leverage
def f16ls_f16_leverage_and_solvency_da_21d_base_v006_signal(debt, assets, marketcap):
    result = _f16_leverage_ratio(debt, assets, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt / assets leverage
def f16ls_f16_leverage_and_solvency_da_63d_base_v007_signal(debt, assets, marketcap):
    result = _f16_leverage_ratio(debt, assets, 63) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt / assets leverage
def f16ls_f16_leverage_and_solvency_da_252d_base_v008_signal(debt, assets, marketcap):
    result = _f16_leverage_ratio(debt, assets, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d debt / assets leverage
def f16ls_f16_leverage_and_solvency_da_504d_base_v009_signal(debt, assets, marketcap):
    result = _f16_leverage_ratio(debt, assets, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d liabilities / assets leverage
def f16ls_f16_leverage_and_solvency_la_21d_base_v010_signal(liabilities, assets, marketcap):
    result = _f16_leverage_ratio(liabilities, assets, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d liabilities / assets
def f16ls_f16_leverage_and_solvency_la_252d_base_v011_signal(liabilities, assets, marketcap):
    result = _f16_leverage_ratio(liabilities, assets, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d liabilities / assets
def f16ls_f16_leverage_and_solvency_la_504d_base_v012_signal(liabilities, assets, marketcap):
    result = _f16_leverage_ratio(liabilities, assets, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d liabilities / equity
def f16ls_f16_leverage_and_solvency_le_21d_base_v013_signal(liabilities, equity, marketcap):
    result = _f16_leverage_ratio(liabilities, equity, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d liabilities / equity
def f16ls_f16_leverage_and_solvency_le_252d_base_v014_signal(liabilities, equity, marketcap):
    result = _f16_leverage_ratio(liabilities, equity, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d liabilities / equity
def f16ls_f16_leverage_and_solvency_le_504d_base_v015_signal(liabilities, equity, marketcap):
    result = _f16_leverage_ratio(liabilities, equity, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt / ebitda leverage
def f16ls_f16_leverage_and_solvency_debtebitda_21d_base_v016_signal(debt, ebitda, marketcap):
    result = _f16_leverage_ratio(debt, ebitda, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt / ebitda
def f16ls_f16_leverage_and_solvency_debtebitda_63d_base_v017_signal(debt, ebitda, marketcap):
    result = _f16_leverage_ratio(debt, ebitda, 63) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt / ebitda
def f16ls_f16_leverage_and_solvency_debtebitda_252d_base_v018_signal(debt, ebitda, marketcap):
    result = _f16_leverage_ratio(debt, ebitda, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d debt / ebitda
def f16ls_f16_leverage_and_solvency_debtebitda_504d_base_v019_signal(debt, ebitda, marketcap):
    result = _f16_leverage_ratio(debt, ebitda, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt / fcf
def f16ls_f16_leverage_and_solvency_debtfcf_21d_base_v020_signal(debt, fcf, marketcap):
    result = _f16_leverage_ratio(debt, fcf, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt / fcf
def f16ls_f16_leverage_and_solvency_debtfcf_252d_base_v021_signal(debt, fcf, marketcap):
    result = _f16_leverage_ratio(debt, fcf, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d debt / fcf
def f16ls_f16_leverage_and_solvency_debtfcf_504d_base_v022_signal(debt, fcf, marketcap):
    result = _f16_leverage_ratio(debt, fcf, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt / ncfo
def f16ls_f16_leverage_and_solvency_debtncfo_21d_base_v023_signal(debt, ncfo, marketcap):
    result = _f16_leverage_ratio(debt, ncfo, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt / ncfo
def f16ls_f16_leverage_and_solvency_debtncfo_252d_base_v024_signal(debt, ncfo, marketcap):
    result = _f16_leverage_ratio(debt, ncfo, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt / opinc
def f16ls_f16_leverage_and_solvency_debtopinc_21d_base_v025_signal(debt, opinc, marketcap):
    result = _f16_leverage_ratio(debt, opinc, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt / opinc
def f16ls_f16_leverage_and_solvency_debtopinc_252d_base_v026_signal(debt, opinc, marketcap):
    result = _f16_leverage_ratio(debt, opinc, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt / revenue
def f16ls_f16_leverage_and_solvency_debtrev_21d_base_v027_signal(debt, revenue, marketcap):
    result = _f16_leverage_ratio(debt, revenue, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt / revenue
def f16ls_f16_leverage_and_solvency_debtrev_252d_base_v028_signal(debt, revenue, marketcap):
    result = _f16_leverage_ratio(debt, revenue, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d debt / revenue
def f16ls_f16_leverage_and_solvency_debtrev_504d_base_v029_signal(debt, revenue, marketcap):
    result = _f16_leverage_ratio(debt, revenue, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ebitda / intexp coverage (interest coverage)
def f16ls_f16_leverage_and_solvency_intcov_21d_base_v030_signal(ebitda, intexp, marketcap):
    result = _f16_solvency_coverage(ebitda, intexp, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ebitda / intexp coverage
def f16ls_f16_leverage_and_solvency_intcov_63d_base_v031_signal(ebitda, intexp, marketcap):
    result = _f16_solvency_coverage(ebitda, intexp, 63) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda / intexp coverage
def f16ls_f16_leverage_and_solvency_intcov_252d_base_v032_signal(ebitda, intexp, marketcap):
    result = _f16_solvency_coverage(ebitda, intexp, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ebitda / intexp coverage
def f16ls_f16_leverage_and_solvency_intcov_504d_base_v033_signal(ebitda, intexp, marketcap):
    result = _f16_solvency_coverage(ebitda, intexp, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d opinc / intexp interest coverage
def f16ls_f16_leverage_and_solvency_intcovop_21d_base_v034_signal(opinc, intexp, marketcap):
    result = _f16_solvency_coverage(opinc, intexp, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d opinc / intexp
def f16ls_f16_leverage_and_solvency_intcovop_252d_base_v035_signal(opinc, intexp, marketcap):
    result = _f16_solvency_coverage(opinc, intexp, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncfo / intexp coverage
def f16ls_f16_leverage_and_solvency_intcovncfo_21d_base_v036_signal(ncfo, intexp, marketcap):
    result = _f16_solvency_coverage(ncfo, intexp, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo / intexp
def f16ls_f16_leverage_and_solvency_intcovncfo_252d_base_v037_signal(ncfo, intexp, marketcap):
    result = _f16_solvency_coverage(ncfo, intexp, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fcf / intexp coverage
def f16ls_f16_leverage_and_solvency_intcovfcf_21d_base_v038_signal(fcf, intexp, marketcap):
    result = _f16_solvency_coverage(fcf, intexp, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf / intexp coverage
def f16ls_f16_leverage_and_solvency_intcovfcf_252d_base_v039_signal(fcf, intexp, marketcap):
    result = _f16_solvency_coverage(fcf, intexp, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ebitda - capex / intexp coverage (true cash interest coverage)
def f16ls_f16_leverage_and_solvency_intcovrue_21d_base_v040_signal(ebitda, capex, intexp, marketcap):
    num = ebitda - capex
    result = _f16_solvency_coverage(num, intexp, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda - capex / intexp
def f16ls_f16_leverage_and_solvency_intcovrue_252d_base_v041_signal(ebitda, capex, intexp, marketcap):
    num = ebitda - capex
    result = _f16_solvency_coverage(num, intexp, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d currentratio raw, x marketcap
def f16ls_f16_leverage_and_solvency_currentratio_21d_base_v042_signal(currentratio, marketcap):
    smoothed = _f16_solvency_coverage(currentratio * marketcap, marketcap, 21)
    result = smoothed * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d currentratio
def f16ls_f16_leverage_and_solvency_currentratio_63d_base_v043_signal(currentratio, marketcap):
    smoothed = _f16_solvency_coverage(currentratio * marketcap, marketcap, 63)
    result = smoothed * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d currentratio
def f16ls_f16_leverage_and_solvency_currentratio_252d_base_v044_signal(currentratio, marketcap):
    smoothed = _f16_solvency_coverage(currentratio * marketcap, marketcap, 252)
    result = smoothed * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d currentratio
def f16ls_f16_leverage_and_solvency_currentratio_504d_base_v045_signal(currentratio, marketcap):
    smoothed = _f16_solvency_coverage(currentratio * marketcap, marketcap, 504)
    result = smoothed * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d workingcapital / liabilities (solvency)
def f16ls_f16_leverage_and_solvency_wcliab_21d_base_v046_signal(workingcapital, liabilities, marketcap):
    result = _f16_solvency_coverage(workingcapital, liabilities, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d workingcapital / liabilities
def f16ls_f16_leverage_and_solvency_wcliab_252d_base_v047_signal(workingcapital, liabilities, marketcap):
    result = _f16_solvency_coverage(workingcapital, liabilities, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d workingcapital / debt
def f16ls_f16_leverage_and_solvency_wcdebt_21d_base_v048_signal(workingcapital, debt, marketcap):
    result = _f16_solvency_coverage(workingcapital, debt, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d workingcapital / debt
def f16ls_f16_leverage_and_solvency_wcdebt_252d_base_v049_signal(workingcapital, debt, marketcap):
    result = _f16_solvency_coverage(workingcapital, debt, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d equity / assets (financial cushion)
def f16ls_f16_leverage_and_solvency_eqassets_21d_base_v050_signal(equity, assets, marketcap):
    result = _f16_solvency_coverage(equity, assets, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d equity / assets
def f16ls_f16_leverage_and_solvency_eqassets_252d_base_v051_signal(equity, assets, marketcap):
    result = _f16_solvency_coverage(equity, assets, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d equity / assets
def f16ls_f16_leverage_and_solvency_eqassets_504d_base_v052_signal(equity, assets, marketcap):
    result = _f16_solvency_coverage(equity, assets, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retearn / debt (debt-paying retained earnings)
def f16ls_f16_leverage_and_solvency_retdebt_21d_base_v053_signal(retearn, debt, marketcap):
    result = _f16_solvency_coverage(retearn, debt, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retearn / debt
def f16ls_f16_leverage_and_solvency_retdebt_252d_base_v054_signal(retearn, debt, marketcap):
    result = _f16_solvency_coverage(retearn, debt, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d retearn / debt
def f16ls_f16_leverage_and_solvency_retdebt_504d_base_v055_signal(retearn, debt, marketcap):
    result = _f16_solvency_coverage(retearn, debt, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retearn / liabilities
def f16ls_f16_leverage_and_solvency_retliab_21d_base_v056_signal(retearn, liabilities, marketcap):
    result = _f16_solvency_coverage(retearn, liabilities, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retearn / liabilities
def f16ls_f16_leverage_and_solvency_retliab_252d_base_v057_signal(retearn, liabilities, marketcap):
    result = _f16_solvency_coverage(retearn, liabilities, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ebitda / debt (cash flow leverage inverse)
def f16ls_f16_leverage_and_solvency_ebitdadebt_21d_base_v058_signal(ebitda, debt, marketcap):
    result = _f16_solvency_coverage(ebitda, debt, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda / debt
def f16ls_f16_leverage_and_solvency_ebitdadebt_252d_base_v059_signal(ebitda, debt, marketcap):
    result = _f16_solvency_coverage(ebitda, debt, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncfo / debt
def f16ls_f16_leverage_and_solvency_ncfodebt_21d_base_v060_signal(ncfo, debt, marketcap):
    result = _f16_solvency_coverage(ncfo, debt, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo / debt
def f16ls_f16_leverage_and_solvency_ncfodebt_252d_base_v061_signal(ncfo, debt, marketcap):
    result = _f16_solvency_coverage(ncfo, debt, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fcf / debt
def f16ls_f16_leverage_and_solvency_fcfdebt_21d_base_v062_signal(fcf, debt, marketcap):
    result = _f16_solvency_coverage(fcf, debt, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf / debt
def f16ls_f16_leverage_and_solvency_fcfdebt_252d_base_v063_signal(fcf, debt, marketcap):
    result = _f16_solvency_coverage(fcf, debt, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d (assets - liabilities) net worth ratio (book leverage measure)
def f16ls_f16_leverage_and_solvency_networth_21d_base_v064_signal(assets, liabilities, marketcap):
    nw = assets - liabilities
    result = _f16_solvency_coverage(nw, assets, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d (assets - liabilities) / assets
def f16ls_f16_leverage_and_solvency_networth_252d_base_v065_signal(assets, liabilities, marketcap):
    nw = assets - liabilities
    result = _f16_solvency_coverage(nw, assets, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d (assets - liabilities) / assets
def f16ls_f16_leverage_and_solvency_networth_504d_base_v066_signal(assets, liabilities, marketcap):
    nw = assets - liabilities
    result = _f16_solvency_coverage(nw, assets, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d (debt - workingcapital) / equity (net leverage)
def f16ls_f16_leverage_and_solvency_netlev_21d_base_v067_signal(debt, workingcapital, equity, marketcap):
    nl = debt - workingcapital
    result = _f16_leverage_ratio(nl, equity, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d (debt - workingcapital) / equity
def f16ls_f16_leverage_and_solvency_netlev_252d_base_v068_signal(debt, workingcapital, equity, marketcap):
    nl = debt - workingcapital
    result = _f16_leverage_ratio(nl, equity, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d (debt - workingcapital) / equity
def f16ls_f16_leverage_and_solvency_netlev_504d_base_v069_signal(debt, workingcapital, equity, marketcap):
    nl = debt - workingcapital
    result = _f16_leverage_ratio(nl, equity, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d (debt - workingcapital) / ebitda
def f16ls_f16_leverage_and_solvency_netlevebitda_21d_base_v070_signal(debt, workingcapital, ebitda, marketcap):
    nl = debt - workingcapital
    result = _f16_leverage_ratio(nl, ebitda, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d (debt - workingcapital) / ebitda
def f16ls_f16_leverage_and_solvency_netlevebitda_252d_base_v071_signal(debt, workingcapital, ebitda, marketcap):
    nl = debt - workingcapital
    result = _f16_leverage_ratio(nl, ebitda, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d intexp / revenue (interest burden as fraction of sales)
def f16ls_f16_leverage_and_solvency_intexprev_21d_base_v072_signal(intexp, revenue, marketcap):
    result = _f16_leverage_ratio(intexp, revenue, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intexp / revenue
def f16ls_f16_leverage_and_solvency_intexprev_252d_base_v073_signal(intexp, revenue, marketcap):
    result = _f16_leverage_ratio(intexp, revenue, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d intexp / ebitda
def f16ls_f16_leverage_and_solvency_intexpebitda_21d_base_v074_signal(intexp, ebitda, marketcap):
    result = _f16_leverage_ratio(intexp, ebitda, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intexp / ebitda
def f16ls_f16_leverage_and_solvency_intexpebitda_252d_base_v075_signal(intexp, ebitda, marketcap):
    result = _f16_leverage_ratio(intexp, ebitda, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f16ls_f16_leverage_and_solvency_de_21d_base_v001_signal,
    f16ls_f16_leverage_and_solvency_de_63d_base_v002_signal,
    f16ls_f16_leverage_and_solvency_de_126d_base_v003_signal,
    f16ls_f16_leverage_and_solvency_de_252d_base_v004_signal,
    f16ls_f16_leverage_and_solvency_de_504d_base_v005_signal,
    f16ls_f16_leverage_and_solvency_da_21d_base_v006_signal,
    f16ls_f16_leverage_and_solvency_da_63d_base_v007_signal,
    f16ls_f16_leverage_and_solvency_da_252d_base_v008_signal,
    f16ls_f16_leverage_and_solvency_da_504d_base_v009_signal,
    f16ls_f16_leverage_and_solvency_la_21d_base_v010_signal,
    f16ls_f16_leverage_and_solvency_la_252d_base_v011_signal,
    f16ls_f16_leverage_and_solvency_la_504d_base_v012_signal,
    f16ls_f16_leverage_and_solvency_le_21d_base_v013_signal,
    f16ls_f16_leverage_and_solvency_le_252d_base_v014_signal,
    f16ls_f16_leverage_and_solvency_le_504d_base_v015_signal,
    f16ls_f16_leverage_and_solvency_debtebitda_21d_base_v016_signal,
    f16ls_f16_leverage_and_solvency_debtebitda_63d_base_v017_signal,
    f16ls_f16_leverage_and_solvency_debtebitda_252d_base_v018_signal,
    f16ls_f16_leverage_and_solvency_debtebitda_504d_base_v019_signal,
    f16ls_f16_leverage_and_solvency_debtfcf_21d_base_v020_signal,
    f16ls_f16_leverage_and_solvency_debtfcf_252d_base_v021_signal,
    f16ls_f16_leverage_and_solvency_debtfcf_504d_base_v022_signal,
    f16ls_f16_leverage_and_solvency_debtncfo_21d_base_v023_signal,
    f16ls_f16_leverage_and_solvency_debtncfo_252d_base_v024_signal,
    f16ls_f16_leverage_and_solvency_debtopinc_21d_base_v025_signal,
    f16ls_f16_leverage_and_solvency_debtopinc_252d_base_v026_signal,
    f16ls_f16_leverage_and_solvency_debtrev_21d_base_v027_signal,
    f16ls_f16_leverage_and_solvency_debtrev_252d_base_v028_signal,
    f16ls_f16_leverage_and_solvency_debtrev_504d_base_v029_signal,
    f16ls_f16_leverage_and_solvency_intcov_21d_base_v030_signal,
    f16ls_f16_leverage_and_solvency_intcov_63d_base_v031_signal,
    f16ls_f16_leverage_and_solvency_intcov_252d_base_v032_signal,
    f16ls_f16_leverage_and_solvency_intcov_504d_base_v033_signal,
    f16ls_f16_leverage_and_solvency_intcovop_21d_base_v034_signal,
    f16ls_f16_leverage_and_solvency_intcovop_252d_base_v035_signal,
    f16ls_f16_leverage_and_solvency_intcovncfo_21d_base_v036_signal,
    f16ls_f16_leverage_and_solvency_intcovncfo_252d_base_v037_signal,
    f16ls_f16_leverage_and_solvency_intcovfcf_21d_base_v038_signal,
    f16ls_f16_leverage_and_solvency_intcovfcf_252d_base_v039_signal,
    f16ls_f16_leverage_and_solvency_intcovrue_21d_base_v040_signal,
    f16ls_f16_leverage_and_solvency_intcovrue_252d_base_v041_signal,
    f16ls_f16_leverage_and_solvency_currentratio_21d_base_v042_signal,
    f16ls_f16_leverage_and_solvency_currentratio_63d_base_v043_signal,
    f16ls_f16_leverage_and_solvency_currentratio_252d_base_v044_signal,
    f16ls_f16_leverage_and_solvency_currentratio_504d_base_v045_signal,
    f16ls_f16_leverage_and_solvency_wcliab_21d_base_v046_signal,
    f16ls_f16_leverage_and_solvency_wcliab_252d_base_v047_signal,
    f16ls_f16_leverage_and_solvency_wcdebt_21d_base_v048_signal,
    f16ls_f16_leverage_and_solvency_wcdebt_252d_base_v049_signal,
    f16ls_f16_leverage_and_solvency_eqassets_21d_base_v050_signal,
    f16ls_f16_leverage_and_solvency_eqassets_252d_base_v051_signal,
    f16ls_f16_leverage_and_solvency_eqassets_504d_base_v052_signal,
    f16ls_f16_leverage_and_solvency_retdebt_21d_base_v053_signal,
    f16ls_f16_leverage_and_solvency_retdebt_252d_base_v054_signal,
    f16ls_f16_leverage_and_solvency_retdebt_504d_base_v055_signal,
    f16ls_f16_leverage_and_solvency_retliab_21d_base_v056_signal,
    f16ls_f16_leverage_and_solvency_retliab_252d_base_v057_signal,
    f16ls_f16_leverage_and_solvency_ebitdadebt_21d_base_v058_signal,
    f16ls_f16_leverage_and_solvency_ebitdadebt_252d_base_v059_signal,
    f16ls_f16_leverage_and_solvency_ncfodebt_21d_base_v060_signal,
    f16ls_f16_leverage_and_solvency_ncfodebt_252d_base_v061_signal,
    f16ls_f16_leverage_and_solvency_fcfdebt_21d_base_v062_signal,
    f16ls_f16_leverage_and_solvency_fcfdebt_252d_base_v063_signal,
    f16ls_f16_leverage_and_solvency_networth_21d_base_v064_signal,
    f16ls_f16_leverage_and_solvency_networth_252d_base_v065_signal,
    f16ls_f16_leverage_and_solvency_networth_504d_base_v066_signal,
    f16ls_f16_leverage_and_solvency_netlev_21d_base_v067_signal,
    f16ls_f16_leverage_and_solvency_netlev_252d_base_v068_signal,
    f16ls_f16_leverage_and_solvency_netlev_504d_base_v069_signal,
    f16ls_f16_leverage_and_solvency_netlevebitda_21d_base_v070_signal,
    f16ls_f16_leverage_and_solvency_netlevebitda_252d_base_v071_signal,
    f16ls_f16_leverage_and_solvency_intexprev_21d_base_v072_signal,
    f16ls_f16_leverage_and_solvency_intexprev_252d_base_v073_signal,
    f16ls_f16_leverage_and_solvency_intexpebitda_21d_base_v074_signal,
    f16ls_f16_leverage_and_solvency_intexpebitda_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F16_LEVERAGE_AND_SOLVENCY_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f16_leverage_and_solvency_base_001_075_claude: {n_features} features pass")
