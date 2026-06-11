import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (cash burn / runway) =====
def _f31_burn_opex(opex, ncfo):
    # operational burn: opex not covered by operating cash flow, floored at 0
    return (opex - ncfo).clip(lower=0)


def _f31_burn_fcf(ncfo, capex):
    # free-cash burn: negative free cash (-ncfo - capex), floored at 0
    return (-ncfo - capex).clip(lower=0)


def _f31_runway_opex(cashneq, opex, ncfo):
    # months of cash at opex-burn rate (annual->months via *12)
    burn = _f31_burn_opex(opex, ncfo)
    return cashneq / burn.replace(0, np.nan) * 12.0


def _f31_runway_fcf(cashneq, ncfo, capex):
    # months of cash at free-cash burn rate
    burn = _f31_burn_fcf(ncfo, capex)
    return cashneq / burn.replace(0, np.nan) * 12.0


def _f31_coverage(ncfo, opex):
    # how much of opex operating cash flow covers
    return ncfo / opex.replace(0, np.nan)


def _f31_logwarp(s):
    return np.sign(s) * np.log1p(s.abs())


# ============================================================
# --- runway level (opex-burn) ---
def f31cr_f31_cash_burn_runway_runwayopx_252d_base_v001_signal(cashneq, opex, ncfo):
    b = _f31_runway_opex(cashneq, opex, ncfo)
    result = _mean(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# runway (fcf-burn) level
def f31cr_f31_cash_burn_runway_runwayfcf_252d_base_v002_signal(cashneq, ncfo, capex):
    b = _f31_runway_fcf(cashneq, ncfo, capex)
    result = _mean(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# log-warped opex-runway level (compress heavy tail)
def f31cr_f31_cash_burn_runway_runwaylog_126d_base_v003_signal(cashneq, opex, ncfo):
    b = _f31_runway_opex(cashneq, opex, ncfo)
    result = _mean(_f31_logwarp(b), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# runway-improvement streak: consecutive months runway rose, normalized (count facet)
def f31cr_f31_cash_burn_runway_invrunway_252d_base_v004_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    up = (rw > rw.shift(1)).astype(float)
    grp = (up == 0).cumsum()
    streak = up.groupby(grp).cumcount() + 1
    streak = streak.where(up == 1, 0.0)
    result = streak.rolling(252, min_periods=126).mean() / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


# short-runway distress momentum: how fast the (18mo - runway) shortfall is widening
def f31cr_f31_cash_burn_runway_shortdist_126d_base_v005_signal(cashneq, opex, ncfo):
    short = (18.0 - _f31_runway_opex(cashneq, opex, ncfo)).clip(lower=0)
    sm = short.ewm(span=42, min_periods=21).mean()
    result = sm - sm.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- burn rate level ---
# opex-burn magnitude (log-scaled level)
def f31cr_f31_cash_burn_runway_burnopx_126d_base_v006_signal(opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    result = _mean(np.log1p(burn), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# free-cash-burn magnitude (log-scaled level)
def f31cr_f31_cash_burn_runway_burnfcf_126d_base_v007_signal(ncfo, capex):
    burn = _f31_burn_fcf(ncfo, capex)
    result = _mean(np.log1p(burn), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# burn intensity de-trended: burn/cash z-scored vs its own 252d history
def f31cr_f31_cash_burn_runway_burnintens_252d_base_v008_signal(cashneq, opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    b = burn / cashneq.replace(0, np.nan)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# free-cash-burn intensity de-trended: fcf-burn/cash z-scored vs own 252d history
def f31cr_f31_cash_burn_runway_burnintfcf_252d_base_v009_signal(cashneq, ncfo, capex):
    burn = _f31_burn_fcf(ncfo, capex)
    b = burn / cashneq.replace(0, np.nan)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# burn-to-opex ratio: fraction of opex that is cash-burning (uncovered)
def f31cr_f31_cash_burn_runway_burnfrac_126d_base_v010_signal(opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    b = burn / opex.replace(0, np.nan)
    result = _mean(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# --- coverage ---
# operating-cash coverage of opex (ncfo/opex), self-funding gauge
def f31cr_f31_cash_burn_runway_cover_252d_base_v011_signal(ncfo, opex):
    b = _f31_coverage(ncfo, opex)
    result = _mean(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# coverage-shortfall worsening: how much the break-even gap widened over a quarter
def f31cr_f31_cash_burn_runway_covergap_126d_base_v012_signal(ncfo, opex):
    gap = (1.0 - _f31_coverage(ncfo, opex)).clip(lower=0)
    sm = gap.ewm(span=42, min_periods=21).mean()
    result = sm - sm.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# cash-vs-burn coverage: cash percentile-ranked against blended (opex+fcf) burn level
def f31cr_f31_cash_burn_runway_cashcover_252d_base_v013_signal(cashneq, ncfo, capex, opex):
    blended = 0.5 * _f31_burn_fcf(ncfo, capex) + 0.5 * _f31_burn_opex(opex, ncfo)
    cov = cashneq / blended.replace(0, np.nan)
    result = _rank(cov, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# operating cash flow vs capex coverage trend (improving/worsening over a half-year)
def f31cr_f31_cash_burn_runway_ocfcapex_252d_base_v014_signal(ncfo, capex):
    b = ncfo / capex.abs().replace(0, np.nan)
    sm = b.ewm(span=63, min_periods=21).mean()
    result = sm - sm.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# --- z-scored levels (de-trended) ---
# opex-runway position within its own 252d high-low range (0=floor, 1=ceiling)
def f31cr_f31_cash_burn_runway_runwayz_252d_base_v015_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    lo = _rmin(rw, 252)
    hi = _rmax(rw, 252)
    result = (rw - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# burn-intensity z vs own 126d history
def f31cr_f31_cash_burn_runway_burnz_126d_base_v016_signal(cashneq, opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    b = burn / cashneq.replace(0, np.nan)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# coverage z vs own 252d history
def f31cr_f31_cash_burn_runway_coverz_252d_base_v017_signal(ncfo, opex):
    b = _f31_coverage(ncfo, opex)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq level z vs own 252d history (cash drawdown gauge)
def f31cr_f31_cash_burn_runway_cashz_252d_base_v018_signal(cashneq):
    result = _z(cashneq, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# --- percentile ranks ---
# opex-runway acceleration: second difference of runway over quarterly steps
def f31cr_f31_cash_burn_runway_runwayrank_504d_base_v019_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    result = (rw - rw.shift(63)) - (rw.shift(63) - rw.shift(126))
    return result.replace([np.inf, -np.inf], np.nan)


# burn-fraction percentile vs own 252d history
def f31cr_f31_cash_burn_runway_burnfracrank_252d_base_v020_signal(opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    b = burn / opex.replace(0, np.nan)
    result = _rank(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# coverage acceleration: change in coverage trend (is self-funding inflecting)
def f31cr_f31_cash_burn_runway_coverrank_504d_base_v021_signal(ncfo, opex):
    b = _f31_coverage(ncfo, opex)
    fast = b - b.shift(63)
    slow = b.shift(63) - b.shift(126)
    result = fast - slow
    return result.replace([np.inf, -np.inf], np.nan)


# --- runway trend (slope-as-level facets, distinct from derivative files) ---
# runway change over a quarter (deteriorating/improving runway)
def f31cr_f31_cash_burn_runway_runwaychg_63d_base_v022_signal(cashneq, opex, ncfo):
    b = _f31_runway_opex(cashneq, opex, ncfo)
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# runway log-growth over a half-year
def f31cr_f31_cash_burn_runway_runwaygro_126d_base_v023_signal(cashneq, opex, ncfo):
    b = _f31_runway_opex(cashneq, opex, ncfo).clip(lower=0)
    result = np.log1p(b) - np.log1p(b.shift(126))
    return result.replace([np.inf, -np.inf], np.nan)


# cash balance log-growth over a quarter (cash trajectory)
def f31cr_f31_cash_burn_runway_cashgro_63d_base_v024_signal(cashneq):
    result = np.log(cashneq.replace(0, np.nan) / cashneq.shift(63).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# burn-rate change over a quarter (burn acceleration as level)
def f31cr_f31_cash_burn_runway_burnchg_63d_base_v025_signal(opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    lw = np.log1p(burn)
    result = lw - lw.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# coverage trend over a half-year
def f31cr_f31_cash_burn_runway_coverchg_126d_base_v026_signal(ncfo, opex):
    b = _f31_coverage(ncfo, opex)
    result = b - b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# --- ratios short vs long window ---
# runway short(63d-mean) relative to long(252d-mean) (near-term vs structural)
def f31cr_f31_cash_burn_runway_runwaysl_base_v027_signal(cashneq, opex, ncfo):
    b = _f31_runway_opex(cashneq, opex, ncfo)
    s = _mean(b, 63)
    l = _mean(b, 252)
    result = s / l.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# burn short vs long ratio (recent burn intensification)
def f31cr_f31_cash_burn_runway_burnsl_base_v028_signal(opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    s = _mean(burn, 63)
    l = _mean(burn, 252)
    result = s / l.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash short vs long mean ratio (cash level momentum)
def f31cr_f31_cash_burn_runway_cashsl_base_v029_signal(cashneq):
    s = _mean(cashneq, 63)
    l = _mean(cashneq, 252)
    result = s / l.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# --- dispersion / stability ---
# runway volatility (instability of cash-life estimate)
def f31cr_f31_cash_burn_runway_runwayvol_252d_base_v030_signal(cashneq, opex, ncfo):
    b = _f31_runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    sd = _std(b, 252)
    mn = _mean(b, 252).abs()
    result = sd / mn.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# burn-rate volatility (lumpy burn)
def f31cr_f31_cash_burn_runway_burnvol_126d_base_v031_signal(opex, ncfo):
    burn = np.log1p(_f31_burn_opex(opex, ncfo))
    result = _std(burn, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# coverage volatility (erratic self-funding)
def f31cr_f31_cash_burn_runway_covervol_252d_base_v032_signal(ncfo, opex):
    b = _f31_coverage(ncfo, opex)
    result = _std(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# --- regime / count-friendly ---
# fraction of last year with elevated burn (opex-burn above its 252d median)
def f31cr_f31_cash_burn_runway_burndays_252d_base_v033_signal(opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    med = burn.rolling(252, min_periods=126).median()
    hot = (burn > med).astype(float)
    result = hot.rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# longest consecutive negative-operating-cash streak over the last year (count facet)
def f31cr_f31_cash_burn_runway_negocf_252d_base_v034_signal(ncfo):
    neg = (ncfo < 0).astype(float)
    grp = (neg == 0).cumsum()
    streak = neg.groupby(grp).cumcount() + 1
    streak = streak.where(neg == 1, 0.0)
    result = streak.rolling(252, min_periods=126).max() / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year with runway below 12 months (critical-runway regime)
def f31cr_f31_cash_burn_runway_critdays_252d_base_v035_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo)
    crit = ((rw < 12.0) & (rw.notna())).astype(float)
    result = crit.rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year with free-cash-burn positive (not self-funding capex)
def f31cr_f31_cash_burn_runway_fcfburndays_252d_base_v036_signal(ncfo, capex):
    burning = (_f31_burn_fcf(ncfo, capex) > 0).astype(float)
    result = burning.rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive rising-burn streak (run of months where burn keeps increasing), normalized
def f31cr_f31_cash_burn_runway_burnstreak_252d_base_v037_signal(opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    rising = (burn > burn.shift(1)).astype(float)
    grp = (rising == 0).cumsum()
    streak = rising.groupby(grp).cumcount() + 1
    streak = streak.where(rising == 1, 0.0)
    result = streak.rolling(252, min_periods=63).max() / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


# --- sign x magnitude / interactions ---
# burn intensity weighted by how short the runway is (compounding distress)
def f31cr_f31_cash_burn_runway_distress_126d_base_v038_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo)
    short = (1.0 / rw.clip(lower=1.0)).clip(upper=1.0)
    burn = _f31_burn_opex(opex, ncfo)
    intens = burn / cashneq.replace(0, np.nan)
    result = _mean(short * intens, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# runway times coverage (combined cash-life quality)
def f31cr_f31_cash_burn_runway_quality_252d_base_v039_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    cov = _f31_coverage(ncfo, opex)
    result = _mean(np.log1p(rw.clip(lower=0)) * (1.0 + cov.clip(-1.0, 2.0)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# bounded burn-rate momentum: tanh-squashed quarterly change in log burn
def f31cr_f31_cash_burn_runway_runwaytanh_63d_base_v040_signal(cashneq, opex, ncfo):
    burn = np.log1p(_f31_burn_opex(opex, ncfo))
    chg = burn - burn.shift(63)
    intens = (_f31_burn_opex(opex, ncfo) / cashneq.replace(0, np.nan)).clip(0, 2)
    result = np.tanh(2.0 * chg) * (0.5 + intens)
    return result.replace([np.inf, -np.inf], np.nan)


# --- fcf-runway facets ---
# fcf-runway z vs own 252d history
def f31cr_f31_cash_burn_runway_runwayfcfz_252d_base_v041_signal(cashneq, ncfo, capex):
    b = _f31_runway_fcf(cashneq, ncfo, capex)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# fcf-runway position within its own 252d high-low range (where in recent range)
def f31cr_f31_cash_burn_runway_runwayfcfrank_504d_base_v042_signal(cashneq, ncfo, capex):
    rw = _f31_runway_fcf(cashneq, ncfo, capex).clip(upper=120.0)
    lo = _rmin(rw, 252)
    hi = _rmax(rw, 252)
    result = (rw - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# fcf-runway change over a quarter
def f31cr_f31_cash_burn_runway_runwayfcfchg_63d_base_v043_signal(cashneq, ncfo, capex):
    b = _f31_runway_fcf(cashneq, ncfo, capex)
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# spread: opex-runway minus fcf-runway (capex drag on cash life)
def f31cr_f31_cash_burn_runway_runwayspr_252d_base_v044_signal(cashneq, opex, ncfo, capex):
    ro = _f31_runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    rf = _f31_runway_fcf(cashneq, ncfo, capex).clip(upper=120.0)
    result = _mean(ro - rf, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# --- capex intensity in burn context ---
# capex relative to opex-burn (investment as share of cash drain)
def f31cr_f31_cash_burn_runway_capexburn_126d_base_v045_signal(capex, opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    b = capex.abs() / (burn + capex.abs()).replace(0, np.nan)
    result = _mean(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex absorbed by operating cash (self-funded investment ratio)
def f31cr_f31_cash_burn_runway_capexselffund_252d_base_v046_signal(ncfo, capex):
    # normalize by |ncfo| scale to keep bounded
    b = (ncfo - capex.abs()) / ncfo.abs().replace(0, np.nan)
    result = _mean(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# --- financing in runway context (ncff) ---
# financing as a lifeline: ncff relative to opex-burn (raise covering burn)
def f31cr_f31_cash_burn_runway_finlifeline_252d_base_v047_signal(ncff, opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    b = ncff / (burn + 1.0)
    result = _mean(b.clip(-50, 50), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# financing-funded burn coverage trend: change in financing-share-of-burn over a quarter
def f31cr_f31_cash_burn_runway_finburn_252d_base_v048_signal(ncff, opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    raised = ncff.clip(lower=0)
    b = raised / (burn + raised).replace(0, np.nan)
    sm = b.ewm(span=42, min_periods=21).mean()
    result = sm - sm.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap: operating cash minus financing reliance (ncfo vs ncff)
def f31cr_f31_cash_burn_runway_selffundgap_252d_base_v049_signal(ncfo, ncff):
    denom = (ncfo.abs() + ncff.abs()).replace(0, np.nan)
    b = (ncfo - ncff) / denom
    result = _mean(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# empirical-vs-accounting runway divergence: realized cash drain faster/slower than burn implies
def f31cr_f31_cash_burn_runway_extrunway_252d_base_v050_signal(cashneq, ncff, opex, ncfo):
    # realized monthly cash drain from the 126d cash slope
    slope = (cashneq - cashneq.shift(126)) / 126.0
    realized_drain = (-slope * 21.0).clip(lower=0)
    # financing inflow offsets the operating burn that the firm must self-fund from cash
    net_burn = (_f31_burn_opex(opex, ncfo) - ncff.clip(lower=0)).clip(lower=0) / 12.0
    # >0 when cash is draining faster than financing-adjusted burn implies (extra leakage)
    div = (realized_drain - net_burn) / (net_burn.abs() + 1.0)
    result = _mean(np.tanh(div), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# --- more level facets ---
# cash balance relative to its own 504d max (cash drawdown from peak)
def f31cr_f31_cash_burn_runway_cashdd_504d_base_v051_signal(cashneq):
    peak = _rmax(cashneq, 504)
    result = cashneq / peak.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# burn drawup off its own 504d trough (how far burn has climbed from its low)
def f31cr_f31_cash_burn_runway_burnpeak_504d_base_v052_signal(opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    trough = _rmin(burn, 504)
    result = burn / trough.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# runway distance from its own 252d min (cushion above worst runway)
def f31cr_f31_cash_burn_runway_runwaycushion_252d_base_v053_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    floor = _rmin(rw, 252)
    result = rw - floor
    return result.replace([np.inf, -np.inf], np.nan)


# --- inverse-runway (burn-multiple style) ---
# burn-rate dispersion rank: variability of burn/cash ranked vs own 504d history
def f31cr_f31_cash_burn_runway_burnratepct_504d_base_v054_signal(cashneq, opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    rate = burn / cashneq.replace(0, np.nan)
    disp = _std(rate, 63)
    result = _rank(disp, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# burn-vs-capex mix trend: change in burn/capex spend share over a quarter
def f31cr_f31_cash_burn_runway_burnvscapex_126d_base_v055_signal(opex, ncfo, capex):
    burn = _f31_burn_opex(opex, ncfo)
    share = burn / (burn + capex.abs()).replace(0, np.nan)
    result = share - share.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- coverage break-even crossing / regime ---
# distance of coverage above break-even smoothed (self-funding surplus)
def f31cr_f31_cash_burn_runway_coversurplus_252d_base_v056_signal(ncfo, opex):
    surplus = (_f31_coverage(ncfo, opex) - 1.0)
    result = surplus.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# coverage stability: how steadily ncfo covers opex (1 - cv)
def f31cr_f31_cash_burn_runway_coverstab_252d_base_v057_signal(ncfo, opex):
    cov = _f31_coverage(ncfo, opex)
    sd = _std(cov, 252)
    mn = _mean(cov, 252).abs()
    result = -sd / mn.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# --- ncfo direct facets ---
# operating-cash margin instability: dispersion of ncfo/opex over a half-year
def f31cr_f31_cash_burn_runway_ocfopex_126d_base_v058_signal(ncfo, opex):
    b = ncfo / opex.replace(0, np.nan)
    result = _std(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# operating cash flow log-growth over a half-year (cash-generation trajectory)
def f31cr_f31_cash_burn_runway_ocfgro_126d_base_v059_signal(ncfo):
    lw = _f31_logwarp(ncfo)
    result = lw - lw.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo recovery off its own 504d trough (operating-cash rebound off the worst)
def f31cr_f31_cash_burn_runway_ocfz_252d_base_v060_signal(ncfo):
    trough = _rmin(ncfo, 504)
    span = _rmax(ncfo, 504) - trough
    result = (ncfo - trough) / span.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# --- runway in volatility units / risk-adjusted ---
# runway change per unit of runway volatility (signal-to-noise of deterioration)
def f31cr_f31_cash_burn_runway_runwaysnr_252d_base_v061_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    chg = rw - rw.shift(63)
    vol = _std(rw, 252)
    result = chg / vol.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# burn-intensity per unit of cash volatility
def f31cr_f31_cash_burn_runway_burnsnr_252d_base_v062_signal(cashneq, opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    intens = burn / cashneq.replace(0, np.nan)
    vol = _std(cashneq.pct_change(), 252)
    result = intens * (1.0 + vol.clip(0, 1))
    return result.replace([np.inf, -np.inf], np.nan)


# --- multi-window dispersion of runway ---
# runway disagreement across 63/126/252 mean windows
def f31cr_f31_cash_burn_runway_runwaydisp_base_v063_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    m1 = _mean(rw, 63)
    m2 = _mean(rw, 126)
    m3 = _mean(rw, 252)
    result = pd.concat([m1, m2, m3], axis=1).std(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# --- year-over-year runway change ---
# runway vs runway one year ago (structural deterioration)
def f31cr_f31_cash_burn_runway_runwayyoy_252d_base_v064_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo)
    result = np.log1p(rw.clip(lower=0)) - np.log1p(rw.shift(252).clip(lower=0))
    return result.replace([np.inf, -np.inf], np.nan)


# cash balance vs one year ago (annual cash burn-down)
def f31cr_f31_cash_burn_runway_cashyoy_252d_base_v065_signal(cashneq):
    result = cashneq / cashneq.shift(252).replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# --- combined survival score ---
# survival-score momentum: change in the runway+coverage-minus-financing composite
def f31cr_f31_cash_burn_runway_survival_252d_base_v066_signal(cashneq, opex, ncfo, ncff):
    rw = _f31_runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    cov = _f31_coverage(ncfo, opex).clip(-2, 2)
    finrel = (ncff.clip(lower=0)) / (cashneq.abs() + 1.0)
    raw = np.log1p(rw.clip(lower=0)) + cov - finrel
    sm = raw.ewm(span=63, min_periods=21).mean()
    result = sm - sm.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# --- burn acceleration as a level (2nd diff of burn, but a base facet) ---
# whether burn is intensifying: burn-now minus burn-2quarters (level)
def f31cr_f31_cash_burn_runway_burnaccel_base_v067_signal(opex, ncfo):
    burn = np.log1p(_f31_burn_opex(opex, ncfo))
    fast = burn - burn.shift(63)
    slow = burn.shift(63) - burn.shift(126)
    result = fast - slow
    return result.replace([np.inf, -np.inf], np.nan)


# --- runway floor proximity ---
# how close runway sits to its trailing 504d minimum (worst-case proximity)
def f31cr_f31_cash_burn_runway_floorprox_504d_base_v068_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    lo = _rmin(rw, 504)
    hi = _rmax(rw, 504)
    result = (rw - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# --- cash relative to burn-rate run-rate ---
# cash months at recent (63d-mean) burn vs at long (252d-mean) burn
def f31cr_f31_cash_burn_runway_runrateshift_base_v069_signal(cashneq, opex, ncfo):
    burn = _f31_burn_opex(opex, ncfo)
    short_burn = _mean(burn, 63)
    long_burn = _mean(burn, 252)
    rw_short = cashneq / short_burn.replace(0, np.nan) * 12.0
    rw_long = cashneq / long_burn.replace(0, np.nan) * 12.0
    result = _mean((rw_short - rw_long).clip(-120, 120), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- free-cash burn fraction of cash drawn ---
# fcf-burn fraction of cash, year-over-year change (is each period's bite growing)
def f31cr_f31_cash_burn_runway_fcfburnfrac_252d_base_v070_signal(cashneq, ncfo, capex):
    burn = _f31_burn_fcf(ncfo, capex)
    b = (burn / cashneq.replace(0, np.nan)).clip(0, 5)
    result = b - b.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# --- coverage regime entries (count) ---
# entries into operating-burn regime (ncfo crosses below 0) over last year
def f31cr_f31_cash_burn_runway_burnentry_252d_base_v071_signal(ncfo, opex):
    burning = ((ncfo < 0) & (opex > 0)).astype(float)
    entries = ((burning == 1) & (burning.shift(1) == 0)).astype(float)
    rate = entries.rolling(252, min_periods=126).sum()
    depth = (-_f31_coverage(ncfo, opex)).clip(lower=0).rolling(63, min_periods=21).mean()
    result = rate + depth
    return result.replace([np.inf, -np.inf], np.nan)


# --- ncff-financed runway extension trend ---
# financing inflow relative to cash balance (dilution-funded survival), smoothed
def f31cr_f31_cash_burn_runway_finratio_126d_base_v072_signal(ncff, cashneq):
    b = ncff / (cashneq.abs() + 1.0)
    result = b.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# --- net cash drain (combined ops+invest+finance against cash) ---
# total cash consumed by burn net of financing relative to balance
def f31cr_f31_cash_burn_runway_netdrain_252d_base_v073_signal(cashneq, ncfo, capex, ncff):
    burn = _f31_burn_fcf(ncfo, capex)
    net = (burn - ncff.clip(lower=0))
    b = net / (cashneq.abs() + 1.0)
    result = _mean(b.clip(-5, 5), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# --- runway-weighted burn streak (severity) ---
# severe-runway pressure: average shortfall below a 15-month runway threshold (months)
def f31cr_f31_cash_burn_runway_severeburn_252d_base_v074_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    shortfall = (15.0 - rw).clip(lower=0)
    # weight by how erratic the runway is (instability deepens distress)
    instab = _std(rw, 63)
    result = _mean(shortfall * np.log1p(instab), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# --- runway momentum smoothed (EMA of quarter-over-quarter runway change) ---
def f31cr_f31_cash_burn_runway_runwaymomsm_base_v075_signal(cashneq, opex, ncfo):
    rw = _f31_runway_opex(cashneq, opex, ncfo).clip(upper=120.0)
    mom = rw - rw.shift(63)
    result = mom.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f31cr_f31_cash_burn_runway_runwayopx_252d_base_v001_signal,
    f31cr_f31_cash_burn_runway_runwayfcf_252d_base_v002_signal,
    f31cr_f31_cash_burn_runway_runwaylog_126d_base_v003_signal,
    f31cr_f31_cash_burn_runway_invrunway_252d_base_v004_signal,
    f31cr_f31_cash_burn_runway_shortdist_126d_base_v005_signal,
    f31cr_f31_cash_burn_runway_burnopx_126d_base_v006_signal,
    f31cr_f31_cash_burn_runway_burnfcf_126d_base_v007_signal,
    f31cr_f31_cash_burn_runway_burnintens_252d_base_v008_signal,
    f31cr_f31_cash_burn_runway_burnintfcf_252d_base_v009_signal,
    f31cr_f31_cash_burn_runway_burnfrac_126d_base_v010_signal,
    f31cr_f31_cash_burn_runway_cover_252d_base_v011_signal,
    f31cr_f31_cash_burn_runway_covergap_126d_base_v012_signal,
    f31cr_f31_cash_burn_runway_cashcover_252d_base_v013_signal,
    f31cr_f31_cash_burn_runway_ocfcapex_252d_base_v014_signal,
    f31cr_f31_cash_burn_runway_runwayz_252d_base_v015_signal,
    f31cr_f31_cash_burn_runway_burnz_126d_base_v016_signal,
    f31cr_f31_cash_burn_runway_coverz_252d_base_v017_signal,
    f31cr_f31_cash_burn_runway_cashz_252d_base_v018_signal,
    f31cr_f31_cash_burn_runway_runwayrank_504d_base_v019_signal,
    f31cr_f31_cash_burn_runway_burnfracrank_252d_base_v020_signal,
    f31cr_f31_cash_burn_runway_coverrank_504d_base_v021_signal,
    f31cr_f31_cash_burn_runway_runwaychg_63d_base_v022_signal,
    f31cr_f31_cash_burn_runway_runwaygro_126d_base_v023_signal,
    f31cr_f31_cash_burn_runway_cashgro_63d_base_v024_signal,
    f31cr_f31_cash_burn_runway_burnchg_63d_base_v025_signal,
    f31cr_f31_cash_burn_runway_coverchg_126d_base_v026_signal,
    f31cr_f31_cash_burn_runway_runwaysl_base_v027_signal,
    f31cr_f31_cash_burn_runway_burnsl_base_v028_signal,
    f31cr_f31_cash_burn_runway_cashsl_base_v029_signal,
    f31cr_f31_cash_burn_runway_runwayvol_252d_base_v030_signal,
    f31cr_f31_cash_burn_runway_burnvol_126d_base_v031_signal,
    f31cr_f31_cash_burn_runway_covervol_252d_base_v032_signal,
    f31cr_f31_cash_burn_runway_burndays_252d_base_v033_signal,
    f31cr_f31_cash_burn_runway_negocf_252d_base_v034_signal,
    f31cr_f31_cash_burn_runway_critdays_252d_base_v035_signal,
    f31cr_f31_cash_burn_runway_fcfburndays_252d_base_v036_signal,
    f31cr_f31_cash_burn_runway_burnstreak_252d_base_v037_signal,
    f31cr_f31_cash_burn_runway_distress_126d_base_v038_signal,
    f31cr_f31_cash_burn_runway_quality_252d_base_v039_signal,
    f31cr_f31_cash_burn_runway_runwaytanh_63d_base_v040_signal,
    f31cr_f31_cash_burn_runway_runwayfcfz_252d_base_v041_signal,
    f31cr_f31_cash_burn_runway_runwayfcfrank_504d_base_v042_signal,
    f31cr_f31_cash_burn_runway_runwayfcfchg_63d_base_v043_signal,
    f31cr_f31_cash_burn_runway_runwayspr_252d_base_v044_signal,
    f31cr_f31_cash_burn_runway_capexburn_126d_base_v045_signal,
    f31cr_f31_cash_burn_runway_capexselffund_252d_base_v046_signal,
    f31cr_f31_cash_burn_runway_finlifeline_252d_base_v047_signal,
    f31cr_f31_cash_burn_runway_finburn_252d_base_v048_signal,
    f31cr_f31_cash_burn_runway_selffundgap_252d_base_v049_signal,
    f31cr_f31_cash_burn_runway_extrunway_252d_base_v050_signal,
    f31cr_f31_cash_burn_runway_cashdd_504d_base_v051_signal,
    f31cr_f31_cash_burn_runway_burnpeak_504d_base_v052_signal,
    f31cr_f31_cash_burn_runway_runwaycushion_252d_base_v053_signal,
    f31cr_f31_cash_burn_runway_burnratepct_504d_base_v054_signal,
    f31cr_f31_cash_burn_runway_burnvscapex_126d_base_v055_signal,
    f31cr_f31_cash_burn_runway_coversurplus_252d_base_v056_signal,
    f31cr_f31_cash_burn_runway_coverstab_252d_base_v057_signal,
    f31cr_f31_cash_burn_runway_ocfopex_126d_base_v058_signal,
    f31cr_f31_cash_burn_runway_ocfgro_126d_base_v059_signal,
    f31cr_f31_cash_burn_runway_ocfz_252d_base_v060_signal,
    f31cr_f31_cash_burn_runway_runwaysnr_252d_base_v061_signal,
    f31cr_f31_cash_burn_runway_burnsnr_252d_base_v062_signal,
    f31cr_f31_cash_burn_runway_runwaydisp_base_v063_signal,
    f31cr_f31_cash_burn_runway_runwayyoy_252d_base_v064_signal,
    f31cr_f31_cash_burn_runway_cashyoy_252d_base_v065_signal,
    f31cr_f31_cash_burn_runway_survival_252d_base_v066_signal,
    f31cr_f31_cash_burn_runway_burnaccel_base_v067_signal,
    f31cr_f31_cash_burn_runway_floorprox_504d_base_v068_signal,
    f31cr_f31_cash_burn_runway_runrateshift_base_v069_signal,
    f31cr_f31_cash_burn_runway_fcfburnfrac_252d_base_v070_signal,
    f31cr_f31_cash_burn_runway_burnentry_252d_base_v071_signal,
    f31cr_f31_cash_burn_runway_finratio_126d_base_v072_signal,
    f31cr_f31_cash_burn_runway_netdrain_252d_base_v073_signal,
    f31cr_f31_cash_burn_runway_severeburn_252d_base_v074_signal,
    f31cr_f31_cash_burn_runway_runwaymomsm_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_CASH_BURN_RUNWAY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
        "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
        "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
        "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
        "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
        "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "de",
        "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    cashneq = _fund(101, base=2e8, drift=-0.02, vol=0.07).rename("cashneq")
    opex = _fund(102, base=1.0e8, drift=0.01, vol=0.06).rename("opex")
    capex = _fund(103, base=2e7, drift=0.02, vol=0.08).rename("capex")
    ncfo = _fund(104, base=1.6e8, drift=-0.13, vol=0.32, allow_neg=True).rename("ncfo")
    ncff = _fund(105, base=6e7, drift=0.01, vol=0.20, allow_neg=True).rename("ncff")

    cols = {"cashneq": cashneq, "opex": opex, "capex": capex,
            "ncfo": ncfo, "ncff": ncff}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f31_cash_burn_runway_base_001_075_claude: %d features pass" % n_features)
