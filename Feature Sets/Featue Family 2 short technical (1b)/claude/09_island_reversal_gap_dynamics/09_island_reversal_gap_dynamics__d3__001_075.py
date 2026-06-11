"""island_reversal_gap_dynamics d3 features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py. Each feature
encodes a *different concept* in the gap / island-reversal theme: up-gap and
down-gap magnitudes in log/pct/ATR units, time-since-last-gap at multiple
severity tiers, counts and density over multiple windows, island patterns
(top/bottom, width, count), exhaustion / breakaway / runaway gap signatures,
unfilled-gap stacks and time-to-fill, gap fade / full-close reversal, and
two-gap / three-gap composite patterns.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family
imports.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


# ---------------------------- helpers ----------------------------

def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


# ---- family-specific helpers (PIT-clean) ----

def _up_gap_bool(high: pd.Series, low: pd.Series) -> pd.Series:
    """True when low[i] > high[i-1] (full up-gap)."""
    return low > high.shift(1)


def _down_gap_bool(high: pd.Series, low: pd.Series) -> pd.Series:
    """True when high[i] < low[i-1] (full down-gap)."""
    return high < low.shift(1)


def _up_gap_size(high: pd.Series, low: pd.Series) -> pd.Series:
    """Up-gap size in price units when up-gap, else NaN."""
    g = low - high.shift(1)
    return g.where(_up_gap_bool(high, low), np.nan)


def _down_gap_size(high: pd.Series, low: pd.Series) -> pd.Series:
    """Down-gap size in price units (positive value) when down-gap, else NaN."""
    g = low.shift(1) - high
    return g.where(_down_gap_bool(high, low), np.nan)


def _bars_since_event(event: pd.Series) -> pd.Series:
    """Bars since the most recent True in `event` (NaN before first event)."""
    idx_at_event = np.where(event.to_numpy(), np.arange(len(event)), np.nan)
    last_idx = pd.Series(idx_at_event, index=event.index).ffill()
    return pd.Series(np.arange(len(event), dtype=float), index=event.index) - last_idx


# ============================================================
# Bucket A — Magnitude of most-recent gap (001-009)
# ============================================================

def f09_irgd_001_log_up_gap_size_most_recent_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log-size of most-recent up-gap event in last 5 bars (low/high_prev). 0 if none."""
    log_g = _safe_log(low) - _safe_log(high.shift(1))
    log_g = log_g.where(_up_gap_bool(high, low), np.nan)
    return log_g.rolling(WDAYS, min_periods=1).max().fillna(0.0)


def f09_irgd_002_log_up_gap_size_most_recent_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log-size of most-recent up-gap in last 21 bars."""
    log_g = (_safe_log(low) - _safe_log(high.shift(1))).where(_up_gap_bool(high, low), np.nan)
    return log_g.rolling(MDAYS, min_periods=1).max().fillna(0.0)


def f09_irgd_003_log_up_gap_size_most_recent_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log-size of most-recent up-gap in last 63 bars."""
    log_g = (_safe_log(low) - _safe_log(high.shift(1))).where(_up_gap_bool(high, low), np.nan)
    return log_g.rolling(QDAYS, min_periods=1).max().fillna(0.0)


def f09_irgd_004_atr_up_gap_size_most_recent_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized largest up-gap size in last 5 bars."""
    g = _up_gap_size(high, low)
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(g, atr).rolling(WDAYS, min_periods=1).max().fillna(0.0)


def f09_irgd_005_atr_up_gap_size_most_recent_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized largest up-gap size in last 21 bars."""
    g = _up_gap_size(high, low)
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(g, atr).rolling(MDAYS, min_periods=1).max().fillna(0.0)


def f09_irgd_006_pct_up_gap_size_most_recent_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Raw % up-gap size: (low - high_prev) / high_prev — non-log normalization, recent-5d max."""
    g = _safe_div(_up_gap_size(high, low), high.shift(1))
    return g.rolling(WDAYS, min_periods=1).max().fillna(0.0)


def f09_irgd_007_log_down_gap_size_most_recent_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log-size of most-recent down-gap in last 5 bars (positive magnitude)."""
    log_g = (_safe_log(low.shift(1)) - _safe_log(high)).where(_down_gap_bool(high, low), np.nan)
    return log_g.rolling(WDAYS, min_periods=1).max().fillna(0.0)


def f09_irgd_008_atr_down_gap_size_most_recent_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized largest down-gap size in last 21 bars."""
    g = _down_gap_size(high, low)
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(g, atr).rolling(MDAYS, min_periods=1).max().fillna(0.0)


def f09_irgd_009_pct_down_gap_size_most_recent_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Raw % down-gap size in last 21 bars."""
    g = _safe_div(_down_gap_size(high, low), low.shift(1))
    return g.rolling(MDAYS, min_periods=1).max().fillna(0.0)


# ============================================================
# Bucket B — Bars-since-last-gap at multiple severity tiers (010-018)
# ============================================================

def f09_irgd_010_bars_since_last_up_gap_any(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since the most recent up-gap event of any size."""
    return _bars_since_event(_up_gap_bool(high, low).fillna(False))


def f09_irgd_011_bars_since_last_up_gap_gt_1atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent up-gap > 1 ATR — mild-severity tier."""
    atr = _atr(high, low, close, n=MDAYS)
    big = (_up_gap_size(high, low) > atr).fillna(False)
    return _bars_since_event(big)


def f09_irgd_012_bars_since_last_up_gap_gt_2atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent up-gap > 2 ATR — moderate-severity tier."""
    atr = _atr(high, low, close, n=MDAYS)
    big = (_up_gap_size(high, low) > 2.0 * atr).fillna(False)
    return _bars_since_event(big)


def f09_irgd_013_bars_since_last_up_gap_gt_3atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent up-gap > 3 ATR — extreme-severity tier."""
    atr = _atr(high, low, close, n=MDAYS)
    big = (_up_gap_size(high, low) > 3.0 * atr).fillna(False)
    return _bars_since_event(big)


def f09_irgd_014_bars_since_last_down_gap_any(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent down-gap of any size."""
    return _bars_since_event(_down_gap_bool(high, low).fillna(False))


def f09_irgd_015_bars_since_last_down_gap_gt_1atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent down-gap > 1 ATR."""
    atr = _atr(high, low, close, n=MDAYS)
    big = (_down_gap_size(high, low) > atr).fillna(False)
    return _bars_since_event(big)


def f09_irgd_016_bars_since_last_down_gap_gt_2atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent down-gap > 2 ATR."""
    atr = _atr(high, low, close, n=MDAYS)
    big = (_down_gap_size(high, low) > 2.0 * atr).fillna(False)
    return _bars_since_event(big)


def f09_irgd_017_bars_since_last_down_gap_gt_3atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent down-gap > 3 ATR."""
    atr = _atr(high, low, close, n=MDAYS)
    big = (_down_gap_size(high, low) > 3.0 * atr).fillna(False)
    return _bars_since_event(big)


def f09_irgd_018_bars_since_last_gap_either_direction(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since the most recent gap event of either direction."""
    either = (_up_gap_bool(high, low) | _down_gap_bool(high, low)).fillna(False)
    return _bars_since_event(either)


# ============================================================
# Bucket C — Counts of gaps in windows (019-027)
# ============================================================

def f09_irgd_019_count_up_gaps_in_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Number of up-gap days in trailing 21 bars."""
    return _up_gap_bool(high, low).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f09_irgd_020_count_up_gaps_in_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Number of up-gap days in trailing 63 bars — quarterly horizon."""
    return _up_gap_bool(high, low).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f09_irgd_021_count_up_gaps_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Number of up-gap days in trailing 252 bars — yearly horizon."""
    return _up_gap_bool(high, low).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_022_count_down_gaps_in_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Number of down-gap days in trailing 21 bars."""
    return _down_gap_bool(high, low).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f09_irgd_023_count_down_gaps_in_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Number of down-gap days in trailing 63 bars."""
    return _down_gap_bool(high, low).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f09_irgd_024_count_down_gaps_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Number of down-gap days in trailing 252 bars."""
    return _down_gap_bool(high, low).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_025_count_large_up_gaps_gt_1atr_in_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of up-gaps > 1 ATR in trailing 63 bars."""
    atr = _atr(high, low, close, n=MDAYS)
    big = (_up_gap_size(high, low) > atr).fillna(False).astype(float)
    return big.rolling(QDAYS, min_periods=MDAYS).sum()


def f09_irgd_026_count_large_up_gaps_gt_2atr_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of up-gaps > 2 ATR in trailing 252 bars."""
    atr = _atr(high, low, close, n=MDAYS)
    big = (_up_gap_size(high, low) > 2.0 * atr).fillna(False).astype(float)
    return big.rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_027_count_extreme_down_gaps_gt_2atr_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of down-gaps > 2 ATR in trailing 252 bars — extreme-tier down events."""
    atr = _atr(high, low, close, n=MDAYS)
    big = (_down_gap_size(high, low) > 2.0 * atr).fillna(False).astype(float)
    return big.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket D — Net gap balance (028-031)
# ============================================================

def f09_irgd_028_net_gap_balance_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Up-gap count minus down-gap count in last 21 bars — directional gap bias."""
    up = _up_gap_bool(high, low).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    dn = _down_gap_bool(high, low).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return up - dn


def f09_irgd_029_net_gap_balance_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Up-gap count minus down-gap count in last 63 bars."""
    up = _up_gap_bool(high, low).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    dn = _down_gap_bool(high, low).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return up - dn


def f09_irgd_030_net_gap_balance_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Up-gap count minus down-gap count in last 252 bars."""
    up = _up_gap_bool(high, low).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    dn = _down_gap_bool(high, low).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return up - dn


def f09_irgd_031_net_gap_log_size_balance_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of up-gap log-sizes minus down-gap log-sizes in last 63 bars."""
    up_log = (_safe_log(low) - _safe_log(high.shift(1))).where(_up_gap_bool(high, low), 0.0)
    dn_log = (_safe_log(low.shift(1)) - _safe_log(high)).where(_down_gap_bool(high, low), 0.0)
    return up_log.rolling(QDAYS, min_periods=MDAYS).sum() - dn_log.rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
# Bucket E — Cumulative gap size (032-035)
# ============================================================

def f09_irgd_032_cum_up_gap_log_size_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of up-gap log sizes in last 63 bars."""
    up_log = (_safe_log(low) - _safe_log(high.shift(1))).where(_up_gap_bool(high, low), 0.0)
    return up_log.rolling(QDAYS, min_periods=MDAYS).sum()


def f09_irgd_033_cum_up_gap_atr_size_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of ATR-normalized up-gap sizes in last 63 bars."""
    atr = _atr(high, low, close, n=MDAYS)
    s = _safe_div(_up_gap_size(high, low), atr).fillna(0.0)
    return s.rolling(QDAYS, min_periods=MDAYS).sum()


def f09_irgd_034_cum_down_gap_log_size_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of down-gap log sizes in last 63 bars (positive magnitudes)."""
    dn_log = (_safe_log(low.shift(1)) - _safe_log(high)).where(_down_gap_bool(high, low), 0.0)
    return dn_log.rolling(QDAYS, min_periods=MDAYS).sum()


def f09_irgd_035_cum_down_gap_atr_size_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of ATR-normalized down-gap sizes in last 252 bars."""
    atr = _atr(high, low, close, n=MDAYS)
    s = _safe_div(_down_gap_size(high, low), atr).fillna(0.0)
    return s.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket F — Island patterns (036-044)
# ============================================================

def f09_irgd_036_island_top_indicator_within_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: an up-gap occurred in last 5d AND a down-gap also occurred in last 5d (tight island)."""
    upg = _up_gap_bool(high, low).fillna(False).astype(float)
    dng = _down_gap_bool(high, low).fillna(False).astype(float)
    up_in = upg.rolling(WDAYS, min_periods=1).sum()
    dn_in = dng.rolling(WDAYS, min_periods=1).sum()
    return ((up_in >= 1) & (dn_in >= 1)).astype(float)


def f09_irgd_037_island_top_indicator_within_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: up-gap and down-gap both within last 21d."""
    upg = _up_gap_bool(high, low).fillna(False).astype(float)
    dng = _down_gap_bool(high, low).fillna(False).astype(float)
    return ((upg.rolling(MDAYS, min_periods=1).sum() >= 1) & (dng.rolling(MDAYS, min_periods=1).sum() >= 1)).astype(float)


def f09_irgd_038_island_top_indicator_within_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: up-gap and down-gap both within last 63d."""
    upg = _up_gap_bool(high, low).fillna(False).astype(float)
    dng = _down_gap_bool(high, low).fillna(False).astype(float)
    return ((upg.rolling(QDAYS, min_periods=1).sum() >= 1) & (dng.rolling(QDAYS, min_periods=1).sum() >= 1)).astype(float)


def f09_irgd_039_island_bottom_indicator_within_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mirror of island top: same indicator (presence of both gap directions) — same hypothesis encoded for bottom-leg detection in tandem.
    For ML, this is identical to 037; here we emit it as a clamped indicator where the down-gap precedes the up-gap chronologically."""
    upg = _up_gap_bool(high, low).fillna(False)
    dng = _down_gap_bool(high, low).fillna(False)
    bars_since_dn = _bars_since_event(dng)
    bars_since_up = _bars_since_event(upg)
    return ((bars_since_dn > bars_since_up) & (bars_since_up <= MDAYS) & (bars_since_dn <= MDAYS)).astype(float)


def f09_irgd_040_island_width_most_recent_top(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars between the most-recent up-gap and the most-recent subsequent down-gap (NaN if none recently)."""
    upg = _up_gap_bool(high, low).fillna(False)
    dng = _down_gap_bool(high, low).fillna(False)
    bars_since_up = _bars_since_event(upg)
    bars_since_dn = _bars_since_event(dng)
    width = bars_since_up - bars_since_dn
    return width.where((width > 0) & (bars_since_dn <= QDAYS), np.nan)


def f09_irgd_041_island_high_above_atr_most_recent_top(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized excursion of intra-island high above the gap-up close — island elevation."""
    upg = _up_gap_bool(high, low).fillna(False)
    bars_since_up = _bars_since_event(upg)
    atr = _atr(high, low, close, n=MDAYS)
    # rolling max high over bars [bars_since_up .. now]
    rmax_window = high.rolling(MDAYS, min_periods=1).max()
    # use close at the up-gap day as the floor reference: shift close by bars_since_up
    bsu_arr = bars_since_up.to_numpy()
    close_arr = close.to_numpy()
    n = len(close)
    floor_arr = np.full(n, np.nan)
    for i in range(n):
        b = bsu_arr[i]
        if np.isnan(b) or b > MDAYS: continue
        j = int(i - int(b))
        if 0 <= j < n: floor_arr[i] = close_arr[j]
    floor = pd.Series(floor_arr, index=close.index)
    return _safe_div(rmax_window - floor, atr)


def f09_irgd_042_island_unfilled_indicator_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: an up-gap occurred in last 21d AND subsequent bars have NOT filled the gap (low never <= prior high)."""
    upg = _up_gap_bool(high, low).fillna(False)
    bsu = _bars_since_event(upg)
    n = len(close)
    bsu_arr = bsu.to_numpy()
    low_arr = low.to_numpy()
    high_arr = high.to_numpy()
    out = np.full(n, 0.0)
    for i in range(n):
        b = bsu_arr[i]
        if np.isnan(b) or b > MDAYS: continue
        j = int(i - int(b))
        if j <= 0: continue
        prior_high = high_arr[j - 1]
        if np.isnan(prior_high): continue
        post_min_low = np.nanmin(low_arr[j:i+1]) if i >= j else np.nan
        if np.isnan(post_min_low): continue
        out[i] = float(post_min_low > prior_high)
    return pd.Series(out, index=close.index)


def f09_irgd_043_count_island_tops_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of distinct island-top events in last 252d (using the within-21d criterion)."""
    upg = _up_gap_bool(high, low).fillna(False)
    dng = _down_gap_bool(high, low).fillna(False)
    is_top = (upg.rolling(MDAYS, min_periods=1).sum() >= 1) & dng
    return is_top.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_044_count_islands_either_kind_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of island events (top OR bottom) in last 252d."""
    upg = _up_gap_bool(high, low).fillna(False)
    dng = _down_gap_bool(high, low).fillna(False)
    top = (upg.rolling(MDAYS, min_periods=1).sum() >= 1) & dng
    bot = (dng.rolling(MDAYS, min_periods=1).sum() >= 1) & upg
    return (top | bot).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket G — Exhaustion gap signatures (045-051)
# ============================================================

def f09_irgd_045_exhaustion_up_gap_indicator_after_uptrend(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: up-gap on a bar where close > 252d SMA for last 60d AND price in top decile of 252d range — classic exhaustion."""
    sma252 = close.rolling(YDAYS, min_periods=QDAYS).mean()
    above60 = (close > sma252).rolling(60, min_periods=20).sum() >= 60
    hi252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    lo252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - lo252, hi252 - lo252)
    in_top = pos >= 0.9
    return (_up_gap_bool(high, low) & above60 & in_top).astype(float)


def f09_irgd_046_exhaustion_gap_atr_size_after_uptrend(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-size of the most-recent exhaustion up-gap event in last 63 bars (else 0)."""
    sma252 = close.rolling(YDAYS, min_periods=QDAYS).mean()
    above60 = (close > sma252).rolling(60, min_periods=20).sum() >= 60
    hi252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    lo252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - lo252, hi252 - lo252)
    in_top = pos >= 0.9
    atr = _atr(high, low, close, n=MDAYS)
    exh_size = _safe_div(_up_gap_size(high, low), atr).where(_up_gap_bool(high, low) & above60 & in_top, np.nan)
    return exh_size.rolling(QDAYS, min_periods=1).max().fillna(0.0)


def f09_irgd_047_exhaustion_gap_count_in_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of exhaustion up-gap events in last 252 bars."""
    sma252 = close.rolling(YDAYS, min_periods=QDAYS).mean()
    above60 = (close > sma252).rolling(60, min_periods=20).sum() >= 60
    hi252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    lo252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - lo252, hi252 - lo252)
    in_top = pos >= 0.9
    ev = (_up_gap_bool(high, low) & above60 & in_top).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_048_bars_since_last_exhaustion_up_gap(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since the most recent exhaustion up-gap event."""
    sma252 = close.rolling(YDAYS, min_periods=QDAYS).mean()
    above60 = (close > sma252).rolling(60, min_periods=20).sum() >= 60
    hi252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    lo252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - lo252, hi252 - lo252)
    in_top = pos >= 0.9
    ev = (_up_gap_bool(high, low) & above60 & in_top).fillna(False)
    return _bars_since_event(ev)


def f09_irgd_049_exhaustion_pattern_density_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Exhaustion gap count / total up-gap count in last 252d — fraction of up-gaps that are exhaustion-typed."""
    sma252 = close.rolling(YDAYS, min_periods=QDAYS).mean()
    above60 = (close > sma252).rolling(60, min_periods=20).sum() >= 60
    hi252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    lo252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - lo252, hi252 - lo252)
    in_top = pos >= 0.9
    exh = (_up_gap_bool(high, low) & above60 & in_top).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    tot = _up_gap_bool(high, low).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(exh, tot)


def f09_irgd_050_exhaustion_gap_volume_zscore(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of volume on most-recent exhaustion-up-gap day vs trailing 63d volume distribution."""
    sma252 = close.rolling(YDAYS, min_periods=QDAYS).mean()
    above60 = (close > sma252).rolling(60, min_periods=20).sum() >= 60
    hi252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    lo252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - lo252, hi252 - lo252)
    in_top = pos >= 0.9
    ev = (_up_gap_bool(high, low) & above60 & in_top)
    vmean = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    vstd = volume.rolling(QDAYS, min_periods=MDAYS).std()
    z = _safe_div(volume - vmean, vstd)
    return z.where(ev, np.nan).rolling(QDAYS, min_periods=1).max().fillna(0.0)


def f09_irgd_051_exhaustion_gap_close_reversal_indicator(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: gap-up where close < open (classic exhaustion reversal bar)."""
    return (_up_gap_bool(high, low) & (close < open_)).astype(float)


# ============================================================
# Bucket H — Breakaway / runaway gaps (052-057)
# ============================================================

def f09_irgd_052_breakaway_up_gap_indicator(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: up-gap on a bar where pre-21d ATR is below trailing-63d ATR median by 30% — consolidation breakout."""
    atr21 = _atr(high, low, close, n=MDAYS)
    atr_median_63d = atr21.rolling(QDAYS, min_periods=MDAYS).median()
    compress = atr21.shift(1) < 0.7 * atr_median_63d.shift(1)
    return (_up_gap_bool(high, low) & compress).astype(float)


def f09_irgd_053_breakaway_gap_atr_size_relative_to_pre_atr(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Most-recent breakaway up-gap size in units of pre-gap ATR (21d) — gap power vs prior compression."""
    atr21 = _atr(high, low, close, n=MDAYS)
    atr_median_63d = atr21.rolling(QDAYS, min_periods=MDAYS).median()
    compress = atr21.shift(1) < 0.7 * atr_median_63d.shift(1)
    g = _up_gap_size(high, low).where(_up_gap_bool(high, low) & compress, np.nan)
    sz = _safe_div(g, atr21.shift(1))
    return sz.rolling(QDAYS, min_periods=1).max().fillna(0.0)


def f09_irgd_054_count_breakaway_up_gaps_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of breakaway up-gap events in last 252 bars."""
    atr21 = _atr(high, low, close, n=MDAYS)
    atr_median_63d = atr21.rolling(QDAYS, min_periods=MDAYS).median()
    compress = atr21.shift(1) < 0.7 * atr_median_63d.shift(1)
    ev = (_up_gap_bool(high, low) & compress).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_055_runaway_up_gap_indicator(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: up-gap on a bar where close is in middle 40%-70% of 252d range — runaway (not exhaustion, not breakout)."""
    hi252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    lo252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - lo252, hi252 - lo252)
    in_mid = (pos >= 0.4) & (pos <= 0.7)
    return (_up_gap_bool(high, low) & in_mid).astype(float)


def f09_irgd_056_count_runaway_up_gaps_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of runaway up-gaps in last 252d."""
    hi252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    lo252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - lo252, hi252 - lo252)
    in_mid = (pos >= 0.4) & (pos <= 0.7)
    ev = (_up_gap_bool(high, low) & in_mid).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_057_breakaway_vs_exhaustion_count_diff_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of breakaway up-gaps minus count of exhaustion up-gaps in last 252d — gap-regime balance."""
    atr21 = _atr(high, low, close, n=MDAYS)
    atr_median_63d = atr21.rolling(QDAYS, min_periods=MDAYS).median()
    compress = atr21.shift(1) < 0.7 * atr_median_63d.shift(1)
    brk = (_up_gap_bool(high, low) & compress).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    sma252 = close.rolling(YDAYS, min_periods=QDAYS).mean()
    above60 = (close > sma252).rolling(60, min_periods=20).sum() >= 60
    hi252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    lo252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - lo252, hi252 - lo252)
    in_top = pos >= 0.9
    exh = (_up_gap_bool(high, low) & above60 & in_top).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return brk - exh


# ============================================================
# Bucket I — Unfilled gap counts & time-to-fill (058-064 → 058-064)
# ============================================================

def _gap_fill_age(high: pd.Series, low: pd.Series, direction: str = 'up', horizon: int = 252) -> pd.Series:
    """For each bar i, find the most recent up/down gap within trailing horizon, then return bars until it was filled
    (or NaN if not filled by bar i)."""
    n = len(high)
    high_arr = high.to_numpy()
    low_arr = low.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        # scan backwards from i-1 down to max(0, i-horizon)
        start = max(0, i - horizon)
        for k in range(i, start - 1, -1):
            if k < 1: break
            if direction == 'up':
                if not (low_arr[k] > high_arr[k - 1]): continue
                gap_floor = high_arr[k - 1]
                # check if any low in [k..i] <= gap_floor
                window_low = low_arr[k:i+1]
                if np.any(window_low <= gap_floor):
                    # fill bar idx
                    fill_offsets = np.where(window_low <= gap_floor)[0]
                    out[i] = float(fill_offsets[0])
                else:
                    out[i] = np.nan
                break
            else:
                if not (high_arr[k] < low_arr[k - 1]): continue
                gap_ceil = low_arr[k - 1]
                window_high = high_arr[k:i+1]
                if np.any(window_high >= gap_ceil):
                    fill_offsets = np.where(window_high >= gap_ceil)[0]
                    out[i] = float(fill_offsets[0])
                else:
                    out[i] = np.nan
                break
    return pd.Series(out, index=high.index)


def f09_irgd_058_unfilled_up_gap_count_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of up-gaps in last 252d that have NOT been filled by current bar."""
    n = len(high)
    high_arr = high.to_numpy()
    low_arr = low.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS)
        cnt = 0
        for k in range(start + 1, i + 1):
            if not (low_arr[k] > high_arr[k - 1]): continue
            gap_floor = high_arr[k - 1]
            # check if any low in (k..i] <= gap_floor
            if i >= k + 1:
                if np.any(low_arr[k + 1:i + 1] <= gap_floor):
                    continue
            cnt += 1
        out[i] = float(cnt)
    return pd.Series(out, index=high.index)


def f09_irgd_059_unfilled_up_gap_log_size_total_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of log-sizes of unfilled up-gaps in last 252d."""
    n = len(high)
    high_arr = high.to_numpy()
    low_arr = low.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS)
        total = 0.0
        for k in range(start + 1, i + 1):
            if not (low_arr[k] > high_arr[k - 1]): continue
            gap_floor = high_arr[k - 1]
            if i >= k + 1:
                if np.any(low_arr[k + 1:i + 1] <= gap_floor): continue
            if gap_floor > 0 and low_arr[k] > 0:
                total += np.log(low_arr[k] / gap_floor)
        out[i] = total
    return pd.Series(out, index=high.index)


def f09_irgd_060_time_to_fill_most_recent_up_gap(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """For the most-recent up-gap in last 252d: bars-to-fill (NaN if not yet filled)."""
    return _gap_fill_age(high, low, direction='up', horizon=YDAYS)


def f09_irgd_061_time_to_fill_most_recent_down_gap(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """For the most-recent down-gap in last 252d: bars-to-fill."""
    return _gap_fill_age(high, low, direction='down', horizon=YDAYS)


def f09_irgd_062_median_time_to_fill_up_gaps_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Median bars-to-fill for up-gaps that occurred in trailing 252d AND were filled by current bar."""
    n = len(high)
    high_arr = high.to_numpy()
    low_arr = low.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS)
        fills = []
        for k in range(start + 1, i + 1):
            if not (low_arr[k] > high_arr[k - 1]): continue
            gap_floor = high_arr[k - 1]
            if i < k + 1: continue
            mask = low_arr[k + 1:i + 1] <= gap_floor
            if np.any(mask):
                fill_at = np.argmax(mask) + 1  # offset from k
                fills.append(float(fill_at))
        if len(fills) > 0:
            out[i] = float(np.median(fills))
    return pd.Series(out, index=high.index)


def f09_irgd_063_mean_unfilled_up_gap_size_atr_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR-normalized size of unfilled up-gaps in last 252d."""
    atr_series = _atr(high, low, close, n=MDAYS)
    n = len(high)
    high_arr = high.to_numpy()
    low_arr = low.to_numpy()
    atr_arr = atr_series.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS)
        sizes = []
        for k in range(start + 1, i + 1):
            if not (low_arr[k] > high_arr[k - 1]): continue
            gap_floor = high_arr[k - 1]
            if i >= k + 1:
                if np.any(low_arr[k + 1:i + 1] <= gap_floor): continue
            if not np.isnan(atr_arr[k]) and atr_arr[k] > 0:
                sizes.append((low_arr[k] - high_arr[k - 1]) / atr_arr[k])
        if len(sizes) > 0:
            out[i] = float(np.mean(sizes))
    return pd.Series(out, index=high.index)


def f09_irgd_064_oldest_unfilled_up_gap_age_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since the oldest still-unfilled up-gap in trailing 252d."""
    n = len(high)
    high_arr = high.to_numpy()
    low_arr = low.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS)
        oldest = np.nan
        for k in range(start + 1, i + 1):
            if not (low_arr[k] > high_arr[k - 1]): continue
            gap_floor = high_arr[k - 1]
            if i >= k + 1:
                if np.any(low_arr[k + 1:i + 1] <= gap_floor): continue
            age = float(i - k)
            if np.isnan(oldest) or age > oldest: oldest = age
        out[i] = oldest
    return pd.Series(out, index=high.index)


# ============================================================
# Bucket J — Gap fade / full-close reversal (065-070)
# ============================================================

def f09_irgd_065_gap_fade_up_indicator(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: up-gap day with close < open (gap was faded intraday)."""
    return (_up_gap_bool(high, low) & (close < open_)).astype(float)


def f09_irgd_066_gap_fade_down_indicator(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: down-gap day with close > open (gap-down was faded intraday)."""
    return (_down_gap_bool(high, low) & (close > open_)).astype(float)


def f09_irgd_067_count_gap_fade_events_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of gap-fade events (either direction) in last 252 bars."""
    ev = (_up_gap_bool(high, low) & (close < open_)) | (_down_gap_bool(high, low) & (close > open_))
    return ev.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_068_gap_fade_magnitude_atr_most_recent(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized (open - close) on the most-recent gap-up-fade day in last 63 bars (positive = larger fade)."""
    atr = _atr(high, low, close, n=MDAYS)
    fade = (open_ - close).where(_up_gap_bool(high, low) & (close < open_), np.nan)
    return _safe_div(fade, atr).rolling(QDAYS, min_periods=1).max().fillna(0.0)


def f09_irgd_069_gap_full_close_reversal_indicator(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: gap-up day where close ends below the prior-day high (entire gap reversed by close)."""
    return (_up_gap_bool(high, low) & (close < high.shift(1))).astype(float)


def f09_irgd_070_count_full_close_reversal_events_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of full-close-reversal gap-up events in last 252 bars."""
    ev = (_up_gap_bool(high, low) & (close < high.shift(1))).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket K — Two-gap / three-gap composite patterns (071-075)
# ============================================================

def f09_irgd_071_two_gap_pattern_up_then_down_within_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: a down-gap today AND an up-gap within prior 5 bars (excl. today)."""
    upg = _up_gap_bool(high, low).fillna(False).astype(float)
    dng = _down_gap_bool(high, low).fillna(False)
    had_up = upg.shift(1).rolling(WDAYS, min_periods=1).sum() >= 1
    return (dng & had_up).astype(float)


def f09_irgd_072_two_gap_pattern_up_then_down_within_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Down-gap today AND up-gap within prior 21 bars."""
    upg = _up_gap_bool(high, low).fillna(False).astype(float)
    dng = _down_gap_bool(high, low).fillna(False)
    had_up = upg.shift(1).rolling(MDAYS, min_periods=1).sum() >= 1
    return (dng & had_up).astype(float)


def f09_irgd_073_three_gap_island_within_21d_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: at least 2 up-gaps + 1 down-gap within last 21d — extended island top with stacked gap-ups."""
    upg = _up_gap_bool(high, low).fillna(False).astype(float)
    dng = _down_gap_bool(high, low).fillna(False).astype(float)
    up_cnt = upg.rolling(MDAYS, min_periods=1).sum()
    dn_cnt = dng.rolling(MDAYS, min_periods=1).sum()
    return ((up_cnt >= 2) & (dn_cnt >= 1)).astype(float)


def f09_irgd_074_count_two_gap_reversal_patterns_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of (down-gap today AND up-gap in prior 21d) events in last 252 bars."""
    upg = _up_gap_bool(high, low).fillna(False).astype(float)
    dng = _down_gap_bool(high, low).fillna(False)
    had_up = upg.shift(1).rolling(MDAYS, min_periods=1).sum() >= 1
    ev = (dng & had_up).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_075_mean_gap_pair_separation_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean inter-event bar gap between consecutive up-gap events in last 252 bars — clustering proxy."""
    cnt = _up_gap_bool(high, low).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(YDAYS, cnt)


# ============================================================
#                         REGISTRY 001-075
# ============================================================



def f09_irgd_001_log_up_gap_size_most_recent_5d_d3(high, low, close):
    return f09_irgd_001_log_up_gap_size_most_recent_5d(high, low, close).diff().diff().diff()


def f09_irgd_002_log_up_gap_size_most_recent_21d_d3(high, low, close):
    return f09_irgd_002_log_up_gap_size_most_recent_21d(high, low, close).diff().diff().diff()


def f09_irgd_003_log_up_gap_size_most_recent_63d_d3(high, low, close):
    return f09_irgd_003_log_up_gap_size_most_recent_63d(high, low, close).diff().diff().diff()


def f09_irgd_004_atr_up_gap_size_most_recent_5d_d3(high, low, close):
    return f09_irgd_004_atr_up_gap_size_most_recent_5d(high, low, close).diff().diff().diff()


def f09_irgd_005_atr_up_gap_size_most_recent_21d_d3(high, low, close):
    return f09_irgd_005_atr_up_gap_size_most_recent_21d(high, low, close).diff().diff().diff()


def f09_irgd_006_pct_up_gap_size_most_recent_5d_d3(high, low, close):
    return f09_irgd_006_pct_up_gap_size_most_recent_5d(high, low, close).diff().diff().diff()


def f09_irgd_007_log_down_gap_size_most_recent_5d_d3(high, low, close):
    return f09_irgd_007_log_down_gap_size_most_recent_5d(high, low, close).diff().diff().diff()


def f09_irgd_008_atr_down_gap_size_most_recent_21d_d3(high, low, close):
    return f09_irgd_008_atr_down_gap_size_most_recent_21d(high, low, close).diff().diff().diff()


def f09_irgd_009_pct_down_gap_size_most_recent_21d_d3(high, low, close):
    return f09_irgd_009_pct_down_gap_size_most_recent_21d(high, low, close).diff().diff().diff()


def f09_irgd_010_bars_since_last_up_gap_any_d3(high, low, close):
    return f09_irgd_010_bars_since_last_up_gap_any(high, low, close).diff().diff().diff()


def f09_irgd_011_bars_since_last_up_gap_gt_1atr_d3(high, low, close):
    return f09_irgd_011_bars_since_last_up_gap_gt_1atr(high, low, close).diff().diff().diff()


def f09_irgd_012_bars_since_last_up_gap_gt_2atr_d3(high, low, close):
    return f09_irgd_012_bars_since_last_up_gap_gt_2atr(high, low, close).diff().diff().diff()


def f09_irgd_013_bars_since_last_up_gap_gt_3atr_d3(high, low, close):
    return f09_irgd_013_bars_since_last_up_gap_gt_3atr(high, low, close).diff().diff().diff()


def f09_irgd_014_bars_since_last_down_gap_any_d3(high, low, close):
    return f09_irgd_014_bars_since_last_down_gap_any(high, low, close).diff().diff().diff()


def f09_irgd_015_bars_since_last_down_gap_gt_1atr_d3(high, low, close):
    return f09_irgd_015_bars_since_last_down_gap_gt_1atr(high, low, close).diff().diff().diff()


def f09_irgd_016_bars_since_last_down_gap_gt_2atr_d3(high, low, close):
    return f09_irgd_016_bars_since_last_down_gap_gt_2atr(high, low, close).diff().diff().diff()


def f09_irgd_017_bars_since_last_down_gap_gt_3atr_d3(high, low, close):
    return f09_irgd_017_bars_since_last_down_gap_gt_3atr(high, low, close).diff().diff().diff()


def f09_irgd_018_bars_since_last_gap_either_direction_d3(high, low, close):
    return f09_irgd_018_bars_since_last_gap_either_direction(high, low, close).diff().diff().diff()


def f09_irgd_019_count_up_gaps_in_21d_d3(high, low, close):
    return f09_irgd_019_count_up_gaps_in_21d(high, low, close).diff().diff().diff()


def f09_irgd_020_count_up_gaps_in_63d_d3(high, low, close):
    return f09_irgd_020_count_up_gaps_in_63d(high, low, close).diff().diff().diff()


def f09_irgd_021_count_up_gaps_in_252d_d3(high, low, close):
    return f09_irgd_021_count_up_gaps_in_252d(high, low, close).diff().diff().diff()


def f09_irgd_022_count_down_gaps_in_21d_d3(high, low, close):
    return f09_irgd_022_count_down_gaps_in_21d(high, low, close).diff().diff().diff()


def f09_irgd_023_count_down_gaps_in_63d_d3(high, low, close):
    return f09_irgd_023_count_down_gaps_in_63d(high, low, close).diff().diff().diff()


def f09_irgd_024_count_down_gaps_in_252d_d3(high, low, close):
    return f09_irgd_024_count_down_gaps_in_252d(high, low, close).diff().diff().diff()


def f09_irgd_025_count_large_up_gaps_gt_1atr_in_63d_d3(high, low, close):
    return f09_irgd_025_count_large_up_gaps_gt_1atr_in_63d(high, low, close).diff().diff().diff()


def f09_irgd_026_count_large_up_gaps_gt_2atr_in_252d_d3(high, low, close):
    return f09_irgd_026_count_large_up_gaps_gt_2atr_in_252d(high, low, close).diff().diff().diff()


def f09_irgd_027_count_extreme_down_gaps_gt_2atr_in_252d_d3(high, low, close):
    return f09_irgd_027_count_extreme_down_gaps_gt_2atr_in_252d(high, low, close).diff().diff().diff()


def f09_irgd_028_net_gap_balance_21d_d3(high, low, close):
    return f09_irgd_028_net_gap_balance_21d(high, low, close).diff().diff().diff()


def f09_irgd_029_net_gap_balance_63d_d3(high, low, close):
    return f09_irgd_029_net_gap_balance_63d(high, low, close).diff().diff().diff()


def f09_irgd_030_net_gap_balance_252d_d3(high, low, close):
    return f09_irgd_030_net_gap_balance_252d(high, low, close).diff().diff().diff()


def f09_irgd_031_net_gap_log_size_balance_63d_d3(high, low, close):
    return f09_irgd_031_net_gap_log_size_balance_63d(high, low, close).diff().diff().diff()


def f09_irgd_032_cum_up_gap_log_size_63d_d3(high, low, close):
    return f09_irgd_032_cum_up_gap_log_size_63d(high, low, close).diff().diff().diff()


def f09_irgd_033_cum_up_gap_atr_size_63d_d3(high, low, close):
    return f09_irgd_033_cum_up_gap_atr_size_63d(high, low, close).diff().diff().diff()


def f09_irgd_034_cum_down_gap_log_size_63d_d3(high, low, close):
    return f09_irgd_034_cum_down_gap_log_size_63d(high, low, close).diff().diff().diff()


def f09_irgd_035_cum_down_gap_atr_size_252d_d3(high, low, close):
    return f09_irgd_035_cum_down_gap_atr_size_252d(high, low, close).diff().diff().diff()


def f09_irgd_036_island_top_indicator_within_5d_d3(high, low, close):
    return f09_irgd_036_island_top_indicator_within_5d(high, low, close).diff().diff().diff()


def f09_irgd_037_island_top_indicator_within_21d_d3(high, low, close):
    return f09_irgd_037_island_top_indicator_within_21d(high, low, close).diff().diff().diff()


def f09_irgd_038_island_top_indicator_within_63d_d3(high, low, close):
    return f09_irgd_038_island_top_indicator_within_63d(high, low, close).diff().diff().diff()


def f09_irgd_039_island_bottom_indicator_within_21d_d3(high, low, close):
    return f09_irgd_039_island_bottom_indicator_within_21d(high, low, close).diff().diff().diff()


def f09_irgd_040_island_width_most_recent_top_d3(high, low, close):
    return f09_irgd_040_island_width_most_recent_top(high, low, close).diff().diff().diff()


def f09_irgd_041_island_high_above_atr_most_recent_top_d3(high, low, close):
    return f09_irgd_041_island_high_above_atr_most_recent_top(high, low, close).diff().diff().diff()


def f09_irgd_042_island_unfilled_indicator_21d_d3(high, low, close):
    return f09_irgd_042_island_unfilled_indicator_21d(high, low, close).diff().diff().diff()


def f09_irgd_043_count_island_tops_in_252d_d3(high, low, close):
    return f09_irgd_043_count_island_tops_in_252d(high, low, close).diff().diff().diff()


def f09_irgd_044_count_islands_either_kind_in_252d_d3(high, low, close):
    return f09_irgd_044_count_islands_either_kind_in_252d(high, low, close).diff().diff().diff()


def f09_irgd_045_exhaustion_up_gap_indicator_after_uptrend_d3(open_, high, low, close):
    return f09_irgd_045_exhaustion_up_gap_indicator_after_uptrend(open_, high, low, close).diff().diff().diff()


def f09_irgd_046_exhaustion_gap_atr_size_after_uptrend_d3(open_, high, low, close):
    return f09_irgd_046_exhaustion_gap_atr_size_after_uptrend(open_, high, low, close).diff().diff().diff()


def f09_irgd_047_exhaustion_gap_count_in_252d_d3(open_, high, low, close):
    return f09_irgd_047_exhaustion_gap_count_in_252d(open_, high, low, close).diff().diff().diff()


def f09_irgd_048_bars_since_last_exhaustion_up_gap_d3(open_, high, low, close):
    return f09_irgd_048_bars_since_last_exhaustion_up_gap(open_, high, low, close).diff().diff().diff()


def f09_irgd_049_exhaustion_pattern_density_252d_d3(open_, high, low, close):
    return f09_irgd_049_exhaustion_pattern_density_252d(open_, high, low, close).diff().diff().diff()


def f09_irgd_050_exhaustion_gap_volume_zscore_d3(open_, high, low, close, volume):
    return f09_irgd_050_exhaustion_gap_volume_zscore(open_, high, low, close, volume).diff().diff().diff()


def f09_irgd_051_exhaustion_gap_close_reversal_indicator_d3(open_, high, low, close):
    return f09_irgd_051_exhaustion_gap_close_reversal_indicator(open_, high, low, close).diff().diff().diff()


def f09_irgd_052_breakaway_up_gap_indicator_d3(open_, high, low, close):
    return f09_irgd_052_breakaway_up_gap_indicator(open_, high, low, close).diff().diff().diff()


def f09_irgd_053_breakaway_gap_atr_size_relative_to_pre_atr_d3(open_, high, low, close):
    return f09_irgd_053_breakaway_gap_atr_size_relative_to_pre_atr(open_, high, low, close).diff().diff().diff()


def f09_irgd_054_count_breakaway_up_gaps_252d_d3(open_, high, low, close):
    return f09_irgd_054_count_breakaway_up_gaps_252d(open_, high, low, close).diff().diff().diff()


def f09_irgd_055_runaway_up_gap_indicator_d3(open_, high, low, close):
    return f09_irgd_055_runaway_up_gap_indicator(open_, high, low, close).diff().diff().diff()


def f09_irgd_056_count_runaway_up_gaps_252d_d3(open_, high, low, close):
    return f09_irgd_056_count_runaway_up_gaps_252d(open_, high, low, close).diff().diff().diff()


def f09_irgd_057_breakaway_vs_exhaustion_count_diff_252d_d3(open_, high, low, close):
    return f09_irgd_057_breakaway_vs_exhaustion_count_diff_252d(open_, high, low, close).diff().diff().diff()


def f09_irgd_058_unfilled_up_gap_count_in_252d_d3(high, low, close):
    return f09_irgd_058_unfilled_up_gap_count_in_252d(high, low, close).diff().diff().diff()


def f09_irgd_059_unfilled_up_gap_log_size_total_252d_d3(high, low, close):
    return f09_irgd_059_unfilled_up_gap_log_size_total_252d(high, low, close).diff().diff().diff()


def f09_irgd_060_time_to_fill_most_recent_up_gap_d3(high, low, close):
    return f09_irgd_060_time_to_fill_most_recent_up_gap(high, low, close).diff().diff().diff()


def f09_irgd_061_time_to_fill_most_recent_down_gap_d3(high, low, close):
    return f09_irgd_061_time_to_fill_most_recent_down_gap(high, low, close).diff().diff().diff()


def f09_irgd_062_median_time_to_fill_up_gaps_252d_d3(high, low, close):
    return f09_irgd_062_median_time_to_fill_up_gaps_252d(high, low, close).diff().diff().diff()


def f09_irgd_063_mean_unfilled_up_gap_size_atr_252d_d3(high, low, close):
    return f09_irgd_063_mean_unfilled_up_gap_size_atr_252d(high, low, close).diff().diff().diff()


def f09_irgd_064_oldest_unfilled_up_gap_age_in_252d_d3(high, low, close):
    return f09_irgd_064_oldest_unfilled_up_gap_age_in_252d(high, low, close).diff().diff().diff()


def f09_irgd_065_gap_fade_up_indicator_d3(open_, high, low, close):
    return f09_irgd_065_gap_fade_up_indicator(open_, high, low, close).diff().diff().diff()


def f09_irgd_066_gap_fade_down_indicator_d3(open_, high, low, close):
    return f09_irgd_066_gap_fade_down_indicator(open_, high, low, close).diff().diff().diff()


def f09_irgd_067_count_gap_fade_events_252d_d3(open_, high, low, close):
    return f09_irgd_067_count_gap_fade_events_252d(open_, high, low, close).diff().diff().diff()


def f09_irgd_068_gap_fade_magnitude_atr_most_recent_d3(open_, high, low, close):
    return f09_irgd_068_gap_fade_magnitude_atr_most_recent(open_, high, low, close).diff().diff().diff()


def f09_irgd_069_gap_full_close_reversal_indicator_d3(open_, high, low, close):
    return f09_irgd_069_gap_full_close_reversal_indicator(open_, high, low, close).diff().diff().diff()


def f09_irgd_070_count_full_close_reversal_events_252d_d3(open_, high, low, close):
    return f09_irgd_070_count_full_close_reversal_events_252d(open_, high, low, close).diff().diff().diff()


def f09_irgd_071_two_gap_pattern_up_then_down_within_5d_d3(high, low, close):
    return f09_irgd_071_two_gap_pattern_up_then_down_within_5d(high, low, close).diff().diff().diff()


def f09_irgd_072_two_gap_pattern_up_then_down_within_21d_d3(high, low, close):
    return f09_irgd_072_two_gap_pattern_up_then_down_within_21d(high, low, close).diff().diff().diff()


def f09_irgd_073_three_gap_island_within_21d_indicator_d3(high, low, close):
    return f09_irgd_073_three_gap_island_within_21d_indicator(high, low, close).diff().diff().diff()


def f09_irgd_074_count_two_gap_reversal_patterns_252d_d3(high, low, close):
    return f09_irgd_074_count_two_gap_reversal_patterns_252d(high, low, close).diff().diff().diff()


def f09_irgd_075_mean_gap_pair_separation_252d_d3(high, low, close):
    return f09_irgd_075_mean_gap_pair_separation_252d(high, low, close).diff().diff().diff()


ISLAND_REVERSAL_GAP_DYNAMICS_D3_REGISTRY_001_075 = {
    "f09_irgd_001_log_up_gap_size_most_recent_5d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_001_log_up_gap_size_most_recent_5d_d3},
    "f09_irgd_002_log_up_gap_size_most_recent_21d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_002_log_up_gap_size_most_recent_21d_d3},
    "f09_irgd_003_log_up_gap_size_most_recent_63d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_003_log_up_gap_size_most_recent_63d_d3},
    "f09_irgd_004_atr_up_gap_size_most_recent_5d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_004_atr_up_gap_size_most_recent_5d_d3},
    "f09_irgd_005_atr_up_gap_size_most_recent_21d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_005_atr_up_gap_size_most_recent_21d_d3},
    "f09_irgd_006_pct_up_gap_size_most_recent_5d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_006_pct_up_gap_size_most_recent_5d_d3},
    "f09_irgd_007_log_down_gap_size_most_recent_5d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_007_log_down_gap_size_most_recent_5d_d3},
    "f09_irgd_008_atr_down_gap_size_most_recent_21d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_008_atr_down_gap_size_most_recent_21d_d3},
    "f09_irgd_009_pct_down_gap_size_most_recent_21d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_009_pct_down_gap_size_most_recent_21d_d3},
    "f09_irgd_010_bars_since_last_up_gap_any_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_010_bars_since_last_up_gap_any_d3},
    "f09_irgd_011_bars_since_last_up_gap_gt_1atr_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_011_bars_since_last_up_gap_gt_1atr_d3},
    "f09_irgd_012_bars_since_last_up_gap_gt_2atr_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_012_bars_since_last_up_gap_gt_2atr_d3},
    "f09_irgd_013_bars_since_last_up_gap_gt_3atr_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_013_bars_since_last_up_gap_gt_3atr_d3},
    "f09_irgd_014_bars_since_last_down_gap_any_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_014_bars_since_last_down_gap_any_d3},
    "f09_irgd_015_bars_since_last_down_gap_gt_1atr_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_015_bars_since_last_down_gap_gt_1atr_d3},
    "f09_irgd_016_bars_since_last_down_gap_gt_2atr_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_016_bars_since_last_down_gap_gt_2atr_d3},
    "f09_irgd_017_bars_since_last_down_gap_gt_3atr_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_017_bars_since_last_down_gap_gt_3atr_d3},
    "f09_irgd_018_bars_since_last_gap_either_direction_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_018_bars_since_last_gap_either_direction_d3},
    "f09_irgd_019_count_up_gaps_in_21d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_019_count_up_gaps_in_21d_d3},
    "f09_irgd_020_count_up_gaps_in_63d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_020_count_up_gaps_in_63d_d3},
    "f09_irgd_021_count_up_gaps_in_252d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_021_count_up_gaps_in_252d_d3},
    "f09_irgd_022_count_down_gaps_in_21d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_022_count_down_gaps_in_21d_d3},
    "f09_irgd_023_count_down_gaps_in_63d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_023_count_down_gaps_in_63d_d3},
    "f09_irgd_024_count_down_gaps_in_252d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_024_count_down_gaps_in_252d_d3},
    "f09_irgd_025_count_large_up_gaps_gt_1atr_in_63d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_025_count_large_up_gaps_gt_1atr_in_63d_d3},
    "f09_irgd_026_count_large_up_gaps_gt_2atr_in_252d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_026_count_large_up_gaps_gt_2atr_in_252d_d3},
    "f09_irgd_027_count_extreme_down_gaps_gt_2atr_in_252d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_027_count_extreme_down_gaps_gt_2atr_in_252d_d3},
    "f09_irgd_028_net_gap_balance_21d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_028_net_gap_balance_21d_d3},
    "f09_irgd_029_net_gap_balance_63d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_029_net_gap_balance_63d_d3},
    "f09_irgd_030_net_gap_balance_252d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_030_net_gap_balance_252d_d3},
    "f09_irgd_031_net_gap_log_size_balance_63d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_031_net_gap_log_size_balance_63d_d3},
    "f09_irgd_032_cum_up_gap_log_size_63d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_032_cum_up_gap_log_size_63d_d3},
    "f09_irgd_033_cum_up_gap_atr_size_63d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_033_cum_up_gap_atr_size_63d_d3},
    "f09_irgd_034_cum_down_gap_log_size_63d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_034_cum_down_gap_log_size_63d_d3},
    "f09_irgd_035_cum_down_gap_atr_size_252d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_035_cum_down_gap_atr_size_252d_d3},
    "f09_irgd_036_island_top_indicator_within_5d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_036_island_top_indicator_within_5d_d3},
    "f09_irgd_037_island_top_indicator_within_21d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_037_island_top_indicator_within_21d_d3},
    "f09_irgd_038_island_top_indicator_within_63d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_038_island_top_indicator_within_63d_d3},
    "f09_irgd_039_island_bottom_indicator_within_21d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_039_island_bottom_indicator_within_21d_d3},
    "f09_irgd_040_island_width_most_recent_top_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_040_island_width_most_recent_top_d3},
    "f09_irgd_041_island_high_above_atr_most_recent_top_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_041_island_high_above_atr_most_recent_top_d3},
    "f09_irgd_042_island_unfilled_indicator_21d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_042_island_unfilled_indicator_21d_d3},
    "f09_irgd_043_count_island_tops_in_252d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_043_count_island_tops_in_252d_d3},
    "f09_irgd_044_count_islands_either_kind_in_252d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_044_count_islands_either_kind_in_252d_d3},
    "f09_irgd_045_exhaustion_up_gap_indicator_after_uptrend_d3": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_045_exhaustion_up_gap_indicator_after_uptrend_d3},
    "f09_irgd_046_exhaustion_gap_atr_size_after_uptrend_d3": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_046_exhaustion_gap_atr_size_after_uptrend_d3},
    "f09_irgd_047_exhaustion_gap_count_in_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_047_exhaustion_gap_count_in_252d_d3},
    "f09_irgd_048_bars_since_last_exhaustion_up_gap_d3": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_048_bars_since_last_exhaustion_up_gap_d3},
    "f09_irgd_049_exhaustion_pattern_density_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_049_exhaustion_pattern_density_252d_d3},
    "f09_irgd_050_exhaustion_gap_volume_zscore_d3": {"inputs": ["open", "high", "low", "close", "volume"], "func": f09_irgd_050_exhaustion_gap_volume_zscore_d3},
    "f09_irgd_051_exhaustion_gap_close_reversal_indicator_d3": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_051_exhaustion_gap_close_reversal_indicator_d3},
    "f09_irgd_052_breakaway_up_gap_indicator_d3": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_052_breakaway_up_gap_indicator_d3},
    "f09_irgd_053_breakaway_gap_atr_size_relative_to_pre_atr_d3": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_053_breakaway_gap_atr_size_relative_to_pre_atr_d3},
    "f09_irgd_054_count_breakaway_up_gaps_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_054_count_breakaway_up_gaps_252d_d3},
    "f09_irgd_055_runaway_up_gap_indicator_d3": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_055_runaway_up_gap_indicator_d3},
    "f09_irgd_056_count_runaway_up_gaps_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_056_count_runaway_up_gaps_252d_d3},
    "f09_irgd_057_breakaway_vs_exhaustion_count_diff_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_057_breakaway_vs_exhaustion_count_diff_252d_d3},
    "f09_irgd_058_unfilled_up_gap_count_in_252d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_058_unfilled_up_gap_count_in_252d_d3},
    "f09_irgd_059_unfilled_up_gap_log_size_total_252d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_059_unfilled_up_gap_log_size_total_252d_d3},
    "f09_irgd_060_time_to_fill_most_recent_up_gap_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_060_time_to_fill_most_recent_up_gap_d3},
    "f09_irgd_061_time_to_fill_most_recent_down_gap_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_061_time_to_fill_most_recent_down_gap_d3},
    "f09_irgd_062_median_time_to_fill_up_gaps_252d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_062_median_time_to_fill_up_gaps_252d_d3},
    "f09_irgd_063_mean_unfilled_up_gap_size_atr_252d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_063_mean_unfilled_up_gap_size_atr_252d_d3},
    "f09_irgd_064_oldest_unfilled_up_gap_age_in_252d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_064_oldest_unfilled_up_gap_age_in_252d_d3},
    "f09_irgd_065_gap_fade_up_indicator_d3": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_065_gap_fade_up_indicator_d3},
    "f09_irgd_066_gap_fade_down_indicator_d3": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_066_gap_fade_down_indicator_d3},
    "f09_irgd_067_count_gap_fade_events_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_067_count_gap_fade_events_252d_d3},
    "f09_irgd_068_gap_fade_magnitude_atr_most_recent_d3": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_068_gap_fade_magnitude_atr_most_recent_d3},
    "f09_irgd_069_gap_full_close_reversal_indicator_d3": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_069_gap_full_close_reversal_indicator_d3},
    "f09_irgd_070_count_full_close_reversal_events_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_070_count_full_close_reversal_events_252d_d3},
    "f09_irgd_071_two_gap_pattern_up_then_down_within_5d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_071_two_gap_pattern_up_then_down_within_5d_d3},
    "f09_irgd_072_two_gap_pattern_up_then_down_within_21d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_072_two_gap_pattern_up_then_down_within_21d_d3},
    "f09_irgd_073_three_gap_island_within_21d_indicator_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_073_three_gap_island_within_21d_indicator_d3},
    "f09_irgd_074_count_two_gap_reversal_patterns_252d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_074_count_two_gap_reversal_patterns_252d_d3},
    "f09_irgd_075_mean_gap_pair_separation_252d_d3": {"inputs": ["high", "low", "close"], "func": f09_irgd_075_mean_gap_pair_separation_252d_d3},
}
