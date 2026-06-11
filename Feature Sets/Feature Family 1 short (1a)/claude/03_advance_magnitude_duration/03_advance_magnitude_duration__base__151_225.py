"""advance_magnitude_duration base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for advance-magnitude / duration detection.
This file carries indices 151-155 (5 distinct hypotheses). Reserved range up to 225.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(-N). Self-contained — no imports across families.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_5Y = 1260


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


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _days_since_multiple(close: pd.Series, low: pd.Series, mult: float) -> pd.Series:
    """Bars since close first crossed mult * (252d trailing low) within the current 252d window.

    For each bar t: identify the 252d-low bar in [t-251, t]; find earliest bar within that window
    AT or after the trough where close >= mult * trough_value; return t - that bar.
    Returns NaN if no crossing observed or window not yet full.
    """
    c = close.to_numpy(dtype=float)
    lo = low.to_numpy(dtype=float)
    n = len(c)
    out = np.full(n, np.nan, dtype=float)
    for t in range(n):
        start = max(0, t - YDAYS + 1)
        win = lo[start:t + 1]
        valid = ~np.isnan(win)
        if valid.sum() < QDAYS:
            continue
        masked = np.where(valid, win, np.inf)
        anchor_local = int(np.argmin(masked))
        trough_val = win[anchor_local]
        if not np.isfinite(trough_val) or trough_val <= 0:
            continue
        anchor = start + anchor_local
        target = mult * trough_val
        post = c[anchor:t + 1]
        hits = np.where(np.isfinite(post) & (post >= target))[0]
        if len(hits) == 0:
            continue
        first_cross = anchor + int(hits[0])
        out[t] = float(t - first_cross)
    return pd.Series(out, index=close.index)


# ============================================================
#                    FEATURES 151-155
# ============================================================


def f03_amad_151_days_since_2x_from_252d_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since close first crossed 2x the 252d trailing low (within current 252d window)."""
    return _days_since_multiple(close, low, 2.0)


def f03_amad_152_days_since_3x_from_252d_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since close first crossed 3x the 252d trailing low (within current 252d window)."""
    return _days_since_multiple(close, low, 3.0)


def f03_amad_153_days_since_5x_from_252d_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since close first crossed 5x the 252d trailing low (within current 252d window)."""
    return _days_since_multiple(close, low, 5.0)


def f03_amad_154_prior_cycle_max_drawdown_5y(close: pd.Series) -> pd.Series:
    """Largest peak-to-trough drawdown observed in trailing 1260d window. Min_periods=252."""

    def _mdd(w):
        valid = ~np.isnan(w)
        x = w[valid]
        if len(x) < YDAYS:
            return np.nan
        cummax = np.maximum.accumulate(x)
        cm = np.where(cummax == 0, np.nan, cummax)
        dd = (x - cummax) / cm
        return float(np.nanmin(dd))

    return close.rolling(DDAYS_5Y, min_periods=YDAYS).apply(_mdd, raw=True)


def f03_amad_155_pivot_swing_count_during_advance_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of past-only pivot-3 swing highs + swing lows in trailing 252d.

    PIT-safe pivot-3: at bar t, check if high[t-3] > all of high[t-6..t-1] (excluding t-3 itself,
    i.e. high[t-6], high[t-5], high[t-4], high[t-2], high[t-1]); same for low (strict min).
    All comparisons use only past data (no future bars). Counts both swing-high and swing-low events.
    """
    h = high
    l = low
    # Center index = t-3; required neighbors = t-6..t-4 and t-2..t-1
    center_h = h.shift(3)
    h_m1 = h.shift(1)
    h_m2 = h.shift(2)
    h_m4 = h.shift(4)
    h_m5 = h.shift(5)
    h_m6 = h.shift(6)
    swing_high = (
        (center_h > h_m1)
        & (center_h > h_m2)
        & (center_h > h_m4)
        & (center_h > h_m5)
        & (center_h > h_m6)
    )
    center_l = l.shift(3)
    l_m1 = l.shift(1)
    l_m2 = l.shift(2)
    l_m4 = l.shift(4)
    l_m5 = l.shift(5)
    l_m6 = l.shift(6)
    swing_low = (
        (center_l < l_m1)
        & (center_l < l_m2)
        & (center_l < l_m4)
        & (center_l < l_m5)
        & (center_l < l_m6)
    )
    swings = (swing_high.fillna(False) | swing_low.fillna(False)).astype(float)
    return swings.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
#                    REGISTRY
# ============================================================

ADVANCE_MAGNITUDE_DURATION_BASE_REGISTRY_151_225 = {
    "f03_amad_151_days_since_2x_from_252d_low": {"inputs": ["close", "low"], "func": f03_amad_151_days_since_2x_from_252d_low},
    "f03_amad_152_days_since_3x_from_252d_low": {"inputs": ["close", "low"], "func": f03_amad_152_days_since_3x_from_252d_low},
    "f03_amad_153_days_since_5x_from_252d_low": {"inputs": ["close", "low"], "func": f03_amad_153_days_since_5x_from_252d_low},
    "f03_amad_154_prior_cycle_max_drawdown_5y": {"inputs": ["close"], "func": f03_amad_154_prior_cycle_max_drawdown_5y},
    "f03_amad_155_pivot_swing_count_during_advance_252d": {"inputs": ["close", "high", "low"], "func": f03_amad_155_pivot_swing_count_during_advance_252d},
}
