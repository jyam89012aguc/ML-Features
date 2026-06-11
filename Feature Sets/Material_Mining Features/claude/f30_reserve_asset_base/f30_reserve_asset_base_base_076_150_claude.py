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


def _slope(s, w):
    return (s - s.shift(w)) / float(w)


# ===== folder domain primitives (reserve / asset base) =====
def _f30_asset_intensity(ppnenet, assets):
    return ppnenet / assets.replace(0, np.nan)


def _f30_tangible_share(tangibles, assets):
    return tangibles / assets.replace(0, np.nan)


def _f30_growth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f30_capex_intensity(capex, assets):
    return capex / assets.replace(0, np.nan)


def _f30_invnc_intensity(investmentsnc, assets):
    return investmentsnc / assets.replace(0, np.nan)


# ============================================================
# --- ANNUALIZED CAPEX-TO-PP&E (reinvestment rate facets) ---
# annual capex-to-PP&E reinvestment rate (gross reinvestment into capacity)
def f30ab_f30_reserve_asset_base_reinvrate_252d_base_v076_signal(capex, ppnenet):
    annual = _mean(capex, 252)
    b = annual / ppnenet.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-rate z-scored vs 504d history (reinvestment regime)
def f30ab_f30_reserve_asset_base_reinvratez_504d_base_v077_signal(capex, ppnenet):
    annual = _mean(capex, 252)
    rr = annual / ppnenet.replace(0, np.nan)
    b = _z(rr, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex run-rate vs financial-reserve flow, ranked (physical-build vs financial-build regime)
def f30ab_f30_reserve_asset_base_capexvsinvrate_504d_base_v078_signal(capex, investmentsnc):
    rr = _mean(capex, 63) / investmentsnc.replace(0, np.nan)
    b = _rank(rr, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ASSET-TURNOVER-OF-BASE PROXIES (capex velocity) ---
# smoothed capex deployment ratio: 63d-mean capex vs 63d-mean tangible base
def f30ab_f30_reserve_asset_base_capexdeploy_63d_base_v079_signal(capex, tangibles):
    b = _mean(capex, 63) / _mean(tangibles, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex run-rate growth ranked vs 504d history (build-pace acceleration percentile)
def f30ab_f30_reserve_asset_base_capexgrrank_504d_base_v080_signal(capex, assets):
    rr = _mean(capex, 63) / assets.replace(0, np.nan)
    g = rr - rr.shift(126)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- PP&E-TO-TANGIBLE DYNAMICS ---
# PP&E share of tangibles change over a year (capacity vs broad tangible build)
def f30ab_f30_reserve_asset_base_ppintangchg_252d_base_v081_signal(ppnenet, tangibles):
    sh = ppnenet / tangibles.replace(0, np.nan)
    b = sh - sh.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PP&E share of tangibles z-scored vs 252d history
def f30ab_f30_reserve_asset_base_ppintangz_252d_base_v082_signal(ppnenet, tangibles):
    sh = ppnenet / tangibles.replace(0, np.nan)
    b = _z(sh, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- INVESTMENTS-NC DYNAMICS ---
# non-current investments share of tangibles (financial reserve depth in hard base)
def f30ab_f30_reserve_asset_base_invnctang_63d_base_v083_signal(investmentsnc, tangibles):
    b = investmentsnc / tangibles.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# non-current investments growth over two years (multi-year reserve accumulation)
def f30ab_f30_reserve_asset_base_invncgr_504d_base_v084_signal(investmentsnc):
    b = _f30_growth(investmentsnc, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# non-current investments growth z-scored vs 504d history
def f30ab_f30_reserve_asset_base_invncgrz_252d_base_v085_signal(investmentsnc):
    g = _f30_growth(investmentsnc, 252)
    b = _z(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ASSET-BASE ACCELERATION (growth-of-growth) ---
# PP&E growth acceleration: 252d growth now vs a year ago
def f30ab_f30_reserve_asset_base_ppgraccel_252d_base_v086_signal(ppnenet):
    g = _f30_growth(ppnenet, 252)
    b = g - g.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset growth acceleration: 252d growth now vs a year ago
def f30ab_f30_reserve_asset_base_assetgraccel_252d_base_v087_signal(assets):
    g = _f30_growth(assets, 252)
    b = g - g.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible growth acceleration: 252d growth now vs a year ago
def f30ab_f30_reserve_asset_base_tanggraccel_252d_base_v088_signal(tangibles):
    g = _f30_growth(tangibles, 252)
    b = g - g.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- GROWTH PERSISTENCE / SIGN STREAKS ---
# net sign of PP&E quarter-growth over 504d (build-direction persistence)
def f30ab_f30_reserve_asset_base_ppdirpersist_504d_base_v089_signal(ppnenet):
    chg = np.sign(ppnenet - ppnenet.shift(63))
    b = chg.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of months over 252d where asset intensity rose (intensifying capacity)
def f30ab_f30_reserve_asset_base_intensupcnt_252d_base_v090_signal(ppnenet, assets):
    ai = _f30_asset_intensity(ppnenet, assets)
    up = (ai > ai.shift(21)).astype(float)
    b = up.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive-quarter capex-intensity-rising streak (sustained build escalation)
def f30ab_f30_reserve_asset_base_capexescalstreak_base_v091_signal(capex, assets):
    ci = _f30_capex_intensity(capex, assets)
    rising = (ci > ci.shift(63)).astype(float)
    grp = (rising == 0).cumsum()
    b = rising.groupby(grp).cumsum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DEPRECIATION / AGING PROXIES (capex vs PP&E maintenance) ---
# maintenance-vs-growth ratio: capex run-rate relative to PP&E change (build efficiency)
def f30ab_f30_reserve_asset_base_maintratio_252d_base_v092_signal(capex, ppnenet):
    annual = _mean(capex, 252)
    delta = (ppnenet - ppnenet.shift(252)).abs()
    b = np.tanh(annual / delta.replace(0, np.nan) - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied PP&E decay: negative PP&E change relative to capex spent (shrinkage proxy)
def f30ab_f30_reserve_asset_base_ppdecay_126d_base_v093_signal(capex, ppnenet):
    delta = ppnenet - ppnenet.shift(126)
    hcapex = _mean(capex, 126)
    b = (-delta).clip(lower=0.0) / hcapex.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ASSET-MIX BREADTH / DISPERSION ---
# dispersion across PP&E / tangible / invnc intensities (asset-mix disagreement)
def f30ab_f30_reserve_asset_base_mixdisp_base_v094_signal(ppnenet, tangibles, investmentsnc, assets):
    a1 = _f30_asset_intensity(ppnenet, assets)
    a2 = _f30_tangible_share(tangibles, assets)
    a3 = _f30_invnc_intensity(investmentsnc, assets)
    b = pd.concat([a1, a2, a3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# span of intensities: max minus min across PP&E / tangible / invnc shares
def f30ab_f30_reserve_asset_base_mixspan_base_v095_signal(ppnenet, tangibles, investmentsnc, assets):
    a1 = _f30_asset_intensity(ppnenet, assets)
    a2 = _f30_tangible_share(tangibles, assets)
    a3 = _f30_invnc_intensity(investmentsnc, assets)
    stacked = pd.concat([a1, a2, a3], axis=1)
    b = stacked.max(axis=1) - stacked.min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ASSET-BASE DRAWDOWN / RECOVERY DYNAMICS ---
# tangible-base drawdown from its 1260d peak (hard-asset retrenchment)
def f30ab_f30_reserve_asset_base_tangdd_1260d_base_v096_signal(tangibles):
    peak = _rmax(tangibles, 1260)
    b = tangibles / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of 504d the asset base was below its trailing peak (underbuild duration)
def f30ab_f30_reserve_asset_base_assetuwfrac_504d_base_v097_signal(assets):
    peak = _rmax(assets, 504)
    under = (assets < peak * 0.999).astype(float)
    b = under.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PP&E recovery off 504d trough scaled by elapsed (reserve-rebuild rate)
def f30ab_f30_reserve_asset_base_pprecovrate_504d_base_v098_signal(ppnenet):
    trough = _rmin(ppnenet, 504)
    rec = ppnenet / trough.replace(0, np.nan) - 1.0
    b = rec.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- INTENSITY TERM STRUCTURE ---
# short vs long asset-intensity spread (intensity term structure)
def f30ab_f30_reserve_asset_base_intensterm_base_v099_signal(ppnenet, assets):
    ai = _f30_asset_intensity(ppnenet, assets)
    short = _mean(ai, 63)
    long = _mean(ai, 504)
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short vs long tangible-share spread (tangibility term structure)
def f30ab_f30_reserve_asset_base_tangterm_base_v100_signal(tangibles, assets):
    ts = _f30_tangible_share(tangibles, assets)
    short = _mean(ts, 63)
    long = _mean(ts, 504)
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short vs long capex-intensity spread (build-pace term structure)
def f30ab_f30_reserve_asset_base_capexterm_base_v101_signal(capex, assets):
    ci = _f30_capex_intensity(capex, assets)
    short = _mean(ci, 63)
    long = _mean(ci, 504)
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- LOG-SCALE GROWTH SLOPES (regression-free trend) ---
# log PP&E linear-trend proxy: 252d change in 63d-mean of log PP&E
def f30ab_f30_reserve_asset_base_pptrend_252d_base_v102_signal(ppnenet):
    lp = np.log(ppnenet.replace(0, np.nan))
    sm = _mean(lp, 63)
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log asset linear-trend proxy: 252d change in 63d-mean of log assets
def f30ab_f30_reserve_asset_base_assettrend_252d_base_v103_signal(assets):
    la = np.log(assets.replace(0, np.nan))
    sm = _mean(la, 63)
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log tangible linear-trend proxy: 252d change in 63d-mean of log tangibles
def f30ab_f30_reserve_asset_base_tangtrend_252d_base_v104_signal(tangibles):
    lt = np.log(tangibles.replace(0, np.nan))
    sm = _mean(lt, 63)
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CAPITAL-BASE COMPOSITES (distinct from file 1) ---
# hard-reserve base (ppnenet+tangibles)/2 growth over a year, isolated from assets
def f30ab_f30_reserve_asset_base_hardbasegr_252d_base_v105_signal(ppnenet, tangibles):
    hb = 0.5 * ppnenet + 0.5 * tangibles
    b = _f30_growth(hb, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# hard-reserve base intensity vs total assets, displacement from EMA
def f30ab_f30_reserve_asset_base_hardbasedisp_252d_base_v106_signal(ppnenet, tangibles, assets):
    hb = 0.5 * ppnenet + 0.5 * tangibles
    hi = hb / assets.replace(0, np.nan)
    b = hi - hi.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ASSET-EFFICIENCY-OF-BUILD (interaction) ---
# build efficiency: PP&E growth divided by capex intensity (output per build pace)
def f30ab_f30_reserve_asset_base_buildeff_252d_base_v107_signal(ppnenet, capex, assets):
    g = _f30_growth(ppnenet, 252)
    ci = _f30_capex_intensity(capex, assets).rolling(252, min_periods=126).mean()
    b = g / ci.replace(0, np.nan)
    b = b.clip(lower=-50.0, upper=50.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-growth per unit of investing intensity (capital deployment efficiency)
def f30ab_f30_reserve_asset_base_deployeff_252d_base_v108_signal(assets, investmentsnc, capex):
    g = _f30_growth(assets, 252)
    deploy = (investmentsnc / assets.replace(0, np.nan)
              + _mean(capex, 252) / assets.replace(0, np.nan))
    b = g / deploy.replace(0, np.nan)
    b = b.clip(lower=-50.0, upper=50.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- INTENSITY RANK SPREADS ---
# asset-intensity rank minus tangible-share rank (capacity vs tangibility tilt)
def f30ab_f30_reserve_asset_base_intvstangrank_504d_base_v109_signal(ppnenet, tangibles, assets):
    air = _rank(_f30_asset_intensity(ppnenet, assets), 504)
    tsr = _rank(_f30_tangible_share(tangibles, assets), 504)
    b = air - tsr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-intensity rank minus invnc-intensity rank (physical vs financial build tilt)
def f30ab_f30_reserve_asset_base_capexvsinvrank_504d_base_v110_signal(capex, investmentsnc, assets):
    cir = _rank(_f30_capex_intensity(capex, assets), 504)
    iir = _rank(_f30_invnc_intensity(investmentsnc, assets), 504)
    b = cir - iir
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- MEAN-REVERSION GAPS (distinct windows / smoothers) ---
# capex-intensity gap from 252d mean in std units (build-pace extremity)
def f30ab_f30_reserve_asset_base_capexintgap_252d_base_v111_signal(capex, assets):
    ci = _f30_capex_intensity(capex, assets)
    gap = ci - _mean(ci, 252)
    b = gap / _std(ci, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invnc-intensity gap from 252d mean in std units (reserve-accumulation extremity)
def f30ab_f30_reserve_asset_base_invncintgap_252d_base_v112_signal(investmentsnc, assets):
    ii = _f30_invnc_intensity(investmentsnc, assets)
    gap = ii - _mean(ii, 252)
    b = gap / _std(ii, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ASSET-BASE CONVEXITY ---
# tangible-share convexity: signed squared deviation from its 252d mean
def f30ab_f30_reserve_asset_base_tangconvex_252d_base_v113_signal(tangibles, assets):
    ts = _f30_tangible_share(tangibles, assets)
    dev = ts - _mean(ts, 252)
    b = np.sign(dev) * (dev ** 2) * 100.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-intensity convexity: signed squared deviation from its 252d mean
def f30ab_f30_reserve_asset_base_intconvex_252d_base_v114_signal(ppnenet, assets):
    ai = _f30_asset_intensity(ppnenet, assets)
    dev = ai - _mean(ai, 252)
    b = np.sign(dev) * (dev ** 2) * 100.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- TANH-BOUNDED MOMENTUM ---
# bounded PP&E-growth momentum (tanh-squashed quarter-over-quarter growth change)
def f30ab_f30_reserve_asset_base_ppgrtanh_63d_base_v115_signal(ppnenet):
    g = _f30_growth(ppnenet, 63)
    chg = g - g.shift(63)
    b = np.tanh(8.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bounded asset-growth momentum (tanh-squashed)
def f30ab_f30_reserve_asset_base_assetgrtanh_63d_base_v116_signal(assets):
    g = _f30_growth(assets, 63)
    chg = g - g.shift(63)
    b = np.tanh(8.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CUMULATIVE-DEPLOYMENT SHARES ---
# cumulative capex share of total-asset growth over two years (build-funded growth)
def f30ab_f30_reserve_asset_base_capexfundgr_504d_base_v117_signal(capex, assets):
    cum = _mean(capex, 504)
    delta = (assets - assets.shift(504)).clip(lower=0.0)
    b = cum / delta.replace(0, np.nan)
    b = b.clip(upper=20.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative invnc change share of total-asset growth (financial-funded growth)
def f30ab_f30_reserve_asset_base_invfundgr_504d_base_v118_signal(investmentsnc, assets):
    d_inv = (investmentsnc - investmentsnc.shift(504))
    delta = (assets - assets.shift(504))
    b = d_inv / delta.replace(0, np.nan)
    b = b.clip(lower=-10.0, upper=10.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- REGIME DISTANCE / CYCLE PHASE (intensity-based) ---
# distance of asset intensity from its 504d max (room below peak intensity)
def f30ab_f30_reserve_asset_base_intpeakdist_504d_base_v119_signal(ppnenet, assets):
    ai = _f30_asset_intensity(ppnenet, assets)
    peak = _rmax(ai, 504)
    b = ai / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of capex intensity from its 504d max (build below peak pace)
def f30ab_f30_reserve_asset_base_capexpeakdist_504d_base_v120_signal(capex, assets):
    ci = _f30_capex_intensity(capex, assets)
    peak = _rmax(ci, 504)
    b = ci / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- GROWTH-DISPERSION ACROSS ASSET TYPES ---
# dispersion across PP&E/asset/tangible 252d growth (build-source disagreement)
def f30ab_f30_reserve_asset_base_growthdisp_252d_base_v121_signal(ppnenet, assets, tangibles):
    g1 = _f30_growth(ppnenet, 252)
    g2 = _f30_growth(assets, 252)
    g3 = _f30_growth(tangibles, 252)
    b = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cross-asset growth centroid: mean 252d growth across PP&E/asset/tangible (broad build)
def f30ab_f30_reserve_asset_base_growthcentroid_252d_base_v122_signal(ppnenet, assets, tangibles):
    g1 = _f30_growth(ppnenet, 252)
    g2 = _f30_growth(assets, 252)
    g3 = _f30_growth(tangibles, 252)
    mean_g = (g1 + g2 + g3) / 3.0
    b = mean_g - mean_g.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- INTENSITY STABILITY ---
# asset-intensity stability: 504d mean over 504d std (steady-capacity proxy)
def f30ab_f30_reserve_asset_base_intstab_504d_base_v123_signal(ppnenet, assets):
    ai = _f30_asset_intensity(ppnenet, assets)
    b = _mean(ai, 504) / _std(ai, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-share stability: 504d mean over 504d std
def f30ab_f30_reserve_asset_base_tangstab_504d_base_v124_signal(tangibles, assets):
    ts = _f30_tangible_share(tangibles, assets)
    b = _mean(ts, 504) / _std(ts, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- INVESTMENTS-VS-CAPACITY BUILD ---
# financial reserve build vs physical reserve build: invnc growth minus ppnenet growth
def f30ab_f30_reserve_asset_base_finvsphysgr_252d_base_v125_signal(investmentsnc, ppnenet):
    b = _f30_growth(investmentsnc, 252) - _f30_growth(ppnenet, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financial vs physical build spread, z-scored vs 504d history
def f30ab_f30_reserve_asset_base_finvsphysz_252d_base_v126_signal(investmentsnc, ppnenet):
    spr = _f30_growth(investmentsnc, 252) - _f30_growth(ppnenet, 252)
    b = _z(spr, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CAPEX BURST / LUMPY-BUILD DETECTION ---
# capex burst: quarterly capex vs its 504d typical quarterly level
def f30ab_f30_reserve_asset_base_capexburst_63d_base_v127_signal(capex):
    qcapex = _mean(capex, 63)
    typ = qcapex.rolling(504, min_periods=252).mean()
    b = qcapex / typ.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of capex-burst quarters over 504d (lumpy-build tally)
def f30ab_f30_reserve_asset_base_capexburstcnt_504d_base_v128_signal(capex):
    qcapex = _mean(capex, 63)
    typ = qcapex.rolling(252, min_periods=126).mean()
    burst = (qcapex > 1.3 * typ).astype(float)
    b = burst.rolling(504, min_periods=252).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ASSET-BASE EXPANSION QUALITY ---
# tangible-weighted asset growth: asset growth times tangible share rank
def f30ab_f30_reserve_asset_base_tangwtgr_252d_base_v129_signal(assets, tangibles):
    g = _f30_growth(assets, 252)
    tsr = _rank(_f30_tangible_share(tangibles, assets), 504)
    b = g * (tsr + 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capacity-weighted asset growth: asset growth times asset-intensity rank
def f30ab_f30_reserve_asset_base_capwtgr_252d_base_v130_signal(assets, ppnenet):
    g = _f30_growth(assets, 252)
    air = _rank(_f30_asset_intensity(ppnenet, assets), 504)
    b = g * (air + 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- INTENSITY MOMENTUM (z-of-z) ---
# asset-intensity z momentum: change in 252d z over a quarter
def f30ab_f30_reserve_asset_base_intzmom_252d_base_v131_signal(ppnenet, assets):
    ai = _f30_asset_intensity(ppnenet, assets)
    zz = _z(ai, 252)
    b = zz - zz.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-share z momentum: change in 252d z over a quarter
def f30ab_f30_reserve_asset_base_tangzmom_252d_base_v132_signal(tangibles, assets):
    ts = _f30_tangible_share(tangibles, assets)
    zz = _z(ts, 252)
    b = zz - zz.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- LONG-HORIZON ASSET CYCLE ---
# asset-base build-momentum ratio: short (63d) growth relative to long (504d) growth
def f30ab_f30_reserve_asset_base_assetmomratio_base_v133_signal(assets):
    g_short = _f30_growth(assets, 63) * 8.0
    g_long = _f30_growth(assets, 504)
    b = np.tanh(g_short - g_long)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PP&E build-momentum ratio: short (63d) growth relative to long (504d) growth
def f30ab_f30_reserve_asset_base_ppmomratio_base_v134_signal(ppnenet):
    g_short = _f30_growth(ppnenet, 63) * 8.0
    g_long = _f30_growth(ppnenet, 504)
    b = np.tanh(g_short - g_long)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible build-momentum ratio: short (63d) growth relative to long (504d) growth
def f30ab_f30_reserve_asset_base_tangmomratio_base_v135_signal(tangibles):
    g_short = _f30_growth(tangibles, 63) * 8.0
    g_long = _f30_growth(tangibles, 504)
    b = np.tanh(g_short - g_long)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- INVESTMENT-TO-ASSET TURNOVER ---
# annual capex as a fraction of the asset base, smoothed (steady deployment rate)
def f30ab_f30_reserve_asset_base_deployrate_252d_base_v136_signal(capex, assets):
    annual = _mean(capex, 252)
    rate = annual / assets.replace(0, np.nan)
    b = rate.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deployment-rate momentum (change in smoothed deployment over a quarter)
def f30ab_f30_reserve_asset_base_deploymom_252d_base_v137_signal(capex, assets):
    annual = _mean(capex, 252)
    rate = (annual / assets.replace(0, np.nan)).ewm(span=126, min_periods=42).mean()
    b = rate - rate.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- RESERVE-COVER RATIOS ---
# tangible-base cover of combined reserve outlay (capex run-rate + invnc), log
def f30ab_f30_reserve_asset_base_tangcoverbuild_63d_base_v138_signal(tangibles, capex, investmentsnc):
    outlay = _mean(capex, 63) + investmentsnc
    b = np.log1p((tangibles / outlay.replace(0, np.nan)).clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PP&E cover of annual capex (years of build embedded in capacity)
def f30ab_f30_reserve_asset_base_ppcovercapex_252d_base_v139_signal(ppnenet, capex):
    annual = _mean(capex, 252)
    b = ppnenet / annual.replace(0, np.nan)
    b = b.clip(upper=100.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ASSET-BASE BREADTH SCORE ---
# magnitude-weighted expansion breadth: mean of tanh-squashed 252d growths
def f30ab_f30_reserve_asset_base_expandbreadth_252d_base_v140_signal(ppnenet, assets, tangibles):
    g1 = np.tanh(6.0 * _f30_growth(ppnenet, 252))
    g2 = np.tanh(6.0 * _f30_growth(assets, 252))
    g3 = np.tanh(6.0 * _f30_growth(tangibles, 252))
    b = (g1 + g2 + g3) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CAPACITY-INTENSITY DETREND ---
# asset intensity minus a long EMA, ranked (de-trended intensity percentile)
def f30ab_f30_reserve_asset_base_intdetrendrank_504d_base_v141_signal(ppnenet, assets):
    ai = _f30_asset_intensity(ppnenet, assets)
    detr = ai - ai.ewm(span=504, min_periods=126).mean()
    b = _rank(detr, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible share minus a long EMA, ranked (de-trended tangibility percentile)
def f30ab_f30_reserve_asset_base_tangdetrendrank_504d_base_v142_signal(tangibles, assets):
    ts = _f30_tangible_share(tangibles, assets)
    detr = ts - ts.ewm(span=504, min_periods=126).mean()
    b = _rank(detr, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- COMPOSITE EXPANSION SCORES ---
# reserve-build composite: ranked PP&E growth plus ranked capex intensity minus ranked aging
def f30ab_f30_reserve_asset_base_buildcomposite_252d_base_v143_signal(ppnenet, capex, assets):
    gr = _rank(_f30_growth(ppnenet, 252), 504)
    ci = _rank(_f30_capex_intensity(capex, assets), 504)
    b = gr + 0.5 * ci
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financial-reserve composite: ranked invnc growth plus ranked invnc intensity
def f30ab_f30_reserve_asset_base_fincomposite_252d_base_v144_signal(investmentsnc, assets):
    gr = _rank(_f30_growth(investmentsnc, 252), 504)
    ii = _rank(_f30_invnc_intensity(investmentsnc, assets), 504)
    b = gr + ii
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CROSS-RATIO LEVELS (remaining facets) ---
# PP&E per dollar of non-current investments (capacity vs financial reserve scale)
def f30ab_f30_reserve_asset_base_ppperinv_63d_base_v145_signal(ppnenet, investmentsnc):
    b = np.log(ppnenet.replace(0, np.nan) / investmentsnc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangibles per dollar of assets minus PP&E per dollar of assets (non-PP&E tangible share)
def f30ab_f30_reserve_asset_base_nonppetang_63d_base_v146_signal(tangibles, ppnenet, assets):
    ts = _f30_tangible_share(tangibles, assets)
    ai = _f30_asset_intensity(ppnenet, assets)
    b = (ts - ai).clip(lower=-1.0, upper=1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ASSET-GROWTH RISK ADJUSTMENT ---
# risk-adjusted asset growth: 252d growth divided by 252d growth volatility
def f30ab_f30_reserve_asset_base_riskadjgr_252d_base_v147_signal(assets):
    g63 = _f30_growth(assets, 63)
    b = _f30_growth(assets, 252) / _std(g63, 252).replace(0, np.nan)
    b = b.clip(lower=-50.0, upper=50.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# risk-adjusted PP&E growth: 252d growth divided by quarterly-growth volatility
def f30ab_f30_reserve_asset_base_ppriskadjgr_252d_base_v148_signal(ppnenet):
    g63 = _f30_growth(ppnenet, 63)
    b = _f30_growth(ppnenet, 252) / _std(g63, 252).replace(0, np.nan)
    b = b.clip(lower=-50.0, upper=50.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- FINAL CYCLE-POSITION COMPOSITE ---
# asset-base maturity: 1260d range position times asset-intensity rank (mature capacity)
def f30ab_f30_reserve_asset_base_maturity_1260d_base_v149_signal(assets, ppnenet):
    hi = _rmax(assets, 1260)
    lo = _rmin(assets, 1260)
    pos = (assets - lo) / (hi - lo).replace(0, np.nan)
    air = _rank(_f30_asset_intensity(ppnenet, assets), 504) + 0.5
    b = pos * air
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reserve-cycle trough proximity: how close PP&E sits to its 1260d low (rebuild setup)
def f30ab_f30_reserve_asset_base_troughprox_1260d_base_v150_signal(ppnenet):
    lo = _rmin(ppnenet, 1260)
    b = lo.replace(0, np.nan) / ppnenet.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f30ab_f30_reserve_asset_base_reinvrate_252d_base_v076_signal,
    f30ab_f30_reserve_asset_base_reinvratez_504d_base_v077_signal,
    f30ab_f30_reserve_asset_base_capexvsinvrate_504d_base_v078_signal,
    f30ab_f30_reserve_asset_base_capexdeploy_63d_base_v079_signal,
    f30ab_f30_reserve_asset_base_capexgrrank_504d_base_v080_signal,
    f30ab_f30_reserve_asset_base_ppintangchg_252d_base_v081_signal,
    f30ab_f30_reserve_asset_base_ppintangz_252d_base_v082_signal,
    f30ab_f30_reserve_asset_base_invnctang_63d_base_v083_signal,
    f30ab_f30_reserve_asset_base_invncgr_504d_base_v084_signal,
    f30ab_f30_reserve_asset_base_invncgrz_252d_base_v085_signal,
    f30ab_f30_reserve_asset_base_ppgraccel_252d_base_v086_signal,
    f30ab_f30_reserve_asset_base_assetgraccel_252d_base_v087_signal,
    f30ab_f30_reserve_asset_base_tanggraccel_252d_base_v088_signal,
    f30ab_f30_reserve_asset_base_ppdirpersist_504d_base_v089_signal,
    f30ab_f30_reserve_asset_base_intensupcnt_252d_base_v090_signal,
    f30ab_f30_reserve_asset_base_capexescalstreak_base_v091_signal,
    f30ab_f30_reserve_asset_base_maintratio_252d_base_v092_signal,
    f30ab_f30_reserve_asset_base_ppdecay_126d_base_v093_signal,
    f30ab_f30_reserve_asset_base_mixdisp_base_v094_signal,
    f30ab_f30_reserve_asset_base_mixspan_base_v095_signal,
    f30ab_f30_reserve_asset_base_tangdd_1260d_base_v096_signal,
    f30ab_f30_reserve_asset_base_assetuwfrac_504d_base_v097_signal,
    f30ab_f30_reserve_asset_base_pprecovrate_504d_base_v098_signal,
    f30ab_f30_reserve_asset_base_intensterm_base_v099_signal,
    f30ab_f30_reserve_asset_base_tangterm_base_v100_signal,
    f30ab_f30_reserve_asset_base_capexterm_base_v101_signal,
    f30ab_f30_reserve_asset_base_pptrend_252d_base_v102_signal,
    f30ab_f30_reserve_asset_base_assettrend_252d_base_v103_signal,
    f30ab_f30_reserve_asset_base_tangtrend_252d_base_v104_signal,
    f30ab_f30_reserve_asset_base_hardbasegr_252d_base_v105_signal,
    f30ab_f30_reserve_asset_base_hardbasedisp_252d_base_v106_signal,
    f30ab_f30_reserve_asset_base_buildeff_252d_base_v107_signal,
    f30ab_f30_reserve_asset_base_deployeff_252d_base_v108_signal,
    f30ab_f30_reserve_asset_base_intvstangrank_504d_base_v109_signal,
    f30ab_f30_reserve_asset_base_capexvsinvrank_504d_base_v110_signal,
    f30ab_f30_reserve_asset_base_capexintgap_252d_base_v111_signal,
    f30ab_f30_reserve_asset_base_invncintgap_252d_base_v112_signal,
    f30ab_f30_reserve_asset_base_tangconvex_252d_base_v113_signal,
    f30ab_f30_reserve_asset_base_intconvex_252d_base_v114_signal,
    f30ab_f30_reserve_asset_base_ppgrtanh_63d_base_v115_signal,
    f30ab_f30_reserve_asset_base_assetgrtanh_63d_base_v116_signal,
    f30ab_f30_reserve_asset_base_capexfundgr_504d_base_v117_signal,
    f30ab_f30_reserve_asset_base_invfundgr_504d_base_v118_signal,
    f30ab_f30_reserve_asset_base_intpeakdist_504d_base_v119_signal,
    f30ab_f30_reserve_asset_base_capexpeakdist_504d_base_v120_signal,
    f30ab_f30_reserve_asset_base_growthdisp_252d_base_v121_signal,
    f30ab_f30_reserve_asset_base_growthcentroid_252d_base_v122_signal,
    f30ab_f30_reserve_asset_base_intstab_504d_base_v123_signal,
    f30ab_f30_reserve_asset_base_tangstab_504d_base_v124_signal,
    f30ab_f30_reserve_asset_base_finvsphysgr_252d_base_v125_signal,
    f30ab_f30_reserve_asset_base_finvsphysz_252d_base_v126_signal,
    f30ab_f30_reserve_asset_base_capexburst_63d_base_v127_signal,
    f30ab_f30_reserve_asset_base_capexburstcnt_504d_base_v128_signal,
    f30ab_f30_reserve_asset_base_tangwtgr_252d_base_v129_signal,
    f30ab_f30_reserve_asset_base_capwtgr_252d_base_v130_signal,
    f30ab_f30_reserve_asset_base_intzmom_252d_base_v131_signal,
    f30ab_f30_reserve_asset_base_tangzmom_252d_base_v132_signal,
    f30ab_f30_reserve_asset_base_assetmomratio_base_v133_signal,
    f30ab_f30_reserve_asset_base_ppmomratio_base_v134_signal,
    f30ab_f30_reserve_asset_base_tangmomratio_base_v135_signal,
    f30ab_f30_reserve_asset_base_deployrate_252d_base_v136_signal,
    f30ab_f30_reserve_asset_base_deploymom_252d_base_v137_signal,
    f30ab_f30_reserve_asset_base_tangcoverbuild_63d_base_v138_signal,
    f30ab_f30_reserve_asset_base_ppcovercapex_252d_base_v139_signal,
    f30ab_f30_reserve_asset_base_expandbreadth_252d_base_v140_signal,
    f30ab_f30_reserve_asset_base_intdetrendrank_504d_base_v141_signal,
    f30ab_f30_reserve_asset_base_tangdetrendrank_504d_base_v142_signal,
    f30ab_f30_reserve_asset_base_buildcomposite_252d_base_v143_signal,
    f30ab_f30_reserve_asset_base_fincomposite_252d_base_v144_signal,
    f30ab_f30_reserve_asset_base_ppperinv_63d_base_v145_signal,
    f30ab_f30_reserve_asset_base_nonppetang_63d_base_v146_signal,
    f30ab_f30_reserve_asset_base_riskadjgr_252d_base_v147_signal,
    f30ab_f30_reserve_asset_base_ppriskadjgr_252d_base_v148_signal,
    f30ab_f30_reserve_asset_base_maturity_1260d_base_v149_signal,
    f30ab_f30_reserve_asset_base_troughprox_1260d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_RESERVE_ASSET_BASE_REGISTRY_076_150 = REGISTRY


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

    # reserve / asset-base fundamentals: all positive with growth drift
    assets = _fund(3001, base=1.2e9, drift=0.015, vol=0.06).rename("assets")
    ppnenet = _fund(3002, base=6e8, drift=0.020, vol=0.10).rename("ppnenet")
    _tang_raw = _fund(3003, base=6.5e8, drift=0.010, vol=0.09)
    tangibles = pd.Series(np.minimum(_tang_raw.values, 0.97 * assets.values),
                          name="tangibles")
    capex = _fund(3004, base=8e7, drift=0.012, vol=0.20).rename("capex")
    investmentsnc = _fund(3005, base=2e8, drift=0.010, vol=0.16).rename("investmentsnc")

    cols = {"assets": assets, "ppnenet": ppnenet, "tangibles": tangibles,
            "capex": capex, "investmentsnc": investmentsnc}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in ("ppnenet", "assets", "tangibles", "capex", "investmentsnc")
                   for c in meta["inputs"]), name
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

    print("OK f30_reserve_asset_base_base_076_150_claude: %d features pass" % n_features)
