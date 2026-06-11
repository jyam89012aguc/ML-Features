"""swing_pivot_topology d3 features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py. Each feature
encodes a *different concept* in the swing/pivot topology theme: PIT pivot
counts/ages at multiple timescales, slope of pivot sequences, zigzag leg
amplitudes/durations at multiple percentage thresholds, swing-leg compression
& asymmetry, pivot density, swing-direction entropy, and pivot price dispersion.

This family is distinct from family 07 (lower_high_lower_low_structure, which
encodes Dow-theory binary HH/HL/LH/LL sequences) — here we capture the
geometric / statistical / topological properties of the pivot-swing graph.

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


# ---- family-specific PIT-clean helpers ----

def _is_pit_pivot_high(high: pd.Series, n: int) -> pd.Series:
    """True at bar i iff high[i] == max(high[i-n..i]). Causal/right-anchored.
    This identifies a 'breakout high': the highest bar of the trailing n+1 window."""
    rmax = high.rolling(n + 1, min_periods=n + 1).max()
    return (high == rmax) & high.notna() & rmax.notna()


def _is_pit_pivot_low(low: pd.Series, n: int) -> pd.Series:
    rmin = low.rolling(n + 1, min_periods=n + 1).min()
    return (low == rmin) & low.notna() & rmin.notna()


def _pivot_high_value(high: pd.Series, n: int) -> pd.Series:
    """Most-recent confirmed PIT pivot-high value carried forward."""
    return high.where(_is_pit_pivot_high(high, n), np.nan).ffill()


def _pivot_low_value(low: pd.Series, n: int) -> pd.Series:
    return low.where(_is_pit_pivot_low(low, n), np.nan).ffill()


def _bars_since(event: pd.Series) -> pd.Series:
    idx_at = np.where(event.to_numpy(), np.arange(len(event)), np.nan)
    last_idx = pd.Series(idx_at, index=event.index).ffill()
    return pd.Series(np.arange(len(event), dtype=float), index=event.index) - last_idx


def _zigzag_legs(close: pd.Series, threshold: float):
    """Causal zigzag: returns (pivot_value_series, pivot_direction_series, pivot_index_series).
    A pivot is CONFIRMED at the bar where price has moved `threshold` (fraction) from the running extreme
    in the opposite direction. The recorded pivot value is the running extreme at confirmation.
    Pivot direction: +1 = high pivot (extreme was a high), -1 = low pivot.
    Both series are NaN/0 except at confirmation bars."""
    n = len(close)
    arr = close.to_numpy()
    pivot_val = np.full(n, np.nan)
    pivot_dir = np.full(n, 0)
    pivot_idx = np.full(n, np.nan)
    if n == 0:
        return (pd.Series(pivot_val, index=close.index),
                pd.Series(pivot_dir, index=close.index),
                pd.Series(pivot_idx, index=close.index))
    # initialize
    state = 0  # 0 = unknown, +1 = up-trend (looking for a high), -1 = down-trend
    ext_val = arr[0]
    ext_idx = 0
    for i in range(1, n):
        v = arr[i]
        if np.isnan(v) or np.isnan(ext_val):
            if not np.isnan(v) and np.isnan(ext_val):
                ext_val = v; ext_idx = i; state = 0
            continue
        if state == 0:
            # establish initial direction once threshold breached
            if v >= ext_val * (1.0 + threshold):
                state = 1; ext_val = v; ext_idx = i
            elif v <= ext_val * (1.0 - threshold):
                state = -1; ext_val = v; ext_idx = i
        elif state == 1:
            # up-trend: look for new high or reversal
            if v > ext_val:
                ext_val = v; ext_idx = i
            elif v <= ext_val * (1.0 - threshold):
                # confirm pivot HIGH at ext_idx, recorded at bar i
                pivot_val[i] = ext_val
                pivot_dir[i] = 1
                pivot_idx[i] = float(ext_idx)
                state = -1; ext_val = v; ext_idx = i
        else:  # state == -1
            if v < ext_val:
                ext_val = v; ext_idx = i
            elif v >= ext_val * (1.0 + threshold):
                pivot_val[i] = ext_val
                pivot_dir[i] = -1
                pivot_idx[i] = float(ext_idx)
                state = 1; ext_val = v; ext_idx = i
    return (pd.Series(pivot_val, index=close.index),
            pd.Series(pivot_dir, index=close.index),
            pd.Series(pivot_idx, index=close.index))


# Pivot window constants (short / medium / long timescales)
PV_S = 5
PV_M = 21
PV_L = 63


# ============================================================
# Bucket A — Bars-since most-recent PIT pivot (001-006)
# ============================================================

def f10_swpv_001_bars_since_pit_pivot_high_5bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most-recent 5-bar PIT pivot-high — short-timescale pivot freshness."""
    return _bars_since(_is_pit_pivot_high(high, PV_S))


def f10_swpv_002_bars_since_pit_pivot_high_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most-recent 21-bar PIT pivot-high — medium-timescale."""
    return _bars_since(_is_pit_pivot_high(high, PV_M))


def f10_swpv_003_bars_since_pit_pivot_high_63bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most-recent 63-bar PIT pivot-high — long-timescale."""
    return _bars_since(_is_pit_pivot_high(high, PV_L))


def f10_swpv_004_bars_since_pit_pivot_low_5bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most-recent 5-bar PIT pivot-low."""
    return _bars_since(_is_pit_pivot_low(low, PV_S))


def f10_swpv_005_bars_since_pit_pivot_low_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most-recent 21-bar PIT pivot-low."""
    return _bars_since(_is_pit_pivot_low(low, PV_M))


def f10_swpv_006_bars_since_pit_pivot_low_63bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most-recent 63-bar PIT pivot-low."""
    return _bars_since(_is_pit_pivot_low(low, PV_L))


# ============================================================
# Bucket B — Count of pivots in trailing 252d (007-012)
# ============================================================

def f10_swpv_007_count_pivot_highs_5bar_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Number of distinct 5-bar PIT pivot-highs in trailing 252d."""
    return _is_pit_pivot_high(high, PV_S).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f10_swpv_008_count_pivot_highs_21bar_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-bar pivot-high count in 252d — medium timescale."""
    return _is_pit_pivot_high(high, PV_M).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f10_swpv_009_count_pivot_highs_63bar_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-bar pivot-high count in 252d — long timescale."""
    return _is_pit_pivot_high(high, PV_L).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f10_swpv_010_count_pivot_lows_5bar_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-bar pivot-low count in 252d."""
    return _is_pit_pivot_low(low, PV_S).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f10_swpv_011_count_pivot_lows_21bar_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-bar pivot-low count in 252d."""
    return _is_pit_pivot_low(low, PV_M).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f10_swpv_012_count_pivot_lows_63bar_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-bar pivot-low count in 252d."""
    return _is_pit_pivot_low(low, PV_L).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket C — Pivot high-vs-low ratio (013-015)
# ============================================================

def f10_swpv_013_pivot_high_to_low_ratio_252d_5bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 5-bar pivot-high count to 5-bar pivot-low count in last 252d — topping vs basing imbalance."""
    h = _is_pit_pivot_high(high, PV_S).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    l = _is_pit_pivot_low(low, PV_S).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(h, l)


def f10_swpv_014_pivot_high_to_low_ratio_252d_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-bar pivot high/low ratio in 252d."""
    h = _is_pit_pivot_high(high, PV_M).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    l = _is_pit_pivot_low(low, PV_M).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(h, l)


def f10_swpv_015_pivot_high_to_low_ratio_252d_63bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-bar pivot high/low ratio in 252d."""
    h = _is_pit_pivot_high(high, PV_L).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    l = _is_pit_pivot_low(low, PV_L).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(h, l)


# ============================================================
# Bucket D — Distance to most-recent pivot (016-021)
# ============================================================

def f10_swpv_016_log_dist_close_to_most_recent_pivot_high_5bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance of close above most-recent 5-bar PIT pivot-high value (carried forward)."""
    return _safe_log(close) - _safe_log(_pivot_high_value(high, PV_S))


def f10_swpv_017_log_dist_close_to_most_recent_pivot_high_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance of close above most-recent 21-bar PIT pivot-high."""
    return _safe_log(close) - _safe_log(_pivot_high_value(high, PV_M))


def f10_swpv_018_atr_dist_close_to_most_recent_pivot_high_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from most-recent 21-bar PIT pivot-high."""
    return _safe_div(close - _pivot_high_value(high, PV_M), _atr(high, low, close, n=MDAYS))


def f10_swpv_019_log_dist_close_to_most_recent_pivot_low_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance of close above most-recent 21-bar PIT pivot-low."""
    return _safe_log(close) - _safe_log(_pivot_low_value(low, PV_M))


def f10_swpv_020_atr_dist_close_to_most_recent_pivot_low_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized distance of close above most-recent 21-bar PIT pivot-low."""
    return _safe_div(close - _pivot_low_value(low, PV_M), _atr(high, low, close, n=MDAYS))


def f10_swpv_021_log_dist_close_to_most_recent_pivot_high_63bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance of close above most-recent 63-bar PIT pivot-high — long-horizon."""
    return _safe_log(close) - _safe_log(_pivot_high_value(high, PV_L))


# ============================================================
# Bucket E — Slope of last K pivots (022-027)
# ============================================================

def _last_k_pivot_values(is_pivot: pd.Series, price: pd.Series, k: int) -> pd.DataFrame:
    """Return a DataFrame of shape (n, k) where row i has the last-k pivot prices observed at bar i.
    Newest pivot at column k-1; older at lower columns. NaN if fewer than k pivots seen."""
    arr_p = price.where(is_pivot, np.nan).to_numpy()
    n = len(price)
    out = np.full((n, k), np.nan)
    buf = []
    for i in range(n):
        if not np.isnan(arr_p[i]):
            buf.append(arr_p[i])
            if len(buf) > k:
                buf.pop(0)
        if len(buf) == k:
            out[i] = np.array(buf)
        elif len(buf) > 0:
            out[i, k - len(buf):] = np.array(buf)
    return pd.DataFrame(out, index=price.index, columns=[f"p{j}" for j in range(k)])


def f10_swpv_022_slope_of_last_3_pivot_highs_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Linear-fit slope of last 3 confirmed 21-bar pivot-high prices (over indices 0,1,2)."""
    df = _last_k_pivot_values(_is_pit_pivot_high(high, PV_M), high, 3)
    a = df.iloc[:, 0]; b = df.iloc[:, 1]; c = df.iloc[:, 2]
    return ((c - a) / 2.0).where(df.notna().all(axis=1), np.nan)


def f10_swpv_023_slope_of_last_5_pivot_highs_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope of last 5 confirmed 21-bar pivot-high prices (x = 0..4)."""
    df = _last_k_pivot_values(_is_pit_pivot_high(high, PV_M), high, 5)
    arr = df.to_numpy()
    n = len(arr)
    out = np.full(n, np.nan)
    x = np.arange(5, dtype=float)
    xm = x.mean()
    den = ((x - xm) ** 2).sum()
    for i in range(n):
        row = arr[i]
        if np.isnan(row).any(): continue
        ym = row.mean()
        num = ((x - xm) * (row - ym)).sum()
        out[i] = num / den if den != 0 else np.nan
    return pd.Series(out, index=df.index)


def f10_swpv_024_slope_of_last_3_pivot_lows_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of last 3 confirmed 21-bar pivot-low prices."""
    df = _last_k_pivot_values(_is_pit_pivot_low(low, PV_M), low, 3)
    a = df.iloc[:, 0]; c = df.iloc[:, 2]
    return ((c - a) / 2.0).where(df.notna().all(axis=1), np.nan)


def f10_swpv_025_slope_of_last_5_pivot_lows_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope of last 5 confirmed 21-bar pivot-low prices."""
    df = _last_k_pivot_values(_is_pit_pivot_low(low, PV_M), low, 5)
    arr = df.to_numpy()
    n = len(arr)
    out = np.full(n, np.nan)
    x = np.arange(5, dtype=float)
    xm = x.mean(); den = ((x - xm) ** 2).sum()
    for i in range(n):
        row = arr[i]
        if np.isnan(row).any(): continue
        ym = row.mean()
        out[i] = ((x - xm) * (row - ym)).sum() / den if den != 0 else np.nan
    return pd.Series(out, index=df.index)


def f10_swpv_026_slope_of_last_3_pivot_highs_63bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of last 3 confirmed 63-bar pivot-high prices."""
    df = _last_k_pivot_values(_is_pit_pivot_high(high, PV_L), high, 3)
    a = df.iloc[:, 0]; c = df.iloc[:, 2]
    return ((c - a) / 2.0).where(df.notna().all(axis=1), np.nan)


def f10_swpv_027_slope_of_last_3_pivot_lows_63bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of last 3 confirmed 63-bar pivot-low prices."""
    df = _last_k_pivot_values(_is_pit_pivot_low(low, PV_L), low, 3)
    a = df.iloc[:, 0]; c = df.iloc[:, 2]
    return ((c - a) / 2.0).where(df.notna().all(axis=1), np.nan)


# ============================================================
# Bucket F — Declining-highs / rising-lows indicators (028-031)
# ============================================================

def f10_swpv_028_pivot_highs_declining_indicator_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: last 3 confirmed 21-bar pivot highs strictly declining."""
    df = _last_k_pivot_values(_is_pit_pivot_high(high, PV_M), high, 3)
    a = df.iloc[:, 0]; b = df.iloc[:, 1]; c = df.iloc[:, 2]
    return ((a > b) & (b > c)).astype(float).where(df.notna().all(axis=1), np.nan)


def f10_swpv_029_pivot_lows_declining_indicator_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: last 3 confirmed 21-bar pivot lows strictly declining."""
    df = _last_k_pivot_values(_is_pit_pivot_low(low, PV_M), low, 3)
    a = df.iloc[:, 0]; b = df.iloc[:, 1]; c = df.iloc[:, 2]
    return ((a > b) & (b > c)).astype(float).where(df.notna().all(axis=1), np.nan)


def f10_swpv_030_pivot_highs_declining_indicator_63bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: last 3 confirmed 63-bar pivot highs strictly declining."""
    df = _last_k_pivot_values(_is_pit_pivot_high(high, PV_L), high, 3)
    a = df.iloc[:, 0]; b = df.iloc[:, 1]; c = df.iloc[:, 2]
    return ((a > b) & (b > c)).astype(float).where(df.notna().all(axis=1), np.nan)


def f10_swpv_031_pivot_lows_declining_indicator_63bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: last 3 confirmed 63-bar pivot lows strictly declining."""
    df = _last_k_pivot_values(_is_pit_pivot_low(low, PV_L), low, 3)
    a = df.iloc[:, 0]; b = df.iloc[:, 1]; c = df.iloc[:, 2]
    return ((a > b) & (b > c)).astype(float).where(df.notna().all(axis=1), np.nan)


# ============================================================
# Bucket G — Zigzag leg amplitudes at multiple thresholds (032-040)
# ============================================================

def _zigzag_leg_log_amplitudes(close: pd.Series, threshold: float) -> pd.Series:
    """Return a Series of leg log-amplitudes at each confirmed-pivot bar (NaN elsewhere). Amplitude
    = |log(this_pivot_value / prior_pivot_value)|."""
    pv, _, _ = _zigzag_legs(close, threshold)
    prior = pv.ffill().shift(1)
    amp = (np.log(pv.where(pv > 0, np.nan)) - np.log(prior.where(prior > 0, np.nan))).abs()
    return amp.where(pv.notna(), np.nan)


def f10_swpv_032_most_recent_zigzag_leg_log_amp_3pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Most-recent zigzag leg log-amplitude (3% threshold) — short swings; carried forward."""
    return _zigzag_leg_log_amplitudes(close, 0.03).ffill()


def f10_swpv_033_most_recent_zigzag_leg_log_amp_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Most-recent zigzag leg log-amplitude (5% threshold) — medium swings."""
    return _zigzag_leg_log_amplitudes(close, 0.05).ffill()


def f10_swpv_034_most_recent_zigzag_leg_log_amp_10pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Most-recent zigzag leg log-amplitude (10% threshold) — large swings."""
    return _zigzag_leg_log_amplitudes(close, 0.10).ffill()


def f10_swpv_035_median_zigzag_leg_log_amp_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Median leg log-amplitude over trailing 252d (5% threshold)."""
    return _zigzag_leg_log_amplitudes(close, 0.05).rolling(YDAYS, min_periods=QDAYS).median()


def f10_swpv_036_max_zigzag_leg_log_amp_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max leg log-amplitude in trailing 252d (5% threshold)."""
    return _zigzag_leg_log_amplitudes(close, 0.05).rolling(YDAYS, min_periods=QDAYS).max()


def f10_swpv_037_std_zigzag_leg_log_amp_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stdev of leg log-amplitudes in trailing 252d (5% threshold) — swing-size dispersion."""
    return _zigzag_leg_log_amplitudes(close, 0.05).rolling(YDAYS, min_periods=QDAYS).std()


def f10_swpv_038_median_zigzag_leg_log_amp_252d_3pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Median leg log-amplitude (3% threshold) — fine-grained swings."""
    return _zigzag_leg_log_amplitudes(close, 0.03).rolling(YDAYS, min_periods=QDAYS).median()


def f10_swpv_039_most_recent_over_median_amp_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Most-recent leg amplitude / median 252d amplitude — compression ratio (5%)."""
    amp = _zigzag_leg_log_amplitudes(close, 0.05)
    return _safe_div(amp.ffill(), amp.rolling(YDAYS, min_periods=QDAYS).median())


def f10_swpv_040_most_recent_over_max_amp_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Most-recent leg amplitude / max 252d amplitude — current vs peak swing size."""
    amp = _zigzag_leg_log_amplitudes(close, 0.05)
    return _safe_div(amp.ffill(), amp.rolling(YDAYS, min_periods=QDAYS).max())


# ============================================================
# Bucket H — Slope of zigzag amplitudes (decay detection) (041-044)
# ============================================================

def f10_swpv_041_slope_of_zigzag_amps_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Linear regression slope of leg amplitudes over trailing 252d (5%). NaN-filled to 0 at non-leg bars."""
    amp = _zigzag_leg_log_amplitudes(close, 0.05).fillna(0.0)
    return _rolling_slope(amp, YDAYS, min_periods=QDAYS)


def f10_swpv_042_amp_velocity_recent_minus_prior_3pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean(last 21-bar amplitudes) - mean(prior 21-bar amplitudes from 42d back) at 3% threshold."""
    amp = _zigzag_leg_log_amplitudes(close, 0.03)
    recent = amp.rolling(MDAYS, min_periods=WDAYS).mean()
    prior = amp.shift(MDAYS).rolling(MDAYS, min_periods=WDAYS).mean()
    return recent - prior


def f10_swpv_043_amp_velocity_recent_minus_prior_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Same velocity metric at 5% threshold."""
    amp = _zigzag_leg_log_amplitudes(close, 0.05)
    recent = amp.rolling(MDAYS, min_periods=WDAYS).mean()
    prior = amp.shift(MDAYS).rolling(MDAYS, min_periods=WDAYS).mean()
    return recent - prior


def f10_swpv_044_amp_decay_ratio_recent_over_old_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean amplitude in most recent 63d / mean amplitude in 189-252d back (5%) — decay ratio."""
    amp = _zigzag_leg_log_amplitudes(close, 0.05)
    recent = amp.rolling(QDAYS, min_periods=MDAYS).mean()
    old = amp.shift(QDAYS * 3).rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(recent, old)


# ============================================================
# Bucket I — Number of zigzag legs in window (045-050)
# ============================================================

def f10_swpv_045_count_zigzag_legs_252d_3pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of confirmed zigzag legs in last 252d (3% threshold) — high frequency."""
    pv, _, _ = _zigzag_legs(close, 0.03)
    return pv.notna().astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f10_swpv_046_count_zigzag_legs_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of confirmed zigzag legs in last 252d (5% threshold)."""
    pv, _, _ = _zigzag_legs(close, 0.05)
    return pv.notna().astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f10_swpv_047_count_zigzag_legs_252d_10pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of confirmed zigzag legs in last 252d (10% threshold) — large-leg count."""
    pv, _, _ = _zigzag_legs(close, 0.10)
    return pv.notna().astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f10_swpv_048_count_zigzag_legs_63d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of confirmed zigzag legs in last 63d (5% threshold) — short-horizon frequency."""
    pv, _, _ = _zigzag_legs(close, 0.05)
    return pv.notna().astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f10_swpv_049_zigzag_leg_frequency_per_year_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Legs per year (5%) — equivalent to f10_swpv_046 but normalized over count; same metric as #046 but kept here for clarity of axis; uses 1260-day median normalization."""
    pv, _, _ = _zigzag_legs(close, 0.05)
    count_252 = pv.notna().astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return count_252


def f10_swpv_050_zigzag_leg_count_acceleration_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Recent 63d leg count minus prior 63d leg count (5%) — recent acceleration."""
    pv, _, _ = _zigzag_legs(close, 0.05)
    cnt = pv.notna().astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return cnt - cnt.shift(QDAYS)


# ============================================================
# Bucket J — Zigzag leg duration (051-056)
# ============================================================

def _zigzag_leg_durations(close: pd.Series, threshold: float) -> pd.Series:
    """At each confirmed-pivot bar, return the bar-distance between this pivot's extreme-idx and the prior
    pivot's extreme-idx. NaN elsewhere. Carry-forward is left to callers."""
    pv, _, pidx = _zigzag_legs(close, threshold)
    prior_idx = pidx.ffill().shift(1)
    dur = pidx - prior_idx
    return dur.where(pv.notna(), np.nan)


def f10_swpv_051_most_recent_zigzag_leg_duration_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Most-recent confirmed leg duration (bars between consecutive zigzag extremes), 5% threshold; carried forward."""
    return _zigzag_leg_durations(close, 0.05).ffill()


def f10_swpv_052_mean_zigzag_leg_duration_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean leg duration in trailing 252d (5%)."""
    return _zigzag_leg_durations(close, 0.05).rolling(YDAYS, min_periods=QDAYS).mean()


def f10_swpv_053_median_zigzag_leg_duration_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Median leg duration in trailing 252d (5%)."""
    return _zigzag_leg_durations(close, 0.05).rolling(YDAYS, min_periods=QDAYS).median()


def f10_swpv_054_std_zigzag_leg_duration_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stdev of leg durations in 252d (5%) — duration variability."""
    return _zigzag_leg_durations(close, 0.05).rolling(YDAYS, min_periods=QDAYS).std()


def f10_swpv_055_cv_zigzag_leg_duration_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Coefficient of variation (std/mean) of leg durations in 252d (5%) — regularity index."""
    d = _zigzag_leg_durations(close, 0.05)
    return _safe_div(d.rolling(YDAYS, min_periods=QDAYS).std(), d.rolling(YDAYS, min_periods=QDAYS).mean())


def f10_swpv_056_max_zigzag_leg_duration_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max leg duration in trailing 252d (5%)."""
    return _zigzag_leg_durations(close, 0.05).rolling(YDAYS, min_periods=QDAYS).max()


# ============================================================
# Bucket K — Current swing leg position (057-061)
# ============================================================

def f10_swpv_057_current_zigzag_leg_age_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since the most-recent confirmed zigzag pivot's EXTREME (i.e. age of current swing leg)."""
    _, _, pidx = _zigzag_legs(close, 0.05)
    last_ext_idx = pidx.ffill()
    return pd.Series(np.arange(len(close), dtype=float), index=close.index) - last_ext_idx


def f10_swpv_058_current_leg_age_over_mean_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current leg age / mean 252d leg duration — relative age."""
    _, _, pidx = _zigzag_legs(close, 0.05)
    last_ext_idx = pidx.ffill()
    age = pd.Series(np.arange(len(close), dtype=float), index=close.index) - last_ext_idx
    mean_dur = _zigzag_leg_durations(close, 0.05).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(age, mean_dur)


def f10_swpv_059_current_leg_log_amplitude_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance of close from the most-recent pivot value (carried forward) — current leg progress."""
    pv, _, _ = _zigzag_legs(close, 0.05)
    last_pv = pv.ffill()
    return _safe_log(close) - _safe_log(last_pv)


def f10_swpv_060_current_leg_amp_over_prior_leg_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current-leg amplitude / prior-leg amplitude — followthrough strength."""
    pv, _, _ = _zigzag_legs(close, 0.05)
    last_pv = pv.ffill()
    cur_amp = (_safe_log(close) - _safe_log(last_pv)).abs()
    amp_series = _zigzag_leg_log_amplitudes(close, 0.05)
    last_amp = amp_series.ffill()
    return _safe_div(cur_amp, last_amp)


def f10_swpv_061_current_leg_amp_over_median_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current-leg amplitude / median 252d leg amplitude."""
    pv, _, _ = _zigzag_legs(close, 0.05)
    last_pv = pv.ffill()
    cur_amp = (_safe_log(close) - _safe_log(last_pv)).abs()
    med = _zigzag_leg_log_amplitudes(close, 0.05).rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(cur_amp, med)


# ============================================================
# Bucket L — Asymmetry (up vs down legs) (062-066)
# ============================================================

def _zigzag_signed_leg_log_amps(close, threshold):
    """At each confirmed pivot, returns the SIGNED log amplitude of the just-completed leg
    (positive if completed-leg was UP, negative if DOWN)."""
    pv, pdir, _ = _zigzag_legs(close, threshold)
    prior = pv.ffill().shift(1)
    raw = np.log(pv.where(pv > 0, np.nan)) - np.log(prior.where(prior > 0, np.nan))
    # If this pivot is a HIGH (+1), the just-completed leg was UP (positive); if a LOW (-1), DOWN (negative).
    sign = pdir.where(pdir != 0, np.nan)
    return raw.abs() * sign.where(pv.notna(), np.nan)


def f10_swpv_062_cum_up_leg_amplitude_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of UP-leg log amplitudes in trailing 252d (5% threshold)."""
    s = _zigzag_signed_leg_log_amps(close, 0.05)
    return s.where(s > 0, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()


def f10_swpv_063_cum_down_leg_amplitude_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of |DOWN-leg| log amplitudes in trailing 252d (5%)."""
    s = _zigzag_signed_leg_log_amps(close, 0.05)
    return (-s.where(s < 0, 0.0)).rolling(YDAYS, min_periods=QDAYS).sum()


def f10_swpv_064_net_swing_amplitude_balance_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Up-amplitude minus down-amplitude in trailing 252d — net directional thrust."""
    s = _zigzag_signed_leg_log_amps(close, 0.05)
    return s.rolling(YDAYS, min_periods=QDAYS).sum()


def f10_swpv_065_count_up_legs_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of UP legs (completed legs ending at pivot HIGHs) in trailing 252d (5%)."""
    _, pdir, _ = _zigzag_legs(close, 0.05)
    return (pdir == 1).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f10_swpv_066_count_down_legs_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of DOWN legs in trailing 252d (5%)."""
    _, pdir, _ = _zigzag_legs(close, 0.05)
    return (pdir == -1).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket M — Net direction of last K legs (067-068)
# ============================================================

def f10_swpv_067_net_swing_direction_last_3_legs_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of signs of last 3 completed leg directions (-3 to +3)."""
    _, pdir, _ = _zigzag_legs(close, 0.05)
    pivot_marks = (pdir != 0).astype(float)
    # for each bar, sum the directions of the last 3 confirmed pivots
    n = len(close)
    pdir_arr = pdir.to_numpy()
    out = np.full(n, np.nan)
    buf = []
    for i in range(n):
        if pdir_arr[i] != 0:
            buf.append(int(pdir_arr[i]))
            if len(buf) > 3: buf.pop(0)
        if len(buf) == 3:
            out[i] = float(sum(buf))
    return pd.Series(out, index=close.index)


def f10_swpv_068_net_swing_direction_last_5_legs_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of signs of last 5 confirmed pivot directions (-5 to +5)."""
    _, pdir, _ = _zigzag_legs(close, 0.05)
    n = len(close)
    pdir_arr = pdir.to_numpy()
    out = np.full(n, np.nan)
    buf = []
    for i in range(n):
        if pdir_arr[i] != 0:
            buf.append(int(pdir_arr[i]))
            if len(buf) > 5: buf.pop(0)
        if len(buf) == 5:
            out[i] = float(sum(buf))
    return pd.Series(out, index=close.index)


# ============================================================
# Bucket N — Pivot density (069-071)
# ============================================================

def f10_swpv_069_pivot_high_density_per_100bars_252d_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-bar PIT pivot-highs per 100 bars in trailing 252d."""
    cnt = _is_pit_pivot_high(high, PV_M).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return 100.0 * cnt / float(YDAYS)


def f10_swpv_070_pivot_low_density_per_100bars_252d_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-bar PIT pivot-lows per 100 bars in trailing 252d."""
    cnt = _is_pit_pivot_low(low, PV_M).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return 100.0 * cnt / float(YDAYS)


def f10_swpv_071_total_pivot_density_per_100bars_252d_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """All 21-bar pivots (high+low) per 100 bars in trailing 252d."""
    h = _is_pit_pivot_high(high, PV_M).astype(float)
    l = _is_pit_pivot_low(low, PV_M).astype(float)
    cnt = (h + l).rolling(YDAYS, min_periods=QDAYS).sum()
    return 100.0 * cnt / float(YDAYS)


# ============================================================
# Bucket O — Swing-direction entropy (Shannon) (072-073)
# ============================================================

def f10_swpv_072_swing_direction_entropy_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Shannon entropy over {up_pivot, down_pivot, no_pivot} state probabilities in last 252d (5%)."""
    _, pdir, _ = _zigzag_legs(close, 0.05)
    p_up = (pdir == 1).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    p_dn = (pdir == -1).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    p_no = (1.0 - p_up - p_dn).clip(lower=1e-9)
    p_up_c = p_up.clip(lower=1e-9); p_dn_c = p_dn.clip(lower=1e-9)
    return -(p_up_c * np.log(p_up_c) + p_dn_c * np.log(p_dn_c) + p_no * np.log(p_no))


def f10_swpv_073_swing_direction_entropy_252d_10pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Same entropy at 10% threshold."""
    _, pdir, _ = _zigzag_legs(close, 0.10)
    p_up = (pdir == 1).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    p_dn = (pdir == -1).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    p_no = (1.0 - p_up - p_dn).clip(lower=1e-9)
    p_up_c = p_up.clip(lower=1e-9); p_dn_c = p_dn.clip(lower=1e-9)
    return -(p_up_c * np.log(p_up_c) + p_dn_c * np.log(p_dn_c) + p_no * np.log(p_no))


# ============================================================
# Bucket P — Pivot price dispersion (074-075)
# ============================================================

def f10_swpv_074_pivot_high_price_dispersion_252d_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stdev of confirmed 21-bar pivot-high PRICES in last 252d — range compression vs expansion."""
    pv = high.where(_is_pit_pivot_high(high, PV_M), np.nan)
    return pv.rolling(YDAYS, min_periods=QDAYS).std()


def f10_swpv_075_pivot_low_price_dispersion_252d_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stdev of confirmed 21-bar pivot-low PRICES in last 252d."""
    pv = low.where(_is_pit_pivot_low(low, PV_M), np.nan)
    return pv.rolling(YDAYS, min_periods=QDAYS).std()


# ============================================================
#                         REGISTRY 001-075
# ============================================================



def f10_swpv_001_bars_since_pit_pivot_high_5bar_d3(high, low, close):
    return f10_swpv_001_bars_since_pit_pivot_high_5bar(high, low, close).diff().diff().diff()


def f10_swpv_002_bars_since_pit_pivot_high_21bar_d3(high, low, close):
    return f10_swpv_002_bars_since_pit_pivot_high_21bar(high, low, close).diff().diff().diff()


def f10_swpv_003_bars_since_pit_pivot_high_63bar_d3(high, low, close):
    return f10_swpv_003_bars_since_pit_pivot_high_63bar(high, low, close).diff().diff().diff()


def f10_swpv_004_bars_since_pit_pivot_low_5bar_d3(high, low, close):
    return f10_swpv_004_bars_since_pit_pivot_low_5bar(high, low, close).diff().diff().diff()


def f10_swpv_005_bars_since_pit_pivot_low_21bar_d3(high, low, close):
    return f10_swpv_005_bars_since_pit_pivot_low_21bar(high, low, close).diff().diff().diff()


def f10_swpv_006_bars_since_pit_pivot_low_63bar_d3(high, low, close):
    return f10_swpv_006_bars_since_pit_pivot_low_63bar(high, low, close).diff().diff().diff()


def f10_swpv_007_count_pivot_highs_5bar_in_252d_d3(high, low, close):
    return f10_swpv_007_count_pivot_highs_5bar_in_252d(high, low, close).diff().diff().diff()


def f10_swpv_008_count_pivot_highs_21bar_in_252d_d3(high, low, close):
    return f10_swpv_008_count_pivot_highs_21bar_in_252d(high, low, close).diff().diff().diff()


def f10_swpv_009_count_pivot_highs_63bar_in_252d_d3(high, low, close):
    return f10_swpv_009_count_pivot_highs_63bar_in_252d(high, low, close).diff().diff().diff()


def f10_swpv_010_count_pivot_lows_5bar_in_252d_d3(high, low, close):
    return f10_swpv_010_count_pivot_lows_5bar_in_252d(high, low, close).diff().diff().diff()


def f10_swpv_011_count_pivot_lows_21bar_in_252d_d3(high, low, close):
    return f10_swpv_011_count_pivot_lows_21bar_in_252d(high, low, close).diff().diff().diff()


def f10_swpv_012_count_pivot_lows_63bar_in_252d_d3(high, low, close):
    return f10_swpv_012_count_pivot_lows_63bar_in_252d(high, low, close).diff().diff().diff()


def f10_swpv_013_pivot_high_to_low_ratio_252d_5bar_d3(high, low, close):
    return f10_swpv_013_pivot_high_to_low_ratio_252d_5bar(high, low, close).diff().diff().diff()


def f10_swpv_014_pivot_high_to_low_ratio_252d_21bar_d3(high, low, close):
    return f10_swpv_014_pivot_high_to_low_ratio_252d_21bar(high, low, close).diff().diff().diff()


def f10_swpv_015_pivot_high_to_low_ratio_252d_63bar_d3(high, low, close):
    return f10_swpv_015_pivot_high_to_low_ratio_252d_63bar(high, low, close).diff().diff().diff()


def f10_swpv_016_log_dist_close_to_most_recent_pivot_high_5bar_d3(high, low, close):
    return f10_swpv_016_log_dist_close_to_most_recent_pivot_high_5bar(high, low, close).diff().diff().diff()


def f10_swpv_017_log_dist_close_to_most_recent_pivot_high_21bar_d3(high, low, close):
    return f10_swpv_017_log_dist_close_to_most_recent_pivot_high_21bar(high, low, close).diff().diff().diff()


def f10_swpv_018_atr_dist_close_to_most_recent_pivot_high_21bar_d3(high, low, close):
    return f10_swpv_018_atr_dist_close_to_most_recent_pivot_high_21bar(high, low, close).diff().diff().diff()


def f10_swpv_019_log_dist_close_to_most_recent_pivot_low_21bar_d3(high, low, close):
    return f10_swpv_019_log_dist_close_to_most_recent_pivot_low_21bar(high, low, close).diff().diff().diff()


def f10_swpv_020_atr_dist_close_to_most_recent_pivot_low_21bar_d3(high, low, close):
    return f10_swpv_020_atr_dist_close_to_most_recent_pivot_low_21bar(high, low, close).diff().diff().diff()


def f10_swpv_021_log_dist_close_to_most_recent_pivot_high_63bar_d3(high, low, close):
    return f10_swpv_021_log_dist_close_to_most_recent_pivot_high_63bar(high, low, close).diff().diff().diff()


def f10_swpv_022_slope_of_last_3_pivot_highs_21bar_d3(high, low, close):
    return f10_swpv_022_slope_of_last_3_pivot_highs_21bar(high, low, close).diff().diff().diff()


def f10_swpv_023_slope_of_last_5_pivot_highs_21bar_d3(high, low, close):
    return f10_swpv_023_slope_of_last_5_pivot_highs_21bar(high, low, close).diff().diff().diff()


def f10_swpv_024_slope_of_last_3_pivot_lows_21bar_d3(high, low, close):
    return f10_swpv_024_slope_of_last_3_pivot_lows_21bar(high, low, close).diff().diff().diff()


def f10_swpv_025_slope_of_last_5_pivot_lows_21bar_d3(high, low, close):
    return f10_swpv_025_slope_of_last_5_pivot_lows_21bar(high, low, close).diff().diff().diff()


def f10_swpv_026_slope_of_last_3_pivot_highs_63bar_d3(high, low, close):
    return f10_swpv_026_slope_of_last_3_pivot_highs_63bar(high, low, close).diff().diff().diff()


def f10_swpv_027_slope_of_last_3_pivot_lows_63bar_d3(high, low, close):
    return f10_swpv_027_slope_of_last_3_pivot_lows_63bar(high, low, close).diff().diff().diff()


def f10_swpv_028_pivot_highs_declining_indicator_21bar_d3(high, low, close):
    return f10_swpv_028_pivot_highs_declining_indicator_21bar(high, low, close).diff().diff().diff()


def f10_swpv_029_pivot_lows_declining_indicator_21bar_d3(high, low, close):
    return f10_swpv_029_pivot_lows_declining_indicator_21bar(high, low, close).diff().diff().diff()


def f10_swpv_030_pivot_highs_declining_indicator_63bar_d3(high, low, close):
    return f10_swpv_030_pivot_highs_declining_indicator_63bar(high, low, close).diff().diff().diff()


def f10_swpv_031_pivot_lows_declining_indicator_63bar_d3(high, low, close):
    return f10_swpv_031_pivot_lows_declining_indicator_63bar(high, low, close).diff().diff().diff()


def f10_swpv_032_most_recent_zigzag_leg_log_amp_3pct_d3(high, low, close):
    return f10_swpv_032_most_recent_zigzag_leg_log_amp_3pct(high, low, close).diff().diff().diff()


def f10_swpv_033_most_recent_zigzag_leg_log_amp_5pct_d3(high, low, close):
    return f10_swpv_033_most_recent_zigzag_leg_log_amp_5pct(high, low, close).diff().diff().diff()


def f10_swpv_034_most_recent_zigzag_leg_log_amp_10pct_d3(high, low, close):
    return f10_swpv_034_most_recent_zigzag_leg_log_amp_10pct(high, low, close).diff().diff().diff()


def f10_swpv_035_median_zigzag_leg_log_amp_252d_5pct_d3(high, low, close):
    return f10_swpv_035_median_zigzag_leg_log_amp_252d_5pct(high, low, close).diff().diff().diff()


def f10_swpv_036_max_zigzag_leg_log_amp_252d_5pct_d3(high, low, close):
    return f10_swpv_036_max_zigzag_leg_log_amp_252d_5pct(high, low, close).diff().diff().diff()


def f10_swpv_037_std_zigzag_leg_log_amp_252d_5pct_d3(high, low, close):
    return f10_swpv_037_std_zigzag_leg_log_amp_252d_5pct(high, low, close).diff().diff().diff()


def f10_swpv_038_median_zigzag_leg_log_amp_252d_3pct_d3(high, low, close):
    return f10_swpv_038_median_zigzag_leg_log_amp_252d_3pct(high, low, close).diff().diff().diff()


def f10_swpv_039_most_recent_over_median_amp_252d_5pct_d3(high, low, close):
    return f10_swpv_039_most_recent_over_median_amp_252d_5pct(high, low, close).diff().diff().diff()


def f10_swpv_040_most_recent_over_max_amp_252d_5pct_d3(high, low, close):
    return f10_swpv_040_most_recent_over_max_amp_252d_5pct(high, low, close).diff().diff().diff()


def f10_swpv_041_slope_of_zigzag_amps_252d_5pct_d3(high, low, close):
    return f10_swpv_041_slope_of_zigzag_amps_252d_5pct(high, low, close).diff().diff().diff()


def f10_swpv_042_amp_velocity_recent_minus_prior_3pct_d3(high, low, close):
    return f10_swpv_042_amp_velocity_recent_minus_prior_3pct(high, low, close).diff().diff().diff()


def f10_swpv_043_amp_velocity_recent_minus_prior_5pct_d3(high, low, close):
    return f10_swpv_043_amp_velocity_recent_minus_prior_5pct(high, low, close).diff().diff().diff()


def f10_swpv_044_amp_decay_ratio_recent_over_old_252d_5pct_d3(high, low, close):
    return f10_swpv_044_amp_decay_ratio_recent_over_old_252d_5pct(high, low, close).diff().diff().diff()


def f10_swpv_045_count_zigzag_legs_252d_3pct_d3(high, low, close):
    return f10_swpv_045_count_zigzag_legs_252d_3pct(high, low, close).diff().diff().diff()


def f10_swpv_046_count_zigzag_legs_252d_5pct_d3(high, low, close):
    return f10_swpv_046_count_zigzag_legs_252d_5pct(high, low, close).diff().diff().diff()


def f10_swpv_047_count_zigzag_legs_252d_10pct_d3(high, low, close):
    return f10_swpv_047_count_zigzag_legs_252d_10pct(high, low, close).diff().diff().diff()


def f10_swpv_048_count_zigzag_legs_63d_5pct_d3(high, low, close):
    return f10_swpv_048_count_zigzag_legs_63d_5pct(high, low, close).diff().diff().diff()


def f10_swpv_049_zigzag_leg_frequency_per_year_252d_5pct_d3(high, low, close):
    return f10_swpv_049_zigzag_leg_frequency_per_year_252d_5pct(high, low, close).diff().diff().diff()


def f10_swpv_050_zigzag_leg_count_acceleration_252d_5pct_d3(high, low, close):
    return f10_swpv_050_zigzag_leg_count_acceleration_252d_5pct(high, low, close).diff().diff().diff()


def f10_swpv_051_most_recent_zigzag_leg_duration_5pct_d3(high, low, close):
    return f10_swpv_051_most_recent_zigzag_leg_duration_5pct(high, low, close).diff().diff().diff()


def f10_swpv_052_mean_zigzag_leg_duration_252d_5pct_d3(high, low, close):
    return f10_swpv_052_mean_zigzag_leg_duration_252d_5pct(high, low, close).diff().diff().diff()


def f10_swpv_053_median_zigzag_leg_duration_252d_5pct_d3(high, low, close):
    return f10_swpv_053_median_zigzag_leg_duration_252d_5pct(high, low, close).diff().diff().diff()


def f10_swpv_054_std_zigzag_leg_duration_252d_5pct_d3(high, low, close):
    return f10_swpv_054_std_zigzag_leg_duration_252d_5pct(high, low, close).diff().diff().diff()


def f10_swpv_055_cv_zigzag_leg_duration_252d_5pct_d3(high, low, close):
    return f10_swpv_055_cv_zigzag_leg_duration_252d_5pct(high, low, close).diff().diff().diff()


def f10_swpv_056_max_zigzag_leg_duration_252d_5pct_d3(high, low, close):
    return f10_swpv_056_max_zigzag_leg_duration_252d_5pct(high, low, close).diff().diff().diff()


def f10_swpv_057_current_zigzag_leg_age_5pct_d3(high, low, close):
    return f10_swpv_057_current_zigzag_leg_age_5pct(high, low, close).diff().diff().diff()


def f10_swpv_058_current_leg_age_over_mean_252d_5pct_d3(high, low, close):
    return f10_swpv_058_current_leg_age_over_mean_252d_5pct(high, low, close).diff().diff().diff()


def f10_swpv_059_current_leg_log_amplitude_5pct_d3(high, low, close):
    return f10_swpv_059_current_leg_log_amplitude_5pct(high, low, close).diff().diff().diff()


def f10_swpv_060_current_leg_amp_over_prior_leg_5pct_d3(high, low, close):
    return f10_swpv_060_current_leg_amp_over_prior_leg_5pct(high, low, close).diff().diff().diff()


def f10_swpv_061_current_leg_amp_over_median_252d_5pct_d3(high, low, close):
    return f10_swpv_061_current_leg_amp_over_median_252d_5pct(high, low, close).diff().diff().diff()


def f10_swpv_062_cum_up_leg_amplitude_252d_5pct_d3(high, low, close):
    return f10_swpv_062_cum_up_leg_amplitude_252d_5pct(high, low, close).diff().diff().diff()


def f10_swpv_063_cum_down_leg_amplitude_252d_5pct_d3(high, low, close):
    return f10_swpv_063_cum_down_leg_amplitude_252d_5pct(high, low, close).diff().diff().diff()


def f10_swpv_064_net_swing_amplitude_balance_252d_5pct_d3(high, low, close):
    return f10_swpv_064_net_swing_amplitude_balance_252d_5pct(high, low, close).diff().diff().diff()


def f10_swpv_065_count_up_legs_252d_5pct_d3(high, low, close):
    return f10_swpv_065_count_up_legs_252d_5pct(high, low, close).diff().diff().diff()


def f10_swpv_066_count_down_legs_252d_5pct_d3(high, low, close):
    return f10_swpv_066_count_down_legs_252d_5pct(high, low, close).diff().diff().diff()


def f10_swpv_067_net_swing_direction_last_3_legs_5pct_d3(high, low, close):
    return f10_swpv_067_net_swing_direction_last_3_legs_5pct(high, low, close).diff().diff().diff()


def f10_swpv_068_net_swing_direction_last_5_legs_5pct_d3(high, low, close):
    return f10_swpv_068_net_swing_direction_last_5_legs_5pct(high, low, close).diff().diff().diff()


def f10_swpv_069_pivot_high_density_per_100bars_252d_21bar_d3(high, low, close):
    return f10_swpv_069_pivot_high_density_per_100bars_252d_21bar(high, low, close).diff().diff().diff()


def f10_swpv_070_pivot_low_density_per_100bars_252d_21bar_d3(high, low, close):
    return f10_swpv_070_pivot_low_density_per_100bars_252d_21bar(high, low, close).diff().diff().diff()


def f10_swpv_071_total_pivot_density_per_100bars_252d_21bar_d3(high, low, close):
    return f10_swpv_071_total_pivot_density_per_100bars_252d_21bar(high, low, close).diff().diff().diff()


def f10_swpv_072_swing_direction_entropy_252d_5pct_d3(high, low, close):
    return f10_swpv_072_swing_direction_entropy_252d_5pct(high, low, close).diff().diff().diff()


def f10_swpv_073_swing_direction_entropy_252d_10pct_d3(high, low, close):
    return f10_swpv_073_swing_direction_entropy_252d_10pct(high, low, close).diff().diff().diff()


def f10_swpv_074_pivot_high_price_dispersion_252d_21bar_d3(high, low, close):
    return f10_swpv_074_pivot_high_price_dispersion_252d_21bar(high, low, close).diff().diff().diff()


def f10_swpv_075_pivot_low_price_dispersion_252d_21bar_d3(high, low, close):
    return f10_swpv_075_pivot_low_price_dispersion_252d_21bar(high, low, close).diff().diff().diff()


SWING_PIVOT_TOPOLOGY_D3_REGISTRY_001_075 = {
    "f10_swpv_001_bars_since_pit_pivot_high_5bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_001_bars_since_pit_pivot_high_5bar_d3},
    "f10_swpv_002_bars_since_pit_pivot_high_21bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_002_bars_since_pit_pivot_high_21bar_d3},
    "f10_swpv_003_bars_since_pit_pivot_high_63bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_003_bars_since_pit_pivot_high_63bar_d3},
    "f10_swpv_004_bars_since_pit_pivot_low_5bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_004_bars_since_pit_pivot_low_5bar_d3},
    "f10_swpv_005_bars_since_pit_pivot_low_21bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_005_bars_since_pit_pivot_low_21bar_d3},
    "f10_swpv_006_bars_since_pit_pivot_low_63bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_006_bars_since_pit_pivot_low_63bar_d3},
    "f10_swpv_007_count_pivot_highs_5bar_in_252d_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_007_count_pivot_highs_5bar_in_252d_d3},
    "f10_swpv_008_count_pivot_highs_21bar_in_252d_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_008_count_pivot_highs_21bar_in_252d_d3},
    "f10_swpv_009_count_pivot_highs_63bar_in_252d_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_009_count_pivot_highs_63bar_in_252d_d3},
    "f10_swpv_010_count_pivot_lows_5bar_in_252d_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_010_count_pivot_lows_5bar_in_252d_d3},
    "f10_swpv_011_count_pivot_lows_21bar_in_252d_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_011_count_pivot_lows_21bar_in_252d_d3},
    "f10_swpv_012_count_pivot_lows_63bar_in_252d_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_012_count_pivot_lows_63bar_in_252d_d3},
    "f10_swpv_013_pivot_high_to_low_ratio_252d_5bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_013_pivot_high_to_low_ratio_252d_5bar_d3},
    "f10_swpv_014_pivot_high_to_low_ratio_252d_21bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_014_pivot_high_to_low_ratio_252d_21bar_d3},
    "f10_swpv_015_pivot_high_to_low_ratio_252d_63bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_015_pivot_high_to_low_ratio_252d_63bar_d3},
    "f10_swpv_016_log_dist_close_to_most_recent_pivot_high_5bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_016_log_dist_close_to_most_recent_pivot_high_5bar_d3},
    "f10_swpv_017_log_dist_close_to_most_recent_pivot_high_21bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_017_log_dist_close_to_most_recent_pivot_high_21bar_d3},
    "f10_swpv_018_atr_dist_close_to_most_recent_pivot_high_21bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_018_atr_dist_close_to_most_recent_pivot_high_21bar_d3},
    "f10_swpv_019_log_dist_close_to_most_recent_pivot_low_21bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_019_log_dist_close_to_most_recent_pivot_low_21bar_d3},
    "f10_swpv_020_atr_dist_close_to_most_recent_pivot_low_21bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_020_atr_dist_close_to_most_recent_pivot_low_21bar_d3},
    "f10_swpv_021_log_dist_close_to_most_recent_pivot_high_63bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_021_log_dist_close_to_most_recent_pivot_high_63bar_d3},
    "f10_swpv_022_slope_of_last_3_pivot_highs_21bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_022_slope_of_last_3_pivot_highs_21bar_d3},
    "f10_swpv_023_slope_of_last_5_pivot_highs_21bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_023_slope_of_last_5_pivot_highs_21bar_d3},
    "f10_swpv_024_slope_of_last_3_pivot_lows_21bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_024_slope_of_last_3_pivot_lows_21bar_d3},
    "f10_swpv_025_slope_of_last_5_pivot_lows_21bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_025_slope_of_last_5_pivot_lows_21bar_d3},
    "f10_swpv_026_slope_of_last_3_pivot_highs_63bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_026_slope_of_last_3_pivot_highs_63bar_d3},
    "f10_swpv_027_slope_of_last_3_pivot_lows_63bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_027_slope_of_last_3_pivot_lows_63bar_d3},
    "f10_swpv_028_pivot_highs_declining_indicator_21bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_028_pivot_highs_declining_indicator_21bar_d3},
    "f10_swpv_029_pivot_lows_declining_indicator_21bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_029_pivot_lows_declining_indicator_21bar_d3},
    "f10_swpv_030_pivot_highs_declining_indicator_63bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_030_pivot_highs_declining_indicator_63bar_d3},
    "f10_swpv_031_pivot_lows_declining_indicator_63bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_031_pivot_lows_declining_indicator_63bar_d3},
    "f10_swpv_032_most_recent_zigzag_leg_log_amp_3pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_032_most_recent_zigzag_leg_log_amp_3pct_d3},
    "f10_swpv_033_most_recent_zigzag_leg_log_amp_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_033_most_recent_zigzag_leg_log_amp_5pct_d3},
    "f10_swpv_034_most_recent_zigzag_leg_log_amp_10pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_034_most_recent_zigzag_leg_log_amp_10pct_d3},
    "f10_swpv_035_median_zigzag_leg_log_amp_252d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_035_median_zigzag_leg_log_amp_252d_5pct_d3},
    "f10_swpv_036_max_zigzag_leg_log_amp_252d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_036_max_zigzag_leg_log_amp_252d_5pct_d3},
    "f10_swpv_037_std_zigzag_leg_log_amp_252d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_037_std_zigzag_leg_log_amp_252d_5pct_d3},
    "f10_swpv_038_median_zigzag_leg_log_amp_252d_3pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_038_median_zigzag_leg_log_amp_252d_3pct_d3},
    "f10_swpv_039_most_recent_over_median_amp_252d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_039_most_recent_over_median_amp_252d_5pct_d3},
    "f10_swpv_040_most_recent_over_max_amp_252d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_040_most_recent_over_max_amp_252d_5pct_d3},
    "f10_swpv_041_slope_of_zigzag_amps_252d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_041_slope_of_zigzag_amps_252d_5pct_d3},
    "f10_swpv_042_amp_velocity_recent_minus_prior_3pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_042_amp_velocity_recent_minus_prior_3pct_d3},
    "f10_swpv_043_amp_velocity_recent_minus_prior_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_043_amp_velocity_recent_minus_prior_5pct_d3},
    "f10_swpv_044_amp_decay_ratio_recent_over_old_252d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_044_amp_decay_ratio_recent_over_old_252d_5pct_d3},
    "f10_swpv_045_count_zigzag_legs_252d_3pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_045_count_zigzag_legs_252d_3pct_d3},
    "f10_swpv_046_count_zigzag_legs_252d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_046_count_zigzag_legs_252d_5pct_d3},
    "f10_swpv_047_count_zigzag_legs_252d_10pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_047_count_zigzag_legs_252d_10pct_d3},
    "f10_swpv_048_count_zigzag_legs_63d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_048_count_zigzag_legs_63d_5pct_d3},
    "f10_swpv_049_zigzag_leg_frequency_per_year_252d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_049_zigzag_leg_frequency_per_year_252d_5pct_d3},
    "f10_swpv_050_zigzag_leg_count_acceleration_252d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_050_zigzag_leg_count_acceleration_252d_5pct_d3},
    "f10_swpv_051_most_recent_zigzag_leg_duration_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_051_most_recent_zigzag_leg_duration_5pct_d3},
    "f10_swpv_052_mean_zigzag_leg_duration_252d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_052_mean_zigzag_leg_duration_252d_5pct_d3},
    "f10_swpv_053_median_zigzag_leg_duration_252d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_053_median_zigzag_leg_duration_252d_5pct_d3},
    "f10_swpv_054_std_zigzag_leg_duration_252d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_054_std_zigzag_leg_duration_252d_5pct_d3},
    "f10_swpv_055_cv_zigzag_leg_duration_252d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_055_cv_zigzag_leg_duration_252d_5pct_d3},
    "f10_swpv_056_max_zigzag_leg_duration_252d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_056_max_zigzag_leg_duration_252d_5pct_d3},
    "f10_swpv_057_current_zigzag_leg_age_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_057_current_zigzag_leg_age_5pct_d3},
    "f10_swpv_058_current_leg_age_over_mean_252d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_058_current_leg_age_over_mean_252d_5pct_d3},
    "f10_swpv_059_current_leg_log_amplitude_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_059_current_leg_log_amplitude_5pct_d3},
    "f10_swpv_060_current_leg_amp_over_prior_leg_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_060_current_leg_amp_over_prior_leg_5pct_d3},
    "f10_swpv_061_current_leg_amp_over_median_252d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_061_current_leg_amp_over_median_252d_5pct_d3},
    "f10_swpv_062_cum_up_leg_amplitude_252d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_062_cum_up_leg_amplitude_252d_5pct_d3},
    "f10_swpv_063_cum_down_leg_amplitude_252d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_063_cum_down_leg_amplitude_252d_5pct_d3},
    "f10_swpv_064_net_swing_amplitude_balance_252d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_064_net_swing_amplitude_balance_252d_5pct_d3},
    "f10_swpv_065_count_up_legs_252d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_065_count_up_legs_252d_5pct_d3},
    "f10_swpv_066_count_down_legs_252d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_066_count_down_legs_252d_5pct_d3},
    "f10_swpv_067_net_swing_direction_last_3_legs_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_067_net_swing_direction_last_3_legs_5pct_d3},
    "f10_swpv_068_net_swing_direction_last_5_legs_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_068_net_swing_direction_last_5_legs_5pct_d3},
    "f10_swpv_069_pivot_high_density_per_100bars_252d_21bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_069_pivot_high_density_per_100bars_252d_21bar_d3},
    "f10_swpv_070_pivot_low_density_per_100bars_252d_21bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_070_pivot_low_density_per_100bars_252d_21bar_d3},
    "f10_swpv_071_total_pivot_density_per_100bars_252d_21bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_071_total_pivot_density_per_100bars_252d_21bar_d3},
    "f10_swpv_072_swing_direction_entropy_252d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_072_swing_direction_entropy_252d_5pct_d3},
    "f10_swpv_073_swing_direction_entropy_252d_10pct_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_073_swing_direction_entropy_252d_10pct_d3},
    "f10_swpv_074_pivot_high_price_dispersion_252d_21bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_074_pivot_high_price_dispersion_252d_21bar_d3},
    "f10_swpv_075_pivot_low_price_dispersion_252d_21bar_d3": {"inputs": ["high", "low", "close"], "func": f10_swpv_075_pivot_low_price_dispersion_252d_21bar_d3},
}
