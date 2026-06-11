"""f20_volatility_compression_expansion base features 001-075.

Domain: volatility COMPRESSION (squeeze, low-vol-building) vs EXPANSION
(release, high-vol-following). Distinct from f17 (regime LEVEL) by focus on
TRANSITION DIRECTION. Distinct from f18 (specific estimators) and f19
(ATR-normalized price). Features here detect:
  - BB squeeze (BB inside Keltner) and squeeze breaks
  - BB width compression ratios vs trailing min/avg/max
  - ATR contraction (short/long ATR ratio, ATR streaks, percentile rank)
  - Range contraction (NR4, NR7, inside-bar streaks)
  - Vol direction (slope, curvature)
  - Compression / expansion magnitude (z-scores, surges, %B-of-width)
  - Cycle indicators (days since contraction / expansion)
  - Pre-breakout / post-break vol behavior
  - Multi-indicator agreement counts
  - Bounded transforms (arctan, tanh, sigmoid of squeeze indicators)
  - Compression-expansion oscillator (vol_long - vol_short normalized)
  - Vol regime transition events
  - Statistical compression (vol-of-vol percentile rank)

NaN policy: never fillna(<value>); only replace([inf,-inf],nan) at the
final return. Window > 21d uses closeadj; <= 21d uses close. Intra-bar
ohlc uses unadjusted high/low/open/close.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers (each feature still spells the formula inline)
# ---------------------------------------------------------------------------


def _sma(s, n):
    return s.rolling(n, min_periods=n).mean()


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _std(s, n):
    return s.rolling(n, min_periods=n).std(ddof=0)


def _tr(high, low, close):
    pc = close.shift(1)
    return pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n):
    return _tr(high, low, close).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()


def _atr_sma(high, low, close, n):
    return _tr(high, low, close).rolling(n, min_periods=n).mean()


def _rank_pct(s, n):
    """Percentile rank of last value within rolling window of length n in [0,1]."""
    return s.rolling(n, min_periods=n).apply(
        lambda x: float((x < x[-1]).sum()) / float(len(x) - 1) if len(x) > 1 else np.nan,
        raw=True,
    )


def _bb_width(s, n, k=2.0):
    m = s.rolling(n, min_periods=n).mean()
    sd = s.rolling(n, min_periods=n).std(ddof=0)
    return (2.0 * k * sd) / m.replace(0.0, np.nan)


def _streak_days_since(cond):
    """Days since last True in the boolean condition series."""
    out = pd.Series(np.nan, index=cond.index, dtype=float)
    cnt = np.nan
    vals = cond.values
    for i in range(len(cond)):
        v = vals[i]
        if not np.isfinite(float(v if isinstance(v, (bool, np.bool_)) else v)):
            out.iat[i] = cnt
            continue
        if bool(v):
            cnt = 0.0
        elif np.isfinite(cnt):
            cnt = cnt + 1.0
        out.iat[i] = cnt
    return out


def _consec_streak(cond):
    """Length of current consecutive run of True at each index."""
    out = pd.Series(np.nan, index=cond.index, dtype=float)
    cnt = 0.0
    started = False
    vals = cond.values
    for i in range(len(cond)):
        v = vals[i]
        if not started and not bool(v):
            # have not yet seen first valid - keep NaN
            if cond.index[i] >= 0:
                started = True
        else:
            started = True
        if bool(v):
            cnt += 1.0
        else:
            cnt = 0.0
        out.iat[i] = cnt
    return out


# ---------------------------------------------------------------------------
# Features 001-075
# ---------------------------------------------------------------------------


# === BB squeeze (BB inside Keltner) + squeeze break signals ================


def f20ce_f20_volatility_compression_expansion_bb_in_kc_20d_base_v001_signal(high, low, close):
    """Binary: BB inside Keltner Channels at window 20. Classic TTM Squeeze."""
    n = 20
    mid = close.rolling(n, min_periods=n).mean()
    sd = close.rolling(n, min_periods=n).std(ddof=0)
    bb_up = mid + 2.0 * sd
    bb_lo = mid - 2.0 * sd
    atr = _tr(high, low, close).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    kc_up = mid + 1.5 * atr
    kc_lo = mid - 1.5 * atr
    sq = ((bb_up < kc_up) & (bb_lo > kc_lo)).astype(float)
    return sq.where(~mid.isna() & ~atr.isna()).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_bb_in_kc_streak_50d_base_v002_signal(high, low, closeadj):
    """Consecutive days of BB-in-KC squeeze at window 30 (mid-term compression).
    Uses BB std multiplier 1.5 and KC ATR multiplier 1.0 to produce active streaks
    in moderate-vol regimes."""
    n = 30
    mid = closeadj.rolling(n, min_periods=n).mean()
    sd = closeadj.rolling(n, min_periods=n).std(ddof=0)
    bb_up = mid + 1.5 * sd
    bb_lo = mid - 1.5 * sd
    atr = _tr(high, low, closeadj).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    kc_up = mid + 1.0 * atr
    kc_lo = mid - 1.0 * atr
    sq = ((bb_up < kc_up) & (bb_lo > kc_lo)).astype(float).where(~mid.isna() & ~atr.isna())
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cnt = 0.0
    for i in range(len(sq)):
        v = sq.iat[i]
        if not np.isfinite(v):
            out.iat[i] = np.nan
            continue
        if v > 0.5:
            cnt += 1.0
        else:
            cnt = 0.0
        out.iat[i] = cnt
    return out.where(out.notna()).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_squeeze_break_20d_base_v003_signal(high, low, close):
    """Squeeze break event: prior bar was BB-in-KC, current bar is not. Binary signed
    by sign(close - mid): release-up = +1, release-down = -1, no-event = 0."""
    n = 20
    mid = close.rolling(n, min_periods=n).mean()
    sd = close.rolling(n, min_periods=n).std(ddof=0)
    bb_up = mid + 2.0 * sd
    bb_lo = mid - 2.0 * sd
    atr = _tr(high, low, close).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    kc_up = mid + 1.5 * atr
    kc_lo = mid - 1.5 * atr
    sq = ((bb_up < kc_up) & (bb_lo > kc_lo)).astype(float).where(~mid.isna() & ~atr.isna())
    just_broke = (sq.shift(1) > 0.5) & (sq < 0.5)
    direction = np.sign(close - mid)
    return (just_broke.astype(float) * direction).where(~mid.isna()).replace([np.inf, -np.inf], np.nan)


# === BB width compression / expansion ratios ===============================


def f20ce_f20_volatility_compression_expansion_bbw_div_min_60d_base_v004_signal(closeadj):
    """BB(20)-width divided by its trailing-60d MIN. ~1.0 = at compression floor."""
    n = 20
    m = closeadj.rolling(n, min_periods=n).mean()
    sd = closeadj.rolling(n, min_periods=n).std(ddof=0)
    bbw = (4.0 * sd) / m.replace(0.0, np.nan)
    mn = bbw.rolling(60, min_periods=30).min()
    return (bbw / mn.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_bbw_div_max_60d_base_v005_signal(closeadj):
    """BB(20)-width divided by its trailing-60d MAX. ~1.0 = at expansion ceiling."""
    n = 20
    m = closeadj.rolling(n, min_periods=n).mean()
    sd = closeadj.rolling(n, min_periods=n).std(ddof=0)
    bbw = (4.0 * sd) / m.replace(0.0, np.nan)
    mx = bbw.rolling(60, min_periods=30).max()
    return (bbw / mx.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_bbw_rank_120d_base_v006_signal(closeadj):
    """Percentile rank of BB(20)-width over trailing 120d. Low = compression."""
    n = 20
    m = closeadj.rolling(n, min_periods=n).mean()
    sd = closeadj.rolling(n, min_periods=n).std(ddof=0)
    bbw = (4.0 * sd) / m.replace(0.0, np.nan)
    return bbw.rolling(120, min_periods=60).apply(
        lambda x: float((x < x[-1]).sum()) / float(len(x) - 1) if len(x) > 1 else np.nan,
        raw=True,
    ).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_bbw_rel_avg_252d_base_v007_signal(closeadj):
    """BB(40)-width / trailing 252d AVG BB-width - 1. Negative = compressed."""
    n = 40
    m = closeadj.rolling(n, min_periods=n).mean()
    sd = closeadj.rolling(n, min_periods=n).std(ddof=0)
    bbw = (4.0 * sd) / m.replace(0.0, np.nan)
    avg = bbw.rolling(252, min_periods=120).mean()
    return (bbw / avg.replace(0.0, np.nan) - 1.0).replace([np.inf, -np.inf], np.nan)


# === ATR contraction / expansion ============================================


def f20ce_f20_volatility_compression_expansion_atr_short_long_ratio_5_20_base_v008_signal(high, low, close):
    """ATR(5) / ATR(20). < 1 = short-term contraction, > 1 = expansion."""
    a5 = _tr(high, low, close).ewm(alpha=1.0 / 5.0, adjust=False, min_periods=5).mean()
    a20 = _tr(high, low, close).ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    return (a5 / a20.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_atr_short_long_ratio_10_50_base_v009_signal(high, low, closeadj):
    """ATR(10) / ATR(50). Mid-horizon contraction/expansion ratio."""
    a10 = _tr(high, low, closeadj).ewm(alpha=1.0 / 10.0, adjust=False, min_periods=10).mean()
    a50 = _tr(high, low, closeadj).ewm(alpha=1.0 / 50.0, adjust=False, min_periods=50).mean()
    return (a10 / a50.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_atr_rank_100d_base_v010_signal(high, low, closeadj):
    """Percentile rank of ATR(14) over 100d. Low = compression, high = expansion."""
    atr = _tr(high, low, closeadj).ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    return atr.rolling(100, min_periods=50).apply(
        lambda x: float((x < x[-1]).sum()) / float(len(x) - 1) if len(x) > 1 else np.nan,
        raw=True,
    ).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_atr_decline_streak_20d_base_v011_signal(high, low, close):
    """Consecutive days ATR(14) is declining (sign(ATR.diff) < 0). Compression streak."""
    atr = _tr(high, low, close).ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    cond = (atr.diff() < 0.0).astype(float).where(~atr.diff().isna())
    out = pd.Series(np.nan, index=close.index, dtype=float)
    cnt = 0.0
    valid = False
    for i in range(len(cond)):
        v = cond.iat[i]
        if not np.isfinite(v):
            out.iat[i] = np.nan
            continue
        valid = True
        if v > 0.5:
            cnt += 1.0
        else:
            cnt = 0.0
        out.iat[i] = cnt
    return out.where(out.notna()).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_atr_rise_streak_20d_base_v012_signal(high, low, close):
    """Consecutive days ATR(14) is rising. Expansion streak."""
    atr = _tr(high, low, close).ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    cond = (atr.diff() > 0.0).astype(float).where(~atr.diff().isna())
    out = pd.Series(np.nan, index=close.index, dtype=float)
    cnt = 0.0
    for i in range(len(cond)):
        v = cond.iat[i]
        if not np.isfinite(v):
            out.iat[i] = np.nan
            continue
        if v > 0.5:
            cnt += 1.0
        else:
            cnt = 0.0
        out.iat[i] = cnt
    return out.where(out.notna()).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_atr_pctile_low_signal_60d_base_v013_signal(high, low, closeadj):
    """Binary: ATR(20) below 25th percentile of its trailing 60d. Compression flag."""
    atr = _tr(high, low, closeadj).ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    q25 = atr.rolling(60, min_periods=30).quantile(0.25)
    sig = (atr < q25).astype(float).where(~atr.isna() & ~q25.isna())
    return sig.replace([np.inf, -np.inf], np.nan)


# === Range contraction (NR4 / NR7 / inside-bar) =============================


def f20ce_f20_volatility_compression_expansion_nr4_v014_signal(high, low):
    """NR4: today's high-low is the narrowest of last 4 bars. Binary squeeze marker."""
    rng = high - low
    mn = rng.rolling(4, min_periods=4).min()
    return (rng <= mn + 1e-12).astype(float).where(~mn.isna()).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_nr7_v015_signal(high, low):
    """NR7: today's range is narrowest of last 7 bars. Stronger compression marker."""
    rng = high - low
    mn = rng.rolling(7, min_periods=7).min()
    return (rng <= mn + 1e-12).astype(float).where(~mn.isna()).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_inside_bar_streak_v016_signal(high, low):
    """Consecutive inside-bar count (today high<prev high AND today low>prev low).
    Coiling pattern, building compression."""
    cond = (high < high.shift(1)) & (low > low.shift(1))
    cond_f = cond.astype(float).where(~high.shift(1).isna())
    out = pd.Series(np.nan, index=high.index, dtype=float)
    cnt = 0.0
    for i in range(len(cond_f)):
        v = cond_f.iat[i]
        if not np.isfinite(v):
            out.iat[i] = np.nan
            continue
        if v > 0.5:
            cnt += 1.0
        else:
            cnt = 0.0
        out.iat[i] = cnt
    return out.where(out.notna()).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_outside_bar_streak_v017_signal(high, low):
    """Outside-bar streak (today high>prev AND low<prev). Aggressive expansion sign."""
    cond = (high > high.shift(1)) & (low < low.shift(1))
    cond_f = cond.astype(float).where(~high.shift(1).isna())
    out = pd.Series(np.nan, index=high.index, dtype=float)
    cnt = 0.0
    for i in range(len(cond_f)):
        v = cond_f.iat[i]
        if not np.isfinite(v):
            out.iat[i] = np.nan
            continue
        if v > 0.5:
            cnt += 1.0
        else:
            cnt = 0.0
        out.iat[i] = cnt
    return out.where(out.notna()).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_range_rank_50d_v018_signal(high, low):
    """Pctile rank of (high - low) over trailing 50d. Low = compressed today."""
    rng = high - low
    return rng.rolling(50, min_periods=25).apply(
        lambda x: float((x < x[-1]).sum()) / float(len(x) - 1) if len(x) > 1 else np.nan,
        raw=True,
    ).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_inside_bar_count_30d_v019_signal(high, low):
    """Number of inside bars in trailing 30d. High count = sustained compression."""
    cond = ((high < high.shift(1)) & (low > low.shift(1))).astype(float).where(~high.shift(1).isna())
    return cond.rolling(30, min_periods=20).sum().replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_wide_range_count_30d_v020_signal(high, low, close):
    """Count of bars where range > 1.5x ATR(14) over trailing 30d. Expansion bursts."""
    rng = high - low
    atr = _tr(high, low, close).ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    wide = (rng > 1.5 * atr).astype(float).where(~atr.isna())
    return wide.rolling(30, min_periods=20).sum().replace([np.inf, -np.inf], np.nan)


# === Vol direction (slope of vol, curvature) ================================


def f20ce_f20_volatility_compression_expansion_vol20_slope_sign_v021_signal(close):
    """sign(d/dt vol(20)). +1 = expanding, -1 = compressing. Discrete."""
    v = close.pct_change().rolling(20, min_periods=20).std(ddof=0)
    return np.sign(v.diff(5)).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_vol60_slope_sign_v022_signal(closeadj):
    """sign(d/dt vol(60)). Long-horizon discrete vol direction."""
    v = closeadj.pct_change().rolling(60, min_periods=60).std(ddof=0)
    return np.sign(v.diff(21)).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_vol_curvature_30d_v023_signal(closeadj):
    """2nd derivative (curvature) of vol(30): v - 2*v.shift(10) + v.shift(20).
    Positive = decelerating compression, negative = accelerating compression."""
    v = closeadj.pct_change().rolling(30, min_periods=30).std(ddof=0)
    return (v - 2.0 * v.shift(10) + v.shift(20)).replace([np.inf, -np.inf], np.nan)


# === Compression magnitude (vol distance from min) ==========================


def f20ce_f20_volatility_compression_expansion_vol_minmax_norm_60d_v024_signal(closeadj):
    """(vol(20) - min60) / (max60 - min60). 0 = compressed, 1 = expanded."""
    v = closeadj.pct_change().rolling(20, min_periods=20).std(ddof=0)
    mn = v.rolling(60, min_periods=30).min()
    mx = v.rolling(60, min_periods=30).max()
    return ((v - mn) / (mx - mn).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_vol_zscore_120d_v025_signal(closeadj):
    """z-score of vol(40) against trailing 120d mean/std. Negative = compressed."""
    v = closeadj.pct_change().rolling(40, min_periods=40).std(ddof=0)
    mu = v.rolling(120, min_periods=60).mean()
    sd = v.rolling(120, min_periods=60).std(ddof=0)
    return ((v - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_vol_z_below_neg1_flag_v026_signal(closeadj):
    """Binary: vol(30) z-score below -1 vs trailing 100d. Strong compression flag."""
    v = closeadj.pct_change().rolling(30, min_periods=30).std(ddof=0)
    mu = v.rolling(100, min_periods=50).mean()
    sd = v.rolling(100, min_periods=50).std(ddof=0)
    z = (v - mu) / sd.replace(0.0, np.nan)
    return (z < -1.0).astype(float).where(~z.isna()).replace([np.inf, -np.inf], np.nan)


# === Expansion magnitude ====================================================


def f20ce_f20_volatility_compression_expansion_vol_surge_5_60_v027_signal(close):
    """vol(5) / SMA(vol(5), 60) - 1. Short-term vol surge vs its own avg."""
    v = close.pct_change().rolling(5, min_periods=5).std(ddof=0)
    avg = v.rolling(60, min_periods=30).mean()
    return (v / avg.replace(0.0, np.nan) - 1.0).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_vol_above_1p5x_trailing_30d_v028_signal(closeadj):
    """Binary: vol(10) > 1.5x SMA(vol(10), 30). Aggressive expansion event."""
    v = closeadj.pct_change().rolling(10, min_periods=10).std(ddof=0)
    avg = v.rolling(30, min_periods=15).mean()
    return (v > 1.5 * avg).astype(float).where(~avg.isna()).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_vol_z_above_1_flag_v029_signal(closeadj):
    """Binary: vol(20) z-score > 1 vs trailing 80d. Expansion flag."""
    v = closeadj.pct_change().rolling(20, min_periods=20).std(ddof=0)
    mu = v.rolling(80, min_periods=40).mean()
    sd = v.rolling(80, min_periods=40).std(ddof=0)
    z = (v - mu) / sd.replace(0.0, np.nan)
    return (z > 1.0).astype(float).where(~z.isna()).replace([np.inf, -np.inf], np.nan)


# === Cycle indicators (days-since compression / expansion) =================


def f20ce_f20_volatility_compression_expansion_days_since_squeeze_60d_v030_signal(high, low, closeadj):
    """Days since last BB-in-KC squeeze event (window 20)."""
    n = 20
    mid = closeadj.rolling(n, min_periods=n).mean()
    sd = closeadj.rolling(n, min_periods=n).std(ddof=0)
    bb_up = mid + 2.0 * sd
    bb_lo = mid - 2.0 * sd
    atr = _tr(high, low, closeadj).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    kc_up = mid + 1.5 * atr
    kc_lo = mid - 1.5 * atr
    sq = ((bb_up < kc_up) & (bb_lo > kc_lo)).where(~mid.isna() & ~atr.isna())
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cnt = np.nan
    for i in range(len(sq)):
        v = sq.iat[i]
        if pd.isna(v):
            out.iat[i] = cnt
            continue
        if bool(v):
            cnt = 0.0
        elif np.isfinite(cnt):
            cnt = cnt + 1.0
        out.iat[i] = cnt
    return out.clip(upper=60.0).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_days_since_expansion_60d_v031_signal(high, low, closeadj):
    """Days since last bar with range > 1.5*ATR(20). Time since explosive event."""
    rng = high - low
    atr = _tr(high, low, closeadj).ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    cond = (rng > 1.5 * atr).where(~atr.isna())
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cnt = np.nan
    for i in range(len(cond)):
        v = cond.iat[i]
        if pd.isna(v):
            out.iat[i] = cnt
            continue
        if bool(v):
            cnt = 0.0
        elif np.isfinite(cnt):
            cnt = cnt + 1.0
        out.iat[i] = cnt
    return out.clip(upper=60.0).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_compression_streak_30d_v032_signal(closeadj):
    """Consecutive days vol(20) below its 60d median. Sustained low-vol streak."""
    v = closeadj.pct_change().rolling(20, min_periods=20).std(ddof=0)
    med = v.rolling(60, min_periods=30).median()
    cond = (v < med).astype(float).where(~med.isna())
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cnt = 0.0
    for i in range(len(cond)):
        x = cond.iat[i]
        if not np.isfinite(x):
            out.iat[i] = np.nan
            continue
        if x > 0.5:
            cnt += 1.0
        else:
            cnt = 0.0
        out.iat[i] = cnt
    return out.where(out.notna()).replace([np.inf, -np.inf], np.nan)


# === Post-break vol behavior ================================================


def f20ce_f20_volatility_compression_expansion_post_break_expansion_mag_v033_signal(high, low, close):
    """ATR(14)/ATR(14).shift(5) - 1 expansion magnitude, smoothed by EMA(5) to
    emphasize sustained post-break expansion phases. NaN preserved through warmup."""
    atr14 = _tr(high, low, close).ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    raw = (atr14 / atr14.shift(5).replace(0.0, np.nan)) - 1.0
    return raw.ewm(span=5, adjust=False, min_periods=5).mean().replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_failed_breakout_count_60d_v034_signal(high, low, close):
    """Count over trailing 60d of bars where the BB-in-KC squeeze state returned
    after exiting in the prior 10 bars (failed breakout count). Uses past-only
    references; never fills NaN, only masks invalid rows."""
    n = 20
    mid = close.rolling(n, min_periods=n).mean()
    sd = close.rolling(n, min_periods=n).std(ddof=0)
    bb_up = mid + 2.0 * sd
    bb_lo = mid - 2.0 * sd
    atr20 = _tr(high, low, close).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    kc_up = mid + 1.5 * atr20
    kc_lo = mid - 1.5 * atr20
    sq = ((bb_up < kc_up) & (bb_lo > kc_lo)).astype(float).where(~mid.isna() & ~atr20.isna())
    # Today's bar is a "return to squeeze" event: yesterday not-in-squeeze, today in-squeeze.
    returned = ((sq.shift(1) < 0.5) & (sq > 0.5)).astype(float).where(~sq.shift(1).isna())
    # Within the last 10 bars (excluding today), was there a "break out" event?
    broke = ((sq.shift(1) > 0.5) & (sq < 0.5)).astype(float).where(~sq.shift(1).isna())
    broke10 = broke.shift(1).rolling(10, min_periods=5).sum()
    failed = (returned * (broke10 > 0.5).astype(float)).where(~broke10.isna())
    return failed.rolling(60, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


# === Multi-indicator agreement counts =======================================


def f20ce_f20_volatility_compression_expansion_agree_compression_count_v035_signal(high, low, closeadj):
    """Count of compression indicators currently TRUE: BB-in-KC, ATR(5)/ATR(20)<1,
    NR4, vol(20) z<0 vs 60d. Range 0..4."""
    n = 20
    mid = closeadj.rolling(n, min_periods=n).mean()
    sd = closeadj.rolling(n, min_periods=n).std(ddof=0)
    bb_up = mid + 2.0 * sd
    bb_lo = mid - 2.0 * sd
    atr20 = _tr(high, low, closeadj).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    kc_up = mid + 1.5 * atr20
    kc_lo = mid - 1.5 * atr20
    sq = ((bb_up < kc_up) & (bb_lo > kc_lo)).astype(float)
    a5 = _tr(high, low, closeadj).ewm(alpha=1.0 / 5.0, adjust=False, min_periods=5).mean()
    a20 = atr20
    short_long = (a5 < a20).astype(float)
    rng = high - low
    nr4 = (rng <= rng.rolling(4, min_periods=4).min() + 1e-12).astype(float)
    v = closeadj.pct_change().rolling(20, min_periods=20).std(ddof=0)
    mu = v.rolling(60, min_periods=30).mean()
    sd2 = v.rolling(60, min_periods=30).std(ddof=0)
    z = (v - mu) / sd2.replace(0.0, np.nan)
    vol_low = (z < 0.0).astype(float)
    total = sq + short_long + nr4 + vol_low
    return total.where(~mid.isna() & ~sd2.isna()).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_agree_expansion_count_v036_signal(high, low, closeadj):
    """Count of expansion indicators TRUE: BB-out-KC, ATR(5)/ATR(20)>1.2,
    range>1.5*ATR, vol(20) z>0. Range 0..4."""
    n = 20
    mid = closeadj.rolling(n, min_periods=n).mean()
    sd = closeadj.rolling(n, min_periods=n).std(ddof=0)
    bb_up = mid + 2.0 * sd
    bb_lo = mid - 2.0 * sd
    atr20 = _tr(high, low, closeadj).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    kc_up = mid + 1.5 * atr20
    kc_lo = mid - 1.5 * atr20
    not_sq = (~((bb_up < kc_up) & (bb_lo > kc_lo))).astype(float)
    a5 = _tr(high, low, closeadj).ewm(alpha=1.0 / 5.0, adjust=False, min_periods=5).mean()
    short_long = (a5 > 1.2 * atr20).astype(float)
    rng = high - low
    wide = (rng > 1.5 * atr20).astype(float)
    v = closeadj.pct_change().rolling(20, min_periods=20).std(ddof=0)
    mu = v.rolling(60, min_periods=30).mean()
    sd2 = v.rolling(60, min_periods=30).std(ddof=0)
    z = (v - mu) / sd2.replace(0.0, np.nan)
    vol_high = (z > 0.0).astype(float)
    total = not_sq + short_long + wide + vol_high
    return total.where(~mid.isna() & ~sd2.isna()).replace([np.inf, -np.inf], np.nan)


# === Volume confirmation of vol regime ======================================


def f20ce_f20_volatility_compression_expansion_vol_during_contraction_v037_signal(closeadj, volume):
    """Avg log(volume) during last 20d when vol(10) was below its 30d median minus
    avg log(volume) during last 20d when vol was above. Negative = quiet compression."""
    v = closeadj.pct_change().rolling(10, min_periods=10).std(ddof=0)
    med = v.rolling(30, min_periods=15).median()
    low_mask = (v < med).astype(float).where(~med.isna())
    high_mask = (v > med).astype(float).where(~med.isna())
    logv = np.log(volume.replace(0.0, np.nan))
    avg_low = (logv * low_mask).rolling(20, min_periods=10).sum() / low_mask.rolling(20, min_periods=10).sum().replace(0.0, np.nan)
    avg_high = (logv * high_mask).rolling(20, min_periods=10).sum() / high_mask.rolling(20, min_periods=10).sum().replace(0.0, np.nan)
    return (avg_low - avg_high).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_volume_zscore_during_squeeze_v038_signal(high, low, closeadj, volume):
    """Volume z-score (vs trailing 60d) on bars currently within BB-in-KC squeeze;
    NaN otherwise. Tests "quiet during compression" hypothesis."""
    n = 20
    mid = closeadj.rolling(n, min_periods=n).mean()
    sd = closeadj.rolling(n, min_periods=n).std(ddof=0)
    bb_up = mid + 2.0 * sd
    bb_lo = mid - 2.0 * sd
    atr = _tr(high, low, closeadj).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    kc_up = mid + 1.5 * atr
    kc_lo = mid - 1.5 * atr
    sq = ((bb_up < kc_up) & (bb_lo > kc_lo))
    vmu = volume.rolling(60, min_periods=30).mean()
    vsd = volume.rolling(60, min_periods=30).std(ddof=0)
    z = (volume - vmu) / vsd.replace(0.0, np.nan)
    return z.where(sq).replace([np.inf, -np.inf], np.nan)


# === Bounded transforms (arctan, tanh, sigmoid of squeeze metrics) =========


def f20ce_f20_volatility_compression_expansion_arctan_bbw_60d_v039_signal(closeadj):
    """arctan( BB(30)-width / 60d-min BB-width - 1 ). Bounded compression signal."""
    n = 30
    m = closeadj.rolling(n, min_periods=n).mean()
    sd = closeadj.rolling(n, min_periods=n).std(ddof=0)
    bbw = (4.0 * sd) / m.replace(0.0, np.nan)
    mn = bbw.rolling(60, min_periods=30).min()
    return np.arctan(bbw / mn.replace(0.0, np.nan) - 1.0).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_tanh_volz_60d_v040_signal(closeadj):
    """tanh of vol(30) z-score vs trailing 60d. Bounded compression/expansion sig."""
    v = closeadj.pct_change().rolling(30, min_periods=30).std(ddof=0)
    mu = v.rolling(60, min_periods=30).mean()
    sd = v.rolling(60, min_periods=30).std(ddof=0)
    z = (v - mu) / sd.replace(0.0, np.nan)
    return np.tanh(z).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_sigmoid_bbw_diff_v041_signal(closeadj):
    """sigmoid( z-score of (BBW(20) - BBW(50)) over 100d ). Bounded compression
    differential between short- and long-window BB widths."""
    n1, n2 = 20, 50
    m1 = closeadj.rolling(n1, min_periods=n1).mean()
    s1 = closeadj.rolling(n1, min_periods=n1).std(ddof=0)
    bbw1 = (4.0 * s1) / m1.replace(0.0, np.nan)
    m2 = closeadj.rolling(n2, min_periods=n2).mean()
    s2 = closeadj.rolling(n2, min_periods=n2).std(ddof=0)
    bbw2 = (4.0 * s2) / m2.replace(0.0, np.nan)
    d = bbw1 - bbw2
    mu = d.rolling(100, min_periods=50).mean()
    sd = d.rolling(100, min_periods=50).std(ddof=0)
    z = (d - mu) / sd.replace(0.0, np.nan)
    out = 1.0 / (1.0 + np.exp(-z))
    return out.replace([np.inf, -np.inf], np.nan)


# === Compression-expansion oscillator =======================================


def f20ce_f20_volatility_compression_expansion_oscillator_vol_long_short_v042_signal(closeadj):
    """(vol(60) - vol(10)) / vol(60). >0 when long-vol > short-vol (compressing)."""
    vs = closeadj.pct_change().rolling(10, min_periods=10).std(ddof=0)
    vl = closeadj.pct_change().rolling(60, min_periods=60).std(ddof=0)
    return ((vl - vs) / vl.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_squeeze_minus_expand_v043_signal(high, low, closeadj):
    """squeeze_signal - expand_signal: BB-in-KC binary minus range>1.5*ATR binary."""
    n = 20
    mid = closeadj.rolling(n, min_periods=n).mean()
    sd = closeadj.rolling(n, min_periods=n).std(ddof=0)
    bb_up = mid + 2.0 * sd
    bb_lo = mid - 2.0 * sd
    atr = _tr(high, low, closeadj).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    kc_up = mid + 1.5 * atr
    kc_lo = mid - 1.5 * atr
    sq = ((bb_up < kc_up) & (bb_lo > kc_lo)).astype(float)
    rng = high - low
    expand = (rng > 1.5 * atr).astype(float)
    return (sq - expand).where(~mid.isna() & ~atr.isna()).replace([np.inf, -np.inf], np.nan)


# === Vol regime transitions =================================================


def f20ce_f20_volatility_compression_expansion_transition_event_signed_v044_signal(closeadj):
    """Signed transition: +1 when entering expansion (vol(20) crosses median from
    below), -1 when entering compression (crosses median from above), else 0."""
    v = closeadj.pct_change().rolling(20, min_periods=20).std(ddof=0)
    med = v.rolling(60, min_periods=30).median()
    above = (v > med).astype(float).where(~med.isna())
    diff = above - above.shift(1)
    return diff.where(~above.shift(1).isna()).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_transition_count_120d_v045_signal(closeadj):
    """Count of vol regime transitions (above/below 60d median) in trailing 120d."""
    v = closeadj.pct_change().rolling(20, min_periods=20).std(ddof=0)
    med = v.rolling(60, min_periods=30).median()
    above = (v > med).astype(float).where(~med.isna())
    flips = (above != above.shift(1)).astype(float).where(~above.shift(1).isna() & ~above.isna())
    return flips.rolling(120, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


# === Statistical compression detection ======================================


def f20ce_f20_volatility_compression_expansion_variance_of_vol_60d_v046_signal(closeadj):
    """Variance of vol(10) over trailing 60d. Low value => vol is stable (compressed)."""
    v = closeadj.pct_change().rolling(10, min_periods=10).std(ddof=0)
    return v.rolling(60, min_periods=30).var(ddof=0).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_vol_of_vol_rank_120d_v047_signal(closeadj):
    """Percentile rank of vol-of-vol(20) over trailing 120d. Low => stable vol."""
    v = closeadj.pct_change().rolling(20, min_periods=20).std(ddof=0)
    vov = v.rolling(20, min_periods=20).std(ddof=0)
    return vov.rolling(120, min_periods=60).apply(
        lambda x: float((x < x[-1]).sum()) / float(len(x) - 1) if len(x) > 1 else np.nan,
        raw=True,
    ).replace([np.inf, -np.inf], np.nan)


# === Squeeze duration before break ==========================================


def f20ce_f20_volatility_compression_expansion_squeeze_duration_pre_break_v048_signal(high, low, closeadj):
    """Duration of the most recent squeeze episode that has just ended.
    On break event: emit length of prior consecutive squeeze run. Else carry forward."""
    n = 20
    mid = closeadj.rolling(n, min_periods=n).mean()
    sd = closeadj.rolling(n, min_periods=n).std(ddof=0)
    bb_up = mid + 2.0 * sd
    bb_lo = mid - 2.0 * sd
    atr = _tr(high, low, closeadj).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    kc_up = mid + 1.5 * atr
    kc_lo = mid - 1.5 * atr
    sq = ((bb_up < kc_up) & (bb_lo > kc_lo)).astype(float).where(~mid.isna() & ~atr.isna())
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cur = 0.0
    last_dur = np.nan
    for i in range(len(sq)):
        v = sq.iat[i]
        if not np.isfinite(v):
            out.iat[i] = np.nan
            continue
        if v > 0.5:
            cur += 1.0
        else:
            if cur > 0.0:
                last_dur = cur
            cur = 0.0
        out.iat[i] = last_dur
    return out.replace([np.inf, -np.inf], np.nan)


# === Width-based stochastic ================================================


def f20ce_f20_volatility_compression_expansion_bbw_acceleration_norm_v049_signal(closeadj):
    """Normalized BBW(25) acceleration: 2nd derivative / SMA(|BBW|, 50).
    Distinct from sign-of-acceleration (v066) by being a continuous magnitude."""
    n = 25
    m = closeadj.rolling(n, min_periods=n).mean()
    sd = closeadj.rolling(n, min_periods=n).std(ddof=0)
    bbw = (4.0 * sd) / m.replace(0.0, np.nan)
    accel = bbw - 2.0 * bbw.shift(5) + bbw.shift(10)
    norm = bbw.abs().rolling(50, min_periods=25).mean()
    return (accel / norm.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ATR / range ratio variants =============================================


def f20ce_f20_volatility_compression_expansion_atr_to_close_arctan_v050_signal(high, low, closeadj):
    """arctan( log(ATR(20) / SMA(ATR(20), 100)) ). Bounded long-vs-short ATR ratio."""
    atr = _tr(high, low, closeadj).ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    atr_avg = atr.rolling(100, min_periods=50).mean()
    return np.arctan(np.log(atr / atr_avg.replace(0.0, np.nan))).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_range_atr_ratio_5_v051_signal(high, low, close):
    """range(today) / ATR(5). Short-horizon expansion magnitude (>1 = wide)."""
    rng = high - low
    a5 = _tr(high, low, close).ewm(alpha=1.0 / 5.0, adjust=False, min_periods=5).mean()
    return (rng / a5.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Kurtosis of returns (regime descriptor) ===============================


def f20ce_f20_volatility_compression_expansion_return_abs_skew_50d_v052_signal(closeadj):
    """Skewness of |returns| over 50d. High = recent expansion shock."""
    r = closeadj.pct_change().abs()
    return r.rolling(50, min_periods=25).skew().replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_return_abs_kurt_80d_v053_signal(closeadj):
    """Excess kurtosis of |returns| over 80d. High = fat-tailed expansion regime."""
    r = closeadj.pct_change().abs()
    return r.rolling(80, min_periods=40).kurt().replace([np.inf, -np.inf], np.nan)


# === Average true range slope, true range vs SMA ============================


def f20ce_f20_volatility_compression_expansion_tr_above_atr_freq_30d_v054_signal(high, low, close):
    """Fraction of last 30 bars where TR > ATR(14). High = sustained expansion."""
    atr = _tr(high, low, close).ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    tr = _tr(high, low, close)
    flag = (tr > atr).astype(float).where(~atr.isna())
    return flag.rolling(30, min_periods=15).mean().replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_atr_normalized_change_v055_signal(high, low, closeadj):
    """(ATR(20) - ATR(20).shift(10)) / ATR(20).shift(10). Pct change in ATR."""
    atr = _tr(high, low, closeadj).ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    return ((atr - atr.shift(10)) / atr.shift(10).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Vol of vol (vol stability indicator) ===================================


def f20ce_f20_volatility_compression_expansion_volofvol_div_vol_60d_v056_signal(closeadj):
    """vol-of-vol(20) / vol(20). Normalized vol-of-vol; low = stable compression."""
    v = closeadj.pct_change().rolling(20, min_periods=20).std(ddof=0)
    vov = v.rolling(20, min_periods=20).std(ddof=0)
    return (vov / v.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Donchian-style range compression =======================================


def f20ce_f20_volatility_compression_expansion_donch_width_rank_50d_v057_signal(high, low):
    """Percentile rank of Donchian(20) width over 50d. Low = squeezing channel."""
    hh = high.rolling(20, min_periods=20).max()
    ll = low.rolling(20, min_periods=20).min()
    w = hh - ll
    return w.rolling(50, min_periods=25).apply(
        lambda x: float((x < x[-1]).sum()) / float(len(x) - 1) if len(x) > 1 else np.nan,
        raw=True,
    ).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_donch_width_div_avg_100d_v058_signal(high, low):
    """Donchian(40) width divided by 100d-avg Donchian-width."""
    hh = high.rolling(40, min_periods=40).max()
    ll = low.rolling(40, min_periods=40).min()
    w = hh - ll
    avg = w.rolling(100, min_periods=50).mean()
    return (w / avg.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Close-to-close vs high-low ratio (signal of intraday vs overnight) ====


def f20ce_f20_volatility_compression_expansion_c2c_vs_hl_ratio_30d_v059_signal(high, low, closeadj):
    """SMA(close-to-close abs returns, 30) / SMA(high-low range / closeadj, 30) - 1.
    Detects compression bias toward intraday vs C2C."""
    c2c = closeadj.pct_change().abs()
    hl = (high - low) / closeadj.replace(0.0, np.nan)
    return (c2c.rolling(30, min_periods=15).mean() / hl.rolling(30, min_periods=15).mean().replace(0.0, np.nan) - 1.0).replace([np.inf, -np.inf], np.nan)


# === Body-based compression =================================================


def f20ce_f20_volatility_compression_expansion_body_size_rank_50d_v060_signal(open_, closeadj):
    """Pctile rank of |close - open| / close over 50d. Low = small body = compressed."""
    body = (closeadj - open_).abs() / closeadj.replace(0.0, np.nan)
    return body.rolling(50, min_periods=25).apply(
        lambda x: float((x < x[-1]).sum()) / float(len(x) - 1) if len(x) > 1 else np.nan,
        raw=True,
    ).replace([np.inf, -np.inf], np.nan)


# === Compressed-then-expanded composite ====================================


def f20ce_f20_volatility_compression_expansion_compress_then_expand_v061_signal(high, low, closeadj):
    """ATR(5)/ATR(40) MINUS its trailing 20d-min. >0 indicates fresh expansion after
    a period of compression. Detects transition phase."""
    a5 = _tr(high, low, closeadj).ewm(alpha=1.0 / 5.0, adjust=False, min_periods=5).mean()
    a40 = _tr(high, low, closeadj).ewm(alpha=1.0 / 40.0, adjust=False, min_periods=40).mean()
    r = a5 / a40.replace(0.0, np.nan)
    mn = r.rolling(20, min_periods=10).min()
    return (r - mn).replace([np.inf, -np.inf], np.nan)


# === Range expansion vs prior squeeze depth ================================


def f20ce_f20_volatility_compression_expansion_range_vs_recent_min_30d_v062_signal(high, low):
    """(today range - 30d-min range) / 30d-min range. Spike above zero = expansion."""
    rng = high - low
    mn = rng.rolling(30, min_periods=15).min()
    return ((rng - mn) / mn.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Hi-lo ratio compression (Mass Index style) ============================


def f20ce_f20_volatility_compression_expansion_mass_index_25d_v063_signal(high, low):
    """Sum over 25d of EMA(H-L, 9) / EMA(EMA(H-L, 9), 9). Mass Index proxy.
    High value = expansion; falling = compression."""
    hl = high - low
    e1 = hl.ewm(span=9, adjust=False, min_periods=9).mean()
    e2 = e1.ewm(span=9, adjust=False, min_periods=9).mean()
    return (e1 / e2.replace(0.0, np.nan)).rolling(25, min_periods=15).sum().replace([np.inf, -np.inf], np.nan)


# === Chaikin Volatility ====================================================


def f20ce_f20_volatility_compression_expansion_chaikin_vol_10_v064_signal(high, low):
    """Chaikin Volatility: (EMA(H-L,10) / EMA(H-L,10).shift(10) - 1) * 100.
    Positive = expansion, negative = compression."""
    hl = high - low
    e = hl.ewm(span=10, adjust=False, min_periods=10).mean()
    return ((e / e.shift(10).replace(0.0, np.nan)) - 1.0).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_chaikin_vol_30_v065_signal(high, low):
    """Chaikin Volatility(30): longer-horizon vol pct change."""
    hl = high - low
    e = hl.ewm(span=30, adjust=False, min_periods=30).mean()
    return ((e / e.shift(30).replace(0.0, np.nan)) - 1.0).replace([np.inf, -np.inf], np.nan)


# === Sign-of-acceleration of BB-width ======================================


def f20ce_f20_volatility_compression_expansion_bbw_acceleration_sign_v066_signal(closeadj):
    """sign( BBW(30) - 2*BBW(30).shift(10) + BBW(30).shift(20) ). Discrete jerk sign."""
    n = 30
    m = closeadj.rolling(n, min_periods=n).mean()
    sd = closeadj.rolling(n, min_periods=n).std(ddof=0)
    bbw = (4.0 * sd) / m.replace(0.0, np.nan)
    return np.sign(bbw - 2.0 * bbw.shift(10) + bbw.shift(20)).replace([np.inf, -np.inf], np.nan)


# === Disagreement between compression indicators ===========================


def f20ce_f20_volatility_compression_expansion_disagreement_count_v067_signal(high, low, closeadj):
    """ABS( compression_count - expansion_count ) inverted. High = agreement,
    Low = mixed regime. Compute as 4 - |comp - exp| with both in [0,4].
    Tests transition zone where indicators disagree."""
    n = 20
    mid = closeadj.rolling(n, min_periods=n).mean()
    sd = closeadj.rolling(n, min_periods=n).std(ddof=0)
    bb_up = mid + 2.0 * sd
    bb_lo = mid - 2.0 * sd
    atr20 = _tr(high, low, closeadj).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    kc_up = mid + 1.5 * atr20
    kc_lo = mid - 1.5 * atr20
    sq = ((bb_up < kc_up) & (bb_lo > kc_lo)).astype(float)
    a5 = _tr(high, low, closeadj).ewm(alpha=1.0 / 5.0, adjust=False, min_periods=5).mean()
    short_long_lt = (a5 < atr20).astype(float)
    short_long_gt = (a5 > 1.2 * atr20).astype(float)
    rng = high - low
    nr4 = (rng <= rng.rolling(4, min_periods=4).min() + 1e-12).astype(float)
    wide = (rng > 1.5 * atr20).astype(float)
    comp = sq + short_long_lt + nr4
    exp = (1.0 - sq) + short_long_gt + wide
    out = (comp - exp).abs()
    return out.where(~mid.isna() & ~atr20.isna()).replace([np.inf, -np.inf], np.nan)


# === Coil score: count of consecutive narrow-then-narrower ratios ==========


def f20ce_f20_volatility_compression_expansion_coil_score_v068_signal(high, low):
    """Coil score: number of consecutive days where today range < yesterday range
    over a max-5-bar window. Tightening coil."""
    rng = high - low
    smaller = (rng < rng.shift(1)).astype(float).where(~rng.shift(1).isna())
    return smaller.rolling(5, min_periods=5).sum().replace([np.inf, -np.inf], np.nan)


# === Vol regime persistence (Hurst-like) ===================================


def f20ce_f20_volatility_compression_expansion_vol_autocorr_30d_v069_signal(closeadj):
    """Lag-1 autocorrelation of vol(10) over trailing 30d. High = persistent regime."""
    v = closeadj.pct_change().rolling(10, min_periods=10).std(ddof=0)
    return v.rolling(30, min_periods=20).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if len(x) > 2 else np.nan,
        raw=True,
    ).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_range_autocorr_50d_v070_signal(high, low):
    """Lag-1 autocorr of (high - low) over 50d. High = persistent range regime."""
    rng = high - low
    return rng.rolling(50, min_periods=30).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if len(x) > 2 else np.nan,
        raw=True,
    ).replace([np.inf, -np.inf], np.nan)


# === Compression rate of change ============================================


def f20ce_f20_volatility_compression_expansion_compression_roc_30d_v071_signal(closeadj):
    """Rate of change in compression: BB(20)-width / BB(20)-width.shift(30) - 1.
    Negative = compressing; positive = expanding."""
    n = 20
    m = closeadj.rolling(n, min_periods=n).mean()
    sd = closeadj.rolling(n, min_periods=n).std(ddof=0)
    bbw = (4.0 * sd) / m.replace(0.0, np.nan)
    return (bbw / bbw.shift(30).replace(0.0, np.nan) - 1.0).replace([np.inf, -np.inf], np.nan)


# === IQR-of-returns compression =============================================


def f20ce_f20_volatility_compression_expansion_iqr_returns_rank_80d_v072_signal(closeadj):
    """Pctile rank of IQR-of-returns(20) over 80d. Low = compressed return spread."""
    r = closeadj.pct_change()
    q75 = r.rolling(20, min_periods=20).quantile(0.75)
    q25 = r.rolling(20, min_periods=20).quantile(0.25)
    iqr = q75 - q25
    return iqr.rolling(80, min_periods=40).apply(
        lambda x: float((x < x[-1]).sum()) / float(len(x) - 1) if len(x) > 1 else np.nan,
        raw=True,
    ).replace([np.inf, -np.inf], np.nan)


# === MAD-based compression =================================================


def f20ce_f20_volatility_compression_expansion_mad_returns_div_avg_v073_signal(closeadj):
    """MAD(returns, 30) / SMA(MAD(returns, 30), 100). >1 = expansion, <1 = compression."""
    r = closeadj.pct_change()
    mad = r.rolling(30, min_periods=30).apply(lambda x: float(np.mean(np.abs(x - np.mean(x)))), raw=True)
    avg = mad.rolling(100, min_periods=50).mean()
    return (mad / avg.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume-vol divergence =================================================


def f20ce_f20_volatility_compression_expansion_volume_vol_corr_60d_v074_signal(closeadj, volume):
    """60d corr between log-volume and abs-returns. Positive => vol moves with volume."""
    r = closeadj.pct_change().abs()
    lv = np.log(volume.replace(0.0, np.nan))
    return r.rolling(60, min_periods=30).corr(lv).replace([np.inf, -np.inf], np.nan)


# === Spike count (extreme expansion) =======================================


def f20ce_f20_volatility_compression_expansion_spike_count_60d_v075_signal(closeadj):
    """Count of days in trailing 60d where |return| > 3 * vol(20). Spike count."""
    r = closeadj.pct_change()
    v = r.rolling(20, min_periods=20).std(ddof=0)
    flag = (r.abs() > 3.0 * v).astype(float).where(~v.isna())
    return flag.rolling(60, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f20_volatility_compression_expansion_base_001_075_REGISTRY = {
    "f20ce_f20_volatility_compression_expansion_bb_in_kc_20d_base_v001_signal": {"inputs": ["high", "low", "close"], "func": f20ce_f20_volatility_compression_expansion_bb_in_kc_20d_base_v001_signal},
    "f20ce_f20_volatility_compression_expansion_bb_in_kc_streak_50d_base_v002_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_bb_in_kc_streak_50d_base_v002_signal},
    "f20ce_f20_volatility_compression_expansion_squeeze_break_20d_base_v003_signal": {"inputs": ["high", "low", "close"], "func": f20ce_f20_volatility_compression_expansion_squeeze_break_20d_base_v003_signal},
    "f20ce_f20_volatility_compression_expansion_bbw_div_min_60d_base_v004_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_bbw_div_min_60d_base_v004_signal},
    "f20ce_f20_volatility_compression_expansion_bbw_div_max_60d_base_v005_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_bbw_div_max_60d_base_v005_signal},
    "f20ce_f20_volatility_compression_expansion_bbw_rank_120d_base_v006_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_bbw_rank_120d_base_v006_signal},
    "f20ce_f20_volatility_compression_expansion_bbw_rel_avg_252d_base_v007_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_bbw_rel_avg_252d_base_v007_signal},
    "f20ce_f20_volatility_compression_expansion_atr_short_long_ratio_5_20_base_v008_signal": {"inputs": ["high", "low", "close"], "func": f20ce_f20_volatility_compression_expansion_atr_short_long_ratio_5_20_base_v008_signal},
    "f20ce_f20_volatility_compression_expansion_atr_short_long_ratio_10_50_base_v009_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_atr_short_long_ratio_10_50_base_v009_signal},
    "f20ce_f20_volatility_compression_expansion_atr_rank_100d_base_v010_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_atr_rank_100d_base_v010_signal},
    "f20ce_f20_volatility_compression_expansion_atr_decline_streak_20d_base_v011_signal": {"inputs": ["high", "low", "close"], "func": f20ce_f20_volatility_compression_expansion_atr_decline_streak_20d_base_v011_signal},
    "f20ce_f20_volatility_compression_expansion_atr_rise_streak_20d_base_v012_signal": {"inputs": ["high", "low", "close"], "func": f20ce_f20_volatility_compression_expansion_atr_rise_streak_20d_base_v012_signal},
    "f20ce_f20_volatility_compression_expansion_atr_pctile_low_signal_60d_base_v013_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_atr_pctile_low_signal_60d_base_v013_signal},
    "f20ce_f20_volatility_compression_expansion_nr4_v014_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_nr4_v014_signal},
    "f20ce_f20_volatility_compression_expansion_nr7_v015_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_nr7_v015_signal},
    "f20ce_f20_volatility_compression_expansion_inside_bar_streak_v016_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_inside_bar_streak_v016_signal},
    "f20ce_f20_volatility_compression_expansion_outside_bar_streak_v017_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_outside_bar_streak_v017_signal},
    "f20ce_f20_volatility_compression_expansion_range_rank_50d_v018_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_range_rank_50d_v018_signal},
    "f20ce_f20_volatility_compression_expansion_inside_bar_count_30d_v019_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_inside_bar_count_30d_v019_signal},
    "f20ce_f20_volatility_compression_expansion_wide_range_count_30d_v020_signal": {"inputs": ["high", "low", "close"], "func": f20ce_f20_volatility_compression_expansion_wide_range_count_30d_v020_signal},
    "f20ce_f20_volatility_compression_expansion_vol20_slope_sign_v021_signal": {"inputs": ["close"], "func": f20ce_f20_volatility_compression_expansion_vol20_slope_sign_v021_signal},
    "f20ce_f20_volatility_compression_expansion_vol60_slope_sign_v022_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol60_slope_sign_v022_signal},
    "f20ce_f20_volatility_compression_expansion_vol_curvature_30d_v023_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol_curvature_30d_v023_signal},
    "f20ce_f20_volatility_compression_expansion_vol_minmax_norm_60d_v024_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol_minmax_norm_60d_v024_signal},
    "f20ce_f20_volatility_compression_expansion_vol_zscore_120d_v025_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol_zscore_120d_v025_signal},
    "f20ce_f20_volatility_compression_expansion_vol_z_below_neg1_flag_v026_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol_z_below_neg1_flag_v026_signal},
    "f20ce_f20_volatility_compression_expansion_vol_surge_5_60_v027_signal": {"inputs": ["close"], "func": f20ce_f20_volatility_compression_expansion_vol_surge_5_60_v027_signal},
    "f20ce_f20_volatility_compression_expansion_vol_above_1p5x_trailing_30d_v028_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol_above_1p5x_trailing_30d_v028_signal},
    "f20ce_f20_volatility_compression_expansion_vol_z_above_1_flag_v029_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol_z_above_1_flag_v029_signal},
    "f20ce_f20_volatility_compression_expansion_days_since_squeeze_60d_v030_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_days_since_squeeze_60d_v030_signal},
    "f20ce_f20_volatility_compression_expansion_days_since_expansion_60d_v031_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_days_since_expansion_60d_v031_signal},
    "f20ce_f20_volatility_compression_expansion_compression_streak_30d_v032_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_compression_streak_30d_v032_signal},
    "f20ce_f20_volatility_compression_expansion_post_break_expansion_mag_v033_signal": {"inputs": ["high", "low", "close"], "func": f20ce_f20_volatility_compression_expansion_post_break_expansion_mag_v033_signal},
    "f20ce_f20_volatility_compression_expansion_failed_breakout_count_60d_v034_signal": {"inputs": ["high", "low", "close"], "func": f20ce_f20_volatility_compression_expansion_failed_breakout_count_60d_v034_signal},
    "f20ce_f20_volatility_compression_expansion_agree_compression_count_v035_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_agree_compression_count_v035_signal},
    "f20ce_f20_volatility_compression_expansion_agree_expansion_count_v036_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_agree_expansion_count_v036_signal},
    "f20ce_f20_volatility_compression_expansion_vol_during_contraction_v037_signal": {"inputs": ["closeadj", "volume"], "func": f20ce_f20_volatility_compression_expansion_vol_during_contraction_v037_signal},
    "f20ce_f20_volatility_compression_expansion_volume_zscore_during_squeeze_v038_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f20ce_f20_volatility_compression_expansion_volume_zscore_during_squeeze_v038_signal},
    "f20ce_f20_volatility_compression_expansion_arctan_bbw_60d_v039_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_arctan_bbw_60d_v039_signal},
    "f20ce_f20_volatility_compression_expansion_tanh_volz_60d_v040_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_tanh_volz_60d_v040_signal},
    "f20ce_f20_volatility_compression_expansion_sigmoid_bbw_diff_v041_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_sigmoid_bbw_diff_v041_signal},
    "f20ce_f20_volatility_compression_expansion_oscillator_vol_long_short_v042_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_oscillator_vol_long_short_v042_signal},
    "f20ce_f20_volatility_compression_expansion_squeeze_minus_expand_v043_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_squeeze_minus_expand_v043_signal},
    "f20ce_f20_volatility_compression_expansion_transition_event_signed_v044_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_transition_event_signed_v044_signal},
    "f20ce_f20_volatility_compression_expansion_transition_count_120d_v045_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_transition_count_120d_v045_signal},
    "f20ce_f20_volatility_compression_expansion_variance_of_vol_60d_v046_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_variance_of_vol_60d_v046_signal},
    "f20ce_f20_volatility_compression_expansion_vol_of_vol_rank_120d_v047_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol_of_vol_rank_120d_v047_signal},
    "f20ce_f20_volatility_compression_expansion_squeeze_duration_pre_break_v048_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_squeeze_duration_pre_break_v048_signal},
    "f20ce_f20_volatility_compression_expansion_bbw_acceleration_norm_v049_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_bbw_acceleration_norm_v049_signal},
    "f20ce_f20_volatility_compression_expansion_atr_to_close_arctan_v050_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_atr_to_close_arctan_v050_signal},
    "f20ce_f20_volatility_compression_expansion_range_atr_ratio_5_v051_signal": {"inputs": ["high", "low", "close"], "func": f20ce_f20_volatility_compression_expansion_range_atr_ratio_5_v051_signal},
    "f20ce_f20_volatility_compression_expansion_return_abs_skew_50d_v052_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_return_abs_skew_50d_v052_signal},
    "f20ce_f20_volatility_compression_expansion_return_abs_kurt_80d_v053_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_return_abs_kurt_80d_v053_signal},
    "f20ce_f20_volatility_compression_expansion_tr_above_atr_freq_30d_v054_signal": {"inputs": ["high", "low", "close"], "func": f20ce_f20_volatility_compression_expansion_tr_above_atr_freq_30d_v054_signal},
    "f20ce_f20_volatility_compression_expansion_atr_normalized_change_v055_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_atr_normalized_change_v055_signal},
    "f20ce_f20_volatility_compression_expansion_volofvol_div_vol_60d_v056_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_volofvol_div_vol_60d_v056_signal},
    "f20ce_f20_volatility_compression_expansion_donch_width_rank_50d_v057_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_donch_width_rank_50d_v057_signal},
    "f20ce_f20_volatility_compression_expansion_donch_width_div_avg_100d_v058_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_donch_width_div_avg_100d_v058_signal},
    "f20ce_f20_volatility_compression_expansion_c2c_vs_hl_ratio_30d_v059_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_c2c_vs_hl_ratio_30d_v059_signal},
    "f20ce_f20_volatility_compression_expansion_body_size_rank_50d_v060_signal": {"inputs": ["open", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_body_size_rank_50d_v060_signal},
    "f20ce_f20_volatility_compression_expansion_compress_then_expand_v061_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_compress_then_expand_v061_signal},
    "f20ce_f20_volatility_compression_expansion_range_vs_recent_min_30d_v062_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_range_vs_recent_min_30d_v062_signal},
    "f20ce_f20_volatility_compression_expansion_mass_index_25d_v063_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_mass_index_25d_v063_signal},
    "f20ce_f20_volatility_compression_expansion_chaikin_vol_10_v064_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_chaikin_vol_10_v064_signal},
    "f20ce_f20_volatility_compression_expansion_chaikin_vol_30_v065_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_chaikin_vol_30_v065_signal},
    "f20ce_f20_volatility_compression_expansion_bbw_acceleration_sign_v066_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_bbw_acceleration_sign_v066_signal},
    "f20ce_f20_volatility_compression_expansion_disagreement_count_v067_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_disagreement_count_v067_signal},
    "f20ce_f20_volatility_compression_expansion_coil_score_v068_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_coil_score_v068_signal},
    "f20ce_f20_volatility_compression_expansion_vol_autocorr_30d_v069_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol_autocorr_30d_v069_signal},
    "f20ce_f20_volatility_compression_expansion_range_autocorr_50d_v070_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_range_autocorr_50d_v070_signal},
    "f20ce_f20_volatility_compression_expansion_compression_roc_30d_v071_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_compression_roc_30d_v071_signal},
    "f20ce_f20_volatility_compression_expansion_iqr_returns_rank_80d_v072_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_iqr_returns_rank_80d_v072_signal},
    "f20ce_f20_volatility_compression_expansion_mad_returns_div_avg_v073_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_mad_returns_div_avg_v073_signal},
    "f20ce_f20_volatility_compression_expansion_volume_vol_corr_60d_v074_signal": {"inputs": ["closeadj", "volume"], "func": f20ce_f20_volatility_compression_expansion_volume_vol_corr_60d_v074_signal},
    "f20ce_f20_volatility_compression_expansion_spike_count_60d_v075_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_spike_count_60d_v075_signal},
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
    for name, entry in f20_volatility_compression_expansion_base_001_075_REGISTRY.items():
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
