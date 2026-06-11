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


# zscore of 21d D/E over 252d
def f16ls_f16_leverage_and_solvency_dez_252d_base_v076_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 21)
    result = _z(base, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 63d D/E over 504d
def f16ls_f16_leverage_and_solvency_dez_504d_base_v077_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 63)
    result = _z(base, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 21d D/A over 252d
def f16ls_f16_leverage_and_solvency_daz_252d_base_v078_signal(debt, assets, marketcap):
    base = _f16_leverage_ratio(debt, assets, 21)
    result = _z(base, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 63d D/A over 504d
def f16ls_f16_leverage_and_solvency_daz_504d_base_v079_signal(debt, assets, marketcap):
    base = _f16_leverage_ratio(debt, assets, 63)
    result = _z(base, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 21d debt/ebitda over 252d
def f16ls_f16_leverage_and_solvency_debtebitdaz_252d_base_v080_signal(debt, ebitda, marketcap):
    base = _f16_leverage_ratio(debt, ebitda, 21)
    result = _z(base, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 63d debt/ebitda over 504d
def f16ls_f16_leverage_and_solvency_debtebitdaz_504d_base_v081_signal(debt, ebitda, marketcap):
    base = _f16_leverage_ratio(debt, ebitda, 63)
    result = _z(base, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 21d intcov over 252d
def f16ls_f16_leverage_and_solvency_intcovz_252d_base_v082_signal(ebitda, intexp, marketcap):
    base = _f16_solvency_coverage(ebitda, intexp, 21)
    result = _z(base, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 63d intcov over 504d
def f16ls_f16_leverage_and_solvency_intcovz_504d_base_v083_signal(ebitda, intexp, marketcap):
    base = _f16_solvency_coverage(ebitda, intexp, 63)
    result = _z(base, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of 21d D/E
def f16ls_f16_leverage_and_solvency_destd_252d_base_v084_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 21)
    result = _std(base, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of 63d D/A
def f16ls_f16_leverage_and_solvency_dastd_504d_base_v085_signal(debt, assets, marketcap):
    base = _f16_leverage_ratio(debt, assets, 63)
    result = _std(base, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of 21d debt/ebitda
def f16ls_f16_leverage_and_solvency_debtebitdastd_252d_base_v086_signal(debt, ebitda, marketcap):
    base = _f16_leverage_ratio(debt, ebitda, 21)
    result = _std(base, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of high-leverage days where D/E > 252d mean
def f16ls_f16_leverage_and_solvency_highde_count_252d_base_v087_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 21)
    avg = _mean(base, 252)
    flag = (base > avg).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of high-debt-ebitda days
def f16ls_f16_leverage_and_solvency_highdebtebitda_count_252d_base_v088_signal(debt, ebitda, marketcap):
    base = _f16_leverage_ratio(debt, ebitda, 21)
    avg = _mean(base, 252)
    flag = (base > avg).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of low intcov days (weak coverage)
def f16ls_f16_leverage_and_solvency_lowintcov_count_252d_base_v089_signal(ebitda, intexp, marketcap):
    base = _f16_solvency_coverage(ebitda, intexp, 21)
    avg = _mean(base, 252)
    flag = (base < avg).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of low currentratio days
def f16ls_f16_leverage_and_solvency_lowcr_count_504d_base_v090_signal(currentratio, marketcap):
    smoothed = _f16_solvency_coverage(currentratio * marketcap, marketcap, 21)
    avg = _mean(smoothed, 504)
    flag = (smoothed < avg).astype(float)
    result = flag.rolling(504, min_periods=126).sum() * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# D/E - 252d mean (deviation), x marketcap
def f16ls_f16_leverage_and_solvency_dedev_252d_base_v091_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 21)
    avg = _mean(base, 252)
    result = (base - avg) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# D/A - 504d mean
def f16ls_f16_leverage_and_solvency_dadev_504d_base_v092_signal(debt, assets, marketcap):
    base = _f16_leverage_ratio(debt, assets, 21)
    avg = _mean(base, 504)
    result = (base - avg) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# debt/ebitda - 252d mean
def f16ls_f16_leverage_and_solvency_debtebitdadev_252d_base_v093_signal(debt, ebitda, marketcap):
    base = _f16_leverage_ratio(debt, ebitda, 21)
    avg = _mean(base, 252)
    result = (base - avg) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# intcov - 252d mean
def f16ls_f16_leverage_and_solvency_intcovdev_252d_base_v094_signal(ebitda, intexp, marketcap):
    base = _f16_solvency_coverage(ebitda, intexp, 21)
    avg = _mean(base, 252)
    result = (base - avg) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# D/E relative to 504d hi
def f16ls_f16_leverage_and_solvency_derelhi_504d_base_v095_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 63)
    hi = base.rolling(504, min_periods=126).max()
    result = (base / hi.replace(0, np.nan)) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# D/A relative to 504d hi
def f16ls_f16_leverage_and_solvency_darelhi_504d_base_v096_signal(debt, assets, marketcap):
    base = _f16_leverage_ratio(debt, assets, 63)
    hi = base.rolling(504, min_periods=126).max()
    result = (base / hi.replace(0, np.nan)) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# debt/ebitda relative to 504d hi
def f16ls_f16_leverage_and_solvency_debtebitdarelhi_504d_base_v097_signal(debt, ebitda, marketcap):
    base = _f16_leverage_ratio(debt, ebitda, 63)
    hi = base.rolling(504, min_periods=126).max()
    result = (base / hi.replace(0, np.nan)) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# D/E position in 504d range
def f16ls_f16_leverage_and_solvency_depos_504d_base_v098_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 63)
    hi = base.rolling(504, min_periods=126).max()
    lo = base.rolling(504, min_periods=126).min()
    pos = (base - lo) / (hi - lo).replace(0, np.nan)
    result = pos * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# D/A position in 504d range
def f16ls_f16_leverage_and_solvency_dapos_504d_base_v099_signal(debt, assets, marketcap):
    base = _f16_leverage_ratio(debt, assets, 63)
    hi = base.rolling(504, min_periods=126).max()
    lo = base.rolling(504, min_periods=126).min()
    pos = (base - lo) / (hi - lo).replace(0, np.nan)
    result = pos * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# intcov position in 504d range (high = strong coverage)
def f16ls_f16_leverage_and_solvency_intcovpos_504d_base_v100_signal(ebitda, intexp, marketcap):
    base = _f16_solvency_coverage(ebitda, intexp, 63)
    hi = base.rolling(504, min_periods=126).max()
    lo = base.rolling(504, min_periods=126).min()
    pos = (base - lo) / (hi - lo).replace(0, np.nan)
    result = pos * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# blended leverage: (D/E + D/A + L/A)
def f16ls_f16_leverage_and_solvency_blendedlev_252d_base_v101_signal(debt, equity, assets, liabilities, marketcap):
    a = _f16_leverage_ratio(debt, equity, 252)
    b = _f16_leverage_ratio(debt, assets, 252)
    c = _f16_leverage_ratio(liabilities, assets, 252)
    result = (a + b + c) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# blended solvency: (intcov + cr)
def f16ls_f16_leverage_and_solvency_blendedsolv_252d_base_v102_signal(ebitda, intexp, currentratio, marketcap):
    a = _f16_solvency_coverage(ebitda, intexp, 252)
    b = _f16_solvency_coverage(currentratio * marketcap, marketcap, 252)
    result = (a + b) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# debt/(ebitda + ncfo) coverage proxy
def f16ls_f16_leverage_and_solvency_debtcfproxy_252d_base_v103_signal(debt, ebitda, ncfo, marketcap):
    cf = ebitda + ncfo
    result = _f16_leverage_ratio(debt, cf, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# debt - retearn (impaired self-funding)
def f16ls_f16_leverage_and_solvency_debtretgap_252d_base_v104_signal(debt, retearn, equity, marketcap):
    gap = debt - retearn
    result = _f16_leverage_ratio(gap, equity, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log D/E x marketcap
def f16ls_f16_leverage_and_solvency_logde_21d_base_v105_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 21)
    result = np.log(base.replace(0, np.nan).abs() + 1.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log D/E x marketcap
def f16ls_f16_leverage_and_solvency_logde_252d_base_v106_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 252)
    result = np.log(base.replace(0, np.nan).abs() + 1.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log debt/ebitda
def f16ls_f16_leverage_and_solvency_logdebtebitda_252d_base_v107_signal(debt, ebitda, marketcap):
    base = _f16_leverage_ratio(debt, ebitda, 252)
    result = np.log(base.replace(0, np.nan).abs() + 1.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of intcov
def f16ls_f16_leverage_and_solvency_logintcov_252d_base_v108_signal(ebitda, intexp, marketcap):
    base = _f16_solvency_coverage(ebitda, intexp, 252)
    result = np.log(base.replace(0, np.nan).abs() + 1.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# composite leverage stress: D/E * debt/ebitda
def f16ls_f16_leverage_and_solvency_levstress_252d_base_v109_signal(debt, equity, ebitda, marketcap):
    a = _f16_leverage_ratio(debt, equity, 252)
    b = _f16_leverage_ratio(debt, ebitda, 252)
    result = (a * b) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# composite cover strength: intcov * currentratio
def f16ls_f16_leverage_and_solvency_solvstrength_252d_base_v110_signal(ebitda, intexp, currentratio, marketcap):
    a = _f16_solvency_coverage(ebitda, intexp, 252)
    b = _f16_solvency_coverage(currentratio * marketcap, marketcap, 252)
    result = (a * b) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d D/E squared
def f16ls_f16_leverage_and_solvency_desq_21d_base_v111_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 21)
    result = base * base.abs() * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d D/E squared
def f16ls_f16_leverage_and_solvency_desq_252d_base_v112_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 252)
    result = base * base.abs() * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt/ebitda squared
def f16ls_f16_leverage_and_solvency_debtebitdasq_252d_base_v113_signal(debt, ebitda, marketcap):
    base = _f16_leverage_ratio(debt, ebitda, 252)
    result = base * base.abs() * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d D/E EMA x marketcap
def f16ls_f16_leverage_and_solvency_de_ema_21d_base_v114_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 21).ewm(span=21, adjust=False).mean()
    result = base * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d D/E EMA x marketcap
def f16ls_f16_leverage_and_solvency_de_ema_252d_base_v115_signal(debt, equity, marketcap):
    base = _f16_leverage_ratio(debt, equity, 252).ewm(span=252, adjust=False).mean()
    result = base * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d D/A EMA x marketcap
def f16ls_f16_leverage_and_solvency_da_ema_21d_base_v116_signal(debt, assets, marketcap):
    base = _f16_leverage_ratio(debt, assets, 21).ewm(span=21, adjust=False).mean()
    result = base * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intcov EMA x marketcap
def f16ls_f16_leverage_and_solvency_intcov_ema_252d_base_v117_signal(ebitda, intexp, marketcap):
    base = _f16_solvency_coverage(ebitda, intexp, 252).ewm(span=252, adjust=False).mean()
    result = base * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ratio of debt to ev (debt as fraction of enterprise value)
def f16ls_f16_leverage_and_solvency_debtev_21d_base_v118_signal(debt, ev, marketcap):
    result = _f16_leverage_ratio(debt, ev, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt/ev
def f16ls_f16_leverage_and_solvency_debtev_252d_base_v119_signal(debt, ev, marketcap):
    result = _f16_leverage_ratio(debt, ev, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d debt/ev
def f16ls_f16_leverage_and_solvency_debtev_504d_base_v120_signal(debt, ev, marketcap):
    result = _f16_leverage_ratio(debt, ev, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ratio (D/E_recent / D/E_trend) - recent leverage shift
def f16ls_f16_leverage_and_solvency_de_recent_vs_trend_base_v121_signal(debt, equity, marketcap):
    a = _f16_leverage_ratio(debt, equity, 63)
    b = _f16_leverage_ratio(debt, equity, 252)
    result = (a / b.replace(0, np.nan)) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# debt/ebitda recent vs trend
def f16ls_f16_leverage_and_solvency_debtebitda_recent_vs_trend_base_v122_signal(debt, ebitda, marketcap):
    a = _f16_leverage_ratio(debt, ebitda, 63)
    b = _f16_leverage_ratio(debt, ebitda, 252)
    result = (a / b.replace(0, np.nan)) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# intcov recent vs trend
def f16ls_f16_leverage_and_solvency_intcov_recent_vs_trend_base_v123_signal(ebitda, intexp, marketcap):
    a = _f16_solvency_coverage(ebitda, intexp, 63)
    b = _f16_solvency_coverage(ebitda, intexp, 252)
    result = (a / b.replace(0, np.nan)) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# D/E adjusted by gross profitability (gross-leverage trade-off)
def f16ls_f16_leverage_and_solvency_de_x_grossmargin_252d_base_v124_signal(debt, equity, gp, revenue, marketcap):
    lev = _f16_leverage_ratio(debt, equity, 252)
    gm = _f16_solvency_coverage(gp, revenue, 252)
    result = (lev * gm) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# debt to (ebitda - capex) [free cash leverage]
def f16ls_f16_leverage_and_solvency_debtfcfproxy_252d_base_v125_signal(debt, ebitda, capex, marketcap):
    fcf_p = ebitda - capex
    result = _f16_leverage_ratio(debt, fcf_p, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retearn / equity (book accumulation rate)
def f16ls_f16_leverage_and_solvency_retequity_21d_base_v126_signal(retearn, equity, marketcap):
    result = _f16_solvency_coverage(retearn, equity, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retearn / equity
def f16ls_f16_leverage_and_solvency_retequity_252d_base_v127_signal(retearn, equity, marketcap):
    result = _f16_solvency_coverage(retearn, equity, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d retearn / equity
def f16ls_f16_leverage_and_solvency_retequity_504d_base_v128_signal(retearn, equity, marketcap):
    result = _f16_solvency_coverage(retearn, equity, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retearn / assets
def f16ls_f16_leverage_and_solvency_retassets_21d_base_v129_signal(retearn, assets, marketcap):
    result = _f16_solvency_coverage(retearn, assets, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retearn / assets
def f16ls_f16_leverage_and_solvency_retassets_252d_base_v130_signal(retearn, assets, marketcap):
    result = _f16_solvency_coverage(retearn, assets, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d (assets - debt) / debt - liquidity buffer multiple
def f16ls_f16_leverage_and_solvency_buffermult_21d_base_v131_signal(assets, debt, marketcap):
    buf = assets - debt
    result = _f16_solvency_coverage(buf, debt, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d (assets - debt) / debt
def f16ls_f16_leverage_and_solvency_buffermult_252d_base_v132_signal(assets, debt, marketcap):
    buf = assets - debt
    result = _f16_solvency_coverage(buf, debt, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d (workingcapital + retearn) / debt - paying ability
def f16ls_f16_leverage_and_solvency_payabil_21d_base_v133_signal(workingcapital, retearn, debt, marketcap):
    pay = workingcapital + retearn
    result = _f16_solvency_coverage(pay, debt, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d (workingcapital + retearn) / debt
def f16ls_f16_leverage_and_solvency_payabil_252d_base_v134_signal(workingcapital, retearn, debt, marketcap):
    pay = workingcapital + retearn
    result = _f16_solvency_coverage(pay, debt, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d (ebitda + ncfo + fcf) / debt - cash buffer to debt
def f16ls_f16_leverage_and_solvency_cashbuf_252d_base_v135_signal(ebitda, ncfo, fcf, debt, marketcap):
    cb = ebitda + ncfo + fcf
    result = _f16_solvency_coverage(cb, debt, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d intexp / fcf (interest as fraction of free cash)
def f16ls_f16_leverage_and_solvency_intexpfcf_21d_base_v136_signal(intexp, fcf, marketcap):
    result = _f16_leverage_ratio(intexp, fcf, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intexp / fcf
def f16ls_f16_leverage_and_solvency_intexpfcf_252d_base_v137_signal(intexp, fcf, marketcap):
    result = _f16_leverage_ratio(intexp, fcf, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d intexp / opinc
def f16ls_f16_leverage_and_solvency_intexpopinc_21d_base_v138_signal(intexp, opinc, marketcap):
    result = _f16_leverage_ratio(intexp, opinc, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intexp / opinc
def f16ls_f16_leverage_and_solvency_intexpopinc_252d_base_v139_signal(intexp, opinc, marketcap):
    result = _f16_leverage_ratio(intexp, opinc, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intexp / netinc
def f16ls_f16_leverage_and_solvency_intexpni_252d_base_v140_signal(intexp, netinc, marketcap):
    result = _f16_leverage_ratio(intexp, netinc, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex / debt (capex burden vs leverage)
def f16ls_f16_leverage_and_solvency_capexdebt_21d_base_v141_signal(capex, debt, marketcap):
    result = _f16_leverage_ratio(capex, debt, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex / debt
def f16ls_f16_leverage_and_solvency_capexdebt_252d_base_v142_signal(capex, debt, marketcap):
    result = _f16_leverage_ratio(capex, debt, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex / equity
def f16ls_f16_leverage_and_solvency_capexequity_252d_base_v143_signal(capex, equity, marketcap):
    result = _f16_leverage_ratio(capex, equity, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intexp / liabilities (effective borrow rate proxy)
def f16ls_f16_leverage_and_solvency_intexpliab_252d_base_v144_signal(intexp, liabilities, marketcap):
    result = _f16_leverage_ratio(intexp, liabilities, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d intexp / debt
def f16ls_f16_leverage_and_solvency_intexpdebt_504d_base_v145_signal(intexp, debt, marketcap):
    result = _f16_leverage_ratio(intexp, debt, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d (debt + liabilities) / equity (full obligations leverage)
def f16ls_f16_leverage_and_solvency_fullob_eq_252d_base_v146_signal(debt, liabilities, equity, marketcap):
    fl = debt + liabilities
    result = _f16_leverage_ratio(fl, equity, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d (debt + liabilities) / assets
def f16ls_f16_leverage_and_solvency_fullob_a_252d_base_v147_signal(debt, liabilities, assets, marketcap):
    fl = debt + liabilities
    result = _f16_leverage_ratio(fl, assets, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d (debt + liabilities) / ebitda
def f16ls_f16_leverage_and_solvency_fullob_ebitda_252d_base_v148_signal(debt, liabilities, ebitda, marketcap):
    fl = debt + liabilities
    result = _f16_leverage_ratio(fl, ebitda, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite distress: D/E * debt/ebitda * 1/intcov
def f16ls_f16_leverage_and_solvency_distresscomp_504d_base_v149_signal(debt, equity, ebitda, intexp, marketcap):
    a = _f16_leverage_ratio(debt, equity, 504)
    b = _f16_leverage_ratio(debt, ebitda, 504)
    c = _f16_solvency_coverage(intexp, ebitda, 504)
    result = (a * b * c) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d health composite: 1/D/E + intcov + currentratio
def f16ls_f16_leverage_and_solvency_healthcomp_252d_base_v150_signal(debt, equity, ebitda, intexp, currentratio, marketcap):
    a = _f16_leverage_ratio(debt, equity, 252).replace(0, np.nan)
    b = _f16_solvency_coverage(ebitda, intexp, 252)
    c = _f16_solvency_coverage(currentratio * marketcap, marketcap, 252)
    result = (1.0 / a + b + c) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f16ls_f16_leverage_and_solvency_dez_252d_base_v076_signal,
    f16ls_f16_leverage_and_solvency_dez_504d_base_v077_signal,
    f16ls_f16_leverage_and_solvency_daz_252d_base_v078_signal,
    f16ls_f16_leverage_and_solvency_daz_504d_base_v079_signal,
    f16ls_f16_leverage_and_solvency_debtebitdaz_252d_base_v080_signal,
    f16ls_f16_leverage_and_solvency_debtebitdaz_504d_base_v081_signal,
    f16ls_f16_leverage_and_solvency_intcovz_252d_base_v082_signal,
    f16ls_f16_leverage_and_solvency_intcovz_504d_base_v083_signal,
    f16ls_f16_leverage_and_solvency_destd_252d_base_v084_signal,
    f16ls_f16_leverage_and_solvency_dastd_504d_base_v085_signal,
    f16ls_f16_leverage_and_solvency_debtebitdastd_252d_base_v086_signal,
    f16ls_f16_leverage_and_solvency_highde_count_252d_base_v087_signal,
    f16ls_f16_leverage_and_solvency_highdebtebitda_count_252d_base_v088_signal,
    f16ls_f16_leverage_and_solvency_lowintcov_count_252d_base_v089_signal,
    f16ls_f16_leverage_and_solvency_lowcr_count_504d_base_v090_signal,
    f16ls_f16_leverage_and_solvency_dedev_252d_base_v091_signal,
    f16ls_f16_leverage_and_solvency_dadev_504d_base_v092_signal,
    f16ls_f16_leverage_and_solvency_debtebitdadev_252d_base_v093_signal,
    f16ls_f16_leverage_and_solvency_intcovdev_252d_base_v094_signal,
    f16ls_f16_leverage_and_solvency_derelhi_504d_base_v095_signal,
    f16ls_f16_leverage_and_solvency_darelhi_504d_base_v096_signal,
    f16ls_f16_leverage_and_solvency_debtebitdarelhi_504d_base_v097_signal,
    f16ls_f16_leverage_and_solvency_depos_504d_base_v098_signal,
    f16ls_f16_leverage_and_solvency_dapos_504d_base_v099_signal,
    f16ls_f16_leverage_and_solvency_intcovpos_504d_base_v100_signal,
    f16ls_f16_leverage_and_solvency_blendedlev_252d_base_v101_signal,
    f16ls_f16_leverage_and_solvency_blendedsolv_252d_base_v102_signal,
    f16ls_f16_leverage_and_solvency_debtcfproxy_252d_base_v103_signal,
    f16ls_f16_leverage_and_solvency_debtretgap_252d_base_v104_signal,
    f16ls_f16_leverage_and_solvency_logde_21d_base_v105_signal,
    f16ls_f16_leverage_and_solvency_logde_252d_base_v106_signal,
    f16ls_f16_leverage_and_solvency_logdebtebitda_252d_base_v107_signal,
    f16ls_f16_leverage_and_solvency_logintcov_252d_base_v108_signal,
    f16ls_f16_leverage_and_solvency_levstress_252d_base_v109_signal,
    f16ls_f16_leverage_and_solvency_solvstrength_252d_base_v110_signal,
    f16ls_f16_leverage_and_solvency_desq_21d_base_v111_signal,
    f16ls_f16_leverage_and_solvency_desq_252d_base_v112_signal,
    f16ls_f16_leverage_and_solvency_debtebitdasq_252d_base_v113_signal,
    f16ls_f16_leverage_and_solvency_de_ema_21d_base_v114_signal,
    f16ls_f16_leverage_and_solvency_de_ema_252d_base_v115_signal,
    f16ls_f16_leverage_and_solvency_da_ema_21d_base_v116_signal,
    f16ls_f16_leverage_and_solvency_intcov_ema_252d_base_v117_signal,
    f16ls_f16_leverage_and_solvency_debtev_21d_base_v118_signal,
    f16ls_f16_leverage_and_solvency_debtev_252d_base_v119_signal,
    f16ls_f16_leverage_and_solvency_debtev_504d_base_v120_signal,
    f16ls_f16_leverage_and_solvency_de_recent_vs_trend_base_v121_signal,
    f16ls_f16_leverage_and_solvency_debtebitda_recent_vs_trend_base_v122_signal,
    f16ls_f16_leverage_and_solvency_intcov_recent_vs_trend_base_v123_signal,
    f16ls_f16_leverage_and_solvency_de_x_grossmargin_252d_base_v124_signal,
    f16ls_f16_leverage_and_solvency_debtfcfproxy_252d_base_v125_signal,
    f16ls_f16_leverage_and_solvency_retequity_21d_base_v126_signal,
    f16ls_f16_leverage_and_solvency_retequity_252d_base_v127_signal,
    f16ls_f16_leverage_and_solvency_retequity_504d_base_v128_signal,
    f16ls_f16_leverage_and_solvency_retassets_21d_base_v129_signal,
    f16ls_f16_leverage_and_solvency_retassets_252d_base_v130_signal,
    f16ls_f16_leverage_and_solvency_buffermult_21d_base_v131_signal,
    f16ls_f16_leverage_and_solvency_buffermult_252d_base_v132_signal,
    f16ls_f16_leverage_and_solvency_payabil_21d_base_v133_signal,
    f16ls_f16_leverage_and_solvency_payabil_252d_base_v134_signal,
    f16ls_f16_leverage_and_solvency_cashbuf_252d_base_v135_signal,
    f16ls_f16_leverage_and_solvency_intexpfcf_21d_base_v136_signal,
    f16ls_f16_leverage_and_solvency_intexpfcf_252d_base_v137_signal,
    f16ls_f16_leverage_and_solvency_intexpopinc_21d_base_v138_signal,
    f16ls_f16_leverage_and_solvency_intexpopinc_252d_base_v139_signal,
    f16ls_f16_leverage_and_solvency_intexpni_252d_base_v140_signal,
    f16ls_f16_leverage_and_solvency_capexdebt_21d_base_v141_signal,
    f16ls_f16_leverage_and_solvency_capexdebt_252d_base_v142_signal,
    f16ls_f16_leverage_and_solvency_capexequity_252d_base_v143_signal,
    f16ls_f16_leverage_and_solvency_intexpliab_252d_base_v144_signal,
    f16ls_f16_leverage_and_solvency_intexpdebt_504d_base_v145_signal,
    f16ls_f16_leverage_and_solvency_fullob_eq_252d_base_v146_signal,
    f16ls_f16_leverage_and_solvency_fullob_a_252d_base_v147_signal,
    f16ls_f16_leverage_and_solvency_fullob_ebitda_252d_base_v148_signal,
    f16ls_f16_leverage_and_solvency_distresscomp_504d_base_v149_signal,
    f16ls_f16_leverage_and_solvency_healthcomp_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F16_LEVERAGE_AND_SOLVENCY_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f16_leverage_and_solvency_base_076_150_claude: {n_features} features pass")
