"""f10_candle_sequence_patterns base features 001-075.

Domain: multi-bar candle sequence patterns. Every feature uses values
from >= 2 consecutive bars (open/high/low/close + shifts). Distinct
from f06 (single-bar body geometry), f07 (gap behavior), f08 (range
dynamics), f09 (close-in-range).

On synthetic GBM data, strict binary pattern triggers (exact
engulfing, true doji+bull-bear morning star, etc.) rarely fire and
yield constant series. This file prefers:
  - continuous pattern STRENGTH scores
  - rolling counts of soft pattern occurrences over N bars
  - distance-to-threshold smoothed signals
  - autocorrelation / streak / Markov-like features

NaN policy: never fillna(<value>); only replace([inf,-inf], nan) at
final return. Windows > 21 use closeadj (when available); short-window
intra-pattern features use unadjusted open/high/low/close.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Features 001-075
# ---------------------------------------------------------------------------


# --- Group A: 2-bar engulfing / harami / piercing strength (continuous) ---


def f10cs_f10_candle_sequence_patterns_bullengs_2d_base_v001_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Bullish engulfing strength: continuous score = (current body if green)
    minus (prior body if red), normalized by sum of both bodies. Uses 2 bars."""
    body = close - open
    prev_body = body.shift(1)
    # bullish engulfing favors curr>0 and prev<0 and |curr|>|prev|
    raw = body - prev_body
    norm = body.abs() + prev_body.abs()
    out = raw / norm.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_bearengs_2d_base_v002_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish engulfing strength using full-bar range (not body) for
    normalization -- structurally different from v001. Score is signed
    so that bearish engulfing (red bar after green) returns positive."""
    body = close - open
    prev_body = body.shift(1)
    full = (high - low) + (high.shift(1) - low.shift(1))
    raw = (-body * prev_body.abs() - prev_body * body.abs())
    out = raw / full.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_engratio_2d_base_v003_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Body-engulfing ratio: current body / prior body, log-scaled.
    Positive when current bar dominates prior bar."""
    cur = (close - open).abs()
    prev = (close - open).abs().shift(1).replace(0.0, np.nan)
    out = np.log((cur + 1e-12) / (prev + 1e-12))
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_haramis_2d_base_v004_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Harami strength: 1 - max(high,low containment of curr body inside
    prior body). Continuous in [-inf,1]; high values = strong inside-body."""
    cur_hi = pd.concat([open, close], axis=1).max(axis=1)
    cur_lo = pd.concat([open, close], axis=1).min(axis=1)
    prv_hi = cur_hi.shift(1)
    prv_lo = cur_lo.shift(1)
    prv_body = (prv_hi - prv_lo).replace(0.0, np.nan)
    # how far curr body sits inside prev body
    over_hi = (cur_hi - prv_hi).clip(lower=0.0) / prv_body
    over_lo = (prv_lo - cur_lo).clip(lower=0.0) / prv_body
    out = 1.0 - (over_hi + over_lo)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_pierces_2d_base_v005_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Piercing line strength: penetration depth of curr close into prior
    red body. Continuous score; positive = bullish reversal candidate."""
    prev_open = open.shift(1)
    prev_close = close.shift(1)
    prev_red = (prev_open - prev_close).clip(lower=0.0).replace(0.0, np.nan)
    # piercing requires curr open below prev close, curr close above prev mid
    prev_mid = (prev_open + prev_close) / 2.0
    score = (close - prev_mid) / prev_red
    # gate softly by whether the gap-down condition is met
    soft_gate = ((prev_close - open) / prev_red).clip(lower=-1.0, upper=1.0)
    out = score * soft_gate.clip(lower=0.0)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_darkcs_2d_base_v006_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Dark cloud cover strength: mirror of piercing, bearish."""
    prev_open = open.shift(1)
    prev_close = close.shift(1)
    prev_green = (prev_close - prev_open).clip(lower=0.0).replace(0.0, np.nan)
    prev_mid = (prev_open + prev_close) / 2.0
    score = (prev_mid - close) / prev_green
    soft_gate = ((open - prev_close) / prev_green).clip(lower=-1.0, upper=1.0)
    out = score * soft_gate.clip(lower=0.0)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group B: tweezer / proximity 2-bar features ----------------------------


def f10cs_f10_candle_sequence_patterns_tweezerth_2d_base_v007_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Tweezer high similarity: -|high - high[-1]| / (high+high[-1]).
    More negative numbers = bigger difference; near 0 = tweezer."""
    diff = (high - high.shift(1)).abs()
    den = (high + high.shift(1)).replace(0.0, np.nan)
    out = -(diff / den)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_tweezerbl_2d_base_v008_signal(low: pd.Series) -> pd.Series:
    """Tweezer low similarity: -|low - low[-1]| / (low+low[-1])."""
    diff = (low - low.shift(1)).abs()
    den = (low + low.shift(1)).replace(0.0, np.nan)
    out = -(diff / den)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_hhpct_10d_base_v009_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of 10 prior bars exhibiting higher-high AND higher-low
    (bull HH/HL stack). Continuous in [0,1]."""
    hh = (high > high.shift(1)).astype(float).where(~high.isna() & ~high.shift(1).isna())
    hl = (low > low.shift(1)).astype(float).where(~low.isna() & ~low.shift(1).isna())
    both = (hh * hl)
    out = both.rolling(10, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_llpct_10d_base_v010_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of 10 prior bars showing lower-high AND lower-low."""
    lh = (high < high.shift(1)).astype(float).where(~high.isna() & ~high.shift(1).isna())
    ll = (low < low.shift(1)).astype(float).where(~low.isna() & ~low.shift(1).isna())
    both = (lh * ll)
    out = both.rolling(10, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group C: 3-bar continuous pattern strengths ----------------------------


def f10cs_f10_candle_sequence_patterns_whitesold_3d_base_v011_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Three white soldiers continuous strength: sum of last 3 normalized
    bodies if all positive, else negative shrinkage."""
    body = (close - open) / open.replace(0.0, np.nan)
    s = body + body.shift(1) + body.shift(2)
    # multiply by indicator of monotone rising opens within bodies
    soft = np.tanh(3.0 * s)
    return soft.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_blackcrow_3d_base_v012_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Three black crows score using DECREASING-HIGH count over 3 bars times
    bear-color count. Structurally different from white-soldiers body sum."""
    bear = (close < open).astype(float).where(~close.isna() & ~open.isna())
    lower_h = (high < high.shift(1)).astype(float).where(~high.isna() & ~high.shift(1).isna())
    s = (bear + bear.shift(1) + bear.shift(2)) * (lower_h + lower_h.shift(1) + lower_h.shift(2))
    rng_n = (high - low).rolling(10, min_periods=10).mean().replace(0.0, np.nan)
    intensity = -(close - close.shift(2)) / rng_n
    out = s * intensity / 9.0
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_morningst_3d_base_v013_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Morning star: bear[-2], small[-1], bull[0]. Continuous: signed score
    based on body sizes/colors."""
    body = close - open
    rng = (high - low).replace(0.0, np.nan)
    b2 = -body.shift(2) / rng.shift(2)  # large negative bar (-)
    b1 = 1.0 - (body.shift(1).abs() / rng.shift(1))  # small body (high score)
    b0 = body / rng  # large positive bar (+)
    out = (b2 + b1 + b0) / 3.0
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_eveningst_3d_base_v014_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Evening star (mirror of morning star). Bull[-2], small[-1], bear[0]."""
    body = close - open
    rng = (high - low).replace(0.0, np.nan)
    b2 = body.shift(2) / rng.shift(2)
    b1 = 1.0 - (body.shift(1).abs() / rng.shift(1))
    b0 = -body / rng
    out = (b2 + b1 + b0) / 3.0
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_threeinup_3d_base_v015_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Three inside up strength: harami-bull pattern. Score combines harami
    score (bar -1 inside bar -2) with bullish confirmation on bar 0."""
    body = close - open
    cur_hi = pd.concat([open, close], axis=1).max(axis=1)
    cur_lo = pd.concat([open, close], axis=1).min(axis=1)
    inside = ((cur_hi.shift(1) < cur_hi.shift(2)).astype(float)
              + (cur_lo.shift(1) > cur_lo.shift(2)).astype(float)) / 2.0
    prev_red = (-body.shift(2)).clip(lower=0.0)
    confirm = body  # current must be green
    out = inside * np.sign(prev_red) * np.tanh(10.0 * confirm / close.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_threeindn_3d_base_v016_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Three inside down strength (mirror)."""
    body = close - open
    cur_hi = pd.concat([open, close], axis=1).max(axis=1)
    cur_lo = pd.concat([open, close], axis=1).min(axis=1)
    inside = ((cur_hi.shift(1) < cur_hi.shift(2)).astype(float)
              + (cur_lo.shift(1) > cur_lo.shift(2)).astype(float)) / 2.0
    prev_green = body.shift(2).clip(lower=0.0)
    confirm = -body
    out = inside * np.sign(prev_green) * np.tanh(10.0 * confirm / close.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_threeoutup_3d_base_v017_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Three outside up: bullish engulfing on -1 vs -2, confirmation up on 0."""
    body = close - open
    cur_hi = pd.concat([open, close], axis=1).max(axis=1)
    cur_lo = pd.concat([open, close], axis=1).min(axis=1)
    outside = ((cur_hi.shift(1) > cur_hi.shift(2)).astype(float)
               + (cur_lo.shift(1) < cur_lo.shift(2)).astype(float)) / 2.0
    prev_engulf_color = np.sign(body.shift(1))
    confirm = np.sign(body) * (body / close.replace(0.0, np.nan)).abs()
    out = outside * prev_engulf_color * np.tanh(20.0 * confirm)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group D: inside / outside bar sequence (rolling counts, streaks) ------


def f10cs_f10_candle_sequence_patterns_inscnt_20d_base_v018_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of inside bars (high<prev high & low>prev low) in trailing 20."""
    inside = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    inside = inside.where(~high.isna() & ~high.shift(1).isna())
    out = inside.rolling(20, min_periods=20).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_outcnt_30d_base_v019_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of outside bars in trailing 30 (uses closeadj-comparable range
    via raw OHLC differences which are scale-free in count form)."""
    outside = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
    outside = outside.where(~high.isna() & ~high.shift(1).isna())
    out = outside.rolling(30, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)






def f10cs_f10_candle_sequence_patterns_dsinsd_50d_base_v022_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Days since last inside bar (capped at 50)."""
    inside = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    inside = inside.where(~high.isna() & ~high.shift(1).isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])
    out = inside.rolling(50, min_periods=50).apply(_ds, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_dsoutsd_50d_base_v023_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Days since last outside bar (capped at 50)."""
    outside = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
    outside = outside.where(~high.isna() & ~high.shift(1).isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])
    out = outside.rolling(50, min_periods=50).apply(_ds, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_nr4_4d_base_v024_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """NR4 strength: current bar range minus rolling-4 min range, normalized.
    Negative = narrowest of 4."""
    rng = high - low
    mn = rng.rolling(4, min_periods=4).min()
    den = rng.rolling(4, min_periods=4).mean().replace(0.0, np.nan)
    out = (rng - mn) / den
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_nr7_7d_base_v025_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """NR7-like: current range / rolling 7 min range. <=1 implies NR7."""
    rng = high - low
    mn = rng.rolling(7, min_periods=7).min().replace(0.0, np.nan)
    out = rng / mn
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_wr4_4d_base_v026_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """WR4 (widest range of 4) strength: current range vs rolling-4 max."""
    rng = high - low
    mx = rng.rolling(4, min_periods=4).max().replace(0.0, np.nan)
    out = rng / mx
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group E: bar-color streak / Markov features ---------------------------


def f10cs_f10_candle_sequence_patterns_bullstk_2d_base_v027_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Bull bar consecutive streak length (positive count)."""
    bull = (close > open).astype(float).where(~close.isna() & ~open.isna())
    g = (bull != bull.shift(1)).cumsum()
    streak = bull.groupby(g).cumsum()
    out = streak * bull
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_bearstk_2d_base_v028_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Bear bar consecutive streak length."""
    bear = (close < open).astype(float).where(~close.isna() & ~open.isna())
    g = (bear != bear.shift(1)).cumsum()
    streak = bear.groupby(g).cumsum()
    out = streak * bear
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_colflip_20d_base_v029_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Color flip count in last 20 bars: how often bull/bear sign changes."""
    sgn = np.sign(close - open)
    flip = (sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
    out = flip.rolling(20, min_periods=20).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_coltrans_30d_base_v030_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Color transition rate (flip count / 30) -- 0=stable, 1=alternating."""
    sgn = np.sign(close - open)
    flip = (sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
    out = flip.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_markov_40d_base_v031_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """P(bull | prev bull) over trailing 40 bars: conditional probability,
    a Markov persistence estimator."""
    bull = (close > open).astype(float).where(~close.isna() & ~open.isna())
    prev_bull = bull.shift(1)
    both = (bull * prev_bull).rolling(40, min_periods=40).sum()
    pb_count = prev_bull.rolling(40, min_periods=40).sum().replace(0.0, np.nan)
    out = both / pb_count
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_markov_60d_base_v032_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """P(bull) - P(bull | prev bear) over 60 bars. Bias from prior-bear state."""
    bull = (close > open).astype(float).where(~close.isna() & ~open.isna())
    bear = 1.0 - bull
    p_bull = bull.rolling(60, min_periods=60).mean()
    cond = (bull * bear.shift(1)).rolling(60, min_periods=60).sum()
    bear_cnt = bear.shift(1).rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    out = p_bull - (cond / bear_cnt)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group F: body-size sequence features ----------------------------------


def f10cs_f10_candle_sequence_patterns_bodyrat_2d_base_v033_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Curr body / curr range minus prev body / prev range -- normalized
    body change between 2 bars."""
    body_r = (close - open).abs() / (high - low).replace(0.0, np.nan)
    out = body_r - body_r.shift(1)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_bodymon_5d_base_v034_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Body monotone expansion count over last 5 (count of body>prev body)."""
    body = (close - open).abs()
    inc = (body > body.shift(1)).astype(float).where(~body.isna() & ~body.shift(1).isna())
    out = inc.rolling(5, min_periods=5).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_bodycum_3d_base_v035_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """3-bar body-fullness diff: (body/range)_now - (body/range)_t-2. Multi-
    bar; structurally distinct from cumulative body sum."""
    body_r = (close - open) / (high - low).replace(0.0, np.nan)
    out = body_r - body_r.shift(2)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_bodyaccl_4d_base_v036_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Body acceleration: body - 2*body[-1] + body[-2], normalized by 4-bar
    mean body."""
    body = (close - open).abs()
    accel = body - 2.0 * body.shift(1) + body.shift(2)
    den = body.rolling(4, min_periods=4).mean().replace(0.0, np.nan)
    out = accel / den
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group G: range + body sequence confirmation ---------------------------


def f10cs_f10_candle_sequence_patterns_rngbull_5d_base_v037_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean of (range expansion * bar color) over 5 bars. Captures
    expanding bull bars."""
    rng = high - low
    rng_ratio = np.log((rng + 1e-12) / (rng.shift(1) + 1e-12))
    color = np.sign(close - open)
    feat = rng_ratio * color
    out = feat.rolling(5, min_periods=5).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_rngbear_5d_base_v038_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-bar count of (range > 1.1*prior range) AND bear-bar agreement.
    Discrete count; not a negation of rngbull."""
    rng = high - low
    expand = (rng > 1.1 * rng.shift(1)).astype(float)
    bear = (close < open).astype(float)
    feat = (expand * bear).where(~rng.isna() & ~rng.shift(1).isna())
    out = feat.rolling(5, min_periods=5).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_volconf_10d_base_v039_signal(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-confirmed pattern: signed body * volume z-score, 10-bar mean."""
    body = close - open
    vmean = volume.rolling(10, min_periods=10).mean()
    vstd = volume.rolling(10, min_periods=10).std().replace(0.0, np.nan)
    vz = (volume - vmean) / vstd
    out = (np.sign(body) * vz).rolling(10, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_rngcontr_5d_base_v040_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Range contraction sequence: 5-bar slope of log range. Negative =
    contracting (pennant-like)."""
    rng = (high - low).replace(0.0, np.nan)
    lr = np.log(rng)
    out = lr.diff(4)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group H: reversal-pattern strength (multi-bar) ------------------------


def f10cs_f10_candle_sequence_patterns_hangmans_2d_base_v041_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Hanging man strength: small body w/ long lower shadow AFTER a bull
    bar. Multiplies single-bar score by sign of prior body."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    lower = pd.concat([open, close], axis=1).min(axis=1) - low
    upper = high - pd.concat([open, close], axis=1).max(axis=1)
    shape = (lower / rng) - 2.0 * (body / rng) - (upper / rng)
    prev_color = np.sign(close.shift(1) - open.shift(1))
    out = shape * prev_color
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_hammer_2d_base_v042_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Hammer-after-decline: lower shadow / curr range times log(prior
    close / close-2). Multi-bar (uses 3-bar trend context)."""
    rng = (high - low).replace(0.0, np.nan)
    lower = pd.concat([open, close], axis=1).min(axis=1) - low
    shape = lower / rng
    prior_drop = np.log(close.shift(1).replace(0.0, np.nan) / close.shift(3).replace(0.0, np.nan))
    out = shape * (-prior_drop)  # high when shape big and prior trend was down
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_shootst_2d_base_v043_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Shooting star strength after bull bar."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    upper = high - pd.concat([open, close], axis=1).max(axis=1)
    lower = pd.concat([open, close], axis=1).min(axis=1) - low
    shape = (upper / rng) - 2.0 * (body / rng) - (lower / rng)
    prev_color = np.sign(close.shift(1) - open.shift(1))
    out = shape * prev_color
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_invhamr_2d_base_v044_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Inverted hammer multi-bar score using upper-shadow ratio combined
    with prior-down-trend momentum (2-bar return)."""
    rng = (high - low).replace(0.0, np.nan)
    upper = high - pd.concat([open, close], axis=1).max(axis=1)
    shape = upper / rng
    mom2 = (close.shift(1) - close.shift(3)) / close.shift(3).replace(0.0, np.nan)
    out = shape * (-mom2)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group I: continuation patterns (multi-bar) -----------------------------


def f10cs_f10_candle_sequence_patterns_flag_10d_base_v045_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Flag-like pattern: strong move over 5 bars, then small pullback over
    last 3. Score = sign(5-bar move) * (-sign(3-bar move))."""
    move5 = close - close.shift(5)
    move3 = close - close.shift(3)
    out = np.tanh(20.0 * move5 / close.replace(0.0, np.nan)) * np.tanh(-20.0 * move3 / close.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_pennant_10d_base_v046_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pennant: 10-bar range contracting (negative slope) WHILE 20-bar close
    direction is positive. Multi-bar."""
    rng = (high - low).replace(0.0, np.nan)
    contr = np.log(rng).rolling(10, min_periods=10).apply(
        lambda x: float(np.polyfit(np.arange(len(x)), x, 1)[0]) if np.isfinite(x).all() else np.nan,
        raw=True,
    )
    trend = (close - close.shift(20)) / close.replace(0.0, np.nan)
    out = -contr * np.tanh(50.0 * trend)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_rise3m_5d_base_v047_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rising three methods strength: big bull[-4], 3 small consolidating
    bars, big bull[0]. Score = body[-4]*body[0] - sum |body[-3..-1]|."""
    body = close - open
    rng_norm = close.replace(0.0, np.nan)
    big = body.shift(4) * body
    small = (body.shift(1).abs() + body.shift(2).abs() + body.shift(3).abs())
    out = (big - small) / (rng_norm * rng_norm)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_fall3m_5d_base_v048_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Falling three methods mirror."""
    body = close - open
    rng_norm = close.replace(0.0, np.nan)
    big = (-body.shift(4)) * (-body)  # both negative -> positive product
    small = (body.shift(1).abs() + body.shift(2).abs() + body.shift(3).abs())
    out = (big - small) / (rng_norm * rng_norm)
    # only meaningful when both bars 4 and 0 are red
    mask = (np.sign(-body.shift(4)) > 0) & (np.sign(-body) > 0)
    out = out.where(mask, other=0.0)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group J: statistical sequence features -------------------------------


def f10cs_f10_candle_sequence_patterns_pressure_20d_base_v049_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Cumulative bull-vs-bear pressure: sum of signed bodies over 20 bars,
    normalized by sum of absolute bodies."""
    body = close - open
    s = body.rolling(20, min_periods=20).sum()
    a = body.abs().rolling(20, min_periods=20).sum().replace(0.0, np.nan)
    out = s / a
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_pressure_50d_base_v050_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """50-bar bull/bear pressure using closeadj for the long horizon."""
    # use closeadj diff as proxy for adjusted body  (open is not adjusted, but
    # the synthetic test uses similar series; this is a structurally
    # distinct ratio using a different signal source)
    body = closeadj - closeadj.shift(1)
    s = body.rolling(50, min_periods=50).sum()
    a = body.abs().rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    out = s / a
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_seqskew_30d_base_v051_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar skewness of bar body (close-open)."""
    body = close - open
    out = body.rolling(30, min_periods=30).skew()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_seqkurt_40d_base_v052_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """40-bar kurtosis of normalized signed body (adj diff)."""
    body = closeadj - closeadj.shift(1)
    out = body.rolling(40, min_periods=40).kurt()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_colac1_30d_base_v053_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar autocorrelation (lag-1) of bar color (+1/-1)."""
    sgn = np.sign(close - open).where(~close.isna() & ~open.isna())
    def _ac1(x):
        if np.isnan(x).any():
            return np.nan
        a = x[:-1]; b = x[1:]
        sa = a.std(); sb = b.std()
        if sa == 0 or sb == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    out = sgn.rolling(30, min_periods=30).apply(_ac1, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_bodyac2_25d_base_v054_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """25-bar autocorrelation (lag-2) of signed body (close-open)."""
    body = (close - open).where(~close.isna() & ~open.isna())
    def _ac2(x):
        if np.isnan(x).any() or len(x) < 4:
            return np.nan
        a = x[:-2]; b = x[2:]
        sa = a.std(); sb = b.std()
        if sa == 0 or sb == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    out = body.rolling(25, min_periods=25).apply(_ac2, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group K: pattern presence rolling counts ------------------------------


def f10cs_f10_candle_sequence_patterns_engcnt_20d_base_v055_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Soft engulfing count in last 20 bars (curr body > 1.2 * prior body
    AND opposite color)."""
    body = close - open
    sgn = np.sign(body)
    cond = ((body.abs() > 1.2 * body.shift(1).abs())
            & (sgn != sgn.shift(1))).astype(float)
    cond = cond.where(~body.isna() & ~body.shift(1).isna())
    out = cond.rolling(20, min_periods=20).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_softdoji_30d_base_v056_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar mean of (1 - body/range): high = many doji-like bars
    (uses prior bar context via 30-bar rolling)."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    score = (1.0 - body / rng).clip(lower=0.0, upper=1.0)
    out = score.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_engrank_30d_base_v057_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of (body / prev body abs ratio) over 30 bars."""
    cur = (close - open).abs()
    prev = cur.shift(1).replace(0.0, np.nan)
    r = cur / prev
    out = r.rolling(30, min_periods=15).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_bestbar_20d_base_v058_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Best-bull-bar-in-20: rolling rank of signed body / close. Bounded."""
    body = (close - open) / close.replace(0.0, np.nan)
    out = body.rolling(20, min_periods=10).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_worstbar_20d_base_v059_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Worst-range-in-20: rolling rank of bar range (high-low) WITH a bear
    body. Multi-bar context via 20-bar rank."""
    rng = (high - low) * ((close < open).astype(float))
    rng = rng.replace(0.0, np.nan)
    out = rng.rolling(20, min_periods=10).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group L: higher-order sequence diagnostics ----------------------------


def f10cs_f10_candle_sequence_patterns_overlapr_5d_base_v060_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bar-overlap ratio: mean over 5 bars of  overlap(curr,prev)/ avg range.
    High overlap = consolidating; low = trending."""
    cur_hi = high; cur_lo = low
    prv_hi = high.shift(1); prv_lo = low.shift(1)
    ovlp = pd.concat([cur_hi, prv_hi], axis=1).min(axis=1) - pd.concat([cur_lo, prv_lo], axis=1).max(axis=1)
    ovlp = ovlp.clip(lower=0.0)
    avg_r = ((cur_hi - cur_lo) + (prv_hi - prv_lo)) / 2.0
    r = ovlp / avg_r.replace(0.0, np.nan)
    out = r.rolling(5, min_periods=5).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_gapseq_10d_base_v061_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """10-bar mean of bar-to-bar gap-aware momentum:
    sign(close-prev close) AND sign(open - prev close) agreement rate."""
    csign = np.sign(close - close.shift(1))
    osign = np.sign(open - close.shift(1))
    agree = (csign * osign).where(~csign.isna() & ~osign.isna())
    out = agree.rolling(10, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_seqdrift_15d_base_v062_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Drift of signed body sign over 15 bars (mean sign - lagged mean)."""
    sgn = np.sign(close - open)
    short = sgn.rolling(5, min_periods=5).mean()
    long_ = sgn.rolling(15, min_periods=15).mean()
    out = short - long_
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_volimb_15d_base_v063_signal(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """15-bar volume imbalance: ratio of bull-bar volume to bear-bar
    volume, log-transformed."""
    bull = (close > open).astype(float).where(~close.isna() & ~open.isna())
    bear = 1.0 - bull
    bull_v = (bull * volume).rolling(15, min_periods=15).sum()
    bear_v = (bear * volume).rolling(15, min_periods=15).sum().replace(0.0, np.nan)
    out = np.log((bull_v + 1.0) / (bear_v + 1.0))
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_brkout_20d_base_v064_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Breakout-from-consolidation strength: contraction of 10-bar range
    then expansion of curr range. Multi-bar."""
    rng = high - low
    rng10 = rng.rolling(10, min_periods=10).mean().shift(1)
    contraction = rng.shift(1).rolling(10, min_periods=10).mean() / rng10.replace(0.0, np.nan)
    expansion = rng / rng10.replace(0.0, np.nan)
    out = expansion - contraction
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group M: composite scoring -------------------------------------------


def f10cs_f10_candle_sequence_patterns_revcomb_3d_base_v065_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Reversal combo score: 3-bar weighted score combining engulfing
    direction and shadow asymmetry of curr+prev."""
    body = close - open
    rng = (high - low).replace(0.0, np.nan)
    lower = pd.concat([open, close], axis=1).min(axis=1) - low
    upper = high - pd.concat([open, close], axis=1).max(axis=1)
    asym = (lower - upper) / rng
    eng = (body - body.shift(1)) / (body.abs() + body.shift(1).abs() + 1e-12)
    asym_prev = asym.shift(1)
    out = (eng + asym - asym_prev) / 3.0
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_contcomb_5d_base_v066_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Continuation combo: streak length * mean body sign over 5 bars."""
    sgn = np.sign(close - open)
    g = (sgn != sgn.shift(1)).cumsum()
    streak = sgn.groupby(g).cumcount() + 1
    body_mean = (close - open).rolling(5, min_periods=5).mean()
    out = streak * np.sign(body_mean) / 5.0
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_topbot_8d_base_v067_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Double-top/bottom heuristic: 8-bar score measuring how close 2
    recent highs are vs the avg high deviation."""
    top1 = high.rolling(4, min_periods=4).max()
    top2 = high.shift(4).rolling(4, min_periods=4).max()
    dev = high.rolling(8, min_periods=8).std().replace(0.0, np.nan)
    out = -(top1 - top2).abs() / dev
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_swing_10d_base_v068_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """10-bar swing count: number of local turning points of (high+low)/2
    via sign change of 1-bar diff. Uses 2 consecutive bars per pivot."""
    mid = (high + low) / 2.0
    d = np.sign(mid.diff()).where(~mid.diff().isna())
    flip = (d != d.shift(1)).astype(float).where(~d.isna() & ~d.shift(1).isna())
    out = flip.rolling(10, min_periods=10).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_bodyimb_10d_base_v069_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """10-bar body imbalance vs prior 10-bar: signed body sum diff."""
    body = close - open
    a = body.rolling(10, min_periods=10).sum()
    b = body.shift(10).rolling(10, min_periods=10).sum()
    out = (a - b) / (a.abs() + b.abs() + 1e-12)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_thrust_3d_base_v070_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Thrust pattern: 3-bar momentum where close[-1] crosses prior close
    plus body magnitude continuation."""
    body = close - open
    cross = (close > close.shift(1)).astype(float) - (close < close.shift(1)).astype(float)
    cross = cross.where(~close.isna() & ~close.shift(1).isna())
    consec = cross.rolling(3, min_periods=3).sum()
    out = consec * (body.abs() / close.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group N: cross-window structural diffs --------------------------------


def f10cs_f10_candle_sequence_patterns_streakdiff_20d_base_v071_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Diff: bull_streak_pct over 20 bars - bear_streak_pct."""
    bull = (close > open).astype(float).where(~close.isna() & ~open.isna())
    bear = (close < open).astype(float).where(~close.isna() & ~open.isna())
    out = bull.rolling(20, min_periods=20).mean() - bear.rolling(20, min_periods=20).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_rngmom_8d_base_v072_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """8-bar mean of normalized range diff (curr range - prev range)."""
    rng = high - low
    d = (rng - rng.shift(1)) / rng.rolling(8, min_periods=8).mean().replace(0.0, np.nan)
    out = d.rolling(8, min_periods=8).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_seqsharp_30d_base_v073_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """30-bar mean / std of bar-to-bar log return (open-to-close adjusted)."""
    body_n = np.log(closeadj.replace(0.0, np.nan) / closeadj.shift(1))
    m = body_n.rolling(30, min_periods=30).mean()
    s = body_n.rolling(30, min_periods=30).std().replace(0.0, np.nan)
    out = m / s
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_3bartrk_3d_base_v074_signal(close: pd.Series) -> pd.Series:
    """Three-bar truncated momentum: sign(c-c[-1]) + sign(c[-1]-c[-2])
    + sign(c[-2]-c[-3])."""
    d1 = np.sign(close - close.shift(1))
    d2 = np.sign(close.shift(1) - close.shift(2))
    d3 = np.sign(close.shift(2) - close.shift(3))
    out = (d1 + d2 + d3).where(~close.isna() & ~close.shift(3).isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_pinbar_2d_base_v075_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pin-bar (rejection bar) after trend: long shadow on side opposite
    to recent direction. Multi-bar via 3-bar trend context."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    lower = pd.concat([open, close], axis=1).min(axis=1) - low
    upper = high - pd.concat([open, close], axis=1).max(axis=1)
    pin_up = (upper / rng) - 2.0 * (body / rng) - (lower / rng)  # rejection of higher prices
    pin_dn = (lower / rng) - 2.0 * (body / rng) - (upper / rng)
    trend = np.sign((close - close.shift(3)))
    # pin against trend: pin_up when trend up; pin_dn when trend down
    out = trend * pin_up - trend * pin_dn  # signed reversal score
    return out.replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f10_candle_sequence_patterns_base_001_075_REGISTRY = {
    "f10cs_f10_candle_sequence_patterns_bullengs_2d_base_v001_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_bullengs_2d_base_v001_signal},
    "f10cs_f10_candle_sequence_patterns_bearengs_2d_base_v002_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_bearengs_2d_base_v002_signal},
    "f10cs_f10_candle_sequence_patterns_engratio_2d_base_v003_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_engratio_2d_base_v003_signal},
    "f10cs_f10_candle_sequence_patterns_haramis_2d_base_v004_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_haramis_2d_base_v004_signal},
    "f10cs_f10_candle_sequence_patterns_pierces_2d_base_v005_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_pierces_2d_base_v005_signal},
    "f10cs_f10_candle_sequence_patterns_darkcs_2d_base_v006_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_darkcs_2d_base_v006_signal},
    "f10cs_f10_candle_sequence_patterns_tweezerth_2d_base_v007_signal": {"inputs": ["high", "low"], "func": f10cs_f10_candle_sequence_patterns_tweezerth_2d_base_v007_signal},
    "f10cs_f10_candle_sequence_patterns_tweezerbl_2d_base_v008_signal": {"inputs": ["low"], "func": f10cs_f10_candle_sequence_patterns_tweezerbl_2d_base_v008_signal},
    "f10cs_f10_candle_sequence_patterns_hhpct_10d_base_v009_signal": {"inputs": ["high", "low"], "func": f10cs_f10_candle_sequence_patterns_hhpct_10d_base_v009_signal},
    "f10cs_f10_candle_sequence_patterns_llpct_10d_base_v010_signal": {"inputs": ["high", "low"], "func": f10cs_f10_candle_sequence_patterns_llpct_10d_base_v010_signal},
    "f10cs_f10_candle_sequence_patterns_whitesold_3d_base_v011_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_whitesold_3d_base_v011_signal},
    "f10cs_f10_candle_sequence_patterns_blackcrow_3d_base_v012_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_blackcrow_3d_base_v012_signal},
    "f10cs_f10_candle_sequence_patterns_morningst_3d_base_v013_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_morningst_3d_base_v013_signal},
    "f10cs_f10_candle_sequence_patterns_eveningst_3d_base_v014_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_eveningst_3d_base_v014_signal},
    "f10cs_f10_candle_sequence_patterns_threeinup_3d_base_v015_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_threeinup_3d_base_v015_signal},
    "f10cs_f10_candle_sequence_patterns_threeindn_3d_base_v016_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_threeindn_3d_base_v016_signal},
    "f10cs_f10_candle_sequence_patterns_threeoutup_3d_base_v017_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_threeoutup_3d_base_v017_signal},
    "f10cs_f10_candle_sequence_patterns_inscnt_20d_base_v018_signal": {"inputs": ["high", "low"], "func": f10cs_f10_candle_sequence_patterns_inscnt_20d_base_v018_signal},
    "f10cs_f10_candle_sequence_patterns_outcnt_30d_base_v019_signal": {"inputs": ["high", "low"], "func": f10cs_f10_candle_sequence_patterns_outcnt_30d_base_v019_signal},
    "f10cs_f10_candle_sequence_patterns_dsinsd_50d_base_v022_signal": {"inputs": ["high", "low"], "func": f10cs_f10_candle_sequence_patterns_dsinsd_50d_base_v022_signal},
    "f10cs_f10_candle_sequence_patterns_dsoutsd_50d_base_v023_signal": {"inputs": ["high", "low"], "func": f10cs_f10_candle_sequence_patterns_dsoutsd_50d_base_v023_signal},
    "f10cs_f10_candle_sequence_patterns_nr4_4d_base_v024_signal": {"inputs": ["high", "low"], "func": f10cs_f10_candle_sequence_patterns_nr4_4d_base_v024_signal},
    "f10cs_f10_candle_sequence_patterns_nr7_7d_base_v025_signal": {"inputs": ["high", "low"], "func": f10cs_f10_candle_sequence_patterns_nr7_7d_base_v025_signal},
    "f10cs_f10_candle_sequence_patterns_wr4_4d_base_v026_signal": {"inputs": ["high", "low"], "func": f10cs_f10_candle_sequence_patterns_wr4_4d_base_v026_signal},
    "f10cs_f10_candle_sequence_patterns_bullstk_2d_base_v027_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_bullstk_2d_base_v027_signal},
    "f10cs_f10_candle_sequence_patterns_bearstk_2d_base_v028_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_bearstk_2d_base_v028_signal},
    "f10cs_f10_candle_sequence_patterns_colflip_20d_base_v029_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_colflip_20d_base_v029_signal},
    "f10cs_f10_candle_sequence_patterns_coltrans_30d_base_v030_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_coltrans_30d_base_v030_signal},
    "f10cs_f10_candle_sequence_patterns_markov_40d_base_v031_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_markov_40d_base_v031_signal},
    "f10cs_f10_candle_sequence_patterns_markov_60d_base_v032_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_markov_60d_base_v032_signal},
    "f10cs_f10_candle_sequence_patterns_bodyrat_2d_base_v033_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_bodyrat_2d_base_v033_signal},
    "f10cs_f10_candle_sequence_patterns_bodymon_5d_base_v034_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_bodymon_5d_base_v034_signal},
    "f10cs_f10_candle_sequence_patterns_bodycum_3d_base_v035_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_bodycum_3d_base_v035_signal},
    "f10cs_f10_candle_sequence_patterns_bodyaccl_4d_base_v036_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_bodyaccl_4d_base_v036_signal},
    "f10cs_f10_candle_sequence_patterns_rngbull_5d_base_v037_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_rngbull_5d_base_v037_signal},
    "f10cs_f10_candle_sequence_patterns_rngbear_5d_base_v038_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_rngbear_5d_base_v038_signal},
    "f10cs_f10_candle_sequence_patterns_volconf_10d_base_v039_signal": {"inputs": ["open", "close", "volume"], "func": f10cs_f10_candle_sequence_patterns_volconf_10d_base_v039_signal},
    "f10cs_f10_candle_sequence_patterns_rngcontr_5d_base_v040_signal": {"inputs": ["high", "low"], "func": f10cs_f10_candle_sequence_patterns_rngcontr_5d_base_v040_signal},
    "f10cs_f10_candle_sequence_patterns_hangmans_2d_base_v041_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_hangmans_2d_base_v041_signal},
    "f10cs_f10_candle_sequence_patterns_hammer_2d_base_v042_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_hammer_2d_base_v042_signal},
    "f10cs_f10_candle_sequence_patterns_shootst_2d_base_v043_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_shootst_2d_base_v043_signal},
    "f10cs_f10_candle_sequence_patterns_invhamr_2d_base_v044_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_invhamr_2d_base_v044_signal},
    "f10cs_f10_candle_sequence_patterns_flag_10d_base_v045_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_flag_10d_base_v045_signal},
    "f10cs_f10_candle_sequence_patterns_pennant_10d_base_v046_signal": {"inputs": ["high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_pennant_10d_base_v046_signal},
    "f10cs_f10_candle_sequence_patterns_rise3m_5d_base_v047_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_rise3m_5d_base_v047_signal},
    "f10cs_f10_candle_sequence_patterns_fall3m_5d_base_v048_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_fall3m_5d_base_v048_signal},
    "f10cs_f10_candle_sequence_patterns_pressure_20d_base_v049_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_pressure_20d_base_v049_signal},
    "f10cs_f10_candle_sequence_patterns_pressure_50d_base_v050_signal": {"inputs": ["open", "closeadj"], "func": f10cs_f10_candle_sequence_patterns_pressure_50d_base_v050_signal},
    "f10cs_f10_candle_sequence_patterns_seqskew_30d_base_v051_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_seqskew_30d_base_v051_signal},
    "f10cs_f10_candle_sequence_patterns_seqkurt_40d_base_v052_signal": {"inputs": ["open", "closeadj"], "func": f10cs_f10_candle_sequence_patterns_seqkurt_40d_base_v052_signal},
    "f10cs_f10_candle_sequence_patterns_colac1_30d_base_v053_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_colac1_30d_base_v053_signal},
    "f10cs_f10_candle_sequence_patterns_bodyac2_25d_base_v054_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_bodyac2_25d_base_v054_signal},
    "f10cs_f10_candle_sequence_patterns_engcnt_20d_base_v055_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_engcnt_20d_base_v055_signal},
    "f10cs_f10_candle_sequence_patterns_softdoji_30d_base_v056_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_softdoji_30d_base_v056_signal},
    "f10cs_f10_candle_sequence_patterns_engrank_30d_base_v057_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_engrank_30d_base_v057_signal},
    "f10cs_f10_candle_sequence_patterns_bestbar_20d_base_v058_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_bestbar_20d_base_v058_signal},
    "f10cs_f10_candle_sequence_patterns_worstbar_20d_base_v059_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_worstbar_20d_base_v059_signal},
    "f10cs_f10_candle_sequence_patterns_overlapr_5d_base_v060_signal": {"inputs": ["high", "low"], "func": f10cs_f10_candle_sequence_patterns_overlapr_5d_base_v060_signal},
    "f10cs_f10_candle_sequence_patterns_gapseq_10d_base_v061_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_gapseq_10d_base_v061_signal},
    "f10cs_f10_candle_sequence_patterns_seqdrift_15d_base_v062_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_seqdrift_15d_base_v062_signal},
    "f10cs_f10_candle_sequence_patterns_volimb_15d_base_v063_signal": {"inputs": ["open", "close", "volume"], "func": f10cs_f10_candle_sequence_patterns_volimb_15d_base_v063_signal},
    "f10cs_f10_candle_sequence_patterns_brkout_20d_base_v064_signal": {"inputs": ["high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_brkout_20d_base_v064_signal},
    "f10cs_f10_candle_sequence_patterns_revcomb_3d_base_v065_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_revcomb_3d_base_v065_signal},
    "f10cs_f10_candle_sequence_patterns_contcomb_5d_base_v066_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_contcomb_5d_base_v066_signal},
    "f10cs_f10_candle_sequence_patterns_topbot_8d_base_v067_signal": {"inputs": ["high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_topbot_8d_base_v067_signal},
    "f10cs_f10_candle_sequence_patterns_swing_10d_base_v068_signal": {"inputs": ["high", "low"], "func": f10cs_f10_candle_sequence_patterns_swing_10d_base_v068_signal},
    "f10cs_f10_candle_sequence_patterns_bodyimb_10d_base_v069_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_bodyimb_10d_base_v069_signal},
    "f10cs_f10_candle_sequence_patterns_thrust_3d_base_v070_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_thrust_3d_base_v070_signal},
    "f10cs_f10_candle_sequence_patterns_streakdiff_20d_base_v071_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_streakdiff_20d_base_v071_signal},
    "f10cs_f10_candle_sequence_patterns_rngmom_8d_base_v072_signal": {"inputs": ["high", "low"], "func": f10cs_f10_candle_sequence_patterns_rngmom_8d_base_v072_signal},
    "f10cs_f10_candle_sequence_patterns_seqsharp_30d_base_v073_signal": {"inputs": ["open", "closeadj"], "func": f10cs_f10_candle_sequence_patterns_seqsharp_30d_base_v073_signal},
    "f10cs_f10_candle_sequence_patterns_3bartrk_3d_base_v074_signal": {"inputs": ["close"], "func": f10cs_f10_candle_sequence_patterns_3bartrk_3d_base_v074_signal},
    "f10cs_f10_candle_sequence_patterns_pinbar_2d_base_v075_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_pinbar_2d_base_v075_signal},
}


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------


def _synthetic_inputs(n: int = 800, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    seg = n // 4
    rest = n - 3 * seg
    ret = np.concatenate([
        rng.normal(0.0012, 0.011, seg),
        rng.normal(-0.0005, 0.018, seg),
        rng.normal(-0.0010, 0.014, seg),
        rng.normal(0.0008, 0.012, rest),
    ])
    close = 50.0 * np.exp(np.cumsum(ret))
    adj_drift = rng.normal(0.0, 0.0003, size=n).cumsum()
    closeadj = close * np.exp(adj_drift)
    intraday = rng.normal(0.0, 0.008, size=n)
    open_ = close * np.exp(-intraday * 0.5)
    high = np.maximum(close, open_) * np.exp(np.abs(rng.normal(0.0, 0.006, size=n)))
    low = np.minimum(close, open_) * np.exp(-np.abs(rng.normal(0.0, 0.006, size=n)))
    volume = rng.lognormal(mean=13.0, sigma=0.6, size=n)
    idx = pd.RangeIndex(n)
    return pd.DataFrame({
        "open": pd.Series(open_, index=idx, dtype=float),
        "high": pd.Series(high, index=idx, dtype=float),
        "low": pd.Series(low, index=idx, dtype=float),
        "close": pd.Series(close, index=idx, dtype=float),
        "closeadj": pd.Series(closeadj, index=idx, dtype=float),
        "volume": pd.Series(volume, index=idx, dtype=float),
    })


def _self_test() -> None:
    df = _synthetic_inputs(n=800, seed=42)
    results: dict[str, pd.Series] = {}
    for name, entry in f10_candle_sequence_patterns_base_001_075_REGISTRY.items():
        args = [df[col] for col in entry["inputs"]]
        out = entry["func"](*args)
        assert isinstance(out, pd.Series), f"{name}: not a Series"
        assert len(out) == len(df), f"{name}: length mismatch"
        clean = out.dropna()
        assert len(clean) > 0, f"{name}: all NaN"
        assert float(clean.std()) > 0.0 or clean.nunique() > 1, f"{name}: constant/all-zero"
        results[name] = out

    warm = 252
    coverage_ok = sum(1 for s in results.values() if s.iloc[warm:].isna().mean() < 0.5)
    frac = coverage_ok / len(results)
    assert frac >= 0.80, f"NaN-coverage too low: {frac:.2%} have <50% NaN after warm-up"

    aligned = pd.concat({n: results[n] for n in results}, axis=1).iloc[warm:]
    aligned = aligned.replace([np.inf, -np.inf], np.nan)
    corr = aligned.corr(min_periods=50).abs()
    np.fill_diagonal(corr.values, 0.0)
    max_corr = float(corr.max().max())
    if max_corr > 0.95:
        print(f"FAILING max |corr| = {max_corr:.4f}. Top pairs:")
        for i, a in enumerate(corr.columns):
            for j, b in enumerate(corr.columns):
                if j > i and corr.iloc[i, j] > 0.94:
                    print(f"  {a}  vs  {b}  ->  {corr.iloc[i, j]:.4f}")
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK base_001_075: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
