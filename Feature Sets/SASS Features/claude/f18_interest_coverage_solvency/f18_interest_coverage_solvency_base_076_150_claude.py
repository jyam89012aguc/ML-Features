import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _slope(s, w):
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = (idx * idx).sum()

    def _f(a):
        if np.any(np.isnan(a)):
            return np.nan
        return float((idx * (a - a.mean())).sum() / denom)

    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== folder domain primitives (interest coverage & solvency, flow) =====
def _f18_icov(ebit, intexp):
    return ebit / intexp.replace(0, np.nan)


def _f18_ecov(ebitda, intexp):
    return ebitda / intexp.replace(0, np.nan)


def _f18_debt_ebitda(debt, ebitda):
    return debt / ebitda.replace(0, np.nan)


def _f18_liab_ebitda(liabilities, ebitda):
    return liabilities / ebitda.replace(0, np.nan)


def _f18_stshare(debtc, debt):
    return debtc / debt.replace(0, np.nan)


def _f18_cushion(ebit, intexp):
    return (ebit - intexp) / intexp.replace(0, np.nan)


def _f18_dscap(ebitda, debtc, intexp):
    return ebitda / (debtc + intexp).replace(0, np.nan)


# ============================================================
# --- coverage trend / slope family ---

# slope of EBIT interest coverage over a quarter (improving/worsening coverage)
def f18ic_f18_interest_coverage_solvency_icovslope_63d_base_v076_signal(ebit, intexp):
    b = _slope(_f18_icov(ebit, intexp), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBITDA interest coverage over a half-year
def f18ic_f18_interest_coverage_solvency_ecovslope_126d_base_v077_signal(ebitda, intexp):
    b = _slope(_f18_ecov(ebitda, intexp), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of debt/EBITDA over a half-year (deleveraging trajectory)
def f18ic_f18_interest_coverage_solvency_levslope_126d_base_v078_signal(debt, ebitda):
    b = _slope(_f18_debt_ebitda(debt, ebitda), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of short-term debt share over a quarter (refi-mix drift)
def f18ic_f18_interest_coverage_solvency_stshareslope_63d_base_v079_signal(debtc, debt):
    b = _slope(_f18_stshare(debtc, debt), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of liabilities/EBITDA over a year (broad solvency trajectory)
def f18ic_f18_interest_coverage_solvency_liabslope_252d_base_v080_signal(liabilities, ebitda):
    b = _slope(_f18_liab_ebitda(liabilities, ebitda), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- coverage hit-rate / streak family ---

# fraction of last year EBITDA coverage improved month-over-month (coverage momentum hit-rate)
def f18ic_f18_interest_coverage_solvency_covhitrate_252d_base_v081_signal(ebitda, intexp):
    ec = _f18_ecov(ebitda, intexp)
    up = (ec > ec.shift(21)).astype(float)
    b = up.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year debt/EBITDA fell month-over-month (deleveraging hit-rate)
def f18ic_f18_interest_coverage_solvency_levhitrate_252d_base_v082_signal(debt, ebitda):
    de = _f18_debt_ebitda(debt, ebitda)
    down = (de < de.shift(21)).astype(float)
    b = down.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive-quarter improvement streak in coverage cushion (sustained strengthening)
def f18ic_f18_interest_coverage_solvency_cushstreak_252d_base_v083_signal(ebit, intexp):
    cush = _f18_cushion(ebit, intexp)
    up = (cush > cush.shift(63)).astype(float)
    b = up.rolling(252, min_periods=63).sum() - 2.0 * (cush < cush.shift(63)).astype(float).rolling(252, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- cross-ratio coverage family (distinct numerator/denominator pairs) ---

# EBIT serviced against short-term debt directly (near-term operating coverage)
def f18ic_f18_interest_coverage_solvency_ebitstd_126d_base_v084_signal(ebit, debtc):
    b = _mean(ebit / debtc.replace(0, np.nan), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA serviced against total debt (gross paydown capacity), z-scored
def f18ic_f18_interest_coverage_solvency_ebitdadebt_252d_base_v085_signal(ebitda, debt):
    b = _z(ebitda / debt.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating income serviced against liabilities (broad solvency yield)
def f18ic_f18_interest_coverage_solvency_opincliab_126d_base_v086_signal(opinc, liabilities):
    b = _mean(opinc / liabilities.replace(0, np.nan), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA serviced against liabilities, percentile-ranked vs own 504d history
def f18ic_f18_interest_coverage_solvency_ebitdaliab_504d_base_v087_signal(ebitda, liabilities):
    b = _rank(ebitda / liabilities.replace(0, np.nan), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT serviced against liabilities, smoothed (broad earnings-solvency)
def f18ic_f18_interest_coverage_solvency_ebitliab_63d_base_v088_signal(ebit, liabilities):
    b = _mean(ebit / liabilities.replace(0, np.nan), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- coverage asymmetry / regime family ---

# coverage downside semi-deviation: dispersion of EBIT coverage below its mean (downside-only)
def f18ic_f18_interest_coverage_solvency_covsemidev_252d_base_v089_signal(ebit, intexp):
    ic = _f18_icov(ebit, intexp)
    m = _mean(ic, 252)
    dn = (ic - m).clip(upper=0)
    b = (dn ** 2).rolling(252, min_periods=126).mean() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage upside semi-deviation: dispersion of debt/EBITDA above its mean (bad-tail vol)
def f18ic_f18_interest_coverage_solvency_levsemidev_252d_base_v090_signal(debt, ebitda):
    de = _f18_debt_ebitda(debt, ebitda)
    m = _mean(de, 252)
    up = (de - m).clip(lower=0)
    b = (up ** 2).rolling(252, min_periods=126).mean() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage regime flag: smoothed sign of coverage minus its 252d median (regime persistence)
def f18ic_f18_interest_coverage_solvency_covregime_252d_base_v091_signal(ebitda, intexp):
    ec = _f18_ecov(ebitda, intexp)
    med = ec.rolling(252, min_periods=126).median()
    sgn = np.sign(ec - med)
    b = sgn.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- interest-cost dynamics family ---

# effective interest cost slope over a year (cost-of-debt trajectory)
def f18ic_f18_interest_coverage_solvency_effrateslope_252d_base_v092_signal(intexp, debt):
    b = _slope(intexp / debt.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# effective interest cost percentile vs own 504d history (financing-stress level)
def f18ic_f18_interest_coverage_solvency_effraterank_504d_base_v093_signal(intexp, debt):
    b = _rank(intexp / debt.replace(0, np.nan), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest cost on the short-term stack: intexp/debtc (near-term carry intensity)
def f18ic_f18_interest_coverage_solvency_streffrate_126d_base_v094_signal(intexp, debtc):
    b = _mean(intexp / debtc.replace(0, np.nan), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest cost relative to liabilities (all-in obligation carry), z-scored
def f18ic_f18_interest_coverage_solvency_intliabz_252d_base_v095_signal(intexp, liabilities):
    b = _z(intexp / liabilities.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite / interaction family ---

# coverage strength minus leverage burden in rank space (relative solvency rank)
def f18ic_f18_interest_coverage_solvency_solvrankspread_504d_base_v096_signal(ebit, intexp, debt, ebitda):
    cov_r = _rank(_f18_icov(ebit, intexp), 504)
    lev_r = _rank(_f18_debt_ebitda(debt, ebitda), 504)
    b = cov_r - lev_r
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage cushion times debt-service capacity (compound safety), z-scored
def f18ic_f18_interest_coverage_solvency_compoundsafe_252d_base_v097_signal(ebit, intexp, ebitda, debtc):
    safe = _f18_cushion(ebit, intexp) * _f18_dscap(ebitda, debtc, intexp)
    b = _z(safe, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest coverage divided by leverage (coverage-per-turn-of-debt), smoothed
def f18ic_f18_interest_coverage_solvency_covperturn_126d_base_v098_signal(ebit, intexp, debt, ebitda):
    cpt = _f18_icov(ebit, intexp) / _f18_debt_ebitda(debt, ebitda).replace(0, np.nan)
    b = _mean(cpt, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term-share-weighted leverage burden (refi-sensitive leverage), z-scored
def f18ic_f18_interest_coverage_solvency_refilev_252d_base_v099_signal(debtc, debt, liabilities, ebitda):
    rl = (debtc / debt.replace(0, np.nan)) * _f18_liab_ebitda(liabilities, ebitda)
    b = _z(rl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-coverage minus EBITDA-coverage gap (D&A and non-op reliance), smoothed
def f18ic_f18_interest_coverage_solvency_opvsebitda_126d_base_v100_signal(opinc, ebitda, intexp):
    gap = (opinc - ebitda) / intexp.replace(0, np.nan)
    b = _mean(gap, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum / change family (distinct windows) ---

# year-over-year change in EBIT interest coverage (annual coverage delta)
def f18ic_f18_interest_coverage_solvency_icovyoy_252d_base_v101_signal(ebit, intexp):
    ic = _f18_icov(ebit, intexp)
    b = ic - ic.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in debt/EBITDA (annual leverage delta)
def f18ic_f18_interest_coverage_solvency_levyoy_252d_base_v102_signal(debt, ebitda):
    de = _f18_debt_ebitda(debt, ebitda)
    b = de - de.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt share acceleration: change in the quarterly st-share change (2nd difference)
def f18ic_f18_interest_coverage_solvency_stshareqoq_63d_base_v103_signal(debtc, debt):
    ss = _f18_stshare(debtc, debt)
    chg = ss - ss.shift(63)
    b = chg - chg.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# month change in EBITDA debt-service capacity (near-term capacity momentum)
def f18ic_f18_interest_coverage_solvency_dscapmom_21d_base_v104_signal(ebitda, debtc, intexp):
    cap = _f18_dscap(ebitda, debtc, intexp)
    b = cap - cap.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year change in liabilities/EBITDA (broad solvency momentum)
def f18ic_f18_interest_coverage_solvency_liabmom_126d_base_v105_signal(liabilities, ebitda):
    le = _f18_liab_ebitda(liabilities, ebitda)
    b = le - le.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- normalized / log-ratio family ---

# log ratio of EBITDA coverage to its 252d-lagged self (multiplicative coverage growth)
def f18ic_f18_interest_coverage_solvency_logcovgrow_252d_base_v106_signal(ebitda, intexp):
    ec = _f18_ecov(ebitda, intexp).abs().replace(0, np.nan)
    b = np.log(ec / ec.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log ratio of debt/EBITDA to its 126d-lagged self (multiplicative leverage growth)
def f18ic_f18_interest_coverage_solvency_loglevgrow_126d_base_v107_signal(debt, ebitda):
    de = _f18_debt_ebitda(debt, ebitda).abs().replace(0, np.nan)
    b = np.log(de / de.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage normalized by leverage AND interest cost (triple-adjusted safety), smoothed
def f18ic_f18_interest_coverage_solvency_tripleadj_126d_base_v108_signal(ebitda, intexp, debt):
    ec = _f18_ecov(ebitda, intexp)
    de = _f18_debt_ebitda(debt, ebitda)
    er = intexp / debt.replace(0, np.nan)
    adj = ec / ((1.0 + de.clip(lower=0)) * (1.0 + er.clip(lower=0)))
    b = _mean(adj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- distress / tail family ---

# distance below the 504d worst coverage (how close to historic distress), smoothed
def f18ic_f18_interest_coverage_solvency_distressdist_504d_base_v109_signal(ebit, intexp):
    ic = _f18_icov(ebit, intexp)
    floor = ic.rolling(504, min_periods=252).min()
    span = ic.rolling(504, min_periods=252).max() - floor
    b = _mean((ic - floor) / span.replace(0, np.nan), 63) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage proximity to its 504d worst (how close to peak leverage), smoothed
def f18ic_f18_interest_coverage_solvency_levpeakprox_504d_base_v110_signal(debt, ebitda):
    de = _f18_debt_ebitda(debt, ebitda)
    ceil = de.rolling(504, min_periods=252).max()
    floor = de.rolling(504, min_periods=252).min()
    b = _mean((de - floor) / (ceil - floor).replace(0, np.nan), 63) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage shortfall depth: average gap below the trailing-252d median coverage (relative thinness)
def f18ic_f18_interest_coverage_solvency_covshortfall_252d_base_v111_signal(ebitda, intexp):
    ec = _f18_ecov(ebitda, intexp)
    med = ec.rolling(252, min_periods=126).median()
    depth = (med - ec).clip(lower=0) / med.replace(0, np.nan)
    b = depth.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- dispersion-of-burden family ---

# dispersion of effective interest cost over a year (financing instability)
def f18ic_f18_interest_coverage_solvency_effratestd_252d_base_v112_signal(intexp, debt):
    er = intexp / debt.replace(0, np.nan)
    b = _std(er, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of liabilities/EBITDA over a year, scaled by mean (solvency CV)
def f18ic_f18_interest_coverage_solvency_liabcv_252d_base_v113_signal(liabilities, ebitda):
    le = _f18_liab_ebitda(liabilities, ebitda)
    b = _std(le, 252) / _mean(le, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of short-term-debt-vs-EBITDA load over a year
def f18ic_f18_interest_coverage_solvency_stloadstd_252d_base_v114_signal(debtc, ebitda):
    load = debtc / ebitda.replace(0, np.nan)
    b = _std(load, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multi-leg composite family ---

# average of three coverage legs (EBIT, EBITDA, opinc) vs interest, smoothed
def f18ic_f18_interest_coverage_solvency_avgleg_63d_base_v115_signal(ebit, ebitda, opinc, intexp):
    c1 = _f18_icov(ebit, intexp)
    c2 = _f18_ecov(ebitda, intexp)
    c3 = opinc / intexp.replace(0, np.nan)
    avg = (c1 + c2 + c3) / 3.0
    b = _mean(avg, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread between best and worst coverage leg (coverage-quality range)
def f18ic_f18_interest_coverage_solvency_legrange_base_v116_signal(ebit, ebitda, opinc, intexp):
    c1 = _f18_icov(ebit, intexp)
    c2 = _f18_ecov(ebitda, intexp)
    c3 = opinc / intexp.replace(0, np.nan)
    stacked = pd.concat([c1, c2, c3], axis=1)
    b = stacked.max(axis=1) - stacked.min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA-to-EBIT coverage ratio (D&A leverage in coverage), smoothed
def f18ic_f18_interest_coverage_solvency_daratio_126d_base_v117_signal(ebit, ebitda, intexp):
    r = _f18_ecov(ebitda, intexp) / _f18_icov(ebit, intexp).replace(0, np.nan)
    b = _mean(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- leverage-mix family ---

# long-term debt burden trajectory: half-year change in (debt - debtc)/EBITDA (term-debt drift)
def f18ic_f18_interest_coverage_solvency_ltshare_252d_base_v118_signal(debt, debtc, ebitda):
    lt = (debt - debtc) / ebitda.replace(0, np.nan)
    b = lt - lt.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# non-debt liabilities vs EBITDA (operating obligation burden), z-scored
def f18ic_f18_interest_coverage_solvency_nondebtz_252d_base_v119_signal(liabilities, debt, ebitda):
    nd = (liabilities - debt) / ebitda.replace(0, np.nan)
    b = _z(nd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt's share of liabilities, percentile-ranked (financial-leverage intensity)
def f18ic_f18_interest_coverage_solvency_debtsharerank_504d_base_v120_signal(debt, liabilities):
    b = _rank(debt / liabilities.replace(0, np.nan), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- capacity / runway family ---

# EBITDA runway: how many years of EBITDA to clear total liabilities, log-compressed & smoothed
def f18ic_f18_interest_coverage_solvency_runway_126d_base_v121_signal(liabilities, ebitda):
    yrs = liabilities / ebitda.replace(0, np.nan)
    b = _mean(np.sign(yrs) * np.log1p(yrs.abs()), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# free cash for paydown after interest: (EBITDA - intexp)/debt, smoothed (organic deleveraging power)
def f18ic_f18_interest_coverage_solvency_paydownpwr_126d_base_v122_signal(ebitda, intexp, debt):
    ppw = (ebitda - intexp) / debt.replace(0, np.nan)
    b = _mean(ppw, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# paydown power percentile vs own 504d history (relative organic deleveraging strength)
def f18ic_f18_interest_coverage_solvency_paydownmom_126d_base_v123_signal(ebitda, intexp, debt):
    ppw = (ebitda - intexp) / debt.replace(0, np.nan)
    b = _rank(ppw, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-income paydown of short-term debt + interest, z-scored (near-term self-funding)
def f18ic_f18_interest_coverage_solvency_opselffundz_252d_base_v124_signal(opinc, debtc, intexp):
    ssf = opinc / (debtc + intexp).replace(0, np.nan)
    b = _z(ssf, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- tanh / bounded family ---

# bounded coverage-cushion stress: tanh of cushion z-score (saturating safety signal)
def f18ic_f18_interest_coverage_solvency_cushtanh_252d_base_v125_signal(ebit, intexp):
    z = _z(_f18_cushion(ebit, intexp), 252)
    b = np.tanh(0.7 * z)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bounded short-term-share stress: tanh of st-share z-score (saturating refi risk)
def f18ic_f18_interest_coverage_solvency_sttanh_252d_base_v126_signal(debtc, debt):
    z = _z(_f18_stshare(debtc, debt), 252)
    b = np.tanh(z)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bounded effective-rate shock: tanh of effective-rate z (saturating financing shock)
def f18ic_f18_interest_coverage_solvency_effratetanh_252d_base_v127_signal(intexp, debt):
    z = _z(intexp / debt.replace(0, np.nan), 252)
    b = np.tanh(z)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- rank-spread / relative family ---

# coverage rank minus interest-burden rank (net coverage standing)
def f18ic_f18_interest_coverage_solvency_netcovrank_504d_base_v128_signal(ebitda, intexp, debt):
    cov_r = _rank(_f18_ecov(ebitda, intexp), 504)
    burden_r = _rank(intexp / debt.replace(0, np.nan), 504)
    b = cov_r - burden_r
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-service-capacity rank minus liabilities-burden rank (relative durability)
def f18ic_f18_interest_coverage_solvency_durablerank_504d_base_v129_signal(ebitda, debtc, intexp, liabilities):
    cap_r = _rank(_f18_dscap(ebitda, debtc, intexp), 504)
    liab_r = _rank(_f18_liab_ebitda(liabilities, ebitda), 504)
    b = cap_r - liab_r
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- interaction with earnings sign / quality ---

# coverage conditioned on positive EBIT only (downside-aware coverage), smoothed
def f18ic_f18_interest_coverage_solvency_poscov_126d_base_v130_signal(ebit, intexp):
    ic = _f18_icov(ebit, intexp)
    pos = ic.where(ebit > 0)
    b = _mean(pos, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-income loss frequency blended with opinc coverage dispersion (operating fragility)
def f18ic_f18_interest_coverage_solvency_negebitfreq_252d_base_v131_signal(opinc, intexp):
    neg = (opinc < 0).astype(float)
    raw = neg.rolling(252, min_periods=126).mean()
    oc = opinc / intexp.replace(0, np.nan)
    b = raw + 0.1 * _std(oc, 63) / _mean(oc, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opinc-coverage stability: inverse CV of opinc/intexp over a year (reliable operating coverage)
def f18ic_f18_interest_coverage_solvency_opcovstab_252d_base_v132_signal(opinc, intexp):
    oc = opinc / intexp.replace(0, np.nan)
    b = _mean(oc, 252).abs() / _std(oc, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- second-order coverage shape ---

# coverage curvature: 252d mean minus midpoint of 252d hi/lo (skew of the coverage path)
def f18ic_f18_interest_coverage_solvency_covcurve_252d_base_v133_signal(ebitda, intexp):
    ec = _f18_ecov(ebitda, intexp)
    hi = ec.rolling(252, min_periods=126).max()
    lo = ec.rolling(252, min_periods=126).min()
    mid = (hi + lo) / 2.0
    b = (_mean(ec, 252) - mid) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage path skew: 252d mean vs midpoint of debt/EBITDA range
def f18ic_f18_interest_coverage_solvency_levcurve_252d_base_v134_signal(debt, ebitda):
    de = _f18_debt_ebitda(debt, ebitda)
    hi = de.rolling(252, min_periods=126).max()
    lo = de.rolling(252, min_periods=126).min()
    mid = (hi + lo) / 2.0
    b = (_mean(de, 252) - mid) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- additional cross-domain ratios ---

# interest expense as share of total liabilities, smoothed (all-in carry rate)
def f18ic_f18_interest_coverage_solvency_intliabrate_63d_base_v135_signal(intexp, liabilities):
    b = _mean(intexp / liabilities.replace(0, np.nan), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage-to-runway momentum: half-year change in EBITDA-coverage-per-unit-runway (improving durability)
def f18ic_f18_interest_coverage_solvency_covrunway_126d_base_v136_signal(ebitda, intexp, liabilities):
    ec = _f18_ecov(ebitda, intexp)
    runway = liabilities / ebitda.replace(0, np.nan)
    cr = ec / (1.0 + runway.clip(lower=0))
    b = cr - cr.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt covered by EBIT minus interest (free near-term coverage), z-scored
def f18ic_f18_interest_coverage_solvency_freestcov_252d_base_v137_signal(ebit, intexp, debtc):
    fc = (ebit - intexp) / debtc.replace(0, np.nan)
    b = _z(fc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-coverage cushion: (opinc - intexp)/intexp, percentile-ranked vs own 504d history
def f18ic_f18_interest_coverage_solvency_opcushionrank_504d_base_v138_signal(opinc, intexp):
    cush = (opinc - intexp) / intexp.replace(0, np.nan)
    b = _rank(cush, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- improvement-composite family ---

# coverage improving while leverage falling (clean strengthening composite), smoothed
def f18ic_f18_interest_coverage_solvency_cleanstrength_126d_base_v139_signal(ebitda, intexp, debt):
    ec = _f18_ecov(ebitda, intexp)
    de = _f18_debt_ebitda(debt, ebitda)
    comp = np.sign(ec - ec.shift(63)) - np.sign(de - de.shift(63))
    b = comp.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest burden falling while coverage rising (financing-relief composite)
def f18ic_f18_interest_coverage_solvency_relief_126d_base_v140_signal(intexp, debt, ebit):
    er = intexp / debt.replace(0, np.nan)
    ic = _f18_icov(ebit, intexp)
    comp = np.sign(ic - ic.shift(63)) - np.sign(er - er.shift(63))
    b = comp.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- final distinct levels & transforms ---

# squared-coverage penalty for thin coverage: 1/(1+EBITDA coverage), smoothed (convex distress weight)
def f18ic_f18_interest_coverage_solvency_thinpenalty_126d_base_v141_signal(ebitda, intexp):
    ec = _f18_ecov(ebitda, intexp)
    pen = 1.0 / (1.0 + ec.clip(lower=0))
    b = _mean(pen, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage convex penalty: (debt/EBITDA)^2 normalized, smoothed (accelerating distress with leverage)
def f18ic_f18_interest_coverage_solvency_levconvex_126d_base_v142_signal(debt, ebitda):
    de = _f18_debt_ebitda(debt, ebitda)
    conv = np.sign(de) * de ** 2
    b = _z(_mean(conv, 63), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage z minus leverage z minus burden z (broad solvency score), distinct weighting
def f18ic_f18_interest_coverage_solvency_solvscore_252d_base_v143_signal(ebit, intexp, debt, ebitda):
    s = (1.5 * _z(_f18_icov(ebit, intexp), 252)
         - _z(_f18_debt_ebitda(debt, ebitda), 252)
         - 0.5 * _z(intexp / debt.replace(0, np.nan), 252))
    b = s
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-service capacity slope over a quarter (capacity trajectory)
def f18ic_f18_interest_coverage_solvency_dscapslope_63d_base_v144_signal(ebitda, debtc, intexp):
    b = _slope(_f18_dscap(ebitda, debtc, intexp), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term-share level smoothed over a half-year (persistent rollover exposure)
def f18ic_f18_interest_coverage_solvency_stshareslow_126d_base_v145_signal(debtc, debt):
    b = _f18_stshare(debtc, debt).ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-coverage trajectory: half-year slope of liabilities-runway-adjusted EBIT coverage
def f18ic_f18_interest_coverage_solvency_durablecov_126d_base_v146_signal(ebit, intexp, liabilities, ebitda):
    ic = _f18_icov(ebit, intexp)
    runway = _f18_liab_ebitda(liabilities, ebitda)
    dc = ic / (1.0 + 0.1 * runway.clip(lower=0))
    b = _slope(dc, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest-coverage-to-short-term-debt-load ratio (near-term solvency efficiency), smoothed
def f18ic_f18_interest_coverage_solvency_stcoveff_126d_base_v147_signal(ebit, intexp, debtc, ebitda):
    ic = _f18_icov(ebit, intexp)
    stload = debtc / ebitda.replace(0, np.nan)
    eff = ic / (1.0 + stload.clip(lower=0))
    b = _mean(eff, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage cushion vs leverage burden interaction in z-space (combined safety tilt)
def f18ic_f18_interest_coverage_solvency_safetytilt_252d_base_v148_signal(ebit, intexp, debt, ebitda):
    cush_z = _z(_f18_cushion(ebit, intexp), 252)
    lev_z = _z(_f18_debt_ebitda(debt, ebitda), 252)
    b = cush_z * np.exp(-0.5 * lev_z.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in effective interest cost (annual cost-of-debt shift)
def f18ic_f18_interest_coverage_solvency_effrateyoy_252d_base_v149_signal(intexp, debt):
    er = intexp / debt.replace(0, np.nan)
    b = er - er.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# all-in solvency composite: average rank across coverage, leverage, st-share, burden (robust score)
def f18ic_f18_interest_coverage_solvency_robustscore_504d_base_v150_signal(ebitda, intexp, debt, debtc):
    r_cov = _rank(_f18_ecov(ebitda, intexp), 504)
    r_lev = -_rank(_f18_debt_ebitda(debt, ebitda), 504)
    r_st = -_rank(_f18_stshare(debtc, debt), 504)
    r_burden = -_rank(intexp / ebitda.replace(0, np.nan), 504)
    b = (r_cov + r_lev + r_st + r_burden) / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f18ic_f18_interest_coverage_solvency_icovslope_63d_base_v076_signal,
    f18ic_f18_interest_coverage_solvency_ecovslope_126d_base_v077_signal,
    f18ic_f18_interest_coverage_solvency_levslope_126d_base_v078_signal,
    f18ic_f18_interest_coverage_solvency_stshareslope_63d_base_v079_signal,
    f18ic_f18_interest_coverage_solvency_liabslope_252d_base_v080_signal,
    f18ic_f18_interest_coverage_solvency_covhitrate_252d_base_v081_signal,
    f18ic_f18_interest_coverage_solvency_levhitrate_252d_base_v082_signal,
    f18ic_f18_interest_coverage_solvency_cushstreak_252d_base_v083_signal,
    f18ic_f18_interest_coverage_solvency_ebitstd_126d_base_v084_signal,
    f18ic_f18_interest_coverage_solvency_ebitdadebt_252d_base_v085_signal,
    f18ic_f18_interest_coverage_solvency_opincliab_126d_base_v086_signal,
    f18ic_f18_interest_coverage_solvency_ebitdaliab_504d_base_v087_signal,
    f18ic_f18_interest_coverage_solvency_ebitliab_63d_base_v088_signal,
    f18ic_f18_interest_coverage_solvency_covsemidev_252d_base_v089_signal,
    f18ic_f18_interest_coverage_solvency_levsemidev_252d_base_v090_signal,
    f18ic_f18_interest_coverage_solvency_covregime_252d_base_v091_signal,
    f18ic_f18_interest_coverage_solvency_effrateslope_252d_base_v092_signal,
    f18ic_f18_interest_coverage_solvency_effraterank_504d_base_v093_signal,
    f18ic_f18_interest_coverage_solvency_streffrate_126d_base_v094_signal,
    f18ic_f18_interest_coverage_solvency_intliabz_252d_base_v095_signal,
    f18ic_f18_interest_coverage_solvency_solvrankspread_504d_base_v096_signal,
    f18ic_f18_interest_coverage_solvency_compoundsafe_252d_base_v097_signal,
    f18ic_f18_interest_coverage_solvency_covperturn_126d_base_v098_signal,
    f18ic_f18_interest_coverage_solvency_refilev_252d_base_v099_signal,
    f18ic_f18_interest_coverage_solvency_opvsebitda_126d_base_v100_signal,
    f18ic_f18_interest_coverage_solvency_icovyoy_252d_base_v101_signal,
    f18ic_f18_interest_coverage_solvency_levyoy_252d_base_v102_signal,
    f18ic_f18_interest_coverage_solvency_stshareqoq_63d_base_v103_signal,
    f18ic_f18_interest_coverage_solvency_dscapmom_21d_base_v104_signal,
    f18ic_f18_interest_coverage_solvency_liabmom_126d_base_v105_signal,
    f18ic_f18_interest_coverage_solvency_logcovgrow_252d_base_v106_signal,
    f18ic_f18_interest_coverage_solvency_loglevgrow_126d_base_v107_signal,
    f18ic_f18_interest_coverage_solvency_tripleadj_126d_base_v108_signal,
    f18ic_f18_interest_coverage_solvency_distressdist_504d_base_v109_signal,
    f18ic_f18_interest_coverage_solvency_levpeakprox_504d_base_v110_signal,
    f18ic_f18_interest_coverage_solvency_covshortfall_252d_base_v111_signal,
    f18ic_f18_interest_coverage_solvency_effratestd_252d_base_v112_signal,
    f18ic_f18_interest_coverage_solvency_liabcv_252d_base_v113_signal,
    f18ic_f18_interest_coverage_solvency_stloadstd_252d_base_v114_signal,
    f18ic_f18_interest_coverage_solvency_avgleg_63d_base_v115_signal,
    f18ic_f18_interest_coverage_solvency_legrange_base_v116_signal,
    f18ic_f18_interest_coverage_solvency_daratio_126d_base_v117_signal,
    f18ic_f18_interest_coverage_solvency_ltshare_252d_base_v118_signal,
    f18ic_f18_interest_coverage_solvency_nondebtz_252d_base_v119_signal,
    f18ic_f18_interest_coverage_solvency_debtsharerank_504d_base_v120_signal,
    f18ic_f18_interest_coverage_solvency_runway_126d_base_v121_signal,
    f18ic_f18_interest_coverage_solvency_paydownpwr_126d_base_v122_signal,
    f18ic_f18_interest_coverage_solvency_paydownmom_126d_base_v123_signal,
    f18ic_f18_interest_coverage_solvency_opselffundz_252d_base_v124_signal,
    f18ic_f18_interest_coverage_solvency_cushtanh_252d_base_v125_signal,
    f18ic_f18_interest_coverage_solvency_sttanh_252d_base_v126_signal,
    f18ic_f18_interest_coverage_solvency_effratetanh_252d_base_v127_signal,
    f18ic_f18_interest_coverage_solvency_netcovrank_504d_base_v128_signal,
    f18ic_f18_interest_coverage_solvency_durablerank_504d_base_v129_signal,
    f18ic_f18_interest_coverage_solvency_poscov_126d_base_v130_signal,
    f18ic_f18_interest_coverage_solvency_negebitfreq_252d_base_v131_signal,
    f18ic_f18_interest_coverage_solvency_opcovstab_252d_base_v132_signal,
    f18ic_f18_interest_coverage_solvency_covcurve_252d_base_v133_signal,
    f18ic_f18_interest_coverage_solvency_levcurve_252d_base_v134_signal,
    f18ic_f18_interest_coverage_solvency_intliabrate_63d_base_v135_signal,
    f18ic_f18_interest_coverage_solvency_covrunway_126d_base_v136_signal,
    f18ic_f18_interest_coverage_solvency_freestcov_252d_base_v137_signal,
    f18ic_f18_interest_coverage_solvency_opcushionrank_504d_base_v138_signal,
    f18ic_f18_interest_coverage_solvency_cleanstrength_126d_base_v139_signal,
    f18ic_f18_interest_coverage_solvency_relief_126d_base_v140_signal,
    f18ic_f18_interest_coverage_solvency_thinpenalty_126d_base_v141_signal,
    f18ic_f18_interest_coverage_solvency_levconvex_126d_base_v142_signal,
    f18ic_f18_interest_coverage_solvency_solvscore_252d_base_v143_signal,
    f18ic_f18_interest_coverage_solvency_dscapslope_63d_base_v144_signal,
    f18ic_f18_interest_coverage_solvency_stshareslow_126d_base_v145_signal,
    f18ic_f18_interest_coverage_solvency_durablecov_126d_base_v146_signal,
    f18ic_f18_interest_coverage_solvency_stcoveff_126d_base_v147_signal,
    f18ic_f18_interest_coverage_solvency_safetytilt_252d_base_v148_signal,
    f18ic_f18_interest_coverage_solvency_effrateyoy_252d_base_v149_signal,
    f18ic_f18_interest_coverage_solvency_robustscore_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F18_INTEREST_COVERAGE_SOLVENCY_REGISTRY_076_150 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
    g = np.random.default_rng(seed)
    n = 1500
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    ebit = _fund(101, base=2e8, drift=0.02, vol=0.06, allow_neg=True).rename("ebit")
    ebitda = _fund(102, base=3e8, drift=0.02, vol=0.05).rename("ebitda")
    intexp = _fund(103, base=2e7, drift=0.01, vol=0.04).rename("intexp")
    debt = _fund(104, base=1.2e9, drift=0.015, vol=0.04).rename("debt")
    debtc = _fund(105, base=3e8, drift=0.015, vol=0.05).rename("debtc")
    liabilities = _fund(106, base=2e9, drift=0.015, vol=0.04).rename("liabilities")
    opinc = _fund(107, base=2.2e8, drift=0.02, vol=0.06, allow_neg=True).rename("opinc")

    cols = {"ebit": ebit, "ebitda": ebitda, "intexp": intexp, "debt": debt,
            "debtc": debtc, "liabilities": liabilities, "opinc": opinc}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f18_interest_coverage_solvency_base_076_150_claude: %d features pass" % n_features)
