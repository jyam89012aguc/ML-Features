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


def _roc(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


def _logwarp(s):
    return np.sign(s) * np.log1p(s.abs())


# ===== folder domain DRIVER primitives (multi-driver distress composite) =====
# This family is a MULTI-DRIVER DISTRESS COMPOSITE. Each feature COMBINES >=2 of
# the four distress drivers below. Standalone single-driver runway / cashneq-yoy /
# burn-rate / coverage-velocity LEVELS belong to f31_cash_burn_runway and are NOT
# emitted here. The driver primitives are normalized building blocks that are only
# ever *combined* (>=2 at a time) inside each feature.

# DRIVER A - cash burn intensity: operating cash outflow vs the cash pile.
# Dimensionless burn pressure (how fast the cushion is consumed), not a runway level.
def _f40_burn_pressure(cashneq, ncfo):
    burn = (-ncfo).clip(lower=0.0)
    cushion = cashneq.abs().rolling(252, min_periods=21).mean() + 1.0
    return burn / cushion


# DRIVER B - dilution intensity: SBC paper dilution blended with share-count growth.
def _f40_dilution(sbcomp, sharesbas, equity, w):
    sbc = sbcomp / equity.abs().replace(0, np.nan)
    shr = (sharesbas / sharesbas.shift(w).replace(0, np.nan) - 1.0).clip(lower=0)
    return sbc.clip(lower=0) + shr


# DRIVER C - no-profit-path: depth of operating cash burn relative to the opex base.
def _f40_noprofit(ncfo, opex):
    return (-ncfo) / opex.replace(0, np.nan)


# DRIVER D - leverage stress: net debt (debt - cash) scaled by equity buffer.
def _f40_leverage(debt, equity, cashneq):
    return (debt - cashneq) / equity.abs().replace(0, np.nan)


# joint binary states of the drivers (regime tallies COMBINE >=2 drivers)
def _f40_burning(ncfo):
    return (ncfo < 0).astype(float)


def _f40_diluting(sbcomp, sharesbas, equity, w):
    # active when dilution intensity exceeds its own trailing median (relative regime)
    d = _f40_dilution(sbcomp, sharesbas, equity, w)
    med = d.rolling(252, min_periods=126).median()
    return (d > med).astype(float)


def _f40_levered(debt, equity, cashneq):
    return (_f40_leverage(debt, equity, cashneq) > 0).astype(float)


def _f40_streak(flag):
    # current consecutive-True run length of a 0/1 flag series
    grp = (flag == 0).cumsum()
    run = flag.groupby(grp).cumcount() + 1
    return run.where(flag == 1, 0.0)


# --- two-driver combiners: both drivers z-scored so EACH contributes variance, then
# combined with a DISTINCT operator per feature (product / sum / max / min / spread /
# sign-interaction / rank-product). This keeps every feature a genuine multi-driver
# composite while avoiding the degenerate "smooth(driverA) x near-const(driverB)" collapse.
def _f40_zprod(a, b, w):
    return _z(a, w) * _z(b, w)


def _f40_zmin(a, b, w):
    return pd.concat([_z(a, w), _z(b, w)], axis=1).min(axis=1)


def _f40_zmax(a, b, w):
    return pd.concat([_z(a, w), _z(b, w)], axis=1).max(axis=1)


def _f40_zsigninter(a, b, w):
    za, zb = _z(a, w), _z(b, w)
    return np.sign(za) * np.sign(zb) * (za.abs() + zb.abs())


# ============================================================
# === ZONE 1: zombie / joint-state flags (burn AND dilute AND/OR leverage) ===

# composite: zombie score = burn-pressure accrued only while ALSO diluting (burn x dilute)
def f40cd_f40_cash_burn_distress_zombiebd_252d_base_v001_signal(ncfo, sbcomp, sharesbas, equity, cashneq):
    dil = _f40_diluting(sbcomp, sharesbas, equity, 252)
    bp = np.tanh(_f40_burn_pressure(cashneq, ncfo))
    result = _mean(dil * bp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: triple-stress index = product of the three driver MAGNITUDES (not flags),
# requiring all three jointly elevated; structurally distinct from flag-fraction features
def f40cd_f40_cash_burn_distress_triple_252d_base_v002_signal(ncfo, sbcomp, sharesbas, equity, debt, cashneq):
    bp = np.tanh(_f40_burn_pressure(cashneq, ncfo))
    dilm = np.tanh(_f40_dilution(sbcomp, sharesbas, equity, 252) * 5.0)
    levm = np.tanh(_f40_leverage(debt, equity, cashneq).clip(lower=0))
    result = _mean(bp * dilm * levm, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn-and-leverage = leverage magnitude accrued only while burning
def f40cd_f40_cash_burn_distress_zombiebl_252d_base_v003_signal(ncfo, debt, equity, cashneq):
    burn = _f40_burning(ncfo)
    lev = np.tanh(_f40_leverage(debt, equity, cashneq).clip(lower=0))
    result = _mean(burn * lev, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: dilute-and-leverage = dilution magnitude accrued only while levered
def f40cd_f40_cash_burn_distress_zombiedl_252d_base_v004_signal(sbcomp, sharesbas, equity, debt, cashneq):
    lev = _f40_levered(debt, equity, cashneq)
    dil = np.tanh(_f40_dilution(sbcomp, sharesbas, equity, 252) * 5.0)
    result = _mean(dil * lev, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: count of distinct active distress drivers (0-3), smoothed
def f40cd_f40_cash_burn_distress_drivercount_252d_base_v005_signal(ncfo, sbcomp, sharesbas, equity, debt, cashneq):
    burn = _f40_burning(ncfo)
    dil = _f40_diluting(sbcomp, sharesbas, equity, 252)
    lev = _f40_levered(debt, equity, cashneq)
    result = _mean(burn + dil + lev, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: zombie persistence = EMA-decayed joint burn x dilute severity (sticky distress)
def f40cd_f40_cash_burn_distress_zombiestreak_base_v006_signal(ncfo, sbcomp, sharesbas, equity, cashneq):
    dil = _f40_diluting(sbcomp, sharesbas, equity, 252)
    bp = np.tanh(_f40_burn_pressure(cashneq, ncfo))
    joint = dil * bp
    result = joint.ewm(span=126, min_periods=42).mean() * _f40_streak(dil).clip(upper=126) / 126.0
    return result.replace([np.inf, -np.inf], np.nan)


# composite: joint burn-x-leverage severity persistence = how long BOTH stay above their
# own medians, weighted by the joint z-product magnitude (multi-driver, not a runway level)
def f40cd_f40_cash_burn_distress_blstreakmax_252d_base_v007_signal(ncfo, debt, equity, cashneq):
    bp = _f40_burn_pressure(cashneq, ncfo)
    lev = _f40_leverage(debt, equity, cashneq)
    hib = (bp > bp.rolling(252, min_periods=126).median()).astype(float)
    hil = (lev > lev.rolling(252, min_periods=126).median()).astype(float)
    streak = _f40_streak(hib * hil).clip(upper=252) / 252.0
    mag = np.tanh(_f40_zprod(bp, lev, 252))
    result = streak * (1.0 + mag).rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# composite: zombie instability = how choppy the joint burn+dilute state is (transition
# rate minus its persistence) -- captures unstable distress, orthogonal to its LEVEL
def f40cd_f40_cash_burn_distress_zombieentry_252d_base_v008_signal(ncfo, sbcomp, sharesbas, equity, cashneq):
    burn = _f40_burning(ncfo)
    dil = _f40_diluting(sbcomp, sharesbas, equity, 252)
    both = burn * dil
    trans = (both != both.shift(1)).astype(float)
    rate = trans.rolling(252, min_periods=126).mean()
    bpvol = _std(np.tanh(_f40_burn_pressure(cashneq, ncfo)), 126)
    result = rate + bpvol
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn-leverage co-occurrence intensity = P(levered | burning) - P(levered),
# i.e. how much MORE likely leverage stress is conditional on burning (joint dependence)
def f40cd_f40_cash_burn_distress_jointratio_252d_base_v009_signal(ncfo, debt, equity, cashneq):
    burn = _f40_burning(ncfo)
    lev = _f40_levered(debt, equity, cashneq)
    p_lev_given_burn = (burn * lev).rolling(504, min_periods=126).sum() / burn.rolling(504, min_periods=126).sum().replace(0, np.nan)
    p_lev = lev.rolling(504, min_periods=126).mean()
    result = p_lev_given_burn - p_lev
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn-vs-dilution co-elevation (z-product of burn-pressure and dilution)
def f40cd_f40_cash_burn_distress_zombiesev_252d_base_v010_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    bp = _f40_burn_pressure(cashneq, ncfo)
    dil = _f40_dilution(sbcomp, sharesbas, equity, 252)
    result = _mean(_f40_zprod(bp, dil, 252), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# === ZONE 2: distress-distance composites (runway-shortness MINUS buffer) ===

# composite: distress distance = burn-pressure penalty minus leverage cushion
def f40cd_f40_cash_burn_distress_distbl_252d_base_v011_signal(cashneq, ncfo, debt, equity):
    bp = _f40_burn_pressure(cashneq, ncfo)
    lev = _f40_leverage(debt, equity, cashneq)
    result = _mean(np.tanh(bp) + np.tanh(lev), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: distance = no-profit depth combined with dilution drag (two drivers)
def f40cd_f40_cash_burn_distress_distnd_252d_base_v012_signal(ncfo, opex, sbcomp, sharesbas, equity):
    npth = np.tanh(_f40_noprofit(ncfo, opex))
    dil = np.tanh(_f40_dilution(sbcomp, sharesbas, equity, 252) * 5.0)
    result = _mean(npth + dil, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: net-cash-after-debt runway eroded by burn (cash AND debt AND burn)
def f40cd_f40_cash_burn_distress_netrunway_252d_base_v013_signal(cashneq, debt, ncfo):
    netcash = cashneq - debt
    burn = (-ncfo).clip(lower=0.0)
    floor = cashneq.abs().rolling(252, min_periods=21).mean() * 0.02 + 1.0
    dist = netcash / (burn + floor)
    result = np.tanh(_mean(dist, 126) / 4.0)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn-AND-leverage co-elevation, worst-case via z-min (both must be high)
def f40cd_f40_cash_burn_distress_burnxlev_252d_base_v014_signal(cashneq, ncfo, debt, equity):
    bp = _f40_burn_pressure(cashneq, ncfo)
    lev = _f40_leverage(debt, equity, cashneq)
    result = _mean(_f40_zmin(bp, lev, 252), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: distance = how far net-cash buffer is from covering a year of burn
def f40cd_f40_cash_burn_distress_bufgap_252d_base_v015_signal(cashneq, debt, ncfo, opex):
    netcash = cashneq - debt
    annburn = (-ncfo).clip(lower=0.0) + (opex - ncfo.clip(lower=0.0)).clip(lower=0.0) * 0.25
    gap = (annburn - netcash).clip(lower=0) / (annburn + 1.0)
    result = _mean(gap, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: distress distance dispersion across burn vs leverage (which dominates)
def f40cd_f40_cash_burn_distress_distspread_252d_base_v016_signal(cashneq, ncfo, debt, equity):
    bp = np.tanh(_f40_burn_pressure(cashneq, ncfo))
    lev = np.tanh(_f40_leverage(debt, equity, cashneq))
    result = (bp - lev).rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn-vs-dilution dominance spread (which stress axis leads), z-scaled
def f40cd_f40_cash_burn_distress_dildist_252d_base_v017_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    bp = _f40_burn_pressure(cashneq, ncfo)
    dil = _f40_dilution(sbcomp, sharesbas, equity, 252)
    result = (_z(bp, 252) - _z(dil, 252)).rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# composite: leverage-AND-noprofit co-elevation (z-product of two non-burn drivers)
def f40cd_f40_cash_burn_distress_equityerode_252d_base_v018_signal(debt, equity, cashneq, ncfo, opex):
    lev = _f40_leverage(debt, equity, cashneq)
    npth = _f40_noprofit(ncfo, opex)
    result = _mean(_f40_zprod(lev, npth, 252), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: signed distress gap = leverage stress minus dilution-funding relief
def f40cd_f40_cash_burn_distress_levdilbal_252d_base_v019_signal(debt, equity, cashneq, sbcomp, sharesbas):
    lev = np.tanh(_f40_leverage(debt, equity, cashneq))
    dil = np.tanh(_f40_dilution(sbcomp, sharesbas, equity, 252) * 5.0)
    result = _mean(lev - dil, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: cash-to-obligations distance combining burn outflow AND debt load
def f40cd_f40_cash_burn_distress_obligdist_126d_base_v020_signal(cashneq, ncfo, debt, opex):
    obligation = debt.clip(lower=0) + (-ncfo).clip(lower=0.0)
    dist = cashneq / (obligation + opex.abs() * 0.1 + 1.0)
    result = np.tanh(_mean(dist, 63) / 3.0)
    return result.replace([np.inf, -np.inf], np.nan)


# === ZONE 3: weighted multi-factor survival-risk scores ===

# composite: survival-risk score = weighted sum of burn, dilution, leverage z-scores
def f40cd_f40_cash_burn_distress_riskscore_252d_base_v021_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    bp = _z(_f40_burn_pressure(cashneq, ncfo), 252)
    dil = _z(_f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    lev = _z(_f40_leverage(debt, equity, cashneq), 252)
    score = 0.45 * bp + 0.30 * dil + 0.25 * lev
    result = _mean(score, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: paper-funded-burn = z-product of burn pressure and SBC-only dilution
def f40cd_f40_cash_burn_distress_paperburn_252d_base_v022_signal(cashneq, ncfo, sbcomp, equity):
    bp = _f40_burn_pressure(cashneq, ncfo)
    sbc = sbcomp / equity.abs().replace(0, np.nan)
    result = _mean(_f40_zprod(bp, sbc, 504), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: indebted-and-unprofitable = z-MAX of leverage and no-profit (worst axis)
def f40cd_f40_cash_burn_distress_levnoprofit_252d_base_v023_signal(debt, equity, cashneq, ncfo, opex):
    lev = _f40_leverage(debt, equity, cashneq)
    npth = _f40_noprofit(ncfo, opex)
    result = _mean(_f40_zmax(lev, npth, 252), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: tri-factor geometric distress (cube-root of burn*dil*lev intensities)
def f40cd_f40_cash_burn_distress_trigeom_252d_base_v024_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    bp = _f40_burn_pressure(cashneq, ncfo).clip(lower=0) + 0.01
    dil = _f40_dilution(sbcomp, sharesbas, equity, 252).clip(lower=0) + 0.01
    lev = _f40_leverage(debt, equity, cashneq).clip(lower=0) + 0.01
    geom = (bp * dil * lev) ** (1.0 / 3.0)
    result = _mean(np.tanh(geom), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: max-of-drivers worst-stress score (distress dominated by worst factor)
def f40cd_f40_cash_burn_distress_worstdriver_252d_base_v025_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    bp = np.tanh(_f40_burn_pressure(cashneq, ncfo))
    dil = np.tanh(_f40_dilution(sbcomp, sharesbas, equity, 252) * 5.0)
    lev = np.tanh(_f40_leverage(debt, equity, cashneq))
    worst = pd.concat([bp, dil, lev], axis=1).max(axis=1)
    result = _mean(worst, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: rank-blended distress (avg percentile across burn/dilute/leverage)
def f40cd_f40_cash_burn_distress_rankblend_252d_base_v026_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    rb = _rank(_f40_burn_pressure(cashneq, ncfo), 252)
    rd_ = _rank(_f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    rl = _rank(_f40_leverage(debt, equity, cashneq), 252)
    result = (rb + rd_ + rl) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn x no-profit interaction score (deep-and-structural burn)
def f40cd_f40_cash_burn_distress_burnnoprofit_252d_base_v027_signal(cashneq, ncfo, opex):
    bp = _f40_burn_pressure(cashneq, ncfo)
    npth = _f40_noprofit(ncfo, opex).clip(lower=0)
    result = _mean(np.tanh(bp * npth), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: dilution x leverage interaction (capital-structure stress)
def f40cd_f40_cash_burn_distress_dilxlev_252d_base_v028_signal(sbcomp, sharesbas, equity, debt, cashneq):
    dil = _f40_dilution(sbcomp, sharesbas, equity, 252).clip(lower=0)
    lev = _f40_leverage(debt, equity, cashneq).clip(lower=0)
    result = _mean(np.tanh(dil * 5.0) * np.tanh(lev), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: dispersion of the three driver z-scores (how broad-based the stress is)
def f40cd_f40_cash_burn_distress_driverdisp_252d_base_v029_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    bp = _z(_f40_burn_pressure(cashneq, ncfo), 252)
    dil = _z(_f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    lev = _z(_f40_leverage(debt, equity, cashneq), 252)
    result = pd.concat([bp, dil, lev], axis=1).std(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: harmonic distress (penalizes only when ALL drivers co-elevated)
def f40cd_f40_cash_burn_distress_harmonic_252d_base_v030_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    bp = _f40_burn_pressure(cashneq, ncfo).clip(lower=0) + 0.05
    dil = (_f40_dilution(sbcomp, sharesbas, equity, 252) * 5.0).clip(lower=0) + 0.05
    lev = _f40_leverage(debt, equity, cashneq).clip(lower=0) + 0.05
    harm = 3.0 / (1.0 / bp + 1.0 / dil + 1.0 / lev)
    result = _mean(np.tanh(harm), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# === ZONE 4: regime / streak tallies of JOINT stress ===

# composite: burn AND dilution simultaneously deepening (z-product of their 21d changes)
def f40cd_f40_cash_burn_distress_deependil_252d_base_v031_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    bp = _f40_burn_pressure(cashneq, ncfo)
    dil = _f40_dilution(sbcomp, sharesbas, equity, 252)
    dbp = bp - bp.shift(21)
    ddil = dil - dil.shift(21)
    result = _mean(_f40_zprod(dbp, ddil, 252), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: leverage-rising-while-burning regime fraction
def f40cd_f40_cash_burn_distress_levupburn_252d_base_v032_signal(debt, equity, cashneq, ncfo):
    lev = _f40_leverage(debt, equity, cashneq)
    rising = (lev > lev.shift(63)).astype(float)
    burn = _f40_burning(ncfo)
    result = _mean(rising * burn, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: consecutive quarters where >=2 drivers active simultaneously
def f40cd_f40_cash_burn_distress_multistreak_base_v033_signal(ncfo, sbcomp, sharesbas, equity, debt, cashneq):
    cnt = _f40_burning(ncfo) + _f40_diluting(sbcomp, sharesbas, equity, 252) + _f40_levered(debt, equity, cashneq)
    flag = (cnt >= 2).astype(float)
    streak = _f40_streak(flag)
    result = streak.rolling(252, min_periods=63).mean() / 42.0
    return result.replace([np.inf, -np.inf], np.nan)


# composite: share of yr both no-profit (ncfo<0 vs opex deep) and diluting
def f40cd_f40_cash_burn_distress_npdilregime_252d_base_v034_signal(ncfo, opex, sbcomp, sharesbas, equity):
    deep = np.tanh(_f40_noprofit(ncfo, opex).clip(lower=0))
    dil = _f40_diluting(sbcomp, sharesbas, equity, 252)
    result = _mean(deep * dil, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: triple-stress onsets over two years, plus dilution-driven severity tilt
def f40cd_f40_cash_burn_distress_tripleentry_504d_base_v035_signal(ncfo, sbcomp, sharesbas, equity, debt, cashneq):
    cnt = _f40_burning(ncfo) + _f40_diluting(sbcomp, sharesbas, equity, 252) + _f40_levered(debt, equity, cashneq)
    flag = (cnt == 3).astype(float)
    entry = ((flag == 1) & (flag.shift(1) == 0)).astype(float)
    onsets = entry.rolling(504, min_periods=252).sum()
    dil = np.tanh(_f40_dilution(sbcomp, sharesbas, equity, 252) * 5.0)
    result = onsets + _mean(dil, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: distress-worsening run = consecutive days risk-score rising (joint)
def f40cd_f40_cash_burn_distress_worsenrun_252d_base_v036_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    bp = _z(_f40_burn_pressure(cashneq, ncfo), 252)
    dil = _z(_f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    lev = _z(_f40_leverage(debt, equity, cashneq), 252)
    score = bp + dil + lev
    rising = (score > score.shift(21)).astype(float)
    streak = _f40_streak(rising)
    result = streak.rolling(252, min_periods=63).mean() / 42.0
    return result.replace([np.inf, -np.inf], np.nan)


# composite: fraction of yr in joint cash-down AND share-up regime
def f40cd_f40_cash_burn_distress_cashdownshrup_252d_base_v037_signal(cashneq, ncfo, sharesbas):
    cashfall = ((cashneq < cashneq.shift(63)) & (ncfo < 0)).astype(float)
    shrup = (sharesbas > sharesbas.shift(63)).astype(float)
    result = _mean(cashfall * shrup, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: persistence of deeper-than-median joint burn+leverage
def f40cd_f40_cash_burn_distress_jointdeep_252d_base_v038_signal(cashneq, ncfo, debt, equity):
    bp = _f40_burn_pressure(cashneq, ncfo)
    lev = _f40_leverage(debt, equity, cashneq).clip(lower=0)
    joint = bp * (1.0 + lev)
    med = joint.rolling(252, min_periods=126).median()
    above = (joint > med).astype(float)
    result = _mean(above, 252) + 0.1 * np.tanh(joint - med)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: regime change = shift in fraction-of-yr triple-stress over the half-year
def f40cd_f40_cash_burn_distress_regimeshift_252d_base_v039_signal(ncfo, sbcomp, sharesbas, equity, debt, cashneq):
    cnt = _f40_burning(ncfo) + _f40_diluting(sbcomp, sharesbas, equity, 252) + _f40_levered(debt, equity, cashneq)
    flag = (cnt >= 2).astype(float)
    frac = _mean(flag, 126)
    result = frac - frac.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: calm distance = trailing-avg of inactive-driver count minus joint severity
def f40cd_f40_cash_burn_distress_allquiet_252d_base_v040_signal(ncfo, sbcomp, sharesbas, equity, debt, cashneq):
    cnt = _f40_burning(ncfo) + _f40_diluting(sbcomp, sharesbas, equity, 252) + _f40_levered(debt, equity, cashneq)
    inactive = 3.0 - cnt
    bp = np.tanh(_f40_burn_pressure(cashneq, ncfo))
    lev = np.tanh(_f40_leverage(debt, equity, cashneq).clip(lower=0))
    result = _mean(inactive, 252) - _mean(bp * (1.0 + lev), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# === ZONE 5: dilution-funded-burn composites (sbcomp/sharesbas + burn) ===

# composite: how much of the cash burn is offset by paper (SBC) issuance
def f40cd_f40_cash_burn_distress_sbcsubsidy_252d_base_v041_signal(cashneq, ncfo, sbcomp):
    burn = (-ncfo).clip(lower=0.0)
    subsidy = sbcomp / (burn + cashneq.abs() * 0.01 + 1.0)
    result = _mean(np.tanh(subsidy), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn coupled to share-count-growth (z-sign-interaction of the two drivers)
def f40cd_f40_cash_burn_distress_shrfundburn_252d_base_v042_signal(cashneq, ncfo, sharesbas):
    bp = _f40_burn_pressure(cashneq, ncfo)
    shr = sharesbas / sharesbas.shift(252).replace(0, np.nan) - 1.0
    result = _mean(_f40_zsigninter(bp, shr, 252), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: SBC-plus-share dilution accelerating while burning (joint deterioration)
def f40cd_f40_cash_burn_distress_dilaccelburn_252d_base_v043_signal(ncfo, sbcomp, sharesbas, equity):
    dil = _f40_dilution(sbcomp, sharesbas, equity, 252)
    accel = (dil > dil.shift(63)).astype(float)
    burn = _f40_burning(ncfo)
    result = _mean(accel * burn, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: dilution intensity scaled by no-profit depth (issuing-into-losses)
def f40cd_f40_cash_burn_distress_dilnoprofit_252d_base_v044_signal(sbcomp, sharesbas, equity, ncfo, opex):
    dil = _f40_dilution(sbcomp, sharesbas, equity, 252)
    npth = _f40_noprofit(ncfo, opex).clip(lower=0)
    result = _mean(dil * (1.0 + npth), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: SBC-funded-burn vs net-cash buffer (dilution-relief-vs-leverage)
def f40cd_f40_cash_burn_distress_sbcvsbuffer_252d_base_v045_signal(sbcomp, cashneq, debt, ncfo):
    burn = (-ncfo).clip(lower=0.0)
    netcash = (cashneq - debt)
    relief = (sbcomp + burn) / (netcash.abs() + 1.0)
    result = np.tanh(_mean(relief, 126) / 2.0)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: cumulative dilution over 2yr while persistently burning
def f40cd_f40_cash_burn_distress_cumdilburn_504d_base_v046_signal(sharesbas, ncfo, equity, sbcomp):
    shr = (sharesbas / sharesbas.shift(504).replace(0, np.nan) - 1.0).clip(lower=0)
    burnfrac = _mean(_f40_burning(ncfo), 504)
    sbc = (sbcomp / equity.abs().replace(0, np.nan)).clip(lower=0)
    result = (shr + sbc) * burnfrac
    return result.replace([np.inf, -np.inf], np.nan)


# composite: dilution-per-unit-burn efficiency (how costly the burn is in dilution)
def f40cd_f40_cash_burn_distress_dilperburn_252d_base_v047_signal(sbcomp, sharesbas, equity, cashneq, ncfo):
    dil = _f40_dilution(sbcomp, sharesbas, equity, 252)
    bp = _f40_burn_pressure(cashneq, ncfo).clip(lower=0) + 0.05
    result = np.tanh(_mean(dil / bp, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# composite: bad-dilution intensity = dilution magnitude conditioned on burn depth
def f40cd_f40_cash_burn_distress_baddilshare_252d_base_v048_signal(ncfo, sbcomp, sharesbas, equity, cashneq):
    dil = _f40_dilution(sbcomp, sharesbas, equity, 252)
    bp = _f40_burn_pressure(cashneq, ncfo)
    bad = _mean(dil * np.tanh(bp), 252)
    total = _mean(dil, 252)
    result = bad / total.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: SBC-as-share-of-opex co-elevated with operating burn depth (z-min worst-case)
def f40cd_f40_cash_burn_distress_sbcopexburn_252d_base_v049_signal(sbcomp, opex, ncfo):
    sbcshare = sbcomp / opex.replace(0, np.nan)
    burn = _f40_noprofit(ncfo, opex)
    result = _mean(_f40_zmin(sbcshare, burn, 504), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: joint dilution+leverage capital-pressure index, ranked
def f40cd_f40_cash_burn_distress_caprank_252d_base_v050_signal(sbcomp, sharesbas, equity, debt, cashneq):
    dil = _f40_dilution(sbcomp, sharesbas, equity, 252)
    lev = _f40_leverage(debt, equity, cashneq).clip(lower=0)
    idx = np.tanh(dil * 5.0) + np.tanh(lev)
    result = _rank(idx, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# === ZONE 6: balance-sheet-erosion composites (equity + cash + burn) ===

# composite: equity cushion eroding while burning cash (joint solvency decay)
def f40cd_f40_cash_burn_distress_equitydecay_252d_base_v051_signal(equity, cashneq, ncfo):
    eqfall = ((equity < equity.shift(63))).astype(float)
    burn = _f40_burning(ncfo)
    result = _mean(eqfall * burn, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: net-cash burn-down coupled with negative equity trend
def f40cd_f40_cash_burn_distress_netcashdecay_252d_base_v052_signal(cashneq, debt, equity, ncfo):
    netcash = cashneq - debt
    nfall = (netcash < netcash.shift(126)).astype(float)
    burn = _f40_burning(ncfo)
    sev = (-_z(netcash, 252)).clip(lower=0)
    result = _mean(nfall * burn, 252) + 0.05 * sev
    return result.replace([np.inf, -np.inf], np.nan)


# composite: solvency ratio = net-cash buffer per unit of burn, log-warped
def f40cd_f40_cash_burn_distress_solvency_252d_base_v053_signal(cashneq, debt, ncfo, equity):
    buffer = (cashneq - debt) + equity.clip(lower=0) * 0.1
    burn = (-ncfo).clip(lower=0.0) + 1.0
    result = _mean(_logwarp(buffer / burn), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: equity-buffer erosion velocity scaled by burn pressure (signed deleveraging)
def f40cd_f40_cash_burn_distress_levbuffshrink_252d_base_v054_signal(equity, debt, cashneq, ncfo):
    buff = equity.abs() / (debt + 1.0)
    erode = -(buff - buff.shift(126))
    bp = _f40_burn_pressure(cashneq, ncfo)
    result = _mean(_f40_zsigninter(erode, bp, 252), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: months-to-insolvency proxy = net-cash / monthly burn, capped & ranked
def f40cd_f40_cash_burn_distress_insolvrank_252d_base_v055_signal(cashneq, debt, ncfo, opex):
    netcash = cashneq - debt
    monthlyburn = ((-ncfo).clip(lower=0.0) + (opex - ncfo.clip(lower=0.0)).clip(lower=0.0) * 0.1) / 12.0 + 1.0
    months = (netcash / monthlyburn).clip(-60, 120)
    result = _rank(months, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: cash-to-debt coverage weakness co-moving with burn (z-product, inverted cover)
def f40cd_f40_cash_burn_distress_covdegrade_252d_base_v056_signal(cashneq, debt, ncfo):
    weakcover = (debt + 1.0) / (cashneq.abs() + 1.0)
    bp = _f40_burn_pressure(cashneq, ncfo)
    result = _mean(_f40_zprod(weakcover, bp, 252), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: equity-burn co-elevated with dilution (book-erosion x dilution), ranked
def f40cd_f40_cash_burn_distress_eqburnrank_252d_base_v057_signal(ncfo, equity, debt, cashneq, sbcomp, sharesbas):
    burn = (-ncfo).clip(lower=0.0)
    eqburn = burn / equity.abs().replace(0, np.nan)
    dil = _f40_dilution(sbcomp, sharesbas, equity, 252)
    result = _rank(_f40_zprod(eqburn, dil, 252), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: distress index = negative-equity pressure blended with deep-burn x high-leverage
def f40cd_f40_cash_burn_distress_distressflag_252d_base_v058_signal(equity, cashneq, ncfo, debt):
    negeq = (-_z(equity, 252)).clip(lower=0)
    deep = np.tanh(_f40_burn_pressure(cashneq, ncfo))
    hilev = np.tanh(_f40_leverage(debt, equity, cashneq).clip(lower=0))
    result = _mean(0.5 * negeq + deep * hilev, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: working-buffer velocity = how fast net-cash buffer shrinks while burning
def f40cd_f40_cash_burn_distress_bufvelburn_252d_base_v059_signal(cashneq, debt, ncfo, opex):
    buff = (cashneq - debt) / (opex.abs() + 1.0)
    vel = buff - buff.shift(63)
    burn = _f40_burning(ncfo)
    result = _mean(vel * burn, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: full-stress = worst-of-three z-driver floor (ALL of burn/leverage/no-profit
# must be elevated for the score to rise); z-min makes it distinct from product features
def f40cd_f40_cash_burn_distress_fullstress_252d_base_v060_signal(cashneq, ncfo, debt, equity, opex):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 252)
    zl = _z(_f40_leverage(debt, equity, cashneq), 252)
    zn = _z(_f40_noprofit(ncfo, opex), 252)
    worst = pd.concat([zb, zl, zn], axis=1).min(axis=1)
    result = _mean(worst, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# === ZONE 7: dynamics of joint-stress (composite then change/vol/rank) ===

# composite: acceleration of joint burn+dilute score (deteriorating fast)
def f40cd_f40_cash_burn_distress_jointaccel_252d_base_v061_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    bp = np.tanh(_f40_burn_pressure(cashneq, ncfo))
    dil = np.tanh(_f40_dilution(sbcomp, sharesbas, equity, 252) * 5.0)
    score = bp + dil
    sm = score.ewm(span=42, min_periods=21).mean()
    result = sm - sm.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: volatility of the tri-factor risk score (unstable distress)
def f40cd_f40_cash_burn_distress_riskvol_252d_base_v062_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    bp = _z(_f40_burn_pressure(cashneq, ncfo), 252)
    dil = _z(_f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    lev = _z(_f40_leverage(debt, equity, cashneq), 252)
    score = bp + dil + lev
    result = _std(score, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: divergence = burn worsening while leverage improving (or vice-versa)
def f40cd_f40_cash_burn_distress_burnlevdiv_252d_base_v063_signal(cashneq, ncfo, debt, equity):
    bp = np.tanh(_f40_burn_pressure(cashneq, ncfo))
    lev = np.tanh(_f40_leverage(debt, equity, cashneq))
    dbp = bp - bp.shift(63)
    dlev = lev - lev.shift(63)
    result = _mean(dbp - dlev, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: distress-score year-over-year change (joint multi-driver trend)
def f40cd_f40_cash_burn_distress_scoreyoy_252d_base_v064_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    bp = np.tanh(_f40_burn_pressure(cashneq, ncfo))
    dil = np.tanh(_f40_dilution(sbcomp, sharesbas, equity, 252) * 5.0)
    lev = np.tanh(_f40_leverage(debt, equity, cashneq))
    score = bp + dil + lev
    result = score - score.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: distress-score smoothed level (slow multi-driver state)
def f40cd_f40_cash_burn_distress_scorelevel_252d_base_v065_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    bp = np.tanh(_f40_burn_pressure(cashneq, ncfo))
    dil = np.tanh(_f40_dilution(sbcomp, sharesbas, equity, 252) * 5.0)
    lev = np.tanh(_f40_leverage(debt, equity, cashneq))
    score = 0.4 * bp + 0.3 * dil + 0.3 * lev
    result = score.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn-pressure x dilution co-movement (do they worsen together?)
def f40cd_f40_cash_burn_distress_comovebd_252d_base_v066_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    bp = _f40_burn_pressure(cashneq, ncfo)
    dil = _f40_dilution(sbcomp, sharesbas, equity, 252)
    dbp = bp - bp.shift(21)
    ddil = dil - dil.shift(21)
    result = _mean(np.sign(dbp) * np.sign(ddil) * (dbp.abs() + ddil.abs()), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: distress-distance recovery (improving net-cash while burn easing)
def f40cd_f40_cash_burn_distress_recovery_252d_base_v067_signal(cashneq, debt, ncfo):
    netcash = (cashneq - debt)
    nc_imp = (netcash > netcash.shift(126)).astype(float)
    burn_ease = (ncfo > ncfo.shift(126)).astype(float)
    result = _mean(nc_imp * burn_ease, 252) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# composite: weighted distress percentile vs own 2yr history (multi-driver)
def f40cd_f40_cash_burn_distress_distpctile_504d_base_v068_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    bp = np.tanh(_f40_burn_pressure(cashneq, ncfo))
    dil = np.tanh(_f40_dilution(sbcomp, sharesbas, equity, 252) * 5.0)
    lev = np.tanh(_f40_leverage(debt, equity, cashneq))
    score = bp + dil + lev
    result = _rank(score, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn-funded-by-debt = z-sign-interaction of debt growth and burn pressure
def f40cd_f40_cash_burn_distress_debtfundburn_252d_base_v069_signal(debt, ncfo, cashneq):
    debtgro = debt / debt.shift(63).replace(0, np.nan) - 1.0
    bp = _f40_burn_pressure(cashneq, ncfo)
    result = _mean(_f40_zsigninter(debtgro, bp, 252), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: stress-amplitude = peak minus trough of risk score over the year
def f40cd_f40_cash_burn_distress_stressamp_252d_base_v070_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    bp = np.tanh(_f40_burn_pressure(cashneq, ncfo))
    dil = np.tanh(_f40_dilution(sbcomp, sharesbas, equity, 252) * 5.0)
    lev = np.tanh(_f40_leverage(debt, equity, cashneq))
    score = bp + dil + lev
    hi = score.rolling(252, min_periods=126).max()
    lo = score.rolling(252, min_periods=126).min()
    result = hi - lo
    return result.replace([np.inf, -np.inf], np.nan)


# composite: half-year vs 2yr distress-score spread (short vs long stress regime)
def f40cd_f40_cash_burn_distress_scorespread_base_v071_signal(cashneq, ncfo, debt, equity):
    bp = np.tanh(_f40_burn_pressure(cashneq, ncfo))
    lev = np.tanh(_f40_leverage(debt, equity, cashneq))
    score = bp + lev
    result = _mean(score, 126) - _mean(score, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: dilution-and-leverage capital-pressure trend over the half year
def f40cd_f40_cash_burn_distress_captrend_252d_base_v072_signal(sbcomp, sharesbas, equity, debt, cashneq):
    dil = np.tanh(_f40_dilution(sbcomp, sharesbas, equity, 252) * 5.0)
    lev = np.tanh(_f40_leverage(debt, equity, cashneq))
    cap = dil + lev
    result = cap.ewm(span=63, min_periods=21).mean() - cap.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn-and-noprofit severity rank vs 2yr history
def f40cd_f40_cash_burn_distress_burnnprank_504d_base_v073_signal(cashneq, ncfo, opex):
    bp = _f40_burn_pressure(cashneq, ncfo)
    npth = _f40_noprofit(ncfo, opex).clip(lower=0)
    sev = np.tanh(bp) * (1.0 + npth)
    result = _rank(sev, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: structural-distress = slow EMA of triple-driver geometric mean
def f40cd_f40_cash_burn_distress_structural_504d_base_v074_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    bp = _f40_burn_pressure(cashneq, ncfo).clip(lower=0) + 0.01
    dil = _f40_dilution(sbcomp, sharesbas, equity, 252).clip(lower=0) * 5.0 + 0.01
    lev = _f40_leverage(debt, equity, cashneq).clip(lower=0) + 0.01
    geom = (bp * dil * lev) ** (1.0 / 3.0)
    result = np.tanh(geom).ewm(span=252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# composite: terminal-distress index = net-cash-runway shortness x dilution-dependence
def f40cd_f40_cash_burn_distress_terminal_252d_base_v075_signal(cashneq, debt, ncfo, sbcomp, sharesbas, equity):
    netcash = cashneq - debt
    burn = (-ncfo).clip(lower=0.0) + 1.0
    runshort = 1.0 / (1.0 + (netcash / burn).clip(lower=0))
    dildep = np.tanh(_f40_dilution(sbcomp, sharesbas, equity, 252) * 5.0)
    result = _mean(runshort * (1.0 + dildep), 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f40cd_f40_cash_burn_distress_zombiebd_252d_base_v001_signal,
    f40cd_f40_cash_burn_distress_triple_252d_base_v002_signal,
    f40cd_f40_cash_burn_distress_zombiebl_252d_base_v003_signal,
    f40cd_f40_cash_burn_distress_zombiedl_252d_base_v004_signal,
    f40cd_f40_cash_burn_distress_drivercount_252d_base_v005_signal,
    f40cd_f40_cash_burn_distress_zombiestreak_base_v006_signal,
    f40cd_f40_cash_burn_distress_blstreakmax_252d_base_v007_signal,
    f40cd_f40_cash_burn_distress_zombieentry_252d_base_v008_signal,
    f40cd_f40_cash_burn_distress_jointratio_252d_base_v009_signal,
    f40cd_f40_cash_burn_distress_zombiesev_252d_base_v010_signal,
    f40cd_f40_cash_burn_distress_distbl_252d_base_v011_signal,
    f40cd_f40_cash_burn_distress_distnd_252d_base_v012_signal,
    f40cd_f40_cash_burn_distress_netrunway_252d_base_v013_signal,
    f40cd_f40_cash_burn_distress_burnxlev_252d_base_v014_signal,
    f40cd_f40_cash_burn_distress_bufgap_252d_base_v015_signal,
    f40cd_f40_cash_burn_distress_distspread_252d_base_v016_signal,
    f40cd_f40_cash_burn_distress_dildist_252d_base_v017_signal,
    f40cd_f40_cash_burn_distress_equityerode_252d_base_v018_signal,
    f40cd_f40_cash_burn_distress_levdilbal_252d_base_v019_signal,
    f40cd_f40_cash_burn_distress_obligdist_126d_base_v020_signal,
    f40cd_f40_cash_burn_distress_riskscore_252d_base_v021_signal,
    f40cd_f40_cash_burn_distress_paperburn_252d_base_v022_signal,
    f40cd_f40_cash_burn_distress_levnoprofit_252d_base_v023_signal,
    f40cd_f40_cash_burn_distress_trigeom_252d_base_v024_signal,
    f40cd_f40_cash_burn_distress_worstdriver_252d_base_v025_signal,
    f40cd_f40_cash_burn_distress_rankblend_252d_base_v026_signal,
    f40cd_f40_cash_burn_distress_burnnoprofit_252d_base_v027_signal,
    f40cd_f40_cash_burn_distress_dilxlev_252d_base_v028_signal,
    f40cd_f40_cash_burn_distress_driverdisp_252d_base_v029_signal,
    f40cd_f40_cash_burn_distress_harmonic_252d_base_v030_signal,
    f40cd_f40_cash_burn_distress_deependil_252d_base_v031_signal,
    f40cd_f40_cash_burn_distress_levupburn_252d_base_v032_signal,
    f40cd_f40_cash_burn_distress_multistreak_base_v033_signal,
    f40cd_f40_cash_burn_distress_npdilregime_252d_base_v034_signal,
    f40cd_f40_cash_burn_distress_tripleentry_504d_base_v035_signal,
    f40cd_f40_cash_burn_distress_worsenrun_252d_base_v036_signal,
    f40cd_f40_cash_burn_distress_cashdownshrup_252d_base_v037_signal,
    f40cd_f40_cash_burn_distress_jointdeep_252d_base_v038_signal,
    f40cd_f40_cash_burn_distress_regimeshift_252d_base_v039_signal,
    f40cd_f40_cash_burn_distress_allquiet_252d_base_v040_signal,
    f40cd_f40_cash_burn_distress_sbcsubsidy_252d_base_v041_signal,
    f40cd_f40_cash_burn_distress_shrfundburn_252d_base_v042_signal,
    f40cd_f40_cash_burn_distress_dilaccelburn_252d_base_v043_signal,
    f40cd_f40_cash_burn_distress_dilnoprofit_252d_base_v044_signal,
    f40cd_f40_cash_burn_distress_sbcvsbuffer_252d_base_v045_signal,
    f40cd_f40_cash_burn_distress_cumdilburn_504d_base_v046_signal,
    f40cd_f40_cash_burn_distress_dilperburn_252d_base_v047_signal,
    f40cd_f40_cash_burn_distress_baddilshare_252d_base_v048_signal,
    f40cd_f40_cash_burn_distress_sbcopexburn_252d_base_v049_signal,
    f40cd_f40_cash_burn_distress_caprank_252d_base_v050_signal,
    f40cd_f40_cash_burn_distress_equitydecay_252d_base_v051_signal,
    f40cd_f40_cash_burn_distress_netcashdecay_252d_base_v052_signal,
    f40cd_f40_cash_burn_distress_solvency_252d_base_v053_signal,
    f40cd_f40_cash_burn_distress_levbuffshrink_252d_base_v054_signal,
    f40cd_f40_cash_burn_distress_insolvrank_252d_base_v055_signal,
    f40cd_f40_cash_burn_distress_covdegrade_252d_base_v056_signal,
    f40cd_f40_cash_burn_distress_eqburnrank_252d_base_v057_signal,
    f40cd_f40_cash_burn_distress_distressflag_252d_base_v058_signal,
    f40cd_f40_cash_burn_distress_bufvelburn_252d_base_v059_signal,
    f40cd_f40_cash_burn_distress_fullstress_252d_base_v060_signal,
    f40cd_f40_cash_burn_distress_jointaccel_252d_base_v061_signal,
    f40cd_f40_cash_burn_distress_riskvol_252d_base_v062_signal,
    f40cd_f40_cash_burn_distress_burnlevdiv_252d_base_v063_signal,
    f40cd_f40_cash_burn_distress_scoreyoy_252d_base_v064_signal,
    f40cd_f40_cash_burn_distress_scorelevel_252d_base_v065_signal,
    f40cd_f40_cash_burn_distress_comovebd_252d_base_v066_signal,
    f40cd_f40_cash_burn_distress_recovery_252d_base_v067_signal,
    f40cd_f40_cash_burn_distress_distpctile_504d_base_v068_signal,
    f40cd_f40_cash_burn_distress_debtfundburn_252d_base_v069_signal,
    f40cd_f40_cash_burn_distress_stressamp_252d_base_v070_signal,
    f40cd_f40_cash_burn_distress_scorespread_base_v071_signal,
    f40cd_f40_cash_burn_distress_captrend_252d_base_v072_signal,
    f40cd_f40_cash_burn_distress_burnnprank_504d_base_v073_signal,
    f40cd_f40_cash_burn_distress_structural_504d_base_v074_signal,
    f40cd_f40_cash_burn_distress_terminal_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F40_CASH_BURN_DISTRESS_REGISTRY_001_075 = REGISTRY


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
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "tbvps",
        "de", "ncfdiv", "ncfinv", "dps", "divyield", "payoutratio", "prefdivis", "netincdis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, amp=0.0):
        # quarterly-stepped fundamental path with a quarterly oscillation of amplitude
        # `amp*base` (pushes the series across distress thresholds so flags toggle) plus
        # mild daily jitter so coarse aggregates retain cardinality. Real comm-services
        # panels (as-of-ffilled, daily-aligned) carry this variation intrinsically.
        g = np.random.default_rng(seed)
        nq = n // 63 + 1
        steps = np.repeat(g.normal(drift, vol, nq), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if amp:
            cyc = np.repeat(g.normal(0.0, 1.0, nq), 63)[:n]
            s = s + amp * base * cyc
        # idiosyncratic daily AR(1) wiggle so each column varies independently day-to-day
        # (decorrelates composite products; mirrors real as-of-ffilled panel micro-moves)
        e = g.normal(0.0, 0.06, n)
        ar = np.zeros(n)
        for t in range(1, n):
            ar[t] = 0.9 * ar[t - 1] + e[t]
        s = s * (1.0 + ar)
        return pd.Series(s, name=None)

    cashneq = _fund(1, base=1.5e8, drift=-0.01, vol=0.08, amp=0.6).rename("cashneq")
    ncfo = _fund(2, base=1.0e8, drift=0.01, vol=0.10, amp=1.3).rename("ncfo")
    sbcomp = _fund(3, base=2e7, drift=0.03, vol=0.06, amp=0.5).rename("sbcomp")
    sharesbas = _fund(4, base=1e8, drift=0.02, vol=0.02).rename("sharesbas")
    debt = _fund(5, base=1.3e8, drift=0.03, vol=0.08, amp=0.7).rename("debt")
    equity = _fund(6, base=2.0e8, drift=0.01, vol=0.06, amp=1.2).rename("equity")
    opex = _fund(7, base=2.5e8, drift=0.02, vol=0.05, amp=0.3).rename("opex")

    cols = {"cashneq": cashneq, "ncfo": ncfo, "sbcomp": sbcomp, "sharesbas": sharesbas,
            "debt": debt, "equity": equity, "opex": opex}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs not in allowlist: %s" % (
            name, set(meta["inputs"]) - ALLOW)
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

    print("OK f40_cash_burn_distress_base_001_075_claude: %d features pass" % n_features)
