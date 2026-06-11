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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


# ===== folder domain primitives (capex / content spend magnitude & funding) =====
def _f27_spend(capex):
    # capex stored as cash outflow (negative); spend magnitude is the absolute value
    return capex.abs()


def _f27_intensity(capex, base):
    # spend intensity: capex magnitude per unit of a balance/flow base
    return _f27_spend(capex) / base.replace(0, np.nan)


def _f27_growth(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _f27_loggrowth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f27_invest_intensity(ncfi, base):
    # investing-cash outflow intensity: -ncfi (outflow positive) per unit base
    return (-ncfi) / base.replace(0, np.nan)


def _f27_capex_vs_depamor(capex, depamor):
    # growth-vs-maintenance content: capex spend relative to amortization/depreciation
    return _f27_spend(capex) / depamor.replace(0, np.nan)


# ============================================================
# capex/assets spend-intensity tilt: level minus its own long EMA (intensity vs trend)
def f27cx_f27_capex_content_spend_cxassetstilt_504d_base_v001_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    result = b - b.ewm(span=504, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets z-scored vs own 504d history (de-trended spend intensity)
def f27cx_f27_capex_content_spend_cxassetsz_504d_base_v002_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    result = _z(b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor: growth-vs-maintenance content spend, 252d smoothed level
def f27cx_f27_capex_content_spend_cxdep_252d_base_v003_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    result = _mean(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor tilt: ratio minus its own long EMA (growth/maintenance vs trend)
def f27cx_f27_capex_content_spend_cxdeptilt_504d_base_v004_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    result = b - b.ewm(span=504, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# capex/ppnenet: content/platform spend per unit of net property base, 252d
def f27cx_f27_capex_content_spend_cxppne_252d_base_v005_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    result = _mean(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/ppnenet z-scored vs own 252d history
def f27cx_f27_capex_content_spend_cxppnez_252d_base_v006_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# investing-cash intensity: -ncfi/assets (total investing outflow magnitude), 252d
def f27cx_f27_capex_content_spend_ncfiassets_252d_base_v007_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    result = _mean(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# investing-cash intensity z-scored vs own 504d history (de-trended)
def f27cx_f27_capex_content_spend_ncfiassetsz_504d_base_v008_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    result = _z(b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend growth over a year (content-spend cycle expansion)
def f27cx_f27_capex_content_spend_cxgrow_252d_base_v009_signal(capex):
    sp = _f27_spend(capex)
    result = _f27_growth(sp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend log-growth over a half-year
def f27cx_f27_capex_content_spend_cxloggrow_126d_base_v010_signal(capex):
    sp = _f27_spend(capex)
    result = _f27_loggrowth(sp, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex-burst: current spend vs its own trailing 252d average (spend surge ratio)
def f27cx_f27_capex_content_spend_cxburst_252d_base_v011_signal(capex):
    sp = _f27_spend(capex)
    result = sp / _mean(sp, 252).replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend coefficient of variation over 252d (content-spend lumpiness)
def f27cx_f27_capex_content_spend_cxcv_252d_base_v012_signal(capex):
    sp = _f27_spend(capex)
    result = _std(sp, 252) / _mean(sp, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# asset-vs-property base wedge: z-scored capex/assets minus z-scored capex/ppnenet
def f27cx_f27_capex_content_spend_cxbasewedge_252d_base_v013_signal(capex, assets, ppnenet):
    a = _f27_intensity(capex, assets)
    p = _f27_intensity(capex, ppnenet)
    result = _z(a, 252) - _z(p, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex-vs-depamor balance momentum: change over a quarter in (sp-d)/(sp+d)
def f27cx_f27_capex_content_spend_cxdepbalmom_63d_base_v014_signal(capex, depamor):
    sp = _f27_spend(capex)
    d = depamor
    bal = (sp - d) / (sp + d).replace(0, np.nan)
    result = bal - bal.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# non-capex investing share rank: (other investing / -ncfi) ranked vs own 504d history
def f27cx_f27_capex_content_spend_noncxinv_504d_base_v015_signal(ncfi, capex):
    out = (-ncfi)
    share = (out - _f27_spend(capex)) / out.replace(0, np.nan)
    result = _rank(share, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets percentile-ranked vs own 504d history (regime position)
def f27cx_f27_capex_content_spend_cxassetsrank_504d_base_v016_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    result = _rank(b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor percentile-ranked vs own 504d history
def f27cx_f27_capex_content_spend_cxdeprank_504d_base_v017_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    result = _rank(b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend acceleration-as-level: 126d growth minus prior 126d growth
def f27cx_f27_capex_content_spend_cxaccel_126d_base_v018_signal(capex):
    sp = _f27_spend(capex)
    g = _f27_growth(sp, 126)
    result = g - g.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# maintenance-share acceleration: 63d change of the 63d change in depamor/(depamor+capex)
def f27cx_f27_capex_content_spend_depcxshareaccel_63d_base_v019_signal(depamor, capex):
    sp = _f27_spend(capex)
    share = depamor / (depamor + sp).replace(0, np.nan)
    g = share - share.shift(63)
    result = g - g.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets short-vs-long spread (63d mean vs 252d mean) intensity momentum
def f27cx_f27_capex_content_spend_cxassetsspr_63v252_base_v020_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    result = _mean(b, 63) - _mean(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/ppnenet short-vs-long spread (content build vs property stock)
def f27cx_f27_capex_content_spend_cxppnespr_63v252_base_v021_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    result = _mean(b, 63) - _mean(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend share of investing outflow (capex/-ncfi), 252d level
def f27cx_f27_capex_content_spend_cxinvshare_252d_base_v022_signal(capex, ncfi):
    sp = _f27_spend(capex)
    out = (-ncfi)
    result = _mean(sp / out.replace(0, np.nan), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# net-investment intensity tilt: (capex - depamor)/assets minus its own long EMA
def f27cx_f27_capex_content_spend_netinvassets_504d_base_v023_signal(capex, depamor, assets):
    net = (_f27_spend(capex) - depamor) / assets.replace(0, np.nan)
    result = net - net.ewm(span=504, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets year-over-year change (spend-intensity drift)
def f27cx_f27_capex_content_spend_cxassetsyoy_252d_base_v024_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    result = b - b.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor year-over-year change (growth/maintenance tilt drift)
def f27cx_f27_capex_content_spend_cxdepyoy_252d_base_v025_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    result = b - b.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# investing-cash burn streak: fraction of last 252d with -ncfi above 252d median
def f27cx_f27_capex_content_spend_ncfistreak_252d_base_v026_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    med = b.rolling(252, min_periods=126).median()
    hot = (b > med).astype(float)
    result = hot.rolling(252, min_periods=126).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# capex-spend step magnitude: average absolute quarter-over-quarter spend jump in 252d
def f27cx_f27_capex_content_spend_cxstepmag_252d_base_v027_signal(capex):
    sp = _f27_spend(capex)
    step = (sp / sp.shift(63).replace(0, np.nan) - 1.0).abs()
    result = step.rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# capex/ppnenet vs capex/assets ratio (property concentration of spend), 252d
def f27cx_f27_capex_content_spend_cxconc_252d_base_v028_signal(capex, ppnenet, assets):
    p = _f27_intensity(capex, ppnenet)
    a = _f27_intensity(capex, assets)
    result = _mean(p / a.replace(0, np.nan), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# investing intensity minus capex intensity on assets (other-investing intensity)
def f27cx_f27_capex_content_spend_otherinv_252d_base_v029_signal(ncfi, capex, assets):
    inv = _f27_invest_intensity(ncfi, assets)
    cx = _f27_intensity(capex, assets)
    result = _mean(inv - cx, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor regime fraction: share of last 252d above its 504d median (build regime)
def f27cx_f27_capex_content_spend_cxdepregfrac_504d_base_v030_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    med = b.rolling(504, min_periods=252).median()
    above = (b > med).astype(float)
    result = above.rolling(252, min_periods=126).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue intensity z-scored vs own history (de-trended; aliases margin so z only)
def f27cx_f27_capex_content_spend_cxrevz_252d_base_v031_signal(capex, revenue):
    b = _f27_intensity(capex, revenue)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets convexity: signed-square distance from its 252d mean
def f27cx_f27_capex_content_spend_cxassetsconv_252d_base_v032_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    m = _mean(b, 252)
    d = b - m
    result = np.sign(d) * (d ** 2)
    return result.replace([np.inf, -np.inf], np.nan)


# investing-cash intensity short-vs-long spread (investing-cycle momentum)
def f27cx_f27_capex_content_spend_ncfispr_63v252_base_v033_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    result = _mean(b, 63) - _mean(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor displacement from its own slow EMA (growth/maintenance tilt pulse)
def f27cx_f27_capex_content_spend_cxdepdisp_ema_base_v034_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    result = b - b.ewm(span=189, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets displacement from its slow EMA (spend-intensity pulse)
def f27cx_f27_capex_content_spend_cxassetsdisp_252d_base_v035_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    result = b - b.ewm(span=189, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# content-spend cycle phase: capex 63d mean vs 252d mean (build vs trough)
def f27cx_f27_capex_content_spend_cxcycle_252d_base_v036_signal(capex):
    sp = _f27_spend(capex)
    result = _mean(sp, 63) / _mean(sp, 252).replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# net-content-investment vs ppnenet, percentile-ranked vs own 504d history (build regime)
def f27cx_f27_capex_content_spend_netinvppnerank_504d_base_v037_signal(capex, depamor, ppnenet):
    net = (_f27_spend(capex) - depamor) / ppnenet.replace(0, np.nan)
    result = _rank(net, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# investing-cash intensity year-over-year change (investing-cycle drift)
def f27cx_f27_capex_content_spend_ncfiyoy_252d_base_v038_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    result = b - b.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor dispersion (rolling std) over 252d (tilt instability)
def f27cx_f27_capex_content_spend_cxdepdisp_252d_base_v039_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    result = _std(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/ppnenet percentile-ranked vs own 504d history (property-build regime)
def f27cx_f27_capex_content_spend_cxppnerank_504d_base_v040_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    result = _rank(b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend burst rank: current spend vs 252d mean, percentile-ranked over 504d
def f27cx_f27_capex_content_spend_cxburstrank_504d_base_v041_signal(capex):
    sp = _f27_spend(capex)
    ratio = sp / _mean(sp, 252).replace(0, np.nan)
    result = _rank(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend half-year growth minus assets half-year growth (spend outpacing base)
def f27cx_f27_capex_content_spend_cxvsassetgrow_126d_base_v042_signal(capex, assets):
    sp = _f27_spend(capex)
    result = _f27_growth(sp, 126) - _f27_growth(assets, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ppnenet growth minus depamor growth (property-base build vs amortization pace)
def f27cx_f27_capex_content_spend_ppnevsdepgrow_252d_base_v043_signal(ppnenet, depamor):
    result = _f27_growth(ppnenet, 252) - _f27_growth(depamor, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# investing-vs-capex gap pulse: z-scored (-ncfi - capex spend) over ppnenet base
def f27cx_f27_capex_content_spend_invgap_252d_base_v044_signal(ncfi, capex, ppnenet):
    gap = ((-ncfi) - _f27_spend(capex)) / ppnenet.replace(0, np.nan)
    result = _z(gap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets regime distance from 504d median scaled by 252d std (intensity z-dist)
def f27cx_f27_capex_content_spend_cxassetszdist_504d_base_v045_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    med = b.rolling(504, min_periods=252).median()
    sd = _std(b, 252)
    result = (b - med) / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# build intensity vs stability: capex/depamor level divided by its 252d dispersion
def f27cx_f27_capex_content_spend_buildstab_252d_base_v046_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    result = _mean(b, 126) / _std(b, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend asymmetry: 252d mean minus 252d median scaled by std (skew proxy)
def f27cx_f27_capex_content_spend_cxasym_252d_base_v047_signal(capex):
    sp = _f27_spend(capex)
    m = _mean(sp, 252)
    med = sp.rolling(252, min_periods=126).median()
    sd = _std(sp, 252)
    result = (m - med) / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/ppnenet relative drift: one-year change scaled by current (property-build drift)
def f27cx_f27_capex_content_spend_cxppnereldrift_252d_base_v048_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    result = (b - b.shift(252)) / b.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend per ppnenet, change over a quarter (property-build momentum)
def f27cx_f27_capex_content_spend_cxppnemom_63d_base_v049_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# investing intensity convexity: signed square of -ncfi/assets distance from mean
def f27cx_f27_capex_content_spend_ncficonv_252d_base_v050_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    d = b - _mean(b, 252)
    result = np.sign(d) * (d ** 2)
    return result.replace([np.inf, -np.inf], np.nan)


# net-build dispersion: rolling std of (capex spend - depamor)/assets (build volatility)
def f27cx_f27_capex_content_spend_netbuildvol_252d_base_v051_signal(capex, depamor, assets):
    net = (_f27_spend(capex) - depamor) / assets.replace(0, np.nan)
    result = _std(net, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor log-ratio short vs long (multiplicative growth/maintenance tilt)
def f27cx_f27_capex_content_spend_cxdeplogspr_252d_base_v052_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    s = _mean(b, 63)
    l = _mean(b, 252)
    result = np.log(s.replace(0, np.nan) / l.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend drawdown: spend vs its own trailing 252d peak (spending pullback)
def f27cx_f27_capex_content_spend_cxdrawdown_252d_base_v053_signal(capex):
    sp = _f27_spend(capex)
    peak = _rmax(sp, 252)
    result = sp / peak.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend recovery: spend vs its own trailing 252d trough
def f27cx_f27_capex_content_spend_cxrecov_252d_base_v054_signal(capex):
    sp = _f27_spend(capex)
    trough = _rmin(sp, 252)
    result = sp / trough.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor band position within its 252d high-low range (build cycle pos)
def f27cx_f27_capex_content_spend_cxdeprngpos_252d_base_v055_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    hi = _rmax(b, 252)
    lo = _rmin(b, 252)
    result = (b - lo) / (hi - lo).replace(0, np.nan) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# investing-intensity pullback: -ncfi/assets headroom below its trailing 252d peak
def f27cx_f27_capex_content_spend_ncfipull_252d_base_v056_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    peak = _rmax(b, 252)
    result = b / peak.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# investing-cash intensity displacement from its slow EMA (investing posture pulse)
def f27cx_f27_capex_content_spend_ncfidisp_252d_base_v057_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    result = b - b.ewm(span=189, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend coefficient of variation over a half-year (short-cycle lumpiness)
def f27cx_f27_capex_content_spend_cxcv_126d_base_v058_signal(capex):
    sp = _f27_spend(capex)
    result = _std(sp, 126) / _mean(sp, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# net-build acceleration: half-year change in the net (capex-depamor)/assets level
def f27cx_f27_capex_content_spend_netbuildaccel_126d_base_v059_signal(capex, depamor, assets):
    net = (_f27_spend(capex) - depamor) / assets.replace(0, np.nan)
    g = net - net.shift(126)
    result = g - g.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/ppnenet displacement from its slow EMA (property-spend pulse)
def f27cx_f27_capex_content_spend_cxppnedisp_252d_base_v060_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    result = b - b.ewm(span=189, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets two-year drift (long content-spend intensity trend)
def f27cx_f27_capex_content_spend_cxassetsdrift_504d_base_v061_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    result = b - b.shift(504)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor tilt vs ppnenet base: z(capex/depamor) minus z(capex/ppnenet)
def f27cx_f27_capex_content_spend_cxdepppnez_252d_base_v062_signal(capex, depamor, ppnenet):
    d = _f27_capex_vs_depamor(capex, depamor)
    p = _f27_intensity(capex, ppnenet)
    result = _z(d, 252) - _z(p, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend directional consistency: net 252d log-change over total absolute path
def f27cx_f27_capex_content_spend_cxefficiency_252d_base_v063_signal(capex):
    sp = np.log(_f27_spend(capex).replace(0, np.nan))
    net = (sp - sp.shift(252)).abs()
    path = sp.diff().abs().rolling(252, min_periods=126).sum()
    result = net / path.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# investing-cash intensity rank vs own 504d history (investing regime position)
def f27cx_f27_capex_content_spend_ncfirank_504d_base_v064_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    result = _rank(b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# net-investment intensity vs assets, percentile-ranked vs own 504d history (build regime)
def f27cx_f27_capex_content_spend_netinvrank_504d_base_v065_signal(capex, depamor, assets):
    net = (_f27_spend(capex) - depamor) / assets.replace(0, np.nan)
    result = _rank(net, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor minus capex/assets (maintenance-relative vs scale-relative spend)
def f27cx_f27_capex_content_spend_cxdualbase_252d_base_v066_signal(capex, depamor, assets):
    d = _f27_capex_vs_depamor(capex, depamor)
    a = _f27_intensity(capex, assets)
    # de-trend each via z so the difference is scale-comparable
    result = _z(d, 252) - _z(a, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor trend: difference of its 126d mean now vs a quarter ago (build-tilt drift)
def f27cx_f27_capex_content_spend_cxdeptrend_252d_base_v067_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    sm = _mean(b, 126)
    result = sm - sm.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets stability: mean/std of intensity over 252d (steady-spend quality)
def f27cx_f27_capex_content_spend_cxassetsstab_252d_base_v068_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    result = _mean(b, 252) / _std(b, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# investing-vs-capex composition drift: non-capex investing share change over a year
def f27cx_f27_capex_content_spend_invcompdrift_252d_base_v069_signal(ncfi, capex):
    out = (-ncfi)
    sp = _f27_spend(capex)
    share = (out - sp) / out.replace(0, np.nan)
    result = share - share.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/ppnenet stability ratio (mean/std) over 252d (steady property-build)
def f27cx_f27_capex_content_spend_cxppnestab_252d_base_v070_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    result = _mean(b, 252) / _std(b, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets intensity vol-ratio: 63d std vs 252d std (spend-intensity vol regime)
def f27cx_f27_capex_content_spend_cxassetsvolratio_252d_base_v071_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    result = _std(b, 63) / _std(b, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# net-build vs ppnenet z-scored (de-trended growth-content net intensity)
def f27cx_f27_capex_content_spend_netinvppnez_252d_base_v072_signal(capex, depamor, ppnenet):
    net = (_f27_spend(capex) - depamor) / ppnenet.replace(0, np.nan)
    result = _z(net, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor convexity (signed square distance from its 252d mean)
def f27cx_f27_capex_content_spend_cxdepconv_252d_base_v073_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    d = b - _mean(b, 252)
    result = np.sign(d) * (d ** 2)
    return result.replace([np.inf, -np.inf], np.nan)


# investing intensity vs capex intensity divergence z (other-investing emphasis)
def f27cx_f27_capex_content_spend_invdivz_252d_base_v074_signal(ncfi, capex, assets):
    inv = _f27_invest_intensity(ncfi, assets)
    cx = _f27_intensity(capex, assets)
    result = _z(inv, 252) - _z(cx, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# investing-intensity fast vs slow EMA crossover (-ncfi/assets regime turn), bounded
def f27cx_f27_capex_content_spend_ncfixover_252d_base_v075_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    fast = b.ewm(span=63, min_periods=21).mean()
    slow = b.ewm(span=252, min_periods=63).mean()
    result = np.tanh((fast - slow) / slow.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f27cx_f27_capex_content_spend_cxassetstilt_504d_base_v001_signal,
    f27cx_f27_capex_content_spend_cxassetsz_504d_base_v002_signal,
    f27cx_f27_capex_content_spend_cxdep_252d_base_v003_signal,
    f27cx_f27_capex_content_spend_cxdeptilt_504d_base_v004_signal,
    f27cx_f27_capex_content_spend_cxppne_252d_base_v005_signal,
    f27cx_f27_capex_content_spend_cxppnez_252d_base_v006_signal,
    f27cx_f27_capex_content_spend_ncfiassets_252d_base_v007_signal,
    f27cx_f27_capex_content_spend_ncfiassetsz_504d_base_v008_signal,
    f27cx_f27_capex_content_spend_cxgrow_252d_base_v009_signal,
    f27cx_f27_capex_content_spend_cxloggrow_126d_base_v010_signal,
    f27cx_f27_capex_content_spend_cxburst_252d_base_v011_signal,
    f27cx_f27_capex_content_spend_cxcv_252d_base_v012_signal,
    f27cx_f27_capex_content_spend_cxbasewedge_252d_base_v013_signal,
    f27cx_f27_capex_content_spend_cxdepbalmom_63d_base_v014_signal,
    f27cx_f27_capex_content_spend_noncxinv_504d_base_v015_signal,
    f27cx_f27_capex_content_spend_cxassetsrank_504d_base_v016_signal,
    f27cx_f27_capex_content_spend_cxdeprank_504d_base_v017_signal,
    f27cx_f27_capex_content_spend_cxaccel_126d_base_v018_signal,
    f27cx_f27_capex_content_spend_depcxshareaccel_63d_base_v019_signal,
    f27cx_f27_capex_content_spend_cxassetsspr_63v252_base_v020_signal,
    f27cx_f27_capex_content_spend_cxppnespr_63v252_base_v021_signal,
    f27cx_f27_capex_content_spend_cxinvshare_252d_base_v022_signal,
    f27cx_f27_capex_content_spend_netinvassets_504d_base_v023_signal,
    f27cx_f27_capex_content_spend_cxassetsyoy_252d_base_v024_signal,
    f27cx_f27_capex_content_spend_cxdepyoy_252d_base_v025_signal,
    f27cx_f27_capex_content_spend_ncfistreak_252d_base_v026_signal,
    f27cx_f27_capex_content_spend_cxstepmag_252d_base_v027_signal,
    f27cx_f27_capex_content_spend_cxconc_252d_base_v028_signal,
    f27cx_f27_capex_content_spend_otherinv_252d_base_v029_signal,
    f27cx_f27_capex_content_spend_cxdepregfrac_504d_base_v030_signal,
    f27cx_f27_capex_content_spend_cxrevz_252d_base_v031_signal,
    f27cx_f27_capex_content_spend_cxassetsconv_252d_base_v032_signal,
    f27cx_f27_capex_content_spend_ncfispr_63v252_base_v033_signal,
    f27cx_f27_capex_content_spend_cxdepdisp_ema_base_v034_signal,
    f27cx_f27_capex_content_spend_cxassetsdisp_252d_base_v035_signal,
    f27cx_f27_capex_content_spend_cxcycle_252d_base_v036_signal,
    f27cx_f27_capex_content_spend_netinvppnerank_504d_base_v037_signal,
    f27cx_f27_capex_content_spend_ncfiyoy_252d_base_v038_signal,
    f27cx_f27_capex_content_spend_cxdepdisp_252d_base_v039_signal,
    f27cx_f27_capex_content_spend_cxppnerank_504d_base_v040_signal,
    f27cx_f27_capex_content_spend_cxburstrank_504d_base_v041_signal,
    f27cx_f27_capex_content_spend_cxvsassetgrow_126d_base_v042_signal,
    f27cx_f27_capex_content_spend_ppnevsdepgrow_252d_base_v043_signal,
    f27cx_f27_capex_content_spend_invgap_252d_base_v044_signal,
    f27cx_f27_capex_content_spend_cxassetszdist_504d_base_v045_signal,
    f27cx_f27_capex_content_spend_buildstab_252d_base_v046_signal,
    f27cx_f27_capex_content_spend_cxasym_252d_base_v047_signal,
    f27cx_f27_capex_content_spend_cxppnereldrift_252d_base_v048_signal,
    f27cx_f27_capex_content_spend_cxppnemom_63d_base_v049_signal,
    f27cx_f27_capex_content_spend_ncficonv_252d_base_v050_signal,
    f27cx_f27_capex_content_spend_netbuildvol_252d_base_v051_signal,
    f27cx_f27_capex_content_spend_cxdeplogspr_252d_base_v052_signal,
    f27cx_f27_capex_content_spend_cxdrawdown_252d_base_v053_signal,
    f27cx_f27_capex_content_spend_cxrecov_252d_base_v054_signal,
    f27cx_f27_capex_content_spend_cxdeprngpos_252d_base_v055_signal,
    f27cx_f27_capex_content_spend_ncfipull_252d_base_v056_signal,
    f27cx_f27_capex_content_spend_ncfidisp_252d_base_v057_signal,
    f27cx_f27_capex_content_spend_cxcv_126d_base_v058_signal,
    f27cx_f27_capex_content_spend_netbuildaccel_126d_base_v059_signal,
    f27cx_f27_capex_content_spend_cxppnedisp_252d_base_v060_signal,
    f27cx_f27_capex_content_spend_cxassetsdrift_504d_base_v061_signal,
    f27cx_f27_capex_content_spend_cxdepppnez_252d_base_v062_signal,
    f27cx_f27_capex_content_spend_cxefficiency_252d_base_v063_signal,
    f27cx_f27_capex_content_spend_ncfirank_504d_base_v064_signal,
    f27cx_f27_capex_content_spend_netinvrank_504d_base_v065_signal,
    f27cx_f27_capex_content_spend_cxdualbase_252d_base_v066_signal,
    f27cx_f27_capex_content_spend_cxdeptrend_252d_base_v067_signal,
    f27cx_f27_capex_content_spend_cxassetsstab_252d_base_v068_signal,
    f27cx_f27_capex_content_spend_invcompdrift_252d_base_v069_signal,
    f27cx_f27_capex_content_spend_cxppnestab_252d_base_v070_signal,
    f27cx_f27_capex_content_spend_cxassetsvolratio_252d_base_v071_signal,
    f27cx_f27_capex_content_spend_netinvppnez_252d_base_v072_signal,
    f27cx_f27_capex_content_spend_cxdepconv_252d_base_v073_signal,
    f27cx_f27_capex_content_spend_invdivz_252d_base_v074_signal,
    f27cx_f27_capex_content_spend_ncfixover_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_CAPEX_CONTENT_SPEND_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc",
        "opex", "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin",
        "netinc", "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps",
        "ncfo", "ncff", "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex",
        "depamor", "sharesbas", "shareswa", "shareswadil", "assets", "assetsc",
        "tangibles", "intangibles", "ppnenet", "investments", "inventory",
        "receivables", "payables", "equity", "retearn", "workingcapital", "debt",
        "debtc", "debtnc", "liabilities", "liabilitiesc", "cashneq", "currentratio",
        "roic", "roe", "roa", "ros", "assetturnover", "invcap", "intexp", "taxexp",
        "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield", "payoutratio",
        "prefdivis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
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

    # capex stored as negative cash outflow; build positive then negate
    capex = (-_fund(271, base=4.0e7, drift=0.030, vol=0.09)).rename("capex")
    revenue = _fund(272, base=1.5e8, drift=0.035, vol=0.08).rename("revenue")
    assets = _fund(273, base=8.0e8, drift=0.020, vol=0.05).rename("assets")
    ppnenet = _fund(274, base=2.0e8, drift=0.025, vol=0.06).rename("ppnenet")
    depamor = _fund(275, base=3.0e7, drift=0.022, vol=0.07).rename("depamor")
    ncfi = _fund(276, base=6.0e7, drift=0.028, vol=0.10, allow_neg=True).rename("ncfi")
    # ncfi is investing cash flow, typically negative (outflow); shift mostly negative
    ncfi = (ncfi - 8.0e7).rename("ncfi")

    cols = {"capex": capex, "revenue": revenue, "assets": assets,
            "ppnenet": ppnenet, "depamor": depamor, "ncfi": ncfi}

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

    print("OK f27_capex_content_spend_base_001_075_claude: %d features pass" % n_features)
