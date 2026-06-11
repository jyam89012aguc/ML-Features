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
# TIGHTENED DOMAIN: capital-cycle DIVERGENCE only. Every feature couples a
# GROWTH/INVESTMENT term with a RETURN-ON-CAPITAL term. NO standalone asset-growth
# or capex-intensity LEVELS (those belong to f30/f28). The build leg is always
# paired with ROIC / a ROIC transform so the feature measures over-investment-at-
# low-return vs capital-starvation-at-improving-return.
def _f40_capex_intensity(capex, assets):
    return capex / assets.replace(0, np.nan)


def _f40_capex_to_ppne(capex, ppnenet):
    return capex / ppnenet.replace(0, np.nan)


def _f40_asset_growth(assets, w):
    return np.log(assets.replace(0, np.nan) / assets.shift(w).replace(0, np.nan))


def _f40_invcap_growth(invcap, w):
    return np.log(invcap.replace(0, np.nan) / invcap.shift(w).replace(0, np.nan))


def _f40_roic_sm(roic, w):
    # smoothed return-on-capital level (the "return" leg)
    return roic.rolling(w, min_periods=max(1, w // 2)).mean()


def _f40_roic_below_hurdle(roic, w=504):
    # how far smoothed ROIC sits below its own mid-cycle hurdle (rolling median);
    # positive => returns below the level required to justify fresh capital.
    sm = roic.rolling(63, min_periods=21).mean()
    hurdle = roic.rolling(w, min_periods=max(1, w // 2)).median()
    return (hurdle - sm).clip(lower=0)


def _f40_marginal_roic(invcap, roic, w):
    # ΔROIC per unit of invested-capital growth: return on the NEW capital
    dr = roic - roic.shift(w)
    dg = np.log(invcap.replace(0, np.nan) / invcap.shift(w).replace(0, np.nan))
    return dr / dg.replace(0, np.nan)


def _f40_build_minus_return(growth_term, roic, w):
    # capital-cycle divergence: capital grows while returns fall
    dr = roic - roic.shift(w)
    return growth_term - dr


# ============================================================
# CAPITAL-CYCLE THESIS: heavy asset/capex BUILD relative to RETURNS-ON-CAPITAL
# predicts poor future returns (over-investment at low/falling ROIC = bad);
# capital STARVATION at improving ROIC predicts good returns. Every feature below
# COUPLES a build/investment term WITH the ROIC/return dimension — there are NO
# standalone build levels (those are f30_reserve_asset_base / f28_capex_intensity).
# Inputs are a subset of {capex, assets, ppnenet, roic, invcap}.

# over-build-at-low-return: capex intensity x distance ROIC sits below hurdle
def f40cc_f40_capital_cycle_signal_overinvhurdle_base_v001_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    pen = _f40_roic_below_hurdle(roic)
    b = _z(ci, 252) * (1.0 + 8.0 * pen)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-intensity z minus ROIC z (normalised build-vs-return divergence, 252d)
def f40cc_f40_capital_cycle_signal_buildretz_252d_base_v002_signal(capex, assets, roic):
    b = _z(_f40_capex_intensity(capex, assets), 252) - _z(roic, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate (capex/PP&E) minus ROIC level (spending faster than it earns)
def f40cc_f40_capital_cycle_signal_reinvminroic_base_v003_signal(capex, ppnenet, roic):
    rr = _f40_capex_to_ppne(capex, ppnenet)
    b = rr - _f40_roic_sm(roic, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-rate z minus ROIC z over 504d (cycle-extreme build vs return)
def f40cc_f40_capital_cycle_signal_reinvretz_504d_base_v004_signal(capex, ppnenet, roic):
    rr = _f40_capex_to_ppne(capex, ppnenet)
    b = _z(rr, 504) - _z(roic, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-to-invested-capital scaled by ROIC shortfall below hurdle (mis-feed of capital)
def f40cc_f40_capital_cycle_signal_capexfeedhurdle_base_v005_signal(capex, invcap, roic):
    feed = capex / invcap.replace(0, np.nan)
    pen = _f40_roic_below_hurdle(roic)
    b = _z(feed, 252) * np.tanh(10.0 * pen)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-growth MINUS ROIC change 252d (build outrunning return — core divergence)
def f40cc_f40_capital_cycle_signal_assetgvsret_252d_base_v006_signal(assets, roic):
    b = _f40_build_minus_return(_f40_asset_growth(assets, 252), roic, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-growth MINUS ROIC change 504d (two-year build vs return divergence)
def f40cc_f40_capital_cycle_signal_assetgvsret_504d_base_v007_signal(assets, roic):
    b = _f40_build_minus_return(_f40_asset_growth(assets, 504), roic, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital growth minus ROIC level 252d (build above the return it earns)
def f40cc_f40_capital_cycle_signal_invcapgvsroic_252d_base_v008_signal(invcap, roic):
    g = _f40_invcap_growth(invcap, 252)
    b = g - _f40_roic_sm(roic, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital growth z minus ROIC z 504d (normalised capital-cycle divergence)
def f40cc_f40_capital_cycle_signal_invcapgvsroic_504d_base_v009_signal(invcap, roic):
    g = _f40_invcap_growth(invcap, 504)
    b = _z(g, 504) - _z(roic, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC level gated by whether capital is expanding (returns earned while building)
def f40cc_f40_capital_cycle_signal_roicwhilebuild_base_v010_signal(roic, invcap):
    g = _f40_invcap_growth(invcap, 252)
    building = np.tanh(8.0 * g)
    b = _f40_roic_sm(roic, 21) * building
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC z penalised by capex-intensity z (low return + high build => very negative)
def f40cc_f40_capital_cycle_signal_roicpenbuild_504d_base_v011_signal(roic, capex, assets):
    zr = _z(roic, 504)
    zci = _z(_f40_capex_intensity(capex, assets), 504)
    b = zr - 0.6 * zci.clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC change minus capex-growth (returns improving as spend rises? mismatch)
def f40cc_f40_capital_cycle_signal_roicvscapexg_252d_base_v012_signal(roic, capex):
    dr = _chg(roic, 252)
    cg = _growth(capex, 252)
    b = dr - cg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# build-vs-return divergence (asset growth - ROIC chg) ranked vs 504d (extremity)
def f40cc_f40_capital_cycle_signal_buildretrank_504d_base_v013_signal(assets, roic):
    d = _f40_build_minus_return(_f40_asset_growth(assets, 252), roic, 252)
    b = _rank(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# build-vs-return divergence smoothed then z-scored (persistent misallocation)
def f40cc_f40_capital_cycle_signal_buildretzsm_504d_base_v014_signal(assets, roic):
    d = _f40_build_minus_return(_f40_asset_growth(assets, 252), roic, 252)
    b = _z(d.ewm(span=63, min_periods=21).mean(), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-growth interacted with ROIC-deceleration (accelerating spend, falling return)
def f40cc_f40_capital_cycle_signal_capexgxroicdec_252d_base_v015_signal(capex, roic):
    cg = _growth(capex, 252)
    rdec = -_chg(roic, 252)
    b = np.tanh(4.0 * cg) * np.tanh(4.0 * rdec)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-growth 504d minus ROIC change 504d (long build vs long return shift)
def f40cc_f40_capital_cycle_signal_capexgvsret_504d_base_v016_signal(capex, roic):
    cg = _growth(capex, 504)
    dr = _chg(roic, 504)
    b = cg - dr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-cycle deviation x ROIC shortfall (over-spend exactly when returns weak)
def f40cc_f40_capital_cycle_signal_capexdevxshort_252d_base_v017_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    med = ci.rolling(252, min_periods=126).median()
    dev = ci / med.replace(0, np.nan) - 1.0
    pen = _f40_roic_below_hurdle(roic)
    b = np.sign(dev) * (dev.abs() ** 0.5) * (1.0 + 6.0 * pen)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-cycle capex z times negative long-cycle ROIC z (1260d over-build trap)
def f40cc_f40_capital_cycle_signal_overbuildtrap_1260d_base_v018_signal(capex, assets, roic):
    zci = _z(_f40_capex_intensity(capex, assets), 1260)
    zr = _z(roic, 1260)
    b = zci * (-zr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PP&E growth minus ROIC change 252d (capacity build outrunning returns)
def f40cc_f40_capital_cycle_signal_ppnegvsret_252d_base_v019_signal(ppnenet, roic):
    pg = _growth(ppnenet, 252)
    dr = _chg(roic, 252)
    b = pg - dr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PP&E-growth rank minus ROIC rank 504d (normalised capacity-vs-return divergence)
def f40cc_f40_capital_cycle_signal_ppnegvsret_504d_base_v020_signal(ppnenet, roic):
    pg = _growth(ppnenet, 504)
    b = _rank(pg, 504) - _rank(roic, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# over-investment distance (capex intensity above its mean) gated by low ROIC
def f40cc_f40_capital_cycle_signal_overinvdistlow_252d_base_v021_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    dist = (ci - _mean(ci, 252)) / _mean(ci, 252).replace(0, np.nan)
    low = np.tanh(6.0 * _f40_roic_below_hurdle(roic))
    b = dist * (0.3 + low)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# under-investment payoff: capex starvation z x ROIC level (starve + earn = reward)
def f40cc_f40_capital_cycle_signal_starvepayoff_504d_base_v022_signal(capex, ppnenet, roic):
    rr = _f40_capex_to_ppne(capex, ppnenet)
    starve = -_z(rr, 504)
    b = starve * np.tanh(5.0 * _f40_roic_sm(roic, 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# starvation-and-rising-return: fraction of year capex<median, weighted by ROIC trend
def f40cc_f40_capital_cycle_signal_starverising_252d_base_v023_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    med = ci.rolling(252, min_periods=126).median()
    starved = (ci < med).astype(float).rolling(252, min_periods=126).mean()
    b = starved * np.tanh(5.0 * _chg(roic, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-over-return ratio: invcap growth divided by ROIC level (build per unit of return)
def f40cc_f40_capital_cycle_signal_gminroic_252d_base_v024_signal(invcap, roic):
    g = _f40_invcap_growth(invcap, 252)
    r = _f40_roic_sm(roic, 63)
    b = np.sign(r) * g / (r.abs() + 0.03)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-intensity rank MINUS ROIC rank 504d (build-rich vs return-rich position)
def f40cc_f40_capital_cycle_signal_capexvsroicrank_504d_base_v025_signal(capex, assets, roic):
    cr = _rank(_f40_capex_intensity(capex, assets), 504)
    rr = _rank(roic, 504)
    b = cr - rr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC rank minus invcap-growth rank (return leadership vs build leadership)
def f40cc_f40_capital_cycle_signal_roicvsinvgrank_504d_base_v026_signal(roic, invcap):
    rr = _rank(roic, 504)
    gr = _rank(_f40_invcap_growth(invcap, 252), 504)
    b = rr - gr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-growth minus ROIC-rank: cheap-build / poor-return composite
def f40cc_f40_capital_cycle_signal_agvsroicrank_base_v027_signal(assets, roic):
    ag = _f40_asset_growth(assets, 252)
    rr = _rank(roic, 504)
    b = ag - rr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marginal ROIC 252d: ΔROIC per unit of invested-capital growth (return on new capital)
def f40cc_f40_capital_cycle_signal_margroic_252d_base_v028_signal(invcap, roic):
    b = _f40_marginal_roic(invcap, roic, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# front-loaded build per ROIC: capex/Δassets divided by ROIC (cost of building return)
def f40cc_f40_capital_cycle_signal_buildcostperret_252d_base_v029_signal(capex, assets, roic):
    dassets = (assets - assets.shift(252)).clip(lower=0)
    front = capex / (dassets + 0.05 * assets)
    r = _f40_roic_sm(roic, 63)
    b = front / r.where(r.abs() > 0.01)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-cycle phase angle: atan2(z capex intensity, z ROIC) — where on the cycle clock
def f40cc_f40_capital_cycle_signal_cyclephase_252d_base_v030_signal(capex, assets, roic):
    zci = _z(_f40_capex_intensity(capex, assets), 252)
    zr = _z(roic, 252)
    b = pd.Series(np.arctan2(zci.values, zr.values), index=zci.index) / np.pi
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-intensity short/long acceleration interacted with ROIC trend
def f40cc_f40_capital_cycle_signal_capexaccelxret_base_v031_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    accel = _mean(ci, 63) / _mean(ci, 252).replace(0, np.nan) - 1.0
    b = accel * np.tanh(-5.0 * _chg(roic, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# build lumpiness penalised by low ROIC: invcap-growth dispersion x ROIC shortfall
def f40cc_f40_capital_cycle_signal_lumpybuildlow_252d_base_v032_signal(invcap, roic):
    g = _f40_invcap_growth(invcap, 63)
    disp = _std(g, 252)
    pen = 1.0 + 5.0 * _f40_roic_below_hurdle(roic)
    b = disp * pen
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC volatility relative to build pace (unstable returns while committing capital)
def f40cc_f40_capital_cycle_signal_roicvolperbuild_252d_base_v033_signal(roic, invcap):
    rv = _std(roic, 252)
    g = _f40_invcap_growth(invcap, 252).abs() + 0.02
    b = rv * np.tanh(5.0 * g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# over-investment streak (capex above mean) weighted by ROIC shortfall while building
def f40cc_f40_capital_cycle_signal_overinvstreaklow_base_v034_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    above = (ci > _mean(ci, 252)).astype(float)
    grp = (above != above.shift(1)).cumsum()
    streak = (above.groupby(grp).cumsum() * above) / 252.0
    pen = 1.0 + 4.0 * _f40_roic_below_hurdle(roic)
    b = streak * pen
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-on-incremental-asset: ROIC change divided by asset growth (build payoff)
def f40cc_f40_capital_cycle_signal_buildpayoff_252d_base_v035_signal(assets, roic):
    dr = _chg(roic, 252)
    ag = _f40_asset_growth(assets, 252)
    b = dr / (ag.abs() + 0.02)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment displacement (capex/PP&E vs its EMA) signed by ROIC direction
def f40cc_f40_capital_cycle_signal_reinvdispxret_base_v036_signal(capex, ppnenet, roic):
    rr = _f40_capex_to_ppne(capex, ppnenet)
    disp = rr - rr.ewm(span=126, min_periods=63).mean()
    b = disp * np.tanh(-5.0 * _f40_roic_sm(roic, 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# build-acceleration vs return-acceleration (asset-g accel minus ROIC-chg accel)
def f40cc_f40_capital_cycle_signal_buildaccelvsret_base_v037_signal(assets, roic):
    ag = _f40_asset_growth(assets, 252)
    aaccel = ag - ag.shift(252)
    dr = _chg(roic, 252)
    raccel = dr - dr.shift(252)
    b = aaccel - raccel
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC drawdown from 1260d peak scaled by capex intensity (penalised return trough)
def f40cc_f40_capital_cycle_signal_roicddxbuild_1260d_base_v038_signal(roic, capex, assets):
    rdd = roic - _rmax(roic, 1260)
    ci = _z(_f40_capex_intensity(capex, assets), 504).clip(lower=0)
    b = rdd * (1.0 + ci)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investment-ramp phase change minus ROIC-position change (build leads return?)
def f40cc_f40_capital_cycle_signal_buildvsretphase_1260d_base_v039_signal(capex, roic):
    chi = _rmax(capex, 1260)
    clo = _rmin(capex, 1260)
    cpos = (capex - clo) / (chi - clo).replace(0, np.nan)
    rhi = _rmax(roic, 1260)
    rlo = _rmin(roic, 1260)
    rpos = (roic - rlo) / (rhi - rlo).replace(0, np.nan)
    b = (cpos - cpos.shift(126)) - (rpos - rpos.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-misallocation: z(invcap growth) times negative z(ROIC) (high build x low ret)
def f40cc_f40_capital_cycle_signal_misalloc_252d_base_v040_signal(invcap, roic):
    zg = _z(_f40_invcap_growth(invcap, 252), 252)
    zr = _z(roic, 252)
    b = zg * (-zr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tightening payoff: low capex z + rising ROIC (under-build then returns recover)
def f40cc_f40_capital_cycle_signal_tighteningpay_base_v041_signal(capex, assets, roic):
    zci = _z(_f40_capex_intensity(capex, assets), 504)
    dr = _chg(roic, 252)
    b = (-zci) + dr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/invcap z minus ROIC z 252d (per-capital build extremity vs return extremity)
def f40cc_f40_capital_cycle_signal_capexinvcapvsret_252d_base_v042_signal(capex, invcap, roic):
    r = capex / invcap.replace(0, np.nan)
    b = _z(r, 252) - _z(roic, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC mid-cycle gap scaled by build pace (return-vs-trend while deploying capital)
def f40cc_f40_capital_cycle_signal_roicmidgapxbuild_1260d_base_v043_signal(roic, invcap):
    gap = roic - _mean(roic, 1260)
    g = np.tanh(8.0 * _f40_invcap_growth(invcap, 252))
    b = gap * (1.0 + g.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-base range-position minus ROIC range-position 1260d (capital vs return phase)
def f40cc_f40_capital_cycle_signal_assetvsroicphase_1260d_base_v044_signal(assets, roic):
    apos = (assets - _rmin(assets, 1260)) / (_rmax(assets, 1260) - _rmin(assets, 1260)).replace(0, np.nan)
    rpos = (roic - _rmin(roic, 1260)) / (_rmax(roic, 1260) - _rmin(roic, 1260)).replace(0, np.nan)
    b = apos - rpos
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate minus ROIC, ranked vs 504d (over-spend-vs-earn extremity)
def f40cc_f40_capital_cycle_signal_reinvminroicrank_504d_base_v045_signal(capex, ppnenet, roic):
    rr = _f40_capex_to_ppne(capex, ppnenet)
    d = rr - _f40_roic_sm(roic, 63)
    b = _rank(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed build-vs-return: EMA of capex intensity minus EMA of ROIC (persistent gap)
def f40cc_f40_capital_cycle_signal_buildretema_base_v046_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    b = _z(ci.ewm(span=126, min_periods=63).mean(), 504) - _z(roic.ewm(span=126, min_periods=63).mean(), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap-growth minus asset-growth, signed by ROIC weakness (capital-mix build x low ret)
def f40cc_f40_capital_cycle_signal_invcapmixlow_252d_base_v047_signal(invcap, assets, roic):
    ig = _f40_invcap_growth(invcap, 252)
    ag = _f40_asset_growth(assets, 252)
    pen = 1.0 + 4.0 * _f40_roic_below_hurdle(roic)
    b = (ig - ag) * pen
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex trough-position interacted with ROIC trend (starvation depth x return recovery)
def f40cc_f40_capital_cycle_signal_capextroughxret_504d_base_v048_signal(capex, roic):
    lo = _rmin(capex, 504)
    hi = _rmax(capex, 504)
    pos = (capex - lo) / (hi - lo).replace(0, np.nan) - 0.5
    b = (-pos) * np.tanh(5.0 * _chg(roic, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC-to-build efficiency: ROIC level per unit of capex intensity (return per build)
def f40cc_f40_capital_cycle_signal_roicperbuild_base_v049_signal(roic, capex, assets):
    ci = _f40_capex_intensity(capex, assets)
    b = _f40_roic_sm(roic, 63) / (ci + 0.01)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-growth volatility interacted with ROIC instability (lumpy spend + lumpy return)
def f40cc_f40_capital_cycle_signal_capexgvolxroicvol_504d_base_v050_signal(capex, roic):
    cgv = _std(_growth(capex, 63), 504)
    rv = _std(roic, 504)
    b = cgv * np.tanh(8.0 * rv)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# build-vs-return divergence (invcap g - ROIC chg) ranked 504d (alt build leg)
def f40cc_f40_capital_cycle_signal_invbuildretrank_504d_base_v051_signal(invcap, roic):
    d = _f40_build_minus_return(_f40_invcap_growth(invcap, 252), roic, 252)
    b = _rank(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PP&E-intensity build interacted with ROIC shortfall (hard-asset heaviness x low ret)
def f40cc_f40_capital_cycle_signal_ppneintxlow_base_v052_signal(ppnenet, invcap, roic):
    pi = ppnenet / invcap.replace(0, np.nan)
    g = pi - pi.shift(252)
    pen = 1.0 + 5.0 * _f40_roic_below_hurdle(roic)
    b = g * pen
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PP&E-intensity z minus ROIC z 504d (capacity-heaviness vs return divergence)
def f40cc_f40_capital_cycle_signal_ppneintvsroic_504d_base_v053_signal(ppnenet, invcap, roic):
    r = ppnenet / invcap.replace(0, np.nan)
    b = _z(r, 504) - _z(roic, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC-below-mean streak weighted by build pace (return-trough while still committing)
def f40cc_f40_capital_cycle_signal_roictroughbuild_base_v054_signal(roic, invcap):
    below = (roic < _mean(roic, 252)).astype(float)
    grp = (below != below.shift(1)).cumsum()
    streak = (below.groupby(grp).cumsum() * below) / 252.0
    g = np.tanh(8.0 * _f40_invcap_growth(invcap, 252)).clip(lower=0)
    b = streak * (0.5 + g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-intensity change minus ROIC change over a quarter (near-term build vs return)
def f40cc_f40_capital_cycle_signal_capexchgvsret_63d_base_v055_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    b = (ci - ci.shift(63)) - 0.5 * (roic - roic.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-year build vs return: rank(asset-growth 1260d) minus rank(ROIC) (long-cycle gap)
def f40cc_f40_capital_cycle_signal_assetgvsret_1260d_base_v056_signal(assets, roic):
    ag = _f40_asset_growth(assets, 1260)
    b = _rank(ag, 252) - _rank(roic, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# favourable starvation regime: -(asset growth) blended with z(ROIC) (starve + earn)
def f40cc_f40_capital_cycle_signal_favstarve_base_v057_signal(assets, roic):
    ag = _f40_asset_growth(assets, 504)
    b = (-ag) * 5.0 + _z(roic, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-rate rank minus ROIC rank 504d (build position vs return position)
def f40cc_f40_capital_cycle_signal_reinvvsroicrank_504d_base_v058_signal(capex, ppnenet, roic):
    rr = _rank(_f40_capex_to_ppne(capex, ppnenet), 504)
    rk = _rank(roic, 504)
    b = rr - rk
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# co-trend of capex intensity and ROIC: sign-aligned trend product (do they move together)
def f40cc_f40_capital_cycle_signal_capexroiccotrend_base_v059_signal(roic, capex, assets):
    dr = _chg(roic, 252)
    ci = _f40_capex_intensity(capex, assets)
    dci = ci - ci.shift(252)
    b = np.sign(dr) * np.sign(dci) * (dr.abs() + dci.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-intensity dispersion across horizons gated by ROIC weakness (chaotic low-ret build)
def f40cc_f40_capital_cycle_signal_capexdispxlow_base_v060_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    disp = pd.concat([_mean(ci, 63), _mean(ci, 252), _mean(ci, 504)], axis=1).std(axis=1) / _mean(ci, 252).replace(0, np.nan)
    pen = 1.0 + 4.0 * _f40_roic_below_hurdle(roic)
    b = disp * pen
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital ramp from trough scaled by ROIC level (re-accumulation that earns)
def f40cc_f40_capital_cycle_signal_invramprxret_1260d_base_v061_signal(invcap, roic):
    tr = _rmin(invcap, 1260)
    ramp = invcap / tr.replace(0, np.nan) - 1.0
    b = ramp * np.tanh(5.0 * _f40_roic_sm(roic, 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bounded over-build-low-return: tanh(z capex) times tanh(-z ROIC) (squashed interaction)
def f40cc_f40_capital_cycle_signal_buildretbounded_504d_base_v062_signal(capex, assets, roic):
    zci = np.tanh(_z(_f40_capex_intensity(capex, assets), 504))
    zr = np.tanh(_z(roic, 504))
    b = zci * (-zr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-build acceleration signed by ROIC deceleration (accelerating into weak returns)
def f40cc_f40_capital_cycle_signal_capexaccelxroicdec_base_v063_signal(capex, roic):
    g = _growth(capex, 126)
    accel = (g - g.shift(126)).ewm(span=63, min_periods=21).mean()
    b = accel * np.tanh(-5.0 * _chg(roic, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# over-build penalty: asset-growth z weighted by how far ROIC sits below mid-cycle
def f40cc_f40_capital_cycle_signal_overbuildpen_base_v064_signal(assets, roic):
    zag = _z(_f40_asset_growth(assets, 252), 504)
    shortfall = (_mean(roic, 1260) - roic).clip(lower=0)
    b = zag * (1.0 + 5.0 * shortfall)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity per unit of ROIC (cost of one unit of return)
def f40cc_f40_capital_cycle_signal_capexperroic_base_v065_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    rr = _f40_roic_sm(roic, 63)
    b = ci / rr.where(rr.abs() > 0.005)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-build convexity (short vs long pace) gated by ROIC weakness
def f40cc_f40_capital_cycle_signal_buildconvexlow_base_v066_signal(assets, roic):
    g126 = _f40_asset_growth(assets, 126)
    g504 = _f40_asset_growth(assets, 504) / 4.0
    conv = g126 / (g504.abs() + 0.01) * np.sign(g504)
    pen = 1.0 + 3.0 * _f40_roic_below_hurdle(roic)
    b = conv * pen
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-cycle distance: Euclidean magnitude of (capex-intensity z, -ROIC z) joint extremity
def f40cc_f40_capital_cycle_signal_cycledist_504d_base_v067_signal(capex, assets, roic):
    zci = _z(_f40_capex_intensity(capex, assets), 504)
    zr = _z(roic, 504)
    b = np.sign(zci - zr) * np.sqrt(zci ** 2 + zr ** 2)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC improvement during capital starvation (favourable inflection)
def f40cc_f40_capital_cycle_signal_starveinflect_base_v068_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    starved = (ci < ci.rolling(504, min_periods=252).median()).astype(float)
    dr = _chg(roic, 126)
    b = starved * dr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# steady-build-that-earns: tanh(ROIC) signed by invcap-growth direction
def f40cc_f40_capital_cycle_signal_steadybuildret_base_v069_signal(invcap, roic):
    g = _f40_invcap_growth(invcap, 252)
    r = roic.ewm(span=63, min_periods=21).mean()
    b = np.tanh(r * 4.0) * np.sign(g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-intensity YoY change minus ROIC YoY change (annual build-regime vs return shift)
def f40cc_f40_capital_cycle_signal_capexyoyvsret_base_v070_signal(capex, assets, roic):
    ci = _f40_capex_intensity(capex, assets)
    b = (ci - ci.shift(252)) - 0.5 * (roic - roic.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PP&E-growth minus invcap-growth spread, ROIC-trend signed (physical-vs-capital build vs return)
def f40cc_f40_capital_cycle_signal_ppnevsinvxlow_252d_base_v071_signal(ppnenet, invcap, roic):
    pg = _growth(ppnenet, 252)
    ig = _f40_invcap_growth(invcap, 252)
    b = (pg - ig) - 0.5 * np.tanh(5.0 * _chg(roic, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital intensity (assets/invcap) interacted with ROIC level (leverage of asset base x ret)
def f40cc_f40_capital_cycle_signal_capintxret_base_v072_signal(assets, invcap, roic):
    ci = assets / invcap.replace(0, np.nan)
    b = _z(ci, 504) * np.tanh(-5.0 * _f40_roic_sm(roic, 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# build-vs-return divergence smoothed and z-scored using invcap leg (persistent)
def f40cc_f40_capital_cycle_signal_invbuildretz_252d_base_v073_signal(invcap, roic):
    d = _f40_build_minus_return(_f40_invcap_growth(invcap, 252), roic, 252)
    b = _z(d.ewm(span=63, min_periods=21).mean(), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex amplitude (boom-bust swing) gated by ROIC weakness (volatile spend, weak returns)
def f40cc_f40_capital_cycle_signal_capexampxlow_504d_base_v074_signal(capex, roic):
    hi = _rmax(capex, 504)
    lo = _rmin(capex, 504)
    amp = (hi - lo) / _mean(capex, 504).replace(0, np.nan)
    pen = 1.0 + 4.0 * _f40_roic_below_hurdle(roic)
    b = amp * pen
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-starvation distance scaled by ROIC recovery (full cycle low-to-payoff)
def f40cc_f40_capital_cycle_signal_starve_payoff_base_v075_signal(capex, invcap, roic):
    r = capex / invcap.replace(0, np.nan)
    zr = _z(r, 504)
    droic = roic - _rmin(roic, 504)
    b = (-zr) * (1.0 + droic.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f40cc_f40_capital_cycle_signal_overinvhurdle_base_v001_signal,
    f40cc_f40_capital_cycle_signal_buildretz_252d_base_v002_signal,
    f40cc_f40_capital_cycle_signal_reinvminroic_base_v003_signal,
    f40cc_f40_capital_cycle_signal_reinvretz_504d_base_v004_signal,
    f40cc_f40_capital_cycle_signal_capexfeedhurdle_base_v005_signal,
    f40cc_f40_capital_cycle_signal_assetgvsret_252d_base_v006_signal,
    f40cc_f40_capital_cycle_signal_assetgvsret_504d_base_v007_signal,
    f40cc_f40_capital_cycle_signal_invcapgvsroic_252d_base_v008_signal,
    f40cc_f40_capital_cycle_signal_invcapgvsroic_504d_base_v009_signal,
    f40cc_f40_capital_cycle_signal_roicwhilebuild_base_v010_signal,
    f40cc_f40_capital_cycle_signal_roicpenbuild_504d_base_v011_signal,
    f40cc_f40_capital_cycle_signal_roicvscapexg_252d_base_v012_signal,
    f40cc_f40_capital_cycle_signal_buildretrank_504d_base_v013_signal,
    f40cc_f40_capital_cycle_signal_buildretzsm_504d_base_v014_signal,
    f40cc_f40_capital_cycle_signal_capexgxroicdec_252d_base_v015_signal,
    f40cc_f40_capital_cycle_signal_capexgvsret_504d_base_v016_signal,
    f40cc_f40_capital_cycle_signal_capexdevxshort_252d_base_v017_signal,
    f40cc_f40_capital_cycle_signal_overbuildtrap_1260d_base_v018_signal,
    f40cc_f40_capital_cycle_signal_ppnegvsret_252d_base_v019_signal,
    f40cc_f40_capital_cycle_signal_ppnegvsret_504d_base_v020_signal,
    f40cc_f40_capital_cycle_signal_overinvdistlow_252d_base_v021_signal,
    f40cc_f40_capital_cycle_signal_starvepayoff_504d_base_v022_signal,
    f40cc_f40_capital_cycle_signal_starverising_252d_base_v023_signal,
    f40cc_f40_capital_cycle_signal_gminroic_252d_base_v024_signal,
    f40cc_f40_capital_cycle_signal_capexvsroicrank_504d_base_v025_signal,
    f40cc_f40_capital_cycle_signal_roicvsinvgrank_504d_base_v026_signal,
    f40cc_f40_capital_cycle_signal_agvsroicrank_base_v027_signal,
    f40cc_f40_capital_cycle_signal_margroic_252d_base_v028_signal,
    f40cc_f40_capital_cycle_signal_buildcostperret_252d_base_v029_signal,
    f40cc_f40_capital_cycle_signal_cyclephase_252d_base_v030_signal,
    f40cc_f40_capital_cycle_signal_capexaccelxret_base_v031_signal,
    f40cc_f40_capital_cycle_signal_lumpybuildlow_252d_base_v032_signal,
    f40cc_f40_capital_cycle_signal_roicvolperbuild_252d_base_v033_signal,
    f40cc_f40_capital_cycle_signal_overinvstreaklow_base_v034_signal,
    f40cc_f40_capital_cycle_signal_buildpayoff_252d_base_v035_signal,
    f40cc_f40_capital_cycle_signal_reinvdispxret_base_v036_signal,
    f40cc_f40_capital_cycle_signal_buildaccelvsret_base_v037_signal,
    f40cc_f40_capital_cycle_signal_roicddxbuild_1260d_base_v038_signal,
    f40cc_f40_capital_cycle_signal_buildvsretphase_1260d_base_v039_signal,
    f40cc_f40_capital_cycle_signal_misalloc_252d_base_v040_signal,
    f40cc_f40_capital_cycle_signal_tighteningpay_base_v041_signal,
    f40cc_f40_capital_cycle_signal_capexinvcapvsret_252d_base_v042_signal,
    f40cc_f40_capital_cycle_signal_roicmidgapxbuild_1260d_base_v043_signal,
    f40cc_f40_capital_cycle_signal_assetvsroicphase_1260d_base_v044_signal,
    f40cc_f40_capital_cycle_signal_reinvminroicrank_504d_base_v045_signal,
    f40cc_f40_capital_cycle_signal_buildretema_base_v046_signal,
    f40cc_f40_capital_cycle_signal_invcapmixlow_252d_base_v047_signal,
    f40cc_f40_capital_cycle_signal_capextroughxret_504d_base_v048_signal,
    f40cc_f40_capital_cycle_signal_roicperbuild_base_v049_signal,
    f40cc_f40_capital_cycle_signal_capexgvolxroicvol_504d_base_v050_signal,
    f40cc_f40_capital_cycle_signal_invbuildretrank_504d_base_v051_signal,
    f40cc_f40_capital_cycle_signal_ppneintxlow_base_v052_signal,
    f40cc_f40_capital_cycle_signal_ppneintvsroic_504d_base_v053_signal,
    f40cc_f40_capital_cycle_signal_roictroughbuild_base_v054_signal,
    f40cc_f40_capital_cycle_signal_capexchgvsret_63d_base_v055_signal,
    f40cc_f40_capital_cycle_signal_assetgvsret_1260d_base_v056_signal,
    f40cc_f40_capital_cycle_signal_favstarve_base_v057_signal,
    f40cc_f40_capital_cycle_signal_reinvvsroicrank_504d_base_v058_signal,
    f40cc_f40_capital_cycle_signal_capexroiccotrend_base_v059_signal,
    f40cc_f40_capital_cycle_signal_capexdispxlow_base_v060_signal,
    f40cc_f40_capital_cycle_signal_invramprxret_1260d_base_v061_signal,
    f40cc_f40_capital_cycle_signal_buildretbounded_504d_base_v062_signal,
    f40cc_f40_capital_cycle_signal_capexaccelxroicdec_base_v063_signal,
    f40cc_f40_capital_cycle_signal_overbuildpen_base_v064_signal,
    f40cc_f40_capital_cycle_signal_capexperroic_base_v065_signal,
    f40cc_f40_capital_cycle_signal_buildconvexlow_base_v066_signal,
    f40cc_f40_capital_cycle_signal_cycledist_504d_base_v067_signal,
    f40cc_f40_capital_cycle_signal_starveinflect_base_v068_signal,
    f40cc_f40_capital_cycle_signal_steadybuildret_base_v069_signal,
    f40cc_f40_capital_cycle_signal_capexyoyvsret_base_v070_signal,
    f40cc_f40_capital_cycle_signal_ppnevsinvxlow_252d_base_v071_signal,
    f40cc_f40_capital_cycle_signal_capintxret_base_v072_signal,
    f40cc_f40_capital_cycle_signal_invbuildretz_252d_base_v073_signal,
    f40cc_f40_capital_cycle_signal_capexampxlow_504d_base_v074_signal,
    f40cc_f40_capital_cycle_signal_starve_payoff_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F40_CAPITAL_CYCLE_SIGNAL_REGISTRY_001_075 = REGISTRY


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

    print("OK f40_capital_cycle_signal_base_001_075_claude: %d features pass" % n_features)
