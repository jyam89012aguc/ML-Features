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
# MULTI-DRIVER DISTRESS COMPOSITE family: each feature COMBINES >=2 of the four distress
# drivers (burn / dilution / no-profit / leverage). Single-driver runway / cashneq-yoy /
# burn-rate / coverage-velocity LEVELS are f31_cash_burn_runway and are NOT emitted here.
def _f40_burn_pressure(cashneq, ncfo):
    burn = (-ncfo).clip(lower=0.0)
    cushion = cashneq.abs().rolling(252, min_periods=21).mean() + 1.0
    return burn / cushion


def _f40_dilution(sbcomp, sharesbas, equity, w):
    sbc = sbcomp / equity.abs().replace(0, np.nan)
    shr = (sharesbas / sharesbas.shift(w).replace(0, np.nan) - 1.0).clip(lower=0)
    return sbc.clip(lower=0) + shr


def _f40_noprofit(ncfo, opex):
    return (-ncfo) / opex.replace(0, np.nan)


def _f40_leverage(debt, equity, cashneq):
    return (debt - cashneq) / equity.abs().replace(0, np.nan)


def _f40_burning(ncfo):
    return (ncfo < 0).astype(float)


def _f40_diluting(sbcomp, sharesbas, equity, w):
    d = _f40_dilution(sbcomp, sharesbas, equity, w)
    med = d.rolling(252, min_periods=126).median()
    return (d > med).astype(float)


def _f40_levered(debt, equity, cashneq):
    return (_f40_leverage(debt, equity, cashneq) > 0).astype(float)


def _f40_streak(flag):
    grp = (flag == 0).cumsum()
    run = flag.groupby(grp).cumcount() + 1
    return run.where(flag == 1, 0.0)


# two-driver combiners (both z-scored, distinct operator each)
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
# === ZONE 8: rank/percentile multi-driver survival indices ===

# composite: cross-sectional-style distress rank = avg of burn & leverage percentiles
def f40cd_f40_cash_burn_distress_blpctile_252d_base_v076_signal(cashneq, ncfo, debt, equity):
    rb = _rank(_f40_burn_pressure(cashneq, ncfo), 252)
    rl = _rank(_f40_leverage(debt, equity, cashneq), 252)
    result = (rb + rl) / 2.0
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn & dilution joint percentile (two-driver rank blend)
def f40cd_f40_cash_burn_distress_bdpctile_252d_base_v077_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    rb = _rank(_f40_burn_pressure(cashneq, ncfo), 252)
    rd_ = _rank(_f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    result = (rb + rd_) / 2.0
    return result.replace([np.inf, -np.inf], np.nan)


# composite: dilution & leverage joint percentile (capital-structure rank)
def f40cd_f40_cash_burn_distress_dlpctile_252d_base_v078_signal(sbcomp, sharesbas, equity, debt, cashneq):
    rd_ = _rank(_f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    rl = _rank(_f40_leverage(debt, equity, cashneq), 252)
    result = (rd_ + rl) / 2.0
    return result.replace([np.inf, -np.inf], np.nan)


# composite: no-profit & dilution joint percentile (issuing-into-losses rank)
def f40cd_f40_cash_burn_distress_ndpctile_252d_base_v079_signal(ncfo, opex, sbcomp, sharesbas, equity):
    rn = _rank(_f40_noprofit(ncfo, opex), 252)
    rd_ = _rank(_f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    result = (rn + rd_) / 2.0
    return result.replace([np.inf, -np.inf], np.nan)


# composite: min-percentile (need BOTH burn and leverage high) survival floor
def f40cd_f40_cash_burn_distress_blpctmin_252d_base_v080_signal(cashneq, ncfo, debt, equity):
    rb = _rank(_f40_burn_pressure(cashneq, ncfo), 252)
    rl = _rank(_f40_leverage(debt, equity, cashneq), 252)
    result = pd.concat([rb, rl], axis=1).min(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: max-percentile (worst single driver) of burn/dilute/leverage
def f40cd_f40_cash_burn_distress_worstpct_252d_base_v081_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    rb = _rank(_f40_burn_pressure(cashneq, ncfo), 252)
    rd_ = _rank(_f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    rl = _rank(_f40_leverage(debt, equity, cashneq), 252)
    result = pd.concat([rb, rd_, rl], axis=1).max(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: distress rank momentum = change in tri-driver rank-blend over a quarter
def f40cd_f40_cash_burn_distress_rankmom_252d_base_v082_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    rb = _rank(_f40_burn_pressure(cashneq, ncfo), 252)
    rd_ = _rank(_f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    rl = _rank(_f40_leverage(debt, equity, cashneq), 252)
    blend = (rb + rd_ + rl) / 3.0
    result = blend - blend.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: net-cash-runway percentile (cash & debt & burn) vs 2yr history
def f40cd_f40_cash_burn_distress_netrwpct_504d_base_v083_signal(cashneq, debt, ncfo):
    netcash = cashneq - debt
    burn = (-ncfo).clip(lower=0.0) + 1.0
    runway = netcash / burn
    result = _rank(runway, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: dispersion of burn/dilute/leverage percentiles (which dimension is extreme)
def f40cd_f40_cash_burn_distress_pctdisp_252d_base_v084_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    rb = _rank(_f40_burn_pressure(cashneq, ncfo), 252)
    rd_ = _rank(_f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    rl = _rank(_f40_leverage(debt, equity, cashneq), 252)
    result = pd.concat([rb, rd_, rl], axis=1).std(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: agreement = product of signs of burn-z and leverage-z (joint direction)
def f40cd_f40_cash_burn_distress_signagree_252d_base_v085_signal(cashneq, ncfo, debt, equity):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 252)
    zl = _z(_f40_leverage(debt, equity, cashneq), 252)
    result = _mean(np.sign(zb) * np.sign(zl), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# === ZONE 9: trend / acceleration of two-driver composites ===

# composite: burn-and-dilution composite trend over the half-year (z-product slope)
def f40cd_f40_cash_burn_distress_bdtrend_252d_base_v086_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    comp = _f40_zprod(_f40_burn_pressure(cashneq, ncfo), _f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    sm = comp.ewm(span=63, min_periods=21).mean()
    result = sm - sm.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn-and-leverage composite acceleration (second difference)
def f40cd_f40_cash_burn_distress_blaccel_252d_base_v087_signal(cashneq, ncfo, debt, equity):
    comp = _f40_zprod(_f40_burn_pressure(cashneq, ncfo), _f40_leverage(debt, equity, cashneq), 252)
    d1 = comp - comp.shift(63)
    result = d1 - d1.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: no-profit & leverage composite year-over-year change
def f40cd_f40_cash_burn_distress_nlyoy_252d_base_v088_signal(ncfo, opex, debt, equity, cashneq):
    comp = _f40_zsigninter(_f40_noprofit(ncfo, opex), _f40_leverage(debt, equity, cashneq), 252)
    result = comp - comp.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: dilution & leverage composite smoothed level (slow capital stress)
def f40cd_f40_cash_burn_distress_dllevel_252d_base_v089_signal(sbcomp, sharesbas, equity, debt, cashneq):
    comp = _f40_zprod(_f40_dilution(sbcomp, sharesbas, equity, 252), _f40_leverage(debt, equity, cashneq), 252)
    result = comp.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn-noprofit composite volatility (unstable structural burn)
def f40cd_f40_cash_burn_distress_bnvol_252d_base_v090_signal(cashneq, ncfo, opex):
    comp = _f40_zprod(_f40_burn_pressure(cashneq, ncfo), _f40_noprofit(ncfo, opex), 252)
    result = _std(comp, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: divergence of dilution and leverage z-trends (capital-mix rotation)
def f40cd_f40_cash_burn_distress_dlrotate_252d_base_v091_signal(sbcomp, sharesbas, equity, debt, cashneq):
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    zl = _z(_f40_leverage(debt, equity, cashneq), 252)
    result = _mean((zd - zd.shift(63)) - (zl - zl.shift(63)), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn-and-leverage composite percentile vs 2yr (joint extremity)
def f40cd_f40_cash_burn_distress_blextpct_504d_base_v092_signal(cashneq, ncfo, debt, equity):
    comp = _f40_zprod(_f40_burn_pressure(cashneq, ncfo), _f40_leverage(debt, equity, cashneq), 252)
    result = _rank(comp, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: tri-driver weighted score acceleration (deterioration speed)
def f40cd_f40_cash_burn_distress_scoreaccel_252d_base_v093_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 252)
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    zl = _z(_f40_leverage(debt, equity, cashneq), 252)
    score = 0.4 * zb + 0.3 * zd + 0.3 * zl
    sm = score.ewm(span=42, min_periods=21).mean()
    result = (sm - sm.shift(42)) - (sm.shift(42) - sm.shift(84))
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn-vs-dilution lead-lag (does burn precede dilution onset)
def f40cd_f40_cash_burn_distress_bdleadlag_252d_base_v094_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 252)
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    result = _mean(zb.shift(63) * zd, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# === ZONE 10: buffer / solvency multi-driver composites ===

# composite: net-cash buffer per year-of-burn, dilution-discounted (cash,debt,burn,dilute)
def f40cd_f40_cash_burn_distress_dilbuffer_252d_base_v095_signal(cashneq, debt, ncfo, sbcomp, sharesbas, equity):
    netcash = cashneq - debt
    burn = (-ncfo).clip(lower=0.0) + 1.0
    runway = netcash / burn
    dildrag = np.tanh(_f40_dilution(sbcomp, sharesbas, equity, 252) * 5.0)
    result = np.tanh(_mean(runway, 126) / 4.0) - dildrag.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# composite: equity-funded buffer eroding under burn AND leverage
def f40cd_f40_cash_burn_distress_eqbuffer_252d_base_v096_signal(equity, cashneq, debt, ncfo):
    buffer = (equity.clip(lower=0) + cashneq - debt)
    bp = _f40_burn_pressure(cashneq, ncfo)
    result = _mean(_f40_zsigninter(-buffer, bp, 252), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: months-of-net-cash x dilution-dependence interaction (terminal proxy)
def f40cd_f40_cash_burn_distress_monthsxdil_252d_base_v097_signal(cashneq, debt, ncfo, sbcomp, sharesbas, equity):
    netcash = cashneq - debt
    monthly = (-ncfo).clip(lower=0.0) / 12.0 + 1.0
    months = (netcash / monthly).clip(-60, 120)
    dil = _f40_dilution(sbcomp, sharesbas, equity, 252)
    result = _mean(_f40_zprod(-months, dil, 252), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: solvency margin = (cash+equity buffer) vs (debt+burn obligations), log
def f40cd_f40_cash_burn_distress_solvmargin_252d_base_v098_signal(cashneq, equity, debt, ncfo):
    assetside = cashneq.clip(lower=0) + equity.clip(lower=0)
    liabside = debt.clip(lower=0) + (-ncfo).clip(lower=0.0)
    result = _mean(_logwarp((assetside + 1.0) / (liabside + 1.0)), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: buffer-velocity AND burn co-deterioration (z-min worst-case)
def f40cd_f40_cash_burn_distress_bufburnmin_252d_base_v099_signal(cashneq, debt, ncfo, opex):
    buffer = (cashneq - debt) / (opex.abs() + 1.0)
    bufdecline = -(buffer - buffer.shift(63))
    bp = _f40_burn_pressure(cashneq, ncfo)
    result = _mean(_f40_zmin(bufdecline, -bp, 252), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: net-cash runway shortness co-elevated with dilution dependence (z-product)
def f40cd_f40_cash_burn_distress_runshortlev_252d_base_v100_signal(cashneq, debt, ncfo, sbcomp, sharesbas, equity):
    netcash = cashneq - debt
    monthly = (-ncfo).clip(lower=0.0) / 12.0 + 1.0
    months = netcash / monthly
    dil = _f40_dilution(sbcomp, sharesbas, equity, 252)
    result = _mean(_f40_zprod(-months, dil, 252), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: equity cushion vs cumulative burn over 2yr (book-value-vs-burn)
def f40cd_f40_cash_burn_distress_eqvsburn_504d_base_v101_signal(equity, ncfo, cashneq):
    cumburn = (-ncfo).clip(lower=0.0).rolling(504, min_periods=252).sum()
    cushion = (equity.clip(lower=0) + cashneq.clip(lower=0))
    result = np.tanh(_mean(cushion, 252) / (cumburn + 1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# composite: distress when BOTH net-cash low AND dilution high (z-min survival floor)
def f40cd_f40_cash_burn_distress_lowcashhighdil_252d_base_v102_signal(cashneq, debt, sbcomp, sharesbas, equity):
    netcash = (cashneq - debt) / (equity.abs() + 1.0)
    dil = _f40_dilution(sbcomp, sharesbas, equity, 252)
    result = _mean(_f40_zmin(-netcash, dil, 252), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: insolvency-distance trend = how fast solvency margin worsens with leverage
def f40cd_f40_cash_burn_distress_insolvtrend_252d_base_v103_signal(cashneq, equity, debt, ncfo):
    assetside = cashneq.clip(lower=0) + equity.clip(lower=0)
    liabside = debt.clip(lower=0) + (-ncfo).clip(lower=0.0)
    margin = _logwarp((assetside + 1.0) / (liabside + 1.0))
    result = margin.ewm(span=63, min_periods=21).mean() - margin.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: weak cash-coverage co-elevated with SBC dilution (z-product, sign-distinct)
def f40cd_f40_cash_burn_distress_cashcover_252d_base_v104_signal(cashneq, debt, sbcomp, ncfo, equity):
    need = debt.clip(lower=0) + sbcomp.clip(lower=0) + (-ncfo).clip(lower=0.0)
    weakcover = need / (cashneq.abs() + 1.0)
    sbcdil = sbcomp / equity.abs().replace(0, np.nan)
    result = _mean(_f40_zsigninter(weakcover, sbcdil, 252), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# === ZONE 11: regime tallies of joint stress (count-friendly) ===

# composite: quarters where burn-pressure above-median AND leverage above-median
def f40cd_f40_cash_burn_distress_dualmedian_252d_base_v105_signal(cashneq, ncfo, debt, equity):
    bp = _f40_burn_pressure(cashneq, ncfo)
    lev = _f40_leverage(debt, equity, cashneq)
    hib = (bp > bp.rolling(252, min_periods=126).median()).astype(float)
    hil = (lev > lev.rolling(252, min_periods=126).median()).astype(float)
    result = _mean(hib * hil, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: fraction of yr both no-profit deep AND leverage rising
def f40cd_f40_cash_burn_distress_nplevreg_252d_base_v106_signal(ncfo, opex, debt, equity, cashneq):
    npv = _f40_noprofit(ncfo, opex)
    npd = (npv > npv.rolling(252, min_periods=126).median()).astype(float)
    lev = _f40_leverage(debt, equity, cashneq)
    levup = (lev > lev.shift(63)).astype(float)
    result = _mean(npd * levup, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: longest joint burn&dilute run, severity-tilted by burn-dilution z-product
def f40cd_f40_cash_burn_distress_dualrunmax_252d_base_v107_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    bp = _f40_burn_pressure(cashneq, ncfo)
    dil = _f40_dilution(sbcomp, sharesbas, equity, 252)
    hib = (bp > bp.rolling(252, min_periods=126).median()).astype(float)
    hid = (dil > dil.rolling(252, min_periods=126).median()).astype(float)
    streak = _f40_streak(hib * hid)
    sev = np.tanh(_f40_zprod(bp, dil, 252)).rolling(63, min_periods=21).mean()
    result = streak.rolling(252, min_periods=63).max() / 252.0 + 0.3 * sev
    return result.replace([np.inf, -np.inf], np.nan)


# composite: count of distress-onset transitions for the tri-driver score
def f40cd_f40_cash_burn_distress_scoretrans_252d_base_v108_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 252)
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    zl = _z(_f40_leverage(debt, equity, cashneq), 252)
    hot = ((zb + zd + zl) > 1.0).astype(float)
    trans = (hot != hot.shift(1)).astype(float)
    result = _mean(trans, 252) + 0.1 * _mean(hot, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn-leverage co-elevation premium = E[severity | both high] - E[severity]
def f40cd_f40_cash_burn_distress_dualsev_252d_base_v109_signal(cashneq, ncfo, debt, equity):
    bp = _f40_burn_pressure(cashneq, ncfo)
    lev = _f40_leverage(debt, equity, cashneq)
    hib = (bp > bp.rolling(252, min_periods=126).median()).astype(float)
    hil = (lev > lev.rolling(252, min_periods=126).median()).astype(float)
    both = hib * hil
    sev = np.tanh(bp) + np.tanh(lev.clip(lower=0))
    cond = (sev * both).rolling(252, min_periods=126).sum() / both.rolling(252, min_periods=126).sum().replace(0, np.nan)
    result = cond - sev.rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# composite: deterioration breadth = avg number of drivers worsening QoQ
def f40cd_f40_cash_burn_distress_detbreadth_252d_base_v110_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    bp = _f40_burn_pressure(cashneq, ncfo)
    dil = _f40_dilution(sbcomp, sharesbas, equity, 252)
    lev = _f40_leverage(debt, equity, cashneq)
    w = (bp > bp.shift(63)).astype(float) + (dil > dil.shift(63)).astype(float) + (lev > lev.shift(63)).astype(float)
    result = _mean(w, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: all-drivers-worsening regime fraction (broad deterioration)
def f40cd_f40_cash_burn_distress_allworsen_252d_base_v111_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    bp = _f40_burn_pressure(cashneq, ncfo)
    dil = _f40_dilution(sbcomp, sharesbas, equity, 252)
    lev = _f40_leverage(debt, equity, cashneq)
    allw = ((bp > bp.shift(63)) & (dil > dil.shift(63)) & (lev > lev.shift(63))).astype(float)
    result = _mean(allw, 252) + 0.05 * np.tanh(_z(bp + lev, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# composite: stress-persistence proxy (sign-autocorr of burn+leverage z-score)
def f40cd_f40_cash_burn_distress_stresspersist_252d_base_v112_signal(cashneq, ncfo, debt, equity):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 252)
    zl = _z(_f40_leverage(debt, equity, cashneq), 252)
    score = zb + zl
    result = _mean(np.sign(score) * np.sign(score.shift(21)), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: fraction of yr in worst-quintile tri-driver score (deep-distress regime)
def f40cd_f40_cash_burn_distress_deepregime_504d_base_v113_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 252)
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    zl = _z(_f40_leverage(debt, equity, cashneq), 252)
    score = zb + zd + zl
    thr = score.rolling(504, min_periods=252).quantile(0.8)
    deep = (score > thr).astype(float)
    result = _mean(deep, 252) + 0.1 * np.tanh(score - thr)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: net-stress entries minus exits, plus current depth (signed distress momentum)
def f40cd_f40_cash_burn_distress_netentries_504d_base_v114_signal(cashneq, ncfo, debt, equity):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 252)
    zl = _z(_f40_leverage(debt, equity, cashneq), 252)
    score = zb + zl
    hot = (score > 1.0).astype(float)
    entry = ((hot == 1) & (hot.shift(1) == 0)).astype(float)
    exit_ = ((hot == 0) & (hot.shift(1) == 1)).astype(float)
    net = (entry - exit_).rolling(504, min_periods=252).sum()
    result = net + np.tanh(_mean(score, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# === ZONE 12: interaction / hybrid multi-driver composites ===

# composite: burn-funded-by-equity-erosion (burn pressure x equity-decline z-product)
def f40cd_f40_cash_burn_distress_burneqerode_252d_base_v115_signal(cashneq, ncfo, equity):
    bp = _f40_burn_pressure(cashneq, ncfo)
    eqdecline = -(equity - equity.shift(63))
    result = _mean(_f40_zprod(bp, eqdecline, 252), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: dilution-to-leverage substitution (which financing channel is used)
def f40cd_f40_cash_burn_distress_finchannel_252d_base_v116_signal(sbcomp, sharesbas, equity, debt, cashneq):
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    levchg = _z(debt - debt.shift(63), 252)
    result = _mean(zd - levchg, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn severity conditioned on negative-equity (deep-distress interaction)
def f40cd_f40_cash_burn_distress_negeqburn_252d_base_v117_signal(equity, cashneq, ncfo):
    negeq_pressure = (-_z(equity, 252)).clip(lower=0)
    bp = _f40_burn_pressure(cashneq, ncfo)
    result = _mean(np.tanh(bp) * negeq_pressure, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: leverage-times-dilution-times-burn tri-interaction (geometric, z-based)
def f40cd_f40_cash_burn_distress_triz_252d_base_v118_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 252).clip(lower=0)
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 252), 252).clip(lower=0)
    zl = _z(_f40_leverage(debt, equity, cashneq), 252).clip(lower=0)
    result = _mean(((zb + 0.1) * (zd + 0.1) * (zl + 0.1)) ** (1.0 / 3.0), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn-pressure scaled by inverse equity cushion (distress amplification)
def f40cd_f40_cash_burn_distress_burnamp_252d_base_v119_signal(cashneq, ncfo, equity):
    bp = _f40_burn_pressure(cashneq, ncfo)
    cushion = equity.abs().rolling(252, min_periods=126).mean() + 1.0
    amp = bp * (cashneq.abs().rolling(252, min_periods=126).mean() + 1.0) / cushion
    result = np.tanh(_mean(amp, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# composite: dilution accelerating into a leverage build (two-financing stress)
def f40cd_f40_cash_burn_distress_dilintolev_252d_base_v120_signal(sbcomp, sharesbas, equity, debt, cashneq):
    dilaccel = _z(_f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    dilaccel = dilaccel - dilaccel.shift(63)
    levbuild = _z(_f40_leverage(debt, equity, cashneq), 252)
    levbuild = levbuild - levbuild.shift(63)
    result = _mean(_f40_zprod(dilaccel.clip(lower=0), levbuild.clip(lower=0), 126), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: structural distress = slow EMA of tri-driver z-min (persistent broad stress)
def f40cd_f40_cash_burn_distress_structmin_504d_base_v121_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 252)
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    zl = _z(_f40_leverage(debt, equity, cashneq), 252)
    floor = pd.concat([zb, zd, zl], axis=1).min(axis=1)
    result = floor.ewm(span=252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn-and-noprofit composite minus leverage-cushion (net distress, signed)
def f40cd_f40_cash_burn_distress_netdistress_252d_base_v122_signal(cashneq, ncfo, opex, debt, equity):
    bn = _f40_zprod(_f40_burn_pressure(cashneq, ncfo), _f40_noprofit(ncfo, opex), 252)
    levz = _z(_f40_leverage(debt, equity, cashneq), 252)
    result = _mean(bn + levz, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: cash-burn duration x dilution-dependence (how long paper can fund the burn)
def f40cd_f40_cash_burn_distress_paperruntime_252d_base_v123_signal(cashneq, ncfo, sbcomp, equity):
    burn = (-ncfo).clip(lower=0.0) + 1.0
    sbc = sbcomp.clip(lower=0)
    paper_cover = (cashneq.clip(lower=0) + sbc) / burn
    sbcdil = sbcomp / equity.abs().replace(0, np.nan)
    result = np.tanh(_mean(paper_cover, 126) / 8.0) - sbcdil.clip(lower=0).rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn-pressure regime x leverage regime concurrency rank
def f40cd_f40_cash_burn_distress_concurrank_504d_base_v124_signal(cashneq, ncfo, debt, equity):
    bp = _f40_burn_pressure(cashneq, ncfo)
    lev = _f40_leverage(debt, equity, cashneq)
    concur = np.tanh(bp) * np.tanh(lev.clip(lower=0))
    result = _rank(concur, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# === ZONE 13: long-horizon survival & terminal composites ===

# composite: 2yr cumulative burn vs net-cash (terminal runway exhaustion, cash+debt+burn)
def f40cd_f40_cash_burn_distress_exhaust_504d_base_v125_signal(cashneq, debt, ncfo):
    cumburn = (-ncfo).clip(lower=0.0).rolling(504, min_periods=252).mean()
    netcash = (cashneq - debt)
    result = np.tanh(cumburn / (netcash.abs().rolling(252, min_periods=126).mean() + 1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# composite: persistent-burn fraction x average leverage (chronic-distress index)
def f40cd_f40_cash_burn_distress_chronic_504d_base_v126_signal(ncfo, debt, equity, cashneq):
    burnfrac = _mean(_f40_burning(ncfo), 504)
    levz = _z(_f40_leverage(debt, equity, cashneq), 504)
    result = burnfrac * np.tanh(levz)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: dilution-funded-burn cumulative drag over 2yr (sharesbas growth x burn)
def f40cd_f40_cash_burn_distress_cumdrag_504d_base_v127_signal(sharesbas, ncfo, cashneq):
    shrgro = sharesbas / sharesbas.shift(504).replace(0, np.nan) - 1.0
    bp = _f40_burn_pressure(cashneq, ncfo)
    result = shrgro.clip(lower=0) * np.tanh(_mean(bp, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# composite: equity-decline-rate x burn (book erosion velocity composite)
def f40cd_f40_cash_burn_distress_bookerode_504d_base_v128_signal(equity, ncfo, cashneq):
    eqgro = equity / equity.shift(252).replace(0, np.nan) - 1.0
    bp = _f40_burn_pressure(cashneq, ncfo)
    result = _mean(_f40_zsigninter(-eqgro, bp, 504), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: terminal-distress = mean of the three z-driver triad (low-cash, dilution,
# leverage) -- average aggregation (distinct from worst-case z-min features)
def f40cd_f40_cash_burn_distress_terminaltriad_252d_base_v129_signal(cashneq, debt, sbcomp, sharesbas, equity):
    netcash = (cashneq - debt) / (equity.abs() + 1.0)
    dil = _f40_dilution(sbcomp, sharesbas, equity, 252)
    lev = (debt - cashneq) / equity.abs().replace(0, np.nan)
    triad = (_z(-netcash, 252) + _z(dil, 252) + _z(lev, 252)) / 3.0
    result = _rank(triad, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: survival-index = tanh(net-cash runway) penalized by dilution+leverage z-sum
def f40cd_f40_cash_burn_distress_survindex_252d_base_v130_signal(cashneq, debt, ncfo, sbcomp, sharesbas, equity):
    netcash = cashneq - debt
    burn = (-ncfo).clip(lower=0.0) + 1.0
    runway = np.tanh((netcash / burn) / 6.0)
    penalty = _z(_f40_dilution(sbcomp, sharesbas, equity, 252), 252) + _z(_f40_leverage(debt, equity, cashneq), 252)
    result = _mean(-runway + 0.3 * penalty, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: distress-acceleration over 2yr = jerk of tri-driver score (long horizon)
def f40cd_f40_cash_burn_distress_longjerk_504d_base_v131_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 504)
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 504), 504)
    zl = _z(_f40_leverage(debt, equity, cashneq), 504)
    score = (zb + zd + zl).ewm(span=126, min_periods=42).mean()
    d1 = score - score.shift(126)
    result = d1 - d1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: chronic-vs-acute distress spread (long-burn-frac minus short-burn-severity)
def f40cd_f40_cash_burn_distress_chronacute_504d_base_v132_signal(ncfo, cashneq, debt, equity):
    chronic = _mean(_f40_burning(ncfo), 504)
    acute = np.tanh(_f40_burn_pressure(cashneq, ncfo)) * np.tanh(_f40_leverage(debt, equity, cashneq).clip(lower=0))
    result = chronic - acute.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# composite: zombie-tenure = how long the firm has been jointly burn+levered (norm)
def f40cd_f40_cash_burn_distress_zombietenure_base_v133_signal(ncfo, debt, equity, cashneq):
    both = _f40_burning(ncfo) * _f40_levered(debt, equity, cashneq)
    streak = _f40_streak(both)
    bp = np.tanh(_f40_burn_pressure(cashneq, ncfo))
    result = (streak.clip(upper=504) / 504.0) * (1.0 + bp).rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# composite: distress-distance recovery over 2yr (net-cash improving while leverage falls)
def f40cd_f40_cash_burn_distress_longrecovery_504d_base_v134_signal(cashneq, debt, equity):
    netcash = (cashneq - debt) / (equity.abs() + 1.0)
    lev = (debt - cashneq) / equity.abs().replace(0, np.nan)
    result = _mean(_f40_zsigninter((netcash - netcash.shift(252)), -(lev - lev.shift(252)), 504), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# === ZONE 14: smoothed / bounded final composites ===

# composite: bounded tri-driver distress (logistic of weighted z-sum)
def f40cd_f40_cash_burn_distress_logistic_252d_base_v135_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 252)
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    zl = _z(_f40_leverage(debt, equity, cashneq), 252)
    # logistic of the WORST-of-three driver floor (z-min) -> distinct from any weighted sum
    floor = pd.concat([zb, zd, zl], axis=1).min(axis=1)
    result = _mean(1.0 / (1.0 + np.exp(-floor)) - 0.5, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn-and-dilution EWMA composite (sticky paper-funded-burn state)
def f40cd_f40_cash_burn_distress_bdewma_252d_base_v136_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    comp = _f40_zprod(_f40_burn_pressure(cashneq, ncfo), _f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    result = comp.ewm(span=84, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn-leverage composite minus its own slow EMA (distress displacement)
def f40cd_f40_cash_burn_distress_bldisp_252d_base_v137_signal(cashneq, ncfo, debt, equity):
    comp = _f40_zprod(_f40_burn_pressure(cashneq, ncfo), _f40_leverage(debt, equity, cashneq), 252)
    result = comp - comp.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# composite: no-profit & dilution composite rank vs 2yr (issuing-into-losses extremity)
def f40cd_f40_cash_burn_distress_ndextpct_504d_base_v138_signal(ncfo, opex, sbcomp, sharesbas, equity):
    comp = _f40_zprod(_f40_noprofit(ncfo, opex), _f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    result = _rank(comp, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: tri-driver score skew (asymmetry of joint stress distribution)
def f40cd_f40_cash_burn_distress_scoreskew_504d_base_v139_signal(cashneq, ncfo, debt, equity):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 252)
    zl = _z(_f40_leverage(debt, equity, cashneq), 252)
    score = zb + zl
    m = _mean(score, 252)
    sd = _std(score, 252).replace(0, np.nan)
    result = _mean(((score - m) / sd) ** 3, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn x leverage harmonic mean (both must be elevated to score)
def f40cd_f40_cash_burn_distress_blharm_252d_base_v140_signal(cashneq, ncfo, debt, equity):
    bp = _f40_burn_pressure(cashneq, ncfo).clip(lower=0) + 0.05
    lev = _f40_leverage(debt, equity, cashneq).clip(lower=0) + 0.05
    harm = 2.0 / (1.0 / bp + 1.0 / lev)
    result = _mean(np.tanh(harm), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: dilution x no-profit harmonic (issuing-into-deep-losses)
def f40cd_f40_cash_burn_distress_dnharm_252d_base_v141_signal(sbcomp, sharesbas, equity, ncfo, opex):
    dil = (_f40_dilution(sbcomp, sharesbas, equity, 252) * 5.0).clip(lower=0) + 0.05
    npth = _f40_noprofit(ncfo, opex).clip(lower=0) + 0.05
    harm = 2.0 / (1.0 / dil + 1.0 / npth)
    result = _mean(np.tanh(harm), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn-pressure & leverage co-volatility (do they spike together)
def f40cd_f40_cash_burn_distress_blcovol_252d_base_v142_signal(cashneq, ncfo, debt, equity):
    bp = _f40_burn_pressure(cashneq, ncfo)
    lev = _f40_leverage(debt, equity, cashneq)
    vb = _std(bp, 63)
    vl = _std(lev, 63)
    result = _mean(_f40_zprod(vb, vl, 252), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: weighted distress with dilution sign-flip (good vs bad dilution)
def f40cd_f40_cash_burn_distress_signeddil_252d_base_v143_signal(cashneq, ncfo, sbcomp, sharesbas, equity):
    bp = _f40_burn_pressure(cashneq, ncfo)
    dilz = _z(_f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    burnsign = pd.Series(np.where(ncfo < 0, 1.0, -1.0), index=ncfo.index)
    result = _mean(burnsign * dilz * np.tanh(bp), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: cash-runway-shortness AND leverage z-sum (additive survival risk)
def f40cd_f40_cash_burn_distress_addrisk_252d_base_v144_signal(cashneq, debt, ncfo, equity):
    netcash = cashneq - debt
    burn = (-ncfo).clip(lower=0.0) + 1.0
    shortz = _z(-(netcash / burn), 252)
    levz = _z(_f40_leverage(debt, equity, cashneq), 252)
    result = _mean(shortz + levz, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: worst pairwise-product among the three drivers (most-stressed driver pair)
def f40cd_f40_cash_burn_distress_worstpair_252d_base_v145_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 252)
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    zl = _z(_f40_leverage(debt, equity, cashneq), 252)
    pairmax = pd.concat([zb * zd, zb * zl, zd * zl], axis=1).max(axis=1)
    result = _mean(pairmax, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: burn-pressure conditioned on leverage above median (regime-gated burn)
def f40cd_f40_cash_burn_distress_gatedburn_252d_base_v146_signal(cashneq, ncfo, debt, equity):
    bp = _f40_burn_pressure(cashneq, ncfo)
    lev = _f40_leverage(debt, equity, cashneq)
    gate = (lev > lev.rolling(252, min_periods=126).median()).astype(float)
    result = _mean(np.tanh(bp) * gate, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: dilution intensity premium when burning vs not (conditional dilution lift)
def f40cd_f40_cash_burn_distress_gateddil_252d_base_v147_signal(ncfo, sbcomp, sharesbas, equity):
    dil = np.tanh(_f40_dilution(sbcomp, sharesbas, equity, 252) * 5.0)
    burn = _f40_burning(ncfo)
    dil_when_burn = (dil * burn).rolling(252, min_periods=126).sum() / burn.rolling(252, min_periods=126).sum().replace(0, np.nan)
    dil_overall = dil.rolling(252, min_periods=126).mean()
    result = dil_when_burn - dil_overall
    return result.replace([np.inf, -np.inf], np.nan)


# composite: tri-driver Euclidean distress distance (magnitude of z-driver vector)
def f40cd_f40_cash_burn_distress_distmag_252d_base_v148_signal(cashneq, ncfo, sbcomp, sharesbas, equity, debt):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 252)
    zd = _z(_f40_dilution(sbcomp, sharesbas, equity, 252), 252)
    zl = _z(_f40_leverage(debt, equity, cashneq), 252)
    result = _mean(np.sqrt(zb ** 2 + zd ** 2 + zl ** 2), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: distress-distance directionality (is the z-vector pointing more-distressed)
def f40cd_f40_cash_burn_distress_distdir_252d_base_v149_signal(cashneq, ncfo, debt, equity, opex):
    zb = _z(_f40_burn_pressure(cashneq, ncfo), 252)
    zl = _z(_f40_leverage(debt, equity, cashneq), 252)
    zn = _z(_f40_noprofit(ncfo, opex), 252)
    mag = np.sqrt(zb ** 2 + zl ** 2 + zn ** 2).replace(0, np.nan)
    result = _mean((zb + zl + zn) / mag, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: distress resilience = net-cash-buffer z minus burn-leverage z (anti-distress)
def f40cd_f40_cash_burn_distress_resilience_base_v150_signal(cashneq, debt, ncfo, equity):
    buffer = (cashneq - debt) / (equity.abs() + 1.0)
    bufz = _z(buffer, 252)
    bp = _z(_f40_burn_pressure(cashneq, ncfo), 252)
    levz = _z(_f40_leverage(debt, equity, cashneq), 252)
    result = _mean(bufz - 0.5 * (bp + levz), 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f40cd_f40_cash_burn_distress_blpctile_252d_base_v076_signal,
    f40cd_f40_cash_burn_distress_bdpctile_252d_base_v077_signal,
    f40cd_f40_cash_burn_distress_dlpctile_252d_base_v078_signal,
    f40cd_f40_cash_burn_distress_ndpctile_252d_base_v079_signal,
    f40cd_f40_cash_burn_distress_blpctmin_252d_base_v080_signal,
    f40cd_f40_cash_burn_distress_worstpct_252d_base_v081_signal,
    f40cd_f40_cash_burn_distress_rankmom_252d_base_v082_signal,
    f40cd_f40_cash_burn_distress_netrwpct_504d_base_v083_signal,
    f40cd_f40_cash_burn_distress_pctdisp_252d_base_v084_signal,
    f40cd_f40_cash_burn_distress_signagree_252d_base_v085_signal,
    f40cd_f40_cash_burn_distress_bdtrend_252d_base_v086_signal,
    f40cd_f40_cash_burn_distress_blaccel_252d_base_v087_signal,
    f40cd_f40_cash_burn_distress_nlyoy_252d_base_v088_signal,
    f40cd_f40_cash_burn_distress_dllevel_252d_base_v089_signal,
    f40cd_f40_cash_burn_distress_bnvol_252d_base_v090_signal,
    f40cd_f40_cash_burn_distress_dlrotate_252d_base_v091_signal,
    f40cd_f40_cash_burn_distress_blextpct_504d_base_v092_signal,
    f40cd_f40_cash_burn_distress_scoreaccel_252d_base_v093_signal,
    f40cd_f40_cash_burn_distress_bdleadlag_252d_base_v094_signal,
    f40cd_f40_cash_burn_distress_dilbuffer_252d_base_v095_signal,
    f40cd_f40_cash_burn_distress_eqbuffer_252d_base_v096_signal,
    f40cd_f40_cash_burn_distress_monthsxdil_252d_base_v097_signal,
    f40cd_f40_cash_burn_distress_solvmargin_252d_base_v098_signal,
    f40cd_f40_cash_burn_distress_bufburnmin_252d_base_v099_signal,
    f40cd_f40_cash_burn_distress_runshortlev_252d_base_v100_signal,
    f40cd_f40_cash_burn_distress_eqvsburn_504d_base_v101_signal,
    f40cd_f40_cash_burn_distress_lowcashhighdil_252d_base_v102_signal,
    f40cd_f40_cash_burn_distress_insolvtrend_252d_base_v103_signal,
    f40cd_f40_cash_burn_distress_cashcover_252d_base_v104_signal,
    f40cd_f40_cash_burn_distress_dualmedian_252d_base_v105_signal,
    f40cd_f40_cash_burn_distress_nplevreg_252d_base_v106_signal,
    f40cd_f40_cash_burn_distress_dualrunmax_252d_base_v107_signal,
    f40cd_f40_cash_burn_distress_scoretrans_252d_base_v108_signal,
    f40cd_f40_cash_burn_distress_dualsev_252d_base_v109_signal,
    f40cd_f40_cash_burn_distress_detbreadth_252d_base_v110_signal,
    f40cd_f40_cash_burn_distress_allworsen_252d_base_v111_signal,
    f40cd_f40_cash_burn_distress_stresspersist_252d_base_v112_signal,
    f40cd_f40_cash_burn_distress_deepregime_504d_base_v113_signal,
    f40cd_f40_cash_burn_distress_netentries_504d_base_v114_signal,
    f40cd_f40_cash_burn_distress_burneqerode_252d_base_v115_signal,
    f40cd_f40_cash_burn_distress_finchannel_252d_base_v116_signal,
    f40cd_f40_cash_burn_distress_negeqburn_252d_base_v117_signal,
    f40cd_f40_cash_burn_distress_triz_252d_base_v118_signal,
    f40cd_f40_cash_burn_distress_burnamp_252d_base_v119_signal,
    f40cd_f40_cash_burn_distress_dilintolev_252d_base_v120_signal,
    f40cd_f40_cash_burn_distress_structmin_504d_base_v121_signal,
    f40cd_f40_cash_burn_distress_netdistress_252d_base_v122_signal,
    f40cd_f40_cash_burn_distress_paperruntime_252d_base_v123_signal,
    f40cd_f40_cash_burn_distress_concurrank_504d_base_v124_signal,
    f40cd_f40_cash_burn_distress_exhaust_504d_base_v125_signal,
    f40cd_f40_cash_burn_distress_chronic_504d_base_v126_signal,
    f40cd_f40_cash_burn_distress_cumdrag_504d_base_v127_signal,
    f40cd_f40_cash_burn_distress_bookerode_504d_base_v128_signal,
    f40cd_f40_cash_burn_distress_terminaltriad_252d_base_v129_signal,
    f40cd_f40_cash_burn_distress_survindex_252d_base_v130_signal,
    f40cd_f40_cash_burn_distress_longjerk_504d_base_v131_signal,
    f40cd_f40_cash_burn_distress_chronacute_504d_base_v132_signal,
    f40cd_f40_cash_burn_distress_zombietenure_base_v133_signal,
    f40cd_f40_cash_burn_distress_longrecovery_504d_base_v134_signal,
    f40cd_f40_cash_burn_distress_logistic_252d_base_v135_signal,
    f40cd_f40_cash_burn_distress_bdewma_252d_base_v136_signal,
    f40cd_f40_cash_burn_distress_bldisp_252d_base_v137_signal,
    f40cd_f40_cash_burn_distress_ndextpct_504d_base_v138_signal,
    f40cd_f40_cash_burn_distress_scoreskew_504d_base_v139_signal,
    f40cd_f40_cash_burn_distress_blharm_252d_base_v140_signal,
    f40cd_f40_cash_burn_distress_dnharm_252d_base_v141_signal,
    f40cd_f40_cash_burn_distress_blcovol_252d_base_v142_signal,
    f40cd_f40_cash_burn_distress_signeddil_252d_base_v143_signal,
    f40cd_f40_cash_burn_distress_addrisk_252d_base_v144_signal,
    f40cd_f40_cash_burn_distress_worstpair_252d_base_v145_signal,
    f40cd_f40_cash_burn_distress_gatedburn_252d_base_v146_signal,
    f40cd_f40_cash_burn_distress_gateddil_252d_base_v147_signal,
    f40cd_f40_cash_burn_distress_distmag_252d_base_v148_signal,
    f40cd_f40_cash_burn_distress_distdir_252d_base_v149_signal,
    f40cd_f40_cash_burn_distress_resilience_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F40_CASH_BURN_DISTRESS_REGISTRY_076_150 = REGISTRY


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
        g = np.random.default_rng(seed)
        nq = n // 63 + 1
        steps = np.repeat(g.normal(drift, vol, nq), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if amp:
            cyc = np.repeat(g.normal(0.0, 1.0, nq), 63)[:n]
            s = s + amp * base * cyc
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

    print("OK f40_cash_burn_distress_base_076_150_claude: %d features pass" % n_features)
