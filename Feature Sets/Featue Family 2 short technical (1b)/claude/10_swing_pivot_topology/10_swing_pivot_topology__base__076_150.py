"""swing_pivot_topology base features 076-150 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__001_075.py. Each feature
encodes a *different concept* in the swing/pivot topology theme: asymmetric leg
durations & amplitudes, pivot-high failure & cascade, sequence detection on
last K pivots, V-vs-U reversal speed, zigzag compression Bollinger-style,
pivot price percentile placement, swing slope dynamics, pivot stack levels,
multi-window pivot agreement, composite topology scores, swing-amplitude
trend / drawdown, zigzag fractal efficiency, and proximity-to-pivot signals.

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


# ---- family-specific PIT helpers ----

def _is_pit_pivot_high(high, n):
    rmax = high.rolling(n + 1, min_periods=n + 1).max()
    return (high == rmax) & high.notna() & rmax.notna()


def _is_pit_pivot_low(low, n):
    rmin = low.rolling(n + 1, min_periods=n + 1).min()
    return (low == rmin) & low.notna() & rmin.notna()


def _pivot_high_value(high, n):
    return high.where(_is_pit_pivot_high(high, n), np.nan).ffill()


def _pivot_low_value(low, n):
    return low.where(_is_pit_pivot_low(low, n), np.nan).ffill()


def _bars_since(event):
    idx_at = np.where(event.to_numpy(), np.arange(len(event)), np.nan)
    last_idx = pd.Series(idx_at, index=event.index).ffill()
    return pd.Series(np.arange(len(event), dtype=float), index=event.index) - last_idx


def _zigzag_legs(close, threshold):
    n = len(close)
    arr = close.to_numpy()
    pivot_val = np.full(n, np.nan)
    pivot_dir = np.full(n, 0)
    pivot_idx = np.full(n, np.nan)
    if n == 0:
        return (pd.Series(pivot_val, index=close.index),
                pd.Series(pivot_dir, index=close.index),
                pd.Series(pivot_idx, index=close.index))
    state = 0
    ext_val = arr[0]
    ext_idx = 0
    for i in range(1, n):
        v = arr[i]
        if np.isnan(v) or np.isnan(ext_val):
            if not np.isnan(v) and np.isnan(ext_val):
                ext_val = v; ext_idx = i; state = 0
            continue
        if state == 0:
            if v >= ext_val * (1.0 + threshold):
                state = 1; ext_val = v; ext_idx = i
            elif v <= ext_val * (1.0 - threshold):
                state = -1; ext_val = v; ext_idx = i
        elif state == 1:
            if v > ext_val:
                ext_val = v; ext_idx = i
            elif v <= ext_val * (1.0 - threshold):
                pivot_val[i] = ext_val; pivot_dir[i] = 1; pivot_idx[i] = float(ext_idx)
                state = -1; ext_val = v; ext_idx = i
        else:
            if v < ext_val:
                ext_val = v; ext_idx = i
            elif v >= ext_val * (1.0 + threshold):
                pivot_val[i] = ext_val; pivot_dir[i] = -1; pivot_idx[i] = float(ext_idx)
                state = 1; ext_val = v; ext_idx = i
    return (pd.Series(pivot_val, index=close.index),
            pd.Series(pivot_dir, index=close.index),
            pd.Series(pivot_idx, index=close.index))


def _zigzag_leg_log_amplitudes(close, threshold):
    pv, _, _ = _zigzag_legs(close, threshold)
    prior = pv.ffill().shift(1)
    return (np.log(pv.where(pv > 0, np.nan)) - np.log(prior.where(prior > 0, np.nan))).abs().where(pv.notna(), np.nan)


def _zigzag_leg_durations(close, threshold):
    pv, _, pidx = _zigzag_legs(close, threshold)
    prior_idx = pidx.ffill().shift(1)
    dur = pidx - prior_idx
    return dur.where(pv.notna(), np.nan)


def _zigzag_signed_leg_log_amps(close, threshold):
    pv, pdir, _ = _zigzag_legs(close, threshold)
    prior = pv.ffill().shift(1)
    raw = np.log(pv.where(pv > 0, np.nan)) - np.log(prior.where(prior > 0, np.nan))
    sign = pdir.where(pdir != 0, np.nan)
    return raw.abs() * sign.where(pv.notna(), np.nan)


PV_S = 5
PV_M = 21
PV_L = 63


# ============================================================
# Bucket Q — Asymmetric swing duration/amplitude (076-082)
# ============================================================

def f10_swpv_076_mean_up_leg_amplitude_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean UP-leg log amplitude in last 252d (5%) — up-swing strength."""
    s = _zigzag_signed_leg_log_amps(close, 0.05)
    pos = s.where(s > 0, np.nan)
    return pos.rolling(YDAYS, min_periods=QDAYS).mean()


def f10_swpv_077_mean_down_leg_amplitude_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean |DOWN-leg| log amplitude in last 252d (5%)."""
    s = _zigzag_signed_leg_log_amps(close, 0.05)
    neg = (-s).where(s < 0, np.nan)
    return neg.rolling(YDAYS, min_periods=QDAYS).mean()


def f10_swpv_078_mean_up_leg_duration_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean UP-leg duration in last 252d (5%) — bars per up-leg."""
    pv, pdir, pidx = _zigzag_legs(close, 0.05)
    prior_idx = pidx.ffill().shift(1)
    dur = (pidx - prior_idx).where(pdir == 1, np.nan)
    return dur.rolling(YDAYS, min_periods=QDAYS).mean()


def f10_swpv_079_mean_down_leg_duration_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean DOWN-leg duration in last 252d (5%)."""
    pv, pdir, pidx = _zigzag_legs(close, 0.05)
    prior_idx = pidx.ffill().shift(1)
    dur = (pidx - prior_idx).where(pdir == -1, np.nan)
    return dur.rolling(YDAYS, min_periods=QDAYS).mean()


def f10_swpv_080_up_leg_amplitude_dominance_ratio_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean up-amp / mean down-amp ratio — up dominance."""
    s = _zigzag_signed_leg_log_amps(close, 0.05)
    up = s.where(s > 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    dn = (-s).where(s < 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(up, dn)


def f10_swpv_081_up_leg_duration_dominance_ratio_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean up-duration / mean down-duration ratio."""
    pv, pdir, pidx = _zigzag_legs(close, 0.05)
    prior_idx = pidx.ffill().shift(1)
    dur = (pidx - prior_idx)
    up = dur.where(pdir == 1, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    dn = dur.where(pdir == -1, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(up, dn)


def f10_swpv_082_asymmetric_swing_count_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of (up-leg followed by down-leg whose amplitude > 1.2 * up's) in trailing 252d — asymmetric pattern count."""
    pv, pdir, _ = _zigzag_legs(close, 0.05)
    amp = _zigzag_leg_log_amplitudes(close, 0.05)
    last_amp = amp.ffill().shift(1)
    asym = (pdir == -1) & (amp > 1.2 * last_amp) & last_amp.notna() & (pdir.shift(1) == 1)
    return asym.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket R — Pivot-high failure & cascade (083-088)
# ============================================================

def f10_swpv_083_pivot_high_failure_indicator_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: most-recent 21-bar PIT pivot high has NOT been exceeded within 21 bars after its confirmation."""
    phv = _pivot_high_value(high, PV_M)
    bsh = _bars_since(_is_pit_pivot_high(high, PV_M))
    return ((bsh >= MDAYS) & (high <= phv)).astype(float)


def f10_swpv_084_pivot_high_failure_count_252d_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Number of 21-bar pivot-highs in trailing 252d that were NOT exceeded within 21 subsequent bars."""
    is_h = _is_pit_pivot_high(high, PV_M)
    fail = pd.Series(False, index=high.index)
    n = len(high)
    h_arr = high.to_numpy()
    is_h_arr = is_h.to_numpy()
    f_arr = np.full(n, False)
    for i in range(n - MDAYS):
        if not is_h_arr[i]: continue
        h_val = h_arr[i]
        if np.isnan(h_val): continue
        window = h_arr[i + 1:i + 1 + MDAYS]
        if not np.any(window > h_val):
            f_arr[i + MDAYS] = True
    fail_series = pd.Series(f_arr, index=high.index)
    return fail_series.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f10_swpv_085_pivot_low_break_indicator_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: today's low < most-recent 21-bar PIT pivot-low value — support break."""
    plv = _pivot_low_value(low, PV_M)
    return (low < plv).astype(float).where(plv.notna(), np.nan)


def f10_swpv_086_pivot_gap_shrinking_indicator_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: time between most-recent 2 pivots is < time between the 2 pivots prior — pivot acceleration."""
    pv, _, pidx = _zigzag_legs(close, 0.05)
    n = len(close)
    pidx_arr = pidx.to_numpy()
    out = np.full(n, np.nan)
    buf = []
    for i in range(n):
        if not np.isnan(pidx_arr[i]):
            buf.append(pidx_arr[i])
            if len(buf) > 4: buf.pop(0)
        if len(buf) == 4:
            gap_recent = buf[3] - buf[2]
            gap_prior = buf[1] - buf[0]
            out[i] = float(gap_recent < gap_prior)
        elif len(buf) >= 1:
            out[i] = 0.0
    return pd.Series(out, index=close.index)


def f10_swpv_087_pivot_cascade_rate_252d_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of 21-bar pivots in trailing 252d where the gap to next pivot is smaller than prior gap — shrinking-gap rate."""
    is_h = _is_pit_pivot_high(high, PV_M) | _is_pit_pivot_low(low, PV_M)
    n = len(high)
    arr = is_h.to_numpy()
    pivot_indices = np.where(arr)[0]
    cascade = np.full(n, np.nan)
    if len(pivot_indices) >= 3:
        for k in range(2, len(pivot_indices)):
            gap_recent = pivot_indices[k] - pivot_indices[k - 1]
            gap_prior = pivot_indices[k - 1] - pivot_indices[k - 2]
            cascade[pivot_indices[k]] = float(gap_recent < gap_prior)
    cascade_s = pd.Series(cascade, index=high.index)
    return cascade_s.rolling(YDAYS, min_periods=QDAYS).mean()


def f10_swpv_088_pivot_high_failure_intensity_score(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pivot-high failure count weighted by failure depth (1 - h/pivot_h) over last 252d."""
    is_h = _is_pit_pivot_high(high, PV_M)
    n = len(high)
    h_arr = high.to_numpy()
    is_h_arr = is_h.to_numpy()
    score_arr = np.full(n, 0.0)
    for i in range(n - MDAYS):
        if not is_h_arr[i]: continue
        h_val = h_arr[i]
        if np.isnan(h_val) or h_val == 0: continue
        window = h_arr[i + 1:i + 1 + MDAYS]
        if not np.any(window > h_val):
            max_in = np.nanmax(window) if window.size > 0 else h_val
            depth = float(1.0 - max_in / h_val) if h_val > 0 else 0.0
            score_arr[i + MDAYS] = max(0.0, depth)
    score = pd.Series(score_arr, index=high.index)
    return score.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket S — Sequence detection on last K pivots (089-093)
# ============================================================

def _last_k_pivot_values(is_pivot, price, k):
    arr_p = price.where(is_pivot, np.nan).to_numpy()
    n = len(price)
    out = np.full((n, k), np.nan)
    buf = []
    for i in range(n):
        if not np.isnan(arr_p[i]):
            buf.append(arr_p[i])
            if len(buf) > k: buf.pop(0)
        if len(buf) == k: out[i] = np.array(buf)
    return pd.DataFrame(out, index=price.index, columns=[f"p{j}" for j in range(k)])


def f10_swpv_089_last_3_pivot_highs_all_higher_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: last 3 21-bar pivot highs strictly INCREASING (HH-HH-HH)."""
    df = _last_k_pivot_values(_is_pit_pivot_high(high, PV_M), high, 3)
    return ((df.iloc[:, 0] < df.iloc[:, 1]) & (df.iloc[:, 1] < df.iloc[:, 2])).astype(float).where(df.notna().all(axis=1), np.nan)


def f10_swpv_090_last_3_pivot_highs_all_lower_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: last 3 21-bar pivot highs strictly DECREASING (LH-LH-LH)."""
    df = _last_k_pivot_values(_is_pit_pivot_high(high, PV_M), high, 3)
    return ((df.iloc[:, 0] > df.iloc[:, 1]) & (df.iloc[:, 1] > df.iloc[:, 2])).astype(float).where(df.notna().all(axis=1), np.nan)


def f10_swpv_091_last_3_pivot_lows_all_higher_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: last 3 21-bar pivot lows strictly INCREASING."""
    df = _last_k_pivot_values(_is_pit_pivot_low(low, PV_M), low, 3)
    return ((df.iloc[:, 0] < df.iloc[:, 1]) & (df.iloc[:, 1] < df.iloc[:, 2])).astype(float).where(df.notna().all(axis=1), np.nan)


def f10_swpv_092_last_3_pivot_lows_all_lower_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: last 3 21-bar pivot lows strictly DECREASING."""
    df = _last_k_pivot_values(_is_pit_pivot_low(low, PV_M), low, 3)
    return ((df.iloc[:, 0] > df.iloc[:, 1]) & (df.iloc[:, 1] > df.iloc[:, 2])).astype(float).where(df.notna().all(axis=1), np.nan)


def f10_swpv_093_last_4_zigzag_pivots_alternating_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: last 4 confirmed zigzag pivot directions strictly alternate (+1, -1, +1, -1 or reverse)."""
    _, pdir, _ = _zigzag_legs(close, 0.05)
    n = len(close)
    arr = pdir.to_numpy()
    out = np.full(n, np.nan)
    buf = []
    for i in range(n):
        if arr[i] != 0:
            buf.append(int(arr[i]))
            if len(buf) > 4: buf.pop(0)
        if len(buf) == 4:
            alt = all(buf[k] == -buf[k - 1] for k in range(1, 4))
            out[i] = float(alt)
    return pd.Series(out, index=close.index)


# ============================================================
# Bucket T — V-vs-U reversal speed (094-097)
# ============================================================

def f10_swpv_094_bars_between_last_pivot_high_and_next_low_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars between most-recent 21-bar pivot-high and the immediately subsequent 21-bar pivot-low."""
    is_h = _is_pit_pivot_high(high, PV_M).fillna(False)
    is_l = _is_pit_pivot_low(low, PV_M).fillna(False)
    n = len(high)
    is_h_arr = is_h.to_numpy()
    is_l_arr = is_l.to_numpy()
    out = np.full(n, np.nan)
    last_h_idx = None
    last_gap = np.nan
    for i in range(n):
        if is_h_arr[i]:
            last_h_idx = i
        if is_l_arr[i] and last_h_idx is not None and i > last_h_idx:
            last_gap = float(i - last_h_idx)
            last_h_idx = None
        out[i] = last_gap
    return pd.Series(out, index=high.index)


def f10_swpv_095_bars_between_last_pivot_low_and_next_high_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mirror — bars between last pivot-low and next pivot-high."""
    is_h = _is_pit_pivot_high(high, PV_M).fillna(False)
    is_l = _is_pit_pivot_low(low, PV_M).fillna(False)
    n = len(high)
    is_h_arr = is_h.to_numpy()
    is_l_arr = is_l.to_numpy()
    out = np.full(n, np.nan)
    last_l_idx = None
    last_gap = np.nan
    for i in range(n):
        if is_l_arr[i]:
            last_l_idx = i
        if is_h_arr[i] and last_l_idx is not None and i > last_l_idx:
            last_gap = float(i - last_l_idx)
            last_l_idx = None
        out[i] = last_gap
    return pd.Series(out, index=high.index)


def f10_swpv_096_median_bars_pivot_high_to_low_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Median bars between consecutive pivot-high → pivot-low pairs in trailing 252d (using 21-bar pivots)."""
    gap_series = f10_swpv_094_bars_between_last_pivot_high_and_next_low_21bar(high, low, close)
    return gap_series.rolling(YDAYS, min_periods=QDAYS).median()


def f10_swpv_097_variance_pivot_reversal_speed_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stdev of pivot-high-to-low gaps in trailing 252d — reversal-speed irregularity."""
    gap_series = f10_swpv_094_bars_between_last_pivot_high_and_next_low_21bar(high, low, close)
    return gap_series.rolling(YDAYS, min_periods=QDAYS).std()


# ============================================================
# Bucket U — Zigzag compression / Bollinger (098-102)
# ============================================================

def f10_swpv_098_stdev_zigzag_pivot_prices_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stdev of confirmed zigzag pivot PRICES in last 252d (5%)."""
    pv, _, _ = _zigzag_legs(close, 0.05)
    return pv.rolling(YDAYS, min_periods=QDAYS).std()


def f10_swpv_099_range_zigzag_pivot_prices_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Range (max - min) of confirmed zigzag pivot PRICES in last 252d (5%)."""
    pv, _, _ = _zigzag_legs(close, 0.05)
    return pv.rolling(YDAYS, min_periods=QDAYS).max() - pv.rolling(YDAYS, min_periods=QDAYS).min()


def f10_swpv_100_log_range_zigzag_pivot_prices_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log range of zigzag pivot PRICES in last 252d (5%): log(max/min)."""
    pv, _, _ = _zigzag_legs(close, 0.05)
    return _safe_log(pv.rolling(YDAYS, min_periods=QDAYS).max()) - _safe_log(pv.rolling(YDAYS, min_periods=QDAYS).min())


def f10_swpv_101_bollinger_width_zigzag_pivots_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bollinger-style width: 2σ band width of zigzag pivot prices over 252d / mean."""
    pv, _, _ = _zigzag_legs(close, 0.05)
    sd = pv.rolling(YDAYS, min_periods=QDAYS).std()
    mn = pv.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(4.0 * sd, mn)


def f10_swpv_102_zigzag_pivot_compression_zscore_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of current pivot-price stdev vs 1260d distribution of same metric — compression regime."""
    pv, _, _ = _zigzag_legs(close, 0.05)
    sd = pv.rolling(YDAYS, min_periods=QDAYS).std()
    return _rolling_zscore(sd, DDAYS_5Y, min_periods=YDAYS)


# ============================================================
# Bucket V — Pivot price percentile / proximity to close (103-107)
# ============================================================

def f10_swpv_103_pct_rank_close_in_pivot_high_distribution_252d_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of close in distribution of 21-bar pivot-high prices over last 252d."""
    pv = high.where(_is_pit_pivot_high(high, PV_M), np.nan)
    n = len(close)
    close_arr = close.to_numpy()
    pv_arr = pv.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        window = pv_arr[start:i + 1]
        valid = window[~np.isnan(window)]
        if valid.size == 0 or np.isnan(close_arr[i]): continue
        out[i] = float((valid <= close_arr[i]).sum()) / float(valid.size)
    return pd.Series(out, index=close.index)


def f10_swpv_104_pct_rank_close_in_pivot_low_distribution_252d_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of close in distribution of 21-bar pivot-low prices over last 252d."""
    pv = low.where(_is_pit_pivot_low(low, PV_M), np.nan)
    n = len(close)
    close_arr = close.to_numpy()
    pv_arr = pv.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        window = pv_arr[start:i + 1]
        valid = window[~np.isnan(window)]
        if valid.size == 0 or np.isnan(close_arr[i]): continue
        out[i] = float((valid <= close_arr[i]).sum()) / float(valid.size)
    return pd.Series(out, index=close.index)


def f10_swpv_105_atr_dist_to_nearest_pivot_high_above_close_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized distance from close to nearest pivot-high (21-bar) above current close in last 252d."""
    pv = high.where(_is_pit_pivot_high(high, PV_M), np.nan)
    atr = _atr(high, low, close, n=MDAYS)
    n = len(close)
    close_arr = close.to_numpy()
    pv_arr = pv.to_numpy()
    atr_arr = atr.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        win = pv_arr[start:i + 1]
        above = win[win > close_arr[i]]
        if above.size == 0 or np.isnan(atr_arr[i]) or atr_arr[i] == 0: continue
        out[i] = float((above.min() - close_arr[i]) / atr_arr[i])
    return pd.Series(out, index=close.index)


def f10_swpv_106_atr_dist_to_nearest_pivot_low_below_close_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized distance from close DOWN to nearest pivot-low (21-bar) below close in last 252d."""
    pv = low.where(_is_pit_pivot_low(low, PV_M), np.nan)
    atr = _atr(high, low, close, n=MDAYS)
    n = len(close)
    close_arr = close.to_numpy()
    pv_arr = pv.to_numpy()
    atr_arr = atr.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        win = pv_arr[start:i + 1]
        below = win[win < close_arr[i]]
        if below.size == 0 or np.isnan(atr_arr[i]) or atr_arr[i] == 0: continue
        out[i] = float((close_arr[i] - below.max()) / atr_arr[i])
    return pd.Series(out, index=close.index)


def f10_swpv_107_count_pivot_highs_within_atr_of_close_252d_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of 21-bar pivot-highs from last 252d within 1 ATR of current close — overhead pivot cluster."""
    pv = high.where(_is_pit_pivot_high(high, PV_M), np.nan)
    atr = _atr(high, low, close, n=MDAYS)
    n = len(close)
    close_arr = close.to_numpy()
    pv_arr = pv.to_numpy()
    atr_arr = atr.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        win = pv_arr[start:i + 1]
        valid = win[~np.isnan(win)]
        if valid.size == 0 or np.isnan(atr_arr[i]) or atr_arr[i] == 0: continue
        out[i] = float(np.sum(np.abs(valid - close_arr[i]) <= atr_arr[i]))
    return pd.Series(out, index=close.index)


# ============================================================
# Bucket W — Swing-leg slope dynamics (108-112)
# ============================================================

def f10_swpv_108_most_recent_swing_leg_slope_log_per_bar_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Most-recent confirmed leg's amplitude / duration → log-progress per bar of that leg (5%)."""
    amp = _zigzag_leg_log_amplitudes(close, 0.05)
    dur = _zigzag_leg_durations(close, 0.05)
    return _safe_div(amp.ffill(), dur.ffill())


def f10_swpv_109_median_swing_leg_slope_log_per_bar_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Median per-bar log slope of confirmed legs in last 252d."""
    amp = _zigzag_leg_log_amplitudes(close, 0.05)
    dur = _zigzag_leg_durations(close, 0.05)
    slope = _safe_div(amp, dur)
    return slope.rolling(YDAYS, min_periods=QDAYS).median()


def f10_swpv_110_max_swing_leg_slope_log_per_bar_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max per-bar log slope of confirmed legs in last 252d — fastest leg."""
    amp = _zigzag_leg_log_amplitudes(close, 0.05)
    dur = _zigzag_leg_durations(close, 0.05)
    slope = _safe_div(amp, dur)
    return slope.rolling(YDAYS, min_periods=QDAYS).max()


def f10_swpv_111_swing_leg_slope_recent_vs_median_ratio_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Most-recent leg slope / median 252d slope — current leg energy vs typical."""
    amp = _zigzag_leg_log_amplitudes(close, 0.05)
    dur = _zigzag_leg_durations(close, 0.05)
    slope = _safe_div(amp, dur)
    return _safe_div(slope.ffill(), slope.rolling(YDAYS, min_periods=QDAYS).median())


def f10_swpv_112_swing_leg_slope_acceleration_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Linear-fit slope of per-leg slope values over trailing 252d (5%) — slope acceleration/decay."""
    amp = _zigzag_leg_log_amplitudes(close, 0.05)
    dur = _zigzag_leg_durations(close, 0.05)
    slope = _safe_div(amp, dur).fillna(0.0)
    return _rolling_slope(slope, YDAYS, min_periods=QDAYS)


# ============================================================
# Bucket X — Pivot stack levels (113-117)
# ============================================================

def f10_swpv_113_count_pivot_highs_above_close_in_252d_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of 21-bar pivot-highs from last 252d that are above current close — overhead supply count."""
    pv = high.where(_is_pit_pivot_high(high, PV_M), np.nan)
    n = len(close)
    close_arr = close.to_numpy()
    pv_arr = pv.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        win = pv_arr[start:i + 1]
        valid = win[~np.isnan(win)]
        if valid.size == 0: continue
        out[i] = float(np.sum(valid > close_arr[i]))
    return pd.Series(out, index=close.index)


def f10_swpv_114_count_pivot_lows_below_close_in_252d_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of 21-bar pivot-lows from last 252d that are below current close — supply stack below."""
    pv = low.where(_is_pit_pivot_low(low, PV_M), np.nan)
    n = len(close)
    close_arr = close.to_numpy()
    pv_arr = pv.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        win = pv_arr[start:i + 1]
        valid = win[~np.isnan(win)]
        if valid.size == 0: continue
        out[i] = float(np.sum(valid < close_arr[i]))
    return pd.Series(out, index=close.index)


def f10_swpv_115_log_dist_close_to_highest_pivot_high_252d_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance from close UP to highest 21-bar pivot-high in last 252d (NaN if close already above)."""
    pv = high.where(_is_pit_pivot_high(high, PV_M), np.nan)
    hi = pv.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_log(hi) - _safe_log(close)


def f10_swpv_116_log_dist_close_to_lowest_pivot_low_252d_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance from close DOWN to lowest 21-bar pivot-low in last 252d."""
    pv = low.where(_is_pit_pivot_low(low, PV_M), np.nan)
    lo = pv.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_log(close) - _safe_log(lo)


def f10_swpv_117_pivot_high_stack_log_height_252d_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log of (max pivot-high / min pivot-high) in last 252d — vertical span of overhead supply."""
    pv = high.where(_is_pit_pivot_high(high, PV_M), np.nan)
    hi = pv.rolling(YDAYS, min_periods=QDAYS).max()
    lo = pv.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_log(hi) - _safe_log(lo)


# ============================================================
# Bucket Y — Multi-window pivot agreement (118-122)
# ============================================================

def f10_swpv_118_pivot_count_ratio_short_over_long_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of (5-bar pivot-high+low count) / (63-bar pivot-high+low count) in last 252d — fine-vs-coarse pivot ratio."""
    sh = _is_pit_pivot_high(high, PV_S) | _is_pit_pivot_low(low, PV_S)
    lo = _is_pit_pivot_high(high, PV_L) | _is_pit_pivot_low(low, PV_L)
    return _safe_div(sh.astype(float).rolling(YDAYS, min_periods=QDAYS).sum(),
                     lo.astype(float).rolling(YDAYS, min_periods=QDAYS).sum())


def f10_swpv_119_pivot_consistency_across_horizons_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in last 252d where BOTH short (5-bar) and medium (21-bar) PIT pivot-high triggers fire on the same bar."""
    coinc = _is_pit_pivot_high(high, PV_S) & _is_pit_pivot_high(high, PV_M)
    return coinc.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f10_swpv_120_pivot_disagreement_index_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 - (consistency / total pivots) — fraction of pivots that DON'T agree across short/medium horizons."""
    sh = _is_pit_pivot_high(high, PV_S)
    md = _is_pit_pivot_high(high, PV_M)
    consist = (sh & md).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    total_md = md.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return 1.0 - _safe_div(consist, total_md)


def f10_swpv_121_pivot_amplitude_dispersion_across_horizons(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stdev across most-recent leg amplitudes at 3%/5%/10% zigzag thresholds — multi-scale disagreement on swing size."""
    a3 = _zigzag_leg_log_amplitudes(close, 0.03).ffill()
    a5 = _zigzag_leg_log_amplitudes(close, 0.05).ffill()
    aA = _zigzag_leg_log_amplitudes(close, 0.10).ffill()
    return pd.concat([a3.rename("a"), a5.rename("b"), aA.rename("c")], axis=1).std(axis=1)


def f10_swpv_122_pivot_age_dispersion_across_horizons(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stdev across bars-since for 5/21/63-bar PIT pivot-highs — multi-scale freshness disagreement."""
    a = _bars_since(_is_pit_pivot_high(high, PV_S))
    b = _bars_since(_is_pit_pivot_high(high, PV_M))
    c = _bars_since(_is_pit_pivot_high(high, PV_L))
    return pd.concat([a.rename("a"), b.rename("b"), c.rename("c")], axis=1).std(axis=1)


# ============================================================
# Bucket Z — Composite topology scores (123-128)
# ============================================================

def f10_swpv_123_topology_compression_score_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: 1/pivot_density + 1/amplitude_dispersion + 1/mean_duration — lower means more compressed."""
    density = _is_pit_pivot_high(high, PV_M).astype(float).rolling(YDAYS, min_periods=QDAYS).sum() / float(YDAYS)
    amp_disp = _zigzag_leg_log_amplitudes(close, 0.05).rolling(YDAYS, min_periods=QDAYS).std()
    dur_mean = _zigzag_leg_durations(close, 0.05).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(1.0, density.replace(0, np.nan)) + _safe_div(1.0, amp_disp) + _safe_div(1.0, dur_mean)


def f10_swpv_124_topology_expansion_score_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: pivot_density + amplitude_dispersion + 1/mean_duration — higher means more chaotic expansion."""
    density = _is_pit_pivot_high(high, PV_M).astype(float).rolling(YDAYS, min_periods=QDAYS).sum() / float(YDAYS)
    amp_disp = _zigzag_leg_log_amplitudes(close, 0.05).rolling(YDAYS, min_periods=QDAYS).std()
    dur_mean = _zigzag_leg_durations(close, 0.05).rolling(YDAYS, min_periods=QDAYS).mean()
    return density + amp_disp + _safe_div(1.0, dur_mean)


def f10_swpv_125_topology_irregularity_index_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CV of leg durations + CV of leg amplitudes (5%) — irregularity composite."""
    dur = _zigzag_leg_durations(close, 0.05)
    amp = _zigzag_leg_log_amplitudes(close, 0.05)
    cv_dur = _safe_div(dur.rolling(YDAYS, min_periods=QDAYS).std(), dur.rolling(YDAYS, min_periods=QDAYS).mean())
    cv_amp = _safe_div(amp.rolling(YDAYS, min_periods=QDAYS).std(), amp.rolling(YDAYS, min_periods=QDAYS).mean())
    return cv_dur + cv_amp


def f10_swpv_126_topology_top_signature_score_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite top: (declining-3-pivot-highs 21bar indicator) + (amp decay ratio < 1) + (bars_since_pivot_high_63bar > 63)."""
    df = _last_k_pivot_values(_is_pit_pivot_high(high, PV_M), high, 3)
    decl = ((df.iloc[:, 0] > df.iloc[:, 1]) & (df.iloc[:, 1] > df.iloc[:, 2])).astype(float).where(df.notna().all(axis=1), np.nan)
    amp = _zigzag_leg_log_amplitudes(close, 0.05)
    recent = amp.rolling(QDAYS, min_periods=MDAYS).mean()
    old = amp.shift(QDAYS * 3).rolling(QDAYS, min_periods=MDAYS).mean()
    decay = (_safe_div(recent, old) < 1.0).astype(float)
    stale = (_bars_since(_is_pit_pivot_high(high, PV_L)) > QDAYS).astype(float)
    return decl.fillna(0) + decay.fillna(0) + stale.fillna(0)


def f10_swpv_127_topology_breakdown_score_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(pivot_low_break_21bar indicator) + (last 3 pivot-lows declining 21bar) + (down-leg count exceeds up-leg count)."""
    break_ = f10_swpv_085_pivot_low_break_indicator_21bar(high, low, close)
    decl = _last_k_pivot_values(_is_pit_pivot_low(low, PV_M), low, 3)
    pivot_decl = ((decl.iloc[:, 0] > decl.iloc[:, 1]) & (decl.iloc[:, 1] > decl.iloc[:, 2])).astype(float).where(decl.notna().all(axis=1), 0.0)
    _, pdir, _ = _zigzag_legs(close, 0.05)
    up = (pdir == 1).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    dn = (pdir == -1).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    dn_dom = (dn > up).astype(float)
    return break_.fillna(0) + pivot_decl + dn_dom


def f10_swpv_128_pivot_regime_indicator_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: pivot density in last 63d > 2 × pivot density in trailing 252d — regime shift to high frequency."""
    is_h_m = _is_pit_pivot_high(high, PV_M).astype(float)
    short_density = is_h_m.rolling(QDAYS, min_periods=MDAYS).mean()
    long_density = is_h_m.rolling(YDAYS, min_periods=QDAYS).mean()
    return (short_density > 2.0 * long_density).astype(float)


# ============================================================
# Bucket AA — Swing amplitude trend (129-133)
# ============================================================

def f10_swpv_129_amplitude_trend_slope_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope of per-leg log-amplitudes over trailing 252d (5%) — amplitude trend."""
    amp = _zigzag_leg_log_amplitudes(close, 0.05).fillna(0.0)
    return _rolling_slope(amp, YDAYS, min_periods=QDAYS)


def f10_swpv_130_amplitude_zscore_recent_vs_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of most-recent leg amplitude vs trailing 252d amplitude distribution."""
    amp = _zigzag_leg_log_amplitudes(close, 0.05).ffill()
    return _rolling_zscore(amp, YDAYS, min_periods=QDAYS)


def f10_swpv_131_amplitude_percentile_rank_recent_vs_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Empirical percentile rank of most-recent leg amplitude vs trailing 252d."""
    amp = _zigzag_leg_log_amplitudes(close, 0.05).ffill()
    def _rk(w):
        if np.isnan(w).all(): return np.nan
        last = w[-1]
        if np.isnan(last): return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0: return np.nan
        return float((v <= last).sum()) / float(v.size)
    return amp.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)


def f10_swpv_132_amplitude_drawdown_from_max_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Most-recent leg amplitude / max(amplitude in 252d) - 1 — amplitude drawdown from peak."""
    amp = _zigzag_leg_log_amplitudes(close, 0.05).ffill()
    return _safe_div(amp, amp.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0


def f10_swpv_133_cum_amplitude_recovery_from_min_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Most-recent leg amplitude / min(amplitude in 252d) - 1 — amplitude recovery from floor."""
    amp = _zigzag_leg_log_amplitudes(close, 0.05).ffill()
    return _safe_div(amp, amp.rolling(YDAYS, min_periods=QDAYS).min()) - 1.0


# ============================================================
# Bucket BB — Zigzag fractal-like measures (134-138)
# ============================================================

def f10_swpv_134_zigzag_path_length_log_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of all leg log amplitudes in trailing 252d (5%) — total fractal path length."""
    amp = _zigzag_leg_log_amplitudes(close, 0.05).fillna(0.0)
    return amp.rolling(YDAYS, min_periods=QDAYS).sum()


def f10_swpv_135_zigzag_efficiency_ratio_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """|252d net log return| / sum of leg amplitudes — fraction of motion that is net direction (Kaufman efficiency, leg version)."""
    amp = _zigzag_leg_log_amplitudes(close, 0.05).fillna(0.0)
    path = amp.rolling(YDAYS, min_periods=QDAYS).sum()
    net = (_safe_log(close) - _safe_log(close.shift(YDAYS))).abs()
    return _safe_div(net, path)


def f10_swpv_136_zigzag_efficiency_ratio_63d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Same Kaufman-style efficiency at 63d horizon."""
    amp = _zigzag_leg_log_amplitudes(close, 0.05).fillna(0.0)
    path = amp.rolling(QDAYS, min_periods=MDAYS).sum()
    net = (_safe_log(close) - _safe_log(close.shift(QDAYS))).abs()
    return _safe_div(net, path)


def f10_swpv_137_zigzag_efficiency_acceleration_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Difference: 63d efficiency - 252d efficiency — short-horizon efficiency change."""
    amp = _zigzag_leg_log_amplitudes(close, 0.05).fillna(0.0)
    path_63 = amp.rolling(QDAYS, min_periods=MDAYS).sum()
    path_252 = amp.rolling(YDAYS, min_periods=QDAYS).sum()
    net_63 = (_safe_log(close) - _safe_log(close.shift(QDAYS))).abs()
    net_252 = (_safe_log(close) - _safe_log(close.shift(YDAYS))).abs()
    return _safe_div(net_63, path_63) - _safe_div(net_252, path_252)


def f10_swpv_138_pivot_path_complexity_ratio_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pivots per bar in trailing 252d (5%): leg_count / 252."""
    pv, _, _ = _zigzag_legs(close, 0.05)
    cnt = pv.notna().astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return cnt / float(YDAYS)


# ============================================================
# Bucket CC — Proximity to pivot (139-142)
# ============================================================

def f10_swpv_139_bars_since_pivot_high_within_1atr_of_close_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most-recent 21-bar pivot-high that was within 1 ATR of (then-)close."""
    is_h = _is_pit_pivot_high(high, PV_M).fillna(False)
    atr = _atr(high, low, close, n=MDAYS)
    near = is_h & ((high - close).abs() <= atr)
    return _bars_since(near.fillna(False))


def f10_swpv_140_bars_since_pivot_low_within_1atr_of_close_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most-recent 21-bar pivot-low within 1 ATR of (then-)close."""
    is_l = _is_pit_pivot_low(low, PV_M).fillna(False)
    atr = _atr(high, low, close, n=MDAYS)
    near = is_l & ((low - close).abs() <= atr)
    return _bars_since(near.fillna(False))


def f10_swpv_141_count_pivots_within_1atr_of_close_252d_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of 21-bar pivots (high or low) within 1 ATR of CURRENT close, drawn from trailing 252d pool."""
    pv_h = high.where(_is_pit_pivot_high(high, PV_M), np.nan)
    pv_l = low.where(_is_pit_pivot_low(low, PV_M), np.nan)
    atr = _atr(high, low, close, n=MDAYS)
    n = len(close)
    out = np.full(n, np.nan)
    close_arr = close.to_numpy()
    pv_h_arr = pv_h.to_numpy(); pv_l_arr = pv_l.to_numpy(); atr_arr = atr.to_numpy()
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        win_h = pv_h_arr[start:i + 1]; win_l = pv_l_arr[start:i + 1]
        vals = np.concatenate([win_h[~np.isnan(win_h)], win_l[~np.isnan(win_l)]])
        if vals.size == 0 or np.isnan(atr_arr[i]) or atr_arr[i] == 0: continue
        out[i] = float(np.sum(np.abs(vals - close_arr[i]) <= atr_arr[i]))
    return pd.Series(out, index=close.index)


def f10_swpv_142_time_since_close_near_a_pivot_high_21bar_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since current close was within 0.5 ATR of any 21-bar pivot-high (PIT-confirmed value at that time)."""
    phv = _pivot_high_value(high, PV_M)
    atr = _atr(high, low, close, n=MDAYS)
    near = (close - phv).abs() <= 0.5 * atr
    return _bars_since(near.fillna(False))


# ============================================================
# Bucket DD — Composite indicators (143-150)
# ============================================================

def f10_swpv_143_distribution_topology_indicator_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: high pivot-high density + low amplitude + long current leg age — distribution-top topology."""
    density = _is_pit_pivot_high(high, PV_M).astype(float).rolling(YDAYS, min_periods=QDAYS).sum() / float(YDAYS)
    amp = _zigzag_leg_log_amplitudes(close, 0.05).rolling(YDAYS, min_periods=QDAYS).median()
    _, _, pidx = _zigzag_legs(close, 0.05)
    age = pd.Series(np.arange(len(close), dtype=float), index=close.index) - pidx.ffill()
    return _safe_div(density * age, amp + 1e-6)


def f10_swpv_144_classic_top_topology_indicator_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: max 252d pivot-high is the OLDEST among last 3 pivot-highs AND subsequent two are lower."""
    df = _last_k_pivot_values(_is_pit_pivot_high(high, PV_M), high, 3)
    a = df.iloc[:, 0]; b = df.iloc[:, 1]; c = df.iloc[:, 2]
    pv_h = high.where(_is_pit_pivot_high(high, PV_M), np.nan)
    max252 = pv_h.rolling(YDAYS, min_periods=QDAYS).max()
    return ((a == max252) & (b < a) & (c < b)).astype(float).where(df.notna().all(axis=1), np.nan)


def f10_swpv_145_pivot_velocity_acceleration_decline_indicator_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: pivot count is accelerating AND amplitude is decaying — terminal-cluster signature."""
    pv, _, _ = _zigzag_legs(close, 0.05)
    cnt = pv.notna().astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    accel = cnt - cnt.shift(QDAYS)
    amp = _zigzag_leg_log_amplitudes(close, 0.05)
    recent = amp.rolling(QDAYS, min_periods=MDAYS).mean()
    old = amp.shift(QDAYS * 3).rolling(QDAYS, min_periods=MDAYS).mean()
    decay = _safe_div(recent, old)
    return ((accel > 0) & (decay < 1.0)).astype(float).where(accel.notna() & decay.notna(), np.nan)


def f10_swpv_146_structural_decay_score_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: amplitude_decay_ratio * topology_compression — combined decay metric."""
    amp = _zigzag_leg_log_amplitudes(close, 0.05)
    recent = amp.rolling(QDAYS, min_periods=MDAYS).mean()
    old = amp.shift(QDAYS * 3).rolling(QDAYS, min_periods=MDAYS).mean()
    decay = _safe_div(recent, old)
    comp = f10_swpv_123_topology_compression_score_252d(high, low, close)
    return decay * comp


def f10_swpv_147_zigzag_compression_top_indicator_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: zigzag pivot price stdev is in bottom decile of 1260d distribution AND price near 252d high."""
    sd = f10_swpv_098_stdev_zigzag_pivot_prices_252d_5pct(high, low, close)
    def _rk(w):
        if np.isnan(w).all(): return np.nan
        last = w[-1]
        if np.isnan(last): return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0: return np.nan
        return float((v <= last).sum()) / float(v.size)
    rk = sd.rolling(DDAYS_5Y, min_periods=YDAYS).apply(_rk, raw=True)
    hi252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    lo252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - lo252, hi252 - lo252)
    return ((rk <= 0.1) & (pos >= 0.9)).astype(float).where(rk.notna() & pos.notna(), np.nan)


def f10_swpv_148_pivot_high_age_stale_indicator_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: no new 63-bar PIT pivot-high in last 63 bars — stale-high regime."""
    bs = _bars_since(_is_pit_pivot_high(high, PV_L))
    return (bs >= QDAYS).astype(float).where(bs.notna(), np.nan)


def f10_swpv_149_swing_failure_pattern_indicator_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: current high exceeded prior pivot-high but close is BELOW that pivot-high — false-breakout swing failure (Wyckoff-style)."""
    phv = _pivot_high_value(high, PV_M)
    return ((high > phv) & (close < phv)).astype(float).where(phv.notna(), np.nan)


def f10_swpv_150_composite_topology_top_score_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Weighted composite: 2*classic_top + topology_top + 0.5*swing_failure + 0.5*stale_high + compression_top."""
    a = f10_swpv_144_classic_top_topology_indicator_252d(high, low, close).fillna(0)
    b = f10_swpv_126_topology_top_signature_score_252d(high, low, close)
    c = f10_swpv_149_swing_failure_pattern_indicator_252d(high, low, close).fillna(0)
    d = f10_swpv_148_pivot_high_age_stale_indicator_252d(high, low, close).fillna(0)
    e = f10_swpv_147_zigzag_compression_top_indicator_252d(high, low, close).fillna(0)
    return 2.0 * a + b + 0.5 * c + 0.5 * d + e


# ============================================================
#                         REGISTRY 076-150
# ============================================================

SWING_PIVOT_TOPOLOGY_BASE_REGISTRY_076_150 = {
    "f10_swpv_076_mean_up_leg_amplitude_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_076_mean_up_leg_amplitude_252d_5pct},
    "f10_swpv_077_mean_down_leg_amplitude_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_077_mean_down_leg_amplitude_252d_5pct},
    "f10_swpv_078_mean_up_leg_duration_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_078_mean_up_leg_duration_252d_5pct},
    "f10_swpv_079_mean_down_leg_duration_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_079_mean_down_leg_duration_252d_5pct},
    "f10_swpv_080_up_leg_amplitude_dominance_ratio_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_080_up_leg_amplitude_dominance_ratio_252d_5pct},
    "f10_swpv_081_up_leg_duration_dominance_ratio_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_081_up_leg_duration_dominance_ratio_252d_5pct},
    "f10_swpv_082_asymmetric_swing_count_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_082_asymmetric_swing_count_252d_5pct},
    "f10_swpv_083_pivot_high_failure_indicator_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_083_pivot_high_failure_indicator_21bar},
    "f10_swpv_084_pivot_high_failure_count_252d_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_084_pivot_high_failure_count_252d_21bar},
    "f10_swpv_085_pivot_low_break_indicator_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_085_pivot_low_break_indicator_21bar},
    "f10_swpv_086_pivot_gap_shrinking_indicator_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_086_pivot_gap_shrinking_indicator_21bar},
    "f10_swpv_087_pivot_cascade_rate_252d_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_087_pivot_cascade_rate_252d_21bar},
    "f10_swpv_088_pivot_high_failure_intensity_score": {"inputs": ["high", "low", "close"], "func": f10_swpv_088_pivot_high_failure_intensity_score},
    "f10_swpv_089_last_3_pivot_highs_all_higher_indicator": {"inputs": ["high", "low", "close"], "func": f10_swpv_089_last_3_pivot_highs_all_higher_indicator},
    "f10_swpv_090_last_3_pivot_highs_all_lower_indicator": {"inputs": ["high", "low", "close"], "func": f10_swpv_090_last_3_pivot_highs_all_lower_indicator},
    "f10_swpv_091_last_3_pivot_lows_all_higher_indicator": {"inputs": ["high", "low", "close"], "func": f10_swpv_091_last_3_pivot_lows_all_higher_indicator},
    "f10_swpv_092_last_3_pivot_lows_all_lower_indicator": {"inputs": ["high", "low", "close"], "func": f10_swpv_092_last_3_pivot_lows_all_lower_indicator},
    "f10_swpv_093_last_4_zigzag_pivots_alternating_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_093_last_4_zigzag_pivots_alternating_5pct},
    "f10_swpv_094_bars_between_last_pivot_high_and_next_low_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_094_bars_between_last_pivot_high_and_next_low_21bar},
    "f10_swpv_095_bars_between_last_pivot_low_and_next_high_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_095_bars_between_last_pivot_low_and_next_high_21bar},
    "f10_swpv_096_median_bars_pivot_high_to_low_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_096_median_bars_pivot_high_to_low_252d},
    "f10_swpv_097_variance_pivot_reversal_speed_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_097_variance_pivot_reversal_speed_252d},
    "f10_swpv_098_stdev_zigzag_pivot_prices_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_098_stdev_zigzag_pivot_prices_252d_5pct},
    "f10_swpv_099_range_zigzag_pivot_prices_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_099_range_zigzag_pivot_prices_252d_5pct},
    "f10_swpv_100_log_range_zigzag_pivot_prices_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_100_log_range_zigzag_pivot_prices_252d_5pct},
    "f10_swpv_101_bollinger_width_zigzag_pivots_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_101_bollinger_width_zigzag_pivots_252d_5pct},
    "f10_swpv_102_zigzag_pivot_compression_zscore_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_102_zigzag_pivot_compression_zscore_252d_5pct},
    "f10_swpv_103_pct_rank_close_in_pivot_high_distribution_252d_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_103_pct_rank_close_in_pivot_high_distribution_252d_21bar},
    "f10_swpv_104_pct_rank_close_in_pivot_low_distribution_252d_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_104_pct_rank_close_in_pivot_low_distribution_252d_21bar},
    "f10_swpv_105_atr_dist_to_nearest_pivot_high_above_close_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_105_atr_dist_to_nearest_pivot_high_above_close_21bar},
    "f10_swpv_106_atr_dist_to_nearest_pivot_low_below_close_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_106_atr_dist_to_nearest_pivot_low_below_close_21bar},
    "f10_swpv_107_count_pivot_highs_within_atr_of_close_252d_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_107_count_pivot_highs_within_atr_of_close_252d_21bar},
    "f10_swpv_108_most_recent_swing_leg_slope_log_per_bar_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_108_most_recent_swing_leg_slope_log_per_bar_5pct},
    "f10_swpv_109_median_swing_leg_slope_log_per_bar_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_109_median_swing_leg_slope_log_per_bar_252d_5pct},
    "f10_swpv_110_max_swing_leg_slope_log_per_bar_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_110_max_swing_leg_slope_log_per_bar_252d_5pct},
    "f10_swpv_111_swing_leg_slope_recent_vs_median_ratio_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_111_swing_leg_slope_recent_vs_median_ratio_252d_5pct},
    "f10_swpv_112_swing_leg_slope_acceleration_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_112_swing_leg_slope_acceleration_252d_5pct},
    "f10_swpv_113_count_pivot_highs_above_close_in_252d_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_113_count_pivot_highs_above_close_in_252d_21bar},
    "f10_swpv_114_count_pivot_lows_below_close_in_252d_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_114_count_pivot_lows_below_close_in_252d_21bar},
    "f10_swpv_115_log_dist_close_to_highest_pivot_high_252d_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_115_log_dist_close_to_highest_pivot_high_252d_21bar},
    "f10_swpv_116_log_dist_close_to_lowest_pivot_low_252d_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_116_log_dist_close_to_lowest_pivot_low_252d_21bar},
    "f10_swpv_117_pivot_high_stack_log_height_252d_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_117_pivot_high_stack_log_height_252d_21bar},
    "f10_swpv_118_pivot_count_ratio_short_over_long_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_118_pivot_count_ratio_short_over_long_252d},
    "f10_swpv_119_pivot_consistency_across_horizons_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_119_pivot_consistency_across_horizons_252d},
    "f10_swpv_120_pivot_disagreement_index_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_120_pivot_disagreement_index_252d},
    "f10_swpv_121_pivot_amplitude_dispersion_across_horizons": {"inputs": ["high", "low", "close"], "func": f10_swpv_121_pivot_amplitude_dispersion_across_horizons},
    "f10_swpv_122_pivot_age_dispersion_across_horizons": {"inputs": ["high", "low", "close"], "func": f10_swpv_122_pivot_age_dispersion_across_horizons},
    "f10_swpv_123_topology_compression_score_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_123_topology_compression_score_252d},
    "f10_swpv_124_topology_expansion_score_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_124_topology_expansion_score_252d},
    "f10_swpv_125_topology_irregularity_index_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_125_topology_irregularity_index_252d},
    "f10_swpv_126_topology_top_signature_score_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_126_topology_top_signature_score_252d},
    "f10_swpv_127_topology_breakdown_score_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_127_topology_breakdown_score_252d},
    "f10_swpv_128_pivot_regime_indicator_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_128_pivot_regime_indicator_252d},
    "f10_swpv_129_amplitude_trend_slope_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_129_amplitude_trend_slope_252d_5pct},
    "f10_swpv_130_amplitude_zscore_recent_vs_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_130_amplitude_zscore_recent_vs_252d_5pct},
    "f10_swpv_131_amplitude_percentile_rank_recent_vs_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_131_amplitude_percentile_rank_recent_vs_252d_5pct},
    "f10_swpv_132_amplitude_drawdown_from_max_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_132_amplitude_drawdown_from_max_252d_5pct},
    "f10_swpv_133_cum_amplitude_recovery_from_min_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_133_cum_amplitude_recovery_from_min_252d_5pct},
    "f10_swpv_134_zigzag_path_length_log_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_134_zigzag_path_length_log_252d_5pct},
    "f10_swpv_135_zigzag_efficiency_ratio_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_135_zigzag_efficiency_ratio_252d_5pct},
    "f10_swpv_136_zigzag_efficiency_ratio_63d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_136_zigzag_efficiency_ratio_63d_5pct},
    "f10_swpv_137_zigzag_efficiency_acceleration_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_137_zigzag_efficiency_acceleration_252d_5pct},
    "f10_swpv_138_pivot_path_complexity_ratio_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_138_pivot_path_complexity_ratio_252d},
    "f10_swpv_139_bars_since_pivot_high_within_1atr_of_close_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_139_bars_since_pivot_high_within_1atr_of_close_21bar},
    "f10_swpv_140_bars_since_pivot_low_within_1atr_of_close_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_140_bars_since_pivot_low_within_1atr_of_close_21bar},
    "f10_swpv_141_count_pivots_within_1atr_of_close_252d_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_141_count_pivots_within_1atr_of_close_252d_21bar},
    "f10_swpv_142_time_since_close_near_a_pivot_high_21bar_atr": {"inputs": ["high", "low", "close"], "func": f10_swpv_142_time_since_close_near_a_pivot_high_21bar_atr},
    "f10_swpv_143_distribution_topology_indicator_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_143_distribution_topology_indicator_252d},
    "f10_swpv_144_classic_top_topology_indicator_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_144_classic_top_topology_indicator_252d},
    "f10_swpv_145_pivot_velocity_acceleration_decline_indicator_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_145_pivot_velocity_acceleration_decline_indicator_252d},
    "f10_swpv_146_structural_decay_score_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_146_structural_decay_score_252d},
    "f10_swpv_147_zigzag_compression_top_indicator_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_147_zigzag_compression_top_indicator_252d},
    "f10_swpv_148_pivot_high_age_stale_indicator_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_148_pivot_high_age_stale_indicator_252d},
    "f10_swpv_149_swing_failure_pattern_indicator_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_149_swing_failure_pattern_indicator_252d},
    "f10_swpv_150_composite_topology_top_score_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_150_composite_topology_top_score_252d},
}
