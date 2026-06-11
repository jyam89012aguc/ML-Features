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


def _chg(s, w):
    return s - s.shift(w)


def _roc(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _glog(a, b):
    return np.log(a.replace(0, np.nan) / b.replace(0, np.nan))


# ===== folder domain primitives (quality-compounder economics) =====
# returns engine
def _f33_roic_level(roic, w):
    # smoothed return-on-invested-capital level
    return roic.rolling(w, min_periods=max(1, w // 2)).mean()


def _f33_roic_stability(roic, w):
    # high stable ROIC -> low coefficient of variation (inverted dispersion)
    m = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = roic.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f33_fcf_roic(fcf, equity, w):
    # FCF return on equity capital (cash-based return on capital)
    r = fcf / equity.replace(0, np.nan)
    return r.rolling(w, min_periods=max(1, w // 2)).mean()


def _f33_reinvest_rate(fcf, netinc, w):
    # retention/reinvestment proxy: earnings NOT paid out as free cash (1 - fcf/netinc)
    payout = fcf / netinc.replace(0, np.nan)
    reinv = 1.0 - payout
    return reinv.rolling(w, min_periods=max(1, w // 2)).mean()


def _f33_dilution(sharesbas, w):
    # share-count growth over window (positive => dilution, negative => buyback)
    return sharesbas / sharesbas.shift(w).replace(0, np.nan) - 1.0


def _f33_revgrowth(revenue, w):
    return revenue / revenue.shift(w).replace(0, np.nan) - 1.0


def _f33_fcf_margin(fcf, revenue, w):
    r = fcf / revenue.replace(0, np.nan)
    return r.rolling(w, min_periods=max(1, w // 2)).mean()


def _f33_capital_turnover(revenue, equity, w):
    t = revenue / equity.replace(0, np.nan)
    return t.rolling(w, min_periods=max(1, w // 2)).mean()


# ============================================================
# --- high-stable-ROIC x low-dilution composites ---

# stable ROIC level minus share-count growth (quality-minus-dilution core)
def f33qc_f33_quality_compounder_qmd_252d_base_v001_signal(roic, sharesbas):
    r = _f33_roic_level(roic, 252)
    d = _f33_dilution(sharesbas, 252)
    b = r - d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC stability scaled down by dilution (durable compounder score)
def f33qc_f33_quality_compounder_stabdil_252d_base_v002_signal(roic, sharesbas):
    stab = _f33_roic_stability(roic, 252)
    d = _f33_dilution(sharesbas, 252)
    b = stab * (1.0 - d.clip(-0.5, 0.5))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback-amplified ROIC where the BUYBACK term dominates the variation
# (returns x anti-dilution, but driven by the dilution dynamics not the ROIC trend)
def f33qc_f33_quality_compounder_roicbuyback_252d_base_v003_signal(roic, sharesbas):
    r = _f33_roic_level(roic, 252).clip(lower=0.0)
    buyback = -_f33_dilution(sharesbas, 63)
    b = np.sign(r) * np.sqrt(r.abs()) * np.tanh(8.0 * buyback)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share ROIC ACCELERATION: change in (ROIC deflated by share growth) over a quarter
def f33qc_f33_quality_compounder_roicpershare_504d_base_v004_signal(roic, sharesbas):
    r = _f33_roic_level(roic, 126)
    sgrowth = sharesbas / sharesbas.shift(252).replace(0, np.nan)
    ratio = r / sgrowth.replace(0, np.nan)
    b = ratio - ratio.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread between ROIC and dilution, z-scored vs own history
def f33qc_f33_quality_compounder_qmdz_252d_base_v005_signal(roic, sharesbas):
    r = _f33_roic_level(roic, 126)
    d = _f33_dilution(sharesbas, 252)
    b = _z(r - d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# high ROIC AND not diluting: product of ROIC-rank and buyback-rank
def f33qc_f33_quality_compounder_dualrank_252d_base_v006_signal(roic, sharesbas):
    rr = _rank(_f33_roic_level(roic, 126), 252)
    br = _rank(-_f33_dilution(sharesbas, 252), 252)
    b = (rr + 0.5) * (br + 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- FCF-ROIC composites ---

# FCF-on-equity return (cash ROIC) level
def f33qc_f33_quality_compounder_fcfroic_252d_base_v007_signal(fcf, equity):
    b = _f33_fcf_roic(fcf, equity, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blend of accounting ROIC and cash FCF-ROIC, z-scored so the trend cancels (quality-of-return)
def f33qc_f33_quality_compounder_blendroic_252d_base_v008_signal(roic, fcf, equity):
    cash = _z(_f33_fcf_roic(fcf, equity, 252), 504)
    acct = _z(_f33_roic_level(roic, 252), 504)
    b = 0.5 * acct + 0.5 * cash
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion of returns: FCF-ROIC minus accounting ROIC (earnings quality of returns)
def f33qc_f33_quality_compounder_cashconv_252d_base_v009_signal(roic, fcf, equity):
    cash = _f33_fcf_roic(fcf, equity, 252)
    acct = _f33_roic_level(roic, 252)
    b = cash - acct
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash returns funding growth, but as the INTERACTION of de-trended cash-return and growth
def f33qc_f33_quality_compounder_fcfroicgrow_504d_base_v010_signal(fcf, equity, revenue):
    cash = _z(_f33_fcf_roic(fcf, equity, 126), 504)
    g = _z(_f33_revgrowth(revenue, 252), 504)
    b = cash * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-ROIC stability (cash return divided by its own dispersion)
def f33qc_f33_quality_compounder_fcfroicstab_252d_base_v011_signal(fcf, equity):
    r = fcf / equity.replace(0, np.nan)
    m = r.rolling(252, min_periods=126).mean()
    sd = r.rolling(252, min_periods=126).std()
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-ROIC net of dilution, both standardized (cash return to existing owners, de-trended)
def f33qc_f33_quality_compounder_fcfroicdil_252d_base_v012_signal(fcf, equity, sharesbas):
    cash = _z(_f33_fcf_roic(fcf, equity, 252), 504)
    d = _z(_f33_dilution(sharesbas, 252), 504)
    b = cash - d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- reinvestment-at-high-returns composites ---

# ROIC x reinvestment rate (the compounding engine: return on reinvested capital)
def f33qc_f33_quality_compounder_compound_252d_base_v013_signal(roic, fcf, netinc):
    r = _f33_roic_level(roic, 252)
    reinv = _f33_reinvest_rate(fcf, netinc, 252)
    b = r * reinv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sustainable growth proxy: ROIC x retention, z-scored
def f33qc_f33_quality_compounder_sustgrow_252d_base_v014_signal(roic, fcf, netinc):
    r = _f33_roic_level(roic, 126)
    reinv = _f33_reinvest_rate(fcf, netinc, 252)
    b = _z(r * reinv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment funded by cash returns and turning into revenue (reinvest x revgrowth)
def f33qc_f33_quality_compounder_reinvgrow_504d_base_v015_signal(fcf, netinc, revenue):
    reinv = _f33_reinvest_rate(fcf, netinc, 252)
    g = _f33_revgrowth(revenue, 504)
    b = reinv * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# high-return reinvestment efficiency: revenue growth per unit reinvested at given ROIC
def f33qc_f33_quality_compounder_reinveff_504d_base_v016_signal(roic, revenue, equity):
    g = _f33_revgrowth(revenue, 504)
    r = _f33_roic_level(roic, 252)
    b = g * r
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate weighted by ROIC quality minus dilution drag
def f33qc_f33_quality_compounder_reinvqual_252d_base_v017_signal(roic, fcf, netinc, sharesbas):
    r = _f33_roic_level(roic, 252)
    reinv = _f33_reinvest_rate(fcf, netinc, 252)
    d = _f33_dilution(sharesbas, 252)
    b = r * reinv - d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book compounding as INTERACTION of de-trended equity-growth and ROIC level
def f33qc_f33_quality_compounder_bookcompound_504d_base_v018_signal(roic, equity):
    eqg = _z(_f33_revgrowth(equity, 252), 504)
    r = _z(_f33_roic_level(roic, 252), 504)
    b = eqg * r
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- FCF-margin x return composites ---

# FCF margin x ROIC (cash-rich high-return composite)
def f33qc_f33_quality_compounder_fcfmgnroic_252d_base_v019_signal(fcf, revenue, roic):
    fm = _f33_fcf_margin(fcf, revenue, 252)
    r = _f33_roic_level(roic, 252)
    b = fm * (1.0 + r.clip(-0.5, 1.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin net of dilution, ranked (cash per dollar of sales to existing owners)
def f33qc_f33_quality_compounder_fcfmgndil_252d_base_v020_signal(fcf, revenue, sharesbas):
    fm = _rank(_f33_fcf_margin(fcf, revenue, 252), 504)
    d = _rank(_f33_dilution(sharesbas, 252), 504)
    b = fm - d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin x revenue growth (Rule-of-40-like quality-of-growth)
def f33qc_f33_quality_compounder_fcfmgngrow_504d_base_v021_signal(fcf, revenue):
    fm = _f33_fcf_margin(fcf, revenue, 252)
    g = _f33_revgrowth(revenue, 504)
    b = fm + g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin x ROIC as interaction of de-trended terms (profitability-quality composite)
def f33qc_f33_quality_compounder_netmgnroic_252d_base_v022_signal(netinc, revenue, roic):
    nm = _z((netinc / revenue.replace(0, np.nan)).rolling(252, min_periods=126).mean(), 504)
    r = _z(_f33_roic_level(roic, 252), 504)
    b = nm * r
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual-quality of returns: cash-vs-accrual margin spread momentum, ROIC-weighted level
def f33qc_f33_quality_compounder_accrqual_252d_base_v023_signal(fcf, netinc, revenue, roic):
    fm = _f33_fcf_margin(fcf, revenue, 126)
    nm = (netinc / revenue.replace(0, np.nan)).rolling(126, min_periods=63).mean()
    spread = fm - nm
    mom = spread - spread.shift(126)
    r = _f33_roic_level(roic, 252).clip(lower=0.0)
    b = mom * np.sqrt(r.abs() + 0.01)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- capital efficiency x return ---

# capital turnover x ROIC (DuPont-style return decomposition composite)
def f33qc_f33_quality_compounder_turnroic_252d_base_v024_signal(revenue, equity, roic):
    t = _f33_capital_turnover(revenue, equity, 252)
    r = _f33_roic_level(roic, 252)
    b = t * r
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital turnover x buyback as interaction of de-trended terms (efficient + shrinking base)
def f33qc_f33_quality_compounder_turnbuyback_252d_base_v025_signal(revenue, equity, sharesbas):
    t = _z(_f33_capital_turnover(revenue, equity, 252), 504)
    buyback = _z(-_f33_dilution(sharesbas, 252), 504)
    b = t * buyback
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share growth x ROIC level (per-share top-line compounding at high returns)
def f33qc_f33_quality_compounder_revpsroic_504d_base_v026_signal(revenue, sharesbas, roic):
    rps = revenue / sharesbas.replace(0, np.nan)
    g = rps / rps.shift(504).replace(0, np.nan) - 1.0
    r = _f33_roic_level(roic, 252).clip(lower=0.0)
    b = np.sign(g) * (g.abs() ** 0.5) * np.tanh(5.0 * r)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF per share level x ROIC stability (durable cash-per-share compounder)
def f33qc_f33_quality_compounder_fcfpsstab_252d_base_v027_signal(fcf, sharesbas, roic):
    fps = (fcf / sharesbas.replace(0, np.nan)).rolling(252, min_periods=126).mean()
    stab = _f33_roic_stability(roic, 252)
    b = np.sign(fps) * np.sqrt(fps.abs()) * np.tanh(stab / 5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- durable-return composite & longer windows ---

# durable return: 504d ROIC level x (1 - 504d dilution), z-scored to break the trend
def f33qc_f33_quality_compounder_durable_504d_base_v028_signal(roic, sharesbas):
    r = _f33_roic_level(roic, 504)
    d = _f33_dilution(sharesbas, 504)
    b = _z(r * (1.0 - d.clip(-0.5, 0.9)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable cash return: 504d FCF-ROIC x reinvestment
def f33qc_f33_quality_compounder_durcash_504d_base_v029_signal(fcf, equity, netinc):
    cash = _f33_fcf_roic(fcf, equity, 504)
    reinv = _f33_reinvest_rate(fcf, netinc, 504)
    b = cash * reinv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5-year compounder: ROIC x revenue growth net of dilution
def f33qc_f33_quality_compounder_fiveyr_1260d_base_v030_signal(roic, revenue, sharesbas):
    r = _f33_roic_level(roic, 252)
    g = _f33_revgrowth(revenue, 1260)
    d = _f33_dilution(sharesbas, 1260)
    b = r * (1.0 + g.clip(-0.9, 5.0)) - d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC premium over its own multi-year baseline times retention
def f33qc_f33_quality_compounder_roicprem_504d_base_v031_signal(roic, fcf, netinc):
    r = _f33_roic_level(roic, 126)
    base = _f33_roic_level(roic, 504)
    reinv = _f33_reinvest_rate(fcf, netinc, 252)
    b = (r - base) * reinv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quality-minus-dilution: rank of ROIC minus rank of dilution (rank-space QMD)
def f33qc_f33_quality_compounder_qmdrank_504d_base_v032_signal(roic, sharesbas):
    rr = _rank(_f33_roic_level(roic, 252), 504)
    dr = _rank(_f33_dilution(sharesbas, 252), 504)
    b = rr - dr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-ROIC x capital turnover interaction, de-trended (cash-return DuPont)
def f33qc_f33_quality_compounder_cashdupont_252d_base_v033_signal(fcf, equity, revenue):
    cash = _z(_f33_fcf_roic(fcf, equity, 252), 504)
    t = _z(_f33_capital_turnover(revenue, equity, 252), 504)
    b = cash * t
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment x ROIC stability (steady high-return reinvestor)
def f33qc_f33_quality_compounder_steadyreinv_252d_base_v034_signal(roic, fcf, netinc):
    stab = _f33_roic_stability(roic, 252)
    reinv = _f33_reinvest_rate(fcf, netinc, 252)
    b = np.tanh(stab / 5.0) * reinv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net issuance drag on high returns: ROIC level gated by SIGN of 3yr issuance (regime split)
def f33qc_f33_quality_compounder_issuedrag_756d_base_v035_signal(roic, sharesbas):
    r = _f33_roic_level(roic, 252)
    iss = _f33_dilution(sharesbas, 756)
    b = r * np.where(iss > 0, -1.0, 1.0)
    result = pd.Series(b, index=r.index)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth x FCF-ROIC minus dilution, all standardized (full compounding triple)
def f33qc_f33_quality_compounder_triple_504d_base_v036_signal(revenue, fcf, equity, sharesbas):
    g = _z(_f33_revgrowth(revenue, 504), 252)
    cash = _z(_f33_fcf_roic(fcf, equity, 252), 252)
    d = _z(_f33_dilution(sharesbas, 504), 252)
    b = g * cash - d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROE-minus-ROIC quality spread net of dilution (return-source quality, de-trended)
def f33qc_f33_quality_compounder_roeroicdil_252d_base_v037_signal(netinc, equity, roic, sharesbas):
    roe = (netinc / equity.replace(0, np.nan)).rolling(252, min_periods=126).mean()
    r = _f33_roic_level(roic, 252)
    d = _f33_dilution(sharesbas, 252)
    b = _z(roe - r, 504) - _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-on-capital consistency hit-rate x reinvestment
def f33qc_f33_quality_compounder_hitreinv_252d_base_v038_signal(roic, fcf, netinc):
    pos = (roic > roic.rolling(252, min_periods=126).median()).astype(float)
    hit = pos.rolling(252, min_periods=126).mean()
    reinv = _f33_reinvest_rate(fcf, netinc, 252)
    b = hit * reinv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash compounder: FCF margin x capital turnover, de-trended (cash generation x efficiency)
def f33qc_f33_quality_compounder_cashgenturn_252d_base_v039_signal(fcf, revenue, equity):
    fm = _z(_f33_fcf_margin(fcf, revenue, 252), 504)
    t = _z(_f33_capital_turnover(revenue, equity, 252), 504)
    b = fm * t
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC above hurdle (8%) x reinvestment (value-creating reinvestment)
def f33qc_f33_quality_compounder_hurdle_252d_base_v040_signal(roic, fcf, netinc):
    excess = (_f33_roic_level(roic, 252) - 0.08).clip(lower=0)
    reinv = _f33_reinvest_rate(fcf, netinc, 252).clip(lower=0)
    b = excess * reinv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# economic-profit proxy: (ROIC - cost) x equity-growth interaction (value created by growth)
def f33qc_f33_quality_compounder_econprofit_504d_base_v041_signal(roic, equity):
    spread = _f33_roic_level(roic, 252) - 0.08
    eqg = _z(_f33_revgrowth(equity, 252), 504)
    b = spread * eqg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-ROIC momentum gated by low dilution (improving cash return + clean cap structure)
def f33qc_f33_quality_compounder_cashmomgate_252d_base_v042_signal(fcf, equity, sharesbas):
    cash = _f33_fcf_roic(fcf, equity, 126)
    mom = cash - cash.shift(252)
    d = _f33_dilution(sharesbas, 252)
    b = mom * (1.0 - d.clip(-0.5, 0.5))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quality-minus-dilution: displacement of QMD from its slow EMA (regime-shift signal)
def f33qc_f33_quality_compounder_qmdema_252d_base_v043_signal(roic, sharesbas):
    r = _f33_roic_level(roic, 126)
    d = _f33_dilution(sharesbas, 252)
    qmd = r - d
    b = qmd - qmd.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-per-share compounding x FCF margin interaction (per-share cash compounding)
def f33qc_f33_quality_compounder_revpsfcf_504d_base_v044_signal(revenue, sharesbas, fcf):
    rps = revenue / sharesbas.replace(0, np.nan)
    g = _z(rps / rps.shift(504).replace(0, np.nan) - 1.0, 252)
    fm = _z(_f33_fcf_margin(fcf, revenue, 252), 252)
    b = g * fm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC interacted with net buyback yield, both de-trended (returns x share shrink)
def f33qc_f33_quality_compounder_roicbbz_252d_base_v045_signal(roic, sharesbas):
    r = _z(_f33_roic_level(roic, 126), 252)
    bb = _z(-_f33_dilution(sharesbas, 252), 252)
    b = r * bb
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-return composite: stability x level x anti-dilution, z-scored (triple quality)
def f33qc_f33_quality_compounder_durtriple_252d_base_v046_signal(roic, sharesbas):
    lvl = _f33_roic_level(roic, 252)
    stab = np.tanh(_f33_roic_stability(roic, 252) / 5.0)
    bb = (1.0 - _f33_dilution(sharesbas, 252).clip(-0.5, 0.9))
    b = _z(lvl * stab * bb, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-return spread vs revenue intensity, de-trended (FCF-ROIC minus FCF-margin tradeoff)
def f33qc_f33_quality_compounder_cashspread_252d_base_v047_signal(fcf, equity, revenue):
    cash = _z(_f33_fcf_roic(fcf, equity, 252), 504)
    fm = _z(_f33_fcf_margin(fcf, revenue, 252), 504)
    b = cash - fm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate change x ROIC (accelerating reinvestment at high returns)
def f33qc_f33_quality_compounder_reinvaccel_252d_base_v048_signal(fcf, netinc, roic):
    reinv = _f33_reinvest_rate(fcf, netinc, 126)
    chg = reinv - reinv.shift(252)
    r = _f33_roic_level(roic, 252)
    b = chg * (1.0 + r.clip(-0.5, 1.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compounder score percentile: interaction of ROIC-rank and reinvest-rank
def f33qc_f33_quality_compounder_comprank_504d_base_v049_signal(roic, fcf, netinc):
    rr = _rank(_f33_roic_level(roic, 126), 504)
    reinvr = _rank(_f33_reinvest_rate(fcf, netinc, 252), 504)
    b = (rr + 0.5) * (reinvr + 0.5) - 0.25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income per share growth x ROIC (per-share earnings compounding)
def f33qc_f33_quality_compounder_epsroic_504d_base_v050_signal(netinc, sharesbas, roic):
    eps = netinc / sharesbas.replace(0, np.nan)
    g = eps / eps.shift(504).replace(0, np.nan) - 1.0
    r = _f33_roic_level(roic, 252)
    b = g.clip(-2.0, 5.0) * (1.0 + r.clip(-0.5, 1.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF growth funded compounding: FCF growth x ROIC net of dilution
def f33qc_f33_quality_compounder_fcfgrowqmd_504d_base_v051_signal(fcf, roic, sharesbas):
    fg = _roc(fcf.rolling(63, min_periods=21).mean(), 504)
    r = _f33_roic_level(roic, 252)
    d = _f33_dilution(sharesbas, 504)
    b = fg.clip(-3.0, 5.0) * (1.0 + r.clip(-0.5, 1.0)) - d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-value-per-share growth x ROIC interaction, de-trended (per-share book compounding)
def f33qc_f33_quality_compounder_bvpsroic_504d_base_v052_signal(equity, sharesbas, roic):
    bvps = equity / sharesbas.replace(0, np.nan)
    g = _z(bvps / bvps.shift(504).replace(0, np.nan) - 1.0, 252)
    r = _z(_f33_roic_level(roic, 252), 252)
    b = g * r
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quality-minus-dilution acceleration (second difference of QMD)
def f33qc_f33_quality_compounder_qmdmom_504d_base_v053_signal(roic, sharesbas):
    r = _f33_roic_level(roic, 126)
    d = _f33_dilution(sharesbas, 126)
    qmd = r - d
    chg = qmd - qmd.shift(126)
    b = chg - chg.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-ROIC x reinvestment minus dilution (full cash compounding net of issuance)
def f33qc_f33_quality_compounder_cashcompnet_252d_base_v054_signal(fcf, equity, netinc, sharesbas):
    cash = _f33_fcf_roic(fcf, equity, 252)
    reinv = _f33_reinvest_rate(fcf, netinc, 252)
    d = _f33_dilution(sharesbas, 252)
    b = cash * reinv - d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC x revenue-growth consistency interaction, de-trended (durable growth at high returns)
def f33qc_f33_quality_compounder_durgrow_504d_base_v055_signal(roic, revenue):
    g21 = _f33_revgrowth(revenue, 252)
    consist = g21.rolling(504, min_periods=252).mean() / g21.rolling(504, min_periods=252).std().replace(0, np.nan)
    r = _z(_f33_roic_level(roic, 252), 504)
    b = np.tanh(consist) * r
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-light high-return: ROIC x (revenue/equity) percentile (asset-light compounder)
def f33qc_f33_quality_compounder_capliterank_252d_base_v056_signal(roic, revenue, equity):
    t = _f33_capital_turnover(revenue, equity, 252)
    r = _f33_roic_level(roic, 252)
    b = _rank(t, 504) + _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# free cash flow conversion x ROIC interaction, de-trended (cash-backed returns)
def f33qc_f33_quality_compounder_fcfconvroic_252d_base_v057_signal(fcf, netinc, roic):
    conv = (fcf / netinc.replace(0, np.nan)).clip(-3.0, 3.0).rolling(252, min_periods=126).mean()
    convz = _z(conv, 504)
    r = _z(_f33_roic_level(roic, 252), 504)
    b = convz * r
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback-adjusted ROIC trend (improving returns + shrinking base)
def f33qc_f33_quality_compounder_roictrendbb_504d_base_v058_signal(roic, sharesbas):
    rtrend = _f33_roic_level(roic, 126) - _f33_roic_level(roic, 504)
    bb = -_f33_dilution(sharesbas, 504)
    b = rtrend + 0.5 * bb
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# economic moat proxy: ROIC stability x FCF margin (durable cash-rich returns)
def f33qc_f33_quality_compounder_moat_252d_base_v059_signal(roic, fcf, revenue):
    stab = np.tanh(_f33_roic_stability(roic, 252) / 5.0)
    fm = _f33_fcf_margin(fcf, revenue, 252)
    b = stab * fm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-funded growth at high ROIC minus dilution, standardized components
def f33qc_f33_quality_compounder_reinvgrowqmd_504d_base_v060_signal(roic, fcf, netinc, revenue, sharesbas):
    reinv = _z(_f33_reinvest_rate(fcf, netinc, 252), 504)
    g = _z(_f33_revgrowth(revenue, 504), 504)
    r = _z(_f33_roic_level(roic, 252), 504)
    d = _z(_f33_dilution(sharesbas, 504), 504)
    b = (reinv + g + r) / 3.0 - d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash return on equity minus share growth, ranked (cash quality-minus-dilution)
def f33qc_f33_quality_compounder_fcfroeqmdrank_252d_base_v061_signal(fcf, equity, sharesbas):
    cash = _f33_fcf_roic(fcf, equity, 252)
    d = _f33_dilution(sharesbas, 252)
    b = _rank(cash - d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sustainable-growth DuPont: retention x turnover gated by ROIC sign-regime
def f33qc_f33_quality_compounder_sgrdupont_252d_base_v062_signal(roic, fcf, netinc, revenue, equity):
    r = _f33_roic_level(roic, 252)
    reinv = _f33_reinvest_rate(fcf, netinc, 252)
    t = _f33_capital_turnover(revenue, equity, 252)
    above = np.sign(r - r.rolling(504, min_periods=126).median())
    b = reinv * np.tanh(t) * above
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# divergence: high ROIC but rising share count (signed product warning gate)
def f33qc_f33_quality_compounder_qualdildiv_252d_base_v063_signal(roic, sharesbas):
    r = _z(_f33_roic_level(roic, 252), 504)
    d = _f33_dilution(sharesbas, 252)
    # large positive when ROIC high AND diluting (the divergence), else damped
    b = r * np.tanh(10.0 * d)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-ROIC x revenue-per-share-growth interaction, de-trended (cash returns + per-share growth)
def f33qc_f33_quality_compounder_cashrevps_504d_base_v064_signal(fcf, equity, revenue, sharesbas):
    cash = _z(_f33_fcf_roic(fcf, equity, 252), 252)
    rps = revenue / sharesbas.replace(0, np.nan)
    g = _z(rps / rps.shift(504).replace(0, np.nan) - 1.0, 252)
    b = cash * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compounding stability: low dispersion of (ROIC x reinvest) -> high score
def f33qc_f33_quality_compounder_compstab_252d_base_v065_signal(roic, fcf, netinc):
    r = roic.rolling(63, min_periods=21).mean()
    reinv = 1.0 - (fcf / netinc.replace(0, np.nan)).clip(-3, 3)
    comp = r * reinv
    m = comp.rolling(252, min_periods=126).mean()
    sd = comp.rolling(252, min_periods=126).std()
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC-funded buyback capacity: FCF margin x buyback-yield interaction (cash returned via shrink)
def f33qc_f33_quality_compounder_buybackcap_252d_base_v066_signal(fcf, revenue, sharesbas):
    fm = _z(_f33_fcf_margin(fcf, revenue, 252), 504)
    bb = _z(-_f33_dilution(sharesbas, 252), 504)
    b = fm * bb
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon ROIC agreement net of dilution (consistent compounder)
def f33qc_f33_quality_compounder_roicagree_504d_base_v067_signal(roic, sharesbas):
    r1 = _f33_roic_level(roic, 126)
    r2 = _f33_roic_level(roic, 504)
    agree = 1.0 - (r1 - r2).abs() / (r1.abs() + r2.abs()).replace(0, np.nan)
    d = _f33_dilution(sharesbas, 252)
    b = agree * (1.0 - d.clip(-0.5, 0.9))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash compounding momentum: FCF-ROIC x reinvest, year-over-year change
def f33qc_f33_quality_compounder_cashcompmom_504d_base_v068_signal(fcf, equity, netinc):
    cash = _f33_fcf_roic(fcf, equity, 252)
    reinv = _f33_reinvest_rate(fcf, netinc, 252)
    comp = cash * reinv
    b = comp - comp.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# high-return self-funding: ROIC minus required reinvestment for growth (excess return)
def f33qc_f33_quality_compounder_selffund_504d_base_v069_signal(roic, revenue, equity):
    r = _f33_roic_level(roic, 252)
    g = _f33_revgrowth(revenue, 504)
    needed = g * _f33_capital_turnover(revenue, equity, 252).rdiv(1.0)
    b = r - needed.clip(-1.0, 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# normalized compounder: tanh(ROIC x reinvest) minus dilution penalty
def f33qc_f33_quality_compounder_tanhcomp_252d_base_v070_signal(roic, fcf, netinc, sharesbas):
    r = _f33_roic_level(roic, 252)
    reinv = _f33_reinvest_rate(fcf, netinc, 252)
    d = _f33_dilution(sharesbas, 252)
    b = np.tanh(3.0 * r * reinv) - d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-ROIC dispersion-adjusted level minus dilution, ranked (risk-adjusted cash compounder)
def f33qc_f33_quality_compounder_riskadjcash_252d_base_v071_signal(fcf, equity, sharesbas):
    cash = fcf / equity.replace(0, np.nan)
    m = cash.rolling(252, min_periods=126).mean()
    sd = cash.rolling(252, min_periods=126).std()
    ra = m / (1.0 + sd.abs())
    d = _f33_dilution(sharesbas, 252)
    b = _rank(ra, 504) - _rank(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-quality blend: de-trended revenue-growth x net-margin interaction minus dilution
def f33qc_f33_quality_compounder_growqualblend_504d_base_v072_signal(revenue, netinc, sharesbas):
    g = _z(_f33_revgrowth(revenue, 504), 252)
    nm = _z((netinc / revenue.replace(0, np.nan)).rolling(252, min_periods=126).mean(), 252)
    d = _z(_f33_dilution(sharesbas, 504), 252)
    b = g * nm - 0.5 * d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compounder regime persistence: fraction of last 2y where QMD>0
def f33qc_f33_quality_compounder_qmdpersist_504d_base_v073_signal(roic, sharesbas):
    r = _f33_roic_level(roic, 126)
    d = _f33_dilution(sharesbas, 126)
    qmd = r - d
    pos = (qmd > 0).astype(float)
    b = pos.rolling(504, min_periods=252).mean() * (0.5 + qmd.clip(-0.5, 0.5))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net cash return to owners: (FCF margin - dilution) x ROIC stability
def f33qc_f33_quality_compounder_netownerret_252d_base_v074_signal(fcf, revenue, sharesbas, roic):
    fm = _f33_fcf_margin(fcf, revenue, 252)
    d = _f33_dilution(sharesbas, 252)
    stab = np.tanh(_f33_roic_stability(roic, 252) / 5.0)
    b = (fm - d) * stab
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# full compounder index: average of standardized ROIC, FCF-ROIC, reinvest, anti-dilution
def f33qc_f33_quality_compounder_index_252d_base_v075_signal(roic, fcf, equity, netinc, sharesbas):
    a = _z(_f33_roic_level(roic, 252), 504)
    c = _z(_f33_fcf_roic(fcf, equity, 252), 504)
    e = _z(_f33_reinvest_rate(fcf, netinc, 252), 504)
    f = _z(-_f33_dilution(sharesbas, 252), 504)
    b = (a + c + e + f) / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f33qc_f33_quality_compounder_qmd_252d_base_v001_signal,
    f33qc_f33_quality_compounder_stabdil_252d_base_v002_signal,
    f33qc_f33_quality_compounder_roicbuyback_252d_base_v003_signal,
    f33qc_f33_quality_compounder_roicpershare_504d_base_v004_signal,
    f33qc_f33_quality_compounder_qmdz_252d_base_v005_signal,
    f33qc_f33_quality_compounder_dualrank_252d_base_v006_signal,
    f33qc_f33_quality_compounder_fcfroic_252d_base_v007_signal,
    f33qc_f33_quality_compounder_blendroic_252d_base_v008_signal,
    f33qc_f33_quality_compounder_cashconv_252d_base_v009_signal,
    f33qc_f33_quality_compounder_fcfroicgrow_504d_base_v010_signal,
    f33qc_f33_quality_compounder_fcfroicstab_252d_base_v011_signal,
    f33qc_f33_quality_compounder_fcfroicdil_252d_base_v012_signal,
    f33qc_f33_quality_compounder_compound_252d_base_v013_signal,
    f33qc_f33_quality_compounder_sustgrow_252d_base_v014_signal,
    f33qc_f33_quality_compounder_reinvgrow_504d_base_v015_signal,
    f33qc_f33_quality_compounder_reinveff_504d_base_v016_signal,
    f33qc_f33_quality_compounder_reinvqual_252d_base_v017_signal,
    f33qc_f33_quality_compounder_bookcompound_504d_base_v018_signal,
    f33qc_f33_quality_compounder_fcfmgnroic_252d_base_v019_signal,
    f33qc_f33_quality_compounder_fcfmgndil_252d_base_v020_signal,
    f33qc_f33_quality_compounder_fcfmgngrow_504d_base_v021_signal,
    f33qc_f33_quality_compounder_netmgnroic_252d_base_v022_signal,
    f33qc_f33_quality_compounder_accrqual_252d_base_v023_signal,
    f33qc_f33_quality_compounder_turnroic_252d_base_v024_signal,
    f33qc_f33_quality_compounder_turnbuyback_252d_base_v025_signal,
    f33qc_f33_quality_compounder_revpsroic_504d_base_v026_signal,
    f33qc_f33_quality_compounder_fcfpsstab_252d_base_v027_signal,
    f33qc_f33_quality_compounder_durable_504d_base_v028_signal,
    f33qc_f33_quality_compounder_durcash_504d_base_v029_signal,
    f33qc_f33_quality_compounder_fiveyr_1260d_base_v030_signal,
    f33qc_f33_quality_compounder_roicprem_504d_base_v031_signal,
    f33qc_f33_quality_compounder_qmdrank_504d_base_v032_signal,
    f33qc_f33_quality_compounder_cashdupont_252d_base_v033_signal,
    f33qc_f33_quality_compounder_steadyreinv_252d_base_v034_signal,
    f33qc_f33_quality_compounder_issuedrag_756d_base_v035_signal,
    f33qc_f33_quality_compounder_triple_504d_base_v036_signal,
    f33qc_f33_quality_compounder_roeroicdil_252d_base_v037_signal,
    f33qc_f33_quality_compounder_hitreinv_252d_base_v038_signal,
    f33qc_f33_quality_compounder_cashgenturn_252d_base_v039_signal,
    f33qc_f33_quality_compounder_hurdle_252d_base_v040_signal,
    f33qc_f33_quality_compounder_econprofit_504d_base_v041_signal,
    f33qc_f33_quality_compounder_cashmomgate_252d_base_v042_signal,
    f33qc_f33_quality_compounder_qmdema_252d_base_v043_signal,
    f33qc_f33_quality_compounder_revpsfcf_504d_base_v044_signal,
    f33qc_f33_quality_compounder_roicbbz_252d_base_v045_signal,
    f33qc_f33_quality_compounder_durtriple_252d_base_v046_signal,
    f33qc_f33_quality_compounder_cashspread_252d_base_v047_signal,
    f33qc_f33_quality_compounder_reinvaccel_252d_base_v048_signal,
    f33qc_f33_quality_compounder_comprank_504d_base_v049_signal,
    f33qc_f33_quality_compounder_epsroic_504d_base_v050_signal,
    f33qc_f33_quality_compounder_fcfgrowqmd_504d_base_v051_signal,
    f33qc_f33_quality_compounder_bvpsroic_504d_base_v052_signal,
    f33qc_f33_quality_compounder_qmdmom_504d_base_v053_signal,
    f33qc_f33_quality_compounder_cashcompnet_252d_base_v054_signal,
    f33qc_f33_quality_compounder_durgrow_504d_base_v055_signal,
    f33qc_f33_quality_compounder_capliterank_252d_base_v056_signal,
    f33qc_f33_quality_compounder_fcfconvroic_252d_base_v057_signal,
    f33qc_f33_quality_compounder_roictrendbb_504d_base_v058_signal,
    f33qc_f33_quality_compounder_moat_252d_base_v059_signal,
    f33qc_f33_quality_compounder_reinvgrowqmd_504d_base_v060_signal,
    f33qc_f33_quality_compounder_fcfroeqmdrank_252d_base_v061_signal,
    f33qc_f33_quality_compounder_sgrdupont_252d_base_v062_signal,
    f33qc_f33_quality_compounder_qualdildiv_252d_base_v063_signal,
    f33qc_f33_quality_compounder_cashrevps_504d_base_v064_signal,
    f33qc_f33_quality_compounder_compstab_252d_base_v065_signal,
    f33qc_f33_quality_compounder_buybackcap_252d_base_v066_signal,
    f33qc_f33_quality_compounder_roicagree_504d_base_v067_signal,
    f33qc_f33_quality_compounder_cashcompmom_504d_base_v068_signal,
    f33qc_f33_quality_compounder_selffund_504d_base_v069_signal,
    f33qc_f33_quality_compounder_tanhcomp_252d_base_v070_signal,
    f33qc_f33_quality_compounder_riskadjcash_252d_base_v071_signal,
    f33qc_f33_quality_compounder_growqualblend_504d_base_v072_signal,
    f33qc_f33_quality_compounder_qmdpersist_504d_base_v073_signal,
    f33qc_f33_quality_compounder_netownerret_252d_base_v074_signal,
    f33qc_f33_quality_compounder_index_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_QUALITY_COMPOUNDER_REGISTRY_001_075 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
    n = 1500
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    roic = _fund(101, base=0.15, drift=0.01, vol=0.20, allow_neg=True).rename("roic")
    fcf = _fund(102, base=5e7, drift=0.02, vol=0.06, allow_neg=True).rename("fcf")
    sharesbas = _fund(103, base=1e8, drift=0.005, vol=0.02).rename("sharesbas")
    revenue = _fund(104, base=5e8, drift=0.02, vol=0.04).rename("revenue")
    equity = _fund(105, base=4e8, drift=0.015, vol=0.04).rename("equity")
    netinc = _fund(106, base=6e7, drift=0.02, vol=0.07, allow_neg=True).rename("netinc")

    cols = {"roic": roic, "fcf": fcf, "sharesbas": sharesbas,
            "revenue": revenue, "equity": equity, "netinc": netinc}

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

    print("OK f33_quality_compounder_base_001_075_claude: %d features pass" % n_features)
