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


def _roc(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _logroc(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


def _slope(s, w):
    # OLS slope of s over a trailing window, per-step (robust to short warm-up windows)
    def _f(a):
        m = len(a)
        idx = np.arange(m, dtype=float)
        xm = idx.mean()
        xden = ((idx - xm) ** 2).sum()
        if xden == 0:
            return np.nan
        return ((idx - xm) * (a - a.mean())).sum() / xden
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


# ===== folder domain primitives (intangible / content base & amortization) =====
def _f26_intang_share(intangibles, assets):
    return intangibles / assets.replace(0, np.nan)


def _f26_tang_share(tangibles, assets):
    return tangibles / assets.replace(0, np.nan)


def _f26_amort_pace(depamor, intangibles):
    return depamor / intangibles.replace(0, np.nan)


def _f26_amort_ppne(depamor, ppnenet):
    return depamor / ppnenet.replace(0, np.nan)


def _f26_intang_to_tang(intangibles, tangibles):
    return intangibles / tangibles.replace(0, np.nan)


def _f26_content_base(intangibles, ppnenet):
    return intangibles + ppnenet


def _f26_amort_aging(depamor, intangibles, ppnenet):
    return depamor / (intangibles + ppnenet).replace(0, np.nan)


# ============================================================
# OLS slope of intangibles/assets over a year (heaviness trend, per-step)
def f26ic_f26_intangible_content_base_heavyslope_252d_base_v076_signal(intangibles, assets):
    s = _f26_intang_share(intangibles, assets)
    b = _slope(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OLS slope of amortization pace over a year (aging trend)
def f26ic_f26_intangible_content_base_paceslope_252d_base_v077_signal(depamor, intangibles):
    s = _f26_amort_pace(depamor, intangibles)
    b = _slope(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OLS slope of log content base over half-year (content-build trend)
def f26ic_f26_intangible_content_base_baseslope_126d_base_v078_signal(intangibles, ppnenet):
    cb = np.log(_f26_content_base(intangibles, ppnenet).replace(0, np.nan))
    b = _slope(cb, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fast vs slow EMA crossover of intangible heaviness (tilt momentum)
def f26ic_f26_intangible_content_base_heavycross_base_v079_signal(intangibles, assets):
    s = _f26_intang_share(intangibles, assets)
    b = s.ewm(span=42, min_periods=21).mean() - s.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fast vs slow EMA crossover of amortization pace (pace momentum)
def f26ic_f26_intangible_content_base_pacecross_base_v080_signal(depamor, intangibles):
    s = _f26_amort_pace(depamor, intangibles)
    b = s.ewm(span=42, min_periods=21).mean() - s.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upside semi-deviation of intangible-share changes (asymmetric tilt expansion risk)
def f26ic_f26_intangible_content_base_heavyupsemi_252d_base_v081_signal(intangibles, assets):
    d = _f26_intang_share(intangibles, assets).diff()
    up = d.clip(lower=0)
    b = np.sqrt((up ** 2).rolling(252, min_periods=63).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside semi-deviation of intangible-share changes (tilt contraction risk)
def f26ic_f26_intangible_content_base_heavydnsemi_252d_base_v082_signal(intangibles, assets):
    d = _f26_intang_share(intangibles, assets).diff()
    dn = (-d).clip(lower=0)
    b = np.sqrt((dn ** 2).rolling(252, min_periods=63).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# semi-deviation skew of amortization pace (up vs down expensing volatility)
def f26ic_f26_intangible_content_base_paceskew_252d_base_v083_signal(depamor, intangibles):
    d = _f26_amort_pace(depamor, intangibles).diff()
    up = np.sqrt((d.clip(lower=0) ** 2).rolling(252, min_periods=63).mean())
    dn = np.sqrt(((-d).clip(lower=0) ** 2).rolling(252, min_periods=63).mean())
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net intangible tilt, sign x sqrt-magnitude of distance from its 504d median (compressed tilt extremity)
def f26ic_f26_intangible_content_base_nettiltsm_base_v084_signal(intangibles, tangibles, assets):
    raw = _f26_intang_share(intangibles, assets) - _f26_tang_share(tangibles, assets)
    dev = raw - raw.rolling(504, min_periods=126).median()
    b = np.sign(dev) * np.sqrt(dev.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content-base growth vs depamor-growth spread, smoothed (net build trend)
def f26ic_f26_intangible_content_base_netbuildsm_252d_base_v085_signal(intangibles, ppnenet, depamor):
    cb = _f26_content_base(intangibles, ppnenet)
    raw = _logroc(cb, 252) - _logroc(depamor, 252)
    b = raw.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization-burden acceleration z-scored vs its own 252d history (burden-bend extremity)
def f26ic_f26_intangible_content_base_burdenaccel_base_v086_signal(depamor, assets):
    s = depamor / assets.replace(0, np.nan)
    accel = s - 2.0 * s.shift(42) + s.shift(84)
    b = _z(accel, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentile-of-percentile: rank(intangible heaviness 504d) ranked again 252d (regime extremity)
def f26ic_f26_intangible_content_base_heavyrr_base_v087_signal(intangibles, assets):
    s = _f26_intang_share(intangibles, assets)
    r1 = s.rolling(504, min_periods=126).rank(pct=True)
    b = r1.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-share above-mean run intensity: run length x cumulative excess over the mean
def f26ic_f26_intangible_content_base_heavyrun_base_v088_signal(intangibles, assets):
    s = _f26_intang_share(intangibles, assets)
    excess = s - _mean(s, 252)
    up = (excess > 0).astype(float)
    grp = (up != up.shift(1)).cumsum()
    runlen = up.groupby(grp).cumsum()
    runmag = (excess.clip(lower=0)).groupby(grp).cumsum()
    b = runlen * runmag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization-pace rising-run intensity: run length x cumulative magnitude of the rises
def f26ic_f26_intangible_content_base_pacerun_base_v089_signal(depamor, intangibles):
    s = _f26_amort_pace(depamor, intangibles)
    d = s.diff()
    rise = (d > 0).astype(float)
    grp = (rise != rise.shift(1)).cumsum()
    runlen = rise.groupby(grp).cumsum()
    runmag = (d.clip(lower=0)).groupby(grp).cumsum()
    b = runlen * runmag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content out-investment sign x magnitude (signed sqrt of intangible-minus-asset growth)
def f26ic_f26_intangible_content_base_outinvestsm_252d_base_v090_signal(intangibles, assets):
    g = _logroc(intangibles, 252) - _logroc(assets, 252)
    b = np.sign(g) * np.sqrt(g.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangibles-within-physical-assets slope: tangibles/(tangibles+ppnenet) trend (per-step OLS, year)
def f26ic_f26_intangible_content_base_tangslope_252d_base_v091_signal(tangibles, ppnenet):
    s = tangibles / (tangibles + ppnenet).replace(0, np.nan)
    b = _slope(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-to-tangible log ratio slope (mix-shift trend)
def f26ic_f26_intangible_content_base_mixslope_252d_base_v092_signal(intangibles, tangibles):
    s = np.log(_f26_intang_to_tang(intangibles, tangibles).replace(0, np.nan))
    b = _slope(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization aging slope (depamor/(intang+ppne) trend over a year)
def f26ic_f26_intangible_content_base_agingslope_252d_base_v093_signal(depamor, intangibles, ppnenet):
    s = _f26_amort_aging(depamor, intangibles, ppnenet)
    b = _slope(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content-life curvature: 2nd diff of log implied content life over a quarter (aging bend)
def f26ic_f26_intangible_content_base_lifecurv_base_v094_signal(intangibles, depamor):
    life = np.log((intangibles / depamor.replace(0, np.nan)).replace(0, np.nan))
    b = life - 2.0 * life.shift(63) + life.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content-base intensity minus its slow EMA (productive-base displacement)
def f26ic_f26_intangible_content_base_intensitydisp_base_v095_signal(intangibles, ppnenet, assets):
    cb = _f26_content_base(intangibles, ppnenet)
    s = cb / assets.replace(0, np.nan)
    b = s - s.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content-base growth dispersion (rolling std of 63d log-growth, lumpiness of build)
def f26ic_f26_intangible_content_base_buildlumpiness_252d_base_v096_signal(intangibles, ppnenet):
    cb = _f26_content_base(intangibles, ppnenet)
    g = _logroc(cb, 63)
    b = _std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-growth lumpiness (std of quarterly intangible log-growth)
def f26ic_f26_intangible_content_base_intanglumpiness_252d_base_v097_signal(intangibles):
    g = _logroc(intangibles, 63)
    b = _std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# depamor lumpiness (std of quarterly depamor log-growth, expensing volatility)
def f26ic_f26_intangible_content_base_amortlumpiness_252d_base_v098_signal(depamor):
    g = _logroc(depamor, 63)
    b = _std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# heaviness vs its 1260d max (distance from peak content-tilt)
def f26ic_f26_intangible_content_base_heavyfrompeak_1260d_base_v099_signal(intangibles, assets):
    s = _f26_intang_share(intangibles, assets)
    hi = _rmax(s, 1260)
    b = s / hi.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization pace vs its 1260d max (distance from peak expensing)
def f26ic_f26_intangible_content_base_pacefrompeak_1260d_base_v100_signal(depamor, intangibles):
    s = _f26_amort_pace(depamor, intangibles)
    hi = _rmax(s, 1260)
    b = s / hi.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content-base intensity range position over 1260d (productive-base cycle position)
def f26ic_f26_intangible_content_base_intensitypos_1260d_base_v101_signal(intangibles, ppnenet, assets):
    cb = _f26_content_base(intangibles, ppnenet)
    s = cb / assets.replace(0, np.nan)
    hi = _rmax(s, 1260)
    lo = _rmin(s, 1260)
    b = (s - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible vs ppnenet log-ratio z-scored (content-library vs platform tilt anomaly)
def f26ic_f26_intangible_content_base_intang2ppnez_252d_base_v102_signal(intangibles, ppnenet):
    s = np.log((intangibles / ppnenet.replace(0, np.nan)).replace(0, np.nan))
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization burden EMA crossover (expensing-cycle momentum)
def f26ic_f26_intangible_content_base_burdencross_base_v103_signal(depamor, assets):
    s = depamor / assets.replace(0, np.nan)
    b = s.ewm(span=63, min_periods=21).mean() - s.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content-life vs platform-life log spread (content ages vs platform), smoothed
def f26ic_f26_intangible_content_base_lifespreadsm_base_v104_signal(intangibles, ppnenet):
    raw = np.log((intangibles / ppnenet.replace(0, np.nan)).replace(0, np.nan))
    b = raw.ewm(span=63, min_periods=21).mean() - raw
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year amortization-aging sits in its upper tercile (heavy-expensing regime)
def f26ic_f26_intangible_content_base_agingupper_252d_base_v105_signal(depamor, intangibles, ppnenet):
    s = _f26_amort_aging(depamor, intangibles, ppnenet)
    r = s.rolling(504, min_periods=126).rank(pct=True)
    upper = (r >= 0.6667).astype(float)
    b = upper.rolling(252, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# low-heaviness regime intensity: entry count plus average depth below the median (capitulation)
def f26ic_f26_intangible_content_base_heavylowentries_252d_base_v106_signal(intangibles, assets):
    s = _f26_intang_share(intangibles, assets)
    med = s.rolling(504, min_periods=126).median()
    low = (s < med * 0.9).astype(float)
    entries = ((low == 1) & (low.shift(1) == 0)).astype(float)
    rate = entries.rolling(252, min_periods=63).sum()
    depth = (med - s).clip(lower=0).rolling(63, min_periods=21).mean()
    b = rate + 50.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content out-investment x amortization-light interaction (clean reinvestment)
def f26ic_f26_intangible_content_base_cleanreinvest_base_v107_signal(intangibles, assets, depamor):
    grow = _logroc(intangibles, 252)
    pace = _f26_amort_pace(depamor, intangibles)
    b = grow * (1.0 - _z(pace, 252).clip(-3, 3) / 6.0 - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible content-base vs total assets, year-over-year log change of the ratio
def f26ic_f26_intangible_content_base_intensityyoy_252d_base_v108_signal(intangibles, ppnenet, assets):
    cb = _f26_content_base(intangibles, ppnenet)
    s = np.log((cb / assets.replace(0, np.nan)).replace(0, np.nan))
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible share range position over 1260d (physical-asset cycle position)
def f26ic_f26_intangible_content_base_tangpos_1260d_base_v109_signal(tangibles, assets):
    s = _f26_tang_share(tangibles, assets)
    hi = _rmax(s, 1260)
    lo = _rmin(s, 1260)
    b = (s - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net content investment proxy (intangible build minus expensing) z-scored
def f26ic_f26_intangible_content_base_netcontentz_252d_base_v110_signal(intangibles, depamor):
    grow = _logroc(intangibles, 252)
    pace = _f26_amort_pace(depamor, intangibles)
    raw = grow - pace
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year minus year intangible growth (build acceleration via horizon spread)
def f26ic_f26_intangible_content_base_growhorizon_base_v111_signal(intangibles):
    b = _logroc(intangibles, 126) - 0.5 * _logroc(intangibles, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization-pace horizon spread, EWM-smoothed (persistent expensing-acceleration tilt)
def f26ic_f26_intangible_content_base_pacehorizon_base_v112_signal(depamor, intangibles):
    s = _f26_amort_pace(depamor, intangibles)
    raw = (s - s.shift(63)) - 0.5 * (s - s.shift(126))
    b = raw.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content base / assets minus its 504d median, scaled by 504d std (intensity extremity)
def f26ic_f26_intangible_content_base_intensitystretch_504d_base_v113_signal(intangibles, ppnenet, assets):
    cb = _f26_content_base(intangibles, ppnenet)
    s = cb / assets.replace(0, np.nan)
    med = s.rolling(504, min_periods=126).median()
    sd = s.rolling(504, min_periods=126).std()
    b = (s - med) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization coverage of net content adds, smoothed (replenish-vs-expense balance)
def f26ic_f26_intangible_content_base_coveragesm_base_v114_signal(depamor, intangibles):
    add = (intangibles - intangibles.shift(126)).clip(lower=0)
    raw = depamor / add.replace(0, np.nan)
    b = np.log(raw.replace(0, np.nan)).ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-of-nontangible-assets z-scored (purity of intangible book ex tangibles)
def f26ic_f26_intangible_content_base_intangofnontangz_252d_base_v115_signal(intangibles, tangibles, assets):
    denom = (assets - tangibles).replace(0, np.nan)
    s = intangibles / denom
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# depamor-to-assets vs depamor-to-content-base spread (where amortization concentrates)
def f26ic_f26_intangible_content_base_amortconc_base_v116_signal(depamor, intangibles, ppnenet, assets):
    onassets = depamor / assets.replace(0, np.nan)
    onbase = _f26_amort_aging(depamor, intangibles, ppnenet)
    b = onbase - onassets
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content-base build acceleration: 2nd diff of log content base over a quarter
def f26ic_f26_intangible_content_base_baseaccel_base_v117_signal(intangibles, ppnenet):
    s = np.log(_f26_content_base(intangibles, ppnenet).replace(0, np.nan))
    b = s - 2.0 * s.shift(63) + s.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-vs-tangible log-mix dispersion: rolling std of the log mix-ratio (mix instability)
def f26ic_f26_intangible_content_base_sharemixz_252d_base_v118_signal(intangibles, tangibles):
    s = np.log(intangibles.replace(0, np.nan)) - np.log(tangibles.replace(0, np.nan))
    b = _std(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization pace efficiency: pace change per unit of content-base growth
def f26ic_f26_intangible_content_base_paceefficiency_base_v119_signal(depamor, intangibles, ppnenet):
    pace = _f26_amort_pace(depamor, intangibles)
    bg = _logroc(_f26_content_base(intangibles, ppnenet), 126)
    b = (pace - pace.shift(126)) / bg.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rolling correlation of intangibles vs depamor growth (do builds drive expensing?)
def f26ic_f26_intangible_content_base_buildexpensecorr_252d_base_v120_signal(intangibles, depamor):
    gi = _logroc(intangibles, 21)
    gd = _logroc(depamor, 21)
    b = gi.rolling(252, min_periods=126).corr(gd)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rolling correlation of intangible vs tangible growth (joint vs divergent investment)
def f26ic_f26_intangible_content_base_initangcorr_252d_base_v121_signal(intangibles, tangibles):
    gi = _logroc(intangibles, 21)
    gt = _logroc(tangibles, 21)
    b = gi.rolling(252, min_periods=126).corr(gt)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible share vs ppnenet share spread (content-library vs platform on the BS)
def f26ic_f26_intangible_content_base_libvsplatform_base_v122_signal(intangibles, ppnenet, assets):
    si = _f26_intang_share(intangibles, assets)
    sp = ppnenet / assets.replace(0, np.nan)
    raw = si - sp
    b = raw - raw.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization-aging acceleration, EWM-smoothed and ranked (persistent aging-bend regime, non-affine)
def f26ic_f26_intangible_content_base_agingaccel_base_v123_signal(depamor, intangibles, ppnenet):
    s = _f26_amort_aging(depamor, intangibles, ppnenet)
    curv = (s - 2.0 * s.shift(42) + s.shift(84)).ewm(span=63, min_periods=21).mean()
    b = _rank(curv, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content-base growth minus tangible growth (productive vs physical reinvestment gap)
def f26ic_f26_intangible_content_base_basevstang_252d_base_v124_signal(intangibles, ppnenet, tangibles):
    cb = _f26_content_base(intangibles, ppnenet)
    b = _logroc(cb, 252) - _logroc(tangibles, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied content life percentile vs 1260d history (aging regime, multi-year)
def f26ic_f26_intangible_content_base_liferank_1260d_base_v125_signal(intangibles, depamor):
    life = intangibles / depamor.replace(0, np.nan)
    b = _rank(life, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# heaviness short-vs-long momentum spread: 21d move minus 126d move per day (tilt acceleration)
def f26ic_f26_intangible_content_base_heavymomadj_base_v126_signal(intangibles, assets):
    s = _f26_intang_share(intangibles, assets)
    fast = (s - s.shift(21)) / 21.0
    slow = (s - s.shift(126)) / 126.0
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-share convexity (signed squared deviation from 252d mean, tilt extremity)
def f26ic_f26_intangible_content_base_heavyconvex_base_v127_signal(intangibles, assets):
    s = _f26_intang_share(intangibles, assets)
    dev = s - _mean(s, 252)
    sd = _std(s, 252).replace(0, np.nan)
    z = dev / sd
    b = np.sign(z) * (z ** 2)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization-burden percentile of 252d vs 504d (short vs long expensing regime gap)
def f26ic_f26_intangible_content_base_burdenregimegap_base_v128_signal(depamor, assets):
    s = depamor / assets.replace(0, np.nan)
    r_short = s.rolling(252, min_periods=63).rank(pct=True)
    r_long = s.rolling(504, min_periods=126).rank(pct=True)
    b = r_short - r_long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year intangible share rising (content-tilt persistence)
def f26ic_f26_intangible_content_base_heavyuptime_252d_base_v129_signal(intangibles, assets):
    s = _f26_intang_share(intangibles, assets)
    up = (s.diff() > 0).astype(float)
    b = up.rolling(252, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content base / depamor (whole productive-base life), de-trended vs 252d mean
def f26ic_f26_intangible_content_base_baselife_base_v130_signal(intangibles, ppnenet, depamor):
    cb = _f26_content_base(intangibles, ppnenet)
    life = cb / depamor.replace(0, np.nan)
    b = life / _mean(life, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-to-content-base ratio (physical vs productive content), log z
def f26ic_f26_intangible_content_base_tang2basez_252d_base_v131_signal(tangibles, intangibles, ppnenet):
    cb = _f26_content_base(intangibles, ppnenet)
    s = np.log((tangibles / cb.replace(0, np.nan)).replace(0, np.nan))
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content-vs-BS expensing co-movement: rolling 252d correlation of amort-pace and amort-burden changes
def f26ic_f26_intangible_content_base_pacevsburden_base_v132_signal(depamor, intangibles, assets):
    pace = _f26_amort_pace(depamor, intangibles)
    burden = depamor / assets.replace(0, np.nan)
    b = pace.diff().rolling(252, min_periods=126).corr(burden.diff())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of amortization burden over half-year (expensing trend, per-step)
def f26ic_f26_intangible_content_base_burdenslope_126d_base_v133_signal(depamor, assets):
    s = depamor / assets.replace(0, np.nan)
    b = _slope(s, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content-base intensity acceleration, z-scored vs its own 252d history (intensity-bend extremity)
def f26ic_f26_intangible_content_base_intensityaccel_base_v134_signal(intangibles, ppnenet, assets):
    cb = _f26_content_base(intangibles, ppnenet)
    s = cb / assets.replace(0, np.nan)
    accel = s - 2.0 * s.shift(42) + s.shift(84)
    b = _z(accel, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-to-tangible mix vs its 1260d median (multi-year mix-regime distance)
def f26ic_f26_intangible_content_base_mixdist_1260d_base_v135_signal(intangibles, tangibles):
    r = np.log(_f26_intang_to_tang(intangibles, tangibles).replace(0, np.nan))
    med = r.rolling(1260, min_periods=252).median()
    b = r - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization-pace vol-of-vol (instability of expensing volatility)
def f26ic_f26_intangible_content_base_pacevov_base_v136_signal(depamor, intangibles):
    s = _f26_amort_pace(depamor, intangibles)
    v = s.diff().rolling(63, min_periods=21).std()
    b = v.rolling(252, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content-base build minus depamor-build, percentile-ranked (net-build regime)
def f26ic_f26_intangible_content_base_netbuildrank_504d_base_v137_signal(intangibles, ppnenet, depamor):
    cb = _f26_content_base(intangibles, ppnenet)
    raw = _logroc(cb, 126) - _logroc(depamor, 126)
    b = _rank(raw, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-share reversal: today's 21d move against the prior 63d move (mean-reversion)
def f26ic_f26_intangible_content_base_heavyreversal_base_v138_signal(intangibles, assets):
    s = _f26_intang_share(intangibles, assets)
    recent = s - s.shift(21)
    prior = s.shift(21) - s.shift(84)
    b = -np.sign(prior) * recent
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# depamor / tangibles (physical-base expensing pace, distinct from ppnenet pace)
def f26ic_f26_intangible_content_base_amorttang_base_v139_signal(depamor, tangibles):
    s = depamor / tangibles.replace(0, np.nan)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content-vs-balance-sheet co-movement: rolling 252d correlation of intangible and asset log-growth
def f26ic_f26_intangible_content_base_intangodds_base_v140_signal(intangibles, assets):
    gi = _logroc(intangibles, 21)
    ga = _logroc(assets, 21)
    b = gi.rolling(252, min_periods=126).corr(ga)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content out-investment streak intensity: positive-gap run length x cumulative gap
def f26ic_f26_intangible_content_base_outinveststreak_base_v141_signal(intangibles, assets):
    g = _logroc(intangibles, 63) - _logroc(assets, 63)
    pos = (g > 0).astype(float)
    grp = (pos != pos.shift(1)).cumsum()
    runlen = pos.groupby(grp).cumsum()
    runmag = (g.clip(lower=0)).groupby(grp).cumsum()
    b = runlen * runmag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization aging vs its slow EMA (expensing displacement)
def f26ic_f26_intangible_content_base_agingdisp_base_v142_signal(depamor, intangibles, ppnenet):
    s = _f26_amort_aging(depamor, intangibles, ppnenet)
    b = s - s.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-heaviness vs tangible-heaviness correlation breakdown (mix regime shift)
def f26ic_f26_intangible_content_base_mixregime_base_v143_signal(intangibles, tangibles, assets):
    si = _f26_intang_share(intangibles, assets)
    st = _f26_tang_share(tangibles, assets)
    b = si.diff().rolling(252, min_periods=126).corr(st.diff())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content-base growth risk-adjusted (252d log-growth / 252d growth vol)
def f26ic_f26_intangible_content_base_buildquality_base_v144_signal(intangibles, ppnenet):
    cb = _f26_content_base(intangibles, ppnenet)
    g = _logroc(cb, 252)
    vol = _logroc(cb, 21).rolling(252, min_periods=63).std()
    b = g / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied content life vs platform life ratio, de-trended (relative aging)
def f26ic_f26_intangible_content_base_relaging_base_v145_signal(intangibles, ppnenet):
    s = np.log((intangibles / ppnenet.replace(0, np.nan)).replace(0, np.nan))
    b = s - s.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year amortization pace falling (refresh / capitalization regime)
def f26ic_f26_intangible_content_base_pacedntime_252d_base_v146_signal(depamor, intangibles):
    s = _f26_amort_pace(depamor, intangibles)
    dn = (s.diff() < 0).astype(float)
    b = dn.rolling(252, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-vs-tangible balance horizon spread: 21d move minus 126d move per day (mix-balance accel)
def f26ic_f26_intangible_content_base_tiltcurv_base_v147_signal(intangibles, tangibles, assets):
    raw = (intangibles - tangibles) / (intangibles + tangibles).replace(0, np.nan)
    fast = (raw - raw.shift(21)) / 21.0
    slow = (raw - raw.shift(126)) / 126.0
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# content-base intensity vs amortization-aging interaction (heavy-and-aging composite)
def f26ic_f26_intangible_content_base_heavyaging_base_v148_signal(intangibles, ppnenet, depamor, assets):
    intensity = _f26_content_base(intangibles, ppnenet) / assets.replace(0, np.nan)
    aging = _z(_f26_amort_aging(depamor, intangibles, ppnenet), 252)
    b = (intensity - intensity.rolling(504, min_periods=126).median()) * aging
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon intangible-share dispersion (std across 63/252/504 share levels)
def f26ic_f26_intangible_content_base_heavymultidisp_base_v149_signal(intangibles, assets):
    s = _f26_intang_share(intangibles, assets)
    m1 = _mean(s, 63)
    m2 = _mean(s, 252)
    m3 = _mean(s, 504)
    b = pd.concat([m1, m2, m3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable content compounder composite: rising heaviness x net build x stable expensing
def f26ic_f26_intangible_content_base_compounder_base_v150_signal(intangibles, ppnenet, depamor, assets):
    heavy_slope = _slope(_f26_intang_share(intangibles, assets), 252)
    cb = _f26_content_base(intangibles, ppnenet)
    netbuild = _logroc(cb, 252) - _logroc(depamor, 252)
    stable = -_std(_f26_amort_aging(depamor, intangibles, ppnenet), 252)
    b = np.tanh(2000.0 * heavy_slope) + np.tanh(5.0 * netbuild) + 0.5 * _z(stable, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f26ic_f26_intangible_content_base_heavyslope_252d_base_v076_signal,
    f26ic_f26_intangible_content_base_paceslope_252d_base_v077_signal,
    f26ic_f26_intangible_content_base_baseslope_126d_base_v078_signal,
    f26ic_f26_intangible_content_base_heavycross_base_v079_signal,
    f26ic_f26_intangible_content_base_pacecross_base_v080_signal,
    f26ic_f26_intangible_content_base_heavyupsemi_252d_base_v081_signal,
    f26ic_f26_intangible_content_base_heavydnsemi_252d_base_v082_signal,
    f26ic_f26_intangible_content_base_paceskew_252d_base_v083_signal,
    f26ic_f26_intangible_content_base_nettiltsm_base_v084_signal,
    f26ic_f26_intangible_content_base_netbuildsm_252d_base_v085_signal,
    f26ic_f26_intangible_content_base_burdenaccel_base_v086_signal,
    f26ic_f26_intangible_content_base_heavyrr_base_v087_signal,
    f26ic_f26_intangible_content_base_heavyrun_base_v088_signal,
    f26ic_f26_intangible_content_base_pacerun_base_v089_signal,
    f26ic_f26_intangible_content_base_outinvestsm_252d_base_v090_signal,
    f26ic_f26_intangible_content_base_tangslope_252d_base_v091_signal,
    f26ic_f26_intangible_content_base_mixslope_252d_base_v092_signal,
    f26ic_f26_intangible_content_base_agingslope_252d_base_v093_signal,
    f26ic_f26_intangible_content_base_lifecurv_base_v094_signal,
    f26ic_f26_intangible_content_base_intensitydisp_base_v095_signal,
    f26ic_f26_intangible_content_base_buildlumpiness_252d_base_v096_signal,
    f26ic_f26_intangible_content_base_intanglumpiness_252d_base_v097_signal,
    f26ic_f26_intangible_content_base_amortlumpiness_252d_base_v098_signal,
    f26ic_f26_intangible_content_base_heavyfrompeak_1260d_base_v099_signal,
    f26ic_f26_intangible_content_base_pacefrompeak_1260d_base_v100_signal,
    f26ic_f26_intangible_content_base_intensitypos_1260d_base_v101_signal,
    f26ic_f26_intangible_content_base_intang2ppnez_252d_base_v102_signal,
    f26ic_f26_intangible_content_base_burdencross_base_v103_signal,
    f26ic_f26_intangible_content_base_lifespreadsm_base_v104_signal,
    f26ic_f26_intangible_content_base_agingupper_252d_base_v105_signal,
    f26ic_f26_intangible_content_base_heavylowentries_252d_base_v106_signal,
    f26ic_f26_intangible_content_base_cleanreinvest_base_v107_signal,
    f26ic_f26_intangible_content_base_intensityyoy_252d_base_v108_signal,
    f26ic_f26_intangible_content_base_tangpos_1260d_base_v109_signal,
    f26ic_f26_intangible_content_base_netcontentz_252d_base_v110_signal,
    f26ic_f26_intangible_content_base_growhorizon_base_v111_signal,
    f26ic_f26_intangible_content_base_pacehorizon_base_v112_signal,
    f26ic_f26_intangible_content_base_intensitystretch_504d_base_v113_signal,
    f26ic_f26_intangible_content_base_coveragesm_base_v114_signal,
    f26ic_f26_intangible_content_base_intangofnontangz_252d_base_v115_signal,
    f26ic_f26_intangible_content_base_amortconc_base_v116_signal,
    f26ic_f26_intangible_content_base_baseaccel_base_v117_signal,
    f26ic_f26_intangible_content_base_sharemixz_252d_base_v118_signal,
    f26ic_f26_intangible_content_base_paceefficiency_base_v119_signal,
    f26ic_f26_intangible_content_base_buildexpensecorr_252d_base_v120_signal,
    f26ic_f26_intangible_content_base_initangcorr_252d_base_v121_signal,
    f26ic_f26_intangible_content_base_libvsplatform_base_v122_signal,
    f26ic_f26_intangible_content_base_agingaccel_base_v123_signal,
    f26ic_f26_intangible_content_base_basevstang_252d_base_v124_signal,
    f26ic_f26_intangible_content_base_liferank_1260d_base_v125_signal,
    f26ic_f26_intangible_content_base_heavymomadj_base_v126_signal,
    f26ic_f26_intangible_content_base_heavyconvex_base_v127_signal,
    f26ic_f26_intangible_content_base_burdenregimegap_base_v128_signal,
    f26ic_f26_intangible_content_base_heavyuptime_252d_base_v129_signal,
    f26ic_f26_intangible_content_base_baselife_base_v130_signal,
    f26ic_f26_intangible_content_base_tang2basez_252d_base_v131_signal,
    f26ic_f26_intangible_content_base_pacevsburden_base_v132_signal,
    f26ic_f26_intangible_content_base_burdenslope_126d_base_v133_signal,
    f26ic_f26_intangible_content_base_intensityaccel_base_v134_signal,
    f26ic_f26_intangible_content_base_mixdist_1260d_base_v135_signal,
    f26ic_f26_intangible_content_base_pacevov_base_v136_signal,
    f26ic_f26_intangible_content_base_netbuildrank_504d_base_v137_signal,
    f26ic_f26_intangible_content_base_heavyreversal_base_v138_signal,
    f26ic_f26_intangible_content_base_amorttang_base_v139_signal,
    f26ic_f26_intangible_content_base_intangodds_base_v140_signal,
    f26ic_f26_intangible_content_base_outinveststreak_base_v141_signal,
    f26ic_f26_intangible_content_base_agingdisp_base_v142_signal,
    f26ic_f26_intangible_content_base_mixregime_base_v143_signal,
    f26ic_f26_intangible_content_base_buildquality_base_v144_signal,
    f26ic_f26_intangible_content_base_relaging_base_v145_signal,
    f26ic_f26_intangible_content_base_pacedntime_252d_base_v146_signal,
    f26ic_f26_intangible_content_base_tiltcurv_base_v147_signal,
    f26ic_f26_intangible_content_base_heavyaging_base_v148_signal,
    f26ic_f26_intangible_content_base_heavymultidisp_base_v149_signal,
    f26ic_f26_intangible_content_base_compounder_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_INTANGIBLE_CONTENT_BASE_REGISTRY_076_150 = REGISTRY


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

    def _wig(seed, amp):
        g = np.random.default_rng(seed)
        w = np.cumsum(g.normal(0.0, amp, n))
        w = w - pd.Series(w).rolling(126, min_periods=1).mean().values
        return np.exp(w)

    assets = _fund(2601, base=1.0e9, drift=0.030, vol=0.06).rename("assets")
    assets = (assets * _wig(3601, 0.022)).rename("assets")
    ishare = _fund(2602, base=0.30, drift=0.010, vol=0.05)
    ishare = (0.16 + 0.20 * (ishare / ishare.iloc[0]).clip(0.6, 1.4) / 1.4) * _wig(3602, 0.030)
    intangibles = (assets * ishare).rename("intangibles")
    tshare = _fund(2603, base=0.28, drift=0.008, vol=0.045)
    tshare = (0.18 + 0.16 * (tshare / tshare.iloc[0]).clip(0.6, 1.4) / 1.4) * _wig(3603, 0.026)
    tangibles = (assets * tshare).rename("tangibles")
    ppshare = _fund(2604, base=0.16, drift=0.012, vol=0.06)
    ppshare = (0.09 + 0.11 * (ppshare / ppshare.iloc[0]).clip(0.6, 1.4) / 1.4) * _wig(3604, 0.034)
    ppnenet = (assets * ppshare).rename("ppnenet")
    dpace = _fund(2605, base=0.08, drift=0.006, vol=0.10)
    dpace = (0.05 + 0.09 * (dpace / dpace.iloc[0]).clip(0.5, 1.6) / 1.6) * _wig(3605, 0.050)
    depamor = ((intangibles + ppnenet) * dpace).rename("depamor")

    assert (intangibles > 0).all() and (tangibles > 0).all()
    assert (ppnenet > 0).all() and (depamor > 0).all() and (assets > 0).all()
    assert (intangibles < assets).all() and (tangibles < assets).all()
    assert ((intangibles + tangibles) <= assets).all()

    cols = {
        "intangibles": intangibles,
        "assets": assets,
        "depamor": depamor,
        "ppnenet": ppnenet,
        "tangibles": tangibles,
    }

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

    print("OK f26_intangible_content_base_base_076_150_claude: %d features pass" % n_features)
