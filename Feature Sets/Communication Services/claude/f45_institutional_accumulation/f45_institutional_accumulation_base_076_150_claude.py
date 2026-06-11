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


# ===== family ownership primitives (institutional accumulation, sf3a) =====
def _f45_growth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f45_roc(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _f45_share(s, w):
    return s / _mean(s, w).replace(0, np.nan)


def _f45_eff(s, w):
    # accumulation efficiency: signed net move / total path traveled
    net = s - s.shift(w)
    path = s.diff().abs().rolling(w, min_periods=max(2, w // 2)).sum()
    return np.sign(net) * net.abs() / path.replace(0, np.nan)


# ============================================================
# inst-value trend: 5d weekly value growth (very fast accumulation impulse)
def f45ia_f45_institutional_accumulation_valgrow_5d_base_v076_signal(shrvalue):
    b = _f45_growth(shrvalue, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst-holder trend: 504d two-year holder growth (long breadth build)
def f45ia_f45_institutional_accumulation_holdgrow_504d_base_v077_signal(shrholders):
    b = _f45_growth(shrholders, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst-units trend: 504d two-year unit growth (long position build)
def f45ia_f45_institutional_accumulation_unitgrow_504d_base_v078_signal(shrunits):
    b = _f45_growth(shrunits, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership-value: totalvalue 252d growth (annual aggregate ownership build)
def f45ia_f45_institutional_accumulation_totvalgrow_252d_base_v079_signal(totalvalue):
    b = _f45_growth(totalvalue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst ownership %: shrvalue/marketcap percentile-ranked vs own 504d history
def f45ia_f45_institutional_accumulation_ownpctrank_504d_base_v080_signal(shrvalue, marketcap):
    own = shrvalue / marketcap.replace(0, np.nan)
    b = own.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation efficiency: holder-count net move / path over 252d (clean breadth trend)
def f45ia_f45_institutional_accumulation_holdeff_252d_base_v081_signal(shrholders):
    b = _f45_eff(shrholders, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation efficiency: unit net move / path over 252d (clean position trend)
def f45ia_f45_institutional_accumulation_uniteff_252d_base_v082_signal(shrunits):
    b = _f45_eff(shrunits, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation efficiency: value net move / path over 504d (clean long value trend)
def f45ia_f45_institutional_accumulation_valeff_504d_base_v083_signal(shrvalue):
    b = _f45_eff(shrvalue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units-per-holder level vs marketcap (block conviction relative to size)
def f45ia_f45_institutional_accumulation_uphvscap_base_v084_signal(shrunits, shrholders, marketcap):
    uph = shrunits / shrholders.replace(0, np.nan)
    b = uph / marketcap.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value share vs trailing 63d mean (short-horizon value surge)
def f45ia_f45_institutional_accumulation_valshare_63d_base_v085_signal(shrvalue):
    b = _f45_share(shrvalue, 63) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder share vs trailing 126d mean (medium-horizon breadth surge)
def f45ia_f45_institutional_accumulation_holdshare_126d_base_v086_signal(shrholders):
    b = _f45_share(shrholders, 126) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units share vs trailing 252d mean (long-horizon position surge)
def f45ia_f45_institutional_accumulation_unitshare_252d_base_v087_signal(shrunits):
    b = _f45_share(shrunits, 252) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-count z vs 126d history (medium de-trended breadth extremity)
def f45ia_f45_institutional_accumulation_holdz_126d_base_v088_signal(shrholders):
    b = _z(shrholders, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-ownership value z vs 252d history (aggregate de-trended value extremity)
def f45ia_f45_institutional_accumulation_totvalz_252d_base_v089_signal(totalvalue):
    b = _z(totalvalue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units z vs 252d history (annual de-trended position extremity)
def f45ia_f45_institutional_accumulation_unitz_252d_base_v090_signal(shrunits):
    b = _z(shrunits, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-vs-cap relative growth over 504d (institutions outpacing price, long horizon)
def f45ia_f45_institutional_accumulation_valvscap_504d_base_v091_signal(shrvalue, marketcap):
    b = _f45_growth(shrvalue, 504) - _f45_growth(marketcap, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units-vs-cap relative growth over 63d (real share accumulation net of price, short)
def f45ia_f45_institutional_accumulation_unitvscap_63d_base_v092_signal(shrunits, marketcap):
    b = _f45_growth(shrunits, 63) - _f45_growth(marketcap, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value vs holder growth divergence over 126d (concentration vs broadening, medium)
def f45ia_f45_institutional_accumulation_valholddiv_126d_base_v093_signal(shrvalue, shrholders):
    b = _f45_growth(shrvalue, 126) - _f45_growth(shrholders, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# unit vs holder growth divergence over 252d (bigger blocks vs more holders, long)
def f45ia_f45_institutional_accumulation_unitholddiv_252d_base_v094_signal(shrunits, shrholders):
    b = _f45_growth(shrunits, 252) - _f45_growth(shrholders, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value growth acceleration over 126d windows (value-flow second order)
def f45ia_f45_institutional_accumulation_valaccel_126d_base_v095_signal(shrvalue):
    g = _f45_growth(shrvalue, 126)
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# unit growth acceleration over 63d windows (position-flow second order)
def f45ia_f45_institutional_accumulation_unitaccel_63d_base_v096_signal(shrunits):
    g = _f45_growth(shrunits, 63)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder growth acceleration over 126d windows (breadth-flow second order)
def f45ia_f45_institutional_accumulation_holdaccel_126d_base_v097_signal(shrholders):
    g = _f45_growth(shrholders, 126)
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage (shrvalue/totalvalue) ranked vs own 504d history (active-share percentile)
def f45ia_f45_institutional_accumulation_coveragerank_base_v098_signal(shrvalue, totalvalue):
    cov = shrvalue / totalvalue.replace(0, np.nan)
    b = cov.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage short-vs-long growth spread (active-share acceleration via windows)
def f45ia_f45_institutional_accumulation_covgrowspr_base_v099_signal(shrvalue, totalvalue):
    cov = shrvalue / totalvalue.replace(0, np.nan)
    b = _f45_roc(cov, 63) - _f45_roc(cov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-ownership flow tilt: 21d totalvalue inflow scaled by 504d typical level (impulse vs long base)
def f45ia_f45_institutional_accumulation_flowtilt_base_v100_signal(totalvalue):
    b = (totalvalue - totalvalue.shift(21)) / _mean(totalvalue, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# unit flow acceleration ratio: 21d unit inflow rate vs 126d unit inflow rate (impulse vs base)
def f45ia_f45_institutional_accumulation_unitflowratio_base_v101_signal(shrunits):
    fast = (shrunits - shrunits.shift(21)) / _mean(shrunits, 252).replace(0, np.nan)
    slow = (shrunits - shrunits.shift(126)) / _mean(shrunits, 252).replace(0, np.nan)
    b = fast - slow / 6.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder new-high frequency: fraction of last quarter holders made a 252d high (breadth)
def f45ia_f45_institutional_accumulation_holdnewhi_base_v102_signal(shrholders):
    hi = _rmax(shrholders, 252)
    is_hi = (shrholders >= hi * 0.99999).astype(float)
    b = is_hi.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value new-high frequency: fraction of last quarter value made a 252d high
def f45ia_f45_institutional_accumulation_valnewhi_base_v103_signal(shrvalue):
    hi = _rmax(shrvalue, 252)
    is_hi = (shrvalue >= hi * 0.99999).astype(float)
    b = is_hi.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units drawup: distance below trailing 252d max units (position pullback depth)
def f45ia_f45_institutional_accumulation_unitdrawup_base_v104_signal(shrunits):
    peak = _rmax(shrunits, 252)
    b = shrunits / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value recovery: distance above trailing 504d min value (long-horizon rebound)
def f45ia_f45_institutional_accumulation_valrecov_504d_base_v105_signal(shrvalue):
    trough = _rmin(shrvalue, 504)
    b = shrvalue / trough.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder recovery: distance above trailing 252d min holders (breadth rebound)
def f45ia_f45_institutional_accumulation_holdrecov_base_v106_signal(shrholders):
    trough = _rmin(shrholders, 252)
    b = shrholders / trough.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder growth over 252d (annual smart-money position re-sizing)
def f45ia_f45_institutional_accumulation_vphgrow_252d_base_v107_signal(shrvalue, shrholders):
    vph = shrvalue / shrholders.replace(0, np.nan)
    b = _f45_growth(vph, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder z vs 252d history (sizing extremity)
def f45ia_f45_institutional_accumulation_vphz_252d_base_v108_signal(shrvalue, shrholders):
    vph = shrvalue / shrholders.replace(0, np.nan)
    b = _z(vph, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit z vs 252d history (implied per-share value extremity)
def f45ia_f45_institutional_accumulation_vpuz_252d_base_v109_signal(shrvalue, shrunits):
    vpu = shrvalue / shrunits.replace(0, np.nan)
    b = _z(vpu, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit growth over 252d (annual implied per-share re-rating by inst)
def f45ia_f45_institutional_accumulation_vpugrow_252d_base_v110_signal(shrvalue, shrunits):
    vpu = shrvalue / shrunits.replace(0, np.nan)
    b = _f45_growth(vpu, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit acceleration: 63d implied re-rating now vs one quarter ago (second order)
def f45ia_f45_institutional_accumulation_vpuaccel_base_v111_signal(shrvalue, shrunits):
    vpu = shrvalue / shrunits.replace(0, np.nan)
    g = _f45_growth(vpu, 63)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage sign x magnitude of 126d momentum (asymmetric active-share flow)
def f45ia_f45_institutional_accumulation_covsignmag_base_v112_signal(shrvalue, totalvalue):
    cov = shrvalue / totalvalue.replace(0, np.nan)
    mom = cov - cov.shift(126)
    b = np.sign(mom) * (mom.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value sign x magnitude of 126d growth (asymmetric value flow)
def f45ia_f45_institutional_accumulation_valsignmag_base_v113_signal(shrvalue):
    g = _f45_growth(shrvalue, 126)
    b = np.sign(g) * (g.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder accumulation streak: count of last 126d with positive 21d holder growth
def f45ia_f45_institutional_accumulation_holdstreak_base_v114_signal(shrholders):
    pos = (_f45_growth(shrholders, 21) > 0).astype(float)
    b = pos.rolling(126, min_periods=42).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# unit accumulation streak: count of last 252d with positive 21d unit growth
def f45ia_f45_institutional_accumulation_unitstreak_base_v115_signal(shrunits):
    pos = (_f45_growth(shrunits, 21) > 0).astype(float)
    b = pos.rolling(252, min_periods=84).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed total-ownership growth momentum (bounded aggregate flow)
def f45ia_f45_institutional_accumulation_tottanh_base_v116_signal(totalvalue):
    chg = _f45_growth(totalvalue, 63)
    b = np.tanh(10.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed unit-growth momentum (bounded position flow)
def f45ia_f45_institutional_accumulation_unittanh_base_v117_signal(shrunits):
    chg = _f45_growth(shrunits, 63)
    b = np.tanh(8.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-flow downside risk: semi-deviation of negative 21d value-growth over 252d (distribution risk)
def f45ia_f45_institutional_accumulation_valdownside_base_v118_signal(shrvalue):
    g = _f45_growth(shrvalue, 21)
    neg = g.where(g < 0)
    b = neg.rolling(252, min_periods=84).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder flow stability: 21d holder-growth mean over its std (steady breadth build)
def f45ia_f45_institutional_accumulation_holdsharpe_base_v119_signal(shrholders):
    g = _f45_growth(shrholders, 21)
    mu = g.rolling(126, min_periods=42).mean()
    sd = g.rolling(126, min_periods=42).std()
    b = mu / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership% deep+broad: ownpct momentum interacted with unit growth (deep real buying)
def f45ia_f45_institutional_accumulation_deepreal_base_v120_signal(shrvalue, marketcap, shrunits):
    own = shrvalue / marketcap.replace(0, np.nan)
    own_mom = own - own.shift(126)
    ug = _f45_growth(shrunits, 126)
    b = own_mom * ug
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation quality: holder-eff and value-eff sign agreement weighted by magnitude
def f45ia_f45_institutional_accumulation_accqual2_base_v121_signal(shrholders, shrvalue):
    he = _f45_eff(shrholders, 252)
    ve = _f45_eff(shrvalue, 252)
    b = np.sign(he) * np.sign(ve) * (he.abs() + ve.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-growth dispersion across 21/63/126 windows (short consistency of flow)
def f45ia_f45_institutional_accumulation_growdisp2_base_v122_signal(shrvalue):
    g1 = _f45_roc(shrvalue, 21)
    g2 = _f45_roc(shrvalue, 63)
    g3 = _f45_roc(shrvalue, 126)
    b = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# unit-growth dispersion across 63/126/252 windows (position consistency)
def f45ia_f45_institutional_accumulation_unitgrowdisp_base_v123_signal(shrunits):
    g1 = _f45_roc(shrunits, 63)
    g2 = _f45_roc(shrunits, 126)
    g3 = _f45_roc(shrunits, 252)
    b = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# passive/other ownership as fraction of marketcap (non-active ownership %-of-cap)
def f45ia_f45_institutional_accumulation_otherownpct_base_v124_signal(totalvalue, shrvalue, marketcap):
    other = (totalvalue - shrvalue).clip(lower=0)
    b = other / marketcap.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# passive/other ownership growth over 63d (non-active accumulation)
def f45ia_f45_institutional_accumulation_othergrow_63d_base_v125_signal(totalvalue, shrvalue):
    other = (totalvalue - shrvalue).clip(lower=0)
    b = _f45_growth(other + 1.0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# totalvalue/marketcap momentum over 63d (broad ownership build vs price, short)
def f45ia_f45_institutional_accumulation_totownmom_63d_base_v126_signal(totalvalue, marketcap):
    own = totalvalue / marketcap.replace(0, np.nan)
    b = own - own.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# totalvalue/marketcap acceleration (broad ownership flow second order)
def f45ia_f45_institutional_accumulation_totownaccel_base_v127_signal(totalvalue, marketcap):
    own = totalvalue / marketcap.replace(0, np.nan)
    mom = own - own.shift(63)
    b = mom - mom.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value risk-adjusted flow over 126d (value growth per unit of its volatility)
def f45ia_f45_institutional_accumulation_riskadjflow126_base_v128_signal(shrvalue):
    g = _f45_growth(shrvalue, 126)
    vol = _f45_growth(shrvalue, 21).rolling(252, min_periods=84).std()
    b = g / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# unit risk-adjusted flow over 63d (unit growth per unit of its volatility)
def f45ia_f45_institutional_accumulation_unitriskadj_base_v129_signal(shrunits):
    g = _f45_growth(shrunits, 63)
    vol = _f45_growth(shrunits, 21).rolling(126, min_periods=42).std()
    b = g / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# active-share mean-reversion: coverage (shrvalue/totalvalue) vs its 252d median (centered)
def f45ia_f45_institutional_accumulation_covmedrev_base_v130_signal(shrvalue, totalvalue):
    cov = shrvalue / totalvalue.replace(0, np.nan)
    med = cov.rolling(252, min_periods=84).median()
    b = cov / med.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# unit-flow asymmetry: mean up-day unit move minus mean down-day unit move over 126d
def f45ia_f45_institutional_accumulation_unitasym_base_v131_signal(shrunits):
    chg = shrunits.pct_change()
    up = chg.clip(lower=0).rolling(126, min_periods=42).mean()
    dn = (-chg.clip(upper=0)).rolling(126, min_periods=42).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-vs-holder growth ranked over 63d (concentration regime percentile)
def f45ia_f45_institutional_accumulation_concregime_base_v132_signal(shrvalue, shrholders):
    spr = _f45_growth(shrvalue, 63) - _f45_growth(shrholders, 63)
    b = spr.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# broad-ownership smoothed displacement: totalvalue/marketcap minus its slow EMA (regime, 252d)
def f45ia_f45_institutional_accumulation_totowndisp252_base_v133_signal(totalvalue, marketcap):
    own = totalvalue / marketcap.replace(0, np.nan)
    b = own - own.ewm(span=252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage smoothed displacement (active-share regime persistence)
def f45ia_f45_institutional_accumulation_covdisp_base_v134_signal(shrvalue, totalvalue):
    cov = shrvalue / totalvalue.replace(0, np.nan)
    b = cov - cov.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value year-over-year growth change (annual value-flow shift)
def f45ia_f45_institutional_accumulation_valyoy_base_v135_signal(shrvalue):
    g = _f45_growth(shrvalue, 63)
    b = g - g.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# unit year-over-year growth change (annual position-flow shift)
def f45ia_f45_institutional_accumulation_unityoy_base_v136_signal(shrunits):
    g = _f45_growth(shrunits, 63)
    b = g - g.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net accumulation composite 2: holder-growth x ownership%-momentum (broad + deepening)
def f45ia_f45_institutional_accumulation_netacc2_base_v137_signal(shrholders, shrvalue, marketcap):
    hg = _f45_growth(shrholders, 126)
    own = shrvalue / marketcap.replace(0, np.nan)
    own_mom = own - own.shift(126)
    b = hg + 5.0 * own_mom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder acceleration: 126d sizing growth now vs half-year ago (second order)
def f45ia_f45_institutional_accumulation_vphaccel_base_v138_signal(shrvalue, shrholders):
    vph = shrvalue / shrholders.replace(0, np.nan)
    g = _f45_growth(vph, 126)
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit rank vs 504d history (implied value percentile, long)
def f45ia_f45_institutional_accumulation_vpurank_base_v139_signal(shrvalue, shrunits):
    vpu = shrvalue / shrunits.replace(0, np.nan)
    b = vpu.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder vs value growth balance over a quarter (breadth vs value concentration, normalized)
def f45ia_f45_institutional_accumulation_breadthvalbal_base_v140_signal(shrholders, shrvalue):
    hg = _f45_growth(shrholders, 63).clip(lower=-1.0, upper=1.0)
    vg = _f45_growth(shrvalue, 63).clip(lower=-1.0, upper=1.0)
    b = (hg - vg) / (hg.abs() + vg.abs() + 1e-6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value vs total balance over a quarter (active vs broad flow, normalized)
def f45ia_f45_institutional_accumulation_activebal_base_v141_signal(shrvalue, totalvalue):
    vg = _f45_growth(shrvalue, 63).clip(lower=-1.0, upper=1.0)
    tg = _f45_growth(totalvalue, 63).clip(lower=-1.0, upper=1.0)
    b = (vg - tg) / (vg.abs() + tg.abs() + 1e-6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units breakout: shrunits vs prior 252d max (new position-high headroom)
def f45ia_f45_institutional_accumulation_unitbreakout_base_v142_signal(shrunits):
    prior_hi = shrunits.shift(21).rolling(252, min_periods=84).max()
    b = shrunits / prior_hi.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value breakout: value vs prior 252d max (new value-high headroom)
def f45ia_f45_institutional_accumulation_valbreakout_base_v143_signal(shrvalue):
    prior_hi = shrvalue.shift(1).rolling(252, min_periods=84).max()
    b = shrvalue / prior_hi.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage flow: change in shrvalue/totalvalue scaled by typical (active-share inflow)
def f45ia_f45_institutional_accumulation_covflow_base_v144_signal(shrvalue, totalvalue):
    cov = shrvalue / totalvalue.replace(0, np.nan)
    b = (cov - cov.shift(21)) / _mean(cov, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units-per-holder efficiency: net move / path over 252d (clean block-conviction trend)
def f45ia_f45_institutional_accumulation_upheff_base_v145_signal(shrunits, shrholders):
    uph = shrunits / shrholders.replace(0, np.nan)
    b = _f45_eff(uph, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership% churn: volatility of daily ownership%-of-cap changes over 126d (instability)
def f45ia_f45_institutional_accumulation_ownchurn_base_v146_signal(shrvalue, marketcap):
    own = shrvalue / marketcap.replace(0, np.nan)
    b = own.pct_change().rolling(126, min_periods=42).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-vs-total relative compression: 126d value growth minus 126d totalvalue growth, centered
def f45ia_f45_institutional_accumulation_valtotcompress_base_v147_signal(shrvalue, totalvalue):
    spr = _f45_growth(shrvalue, 126) - _f45_growth(totalvalue, 126)
    typ = spr.rolling(252, min_periods=84).mean()
    b = spr - typ
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-vs-total relative compression: 126d holder growth minus 126d totalvalue growth, centered
def f45ia_f45_institutional_accumulation_holdtotcompress_base_v148_signal(shrholders, totalvalue):
    spr = _f45_growth(shrholders, 126) - _f45_growth(totalvalue, 126)
    typ = spr.rolling(252, min_periods=84).mean()
    b = spr - typ
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deep-broad triple composite: holder-surge x value-surge interaction gated by ownership%-of-cap
def f45ia_f45_institutional_accumulation_triplecomp_base_v149_signal(shrvalue, marketcap, shrholders):
    own = shrvalue / marketcap.replace(0, np.nan)
    breadth = _f45_share(shrholders, 252) - 1.0
    valsurge = _f45_share(shrvalue, 126) - 1.0
    b = breadth * valsurge * np.sign(own - own.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smart-money inflow composite: value-per-holder growth x ownership%-of-cap level
def f45ia_f45_institutional_accumulation_smartflow_base_v150_signal(shrvalue, shrholders, marketcap):
    vph = shrvalue / shrholders.replace(0, np.nan)
    vphg = _f45_growth(vph, 63)
    own = shrvalue / marketcap.replace(0, np.nan)
    b = vphg * own
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f45ia_f45_institutional_accumulation_valgrow_5d_base_v076_signal,
    f45ia_f45_institutional_accumulation_holdgrow_504d_base_v077_signal,
    f45ia_f45_institutional_accumulation_unitgrow_504d_base_v078_signal,
    f45ia_f45_institutional_accumulation_totvalgrow_252d_base_v079_signal,
    f45ia_f45_institutional_accumulation_ownpctrank_504d_base_v080_signal,
    f45ia_f45_institutional_accumulation_holdeff_252d_base_v081_signal,
    f45ia_f45_institutional_accumulation_uniteff_252d_base_v082_signal,
    f45ia_f45_institutional_accumulation_valeff_504d_base_v083_signal,
    f45ia_f45_institutional_accumulation_uphvscap_base_v084_signal,
    f45ia_f45_institutional_accumulation_valshare_63d_base_v085_signal,
    f45ia_f45_institutional_accumulation_holdshare_126d_base_v086_signal,
    f45ia_f45_institutional_accumulation_unitshare_252d_base_v087_signal,
    f45ia_f45_institutional_accumulation_holdz_126d_base_v088_signal,
    f45ia_f45_institutional_accumulation_totvalz_252d_base_v089_signal,
    f45ia_f45_institutional_accumulation_unitz_252d_base_v090_signal,
    f45ia_f45_institutional_accumulation_valvscap_504d_base_v091_signal,
    f45ia_f45_institutional_accumulation_unitvscap_63d_base_v092_signal,
    f45ia_f45_institutional_accumulation_valholddiv_126d_base_v093_signal,
    f45ia_f45_institutional_accumulation_unitholddiv_252d_base_v094_signal,
    f45ia_f45_institutional_accumulation_valaccel_126d_base_v095_signal,
    f45ia_f45_institutional_accumulation_unitaccel_63d_base_v096_signal,
    f45ia_f45_institutional_accumulation_holdaccel_126d_base_v097_signal,
    f45ia_f45_institutional_accumulation_coveragerank_base_v098_signal,
    f45ia_f45_institutional_accumulation_covgrowspr_base_v099_signal,
    f45ia_f45_institutional_accumulation_flowtilt_base_v100_signal,
    f45ia_f45_institutional_accumulation_unitflowratio_base_v101_signal,
    f45ia_f45_institutional_accumulation_holdnewhi_base_v102_signal,
    f45ia_f45_institutional_accumulation_valnewhi_base_v103_signal,
    f45ia_f45_institutional_accumulation_unitdrawup_base_v104_signal,
    f45ia_f45_institutional_accumulation_valrecov_504d_base_v105_signal,
    f45ia_f45_institutional_accumulation_holdrecov_base_v106_signal,
    f45ia_f45_institutional_accumulation_vphgrow_252d_base_v107_signal,
    f45ia_f45_institutional_accumulation_vphz_252d_base_v108_signal,
    f45ia_f45_institutional_accumulation_vpuz_252d_base_v109_signal,
    f45ia_f45_institutional_accumulation_vpugrow_252d_base_v110_signal,
    f45ia_f45_institutional_accumulation_vpuaccel_base_v111_signal,
    f45ia_f45_institutional_accumulation_covsignmag_base_v112_signal,
    f45ia_f45_institutional_accumulation_valsignmag_base_v113_signal,
    f45ia_f45_institutional_accumulation_holdstreak_base_v114_signal,
    f45ia_f45_institutional_accumulation_unitstreak_base_v115_signal,
    f45ia_f45_institutional_accumulation_tottanh_base_v116_signal,
    f45ia_f45_institutional_accumulation_unittanh_base_v117_signal,
    f45ia_f45_institutional_accumulation_valdownside_base_v118_signal,
    f45ia_f45_institutional_accumulation_holdsharpe_base_v119_signal,
    f45ia_f45_institutional_accumulation_deepreal_base_v120_signal,
    f45ia_f45_institutional_accumulation_accqual2_base_v121_signal,
    f45ia_f45_institutional_accumulation_growdisp2_base_v122_signal,
    f45ia_f45_institutional_accumulation_unitgrowdisp_base_v123_signal,
    f45ia_f45_institutional_accumulation_otherownpct_base_v124_signal,
    f45ia_f45_institutional_accumulation_othergrow_63d_base_v125_signal,
    f45ia_f45_institutional_accumulation_totownmom_63d_base_v126_signal,
    f45ia_f45_institutional_accumulation_totownaccel_base_v127_signal,
    f45ia_f45_institutional_accumulation_riskadjflow126_base_v128_signal,
    f45ia_f45_institutional_accumulation_unitriskadj_base_v129_signal,
    f45ia_f45_institutional_accumulation_covmedrev_base_v130_signal,
    f45ia_f45_institutional_accumulation_unitasym_base_v131_signal,
    f45ia_f45_institutional_accumulation_concregime_base_v132_signal,
    f45ia_f45_institutional_accumulation_totowndisp252_base_v133_signal,
    f45ia_f45_institutional_accumulation_covdisp_base_v134_signal,
    f45ia_f45_institutional_accumulation_valyoy_base_v135_signal,
    f45ia_f45_institutional_accumulation_unityoy_base_v136_signal,
    f45ia_f45_institutional_accumulation_netacc2_base_v137_signal,
    f45ia_f45_institutional_accumulation_vphaccel_base_v138_signal,
    f45ia_f45_institutional_accumulation_vpurank_base_v139_signal,
    f45ia_f45_institutional_accumulation_breadthvalbal_base_v140_signal,
    f45ia_f45_institutional_accumulation_activebal_base_v141_signal,
    f45ia_f45_institutional_accumulation_unitbreakout_base_v142_signal,
    f45ia_f45_institutional_accumulation_valbreakout_base_v143_signal,
    f45ia_f45_institutional_accumulation_covflow_base_v144_signal,
    f45ia_f45_institutional_accumulation_upheff_base_v145_signal,
    f45ia_f45_institutional_accumulation_ownchurn_base_v146_signal,
    f45ia_f45_institutional_accumulation_valtotcompress_base_v147_signal,
    f45ia_f45_institutional_accumulation_holdtotcompress_base_v148_signal,
    f45ia_f45_institutional_accumulation_triplecomp_base_v149_signal,
    f45ia_f45_institutional_accumulation_smartflow_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F45_INSTITUTIONAL_ACCUMULATION_REGISTRY_076_150 = REGISTRY


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

    shrholders = _fund(101, base=350.0, drift=0.05, vol=0.10).rename("shrholders")
    shrunits = _fund(102, base=4.0e7, drift=0.06, vol=0.12).rename("shrunits")
    shrvalue = _fund(103, base=6.0e8, drift=0.05, vol=0.11).rename("shrvalue")
    totalvalue = _fund(104, base=9.0e8, drift=0.045, vol=0.10).rename("totalvalue")
    marketcap = _fund(105, base=1.5e9, drift=0.035, vol=0.13).rename("marketcap")

    cols = {
        "shrholders": shrholders, "shrunits": shrunits, "shrvalue": shrvalue,
        "totalvalue": totalvalue, "marketcap": marketcap,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "BAD INPUTS %s: %s" % (name, meta["inputs"])
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

    print("OK f45_institutional_accumulation_base_076_150_claude: %d features pass" % n_features)
