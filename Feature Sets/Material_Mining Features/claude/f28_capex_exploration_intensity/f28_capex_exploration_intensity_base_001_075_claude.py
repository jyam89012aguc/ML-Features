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


# ===== folder domain primitives =====
# TIGHTENED DOMAIN: capex / exploration MAGNITUDE & FUNDING & DEVELOPMENT INTENSITY.
# Central novel axis = depamor (maintenance-capex proxy), plus ncfi and rnd mix.
# Deliberately AVOIDS: capex/revenue & rnd/revenue momentum (collides f25/f27 margins/costs),
# and raw capex/assets & capex/ppnenet level z/rank (owned by f40/f30).
def _f28_capex_depamor(capex, depamor):
    # growth-vs-maintenance: capex relative to depreciation/amortization run-rate
    return capex / depamor.replace(0, np.nan)


def _f28_excess_capex(capex, depamor):
    # capex spent ABOVE the maintenance (depamor) run-rate = pure growth capex dollars
    return capex - depamor


def _f28_excess_over_ppne(capex, depamor, ppnenet):
    # growth capex (above maintenance) normalized by installed PP&E base
    return (capex - depamor) / ppnenet.replace(0, np.nan)


def _f28_rnd_capex(rnd, capex):
    # exploration-vs-development mix: greenfield (rnd) per development dollar (capex)
    return rnd / capex.replace(0, np.nan)


def _f28_rnd_depamor(rnd, depamor):
    # exploration spend scaled by maintenance run-rate (asset-renewal-normalized)
    return rnd / depamor.replace(0, np.nan)


def _f28_explore_share(capex, rnd):
    # exploration share of discretionary investment = rnd / (capex + rnd)
    return rnd / (capex + rnd).replace(0, np.nan)


def _f28_invest_intensity(ncfi, depamor):
    # investing-cash outflow scaled by the maintenance run-rate (deployment multiple)
    return (-ncfi) / depamor.replace(0, np.nan)


def _f28_age(depamor, ppnenet):
    # asset-aging proxy: depreciation as a fraction of installed PP&E
    return depamor / ppnenet.replace(0, np.nan)


def _f28_capex_age(capex, depamor, ppnenet):
    # gross reinvestment relative to asset aging (build vs decay race), via depamor gate
    reinvest = capex / ppnenet.replace(0, np.nan)
    age = depamor / ppnenet.replace(0, np.nan)
    return reinvest - age


# ============================================================
# === GROWTH-VS-MAINTENANCE CAPEX (capex vs depamor) — central axis ===

# capex/depamor reinvestment multiple, log-compressed (>1 = expanding beyond maintenance)
def f28cx_f28_capex_exploration_intensity_capdep_63d_base_v001_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    b = np.log(r.clip(lower=1e-6))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor smoothed over a quarter (persistent growth-vs-maintenance stance)
def f28cx_f28_capex_exploration_intensity_capdep_smooth63d_base_v002_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    b = _mean(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor z-scored vs its own 252d history (growth-spend regime, de-trended)
def f28cx_f28_capex_exploration_intensity_capdep_z252d_base_v003_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor percentile-rank vs 504d (where in the build-vs-maintain cycle)
def f28cx_f28_capex_exploration_intensity_capdep_rank504d_base_v004_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sustained-expansion regime: fraction of last year capex/depamor sat above its 252d median
def f28cx_f28_capex_exploration_intensity_growthregime_base_v005_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    med = r.rolling(252, min_periods=126).median()
    growing = (r > med).astype(float)
    b = growing.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# excess (growth) capex over maintenance, normalized by PP&E base
def f28cx_f28_capex_exploration_intensity_excessppne_63d_base_v006_signal(capex, depamor, ppnenet):
    b = _f28_excess_over_ppne(capex, depamor, ppnenet)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# excess-capex/PP&E z-scored vs its own 252d history (growth-capex surprise)
def f28cx_f28_capex_exploration_intensity_excessppne_z252d_base_v007_signal(capex, depamor, ppnenet):
    r = _f28_excess_over_ppne(capex, depamor, ppnenet)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-capex funding of asset growth: excess capex (above maint) vs the 252d PP&E increment
def f28cx_f28_capex_exploration_intensity_growthshare_base_v008_signal(capex, depamor, ppnenet):
    excess = (capex - depamor)
    ppne_chg = (ppnenet - ppnenet.shift(252)).abs()
    b = excess / ppne_chg.replace(0, np.nan)
    result = b.clip(lower=-10.0, upper=10.0)
    return result.replace([np.inf, -np.inf], np.nan)


# growth-share acceleration: half-year change of growth-share-of-capex vs the prior half-year
def f28cx_f28_capex_exploration_intensity_growthshare_yoy_base_v009_signal(capex, depamor):
    excess = (capex - depamor).clip(lower=0)
    share = _mean(excess / capex.replace(0, np.nan), 21)
    b = (share - share.shift(126)) - (share.shift(126) - share.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor distance below its own 504d peak (build pullback from cycle high)
def f28cx_f28_capex_exploration_intensity_capdep_peakgap_base_v010_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    peak = _rmax(r, 504)
    b = r / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === EXPLORATION INTENSITY (rnd, NEVER /revenue) ===

# rnd/depamor exploration intensity scaled by maintenance run-rate, log level
def f28cx_f28_capex_exploration_intensity_rnddep_63d_base_v011_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    b = np.log1p(r.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/depamor z-scored vs own 252d history (exploration burst de-trended)
def f28cx_f28_capex_exploration_intensity_rnddep_z252d_base_v012_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/capex exploration-vs-development mix: displacement from its slow EMA (mix shift, not level)
def f28cx_f28_capex_exploration_intensity_rndcap_63d_base_v013_signal(rnd, capex):
    r = _f28_rnd_capex(rnd, capex)
    b = r - r.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/capex percentile-rank vs 504d (explorer-vs-developer cycle position)
def f28cx_f28_capex_exploration_intensity_rndcap_rank504d_base_v014_signal(rnd, capex):
    r = _f28_rnd_capex(rnd, capex)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# exploration share of discretionary investment: rnd/(capex+rnd) relative to its 1260d mean (regime tilt)
def f28cx_f28_capex_exploration_intensity_explshare_63d_base_v015_signal(capex, rnd):
    share = _f28_explore_share(capex, rnd)
    base = share.rolling(1260, min_periods=252).mean()
    b = share - base
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# exploration-share short-vs-long ratio (explorer mix ramp regime)
def f28cx_f28_capex_exploration_intensity_explshare_slratio_base_v016_signal(capex, rnd):
    share = _f28_explore_share(capex, rnd)
    short = _mean(share, 63)
    long = _mean(share, 252)
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/ppnenet exploration vs installed base (greenfield-vs-built tilt), rank vs 504d
def f28cx_f28_capex_exploration_intensity_rndppne_rank504d_base_v017_signal(rnd, ppnenet):
    r = rnd / ppnenet.replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# high-exploration regime: fraction of last year rnd/depamor above its 252d median
def f28cx_f28_capex_exploration_intensity_explregime_base_v018_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    med = r.rolling(252, min_periods=126).median()
    above = (r > med).astype(float)
    b = above.rolling(252, min_periods=126).mean() + 0.2 * np.tanh(_z(r, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# exploration-cut streak: consecutive periods of falling smoothed rnd/depamor
def f28cx_f28_capex_exploration_intensity_explcut_streak_base_v019_signal(rnd, depamor):
    r = _mean(_f28_rnd_depamor(rnd, depamor), 63)
    falling = (r < r.shift(21)).astype(float)
    grp = (falling != falling.shift(1)).cumsum()
    streak = falling.groupby(grp).cumsum() * falling
    b = streak / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/depamor distance above its 504d trough (exploration revival)
def f28cx_f28_capex_exploration_intensity_rnddep_troughgap_base_v020_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    trough = _rmin(r, 504)
    b = r / trough.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === INVESTING-CASH INTENSITY (-ncfi), scaled by depamor (NOT assets, to avoid f40/f30) ===

# -ncfi/depamor investing-deployment multiple (cash deployed vs maintenance run-rate)
def f28cx_f28_capex_exploration_intensity_ncfidep_63d_base_v021_signal(ncfi, depamor):
    b = _f28_invest_intensity(ncfi, depamor)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# -ncfi/depamor z-scored vs own 252d history (investing-deploy regime)
def f28cx_f28_capex_exploration_intensity_ncfidep_z252d_base_v022_signal(ncfi, depamor):
    r = _f28_invest_intensity(ncfi, depamor)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investing outflow regime: fraction of last year -ncfi deployment ran above its 252d median
def f28cx_f28_capex_exploration_intensity_outflowregime_base_v023_signal(ncfi):
    deploy = -ncfi
    med = deploy.rolling(252, min_periods=126).median()
    heavy = (deploy > med).astype(float)
    b = heavy.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investing-flow swing amplitude: 252d range of ncfi/depamor (lumpy deal-driven deployment)
def f28cx_f28_capex_exploration_intensity_ncfi_swing_base_v024_signal(ncfi, depamor):
    r = ncfi / depamor.replace(0, np.nan)
    b = _rmax(r, 252) - _rmin(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inorganic investing share displacement: inorganic-share-of-investing minus its slow EMA
def f28cx_f28_capex_exploration_intensity_inorganic_base_v025_signal(ncfi, capex, depamor):
    deployed = ncfi.abs()
    share = (deployed - capex).clip(lower=0) / deployed.replace(0, np.nan)
    b = share - share.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex share of total investing magnitude: capex / (capex + |ncfi|) (organic-vs-total, bounded)
def f28cx_f28_capex_exploration_intensity_organicshare_base_v026_signal(capex, ncfi):
    outflow = ncfi.abs()
    b = (capex / (capex + outflow).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investing-cash intensity rank vs 1260d (multi-year deployment-cycle position)
def f28cx_f28_capex_exploration_intensity_ncfi_rank1260_base_v027_signal(ncfi, depamor):
    r = _f28_invest_intensity(ncfi, depamor)
    b = r.rolling(1260, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inorganic-tilt momentum: half-year change in (-ncfi-capex)/depamor (deal-cycle shift)
def f28cx_f28_capex_exploration_intensity_inorganic_mom_base_v028_signal(ncfi, capex, depamor):
    tilt = (-ncfi - capex) / depamor.replace(0, np.nan)
    sm = _mean(tilt, 63)
    b = sm - sm.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of investing-deploy surges: entries into top-quartile -ncfi/depamor over a year
def f28cx_f28_capex_exploration_intensity_deploycount_base_v029_signal(ncfi, depamor):
    r = _f28_invest_intensity(ncfi, depamor)
    q75 = r.rolling(504, min_periods=126).quantile(0.75)
    hot = (r >= q75).astype(float)
    entries = ((hot == 1) & (hot.shift(1) == 0)).astype(float)
    b = entries.rolling(252, min_periods=126).sum() + hot.rolling(63, min_periods=21).mean() + 0.5 * _z(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investing-deploy acceleration: change in -ncfi/depamor over a half-year vs prior half
def f28cx_f28_capex_exploration_intensity_deployaccel_base_v030_signal(ncfi, depamor):
    intens = _f28_invest_intensity(ncfi, depamor)
    sm = _mean(intens, 63)
    b = (sm - sm.shift(126)) - (sm.shift(126) - sm.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === ASSET AGING vs REINVESTMENT (depamor/ppnenet gate) ===

# asset-aging rate: depamor/ppnenet, log level (high = old/short-life asset base)
def f28cx_f28_capex_exploration_intensity_aging_63d_base_v031_signal(depamor, ppnenet):
    r = _f28_age(depamor, ppnenet)
    b = np.log1p(r.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net capacity expansion position: (capex-depamor)/ppnenet percentile-ranked vs 1260d (cycle phase)
def f28cx_f28_capex_exploration_intensity_buildvsdecay_base_v032_signal(capex, depamor, ppnenet):
    r = _f28_capex_age(capex, depamor, ppnenet)
    b = r.rolling(1260, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-expansion rising regime: fraction of last year net (capex-depamor)/ppnenet rose vs a month ago
def f28cx_f28_capex_exploration_intensity_buildvsdecay_z_base_v033_signal(capex, depamor, ppnenet):
    r = _mean(_f28_capex_age(capex, depamor, ppnenet), 21)
    rising = (r > r.shift(21)).astype(float)
    b = rising.rolling(252, min_periods=126).mean() + 0.25 * np.tanh(_z(r, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging-rate trend: change in depamor/ppnenet over a year (asset base aging/refreshing)
def f28cx_f28_capex_exploration_intensity_aging_yoy_base_v034_signal(depamor, ppnenet):
    r = _f28_age(depamor, ppnenet)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-expansion regime: fraction of last year net (capex-depamor)/ppnenet sat above its 252d median
def f28cx_f28_capex_exploration_intensity_expandregime_base_v035_signal(capex, depamor, ppnenet):
    net = _f28_capex_age(capex, depamor, ppnenet)
    med = net.rolling(252, min_periods=126).median()
    net_grow = (net > med).astype(float)
    b = net_grow.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === EXCESS-CAPEX DYNAMICS / SPREADS ===

# excess-capex over maintenance: capex/depamor minus 1, smoothed, ranked vs 504d
def f28cx_f28_capex_exploration_intensity_excessmult_rank_base_v036_signal(capex, depamor):
    r = _mean(_f28_capex_depamor(capex, depamor) - 1.0, 63)
    b = r.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# development-vs-exploration tilt: (capex - rnd) per depamor (build-heavy vs explore-heavy)
def f28cx_f28_capex_exploration_intensity_devexpl_tilt_base_v037_signal(capex, rnd, depamor):
    b = (capex - rnd) / depamor.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total discretionary investment vs maintenance: (capex+rnd)/depamor, log level
def f28cx_f28_capex_exploration_intensity_totinvdep_base_v038_signal(capex, rnd, depamor):
    tot = capex + rnd
    r = tot / depamor.replace(0, np.nan)
    b = np.log(r.clip(lower=1e-6))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# (capex+rnd)/depamor total-investment-vs-maintenance: z-scored vs 504d AND less the capex-only z
# (isolates the exploration contribution to total-investment intensity)
def f28cx_f28_capex_exploration_intensity_totinvdep_rank1260_base_v039_signal(capex, rnd, depamor):
    tot_z = _z((capex + rnd) / depamor.replace(0, np.nan), 504)
    cap_z = _z(capex / depamor.replace(0, np.nan), 504)
    b = tot_z - cap_z
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# explore-vs-build divergence MOMENTUM: YoY change in rnd/(capex+rnd+depamor)-style greenfield weight
def f28cx_f28_capex_exploration_intensity_explbuilddiv_base_v040_signal(rnd, capex, depamor):
    weight = rnd / (capex + rnd + depamor).replace(0, np.nan)
    b = weight - weight.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === CAPEX BURST / PAUSE REGIMES (depamor-normalized magnitude) ===

# capex burst flag intensity: capex/depamor far above its 252d norm (build surge)
def f28cx_f28_capex_exploration_intensity_burst_base_v041_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    z = _z(r, 252)
    burst = (z > 1.0).astype(float)
    b = burst.rolling(252, min_periods=126).mean() + 0.25 * np.tanh(z)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex pause flag intensity: capex/depamor far below its 252d norm (build pause)
def f28cx_f28_capex_exploration_intensity_pause_base_v042_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    z = _z(r, 252)
    pause = (z < -1.0).astype(float)
    b = pause.rolling(252, min_periods=126).mean() - 0.25 * np.tanh(z)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-build streak length: consecutive periods of rising smoothed capex/depamor
def f28cx_f28_capex_exploration_intensity_buildstreak_base_v043_signal(capex, depamor):
    r = _mean(_f28_capex_depamor(capex, depamor), 63)
    rising = (r > r.shift(21)).astype(float)
    grp = (rising != rising.shift(1)).cumsum()
    streak = rising.groupby(grp).cumsum() * rising
    b = streak / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of build-surge entries over a year (boom-spend tally, depamor-normalized)
def f28cx_f28_capex_exploration_intensity_surgecount_base_v044_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    sm = _mean(r, 21)
    g = sm / sm.shift(63).replace(0, np.nan) - 1.0
    surge = (g > 0.15).astype(float)
    entries = ((surge == 1) & (surge.shift(1) == 0)).astype(float)
    b = entries.rolling(252, min_periods=126).sum() + g.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of capex/depamor from mid of its 504d range (build cycle-phase distance)
def f28cx_f28_capex_exploration_intensity_capdep_cycdist_base_v045_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    hi = _rmax(r, 504)
    lo = _rmin(r, 504)
    mid = (hi + lo) / 2.0
    b = (r - mid) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === CAPEX & RND GROWTH / ACCELERATION (self-normalized, NOT raw capex growth = f40) ===

# capex/depamor year-over-year change (growth-stance drift through cycle)
def f28cx_f28_capex_exploration_intensity_capdep_yoy_base_v046_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/depamor year-over-year change (exploration-stance drift)
def f28cx_f28_capex_exploration_intensity_rnddep_yoy_base_v047_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# exploration-vs-development growth divergence: rnd growth minus capex growth (YoY)
def f28cx_f28_capex_exploration_intensity_explgrowthdiv_base_v048_signal(rnd, capex):
    rsm = _mean(rnd, 63)
    csm = _mean(capex, 63)
    rg = np.log(rsm.replace(0, np.nan) / rsm.shift(252).replace(0, np.nan))
    cg = np.log(csm.replace(0, np.nan) / csm.shift(252).replace(0, np.nan))
    b = rg - cg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-capex acceleration: 2nd difference of (capex-depamor)/ppnenet over quarters
def f28cx_f28_capex_exploration_intensity_excessaccel_base_v049_signal(capex, depamor, ppnenet):
    r = _mean(_f28_excess_over_ppne(capex, depamor, ppnenet), 21)
    b = r - 2.0 * r.shift(63) + r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-investment-vs-maintenance acceleration: 2nd diff of (capex+rnd)/depamor
def f28cx_f28_capex_exploration_intensity_totinvaccel_base_v050_signal(capex, rnd, depamor):
    tot = capex + rnd
    r = _mean(tot / depamor.replace(0, np.nan), 21)
    b = r - 2.0 * r.shift(63) + r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === DISPERSION / VOLATILITY OF INTENSITY (depamor-normalized) ===

# capex/depamor volatility over a year (lumpy growth-capex program)
def f28cx_f28_capex_exploration_intensity_capdep_vol_base_v051_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    b = _std(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside lumpiness of capex/depamor: semi-deviation of below-mean build periods (cut-risk)
def f28cx_f28_capex_exploration_intensity_capdep_cv_base_v052_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    mu = _mean(r, 252)
    downdev = (r - mu).clip(upper=0).pow(2)
    b = np.sqrt(downdev.rolling(252, min_periods=126).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/depamor volatility (exploration-spend lumpiness)
def f28cx_f28_capex_exploration_intensity_rnddep_vol_base_v053_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    b = _std(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investing-deployment lumpiness, scale-free: coefficient of variation of -ncfi/depamor
def f28cx_f28_capex_exploration_intensity_ncfi_vol_base_v054_signal(ncfi, depamor):
    r = _f28_invest_intensity(ncfi, depamor)
    b = _std(r, 252) / _mean(r, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion across the three intensity ranks (capex/dep, rnd/dep, -ncfi/dep)
def f28cx_f28_capex_exploration_intensity_multidisp_base_v055_signal(capex, rnd, ncfi, depamor):
    a = _rank(_f28_capex_depamor(capex, depamor), 252)
    b2 = _rank(_f28_rnd_depamor(rnd, depamor), 252)
    c = _rank(_f28_invest_intensity(ncfi, depamor), 252)
    b = pd.concat([a, b2, c], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === EWM / DISPLACEMENT FACETS (depamor-normalized) ===

# capex/depamor minus its slow EMA (growth-stance displacement)
def f28cx_f28_capex_exploration_intensity_capdep_disp_base_v056_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    b = r - r.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rnd/depamor minus its slow EMA (exploration-burst displacement)
def f28cx_f28_capex_exploration_intensity_rnddep_disp_base_v057_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    b = r - r.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# excess-capex/PP&E smoothed via EMA (persistent net-expansion rate)
def f28cx_f28_capex_exploration_intensity_excess_ema_base_v058_signal(capex, depamor, ppnenet):
    r = _f28_excess_over_ppne(capex, depamor, ppnenet)
    b = r.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# -ncfi/depamor minus its slow EMA (investing-deploy displacement)
def f28cx_f28_capex_exploration_intensity_ncfidep_disp_base_v059_signal(ncfi, depamor):
    r = _f28_invest_intensity(ncfi, depamor)
    b = r - r.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-investment/depamor EWM fast-vs-slow gap (trend-slope proxy)
def f28cx_f28_capex_exploration_intensity_totinv_emagap_base_v060_signal(capex, rnd, depamor):
    tot = capex + rnd
    r = tot / depamor.replace(0, np.nan)
    b = r.ewm(span=42, min_periods=21).mean() - r.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === INTERACTION / SIGN-MAGNITUDE FACETS ===

# growth-stance x build-momentum interaction (capex/depamor scaled by its recent change)
def f28cx_f28_capex_exploration_intensity_capdep_mom_int_base_v061_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    mom = r - r.shift(126)
    b = np.sign(mom) * (r.clip(lower=0) * mom.abs()) ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# explorer pre-producer signature: exploration burst gated by build being low vs its own history
def f28cx_f28_capex_exploration_intensity_explorergate_base_v062_signal(rnd, capex, depamor):
    expl_z = _z(_f28_rnd_depamor(rnd, depamor), 126)
    capdep = _f28_capex_depamor(capex, depamor)
    build_low = (0.5 - capdep.rolling(504, min_periods=126).rank(pct=True))  # high when build near its multi-yr low
    b = expl_z * build_low
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed short-horizon capex/depamor surprise vs 63d norm (bounded build surprise)
def f28cx_f28_capex_exploration_intensity_capdep_tanh_base_v063_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    z = _z(r, 63)
    b = np.tanh(z)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# build-vs-explore tilt regime: fraction of last year (capex-rnd)/depamor sat above its 252d median
def f28cx_f28_capex_exploration_intensity_buildvsexpl_signmag_base_v064_signal(capex, rnd, depamor):
    d = (capex - rnd) / depamor.replace(0, np.nan)
    med = d.rolling(252, min_periods=126).median()
    build_heavy = (d > med).astype(float)
    b = build_heavy.rolling(252, min_periods=126).mean() + 0.2 * np.tanh(_z(d, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-expansion x acceleration interaction (compounding build signal, build-vs-decay)
def f28cx_f28_capex_exploration_intensity_expand_accel_int_base_v065_signal(capex, depamor, ppnenet):
    r = _f28_capex_age(capex, depamor, ppnenet)
    accel = r - 2.0 * r.shift(63) + r.shift(126)
    b = np.tanh(10.0 * r) * np.sign(accel) * accel.abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === LONG-HORIZON / CYCLE FACETS ===

# capex/depamor z-scored against a long 504d baseline (deep-cycle growth-stance)
def f28cx_f28_capex_exploration_intensity_capdep_z504d_base_v066_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    b = _z(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex/depamor rank vs 1260d (multi-year build-vs-maintain cycle position)
def f28cx_f28_capex_exploration_intensity_capdep_rank1260_base_v067_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    b = r.rolling(1260, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# over-build stretch LEVEL: capex/depamor relative to its 1260d mean (multi-year over/under-build)
def f28cx_f28_capex_exploration_intensity_overbuild_dist_base_v068_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    base = r.rolling(1260, min_periods=252).mean()
    b = r / base.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# exploration-program stretch: rnd/depamor relative to its 1260d mean
def f28cx_f28_capex_exploration_intensity_overexpl_dist_base_v069_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    base = r.rolling(1260, min_periods=252).mean()
    b = r / base.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging-rate rank vs 1260d (multi-year asset-base-age position)
def f28cx_f28_capex_exploration_intensity_aging_rank1260_base_v070_signal(depamor, ppnenet):
    r = _f28_age(depamor, ppnenet)
    b = r.rolling(1260, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === COMPLETE 75 ===

# above-norm build streak: consecutive periods capex/depamor stays above its 252d median
def f28cx_f28_capex_exploration_intensity_coveragestreak_base_v071_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    med = r.rolling(252, min_periods=63).median()
    covers = (r >= med).astype(float)
    grp = (covers != covers.shift(1)).cumsum()
    streak = covers.groupby(grp).cumsum() * covers
    b = streak / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# exploration-vs-development growth ratio level: rnd/capex smoothed and z-scored
def f28cx_f28_capex_exploration_intensity_rndcap_z252d_base_v072_signal(rnd, capex):
    r = _f28_rnd_capex(rnd, capex)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investing-deployment smoothed and ranked vs 504d (deployment-cycle position)
def f28cx_f28_capex_exploration_intensity_ncfi_smoothrank_base_v073_signal(ncfi, depamor):
    r = _mean(_f28_invest_intensity(ncfi, depamor), 63)
    b = r.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# organic-funding coverage TREND: YoY change in organic-spend share of total investing magnitude
def f28cx_f28_capex_exploration_intensity_fundinggap_base_v074_signal(capex, rnd, ncfi, depamor):
    spend = (capex + rnd)
    share = spend / (spend + ncfi.abs()).replace(0, np.nan)
    b = _mean(share, 21) - _mean(share, 21).shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined intensity composite: avg rank of capex/dep, rnd/dep, -ncfi/dep
def f28cx_f28_capex_exploration_intensity_composite_rank_base_v075_signal(capex, rnd, ncfi, depamor):
    a = _rank(_f28_capex_depamor(capex, depamor), 504)
    b2 = _rank(_f28_rnd_depamor(rnd, depamor), 504)
    c = _rank(_f28_invest_intensity(ncfi, depamor), 504)
    b = (a + b2 + c) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f28cx_f28_capex_exploration_intensity_capdep_63d_base_v001_signal,
    f28cx_f28_capex_exploration_intensity_capdep_smooth63d_base_v002_signal,
    f28cx_f28_capex_exploration_intensity_capdep_z252d_base_v003_signal,
    f28cx_f28_capex_exploration_intensity_capdep_rank504d_base_v004_signal,
    f28cx_f28_capex_exploration_intensity_growthregime_base_v005_signal,
    f28cx_f28_capex_exploration_intensity_excessppne_63d_base_v006_signal,
    f28cx_f28_capex_exploration_intensity_excessppne_z252d_base_v007_signal,
    f28cx_f28_capex_exploration_intensity_growthshare_base_v008_signal,
    f28cx_f28_capex_exploration_intensity_growthshare_yoy_base_v009_signal,
    f28cx_f28_capex_exploration_intensity_capdep_peakgap_base_v010_signal,
    f28cx_f28_capex_exploration_intensity_rnddep_63d_base_v011_signal,
    f28cx_f28_capex_exploration_intensity_rnddep_z252d_base_v012_signal,
    f28cx_f28_capex_exploration_intensity_rndcap_63d_base_v013_signal,
    f28cx_f28_capex_exploration_intensity_rndcap_rank504d_base_v014_signal,
    f28cx_f28_capex_exploration_intensity_explshare_63d_base_v015_signal,
    f28cx_f28_capex_exploration_intensity_explshare_slratio_base_v016_signal,
    f28cx_f28_capex_exploration_intensity_rndppne_rank504d_base_v017_signal,
    f28cx_f28_capex_exploration_intensity_explregime_base_v018_signal,
    f28cx_f28_capex_exploration_intensity_explcut_streak_base_v019_signal,
    f28cx_f28_capex_exploration_intensity_rnddep_troughgap_base_v020_signal,
    f28cx_f28_capex_exploration_intensity_ncfidep_63d_base_v021_signal,
    f28cx_f28_capex_exploration_intensity_ncfidep_z252d_base_v022_signal,
    f28cx_f28_capex_exploration_intensity_outflowregime_base_v023_signal,
    f28cx_f28_capex_exploration_intensity_ncfi_swing_base_v024_signal,
    f28cx_f28_capex_exploration_intensity_inorganic_base_v025_signal,
    f28cx_f28_capex_exploration_intensity_organicshare_base_v026_signal,
    f28cx_f28_capex_exploration_intensity_ncfi_rank1260_base_v027_signal,
    f28cx_f28_capex_exploration_intensity_inorganic_mom_base_v028_signal,
    f28cx_f28_capex_exploration_intensity_deploycount_base_v029_signal,
    f28cx_f28_capex_exploration_intensity_deployaccel_base_v030_signal,
    f28cx_f28_capex_exploration_intensity_aging_63d_base_v031_signal,
    f28cx_f28_capex_exploration_intensity_buildvsdecay_base_v032_signal,
    f28cx_f28_capex_exploration_intensity_buildvsdecay_z_base_v033_signal,
    f28cx_f28_capex_exploration_intensity_aging_yoy_base_v034_signal,
    f28cx_f28_capex_exploration_intensity_expandregime_base_v035_signal,
    f28cx_f28_capex_exploration_intensity_excessmult_rank_base_v036_signal,
    f28cx_f28_capex_exploration_intensity_devexpl_tilt_base_v037_signal,
    f28cx_f28_capex_exploration_intensity_totinvdep_base_v038_signal,
    f28cx_f28_capex_exploration_intensity_totinvdep_rank1260_base_v039_signal,
    f28cx_f28_capex_exploration_intensity_explbuilddiv_base_v040_signal,
    f28cx_f28_capex_exploration_intensity_burst_base_v041_signal,
    f28cx_f28_capex_exploration_intensity_pause_base_v042_signal,
    f28cx_f28_capex_exploration_intensity_buildstreak_base_v043_signal,
    f28cx_f28_capex_exploration_intensity_surgecount_base_v044_signal,
    f28cx_f28_capex_exploration_intensity_capdep_cycdist_base_v045_signal,
    f28cx_f28_capex_exploration_intensity_capdep_yoy_base_v046_signal,
    f28cx_f28_capex_exploration_intensity_rnddep_yoy_base_v047_signal,
    f28cx_f28_capex_exploration_intensity_explgrowthdiv_base_v048_signal,
    f28cx_f28_capex_exploration_intensity_excessaccel_base_v049_signal,
    f28cx_f28_capex_exploration_intensity_totinvaccel_base_v050_signal,
    f28cx_f28_capex_exploration_intensity_capdep_vol_base_v051_signal,
    f28cx_f28_capex_exploration_intensity_capdep_cv_base_v052_signal,
    f28cx_f28_capex_exploration_intensity_rnddep_vol_base_v053_signal,
    f28cx_f28_capex_exploration_intensity_ncfi_vol_base_v054_signal,
    f28cx_f28_capex_exploration_intensity_multidisp_base_v055_signal,
    f28cx_f28_capex_exploration_intensity_capdep_disp_base_v056_signal,
    f28cx_f28_capex_exploration_intensity_rnddep_disp_base_v057_signal,
    f28cx_f28_capex_exploration_intensity_excess_ema_base_v058_signal,
    f28cx_f28_capex_exploration_intensity_ncfidep_disp_base_v059_signal,
    f28cx_f28_capex_exploration_intensity_totinv_emagap_base_v060_signal,
    f28cx_f28_capex_exploration_intensity_capdep_mom_int_base_v061_signal,
    f28cx_f28_capex_exploration_intensity_explorergate_base_v062_signal,
    f28cx_f28_capex_exploration_intensity_capdep_tanh_base_v063_signal,
    f28cx_f28_capex_exploration_intensity_buildvsexpl_signmag_base_v064_signal,
    f28cx_f28_capex_exploration_intensity_expand_accel_int_base_v065_signal,
    f28cx_f28_capex_exploration_intensity_capdep_z504d_base_v066_signal,
    f28cx_f28_capex_exploration_intensity_capdep_rank1260_base_v067_signal,
    f28cx_f28_capex_exploration_intensity_overbuild_dist_base_v068_signal,
    f28cx_f28_capex_exploration_intensity_overexpl_dist_base_v069_signal,
    f28cx_f28_capex_exploration_intensity_aging_rank1260_base_v070_signal,
    f28cx_f28_capex_exploration_intensity_coveragestreak_base_v071_signal,
    f28cx_f28_capex_exploration_intensity_rndcap_z252d_base_v072_signal,
    f28cx_f28_capex_exploration_intensity_ncfi_smoothrank_base_v073_signal,
    f28cx_f28_capex_exploration_intensity_fundinggap_base_v074_signal,
    f28cx_f28_capex_exploration_intensity_composite_rank_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_CAPEX_EXPLORATION_INTENSITY_REGISTRY_001_075 = REGISTRY


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

    print("OK f28_capex_exploration_intensity_base_001_075_claude: %d features pass" % n_features)
