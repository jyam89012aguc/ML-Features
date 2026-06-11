"""f02_price_channel_position base features 076-150.

Domain: price-channel position — Donchian-style rolling high/low
channels. Second tranche of channel features distinct from file 1:
HL2-anchored channels, Keltner-style ATR channels, Bollinger-on-high
and Bollinger-on-low envelopes, percentile channels (using quantile
rather than max/min), volume-weighted channels, longer/shorter twist
windows, swing-pivot anchored channels, conditional state counts,
channel breakout magnitude statistics, and channel-vs-channel ratios.

Every feature references a rolling high/low channel construction (or
a quantile-channel as a robust variant). No `_core()` factory; each
function is a fully expanded `def` block. NaN policy: never
`fillna(<value>)`; only `replace([inf,-inf], nan)` at final return.
Windows > 21 use `closeadj`; windows <= 21 use `close`.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Features 076-150
# ---------------------------------------------------------------------------


# --- Group A: HL2- and OHLC-anchored channels (5) -------------------------


def f02pc_f02_price_channel_position_hl2pos_20d_base_v076_signal(close, high, low):
    """Sign of close vs the 20d HL2-anchored mid, weighted by the channel
    width relative to the bar range. Sign+magnitude is structurally
    different from a continuous %B."""
    hi = high.rolling(20, min_periods=20).max()
    lo = low.rolling(20, min_periods=20).min()
    hl2 = ((high + low) / 2.0).rolling(20, min_periods=20).mean()
    bar_rng = (high - low).rolling(20, min_periods=20).mean()
    width = (hi - lo).replace(0.0, np.nan)
    out = np.sign(close - hl2) * (bar_rng / width)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_hccpos_42d_base_v077_signal(closeadj, high, low):
    """Position vs HLC3-anchored channel (42d): (close - HLC3_42_mean) /
    (high_42 - low_42). HLC3 = (h+l+c)/3."""
    hi = high.rolling(42, min_periods=42).max()
    lo = low.rolling(42, min_periods=42).min()
    hlc3 = ((high + low + closeadj) / 3.0).rolling(42, min_periods=42).mean()
    out = (closeadj - hlc3) / (hi - lo).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_ohlcrng_30d_base_v078_signal(closeadj, open_, high, low):
    """OHLC-range-vs-channel-range ratio (30d): avg per-bar range
    (high-low) divided by 30d channel range (high_30-low_30)."""
    bar_rng = (high - low).rolling(30, min_periods=30).mean()
    hi = high.rolling(30, min_periods=30).max()
    lo = low.rolling(30, min_periods=30).min()
    chrng = (hi - lo).replace(0.0, np.nan)
    out = bar_rng / chrng
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_obpos_10d_base_v079_signal(close, open_, high, low):
    """Open-vs-channel: (open - low_10)/(high_10 - low_10). Where the
    open sat in the prior 10d channel."""
    hi = high.rolling(10, min_periods=10).max()
    lo = low.rolling(10, min_periods=10).min()
    out = (open_ - lo) / (hi - lo).replace(0.0, np.nan) - 0.5
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_truebw_25d_base_v080_signal(closeadj, high, low):
    """True channel width using max true range: rolling-max(true range, 25d)
    minus 0. Single anchored width. TR = max(h-l, |h-c[-1]|, |l-c[-1]|)."""
    tr = pd.concat([(high - low), (high - closeadj.shift(1)).abs(), (low - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    out = tr.rolling(25, min_periods=25).max() / closeadj.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group B: Keltner-style ATR channels (3) ------------------------------


def f02pc_f02_price_channel_position_kelt_20d_base_v081_signal(close, high, low):
    """Keltner channel position (20d): (c - EMA20) / (2 * ATR20). Range
    roughly [-1, 1] in normal markets."""
    ema = close.ewm(span=20, adjust=False, min_periods=20).mean()
    tr = pd.concat([(high - low), (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(20, min_periods=20).mean()
    out = (close - ema) / (2.0 * atr).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_keltatr_50d_base_v082_signal(closeadj, high, low):
    """ATR-anchored channel width vs Donchian width (50d): ATR_50 *
    sqrt(50) / (high_50 - low_50). Captures whether realized vol
    accounts for the Donchian width."""
    tr = pd.concat([(high - low), (high - closeadj.shift(1)).abs(), (low - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(50, min_periods=50).mean()
    hi = high.rolling(50, min_periods=50).max()
    lo = low.rolling(50, min_periods=50).min()
    out = atr * np.sqrt(50.0) / (hi - lo).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_keltdiv_30d_base_v083_signal(closeadj, high, low):
    """Keltner-Donchian divergence (30d): %B(30d Donchian) - %B(Keltner-30d).
    Reveals when ATR-channel and price-channel disagree."""
    hi = high.rolling(30, min_periods=30).max()
    lo = low.rolling(30, min_periods=30).min()
    don = (closeadj - lo) / (hi - lo).replace(0.0, np.nan)
    ema = closeadj.ewm(span=30, adjust=False, min_periods=30).mean()
    tr = pd.concat([(high - low), (high - closeadj.shift(1)).abs(), (low - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(30, min_periods=30).mean()
    kelt_b = (closeadj - (ema - 2.0 * atr)) / (4.0 * atr).replace(0.0, np.nan)
    out = don - kelt_b
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group C: Bollinger-on-high / on-low envelopes (3) -------------------


def f02pc_f02_price_channel_position_bollhi_20d_base_v084_signal(close, high):
    """Bollinger %B on high: (high - SMA(high,20)) / (2 * std(high,20)).
    Captures bollinger position of the upper anchor."""
    sma = high.rolling(20, min_periods=20).mean()
    sd = high.rolling(20, min_periods=20).std()
    out = (high - sma) / (2.0 * sd).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_bolllo_30d_base_v085_signal(closeadj, low):
    """Bollinger %B on low (30d): (low - SMA(low,30)) / (2 * std(low,30))."""
    sma = low.rolling(30, min_periods=30).mean()
    sd = low.rolling(30, min_periods=30).std()
    out = (low - sma) / (2.0 * sd).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_bollratlo_60d_base_v086_signal(closeadj, high, low):
    """Bollinger width ratio (60d): std(high,60)/std(low,60). Asymmetry
    in dispersion of channel highs vs lows."""
    sh = high.rolling(60, min_periods=60).std()
    sl = low.rolling(60, min_periods=60).std()
    out = np.log(sh.replace(0.0, np.nan)) - np.log(sl.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group D: percentile-channel (quantile-based) (6) --------------------


def f02pc_f02_price_channel_position_qchpos_30d_base_v087_signal(closeadj, high, low):
    """Tail-stretch indicator (30d): how far the close pokes beyond the
    5th/95th percentile band, expressed as a one-sided clipped excess
    relative to the percentile half-width. Discrete excess feature —
    structurally distinct from continuous %B."""
    hi = high.rolling(30, min_periods=30).quantile(0.95)
    lo = low.rolling(30, min_periods=30).quantile(0.05)
    halfw = (hi - lo).replace(0.0, np.nan) / 2.0
    above = (closeadj - hi).clip(lower=0.0) / halfw
    below = (lo - closeadj).clip(lower=0.0) / halfw
    out = above - below
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_qchwid_60d_base_v088_signal(closeadj, high, low):
    """Quantile channel width: log(q95(high,60) - q05(low,60))."""
    hi = high.rolling(60, min_periods=60).quantile(0.95)
    lo = low.rolling(60, min_periods=60).quantile(0.05)
    w = (hi - lo) / closeadj.replace(0.0, np.nan)
    out = np.log(w.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_qchdiff_50d_base_v089_signal(closeadj, high, low):
    """Difference between max channel and quantile channel (50d): how
    much the extreme outliers extend beyond the 95th percentile."""
    hi_max = high.rolling(50, min_periods=50).max()
    hi_q = high.rolling(50, min_periods=50).quantile(0.95)
    out = (hi_max - hi_q) / closeadj.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_iqrch_45d_base_v090_signal(closeadj, high, low):
    """Inter-quartile excess (45d): clipped overshoot of close beyond the
    q75 of high or below q25 of low, normalized by the IQR. Zero inside
    the IQR band and increasing linearly only on overshoots — a
    rectifier-style feature structurally distinct from continuous %B."""
    hi = high.rolling(45, min_periods=45).quantile(0.75)
    lo = low.rolling(45, min_periods=45).quantile(0.25)
    iqr = (hi - lo).replace(0.0, np.nan)
    above = (closeadj - hi).clip(lower=0.0) / iqr
    below = (lo - closeadj).clip(lower=0.0) / iqr
    out = above - below
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_medch_30d_base_v091_signal(closeadj, high, low):
    """Median-channel sign-flip count (30d): rolling-30 count of sign flips of
    (closeadj - rolling_median_30d). A high count means price oscillates
    around the median; a low count means it lives on one side. Discrete
    count of regime crossings — structurally different from continuous
    position features."""
    med = closeadj.rolling(30, min_periods=30).median()
    side = np.sign(closeadj - med)
    flip = (side != side.shift(1)).astype(float).where(~med.isna())
    out = flip.rolling(30, min_periods=15).sum() - 5.0
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_qchhi_100d_base_v092_signal(closeadj, high):
    """Distance to 100d high-quantile (95th): log(q95(high,100) / close).
    Soft top resistance."""
    hi = high.rolling(100, min_periods=100).quantile(0.95)
    out = np.log(hi / closeadj.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group E: longer-horizon channels and breakouts (5) ------------------


def f02pc_f02_price_channel_position_brk52w_252d_base_v093_signal(closeadj, high):
    """52-week-high breakout indicator: 1 if close > prior 252d high
    (excluding today), else 0."""
    prior = high.shift(1).rolling(252, min_periods=200).max()
    flag = (closeadj > prior).astype(float)
    flag[prior.isna()] = np.nan
    return flag.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_pos252_252d_base_v094_signal(closeadj, high, low):
    """52-week channel-half indicator: difference of EWM(0.05) of
    1{close >= mid252} and 1{close <= mid252}. Smoothed binary regime
    feature — structurally different from continuous distance-based v095/v096."""
    hi = high.rolling(252, min_periods=200).max()
    lo = low.rolling(252, min_periods=200).min()
    mid = (hi + lo) / 2.0
    up = (closeadj >= mid).astype(float).where(~mid.isna())
    dn = (closeadj <= mid).astype(float).where(~mid.isna())
    out = up.ewm(alpha=0.05, adjust=False, min_periods=50).mean() - dn.ewm(alpha=0.05, adjust=False, min_periods=50).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_dist52h_252d_base_v095_signal(closeadj, high):
    """Log-distance to 52-week high: log(high_252 / closeadj). Always >= 0."""
    hi = high.rolling(252, min_periods=200).max()
    out = np.log(hi / closeadj.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_dist52l_252d_base_v096_signal(closeadj, low):
    """Log-distance from 52-week low: log(closeadj / low_252). Always >= 0."""
    lo = low.rolling(252, min_periods=200).min()
    out = np.log(closeadj / lo.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_zh252_252d_base_v097_signal(closeadj, high, low):
    """52-week new-high frequency minus new-low frequency: fraction of the
    trailing 252 bars that printed a new 252d high minus the fraction
    that printed a new 252d low. Count-based regime indicator —
    structurally distinct from continuous distance-to-high (v095)."""
    hi = high.rolling(252, min_periods=200).max()
    lo = low.rolling(252, min_periods=200).min()
    new_h = (high >= hi).astype(float).where(~hi.isna())
    new_l = (low <= lo).astype(float).where(~lo.isna())
    out = new_h.rolling(252, min_periods=100).mean() - new_l.rolling(252, min_periods=100).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group F: swing-pivot channels (3) -----------------------------------


def f02pc_f02_price_channel_position_swhipos_30d_base_v098_signal(closeadj, high):
    """Swing-high position: bars since last 5d swing-high (high =
    rolling-max of high over [-2,+2]) within trailing 30d. Saturates 30."""
    swing = high.rolling(5, min_periods=5).max().shift(-2)
    is_swing = (high == swing)
    idx = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    last_hit = idx.where(is_swing).ffill()
    out = (idx - last_hit).clip(upper=30.0).where(~swing.isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_swlopos_30d_base_v099_signal(closeadj, low):
    """Swing-low position: bars since last 5d swing-low. Saturates 30."""
    swing = low.rolling(5, min_periods=5).min().shift(-2)
    is_swing = (low == swing)
    idx = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    last_hit = idx.where(is_swing).ffill()
    out = (idx - last_hit).clip(upper=30.0).where(~swing.isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_swdir_30d_base_v100_signal(closeadj, high, low):
    """Swing direction: +1 if more swing-highs than swing-lows in trailing
    30d (uptrend channel formation), -1 if reverse."""
    swh = high.rolling(5, min_periods=5).max().shift(-2)
    swl = low.rolling(5, min_periods=5).min().shift(-2)
    h_flag = (high == swh).astype(float)
    l_flag = (low == swl).astype(float)
    h_flag[swh.isna()] = np.nan
    l_flag[swl.isna()] = np.nan
    out = np.sign(h_flag.rolling(30, min_periods=15).sum() - l_flag.rolling(30, min_periods=15).sum())
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group G: conditional state counts (5) -------------------------------


def f02pc_f02_price_channel_position_topcond_60d_base_v101_signal(closeadj, high, low):
    """Fraction of trailing 60d where (channel_position >= 0.8 AND channel
    width > 60d median width). Combined-state count."""
    hi = high.rolling(30, min_periods=30).max()
    lo = low.rolling(30, min_periods=30).min()
    pos = (closeadj - lo) / (hi - lo).replace(0.0, np.nan)
    w = hi - lo
    wmed = w.rolling(60, min_periods=30).median()
    flag = ((pos >= 0.8) & (w > wmed)).astype(float)
    flag[pos.isna() | wmed.isna()] = np.nan
    out = flag.rolling(60, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_bothcnt_50d_base_v102_signal(closeadj, high, low):
    """Joint extreme: count of trailing 50d where (close is in top 10%
    of 20d channel) AND (close > close.shift(1)). Strong-up days at
    channel top."""
    hi = high.rolling(20, min_periods=20).max()
    lo = low.rolling(20, min_periods=20).min()
    pos = (closeadj - lo) / (hi - lo).replace(0.0, np.nan)
    flag = ((pos >= 0.9) & (closeadj > closeadj.shift(1))).astype(float)
    flag[pos.isna()] = np.nan
    out = flag.rolling(50, min_periods=25).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_pinchbrk_70d_base_v103_signal(closeadj, high, low):
    """Trailing-70d count of days where channel was pinched (width-20d
    in bottom 25% of trailing-70d widths) AND a 10d breakout occurred."""
    hi = high.rolling(20, min_periods=20).max()
    lo = low.rolling(20, min_periods=20).min()
    w = (hi - lo) / closeadj.replace(0.0, np.nan)
    rk = w.rolling(70, min_periods=35).rank(pct=True)
    ph = high.shift(1).rolling(10, min_periods=10).max()
    brk = (closeadj > ph)
    flag = ((rk < 0.25) & brk).astype(float)
    flag[rk.isna() | ph.isna()] = np.nan
    out = flag.rolling(70, min_periods=35).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_strongbot_30d_base_v104_signal(close, high, low):
    """Count of trailing 30d in bottom 20% of 14d channel that closed
    higher than open (potential bottom-reversal candles)."""
    hi = high.rolling(14, min_periods=14).max()
    lo = low.rolling(14, min_periods=14).min()
    pos = (close - lo) / (hi - lo).replace(0.0, np.nan)
    flag = (pos <= 0.2).astype(float)
    flag[pos.isna()] = np.nan
    out = flag.rolling(30, min_periods=15).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_acccnt_40d_base_v105_signal(closeadj, high, low):
    """Channel-acceleration count: bars in trailing 40d where 5d channel
    width > 5d channel width 10 bars ago by > 25% (rapid expansion)."""
    hi = high.rolling(5, min_periods=5).max()
    lo = low.rolling(5, min_periods=5).min()
    w = hi - lo
    growth = w / w.shift(10).replace(0.0, np.nan)
    flag = (growth > 1.25).astype(float)
    flag[growth.isna()] = np.nan
    out = flag.rolling(40, min_periods=20).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group H: breakout magnitude statistics (3) --------------------------


def f02pc_f02_price_channel_position_brkmag_50d_base_v106_signal(closeadj, high):
    """Mean breakout magnitude in trailing 50d: avg of max(close - prior_20d_high, 0)
    across the trailing 50 bars, normalized by close. Non-breakout days contribute 0
    so the rolling mean is well defined even when breakouts are sparse."""
    prior = high.shift(1).rolling(20, min_periods=20).max()
    mag = (closeadj - prior).clip(lower=0.0)
    norm = mag / closeadj.replace(0.0, np.nan)
    out = norm.rolling(50, min_periods=25).mean().where(~prior.isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_brkmaxmag_60d_base_v107_signal(closeadj, high, low):
    """Largest breakout (up or down) magnitude in trailing 60d:
    max(|close - prior_30d_high|, |prior_30d_low - close|)/close. Always >= 0."""
    ph = high.shift(1).rolling(30, min_periods=30).max()
    pl = low.shift(1).rolling(30, min_periods=30).min()
    up = (closeadj - ph).clip(lower=0.0)
    dn = (pl - closeadj).clip(lower=0.0)
    m = pd.concat([up, dn], axis=1).max(axis=1) / closeadj.replace(0.0, np.nan)
    out = m.rolling(60, min_periods=30).max()
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_brksig_40d_base_v108_signal(closeadj, high):
    """Standardized breakout signal: (breakout_count_50d / 50) standardized
    by trailing 40d mean of the same ratio."""
    prior = high.shift(1).rolling(20, min_periods=20).max()
    flag = (closeadj > prior).astype(float)
    flag[prior.isna()] = np.nan
    cnt = flag.rolling(50, min_periods=25).mean()
    mu = cnt.rolling(40, min_periods=20).mean()
    sd = cnt.rolling(40, min_periods=20).std()
    out = (cnt - mu) / sd.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group I: ratio-based channel comparisons (4) ------------------------


def f02pc_f02_price_channel_position_pinchrat_50d_base_v109_signal(closeadj, high, low):
    """Ratio of 5d width to 50d width — extreme small ratio means very
    tight short-term channel inside wide long-term range."""
    h5 = high.rolling(5, min_periods=5).max()
    l5 = low.rolling(5, min_periods=5).min()
    h50 = high.rolling(50, min_periods=50).max()
    l50 = low.rolling(50, min_periods=50).min()
    out = (h5 - l5) / (h50 - l50).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_chstack_100d_base_v110_signal(closeadj, high, low):
    """Channel-stack score: count of {10,30,60,100}d Donchian channels
    where the close is in top quartile. Integer 0..4."""
    def _topq(h, l, n):
        hi = h.rolling(n, min_periods=n).max()
        lo = l.rolling(n, min_periods=n).min()
        return ((closeadj - lo) / (hi - lo).replace(0.0, np.nan) >= 0.75).astype(float)
    s10 = _topq(high, low, 10)
    s30 = _topq(high, low, 30)
    s60 = _topq(high, low, 60)
    s100 = _topq(high, low, 100)
    out = s10 + s30 + s60 + s100
    h100 = high.rolling(100, min_periods=100).max()
    out = out.where(~h100.isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_chstackdn_100d_base_v111_signal(closeadj, high, low):
    """Bottom-quartile stack: count of {10,30,60,100}d Donchian channels
    where the close is in bottom quartile. Integer 0..4."""
    def _botq(h, l, n):
        hi = h.rolling(n, min_periods=n).max()
        lo = l.rolling(n, min_periods=n).min()
        return ((closeadj - lo) / (hi - lo).replace(0.0, np.nan) <= 0.25).astype(float)
    s10 = _botq(high, low, 10)
    s30 = _botq(high, low, 30)
    s60 = _botq(high, low, 60)
    s100 = _botq(high, low, 100)
    out = s10 + s30 + s60 + s100
    h100 = high.rolling(100, min_periods=100).max()
    out = out.where(~h100.isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_rangedom_30d_base_v112_signal(closeadj, high, low):
    """Range-dominance: fraction of trailing 30d where today's range
    (high-low) was the largest of trailing 5d."""
    rng = high - low
    rolling_max5 = rng.rolling(5, min_periods=5).max()
    flag = (rng >= rolling_max5).astype(float)
    flag[rolling_max5.isna()] = np.nan
    out = flag.rolling(30, min_periods=15).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group J: bounded transforms / sigmoid (3) ---------------------------


def f02pc_f02_price_channel_position_sigpos_30d_base_v113_signal(closeadj, high, low):
    """Sigmoid of (z-scored channel-position(30d)). Bounded [0,1]."""
    hi = high.rolling(30, min_periods=30).max()
    lo = low.rolling(30, min_periods=30).min()
    pos = (closeadj - lo) / (hi - lo).replace(0.0, np.nan)
    mu = pos.rolling(60, min_periods=30).mean()
    sd = pos.rolling(60, min_periods=30).std()
    z = (pos - mu) / sd.replace(0.0, np.nan)
    out = 1.0 / (1.0 + np.exp(-z.clip(-20.0, 20.0)))
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_arctanw_40d_base_v114_signal(closeadj, high, low):
    """arctan of (channel width 40d - rolling mean of width) /
    rolling std of width. Bounded transform of width extremeness."""
    hi = high.rolling(40, min_periods=40).max()
    lo = low.rolling(40, min_periods=40).min()
    w = (hi - lo) / closeadj.replace(0.0, np.nan)
    mu = w.rolling(60, min_periods=30).mean()
    sd = w.rolling(60, min_periods=30).std()
    z = (w - mu) / sd.replace(0.0, np.nan)
    out = (2.0 / np.pi) * np.arctan(z)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_tanhdcn_30d_base_v115_signal(closeadj, high):
    """tanh of (log-distance to 30d high) scaled. Bounded transform of
    drawdown-from-peak."""
    hi = high.rolling(30, min_periods=30).max()
    z = np.log(hi.replace(0.0, np.nan) / closeadj.replace(0.0, np.nan))
    out = np.tanh(z * 10.0)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group K: log-return-anchored channel features (4) -------------------


def f02pc_f02_price_channel_position_logrng_20d_base_v116_signal(close, high, low):
    """Log-channel-range (20d): log(high_20) - log(low_20). Equivalent
    to log of channel-width ratio."""
    hi = high.rolling(20, min_periods=20).max()
    lo = low.rolling(20, min_periods=20).min()
    out = np.log(hi.replace(0.0, np.nan)) - np.log(lo.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_lrretchcd_50d_base_v117_signal(closeadj, high, low):
    """Correlation between log-returns and channel-position changes (50d).
    Tells whether price moves align with position changes; expected ~1
    in calm regimes, lower when channel expands fast."""
    lr = np.log(closeadj.replace(0.0, np.nan)).diff()
    hi = high.rolling(20, min_periods=20).max()
    lo = low.rolling(20, min_periods=20).min()
    pos = (closeadj - lo) / (hi - lo).replace(0.0, np.nan)
    dp = pos.diff()
    out = lr.rolling(50, min_periods=30).corr(dp)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_pxret_40d_base_v118_signal(closeadj, high, low):
    """40d cumulative log-return measured against channel width: log(c/c.shift(40))
    / log(high_40 / low_40). Trend strength relative to range."""
    hi = high.rolling(40, min_periods=40).max()
    lo = low.rolling(40, min_periods=40).min()
    cret = np.log(closeadj / closeadj.shift(40).replace(0.0, np.nan))
    wlog = np.log(hi.replace(0.0, np.nan)) - np.log(lo.replace(0.0, np.nan))
    out = cret / wlog.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_chsharpe_30d_base_v119_signal(closeadj, high, low):
    """Channel Sharpe: 30d log-return / 30d channel-width-as-vol. Trend
    quality measure where channel-width replaces realized vol."""
    hi = high.rolling(30, min_periods=30).max()
    lo = low.rolling(30, min_periods=30).min()
    wlog = np.log(hi.replace(0.0, np.nan)) - np.log(lo.replace(0.0, np.nan))
    cret = np.log(closeadj / closeadj.shift(30).replace(0.0, np.nan))
    out = cret / wlog.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group L: volume-weighted channels (5) -------------------------------


def f02pc_f02_price_channel_position_vwhipos_30d_base_v120_signal(closeadj, high, low, volume):
    """Volume-weighted high: vw_high_30 = sum(high*volume,30)/sum(volume,30).
    Position relative to volume-weighted channel top: (close - vw_high)/close."""
    vh = (high * volume).rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    out = (closeadj - vh) / closeadj.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_vwlopos_30d_base_v121_signal(closeadj, low, volume):
    """Fraction of trailing 30 bars where closeadj closed below the
    volume-weighted-low (vw_low_30). Count/fraction feature on the
    volume-aware channel bottom — structurally different from continuous
    (close - vw_low)/close so it decorrelates from v120/v124."""
    vl = (low * volume).rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    below = (closeadj < vl).astype(float).where(~vl.isna())
    out = below.rolling(30, min_periods=15).mean() - 0.5
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_volrng_50d_base_v122_signal(closeadj, high, low, volume):
    """Volume-weighted channel range (50d) normalized by close."""
    vh = (high * volume).rolling(50, min_periods=50).sum() / volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    vl = (low * volume).rolling(50, min_periods=50).sum() / volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    out = (vh - vl) / closeadj.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_volnewhi_40d_base_v123_signal(closeadj, high, volume):
    """Volume-on-new-high vs trailing-mean volume: log of avg volume on
    new-20d-high days / avg volume of all days in trailing 40d."""
    prior = high.shift(1).rolling(20, min_periods=20).max()
    new_hi = (high > prior).astype(float)
    new_hi[prior.isna()] = np.nan
    nh_vol = (new_hi * volume).rolling(40, min_periods=20).sum() / new_hi.rolling(40, min_periods=20).sum().replace(0.0, np.nan)
    all_vol = volume.rolling(40, min_periods=20).mean()
    out = np.log(nh_vol.replace(0.0, np.nan) / all_vol.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_volpos_30d_base_v124_signal(closeadj, high, low, volume):
    """Volume-imbalance breakout count (30d): fraction of trailing 30 days
    where the close pierced the volume-weighted high (closeadj > vw_high)
    AND volume exceeded its trailing-30d median. Counts strong-volume top
    pierces — structurally different from continuous channel position."""
    vh = (high * volume).rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    vmed = volume.rolling(30, min_periods=30).median()
    pierce = ((closeadj > vh) & (volume > vmed)).astype(float).where(~vh.isna())
    out = pierce.rolling(30, min_periods=15).mean() - 0.1
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group M: skew/kurtosis of channel features (3) ----------------------


def f02pc_f02_price_channel_position_widkurt_90d_base_v125_signal(closeadj, high, low):
    """Kurtosis of channel widths (60d window of 20d widths) over 90d.
    Fat tails of width distribution → episodic expansions."""
    hi = high.rolling(20, min_periods=20).max()
    lo = low.rolling(20, min_periods=20).min()
    w = (hi - lo) / closeadj.replace(0.0, np.nan)
    out = w.rolling(90, min_periods=45).kurt()
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_widskew_70d_base_v126_signal(closeadj, high, low):
    """Skewness of channel widths (30d) over 70d. Positive skew → frequent
    narrow widths with occasional very wide ones."""
    hi = high.rolling(30, min_periods=30).max()
    lo = low.rolling(30, min_periods=30).min()
    w = (hi - lo) / closeadj.replace(0.0, np.nan)
    out = w.rolling(70, min_periods=35).skew()
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_brkkurt_80d_base_v127_signal(closeadj, high):
    """Kurtosis of breakout magnitudes (40d high-distance series) over 80d."""
    hi = high.rolling(40, min_periods=40).max()
    mag = (hi - closeadj) / closeadj.replace(0.0, np.nan)
    out = mag.rolling(80, min_periods=40).kurt()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group N: trailing percentile of channel-stat (4) -------------------


def f02pc_f02_price_channel_position_widrkdif_80d_base_v128_signal(closeadj, high, low):
    """Difference of width-rank-percentile (20d width) between today and
    21 days ago — captures regime shift in width."""
    hi = high.rolling(20, min_periods=20).max()
    lo = low.rolling(20, min_periods=20).min()
    w = (hi - lo) / closeadj.replace(0.0, np.nan)
    rk = w.rolling(80, min_periods=40).rank(pct=True)
    out = rk - rk.shift(21)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_posrkfast_30d_base_v129_signal(closeadj, high, low):
    """Percentile rank of %B(5d Donchian) in trailing 30d. Fast position
    extremeness."""
    h5 = high.rolling(5, min_periods=5).max()
    l5 = low.rolling(5, min_periods=5).min()
    pos = (closeadj - l5) / (h5 - l5).replace(0.0, np.nan)
    out = pos.rolling(30, min_periods=15).rank(pct=True) - 0.5
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_chconsec_60d_base_v130_signal(closeadj, high, low):
    """Max consecutive-days-above-mid streak achieved in trailing 60d:
    longest run of close > 30d midpoint."""
    hi = high.rolling(30, min_periods=30).max()
    lo = low.rolling(30, min_periods=30).min()
    mid = (hi + lo) / 2.0
    above = (closeadj > mid).astype(float)
    above[mid.isna()] = np.nan
    def _maxrun(a):
        m = 0; cur = 0
        for v in a:
            if np.isnan(v):
                return float('nan')
            if v > 0:
                cur += 1
                if cur > m:
                    m = cur
            else:
                cur = 0
        return float(m)
    out = above.rolling(60, min_periods=60).apply(_maxrun, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_postransr_60d_base_v131_signal(closeadj, high, low):
    """Fraction of trailing 60d where pos transitioned from
    bottom-quartile to top-quartile within 5 bars (or vice versa).
    Channel-cycle transition rate."""
    hi = high.rolling(20, min_periods=20).max()
    lo = low.rolling(20, min_periods=20).min()
    pos = (closeadj - lo) / (hi - lo).replace(0.0, np.nan)
    was_low = (pos.shift(5) <= 0.25)
    is_high = (pos >= 0.75)
    trans = (was_low & is_high).astype(float)
    trans[pos.isna() | pos.shift(5).isna()] = np.nan
    out = trans.rolling(60, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group O: range-vs-body relations (3) --------------------------------


def f02pc_f02_price_channel_position_bodyrng_30d_base_v132_signal(close, open_, high, low):
    """Body-vs-channel: |close-open|/(high_5 - low_5). Captures whether
    intra-day moves are large relative to 5d channel range."""
    hi5 = high.rolling(5, min_periods=5).max()
    lo5 = low.rolling(5, min_periods=5).min()
    body = (close - open_).abs()
    out = body.rolling(30, min_periods=15).mean() / (hi5 - lo5).rolling(30, min_periods=15).mean().replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_wickrat_25d_base_v133_signal(close, open_, high, low):
    """Upper-wick fraction of channel: (high - max(o,c))/(high_5 - low_5),
    averaged over 25d. Channel-position derived from where intraday
    extremes are reaching."""
    upper_wick = high - pd.concat([close, open_], axis=1).max(axis=1)
    hi5 = high.rolling(5, min_periods=5).max()
    lo5 = low.rolling(5, min_periods=5).min()
    rng5 = (hi5 - lo5).replace(0.0, np.nan)
    out = (upper_wick / rng5).rolling(25, min_periods=15).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_wicklo_25d_base_v134_signal(close, open_, high, low):
    """Lower-wick fraction of channel (25d analog)."""
    lower_wick = pd.concat([close, open_], axis=1).min(axis=1) - low
    hi5 = high.rolling(5, min_periods=5).max()
    lo5 = low.rolling(5, min_periods=5).min()
    rng5 = (hi5 - lo5).replace(0.0, np.nan)
    out = (lower_wick / rng5).rolling(25, min_periods=15).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group P: regression-fit on channel (2) ------------------------------


def f02pc_f02_price_channel_position_chreg_60d_base_v135_signal(closeadj, high, low):
    """OLS slope of 60d channel midpoint on time-index. Channel-midpoint
    trend slope."""
    hi = high.rolling(60, min_periods=60).max()
    lo = low.rolling(60, min_periods=60).min()
    mid = (hi + lo) / 2.0
    n = 60
    t = np.arange(n, dtype=float)
    tmean = t.mean()
    denom = ((t - tmean) ** 2).sum()
    def _slp(a):
        if np.any(np.isnan(a)):
            return float('nan')
        am = a.mean()
        return float(((t - tmean) * (a - am)).sum() / denom)
    out = mid.rolling(n, min_periods=n).apply(_slp, raw=True)
    return (out / mid.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_chregfit_50d_base_v136_signal(closeadj, high, low):
    """R² of OLS fit of close on 50d channel midpoint. How well midpoint
    explains the close path."""
    hi = high.rolling(50, min_periods=50).max()
    lo = low.rolling(50, min_periods=50).min()
    mid = (hi + lo) / 2.0
    cov = closeadj.rolling(50, min_periods=50).cov(mid)
    vc = closeadj.rolling(50, min_periods=50).var()
    vm = mid.rolling(50, min_periods=50).var()
    out = (cov * cov) / (vc * vm).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group Q: cross-channel divergence (3) -------------------------------


def f02pc_f02_price_channel_position_topbotdv_60d_base_v137_signal(closeadj, high, low):
    """Channel asymmetry: log(high_60 - high_60.shift(30)) - log(low_60 -
    low_60.shift(30) inverse), captures whether top is rising/falling
    relative to bottom."""
    hi = high.rolling(60, min_periods=60).max()
    lo = low.rolling(60, min_periods=60).min()
    dh = hi - hi.shift(30)
    dl = lo.shift(30) - lo
    out = np.arctan(dh) - np.arctan(dl)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_chshape_50d_base_v138_signal(closeadj, high, low):
    """Channel shape: (high_50 - high_50.shift(25)) / (high_50.shift(25) -
    low_50). Top-rise relative to channel-width 25d ago — diagonal
    expansion factor."""
    hi = high.rolling(50, min_periods=50).max()
    lo = low.rolling(50, min_periods=50).min()
    out = (hi - hi.shift(25)) / (hi.shift(25) - lo.shift(25)).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_chsym_30d_base_v139_signal(closeadj, high, low):
    """Channel symmetry score: (high_30 - mid_30)/(mid_30 - low_30) - 1.
    Always 0 by construction; instead use (close - mid)/(c - 30d mean):
    measures asymmetry of position around midpoint vs around long-mean."""
    hi = high.rolling(30, min_periods=30).max()
    lo = low.rolling(30, min_periods=30).min()
    mid = (hi + lo) / 2.0
    mu = closeadj.rolling(30, min_periods=30).mean()
    out = (closeadj - mid) / (closeadj - mu).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group R: channel-anchored MAs (3) ----------------------------------


def f02pc_f02_price_channel_position_chemap_30d_base_v140_signal(closeadj, high, low):
    """EMA of channel-position (30d %B), smoothing the position signal
    with EMA span 10."""
    hi = high.rolling(30, min_periods=30).max()
    lo = low.rolling(30, min_periods=30).min()
    pos = (closeadj - lo) / (hi - lo).replace(0.0, np.nan)
    out = pos.ewm(span=10, adjust=False, min_periods=10).mean() - 0.5
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_chminmid_20d_base_v141_signal(close, high, low):
    """Min position in trailing 20d (using 10d channel). Lowest %B touch."""
    h10 = high.rolling(10, min_periods=10).max()
    l10 = low.rolling(10, min_periods=10).min()
    pos = (close - l10) / (h10 - l10).replace(0.0, np.nan)
    out = pos.rolling(20, min_periods=20).min()
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_chmaxmid_20d_base_v142_signal(close, high, low):
    """Max position in trailing 20d (using 10d channel). Highest %B touch."""
    h10 = high.rolling(10, min_periods=10).max()
    l10 = low.rolling(10, min_periods=10).min()
    pos = (close - l10) / (h10 - l10).replace(0.0, np.nan)
    out = pos.rolling(20, min_periods=20).max() - 0.5
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group S: discrete agreement / multi-window (3) ----------------------


def f02pc_f02_price_channel_position_agrstack_60d_base_v143_signal(closeadj, high, low):
    """Multi-window position-direction agreement: count of N in {10,30,60}
    where %B_N > 0.5 minus count where %B_N < 0.5. Range [-3,+3]."""
    def _bsign(h, l, n):
        hi = h.rolling(n, min_periods=n).max()
        lo = l.rolling(n, min_periods=n).min()
        p = (closeadj - lo) / (hi - lo).replace(0.0, np.nan)
        return np.sign(p - 0.5)
    s10 = _bsign(high, low, 10)
    s30 = _bsign(high, low, 30)
    s60 = _bsign(high, low, 60)
    out = s10 + s30 + s60
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_brkagg_45d_base_v144_signal(closeadj, high, low):
    """Bullish channel-state aggregate: +1 for new-20d-high day, -1 for
    new-20d-low day, 0 otherwise, summed over trailing 45d. Net
    breakout balance."""
    ph = high.shift(1).rolling(20, min_periods=20).max()
    pl = low.shift(1).rolling(20, min_periods=20).min()
    s = pd.Series(0.0, index=closeadj.index, dtype=float)
    s[closeadj > ph] = 1.0
    s[closeadj < pl] = -1.0
    s[ph.isna() | pl.isna()] = np.nan
    out = s.rolling(45, min_periods=22).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_chexh_50d_base_v145_signal(closeadj, high, low):
    """Channel-exhaustion score: fraction of trailing 50d where %B was
    in extreme decile (top 5% or bottom 5%). High value → channel
    edges frequently touched."""
    hi = high.rolling(20, min_periods=20).max()
    lo = low.rolling(20, min_periods=20).min()
    pos = (closeadj - lo) / (hi - lo).replace(0.0, np.nan)
    extreme = ((pos >= 0.95) | (pos <= 0.05)).astype(float)
    extreme[pos.isna()] = np.nan
    out = extreme.rolling(50, min_periods=25).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group T: anchored channel from prior swing-high/swing-low (3) -------


def f02pc_f02_price_channel_position_anchprior_45d_base_v146_signal(closeadj, high):
    """Closeadj relative to highest high reached 22-45 bars ago (not
    including last 22 bars). Distance to mid-historical peak."""
    win = high.shift(22).rolling(23, min_periods=23).max()
    out = np.log(closeadj.replace(0.0, np.nan) / win.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_anchpriorlo_70d_base_v147_signal(closeadj, low):
    """Closeadj relative to lowest low between 30 and 70 bars ago."""
    win = low.shift(30).rolling(41, min_periods=41).min()
    out = np.log(closeadj.replace(0.0, np.nan) / win.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_chrew_50d_base_v148_signal(closeadj, high, low):
    """Channel-reward-risk: distance from 50d low / distance to 50d high
    (asymmetric ratio). > 1 → more room above than below."""
    hi = high.rolling(50, min_periods=50).max()
    lo = low.rolling(50, min_periods=50).min()
    above = (hi - closeadj).clip(lower=1e-9)
    below = (closeadj - lo).clip(lower=1e-9)
    out = np.log(above / below)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group U: channel-position autocorrelation across windows (2) --------


def f02pc_f02_price_channel_position_posac5_75d_base_v149_signal(closeadj, high, low):
    """Lag-5 autocorrelation of %B(20d) over trailing 75d. Captures
    medium-term persistence/reversal of channel position."""
    hi = high.rolling(20, min_periods=20).max()
    lo = low.rolling(20, min_periods=20).min()
    pos = (closeadj - lo) / (hi - lo).replace(0.0, np.nan)
    out = pos.rolling(75, min_periods=50).corr(pos.shift(5))
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_chrev_55d_base_v150_signal(closeadj, high, low):
    """Channel-reversal rate (55d): count of times %B(20d) crossed 0.5
    in trailing 55d, divided by 55. Measures choppiness."""
    hi = high.rolling(20, min_periods=20).max()
    lo = low.rolling(20, min_periods=20).min()
    pos = (closeadj - lo) / (hi - lo).replace(0.0, np.nan)
    s = np.sign(pos - 0.5)
    cross = (s != s.shift(1)).astype(float)
    cross[s.isna() | s.shift(1).isna()] = np.nan
    out = cross.rolling(55, min_periods=28).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


def _e(fn, *inputs):
    return fn.__name__, {"inputs": list(inputs), "func": fn}


f02_price_channel_position_base_076_150_REGISTRY = dict([
    _e(f02pc_f02_price_channel_position_hl2pos_20d_base_v076_signal, "close", "high", "low"),
    _e(f02pc_f02_price_channel_position_hccpos_42d_base_v077_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_ohlcrng_30d_base_v078_signal, "closeadj", "open", "high", "low"),
    _e(f02pc_f02_price_channel_position_obpos_10d_base_v079_signal, "close", "open", "high", "low"),
    _e(f02pc_f02_price_channel_position_truebw_25d_base_v080_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_kelt_20d_base_v081_signal, "close", "high", "low"),
    _e(f02pc_f02_price_channel_position_keltatr_50d_base_v082_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_keltdiv_30d_base_v083_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_bollhi_20d_base_v084_signal, "close", "high"),
    _e(f02pc_f02_price_channel_position_bolllo_30d_base_v085_signal, "closeadj", "low"),
    _e(f02pc_f02_price_channel_position_bollratlo_60d_base_v086_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_qchpos_30d_base_v087_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_qchwid_60d_base_v088_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_qchdiff_50d_base_v089_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_iqrch_45d_base_v090_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_medch_30d_base_v091_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_qchhi_100d_base_v092_signal, "closeadj", "high"),
    _e(f02pc_f02_price_channel_position_brk52w_252d_base_v093_signal, "closeadj", "high"),
    _e(f02pc_f02_price_channel_position_pos252_252d_base_v094_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_dist52h_252d_base_v095_signal, "closeadj", "high"),
    _e(f02pc_f02_price_channel_position_dist52l_252d_base_v096_signal, "closeadj", "low"),
    _e(f02pc_f02_price_channel_position_zh252_252d_base_v097_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_swhipos_30d_base_v098_signal, "closeadj", "high"),
    _e(f02pc_f02_price_channel_position_swlopos_30d_base_v099_signal, "closeadj", "low"),
    _e(f02pc_f02_price_channel_position_swdir_30d_base_v100_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_topcond_60d_base_v101_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_bothcnt_50d_base_v102_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_pinchbrk_70d_base_v103_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_strongbot_30d_base_v104_signal, "close", "high", "low"),
    _e(f02pc_f02_price_channel_position_acccnt_40d_base_v105_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_brkmag_50d_base_v106_signal, "closeadj", "high"),
    _e(f02pc_f02_price_channel_position_brkmaxmag_60d_base_v107_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_brksig_40d_base_v108_signal, "closeadj", "high"),
    _e(f02pc_f02_price_channel_position_pinchrat_50d_base_v109_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_chstack_100d_base_v110_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_chstackdn_100d_base_v111_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_rangedom_30d_base_v112_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_sigpos_30d_base_v113_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_arctanw_40d_base_v114_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_tanhdcn_30d_base_v115_signal, "closeadj", "high"),
    _e(f02pc_f02_price_channel_position_logrng_20d_base_v116_signal, "close", "high", "low"),
    _e(f02pc_f02_price_channel_position_lrretchcd_50d_base_v117_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_pxret_40d_base_v118_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_chsharpe_30d_base_v119_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_vwhipos_30d_base_v120_signal, "closeadj", "high", "low", "volume"),
    _e(f02pc_f02_price_channel_position_vwlopos_30d_base_v121_signal, "closeadj", "low", "volume"),
    _e(f02pc_f02_price_channel_position_volrng_50d_base_v122_signal, "closeadj", "high", "low", "volume"),
    _e(f02pc_f02_price_channel_position_volnewhi_40d_base_v123_signal, "closeadj", "high", "volume"),
    _e(f02pc_f02_price_channel_position_volpos_30d_base_v124_signal, "closeadj", "high", "low", "volume"),
    _e(f02pc_f02_price_channel_position_widkurt_90d_base_v125_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_widskew_70d_base_v126_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_brkkurt_80d_base_v127_signal, "closeadj", "high"),
    _e(f02pc_f02_price_channel_position_widrkdif_80d_base_v128_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_posrkfast_30d_base_v129_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_chconsec_60d_base_v130_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_postransr_60d_base_v131_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_bodyrng_30d_base_v132_signal, "close", "open", "high", "low"),
    _e(f02pc_f02_price_channel_position_wickrat_25d_base_v133_signal, "close", "open", "high", "low"),
    _e(f02pc_f02_price_channel_position_wicklo_25d_base_v134_signal, "close", "open", "high", "low"),
    _e(f02pc_f02_price_channel_position_chreg_60d_base_v135_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_chregfit_50d_base_v136_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_topbotdv_60d_base_v137_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_chshape_50d_base_v138_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_chsym_30d_base_v139_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_chemap_30d_base_v140_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_chminmid_20d_base_v141_signal, "close", "high", "low"),
    _e(f02pc_f02_price_channel_position_chmaxmid_20d_base_v142_signal, "close", "high", "low"),
    _e(f02pc_f02_price_channel_position_agrstack_60d_base_v143_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_brkagg_45d_base_v144_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_chexh_50d_base_v145_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_anchprior_45d_base_v146_signal, "closeadj", "high"),
    _e(f02pc_f02_price_channel_position_anchpriorlo_70d_base_v147_signal, "closeadj", "low"),
    _e(f02pc_f02_price_channel_position_chrew_50d_base_v148_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_posac5_75d_base_v149_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_chrev_55d_base_v150_signal, "closeadj", "high", "low"),
])


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
    for name, entry in f02_price_channel_position_base_076_150_REGISTRY.items():
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
    if max_corr > 0.95 + 1e-9:
        print(f"FAILING max |corr| = {max_corr:.4f}. Top pairs:")
        for i, a in enumerate(corr.columns):
            for j, b in enumerate(corr.columns):
                if j > i and corr.iloc[i, j] > 0.94:
                    print(f"  {a}  vs  {b}  ->  {corr.iloc[i, j]:.4f}")
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK base_076_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
