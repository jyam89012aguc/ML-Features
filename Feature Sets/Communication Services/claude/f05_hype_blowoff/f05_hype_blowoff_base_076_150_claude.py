import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).min()


def _ema(s, span):
    return s.ewm(span=span, min_periods=max(2, span // 2)).mean()


# ===== folder domain primitives (hype / blowoff / overextension) =====
def _f05hb_atr(high, low, closeadj, w):
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low),
                    (high - pc).abs(),
                    (low - pc).abs()], axis=1).max(axis=1)
    return tr.rolling(w, min_periods=max(2, w // 2)).mean()


def _f05hb_stretch_atr(high, low, closeadj, maw, atrw):
    ma = closeadj.rolling(maw, min_periods=max(2, maw // 2)).mean()
    atr = _f05hb_atr(high, low, closeadj, atrw)
    return (closeadj - ma) / atr.replace(0, np.nan)


def _f05hb_dist_ma(closeadj, maw):
    ma = closeadj.rolling(maw, min_periods=max(2, maw // 2)).mean()
    return closeadj / ma.replace(0, np.nan) - 1.0


def _f05hb_run_slope(closeadj, w):
    return np.log(closeadj.replace(0, np.nan) / closeadj.shift(w).replace(0, np.nan)) / float(w)


def _f05hb_volspike(volume, w):
    return volume / volume.rolling(w, min_periods=max(2, w // 2)).mean().replace(0, np.nan)


def _f05hb_rsi(closeadj, w):
    d = closeadj.diff()
    up = d.clip(lower=0.0)
    dn = (-d).clip(lower=0.0)
    au = up.rolling(w, min_periods=max(2, w // 2)).mean()
    ad = dn.rolling(w, min_periods=max(2, w // 2)).mean()
    rs = au / ad.replace(0, np.nan)
    return 100.0 - 100.0 / (1.0 + rs)


def _f05hb_parkinson(high, low, w):
    # Parkinson high-low range volatility
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan)) ** 2
    return np.sqrt(hl.rolling(w, min_periods=max(2, w // 2)).mean() / (4.0 * np.log(2.0)))


# ============================================================
# --- stretch facets (different MA / ATR window pairings) ---

# stretch above 5d MA in 5d ATR units (ultra-acute overextension)
def f05hb_f05_hype_blowoff_stretchatr_5x5_base_v076_signal(closeadj, high, low):
    b = _f05hb_stretch_atr(high, low, closeadj, 5, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stretch above 10d MA in 21d ATR units, smoothed (persistent extension)
def f05hb_f05_hype_blowoff_stretchatr_10x21_base_v077_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 10, 21)
    b = _ema(st, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stretch percentile vs own 252d history (rank of overextension)
def f05hb_f05_hype_blowoff_stretchrank_base_v078_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 10, 14)
    b = st.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stretch momentum: change in 5d-MA stretch over 10 days (extension building)
def f05hb_f05_hype_blowoff_stretchmom_base_v079_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 5, 14)
    b = st - st.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# integral of positive stretch over 10d (accumulated overextension exposure)
def f05hb_f05_hype_blowoff_stretchinteg_base_v080_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 5, 14)
    b = st.clip(lower=0).rolling(10, min_periods=5).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stretch vs its own 63d max (proximity to own blowoff ceiling)
def f05hb_f05_hype_blowoff_stretchceil_base_v081_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 10, 14)
    ceil = st.rolling(63, min_periods=21).max()
    b = st - ceil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- distance-above-MA facets ---

# distance above 10d MA in percent (fast overextension)
def f05hb_f05_hype_blowoff_distma_10d_base_v082_signal(closeadj):
    b = _f05hb_dist_ma(closeadj, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 126d MA (longer-horizon overextension)
def f05hb_f05_hype_blowoff_distma_126d_base_v083_signal(closeadj):
    b = _f05hb_dist_ma(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log distance above EMA-21 (smoother extension reference)
def f05hb_f05_hype_blowoff_distema_21d_base_v084_signal(closeadj):
    ema = _ema(closeadj, 21)
    b = np.log(closeadj.replace(0, np.nan) / ema.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 21d MA percentile-ranked vs 126d history
def f05hb_f05_hype_blowoff_distmarank_21d_base_v085_signal(closeadj):
    d = _f05hb_dist_ma(closeadj, 21)
    b = d.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread of fast vs slow extension: dist-above-10d minus dist-above-63d MA
def f05hb_f05_hype_blowoff_distspread_base_v086_signal(closeadj):
    d10 = _f05hb_dist_ma(closeadj, 10)
    d63 = _f05hb_dist_ma(closeadj, 63)
    b = d10 - d63
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# extension above the max of (21d MA, 63d MA) -- conservative overextension
def f05hb_f05_hype_blowoff_distmaxma_base_v087_signal(closeadj):
    ma21 = closeadj.rolling(21, min_periods=10).mean()
    ma63 = closeadj.rolling(63, min_periods=21).mean()
    ref = pd.concat([ma21, ma63], axis=1).max(axis=1)
    b = closeadj / ref.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- run-slope / parabolicity facets ---

# 3d ultra-short run slope (sharpest vertical reading)
def f05hb_f05_hype_blowoff_runslope_3d_base_v088_signal(closeadj):
    b = _f05hb_run_slope(closeadj, 3)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope steepening ratio: 5d slope over 21d slope (relative verticalization)
def f05hb_f05_hype_blowoff_sloperatio_base_v089_signal(closeadj):
    s5 = _f05hb_run_slope(closeadj, 5)
    s21 = _f05hb_run_slope(closeadj, 21)
    b = s5 / (s21.abs() + 0.002)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# parabolic curvature: change in 5d run-slope over 5 days (slope acceleration)
def f05hb_f05_hype_blowoff_slopeaccel_base_v090_signal(closeadj):
    s = _f05hb_run_slope(closeadj, 5)
    b = s - s.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share of the 21d move delivered in the most recent 5 days (front-loaded burst)
def f05hb_f05_hype_blowoff_moveshare_base_v091_signal(closeadj):
    g5 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(5).replace(0, np.nan))
    g21 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(21).replace(0, np.nan))
    b = g5 / (g21.abs() + 0.01)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how many of the last 10 days made fresh 10d closing highs (staircase parabola)
def f05hb_f05_hype_blowoff_staircase_base_v092_signal(closeadj):
    hi = closeadj.rolling(10, min_periods=5).max()
    fresh = (closeadj >= hi * 0.99999).astype(float)
    cnt = fresh.rolling(10, min_periods=5).sum()
    g = np.log(closeadj.replace(0, np.nan) / closeadj.shift(10).replace(0, np.nan))
    b = cnt * (1.0 + 5.0 * g.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume / dollar-volume facets ---

# log dollar-volume z-score vs 63d history (capital frenzy, standardized)
def f05hb_f05_hype_blowoff_dvolz_63d_base_v093_signal(closeadj, volume):
    dv = closeadj * volume
    b = _z(np.log(dv.replace(0, np.nan)), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume spike percentile rank vs 126d (rarity of today's participation)
def f05hb_f05_hype_blowoff_volrank_base_v094_signal(volume):
    vs = _f05hb_volspike(volume, 63)
    b = vs.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume acceleration: 5d volume avg change vs 5d ago (crowd building)
def f05hb_f05_hype_blowoff_volaccel_base_v095_signal(volume):
    av = volume.rolling(5, min_periods=3).mean()
    b = av / av.shift(5).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# climax-volume day: peak single-day log-volume z over the last 10 days
def f05hb_f05_hype_blowoff_volclimax_base_v096_signal(volume):
    lvz = _z(np.log(volume.replace(0, np.nan)), 63)
    b = lvz.rolling(10, min_periods=5).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume concentration: top-day volume share of trailing 21d total (single-day climax)
def f05hb_f05_hype_blowoff_volconc_base_v097_signal(volume):
    tot = volume.rolling(21, min_periods=10).sum()
    mx = volume.rolling(21, min_periods=10).max()
    b = mx / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume trend slope over 21d (rising capital interest)
def f05hb_f05_hype_blowoff_dvoltrend_base_v098_signal(closeadj, volume):
    dv = np.log((closeadj * volume).replace(0, np.nan))
    b = (dv - dv.shift(21)) / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- blowoff interaction facets ---

# price-up x volume-up co-spike: 5d-return rank times volume-spike rank
def f05hb_f05_hype_blowoff_cospike_base_v099_signal(closeadj, volume):
    r5 = closeadj.pct_change(5).rolling(126, min_periods=42).rank(pct=True)
    vs = _f05hb_volspike(volume, 63).rolling(126, min_periods=42).rank(pct=True)
    b = (r5 - 0.5) * (vs - 0.5) * 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blowoff thrust: distance-above-21d-MA times dollar-volume z (extended & funded)
def f05hb_f05_hype_blowoff_fundext_base_v100_signal(closeadj, volume):
    d = _f05hb_dist_ma(closeadj, 21)
    dvz = _z(np.log((closeadj * volume).replace(0, np.nan)), 63)
    b = d * dvz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# climactic candle interaction: intraday range z times volume spike (single-bar climax)
def f05hb_f05_hype_blowoff_barclimax_base_v101_signal(closeadj, high, low, volume):
    rng = (high - low) / closeadj.replace(0, np.nan)
    rngz = _z(rng, 63)
    vs = _f05hb_volspike(volume, 21)
    b = rngz * vs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# run-and-volume divergence: price slope up but volume fading (weakening blowoff)
def f05hb_f05_hype_blowoff_pvdiverge_base_v102_signal(closeadj, volume):
    s = _f05hb_run_slope(closeadj, 10)
    vtrend = volume.rolling(5, min_periods=3).mean() / volume.rolling(21, min_periods=10).mean().replace(0, np.nan) - 1.0
    b = s.clip(lower=0) * (-vtrend)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- mean-reversion-from-spike facets ---

# 3d snapback: negative 3d return after extension above 10d MA
def f05hb_f05_hype_blowoff_snapback3_base_v103_signal(closeadj):
    d = _f05hb_dist_ma(closeadj, 10)
    r3 = closeadj.pct_change(3)
    b = d.shift(3).clip(lower=0) * (-r3)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retrace depth from 10d high relative to the prior 10d run (give-back ratio)
def f05hb_f05_hype_blowoff_giveback_base_v104_signal(closeadj):
    hi = closeadj.rolling(10, min_periods=5).max()
    retr = (hi - closeadj) / hi.replace(0, np.nan)
    run = np.log(hi.replace(0, np.nan) / closeadj.shift(10).replace(0, np.nan)).clip(lower=0)
    b = retr / (run + 0.02)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fade velocity: how fast price is dropping from a 21d high (post-blowoff decay)
def f05hb_f05_hype_blowoff_fadevel_base_v105_signal(closeadj):
    hi = closeadj.rolling(21, min_periods=10).max()
    dd = closeadj / hi.replace(0, np.nan) - 1.0
    b = dd - dd.shift(3)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reversal confirmation: prior overextension times subsequent RSI roll-down
def f05hb_f05_hype_blowoff_revconf_base_v106_signal(closeadj):
    d = _f05hb_dist_ma(closeadj, 21).shift(5).clip(lower=0)
    rsi = _f05hb_rsi(closeadj, 14)
    roll = (rsi.shift(5) - rsi).clip(lower=0)
    b = d * roll
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mean-reversion pressure: stretch-ATR times negative recent return (snap risk)
def f05hb_f05_hype_blowoff_revpressure_base_v107_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 5, 14)
    r2 = closeadj.pct_change(2)
    b = st.clip(lower=0) * (-r2)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight-style gap reversal proxy: distance from low after touching 5d high
def f05hb_f05_hype_blowoff_intrabarrev_base_v108_signal(closeadj, high, low):
    hh = high.rolling(5, min_periods=3).max()
    near_hi = (high >= hh * 0.999).astype(float)
    rev = (high - closeadj) / (high - low).replace(0, np.nan)
    b = (rev * near_hi).rolling(5, min_periods=3).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- exhaustion / overbought facets ---

# 21d RSI centered (slower overbought)
def f05hb_f05_hype_blowoff_rsi_21d_base_v109_signal(closeadj):
    b = _f05hb_rsi(closeadj, 21) - 50.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# RSI divergence: price 10d high but RSI lower than 10d ago (bearish exhaustion)
def f05hb_f05_hype_blowoff_rsidiverge_base_v110_signal(closeadj):
    rsi = _f05hb_rsi(closeadj, 14)
    px_hi = (closeadj >= closeadj.rolling(10, min_periods=5).max() * 0.999).astype(float)
    rsi_drop = (rsi.shift(10) - rsi).clip(lower=0)
    b = px_hi * rsi_drop
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stochastic %K minus %D (fast/slow oscillator gap, overbought turn)
def f05hb_f05_hype_blowoff_stochcross_base_v111_signal(closeadj, high, low):
    hh = high.rolling(14, min_periods=7).max()
    ll = low.rolling(14, min_periods=7).min()
    k = (closeadj - ll) / (hh - ll).replace(0, np.nan)
    d = k.rolling(3, min_periods=2).mean()
    b = k - d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Commodity Channel Index style overbought (price vs typical, mean-dev scaled)
def f05hb_f05_hype_blowoff_cci_base_v112_signal(closeadj, high, low):
    tp = (high + low + closeadj) / 3.0
    ma = tp.rolling(21, min_periods=10).mean()
    md = (tp - ma).abs().rolling(21, min_periods=10).mean()
    b = (tp - ma) / (0.015 * md).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive-up-day energy: sum of up-returns in the current green streak (21d)
def f05hb_f05_hype_blowoff_streakenergy_base_v113_signal(closeadj):
    r = closeadj.pct_change()

    def _eng(a):
        s = 0.0
        for x in a[::-1]:
            if x > 0:
                s += x
            else:
                break
        return float(s)

    b = r.rolling(21, min_periods=10).apply(_eng, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of 10d in upper Bollinger zone weighted by breach magnitude
def f05hb_f05_hype_blowoff_bandheat_base_v114_signal(closeadj):
    ma = closeadj.rolling(21, min_periods=10).mean()
    sd = closeadj.rolling(21, min_periods=10).std()
    pctb = (closeadj - ma) / (2.0 * sd).replace(0, np.nan)
    b = pctb.clip(lower=0).rolling(10, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volatility-of-blowoff facets ---

# Parkinson high-low vol surge: 5d vs 63d (range explosion)
def f05hb_f05_hype_blowoff_parksurge_base_v115_signal(high, low):
    p5 = _f05hb_parkinson(high, low, 5)
    p63 = _f05hb_parkinson(high, low, 63)
    b = p5 / p63.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday range expansion z: today's high-low range vs 63d typical
def f05hb_f05_hype_blowoff_rangez_base_v116_signal(closeadj, high, low):
    rng = (high - low) / closeadj.replace(0, np.nan)
    b = _z(rng, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-wick dominance: avg upper-wick share over 5d (rejection at highs, exhaustion)
def f05hb_f05_hype_blowoff_upperwick_base_v117_signal(closeadj, high, low):
    upper_wick = (high - closeadj).clip(lower=0)
    rng = (high - low).replace(0, np.nan)
    b = (upper_wick / rng).rolling(5, min_periods=3).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fading-close strength: 5d avg close-in-range minus its 21d avg (waning daily strength)
def f05hb_f05_hype_blowoff_clrange_base_v118_signal(closeadj, high, low):
    clr = (closeadj - low) / (high - low).replace(0, np.nan)
    b = clr.rolling(5, min_periods=3).mean() - clr.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol spike: 5d return std vs 126d return std (turbulent blowoff)
def f05hb_f05_hype_blowoff_rvspike_base_v119_signal(closeadj):
    r = closeadj.pct_change()
    v5 = r.rolling(5, min_periods=3).std()
    v126 = r.rolling(126, min_periods=42).std()
    b = v5 / v126.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite / regime facets ---

# composite blowoff score: z(stretch) + z(volspike) + z(rsi) averaged
def f05hb_f05_hype_blowoff_compscore_base_v120_signal(closeadj, high, low, volume):
    st = _z(_f05hb_stretch_atr(high, low, closeadj, 10, 14), 63)
    vz = _z(np.log(volume.replace(0, np.nan)), 63)
    rz = (_f05hb_rsi(closeadj, 14) - 50.0) / 20.0
    b = (st + vz + rz) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# froth regime persistence: mean composite-positive flag-magnitude over 21d
def f05hb_f05_hype_blowoff_frothregime_base_v121_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 5, 14)
    rsi = (_f05hb_rsi(closeadj, 14) - 60.0) / 40.0
    score = (st.clip(lower=0) * rsi.clip(lower=0))
    b = score.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overextension entropy: dispersion of dist-above-MA across 10/21/63 horizons
def f05hb_f05_hype_blowoff_extdisp_base_v122_signal(closeadj):
    d10 = _f05hb_dist_ma(closeadj, 10)
    d21 = _f05hb_dist_ma(closeadj, 21)
    d63 = _f05hb_dist_ma(closeadj, 63)
    b = pd.concat([d10, d21, d63], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blowoff vs base: 10d gain divided by 126d gain (move concentration, long base)
def f05hb_f05_hype_blowoff_concbase_base_v123_signal(closeadj):
    g10 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(10).replace(0, np.nan))
    g126 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(126).replace(0, np.nan))
    b = g10 / (g126.abs() + 0.05)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 21d MA in ATR units, change over a month (extension momentum)
def f05hb_f05_hype_blowoff_extmom_base_v124_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 21, 21)
    b = st - st.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign-magnitude of stretch: signed sqrt of 5d-MA stretch (tame extremes, keep sign)
def f05hb_f05_hype_blowoff_signmagstretch_base_v125_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 5, 14)
    b = np.sign(st) * np.sqrt(st.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how stretched the 21d high is above the 21d MA (anchor extension of the run)
def f05hb_f05_hype_blowoff_hiextend_base_v126_signal(closeadj):
    hi = closeadj.rolling(21, min_periods=10).max()
    ma = closeadj.rolling(21, min_periods=10).mean()
    b = (hi - ma) / ma.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap between price and 21d MA divided by 21d high-low amplitude (range-relative ext)
def f05hb_f05_hype_blowoff_rangerelext_base_v127_signal(closeadj):
    ma = closeadj.rolling(21, min_periods=10).mean()
    hi = closeadj.rolling(21, min_periods=10).max()
    lo = closeadj.rolling(21, min_periods=10).min()
    b = (closeadj - ma) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of price vs 63d MA gap (medium overextension building)
def f05hb_f05_hype_blowoff_extaccel63_base_v128_signal(closeadj):
    d = _f05hb_dist_ma(closeadj, 63)
    b = d - 2.0 * d.shift(10) + d.shift(20)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-day fraction: fraction of last 10d that closed in top 20% of their range
def f05hb_f05_hype_blowoff_trendday_base_v129_signal(closeadj, high, low):
    clr = (closeadj - low) / (high - low).replace(0, np.nan)
    strong = (clr - 0.8).clip(lower=0)
    b = strong.rolling(10, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rate of new 21d highs over a month, weighted by stretch (repeated breakouts)
def f05hb_f05_hype_blowoff_newhirate_base_v130_signal(closeadj):
    hi = closeadj.rolling(21, min_periods=10).max()
    fresh = (closeadj >= hi * 0.99999).astype(float)
    rate = fresh.rolling(21, min_periods=10).mean()
    d = _f05hb_dist_ma(closeadj, 21).clip(lower=0)
    b = rate * (1.0 + 3.0 * d)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bubble score: cumulative log-return over 63d times current overbought (RSI/100)
def f05hb_f05_hype_blowoff_bubble_base_v131_signal(closeadj):
    g = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    ob = (_f05hb_rsi(closeadj, 14) / 100.0)
    b = g.clip(lower=0) * ob
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration ratio: 5d return vs 63d average abs daily return (impulse magnitude)
def f05hb_f05_hype_blowoff_impulseratio_base_v132_signal(closeadj):
    r5 = closeadj.pct_change(5)
    typ = closeadj.pct_change().abs().rolling(63, min_periods=21).mean()
    b = r5 / (5.0 * typ.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overextension drawdown: stretch peak (21d) minus current stretch, signed (rollover)
def f05hb_f05_hype_blowoff_stretchdd_base_v133_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 5, 14)
    peak = st.rolling(21, min_periods=10).max()
    b = st - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# velocity of dollar-volume relative to price velocity (capital vs price thrust)
def f05hb_f05_hype_blowoff_capvspx_base_v134_signal(closeadj, volume):
    dvslope = np.log((closeadj * volume).rolling(5, min_periods=3).mean().replace(0, np.nan))
    dvslope = dvslope - dvslope.shift(10)
    pxslope = np.log(closeadj.replace(0, np.nan) / closeadj.shift(10).replace(0, np.nan))
    b = dvslope - 3.0 * pxslope
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overbought streak energy: sum of (RSI-50)+ over the last 10 days
def f05hb_f05_hype_blowoff_obenergy_base_v135_signal(closeadj):
    rsi = _f05hb_rsi(closeadj, 14)
    b = (rsi - 50.0).clip(lower=0).rolling(10, min_periods=5).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of stretch in vol-adjusted terms: tanh of 10d change in stretch-z
def f05hb_f05_hype_blowoff_stretchzaccel_base_v136_signal(closeadj, high, low):
    stz = _z(_f05hb_stretch_atr(high, low, closeadj, 10, 14), 63)
    b = np.tanh(0.7 * (stz - stz.shift(10)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blowoff exhaustion: high stretch but decelerating slope (topping signature)
def f05hb_f05_hype_blowoff_topping_base_v137_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 5, 14).clip(lower=0)
    slope = _f05hb_run_slope(closeadj, 5)
    decel = (slope.shift(5) - slope).clip(lower=0)
    b = st * decel
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-weighted overextension: dist-above-21d MA weighted by share of dollar-volume
def f05hb_f05_hype_blowoff_vwext_base_v138_signal(closeadj, volume):
    d = _f05hb_dist_ma(closeadj, 21)
    dv = closeadj * volume
    vw = dv / dv.rolling(21, min_periods=10).sum().replace(0, np.nan) * 21.0
    b = d * vw
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-position of close in the 63d window with overbought tilt (high & frothy)
def f05hb_f05_hype_blowoff_rngpos63_base_v139_signal(closeadj, high, low):
    hh = high.rolling(63, min_periods=21).max()
    ll = low.rolling(63, min_periods=21).min()
    pos = (closeadj - ll) / (hh - ll).replace(0, np.nan)
    b = (pos - 0.5) ** 3 * 8.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of overbought oscillator: 10d change in (RSI-50) (momentum of froth)
def f05hb_f05_hype_blowoff_obslope_base_v140_signal(closeadj):
    osc = _f05hb_rsi(closeadj, 14) - 50.0
    b = osc - osc.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capitulation-after-blowoff: depth of 5d drop following a 21d-high touch, vol-weighted
def f05hb_f05_hype_blowoff_postpeakdrop_base_v141_signal(closeadj, volume):
    hi = closeadj.rolling(21, min_periods=10).max()
    touched = (closeadj.shift(5) >= hi.shift(5) * 0.999).astype(float)
    drop = (closeadj.shift(5) / closeadj - 1.0).clip(lower=0)
    vs = _f05hb_volspike(volume, 21)
    b = touched * drop * vs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# extension percentile blended across vol/price (composite rank of frothiness)
def f05hb_f05_hype_blowoff_blendrank_base_v142_signal(closeadj, high, low, volume):
    st = _f05hb_stretch_atr(high, low, closeadj, 10, 14).rolling(126, min_periods=42).rank(pct=True)
    vr = _f05hb_volspike(volume, 63).rolling(126, min_periods=42).rank(pct=True)
    b = (st + vr) / 2.0 - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spring-out-of-base: 21d return scaled by prior 63d range compression (quiet->blowoff)
def f05hb_f05_hype_blowoff_quietbase_base_v143_signal(closeadj, high, low):
    g = np.log(closeadj.replace(0, np.nan) / closeadj.shift(21).replace(0, np.nan))
    compress = _f05hb_parkinson(high, low, 63).shift(21)
    b = g.clip(lower=0) / (compress.replace(0, np.nan) + 0.01)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log-price third-window convexity (parabola curvature over 21d via 7d steps)
def f05hb_f05_hype_blowoff_curve21_base_v144_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    b = lp - 2.0 * lp.shift(7) + lp.shift(14)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stretch-ATR EMA cross: fast EMA minus slow EMA of 5d-MA stretch (froth turn)
def f05hb_f05_hype_blowoff_stretchemacross_base_v145_signal(closeadj, high, low):
    st = _f05hb_stretch_atr(high, low, closeadj, 5, 14)
    b = _ema(st, 5) - _ema(st, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smooth-run quality: 21d gain divided by deepest intra-window dip (clean parabola)
def f05hb_f05_hype_blowoff_riskadjrun_base_v146_signal(closeadj):
    g = (closeadj / closeadj.shift(21).replace(0, np.nan) - 1.0)
    roll_peak = closeadj.rolling(21, min_periods=10).max()
    maxdd = (closeadj / roll_peak.replace(0, np.nan) - 1.0).rolling(21, min_periods=10).min().abs()
    b = g.clip(lower=0) / (maxdd + 0.02)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above upper Donchian-mid in ATR units (overextension vs channel center)
def f05hb_f05_hype_blowoff_donchext_base_v147_signal(closeadj, high, low):
    hh = high.rolling(21, min_periods=10).max()
    ll = low.rolling(21, min_periods=10).min()
    mid = (hh + ll) / 2.0
    atr = _f05hb_atr(high, low, closeadj, 21)
    b = (closeadj - mid) / atr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# crowd-exhaustion: high volume spike with weak close-in-range (buying into rejection)
def f05hb_f05_hype_blowoff_crowdexhaust_base_v148_signal(closeadj, high, low, volume):
    vs = _f05hb_volspike(volume, 21)
    clr = (closeadj - low) / (high - low).replace(0, np.nan)
    weak = (0.5 - clr).clip(lower=0)
    b = (vs * weak).rolling(5, min_periods=3).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# parabolic over-acceleration: positive second derivative of log price (10d steps)
def f05hb_f05_hype_blowoff_overaccel_base_v149_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    accel = lp - 2.0 * lp.shift(10) + lp.shift(20)
    rising = (lp - lp.shift(10)) > 0
    b = accel * rising.astype(float)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# full blowoff signature: stretch x volume-z x positive-slope (the complete pattern)
def f05hb_f05_hype_blowoff_fullsig_base_v150_signal(closeadj, high, low, volume):
    st = _f05hb_stretch_atr(high, low, closeadj, 5, 14).clip(lower=0)
    vz = _z(np.log(volume.replace(0, np.nan)), 63)
    slope = _f05hb_run_slope(closeadj, 5).clip(lower=0)
    b = st * vz * (1.0 + 50.0 * slope)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f05hb_f05_hype_blowoff_stretchatr_5x5_base_v076_signal,
    f05hb_f05_hype_blowoff_stretchatr_10x21_base_v077_signal,
    f05hb_f05_hype_blowoff_stretchrank_base_v078_signal,
    f05hb_f05_hype_blowoff_stretchmom_base_v079_signal,
    f05hb_f05_hype_blowoff_stretchinteg_base_v080_signal,
    f05hb_f05_hype_blowoff_stretchceil_base_v081_signal,
    f05hb_f05_hype_blowoff_distma_10d_base_v082_signal,
    f05hb_f05_hype_blowoff_distma_126d_base_v083_signal,
    f05hb_f05_hype_blowoff_distema_21d_base_v084_signal,
    f05hb_f05_hype_blowoff_distmarank_21d_base_v085_signal,
    f05hb_f05_hype_blowoff_distspread_base_v086_signal,
    f05hb_f05_hype_blowoff_distmaxma_base_v087_signal,
    f05hb_f05_hype_blowoff_runslope_3d_base_v088_signal,
    f05hb_f05_hype_blowoff_sloperatio_base_v089_signal,
    f05hb_f05_hype_blowoff_slopeaccel_base_v090_signal,
    f05hb_f05_hype_blowoff_moveshare_base_v091_signal,
    f05hb_f05_hype_blowoff_staircase_base_v092_signal,
    f05hb_f05_hype_blowoff_dvolz_63d_base_v093_signal,
    f05hb_f05_hype_blowoff_volrank_base_v094_signal,
    f05hb_f05_hype_blowoff_volaccel_base_v095_signal,
    f05hb_f05_hype_blowoff_volclimax_base_v096_signal,
    f05hb_f05_hype_blowoff_volconc_base_v097_signal,
    f05hb_f05_hype_blowoff_dvoltrend_base_v098_signal,
    f05hb_f05_hype_blowoff_cospike_base_v099_signal,
    f05hb_f05_hype_blowoff_fundext_base_v100_signal,
    f05hb_f05_hype_blowoff_barclimax_base_v101_signal,
    f05hb_f05_hype_blowoff_pvdiverge_base_v102_signal,
    f05hb_f05_hype_blowoff_snapback3_base_v103_signal,
    f05hb_f05_hype_blowoff_giveback_base_v104_signal,
    f05hb_f05_hype_blowoff_fadevel_base_v105_signal,
    f05hb_f05_hype_blowoff_revconf_base_v106_signal,
    f05hb_f05_hype_blowoff_revpressure_base_v107_signal,
    f05hb_f05_hype_blowoff_intrabarrev_base_v108_signal,
    f05hb_f05_hype_blowoff_rsi_21d_base_v109_signal,
    f05hb_f05_hype_blowoff_rsidiverge_base_v110_signal,
    f05hb_f05_hype_blowoff_stochcross_base_v111_signal,
    f05hb_f05_hype_blowoff_cci_base_v112_signal,
    f05hb_f05_hype_blowoff_streakenergy_base_v113_signal,
    f05hb_f05_hype_blowoff_bandheat_base_v114_signal,
    f05hb_f05_hype_blowoff_parksurge_base_v115_signal,
    f05hb_f05_hype_blowoff_rangez_base_v116_signal,
    f05hb_f05_hype_blowoff_upperwick_base_v117_signal,
    f05hb_f05_hype_blowoff_clrange_base_v118_signal,
    f05hb_f05_hype_blowoff_rvspike_base_v119_signal,
    f05hb_f05_hype_blowoff_compscore_base_v120_signal,
    f05hb_f05_hype_blowoff_frothregime_base_v121_signal,
    f05hb_f05_hype_blowoff_extdisp_base_v122_signal,
    f05hb_f05_hype_blowoff_concbase_base_v123_signal,
    f05hb_f05_hype_blowoff_extmom_base_v124_signal,
    f05hb_f05_hype_blowoff_signmagstretch_base_v125_signal,
    f05hb_f05_hype_blowoff_hiextend_base_v126_signal,
    f05hb_f05_hype_blowoff_rangerelext_base_v127_signal,
    f05hb_f05_hype_blowoff_extaccel63_base_v128_signal,
    f05hb_f05_hype_blowoff_trendday_base_v129_signal,
    f05hb_f05_hype_blowoff_newhirate_base_v130_signal,
    f05hb_f05_hype_blowoff_bubble_base_v131_signal,
    f05hb_f05_hype_blowoff_impulseratio_base_v132_signal,
    f05hb_f05_hype_blowoff_stretchdd_base_v133_signal,
    f05hb_f05_hype_blowoff_capvspx_base_v134_signal,
    f05hb_f05_hype_blowoff_obenergy_base_v135_signal,
    f05hb_f05_hype_blowoff_stretchzaccel_base_v136_signal,
    f05hb_f05_hype_blowoff_topping_base_v137_signal,
    f05hb_f05_hype_blowoff_vwext_base_v138_signal,
    f05hb_f05_hype_blowoff_rngpos63_base_v139_signal,
    f05hb_f05_hype_blowoff_obslope_base_v140_signal,
    f05hb_f05_hype_blowoff_postpeakdrop_base_v141_signal,
    f05hb_f05_hype_blowoff_blendrank_base_v142_signal,
    f05hb_f05_hype_blowoff_quietbase_base_v143_signal,
    f05hb_f05_hype_blowoff_curve21_base_v144_signal,
    f05hb_f05_hype_blowoff_stretchemacross_base_v145_signal,
    f05hb_f05_hype_blowoff_riskadjrun_base_v146_signal,
    f05hb_f05_hype_blowoff_donchext_base_v147_signal,
    f05hb_f05_hype_blowoff_crowdexhaust_base_v148_signal,
    f05hb_f05_hype_blowoff_overaccel_base_v149_signal,
    f05hb_f05_hype_blowoff_fullsig_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F05_HYPE_BLOWOFF_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.012, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1.2e6, 7e5, n)) + 5e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    ALLOW = {"open", "high", "low", "close", "closeadj", "volume"}

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

    print("OK f05_hype_blowoff_base_076_150_claude: %d features pass" % n_features)
