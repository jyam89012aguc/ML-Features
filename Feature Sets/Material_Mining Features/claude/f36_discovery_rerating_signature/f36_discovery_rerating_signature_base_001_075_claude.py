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
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives: discovery / re-rating signature =====
# A junior re-rating combines THREE drivers, all required by the family row:
#   (1) BREAKOUT FROM BASE  — price clearing a prior consolidation high
#   (2) VOLUME SURGE        — dollar-volume blowing out vs its base
#   (3) VOLATILITY EXPANSION — range/return dispersion widening out of quiet
# These primitives express each driver; composite features multiply / blend them.

def _f36_dollar_vol(closeadj, volume):
    # dollar-volume = closeadj*volume (per spec, used on windows > 21d)
    return (closeadj * volume).astype(float)


def _f36_breakout(closeadj, w):
    # how far price sits above the PRIOR base high (excludes today): >0 means breakout
    prior_hi = closeadj.shift(1).rolling(w, min_periods=max(2, w // 2)).max()
    return closeadj / prior_hi.replace(0, np.nan) - 1.0


def _f36_base_pos(closeadj, w):
    # position within the consolidation base [0,1]; 1 = at top of the base
    hi = _rmax(closeadj, w)
    lo = _rmin(closeadj, w)
    return (closeadj - lo) / (hi - lo).replace(0, np.nan)


def _f36_vol_surge(closeadj, volume, w):
    # dollar-volume today vs its trailing base average (surge multiple, log)
    dv = _f36_dollar_vol(closeadj, volume)
    base = dv.rolling(w, min_periods=max(2, w // 2)).mean()
    return np.log(dv.replace(0, np.nan) / base.replace(0, np.nan))


def _f36_ret_vol(closeadj, w):
    # realized return volatility over w
    return closeadj.pct_change().rolling(w, min_periods=max(2, w // 2)).std()


def _f36_vol_expand(closeadj, short, long):
    # volatility expansion: short-window vol relative to long-window vol
    vs = _f36_ret_vol(closeadj, short)
    vl = _f36_ret_vol(closeadj, long)
    return vs / vl.replace(0, np.nan)


def _f36_range_atr(high, low, closeadj, w):
    # normalized true-ish range (intraday amplitude) per unit price
    rng = (high - low)
    return (rng.rolling(w, min_periods=max(2, w // 2)).mean()) / closeadj.replace(0, np.nan)


def _f36_thrust(closeadj, w):
    # price thrust: log return over w (re-rating momentum core)
    return np.log(closeadj.replace(0, np.nan) / closeadj.shift(w).replace(0, np.nan))


def _f36_squash(x):
    # bounded composite combiner
    return np.tanh(x)


# ============================================================
# ---- breakout-from-base core (driver 1) ----

# raw 63d breakout above the prior quarter base high
def f36dr_f36_discovery_rerating_signature_brk_63d_base_v001_signal(closeadj):
    b = _f36_breakout(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d breakout above prior half-year base high
def f36dr_f36_discovery_rerating_signature_brk_126d_base_v002_signal(closeadj):
    b = _f36_breakout(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d breakout above prior year base high (true discovery to new 52w high)
def f36dr_f36_discovery_rerating_signature_brk_252d_base_v003_signal(closeadj):
    b = _f36_breakout(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout extension z-scored vs its own quarter history (de-trended breakout)
def f36dr_f36_discovery_rerating_signature_brkz_126d_base_v004_signal(closeadj):
    raw = _f36_breakout(closeadj, 126)
    b = _z(raw, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# position inside the 63d base (how coiled at the top before the break)
def f36dr_f36_discovery_rerating_signature_basepos_63d_base_v005_signal(closeadj):
    b = _f36_base_pos(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# position inside the 252d base, percentile-ranked vs 504d history
def f36dr_f36_discovery_rerating_signature_baseposrnk_252d_base_v006_signal(closeadj):
    bp = _f36_base_pos(closeadj, 252)
    b = _rank(bp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout momentum: change in 126d breakout over a month (re-rating acceleration)
def f36dr_f36_discovery_rerating_signature_brkmom_126d_base_v007_signal(closeadj):
    raw = _f36_breakout(closeadj, 126)
    b = raw - raw.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# clean-break tally weighted by break depth: sum of positive break-extensions in last month
def f36dr_f36_discovery_rerating_signature_brkcount_63d_base_v008_signal(closeadj):
    prior_hi = closeadj.shift(1).rolling(63, min_periods=21).max()
    ext = (closeadj / prior_hi.replace(0, np.nan) - 1.0).clip(lower=0)
    b = ext.rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above base measured against the base's own width (break per unit consolidation)
def f36dr_f36_discovery_rerating_signature_brkwidth_126d_base_v009_signal(closeadj):
    prior_hi = closeadj.shift(1).rolling(126, min_periods=63).max()
    prior_lo = closeadj.shift(1).rolling(126, min_periods=63).min()
    width = (prior_hi - prior_lo) / prior_hi.replace(0, np.nan)
    brk = closeadj / prior_hi.replace(0, np.nan) - 1.0
    b = brk / width.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- volume-surge core (driver 2) ----

# dollar-volume surge multiple vs 63d base
def f36dr_f36_discovery_rerating_signature_vsurge_63d_base_v010_signal(closeadj, volume):
    b = _f36_vol_surge(closeadj, volume, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sustained dollar-volume surge: 21d-avg dollar-vol vs its 126d base (structural step)
def f36dr_f36_discovery_rerating_signature_vsurge_126d_base_v011_signal(closeadj, volume):
    dv = _f36_dollar_vol(closeadj, volume)
    smooth = dv.rolling(21, min_periods=10).mean()
    base = dv.rolling(126, min_periods=63).mean()
    b = np.log(smooth.replace(0, np.nan) / base.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5d-average dollar-volume surge vs 63d base (sustained surge, not a 1-day blip)
def f36dr_f36_discovery_rerating_signature_vsurge5_63d_base_v012_signal(closeadj, volume):
    dv = _f36_dollar_vol(closeadj, volume)
    short = dv.rolling(5, min_periods=3).mean()
    base = dv.rolling(63, min_periods=21).mean()
    b = np.log(short.replace(0, np.nan) / base.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge asymmetry: 5d up-day dollar-vol share minus down-day share (directional surge)
def f36dr_f36_discovery_rerating_signature_vsurgez_63d_base_v013_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f36_dollar_vol(closeadj, volume)
    upv = dv.where(ret > 0, 0.0).rolling(5, min_periods=3).sum()
    dnv = dv.where(ret < 0, 0.0).rolling(5, min_periods=3).sum()
    share = (upv - dnv) / (upv + dnv).replace(0, np.nan)
    surge = _f36_vol_surge(closeadj, volume, 63).clip(lower=0)
    b = share * surge
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-surge persistence: 21d-summed excess of dollar-vol above 2x its 63d base
def f36dr_f36_discovery_rerating_signature_vspersist_63d_base_v014_signal(closeadj, volume):
    dv = _f36_dollar_vol(closeadj, volume)
    base = dv.rolling(63, min_periods=21).mean()
    excess = (dv / base.replace(0, np.nan) - 2.0).clip(lower=0)
    b = excess.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-surge acceleration: 5d-avg share volume vs prior 5d-avg, scaled by 126d base
def f36dr_f36_discovery_rerating_signature_volturn_126d_base_v015_signal(volume):
    short = volume.rolling(5, min_periods=3).mean()
    base = volume.rolling(126, min_periods=63).mean()
    accel = (short - short.shift(5)) / base.replace(0, np.nan)
    b = accel
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume momentum: 21d avg dollar-vol vs 252d avg (re-rating in liquidity)
def f36dr_f36_discovery_rerating_signature_dvmom_252d_base_v016_signal(closeadj, volume):
    dv = _f36_dollar_vol(closeadj, volume)
    short = dv.rolling(21, min_periods=10).mean()
    long = dv.rolling(252, min_periods=126).mean()
    b = np.log(short.replace(0, np.nan) / long.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume percentile vs 252d history (where today's liquidity ranks)
def f36dr_f36_discovery_rerating_signature_dvrank_252d_base_v017_signal(closeadj, volume):
    dv = _f36_dollar_vol(closeadj, volume)
    b = _rank(dv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- volatility-expansion core (driver 3) ----

# return-vol expansion: 21d vol relative to 126d vol
def f36dr_f36_discovery_rerating_signature_volexp_21v126_base_v018_signal(closeadj):
    b = _f36_vol_expand(closeadj, 21, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-vol expansion: 5d vol relative to 63d vol (sharp expansion out of quiet)
def f36dr_f36_discovery_rerating_signature_volexp_5v63_base_v019_signal(closeadj):
    b = _f36_vol_expand(closeadj, 5, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday-range expansion: 21d avg (high-low)/close vs 126d avg
def f36dr_f36_discovery_rerating_signature_rngexp_21v126_base_v020_signal(high, low, closeadj):
    short = _f36_range_atr(high, low, closeadj, 21)
    long = _f36_range_atr(high, low, closeadj, 126)
    b = short / long.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volatility-expansion z-scored vs own history (de-trended expansion regime)
def f36dr_f36_discovery_rerating_signature_volexpz_21v126_base_v021_signal(closeadj):
    raw = _f36_vol_expand(closeadj, 21, 126)
    b = _z(raw, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime distance: current 21d vol minus its own 252d median level
def f36dr_f36_discovery_rerating_signature_volregime_252d_base_v022_signal(closeadj):
    v = _f36_ret_vol(closeadj, 21)
    med = v.rolling(252, min_periods=126).median()
    b = (v - med) / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range amplitude percentile vs 252d history (where current vol ranks)
def f36dr_f36_discovery_rerating_signature_rngrank_252d_base_v023_signal(high, low, closeadj):
    amp = _f36_range_atr(high, low, closeadj, 5)
    b = _rank(amp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger-style squeeze release: 21d vol now vs its own 126d minimum (out of squeeze)
def f36dr_f36_discovery_rerating_signature_squeezerel_base_v024_signal(closeadj):
    v = _f36_ret_vol(closeadj, 21)
    floor = v.rolling(126, min_periods=63).min()
    b = v / floor.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- COMPOSITE signatures: combine the THREE drivers ----

# discovery-spike signature: breakout x volume-surge x vol-expansion (63d base)
def f36dr_f36_discovery_rerating_signature_spike_63d_base_v025_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 63).clip(lower=0)
    vs = _f36_vol_surge(closeadj, volume, 63).clip(lower=0)
    ve = (_f36_vol_expand(closeadj, 21, 126) - 1.0).clip(lower=0)
    b = brk * vs * ve
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# discovery-spike signature, long-base variant: 252d breakout x 126d surge x 5v63 expansion
def f36dr_f36_discovery_rerating_signature_spike_126d_base_v026_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 252).clip(lower=0)
    vs = _f36_vol_surge(closeadj, volume, 126).clip(lower=0)
    ve = (_f36_vol_expand(closeadj, 5, 63) - 1.0).clip(lower=0)
    b = brk * vs * ve
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-bounded triple composite: standardized sum of the three drivers, squashed
def f36dr_f36_discovery_rerating_signature_tripleblend_base_v027_signal(closeadj, volume):
    brk = _z(_f36_breakout(closeadj, 126), 126)
    vs = _z(_f36_vol_surge(closeadj, volume, 63), 126)
    ve = _z(_f36_vol_expand(closeadj, 21, 126), 126)
    b = _f36_squash((brk + vs + ve) / 3.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# geometric-mean composite of the three drivers (all must be present to fire)
def f36dr_f36_discovery_rerating_signature_geomtriple_base_v028_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 126).clip(lower=0) + 1e-6
    vs = _f36_vol_surge(closeadj, volume, 63).clip(lower=0) + 1e-6
    ve = (_f36_vol_expand(closeadj, 21, 126) - 1.0).clip(lower=0) + 1e-6
    b = (brk * vs * ve) ** (1.0 / 3.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout x volume-surge interaction only (price-confirmed-by-liquidity, 63d)
def f36dr_f36_discovery_rerating_signature_brkvol_63d_base_v029_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 63)
    vs = _f36_vol_surge(closeadj, volume, 63)
    b = brk * vs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout x vol-expansion interaction only (price-confirmed-by-volatility, 126d)
def f36dr_f36_discovery_rerating_signature_brkvolat_126d_base_v030_signal(closeadj):
    brk = _f36_breakout(closeadj, 126)
    ve = _f36_vol_expand(closeadj, 21, 126) - 1.0
    b = brk * ve
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-surge x vol-expansion (energy without the price break yet — early discovery)
def f36dr_f36_discovery_rerating_signature_volvolat_63d_base_v031_signal(closeadj, volume):
    vs = _f36_vol_surge(closeadj, volume, 63)
    ve = _f36_vol_expand(closeadj, 5, 63) - 1.0
    b = vs * ve
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- sustained re-rating momentum (price thrust confirmed) ----

# 63d price thrust confirmed by dollar-volume surge (momentum x liquidity)
def f36dr_f36_discovery_rerating_signature_thrustconf_63d_base_v032_signal(closeadj, volume):
    thr = _f36_thrust(closeadj, 63)
    vs = _f36_vol_surge(closeadj, volume, 126).clip(lower=0)
    b = thr * (1.0 + vs)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d price thrust confirmed by vol expansion (durable re-rating)
def f36dr_f36_discovery_rerating_signature_thrustconf_126d_base_v033_signal(closeadj):
    thr = _f36_thrust(closeadj, 126)
    ve = (_f36_vol_expand(closeadj, 21, 252)).clip(lower=0)
    b = thr * ve
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sustained re-rating: 252d thrust scaled by fraction of year above prior 63d base
def f36dr_f36_discovery_rerating_signature_sustain_252d_base_v034_signal(closeadj):
    thr = _f36_thrust(closeadj, 252)
    prior_hi = closeadj.shift(1).rolling(63, min_periods=21).max()
    above = (closeadj > prior_hi).astype(float).rolling(252, min_periods=126).mean()
    b = thr * above
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# re-rating momentum quality: thrust per unit of drawdown-from-high (smooth ascent)
def f36dr_f36_discovery_rerating_signature_thrustqual_126d_base_v035_signal(closeadj):
    thr = _f36_thrust(closeadj, 126)
    hi = _rmax(closeadj, 126)
    dd = (hi - closeadj) / hi.replace(0, np.nan)
    pain = dd.rolling(63, min_periods=21).mean()
    b = thr / (pain + 0.05)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# thrust acceleration: 63d thrust now minus 63d thrust a quarter ago
def f36dr_f36_discovery_rerating_signature_thrustaccel_63d_base_v036_signal(closeadj):
    thr = _f36_thrust(closeadj, 63)
    b = thr - thr.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- more breakout facets ----

# breakout-in-risk-units momentum: how the 252d break/vol ratio changed over a quarter
def f36dr_f36_discovery_rerating_signature_brkrisk_252d_base_v037_signal(closeadj):
    brk = _f36_breakout(closeadj, 252)
    vol = _f36_ret_vol(closeadj, 63)
    ratio = brk / vol.replace(0, np.nan)
    b = ratio - ratio.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since the 252d base high was last exceeded (freshness of the breakout)
def f36dr_f36_discovery_rerating_signature_brkfresh_252d_base_v038_signal(closeadj):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    b = closeadj.rolling(252, min_periods=126).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tightness of the base before the break: inverse of 63d base width (coil)
def f36dr_f36_discovery_rerating_signature_coil_63d_base_v039_signal(closeadj):
    hi = _rmax(closeadj, 63)
    lo = _rmin(closeadj, 63)
    width = (hi - lo) / closeadj.replace(0, np.nan)
    b = 1.0 / (width + 0.02)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coiled-then-break composite: base tightness x current breakout magnitude
def f36dr_f36_discovery_rerating_signature_coilbreak_63d_base_v040_signal(closeadj):
    hi = _rmax(closeadj, 63)
    lo = _rmin(closeadj, 63)
    width = (hi - lo) / closeadj.replace(0, np.nan)
    tight = 1.0 / (width + 0.02)
    brk = _f36_breakout(closeadj, 63).clip(lower=0)
    b = tight * brk
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout spread: 63d breakout minus 252d breakout (short vs long base)
def f36dr_f36_discovery_rerating_signature_brkspr_63v252_base_v041_signal(closeadj):
    s = _f36_breakout(closeadj, 63)
    l = _f36_breakout(closeadj, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-base hugging: fraction of last month spent in top 20% of the 63d base
def f36dr_f36_discovery_rerating_signature_basehug_63d_base_v042_signal(closeadj):
    bp = _f36_base_pos(closeadj, 63)
    top = (bp >= 0.8).astype(float)
    b = top.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- more volume facets ----

# up-volume vs down-volume balance over a quarter (accumulation signature)
def f36dr_f36_discovery_rerating_signature_updownvol_63d_base_v043_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f36_dollar_vol(closeadj, volume)
    upv = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    dnv = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    b = (upv - dnv) / (upv + dnv).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# on-balance dollar-volume slope: 21d change in cumulative signed dollar-vol, normalized
def f36dr_f36_discovery_rerating_signature_obvslope_base_v044_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f36_dollar_vol(closeadj, volume)
    signed = np.sign(ret) * dv
    obv = signed.cumsum()
    base = dv.rolling(63, min_periods=21).mean()
    b = (obv - obv.shift(21)) / (21.0 * base.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume thrust: dollar-volume z-score multiplied by return sign (directional surge)
def f36dr_f36_discovery_rerating_signature_dirvol_63d_base_v045_signal(closeadj, volume):
    dv = _f36_dollar_vol(closeadj, volume)
    zdv = _z(dv, 63)
    ret5 = _f36_thrust(closeadj, 5)
    b = zdv * np.sign(ret5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity re-rating: 63d avg dollar-volume vs prior-year avg (structural step-up)
def f36dr_f36_discovery_rerating_signature_liqstep_base_v046_signal(closeadj, volume):
    dv = _f36_dollar_vol(closeadj, volume)
    recent = dv.rolling(63, min_periods=21).mean()
    prior = dv.shift(63).rolling(252, min_periods=126).mean()
    b = np.log(recent.replace(0, np.nan) / prior.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-spike intensity: quarter-summed excess of dollar-vol above 1.5x its 63d base
def f36dr_f36_discovery_rerating_signature_spikecount_63d_base_v047_signal(closeadj, volume):
    dv = _f36_dollar_vol(closeadj, volume)
    base = dv.rolling(63, min_periods=21).mean()
    excess = (dv / base.replace(0, np.nan) - 1.5).clip(lower=0)
    b = excess.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- more volatility facets ----

# range/return-vol expansion confirmed by directional thrust (true expansion, not chop)
def f36dr_f36_discovery_rerating_signature_dirvolat_21d_base_v048_signal(closeadj):
    ve = _f36_vol_expand(closeadj, 21, 126) - 1.0
    thr = _f36_thrust(closeadj, 21)
    b = ve * np.sign(thr) * thr.abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-up energy: avg of positive overnight-style daily up-moves over a month
def f36dr_f36_discovery_rerating_signature_upenergy_21d_base_v049_signal(closeadj):
    ret = closeadj.pct_change()
    up = ret.clip(lower=0)
    b = up.rolling(21, min_periods=10).mean() / _f36_ret_vol(closeadj, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# structural range expansion: 21d intraday range vs its own 252d-trailing range, logged
def f36dr_f36_discovery_rerating_signature_rngexpz_252d_base_v050_signal(high, low, closeadj):
    amp21 = _f36_range_atr(high, low, closeadj, 21)
    amp252 = _f36_range_atr(high, low, closeadj, 252)
    b = np.log(amp21.replace(0, np.nan) / amp252.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-of-range: how much the 21d range amplitude itself is widening (vol-of-vol)
def f36dr_f36_discovery_rerating_signature_volofvol_base_v051_signal(closeadj):
    v = _f36_ret_vol(closeadj, 21)
    b = v.rolling(63, min_periods=21).std() / v.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- richer composites & signatures ----

# full discovery signature: standardized triple product gated to fire only when all positive
def f36dr_f36_discovery_rerating_signature_sigfire_base_v052_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 126)
    vs = _f36_vol_surge(closeadj, volume, 63)
    ve = _f36_vol_expand(closeadj, 21, 126) - 1.0
    gate = ((brk > 0) & (vs > 0) & (ve > 0)).astype(float)
    mag = _z(brk, 126).fillna(0) + _z(vs, 126).fillna(0) + _z(ve, 126).fillna(0)
    b = gate * mag
    result = b.where(~closeadj.isna())
    return result.replace([np.inf, -np.inf], np.nan)


# weakest-link composite: min of the three standardized drivers (all-must-confirm)
def f36dr_f36_discovery_rerating_signature_minlink_base_v053_signal(closeadj, volume):
    brk = _z(_f36_breakout(closeadj, 126), 126)
    vs = _z(_f36_vol_surge(closeadj, volume, 63), 126)
    ve = _z(_f36_vol_expand(closeadj, 21, 126), 126)
    b = pd.concat([brk, vs, ve], axis=1).min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# strongest-driver composite: max of three standardized drivers (any-trigger discovery)
def f36dr_f36_discovery_rerating_signature_maxlink_base_v054_signal(closeadj, volume):
    brk = _z(_f36_breakout(closeadj, 126), 126)
    vs = _z(_f36_vol_surge(closeadj, volume, 63), 126)
    ve = _z(_f36_vol_expand(closeadj, 21, 126), 126)
    b = pd.concat([brk, vs, ve], axis=1).max(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# driver agreement: dispersion across the three standardized drivers (low = aligned)
def f36dr_f36_discovery_rerating_signature_agree_base_v055_signal(closeadj, volume):
    brk = _z(_f36_breakout(closeadj, 126), 126)
    vs = _z(_f36_vol_surge(closeadj, volume, 63), 126)
    ve = _z(_f36_vol_expand(closeadj, 21, 126), 126)
    b = pd.concat([brk, vs, ve], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signature persistence: quarter-mean of the gated composite intensity (depth-weighted)
def f36dr_f36_discovery_rerating_signature_sigpersist_base_v056_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 126)
    vs = _f36_vol_surge(closeadj, volume, 63)
    ve = _f36_vol_expand(closeadj, 21, 126) - 1.0
    gate = ((brk > 0) & (vs > 0) & (ve > 0)).astype(float)
    intensity = gate * (brk.clip(lower=0) + 0.3 * vs.clip(lower=0) + 0.3 * ve.clip(lower=0))
    b = intensity.rolling(63, min_periods=21).mean()
    result = b.where(~closeadj.isna())
    return result.replace([np.inf, -np.inf], np.nan)


# discovery onset: first-fire count blended with concurrent breakout depth (quarter)
def f36dr_f36_discovery_rerating_signature_onset_base_v057_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 126)
    vs = _f36_vol_surge(closeadj, volume, 63)
    ve = _f36_vol_expand(closeadj, 21, 126) - 1.0
    gate = ((brk > 0) & (vs > 0) & (ve > 0)).astype(float)
    onset = ((gate == 1) & (gate.shift(1) == 0)).astype(float)
    b = onset.rolling(63, min_periods=21).sum() + 5.0 * (gate * brk.clip(lower=0)).rolling(21, min_periods=10).mean()
    result = b.where(~closeadj.isna())
    return result.replace([np.inf, -np.inf], np.nan)


# re-rating maturity: thrust x signature-persistence (sustained confirmed move)
def f36dr_f36_discovery_rerating_signature_maturity_base_v058_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 126)
    vs = _f36_vol_surge(closeadj, volume, 63)
    ve = _f36_vol_expand(closeadj, 21, 126) - 1.0
    gate = ((brk > 0) & (vs > 0) & (ve > 0)).astype(float)
    persist = gate.rolling(63, min_periods=21).mean()
    thr = _f36_thrust(closeadj, 63)
    b = thr * persist
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-weighted breakout: breakout magnitude weighted by concurrent dollar-vol rank
def f36dr_f36_discovery_rerating_signature_vwbreak_126d_base_v059_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 126).clip(lower=0)
    dvr = _rank(_f36_dollar_vol(closeadj, volume), 126) + 0.5
    b = brk * dvr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion-weighted thrust: 21d thrust scaled by the vol-expansion ratio
def f36dr_f36_discovery_rerating_signature_ewthrust_21d_base_v060_signal(closeadj):
    thr = _f36_thrust(closeadj, 21)
    ve = _f36_vol_expand(closeadj, 5, 63)
    b = thr * ve
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rate of new-high creation: log-slope of the rolling 63d max (re-rating staircase)
def f36dr_f36_discovery_rerating_signature_newhirate_63d_base_v061_signal(closeadj):
    hi = _rmax(closeadj, 63)
    b = np.log(hi.replace(0, np.nan) / hi.shift(21).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout-with-volume divergence: price at new 63d high but volume NOT surging (suspect)
def f36dr_f36_discovery_rerating_signature_divergence_63d_base_v062_signal(closeadj, volume):
    brk = (_f36_breakout(closeadj, 63) > 0).astype(float)
    vs = _f36_vol_surge(closeadj, volume, 63)
    b = brk * (-vs)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# clean re-rating quality: thrust x up/down-volume balance (accumulation-confirmed)
def f36dr_f36_discovery_rerating_signature_accumthrust_base_v063_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f36_dollar_vol(closeadj, volume)
    upv = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    dnv = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    bal = (upv - dnv) / (upv + dnv).replace(0, np.nan)
    thr = _f36_thrust(closeadj, 63)
    b = thr * (0.5 + bal)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze-then-expand signature: was tight (low 21d vol vs 126d) then expanded — change
def f36dr_f36_discovery_rerating_signature_sqzexpand_base_v064_signal(closeadj):
    ratio = _f36_vol_expand(closeadj, 21, 126)
    b = ratio - ratio.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite intensity vs cross-time history: base-position x surge-rank product, ranked
def f36dr_f36_discovery_rerating_signature_intensity_base_v065_signal(closeadj, volume):
    bp = _f36_base_pos(closeadj, 252)
    dvr = _rank(_f36_dollar_vol(closeadj, volume), 252) + 0.5
    prod = bp * dvr
    b = _rank(prod, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-expansion confirmed breakout: intraday range widening AND price breaking out
def f36dr_f36_discovery_rerating_signature_rngbreak_63d_base_v066_signal(high, low, closeadj):
    brk = _f36_breakout(closeadj, 63).clip(lower=0)
    short = _f36_range_atr(high, low, closeadj, 5)
    long = _f36_range_atr(high, low, closeadj, 63)
    rexp = (short / long.replace(0, np.nan) - 1.0).clip(lower=0)
    b = brk * rexp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# discovery thrust in ATR units: 21d thrust scaled by inverse intraday range (move per vol)
def f36dr_f36_discovery_rerating_signature_thrustatr_21d_base_v067_signal(high, low, closeadj):
    thr = _f36_thrust(closeadj, 21)
    atr = _f36_range_atr(high, low, closeadj, 21)
    b = thr / (atr + 0.005)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sustained-momentum tally: count of weeks in last quarter with positive 5d thrust
def f36dr_f36_discovery_rerating_signature_upweeks_63d_base_v068_signal(closeadj):
    thr5 = _f36_thrust(closeadj, 5)
    up = (thr5 > 0).astype(float)
    b = up.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout extension above 126d base, smoothed (persistent re-rating level)
def f36dr_f36_discovery_rerating_signature_brkema_126d_base_v069_signal(closeadj):
    brk = _f36_breakout(closeadj, 126)
    b = brk.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-thrust interaction: dollar-vol momentum x price thrust (re-rating fuel)
def f36dr_f36_discovery_rerating_signature_liqthrust_base_v070_signal(closeadj, volume):
    dv = _f36_dollar_vol(closeadj, volume)
    dvmom = np.log(dv.rolling(21, min_periods=10).mean().replace(0, np.nan)
                   / dv.rolling(252, min_periods=126).mean().replace(0, np.nan))
    thr = _f36_thrust(closeadj, 63)
    b = dvmom * thr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# discovery breadth: average of the three standardized drivers (balanced composite)
def f36dr_f36_discovery_rerating_signature_breadth_base_v071_signal(closeadj, volume):
    brk = _z(_f36_breakout(closeadj, 63), 126)
    vs = _z(_f36_vol_surge(closeadj, volume, 126), 126)
    ve = _z(_f36_vol_expand(closeadj, 5, 63), 126)
    b = pd.concat([brk, vs, ve], axis=1).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-expansion regime entries: count of times 21d vol crossed above its 126d mean (quarter)
def f36dr_f36_discovery_rerating_signature_expentries_base_v072_signal(closeadj):
    v = _f36_ret_vol(closeadj, 21)
    mean126 = v.rolling(126, min_periods=63).mean()
    above = (v > mean126).astype(float)
    entries = ((above == 1) & (above.shift(1) == 0)).astype(float)
    b = entries.rolling(63, min_periods=21).sum() + above.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout-volume coincidence rate: fraction of breakout days that had a volume spike
def f36dr_f36_discovery_rerating_signature_coincide_63d_base_v073_signal(closeadj, volume):
    prior_hi = closeadj.shift(1).rolling(63, min_periods=21).max()
    brkday = (closeadj > prior_hi)
    dv = _f36_dollar_vol(closeadj, volume)
    base = dv.rolling(63, min_periods=21).mean()
    spike = dv > 2.0 * base
    coincide = (brkday & spike).astype(float)
    brkcount = brkday.astype(float).rolling(63, min_periods=21).sum()
    b = coincide.rolling(63, min_periods=21).sum() / brkcount.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# re-rating slope vs base: 252d thrust divided by trailing 252d realized vol (Sharpe-ish)
def f36dr_f36_discovery_rerating_signature_rerateSharpe_252d_base_v074_signal(closeadj):
    thr = _f36_thrust(closeadj, 252)
    vol = _f36_ret_vol(closeadj, 252) * np.sqrt(252.0)
    b = thr / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# full discovery composite, EMA-smoothed and bounded (headline signature level)
def f36dr_f36_discovery_rerating_signature_headline_base_v075_signal(closeadj, volume):
    brk = _z(_f36_breakout(closeadj, 126), 126)
    vs = _z(_f36_vol_surge(closeadj, volume, 63), 126)
    ve = _z(_f36_vol_expand(closeadj, 21, 126), 126)
    raw = _f36_squash((brk + vs + ve) / 3.0)
    b = raw.ewm(span=10, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f36dr_f36_discovery_rerating_signature_brk_63d_base_v001_signal,
    f36dr_f36_discovery_rerating_signature_brk_126d_base_v002_signal,
    f36dr_f36_discovery_rerating_signature_brk_252d_base_v003_signal,
    f36dr_f36_discovery_rerating_signature_brkz_126d_base_v004_signal,
    f36dr_f36_discovery_rerating_signature_basepos_63d_base_v005_signal,
    f36dr_f36_discovery_rerating_signature_baseposrnk_252d_base_v006_signal,
    f36dr_f36_discovery_rerating_signature_brkmom_126d_base_v007_signal,
    f36dr_f36_discovery_rerating_signature_brkcount_63d_base_v008_signal,
    f36dr_f36_discovery_rerating_signature_brkwidth_126d_base_v009_signal,
    f36dr_f36_discovery_rerating_signature_vsurge_63d_base_v010_signal,
    f36dr_f36_discovery_rerating_signature_vsurge_126d_base_v011_signal,
    f36dr_f36_discovery_rerating_signature_vsurge5_63d_base_v012_signal,
    f36dr_f36_discovery_rerating_signature_vsurgez_63d_base_v013_signal,
    f36dr_f36_discovery_rerating_signature_vspersist_63d_base_v014_signal,
    f36dr_f36_discovery_rerating_signature_volturn_126d_base_v015_signal,
    f36dr_f36_discovery_rerating_signature_dvmom_252d_base_v016_signal,
    f36dr_f36_discovery_rerating_signature_dvrank_252d_base_v017_signal,
    f36dr_f36_discovery_rerating_signature_volexp_21v126_base_v018_signal,
    f36dr_f36_discovery_rerating_signature_volexp_5v63_base_v019_signal,
    f36dr_f36_discovery_rerating_signature_rngexp_21v126_base_v020_signal,
    f36dr_f36_discovery_rerating_signature_volexpz_21v126_base_v021_signal,
    f36dr_f36_discovery_rerating_signature_volregime_252d_base_v022_signal,
    f36dr_f36_discovery_rerating_signature_rngrank_252d_base_v023_signal,
    f36dr_f36_discovery_rerating_signature_squeezerel_base_v024_signal,
    f36dr_f36_discovery_rerating_signature_spike_63d_base_v025_signal,
    f36dr_f36_discovery_rerating_signature_spike_126d_base_v026_signal,
    f36dr_f36_discovery_rerating_signature_tripleblend_base_v027_signal,
    f36dr_f36_discovery_rerating_signature_geomtriple_base_v028_signal,
    f36dr_f36_discovery_rerating_signature_brkvol_63d_base_v029_signal,
    f36dr_f36_discovery_rerating_signature_brkvolat_126d_base_v030_signal,
    f36dr_f36_discovery_rerating_signature_volvolat_63d_base_v031_signal,
    f36dr_f36_discovery_rerating_signature_thrustconf_63d_base_v032_signal,
    f36dr_f36_discovery_rerating_signature_thrustconf_126d_base_v033_signal,
    f36dr_f36_discovery_rerating_signature_sustain_252d_base_v034_signal,
    f36dr_f36_discovery_rerating_signature_thrustqual_126d_base_v035_signal,
    f36dr_f36_discovery_rerating_signature_thrustaccel_63d_base_v036_signal,
    f36dr_f36_discovery_rerating_signature_brkrisk_252d_base_v037_signal,
    f36dr_f36_discovery_rerating_signature_brkfresh_252d_base_v038_signal,
    f36dr_f36_discovery_rerating_signature_coil_63d_base_v039_signal,
    f36dr_f36_discovery_rerating_signature_coilbreak_63d_base_v040_signal,
    f36dr_f36_discovery_rerating_signature_brkspr_63v252_base_v041_signal,
    f36dr_f36_discovery_rerating_signature_basehug_63d_base_v042_signal,
    f36dr_f36_discovery_rerating_signature_updownvol_63d_base_v043_signal,
    f36dr_f36_discovery_rerating_signature_obvslope_base_v044_signal,
    f36dr_f36_discovery_rerating_signature_dirvol_63d_base_v045_signal,
    f36dr_f36_discovery_rerating_signature_liqstep_base_v046_signal,
    f36dr_f36_discovery_rerating_signature_spikecount_63d_base_v047_signal,
    f36dr_f36_discovery_rerating_signature_dirvolat_21d_base_v048_signal,
    f36dr_f36_discovery_rerating_signature_upenergy_21d_base_v049_signal,
    f36dr_f36_discovery_rerating_signature_rngexpz_252d_base_v050_signal,
    f36dr_f36_discovery_rerating_signature_volofvol_base_v051_signal,
    f36dr_f36_discovery_rerating_signature_sigfire_base_v052_signal,
    f36dr_f36_discovery_rerating_signature_minlink_base_v053_signal,
    f36dr_f36_discovery_rerating_signature_maxlink_base_v054_signal,
    f36dr_f36_discovery_rerating_signature_agree_base_v055_signal,
    f36dr_f36_discovery_rerating_signature_sigpersist_base_v056_signal,
    f36dr_f36_discovery_rerating_signature_onset_base_v057_signal,
    f36dr_f36_discovery_rerating_signature_maturity_base_v058_signal,
    f36dr_f36_discovery_rerating_signature_vwbreak_126d_base_v059_signal,
    f36dr_f36_discovery_rerating_signature_ewthrust_21d_base_v060_signal,
    f36dr_f36_discovery_rerating_signature_newhirate_63d_base_v061_signal,
    f36dr_f36_discovery_rerating_signature_divergence_63d_base_v062_signal,
    f36dr_f36_discovery_rerating_signature_accumthrust_base_v063_signal,
    f36dr_f36_discovery_rerating_signature_sqzexpand_base_v064_signal,
    f36dr_f36_discovery_rerating_signature_intensity_base_v065_signal,
    f36dr_f36_discovery_rerating_signature_rngbreak_63d_base_v066_signal,
    f36dr_f36_discovery_rerating_signature_thrustatr_21d_base_v067_signal,
    f36dr_f36_discovery_rerating_signature_upweeks_63d_base_v068_signal,
    f36dr_f36_discovery_rerating_signature_brkema_126d_base_v069_signal,
    f36dr_f36_discovery_rerating_signature_liqthrust_base_v070_signal,
    f36dr_f36_discovery_rerating_signature_breadth_base_v071_signal,
    f36dr_f36_discovery_rerating_signature_expentries_base_v072_signal,
    f36dr_f36_discovery_rerating_signature_coincide_63d_base_v073_signal,
    f36dr_f36_discovery_rerating_signature_rerateSharpe_252d_base_v074_signal,
    f36dr_f36_discovery_rerating_signature_headline_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F36_DISCOVERY_RERATING_SIGNATURE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0003, 0.035, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.01, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(8e5, 5e5, n)) + 1e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
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

    print("OK f36_discovery_rerating_signature_base_001_075_claude: %d features pass" % n_features)
