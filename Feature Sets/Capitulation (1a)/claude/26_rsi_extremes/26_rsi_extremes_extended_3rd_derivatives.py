"""
26_rsi_extremes — Extended 3rd Derivatives (Features rsi_extdrv3_001-025)
Domain: rate of change of extended 2nd-derivative RSI features — acceleration of velocity
        (slope-of-slope / second-diff) capturing exhaustion and inflection of extended
        RSI oversold measures including VRSI, weighted-close, confluence, z-score variants
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rsi(close: pd.Series, period: int) -> pd.Series:
    """Wilder smoothed RSI for a given lookback period."""
    delta = close.diff(1)
    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)
    avg_gain = gain.ewm(alpha=1.0 / period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1.0 / period, min_periods=period, adjust=False).mean()
    rs = _safe_div(avg_gain, avg_loss)
    return 100.0 - 100.0 / (1.0 + rs)


def _vrsi(close: pd.Series, volume: pd.Series, period: int) -> pd.Series:
    """Volume-weighted RSI: gains/losses weighted by volume before smoothing."""
    delta = close.diff(1)
    gain = delta.clip(lower=0.0) * volume
    loss = (-delta).clip(lower=0.0) * volume
    avg_gain = gain.ewm(alpha=1.0 / period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1.0 / period, min_periods=period, adjust=False).mean()
    rs = _safe_div(avg_gain, avg_loss)
    return 100.0 - 100.0 / (1.0 + rs)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── Extended 3rd-Derivative Feature Functions ─────────────────────────────────
# Each feature applies a second diff / slope-of-slope / diff-of-slope to an
# extended-2nd-derivative concept, capturing inflection and exhaustion.

# --- Group A (001-005): Acceleration of additional Wilder RSI velocity ---

def rsi_extdrv3_001_rsi10_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of RSI10 (acceleration of 10-day RSI velocity)."""
    vel = _rsi(close, 10).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rsi_extdrv3_002_rsi12_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of RSI12 (acceleration of 12-day RSI velocity)."""
    vel = _rsi(close, 12).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rsi_extdrv3_003_rsi45_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of RSI45 (acceleration of 45-day RSI velocity)."""
    vel = _rsi(close, 45).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rsi_extdrv3_004_rsi180_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of RSI180 (jerk in semi-annual RSI)."""
    vel21 = _rsi(close, 180).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rsi_extdrv3_005_rsi252_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of RSI252 (jerk in annual RSI)."""
    vel21 = _rsi(close, _TD_YEAR).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


# --- Group B (006-008): Acceleration of oversold depth velocity ---

def rsi_extdrv3_006_rsi10_depth_below30_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of RSI10 depth below 30 (jerk in 10-day oversold depth)."""
    depth = (30.0 - _rsi(close, 10)).clip(lower=0.0)
    vel = depth.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rsi_extdrv3_007_rsi14_depth_below25_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of RSI14 depth below 25 (acceleration of deeper oversold depth)."""
    depth = (25.0 - _rsi(close, 14)).clip(lower=0.0)
    vel = depth.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rsi_extdrv3_008_rsi14_depth_below15_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of RSI14 depth below 15 (jerk in severe capitulation depth)."""
    depth = (15.0 - _rsi(close, 14)).clip(lower=0.0)
    vel = depth.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group C (009-011): Acceleration of consecutive-day streak velocity ---

def rsi_extdrv3_009_consec_rsi14_below25_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive-RSI14-below-25 streak (streak jerk)."""
    streak = _consec_streak(_rsi(close, 14) < 25.0)
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rsi_extdrv3_010_consec_rsi21_below20_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive-RSI21-below-20 streak acceleration."""
    streak = _consec_streak(_rsi(close, _TD_MON) < 20.0)
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rsi_extdrv3_011_consec_rsi7_below15_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive-RSI7-below-15 streak (fast extreme jerk)."""
    streak = _consec_streak(_rsi(close, 7) < 15.0)
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group D (012-013): Acceleration of rolling minimum RSI velocity ---

def rsi_extdrv3_012_rsi10_min_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d minimum RSI10 (acceleration of trough shift)."""
    mn = _rolling_min(_rsi(close, 10), _TD_MON)
    vel = mn.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rsi_extdrv3_013_rsi21_min_21d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 21d-minimum RSI21."""
    mn = _rolling_min(_rsi(close, _TD_MON), _TD_MON)
    vel = mn.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


# --- Group E (014-015): Acceleration of percentile-rank velocity ---

def rsi_extdrv3_014_rsi14_pct_rank_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of RSI14 21d percentile rank (jerk in rank velocity)."""
    r = _rsi(close, 14)
    pct = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)
    vel = pct.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rsi_extdrv3_015_rsi7_pct_rank_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of RSI7 21d percentile rank acceleration."""
    r = _rsi(close, 7)
    pct = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)
    vel = pct.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group F (016-017): Acceleration of z-score velocity ---

def rsi_extdrv3_016_rsi7_zscore_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of RSI7 z-score vs 63-day distribution (z-score jerk)."""
    r = _rsi(close, 7)
    m = _rolling_mean(r, _TD_QTR)
    s = _rolling_std(r, _TD_QTR)
    z = _safe_div(r - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rsi_extdrv3_017_rsi21_zscore_252d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of RSI21 z-score vs 252d."""
    r = _rsi(close, _TD_MON)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    z = _safe_div(r - m, s)
    vel = z.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


# --- Group G (018-019): Acceleration of VRSI velocity ---

def rsi_extdrv3_018_vrsi14_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of VRSI(14) (acceleration of volume-weighted RSI velocity)."""
    vel = _vrsi(close, volume, 14).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rsi_extdrv3_019_vrsi14_depth_below30_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of VRSI(14) depth below 30 (jerk in vol-weighted oversold depth)."""
    depth = (30.0 - _vrsi(close, volume, 14)).clip(lower=0.0)
    vel = depth.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group H (020-021): Acceleration of alternative price series RSI velocity ---

def rsi_extdrv3_020_rsi14_on_open_5d_diff_5d_diff(open: pd.Series) -> pd.Series:
    """Second 5-day diff of RSI14 on open prices (acceleration of open-series RSI)."""
    vel = _rsi(open, 14).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rsi_extdrv3_021_rsi14_weighted_close_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of RSI14 of weighted close (H+L+2*C)/4."""
    wc = (high + low + 2.0 * close) / 4.0
    vel = _rsi(wc, 14).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group I (022-023): Acceleration of cross-RSI confluence velocity ---

def rsi_extdrv3_022_confluence_count_below30_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of RSI confluence count below 30 (jerk in multi-RSI confluence)."""
    flags = [
        (_rsi(close, _TD_WEEK) < 30.0).astype(float),
        (_rsi(close, 10) < 30.0).astype(float),
        (_rsi(close, 14) < 30.0).astype(float),
        (_rsi(close, _TD_MON) < 30.0).astype(float),
        (_rsi(close, _TD_QTR) < 30.0).astype(float),
    ]
    conf = flags[0]
    for f in flags[1:]:
        conf = conf + f
    vel = conf.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rsi_extdrv3_023_confluence_depth_sum_5variants_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of sum-of-depths across 5 RSI variants (depth-sum jerk)."""
    depths = [
        (30.0 - _rsi(close, _TD_WEEK)).clip(lower=0.0),
        (30.0 - _rsi(close, 10)).clip(lower=0.0),
        (30.0 - _rsi(close, 14)).clip(lower=0.0),
        (30.0 - _rsi(close, _TD_MON)).clip(lower=0.0),
        (30.0 - _rsi(close, _TD_QTR)).clip(lower=0.0),
    ]
    total = depths[0]
    for d in depths[1:]:
        total = total + d
    vel = total.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group J (024-025): Acceleration of capitulation composite velocity ---

def rsi_extdrv3_024_rsi14_capitulation_composite_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of RSI14 capitulation composite score (composite jerk)."""
    r = _rsi(close, 14)
    depth = (30.0 - r).clip(lower=0.0) / 30.0
    pct_rank = r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    z = _safe_div(r - m, s).abs().clip(upper=3.0) / 3.0
    composite = depth + (1.0 - pct_rank.fillna(0.5)) + z
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rsi_extdrv3_025_rsi14_capitulation_composite_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of RSI14 capitulation composite
    (slope-of-slope of composite — exhaustion/inflection of capitulation acceleration)."""
    r = _rsi(close, 14)
    depth = (30.0 - r).clip(lower=0.0) / 30.0
    pct_rank = r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    z = _safe_div(r - m, s).abs().clip(upper=3.0) / 3.0
    composite = depth + (1.0 - pct_rank.fillna(0.5)) + z
    vel = composite.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

RSI_EXTREMES_EXTENDED_REGISTRY_3RD_DERIVATIVES = {
    "rsi_extdrv3_001_rsi10_5d_diff_5d_diff": {"inputs": ["close"], "func": rsi_extdrv3_001_rsi10_5d_diff_5d_diff},
    "rsi_extdrv3_002_rsi12_5d_diff_5d_diff": {"inputs": ["close"], "func": rsi_extdrv3_002_rsi12_5d_diff_5d_diff},
    "rsi_extdrv3_003_rsi45_5d_diff_5d_diff": {"inputs": ["close"], "func": rsi_extdrv3_003_rsi45_5d_diff_5d_diff},
    "rsi_extdrv3_004_rsi180_21d_diff_5d_diff": {"inputs": ["close"], "func": rsi_extdrv3_004_rsi180_21d_diff_5d_diff},
    "rsi_extdrv3_005_rsi252_21d_diff_5d_diff": {"inputs": ["close"], "func": rsi_extdrv3_005_rsi252_21d_diff_5d_diff},
    "rsi_extdrv3_006_rsi10_depth_below30_5d_diff_5d_diff": {"inputs": ["close"], "func": rsi_extdrv3_006_rsi10_depth_below30_5d_diff_5d_diff},
    "rsi_extdrv3_007_rsi14_depth_below25_5d_diff_5d_diff": {"inputs": ["close"], "func": rsi_extdrv3_007_rsi14_depth_below25_5d_diff_5d_diff},
    "rsi_extdrv3_008_rsi14_depth_below15_5d_diff_5d_diff": {"inputs": ["close"], "func": rsi_extdrv3_008_rsi14_depth_below15_5d_diff_5d_diff},
    "rsi_extdrv3_009_consec_rsi14_below25_5d_diff_5d_diff": {"inputs": ["close"], "func": rsi_extdrv3_009_consec_rsi14_below25_5d_diff_5d_diff},
    "rsi_extdrv3_010_consec_rsi21_below20_5d_diff_5d_diff": {"inputs": ["close"], "func": rsi_extdrv3_010_consec_rsi21_below20_5d_diff_5d_diff},
    "rsi_extdrv3_011_consec_rsi7_below15_5d_diff_5d_diff": {"inputs": ["close"], "func": rsi_extdrv3_011_consec_rsi7_below15_5d_diff_5d_diff},
    "rsi_extdrv3_012_rsi10_min_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": rsi_extdrv3_012_rsi10_min_21d_5d_diff_5d_diff},
    "rsi_extdrv3_013_rsi21_min_21d_slope_21d": {"inputs": ["close"], "func": rsi_extdrv3_013_rsi21_min_21d_slope_21d},
    "rsi_extdrv3_014_rsi14_pct_rank_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": rsi_extdrv3_014_rsi14_pct_rank_21d_5d_diff_5d_diff},
    "rsi_extdrv3_015_rsi7_pct_rank_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": rsi_extdrv3_015_rsi7_pct_rank_21d_5d_diff_5d_diff},
    "rsi_extdrv3_016_rsi7_zscore_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rsi_extdrv3_016_rsi7_zscore_63d_5d_diff_5d_diff},
    "rsi_extdrv3_017_rsi21_zscore_252d_5d_diff_slope_21d": {"inputs": ["close"], "func": rsi_extdrv3_017_rsi21_zscore_252d_5d_diff_slope_21d},
    "rsi_extdrv3_018_vrsi14_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": rsi_extdrv3_018_vrsi14_5d_diff_5d_diff},
    "rsi_extdrv3_019_vrsi14_depth_below30_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": rsi_extdrv3_019_vrsi14_depth_below30_5d_diff_5d_diff},
    "rsi_extdrv3_020_rsi14_on_open_5d_diff_5d_diff": {"inputs": ["open"], "func": rsi_extdrv3_020_rsi14_on_open_5d_diff_5d_diff},
    "rsi_extdrv3_021_rsi14_weighted_close_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rsi_extdrv3_021_rsi14_weighted_close_5d_diff_5d_diff},
    "rsi_extdrv3_022_confluence_count_below30_5d_diff_5d_diff": {"inputs": ["close"], "func": rsi_extdrv3_022_confluence_count_below30_5d_diff_5d_diff},
    "rsi_extdrv3_023_confluence_depth_sum_5variants_5d_diff_5d_diff": {"inputs": ["close"], "func": rsi_extdrv3_023_confluence_depth_sum_5variants_5d_diff_5d_diff},
    "rsi_extdrv3_024_rsi14_capitulation_composite_5d_diff_5d_diff": {"inputs": ["close"], "func": rsi_extdrv3_024_rsi14_capitulation_composite_5d_diff_5d_diff},
    "rsi_extdrv3_025_rsi14_capitulation_composite_5d_diff_slope_21d": {"inputs": ["close"], "func": rsi_extdrv3_025_rsi14_capitulation_composite_5d_diff_slope_21d},
}
