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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _growth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _chg(s, w):
    return s - s.shift(w)


# ===== folder domain primitives (capital cycle: build COUPLED WITH return) =====
# TIGHTENED DOMAIN (part 2): every feature couples a build/investment term WITH a
# return-on-capital term. NO standalone capex/asset/ppne LEVELS or GROWTH (f30/f28).
def _f40_capex_intensity(capex, assets):
    return capex / assets.replace(0, np.nan)


def _f40_capex_to_ppne(capex, ppnenet):
    return capex / ppnenet.replace(0, np.nan)


def _f40_asset_growth(assets, w):
    return np.log(assets.replace(0, np.nan) / assets.shift(w).replace(0, np.nan))


def _f40_invcap_growth(invcap, w):
    return np.log(invcap.replace(0, np.nan) / invcap.shift(w).replace(0, np.nan))


def _f40_roic_sm(roic, w):
    return roic.rolling(w, min_periods=max(1, w // 2)).mean()


def _f40_roic_below_hurdle(roic, w=504):
    # how far smoothed ROIC sits below its own mid-cycle hurdle (rolling median)
    sm = roic.rolling(63, min_periods=21).mean()
    hurdle = roic.rolling(w, min_periods=max(1, w // 2)).median()
    return (hurdle - sm).clip(lower=0)


def _f40_marginal_roic(invcap, roic, w):
    dr = roic - roic.shift(w)
    dg = np.log(invcap.replace(0, np.nan) / invcap.shift(w).replace(0, np.nan))
    return dr / dg.replace(0, np.nan)


def _f40_build_minus_return(growth_term, roic, w):
    dr = roic - roic.shift(w)
    return growth_term - dr


# ============================================================
# CAPITAL-CYCLE part 2: continued divergence facets — interactions, regimes,
# dispersions, distances, streaks — each COUPLING a build/investment term with the
# ROIC/return dimension. Inputs subset of {capex, assets, ppnenet, roic, invcap}.

# marginal-ROIC level (504d): ΔROIC per unit of invcap growth, smoothed (return on new capital)
def f40cc_f40_capital_cycle_signal_margroicsm_504d_base_v076_signal(invcap, roic):
    b = _f40_marginal_roic(invcap, roic, 504).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC drawdown from 504d peak scaled by capex intensity (penalised return drawdown)
def f40cc_f40_capital_cycle_signal_roicddxbuild_base_v077_signal(roic, capex, assets):
    rdd = roic - _rmax(roic, 504)
    ci = _f40_capex_intensity(capex, assets)
    b = rdd * (1.0 + _z(ci, 504).clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-intensity acceleration signed by ROIC trend (build accel into rising/falling return)
def f40cc_f40_capital_cycle_signal_capexaccelxret_base_v078_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    d = ci - ci.shift(126)
    accel = d - d.shift(126)
    b = accel * np.tanh(-5.0 * _chg(roic, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-growth z minus ROIC z 504d (normalised build-vs-return divergence)
def f40cc_f40_capital_cycle_signal_buildretz2_504d_base_v079_signal(assets, roic):
    b = _z(_f40_asset_growth(assets, 504), 504) - _z(roic, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-above-median streak weighted by ROIC shortfall (sustained low-return over-build)
def f40cc_f40_capital_cycle_signal_reinvstreaklow_base_v080_signal(capex, ppnenet, roic):
    rr = _f40_capex_to_ppne(capex, ppnenet)
    above = (rr > rr.rolling(252, min_periods=126).median()).astype(float)
    grp = (above != above.shift(1)).cumsum()
    streak = (above.groupby(grp).cumsum() * above) / 252.0
    pen = 1.0 + 4.0 * _f40_roic_below_hurdle(roic)
    b = streak * pen
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap-growth rank minus ROIC rank 504d (build-position vs return-position)
def f40cc_f40_capital_cycle_signal_invgvsroicrank_504d_base_v081_signal(invcap, roic):
    g = _f40_invcap_growth(invcap, 252)
    b = _rank(g, 504) - _rank(roic, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC trough-position interacted with capex starvation (return bottom + under-build)
def f40cc_f40_capital_cycle_signal_roictroughstarve_1260d_base_v082_signal(roic, capex, assets):
    hi = _rmax(roic, 1260)
    lo = _rmin(roic, 1260)
    rpos = (roic - lo) / (hi - lo).replace(0, np.nan) - 0.5
    starve = (-_z(_f40_capex_intensity(capex, assets), 504)).clip(lower=0)
    b = (-rpos) * (0.5 + starve)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-landing spread (capex/PP&E z minus capex/assets z) gated by ROIC weakness
def f40cc_f40_capital_cycle_signal_capexlocxlow_base_v083_signal(capex, assets, ppnenet, roic):
    a = _f40_capex_intensity(capex, assets)
    p = _f40_capex_to_ppne(capex, ppnenet)
    spread = _z(p, 252) - _z(a, 252)
    pen = 1.0 + 4.0 * _f40_roic_below_hurdle(roic)
    b = spread * pen
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative excess capex intensity over 252d, signed by ROIC shortfall (sustained mis-build)
def f40cc_f40_capital_cycle_signal_cumoverinvlow_1260d_base_v084_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    excess = (ci - _mean(ci, 1260)).rolling(252, min_periods=126).sum()
    pen = 1.0 + 4.0 * _f40_roic_below_hurdle(roic)
    b = _z(excess, 504) * pen
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC per unit of invested-capital growth, smoothed (capital-deployment efficiency)
def f40cc_f40_capital_cycle_signal_roicpergrowth_base_v085_signal(roic, invcap):
    g = _f40_invcap_growth(invcap, 252)
    b = _f40_roic_sm(roic, 63) / (g.abs() + 0.03)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-spend volatility relative to ROIC volatility (which leg drives the cycle)
def f40cc_f40_capital_cycle_signal_volratio_base_v086_signal(capex, roic):
    cv = _std(_growth(capex, 63), 252)
    rv = _std(roic, 252)
    b = cv / (rv + 0.01)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed asset-build EMA times negative ROIC trend (persistent build into weak return)
def f40cc_f40_capital_cycle_signal_buildemaxret_base_v087_signal(assets, roic):
    g = _f40_asset_growth(assets, 63).ewm(span=126, min_periods=63).mean()
    b = _z(g, 252) * np.tanh(-5.0 * _chg(roic, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# build-vs-return divergence using invcap (capital-cycle core, 504d)
def f40cc_f40_capital_cycle_signal_invbuildret_504d_base_v088_signal(invcap, roic):
    b = _f40_build_minus_return(_f40_invcap_growth(invcap, 504), roic, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# over-invest regime fraction signed by ROIC weakness (time over-building at low return)
def f40cc_f40_capital_cycle_signal_overinvregimelow_base_v089_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    above = (ci > _mean(ci, 1260)).astype(float)
    frac = above.rolling(504, min_periods=252).mean() - 0.5
    pen = 1.0 + 4.0 * _f40_roic_below_hurdle(roic)
    b = frac * pen
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC recovery off 504d low scaled by capex starvation (tightening-payoff setup)
def f40cc_f40_capital_cycle_signal_tightpayoff2_base_v090_signal(roic, capex, ppnenet):
    rec = roic - _rmin(roic, 504)
    rr = _f40_capex_to_ppne(capex, ppnenet)
    starve = (-_z(rr, 504)).clip(lower=0)
    b = rec * (1.0 + starve)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PP&E growth minus ROIC change (capacity build outrunning returns)
def f40cc_f40_capital_cycle_signal_ppnevsroic_252d_base_v091_signal(ppnenet, roic):
    pg = _growth(ppnenet, 252)
    dr = _chg(roic, 252)
    b = pg - dr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital intensity (invcap/assets) interacted with ROIC level (capital efficiency x ret)
def f40cc_f40_capital_cycle_signal_invcapintxret_base_v092_signal(invcap, assets, roic):
    ie = invcap / assets.replace(0, np.nan)
    b = _z(ie, 504) * np.tanh(-5.0 * _f40_roic_sm(roic, 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap-intensity z minus ROIC z 504d (capital-structure build vs return divergence)
def f40cc_f40_capital_cycle_signal_invcapintvsroic_504d_base_v093_signal(invcap, assets, roic):
    r = invcap / assets.replace(0, np.nan)
    b = _z(r, 504) - _z(roic, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex acceleration sign x ROIC deceleration sign (classic capital-cycle warning)
def f40cc_f40_capital_cycle_signal_warningsign_base_v094_signal(capex, roic):
    cacc = _growth(capex, 126) - _growth(capex, 126).shift(126)
    rdec = -(_chg(roic, 126))
    b = np.tanh(8.0 * cacc) * np.tanh(4.0 * rdec)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# extreme-over-build band distance gated by ROIC shortfall (capex past 75th pct + low return)
def f40cc_f40_capital_cycle_signal_overbuildbandlow_base_v095_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    q75 = ci.rolling(252, min_periods=126).quantile(0.75)
    band = (ci - q75) / ci.rolling(252, min_periods=126).std().replace(0, np.nan)
    pen = 1.0 + 5.0 * _f40_roic_below_hurdle(roic)
    b = band * pen
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC stability (inverse CoV) gated by build pace (steady return while deploying capital)
def f40cc_f40_capital_cycle_signal_roicstabxbuild_base_v096_signal(roic, invcap):
    m = _mean(roic, 252)
    s = _std(roic, 252)
    stab = m / (s + 0.01)
    g = np.tanh(8.0 * _f40_invcap_growth(invcap, 252)).clip(lower=0)
    b = stab * (0.5 + g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year asset-growth minus ROIC change 126d (half-cycle build vs return)
def f40cc_f40_capital_cycle_signal_assetgvsret_126d_base_v097_signal(assets, roic):
    b = _f40_build_minus_return(_f40_asset_growth(assets, 126), roic, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year capex-growth minus ROIC change 126d (spend ramp vs return shift)
def f40cc_f40_capital_cycle_signal_capexgvsret_126d_base_v098_signal(capex, roic):
    cg = _growth(capex, 126)
    dr = _chg(roic, 126)
    b = cg - dr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# joint cycle extremity: |z capex intensity| times |z ROIC| (both legs stretched)
def f40cc_f40_capital_cycle_signal_jointextreme_base_v099_signal(capex, assets, roic):
    zci = _z(_f40_capex_intensity(capex, assets), 504)
    zr = _z(roic, 504)
    b = zci.abs() * zr.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate per ROIC (spend per unit of return generated)
def f40cc_f40_capital_cycle_signal_reinvperroic_base_v100_signal(capex, ppnenet, roic):
    rr = _f40_capex_to_ppne(capex, ppnenet)
    r = _f40_roic_sm(roic, 63)
    b = rr / r.where(r.abs() > 0.01)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap-growth minus PP&E-growth spread, ROIC-trend signed (financial-vs-physical build vs ret)
def f40cc_f40_capital_cycle_signal_invvsppnexret_252d_base_v101_signal(invcap, ppnenet, roic):
    ig = _f40_invcap_growth(invcap, 252)
    pg = _growth(ppnenet, 252)
    b = (ig - pg) + 0.5 * np.tanh(5.0 * _chg(roic, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex mean-reversion deviation x ROIC shortfall (over-spend vs own trend at low return)
def f40cc_f40_capital_cycle_signal_capexrevxlow_base_v102_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    dev = ci - ci.ewm(span=252, min_periods=126).mean()
    pen = np.tanh(8.0 * _f40_roic_below_hurdle(roic))
    b = _z(dev, 504) * (0.3 + pen)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# misallocation: asset-growth z times tanh of ROIC-below-mid-cycle (low ret AND high build)
def f40cc_f40_capital_cycle_signal_misalloc2_base_v103_signal(assets, roic):
    zag = _z(_f40_asset_growth(assets, 252), 504)
    lowret = (_mean(roic, 1260) - roic).clip(lower=-0.05)
    b = zag * np.tanh(6.0 * lowret)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-cut depth interacted with ROIC level (spend slashed while returns hold = good)
def f40cc_f40_capital_cycle_signal_capexcutxret_504d_base_v104_signal(capex, roic):
    cut = capex / _rmax(capex, 504).replace(0, np.nan) - 1.0
    b = (-cut) * np.tanh(5.0 * _f40_roic_sm(roic, 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-cut depth interacted with rising ROIC (capitulation-then-payoff)
def f40cc_f40_capital_cycle_signal_cutthenpay_base_v105_signal(capex, roic):
    cut = (capex / _rmax(capex, 504).replace(0, np.nan) - 1.0)
    dr = _chg(roic, 126)
    b = (-cut) * np.tanh(5.0 * dr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# build co-movement (asset-g x invcap-g deviations) signed by ROIC weakness
def f40cc_f40_capital_cycle_signal_buildcomovelow_base_v106_signal(assets, invcap, roic):
    ag = _f40_asset_growth(assets, 63)
    ig = _f40_invcap_growth(invcap, 63)
    comove = (ag - _mean(ag, 252)) * (ig - _mean(ig, 252))
    pen = 1.0 + 4.0 * _f40_roic_below_hurdle(roic)
    b = comove * pen
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC EMA crossover gated by build pace (return-momentum regime while committing capital)
def f40cc_f40_capital_cycle_signal_roiccrossxbuild_base_v107_signal(roic, invcap):
    fast = roic.ewm(span=63, min_periods=21).mean()
    slow = roic.ewm(span=252, min_periods=126).mean()
    g = np.tanh(8.0 * _f40_invcap_growth(invcap, 252))
    b = (fast - slow) * (1.0 + g.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-intensity EMA crossover minus ROIC EMA crossover (build vs return momentum)
def f40cc_f40_capital_cycle_signal_capexvsroiccross_base_v108_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    cfast = ci.ewm(span=63, min_periods=21).mean()
    cslow = ci.ewm(span=252, min_periods=126).mean()
    cmom = (cfast - cslow) / cslow.replace(0, np.nan)
    rmom = roic.ewm(span=63, min_periods=21).mean() - roic.ewm(span=252, min_periods=126).mean()
    b = cmom - np.tanh(5.0 * rmom)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-cycle over-invest regime distance times negative ROIC z (1260d build-trap)
def f40cc_f40_capital_cycle_signal_capexregxret_1260d_base_v109_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    b = np.tanh(_z(ci, 1260)) * (-np.tanh(_z(roic, 1260)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital amplitude (boom-bust swing) gated by ROIC weakness
def f40cc_f40_capital_cycle_signal_invcapampxlow_504d_base_v110_signal(invcap, roic):
    hi = _rmax(invcap, 504)
    lo = _rmin(invcap, 504)
    amp = (hi - lo) / _mean(invcap, 504).replace(0, np.nan)
    pen = 1.0 + 4.0 * _f40_roic_below_hurdle(roic)
    b = amp * pen
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC amplitude (return swing) relative to invcap amplitude (return vs capital volatility)
def f40cc_f40_capital_cycle_signal_roicvsinvcapamp_504d_base_v111_signal(roic, invcap):
    ramp = (_rmax(roic, 504) - _rmin(roic, 504)) / (_mean(roic, 504).abs() + 0.02)
    iamp = (_rmax(invcap, 504) - _rmin(invcap, 504)) / _mean(invcap, 504).replace(0, np.nan)
    b = ramp / (iamp + 0.05)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-intensity rank minus ROIC rank 252d (short-window build-rich vs return-rich)
def f40cc_f40_capital_cycle_signal_buildretrankspr_base_v112_signal(capex, assets, roic):
    cr = _rank(_f40_capex_intensity(capex, assets), 252)
    rr = _rank(roic, 252)
    b = cr - rr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-growth minus PP&E-growth, ROIC-trend signed (gross vs net build vs return)
def f40cc_f40_capital_cycle_signal_capexvsppnegxret_base_v113_signal(capex, ppnenet, roic):
    cg = _growth(capex, 252)
    pg = _growth(ppnenet, 252)
    b = (cg - pg) - 0.5 * np.tanh(5.0 * _chg(roic, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC slope-sign persistence gated by build pace (consistent return trend while building)
def f40cc_f40_capital_cycle_signal_roicpersistxbuild_base_v114_signal(roic, invcap):
    sl = _chg(roic, 63)
    pos = (sl > 0).astype(float).rolling(252, min_periods=126).mean() - 0.5
    g = np.tanh(8.0 * _f40_invcap_growth(invcap, 252))
    b = pos * (1.0 + g.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex regime instability gated by ROIC weakness (chaotic build at low return)
def f40cc_f40_capital_cycle_signal_capexregswitchlow_base_v115_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    med = ci.rolling(252, min_periods=126).median()
    above = (ci > med).astype(float)
    switch = (above != above.shift(1)).astype(float)
    cnt = switch.rolling(252, min_periods=126).sum()
    pen = 1.0 + 3.0 * _f40_roic_below_hurdle(roic)
    b = cnt * pen
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap-growth acceleration signed by ROIC trend (build momentum into rising/falling return)
def f40cc_f40_capital_cycle_signal_invcapaccelxret_base_v116_signal(invcap, roic):
    g = _f40_invcap_growth(invcap, 252)
    accel = g - g.shift(252)
    b = accel * np.tanh(-5.0 * _chg(roic, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-intensity convexity (upper/lower bias) gated by ROIC shortfall
def f40cc_f40_capital_cycle_signal_capexconvexlow_504d_base_v117_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    hi = _rmax(ci, 504)
    lo = _rmin(ci, 504)
    pos = (ci - lo) / (hi - lo).replace(0, np.nan)
    conv = np.sign(pos - 0.5) * (pos - 0.5) ** 2 * 4.0
    pen = 1.0 + 4.0 * _f40_roic_below_hurdle(roic)
    b = conv * pen
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC gap from median per unit of capex intensity (return gap per build)
def f40cc_f40_capital_cycle_signal_roicgapperbuild_base_v118_signal(roic, capex, assets):
    gap = roic - roic.rolling(252, min_periods=126).median()
    ci = _f40_capex_intensity(capex, assets)
    b = gap / (ci + 0.005)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-cycle full-loop: long capex z times negative long ROIC z (over-build trap)
def f40cc_f40_capital_cycle_signal_overbuildtrap_1260d_base_v119_signal(capex, assets, roic):
    zci = _z(_f40_capex_intensity(capex, assets), 1260)
    zr = _z(roic, 1260)
    b = (zci * (-zr)).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-feed efficiency change interacted with ROIC level (capital-feed shift x return)
def f40cc_f40_capital_cycle_signal_capexfeedxret_base_v120_signal(capex, invcap, roic):
    dinv = (invcap - invcap.shift(252)).clip(lower=0)
    feed = capex / (dinv + 0.05 * invcap)
    chg = _z(feed, 252) - _z(feed, 252).shift(126)
    b = chg * np.tanh(-5.0 * _f40_roic_sm(roic, 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-rate change minus ROIC change 252d (plant-replacement pace vs return shift)
def f40cc_f40_capital_cycle_signal_reinvchgvsret_252d_base_v121_signal(capex, ppnenet, roic):
    rr = _f40_capex_to_ppne(capex, ppnenet)
    b = (rr - rr.shift(252)) - (roic - roic.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC rebound off 504d trough scaled by capex starvation (return-cycle rebound + under-build)
def f40cc_f40_capital_cycle_signal_roicreboundstarve_504d_base_v122_signal(roic, capex, assets):
    lo = _rmin(roic, 504)
    hi = _rmax(roic, 504)
    rebound = (roic - lo) / (hi - lo).replace(0, np.nan)
    chg = rebound - rebound.shift(126)
    starve = (-_z(_f40_capex_intensity(capex, assets), 504)).clip(lower=0)
    b = chg * (0.5 + starve)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-build rank minus ROIC rank 504d (build lead vs return lead)
def f40cc_f40_capital_cycle_signal_buildleadspr_base_v123_signal(capex, roic):
    cr = _rank(capex, 504)
    rr = _rank(roic, 504)
    b = cr - rr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC mean over capex-intensity mean (return-per-build efficiency level)
def f40cc_f40_capital_cycle_signal_retperbuild_lvl_base_v124_signal(roic, capex, assets):
    r = _mean(roic, 252)
    ci = _mean(_f40_capex_intensity(capex, assets), 252)
    b = r / (ci + 0.005)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-intensity skewness gated by ROIC weakness (boom-spike asymmetry at low return)
def f40cc_f40_capital_cycle_signal_capexskewlow_252d_base_v125_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    m = _mean(ci, 252)
    s = _std(ci, 252)
    skew = ((ci - m) ** 3).rolling(252, min_periods=126).mean() / (s ** 3 + 1e-9)
    pen = 1.0 + 3.0 * _f40_roic_below_hurdle(roic)
    b = skew * pen
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-growth distance from long trend minus ROIC distance from trend (relative divergence)
def f40cc_f40_capital_cycle_signal_buildvsrettrenddev_base_v126_signal(assets, roic):
    ag = _f40_asset_growth(assets, 252)
    adev = ag - _mean(ag, 1260)
    rdev = roic - _mean(roic, 1260)
    b = adev - rdev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap z minus PP&E z, gated by ROIC weakness (capital-mix divergence at low return)
def f40cc_f40_capital_cycle_signal_capmixdivlow_base_v127_signal(invcap, ppnenet, roic):
    div = _z(invcap, 504) - _z(ppnenet, 504)
    pen = 1.0 + 4.0 * _f40_roic_below_hurdle(roic)
    b = div * pen
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-intensity peak-staleness minus ROIC trough-staleness (build-anchor vs return-anchor age)
def f40cc_f40_capital_cycle_signal_buildvsretage_504d_base_v128_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    def _peak(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    def _trough(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    cage = ci.rolling(504, min_periods=252).apply(_peak, raw=True)
    rage = roic.rolling(504, min_periods=252).apply(_trough, raw=True)
    b = cage - rage
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC trough-staleness scaled by build pace (recovery age while still deploying capital)
def f40cc_f40_capital_cycle_signal_roictroughagebuild_504d_base_v129_signal(roic, invcap):
    def _trough(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    age = roic.rolling(504, min_periods=252).apply(_trough, raw=True)
    g = np.tanh(8.0 * _f40_invcap_growth(invcap, 252))
    b = age * (1.0 + g.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# build-vs-return divergence (invcap) year-over-year change (acceleration of misallocation)
def f40cc_f40_capital_cycle_signal_invbuildretyoy_base_v130_signal(invcap, roic):
    d = _f40_build_minus_return(_f40_invcap_growth(invcap, 252), roic, 252)
    b = d - d.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bounded over-build-low-return: tanh(z capex) minus tanh(z ROIC) (squashed divergence)
def f40cc_f40_capital_cycle_signal_buildretbounded_base_v131_signal(capex, assets, roic):
    zci = np.tanh(_z(_f40_capex_intensity(capex, assets), 504))
    zr = np.tanh(_z(roic, 504))
    b = zci - zr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PP&E-intensity (ppne/assets) interacted with ROIC level (hard-asset heaviness x return)
def f40cc_f40_capital_cycle_signal_ppneintxret_base_v132_signal(ppnenet, assets, roic):
    pi = ppnenet / assets.replace(0, np.nan)
    b = _z(pi, 504) * np.tanh(-5.0 * _f40_roic_sm(roic, 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PP&E-intensity trend minus ROIC change (capacity-heaviness drift vs return shift)
def f40cc_f40_capital_cycle_signal_ppneinttrendvsret_base_v133_signal(ppnenet, assets, roic):
    pi = ppnenet / assets.replace(0, np.nan)
    b = (pi - pi.shift(252)) - 0.5 * (roic - roic.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-intensity CoV (spend predictability) gated by ROIC weakness
def f40cc_f40_capital_cycle_signal_capexcvlow_504d_base_v134_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    cv = _std(ci, 504) / _mean(ci, 504).replace(0, np.nan)
    pen = 1.0 + 4.0 * _f40_roic_below_hurdle(roic)
    b = cv * pen
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC improvement per capex cut (returns rising as spend falls — supply tightening)
def f40cc_f40_capital_cycle_signal_returnspercut_base_v135_signal(roic, capex):
    dr = _chg(roic, 252)
    cg = -_growth(capex, 252)
    b = dr * np.tanh(3.0 * cg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap-growth EMA times negative ROIC trend (smoothed deployment into weak returns)
def f40cc_f40_capital_cycle_signal_invgemaxret_base_v136_signal(invcap, roic):
    g = _f40_invcap_growth(invcap, 63).ewm(span=126, min_periods=63).mean()
    b = _z(g, 252) * np.tanh(-5.0 * _chg(roic, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-intensity z minus invcap-intensity z, gated by ROIC weakness (gross-spend vs cap-eff)
def f40cc_f40_capital_cycle_signal_spendvscapefflow_base_v137_signal(capex, assets, invcap, roic):
    ci = _f40_capex_intensity(capex, assets)
    ie = invcap / assets.replace(0, np.nan)
    spread = _z(ci, 252) - _z(ie, 252)
    pen = 1.0 + 4.0 * _f40_roic_below_hurdle(roic)
    b = spread * pen
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon capex-intensity dispersion gated by ROIC weakness (regime disagreement at low ret)
def f40cc_f40_capital_cycle_signal_capexmhdisplow_base_v138_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    disp = pd.concat([_mean(ci, 21), _mean(ci, 126), _mean(ci, 504)], axis=1).std(axis=1) / _mean(ci, 126).replace(0, np.nan)
    pen = 1.0 + 4.0 * _f40_roic_below_hurdle(roic)
    b = disp * pen
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC level gated by PP&E-build regime (returns earned while expanding capacity)
def f40cc_f40_capital_cycle_signal_roicvsppne_base_v139_signal(roic, ppnenet):
    pg = _growth(ppnenet, 252)
    building = np.tanh(8.0 * pg)
    b = _f40_roic_sm(roic, 63) * building
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-build thermometer (deviation from 1260d median) signed by ROIC weakness
def f40cc_f40_capital_cycle_signal_capexthermoxlow_base_v140_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    med = ci.rolling(1260, min_periods=504).median()
    thermo = np.tanh((ci - med) / (_std(ci, 504) + 1e-9))
    pen = np.tanh(8.0 * _f40_roic_below_hurdle(roic))
    b = thermo * (0.3 + pen)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# under-investment count (capex below 25th pct) weighted by ROIC trend (starve-and-recover tally)
def f40cc_f40_capital_cycle_signal_starvecountxret_base_v141_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    q25 = ci.rolling(252, min_periods=126).quantile(0.25)
    cnt = (ci < q25).astype(float).rolling(504, min_periods=252).sum()
    b = cnt * np.tanh(5.0 * _chg(roic, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# build quality: rank capex intensity minus rank ROIC drawdown depth (over-build vs return loss)
def f40cc_f40_capital_cycle_signal_buildquality_base_v142_signal(capex, assets, roic):
    cir = _rank(_f40_capex_intensity(capex, assets), 252)
    rdd = (roic - _rmax(roic, 504))
    b = cir - _rank(rdd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-growth z times ROIC rank (build-and-return co-extremity)
def f40cc_f40_capital_cycle_signal_buildretprod_base_v143_signal(assets, roic):
    ag = _z(_f40_asset_growth(assets, 252), 504)
    rr = _rank(roic, 504) * 2.0
    b = ag * rr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap range-position minus ROIC range-position 1260d (capital phase vs return phase)
def f40cc_f40_capital_cycle_signal_capvsretphase_base_v144_signal(invcap, roic):
    ipos = (invcap - _rmin(invcap, 1260)) / (_rmax(invcap, 1260) - _rmin(invcap, 1260)).replace(0, np.nan)
    rpos = (roic - _rmin(roic, 1260)) / (_rmax(roic, 1260) - _rmin(roic, 1260)).replace(0, np.nan)
    b = ipos - rpos
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex surge (21d vs 252d) interacted with ROIC deceleration (spend spike into weak return)
def f40cc_f40_capital_cycle_signal_capexsurgexret_base_v145_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    surge = _z(_mean(ci, 21) / _mean(ci, 252).replace(0, np.nan) - 1.0, 252)
    b = surge * np.tanh(-5.0 * _chg(roic, 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC EMA slope gated by build pace (return momentum while deploying capital)
def f40cc_f40_capital_cycle_signal_roicemaslopebuild_base_v146_signal(roic, invcap):
    e = roic.ewm(span=126, min_periods=63).mean()
    slope = e - e.shift(63)
    g = np.tanh(8.0 * _f40_invcap_growth(invcap, 252))
    b = slope * (1.0 + g.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative excess capex z signed by ROIC shortfall (sustained over-spend cost at low return)
def f40cc_f40_capital_cycle_signal_excesscapexxlow_base_v147_signal(capex, assets, roic):
    zci = _z(_f40_capex_intensity(capex, assets), 504).clip(lower=0)
    csum = zci.rolling(252, min_periods=126).sum()
    pen = 1.0 + 4.0 * _f40_roic_below_hurdle(roic)
    b = csum * pen
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-cycle reversion: -z(invcap growth) + z(ROIC) (starve-and-earn regime)
def f40cc_f40_capital_cycle_signal_starveearn_base_v148_signal(invcap, roic):
    b = -_z(_f40_invcap_growth(invcap, 252), 504) + _z(roic, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-rate range-position minus ROIC range-position 252d (build phase vs return phase)
def f40cc_f40_capital_cycle_signal_capexphasevsret_252d_base_v149_signal(capex, ppnenet, roic):
    rr = _f40_capex_to_ppne(capex, ppnenet)
    cpos = (rr - _rmin(rr, 252)) / (_rmax(rr, 252) - _rmin(rr, 252)).replace(0, np.nan)
    rpos = (roic - _rmin(roic, 252)) / (_rmax(roic, 252) - _rmin(roic, 252)).replace(0, np.nan)
    b = (cpos - rpos).ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# full capital-cycle score: blended over-build (capex z + invcap-g z) minus return (ROIC z)
def f40cc_f40_capital_cycle_signal_cyclescore_base_v150_signal(capex, assets, invcap, roic):
    build = 0.5 * _z(_f40_capex_intensity(capex, assets), 504) + 0.5 * _z(_f40_invcap_growth(invcap, 252), 504)
    b = build - _z(roic, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f40cc_f40_capital_cycle_signal_margroicsm_504d_base_v076_signal,
    f40cc_f40_capital_cycle_signal_roicddxbuild_base_v077_signal,
    f40cc_f40_capital_cycle_signal_capexaccelxret_base_v078_signal,
    f40cc_f40_capital_cycle_signal_buildretz2_504d_base_v079_signal,
    f40cc_f40_capital_cycle_signal_reinvstreaklow_base_v080_signal,
    f40cc_f40_capital_cycle_signal_invgvsroicrank_504d_base_v081_signal,
    f40cc_f40_capital_cycle_signal_roictroughstarve_1260d_base_v082_signal,
    f40cc_f40_capital_cycle_signal_capexlocxlow_base_v083_signal,
    f40cc_f40_capital_cycle_signal_cumoverinvlow_1260d_base_v084_signal,
    f40cc_f40_capital_cycle_signal_roicpergrowth_base_v085_signal,
    f40cc_f40_capital_cycle_signal_volratio_base_v086_signal,
    f40cc_f40_capital_cycle_signal_buildemaxret_base_v087_signal,
    f40cc_f40_capital_cycle_signal_invbuildret_504d_base_v088_signal,
    f40cc_f40_capital_cycle_signal_overinvregimelow_base_v089_signal,
    f40cc_f40_capital_cycle_signal_tightpayoff2_base_v090_signal,
    f40cc_f40_capital_cycle_signal_ppnevsroic_252d_base_v091_signal,
    f40cc_f40_capital_cycle_signal_invcapintxret_base_v092_signal,
    f40cc_f40_capital_cycle_signal_invcapintvsroic_504d_base_v093_signal,
    f40cc_f40_capital_cycle_signal_warningsign_base_v094_signal,
    f40cc_f40_capital_cycle_signal_overbuildbandlow_base_v095_signal,
    f40cc_f40_capital_cycle_signal_roicstabxbuild_base_v096_signal,
    f40cc_f40_capital_cycle_signal_assetgvsret_126d_base_v097_signal,
    f40cc_f40_capital_cycle_signal_capexgvsret_126d_base_v098_signal,
    f40cc_f40_capital_cycle_signal_jointextreme_base_v099_signal,
    f40cc_f40_capital_cycle_signal_reinvperroic_base_v100_signal,
    f40cc_f40_capital_cycle_signal_invvsppnexret_252d_base_v101_signal,
    f40cc_f40_capital_cycle_signal_capexrevxlow_base_v102_signal,
    f40cc_f40_capital_cycle_signal_misalloc2_base_v103_signal,
    f40cc_f40_capital_cycle_signal_capexcutxret_504d_base_v104_signal,
    f40cc_f40_capital_cycle_signal_cutthenpay_base_v105_signal,
    f40cc_f40_capital_cycle_signal_buildcomovelow_base_v106_signal,
    f40cc_f40_capital_cycle_signal_roiccrossxbuild_base_v107_signal,
    f40cc_f40_capital_cycle_signal_capexvsroiccross_base_v108_signal,
    f40cc_f40_capital_cycle_signal_capexregxret_1260d_base_v109_signal,
    f40cc_f40_capital_cycle_signal_invcapampxlow_504d_base_v110_signal,
    f40cc_f40_capital_cycle_signal_roicvsinvcapamp_504d_base_v111_signal,
    f40cc_f40_capital_cycle_signal_buildretrankspr_base_v112_signal,
    f40cc_f40_capital_cycle_signal_capexvsppnegxret_base_v113_signal,
    f40cc_f40_capital_cycle_signal_roicpersistxbuild_base_v114_signal,
    f40cc_f40_capital_cycle_signal_capexregswitchlow_base_v115_signal,
    f40cc_f40_capital_cycle_signal_invcapaccelxret_base_v116_signal,
    f40cc_f40_capital_cycle_signal_capexconvexlow_504d_base_v117_signal,
    f40cc_f40_capital_cycle_signal_roicgapperbuild_base_v118_signal,
    f40cc_f40_capital_cycle_signal_overbuildtrap_1260d_base_v119_signal,
    f40cc_f40_capital_cycle_signal_capexfeedxret_base_v120_signal,
    f40cc_f40_capital_cycle_signal_reinvchgvsret_252d_base_v121_signal,
    f40cc_f40_capital_cycle_signal_roicreboundstarve_504d_base_v122_signal,
    f40cc_f40_capital_cycle_signal_buildleadspr_base_v123_signal,
    f40cc_f40_capital_cycle_signal_retperbuild_lvl_base_v124_signal,
    f40cc_f40_capital_cycle_signal_capexskewlow_252d_base_v125_signal,
    f40cc_f40_capital_cycle_signal_buildvsrettrenddev_base_v126_signal,
    f40cc_f40_capital_cycle_signal_capmixdivlow_base_v127_signal,
    f40cc_f40_capital_cycle_signal_buildvsretage_504d_base_v128_signal,
    f40cc_f40_capital_cycle_signal_roictroughagebuild_504d_base_v129_signal,
    f40cc_f40_capital_cycle_signal_invbuildretyoy_base_v130_signal,
    f40cc_f40_capital_cycle_signal_buildretbounded_base_v131_signal,
    f40cc_f40_capital_cycle_signal_ppneintxret_base_v132_signal,
    f40cc_f40_capital_cycle_signal_ppneinttrendvsret_base_v133_signal,
    f40cc_f40_capital_cycle_signal_capexcvlow_504d_base_v134_signal,
    f40cc_f40_capital_cycle_signal_returnspercut_base_v135_signal,
    f40cc_f40_capital_cycle_signal_invgemaxret_base_v136_signal,
    f40cc_f40_capital_cycle_signal_spendvscapefflow_base_v137_signal,
    f40cc_f40_capital_cycle_signal_capexmhdisplow_base_v138_signal,
    f40cc_f40_capital_cycle_signal_roicvsppne_base_v139_signal,
    f40cc_f40_capital_cycle_signal_capexthermoxlow_base_v140_signal,
    f40cc_f40_capital_cycle_signal_starvecountxret_base_v141_signal,
    f40cc_f40_capital_cycle_signal_buildquality_base_v142_signal,
    f40cc_f40_capital_cycle_signal_buildretprod_base_v143_signal,
    f40cc_f40_capital_cycle_signal_capvsretphase_base_v144_signal,
    f40cc_f40_capital_cycle_signal_capexsurgexret_base_v145_signal,
    f40cc_f40_capital_cycle_signal_roicemaslopebuild_base_v146_signal,
    f40cc_f40_capital_cycle_signal_excesscapexxlow_base_v147_signal,
    f40cc_f40_capital_cycle_signal_starveearn_base_v148_signal,
    f40cc_f40_capital_cycle_signal_capexphasevsret_252d_base_v149_signal,
    f40cc_f40_capital_cycle_signal_cyclescore_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F40_CAPITAL_CYCLE_SIGNAL_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    capex = _fund(4001, base=9e7, drift=0.010, vol=0.22).rename("capex")
    assets = _fund(4002, base=1.5e9, drift=0.015, vol=0.06).rename("assets")
    ppnenet = _fund(4003, base=7e8, drift=0.018, vol=0.11).rename("ppnenet")
    invcap = _fund(4004, base=1.0e9, drift=0.012, vol=0.08).rename("invcap")
    roic = _fund(4005, base=0.12, drift=-0.004, vol=0.30, allow_neg=True).rename("roic")

    cols = {"capex": capex, "assets": assets, "ppnenet": ppnenet,
            "invcap": invcap, "roic": roic}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in ("capex", "assets", "ppnenet", "roic", "invcap")
                   for c in meta["inputs"]), name
        # TIGHTENED DOMAIN: every feature must couple a build term WITH roic
        assert "roic" in meta["inputs"], "%s missing return leg" % name
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

    print("OK f40_capital_cycle_signal_base_076_150_claude: %d features pass" % n_features)
