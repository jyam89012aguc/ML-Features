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
    return capex.abs()


def _f27_intensity(capex, base):
    return _f27_spend(capex) / base.replace(0, np.nan)


def _f27_growth(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _f27_loggrowth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f27_invest_intensity(ncfi, base):
    return (-ncfi) / base.replace(0, np.nan)


def _f27_capex_vs_depamor(capex, depamor):
    return _f27_spend(capex) / depamor.replace(0, np.nan)


# ============================================================
# capex/assets spend intensity, 126d smoothed level (half-year content intensity)
def f27cx_f27_capex_content_spend_cxassets126_base_v076_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    result = _mean(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor 126d smoothed level (half-year growth/maintenance ratio)
def f27cx_f27_capex_content_spend_cxdep126_base_v077_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    result = _mean(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/ppnenet 126d z-scored (de-trended half-year property-spend intensity)
def f27cx_f27_capex_content_spend_cxppnez126_base_v078_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# -ncfi/ppnenet investing intensity per property base, 252d level
def f27cx_f27_capex_content_spend_ncfippne_252d_base_v079_signal(ncfi, ppnenet):
    b = _f27_invest_intensity(ncfi, ppnenet)
    result = _mean(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# -ncfi/depamor investing intensity per amortization base, 252d z-scored (de-trended)
def f27cx_f27_capex_content_spend_ncfidepz_252d_base_v080_signal(ncfi, depamor):
    b = _f27_invest_intensity(ncfi, depamor)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend quarter-over-quarter growth (short content-spend momentum)
def f27cx_f27_capex_content_spend_cxgrow63_base_v081_signal(capex):
    sp = _f27_spend(capex)
    result = _f27_growth(sp, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend two-year log-growth (long content-spend trend)
def f27cx_f27_capex_content_spend_cxloggrow504_base_v082_signal(capex):
    sp = _f27_spend(capex)
    result = _f27_loggrowth(sp, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets year-over-year change ranked vs own 504d history (intensity-drift regime)
def f27cx_f27_capex_content_spend_cxassetsyoyrank_504d_base_v083_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    yoy = b - b.shift(252)
    result = _rank(yoy, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor minus its 126d mean, ranked vs own 252d history (build-tilt regime)
def f27cx_f27_capex_content_spend_cxdepmedtiltrank_252d_base_v084_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    tilt = b - _mean(b, 126)
    result = _rank(tilt, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend share of investing outflow (capex/-ncfi) z-scored (funding-mix tilt)
def f27cx_f27_capex_content_spend_cxinvsharez_252d_base_v085_signal(capex, ncfi):
    sp = _f27_spend(capex)
    out = (-ncfi)
    share = sp / out.replace(0, np.nan)
    result = _z(share, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/ppnenet half-year change minus quarter change (property-spend curvature)
def f27cx_f27_capex_content_spend_cxppnecurv_base_v086_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    result = (b - b.shift(126)) - (b - b.shift(63))
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend vs ppnenet growth gap (content build outpacing property base)
def f27cx_f27_capex_content_spend_cxvsppnegrow_126d_base_v087_signal(capex, ppnenet):
    sp = _f27_spend(capex)
    result = _f27_growth(sp, 126) - _f27_growth(ppnenet, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# other-investing per depamor: (-ncfi - capex spend)/depamor, z-scored (non-capex pace tilt)
def f27cx_f27_capex_content_spend_otherinvdepz_252d_base_v088_signal(ncfi, capex, depamor):
    other = ((-ncfi) - _f27_spend(capex)) / depamor.replace(0, np.nan)
    result = _z(other, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets convexity over a half-year window (intensity tail emphasis)
def f27cx_f27_capex_content_spend_cxassetsconv126_base_v089_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    d = b - _mean(b, 126)
    result = np.sign(d) * (d ** 2)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor regime fraction: share of 126d above its 252d median (build regime)
def f27cx_f27_capex_content_spend_cxdepregfrac_252d_base_v090_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    med = b.rolling(252, min_periods=126).median()
    above = (b > med).astype(float)
    result = above.rolling(126, min_periods=63).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend drawdown over a two-year peak (long content-spend pullback)
def f27cx_f27_capex_content_spend_cxdrawdown504_base_v091_signal(capex):
    sp = _f27_spend(capex)
    peak = _rmax(sp, 504)
    result = sp / peak.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend recovery over a two-year trough (long content-spend rebound)
def f27cx_f27_capex_content_spend_cxrecov504_base_v092_signal(capex):
    sp = _f27_spend(capex)
    trough = _rmin(sp, 504)
    result = sp / trough.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets band position within its 504d range (long intensity cycle position)
def f27cx_f27_capex_content_spend_cxassetsrngpos_504d_base_v093_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    hi = _rmax(b, 504)
    lo = _rmin(b, 504)
    result = (b - lo) / (hi - lo).replace(0, np.nan) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# -ncfi/assets band position within its 252d range (investing-cycle position)
def f27cx_f27_capex_content_spend_ncfirngpos_252d_base_v094_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    hi = _rmax(b, 252)
    lo = _rmin(b, 252)
    result = (b - lo) / (hi - lo).replace(0, np.nan) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor dispersion over a half-year (short build-tilt instability)
def f27cx_f27_capex_content_spend_cxdepdisp126_base_v095_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    result = _std(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend half-year coefficient-of-variation ranked vs own 504d history
def f27cx_f27_capex_content_spend_cxcvrank_504d_base_v096_signal(capex):
    sp = _f27_spend(capex)
    cv = _std(sp, 126) / _mean(sp, 126).replace(0, np.nan)
    result = _rank(cv, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend vs investing-outflow gap over depamor, 126d z-scored (funding-gap tilt)
def f27cx_f27_capex_content_spend_cxinvgapdepz_126d_base_v097_signal(capex, ncfi, depamor):
    gap = (_f27_spend(capex) - (-ncfi)) / depamor.replace(0, np.nan)
    result = _z(gap, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor displacement from its 252d EMA (medium growth/maintenance pulse)
def f27cx_f27_capex_content_spend_cxdepema252disp_base_v098_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    result = b - b.ewm(span=252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets intensity momentum: 63d change of capex/assets (short intensity ramp)
def f27cx_f27_capex_content_spend_cxassetsmom_63d_base_v099_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend year-over-year acceleration (252d growth now minus a year ago)
def f27cx_f27_capex_content_spend_cxgrowaccel_252d_base_v100_signal(capex):
    sp = _f27_spend(capex)
    g = _f27_growth(sp, 252)
    result = g - g.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# -ncfi/assets year-over-year acceleration (investing-cycle second difference)
def f27cx_f27_capex_content_spend_ncfiaccel_252d_base_v101_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    g = b - b.shift(126)
    result = g - g.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/ppnenet stability over a half-year (mean/std, steady property-build)
def f27cx_f27_capex_content_spend_cxppnestab126_base_v102_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    result = _mean(b, 126) / _std(b, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# -ncfi/assets crossover bounded: 21d EMA vs 126d EMA (fast investing-cycle turn)
def f27cx_f27_capex_content_spend_ncfifastturn_base_v103_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    fast = b.ewm(span=21, min_periods=10).mean()
    slow = b.ewm(span=126, min_periods=42).mean()
    result = np.tanh((fast - slow) / slow.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets rank vs own 252d history (medium intensity regime position)
def f27cx_f27_capex_content_spend_cxassetsrank_252d_base_v104_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    result = _rank(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# property-vs-scale spend tilt momentum: change over a quarter in z(cx/ppne) - z(cx/assets)
def f27cx_f27_capex_content_spend_cxppneassetmom_63d_base_v105_signal(capex, ppnenet, assets):
    p = _z(_f27_intensity(capex, ppnenet), 252)
    a = _z(_f27_intensity(capex, assets), 252)
    spread = p - a
    result = spread - spread.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# net-build (capex - depamor)/ppnenet ranked vs own 252d history (build regime, property)
def f27cx_f27_capex_content_spend_netinvppnerank_252d_base_v106_signal(capex, depamor, ppnenet):
    net = (_f27_spend(capex) - depamor) / ppnenet.replace(0, np.nan)
    result = _rank(net, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend skew-proxy over 126d (mean-median)/std (short lumpiness asymmetry)
def f27cx_f27_capex_content_spend_cxasym126_base_v107_signal(capex):
    sp = _f27_spend(capex)
    m = _mean(sp, 126)
    med = sp.rolling(126, min_periods=63).median()
    sd = _std(sp, 126)
    result = (m - med) / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets directional efficiency over 252d (net change over total path)
def f27cx_f27_capex_content_spend_cxassetseff_252d_base_v108_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    net = (b - b.shift(252)).abs()
    path = b.diff().abs().rolling(252, min_periods=126).sum()
    result = net / path.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# investing intensity dispersion over 252d (investing-program volatility)
def f27cx_f27_capex_content_spend_ncfidisp252_base_v109_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    result = _std(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# -ncfi/ppnenet pulse: investing intensity minus its 63d EMA (short property-fund pulse)
def f27cx_f27_capex_content_spend_ncfippnepulse_63d_base_v110_signal(ncfi, ppnenet):
    b = _f27_invest_intensity(ncfi, ppnenet)
    result = b - b.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend burst over a half-year mean, ranked vs own 252d history (surge regime)
def f27cx_f27_capex_content_spend_cxburstrank_252d_base_v111_signal(capex):
    sp = _f27_spend(capex)
    ratio = sp / _mean(sp, 126).replace(0, np.nan)
    result = _rank(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/ppnenet convexity (signed square distance from 252d mean)
def f27cx_f27_capex_content_spend_cxppneconv_252d_base_v112_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    d = b - _mean(b, 252)
    result = np.sign(d) * (d ** 2)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor excess-over-1 momentum: 63d change of the smoothed (capex/depamor - 1)
def f27cx_f27_capex_content_spend_cxdepexcessmom_63d_base_v113_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor) - 1.0
    sm = _mean(b, 126)
    result = sm - sm.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets two-year mean vs one-year mean (slow intensity regime shift)
def f27cx_f27_capex_content_spend_cxassetsregime_504d_base_v114_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    result = _mean(b, 252) - _mean(b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# -ncfi/assets minus its 504d mean (long investing-intensity tilt)
def f27cx_f27_capex_content_spend_ncfitilt_504d_base_v115_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    result = b - _mean(b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend log-level minus revenue log-level, half-year (spend scale vs sales; z-only)
def f27cx_f27_capex_content_spend_cxrevsizez_126d_base_v116_signal(capex, revenue):
    sp = np.log(_f27_spend(capex).replace(0, np.nan))
    rv = np.log(revenue.replace(0, np.nan))
    result = _z(sp - rv, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor rank vs own 252d history (medium build regime position)
def f27cx_f27_capex_content_spend_cxdeprank_252d_base_v117_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    result = _rank(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets acceleration: 126d-mean change now vs a half-year ago
def f27cx_f27_capex_content_spend_cxassetsaccel_126d_base_v118_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    sm = _mean(b, 126)
    g = sm - sm.shift(126)
    result = g - g.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/ppnenet displacement from its 63d EMA (short property-spend pulse)
def f27cx_f27_capex_content_spend_cxppnepulse_63d_base_v119_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    result = b - b.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# net-build (capex-depamor)/assets directional efficiency over 252d
def f27cx_f27_capex_content_spend_netinveff_252d_base_v120_signal(capex, depamor, assets):
    net = (_f27_spend(capex) - depamor) / assets.replace(0, np.nan)
    num = (net - net.shift(252)).abs()
    path = net.diff().abs().rolling(252, min_periods=126).sum()
    result = num / path.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend half-year growth minus quarter growth (growth-shape curvature)
def f27cx_f27_capex_content_spend_cxgrowshape_base_v121_signal(capex):
    sp = _f27_spend(capex)
    result = _f27_growth(sp, 126) - _f27_growth(sp, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor amplitude: 252d high-low range normalized by its mean (build cycle width)
def f27cx_f27_capex_content_spend_cxdepamp_252d_base_v122_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    hi = _rmax(b, 252)
    lo = _rmin(b, 252)
    result = (hi - lo) / _mean(b, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets amplitude: 252d high-low range normalized by mean (intensity cycle width)
def f27cx_f27_capex_content_spend_cxassetsamp_252d_base_v123_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    hi = _rmax(b, 252)
    lo = _rmin(b, 252)
    result = (hi - lo) / _mean(b, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend vs depamor: signed-root spread (bounded growth-vs-maintenance magnitude)
def f27cx_f27_capex_content_spend_cxdeproot_252d_base_v124_signal(capex, depamor):
    sp = _f27_spend(capex)
    d = depamor
    diff = (sp - d) / (sp + d).replace(0, np.nan)
    result = np.sign(diff) * (diff.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)


# investing vs capex emphasis over depamor base, z-scored (de-trended funding tilt)
def f27cx_f27_capex_content_spend_invcxdepz_252d_base_v125_signal(ncfi, capex, depamor):
    inv = _f27_invest_intensity(ncfi, depamor)
    cx = _f27_capex_vs_depamor(capex, depamor)
    result = _z(inv, 252) - _z(cx, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor half-year change minus quarter change (build-tilt curvature)
def f27cx_f27_capex_content_spend_cxdepcurv_base_v126_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    result = (b - b.shift(126)) - (b - b.shift(63))
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor 504d directional efficiency (long build-tilt consistency)
def f27cx_f27_capex_content_spend_cxdepeff_504d_base_v127_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    num = (b - b.shift(504)).abs()
    path = b.diff().abs().rolling(504, min_periods=252).sum()
    result = num / path.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend mean over a quarter vs over a year, ranked (build-phase regime)
def f27cx_f27_capex_content_spend_cxcyclerank_504d_base_v128_signal(capex):
    sp = _f27_spend(capex)
    cyc = _mean(sp, 63) / _mean(sp, 252).replace(0, np.nan)
    result = _rank(cyc, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# -ncfi/assets minus capex/assets, z-scored (other-investing emphasis pulse)
def f27cx_f27_capex_content_spend_otherinvz_252d_base_v129_signal(ncfi, capex, assets):
    inv = _f27_invest_intensity(ncfi, assets)
    cx = _f27_intensity(capex, assets)
    result = _z(inv - cx, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/ppnenet two-year drift (long property-spend intensity trend)
def f27cx_f27_capex_content_spend_cxppnedrift_504d_base_v130_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    result = b - b.shift(504)
    return result.replace([np.inf, -np.inf], np.nan)


# depamor/ppnenet amortization pace minus capex/ppnenet (maintenance vs build on property)
def f27cx_f27_capex_content_spend_amortbuildgap_252d_base_v131_signal(depamor, capex, ppnenet):
    amort = depamor / ppnenet.replace(0, np.nan)
    build = _f27_intensity(capex, ppnenet)
    result = _mean(amort - build, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets minus its 63d EMA (short intensity pulse)
def f27cx_f27_capex_content_spend_cxassetspulse_63d_base_v132_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    result = b - b.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend 126d burst persistence: avg deviation above 126d mean over a quarter
def f27cx_f27_capex_content_spend_cxburstpers126_base_v133_signal(capex):
    sp = _f27_spend(capex)
    dev = sp / _mean(sp, 126).replace(0, np.nan) - 1.0
    result = dev.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor 504d z-scored (long de-trended growth/maintenance level)
def f27cx_f27_capex_content_spend_cxdepz_504d_base_v134_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    result = _z(b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# investing-cash intensity 126d z-scored (de-trended medium investing intensity)
def f27cx_f27_capex_content_spend_ncfiz_126d_base_v135_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor growth vs capex/assets growth over a year (build-base divergence)
def f27cx_f27_capex_content_spend_cxdepvsassetintgrow_252d_base_v136_signal(capex, depamor, assets):
    d = _f27_capex_vs_depamor(capex, depamor)
    a = _f27_intensity(capex, assets)
    result = _f27_growth(d, 252) - _f27_growth(a, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/ppnenet regime fraction: share of 252d above its 504d median (property-build regime)
def f27cx_f27_capex_content_spend_cxppneregfrac_504d_base_v137_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    med = b.rolling(504, min_periods=252).median()
    above = (b > med).astype(float)
    result = above.rolling(252, min_periods=126).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend half-year drawdown (medium content-spend pullback)
def f27cx_f27_capex_content_spend_cxdrawdown126_base_v138_signal(capex):
    sp = _f27_spend(capex)
    peak = _rmax(sp, 126)
    result = sp / peak.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor band position within its 504d range (long build cycle position)
def f27cx_f27_capex_content_spend_cxdeprngpos_504d_base_v139_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    hi = _rmax(b, 504)
    lo = _rmin(b, 504)
    result = (b - lo) / (hi - lo).replace(0, np.nan) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets stability over a half-year (mean/std, steady-spend quality)
def f27cx_f27_capex_content_spend_cxassetsstab126_base_v140_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    result = _mean(b, 126) / _std(b, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# capex spend quarter-over-quarter step magnitude over 504d (long lumpiness)
def f27cx_f27_capex_content_spend_cxstepmag_504d_base_v141_signal(capex):
    sp = _f27_spend(capex)
    step = (sp / sp.shift(63).replace(0, np.nan) - 1.0).abs()
    result = step.rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# capex/-ncfi share rank vs own 252d history (medium funding-mix regime)
def f27cx_f27_capex_content_spend_cxinvsharerank_252d_base_v142_signal(capex, ncfi):
    sp = _f27_spend(capex)
    out = (-ncfi)
    share = sp / out.replace(0, np.nan)
    result = _rank(share, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor vs capex/assets cross-tilt momentum (change over a quarter)
def f27cx_f27_capex_content_spend_cxdualbasemom_63d_base_v143_signal(capex, depamor, assets):
    d = _z(_f27_capex_vs_depamor(capex, depamor), 252)
    a = _z(_f27_intensity(capex, assets), 252)
    spread = d - a
    result = spread - spread.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# -ncfi/assets minus its 126d mean (medium investing-intensity tilt)
def f27cx_f27_capex_content_spend_ncfimedtilt_126d_base_v144_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    result = b - _mean(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets bounded burst over 126d (tanh of intensity surge vs medium mean)
def f27cx_f27_capex_content_spend_cxassetsbursttanh126_base_v145_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    ratio = b / _mean(b, 126).replace(0, np.nan) - 1.0
    result = np.tanh(3.0 * ratio)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor amplitude ranked vs own 504d history (build-cycle-width regime)
def f27cx_f27_capex_content_spend_cxdepamprank_504d_base_v146_signal(capex, depamor):
    b = _f27_capex_vs_depamor(capex, depamor)
    amp = (_rmax(b, 252) - _rmin(b, 252)) / _mean(b, 252).replace(0, np.nan)
    result = _rank(amp, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# net-build (capex-depamor)/ppnenet minus its 504d mean (long net-build tilt)
def f27cx_f27_capex_content_spend_netinvppnetilt_504d_base_v147_signal(capex, depamor, ppnenet):
    net = (_f27_spend(capex) - depamor) / ppnenet.replace(0, np.nan)
    result = net - _mean(net, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets short-vs-medium log-spread (multiplicative intensity tilt 63 vs 126)
def f27cx_f27_capex_content_spend_cxassetslogspr_126d_base_v148_signal(capex, assets):
    b = _f27_intensity(capex, assets)
    s = _mean(b, 63)
    l = _mean(b, 126)
    result = np.log(s.replace(0, np.nan) / l.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# investing intensity directional efficiency over 252d (investing-program consistency)
def f27cx_f27_capex_content_spend_ncfieff_252d_base_v149_signal(ncfi, assets):
    b = _f27_invest_intensity(ncfi, assets)
    num = (b - b.shift(252)).abs()
    path = b.diff().abs().rolling(252, min_periods=126).sum()
    result = num / path.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/ppnenet 21d-vs-126d cycle phase (fast property-spend vs medium baseline)
def f27cx_f27_capex_content_spend_cxppnefastcycle_base_v150_signal(capex, ppnenet):
    b = _f27_intensity(capex, ppnenet)
    result = _mean(b, 21) / _mean(b, 126).replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f27cx_f27_capex_content_spend_cxassets126_base_v076_signal,
    f27cx_f27_capex_content_spend_cxdep126_base_v077_signal,
    f27cx_f27_capex_content_spend_cxppnez126_base_v078_signal,
    f27cx_f27_capex_content_spend_ncfippne_252d_base_v079_signal,
    f27cx_f27_capex_content_spend_ncfidepz_252d_base_v080_signal,
    f27cx_f27_capex_content_spend_cxgrow63_base_v081_signal,
    f27cx_f27_capex_content_spend_cxloggrow504_base_v082_signal,
    f27cx_f27_capex_content_spend_cxassetsyoyrank_504d_base_v083_signal,
    f27cx_f27_capex_content_spend_cxdepmedtiltrank_252d_base_v084_signal,
    f27cx_f27_capex_content_spend_cxinvsharez_252d_base_v085_signal,
    f27cx_f27_capex_content_spend_cxppnecurv_base_v086_signal,
    f27cx_f27_capex_content_spend_cxvsppnegrow_126d_base_v087_signal,
    f27cx_f27_capex_content_spend_otherinvdepz_252d_base_v088_signal,
    f27cx_f27_capex_content_spend_cxassetsconv126_base_v089_signal,
    f27cx_f27_capex_content_spend_cxdepregfrac_252d_base_v090_signal,
    f27cx_f27_capex_content_spend_cxdrawdown504_base_v091_signal,
    f27cx_f27_capex_content_spend_cxrecov504_base_v092_signal,
    f27cx_f27_capex_content_spend_cxassetsrngpos_504d_base_v093_signal,
    f27cx_f27_capex_content_spend_ncfirngpos_252d_base_v094_signal,
    f27cx_f27_capex_content_spend_cxdepdisp126_base_v095_signal,
    f27cx_f27_capex_content_spend_cxcvrank_504d_base_v096_signal,
    f27cx_f27_capex_content_spend_cxinvgapdepz_126d_base_v097_signal,
    f27cx_f27_capex_content_spend_cxdepema252disp_base_v098_signal,
    f27cx_f27_capex_content_spend_cxassetsmom_63d_base_v099_signal,
    f27cx_f27_capex_content_spend_cxgrowaccel_252d_base_v100_signal,
    f27cx_f27_capex_content_spend_ncfiaccel_252d_base_v101_signal,
    f27cx_f27_capex_content_spend_cxppnestab126_base_v102_signal,
    f27cx_f27_capex_content_spend_ncfifastturn_base_v103_signal,
    f27cx_f27_capex_content_spend_cxassetsrank_252d_base_v104_signal,
    f27cx_f27_capex_content_spend_cxppneassetmom_63d_base_v105_signal,
    f27cx_f27_capex_content_spend_netinvppnerank_252d_base_v106_signal,
    f27cx_f27_capex_content_spend_cxasym126_base_v107_signal,
    f27cx_f27_capex_content_spend_cxassetseff_252d_base_v108_signal,
    f27cx_f27_capex_content_spend_ncfidisp252_base_v109_signal,
    f27cx_f27_capex_content_spend_ncfippnepulse_63d_base_v110_signal,
    f27cx_f27_capex_content_spend_cxburstrank_252d_base_v111_signal,
    f27cx_f27_capex_content_spend_cxppneconv_252d_base_v112_signal,
    f27cx_f27_capex_content_spend_cxdepexcessmom_63d_base_v113_signal,
    f27cx_f27_capex_content_spend_cxassetsregime_504d_base_v114_signal,
    f27cx_f27_capex_content_spend_ncfitilt_504d_base_v115_signal,
    f27cx_f27_capex_content_spend_cxrevsizez_126d_base_v116_signal,
    f27cx_f27_capex_content_spend_cxdeprank_252d_base_v117_signal,
    f27cx_f27_capex_content_spend_cxassetsaccel_126d_base_v118_signal,
    f27cx_f27_capex_content_spend_cxppnepulse_63d_base_v119_signal,
    f27cx_f27_capex_content_spend_netinveff_252d_base_v120_signal,
    f27cx_f27_capex_content_spend_cxgrowshape_base_v121_signal,
    f27cx_f27_capex_content_spend_cxdepamp_252d_base_v122_signal,
    f27cx_f27_capex_content_spend_cxassetsamp_252d_base_v123_signal,
    f27cx_f27_capex_content_spend_cxdeproot_252d_base_v124_signal,
    f27cx_f27_capex_content_spend_invcxdepz_252d_base_v125_signal,
    f27cx_f27_capex_content_spend_cxdepcurv_base_v126_signal,
    f27cx_f27_capex_content_spend_cxdepeff_504d_base_v127_signal,
    f27cx_f27_capex_content_spend_cxcyclerank_504d_base_v128_signal,
    f27cx_f27_capex_content_spend_otherinvz_252d_base_v129_signal,
    f27cx_f27_capex_content_spend_cxppnedrift_504d_base_v130_signal,
    f27cx_f27_capex_content_spend_amortbuildgap_252d_base_v131_signal,
    f27cx_f27_capex_content_spend_cxassetspulse_63d_base_v132_signal,
    f27cx_f27_capex_content_spend_cxburstpers126_base_v133_signal,
    f27cx_f27_capex_content_spend_cxdepz_504d_base_v134_signal,
    f27cx_f27_capex_content_spend_ncfiz_126d_base_v135_signal,
    f27cx_f27_capex_content_spend_cxdepvsassetintgrow_252d_base_v136_signal,
    f27cx_f27_capex_content_spend_cxppneregfrac_504d_base_v137_signal,
    f27cx_f27_capex_content_spend_cxdrawdown126_base_v138_signal,
    f27cx_f27_capex_content_spend_cxdeprngpos_504d_base_v139_signal,
    f27cx_f27_capex_content_spend_cxassetsstab126_base_v140_signal,
    f27cx_f27_capex_content_spend_cxstepmag_504d_base_v141_signal,
    f27cx_f27_capex_content_spend_cxinvsharerank_252d_base_v142_signal,
    f27cx_f27_capex_content_spend_cxdualbasemom_63d_base_v143_signal,
    f27cx_f27_capex_content_spend_ncfimedtilt_126d_base_v144_signal,
    f27cx_f27_capex_content_spend_cxassetsbursttanh126_base_v145_signal,
    f27cx_f27_capex_content_spend_cxdepamprank_504d_base_v146_signal,
    f27cx_f27_capex_content_spend_netinvppnetilt_504d_base_v147_signal,
    f27cx_f27_capex_content_spend_cxassetslogspr_126d_base_v148_signal,
    f27cx_f27_capex_content_spend_ncfieff_252d_base_v149_signal,
    f27cx_f27_capex_content_spend_cxppnefastcycle_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_CAPEX_CONTENT_SPEND_REGISTRY_076_150 = REGISTRY


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

    capex = (-_fund(271, base=4.0e7, drift=0.030, vol=0.09)).rename("capex")
    revenue = _fund(272, base=1.5e8, drift=0.035, vol=0.08).rename("revenue")
    assets = _fund(273, base=8.0e8, drift=0.020, vol=0.05).rename("assets")
    ppnenet = _fund(274, base=2.0e8, drift=0.025, vol=0.06).rename("ppnenet")
    depamor = _fund(275, base=3.0e7, drift=0.022, vol=0.07).rename("depamor")
    ncfi = _fund(276, base=6.0e7, drift=0.028, vol=0.10, allow_neg=True)
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

    print("OK f27_capex_content_spend_base_076_150_claude: %d features pass" % n_features)
