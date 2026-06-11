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
    # PP&E as a share of the total asset base (capacity intensity)
    return ppnenet / assets.replace(0, np.nan)


def _f30_tangible_share(tangibles, assets):
    # tangible-asset share of the balance sheet
    return tangibles / assets.replace(0, np.nan)


def _f30_growth(s, w):
    # log growth of an asset-base stock over w trading days
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f30_capex_intensity(capex, assets):
    # capital-expenditure intensity vs the asset base (development pace)
    return capex / assets.replace(0, np.nan)


def _f30_invnc_intensity(investmentsnc, assets):
    # non-current investments as a share of assets (reserve/asset accumulation)
    return investmentsnc / assets.replace(0, np.nan)


# ============================================================
# --- ASSET INTENSITY LEVELS (ppnenet / assets) ---
# PP&E asset intensity level (capacity proxy)
def f30ab_f30_reserve_asset_base_assetint_63d_base_v001_signal(ppnenet, assets):
    b = _f30_asset_intensity(ppnenet, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset intensity z-scored vs its own 252d history (de-trended intensity)
def f30ab_f30_reserve_asset_base_assetintz_252d_base_v002_signal(ppnenet, assets):
    ai = _f30_asset_intensity(ppnenet, assets)
    b = _z(ai, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset intensity percentile-ranked vs its own 504d history
def f30ab_f30_reserve_asset_base_assetintrank_504d_base_v003_signal(ppnenet, assets):
    ai = _f30_asset_intensity(ppnenet, assets)
    b = _rank(ai, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset intensity vs its own 252d mean (relative capacity intensity)
def f30ab_f30_reserve_asset_base_assetintrel_252d_base_v004_signal(ppnenet, assets):
    ai = _f30_asset_intensity(ppnenet, assets)
    b = ai / _mean(ai, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset intensity smoothed (persistent capacity intensity regime)
def f30ab_f30_reserve_asset_base_assetintema_126d_base_v005_signal(ppnenet, assets):
    ai = _f30_asset_intensity(ppnenet, assets)
    b = ai.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- TANGIBLE SHARE LEVELS (tangibles / assets) ---
# tangible-asset share level (hard-asset backing of the base)
def f30ab_f30_reserve_asset_base_tangshare_63d_base_v006_signal(tangibles, assets):
    b = _f30_tangible_share(tangibles, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible share z-scored vs its own 252d history
def f30ab_f30_reserve_asset_base_tangsharez_252d_base_v007_signal(tangibles, assets):
    ts = _f30_tangible_share(tangibles, assets)
    b = _z(ts, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible share percentile-ranked vs its own 504d history
def f30ab_f30_reserve_asset_base_tangsharerank_504d_base_v008_signal(tangibles, assets):
    ts = _f30_tangible_share(tangibles, assets)
    b = _rank(ts, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# non-tangible assets relative to PP&E base (intangible weight vs hard capacity)
def f30ab_f30_reserve_asset_base_intangvsppe_63d_base_v009_signal(tangibles, assets, ppnenet):
    intang = (assets - tangibles).clip(lower=0.0)
    b = intang / ppnenet.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible share displacement from its slow EMA (hard-asset drift)
def f30ab_f30_reserve_asset_base_tangsharedisp_252d_base_v010_signal(tangibles, assets):
    ts = _f30_tangible_share(tangibles, assets)
    b = ts - ts.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- PP&E GROWTH (capacity / reserve growth) ---
# PP&E base growth over a quarter (capacity expansion rate)
def f30ab_f30_reserve_asset_base_ppgrowth_63d_base_v011_signal(ppnenet):
    b = _f30_growth(ppnenet, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PP&E base growth over a year (annual capacity expansion)
def f30ab_f30_reserve_asset_base_ppgrowth_252d_base_v012_signal(ppnenet):
    b = _f30_growth(ppnenet, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PP&E base growth over two years (multi-year build-out)
def f30ab_f30_reserve_asset_base_ppgrowth_504d_base_v013_signal(ppnenet):
    b = _f30_growth(ppnenet, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PP&E growth z-scored vs its own 504d history (de-trended capacity growth)
def f30ab_f30_reserve_asset_base_ppgrowthz_252d_base_v014_signal(ppnenet):
    g = _f30_growth(ppnenet, 252)
    b = _z(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PP&E growth ranked vs its own 504d history
def f30ab_f30_reserve_asset_base_ppgrowthrank_504d_base_v015_signal(ppnenet):
    g = _f30_growth(ppnenet, 252)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- GROSS-ASSET GROWTH (total asset base expansion) ---
# total-asset base growth over a year (gross-asset growth)
def f30ab_f30_reserve_asset_base_assetgrowth_252d_base_v016_signal(assets):
    b = _f30_growth(assets, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-asset base growth over a quarter
def f30ab_f30_reserve_asset_base_assetgrowth_63d_base_v017_signal(assets):
    b = _f30_growth(assets, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-asset base growth over two years (multi-year asset accumulation)
def f30ab_f30_reserve_asset_base_assetgrowth_504d_base_v018_signal(assets):
    b = _f30_growth(assets, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset growth z-scored vs its own 504d history
def f30ab_f30_reserve_asset_base_assetgrowthz_252d_base_v019_signal(assets):
    g = _f30_growth(assets, 252)
    b = _z(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-asset base growth over a year (hard-reserve accumulation)
def f30ab_f30_reserve_asset_base_tanggrowth_252d_base_v020_signal(tangibles):
    b = _f30_growth(tangibles, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-asset base growth over two years
def f30ab_f30_reserve_asset_base_tanggrowth_504d_base_v021_signal(tangibles):
    b = _f30_growth(tangibles, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CAPEX INTENSITY (development / build pace vs asset base) ---
# capex intensity level (development spend vs asset base)
def f30ab_f30_reserve_asset_base_capexint_63d_base_v022_signal(capex, assets):
    b = _f30_capex_intensity(capex, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity z-scored vs its own 252d history (build-pace regime)
def f30ab_f30_reserve_asset_base_capexintz_252d_base_v023_signal(capex, assets):
    ci = _f30_capex_intensity(capex, assets)
    b = _z(ci, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex relative to PP&E base (reinvestment into existing capacity)
def f30ab_f30_reserve_asset_base_capexppe_63d_base_v024_signal(capex, ppnenet):
    b = capex / ppnenet.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-to-PP&E percentile-ranked vs its 504d history
def f30ab_f30_reserve_asset_base_capexpperank_504d_base_v025_signal(capex, ppnenet):
    ratio = capex / ppnenet.replace(0, np.nan)
    b = _rank(ratio, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity smoothed (sustained development pace)
def f30ab_f30_reserve_asset_base_capexintema_126d_base_v026_signal(capex, assets):
    ci = _f30_capex_intensity(capex, assets)
    b = ci.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- NON-CURRENT INVESTMENTS (reserve / asset accumulation) ---
# non-current-investment intensity (long-asset accumulation vs base)
def f30ab_f30_reserve_asset_base_invncint_63d_base_v027_signal(investmentsnc, assets):
    b = _f30_invnc_intensity(investmentsnc, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# non-current-investment intensity z-scored vs 252d history
def f30ab_f30_reserve_asset_base_invncintz_252d_base_v028_signal(investmentsnc, assets):
    ii = _f30_invnc_intensity(investmentsnc, assets)
    b = _z(ii, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# non-current investments growth over a year (reserve accumulation rate)
def f30ab_f30_reserve_asset_base_invncgrowth_252d_base_v029_signal(investmentsnc):
    b = _f30_growth(investmentsnc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# non-current investments relative to PP&E (financial vs physical reserve mix)
def f30ab_f30_reserve_asset_base_invncppe_63d_base_v030_signal(investmentsnc, ppnenet):
    b = investmentsnc / ppnenet.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- GROWTH SPREADS (build vs base) ---
# PP&E growth minus total-asset growth (capacity-led vs broad expansion)
def f30ab_f30_reserve_asset_base_ppvsassetgr_252d_base_v031_signal(ppnenet, assets):
    b = _f30_growth(ppnenet, 252) - _f30_growth(assets, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible growth minus total-asset growth (hard-asset-led expansion)
def f30ab_f30_reserve_asset_base_tangvsassetgr_252d_base_v032_signal(tangibles, assets):
    b = _f30_growth(tangibles, 252) - _f30_growth(assets, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PP&E growth minus tangible growth (PP&E vs broader tangible base)
def f30ab_f30_reserve_asset_base_ppvstanggr_252d_base_v033_signal(ppnenet, tangibles):
    b = _f30_growth(ppnenet, 252) - _f30_growth(tangibles, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short vs long PP&E growth spread (acceleration of capacity build)
def f30ab_f30_reserve_asset_base_ppgrspread_63v252_base_v034_signal(ppnenet):
    b = _f30_growth(ppnenet, 63) * 4.0 - _f30_growth(ppnenet, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short vs long asset growth spread (broad-base acceleration)
def f30ab_f30_reserve_asset_base_assetgrspread_63v252_base_v035_signal(assets):
    b = _f30_growth(assets, 63) * 4.0 - _f30_growth(assets, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- INTENSITY DYNAMICS ---
# asset-intensity mean-reversion gap: intensity vs its slow EMA, in std units
def f30ab_f30_reserve_asset_base_assetintgap_126d_base_v036_signal(ppnenet, assets):
    ai = _f30_asset_intensity(ppnenet, assets)
    gap = ai - ai.ewm(span=126, min_periods=42).mean()
    b = gap / _std(ai, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-share mean-reversion gap: share vs its slow EMA, in std units
def f30ab_f30_reserve_asset_base_tangsharegap_126d_base_v037_signal(tangibles, assets):
    ts = _f30_tangible_share(tangibles, assets)
    gap = ts - ts.ewm(span=126, min_periods=42).mean()
    b = gap / _std(ts, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in capex intensity over a year (build-pace drift)
def f30ab_f30_reserve_asset_base_capexintchg_252d_base_v038_signal(capex, assets):
    ci = _f30_capex_intensity(capex, assets)
    b = ci - ci.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-intensity cycle-position velocity: change in 504d range position over a quarter
def f30ab_f30_reserve_asset_base_assetintposvel_504d_base_v039_signal(ppnenet, assets):
    ai = _f30_asset_intensity(ppnenet, assets)
    hi = _rmax(ai, 504)
    lo = _rmin(ai, 504)
    pos = (ai - lo) / (hi - lo).replace(0, np.nan)
    b = pos - pos.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible share over its 504d range position
def f30ab_f30_reserve_asset_base_tangsharepos_504d_base_v040_signal(tangibles, assets):
    ts = _f30_tangible_share(tangibles, assets)
    hi = _rmax(ts, 504)
    lo = _rmin(ts, 504)
    b = (ts - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CAPITAL BASE EXPANSION THROUGH CYCLE ---
# investmentsnc weight in capital-base growth: invnc 252d growth share of capbase growth
def f30ab_f30_reserve_asset_base_invnccontrib_252d_base_v041_signal(ppnenet, investmentsnc):
    d_inv = investmentsnc - investmentsnc.shift(252)
    d_cap = (ppnenet + investmentsnc) - (ppnenet + investmentsnc).shift(252)
    b = d_inv / d_cap.replace(0, np.nan)
    b = b.clip(lower=-3.0, upper=3.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financial-vs-physical build balance: invnc intensity minus capex intensity
def f30ab_f30_reserve_asset_base_buildbal_63d_base_v042_signal(investmentsnc, capex, assets):
    ii = _f30_invnc_intensity(investmentsnc, assets)
    ci = _f30_capex_intensity(capex, assets)
    b = ii - ci
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# build-balance z-scored vs 252d history (reserve-accumulation-mix regime)
def f30ab_f30_reserve_asset_base_buildbalz_252d_base_v043_signal(investmentsnc, capex, assets):
    ii = _f30_invnc_intensity(investmentsnc, assets)
    ci = _f30_capex_intensity(capex, assets)
    b = _z(ii - ci, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# non-PP&E reserve expansion: capital-base 504d growth in excess of PP&E growth
def f30ab_f30_reserve_asset_base_invledexpand_504d_base_v044_signal(ppnenet, investmentsnc):
    capbase = ppnenet + investmentsnc
    b = _f30_growth(capbase, 504) - _f30_growth(ppnenet, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative capex relative to PP&E base (gross investment intensity)
def f30ab_f30_reserve_asset_base_cumcapexppe_252d_base_v045_signal(capex, ppnenet):
    cum = capex.rolling(252, min_periods=126).sum()
    b = cum / ppnenet.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ACCUMULATED CAPEX / BUILD STREAKS ---
# cumulative capex over a year vs total assets (annual build intensity)
def f30ab_f30_reserve_asset_base_cumcapexassets_252d_base_v046_signal(capex, assets):
    cum = capex.rolling(252, min_periods=126).sum()
    b = cum / assets.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive-month PP&E-build streak length (capacity-build persistence regime)
def f30ab_f30_reserve_asset_base_ppbuildstreak_base_v047_signal(ppnenet):
    rising = (ppnenet > ppnenet.shift(21)).astype(float)
    # length of the current run of rising months (reset on a non-rising month)
    grp = (rising == 0).cumsum()
    b = rising.groupby(grp).cumsum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-base expansion breadth: net (up minus down) quarters over 504d, demeaned
def f30ab_f30_reserve_asset_base_assetbuildbreadth_504d_base_v048_signal(assets):
    chg = np.sign(assets - assets.shift(63))
    b = chg.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of quarters in last 2y with rising asset intensity (intensifying capacity)
def f30ab_f30_reserve_asset_base_intensifycnt_504d_base_v049_signal(ppnenet, assets):
    ai = _f30_asset_intensity(ppnenet, assets)
    rising = (ai > ai.shift(63)).astype(float)
    b = rising.rolling(504, min_periods=252).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- GROWTH STABILITY / DISPERSION ---
# PP&E growth stability: 252d growth divided by dispersion of growth
def f30ab_f30_reserve_asset_base_ppgrstab_252d_base_v050_signal(ppnenet):
    g = _f30_growth(ppnenet, 63)
    b = _mean(g, 252) / _std(g, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset growth stability (growth-to-dispersion of total assets)
def f30ab_f30_reserve_asset_base_assetgrstab_252d_base_v051_signal(assets):
    g = _f30_growth(assets, 63)
    b = _mean(g, 252) / _std(g, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of asset intensity over a year (capacity-mix instability)
def f30ab_f30_reserve_asset_base_assetintdisp_252d_base_v052_signal(ppnenet, assets):
    ai = _f30_asset_intensity(ppnenet, assets)
    b = _std(ai, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of capex intensity over a year (lumpy-build proxy)
def f30ab_f30_reserve_asset_base_capexintdisp_252d_base_v053_signal(capex, assets):
    ci = _f30_capex_intensity(capex, assets)
    b = _std(ci, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- LOG LEVELS / SCALE ---
# log PP&E level normalized vs its 504d mean (reserve-scale deviation)
def f30ab_f30_reserve_asset_base_ppscale_504d_base_v054_signal(ppnenet):
    lp = np.log(ppnenet.replace(0, np.nan))
    b = lp - _mean(lp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log asset level vs its 504d mean (asset-scale deviation)
def f30ab_f30_reserve_asset_base_assetscale_504d_base_v055_signal(assets):
    la = np.log(assets.replace(0, np.nan))
    b = la - _mean(la, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log tangible level vs its 504d mean (hard-asset-scale deviation)
def f30ab_f30_reserve_asset_base_tangscale_504d_base_v056_signal(tangibles):
    lt = np.log(tangibles.replace(0, np.nan))
    b = lt - _mean(lt, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- MULTI-WINDOW GROWTH COMPOSITES ---
# blended PP&E growth across 63/252/504 windows (composite capacity build)
def f30ab_f30_reserve_asset_base_ppgrblend_base_v057_signal(ppnenet):
    g1 = _f30_growth(ppnenet, 63) * 4.0
    g2 = _f30_growth(ppnenet, 252)
    g3 = _f30_growth(ppnenet, 504) * 0.5
    b = (g1 + g2 + g3) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended asset growth across windows (composite base expansion)
def f30ab_f30_reserve_asset_base_assetgrblend_base_v058_signal(assets):
    g1 = _f30_growth(assets, 63) * 4.0
    g2 = _f30_growth(assets, 252)
    g3 = _f30_growth(assets, 504) * 0.5
    b = (g1 + g2 + g3) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion across multi-window PP&E growth (build-pace disagreement)
def f30ab_f30_reserve_asset_base_ppgrdisp_base_v059_signal(ppnenet):
    g1 = _f30_growth(ppnenet, 63) * 4.0
    g2 = _f30_growth(ppnenet, 252)
    g3 = _f30_growth(ppnenet, 504) * 0.5
    b = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- RATIO INTERACTIONS ---
# capex-vs-investments build-mix tilt: log ratio of capex to non-current investments
def f30ab_f30_reserve_asset_base_capexinvtilt_63d_base_v060_signal(capex, investmentsnc):
    b = np.log(capex.replace(0, np.nan) / investmentsnc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PP&E intensity times asset growth (capacity-weighted expansion)
def f30ab_f30_reserve_asset_base_intensxgrowth_252d_base_v061_signal(ppnenet, assets):
    ai = _f30_asset_intensity(ppnenet, assets)
    g = _f30_growth(assets, 252)
    b = ai * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# relative hard-asset momentum: tangible growth z minus PP&E growth z (mix shift)
def f30ab_f30_reserve_asset_base_tangppmomspr_252d_base_v062_signal(tangibles, ppnenet):
    gt = _z(_f30_growth(tangibles, 252), 504)
    gp = _z(_f30_growth(ppnenet, 252), 504)
    b = gt - gp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- INVESTMENT MIX ---
# instability of the capex/(capex+invnc) build mix over a year (lumpy-allocation proxy)
def f30ab_f30_reserve_asset_base_buildmixvol_252d_base_v063_signal(capex, investmentsnc):
    mix = capex / (capex + investmentsnc).replace(0, np.nan)
    b = _std(mix, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# physical-mix z-scored vs 252d history (mix-shift regime)
def f30ab_f30_reserve_asset_base_physmixz_252d_base_v064_signal(ppnenet, investmentsnc):
    mix = ppnenet / (ppnenet + investmentsnc).replace(0, np.nan)
    b = _z(mix, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in physical-mix over a year (reserve-composition shift)
def f30ab_f30_reserve_asset_base_physmixchg_252d_base_v065_signal(ppnenet, investmentsnc):
    mix = ppnenet / (ppnenet + investmentsnc).replace(0, np.nan)
    b = mix - mix.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- NET-OF-DEPRECIATION / EFFICIENCY PROXIES ---
# capex spending acceleration: annual capex vs prior-year capex (build-cycle momentum)
def f30ab_f30_reserve_asset_base_capexaccel_252d_base_v066_signal(capex):
    cum = capex.rolling(252, min_periods=126).sum()
    b = np.log(cum.replace(0, np.nan) / cum.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex coverage of asset growth (how much asset growth was capex-funded)
def f30ab_f30_reserve_asset_base_capexcover_252d_base_v067_signal(capex, assets):
    cum = capex.rolling(252, min_periods=126).sum()
    delta = (assets - assets.shift(252)).clip(lower=0.0)
    b = cum / delta.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financial-vs-physical reserve growth spread: invnc growth minus cumulative-capex growth
def f30ab_f30_reserve_asset_base_invvscapexgr_252d_base_v068_signal(investmentsnc, capex):
    gi = _f30_growth(investmentsnc, 252)
    cum = capex.rolling(126, min_periods=63).sum()
    gc = _f30_growth(cum, 252)
    b = gi - gc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CYCLE-PHASE OF THE ASSET BASE ---
# new-asset-base-high frequency: fraction of last year assets set a fresh 1260d peak
def f30ab_f30_reserve_asset_base_assetnewhi_1260d_base_v069_signal(assets):
    peak = _rmax(assets, 1260)
    is_high = (assets >= peak * 0.99999).astype(float)
    b = is_high.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PP&E cycle-phase velocity: change in 1260d range position over a half-year
def f30ab_f30_reserve_asset_base_ppcycvel_1260d_base_v070_signal(ppnenet):
    hi = _rmax(ppnenet, 1260)
    lo = _rmin(ppnenet, 1260)
    pos = (ppnenet - lo) / (hi - lo).replace(0, np.nan)
    b = pos - pos.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown of PP&E from its 1260d peak (capacity retrenchment)
def f30ab_f30_reserve_asset_base_ppdd_1260d_base_v071_signal(ppnenet):
    peak = _rmax(ppnenet, 1260)
    b = ppnenet / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown of total assets from 1260d peak (base contraction)
def f30ab_f30_reserve_asset_base_assetdd_1260d_base_v072_signal(assets):
    peak = _rmax(assets, 1260)
    b = assets / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery of PP&E off its 1260d trough (reserve rebuild)
def f30ab_f30_reserve_asset_base_pprecov_1260d_base_v073_signal(ppnenet):
    trough = _rmin(ppnenet, 1260)
    b = ppnenet / trough.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- COMPOSITE INTENSITY ---
# tangible-base coverage of annual capex (years of build embedded in hard assets)
def f30ab_f30_reserve_asset_base_tangcapexcov_252d_base_v074_signal(tangibles, capex):
    annual_capex = capex.rolling(252, min_periods=126).sum()
    b = tangibles / annual_capex.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reserve-expansion composite score: ranked PP&E growth plus ranked tangible share
# minus ranked capex intensity (build pace), a blended cross-sectional-style score
def f30ab_f30_reserve_asset_base_expandscore_252d_base_v075_signal(ppnenet, tangibles, capex, assets):
    g_rank = _rank(_f30_growth(ppnenet, 252), 504)
    ts_rank = _rank(_f30_tangible_share(tangibles, assets), 504)
    ci_rank = _rank(_f30_capex_intensity(capex, assets), 504)
    b = g_rank + ts_rank - ci_rank
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f30ab_f30_reserve_asset_base_assetint_63d_base_v001_signal,
    f30ab_f30_reserve_asset_base_assetintz_252d_base_v002_signal,
    f30ab_f30_reserve_asset_base_assetintrank_504d_base_v003_signal,
    f30ab_f30_reserve_asset_base_assetintrel_252d_base_v004_signal,
    f30ab_f30_reserve_asset_base_assetintema_126d_base_v005_signal,
    f30ab_f30_reserve_asset_base_tangshare_63d_base_v006_signal,
    f30ab_f30_reserve_asset_base_tangsharez_252d_base_v007_signal,
    f30ab_f30_reserve_asset_base_tangsharerank_504d_base_v008_signal,
    f30ab_f30_reserve_asset_base_intangvsppe_63d_base_v009_signal,
    f30ab_f30_reserve_asset_base_tangsharedisp_252d_base_v010_signal,
    f30ab_f30_reserve_asset_base_ppgrowth_63d_base_v011_signal,
    f30ab_f30_reserve_asset_base_ppgrowth_252d_base_v012_signal,
    f30ab_f30_reserve_asset_base_ppgrowth_504d_base_v013_signal,
    f30ab_f30_reserve_asset_base_ppgrowthz_252d_base_v014_signal,
    f30ab_f30_reserve_asset_base_ppgrowthrank_504d_base_v015_signal,
    f30ab_f30_reserve_asset_base_assetgrowth_252d_base_v016_signal,
    f30ab_f30_reserve_asset_base_assetgrowth_63d_base_v017_signal,
    f30ab_f30_reserve_asset_base_assetgrowth_504d_base_v018_signal,
    f30ab_f30_reserve_asset_base_assetgrowthz_252d_base_v019_signal,
    f30ab_f30_reserve_asset_base_tanggrowth_252d_base_v020_signal,
    f30ab_f30_reserve_asset_base_tanggrowth_504d_base_v021_signal,
    f30ab_f30_reserve_asset_base_capexint_63d_base_v022_signal,
    f30ab_f30_reserve_asset_base_capexintz_252d_base_v023_signal,
    f30ab_f30_reserve_asset_base_capexppe_63d_base_v024_signal,
    f30ab_f30_reserve_asset_base_capexpperank_504d_base_v025_signal,
    f30ab_f30_reserve_asset_base_capexintema_126d_base_v026_signal,
    f30ab_f30_reserve_asset_base_invncint_63d_base_v027_signal,
    f30ab_f30_reserve_asset_base_invncintz_252d_base_v028_signal,
    f30ab_f30_reserve_asset_base_invncgrowth_252d_base_v029_signal,
    f30ab_f30_reserve_asset_base_invncppe_63d_base_v030_signal,
    f30ab_f30_reserve_asset_base_ppvsassetgr_252d_base_v031_signal,
    f30ab_f30_reserve_asset_base_tangvsassetgr_252d_base_v032_signal,
    f30ab_f30_reserve_asset_base_ppvstanggr_252d_base_v033_signal,
    f30ab_f30_reserve_asset_base_ppgrspread_63v252_base_v034_signal,
    f30ab_f30_reserve_asset_base_assetgrspread_63v252_base_v035_signal,
    f30ab_f30_reserve_asset_base_assetintgap_126d_base_v036_signal,
    f30ab_f30_reserve_asset_base_tangsharegap_126d_base_v037_signal,
    f30ab_f30_reserve_asset_base_capexintchg_252d_base_v038_signal,
    f30ab_f30_reserve_asset_base_assetintposvel_504d_base_v039_signal,
    f30ab_f30_reserve_asset_base_tangsharepos_504d_base_v040_signal,
    f30ab_f30_reserve_asset_base_invnccontrib_252d_base_v041_signal,
    f30ab_f30_reserve_asset_base_buildbal_63d_base_v042_signal,
    f30ab_f30_reserve_asset_base_buildbalz_252d_base_v043_signal,
    f30ab_f30_reserve_asset_base_invledexpand_504d_base_v044_signal,
    f30ab_f30_reserve_asset_base_cumcapexppe_252d_base_v045_signal,
    f30ab_f30_reserve_asset_base_cumcapexassets_252d_base_v046_signal,
    f30ab_f30_reserve_asset_base_ppbuildstreak_base_v047_signal,
    f30ab_f30_reserve_asset_base_assetbuildbreadth_504d_base_v048_signal,
    f30ab_f30_reserve_asset_base_intensifycnt_504d_base_v049_signal,
    f30ab_f30_reserve_asset_base_ppgrstab_252d_base_v050_signal,
    f30ab_f30_reserve_asset_base_assetgrstab_252d_base_v051_signal,
    f30ab_f30_reserve_asset_base_assetintdisp_252d_base_v052_signal,
    f30ab_f30_reserve_asset_base_capexintdisp_252d_base_v053_signal,
    f30ab_f30_reserve_asset_base_ppscale_504d_base_v054_signal,
    f30ab_f30_reserve_asset_base_assetscale_504d_base_v055_signal,
    f30ab_f30_reserve_asset_base_tangscale_504d_base_v056_signal,
    f30ab_f30_reserve_asset_base_ppgrblend_base_v057_signal,
    f30ab_f30_reserve_asset_base_assetgrblend_base_v058_signal,
    f30ab_f30_reserve_asset_base_ppgrdisp_base_v059_signal,
    f30ab_f30_reserve_asset_base_capexinvtilt_63d_base_v060_signal,
    f30ab_f30_reserve_asset_base_intensxgrowth_252d_base_v061_signal,
    f30ab_f30_reserve_asset_base_tangppmomspr_252d_base_v062_signal,
    f30ab_f30_reserve_asset_base_buildmixvol_252d_base_v063_signal,
    f30ab_f30_reserve_asset_base_physmixz_252d_base_v064_signal,
    f30ab_f30_reserve_asset_base_physmixchg_252d_base_v065_signal,
    f30ab_f30_reserve_asset_base_capexaccel_252d_base_v066_signal,
    f30ab_f30_reserve_asset_base_capexcover_252d_base_v067_signal,
    f30ab_f30_reserve_asset_base_invvscapexgr_252d_base_v068_signal,
    f30ab_f30_reserve_asset_base_assetnewhi_1260d_base_v069_signal,
    f30ab_f30_reserve_asset_base_ppcycvel_1260d_base_v070_signal,
    f30ab_f30_reserve_asset_base_ppdd_1260d_base_v071_signal,
    f30ab_f30_reserve_asset_base_assetdd_1260d_base_v072_signal,
    f30ab_f30_reserve_asset_base_pprecov_1260d_base_v073_signal,
    f30ab_f30_reserve_asset_base_tangcapexcov_252d_base_v074_signal,
    f30ab_f30_reserve_asset_base_expandscore_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_RESERVE_ASSET_BASE_REGISTRY_001_075 = REGISTRY


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
    # tangibles: own dynamics but capped to stay a subset of assets (tangibles <= assets)
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

    print("OK f30_reserve_asset_base_base_001_075_claude: %d features pass" % n_features)
