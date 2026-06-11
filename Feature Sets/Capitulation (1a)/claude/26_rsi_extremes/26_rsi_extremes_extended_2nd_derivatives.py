"""
26_rsi_extremes — Extended 2nd Derivatives (Features rsi_extdrv2_001-025)
Domain: rate of change of extended-base RSI features (ext_001-075) — velocity of extended
        RSI oversold measures including VRSI, weighted-close RSI, confluence, z-score,
        pct-rank, and rolling-min extended variants
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


def _rsi_sma(close: pd.Series, period: int) -> pd.Series:
    """Simple-average (Cutler) RSI for a given lookback."""
    delta = close.diff(1)
    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)
    avg_gain = _rolling_mean(gain, period)
    avg_loss = _rolling_mean(loss, period)
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


def _time_since_below(rsi_series: pd.Series, threshold: float) -> pd.Series:
    """Days elapsed since rsi_series was last below threshold (0 = currently below)."""
    below = (rsi_series < threshold).astype(float)
    idx = pd.Series(range(len(below)), index=below.index, dtype=float)
    last_idx = idx.where(below == 1.0).ffill().fillna(0.0)
    return (idx - last_idx).where(~rsi_series.isna(), np.nan)


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


# ── Extended 2nd-Derivative Feature Functions ─────────────────────────────────
# Each feature takes the velocity (diff/slope/pct_change) of an extended-base
# concept from 26_rsi_extremes_extended_001_075.py.

# --- Group A (001-005): Velocity of additional Wilder RSI lookback periods ---

def rsi_extdrv2_001_rsi10_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of RSI10 (velocity of the 10-day Wilder RSI)."""
    return _rsi(close, 10).diff(_TD_WEEK)


def rsi_extdrv2_002_rsi12_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of RSI12 (velocity of the 12-day Wilder RSI)."""
    return _rsi(close, 12).diff(_TD_WEEK)


def rsi_extdrv2_003_rsi45_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of RSI45 (velocity of the 45-day Wilder RSI)."""
    return _rsi(close, 45).diff(_TD_WEEK)


def rsi_extdrv2_004_rsi180_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of RSI180 (monthly velocity of the semi-annual RSI)."""
    return _rsi(close, 180).diff(_TD_MON)


def rsi_extdrv2_005_rsi252_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of RSI252 (monthly velocity of the annual-horizon RSI)."""
    return _rsi(close, _TD_YEAR).diff(_TD_MON)


# --- Group B (006-009): Velocity of oversold depth variants ---

def rsi_extdrv2_006_rsi10_depth_below30_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of RSI10 depth below 30 (how fast 10-day oversold depth is changing)."""
    depth = (30.0 - _rsi(close, 10)).clip(lower=0.0)
    return depth.diff(_TD_WEEK)


def rsi_extdrv2_007_rsi12_depth_below30_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of RSI12 depth below 30 (velocity of 12-day oversold depth)."""
    depth = (30.0 - _rsi(close, 12)).clip(lower=0.0)
    return depth.diff(_TD_WEEK)


def rsi_extdrv2_008_rsi14_depth_below25_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of RSI14 depth below 25 (velocity of deeper oversold threshold)."""
    depth = (25.0 - _rsi(close, 14)).clip(lower=0.0)
    return depth.diff(_TD_WEEK)


def rsi_extdrv2_009_rsi14_depth_below15_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of RSI14 depth below 15 (velocity of severe capitulation depth)."""
    depth = (15.0 - _rsi(close, 14)).clip(lower=0.0)
    return depth.diff(_TD_WEEK)


# --- Group C (010-012): Velocity of consecutive-day oversold streaks ---

def rsi_extdrv2_010_consec_rsi14_below25_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of consecutive-days RSI14 below 25 streak."""
    streak = _consec_streak(_rsi(close, 14) < 25.0)
    return streak.diff(_TD_WEEK)


def rsi_extdrv2_011_consec_rsi21_below20_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of consecutive-days RSI21 below 20 streak."""
    streak = _consec_streak(_rsi(close, _TD_MON) < 20.0)
    return streak.diff(_TD_WEEK)


def rsi_extdrv2_012_consec_rsi7_below15_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of consecutive-days RSI7 below 15 streak (fast extreme velocity)."""
    streak = _consec_streak(_rsi(close, 7) < 15.0)
    return streak.diff(_TD_WEEK)


# --- Group D (013-014): Velocity of rolling minimum RSI ---

def rsi_extdrv2_013_rsi10_min_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day minimum RSI10 (how fast the 21d trough is shifting)."""
    mn = _rolling_min(_rsi(close, 10), _TD_MON)
    return mn.diff(_TD_WEEK)


def rsi_extdrv2_014_rsi21_min_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day minimum RSI21."""
    mn = _rolling_min(_rsi(close, _TD_MON), _TD_MON)
    return mn.diff(_TD_WEEK)


# --- Group E (015-016): Velocity of percentile-rank measures ---

def rsi_extdrv2_015_rsi14_pct_rank_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of RSI14 percentile rank within trailing 21 days."""
    r = _rsi(close, 14)
    pct = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)
    return pct.diff(_TD_WEEK)


def rsi_extdrv2_016_rsi7_pct_rank_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of RSI7 percentile rank within trailing 21 days."""
    r = _rsi(close, 7)
    pct = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)
    return pct.diff(_TD_WEEK)


# --- Group F (017-018): Velocity of z-score variants ---

def rsi_extdrv2_017_rsi7_zscore_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of RSI7 z-score vs 63-day distribution (velocity of fast RSI z-score)."""
    r = _rsi(close, 7)
    m = _rolling_mean(r, _TD_QTR)
    s = _rolling_std(r, _TD_QTR)
    z = _safe_div(r - m, s)
    return z.diff(_TD_WEEK)


def rsi_extdrv2_018_rsi21_zscore_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of RSI21 z-score vs 252-day distribution."""
    r = _rsi(close, _TD_MON)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    z = _safe_div(r - m, s)
    return z.diff(_TD_WEEK)


# --- Group G (019-020): Velocity of VRSI (volume-weighted RSI) ---

def rsi_extdrv2_019_vrsi14_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of VRSI(14) — velocity of volume-weighted RSI14."""
    return _vrsi(close, volume, 14).diff(_TD_WEEK)


def rsi_extdrv2_020_vrsi14_depth_below30_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of VRSI(14) depth below 30 (deepening volume-weighted oversold)."""
    depth = (30.0 - _vrsi(close, volume, 14)).clip(lower=0.0)
    return depth.diff(_TD_WEEK)


# --- Group H (021-022): Velocity of RSI on alternative price series ---

def rsi_extdrv2_021_rsi14_on_open_5d_diff(open: pd.Series) -> pd.Series:
    """5-day diff of RSI14 computed on open prices."""
    return _rsi(open, 14).diff(_TD_WEEK)


def rsi_extdrv2_022_rsi14_weighted_close_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of RSI14 of weighted close (H+L+2*C)/4."""
    wc = (high + low + 2.0 * close) / 4.0
    return _rsi(wc, 14).diff(_TD_WEEK)


# --- Group I (023-024): Velocity of cross-RSI confluence ---

def rsi_extdrv2_023_confluence_count_below30_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of count of RSI variants simultaneously below 30 (velocity of confluence)."""
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
    return conf.diff(_TD_WEEK)


def rsi_extdrv2_024_confluence_depth_sum_5variants_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of sum-of-depths across RSI5/10/14/21/63 below 30."""
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
    return total.diff(_TD_WEEK)


# --- Group J (025): Velocity of capitulation composite ---

def rsi_extdrv2_025_rsi14_capitulation_composite_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the RSI14 capitulation composite score (velocity of overall distress)."""
    r = _rsi(close, 14)
    depth = (30.0 - r).clip(lower=0.0) / 30.0
    pct_rank = r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    z = _safe_div(r - m, s).abs().clip(upper=3.0) / 3.0
    composite = depth + (1.0 - pct_rank.fillna(0.5)) + z
    return composite.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

RSI_EXTREMES_EXTENDED_REGISTRY_2ND_DERIVATIVES = {
    "rsi_extdrv2_001_rsi10_5d_diff": {"inputs": ["close"], "func": rsi_extdrv2_001_rsi10_5d_diff},
    "rsi_extdrv2_002_rsi12_5d_diff": {"inputs": ["close"], "func": rsi_extdrv2_002_rsi12_5d_diff},
    "rsi_extdrv2_003_rsi45_5d_diff": {"inputs": ["close"], "func": rsi_extdrv2_003_rsi45_5d_diff},
    "rsi_extdrv2_004_rsi180_21d_diff": {"inputs": ["close"], "func": rsi_extdrv2_004_rsi180_21d_diff},
    "rsi_extdrv2_005_rsi252_21d_diff": {"inputs": ["close"], "func": rsi_extdrv2_005_rsi252_21d_diff},
    "rsi_extdrv2_006_rsi10_depth_below30_5d_diff": {"inputs": ["close"], "func": rsi_extdrv2_006_rsi10_depth_below30_5d_diff},
    "rsi_extdrv2_007_rsi12_depth_below30_5d_diff": {"inputs": ["close"], "func": rsi_extdrv2_007_rsi12_depth_below30_5d_diff},
    "rsi_extdrv2_008_rsi14_depth_below25_5d_diff": {"inputs": ["close"], "func": rsi_extdrv2_008_rsi14_depth_below25_5d_diff},
    "rsi_extdrv2_009_rsi14_depth_below15_5d_diff": {"inputs": ["close"], "func": rsi_extdrv2_009_rsi14_depth_below15_5d_diff},
    "rsi_extdrv2_010_consec_rsi14_below25_5d_diff": {"inputs": ["close"], "func": rsi_extdrv2_010_consec_rsi14_below25_5d_diff},
    "rsi_extdrv2_011_consec_rsi21_below20_5d_diff": {"inputs": ["close"], "func": rsi_extdrv2_011_consec_rsi21_below20_5d_diff},
    "rsi_extdrv2_012_consec_rsi7_below15_5d_diff": {"inputs": ["close"], "func": rsi_extdrv2_012_consec_rsi7_below15_5d_diff},
    "rsi_extdrv2_013_rsi10_min_21d_5d_diff": {"inputs": ["close"], "func": rsi_extdrv2_013_rsi10_min_21d_5d_diff},
    "rsi_extdrv2_014_rsi21_min_21d_5d_diff": {"inputs": ["close"], "func": rsi_extdrv2_014_rsi21_min_21d_5d_diff},
    "rsi_extdrv2_015_rsi14_pct_rank_21d_5d_diff": {"inputs": ["close"], "func": rsi_extdrv2_015_rsi14_pct_rank_21d_5d_diff},
    "rsi_extdrv2_016_rsi7_pct_rank_21d_5d_diff": {"inputs": ["close"], "func": rsi_extdrv2_016_rsi7_pct_rank_21d_5d_diff},
    "rsi_extdrv2_017_rsi7_zscore_63d_5d_diff": {"inputs": ["close"], "func": rsi_extdrv2_017_rsi7_zscore_63d_5d_diff},
    "rsi_extdrv2_018_rsi21_zscore_252d_5d_diff": {"inputs": ["close"], "func": rsi_extdrv2_018_rsi21_zscore_252d_5d_diff},
    "rsi_extdrv2_019_vrsi14_5d_diff": {"inputs": ["close", "volume"], "func": rsi_extdrv2_019_vrsi14_5d_diff},
    "rsi_extdrv2_020_vrsi14_depth_below30_5d_diff": {"inputs": ["close", "volume"], "func": rsi_extdrv2_020_vrsi14_depth_below30_5d_diff},
    "rsi_extdrv2_021_rsi14_on_open_5d_diff": {"inputs": ["open"], "func": rsi_extdrv2_021_rsi14_on_open_5d_diff},
    "rsi_extdrv2_022_rsi14_weighted_close_5d_diff": {"inputs": ["close", "high", "low"], "func": rsi_extdrv2_022_rsi14_weighted_close_5d_diff},
    "rsi_extdrv2_023_confluence_count_below30_5d_diff": {"inputs": ["close"], "func": rsi_extdrv2_023_confluence_count_below30_5d_diff},
    "rsi_extdrv2_024_confluence_depth_sum_5variants_5d_diff": {"inputs": ["close"], "func": rsi_extdrv2_024_confluence_depth_sum_5variants_5d_diff},
    "rsi_extdrv2_025_rsi14_capitulation_composite_5d_diff": {"inputs": ["close"], "func": rsi_extdrv2_025_rsi14_capitulation_composite_5d_diff},
}
