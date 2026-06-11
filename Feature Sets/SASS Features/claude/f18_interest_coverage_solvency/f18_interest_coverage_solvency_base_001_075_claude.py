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


# ===== folder domain primitives (interest coverage & solvency, flow) =====
def _f18_icov(ebit, intexp):
    # classic interest coverage: EBIT / interest expense
    return ebit / intexp.replace(0, np.nan)


def _f18_ecov(ebitda, intexp):
    # EBITDA interest coverage
    return ebitda / intexp.replace(0, np.nan)


def _f18_debt_ebitda(debt, ebitda):
    # leverage measured against cash earnings (solvency, flow)
    return debt / ebitda.replace(0, np.nan)


def _f18_liab_ebitda(liabilities, ebitda):
    return liabilities / ebitda.replace(0, np.nan)


def _f18_stshare(debtc, debt):
    # short-term debt share of total debt (refi / rollover risk)
    return debtc / debt.replace(0, np.nan)


def _f18_cushion(ebit, intexp):
    # coverage cushion: how far EBIT exceeds interest, scaled by interest
    return (ebit - intexp) / intexp.replace(0, np.nan)


def _f18_dscap(ebitda, debtc, intexp):
    # debt-service capacity: cash earnings vs near-term obligations
    return ebitda / (debtc + intexp).replace(0, np.nan)


# ============================================================
# --- interest coverage (EBIT/intexp) level family ---

# EBIT interest coverage, smoothed over a quarter
def f18ic_f18_interest_coverage_solvency_icov_63d_base_v001_signal(ebit, intexp):
    b = _mean(_f18_icov(ebit, intexp), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT interest coverage, z-scored vs its own 252d history (de-trended)
def f18ic_f18_interest_coverage_solvency_icovz_252d_base_v002_signal(ebit, intexp):
    b = _z(_f18_icov(ebit, intexp), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT interest coverage, percentile-ranked vs its own 504d history
def f18ic_f18_interest_coverage_solvency_icovrank_504d_base_v003_signal(ebit, intexp):
    b = _rank(_f18_icov(ebit, intexp), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log-coverage (compresses the heavy tail of EBIT/intexp), smoothed
def f18ic_f18_interest_coverage_solvency_logicov_126d_base_v004_signal(ebit, intexp):
    ic = _f18_icov(ebit, intexp)
    b = _mean(np.sign(ic) * np.log1p(ic.abs()), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion (instability) of EBIT interest coverage over a year
def f18ic_f18_interest_coverage_solvency_icovstd_252d_base_v005_signal(ebit, intexp):
    ic = _f18_icov(ebit, intexp)
    b = _std(ic, 252) / _mean(ic, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of current coverage above the trailing 252d minimum coverage (stress buffer)
def f18ic_f18_interest_coverage_solvency_icovbuf_252d_base_v006_signal(ebit, intexp):
    ic = _f18_icov(ebit, intexp)
    floor = ic.rolling(252, min_periods=126).min()
    b = (ic - floor) / floor.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EBITDA interest coverage family ---

# EBITDA interest coverage, smoothed
def f18ic_f18_interest_coverage_solvency_ecov_63d_base_v007_signal(ebitda, intexp):
    b = _mean(_f18_ecov(ebitda, intexp), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA interest coverage, z-scored vs own 252d history
def f18ic_f18_interest_coverage_solvency_ecovz_252d_base_v008_signal(ebitda, intexp):
    b = _z(_f18_ecov(ebitda, intexp), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA coverage minus EBIT coverage (D&A cushion on top of operating coverage)
def f18ic_f18_interest_coverage_solvency_dacushion_126d_base_v009_signal(ebit, ebitda, intexp):
    spread = _f18_ecov(ebitda, intexp) - _f18_icov(ebit, intexp)
    b = _mean(spread, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA coverage percentile vs own 504d history
def f18ic_f18_interest_coverage_solvency_ecovrank_504d_base_v010_signal(ebitda, intexp):
    b = _rank(_f18_ecov(ebitda, intexp), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log EBITDA coverage dispersion: rolling std of log-coverage over a year (coverage volatility)
def f18ic_f18_interest_coverage_solvency_logecov_126d_base_v011_signal(ebitda, intexp):
    ec = _f18_ecov(ebitda, intexp)
    lec = np.sign(ec) * np.log1p(ec.abs())
    b = _std(lec, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- coverage cushion family ---

# coverage cushion momentum: quarter-over-quarter change in (EBIT-intexp)/intexp
def f18ic_f18_interest_coverage_solvency_cushion_63d_base_v012_signal(ebit, intexp):
    cush = _f18_cushion(ebit, intexp)
    b = cush - cush.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage cushion convexity: signed sqrt of cushion vs its own 126d typical (asymmetric stress)
def f18ic_f18_interest_coverage_solvency_cushionz_252d_base_v013_signal(ebit, intexp):
    cush = _f18_cushion(ebit, intexp)
    typ = cush.rolling(126, min_periods=63).mean()
    b = np.sign(cush) * (cush.abs() ** 0.5) - np.sign(typ) * (typ.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last quarter EBIT coverage sat below its trailing-252d median (thin-coverage time)
def f18ic_f18_interest_coverage_solvency_thintime_252d_base_v014_signal(ebit, intexp):
    ic = _f18_icov(ebit, intexp)
    med = ic.rolling(252, min_periods=126).median()
    thin = (ic < med).astype(float)
    b = thin.rolling(63, min_periods=21).mean() + 0.25 * (ic / med.replace(0, np.nan) - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- debt/EBITDA leverage family ---

# net leverage debt/EBITDA, smoothed (lower is safer)
def f18ic_f18_interest_coverage_solvency_dbtebd_63d_base_v015_signal(debt, ebitda):
    b = _mean(_f18_debt_ebitda(debt, ebitda), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt/EBITDA z-scored vs own 252d history (de-trended leverage)
def f18ic_f18_interest_coverage_solvency_dbtebdz_252d_base_v016_signal(debt, ebitda):
    b = _z(_f18_debt_ebitda(debt, ebitda), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt/EBITDA percentile vs own 504d history
def f18ic_f18_interest_coverage_solvency_dbtebdrank_504d_base_v017_signal(debt, ebitda):
    b = _rank(_f18_debt_ebitda(debt, ebitda), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log debt/EBITDA smoothed (tail-compressed leverage level)
def f18ic_f18_interest_coverage_solvency_logdbtebd_126d_base_v018_signal(debt, ebitda):
    de = _f18_debt_ebitda(debt, ebitda)
    b = _mean(np.sign(de) * np.log1p(de.abs()), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage instability: dispersion of debt/EBITDA over a year
def f18ic_f18_interest_coverage_solvency_dbtebdstd_252d_base_v019_signal(debt, ebitda):
    de = _f18_debt_ebitda(debt, ebitda)
    b = _std(de, 252) / _mean(de, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of current leverage above its trailing-252d safest (min) level
def f18ic_f18_interest_coverage_solvency_dbtebdgap_252d_base_v020_signal(debt, ebitda):
    de = _f18_debt_ebitda(debt, ebitda)
    floor = de.rolling(252, min_periods=126).min()
    b = (de - floor) / floor.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- liabilities/EBITDA family ---

# total liabilities / EBITDA, smoothed (broad solvency burden)
def f18ic_f18_interest_coverage_solvency_liabebd_63d_base_v021_signal(liabilities, ebitda):
    b = _mean(_f18_liab_ebitda(liabilities, ebitda), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities/EBITDA z-scored vs own 252d history
def f18ic_f18_interest_coverage_solvency_liabebdz_252d_base_v022_signal(liabilities, ebitda):
    b = _z(_f18_liab_ebitda(liabilities, ebitda), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities/EBITDA percentile vs own 504d history
def f18ic_f18_interest_coverage_solvency_liabebdrank_504d_base_v023_signal(liabilities, ebitda):
    b = _rank(_f18_liab_ebitda(liabilities, ebitda), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# excess broad-solvency burden over debt burden ((liab-debt)/EBITDA): non-debt obligations
def f18ic_f18_interest_coverage_solvency_nondebtebd_126d_base_v024_signal(liabilities, debt, ebitda):
    burden = (liabilities - debt) / ebitda.replace(0, np.nan)
    b = _mean(burden, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- short-term debt share family ---

# short-term debt share debtc/debt, smoothed (rollover risk)
def f18ic_f18_interest_coverage_solvency_stshare_63d_base_v025_signal(debtc, debt):
    b = _mean(_f18_stshare(debtc, debt), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt share z-scored vs own 252d history
def f18ic_f18_interest_coverage_solvency_stsharez_252d_base_v026_signal(debtc, debt):
    b = _z(_f18_stshare(debtc, debt), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt share percentile vs own 504d history
def f18ic_f18_interest_coverage_solvency_stsharerank_504d_base_v027_signal(debtc, debt):
    b = _rank(_f18_stshare(debtc, debt), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rollover-risk z: short-term debt share interacted with effective interest cost, de-trended
def f18ic_f18_interest_coverage_solvency_rollrisk_126d_base_v028_signal(debtc, debt, intexp):
    risk = _f18_stshare(debtc, debt) * (intexp / debt.replace(0, np.nan))
    b = _z(risk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# near-term debt vs interest service: debtc / intexp (how many years of interest the ST stack equals)
def f18ic_f18_interest_coverage_solvency_stdebtebd_126d_base_v029_signal(debtc, intexp):
    ratio = debtc / intexp.replace(0, np.nan)
    b = _z(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- debt-service capacity family ---

# debt-service capacity EBITDA/(debtc+intexp), smoothed
def f18ic_f18_interest_coverage_solvency_dscap_63d_base_v030_signal(ebitda, debtc, intexp):
    b = _mean(_f18_dscap(ebitda, debtc, intexp), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-service capacity z-scored vs own 252d history
def f18ic_f18_interest_coverage_solvency_dscapz_252d_base_v031_signal(ebitda, debtc, intexp):
    b = _z(_f18_dscap(ebitda, debtc, intexp), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-service capacity percentile vs own 504d history
def f18ic_f18_interest_coverage_solvency_dscaprank_504d_base_v032_signal(ebitda, debtc, intexp):
    b = _rank(_f18_dscap(ebitda, debtc, intexp), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# free-coverage after near-term debt: (EBIT-intexp) vs short-term debt
def f18ic_f18_interest_coverage_solvency_freecov_126d_base_v033_signal(ebit, intexp, debtc):
    fc = (ebit - intexp) / debtc.replace(0, np.nan)
    b = _mean(fc, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- opinc-based coverage family (operating income leg) ---

# operating-income interest coverage opinc/intexp, smoothed
def f18ic_f18_interest_coverage_solvency_opcov_63d_base_v034_signal(opinc, intexp):
    b = _mean(opinc / intexp.replace(0, np.nan), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-income coverage z-scored vs own 252d history
def f18ic_f18_interest_coverage_solvency_opcovz_252d_base_v035_signal(opinc, intexp):
    b = _z(opinc / intexp.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quality-of-coverage gap: EBIT coverage minus opinc coverage (non-operating drag)
def f18ic_f18_interest_coverage_solvency_covqualgap_126d_base_v036_signal(ebit, opinc, intexp):
    gap = (ebit - opinc) / intexp.replace(0, np.nan)
    b = _mean(gap, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opinc serviced against total debt + interest (operating debt-service capacity)
def f18ic_f18_interest_coverage_solvency_opdscap_126d_base_v037_signal(opinc, debt, intexp):
    cap = opinc / (debt + intexp).replace(0, np.nan)
    b = _mean(cap, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- effective interest-cost / burden family ---

# effective interest cost intexp/debt, smoothed (cost of carry on the stack)
def f18ic_f18_interest_coverage_solvency_effrate_126d_base_v038_signal(intexp, debt):
    b = _mean(intexp / debt.replace(0, np.nan), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# effective interest cost z-scored vs own 252d history (financing-stress)
def f18ic_f18_interest_coverage_solvency_effratez_252d_base_v039_signal(intexp, debt):
    b = _z(intexp / debt.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest burden tail-risk: how far intexp/EBITDA sits above its trailing-252d median, smoothed
def f18ic_f18_interest_coverage_solvency_intburden_63d_base_v040_signal(intexp, ebitda):
    bd = intexp / ebitda.replace(0, np.nan)
    med = bd.rolling(252, min_periods=126).median()
    excess = (bd - med).clip(lower=0)
    b = _mean(excess, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest burden momentum: half-year change in intexp/EBITDA (rising cost of carry)
def f18ic_f18_interest_coverage_solvency_intburdenrank_504d_base_v041_signal(intexp, ebitda):
    bd = intexp / ebitda.replace(0, np.nan)
    b = bd - bd.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest as a share of operating income (opinc), smoothed
def f18ic_f18_interest_coverage_solvency_intopshare_126d_base_v042_signal(intexp, opinc):
    b = _mean(intexp / opinc.replace(0, np.nan), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite solvency scores ---

# coverage-minus-leverage composite: z(EBITDA coverage) - z(debt/EBITDA)
def f18ic_f18_interest_coverage_solvency_covlevscore_252d_base_v043_signal(ebitda, intexp, debt):
    score = _z(_f18_ecov(ebitda, intexp), 252) - _z(_f18_debt_ebitda(debt, ebitda), 252)
    b = score
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# solvency triad: z(coverage) - z(stshare) - z(liab/EBITDA)
def f18ic_f18_interest_coverage_solvency_triad_252d_base_v044_signal(ebit, intexp, debtc, debt, liabilities, ebitda):
    s = (_z(_f18_icov(ebit, intexp), 252)
         - _z(_f18_stshare(debtc, debt), 252)
         - _z(_f18_liab_ebitda(liabilities, ebitda), 252))
    b = s / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distress-tilt: high short-term share over thin coverage cushion interaction
def f18ic_f18_interest_coverage_solvency_distresstilt_126d_base_v045_signal(debtc, debt, ebit, intexp):
    tilt = _f18_stshare(debtc, debt) / _f18_cushion(ebit, intexp).clip(lower=0.01)
    b = _mean(tilt, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- coverage asymmetry / downside ---

# downside coverage dispersion: std of coverage only on below-median observations
def f18ic_f18_interest_coverage_solvency_covdownvol_252d_base_v046_signal(ebitda, intexp):
    ec = _f18_ecov(ebitda, intexp)
    med = ec.rolling(252, min_periods=126).median()
    dn = ec.where(ec < med)
    b = dn.rolling(252, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage skew proxy: (mean - median)/std of EBIT coverage over a year
def f18ic_f18_interest_coverage_solvency_covskew_252d_base_v047_signal(ebit, intexp):
    ic = _f18_icov(ebit, intexp)
    m = _mean(ic, 252)
    md = ic.rolling(252, min_periods=126).median()
    sd = _std(ic, 252)
    b = (m - md) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# worst-quarter coverage: trailing-252d minimum of the 63d-smoothed coverage
def f18ic_f18_interest_coverage_solvency_worstcov_252d_base_v048_signal(ebitda, intexp):
    ec = _mean(_f18_ecov(ebitda, intexp), 63)
    b = ec.rolling(252, min_periods=126).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- additional leverage / coverage cross-sections ---

# debt/EBITDA minus its own slow EMA (leverage displacement)
def f18ic_f18_interest_coverage_solvency_dbtebddisp_126d_base_v049_signal(debt, ebitda):
    de = _f18_debt_ebitda(debt, ebitda)
    b = de - de.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage acceleration: change in the quarter-over-quarter coverage change (2nd difference of level)
def f18ic_f18_interest_coverage_solvency_covdisp_126d_base_v050_signal(ebit, intexp):
    ic = _f18_icov(ebit, intexp)
    chg = ic - ic.shift(63)
    b = chg - chg.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fast-vs-slow coverage crossover: EBITDA coverage 21d EMA minus 126d EMA (coverage trend tilt)
def f18ic_f18_interest_coverage_solvency_covema_63d_base_v051_signal(ebitda, intexp):
    ec = _f18_ecov(ebitda, intexp)
    b = ec.ewm(span=21, min_periods=10).mean() - ec.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt vs liabilities (near-term share of all obligations)
def f18ic_f18_interest_coverage_solvency_stliabshare_126d_base_v052_signal(debtc, liabilities):
    b = _mean(debtc / liabilities.replace(0, np.nan), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-share-of-liabilities momentum: half-year change in debt/liabilities (financing-mix shift)
def f18ic_f18_interest_coverage_solvency_debtliabmix_126d_base_v053_signal(debt, liabilities):
    mix = debt / liabilities.replace(0, np.nan)
    b = mix - mix.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# years-to-repay net of interest: half-year momentum of debt/(EBITDA - intexp) (paydown trajectory)
def f18ic_f18_interest_coverage_solvency_intadjlev_126d_base_v054_signal(debt, intexp, ebitda):
    horizon = debt / (ebitda - intexp).replace(0, np.nan)
    b = horizon - horizon.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage robustness: min(EBIT cov, EBITDA cov, opinc cov) smoothed (weakest leg)
def f18ic_f18_interest_coverage_solvency_minleg_63d_base_v055_signal(ebit, ebitda, opinc, intexp):
    c1 = _f18_icov(ebit, intexp)
    c2 = _f18_ecov(ebitda, intexp)
    c3 = opinc / intexp.replace(0, np.nan)
    weakest = pd.concat([c1, c2, c3], axis=1).min(axis=1)
    b = _mean(weakest, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage leg dispersion: std across EBIT/EBITDA/opinc coverage (quality disagreement)
def f18ic_f18_interest_coverage_solvency_legdisp_base_v056_signal(ebit, ebitda, opinc, intexp):
    c1 = _f18_icov(ebit, intexp)
    c2 = _f18_ecov(ebitda, intexp)
    c3 = opinc / intexp.replace(0, np.nan)
    b = pd.concat([c1, c2, c3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage per unit of leverage: EBITDA coverage / debt-EBITDA (efficiency of debt)
def f18ic_f18_interest_coverage_solvency_coveff_126d_base_v057_signal(ebitda, intexp, debt):
    eff = _f18_ecov(ebitda, intexp) / _f18_debt_ebitda(debt, ebitda).replace(0, np.nan)
    b = _mean(eff, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed deviation of coverage from its 252d norm (bounded stress signal)
def f18ic_f18_interest_coverage_solvency_covtanh_252d_base_v058_signal(ebit, intexp):
    z = _z(_f18_icov(ebit, intexp), 252)
    b = np.tanh(z)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed leverage z (bounded over-leverage signal)
def f18ic_f18_interest_coverage_solvency_levtanh_252d_base_v059_signal(debt, ebitda):
    z = _z(_f18_debt_ebitda(debt, ebitda), 252)
    b = np.tanh(z)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage cushion relative to leverage: cushion x (1/(1+debt/EBITDA))
def f18ic_f18_interest_coverage_solvency_safecushion_126d_base_v060_signal(ebit, intexp, debt, ebitda):
    cush = _f18_cushion(ebit, intexp)
    lev = _f18_debt_ebitda(debt, ebitda)
    safe = cush / (1.0 + lev.clip(lower=0))
    b = _mean(safe, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest expense growth vs liabilities growth (rising cost vs broad obligation base)
def f18ic_f18_interest_coverage_solvency_intvsearn_126d_base_v061_signal(intexp, liabilities):
    ig = np.log(intexp.replace(0, np.nan)) - np.log(intexp.shift(63).replace(0, np.nan))
    lg = np.log(liabilities.replace(0, np.nan)) - np.log(liabilities.shift(63).replace(0, np.nan))
    b = ig - lg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of debt-service capacity relative to leverage rank (relative safety)
def f18ic_f18_interest_coverage_solvency_dscaprelev_504d_base_v062_signal(ebitda, debtc, intexp, debt):
    cap_r = _rank(_f18_dscap(ebitda, debtc, intexp), 504)
    lev_r = _rank(_f18_debt_ebitda(debt, ebitda), 504)
    b = cap_r - lev_r
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cushion-improvement percentile: rank of the 63d cushion change vs own 504d history
def f18ic_f18_interest_coverage_solvency_cushionrank_504d_base_v063_signal(ebit, intexp):
    cush = _f18_cushion(ebit, intexp)
    chg = cush - cush.shift(63)
    b = _rank(chg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interest-burden displacement: intexp/EBITDA minus slow EMA
def f18ic_f18_interest_coverage_solvency_burdendisp_126d_base_v064_signal(intexp, ebitda):
    bd = intexp / ebitda.replace(0, np.nan)
    b = bd - bd.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities/EBITDA displacement vs slow EMA (broad solvency drift)
def f18ic_f18_interest_coverage_solvency_liabdisp_126d_base_v065_signal(liabilities, ebitda):
    le = _f18_liab_ebitda(liabilities, ebitda)
    b = le - le.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of quarter debt/EBITDA above its trailing-252d median (over-levered time)
def f18ic_f18_interest_coverage_solvency_overlevtime_252d_base_v066_signal(debt, ebitda):
    de = _f18_debt_ebitda(debt, ebitda)
    med = de.rolling(252, min_periods=126).median()
    over = (de > med).astype(float)
    b = over.rolling(63, min_periods=21).mean() + 0.25 * (de / med.replace(0, np.nan) - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term-share dispersion over a year (refi-mix instability)
def f18ic_f18_interest_coverage_solvency_stsharestd_252d_base_v067_signal(debtc, debt):
    b = _std(_f18_stshare(debtc, debt), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-service capacity instability (dispersion / mean)
def f18ic_f18_interest_coverage_solvency_dscapstd_252d_base_v068_signal(ebitda, debtc, intexp):
    cap = _f18_dscap(ebitda, debtc, intexp)
    b = _std(cap, 252) / _mean(cap, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-stress interaction: debt/EBITDA scaled by the interest burden it carries
def f18ic_f18_interest_coverage_solvency_netlev_126d_base_v069_signal(debt, ebitda, intexp):
    lev = _f18_debt_ebitda(debt, ebitda)
    burden = intexp / ebitda.replace(0, np.nan)
    stress = lev * burden
    b = _z(stress, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage rebound off its 252d trough (coverage recovery)
def f18ic_f18_interest_coverage_solvency_covrecov_252d_base_v070_signal(ebitda, intexp):
    ec = _f18_ecov(ebitda, intexp)
    trough = ec.rolling(252, min_periods=126).min()
    b = ec / trough.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage recovery from its 252d worst level (how much leverage has improved off the peak)
def f18ic_f18_interest_coverage_solvency_levdd_252d_base_v071_signal(debt, ebitda):
    de = _f18_debt_ebitda(debt, ebitda)
    worst = de.rolling(252, min_periods=126).max()
    b = 1.0 - de / worst.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt + interest covered by operating income (near-term self-funding)
def f18ic_f18_interest_coverage_solvency_stselffund_126d_base_v072_signal(opinc, debtc, intexp):
    ssf = opinc / (debtc + intexp).replace(0, np.nan)
    b = _mean(ssf, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite stress rank: avg of leverage rank, burden rank, st-share rank
def f18ic_f18_interest_coverage_solvency_stressrank_504d_base_v073_signal(debt, ebitda, intexp, debtc):
    r1 = _rank(_f18_debt_ebitda(debt, ebitda), 504)
    r2 = _rank(intexp / ebitda.replace(0, np.nan), 504)
    r3 = _rank(_f18_stshare(debtc, debt), 504)
    b = (r1 + r2 + r3) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage momentum vs leverage momentum (improving fundamentals)
def f18ic_f18_interest_coverage_solvency_covlevmom_126d_base_v074_signal(ebitda, intexp, debt):
    ec = _f18_ecov(ebitda, intexp)
    de = _f18_debt_ebitda(debt, ebitda)
    cm = ec / ec.shift(126) - 1.0
    lm = de / de.shift(126) - 1.0
    b = cm - lm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# all-in solvency cushion momentum: half-year change in debt-service capacity minus st-share drift
def f18ic_f18_interest_coverage_solvency_allincushion_126d_base_v075_signal(ebitda, debtc, intexp, debt):
    cap = _f18_dscap(ebitda, debtc, intexp)
    pen = _f18_stshare(debtc, debt)
    capchg = cap - cap.shift(126)
    penchg = pen - pen.shift(126)
    b = capchg - 2.0 * penchg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f18ic_f18_interest_coverage_solvency_icov_63d_base_v001_signal,
    f18ic_f18_interest_coverage_solvency_icovz_252d_base_v002_signal,
    f18ic_f18_interest_coverage_solvency_icovrank_504d_base_v003_signal,
    f18ic_f18_interest_coverage_solvency_logicov_126d_base_v004_signal,
    f18ic_f18_interest_coverage_solvency_icovstd_252d_base_v005_signal,
    f18ic_f18_interest_coverage_solvency_icovbuf_252d_base_v006_signal,
    f18ic_f18_interest_coverage_solvency_ecov_63d_base_v007_signal,
    f18ic_f18_interest_coverage_solvency_ecovz_252d_base_v008_signal,
    f18ic_f18_interest_coverage_solvency_dacushion_126d_base_v009_signal,
    f18ic_f18_interest_coverage_solvency_ecovrank_504d_base_v010_signal,
    f18ic_f18_interest_coverage_solvency_logecov_126d_base_v011_signal,
    f18ic_f18_interest_coverage_solvency_cushion_63d_base_v012_signal,
    f18ic_f18_interest_coverage_solvency_cushionz_252d_base_v013_signal,
    f18ic_f18_interest_coverage_solvency_thintime_252d_base_v014_signal,
    f18ic_f18_interest_coverage_solvency_dbtebd_63d_base_v015_signal,
    f18ic_f18_interest_coverage_solvency_dbtebdz_252d_base_v016_signal,
    f18ic_f18_interest_coverage_solvency_dbtebdrank_504d_base_v017_signal,
    f18ic_f18_interest_coverage_solvency_logdbtebd_126d_base_v018_signal,
    f18ic_f18_interest_coverage_solvency_dbtebdstd_252d_base_v019_signal,
    f18ic_f18_interest_coverage_solvency_dbtebdgap_252d_base_v020_signal,
    f18ic_f18_interest_coverage_solvency_liabebd_63d_base_v021_signal,
    f18ic_f18_interest_coverage_solvency_liabebdz_252d_base_v022_signal,
    f18ic_f18_interest_coverage_solvency_liabebdrank_504d_base_v023_signal,
    f18ic_f18_interest_coverage_solvency_nondebtebd_126d_base_v024_signal,
    f18ic_f18_interest_coverage_solvency_stshare_63d_base_v025_signal,
    f18ic_f18_interest_coverage_solvency_stsharez_252d_base_v026_signal,
    f18ic_f18_interest_coverage_solvency_stsharerank_504d_base_v027_signal,
    f18ic_f18_interest_coverage_solvency_rollrisk_126d_base_v028_signal,
    f18ic_f18_interest_coverage_solvency_stdebtebd_126d_base_v029_signal,
    f18ic_f18_interest_coverage_solvency_dscap_63d_base_v030_signal,
    f18ic_f18_interest_coverage_solvency_dscapz_252d_base_v031_signal,
    f18ic_f18_interest_coverage_solvency_dscaprank_504d_base_v032_signal,
    f18ic_f18_interest_coverage_solvency_freecov_126d_base_v033_signal,
    f18ic_f18_interest_coverage_solvency_opcov_63d_base_v034_signal,
    f18ic_f18_interest_coverage_solvency_opcovz_252d_base_v035_signal,
    f18ic_f18_interest_coverage_solvency_covqualgap_126d_base_v036_signal,
    f18ic_f18_interest_coverage_solvency_opdscap_126d_base_v037_signal,
    f18ic_f18_interest_coverage_solvency_effrate_126d_base_v038_signal,
    f18ic_f18_interest_coverage_solvency_effratez_252d_base_v039_signal,
    f18ic_f18_interest_coverage_solvency_intburden_63d_base_v040_signal,
    f18ic_f18_interest_coverage_solvency_intburdenrank_504d_base_v041_signal,
    f18ic_f18_interest_coverage_solvency_intopshare_126d_base_v042_signal,
    f18ic_f18_interest_coverage_solvency_covlevscore_252d_base_v043_signal,
    f18ic_f18_interest_coverage_solvency_triad_252d_base_v044_signal,
    f18ic_f18_interest_coverage_solvency_distresstilt_126d_base_v045_signal,
    f18ic_f18_interest_coverage_solvency_covdownvol_252d_base_v046_signal,
    f18ic_f18_interest_coverage_solvency_covskew_252d_base_v047_signal,
    f18ic_f18_interest_coverage_solvency_worstcov_252d_base_v048_signal,
    f18ic_f18_interest_coverage_solvency_dbtebddisp_126d_base_v049_signal,
    f18ic_f18_interest_coverage_solvency_covdisp_126d_base_v050_signal,
    f18ic_f18_interest_coverage_solvency_covema_63d_base_v051_signal,
    f18ic_f18_interest_coverage_solvency_stliabshare_126d_base_v052_signal,
    f18ic_f18_interest_coverage_solvency_debtliabmix_126d_base_v053_signal,
    f18ic_f18_interest_coverage_solvency_intadjlev_126d_base_v054_signal,
    f18ic_f18_interest_coverage_solvency_minleg_63d_base_v055_signal,
    f18ic_f18_interest_coverage_solvency_legdisp_base_v056_signal,
    f18ic_f18_interest_coverage_solvency_coveff_126d_base_v057_signal,
    f18ic_f18_interest_coverage_solvency_covtanh_252d_base_v058_signal,
    f18ic_f18_interest_coverage_solvency_levtanh_252d_base_v059_signal,
    f18ic_f18_interest_coverage_solvency_safecushion_126d_base_v060_signal,
    f18ic_f18_interest_coverage_solvency_intvsearn_126d_base_v061_signal,
    f18ic_f18_interest_coverage_solvency_dscaprelev_504d_base_v062_signal,
    f18ic_f18_interest_coverage_solvency_cushionrank_504d_base_v063_signal,
    f18ic_f18_interest_coverage_solvency_burdendisp_126d_base_v064_signal,
    f18ic_f18_interest_coverage_solvency_liabdisp_126d_base_v065_signal,
    f18ic_f18_interest_coverage_solvency_overlevtime_252d_base_v066_signal,
    f18ic_f18_interest_coverage_solvency_stsharestd_252d_base_v067_signal,
    f18ic_f18_interest_coverage_solvency_dscapstd_252d_base_v068_signal,
    f18ic_f18_interest_coverage_solvency_netlev_126d_base_v069_signal,
    f18ic_f18_interest_coverage_solvency_covrecov_252d_base_v070_signal,
    f18ic_f18_interest_coverage_solvency_levdd_252d_base_v071_signal,
    f18ic_f18_interest_coverage_solvency_stselffund_126d_base_v072_signal,
    f18ic_f18_interest_coverage_solvency_stressrank_504d_base_v073_signal,
    f18ic_f18_interest_coverage_solvency_covlevmom_126d_base_v074_signal,
    f18ic_f18_interest_coverage_solvency_allincushion_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F18_INTEREST_COVERAGE_SOLVENCY_REGISTRY_001_075 = REGISTRY


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

    print("OK f18_interest_coverage_solvency_base_001_075_claude: %d features pass" % n_features)
