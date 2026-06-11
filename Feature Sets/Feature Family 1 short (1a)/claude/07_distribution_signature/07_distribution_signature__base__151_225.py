"""distribution_signature base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for Wyckoff-style distribution detection.
This file carries indices 151-152 (2 distinct hypotheses). Reserved range up to 225.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(-N). Self-contained — no imports across families.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


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


# ============================================================
#                    FEATURES 151-152
# ============================================================


def f07_dsig_151_spring_upthrust_ratio_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of upthrust bars to spring bars over 63d — Wyckoff distribution-vs-accumulation balance.

    Upthrust: new 21d high AND close in lower third of the bar range.
    Spring: new 21d low AND close in upper third of the bar range.
    Both are flagged per bar; the ratio is rolling count(upthrust)/count(spring) over 63d.
    Where count(spring) == 0, returns NaN (avoids spurious inf).
    """
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    rmin21 = low.rolling(MDAYS, min_periods=WDAYS).min()
    rng = (high - low).replace(0, np.nan)
    pos = _safe_div(close - low, rng)  # 0 = at low, 1 = at high
    new_high = high >= rmax21
    new_low = low <= rmin21
    upthrust = (new_high & (pos < (1.0 / 3.0))).astype(float)
    spring = (new_low & (pos > (2.0 / 3.0))).astype(float)
    up_ct = upthrust.rolling(QDAYS, min_periods=MDAYS).sum()
    sp_ct = spring.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(up_ct, sp_ct)


def f07_dsig_152_distribution_day_after_252d_high_count_42d(close: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    """Count of distribution days in last 42d that occurred AFTER the most recent 252d-high bar within 42d.

    Distribution day := close down > 0.2% AND volume > prior-day volume.
    Conditioned on: trailing 42d contains a new 252d high. If no 252d high in last 42d, return NaN.
    Fully vectorized: uses cummax on position indices to find last-high-idx, and cumsum
    differencing to count distribution days strictly after that index.
    """
    ret = _safe_log(close).diff()
    dist_day = ((ret < -0.002) & (volume > volume.shift(1))).astype(float)
    rmax252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_new_high = (high >= rmax252) & rmax252.notna()
    HORIZON = 2 * MDAYS  # 42

    n = len(close)
    pos = np.arange(n, dtype=np.float64)
    # last_high_idx[t] = max position k<=t such that is_new_high[k]; else NaN
    # pandas .cummax() leaves NaN where the input is NaN — use fmax.accumulate on
    # a -inf-replaced array and restore NaN where no high has ever fired.
    high_pos = np.where(is_new_high.values, pos, -np.inf)
    cm = np.fmax.accumulate(high_pos)
    last_high_idx = pd.Series(np.where(cm == -np.inf, np.nan, cm), index=close.index)
    # cumulative count of distribution days (treat NaN as 0 for the sum but track validity separately)
    dd_arr = dist_day.values.astype(float)
    dd_safe = np.where(np.isnan(dd_arr), 0.0, dd_arr)
    cum_dd = np.concatenate(([0.0], np.cumsum(dd_safe)))  # cum_dd[k] = sum of dd[0..k-1]
    # count of distribution days in (lh, t]  = cum_dd[t+1] - cum_dd[lh+1]
    t_arr = pos.astype(np.int64)
    lh = last_high_idx.values
    # qualifying mask: lh is not NaN AND lh >= t - HORIZON + 1
    window_start = t_arr - HORIZON + 1
    qualifies = (~np.isnan(lh)) & (lh >= window_start)
    lh_int = np.where(np.isnan(lh), 0, lh).astype(np.int64)
    raw = cum_dd[t_arr + 1] - cum_dd[lh_int + 1]
    out = np.where(qualifies, raw, np.nan)
    return pd.Series(out, index=close.index)


# ============================================================
#                    REGISTRY
# ============================================================

DISTRIBUTION_SIGNATURE_BASE_REGISTRY_151_225 = {
    "f07_dsig_151_spring_upthrust_ratio_63d": {"inputs": ["close", "high", "low"], "func": f07_dsig_151_spring_upthrust_ratio_63d},
    "f07_dsig_152_distribution_day_after_252d_high_count_42d": {"inputs": ["close", "volume", "high"], "func": f07_dsig_152_distribution_day_after_252d_high_count_42d},
}
