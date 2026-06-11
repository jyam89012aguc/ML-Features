"""f02_price_channel_position base features 001-075.

Domain: price-channel position — Donchian-style rolling high/low
channels. Every feature references `high.rolling(N).max()` and/or
`low.rolling(N).min()` as anchors. Position-in-channel, distance to
top/bottom, breakouts, streaks/days-since, Donchian state, stochastic
%K/%D, Williams %R, channel slopes/midpoint dynamics, channel widths
and pinches, asymmetry between touches of top vs bottom, volume-aware
channels, anchored-event channels, and statistical descriptors of the
channel position.

NaN policy: NEVER `fillna(<value>)` inside any rolling computation;
only `replace([inf,-inf], nan)` at each function's final return.
Windows > 21 use `closeadj` where the price reference is meaningful at
horizon (channel still uses high/low which are unadjusted intraday
OHLC); windows <= 21 use `close`. Each feature is a fully expanded
`def` block — no `_core()` factory, no `formulas[i]` indexing.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Features 001-075. Each function carries its full channel formula inline.
# ---------------------------------------------------------------------------


# --- Group A: position-inside-channel (only 1 raw %B; rest are transforms) --


def f02pc_f02_price_channel_position_chpos_20d_base_v001_signal(close, high, low):
    """%B-style position in 20d Donchian channel: (c - low_20)/(high_20 - low_20)."""
    hi = high.rolling(20, min_periods=20).max()
    lo = low.rolling(20, min_periods=20).min()
    out = (close - lo) / (hi - lo).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_chposlg_55d_base_v002_signal(closeadj, high, low):
    """log-transformed position: log((c - low_55)+eps) - log((high_55 - c)+eps).
    Bounded transform; structurally different from raw %B."""
    hi = high.rolling(55, min_periods=55).max()
    lo = low.rolling(55, min_periods=55).min()
    eps = (hi - lo) * 0.001 + 1e-9
    out = np.log((closeadj - lo) + eps) - np.log((hi - closeadj) + eps)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_chmid_200d_base_v003_signal(closeadj, high, low):
    """200d channel-midpoint regime crossings: fraction of the trailing 200 bars
    where closeadj is above mid200, minus the fraction below — smoothed via an
    EWMA. Discrete majority-vote feature, structurally distinct from continuous
    %B-style position."""
    hi = high.rolling(200, min_periods=200).max()
    lo = low.rolling(200, min_periods=200).min()
    mid = (hi + lo) / 2.0
    side = np.sign(closeadj - mid).where(~mid.isna())
    out = side.ewm(alpha=0.02, adjust=False, min_periods=50).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group B: distance to channel top / bottom (level-distance) ------------


def f02pc_f02_price_channel_position_dtop_10d_base_v004_signal(close, high):
    """Distance to 10d rolling high (top): (high_10 - close)/close. Always
    >= 0; touches zero at a new high."""
    hi = high.rolling(10, min_periods=10).max()
    out = (hi - close) / close.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_dbot_50d_base_v005_signal(closeadj, low):
    """Distance from 50d rolling low (bottom): (close - low_50)/close."""
    lo = low.rolling(50, min_periods=50).min()
    out = (closeadj - lo) / closeadj.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_dtoplg_200d_base_v006_signal(closeadj, high):
    """log(high_200 / closeadj). Long-horizon log distance to channel top."""
    hi = high.rolling(200, min_periods=200).max()
    out = np.log(hi / closeadj.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group C: channel width and width-dynamics -----------------------------


def f02pc_f02_price_channel_position_chwid_20d_base_v007_signal(close, high, low):
    """Channel width (20d) normalized by spot: (high_20 - low_20)/close."""
    hi = high.rolling(20, min_periods=20).max()
    lo = low.rolling(20, min_periods=20).min()
    out = (hi - lo) / close.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_chwidlg_63d_base_v008_signal(closeadj, high, low):
    """log channel width (63d): log(high_63/low_63). Scale-free width."""
    hi = high.rolling(63, min_periods=63).max()
    lo = low.rolling(63, min_periods=63).min()
    out = np.log(hi.replace(0.0, np.nan) / lo.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_chwidrk_120d_base_v009_signal(closeadj, high, low):
    """Channel-width percentile rank in trailing 120d. Detects regime of
    width (expanded/compressed)."""
    hi = high.rolling(30, min_periods=30).max()
    lo = low.rolling(30, min_periods=30).min()
    w = (hi - lo) / closeadj.replace(0.0, np.nan)
    out = w.rolling(120, min_periods=60).rank(pct=True) - 0.5
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_chwidslp_50d_base_v010_signal(closeadj, high, low):
    """50d channel width slope: width(50d).diff(21)/width — widening>0,
    narrowing<0."""
    hi = high.rolling(50, min_periods=50).max()
    lo = low.rolling(50, min_periods=50).min()
    w = (hi - lo) / closeadj.replace(0.0, np.nan)
    out = w.diff(21) / w.abs().rolling(21, min_periods=21).mean().replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_chwidrat_50d_base_v011_signal(closeadj, high, low):
    """log of short-channel width / long-channel width: log(w_10 / w_50).
    >0 when short channel is wider (recent expansion)."""
    hi10 = high.rolling(10, min_periods=10).max()
    lo10 = low.rolling(10, min_periods=10).min()
    hi50 = high.rolling(50, min_periods=50).max()
    lo50 = low.rolling(50, min_periods=50).min()
    w10 = (hi10 - lo10).replace(0.0, np.nan)
    w50 = (hi50 - lo50).replace(0.0, np.nan)
    out = np.log(w10) - np.log(w50)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_chpinch_60d_base_v012_signal(closeadj, high, low):
    """Channel pinch detector: 1 if current 20d width < 20th percentile of
    trailing 60d widths, else 0. Discrete state."""
    hi = high.rolling(20, min_periods=20).max()
    lo = low.rolling(20, min_periods=20).min()
    w = (hi - lo) / closeadj.replace(0.0, np.nan)
    rk = w.rolling(60, min_periods=30).rank(pct=True)
    out = (rk < 0.20).astype(float)
    out[rk.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group D: channel slopes -----------------------------------------------


def f02pc_f02_price_channel_position_chhislp_30d_base_v013_signal(closeadj, high):
    """Slope of 30d rolling high: high_30.diff(10)/high_30. Top-rising."""
    hi = high.rolling(30, min_periods=30).max()
    out = hi.diff(10) / hi.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_chloslp_30d_base_v014_signal(closeadj, low):
    """Slope of 30d rolling low: low_30.diff(10)/low_30. Bottom-rising."""
    lo = low.rolling(30, min_periods=30).min()
    out = lo.diff(10) / lo.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_chmidslp_100d_base_v015_signal(closeadj, high, low):
    """Slope of 100d channel midpoint: mid.diff(21)/mid."""
    hi = high.rolling(100, min_periods=100).max()
    lo = low.rolling(100, min_periods=100).min()
    mid = (hi + lo) / 2.0
    out = mid.diff(21) / mid.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_chexpdv_30d_base_v016_signal(closeadj, high, low):
    """Channel expansion divergence: high_30.diff(10)/high_30 - low_30.diff(10)/low_30.
    Positive = top rising faster than bottom (asymmetric expansion)."""
    hi = high.rolling(30, min_periods=30).max()
    lo = low.rolling(30, min_periods=30).min()
    out = (hi.diff(10) / hi.replace(0.0, np.nan)) - (lo.diff(10) / lo.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group E: breakouts (binary / signed) ----------------------------------


def f02pc_f02_price_channel_position_brkup_20d_base_v017_signal(close, high):
    """sign(close - prior_20d_high_excluding_today): +1 if today broke
    above the 20d high computed up to yesterday."""
    prior = high.shift(1).rolling(20, min_periods=20).max()
    out = np.sign(close - prior).astype(float)
    out[prior.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_brkdn_55d_base_v018_signal(closeadj, low):
    """sign(close - prior_55d_low): +1 above, -1 below prior 55d low."""
    prior = low.shift(1).rolling(55, min_periods=55).min()
    out = np.sign(closeadj - prior).astype(float)
    out[prior.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_brkcnt_60d_base_v019_signal(closeadj, high):
    """Count of upside channel-break days in trailing 60: bars where
    today's close exceeded prior 20d high. Integer 0..60."""
    prior20 = high.shift(1).rolling(20, min_periods=20).max()
    brk = (closeadj > prior20).astype(float)
    brk[prior20.isna()] = np.nan
    out = brk.rolling(60, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_brkbal_50d_base_v020_signal(closeadj, high, low):
    """Up-break minus down-break count in trailing 50: number of new
    20d highs minus number of new 20d lows."""
    ph = high.shift(1).rolling(20, min_periods=20).max()
    pl = low.shift(1).rolling(20, min_periods=20).min()
    up = (closeadj > ph).astype(float)
    dn = (closeadj < pl).astype(float)
    up[ph.isna()] = np.nan
    dn[pl.isna()] = np.nan
    out = up.rolling(50, min_periods=25).sum() - dn.rolling(50, min_periods=25).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group F: streaks / days-since ----------------------------------------


def f02pc_f02_price_channel_position_streakup_20d_base_v021_signal(close, high):
    """Streak of consecutive days where close sits in the top quintile of the
    trailing 20d high-low channel (close >= low_20 + 0.8*(high_20 - low_20)).
    Resets to 0 once the close drops out of the top quintile."""
    hi = high.rolling(20, min_periods=20).max()
    lo = close.rolling(20, min_periods=20).min()
    thr = lo + 0.8 * (hi - lo)
    hit = (close >= thr).astype(float)
    grp = (hit != hit.shift()).cumsum()
    out = hit.groupby(grp).cumsum().where(~hi.isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_dayslast_50d_base_v022_signal(closeadj, high):
    """Days since last 50d channel high (close == high_50). Saturates at
    50. Resets to 0 on each touch of the top."""
    hi = high.rolling(50, min_periods=50).max()
    at_top = (closeadj >= hi)
    idx = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    last_hit = idx.where(at_top).ffill()
    out = (idx - last_hit).clip(upper=50.0).where(~hi.isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_dayslo_100d_base_v023_signal(closeadj, low):
    """Days since last 100d channel low (close == low_100). Saturates at 100."""
    lo = low.rolling(100, min_periods=100).min()
    at_bot = (low <= lo)
    idx = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    last_hit = idx.where(at_bot).ffill()
    out = (idx - last_hit).clip(upper=100.0).where(~lo.isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_dayswide_60d_base_v024_signal(closeadj, high, low):
    """Days since last channel-width 90th percentile event (width=high_20-low_20).
    Saturates at 60."""
    hi = high.rolling(20, min_periods=20).max()
    lo = low.rolling(20, min_periods=20).min()
    w = (hi - lo) / closeadj.replace(0.0, np.nan)
    rk = w.rolling(60, min_periods=30).rank(pct=True)
    wide = (rk >= 0.90)
    idx = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    last_hit = idx.where(wide).ffill()
    out = (idx - last_hit).clip(upper=60.0).where(~rk.isna())
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group G: Donchian state (discrete buckets) ----------------------------


def f02pc_f02_price_channel_position_donst_30d_base_v025_signal(closeadj, high, low):
    """Donchian state in 30d channel: +1 top quartile, -1 bottom quartile,
    0 middle. Discrete state."""
    hi = high.rolling(30, min_periods=30).max()
    lo = low.rolling(30, min_periods=30).min()
    pos = (closeadj - lo) / (hi - lo).replace(0.0, np.nan)
    out = pd.Series(0.0, index=closeadj.index, dtype=float)
    out[pos >= 0.75] = 1.0
    out[pos <= 0.25] = -1.0
    out[pos.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_donqt_75d_base_v026_signal(closeadj, high, low):
    """Donchian quartile bucket (75d): integer 0/1/2/3 for which quartile
    of the 75d channel the close occupies."""
    hi = high.rolling(75, min_periods=75).max()
    lo = low.rolling(75, min_periods=75).min()
    pos = (closeadj - lo) / (hi - lo).replace(0.0, np.nan)
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    out[pos < 0.25] = 0.0
    out[(pos >= 0.25) & (pos < 0.5)] = 1.0
    out[(pos >= 0.5) & (pos < 0.75)] = 2.0
    out[pos >= 0.75] = 3.0
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group H: stochastic %K / %D / slow-K ----------------------------------




def f02pc_f02_price_channel_position_stoXdrt_14d_base_v028_signal(close, high, low):
    """Channel-position acceleration: stochastic %K (14d) diff over 5 bars
    minus diff over 1 bar — captures whether the channel-position trend
    is accelerating or decelerating. Distinct from raw %K levels."""
    hi = high.rolling(14, min_periods=14).max()
    lo = low.rolling(14, min_periods=14).min()
    k = 100.0 * (close - lo) / (hi - lo).replace(0.0, np.nan)
    out = k.diff(5) - 5.0 * k.diff(1)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_stoSK_42d_base_v029_signal(closeadj, high, low):
    """Slow-K stochastic on 42d channel: 5-day smoothed (c-low_42)/(high_42-low_42)."""
    hi = high.rolling(42, min_periods=42).max()
    lo = low.rolling(42, min_periods=42).min()
    k = (closeadj - lo) / (hi - lo).replace(0.0, np.nan)
    out = k.rolling(5, min_periods=5).mean() - 0.5
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_stochmi_25d_base_v030_signal(closeadj, high, low):
    """Stochastic Momentum Index variant (25d): position relative to
    midpoint, scaled by half-range, double-smoothed."""
    hi = high.rolling(25, min_periods=25).max()
    lo = low.rolling(25, min_periods=25).min()
    mid = (hi + lo) / 2.0
    num = (closeadj - mid).ewm(span=5, adjust=False, min_periods=5).mean()
    den = ((hi - lo) / 2.0).ewm(span=5, adjust=False, min_periods=5).mean()
    out = num / den.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group I: Williams %R ---------------------------------------------------


def f02pc_f02_price_channel_position_wpr_10d_base_v031_signal(close, high, low):
    """Williams %R (10d): -100*(high_10 - c)/(high_10 - low_10). Range
    approximately [-100, 0]."""
    hi = high.rolling(10, min_periods=10).max()
    lo = low.rolling(10, min_periods=10).min()
    out = -100.0 * (hi - close) / (hi - lo).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_halfbin_63d_base_v032_signal(closeadj, high, low):
    """Half-channel binary state (63d): +1 if close above 63d midpoint,
    -1 if below. Discrete; structurally different from continuous %B."""
    hi = high.rolling(63, min_periods=63).max()
    lo = low.rolling(63, min_periods=63).min()
    mid = (hi + lo) / 2.0
    out = np.sign(closeadj - mid).astype(float)
    out[mid.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group J: asymmetry: top-touch vs bottom-touch ------------------------


def f02pc_f02_price_channel_position_asymabs_30d_base_v033_signal(closeadj, high, low):
    """log( |close - high_30| / |close - low_30| ): asymmetry between
    distance to top and distance to bottom."""
    hi = high.rolling(30, min_periods=30).max()
    lo = low.rolling(30, min_periods=30).min()
    a = (hi - closeadj).abs() + 1e-9
    b = (closeadj - lo).abs() + 1e-9
    out = np.log(a) - np.log(b)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_lastside_40d_base_v034_signal(closeadj, high, low):
    """Sign indicating which side of 40d channel was touched most recently:
    +1 if last touched top, -1 if last touched bottom."""
    hi = high.rolling(40, min_periods=40).max()
    lo = low.rolling(40, min_periods=40).min()
    at_top = (high >= hi)
    at_bot = (low <= lo)
    idx = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    top_idx = idx.where(at_top).ffill()
    bot_idx = idx.where(at_bot).ffill()
    state = np.sign(top_idx - bot_idx).where(~(hi.isna() | lo.isna()))
    return state.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_topvsbot_60d_base_v035_signal(closeadj, high, low):
    """Top-touch count minus bottom-touch count in trailing 60d (touch =
    close in top/bottom 5% of channel)."""
    hi = high.rolling(30, min_periods=30).max()
    lo = low.rolling(30, min_periods=30).min()
    pos = (closeadj - lo) / (hi - lo).replace(0.0, np.nan)
    top_hit = (pos >= 0.95).astype(float)
    bot_hit = (pos <= 0.05).astype(float)
    top_hit[pos.isna()] = np.nan
    bot_hit[pos.isna()] = np.nan
    out = top_hit.rolling(60, min_periods=30).sum() - bot_hit.rolling(60, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group K: time-in-extreme (statistical) --------------------------------


def f02pc_f02_price_channel_position_timetop_60d_base_v036_signal(closeadj, high, low):
    """Fraction of trailing 60d in top decile of 30d channel."""
    hi = high.rolling(30, min_periods=30).max()
    lo = low.rolling(30, min_periods=30).min()
    pos = (closeadj - lo) / (hi - lo).replace(0.0, np.nan)
    in_top = (pos >= 0.90).astype(float)
    in_top[pos.isna()] = np.nan
    out = in_top.rolling(60, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_timebot_120d_base_v037_signal(closeadj, high, low):
    """Fraction of trailing 120d in bottom decile of 50d channel."""
    hi = high.rolling(50, min_periods=50).max()
    lo = low.rolling(50, min_periods=50).min()
    pos = (closeadj - lo) / (hi - lo).replace(0.0, np.nan)
    in_bot = (pos <= 0.10).astype(float)
    in_bot[pos.isna()] = np.nan
    out = in_bot.rolling(120, min_periods=60).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group L: anchored-event channels --------------------------------------


def f02pc_f02_price_channel_position_anchhi_30d_base_v038_signal(closeadj, high):
    """Distance from the highest high reached in the last 30d to current
    closeadj, normalized: drawdown-from-30d-peak. Always <=0."""
    hi = high.rolling(30, min_periods=30).max()
    out = np.log(closeadj.replace(0.0, np.nan) / hi.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_anchlo_100d_base_v039_signal(closeadj, low):
    """Run-up from 100d lowest low to current closeadj, log-normalized."""
    lo = low.rolling(100, min_periods=100).min()
    out = np.log(closeadj.replace(0.0, np.nan) / lo.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_decay_50d_base_v040_signal(closeadj, high):
    """Channel decay: how many bars-equivalent the close has spent below
    the 50d high — measured as (high_50 - closeadj)/sigma_50. Scale-free."""
    hi = high.rolling(50, min_periods=50).max()
    sig = closeadj.diff().rolling(50, min_periods=50).std()
    out = (hi - closeadj) / sig.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group M: volume-aware channel features (uses volume) ------------------


def f02pc_f02_price_channel_position_vwapchpos_30d_base_v041_signal(closeadj, high, low, volume):
    """Position vs VWAP-anchored channel: (close - vwap_30) /
    (high_30 - low_30). VWAP replaces midpoint as anchor."""
    typ = (high + low + closeadj) / 3.0
    pv = typ * volume
    vwap = pv.rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    hi = high.rolling(30, min_periods=30).max()
    lo = low.rolling(30, min_periods=30).min()
    out = (closeadj - vwap) / (hi - lo).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_volbrk_40d_base_v042_signal(closeadj, high, volume):
    """Volume on channel-break days vs all-day volume in trailing 40d:
    >1 means breaks happen on heavier volume."""
    ph = high.shift(1).rolling(20, min_periods=20).max()
    brk = (closeadj > ph).astype(float)
    brk[ph.isna()] = np.nan
    brk_vol = (brk * volume).rolling(40, min_periods=20).sum()
    all_vol = volume.rolling(40, min_periods=20).sum().replace(0.0, np.nan)
    avg_brk = brk_vol / (brk.rolling(40, min_periods=20).sum().replace(0.0, np.nan))
    avg_all = all_vol / 40.0
    out = np.log(avg_brk.replace(0.0, np.nan) / avg_all.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group N: statistical / percentile-rank on the position series ---------


def f02pc_f02_price_channel_position_posrk_120d_base_v043_signal(closeadj, high, low):
    """Percentile rank of current %B (20d) over trailing 120d. Captures
    whether the position itself is at an extreme of its own history."""
    hi = high.rolling(20, min_periods=20).max()
    lo = low.rolling(20, min_periods=20).min()
    pos = (closeadj - lo) / (hi - lo).replace(0.0, np.nan)
    out = pos.rolling(120, min_periods=60).rank(pct=True) - 0.5
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_posstd_60d_base_v044_signal(closeadj, high, low):
    """Std-dev of %B (20d) over trailing 60d. Measures channel-position
    volatility, distinct from channel width."""
    hi = high.rolling(20, min_periods=20).max()
    lo = low.rolling(20, min_periods=20).min()
    pos = (closeadj - lo) / (hi - lo).replace(0.0, np.nan)
    out = pos.rolling(60, min_periods=30).std()
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_posskew_90d_base_v045_signal(closeadj, high, low):
    """Skew of %B (30d) over trailing 90d. Asymmetry of channel-position
    distribution."""
    hi = high.rolling(30, min_periods=30).max()
    lo = low.rolling(30, min_periods=30).min()
    pos = (closeadj - lo) / (hi - lo).replace(0.0, np.nan)
    out = pos.rolling(90, min_periods=45).skew()
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_zscpos_50d_base_v046_signal(closeadj, high, low):
    """Z-score of %B (20d) over trailing 50d. Bounded transform of
    extremeness."""
    hi = high.rolling(20, min_periods=20).max()
    lo = low.rolling(20, min_periods=20).min()
    pos = (closeadj - lo) / (hi - lo).replace(0.0, np.nan)
    mu = pos.rolling(50, min_periods=25).mean()
    sd = pos.rolling(50, min_periods=25).std()
    out = (pos - mu) / sd.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group O: nearest-edge signed distance ---------------------------------


def f02pc_f02_price_channel_position_nearedge_30d_base_v047_signal(closeadj, high, low):
    """Signed distance to nearest channel edge (30d): sign(2*pos-1) *
    min(c-low, high-c) / (high - low). Positive when nearer top."""
    hi = high.rolling(30, min_periods=30).max()
    lo = low.rolling(30, min_periods=30).min()
    width = (hi - lo).replace(0.0, np.nan)
    to_top = (hi - closeadj) / width
    to_bot = (closeadj - lo) / width
    nearest = pd.concat([to_top, to_bot], axis=1).min(axis=1)
    s = np.sign(to_bot - to_top)
    out = s * nearest
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group P: bounded transforms of position --------------------------------


def f02pc_f02_price_channel_position_posagree_60d_base_v048_signal(closeadj, high, low):
    """Sign agreement of short and long channel positions: sign(%B_10 -
    0.5) * sign(%B_60 - 0.5). +1 means both halves agree (top or both
    bottom), -1 means split. Discrete {-1,0,1}."""
    h10 = high.rolling(10, min_periods=10).max()
    l10 = low.rolling(10, min_periods=10).min()
    h60 = high.rolling(60, min_periods=60).max()
    l60 = low.rolling(60, min_periods=60).min()
    p10 = (closeadj - l10) / (h10 - l10).replace(0.0, np.nan) - 0.5
    p60 = (closeadj - l60) / (h60 - l60).replace(0.0, np.nan) - 0.5
    out = np.sign(p10) * np.sign(p60)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_tanhdt_25d_base_v049_signal(close, high, low):
    """25d edge-streak indicator: streak of consecutive bars where the close
    sits within 10% of one channel edge. Signed (+streak near top,
    -streak near bottom), zero when in the middle band. Streak/count
    feature — structurally distinct from continuous tanh position."""
    hi = high.rolling(25, min_periods=25).max()
    lo = low.rolling(25, min_periods=25).min()
    pos = (close - lo) / (hi - lo).replace(0.0, np.nan)
    near_top = (pos >= 0.9).astype(float)
    near_bot = (pos <= 0.1).astype(float)
    state = near_top - near_bot
    grp = (state != state.shift()).cumsum()
    streak = state.groupby(grp).cumcount() + 1
    out = (state * streak).where(~hi.isna())
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group Q: cross-channel differential -----------------------------------


def f02pc_f02_price_channel_position_diffpos_50d_base_v050_signal(closeadj, high, low):
    """Pos(10d) - pos(50d). Short minus long channel position; nulls
    long-horizon drift."""
    h10 = high.rolling(10, min_periods=10).max()
    l10 = low.rolling(10, min_periods=10).min()
    h50 = high.rolling(50, min_periods=50).max()
    l50 = low.rolling(50, min_periods=50).min()
    p10 = (closeadj - l10) / (h10 - l10).replace(0.0, np.nan)
    p50 = (closeadj - l50) / (h50 - l50).replace(0.0, np.nan)
    out = p10 - p50
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_diffdt_100d_base_v051_signal(closeadj, high, low):
    """log( (high_20 - close) / (high_100 - close) ). Cross-window
    distance-to-top differential — captures whether the short-channel
    top is near the long-channel top."""
    h20 = high.rolling(20, min_periods=20).max()
    h100 = high.rolling(100, min_periods=100).max()
    a = (h20 - closeadj) + 1e-9
    b = (h100 - closeadj) + 1e-9
    out = np.log(a) - np.log(b)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group R: signal counts of mid-crossings -------------------------------


def f02pc_f02_price_channel_position_midcross_60d_base_v052_signal(closeadj, high, low):
    """Count of mid-channel crossings in trailing 60d (30d channel
    midpoint). Indicator of choppy channel behavior."""
    hi = high.rolling(30, min_periods=30).max()
    lo = low.rolling(30, min_periods=30).min()
    mid = (hi + lo) / 2.0
    sgn = np.sign(closeadj - mid)
    cross = (sgn != sgn.shift(1)).astype(float)
    cross[sgn.isna() | sgn.shift(1).isna()] = np.nan
    out = cross.rolling(60, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_topcnt_40d_base_v053_signal(closeadj, high):
    """Count of new 5d highs that simultaneously also broke prior 20d
    high — distinct (rare) compound-breakout count in trailing 40d."""
    h5p = high.shift(1).rolling(5, min_periods=5).max()
    h20p = high.shift(1).rolling(20, min_periods=20).max()
    comp = ((closeadj > h5p) & (closeadj > h20p)).astype(float)
    comp[h5p.isna() | h20p.isna()] = np.nan
    out = comp.rolling(40, min_periods=20).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group S: percentile rank of the high/low itself -----------------------


def f02pc_f02_price_channel_position_hirk_100d_base_v054_signal(closeadj, high, low):
    """Top-touch density (100d): rolling 100d count of bars whose intraday
    high equals the trailing 100d max, minus the count of bars whose
    intraday low equals the trailing 100d min. Discrete event-count
    indicator — structurally distinct from continuous channel positions."""
    h100 = high.rolling(100, min_periods=100).max()
    l100 = low.rolling(100, min_periods=100).min()
    top_hit = (high >= h100).astype(float).where(~h100.isna())
    bot_hit = (low <= l100).astype(float).where(~l100.isna())
    out = top_hit.rolling(100, min_periods=50).sum() - bot_hit.rolling(100, min_periods=50).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_lork_60d_base_v055_signal(closeadj, high, low):
    """60d low-touch streak: signed streak of consecutive bars where the
    intraday low equals the trailing 60d minimum (negative streak) minus
    where intraday low equals the trailing 60d maximum-low (positive).
    Discrete streak feature, structurally distinct from continuous %B."""
    h60 = high.rolling(60, min_periods=60).max()
    l60 = low.rolling(60, min_periods=60).min()
    at_bot = (low <= l60).astype(float)
    at_top = (low >= h60).astype(float)
    state = at_top - at_bot
    grp = (state != state.shift()).cumsum()
    streak = state.groupby(grp).cumcount() + 1
    out = (state * streak).where(~l60.isna())
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group T: channel acceleration ----------------------------------------


def f02pc_f02_price_channel_position_chacc_50d_base_v056_signal(closeadj, high, low):
    """2nd difference of channel midpoint (50d): mid - 2*mid.shift(10) +
    mid.shift(20), normalized by mid."""
    hi = high.rolling(50, min_periods=50).max()
    lo = low.rolling(50, min_periods=50).min()
    mid = (hi + lo) / 2.0
    out = (mid - 2.0 * mid.shift(10) + mid.shift(20)) / mid.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_widacc_30d_base_v057_signal(closeadj, high, low):
    """Acceleration of channel width (30d)."""
    hi = high.rolling(30, min_periods=30).max()
    lo = low.rolling(30, min_periods=30).min()
    w = (hi - lo)
    out = (w - 2.0 * w.shift(10) + w.shift(20)) / w.abs().rolling(20, min_periods=20).mean().replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group U: range-based bands --------------------------------------------


def f02pc_f02_price_channel_position_ulpos_20d_base_v058_signal(close, high, low):
    """Ulcer-like position: rolling RMS of channel-drawdown depth.
    Drawdown = (high_20 - close)/high_20. Always >= 0."""
    hi = high.rolling(20, min_periods=20).max()
    dd = (hi - close) / hi.replace(0.0, np.nan)
    out = (dd ** 2).rolling(20, min_periods=20).mean().pow(0.5)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_uppos_30d_base_v059_signal(closeadj, high, low):
    """Symmetric — up-pos: rolling RMS of channel-runup height
    (close - low_30)/low_30."""
    lo = low.rolling(30, min_periods=30).min()
    ru = (closeadj - lo) / lo.replace(0.0, np.nan)
    out = (ru ** 2).rolling(30, min_periods=30).mean().pow(0.5)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group V: ATR-style anchored channel -----------------------------------


def f02pc_f02_price_channel_position_atrwid_20d_base_v060_signal(close, high, low):
    """Channel width measured in ATR-units: (high_20 - low_20) / ATR(20)."""
    tr = pd.concat([(high - low), (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(20, min_periods=20).mean()
    hi = high.rolling(20, min_periods=20).max()
    lo = low.rolling(20, min_periods=20).min()
    out = (hi - lo) / atr.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_atrposd_30d_base_v061_signal(closeadj, high, low):
    """ATR-stride distance from 30d channel midpoint, in *integer* ATR units:
    floor((c - mid_30) / ATR(30)). Discrete stride feature — structurally
    distinct from continuous VWAP-position v041."""
    tr = pd.concat([(high - low), (high - closeadj.shift(1)).abs(), (low - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(30, min_periods=30).mean()
    hi = high.rolling(30, min_periods=30).max()
    lo = low.rolling(30, min_periods=30).min()
    mid = (hi + lo) / 2.0
    raw = (closeadj - mid) / atr.replace(0.0, np.nan)
    out = np.floor(raw)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group W: rate of channel expansion -----------------------------------


def f02pc_f02_price_channel_position_newhicnt_50d_base_v062_signal(closeadj, high):
    """Number of new 50d highs scored in trailing 50d (= number of
    distinct days where high == high_50.shift(1))."""
    prior = high.shift(1).rolling(50, min_periods=50).max()
    new_hi = (high > prior).astype(float)
    new_hi[prior.isna()] = np.nan
    out = new_hi.rolling(50, min_periods=25).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_newlocnt_30d_base_v063_signal(closeadj, low):
    """Number of new 30d lows scored in trailing 30d."""
    prior = low.shift(1).rolling(30, min_periods=30).min()
    new_lo = (low < prior).astype(float)
    new_lo[prior.isna()] = np.nan
    out = new_lo.rolling(30, min_periods=15).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group X: channel envelope penetration ---------------------------------


def f02pc_f02_price_channel_position_pierce_30d_base_v064_signal(close, high, low):
    """Channel pierce magnitude: max( c - high_30.shift(1), low_30.shift(1) - c, 0 )
    normalized by channel width. Captures how far beyond the prior
    channel today went."""
    ph = high.shift(1).rolling(30, min_periods=30).max()
    pl = low.shift(1).rolling(30, min_periods=30).min()
    width = (ph - pl).replace(0.0, np.nan)
    up = (close - ph).clip(lower=0.0) / width
    dn = (pl - close).clip(lower=0.0) / width
    out = up - dn
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_pierce_100d_base_v065_signal(closeadj, high, low):
    """100d pierce magnitude: same construction as v064 but at a long
    horizon — a 100d break is structurally rarer."""
    ph = high.shift(1).rolling(100, min_periods=100).max()
    pl = low.shift(1).rolling(100, min_periods=100).min()
    width = (ph - pl).replace(0.0, np.nan)
    up = (closeadj - ph).clip(lower=0.0) / width
    dn = (pl - closeadj).clip(lower=0.0) / width
    out = up - dn
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group Y: time-decay of channel high ----------------------------------


def f02pc_f02_price_channel_position_decayrt_70d_base_v066_signal(closeadj, high):
    """Decay-from-peak speed: avg per-day drop in (high_70 - close)/close
    over trailing 21d, captures speed of pullback off a peak."""
    hi = high.rolling(70, min_periods=70).max()
    drop = (hi - closeadj) / closeadj.replace(0.0, np.nan)
    out = drop.diff(21) / 21.0
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group Z: dispersion of channel highs ---------------------------------


def f02pc_f02_price_channel_position_hivol_60d_base_v067_signal(closeadj, high):
    """Std of 20d rolling high over trailing 60d, normalized: how
    volatile is the channel-top itself."""
    hi = high.rolling(20, min_periods=20).max()
    sd = hi.rolling(60, min_periods=30).std()
    mu = hi.rolling(60, min_periods=30).mean().replace(0.0, np.nan)
    out = sd / mu
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_lovol_90d_base_v068_signal(closeadj, low):
    """Std of 40d rolling low over trailing 90d, normalized: channel-bottom
    volatility."""
    lo = low.rolling(40, min_periods=40).min()
    sd = lo.rolling(90, min_periods=45).std()
    mu = lo.rolling(90, min_periods=45).mean().replace(0.0, np.nan)
    out = sd / mu
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group AA: channel-position autocorr ---------------------------------


def f02pc_f02_price_channel_position_posac1_60d_base_v069_signal(closeadj, high, low):
    """Lag-1 autocorrelation of %B(20d) over trailing 60d. Measures
    persistence of channel position; mean-reverting if negative."""
    hi = high.rolling(20, min_periods=20).max()
    lo = low.rolling(20, min_periods=20).min()
    pos = (closeadj - lo) / (hi - lo).replace(0.0, np.nan)
    out = pos.rolling(60, min_periods=40).corr(pos.shift(1))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group BB: high-low spread asymmetry ---------------------------------


def f02pc_f02_price_channel_position_hiprgr_30d_base_v070_signal(closeadj, high):
    """Progress toward 30d high: (high - high.shift(21))/high.shift(21).
    Positive when 30d high is making new ground."""
    hi = high.rolling(30, min_periods=30).max()
    out = (hi - hi.shift(21)) / hi.shift(21).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f02pc_f02_price_channel_position_loprgr_30d_base_v071_signal(closeadj, low):
    """Progress of 30d low: (low_30 - low_30.shift(21))/low_30.shift(21).
    Positive when channel bottom is rising."""
    lo = low.rolling(30, min_periods=30).min()
    out = (lo - lo.shift(21)) / lo.shift(21).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group CC: realized range vs channel ---------------------------------


def f02pc_f02_price_channel_position_pkfill_30d_base_v072_signal(closeadj, high, low):
    """How much of the 30d channel-top has been touched in trailing 30d:
    1 minus fraction of bars where high < high_30 (so 0 means top never
    touched after first day, 1 means daily new high). Bounded [0,1]."""
    hi = high.rolling(30, min_periods=30).max()
    touch = (high >= hi).astype(float)
    touch[hi.isna()] = np.nan
    out = touch.rolling(30, min_periods=15).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group DD: pivot-based channel ----------------------------------------


def f02pc_f02_price_channel_position_pivpos_50d_base_v073_signal(closeadj, high, low):
    """Pivot breach asymmetry (50d): count of bars in trailing 50d where
    closeadj > R1 minus count where closeadj < S1. R1/S1 are classical
    floor-trader pivots (R1 = 2P - low_50, S1 = 2P - high_50). Count
    asymmetry is structurally distinct from continuous position."""
    hi = high.rolling(50, min_periods=50).max()
    lo = low.rolling(50, min_periods=50).min()
    c50 = closeadj.rolling(50, min_periods=50).mean()
    piv = (hi + lo + c50) / 3.0
    r1 = 2.0 * piv - lo
    s1 = 2.0 * piv - hi
    above = (closeadj > r1).astype(float).where(~piv.isna())
    below = (closeadj < s1).astype(float).where(~piv.isna())
    out = above.rolling(50, min_periods=25).sum() - below.rolling(50, min_periods=25).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group EE: percentile of high-low spread (volatility channel) ---------


def f02pc_f02_price_channel_position_hlrk_80d_base_v074_signal(closeadj, high, low):
    """Percentile rank of (high - low)/close in trailing 80d. Range-
    expansion regime indicator."""
    hl = (high - low) / closeadj.replace(0.0, np.nan)
    out = hl.rolling(80, min_periods=40).rank(pct=True) - 0.5
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group FF: regime-anchored channel position --------------------------


def f02pc_f02_price_channel_position_regpos_150d_base_v075_signal(closeadj, high, low):
    """150d regime tilt: rolling 150d count of new-150d-highs minus new-150d-lows
    (each event detected against the *prior* 150d extreme, excluding today),
    scaled by 150. Count-based regime indicator, structurally distinct from
    continuous channel position."""
    pri_hi = high.shift(1).rolling(150, min_periods=150).max()
    pri_lo = low.shift(1).rolling(150, min_periods=150).min()
    nh = (high > pri_hi).astype(float).where(~pri_hi.isna())
    nl = (low < pri_lo).astype(float).where(~pri_lo.isna())
    out = (nh.rolling(150, min_periods=75).sum() - nl.rolling(150, min_periods=75).sum()) / 150.0
    return out.replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


def _e(fn, *inputs):
    return fn.__name__, {"inputs": list(inputs), "func": fn}


f02_price_channel_position_base_001_075_REGISTRY = dict([
    _e(f02pc_f02_price_channel_position_chpos_20d_base_v001_signal, "close", "high", "low"),
    _e(f02pc_f02_price_channel_position_chposlg_55d_base_v002_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_chmid_200d_base_v003_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_dtop_10d_base_v004_signal, "close", "high"),
    _e(f02pc_f02_price_channel_position_dbot_50d_base_v005_signal, "closeadj", "low"),
    _e(f02pc_f02_price_channel_position_dtoplg_200d_base_v006_signal, "closeadj", "high"),
    _e(f02pc_f02_price_channel_position_chwid_20d_base_v007_signal, "close", "high", "low"),
    _e(f02pc_f02_price_channel_position_chwidlg_63d_base_v008_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_chwidrk_120d_base_v009_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_chwidslp_50d_base_v010_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_chwidrat_50d_base_v011_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_chpinch_60d_base_v012_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_chhislp_30d_base_v013_signal, "closeadj", "high"),
    _e(f02pc_f02_price_channel_position_chloslp_30d_base_v014_signal, "closeadj", "low"),
    _e(f02pc_f02_price_channel_position_chmidslp_100d_base_v015_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_chexpdv_30d_base_v016_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_brkup_20d_base_v017_signal, "close", "high"),
    _e(f02pc_f02_price_channel_position_brkdn_55d_base_v018_signal, "closeadj", "low"),
    _e(f02pc_f02_price_channel_position_brkcnt_60d_base_v019_signal, "closeadj", "high"),
    _e(f02pc_f02_price_channel_position_brkbal_50d_base_v020_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_streakup_20d_base_v021_signal, "close", "high"),
    _e(f02pc_f02_price_channel_position_dayslast_50d_base_v022_signal, "closeadj", "high"),
    _e(f02pc_f02_price_channel_position_dayslo_100d_base_v023_signal, "closeadj", "low"),
    _e(f02pc_f02_price_channel_position_dayswide_60d_base_v024_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_donst_30d_base_v025_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_donqt_75d_base_v026_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_stoXdrt_14d_base_v028_signal, "close", "high", "low"),
    _e(f02pc_f02_price_channel_position_stoSK_42d_base_v029_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_stochmi_25d_base_v030_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_wpr_10d_base_v031_signal, "close", "high", "low"),
    _e(f02pc_f02_price_channel_position_halfbin_63d_base_v032_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_asymabs_30d_base_v033_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_lastside_40d_base_v034_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_topvsbot_60d_base_v035_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_timetop_60d_base_v036_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_timebot_120d_base_v037_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_anchhi_30d_base_v038_signal, "closeadj", "high"),
    _e(f02pc_f02_price_channel_position_anchlo_100d_base_v039_signal, "closeadj", "low"),
    _e(f02pc_f02_price_channel_position_decay_50d_base_v040_signal, "closeadj", "high"),
    _e(f02pc_f02_price_channel_position_vwapchpos_30d_base_v041_signal, "closeadj", "high", "low", "volume"),
    _e(f02pc_f02_price_channel_position_volbrk_40d_base_v042_signal, "closeadj", "high", "volume"),
    _e(f02pc_f02_price_channel_position_posrk_120d_base_v043_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_posstd_60d_base_v044_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_posskew_90d_base_v045_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_zscpos_50d_base_v046_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_nearedge_30d_base_v047_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_posagree_60d_base_v048_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_tanhdt_25d_base_v049_signal, "close", "high", "low"),
    _e(f02pc_f02_price_channel_position_diffpos_50d_base_v050_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_diffdt_100d_base_v051_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_midcross_60d_base_v052_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_topcnt_40d_base_v053_signal, "closeadj", "high"),
    _e(f02pc_f02_price_channel_position_hirk_100d_base_v054_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_lork_60d_base_v055_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_chacc_50d_base_v056_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_widacc_30d_base_v057_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_ulpos_20d_base_v058_signal, "close", "high", "low"),
    _e(f02pc_f02_price_channel_position_uppos_30d_base_v059_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_atrwid_20d_base_v060_signal, "close", "high", "low"),
    _e(f02pc_f02_price_channel_position_atrposd_30d_base_v061_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_newhicnt_50d_base_v062_signal, "closeadj", "high"),
    _e(f02pc_f02_price_channel_position_newlocnt_30d_base_v063_signal, "closeadj", "low"),
    _e(f02pc_f02_price_channel_position_pierce_30d_base_v064_signal, "close", "high", "low"),
    _e(f02pc_f02_price_channel_position_pierce_100d_base_v065_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_decayrt_70d_base_v066_signal, "closeadj", "high"),
    _e(f02pc_f02_price_channel_position_hivol_60d_base_v067_signal, "closeadj", "high"),
    _e(f02pc_f02_price_channel_position_lovol_90d_base_v068_signal, "closeadj", "low"),
    _e(f02pc_f02_price_channel_position_posac1_60d_base_v069_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_hiprgr_30d_base_v070_signal, "closeadj", "high"),
    _e(f02pc_f02_price_channel_position_loprgr_30d_base_v071_signal, "closeadj", "low"),
    _e(f02pc_f02_price_channel_position_pkfill_30d_base_v072_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_pivpos_50d_base_v073_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_hlrk_80d_base_v074_signal, "closeadj", "high", "low"),
    _e(f02pc_f02_price_channel_position_regpos_150d_base_v075_signal, "closeadj", "high", "low"),
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
    for name, entry in f02_price_channel_position_base_001_075_REGISTRY.items():
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
    print(f"OK base_001_075: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
