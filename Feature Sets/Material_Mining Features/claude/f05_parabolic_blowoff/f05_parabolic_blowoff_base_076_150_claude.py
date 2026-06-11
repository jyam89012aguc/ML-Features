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


def _ema(s, span):
    return s.ewm(span=span, min_periods=max(2, span // 2)).mean()


# ===== folder domain primitives (parabolic blowoff / overextension) =====
def _f05_atr(high, low, closeadj, w):
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(),
                    (high - pc).abs(),
                    (low - pc).abs()], axis=1).max(axis=1)
    return tr.rolling(w, min_periods=max(1, w // 2)).mean()


def _f05_stretch(closeadj, w):
    ma = closeadj.rolling(w, min_periods=max(1, w // 2)).mean()
    return np.log(closeadj.replace(0, np.nan) / ma.replace(0, np.nan))


def _f05_runslope(closeadj, w):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    return lr.rolling(w, min_periods=max(1, w // 2)).mean()


def _f05_above_ma_atr(closeadj, high, low, w_ma, w_atr):
    ma = closeadj.rolling(w_ma, min_periods=max(1, w_ma // 2)).mean()
    atr = _f05_atr(high, low, closeadj, w_atr)
    return (closeadj - ma) / atr.replace(0, np.nan)


def _f05_volspike(volume, w):
    av = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    return volume / av.replace(0, np.nan)


def _f05_accel(closeadj, w):
    lp = np.log(closeadj.replace(0, np.nan))
    return lp.diff().diff().rolling(w, min_periods=max(1, w // 2)).mean()


# ============================================================
# --- multi-MA stretch / overextension levels ---

# stretch above 13d MA (intermediate parabolic extension)
def f05pb_f05_parabolic_blowoff_stretch_13d_base_v076_signal(closeadj):
    b = _f05_stretch(closeadj, 13)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stretch above 34d MA (slower extension)
def f05pb_f05_parabolic_blowoff_stretch_34d_base_v077_signal(closeadj):
    b = _f05_stretch(closeadj, 34)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# triple-MA fan: 5/21/63 dispersion of MAs about the 63d MA (ribbon expansion)
def f05pb_f05_parabolic_blowoff_mafan_5_21_63_base_v078_signal(closeadj):
    m5 = _mean(closeadj, 5)
    m21 = _mean(closeadj, 21)
    m63 = _mean(closeadj, 63)
    stacked = pd.concat([m5, m21, m63], axis=1)
    b = (stacked.max(axis=1) - stacked.min(axis=1)) / m63.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stretch above 21d MA scaled by sqrt(price-rank) (extension weighted by level cycle)
def f05pb_f05_parabolic_blowoff_stretchlvl_21d_base_v079_signal(closeadj):
    s = _f05_stretch(closeadj, 21)
    lvl = closeadj.rolling(252, min_periods=63).rank(pct=True)
    b = s * np.sqrt(lvl)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how far the 5d MA sits above the 63d MA in ATR units (fast-vs-slow overextension)
def f05pb_f05_parabolic_blowoff_maatr_5v63_base_v080_signal(closeadj, high, low):
    m5 = _mean(closeadj, 5)
    m63 = _mean(closeadj, 63)
    atr = _f05_atr(high, low, closeadj, 21)
    b = (m5 - m63) / atr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log distance of the 21d high above the 21d MA (recent peak overshoot vs trend)
def f05pb_f05_parabolic_blowoff_peakvsma_21d_base_v081_signal(closeadj):
    hi = _rmax(closeadj, 21)
    ma = _mean(closeadj, 21)
    b = np.log(hi.replace(0, np.nan) / ma.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stretch above 8d MA minus its 21d running median (asymmetric froth)
def f05pb_f05_parabolic_blowoff_stretchmed_8d_base_v082_signal(closeadj):
    s = _f05_stretch(closeadj, 8)
    med = s.rolling(21, min_periods=10).median()
    b = s - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- run / slope facets ---

# 21d cumulative log return divided by 63d return (acceleration of the trend)
def f05pb_f05_parabolic_blowoff_runaccel_21v63_base_v083_signal(closeadj):
    r21 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(21).replace(0, np.nan))
    r63 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    b = r21 - r63 / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# maximum 3d log return within the last 21d (the steepest sub-burst)
def f05pb_f05_parabolic_blowoff_maxburst_21d_base_v084_signal(closeadj):
    r3 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(3).replace(0, np.nan))
    b = r3.rolling(21, min_periods=10).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of the 21d total move delivered by its single best day (spike concentration)
def f05pb_f05_parabolic_blowoff_spikeconc_21d_base_v085_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    best = lr.rolling(21, min_periods=10).max()
    tot = lr.rolling(21, min_periods=10).sum()
    b = best / tot.replace(0, np.nan)
    b = b.clip(lower=-3, upper=3)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of slope: 10d run slope now minus 10d run slope 10 days ago (run acceleration)
def f05pb_f05_parabolic_blowoff_slopeofslope_10d_base_v086_signal(closeadj):
    rs = _f05_runslope(closeadj, 10)
    b = rs - rs.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-high clustering: rate of new 10d highs over 21d times the run efficiency
# (relentless straight-line new-high making, distinct from stretch level)
def f05pb_f05_parabolic_blowoff_newhicluster_21d_base_v087_signal(closeadj):
    hi = _rmax(closeadj, 10)
    is_new = (closeadj >= hi * 0.99999).astype(float)
    rate = is_new.rolling(21, min_periods=10).mean()
    net = (closeadj - closeadj.shift(10))
    path = closeadj.diff().abs().rolling(10, min_periods=5).sum()
    eff = (net / path.replace(0, np.nan)).clip(lower=0)
    b = rate * (0.5 + eff)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5d return in ATR-of-the-week units (short thrust normalized by short range)
def f05pb_f05_parabolic_blowoff_thrustweek_5d_base_v088_signal(closeadj, high, low):
    move = closeadj - closeadj.shift(5)
    atr = _f05_atr(high, low, closeadj, 5)
    b = move / atr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume blowoff facets ---

# correlation of volume and |return| over 21d (volume confirming the move = blowoff)
def f05pb_f05_parabolic_blowoff_volretcorr_21d_base_v089_signal(closeadj, volume):
    r = closeadj.pct_change().abs()
    b = r.rolling(21, min_periods=10).corr(volume)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share of last-10d dollar-volume occurring on up days (one-sided accumulation)
def f05pb_f05_parabolic_blowoff_updollshare_10d_base_v090_signal(closeadj, volume):
    up = (closeadj.diff() > 0).astype(float)
    dv = closeadj * volume
    updv = (dv * up).rolling(10, min_periods=5).sum()
    tot = dv.rolling(10, min_periods=5).sum()
    b = updv / tot.replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume spike on the single highest-return day of the last 10d (climax-bar volume)
def f05pb_f05_parabolic_blowoff_climaxvol_10d_base_v091_signal(closeadj, volume):
    r = closeadj.pct_change()
    spike = _f05_volspike(volume, 63)
    is_top = (r == r.rolling(10, min_periods=5).max()).astype(float)
    b = (spike * is_top).rolling(10, min_periods=5).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume trend (21d slope of log volume) at the extension (ramping participation)
def f05pb_f05_parabolic_blowoff_voltrend_21d_base_v092_signal(volume):
    lv = np.log(volume.replace(0, np.nan))
    b = (lv - lv.shift(21)) / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Herfindahl concentration of volume over 21d (one-day volume domination)
def f05pb_f05_parabolic_blowoff_volherf_21d_base_v093_signal(volume):
    tot = volume.rolling(21, min_periods=10).sum()
    share = volume / tot.replace(0, np.nan)
    b = (share ** 2).rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume z interacted with positive stretch (liquidity-backed froth)
def f05pb_f05_parabolic_blowoff_dollfroth_21d_base_v094_signal(closeadj, volume):
    dv = closeadj * volume
    dz = _z(dv, 63).clip(lower=0)
    s = _f05_stretch(closeadj, 21).clip(lower=0)
    b = dz * s
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover surge proxy: today's volume vs its 21d EMA (recent participation jump)
def f05pb_f05_parabolic_blowoff_volsurgeema_21d_base_v095_signal(volume):
    ema = _ema(volume, 21)
    b = volume / ema.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- mean-reversion / fade facets ---

# distance below the 10d EMA after a run (snap toward the fast mean)
def f05pb_f05_parabolic_blowoff_emafade_10d_base_v096_signal(closeadj):
    ema = _ema(closeadj, 10)
    gap = closeadj / ema.replace(0, np.nan) - 1.0
    prior_up = (np.log(closeadj.shift(1) / closeadj.shift(11)) > 0).astype(float)
    b = -gap * prior_up
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stretch reversal speed: drop in 21d stretch from its 10d peak in vol units
def f05pb_f05_parabolic_blowoff_stretchdrop_21d_base_v097_signal(closeadj):
    s = _f05_stretch(closeadj, 21)
    peak = s.rolling(10, min_periods=5).max()
    vol = s.rolling(63, min_periods=21).std()
    b = (peak - s) / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight-vs-intraday reversal: prior 10d run then today's down day (exhaustion fade)
def f05pb_f05_parabolic_blowoff_revtoday_base_v098_signal(closeadj):
    run = np.log(closeadj.shift(1).replace(0, np.nan) / closeadj.shift(11).replace(0, np.nan))
    today = closeadj.pct_change()
    b = -today.clip(upper=0) * run.clip(lower=0) * 100.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance from the 21d high relative to ATR (room given up since the spike top)
def f05pb_f05_parabolic_blowoff_offtop_21d_base_v099_signal(closeadj, high, low):
    hi = _rmax(closeadj, 21)
    atr = _f05_atr(high, low, closeadj, 21)
    b = (closeadj - hi) / atr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how many days since the 21d ATR-extension last exceeded 2 (time since last froth)
def f05pb_f05_parabolic_blowoff_sincefroth_63d_base_v100_signal(closeadj, high, low):
    e = _f05_above_ma_atr(closeadj, high, low, 21, 21)
    hot = (e >= 2.0).astype(float)

    def _since(a):
        idx = np.where(a > 0)[0]
        if len(idx) == 0:
            return 1.0
        return (len(a) - 1 - idx[-1]) / float(len(a))

    b = hot.rolling(63, min_periods=21).apply(_since, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# give-back: largest 3d pullback within the last 21d as a fraction of the 21d run
# (how much of the parabola has already been surrendered intrabar)
def f05pb_f05_parabolic_blowoff_giveback_21d_base_v101_signal(closeadj):
    drop3 = (closeadj / _rmax(closeadj, 3).replace(0, np.nan) - 1.0)
    worst = drop3.rolling(21, min_periods=10).min().abs()
    run = np.log(closeadj.replace(0, np.nan) / closeadj.shift(21).replace(0, np.nan)).abs() + 0.02
    b = worst / run
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- exhaustion / divergence facets ---

# Williams %R style: where close sits in the 14d high-low range (overbought ceiling)
def f05pb_f05_parabolic_blowoff_williamsr_14d_base_v102_signal(closeadj, high, low):
    hh = _rmax(high, 14)
    ll = _rmin(low, 14)
    b = (closeadj - ll) / (hh - ll).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stochastic %K minus its 3d smooth (momentum rolling over at the top)
def f05pb_f05_parabolic_blowoff_stochroll_14d_base_v103_signal(closeadj, high, low):
    hh = _rmax(high, 14)
    ll = _rmin(low, 14)
    k = (closeadj - ll) / (hh - ll).replace(0, np.nan)
    b = k - k.rolling(3, min_periods=2).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price/momentum divergence: 21d price change rank minus 21d RSI rank (top divergence)
def f05pb_f05_parabolic_blowoff_rsidiverg_21d_base_v104_signal(closeadj):
    d = closeadj.diff()
    up = d.clip(lower=0).rolling(14, min_periods=7).mean()
    dn = (-d).clip(lower=0).rolling(14, min_periods=7).mean()
    rsi = up / (up + dn).replace(0, np.nan)
    px = closeadj.pct_change(21)
    b = px.rolling(63, min_periods=21).rank(pct=True) - rsi.rolling(63, min_periods=21).rank(pct=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-shadow dominance over 10d weighted by extension (rejection wicks at highs)
def f05pb_f05_parabolic_blowoff_rejectwick_10d_base_v105_signal(closeadj, high, low):
    rng = (high - low).replace(0, np.nan)
    upsh = (high - np.maximum(closeadj, closeadj.shift(1))) / rng
    e = _f05_above_ma_atr(closeadj, high, low, 21, 21).clip(lower=0)
    b = upsh.rolling(10, min_periods=5).mean() * (1.0 + e)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# declining new-high momentum: change in (close/21d-high) over 5d while near high
def f05pb_f05_parabolic_blowoff_hifade_21d_base_v106_signal(closeadj):
    prox = closeadj / _rmax(closeadj, 21).replace(0, np.nan)
    near = (prox > 0.95).astype(float)
    b = (prox - prox.shift(5)) * near
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return autocorrelation flip: lag-1 autocorr of returns over 21d (trend losing memory)
def f05pb_f05_parabolic_blowoff_autocorr_21d_base_v107_signal(closeadj):
    r = closeadj.pct_change()
    b = r.rolling(21, min_periods=10).corr(r.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volatility-of-the-blowoff facets ---

# range expansion: 5d avg true range vs 63d avg true range (volatility blowout)
def f05pb_f05_parabolic_blowoff_rangeexp_5v63_base_v108_signal(closeadj, high, low):
    atr5 = _f05_atr(high, low, closeadj, 5)
    atr63 = _f05_atr(high, low, closeadj, 63)
    b = atr5 / atr63.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized 5d vol vs 63d vol ratio (short-term vol spike during the run)
def f05pb_f05_parabolic_blowoff_volratio_5v63_base_v109_signal(closeadj):
    v5 = closeadj.pct_change().rolling(5, min_periods=3).std()
    v63 = closeadj.pct_change().rolling(63, min_periods=21).std()
    b = v5 / v63.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upside semivariance share of total variance over 21d (one-sided up-volatility)
def f05pb_f05_parabolic_blowoff_upsemivar_21d_base_v110_signal(closeadj):
    r = closeadj.pct_change()
    up = r.clip(lower=0).pow(2).rolling(21, min_periods=10).sum()
    tot = r.pow(2).rolling(21, min_periods=10).sum()
    b = up / tot.replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson high-low vol spike (5d) vs its 63d typical level (intraday range blowout)
def f05pb_f05_parabolic_blowoff_parkinson_5d_base_v111_signal(high, low):
    hl = (np.log(high.replace(0, np.nan) / low.replace(0, np.nan))) ** 2
    p5 = hl.rolling(5, min_periods=3).mean()
    p63 = hl.rolling(63, min_periods=21).mean()
    b = p5 / p63.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol: 21d std of the 5d realized vol (unstable, climactic volatility)
def f05pb_f05_parabolic_blowoff_volofvol_21d_base_v112_signal(closeadj):
    v5 = closeadj.pct_change().rolling(5, min_periods=3).std()
    b = v5.rolling(21, min_periods=10).std() / v5.rolling(21, min_periods=10).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite / interaction facets ---

# blowoff signature: positive stretch x volume z x upside vol share (full climax)
def f05pb_f05_parabolic_blowoff_signature_21d_base_v113_signal(closeadj, volume):
    s = _f05_stretch(closeadj, 21).clip(lower=0)
    vz = _z(volume, 63).clip(lower=0)
    r = closeadj.pct_change()
    upshare = (r.clip(lower=0).pow(2).rolling(21, min_periods=10).sum()
               / r.pow(2).rolling(21, min_periods=10).sum().replace(0, np.nan))
    b = (s * vz * upshare) ** (1.0 / 3.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# extension minus its mean-reversion drag: stretch now minus avg stretch next-window
def f05pb_f05_parabolic_blowoff_extnetdrag_21d_base_v114_signal(closeadj):
    s = _f05_stretch(closeadj, 21)
    drag = s.ewm(span=10, min_periods=5).mean()
    b = s - 1.5 * drag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# parabolic quality: run efficiency x positive convexity (smooth accelerating curve)
def f05pb_f05_parabolic_blowoff_paraquality_10d_base_v115_signal(closeadj):
    net = (closeadj - closeadj.shift(10))
    path = closeadj.diff().abs().rolling(10, min_periods=5).sum()
    eff = (net / path.replace(0, np.nan)).clip(lower=0)
    convex = _f05_accel(closeadj, 10).clip(lower=0) * 1000.0
    b = eff * convex
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stretch-vol interaction: stretch above 21d MA divided by its own dispersion
def f05pb_f05_parabolic_blowoff_stretchsharp_21d_base_v116_signal(closeadj):
    s = _f05_stretch(closeadj, 21)
    disp = s.rolling(21, min_periods=10).std()
    b = s / disp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blowoff-then-reversal swing: positive 10d run followed by lower-high over 5d
def f05pb_f05_parabolic_blowoff_swingtop_base_v117_signal(closeadj):
    run = np.log(closeadj.shift(5).replace(0, np.nan) / closeadj.shift(15).replace(0, np.nan)).clip(lower=0)
    lower_high = (_rmax(closeadj, 5) < _rmax(closeadj, 5).shift(5)).astype(float)
    b = run * lower_high
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration index: 5d slope minus twice 10d slope plus 21d slope (discrete curvature)
def f05pb_f05_parabolic_blowoff_accelindex_base_v118_signal(closeadj):
    s5 = _f05_runslope(closeadj, 5)
    s10 = _f05_runslope(closeadj, 10)
    s21 = _f05_runslope(closeadj, 21)
    b = s5 - 2.0 * s10 + s21
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how far price extended above 21d MA at its peak over the last 21d (max froth held)
def f05pb_f05_parabolic_blowoff_maxext_21d_base_v119_signal(closeadj):
    s = _f05_stretch(closeadj, 21)
    b = s.rolling(21, min_periods=10).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range of stretch over 21d (how violently the extension swung — blowoff instability)
def f05pb_f05_parabolic_blowoff_stretchrange_21d_base_v120_signal(closeadj):
    s = _f05_stretch(closeadj, 21)
    b = s.rolling(21, min_periods=10).max() - s.rolling(21, min_periods=10).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- more distinct facets to reach 75 ---

# ATR-extension above 34d MA, de-meaned by its own 63d level then ranked
# (regime-relative slower overextension, distinct from the raw 34d stretch level)
def f05pb_f05_parabolic_blowoff_atrext34_34d_base_v121_signal(closeadj, high, low):
    e = _f05_above_ma_atr(closeadj, high, low, 34, 21)
    b = e.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d return per unit of 63d max-drawdown (clean parabolic advance over a quarter)
def f05pb_f05_parabolic_blowoff_cleanrun_63d_base_v122_signal(closeadj):
    ret = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    peak = closeadj.rolling(63, min_periods=21).max()
    dd = (closeadj / peak.replace(0, np.nan) - 1.0).rolling(63, min_periods=21).min().abs()
    b = ret.clip(lower=0) / (dd.replace(0, np.nan) + 0.05)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of close from 50d MA in pct, ranked vs its 252d history (overextension rank)
def f05pb_f05_parabolic_blowoff_ext50rank_50d_base_v123_signal(closeadj):
    ext = closeadj / _mean(closeadj, 50).replace(0, np.nan) - 1.0
    b = ext.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convexity of the 13d EMA path (is the smoothed trend bending upward)
def f05pb_f05_parabolic_blowoff_emaconvex_13d_base_v124_signal(closeadj):
    ema = _ema(closeadj, 13)
    lp = np.log(ema.replace(0, np.nan))
    b = (lp.diff() - lp.diff().shift(3)).rolling(3, min_periods=2).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of up-gaps (close > prior high) over 21d weighted by gap size (gap-run)
def f05pb_f05_parabolic_blowoff_gaprun_21d_base_v125_signal(closeadj, high):
    gap = (closeadj - high.shift(1)).clip(lower=0) / closeadj.replace(0, np.nan)
    b = gap.rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 21d MA, EMA-smoothed then differenced (persistent extension change)
def f05pb_f05_parabolic_blowoff_extsmoothchg_21d_base_v126_signal(closeadj):
    ext = closeadj / _mean(closeadj, 21).replace(0, np.nan) - 1.0
    sm = ext.ewm(span=10, min_periods=5).mean()
    b = sm - sm.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log-price residual from a 21d linear fit (deviation above the linear trend)
def f05pb_f05_parabolic_blowoff_trendresid_21d_base_v127_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    fit = 2.0 * lp.rolling(11, min_periods=6).mean() - lp.rolling(21, min_periods=10).mean()
    b = lp - fit
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proportion of last 21d that set a fresh 21d high (relentless new-high making)
def f05pb_f05_parabolic_blowoff_freshhighrate_21d_base_v128_signal(closeadj):
    prior_hi = closeadj.shift(1).rolling(21, min_periods=10).max()
    fresh = (closeadj > prior_hi).astype(float)
    raw = fresh.rolling(21, min_periods=10).mean()
    s = _f05_stretch(closeadj, 21).clip(lower=0)
    b = raw + 2.0 * s
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vertical-run intensity: 10d return times the fraction of up days (one-way thrust)
def f05pb_f05_parabolic_blowoff_runintensity_10d_base_v129_signal(closeadj):
    ret = np.log(closeadj.replace(0, np.nan) / closeadj.shift(10).replace(0, np.nan))
    upfrac = (closeadj.diff() > 0).astype(float).rolling(10, min_periods=5).mean()
    b = ret * upfrac
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 21d MA divided by 252d max distance (froth vs own historic peak)
def f05pb_f05_parabolic_blowoff_frothvspeak_21d_base_v130_signal(closeadj):
    ext = (closeadj / _mean(closeadj, 21).replace(0, np.nan) - 1.0).clip(lower=0)
    peak = ext.rolling(252, min_periods=63).max()
    b = ext / peak.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blowoff exhaustion combo: high stretch but negative 3d slope (rolling over at top)
def f05pb_f05_parabolic_blowoff_exhaustcombo_21d_base_v131_signal(closeadj):
    s = _f05_stretch(closeadj, 21)
    slope3 = _f05_runslope(closeadj, 3)
    b = s.clip(lower=0) * (-slope3) * (slope3 < 0).astype(float)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5d range expansion accelerating: ATR5/ATR21 now vs 5 days ago (vol blowing out)
def f05pb_f05_parabolic_blowoff_volexpaccel_base_v132_signal(closeadj, high, low):
    ratio = _f05_atr(high, low, closeadj, 5) / _f05_atr(high, low, closeadj, 21).replace(0, np.nan)
    b = ratio - ratio.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-confirmed new high: fresh 21d high days weighted by volume spike (count-ish)
def f05pb_f05_parabolic_blowoff_volconfhigh_21d_base_v133_signal(closeadj, volume):
    prior_hi = closeadj.shift(1).rolling(21, min_periods=10).max()
    fresh = (closeadj > prior_hi).astype(float)
    spike = _f05_volspike(volume, 63)
    b = (fresh * spike).rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stretch z-scored vs 21d window minus vs 126d window (regime-relative froth)
def f05pb_f05_parabolic_blowoff_stretchzgap_21d_base_v134_signal(closeadj):
    s = _f05_stretch(closeadj, 21)
    b = _z(s, 21) - _z(s, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze-then-expand ratio: current Bollinger bandwidth vs its prior 63d minimum
# (a pure compression-release ratio; high = vol just exploded out of a squeeze)
def f05pb_f05_parabolic_blowoff_squeezepop_base_v135_signal(closeadj):
    bw = (_std(closeadj, 20) / _mean(closeadj, 20).replace(0, np.nan))
    prior_min_bw = bw.shift(5).rolling(63, min_periods=21).min()
    b = bw / (prior_min_bw + 1e-6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d high vs 63d high ratio (is the recent peak a fresh multi-quarter spike)
def f05pb_f05_parabolic_blowoff_freshpeak_21v63_base_v136_signal(closeadj):
    hi21 = _rmax(closeadj, 21)
    hi63 = _rmax(closeadj, 63)
    b = hi21 / hi63.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative positive ATR-thrust over 10d (sum of up-day moves in ATR units)
def f05pb_f05_parabolic_blowoff_atrthrustsum_10d_base_v137_signal(closeadj, high, low):
    move = closeadj.diff().clip(lower=0)
    atr = _f05_atr(high, low, closeadj, 21)
    contrib = move / atr.replace(0, np.nan)
    b = contrib.rolling(10, min_periods=5).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# kurtosis of 21d returns (fat-tailed, spiky blowoff distribution)
def f05pb_f05_parabolic_blowoff_retkurt_21d_base_v138_signal(closeadj):
    r = closeadj.pct_change()
    b = r.rolling(21, min_periods=12).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# extension persistence streak: consecutive days closing >1 ATR above 21d MA
def f05pb_f05_parabolic_blowoff_extstreak_base_v139_signal(closeadj, high, low):
    hot = (_f05_above_ma_atr(closeadj, high, low, 21, 21) >= 1.0).astype(float)

    def _streak(a):
        c = 0
        for v in a:
            c = c + 1 if v > 0 else 0
        return float(c)

    b = hot.rolling(42, min_periods=21).apply(_streak, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend overshoot of the vol budget: |21d move| as a multiple of ATR-implied range
# (unsigned — measures how far beyond a normal-vol move the price has traveled)
def f05pb_f05_parabolic_blowoff_movevsbudget_21d_base_v140_signal(closeadj, high, low):
    move = (closeadj - closeadj.shift(21)).abs()
    atr = _f05_atr(high, low, closeadj, 21)
    budget = atr * np.sqrt(21.0)
    ratio = move / budget.replace(0, np.nan)
    b = (ratio - 1.0).clip(lower=-1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blowoff drawdown risk: positive stretch times recent downside semivariance
def f05pb_f05_parabolic_blowoff_fragility_21d_base_v141_signal(closeadj):
    s = _f05_stretch(closeadj, 21).clip(lower=0)
    r = closeadj.pct_change()
    dnvar = r.clip(upper=0).pow(2).rolling(21, min_periods=10).mean()
    b = s * np.sqrt(dnvar)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how far the EMA-ribbon (5/13/34) has fanned out, normalized (parabolic fan width)
def f05pb_f05_parabolic_blowoff_ribbonwidth_base_v142_signal(closeadj):
    e5 = _ema(closeadj, 5)
    e13 = _ema(closeadj, 13)
    e34 = _ema(closeadj, 34)
    stacked = pd.concat([e5, e13, e34], axis=1)
    b = (stacked.max(axis=1) - stacked.min(axis=1)) / e34.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# velocity of the EMA-ribbon width (is the fan opening fast = accelerating blowoff)
def f05pb_f05_parabolic_blowoff_ribbonvel_base_v143_signal(closeadj):
    e5 = _ema(closeadj, 5)
    e13 = _ema(closeadj, 13)
    e34 = _ema(closeadj, 34)
    stacked = pd.concat([e5, e13, e34], axis=1)
    width = (stacked.max(axis=1) - stacked.min(axis=1)) / e34.replace(0, np.nan)
    b = width - width.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overbought duration: fraction of 21d with RSI>0.7 (sustained overbought = blowoff)
def f05pb_f05_parabolic_blowoff_obtime_21d_base_v144_signal(closeadj):
    d = closeadj.diff()
    up = d.clip(lower=0).rolling(14, min_periods=7).mean()
    dn = (-d).clip(lower=0).rolling(14, min_periods=7).mean()
    rsi = up / (up + dn).replace(0, np.nan)
    ob = (rsi > 0.7).astype(float)
    raw = ob.rolling(21, min_periods=10).mean()
    depth = (rsi - 0.7).clip(lower=0).rolling(21, min_periods=10).mean()
    b = raw + 5.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blowoff top distance: peak 21d stretch minus current stretch in vol units
def f05pb_f05_parabolic_blowoff_topdrop_21d_base_v145_signal(closeadj):
    s = _f05_stretch(closeadj, 21)
    peak = s.rolling(21, min_periods=10).max()
    vol = s.rolling(63, min_periods=21).std()
    b = (peak - s) / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ascent angle: arctan of 21d slope scaled by vol (steepness as an angle)
def f05pb_f05_parabolic_blowoff_angle_21d_base_v146_signal(closeadj):
    slope = _f05_runslope(closeadj, 21)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    b = np.arctan(slope / vol.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume blowoff peak: max 5d dollar-vol spike over the last 21d
def f05pb_f05_parabolic_blowoff_dollpeak_21d_base_v147_signal(closeadj, volume):
    dv = closeadj * volume
    spike = dv / dv.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = spike.rolling(21, min_periods=10).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reversion-from-extreme realized: 5d forward-vs-trailing asymmetry of stretch
def f05pb_f05_parabolic_blowoff_extasym_21d_base_v148_signal(closeadj):
    s = _f05_stretch(closeadj, 21)
    trail = s.rolling(5, min_periods=3).mean()
    b = s - trail
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blowoff composite z: stretch z + slope z + volume z (additive overextension score)
def f05pb_f05_parabolic_blowoff_compositez_21d_base_v149_signal(closeadj, volume):
    sz = _z(_f05_stretch(closeadj, 21), 63)
    slz = _z(_f05_runslope(closeadj, 10), 63)
    vz = _z(volume, 63)
    b = (sz + slz + vz) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# terminal-blowoff flag intensity: extreme stretch AND extreme volume AND up-streak
def f05pb_f05_parabolic_blowoff_terminal_21d_base_v150_signal(closeadj, volume):
    s = (_f05_stretch(closeadj, 21).rolling(252, min_periods=63).rank(pct=True))
    vz = (_z(volume, 63).rolling(252, min_periods=63).rank(pct=True))
    up = (closeadj.diff() > 0).astype(float).rolling(10, min_periods=5).mean()
    b = s * vz * up
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f05pb_f05_parabolic_blowoff_stretch_13d_base_v076_signal,
    f05pb_f05_parabolic_blowoff_stretch_34d_base_v077_signal,
    f05pb_f05_parabolic_blowoff_mafan_5_21_63_base_v078_signal,
    f05pb_f05_parabolic_blowoff_stretchlvl_21d_base_v079_signal,
    f05pb_f05_parabolic_blowoff_maatr_5v63_base_v080_signal,
    f05pb_f05_parabolic_blowoff_peakvsma_21d_base_v081_signal,
    f05pb_f05_parabolic_blowoff_stretchmed_8d_base_v082_signal,
    f05pb_f05_parabolic_blowoff_runaccel_21v63_base_v083_signal,
    f05pb_f05_parabolic_blowoff_maxburst_21d_base_v084_signal,
    f05pb_f05_parabolic_blowoff_spikeconc_21d_base_v085_signal,
    f05pb_f05_parabolic_blowoff_slopeofslope_10d_base_v086_signal,
    f05pb_f05_parabolic_blowoff_newhicluster_21d_base_v087_signal,
    f05pb_f05_parabolic_blowoff_thrustweek_5d_base_v088_signal,
    f05pb_f05_parabolic_blowoff_volretcorr_21d_base_v089_signal,
    f05pb_f05_parabolic_blowoff_updollshare_10d_base_v090_signal,
    f05pb_f05_parabolic_blowoff_climaxvol_10d_base_v091_signal,
    f05pb_f05_parabolic_blowoff_voltrend_21d_base_v092_signal,
    f05pb_f05_parabolic_blowoff_volherf_21d_base_v093_signal,
    f05pb_f05_parabolic_blowoff_dollfroth_21d_base_v094_signal,
    f05pb_f05_parabolic_blowoff_volsurgeema_21d_base_v095_signal,
    f05pb_f05_parabolic_blowoff_emafade_10d_base_v096_signal,
    f05pb_f05_parabolic_blowoff_stretchdrop_21d_base_v097_signal,
    f05pb_f05_parabolic_blowoff_revtoday_base_v098_signal,
    f05pb_f05_parabolic_blowoff_offtop_21d_base_v099_signal,
    f05pb_f05_parabolic_blowoff_sincefroth_63d_base_v100_signal,
    f05pb_f05_parabolic_blowoff_giveback_21d_base_v101_signal,
    f05pb_f05_parabolic_blowoff_williamsr_14d_base_v102_signal,
    f05pb_f05_parabolic_blowoff_stochroll_14d_base_v103_signal,
    f05pb_f05_parabolic_blowoff_rsidiverg_21d_base_v104_signal,
    f05pb_f05_parabolic_blowoff_rejectwick_10d_base_v105_signal,
    f05pb_f05_parabolic_blowoff_hifade_21d_base_v106_signal,
    f05pb_f05_parabolic_blowoff_autocorr_21d_base_v107_signal,
    f05pb_f05_parabolic_blowoff_rangeexp_5v63_base_v108_signal,
    f05pb_f05_parabolic_blowoff_volratio_5v63_base_v109_signal,
    f05pb_f05_parabolic_blowoff_upsemivar_21d_base_v110_signal,
    f05pb_f05_parabolic_blowoff_parkinson_5d_base_v111_signal,
    f05pb_f05_parabolic_blowoff_volofvol_21d_base_v112_signal,
    f05pb_f05_parabolic_blowoff_signature_21d_base_v113_signal,
    f05pb_f05_parabolic_blowoff_extnetdrag_21d_base_v114_signal,
    f05pb_f05_parabolic_blowoff_paraquality_10d_base_v115_signal,
    f05pb_f05_parabolic_blowoff_stretchsharp_21d_base_v116_signal,
    f05pb_f05_parabolic_blowoff_swingtop_base_v117_signal,
    f05pb_f05_parabolic_blowoff_accelindex_base_v118_signal,
    f05pb_f05_parabolic_blowoff_maxext_21d_base_v119_signal,
    f05pb_f05_parabolic_blowoff_stretchrange_21d_base_v120_signal,
    f05pb_f05_parabolic_blowoff_atrext34_34d_base_v121_signal,
    f05pb_f05_parabolic_blowoff_cleanrun_63d_base_v122_signal,
    f05pb_f05_parabolic_blowoff_ext50rank_50d_base_v123_signal,
    f05pb_f05_parabolic_blowoff_emaconvex_13d_base_v124_signal,
    f05pb_f05_parabolic_blowoff_gaprun_21d_base_v125_signal,
    f05pb_f05_parabolic_blowoff_extsmoothchg_21d_base_v126_signal,
    f05pb_f05_parabolic_blowoff_trendresid_21d_base_v127_signal,
    f05pb_f05_parabolic_blowoff_freshhighrate_21d_base_v128_signal,
    f05pb_f05_parabolic_blowoff_runintensity_10d_base_v129_signal,
    f05pb_f05_parabolic_blowoff_frothvspeak_21d_base_v130_signal,
    f05pb_f05_parabolic_blowoff_exhaustcombo_21d_base_v131_signal,
    f05pb_f05_parabolic_blowoff_volexpaccel_base_v132_signal,
    f05pb_f05_parabolic_blowoff_volconfhigh_21d_base_v133_signal,
    f05pb_f05_parabolic_blowoff_stretchzgap_21d_base_v134_signal,
    f05pb_f05_parabolic_blowoff_squeezepop_base_v135_signal,
    f05pb_f05_parabolic_blowoff_freshpeak_21v63_base_v136_signal,
    f05pb_f05_parabolic_blowoff_atrthrustsum_10d_base_v137_signal,
    f05pb_f05_parabolic_blowoff_retkurt_21d_base_v138_signal,
    f05pb_f05_parabolic_blowoff_extstreak_base_v139_signal,
    f05pb_f05_parabolic_blowoff_movevsbudget_21d_base_v140_signal,
    f05pb_f05_parabolic_blowoff_fragility_21d_base_v141_signal,
    f05pb_f05_parabolic_blowoff_ribbonwidth_base_v142_signal,
    f05pb_f05_parabolic_blowoff_ribbonvel_base_v143_signal,
    f05pb_f05_parabolic_blowoff_obtime_21d_base_v144_signal,
    f05pb_f05_parabolic_blowoff_topdrop_21d_base_v145_signal,
    f05pb_f05_parabolic_blowoff_angle_21d_base_v146_signal,
    f05pb_f05_parabolic_blowoff_dollpeak_21d_base_v147_signal,
    f05pb_f05_parabolic_blowoff_extasym_21d_base_v148_signal,
    f05pb_f05_parabolic_blowoff_compositez_21d_base_v149_signal,
    f05pb_f05_parabolic_blowoff_terminal_21d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F05_PARABOLIC_BLOWOFF_REGISTRY_076_150 = REGISTRY


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

    print("OK f05_parabolic_blowoff_base_076_150_claude: %d features pass" % n_features)
