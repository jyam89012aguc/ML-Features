"""f10_candle_sequence_patterns base features 076-150.

Continuation of the multi-bar candle-sequence-pattern domain. Each
feature references >= 2 bars via shifts of open/high/low/close (with
volume where relevant). Continuous strength scores, rolling counts,
sequence diagnostics. NaN policy: only replace([inf,-inf], nan) at
final return.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Features 076-150
# ---------------------------------------------------------------------------


# --- Group A: extended 2-bar / 3-bar pattern strength ---------------------


def f10cs_f10_candle_sequence_patterns_bsidvr_2d_base_v076_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Body-side identity vs prev: same-color streak boolean times relative
    body proportion change."""
    body = close - open
    same_col = np.sign(body) * np.sign(body.shift(1))
    rng = (high - low).replace(0.0, np.nan)
    rel = (body.abs() - body.shift(1).abs()) / rng
    out = same_col * rel
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_concl3_3d_base_v077_signal(close: pd.Series) -> pd.Series:
    """Three-bar concavity: close - 2*close[-1] + close[-2] normalized by
    3-bar mean close. Multi-bar second-difference."""
    c2 = close - 2.0 * close.shift(1) + close.shift(2)
    den = close.rolling(3, min_periods=3).mean().replace(0.0, np.nan)
    out = c2 / den
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_gap2bdy_2d_base_v078_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 2-bar overnight gap to combined body magnitude
    (open - prev close) / (|body| + |prev body|)."""
    gap = open - close.shift(1)
    den = (close - open).abs() + (close.shift(1) - open.shift(1)).abs()
    out = gap / den.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_2bartrk_2d_base_v079_signal(close: pd.Series) -> pd.Series:
    """Two-bar truncated momentum sign sum: sign(c-c[-1]) + sign(c[-1]-c[-2])."""
    d1 = np.sign(close - close.shift(1))
    d2 = np.sign(close.shift(1) - close.shift(2))
    out = (d1 + d2).where(~close.isna() & ~close.shift(2).isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_bothshad_3d_base_v080_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """3-bar mean of shadow-symmetry: |upper-lower|/range -- continuous,
    multi-bar via rolling."""
    upper = high - pd.concat([open, close], axis=1).max(axis=1)
    lower = pd.concat([open, close], axis=1).min(axis=1) - low
    rng = (high - low).replace(0.0, np.nan)
    asym = (upper - lower) / rng
    out = asym.rolling(3, min_periods=3).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_riseclos_5d_base_v081_signal(close: pd.Series) -> pd.Series:
    """Fraction of 5-bar window with close[t] > close[t-1] (count form)."""
    up = (close > close.shift(1)).astype(float).where(~close.isna() & ~close.shift(1).isna())
    out = up.rolling(5, min_periods=5).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_clsclose_2d_base_v082_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """2-bar close-vs-open consistency: are both bars closing in same
    direction relative to opens? +1 same, -1 opposite."""
    s_cur = np.sign(close - open)
    s_prv = np.sign(close.shift(1) - open.shift(1))
    out = (s_cur * s_prv).where(~s_cur.isna() & ~s_prv.isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_thirteenseq_13d_base_v083_signal(close: pd.Series) -> pd.Series:
    """13-bar setup count: number of bars in last 13 where close > close[-4]
    (TD-Sequential-style). Multi-bar with lag 4."""
    flag = (close > close.shift(4)).astype(float).where(~close.isna() & ~close.shift(4).isna())
    out = flag.rolling(13, min_periods=13).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_dnsetup_9d_base_v084_signal(close: pd.Series) -> pd.Series:
    """9-bar TD-style setup down count: close < close[-4] occurrences."""
    flag = (close < close.shift(4)).astype(float).where(~close.isna() & ~close.shift(4).isna())
    out = flag.rolling(9, min_periods=9).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group B: gap-and-pattern joint signals ----------------------------


def f10cs_f10_candle_sequence_patterns_islndrev_3d_base_v085_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Island reversal continuous strength: gap on day -1, gap on day 0 in
    opposite direction. Score = sign(gap0) * (-sign(gap_prev)) * scaled
    magnitudes."""
    gap_prev = (low.shift(1) - high.shift(2)).clip(lower=0.0) - (low.shift(2) - high.shift(1)).clip(lower=0.0)
    gap_cur = (high - low.shift(1)).clip(lower=0.0) - (high.shift(1) - low).clip(lower=0.0)
    norm = (high - low).rolling(20, min_periods=20).mean().replace(0.0, np.nan)
    out = -(gap_prev * gap_cur) / (norm * norm)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_winflwthru_3d_base_v086_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """3-bar bull follow-through: each successive bar greener than prev,
    measured as count + cumulative-body normalized."""
    body = close - open
    seq = ((body > 0) & (body.shift(1) > 0) & (body.shift(2) > 0)).astype(float)
    seq = seq.where(~body.isna() & ~body.shift(2).isna())
    cum = (body + body.shift(1) + body.shift(2)) / close.replace(0.0, np.nan)
    out = seq * cum
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_losflwthru_3d_base_v087_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """3-bar bear follow-through (mirror); separate by 3-bar all-red filter."""
    body = close - open
    seq = ((body < 0) & (body.shift(1) < 0) & (body.shift(2) < 0)).astype(float)
    seq = seq.where(~body.isna() & ~body.shift(2).isna())
    cum = (body + body.shift(1) + body.shift(2)) / close.replace(0.0, np.nan)
    out = seq * cum  # negative score reflects strength
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group C: rolling-N pattern counts and percentiles ------------------


def f10cs_f10_candle_sequence_patterns_engcnt_40d_base_v088_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Engulfing-like count in last 40 bars: body[t].abs > body[t-1].abs and
    opposite color."""
    body = close - open
    sgn = np.sign(body)
    cond = ((body.abs() > body.shift(1).abs())
            & (sgn != sgn.shift(1))).astype(float)
    cond = cond.where(~body.isna() & ~body.shift(1).isna())
    out = cond.rolling(40, min_periods=40).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_haramicnt_30d_base_v089_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Harami-like count in 30 bars (curr body abs < 0.7 prev body abs and
    opposite color)."""
    body = close - open
    sgn = np.sign(body)
    cond = ((body.abs() < 0.7 * body.shift(1).abs())
            & (sgn != sgn.shift(1))
            & (body.shift(1).abs() > 1e-12)).astype(float)
    cond = cond.where(~body.isna() & ~body.shift(1).isna())
    out = cond.rolling(30, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_dojicnt_25d_base_v090_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Doji-like count: 25-bar count of bars with body/range < 0.15
    PRECEDED by a non-doji bar."""
    body_r = (close - open).abs() / (high - low).replace(0.0, np.nan)
    doji = (body_r < 0.15).astype(float)
    non_doji_prev = (body_r.shift(1) >= 0.15).astype(float)
    cond = (doji * non_doji_prev).where(~body_r.isna() & ~body_r.shift(1).isna())
    out = cond.rolling(25, min_periods=25).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_revcnt_20d_base_v091_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Reversal count: 20-bar count of bars where sign(body) != sign(prev
    body) AND |close diff| > 1.5 * 20-bar mean |close diff|."""
    body_s = np.sign(close - open)
    chg = (close - close.shift(1)).abs()
    m = chg.rolling(20, min_periods=20).mean().replace(0.0, np.nan)
    cond = ((body_s != body_s.shift(1)) & (chg > 1.5 * m)).astype(float)
    cond = cond.where(~body_s.isna() & ~body_s.shift(1).isna())
    out = cond.rolling(20, min_periods=20).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_btopcnt_30d_base_v092_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish top hint count: 30-bar count of bars where high > prev high
    BUT close < prev close (upside rejection)."""
    cond = ((high > high.shift(1)) & (close < close.shift(1))).astype(float)
    cond = cond.where(~high.isna() & ~high.shift(1).isna() & ~close.isna())
    out = cond.rolling(30, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_bbotcnt_30d_base_v093_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bullish bottom hint count: low < prev low BUT close > prev close."""
    cond = ((low < low.shift(1)) & (close > close.shift(1))).astype(float)
    cond = cond.where(~low.isna() & ~low.shift(1).isna() & ~close.isna())
    out = cond.rolling(30, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group D: distance-to-pattern continuous signals -----------------


def f10cs_f10_candle_sequence_patterns_distinsd_10d_base_v094_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance to inside-bar criterion: (high - prev_high) + (prev_low -
    low), normalized by 10-bar range. Negative when current bar is
    inside; positive when fully outside."""
    a = high - high.shift(1)
    b = low.shift(1) - low
    avg_r = (high - low).rolling(10, min_periods=10).mean().replace(0.0, np.nan)
    out = (a - b) / avg_r  # range-asymmetric measure
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_distoutsd_10d_base_v095_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance to outside-bar criterion: (high - prev_high) - (low -
    prev_low), normalized by 10-bar range."""
    a = high - high.shift(1)
    b = low - low.shift(1)
    avg_r = (high - low).rolling(10, min_periods=10).mean().replace(0.0, np.nan)
    out = (a - b) / avg_r
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_disteng_2d_base_v096_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Continuous engulfing distance: (body - 1.0*prev_body) / std(body, 20)."""
    body = close - open
    sd = body.rolling(20, min_periods=20).std().replace(0.0, np.nan)
    out = (body - body.shift(1)) / sd
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_disthar_2d_base_v097_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Continuous harami distance: log(|body|/|prev body|) when body has
    opposite color; else 0."""
    body = close - open
    sgn = np.sign(body)
    raw = np.log((body.abs() + 1e-12) / (body.shift(1).abs() + 1e-12))
    mask = (sgn != sgn.shift(1)).astype(float)
    out = raw * mask
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group E: cross-feature normalized differentials ----------------


def f10cs_f10_candle_sequence_patterns_engdiff_20d_base_v098_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Engulf-count - harami-count over 20 bars (signed sequence balance)."""
    body = close - open
    sgn = np.sign(body)
    eng = ((body.abs() > body.shift(1).abs()) & (sgn != sgn.shift(1))).astype(float)
    har = ((body.abs() < body.shift(1).abs()) & (sgn != sgn.shift(1))).astype(float)
    eng = eng.where(~body.isna() & ~body.shift(1).isna())
    har = har.where(~body.isna() & ~body.shift(1).isna())
    out = eng.rolling(20, min_periods=20).sum() - har.rolling(20, min_periods=20).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_insoutd_30d_base_v099_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Inside-count - outside-count over 30 bars."""
    inside = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    outside = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
    inside = inside.where(~high.isna() & ~high.shift(1).isna())
    outside = outside.where(~high.isna() & ~high.shift(1).isna())
    out = inside.rolling(30, min_periods=30).sum() - outside.rolling(30, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group F: sequence runs/streaks of OHLC structure ---------------


def f10cs_f10_candle_sequence_patterns_hhstk_2d_base_v100_signal(high: pd.Series) -> pd.Series:
    """Consecutive higher-high streak length."""
    hh = (high > high.shift(1)).astype(float).where(~high.isna() & ~high.shift(1).isna())
    g = (hh != hh.shift(1)).cumsum()
    streak = hh.groupby(g).cumsum()
    out = streak * hh
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_llstk_2d_base_v101_signal(low: pd.Series) -> pd.Series:
    """Consecutive lower-low streak length."""
    ll = (low < low.shift(1)).astype(float).where(~low.isna() & ~low.shift(1).isna())
    g = (ll != ll.shift(1)).cumsum()
    streak = ll.groupby(g).cumsum()
    out = streak * ll
    return out.replace([np.inf, -np.inf], np.nan)






# --- Group G: pattern-strength rolling means ------------------------


def f10cs_f10_candle_sequence_patterns_engsmean_20d_base_v104_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """20-bar mean engulfing strength (signed body diff / sum body abs)."""
    body = close - open
    raw = (body - body.shift(1))
    den = (body.abs() + body.shift(1).abs()).replace(0.0, np.nan)
    s = raw / den
    out = s.rolling(20, min_periods=20).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_harasm_30d_base_v105_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar mean of harami containment score."""
    cur_hi = pd.concat([open, close], axis=1).max(axis=1)
    cur_lo = pd.concat([open, close], axis=1).min(axis=1)
    prv_hi = cur_hi.shift(1); prv_lo = cur_lo.shift(1)
    body = (prv_hi - prv_lo).replace(0.0, np.nan)
    over_h = (cur_hi - prv_hi).clip(lower=0.0) / body
    over_l = (prv_lo - cur_lo).clip(lower=0.0) / body
    s = 1.0 - (over_h + over_l)
    out = s.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_tweezm_20d_base_v106_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """20-bar mean of -|high diff|/(high+prev high) ('tweezer affinity')."""
    diff = (high - high.shift(1)).abs()
    den = (high + high.shift(1)).replace(0.0, np.nan)
    s = -(diff / den)
    out = s.rolling(20, min_periods=20).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group H: high-low touch / breakout sequences ------------------


def f10cs_f10_candle_sequence_patterns_highbrk_10d_base_v107_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of 10-bar window where close > rolling-5-bar prior high (a
    breakout above prior 5-bar high). Multi-bar."""
    prior_hi = high.shift(1).rolling(5, min_periods=5).max()
    brk = (close > prior_hi).astype(float).where(~prior_hi.isna() & ~close.isna())
    out = brk.rolling(10, min_periods=10).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_lowbrk_10d_base_v108_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of 10-bar window where close < rolling-5-bar prior low."""
    prior_lo = low.shift(1).rolling(5, min_periods=5).min()
    brk = (close < prior_lo).astype(float).where(~prior_lo.isna() & ~close.isna())
    out = brk.rolling(10, min_periods=10).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_failbrk_15d_base_v109_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    """Failed-breakout count: 15-bar count of bars where high > prior 5-bar
    high but close < the prior high. Multi-bar."""
    prior_hi = high.shift(1).rolling(5, min_periods=5).max()
    cond = ((high > prior_hi) & (close < prior_hi)).astype(float).where(~prior_hi.isna())
    out = cond.rolling(15, min_periods=15).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group I: body-color alignment with close/open differentials ---


def f10cs_f10_candle_sequence_patterns_colcons_15d_base_v110_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """15-bar fraction of bars whose color agrees with closing direction
    (close>prev close iff close>open)."""
    co = np.sign(close - close.shift(1))
    bo = np.sign(close - open)
    agree = (co == bo).astype(float).where(~co.isna() & ~bo.isna())
    out = agree.rolling(15, min_periods=15).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_oprng_10d_base_v111_signal(open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Open vs prior range: (open - prev_mid)/prev_range. 10-bar mean.
    Indicator of trend bias at the open."""
    prv_mid = (high.shift(1) + low.shift(1)) / 2.0
    prv_rng = (high.shift(1) - low.shift(1)).replace(0.0, np.nan)
    s = (open - prv_mid) / prv_rng
    out = s.rolling(10, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_clrng_15d_base_v112_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close vs prior range: (close - prev_mid)/prev_range -- 15-bar mean."""
    prv_mid = (high.shift(1) + low.shift(1)) / 2.0
    prv_rng = (high.shift(1) - low.shift(1)).replace(0.0, np.nan)
    s = (close - prv_mid) / prv_rng
    out = s.rolling(15, min_periods=15).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group J: volume-confirmed pattern features ---------------------


def f10cs_f10_candle_sequence_patterns_volup_20d_base_v113_signal(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """20-bar fraction of bull bars with above-average volume."""
    bull = (close > open).astype(float)
    vmean = volume.rolling(20, min_periods=20).mean()
    high_v = (volume > vmean).astype(float)
    s = (bull * high_v).where(~bull.isna() & ~high_v.isna())
    out = s.rolling(20, min_periods=20).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_voldn_20d_base_v114_signal(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """20-bar fraction of bear bars with above-average volume."""
    bear = (close < open).astype(float)
    vmean = volume.rolling(20, min_periods=20).mean()
    high_v = (volume > vmean).astype(float)
    s = (bear * high_v).where(~bear.isna() & ~high_v.isna())
    out = s.rolling(20, min_periods=20).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_volclmx_30d_base_v115_signal(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """30-bar signed body weighted by volume z-score and summed."""
    body = close - open
    vmean = volume.rolling(30, min_periods=30).mean()
    vstd = volume.rolling(30, min_periods=30).std().replace(0.0, np.nan)
    vz = (volume - vmean) / vstd
    w = body * vz / close.replace(0.0, np.nan)
    out = w.rolling(30, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group K: statistical sequence ---------------------------------


def f10cs_f10_candle_sequence_patterns_clseac1_25d_base_v116_signal(close: pd.Series) -> pd.Series:
    """25-bar lag-1 autocorrelation of close diff sign."""
    s = np.sign(close.diff()).where(~close.isna())
    def _ac1(x):
        if np.isnan(x).any():
            return np.nan
        a = x[:-1]; b = x[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    out = s.rolling(25, min_periods=25).apply(_ac1, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_rngac1_30d_base_v117_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """30-bar lag-1 autocorrelation of (high - low)."""
    rng = (high - low).where(~high.isna() & ~low.isna())
    def _ac1(x):
        if np.isnan(x).any():
            return np.nan
        a = x[:-1]; b = x[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    out = rng.rolling(30, min_periods=30).apply(_ac1, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_bodyrs_30d_base_v118_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar rescaled-range Hurst proxy of body sign series:
    log(R/S) — measures persistence of bull/bear sequence."""
    s = np.sign(close - open).where(~close.isna() & ~open.isna())
    def _rs(x):
        x = x - x.mean()
        c = x.cumsum()
        R = c.max() - c.min()
        S = x.std()
        if S == 0:
            return np.nan
        return float(np.log((R / S) + 1e-12))
    out = s.rolling(30, min_periods=30).apply(_rs, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_seqent_30d_base_v119_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar binary entropy of bar color sequence."""
    bull = (close > open).astype(float).where(~close.isna() & ~open.isna())
    def _ent(x):
        if np.isnan(x).any():
            return np.nan
        p = float(np.mean(x))
        if p <= 0.0 or p >= 1.0:
            return 0.0
        return -p * np.log(p) - (1.0 - p) * np.log(1.0 - p)
    out = bull.rolling(30, min_periods=30).apply(_ent, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_runlen_50d_base_v120_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """50-bar mean run-length of consecutive bull or bear bars."""
    sgn = np.sign(close - open)
    def _mean_run(x):
        if np.isnan(x).any() or len(x) < 2:
            return np.nan
        runs = []; cur = 1
        for i in range(1, len(x)):
            if x[i] == x[i-1]:
                cur += 1
            else:
                runs.append(cur); cur = 1
        runs.append(cur)
        return float(np.mean(runs))
    out = sgn.rolling(50, min_periods=50).apply(_mean_run, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group L: pattern-rank / percentile signals --------------------


def f10cs_f10_candle_sequence_patterns_engrank_50d_base_v121_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """50-bar percentile rank of (body_abs - prev_body_abs)."""
    body = (close - open).abs()
    diff = body - body.shift(1)
    out = diff.rolling(50, min_periods=25).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_brngrnk_30d_base_v122_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """30-bar percentile rank of (range / prev range)."""
    rng = (high - low)
    ratio = rng / rng.shift(1).replace(0.0, np.nan)
    out = ratio.rolling(30, min_periods=15).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group M: longer-horizon adjusted sequence (closeadj) ----------


def f10cs_f10_candle_sequence_patterns_seqdir_60d_base_v123_signal(closeadj: pd.Series) -> pd.Series:
    """60-bar mean sign of (closeadj - closeadj.shift(1)). Quarterly bias."""
    s = np.sign(closeadj - closeadj.shift(1)).where(~closeadj.isna())
    out = s.rolling(60, min_periods=60).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_seqac1_80d_base_v124_signal(closeadj: pd.Series) -> pd.Series:
    """80-bar lag-1 autocorrelation of log returns of closeadj."""
    r = np.log(closeadj.replace(0.0, np.nan) / closeadj.shift(1))
    def _ac1(x):
        if np.isnan(x).any():
            return np.nan
        a = x[:-1]; b = x[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    out = r.rolling(80, min_periods=80).apply(_ac1, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_drmonotn_40d_base_v125_signal(closeadj: pd.Series) -> pd.Series:
    """40-bar 'monotonicity score': (max consec up runs - max consec down
    runs) / 40."""
    s = np.sign(closeadj.diff()).where(~closeadj.isna())
    def _mono(x):
        if np.isnan(x).any() or len(x) < 2:
            return np.nan
        max_up = max_dn = cur = 1; sign = 0
        for i in range(1, len(x)):
            if x[i] == x[i-1] and x[i] != 0:
                cur += 1
            else:
                if sign > 0:
                    max_up = max(max_up, cur)
                elif sign < 0:
                    max_dn = max(max_dn, cur)
                cur = 1; sign = x[i]
                continue
            sign = x[i]
        if sign > 0:
            max_up = max(max_up, cur)
        elif sign < 0:
            max_dn = max(max_dn, cur)
        return float(max_up - max_dn) / float(len(x))
    out = s.rolling(40, min_periods=40).apply(_mono, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group N: sequence dispersion / variability ----------------


def f10cs_f10_candle_sequence_patterns_bodyvar_25d_base_v126_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """25-bar std of signed body / 25-bar mean |body|."""
    body = close - open
    s = body.rolling(25, min_periods=25).std()
    m = body.abs().rolling(25, min_periods=25).mean().replace(0.0, np.nan)
    out = s / m
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_seqvar_30d_base_v127_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """30-bar std of range-diff (range expansion variability)."""
    rng = high - low
    d = rng - rng.shift(1)
    out = d.rolling(30, min_periods=30).std()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_clmad_20d_base_v128_signal(close: pd.Series) -> pd.Series:
    """20-bar MAD of close diff / 20-bar std of close diff. Sequence
    leptokurtosis."""
    d = close.diff()
    mad = (d - d.rolling(20, min_periods=20).mean()).abs().rolling(20, min_periods=20).mean()
    sd = d.rolling(20, min_periods=20).std().replace(0.0, np.nan)
    out = mad / sd
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group O: pattern bias signals --------------------------


def f10cs_f10_candle_sequence_patterns_morncnt_50d_base_v129_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """50-bar count of soft morning-star: bear bar at -2, small body at -1,
    bull bar at 0."""
    body = close - open
    rng = (high - low).replace(0.0, np.nan)
    rel = body / rng
    cond = ((rel.shift(2) < -0.3) & (rel.shift(1).abs() < 0.3) & (rel > 0.3)).astype(float)
    cond = cond.where(~rel.shift(2).isna() & ~rel.isna())
    out = cond.rolling(50, min_periods=50).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_evencnt_50d_base_v130_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """50-bar count of soft evening-star."""
    body = close - open
    rng = (high - low).replace(0.0, np.nan)
    rel = body / rng
    cond = ((rel.shift(2) > 0.3) & (rel.shift(1).abs() < 0.3) & (rel < -0.3)).astype(float)
    cond = cond.where(~rel.shift(2).isna() & ~rel.isna())
    out = cond.rolling(50, min_periods=50).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_3soldcnt_40d_base_v131_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """40-bar count of soft three-white-soldiers: 3 consecutive bull bars
    with rising closes."""
    body = close - open
    bull = (body > 0).astype(float)
    rising = (close > close.shift(1)).astype(float)
    cond = (bull * bull.shift(1) * bull.shift(2)
            * rising * rising.shift(1) * rising.shift(2))
    cond = cond.where(~body.isna() & ~body.shift(2).isna())
    out = cond.rolling(40, min_periods=40).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_3crowcnt_40d_base_v132_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """40-bar count of soft three-black-crows."""
    body = close - open
    bear = (body < 0).astype(float)
    falling = (close < close.shift(1)).astype(float)
    cond = (bear * bear.shift(1) * bear.shift(2)
            * falling * falling.shift(1) * falling.shift(2))
    cond = cond.where(~body.isna() & ~body.shift(2).isna())
    out = cond.rolling(40, min_periods=40).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group P: misc multi-bar features -----------------------


def f10cs_f10_candle_sequence_patterns_acmrange_20d_base_v133_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """20-bar sum of (range - prev range): cumulative range expansion."""
    rng = high - low
    d = rng - rng.shift(1)
    out = d.rolling(20, min_periods=20).sum() / rng.rolling(20, min_periods=20).mean().replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_clseyema_15d_base_v134_signal(close: pd.Series, open: pd.Series) -> pd.Series:
    """15-bar count of close > open AND close > close[-1] (consensus
    bullish). Multi-bar."""
    cond = ((close > open) & (close > close.shift(1))).astype(float)
    cond = cond.where(~close.isna() & ~open.isna() & ~close.shift(1).isna())
    out = cond.rolling(15, min_periods=15).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_clshema_15d_base_v135_signal(close: pd.Series, open: pd.Series) -> pd.Series:
    """15-bar count of close < open AND close < close[-1]."""
    cond = ((close < open) & (close < close.shift(1))).astype(float)
    cond = cond.where(~close.isna() & ~open.isna() & ~close.shift(1).isna())
    out = cond.rolling(15, min_periods=15).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_inssbur_10d_base_v136_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """10-bar count of inside bars followed by close > prev high
    (inside-bar breakouts)."""
    inside = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    brk = (close > high.shift(1)).astype(float)
    cond = (inside.shift(1) * brk).where(~inside.isna() & ~brk.isna())
    out = cond.rolling(10, min_periods=10).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_outscont_10d_base_v137_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """10-bar count of outside-bar continuation in the same direction
    (close > prev close after outside)."""
    outside = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
    cont = (close > close.shift(1)).astype(float)
    cond = (outside.shift(1) * cont).where(~outside.isna() & ~cont.isna())
    out = cond.rolling(10, min_periods=10).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_innbody_3d_base_v138_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """3-bar inner-body proportion: middle bar body / (range of 3-bar
    body envelope)."""
    cur_hi = pd.concat([open, close], axis=1).max(axis=1)
    cur_lo = pd.concat([open, close], axis=1).min(axis=1)
    env_hi = cur_hi.rolling(3, min_periods=3).max()
    env_lo = cur_lo.rolling(3, min_periods=3).min()
    env_r = (env_hi - env_lo).replace(0.0, np.nan)
    inner = (cur_hi.shift(1) - cur_lo.shift(1)) / env_r
    out = inner
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_clsmag_5d_base_v139_signal(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-bar mean of (close - open)^2 / variance(close-open, 30). A
    'quadratic body intensity'."""
    body = close - open
    var30 = (body * body).rolling(30, min_periods=30).mean().replace(0.0, np.nan)
    s = (body * body) / var30
    out = s.rolling(5, min_periods=5).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_volpeak_15d_base_v140_signal(volume: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """15-bar count of volume peaks (>1.5x 5-bar mean) co-occurring with
    a bull bar."""
    bull = (close > open).astype(float)
    vm = volume.rolling(5, min_periods=5).mean().replace(0.0, np.nan)
    peak = (volume > 1.5 * vm).astype(float)
    cond = (peak * bull).where(~bull.isna() & ~peak.isna())
    out = cond.rolling(15, min_periods=15).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_voltrough_15d_base_v141_signal(volume: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """15-bar count of volume troughs with bear bars."""
    bear = (close < open).astype(float)
    vm = volume.rolling(5, min_periods=5).mean().replace(0.0, np.nan)
    trough = (volume < 0.67 * vm).astype(float)
    cond = (trough * bear).where(~bear.isna() & ~trough.isna())
    out = cond.rolling(15, min_periods=15).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_gapfilcnt_20d_base_v142_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """20-bar count of gap-fills: |open - prev close| > 0.005*close and
    close on opposite side of prev close. Multi-bar."""
    gap = open - close.shift(1)
    fill = (np.sign(gap) != np.sign(close - close.shift(1))) & (gap.abs() > 0.005 * close)
    fill = fill.astype(float).where(~gap.isna())
    out = fill.rolling(20, min_periods=20).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_gapfollow_20d_base_v143_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """20-bar count of gap-follow-through: |gap| > 0.5*|body[-1]| AND same
    direction body."""
    gap = open - close.shift(1)
    prev_body = (close.shift(1) - open.shift(1))
    cond = ((gap.abs() > 0.5 * prev_body.abs()) &
            (np.sign(gap) == np.sign(prev_body))).astype(float)
    cond = cond.where(~gap.isna() & ~prev_body.isna())
    out = cond.rolling(20, min_periods=20).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_consec_25d_base_v144_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """25-bar lagged-1 partial autocorrelation of body sign times
    body abs."""
    body = (close - open).where(~close.isna() & ~open.isna())
    def _ac(x):
        if np.isnan(x).any() or len(x) < 5:
            return np.nan
        a = x[:-1]; b = x[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    out = body.rolling(25, min_periods=25).apply(_ac, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_pinrng_30d_base_v145_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar count of pin-bar shapes (max shadow > 2*body) following a
    prior bar move."""
    body = (close - open).abs()
    upper = high - pd.concat([open, close], axis=1).max(axis=1)
    lower = pd.concat([open, close], axis=1).min(axis=1) - low
    max_sh = pd.concat([upper, lower], axis=1).max(axis=1)
    cond = (max_sh > 2.0 * body).astype(float)
    prior_move = (close.shift(1) - close.shift(3)).abs() > 0.01 * close.shift(3)
    cond = cond.where(~body.isna()).astype(float) * prior_move.astype(float)
    out = cond.rolling(30, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_emadev_3d_base_v146_signal(close: pd.Series, open: pd.Series) -> pd.Series:
    """3-bar mean body sign vs body sign of 6-bar EMA-smoothed body. Multi-
    bar trend vs momentum diff."""
    body = close - open
    ema = body.ewm(span=6, adjust=False, min_periods=6).mean()
    s_short = np.sign(body.rolling(3, min_periods=3).mean())
    s_ema = np.sign(ema)
    out = (s_short - s_ema)
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_hlbal_15d_base_v147_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """15-bar mean of (high - high[-1]) / (low[-1] - low). Captures whether
    bars push more on highs or lows."""
    a = high - high.shift(1)
    b = (low.shift(1) - low).replace(0.0, np.nan)
    s = a / b
    out = s.rolling(15, min_periods=15).apply(
        lambda x: float(np.nanmedian(x[np.isfinite(x)])) if np.isfinite(x).any() else np.nan,
        raw=True,
    )
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_clseopn_8d_base_v148_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """8-bar count of close[t] > open[t+1] inverted: close[t-1] > open[t]
    (gap-down open). Multi-bar."""
    cond = (close.shift(1) > open).astype(float).where(~close.shift(1).isna() & ~open.isna())
    out = cond.rolling(8, min_periods=8).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_clblopn_8d_base_v149_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """8-bar mean of (open - close[-1]) / range[-1]. Continuous gap-from-
    prior-close measure with range normalization."""
    gap = open - close.shift(1)
    prv_rng = (high.shift(1) - low.shift(1)).replace(0.0, np.nan)
    s = gap / prv_rng
    out = s.rolling(8, min_periods=8).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f10cs_f10_candle_sequence_patterns_evenodd_20d_base_v150_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """20-bar mean: bull on odd-day, bear on even-day pattern test (count
    alternation). Tests for alternating-bar behavior."""
    sgn = np.sign(close - open).where(~close.isna() & ~open.isna())
    target = (-1.0) ** pd.Series(np.arange(len(sgn)), index=sgn.index)
    score = (sgn * target).where(~sgn.isna())
    out = score.rolling(20, min_periods=20).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f10_candle_sequence_patterns_base_076_150_REGISTRY = {
    "f10cs_f10_candle_sequence_patterns_bsidvr_2d_base_v076_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_bsidvr_2d_base_v076_signal},
    "f10cs_f10_candle_sequence_patterns_concl3_3d_base_v077_signal": {"inputs": ["close"], "func": f10cs_f10_candle_sequence_patterns_concl3_3d_base_v077_signal},
    "f10cs_f10_candle_sequence_patterns_gap2bdy_2d_base_v078_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_gap2bdy_2d_base_v078_signal},
    "f10cs_f10_candle_sequence_patterns_2bartrk_2d_base_v079_signal": {"inputs": ["close"], "func": f10cs_f10_candle_sequence_patterns_2bartrk_2d_base_v079_signal},
    "f10cs_f10_candle_sequence_patterns_bothshad_3d_base_v080_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_bothshad_3d_base_v080_signal},
    "f10cs_f10_candle_sequence_patterns_riseclos_5d_base_v081_signal": {"inputs": ["close"], "func": f10cs_f10_candle_sequence_patterns_riseclos_5d_base_v081_signal},
    "f10cs_f10_candle_sequence_patterns_clsclose_2d_base_v082_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_clsclose_2d_base_v082_signal},
    "f10cs_f10_candle_sequence_patterns_thirteenseq_13d_base_v083_signal": {"inputs": ["close"], "func": f10cs_f10_candle_sequence_patterns_thirteenseq_13d_base_v083_signal},
    "f10cs_f10_candle_sequence_patterns_dnsetup_9d_base_v084_signal": {"inputs": ["close"], "func": f10cs_f10_candle_sequence_patterns_dnsetup_9d_base_v084_signal},
    "f10cs_f10_candle_sequence_patterns_islndrev_3d_base_v085_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_islndrev_3d_base_v085_signal},
    "f10cs_f10_candle_sequence_patterns_winflwthru_3d_base_v086_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_winflwthru_3d_base_v086_signal},
    "f10cs_f10_candle_sequence_patterns_losflwthru_3d_base_v087_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_losflwthru_3d_base_v087_signal},
    "f10cs_f10_candle_sequence_patterns_engcnt_40d_base_v088_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_engcnt_40d_base_v088_signal},
    "f10cs_f10_candle_sequence_patterns_haramicnt_30d_base_v089_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_haramicnt_30d_base_v089_signal},
    "f10cs_f10_candle_sequence_patterns_dojicnt_25d_base_v090_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_dojicnt_25d_base_v090_signal},
    "f10cs_f10_candle_sequence_patterns_revcnt_20d_base_v091_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_revcnt_20d_base_v091_signal},
    "f10cs_f10_candle_sequence_patterns_btopcnt_30d_base_v092_signal": {"inputs": ["high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_btopcnt_30d_base_v092_signal},
    "f10cs_f10_candle_sequence_patterns_bbotcnt_30d_base_v093_signal": {"inputs": ["high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_bbotcnt_30d_base_v093_signal},
    "f10cs_f10_candle_sequence_patterns_distinsd_10d_base_v094_signal": {"inputs": ["high", "low"], "func": f10cs_f10_candle_sequence_patterns_distinsd_10d_base_v094_signal},
    "f10cs_f10_candle_sequence_patterns_distoutsd_10d_base_v095_signal": {"inputs": ["high", "low"], "func": f10cs_f10_candle_sequence_patterns_distoutsd_10d_base_v095_signal},
    "f10cs_f10_candle_sequence_patterns_disteng_2d_base_v096_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_disteng_2d_base_v096_signal},
    "f10cs_f10_candle_sequence_patterns_disthar_2d_base_v097_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_disthar_2d_base_v097_signal},
    "f10cs_f10_candle_sequence_patterns_engdiff_20d_base_v098_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_engdiff_20d_base_v098_signal},
    "f10cs_f10_candle_sequence_patterns_insoutd_30d_base_v099_signal": {"inputs": ["high", "low"], "func": f10cs_f10_candle_sequence_patterns_insoutd_30d_base_v099_signal},
    "f10cs_f10_candle_sequence_patterns_hhstk_2d_base_v100_signal": {"inputs": ["high"], "func": f10cs_f10_candle_sequence_patterns_hhstk_2d_base_v100_signal},
    "f10cs_f10_candle_sequence_patterns_llstk_2d_base_v101_signal": {"inputs": ["low"], "func": f10cs_f10_candle_sequence_patterns_llstk_2d_base_v101_signal},
    "f10cs_f10_candle_sequence_patterns_engsmean_20d_base_v104_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_engsmean_20d_base_v104_signal},
    "f10cs_f10_candle_sequence_patterns_harasm_30d_base_v105_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_harasm_30d_base_v105_signal},
    "f10cs_f10_candle_sequence_patterns_tweezm_20d_base_v106_signal": {"inputs": ["high", "low"], "func": f10cs_f10_candle_sequence_patterns_tweezm_20d_base_v106_signal},
    "f10cs_f10_candle_sequence_patterns_highbrk_10d_base_v107_signal": {"inputs": ["high", "close"], "func": f10cs_f10_candle_sequence_patterns_highbrk_10d_base_v107_signal},
    "f10cs_f10_candle_sequence_patterns_lowbrk_10d_base_v108_signal": {"inputs": ["low", "close"], "func": f10cs_f10_candle_sequence_patterns_lowbrk_10d_base_v108_signal},
    "f10cs_f10_candle_sequence_patterns_failbrk_15d_base_v109_signal": {"inputs": ["high", "close"], "func": f10cs_f10_candle_sequence_patterns_failbrk_15d_base_v109_signal},
    "f10cs_f10_candle_sequence_patterns_colcons_15d_base_v110_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_colcons_15d_base_v110_signal},
    "f10cs_f10_candle_sequence_patterns_oprng_10d_base_v111_signal": {"inputs": ["open", "high", "low"], "func": f10cs_f10_candle_sequence_patterns_oprng_10d_base_v111_signal},
    "f10cs_f10_candle_sequence_patterns_clrng_15d_base_v112_signal": {"inputs": ["high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_clrng_15d_base_v112_signal},
    "f10cs_f10_candle_sequence_patterns_volup_20d_base_v113_signal": {"inputs": ["open", "close", "volume"], "func": f10cs_f10_candle_sequence_patterns_volup_20d_base_v113_signal},
    "f10cs_f10_candle_sequence_patterns_voldn_20d_base_v114_signal": {"inputs": ["open", "close", "volume"], "func": f10cs_f10_candle_sequence_patterns_voldn_20d_base_v114_signal},
    "f10cs_f10_candle_sequence_patterns_volclmx_30d_base_v115_signal": {"inputs": ["open", "close", "volume"], "func": f10cs_f10_candle_sequence_patterns_volclmx_30d_base_v115_signal},
    "f10cs_f10_candle_sequence_patterns_clseac1_25d_base_v116_signal": {"inputs": ["close"], "func": f10cs_f10_candle_sequence_patterns_clseac1_25d_base_v116_signal},
    "f10cs_f10_candle_sequence_patterns_rngac1_30d_base_v117_signal": {"inputs": ["high", "low"], "func": f10cs_f10_candle_sequence_patterns_rngac1_30d_base_v117_signal},
    "f10cs_f10_candle_sequence_patterns_bodyrs_30d_base_v118_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_bodyrs_30d_base_v118_signal},
    "f10cs_f10_candle_sequence_patterns_seqent_30d_base_v119_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_seqent_30d_base_v119_signal},
    "f10cs_f10_candle_sequence_patterns_runlen_50d_base_v120_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_runlen_50d_base_v120_signal},
    "f10cs_f10_candle_sequence_patterns_engrank_50d_base_v121_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_engrank_50d_base_v121_signal},
    "f10cs_f10_candle_sequence_patterns_brngrnk_30d_base_v122_signal": {"inputs": ["high", "low"], "func": f10cs_f10_candle_sequence_patterns_brngrnk_30d_base_v122_signal},
    "f10cs_f10_candle_sequence_patterns_seqdir_60d_base_v123_signal": {"inputs": ["closeadj"], "func": f10cs_f10_candle_sequence_patterns_seqdir_60d_base_v123_signal},
    "f10cs_f10_candle_sequence_patterns_seqac1_80d_base_v124_signal": {"inputs": ["closeadj"], "func": f10cs_f10_candle_sequence_patterns_seqac1_80d_base_v124_signal},
    "f10cs_f10_candle_sequence_patterns_drmonotn_40d_base_v125_signal": {"inputs": ["closeadj"], "func": f10cs_f10_candle_sequence_patterns_drmonotn_40d_base_v125_signal},
    "f10cs_f10_candle_sequence_patterns_bodyvar_25d_base_v126_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_bodyvar_25d_base_v126_signal},
    "f10cs_f10_candle_sequence_patterns_seqvar_30d_base_v127_signal": {"inputs": ["high", "low"], "func": f10cs_f10_candle_sequence_patterns_seqvar_30d_base_v127_signal},
    "f10cs_f10_candle_sequence_patterns_clmad_20d_base_v128_signal": {"inputs": ["close"], "func": f10cs_f10_candle_sequence_patterns_clmad_20d_base_v128_signal},
    "f10cs_f10_candle_sequence_patterns_morncnt_50d_base_v129_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_morncnt_50d_base_v129_signal},
    "f10cs_f10_candle_sequence_patterns_evencnt_50d_base_v130_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_evencnt_50d_base_v130_signal},
    "f10cs_f10_candle_sequence_patterns_3soldcnt_40d_base_v131_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_3soldcnt_40d_base_v131_signal},
    "f10cs_f10_candle_sequence_patterns_3crowcnt_40d_base_v132_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_3crowcnt_40d_base_v132_signal},
    "f10cs_f10_candle_sequence_patterns_acmrange_20d_base_v133_signal": {"inputs": ["high", "low"], "func": f10cs_f10_candle_sequence_patterns_acmrange_20d_base_v133_signal},
    "f10cs_f10_candle_sequence_patterns_clseyema_15d_base_v134_signal": {"inputs": ["close", "open"], "func": f10cs_f10_candle_sequence_patterns_clseyema_15d_base_v134_signal},
    "f10cs_f10_candle_sequence_patterns_clshema_15d_base_v135_signal": {"inputs": ["close", "open"], "func": f10cs_f10_candle_sequence_patterns_clshema_15d_base_v135_signal},
    "f10cs_f10_candle_sequence_patterns_inssbur_10d_base_v136_signal": {"inputs": ["high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_inssbur_10d_base_v136_signal},
    "f10cs_f10_candle_sequence_patterns_outscont_10d_base_v137_signal": {"inputs": ["high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_outscont_10d_base_v137_signal},
    "f10cs_f10_candle_sequence_patterns_innbody_3d_base_v138_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_innbody_3d_base_v138_signal},
    "f10cs_f10_candle_sequence_patterns_clsmag_5d_base_v139_signal": {"inputs": ["close", "open"], "func": f10cs_f10_candle_sequence_patterns_clsmag_5d_base_v139_signal},
    "f10cs_f10_candle_sequence_patterns_volpeak_15d_base_v140_signal": {"inputs": ["volume", "close", "open"], "func": f10cs_f10_candle_sequence_patterns_volpeak_15d_base_v140_signal},
    "f10cs_f10_candle_sequence_patterns_voltrough_15d_base_v141_signal": {"inputs": ["volume", "close", "open"], "func": f10cs_f10_candle_sequence_patterns_voltrough_15d_base_v141_signal},
    "f10cs_f10_candle_sequence_patterns_gapfilcnt_20d_base_v142_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_gapfilcnt_20d_base_v142_signal},
    "f10cs_f10_candle_sequence_patterns_gapfollow_20d_base_v143_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_gapfollow_20d_base_v143_signal},
    "f10cs_f10_candle_sequence_patterns_consec_25d_base_v144_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_consec_25d_base_v144_signal},
    "f10cs_f10_candle_sequence_patterns_pinrng_30d_base_v145_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_pinrng_30d_base_v145_signal},
    "f10cs_f10_candle_sequence_patterns_emadev_3d_base_v146_signal": {"inputs": ["close", "open"], "func": f10cs_f10_candle_sequence_patterns_emadev_3d_base_v146_signal},
    "f10cs_f10_candle_sequence_patterns_hlbal_15d_base_v147_signal": {"inputs": ["high", "low"], "func": f10cs_f10_candle_sequence_patterns_hlbal_15d_base_v147_signal},
    "f10cs_f10_candle_sequence_patterns_clseopn_8d_base_v148_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_clseopn_8d_base_v148_signal},
    "f10cs_f10_candle_sequence_patterns_clblopn_8d_base_v149_signal": {"inputs": ["open", "high", "low", "close"], "func": f10cs_f10_candle_sequence_patterns_clblopn_8d_base_v149_signal},
    "f10cs_f10_candle_sequence_patterns_evenodd_20d_base_v150_signal": {"inputs": ["open", "close"], "func": f10cs_f10_candle_sequence_patterns_evenodd_20d_base_v150_signal},
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
    for name, entry in f10_candle_sequence_patterns_base_076_150_REGISTRY.items():
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
    print(f"OK base_076_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
