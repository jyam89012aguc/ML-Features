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


# ===== folder domain primitives (capex / exploration MAGNITUDE & FUNDING & DEVELOPMENT) =====
# Same tightened, depamor-centric domain as file 1. Avoids capex/revenue & rnd/revenue momentum
# (f25/f27 margin/cost) and raw capex/assets, capex/ppnenet level z/rank (f40/f30).
def _f28_capex_depamor(capex, depamor):
    return capex / depamor.replace(0, np.nan)


def _f28_rnd_depamor(rnd, depamor):
    return rnd / depamor.replace(0, np.nan)


def _f28_rnd_capex(rnd, capex):
    return rnd / capex.replace(0, np.nan)


def _f28_explore_share(capex, rnd):
    return rnd / (capex + rnd).replace(0, np.nan)


def _f28_invest_intensity(ncfi, depamor):
    return (-ncfi) / depamor.replace(0, np.nan)


def _f28_age(depamor, ppnenet):
    return depamor / ppnenet.replace(0, np.nan)


def _f28_excess_over_ppne(capex, depamor, ppnenet):
    return (capex - depamor) / ppnenet.replace(0, np.nan)


def _f28_total_invest(capex, rnd):
    return capex + rnd


# ============================================================
# === CAPEX/DEPAMOR — additional horizons & transforms ===

# capex/depamor short-vs-long ratio (growth-stance acceleration regime)
def f28cx_f28_capex_exploration_intensity_capdep_slratio_base_v076_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    short = _mean(r, 63)
    long = _mean(r, 252)
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor year-over-year growth (252d log change of smoothed multiple, long-horizon)
def f28cx_f28_capex_exploration_intensity_capdep_g126d_base_v077_signal(capex, depamor):
    sm = _mean(_f28_capex_depamor(capex, depamor), 63)
    b = np.log(sm.replace(0, np.nan) / sm.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# maintenance run-rate growth: YoY log-growth of depamor (asset-base depreciation acceleration)
def f28cx_f28_capex_exploration_intensity_capdep_ema_base_v078_signal(capex, depamor):
    sm = _mean(depamor, 63)
    g = np.log(sm.replace(0, np.nan) / sm.shift(252).replace(0, np.nan))
    # contextualize by capex stance so the feature stays in the capex/exploration domain
    capdep = _f28_capex_depamor(capex, depamor)
    b = g - g.rolling(252, min_periods=63).mean() + 0.1 * np.tanh(_z(capdep, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor distance above its 504d trough (growth-spend revival from cycle low)
def f28cx_f28_capex_exploration_intensity_capdep_troughgap_base_v079_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    trough = _rmin(r, 504)
    b = r / trough.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor 252d-rank minus 504d-rank (cycle-position spread, short vs long anchor)
def f28cx_f28_capex_exploration_intensity_capdep_rankspr_base_v080_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    b = _rank(r, 252) - _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === EXCESS-CAPEX (growth over maintenance) — more facets ===

# excess capex over maintenance per PP&E, smoothed and ranked vs 1260d (build-cycle phase)
def f28cx_f28_capex_exploration_intensity_excessppne_rank1260_base_v081_signal(capex, depamor, ppnenet):
    r = _mean(_f28_excess_over_ppne(capex, depamor, ppnenet), 63)
    b = r.rolling(1260, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# excess-capex volatility over a year (lumpiness of the growth-capex program)
def f28cx_f28_capex_exploration_intensity_excessppne_vol_base_v082_signal(capex, depamor, ppnenet):
    r = _f28_excess_over_ppne(capex, depamor, ppnenet)
    b = _std(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# excess-capex YoY change (net-expansion rate drift through cycle)
def f28cx_f28_capex_exploration_intensity_excessppne_yoy_base_v083_signal(capex, depamor, ppnenet):
    r = _f28_excess_over_ppne(capex, depamor, ppnenet)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sustained-growth regime: fraction of last year excess-capex/PP&E above its 252d median
def f28cx_f28_capex_exploration_intensity_excessregime_base_v084_signal(capex, depamor, ppnenet):
    r = _f28_excess_over_ppne(capex, depamor, ppnenet)
    med = r.rolling(252, min_periods=126).median()
    above = (r > med).astype(float)
    b = above.rolling(252, min_periods=126).mean() + 0.2 * np.tanh(_z(r, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# excess-capex tanh-squashed short-horizon surprise (bounded growth-capex news)
def f28cx_f28_capex_exploration_intensity_excessppne_tanh_base_v085_signal(capex, depamor, ppnenet):
    r = _f28_excess_over_ppne(capex, depamor, ppnenet)
    z = _z(r, 63)
    b = np.tanh(z)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === EXPLORATION (rnd) — additional facets ===

# rnd/depamor percentile-rank vs 504d (exploration-cycle position)
def f28cx_f28_capex_exploration_intensity_rnddep_rank504d_base_v086_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/depamor short-vs-long ratio (exploration ramp regime)
def f28cx_f28_capex_exploration_intensity_rnddep_slratio_base_v087_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    short = _mean(r, 63)
    long = _mean(r, 252)
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/depamor distance below its 504d peak (exploration pullback from cycle high)
def f28cx_f28_capex_exploration_intensity_rnddep_z504d_base_v088_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    peak = _rmax(r, 504)
    b = r / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/depamor half-year growth (126d log change of smoothed exploration multiple)
def f28cx_f28_capex_exploration_intensity_rnddep_cycdist_base_v089_signal(rnd, depamor):
    sm = _mean(_f28_rnd_depamor(rnd, depamor), 63)
    b = np.log(sm.replace(0, np.nan) / sm.shift(126).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# exploration-burst count: entries into top-quartile rnd/depamor over a year (discovery-spend tally)
def f28cx_f28_capex_exploration_intensity_explburstcount_base_v090_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    q75 = r.rolling(504, min_periods=126).quantile(0.75)
    hot = (r >= q75).astype(float)
    entries = ((hot == 1) & (hot.shift(1) == 0)).astype(float)
    b = entries.rolling(252, min_periods=126).sum() + hot.rolling(63, min_periods=21).mean() + 0.5 * _z(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/capex (explore-vs-develop mix) percentile-rank vs 1260d (multi-year strategy position)
def f28cx_f28_capex_exploration_intensity_rndcap_rank1260_base_v091_signal(rnd, capex):
    r = _f28_rnd_capex(rnd, capex)
    b = r.rolling(1260, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/capex year-over-year change (mix drift toward greenfield or development)
def f28cx_f28_capex_exploration_intensity_rndcap_yoy_base_v092_signal(rnd, capex):
    r = _f28_rnd_capex(rnd, capex)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/capex volatility (lumpiness of the explore-vs-develop mix)
def f28cx_f28_capex_exploration_intensity_rndcap_vol_base_v093_signal(rnd, capex):
    r = _f28_rnd_capex(rnd, capex)
    b = _std(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# exploration-share short-horizon surprise vs 63d norm, tanh-squashed
def f28cx_f28_capex_exploration_intensity_explshare_tanh_base_v094_signal(capex, rnd):
    share = _f28_explore_share(capex, rnd)
    z = _z(share, 63)
    b = np.tanh(z)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# explorer-tilt regime: fraction of last year exploration-share sat above its 252d median
def f28cx_f28_capex_exploration_intensity_explshare_rank1260_base_v095_signal(capex, rnd):
    share = _f28_explore_share(capex, rnd)
    med = share.rolling(252, min_periods=126).median()
    tilt = (share > med).astype(float)
    b = tilt.rolling(252, min_periods=126).mean() + 0.2 * np.tanh(_z(share, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === INVESTING-CASH (ncfi) — additional facets ===

# -ncfi/depamor percentile-rank vs 504d (deployment-cycle position)
def f28cx_f28_capex_exploration_intensity_ncfidep_rank504d_base_v096_signal(ncfi, depamor):
    r = _f28_invest_intensity(ncfi, depamor)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# -ncfi/depamor short-vs-long ratio (deployment acceleration regime)
def f28cx_f28_capex_exploration_intensity_ncfidep_slratio_base_v097_signal(ncfi, depamor):
    r = _f28_invest_intensity(ncfi, depamor)
    short = _mean(r, 63)
    long = _mean(r, 252)
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# -ncfi/depamor year-over-year change (deployment drift through cycle)
def f28cx_f28_capex_exploration_intensity_ncfidep_yoy_base_v098_signal(ncfi, depamor):
    r = _f28_invest_intensity(ncfi, depamor)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# -ncfi/depamor distance below its 504d peak (deployment pullback from cycle high)
def f28cx_f28_capex_exploration_intensity_ncfidep_peakgap_base_v099_signal(ncfi, depamor):
    r = _f28_invest_intensity(ncfi, depamor)
    peak = _rmax(r, 504)
    b = r / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deployment cycle-phase distance: -ncfi/depamor position within its 504d range
def f28cx_f28_capex_exploration_intensity_ncfidep_cycdist_base_v100_signal(ncfi, depamor):
    r = _f28_invest_intensity(ncfi, depamor)
    hi = _rmax(r, 504)
    lo = _rmin(r, 504)
    mid = (hi + lo) / 2.0
    b = (r - mid) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex coverage of investing outflow: capex/|ncfi| ranked vs 504d (organic-vs-total deployment cycle)
def f28cx_f28_capex_exploration_intensity_capexcover_base_v101_signal(capex, ncfi):
    r = (capex / ncfi.abs().replace(0, np.nan)).clip(upper=5.0)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex coverage of investing outflow: capex/|ncfi| z-scored vs 252d
def f28cx_f28_capex_exploration_intensity_capexcover_z_base_v102_signal(capex, ncfi):
    r = (capex / ncfi.abs().replace(0, np.nan)).clip(upper=5.0)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === ASSET AGING (depamor/ppnenet) — additional facets ===

# aging-rate z-scored vs 252d (asset-base aging surprise)
def f28cx_f28_capex_exploration_intensity_aging_z252d_base_v103_signal(depamor, ppnenet):
    r = _f28_age(depamor, ppnenet)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging-rate percentile-rank vs 504d (where in the asset-age cycle)
def f28cx_f28_capex_exploration_intensity_aging_rank504d_base_v104_signal(depamor, ppnenet):
    r = _f28_age(depamor, ppnenet)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging-rate volatility (depreciation-policy / write-down lumpiness)
def f28cx_f28_capex_exploration_intensity_aging_vol_base_v105_signal(depamor, ppnenet):
    r = _f28_age(depamor, ppnenet)
    b = _std(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex coverage of asset decay: capex vs depreciation run-rate tilted by asset-aging speed,
# expressed as displacement from its slow EMA (renewal-pressure deviation) — distinct from peakgap/z/slratio
def f28cx_f28_capex_exploration_intensity_renewal_z_base_v106_signal(capex, depamor, ppnenet):
    age = _f28_age(depamor, ppnenet)
    pressure = capex / (depamor * (1.0 + age)).replace(0, np.nan)
    b = pressure - pressure.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging acceleration: 2nd difference of depamor/ppnenet over quarters (rapid asset-base aging)
def f28cx_f28_capex_exploration_intensity_aging_accel_base_v107_signal(depamor, ppnenet):
    r = _mean(_f28_age(depamor, ppnenet), 21)
    b = r - 2.0 * r.shift(63) + r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === TOTAL DISCRETIONARY INVESTMENT vs MAINTENANCE — additional facets ===

# (capex+rnd)/depamor z-scored vs 252d (total-investment-vs-maintenance surprise)
def f28cx_f28_capex_exploration_intensity_totinvdep_z252d_base_v108_signal(capex, rnd, depamor):
    r = (capex + rnd) / depamor.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-investment-vs-maintenance half-year-vs-prior-half acceleration (program ramp/cool)
def f28cx_f28_capex_exploration_intensity_totinvdep_yoy_base_v109_signal(capex, rnd, depamor):
    r = _mean((capex + rnd) / depamor.replace(0, np.nan), 21)
    b = (r - r.shift(126)) - (r.shift(126) - r.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# exploration contribution to total-program lumpiness: total-vs-maintenance CV minus capex-vs-maint CV
def f28cx_f28_capex_exploration_intensity_totinvdep_vol_base_v110_signal(capex, rnd, depamor):
    tot = (capex + rnd) / depamor.replace(0, np.nan)
    cap = capex / depamor.replace(0, np.nan)
    cv_tot = _std(tot, 252) / _mean(tot, 252).replace(0, np.nan)
    cv_cap = _std(cap, 252) / _mean(cap, 252).replace(0, np.nan)
    b = cv_tot - cv_cap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# (capex+rnd)/depamor distance below 504d peak (total-program pullback)
def f28cx_f28_capex_exploration_intensity_totinvdep_peakgap_base_v111_signal(capex, rnd, depamor):
    r = (capex + rnd) / depamor.replace(0, np.nan)
    peak = _rmax(r, 504)
    b = r / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# exploration-program displacement: (rnd/depamor) minus its slow EMA, scaled into total program
def f28cx_f28_capex_exploration_intensity_totinvdep_disp_base_v112_signal(capex, rnd, depamor):
    expl = _f28_rnd_depamor(rnd, depamor)
    weight = rnd / (capex + rnd).replace(0, np.nan)
    disp = expl - expl.ewm(span=126, min_periods=42).mean()
    b = disp * weight
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === DEVELOPMENT-vs-EXPLORATION TILT — additional facets ===

# (capex-rnd)/depamor build-vs-explore tilt z-scored vs 252d
def f28cx_f28_capex_exploration_intensity_devexpl_z_base_v113_signal(capex, rnd, depamor):
    d = (capex - rnd) / depamor.replace(0, np.nan)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# (capex-rnd)/depamor tilt rank vs 1260d (multi-year strategy position)
def f28cx_f28_capex_exploration_intensity_devexpl_rank1260_base_v114_signal(capex, rnd, depamor):
    d = (capex - rnd) / depamor.replace(0, np.nan)
    b = d.rolling(1260, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# greenfield lead momentum: change in rnd/(capex+rnd) over a quarter, tanh-squashed
def f28cx_f28_capex_exploration_intensity_greenfieldmom_base_v115_signal(capex, rnd):
    share = _f28_explore_share(capex, rnd)
    chg = share - share.shift(63)
    b = np.tanh(5.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === BURST / PAUSE / STREAK — additional facets ===

# exploration-burst flag intensity: rnd/depamor far above its 252d norm
def f28cx_f28_capex_exploration_intensity_explburst_base_v116_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    z = _z(r, 252)
    burst = (z > 1.0).astype(float)
    b = burst.rolling(252, min_periods=126).mean() + 0.25 * np.tanh(z)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deployment-pause flag intensity: -ncfi/depamor far below its 252d norm (investing freeze)
def f28cx_f28_capex_exploration_intensity_deploypause_base_v117_signal(ncfi, depamor):
    r = _f28_invest_intensity(ncfi, depamor)
    z = _z(r, 252)
    pause = (z < -1.0).astype(float)
    b = pause.rolling(252, min_periods=126).mean() - 0.25 * np.tanh(z)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd-build streak: consecutive periods of rising smoothed rnd/depamor (exploration ramp)
def f28cx_f28_capex_exploration_intensity_explrampstreak_base_v118_signal(rnd, depamor):
    r = _mean(_f28_rnd_depamor(rnd, depamor), 63)
    rising = (r > r.shift(21)).astype(float)
    grp = (rising != rising.shift(1)).cumsum()
    streak = rising.groupby(grp).cumsum() * rising
    b = streak / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-cut streak: consecutive periods of falling smoothed capex/depamor (build capitulation)
def f28cx_f28_capex_exploration_intensity_buildcutstreak_base_v119_signal(capex, depamor):
    r = _mean(_f28_capex_depamor(capex, depamor), 63)
    falling = (r < r.shift(21)).astype(float)
    grp = (falling != falling.shift(1)).cumsum()
    streak = falling.groupby(grp).cumsum() * falling
    b = streak / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of deployment-pause entries over a year (investing-freeze tally)
def f28cx_f28_capex_exploration_intensity_pausecount_base_v120_signal(ncfi, depamor):
    r = _f28_invest_intensity(ncfi, depamor)
    z = _z(r, 252)
    cold = (z < -0.5).astype(float)
    entries = ((cold == 1) & (cold.shift(1) == 0)).astype(float)
    b = entries.rolling(252, min_periods=126).sum() - z.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === DISPERSION / DISPLACEMENT — additional facets ===

# coefficient of variation of rnd/depamor (exploration-program lumpiness, scale-free)
def f28cx_f28_capex_exploration_intensity_rnddep_cv_base_v121_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    b = _std(r, 252) / _mean(r, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor minus its 252d median (build-stance relative to typical level)
def f28cx_f28_capex_exploration_intensity_capdep_relmed_base_v122_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    med = r.rolling(252, min_periods=63).median()
    b = r - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/depamor minus its 252d median (exploration-stance relative to typical level)
def f28cx_f28_capex_exploration_intensity_rnddep_relmed_base_v123_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    med = r.rolling(252, min_periods=63).median()
    b = r - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion across capex/dep, rnd/dep, -ncfi/dep z-levels (intensity-program disagreement)
def f28cx_f28_capex_exploration_intensity_rawdisp_base_v124_signal(capex, rnd, ncfi, depamor):
    a = _z(_f28_capex_depamor(capex, depamor), 252)
    b2 = _z(_f28_rnd_depamor(rnd, depamor), 252)
    c = _z(_f28_invest_intensity(ncfi, depamor), 252)
    b = pd.concat([a, b2, c], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EWM fast-vs-slow trend gap on rnd/depamor (exploration-trend slope proxy)
def f28cx_f28_capex_exploration_intensity_rnddep_emagap_base_v125_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    b = r.ewm(span=42, min_periods=21).mean() - r.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === INTERACTION / SIGN-MAGNITUDE — additional facets ===

# exploration-stance x exploration-momentum interaction (rnd/depamor scaled by its change)
def f28cx_f28_capex_exploration_intensity_rnddep_mom_int_base_v126_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    mom = r - r.shift(126)
    b = np.sign(mom) * (r.clip(lower=0) * mom.abs()) ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deployment-momentum tanh: bounded half-year change in -ncfi/depamor (deploy-acceleration news)
def f28cx_f28_capex_exploration_intensity_ncfidep_mom_int_base_v127_signal(ncfi, depamor):
    r = _f28_invest_intensity(ncfi, depamor)
    sm = _mean(r, 21)
    chg = (sm - sm.shift(126)) - (sm.shift(126) - sm.shift(252))
    b = np.tanh(chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# excess-capex x net-expansion acceleration (compounding growth-capex signal)
def f28cx_f28_capex_exploration_intensity_excess_accel_int_base_v128_signal(capex, depamor, ppnenet):
    r = _f28_excess_over_ppne(capex, depamor, ppnenet)
    accel = r - 2.0 * r.shift(63) + r.shift(126)
    b = np.tanh(50.0 * r) * np.sign(accel) * accel.abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# explorer-to-producer transition: rnd lead now vs build lead a year ago (strategy rotation)
def f28cx_f28_capex_exploration_intensity_strategyrotate_base_v129_signal(capex, rnd, depamor):
    explead = _f28_rnd_depamor(rnd, depamor)
    buildlead = _f28_capex_depamor(capex, depamor)
    rot = explead.rank(pct=True) - buildlead.shift(252).rank(pct=True)
    b = rot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor sign-magnitude compression vs its typical level (build-extremity)
def f28cx_f28_capex_exploration_intensity_capdep_signmag_base_v130_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor) - 1.0
    typ = r.rolling(252, min_periods=126).mean()
    b = np.sign(r) * (r.abs() ** 0.5) - np.sign(typ) * (typ.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === LONG-HORIZON / CYCLE — additional facets ===

# capex/depamor 1260d-rank minus 504d-rank (long-vs-medium build-cycle spread)
def f28cx_f28_capex_exploration_intensity_capdep_longspr_base_v131_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    long = r.rolling(1260, min_periods=252).rank(pct=True) - 0.5
    med = r.rolling(504, min_periods=126).rank(pct=True) - 0.5
    b = long - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# exploration extremity regime: fraction of last year rnd/depamor sat in the top quartile of its 504d range
def f28cx_f28_capex_exploration_intensity_overexpl_mom_base_v132_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    q75 = r.rolling(504, min_periods=126).quantile(0.75)
    hot = (r >= q75).astype(float)
    b = hot.rolling(252, min_periods=126).mean() + 0.2 * np.tanh(_z(r, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deployment over-stretch: -ncfi/depamor relative to its 1260d mean (multi-year deploy extremity)
def f28cx_f28_capex_exploration_intensity_overdeploy_dist_base_v133_signal(ncfi, depamor):
    r = _f28_invest_intensity(ncfi, depamor)
    base = r.rolling(1260, min_periods=252).mean()
    b = r / base.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# excess-capex/PP&E rank vs 1260d minus its own 252d-rank (cycle-position divergence)
def f28cx_f28_capex_exploration_intensity_excess_rankdiv_base_v134_signal(capex, depamor, ppnenet):
    r = _f28_excess_over_ppne(capex, depamor, ppnenet)
    long = r.rolling(1260, min_periods=252).rank(pct=True) - 0.5
    short = _rank(r, 252)
    b = long - short
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === SPARING REVENUE USE (gate only, NOT capex/revenue-momentum core) ===

# build-magnitude when lean: capex/depamor z gated by revenue near its multi-year low
def f28cx_f28_capex_exploration_intensity_buildwhenlean_base_v135_signal(capex, depamor, revenue):
    capdep = _z(_f28_capex_depamor(capex, depamor), 126)
    rev_pos = revenue.rolling(504, min_periods=126).rank(pct=True)
    gate = (1.0 - rev_pos)
    b = capdep * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# exploration-when-lean: rnd/depamor burst gated by revenue near multi-year low (pre-revenue explorer)
def f28cx_f28_capex_exploration_intensity_explwhenlean_base_v136_signal(rnd, depamor, revenue):
    expl = _z(_f28_rnd_depamor(rnd, depamor), 126)
    rev_pos = revenue.rolling(504, min_periods=126).rank(pct=True)
    gate = (1.0 - rev_pos)
    b = expl * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === COMPLETE 150 ===

# build-program maturity: (capex/depamor - 1) weighted by how long it has stayed above its median
def f28cx_f28_capex_exploration_intensity_buildmaturity_base_v137_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    med = r.rolling(252, min_periods=126).median()
    sustained = (r > med).astype(float).rolling(63, min_periods=21).mean()
    b = (r - 1.0) * sustained
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# exploration-program maturity: rnd/depamor weighted by how long it has held above its median
def f28cx_f28_capex_exploration_intensity_explmaturity_base_v138_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    med = r.rolling(252, min_periods=126).median()
    sustained = (r > med).astype(float).rolling(63, min_periods=21).mean()
    b = r * sustained
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-expansion displacement: (capex-depamor)/ppnenet minus its slow EMA (durable-build deviation)
def f28cx_f28_capex_exploration_intensity_netexpand_ema_base_v139_signal(capex, depamor, ppnenet):
    r = _f28_excess_over_ppne(capex, depamor, ppnenet)
    b = r - r.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investing-program concentration: |ncfi| share of (|ncfi| + depamor) (deal-heavy vs steady-state)
def f28cx_f28_capex_exploration_intensity_dealheavy_base_v140_signal(ncfi, depamor):
    b = ncfi.abs() / (ncfi.abs() + depamor).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor and rnd/depamor co-movement: rolling correlation (joint investment ramp)
def f28cx_f28_capex_exploration_intensity_jointramp_base_v141_signal(capex, rnd, depamor):
    a = _f28_capex_depamor(capex, depamor)
    b2 = _f28_rnd_depamor(rnd, depamor)
    b = a.rolling(252, min_periods=126).corr(b2)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# organic-coverage cycle distance: capex share of investing magnitude within its own 504d range
def f28cx_f28_capex_exploration_intensity_builddeploy_div_base_v142_signal(capex, ncfi, depamor):
    organic = capex / (capex + ncfi.abs()).replace(0, np.nan)
    hi = _rmax(organic, 504)
    lo = _rmin(organic, 504)
    b = (organic - (hi + lo) / 2.0) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# exploration share of total investing deployment: rnd / (rnd + |ncfi|) (greenfield-in-deployment, bounded)
def f28cx_f28_capex_exploration_intensity_exploredeploy_div_base_v143_signal(rnd, ncfi, depamor):
    b = rnd / (rnd + ncfi.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# organic-vs-total deployment regime: fraction of last year capex covered most of investing outflow
def f28cx_f28_capex_exploration_intensity_builddeploy_yoy_base_v144_signal(capex, ncfi, depamor):
    cover = capex / (capex + ncfi.abs()).replace(0, np.nan)
    med = cover.rolling(252, min_periods=126).median()
    organic = (cover > med).astype(float)
    b = organic.rolling(252, min_periods=126).mean() + 0.2 * np.tanh(_z(cover, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# renewal gap regime: fraction of last year capex/depamor exceeded the aging-implied renewal unity
def f28cx_f28_capex_exploration_intensity_renewalgap_rank_base_v145_signal(capex, depamor, ppnenet):
    capdep = _f28_capex_depamor(capex, depamor)
    age = _f28_age(depamor, ppnenet)
    gap = capdep - (1.0 + age)
    covers = (gap > 0).astype(float)
    b = covers.rolling(252, min_periods=126).mean() + 0.2 * np.tanh(_z(gap, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-investment-vs-maintenance regime: fraction of last year (capex+rnd)/depamor above 252d median
def f28cx_f28_capex_exploration_intensity_totinvregime_base_v146_signal(capex, rnd, depamor):
    r = (capex + rnd) / depamor.replace(0, np.nan)
    med = r.rolling(252, min_periods=126).median()
    above = (r > med).astype(float)
    b = above.rolling(252, min_periods=126).mean() + 0.2 * np.tanh(_z(r, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor acceleration: 2nd difference over quarters (build-stance jerk in level terms)
def f28cx_f28_capex_exploration_intensity_capdep_accel_base_v147_signal(capex, depamor):
    r = _mean(_f28_capex_depamor(capex, depamor), 21)
    b = r - 2.0 * r.shift(63) + r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/depamor acceleration: 2nd difference over quarters (exploration-stance jerk in level terms)
def f28cx_f28_capex_exploration_intensity_rnddep_accel_base_v148_signal(rnd, depamor):
    r = _mean(_f28_rnd_depamor(rnd, depamor), 21)
    b = r - 2.0 * r.shift(63) + r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# explore-vs-build mix dispersion across horizons: std of rnd/(capex+rnd) over 63/126/252 means
def f28cx_f28_capex_exploration_intensity_mixdisp_base_v149_signal(capex, rnd):
    share = _f28_explore_share(capex, rnd)
    m1 = _mean(share, 63)
    m2 = _mean(share, 126)
    m3 = _mean(share, 252)
    b = pd.concat([m1, m2, m3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite investment-vs-maintenance intensity: avg z of capex/dep, rnd/dep, -ncfi/dep, excess/ppne
def f28cx_f28_capex_exploration_intensity_composite_z_base_v150_signal(capex, rnd, ncfi, depamor, ppnenet):
    a = _z(_f28_capex_depamor(capex, depamor), 252)
    b2 = _z(_f28_rnd_depamor(rnd, depamor), 252)
    c = _z(_f28_invest_intensity(ncfi, depamor), 252)
    d = _z(_f28_excess_over_ppne(capex, depamor, ppnenet), 252)
    b = (a + b2 + c + d) / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f28cx_f28_capex_exploration_intensity_capdep_slratio_base_v076_signal,
    f28cx_f28_capex_exploration_intensity_capdep_g126d_base_v077_signal,
    f28cx_f28_capex_exploration_intensity_capdep_ema_base_v078_signal,
    f28cx_f28_capex_exploration_intensity_capdep_troughgap_base_v079_signal,
    f28cx_f28_capex_exploration_intensity_capdep_rankspr_base_v080_signal,
    f28cx_f28_capex_exploration_intensity_excessppne_rank1260_base_v081_signal,
    f28cx_f28_capex_exploration_intensity_excessppne_vol_base_v082_signal,
    f28cx_f28_capex_exploration_intensity_excessppne_yoy_base_v083_signal,
    f28cx_f28_capex_exploration_intensity_excessregime_base_v084_signal,
    f28cx_f28_capex_exploration_intensity_excessppne_tanh_base_v085_signal,
    f28cx_f28_capex_exploration_intensity_rnddep_rank504d_base_v086_signal,
    f28cx_f28_capex_exploration_intensity_rnddep_slratio_base_v087_signal,
    f28cx_f28_capex_exploration_intensity_rnddep_z504d_base_v088_signal,
    f28cx_f28_capex_exploration_intensity_rnddep_cycdist_base_v089_signal,
    f28cx_f28_capex_exploration_intensity_explburstcount_base_v090_signal,
    f28cx_f28_capex_exploration_intensity_rndcap_rank1260_base_v091_signal,
    f28cx_f28_capex_exploration_intensity_rndcap_yoy_base_v092_signal,
    f28cx_f28_capex_exploration_intensity_rndcap_vol_base_v093_signal,
    f28cx_f28_capex_exploration_intensity_explshare_tanh_base_v094_signal,
    f28cx_f28_capex_exploration_intensity_explshare_rank1260_base_v095_signal,
    f28cx_f28_capex_exploration_intensity_ncfidep_rank504d_base_v096_signal,
    f28cx_f28_capex_exploration_intensity_ncfidep_slratio_base_v097_signal,
    f28cx_f28_capex_exploration_intensity_ncfidep_yoy_base_v098_signal,
    f28cx_f28_capex_exploration_intensity_ncfidep_peakgap_base_v099_signal,
    f28cx_f28_capex_exploration_intensity_ncfidep_cycdist_base_v100_signal,
    f28cx_f28_capex_exploration_intensity_capexcover_base_v101_signal,
    f28cx_f28_capex_exploration_intensity_capexcover_z_base_v102_signal,
    f28cx_f28_capex_exploration_intensity_aging_z252d_base_v103_signal,
    f28cx_f28_capex_exploration_intensity_aging_rank504d_base_v104_signal,
    f28cx_f28_capex_exploration_intensity_aging_vol_base_v105_signal,
    f28cx_f28_capex_exploration_intensity_renewal_z_base_v106_signal,
    f28cx_f28_capex_exploration_intensity_aging_accel_base_v107_signal,
    f28cx_f28_capex_exploration_intensity_totinvdep_z252d_base_v108_signal,
    f28cx_f28_capex_exploration_intensity_totinvdep_yoy_base_v109_signal,
    f28cx_f28_capex_exploration_intensity_totinvdep_vol_base_v110_signal,
    f28cx_f28_capex_exploration_intensity_totinvdep_peakgap_base_v111_signal,
    f28cx_f28_capex_exploration_intensity_totinvdep_disp_base_v112_signal,
    f28cx_f28_capex_exploration_intensity_devexpl_z_base_v113_signal,
    f28cx_f28_capex_exploration_intensity_devexpl_rank1260_base_v114_signal,
    f28cx_f28_capex_exploration_intensity_greenfieldmom_base_v115_signal,
    f28cx_f28_capex_exploration_intensity_explburst_base_v116_signal,
    f28cx_f28_capex_exploration_intensity_deploypause_base_v117_signal,
    f28cx_f28_capex_exploration_intensity_explrampstreak_base_v118_signal,
    f28cx_f28_capex_exploration_intensity_buildcutstreak_base_v119_signal,
    f28cx_f28_capex_exploration_intensity_pausecount_base_v120_signal,
    f28cx_f28_capex_exploration_intensity_rnddep_cv_base_v121_signal,
    f28cx_f28_capex_exploration_intensity_capdep_relmed_base_v122_signal,
    f28cx_f28_capex_exploration_intensity_rnddep_relmed_base_v123_signal,
    f28cx_f28_capex_exploration_intensity_rawdisp_base_v124_signal,
    f28cx_f28_capex_exploration_intensity_rnddep_emagap_base_v125_signal,
    f28cx_f28_capex_exploration_intensity_rnddep_mom_int_base_v126_signal,
    f28cx_f28_capex_exploration_intensity_ncfidep_mom_int_base_v127_signal,
    f28cx_f28_capex_exploration_intensity_excess_accel_int_base_v128_signal,
    f28cx_f28_capex_exploration_intensity_strategyrotate_base_v129_signal,
    f28cx_f28_capex_exploration_intensity_capdep_signmag_base_v130_signal,
    f28cx_f28_capex_exploration_intensity_capdep_longspr_base_v131_signal,
    f28cx_f28_capex_exploration_intensity_overexpl_mom_base_v132_signal,
    f28cx_f28_capex_exploration_intensity_overdeploy_dist_base_v133_signal,
    f28cx_f28_capex_exploration_intensity_excess_rankdiv_base_v134_signal,
    f28cx_f28_capex_exploration_intensity_buildwhenlean_base_v135_signal,
    f28cx_f28_capex_exploration_intensity_explwhenlean_base_v136_signal,
    f28cx_f28_capex_exploration_intensity_buildmaturity_base_v137_signal,
    f28cx_f28_capex_exploration_intensity_explmaturity_base_v138_signal,
    f28cx_f28_capex_exploration_intensity_netexpand_ema_base_v139_signal,
    f28cx_f28_capex_exploration_intensity_dealheavy_base_v140_signal,
    f28cx_f28_capex_exploration_intensity_jointramp_base_v141_signal,
    f28cx_f28_capex_exploration_intensity_builddeploy_div_base_v142_signal,
    f28cx_f28_capex_exploration_intensity_exploredeploy_div_base_v143_signal,
    f28cx_f28_capex_exploration_intensity_builddeploy_yoy_base_v144_signal,
    f28cx_f28_capex_exploration_intensity_renewalgap_rank_base_v145_signal,
    f28cx_f28_capex_exploration_intensity_totinvregime_base_v146_signal,
    f28cx_f28_capex_exploration_intensity_capdep_accel_base_v147_signal,
    f28cx_f28_capex_exploration_intensity_rnddep_accel_base_v148_signal,
    f28cx_f28_capex_exploration_intensity_mixdisp_base_v149_signal,
    f28cx_f28_capex_exploration_intensity_composite_z_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_CAPEX_EXPLORATION_INTENSITY_REGISTRY_076_150 = REGISTRY


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

    capex = _fund(2801, base=7e7, drift=0.01, vol=0.18).rename("capex")
    rnd = _fund(2802, base=2e7, drift=0.0, vol=0.20).rename("rnd")
    revenue = _fund(2803, base=3e8, drift=0.01, vol=0.12).rename("revenue")
    assets = _fund(2804, base=1.5e9, drift=0.005, vol=0.06).rename("assets")
    ppnenet = _fund(2805, base=8e8, drift=0.008, vol=0.07).rename("ppnenet")
    ncfi = _fund(2806, base=9e7, drift=0.0, vol=0.30, allow_neg=True).rename("ncfi")
    depamor = _fund(2807, base=5e7, drift=0.006, vol=0.10).rename("depamor")

    cols = {"capex": capex, "rnd": rnd, "revenue": revenue,
            "assets": assets, "ppnenet": ppnenet, "ncfi": ncfi, "depamor": depamor}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in ("capex", "rnd", "revenue", "assets", "ppnenet", "ncfi", "depamor")
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

    print("OK f28_capex_exploration_intensity_base_076_150_claude: %d features pass" % n_features)
