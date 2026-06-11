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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _slope(s, w):
    # 1st math derivative: rate of change over w trading days
    return (s - s.shift(w)) / float(w)


# ===== folder domain primitives (reserve / asset base) =====
def _asset_intensity(ppnenet, assets):
    return ppnenet / assets.replace(0, np.nan)


def _tangible_share(tangibles, assets):
    return tangibles / assets.replace(0, np.nan)


def _growth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _capex_intensity(capex, assets):
    return capex / assets.replace(0, np.nan)


def _invnc_intensity(investmentsnc, assets):
    return investmentsnc / assets.replace(0, np.nan)


# ============================================================
# Each feature builds a reserve/asset-base base series inline, then takes its
# 1st math derivative (slope) over a window matched to the base window.

# slope of asset intensity (capacity-intensity velocity), 21d
def f30ab_f30_reserve_asset_base_assetint_21d_slope_v001_signal(ppnenet, assets):
    base = _asset_intensity(ppnenet, assets)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asset intensity, 63d (slower capacity-intensity velocity)
def f30ab_f30_reserve_asset_base_assetint_63d_slope_v002_signal(ppnenet, assets):
    base = _asset_intensity(ppnenet, assets)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tangible share (tangibility velocity), 21d
def f30ab_f30_reserve_asset_base_tangshare_21d_slope_v003_signal(tangibles, assets):
    base = _tangible_share(tangibles, assets)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tangible share, 63d
def f30ab_f30_reserve_asset_base_tangshare_63d_slope_v004_signal(tangibles, assets):
    base = _tangible_share(tangibles, assets)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex intensity (build-pace velocity), 21d
def f30ab_f30_reserve_asset_base_capexint_21d_slope_v005_signal(capex, assets):
    base = _capex_intensity(capex, assets)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex intensity, 63d
def f30ab_f30_reserve_asset_base_capexint_63d_slope_v006_signal(capex, assets):
    base = _capex_intensity(capex, assets)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of non-current-investment intensity (reserve-accumulation velocity), 21d
def f30ab_f30_reserve_asset_base_invncint_21d_slope_v007_signal(investmentsnc, assets):
    base = _invnc_intensity(investmentsnc, assets)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of non-current-investment intensity, 63d
def f30ab_f30_reserve_asset_base_invncint_63d_slope_v008_signal(investmentsnc, assets):
    base = _invnc_intensity(investmentsnc, assets)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PP&E 63d growth (capacity-build acceleration), 21d
def f30ab_f30_reserve_asset_base_ppgrowth_21d_slope_v009_signal(ppnenet):
    base = _growth(ppnenet, 63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PP&E 252d growth, 63d (annual-build velocity)
def f30ab_f30_reserve_asset_base_ppgrowth_63d_slope_v010_signal(ppnenet):
    base = _growth(ppnenet, 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of total-asset 63d growth, 21d (base-expansion acceleration)
def f30ab_f30_reserve_asset_base_assetgrowth_21d_slope_v011_signal(assets):
    base = _growth(assets, 63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of total-asset 252d growth, 63d
def f30ab_f30_reserve_asset_base_assetgrowth_63d_slope_v012_signal(assets):
    base = _growth(assets, 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tangible 63d growth, 21d (hard-reserve build acceleration)
def f30ab_f30_reserve_asset_base_tanggrowth_21d_slope_v013_signal(tangibles):
    base = _growth(tangibles, 63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tangible 252d growth, 63d
def f30ab_f30_reserve_asset_base_tanggrowth_63d_slope_v014_signal(tangibles):
    base = _growth(tangibles, 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of non-current investments 63d growth, 21d
def f30ab_f30_reserve_asset_base_invncgrowth_21d_slope_v015_signal(investmentsnc):
    base = _growth(investmentsnc, 63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-to-PP&E ratio (reinvestment-rate velocity), 21d
def f30ab_f30_reserve_asset_base_capexppe_21d_slope_v016_signal(capex, ppnenet):
    base = capex / ppnenet.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-to-PP&E ratio, 63d
def f30ab_f30_reserve_asset_base_capexppe_63d_slope_v017_signal(capex, ppnenet):
    base = capex / ppnenet.replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of invnc-to-PP&E ratio (financial-vs-physical reserve velocity), 21d
def f30ab_f30_reserve_asset_base_invncppe_21d_slope_v018_signal(investmentsnc, ppnenet):
    base = investmentsnc / ppnenet.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PP&E-within-tangibles share (physical-reserve concentration velocity), 21d
def f30ab_f30_reserve_asset_base_pptang_21d_slope_v019_signal(ppnenet, tangibles):
    base = ppnenet / tangibles.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PP&E-within-tangibles share, 63d
def f30ab_f30_reserve_asset_base_pptang_63d_slope_v020_signal(ppnenet, tangibles):
    base = ppnenet / tangibles.replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capital-base coverage of tangible base ((ppnenet+invnc)/tangibles), 21d
def f30ab_f30_reserve_asset_base_capbasecov_21d_slope_v021_signal(ppnenet, investmentsnc, tangibles):
    base = (ppnenet + investmentsnc) / tangibles.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capital-base intensity (ppnenet+invnc)/assets, 63d
def f30ab_f30_reserve_asset_base_capbaseint_63d_slope_v022_signal(ppnenet, investmentsnc, assets):
    base = (ppnenet + investmentsnc) / assets.replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tangible-base hard-asset intensity (ppnenet/tangibles smoothed), 63d
def f30ab_f30_reserve_asset_base_hardint_63d_slope_v023_signal(ppnenet, tangibles):
    base = (ppnenet / tangibles.replace(0, np.nan)).ewm(span=63, min_periods=21).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asset-intensity z-score (de-trended intensity velocity), 21d
def f30ab_f30_reserve_asset_base_assetintz_21d_slope_v024_signal(ppnenet, assets):
    base = _z(_asset_intensity(ppnenet, assets), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tangible-share z-score, 21d
def f30ab_f30_reserve_asset_base_tangsharez_21d_slope_v025_signal(tangibles, assets):
    base = _z(_tangible_share(tangibles, assets), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-intensity z-score (build-pace regime velocity), 21d
def f30ab_f30_reserve_asset_base_capexintz_21d_slope_v026_signal(capex, assets):
    base = _z(_capex_intensity(capex, assets), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asset-intensity EMA (persistent-intensity velocity), 63d
def f30ab_f30_reserve_asset_base_assetintema_63d_slope_v027_signal(ppnenet, assets):
    base = _asset_intensity(ppnenet, assets).ewm(span=126, min_periods=42).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log PP&E level (capacity-scale velocity), 63d
def f30ab_f30_reserve_asset_base_pplevel_63d_slope_v028_signal(ppnenet):
    base = np.log(ppnenet.replace(0, np.nan))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log asset level (base-scale velocity), 63d
def f30ab_f30_reserve_asset_base_assetlevel_63d_slope_v029_signal(assets):
    base = np.log(assets.replace(0, np.nan))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log tangible level, 63d
def f30ab_f30_reserve_asset_base_tanglevel_63d_slope_v030_signal(tangibles):
    base = np.log(tangibles.replace(0, np.nan))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-to-assets reinvestment rate (smoothed), 63d
def f30ab_f30_reserve_asset_base_reinvrate_63d_slope_v031_signal(capex, assets):
    base = (_mean(capex, 63) / assets.replace(0, np.nan))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of invnc-to-tangibles share (financial-depth velocity), 21d
def f30ab_f30_reserve_asset_base_invnctang_21d_slope_v032_signal(investmentsnc, tangibles):
    base = investmentsnc / tangibles.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex/(capex+invnc) build-mix (allocation velocity), 21d
def f30ab_f30_reserve_asset_base_buildmix_21d_slope_v033_signal(capex, investmentsnc):
    base = capex / (capex + investmentsnc).replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PP&E 1260d range position (cycle-phase velocity), 63d
def f30ab_f30_reserve_asset_base_ppcyc_63d_slope_v034_signal(ppnenet):
    hi = _rmax(ppnenet, 1260)
    lo = _rmin(ppnenet, 1260)
    base = (ppnenet - lo) / (hi - lo).replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asset 1260d range position, 63d
def f30ab_f30_reserve_asset_base_assetcyc_63d_slope_v035_signal(assets):
    hi = _rmax(assets, 1260)
    lo = _rmin(assets, 1260)
    base = (assets - lo) / (hi - lo).replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PP&E underwater fraction (time spent below trailing peak), 63d
def f30ab_f30_reserve_asset_base_ppuw_63d_slope_v036_signal(ppnenet):
    peak = _rmax(ppnenet, 504)
    under = (ppnenet < peak * 0.999).astype(float)
    base = under.rolling(252, min_periods=126).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asset-base drawdown depth relative to its own 252d typical depth, 63d
def f30ab_f30_reserve_asset_base_assetddrel_63d_slope_v037_signal(assets):
    peak = _rmax(assets, 1260)
    dd = assets / peak.replace(0, np.nan) - 1.0
    base = dd - _mean(dd, 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of physical-vs-financial growth spread (invnc gr - ppnenet gr), 63d
def f30ab_f30_reserve_asset_base_finphysspr_63d_slope_v038_signal(investmentsnc, ppnenet):
    base = _growth(investmentsnc, 252) - _growth(ppnenet, 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PP&E-minus-asset growth spread (capacity-led tilt velocity), 63d
def f30ab_f30_reserve_asset_base_ppvsassetspr_63d_slope_v039_signal(ppnenet, assets):
    base = _growth(ppnenet, 252) - _growth(assets, 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tangible-minus-asset growth spread, 63d
def f30ab_f30_reserve_asset_base_tangvsassetspr_63d_slope_v040_signal(tangibles, assets):
    base = _growth(tangibles, 252) - _growth(assets, 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asset-intensity 504d range position (intensity-cycle velocity), 63d
def f30ab_f30_reserve_asset_base_intpos_63d_slope_v041_signal(ppnenet, assets):
    ai = _asset_intensity(ppnenet, assets)
    hi = _rmax(ai, 504)
    lo = _rmin(ai, 504)
    base = (ai - lo) / (hi - lo).replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tangible-share 504d range position, 63d
def f30ab_f30_reserve_asset_base_tangpos_63d_slope_v042_signal(tangibles, assets):
    ts = _tangible_share(tangibles, assets)
    hi = _rmax(ts, 504)
    lo = _rmin(ts, 504)
    base = (ts - lo) / (hi - lo).replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex run-rate vs PP&E (reinvestment velocity), 21d
def f30ab_f30_reserve_asset_base_capexrr_21d_slope_v043_signal(capex, ppnenet):
    base = _mean(capex, 63) / ppnenet.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex deployment vs tangibles (hard-build velocity), 21d
def f30ab_f30_reserve_asset_base_capexdeploy_21d_slope_v044_signal(capex, tangibles):
    base = _mean(capex, 63) / _mean(tangibles, 63).replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of intangible-vs-PP&E share (intangible-weight velocity), 21d
def f30ab_f30_reserve_asset_base_intangppe_21d_slope_v045_signal(assets, tangibles, ppnenet):
    intang = (assets - tangibles).clip(lower=0.0)
    base = intang / ppnenet.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capital-base-vs-asset growth spread (reserve build vs broad base), 63d
def f30ab_f30_reserve_asset_base_capbasevsasset_63d_slope_v046_signal(ppnenet, investmentsnc, assets):
    cap = ppnenet + investmentsnc
    base = _growth(cap, 252) - _growth(assets, 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asset-intensity vs its 252d mean (relative-intensity velocity), 21d
def f30ab_f30_reserve_asset_base_intrel_21d_slope_v047_signal(ppnenet, assets):
    ai = _asset_intensity(ppnenet, assets)
    base = ai / _mean(ai, 252).replace(0, np.nan) - 1.0
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tangible-share displacement from EMA (hard-asset drift velocity), 21d
def f30ab_f30_reserve_asset_base_tangdisp_21d_slope_v048_signal(tangibles, assets):
    ts = _tangible_share(tangibles, assets)
    base = ts - ts.ewm(span=252, min_periods=63).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PP&E 504d growth (multi-year build velocity), 63d
def f30ab_f30_reserve_asset_base_ppgrowth504_63d_slope_v049_signal(ppnenet):
    base = _growth(ppnenet, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asset 504d growth, 63d
def f30ab_f30_reserve_asset_base_assetgrowth504_63d_slope_v050_signal(assets):
    base = _growth(assets, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-vs-invnc growth spread (build-source momentum), 21d
def f30ab_f30_reserve_asset_base_capexinvgrspr_21d_slope_v051_signal(capex, investmentsnc):
    base = _growth(_mean(capex, 63), 126) - _growth(investmentsnc, 126)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex run-rate to assets (deployment velocity), 21d
def f30ab_f30_reserve_asset_base_deploy_21d_slope_v052_signal(capex, assets):
    base = _mean(capex, 63) / assets.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of invnc-to-assets intensity vs its EMA (reserve-surge velocity), 21d
def f30ab_f30_reserve_asset_base_invncsurge_21d_slope_v053_signal(investmentsnc, assets):
    ii = _invnc_intensity(investmentsnc, assets)
    base = ii - ii.ewm(span=126, min_periods=42).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PP&E-to-assets intensity rank (intensity-percentile velocity), 21d
def f30ab_f30_reserve_asset_base_intrank_21d_slope_v054_signal(ppnenet, assets):
    base = _rank(_asset_intensity(ppnenet, assets), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tangible-share rank, 21d
def f30ab_f30_reserve_asset_base_tangrank_21d_slope_v055_signal(tangibles, assets):
    base = _rank(_tangible_share(tangibles, assets), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capital-base intensity vs tangible base (reserve-cover velocity), 63d
def f30ab_f30_reserve_asset_base_capbasetang_63d_slope_v056_signal(ppnenet, investmentsnc, tangibles):
    base = (ppnenet + investmentsnc) / tangibles.replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of build-balance (invnc int - capex int), 21d
def f30ab_f30_reserve_asset_base_buildbal_21d_slope_v057_signal(investmentsnc, capex, assets):
    base = _invnc_intensity(investmentsnc, assets) - _capex_intensity(capex, assets)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PP&E recovery off 504d trough (rebuild velocity), 63d
def f30ab_f30_reserve_asset_base_pprecov_63d_slope_v058_signal(ppnenet):
    trough = _rmin(ppnenet, 504)
    base = ppnenet / trough.replace(0, np.nan) - 1.0
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tangible recovery off 504d trough (hard-reserve rebuild velocity), 63d
def f30ab_f30_reserve_asset_base_tangrecov_63d_slope_v059_signal(tangibles):
    trough = _rmin(tangibles, 504)
    base = tangibles / trough.replace(0, np.nan) - 1.0
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of hard-reserve base growth ((ppnenet+tangibles)/2), 63d
def f30ab_f30_reserve_asset_base_hardbasegr_63d_slope_v060_signal(ppnenet, tangibles):
    hb = 0.5 * ppnenet + 0.5 * tangibles
    base = _growth(hb, 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-vs-invnc growth spread, 63d
def f30ab_f30_reserve_asset_base_capexinvgrspr_63d_slope_v061_signal(capex, investmentsnc):
    cum = _mean(capex, 63)
    base = _growth(investmentsnc, 252) - _growth(cum, 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PP&E-within-tangibles z-score, 21d
def f30ab_f30_reserve_asset_base_pptangz_21d_slope_v062_signal(ppnenet, tangibles):
    base = _z(ppnenet / tangibles.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of invnc-to-assets intensity z-score, 21d
def f30ab_f30_reserve_asset_base_invncz_21d_slope_v063_signal(investmentsnc, assets):
    base = _z(_invnc_intensity(investmentsnc, assets), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex burst (qcapex vs typical), 21d
def f30ab_f30_reserve_asset_base_capexburst_21d_slope_v064_signal(capex):
    qcapex = _mean(capex, 63)
    typ = qcapex.rolling(504, min_periods=252).mean()
    base = qcapex / typ.replace(0, np.nan) - 1.0
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of reinvestment-rate z (reinvestment-regime velocity), 21d
def f30ab_f30_reserve_asset_base_reinvz_21d_slope_v065_signal(capex, ppnenet):
    rr = _mean(capex, 252) / ppnenet.replace(0, np.nan)
    base = _z(rr, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asset-intensity term structure (short mean - long mean), 21d
def f30ab_f30_reserve_asset_base_intterm_21d_slope_v066_signal(ppnenet, assets):
    ai = _asset_intensity(ppnenet, assets)
    base = _mean(ai, 63) - _mean(ai, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tangible-share term structure, 21d
def f30ab_f30_reserve_asset_base_tangterm_21d_slope_v067_signal(tangibles, assets):
    ts = _tangible_share(tangibles, assets)
    base = _mean(ts, 63) - _mean(ts, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-intensity term structure, 21d
def f30ab_f30_reserve_asset_base_capexterm_21d_slope_v068_signal(capex, assets):
    ci = _capex_intensity(capex, assets)
    base = _mean(ci, 63) - _mean(ci, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of physical-reserve dominance log(ppnenet/invnc), 21d
def f30ab_f30_reserve_asset_base_ppperinv_21d_slope_v069_signal(ppnenet, investmentsnc):
    base = np.log(ppnenet.replace(0, np.nan) / investmentsnc.replace(0, np.nan))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-to-PP&E rank (reinvestment-percentile velocity), 21d
def f30ab_f30_reserve_asset_base_capexpperank_21d_slope_v070_signal(capex, ppnenet):
    base = _rank(capex / ppnenet.replace(0, np.nan), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of reserve-outlay tilt vs tangibles (invnc - capex run-rate, over tangibles), 21d
def f30ab_f30_reserve_asset_base_outlaytilt_21d_slope_v071_signal(investmentsnc, capex, tangibles):
    base = (investmentsnc - _mean(capex, 63)) / tangibles.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capital-base 252d growth, 63d
def f30ab_f30_reserve_asset_base_capbasegr_63d_slope_v072_signal(ppnenet, investmentsnc):
    cap = ppnenet + investmentsnc
    base = _growth(cap, 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tangible drawdown from 1260d peak, 63d
def f30ab_f30_reserve_asset_base_tangdd_63d_slope_v073_signal(tangibles):
    peak = _rmax(tangibles, 1260)
    base = tangibles / peak.replace(0, np.nan) - 1.0
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asset-intensity gap from EMA in std units, 21d
def f30ab_f30_reserve_asset_base_intgap_21d_slope_v074_signal(ppnenet, assets):
    ai = _asset_intensity(ppnenet, assets)
    gap = ai - ai.ewm(span=126, min_periods=42).mean()
    base = gap / _std(ai, 252).replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tangible-share gap from EMA in std units, 21d
def f30ab_f30_reserve_asset_base_tanggap_21d_slope_v075_signal(tangibles, assets):
    ts = _tangible_share(tangibles, assets)
    gap = ts - ts.ewm(span=126, min_periods=42).mean()
    base = gap / _std(ts, 252).replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asset intensity, 5d (fast capacity-intensity velocity)
def f30ab_f30_reserve_asset_base_assetint_5d_slope_v076_signal(ppnenet, assets):
    base = _asset_intensity(ppnenet, assets)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tangible share, 5d
def f30ab_f30_reserve_asset_base_tangshare_5d_slope_v077_signal(tangibles, assets):
    base = _tangible_share(tangibles, assets)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex intensity, 5d
def f30ab_f30_reserve_asset_base_capexint_5d_slope_v078_signal(capex, assets):
    base = _capex_intensity(capex, assets)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of invnc intensity, 5d
def f30ab_f30_reserve_asset_base_invncint_5d_slope_v079_signal(investmentsnc, assets):
    base = _invnc_intensity(investmentsnc, assets)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PP&E 126d growth, 21d (half-year build velocity)
def f30ab_f30_reserve_asset_base_ppgrowth126_21d_slope_v080_signal(ppnenet):
    base = _growth(ppnenet, 126)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asset 126d growth, 21d
def f30ab_f30_reserve_asset_base_assetgrowth126_21d_slope_v081_signal(assets):
    base = _growth(assets, 126)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tangible 126d growth, 21d
def f30ab_f30_reserve_asset_base_tanggrowth126_21d_slope_v082_signal(tangibles):
    base = _growth(tangibles, 126)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of invnc 252d growth, 63d
def f30ab_f30_reserve_asset_base_invncgrowth252_63d_slope_v083_signal(investmentsnc):
    base = _growth(investmentsnc, 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-to-assets cumulative-vs-base ratio (smoothed), 63d
def f30ab_f30_reserve_asset_base_capexassets_63d_slope_v084_signal(capex, assets):
    base = (_mean(capex, 252) / assets.replace(0, np.nan))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PP&E-within-tangibles change-rate, 63d
def f30ab_f30_reserve_asset_base_pptangchg_63d_slope_v085_signal(ppnenet, tangibles):
    sh = ppnenet / tangibles.replace(0, np.nan)
    base = sh - sh.shift(126)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of build-mix instability (std of capex/(capex+invnc)), 21d
def f30ab_f30_reserve_asset_base_buildmixvol_21d_slope_v086_signal(capex, investmentsnc):
    mix = capex / (capex + investmentsnc).replace(0, np.nan)
    base = _std(mix, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asset-intensity dispersion (mix instability), 21d
def f30ab_f30_reserve_asset_base_intdisp_21d_slope_v087_signal(ppnenet, assets):
    base = _std(_asset_intensity(ppnenet, assets), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-intensity dispersion (lumpy-build velocity), 21d
def f30ab_f30_reserve_asset_base_capexdisp_21d_slope_v088_signal(capex, assets):
    base = _std(_capex_intensity(capex, assets), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PP&E build-momentum ratio (tanh short-minus-long growth), 21d
def f30ab_f30_reserve_asset_base_ppmomratio_21d_slope_v089_signal(ppnenet):
    base = np.tanh(_growth(ppnenet, 63) * 8.0 - _growth(ppnenet, 504))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asset growth acceleration (g252 vs g252 a year ago), 63d
def f30ab_f30_reserve_asset_base_assetgraccel_63d_slope_v090_signal(assets):
    g = _growth(assets, 252)
    base = g - g.shift(252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex coverage of asset growth, 63d
def f30ab_f30_reserve_asset_base_capexcover_63d_slope_v091_signal(capex, assets):
    cum = _mean(capex, 252)
    delta = (assets - assets.shift(252)).clip(lower=0.0)
    base = (cum / delta.replace(0, np.nan)).clip(upper=20.0)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex run-rate vs invnc rank, 21d
def f30ab_f30_reserve_asset_base_capexinvrank_21d_slope_v092_signal(capex, investmentsnc):
    rr = _mean(capex, 63) / investmentsnc.replace(0, np.nan)
    base = _rank(rr, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PP&E distance above its 252d mean (capacity-stretch velocity), 63d
def f30ab_f30_reserve_asset_base_ppstretch_63d_slope_v093_signal(ppnenet):
    base = ppnenet / _mean(ppnenet, 252).replace(0, np.nan) - 1.0
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asset-base underbuild fraction, 63d
def f30ab_f30_reserve_asset_base_uwfrac_63d_slope_v094_signal(assets):
    peak = _rmax(assets, 504)
    under = (assets < peak * 0.999).astype(float)
    base = under.rolling(504, min_periods=252).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of intensity peak-distance (room below peak intensity), 63d
def f30ab_f30_reserve_asset_base_intpeakdist_63d_slope_v095_signal(ppnenet, assets):
    ai = _asset_intensity(ppnenet, assets)
    peak = _rmax(ai, 504)
    base = ai / peak.replace(0, np.nan) - 1.0
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex peak-distance, 63d
def f30ab_f30_reserve_asset_base_capexpeakdist_63d_slope_v096_signal(capex, assets):
    ci = _capex_intensity(capex, assets)
    peak = _rmax(ci, 504)
    base = ci / peak.replace(0, np.nan) - 1.0
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of hard-base intensity displacement, 21d
def f30ab_f30_reserve_asset_base_hardbasedisp_21d_slope_v097_signal(ppnenet, tangibles, assets):
    hb = 0.5 * ppnenet + 0.5 * tangibles
    hi = hb / assets.replace(0, np.nan)
    base = hi - hi.ewm(span=252, min_periods=63).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of intensity-vs-tangible rank spread, 21d
def f30ab_f30_reserve_asset_base_intvstangrank_21d_slope_v098_signal(ppnenet, tangibles, assets):
    base = (_rank(_asset_intensity(ppnenet, assets), 504)
            - _rank(_tangible_share(tangibles, assets), 504))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-vs-invnc rank spread, 21d
def f30ab_f30_reserve_asset_base_capexvsinvrank_21d_slope_v099_signal(capex, investmentsnc, assets):
    base = (_rank(_capex_intensity(capex, assets), 504)
            - _rank(_invnc_intensity(investmentsnc, assets), 504))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of risk-adjusted asset growth, 63d
def f30ab_f30_reserve_asset_base_riskadjgr_63d_slope_v100_signal(assets):
    g63 = _growth(assets, 63)
    base = (_growth(assets, 252) / _std(g63, 252).replace(0, np.nan)).clip(-50.0, 50.0)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of risk-adjusted PP&E growth, 63d
def f30ab_f30_reserve_asset_base_ppriskadjgr_63d_slope_v101_signal(ppnenet):
    g63 = _growth(ppnenet, 63)
    base = (_growth(ppnenet, 252) / _std(g63, 252).replace(0, np.nan)).clip(-50.0, 50.0)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PP&E growth stability (mean/std), 63d
def f30ab_f30_reserve_asset_base_ppgrstab_63d_slope_v102_signal(ppnenet):
    g = _growth(ppnenet, 63)
    base = _mean(g, 252) / _std(g, 252).replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asset growth stability, 63d
def f30ab_f30_reserve_asset_base_assetgrstab_63d_slope_v103_signal(assets):
    g = _growth(assets, 63)
    base = _mean(g, 252) / _std(g, 252).replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex run-rate growth (build-pace acceleration), 21d
def f30ab_f30_reserve_asset_base_capexrrgr_21d_slope_v104_signal(capex, assets):
    rr = _mean(capex, 63) / assets.replace(0, np.nan)
    base = rr - rr.shift(126)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tangible-base cover of combined build outlay, 21d
def f30ab_f30_reserve_asset_base_tangcoverbuild_21d_slope_v105_signal(tangibles, capex, investmentsnc):
    outlay = _mean(capex, 63) + investmentsnc
    base = np.log1p((tangibles / outlay.replace(0, np.nan)).clip(lower=0))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PP&E cover of annual capex, 63d
def f30ab_f30_reserve_asset_base_ppcovercapex_63d_slope_v106_signal(ppnenet, capex):
    base = (ppnenet / _mean(capex, 252).replace(0, np.nan)).clip(upper=100.0)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-to-invnc-flow rank, 21d
def f30ab_f30_reserve_asset_base_capexflowrank_21d_slope_v107_signal(capex, investmentsnc):
    base = _rank(_mean(capex, 63) / investmentsnc.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of magnitude-weighted expansion breadth, 21d
def f30ab_f30_reserve_asset_base_expandbreadth_21d_slope_v108_signal(ppnenet, assets, tangibles):
    g1 = np.tanh(6.0 * _growth(ppnenet, 252))
    g2 = np.tanh(6.0 * _growth(assets, 252))
    g3 = np.tanh(6.0 * _growth(tangibles, 252))
    base = (g1 + g2 + g3) / 3.0
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of growth-centroid displacement, 21d
def f30ab_f30_reserve_asset_base_growthcentroid_21d_slope_v109_signal(ppnenet, assets, tangibles):
    mean_g = (_growth(ppnenet, 252) + _growth(assets, 252) + _growth(tangibles, 252)) / 3.0
    base = mean_g - mean_g.ewm(span=252, min_periods=63).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cross-asset growth dispersion, 21d
def f30ab_f30_reserve_asset_base_growthdisp_21d_slope_v110_signal(ppnenet, assets, tangibles):
    g1 = _growth(ppnenet, 252)
    g2 = _growth(assets, 252)
    g3 = _growth(tangibles, 252)
    base = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asset-mix dispersion (intensity disagreement), 21d
def f30ab_f30_reserve_asset_base_mixdisp_21d_slope_v111_signal(ppnenet, tangibles, investmentsnc, assets):
    a1 = _asset_intensity(ppnenet, assets)
    a2 = _tangible_share(tangibles, assets)
    a3 = _invnc_intensity(investmentsnc, assets)
    base = pd.concat([a1, a2, a3], axis=1).std(axis=1)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PP&E 252d growth detrended by EMA, 21d
def f30ab_f30_reserve_asset_base_ppgrdetrend_21d_slope_v112_signal(ppnenet):
    g = _growth(ppnenet, 252)
    base = g - g.ewm(span=252, min_periods=63).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asset 252d growth detrended by EMA, 21d
def f30ab_f30_reserve_asset_base_assetgrdetrend_21d_slope_v113_signal(assets):
    g = _growth(assets, 252)
    base = g - g.ewm(span=252, min_periods=63).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tangible-vs-PP&E momentum spread (z gt - z gp), 21d
def f30ab_f30_reserve_asset_base_tangppmom_21d_slope_v114_signal(tangibles, ppnenet):
    base = _z(_growth(tangibles, 252), 504) - _z(_growth(ppnenet, 252), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of invnc contribution to capital-base growth, 21d
def f30ab_f30_reserve_asset_base_invnccontrib_21d_slope_v115_signal(ppnenet, investmentsnc):
    d_inv = investmentsnc - investmentsnc.shift(252)
    d_cap = (ppnenet + investmentsnc) - (ppnenet + investmentsnc).shift(252)
    base = (d_inv / d_cap.replace(0, np.nan)).clip(-3.0, 3.0)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex acceleration (annual run-rate vs prior year), 63d
def f30ab_f30_reserve_asset_base_capexaccel_63d_slope_v116_signal(capex):
    rr = _mean(capex, 252)
    base = np.log(rr.replace(0, np.nan) / rr.shift(252).replace(0, np.nan))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asset-intensity convexity, 21d
def f30ab_f30_reserve_asset_base_intconvex_21d_slope_v117_signal(ppnenet, assets):
    ai = _asset_intensity(ppnenet, assets)
    dev = ai - _mean(ai, 252)
    base = np.sign(dev) * (dev ** 2) * 100.0
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tangible-share convexity, 21d
def f30ab_f30_reserve_asset_base_tangconvex_21d_slope_v118_signal(tangibles, assets):
    ts = _tangible_share(tangibles, assets)
    dev = ts - _mean(ts, 252)
    base = np.sign(dev) * (dev ** 2) * 100.0
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PP&E intensity vs assets stability (mean/std), 63d
def f30ab_f30_reserve_asset_base_intstab_63d_slope_v119_signal(ppnenet, assets):
    ai = _asset_intensity(ppnenet, assets)
    base = _mean(ai, 504) / _std(ai, 504).replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tangible-share stability, 63d
def f30ab_f30_reserve_asset_base_tangstab_63d_slope_v120_signal(tangibles, assets):
    ts = _tangible_share(tangibles, assets)
    base = _mean(ts, 504) / _std(ts, 504).replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-funded asset growth coverage (504d), 63d
def f30ab_f30_reserve_asset_base_capexfund_63d_slope_v121_signal(capex, assets):
    cum = _mean(capex, 504)
    delta = (assets - assets.shift(504)).clip(lower=0.0)
    base = (cum / delta.replace(0, np.nan)).clip(upper=20.0)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of invnc-funded asset growth (504d), 63d
def f30ab_f30_reserve_asset_base_invfund_63d_slope_v122_signal(investmentsnc, assets):
    d_inv = investmentsnc - investmentsnc.shift(504)
    delta = assets - assets.shift(504)
    base = (d_inv / delta.replace(0, np.nan)).clip(-10.0, 10.0)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tangible-weighted asset growth, 21d
def f30ab_f30_reserve_asset_base_tangwtgr_21d_slope_v123_signal(assets, tangibles):
    g = _growth(assets, 252)
    tsr = _rank(_tangible_share(tangibles, assets), 504)
    base = g * (tsr + 0.5)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capacity-weighted asset growth, 21d
def f30ab_f30_reserve_asset_base_capwtgr_21d_slope_v124_signal(assets, ppnenet):
    g = _growth(assets, 252)
    air = _rank(_asset_intensity(ppnenet, assets), 504)
    base = g * (air + 0.5)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asset-intensity z momentum, 21d
def f30ab_f30_reserve_asset_base_intzmom_21d_slope_v125_signal(ppnenet, assets):
    zz = _z(_asset_intensity(ppnenet, assets), 252)
    base = zz - zz.shift(63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tangible-share z momentum, 21d
def f30ab_f30_reserve_asset_base_tangzmom_21d_slope_v126_signal(tangibles, assets):
    zz = _z(_tangible_share(tangibles, assets), 252)
    base = zz - zz.shift(63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of financial-vs-physical growth spread z, 21d
def f30ab_f30_reserve_asset_base_finvsphysz_21d_slope_v127_signal(investmentsnc, ppnenet):
    base = _z(_growth(investmentsnc, 252) - _growth(ppnenet, 252), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of deployment-rate (smoothed annual capex/assets), 21d
def f30ab_f30_reserve_asset_base_deployrate_21d_slope_v128_signal(capex, assets):
    base = (_mean(capex, 252) / assets.replace(0, np.nan)).ewm(span=126, min_periods=42).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of intangible-asset base growth (non-tangible reserve velocity), 63d
def f30ab_f30_reserve_asset_base_intanggr_63d_slope_v129_signal(tangibles, assets):
    intang = (assets - tangibles).clip(lower=1.0)
    base = _growth(intang, 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capital-base intensity rank, 21d
def f30ab_f30_reserve_asset_base_capbaserank_21d_slope_v130_signal(ppnenet, investmentsnc, assets):
    base = _rank((ppnenet + investmentsnc) / assets.replace(0, np.nan), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PP&E 21d momentum within range, 21d
def f30ab_f30_reserve_asset_base_pprng_21d_slope_v131_signal(ppnenet):
    hi = _rmax(ppnenet, 504)
    lo = _rmin(ppnenet, 504)
    base = (ppnenet - lo) / (hi - lo).replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asset 21d momentum within range, 21d
def f30ab_f30_reserve_asset_base_assetrng_21d_slope_v132_signal(assets):
    hi = _rmax(assets, 504)
    lo = _rmin(assets, 504)
    base = (assets - lo) / (hi - lo).replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-intensity percentile rank (build-pace percentile velocity), 21d
def f30ab_f30_reserve_asset_base_capexintrank_21d_slope_v133_signal(capex, assets):
    base = _rank(_capex_intensity(capex, assets), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of invnc-intensity percentile rank (reserve-accumulation percentile velocity), 21d
def f30ab_f30_reserve_asset_base_invncintrank_21d_slope_v134_signal(investmentsnc, assets):
    base = _rank(_invnc_intensity(investmentsnc, assets), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PP&E build-direction persistence, 63d
def f30ab_f30_reserve_asset_base_ppdirpersist_63d_slope_v135_signal(ppnenet):
    chg = np.sign(ppnenet - ppnenet.shift(63))
    base = chg.rolling(504, min_periods=252).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of intensity-rising month count, 63d
def f30ab_f30_reserve_asset_base_intupcnt_63d_slope_v136_signal(ppnenet, assets):
    ai = _asset_intensity(ppnenet, assets)
    up = (ai > ai.shift(21)).astype(float)
    base = up.rolling(252, min_periods=126).sum()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex-burst count, 63d
def f30ab_f30_reserve_asset_base_capexburstcnt_63d_slope_v137_signal(capex):
    qcapex = _mean(capex, 63)
    typ = qcapex.rolling(252, min_periods=126).mean()
    burst = (qcapex > 1.3 * typ).astype(float)
    base = burst.rolling(504, min_periods=252).sum()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PP&E short-term build trend (63d change in 21d mean of log PP&E), 21d
def f30ab_f30_reserve_asset_base_ppshorttrend_21d_slope_v138_signal(ppnenet):
    lp = np.log(ppnenet.replace(0, np.nan))
    sm = _mean(lp, 21)
    base = sm - sm.shift(63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asset linear-trend proxy, 21d
def f30ab_f30_reserve_asset_base_assettrend_21d_slope_v139_signal(assets):
    la = np.log(assets.replace(0, np.nan))
    sm = _mean(la, 63)
    base = sm - sm.shift(252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tangible linear-trend proxy, 21d
def f30ab_f30_reserve_asset_base_tangtrend_21d_slope_v140_signal(tangibles):
    lt = np.log(tangibles.replace(0, np.nan))
    sm = _mean(lt, 63)
    base = sm - sm.shift(252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of reserve-build composite (ranked gr + ranked capex int), 21d
def f30ab_f30_reserve_asset_base_buildcomposite_21d_slope_v141_signal(ppnenet, capex, assets):
    gr = _rank(_growth(ppnenet, 252), 504)
    ci = _rank(_capex_intensity(capex, assets), 504)
    base = gr + 0.5 * ci
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of financial-reserve composite (ranked invnc gr + ranked invnc int), 21d
def f30ab_f30_reserve_asset_base_fincomposite_21d_slope_v142_signal(investmentsnc, assets):
    gr = _rank(_growth(investmentsnc, 252), 504)
    ii = _rank(_invnc_intensity(investmentsnc, assets), 504)
    base = gr + ii
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PP&E-within-tangibles detrended rank, 21d
def f30ab_f30_reserve_asset_base_pptangdetr_21d_slope_v143_signal(ppnenet, tangibles):
    sh = ppnenet / tangibles.replace(0, np.nan)
    detr = sh - sh.ewm(span=504, min_periods=126).mean()
    base = _rank(detr, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asset-intensity detrended rank, 21d
def f30ab_f30_reserve_asset_base_intdetr_21d_slope_v144_signal(ppnenet, assets):
    ai = _asset_intensity(ppnenet, assets)
    detr = ai - ai.ewm(span=504, min_periods=126).mean()
    base = _rank(detr, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of tangible-share detrended rank, 21d
def f30ab_f30_reserve_asset_base_tangdetr_21d_slope_v145_signal(tangibles, assets):
    ts = _tangible_share(tangibles, assets)
    detr = ts - ts.ewm(span=504, min_periods=126).mean()
    base = _rank(detr, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asset-base maturity (cycle pos x intensity rank), 63d
def f30ab_f30_reserve_asset_base_maturity_63d_slope_v146_signal(assets, ppnenet):
    hi = _rmax(assets, 1260)
    lo = _rmin(assets, 1260)
    pos = (assets - lo) / (hi - lo).replace(0, np.nan)
    air = _rank(_asset_intensity(ppnenet, assets), 504) + 0.5
    base = pos * air
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of PP&E span ratio (1260d high vs 252d low) — multi-year reserve range, 63d
def f30ab_f30_reserve_asset_base_ppspan_63d_slope_v147_signal(ppnenet):
    hi = _rmax(ppnenet, 1260)
    lo = _rmin(ppnenet, 252)
    base = np.log(hi.replace(0, np.nan) / lo.replace(0, np.nan))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cumulative-capex-to-PP&E (gross investment intensity), 63d
def f30ab_f30_reserve_asset_base_cumcapexppe_63d_slope_v148_signal(capex, ppnenet):
    base = _mean(capex, 252) / ppnenet.replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of capex build-mix detrended from EMA (allocation-shift velocity), 21d
def f30ab_f30_reserve_asset_base_buildmixdetr_21d_slope_v149_signal(capex, investmentsnc):
    mix = capex / (capex + investmentsnc).replace(0, np.nan)
    base = mix - mix.ewm(span=252, min_periods=63).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of financial-vs-physical intensity ratio (invnc int / capex int), 21d
def f30ab_f30_reserve_asset_base_finphysint_21d_slope_v150_signal(investmentsnc, capex, assets):
    base = (_invnc_intensity(investmentsnc, assets)
            / _capex_intensity(capex, assets).replace(0, np.nan))
    base = base.clip(upper=50.0)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f30ab_f30_reserve_asset_base_assetint_21d_slope_v001_signal,
    f30ab_f30_reserve_asset_base_assetint_63d_slope_v002_signal,
    f30ab_f30_reserve_asset_base_tangshare_21d_slope_v003_signal,
    f30ab_f30_reserve_asset_base_tangshare_63d_slope_v004_signal,
    f30ab_f30_reserve_asset_base_capexint_21d_slope_v005_signal,
    f30ab_f30_reserve_asset_base_capexint_63d_slope_v006_signal,
    f30ab_f30_reserve_asset_base_invncint_21d_slope_v007_signal,
    f30ab_f30_reserve_asset_base_invncint_63d_slope_v008_signal,
    f30ab_f30_reserve_asset_base_ppgrowth_21d_slope_v009_signal,
    f30ab_f30_reserve_asset_base_ppgrowth_63d_slope_v010_signal,
    f30ab_f30_reserve_asset_base_assetgrowth_21d_slope_v011_signal,
    f30ab_f30_reserve_asset_base_assetgrowth_63d_slope_v012_signal,
    f30ab_f30_reserve_asset_base_tanggrowth_21d_slope_v013_signal,
    f30ab_f30_reserve_asset_base_tanggrowth_63d_slope_v014_signal,
    f30ab_f30_reserve_asset_base_invncgrowth_21d_slope_v015_signal,
    f30ab_f30_reserve_asset_base_capexppe_21d_slope_v016_signal,
    f30ab_f30_reserve_asset_base_capexppe_63d_slope_v017_signal,
    f30ab_f30_reserve_asset_base_invncppe_21d_slope_v018_signal,
    f30ab_f30_reserve_asset_base_pptang_21d_slope_v019_signal,
    f30ab_f30_reserve_asset_base_pptang_63d_slope_v020_signal,
    f30ab_f30_reserve_asset_base_capbasecov_21d_slope_v021_signal,
    f30ab_f30_reserve_asset_base_capbaseint_63d_slope_v022_signal,
    f30ab_f30_reserve_asset_base_hardint_63d_slope_v023_signal,
    f30ab_f30_reserve_asset_base_assetintz_21d_slope_v024_signal,
    f30ab_f30_reserve_asset_base_tangsharez_21d_slope_v025_signal,
    f30ab_f30_reserve_asset_base_capexintz_21d_slope_v026_signal,
    f30ab_f30_reserve_asset_base_assetintema_63d_slope_v027_signal,
    f30ab_f30_reserve_asset_base_pplevel_63d_slope_v028_signal,
    f30ab_f30_reserve_asset_base_assetlevel_63d_slope_v029_signal,
    f30ab_f30_reserve_asset_base_tanglevel_63d_slope_v030_signal,
    f30ab_f30_reserve_asset_base_reinvrate_63d_slope_v031_signal,
    f30ab_f30_reserve_asset_base_invnctang_21d_slope_v032_signal,
    f30ab_f30_reserve_asset_base_buildmix_21d_slope_v033_signal,
    f30ab_f30_reserve_asset_base_ppcyc_63d_slope_v034_signal,
    f30ab_f30_reserve_asset_base_assetcyc_63d_slope_v035_signal,
    f30ab_f30_reserve_asset_base_ppuw_63d_slope_v036_signal,
    f30ab_f30_reserve_asset_base_assetddrel_63d_slope_v037_signal,
    f30ab_f30_reserve_asset_base_finphysspr_63d_slope_v038_signal,
    f30ab_f30_reserve_asset_base_ppvsassetspr_63d_slope_v039_signal,
    f30ab_f30_reserve_asset_base_tangvsassetspr_63d_slope_v040_signal,
    f30ab_f30_reserve_asset_base_intpos_63d_slope_v041_signal,
    f30ab_f30_reserve_asset_base_tangpos_63d_slope_v042_signal,
    f30ab_f30_reserve_asset_base_capexrr_21d_slope_v043_signal,
    f30ab_f30_reserve_asset_base_capexdeploy_21d_slope_v044_signal,
    f30ab_f30_reserve_asset_base_intangppe_21d_slope_v045_signal,
    f30ab_f30_reserve_asset_base_capbasevsasset_63d_slope_v046_signal,
    f30ab_f30_reserve_asset_base_intrel_21d_slope_v047_signal,
    f30ab_f30_reserve_asset_base_tangdisp_21d_slope_v048_signal,
    f30ab_f30_reserve_asset_base_ppgrowth504_63d_slope_v049_signal,
    f30ab_f30_reserve_asset_base_assetgrowth504_63d_slope_v050_signal,
    f30ab_f30_reserve_asset_base_capexinvgrspr_21d_slope_v051_signal,
    f30ab_f30_reserve_asset_base_deploy_21d_slope_v052_signal,
    f30ab_f30_reserve_asset_base_invncsurge_21d_slope_v053_signal,
    f30ab_f30_reserve_asset_base_intrank_21d_slope_v054_signal,
    f30ab_f30_reserve_asset_base_tangrank_21d_slope_v055_signal,
    f30ab_f30_reserve_asset_base_capbasetang_63d_slope_v056_signal,
    f30ab_f30_reserve_asset_base_buildbal_21d_slope_v057_signal,
    f30ab_f30_reserve_asset_base_pprecov_63d_slope_v058_signal,
    f30ab_f30_reserve_asset_base_tangrecov_63d_slope_v059_signal,
    f30ab_f30_reserve_asset_base_hardbasegr_63d_slope_v060_signal,
    f30ab_f30_reserve_asset_base_capexinvgrspr_63d_slope_v061_signal,
    f30ab_f30_reserve_asset_base_pptangz_21d_slope_v062_signal,
    f30ab_f30_reserve_asset_base_invncz_21d_slope_v063_signal,
    f30ab_f30_reserve_asset_base_capexburst_21d_slope_v064_signal,
    f30ab_f30_reserve_asset_base_reinvz_21d_slope_v065_signal,
    f30ab_f30_reserve_asset_base_intterm_21d_slope_v066_signal,
    f30ab_f30_reserve_asset_base_tangterm_21d_slope_v067_signal,
    f30ab_f30_reserve_asset_base_capexterm_21d_slope_v068_signal,
    f30ab_f30_reserve_asset_base_ppperinv_21d_slope_v069_signal,
    f30ab_f30_reserve_asset_base_capexpperank_21d_slope_v070_signal,
    f30ab_f30_reserve_asset_base_outlaytilt_21d_slope_v071_signal,
    f30ab_f30_reserve_asset_base_capbasegr_63d_slope_v072_signal,
    f30ab_f30_reserve_asset_base_tangdd_63d_slope_v073_signal,
    f30ab_f30_reserve_asset_base_intgap_21d_slope_v074_signal,
    f30ab_f30_reserve_asset_base_tanggap_21d_slope_v075_signal,
    f30ab_f30_reserve_asset_base_assetint_5d_slope_v076_signal,
    f30ab_f30_reserve_asset_base_tangshare_5d_slope_v077_signal,
    f30ab_f30_reserve_asset_base_capexint_5d_slope_v078_signal,
    f30ab_f30_reserve_asset_base_invncint_5d_slope_v079_signal,
    f30ab_f30_reserve_asset_base_ppgrowth126_21d_slope_v080_signal,
    f30ab_f30_reserve_asset_base_assetgrowth126_21d_slope_v081_signal,
    f30ab_f30_reserve_asset_base_tanggrowth126_21d_slope_v082_signal,
    f30ab_f30_reserve_asset_base_invncgrowth252_63d_slope_v083_signal,
    f30ab_f30_reserve_asset_base_capexassets_63d_slope_v084_signal,
    f30ab_f30_reserve_asset_base_pptangchg_63d_slope_v085_signal,
    f30ab_f30_reserve_asset_base_buildmixvol_21d_slope_v086_signal,
    f30ab_f30_reserve_asset_base_intdisp_21d_slope_v087_signal,
    f30ab_f30_reserve_asset_base_capexdisp_21d_slope_v088_signal,
    f30ab_f30_reserve_asset_base_ppmomratio_21d_slope_v089_signal,
    f30ab_f30_reserve_asset_base_assetgraccel_63d_slope_v090_signal,
    f30ab_f30_reserve_asset_base_capexcover_63d_slope_v091_signal,
    f30ab_f30_reserve_asset_base_capexinvrank_21d_slope_v092_signal,
    f30ab_f30_reserve_asset_base_ppstretch_63d_slope_v093_signal,
    f30ab_f30_reserve_asset_base_uwfrac_63d_slope_v094_signal,
    f30ab_f30_reserve_asset_base_intpeakdist_63d_slope_v095_signal,
    f30ab_f30_reserve_asset_base_capexpeakdist_63d_slope_v096_signal,
    f30ab_f30_reserve_asset_base_hardbasedisp_21d_slope_v097_signal,
    f30ab_f30_reserve_asset_base_intvstangrank_21d_slope_v098_signal,
    f30ab_f30_reserve_asset_base_capexvsinvrank_21d_slope_v099_signal,
    f30ab_f30_reserve_asset_base_riskadjgr_63d_slope_v100_signal,
    f30ab_f30_reserve_asset_base_ppriskadjgr_63d_slope_v101_signal,
    f30ab_f30_reserve_asset_base_ppgrstab_63d_slope_v102_signal,
    f30ab_f30_reserve_asset_base_assetgrstab_63d_slope_v103_signal,
    f30ab_f30_reserve_asset_base_capexrrgr_21d_slope_v104_signal,
    f30ab_f30_reserve_asset_base_tangcoverbuild_21d_slope_v105_signal,
    f30ab_f30_reserve_asset_base_ppcovercapex_63d_slope_v106_signal,
    f30ab_f30_reserve_asset_base_capexflowrank_21d_slope_v107_signal,
    f30ab_f30_reserve_asset_base_expandbreadth_21d_slope_v108_signal,
    f30ab_f30_reserve_asset_base_growthcentroid_21d_slope_v109_signal,
    f30ab_f30_reserve_asset_base_growthdisp_21d_slope_v110_signal,
    f30ab_f30_reserve_asset_base_mixdisp_21d_slope_v111_signal,
    f30ab_f30_reserve_asset_base_ppgrdetrend_21d_slope_v112_signal,
    f30ab_f30_reserve_asset_base_assetgrdetrend_21d_slope_v113_signal,
    f30ab_f30_reserve_asset_base_tangppmom_21d_slope_v114_signal,
    f30ab_f30_reserve_asset_base_invnccontrib_21d_slope_v115_signal,
    f30ab_f30_reserve_asset_base_capexaccel_63d_slope_v116_signal,
    f30ab_f30_reserve_asset_base_intconvex_21d_slope_v117_signal,
    f30ab_f30_reserve_asset_base_tangconvex_21d_slope_v118_signal,
    f30ab_f30_reserve_asset_base_intstab_63d_slope_v119_signal,
    f30ab_f30_reserve_asset_base_tangstab_63d_slope_v120_signal,
    f30ab_f30_reserve_asset_base_capexfund_63d_slope_v121_signal,
    f30ab_f30_reserve_asset_base_invfund_63d_slope_v122_signal,
    f30ab_f30_reserve_asset_base_tangwtgr_21d_slope_v123_signal,
    f30ab_f30_reserve_asset_base_capwtgr_21d_slope_v124_signal,
    f30ab_f30_reserve_asset_base_intzmom_21d_slope_v125_signal,
    f30ab_f30_reserve_asset_base_tangzmom_21d_slope_v126_signal,
    f30ab_f30_reserve_asset_base_finvsphysz_21d_slope_v127_signal,
    f30ab_f30_reserve_asset_base_deployrate_21d_slope_v128_signal,
    f30ab_f30_reserve_asset_base_intanggr_63d_slope_v129_signal,
    f30ab_f30_reserve_asset_base_capbaserank_21d_slope_v130_signal,
    f30ab_f30_reserve_asset_base_pprng_21d_slope_v131_signal,
    f30ab_f30_reserve_asset_base_assetrng_21d_slope_v132_signal,
    f30ab_f30_reserve_asset_base_capexintrank_21d_slope_v133_signal,
    f30ab_f30_reserve_asset_base_invncintrank_21d_slope_v134_signal,
    f30ab_f30_reserve_asset_base_ppdirpersist_63d_slope_v135_signal,
    f30ab_f30_reserve_asset_base_intupcnt_63d_slope_v136_signal,
    f30ab_f30_reserve_asset_base_capexburstcnt_63d_slope_v137_signal,
    f30ab_f30_reserve_asset_base_ppshorttrend_21d_slope_v138_signal,
    f30ab_f30_reserve_asset_base_assettrend_21d_slope_v139_signal,
    f30ab_f30_reserve_asset_base_tangtrend_21d_slope_v140_signal,
    f30ab_f30_reserve_asset_base_buildcomposite_21d_slope_v141_signal,
    f30ab_f30_reserve_asset_base_fincomposite_21d_slope_v142_signal,
    f30ab_f30_reserve_asset_base_pptangdetr_21d_slope_v143_signal,
    f30ab_f30_reserve_asset_base_intdetr_21d_slope_v144_signal,
    f30ab_f30_reserve_asset_base_tangdetr_21d_slope_v145_signal,
    f30ab_f30_reserve_asset_base_maturity_63d_slope_v146_signal,
    f30ab_f30_reserve_asset_base_ppspan_63d_slope_v147_signal,
    f30ab_f30_reserve_asset_base_cumcapexppe_63d_slope_v148_signal,
    f30ab_f30_reserve_asset_base_buildmixdetr_21d_slope_v149_signal,
    f30ab_f30_reserve_asset_base_finphysint_21d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_RESERVE_ASSET_BASE_REGISTRY_SLOPE_001_150 = REGISTRY


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

    assert n_features == 150, n_features
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

    print("OK f30_reserve_asset_base_2nd_derivatives_001_150_claude: %d features pass" % n_features)
