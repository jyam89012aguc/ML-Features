"""topping_pattern base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for topping-pattern recognition.
This file carries indices 151-158 (8 distinct hypotheses). Reserved range up to 225.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(-N). Self-contained — no imports across families.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
HALF_Y = 126
WIN_42 = 42
WIN_84 = 84


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


def _slope_lr(w):
    """Simple least-squares slope of w vs x=[0..n-1]. NaN-aware."""
    valid = ~np.isnan(w)
    n = int(valid.sum())
    if n < 5:
        return np.nan
    y = w[valid]
    x = np.arange(len(w), dtype=float)[valid]
    xm = x.mean()
    ym = y.mean()
    denom = ((x - xm) ** 2).sum()
    if denom == 0:
        return np.nan
    return float(((x - xm) * (y - ym)).sum() / denom)


def _quad_r2(w):
    """R^2 of quadratic (degree-2) polyfit of w vs x=[0..n-1]. NaN-aware."""
    valid = ~np.isnan(w)
    n = int(valid.sum())
    if n < 6:
        return np.nan
    y = w[valid]
    x = np.arange(len(w), dtype=float)[valid]
    try:
        coefs = np.polyfit(x, y, 2)
    except (np.linalg.LinAlgError, ValueError):
        return np.nan
    yhat = np.polyval(coefs, x)
    ss_res = float(((y - yhat) ** 2).sum())
    ss_tot = float(((y - y.mean()) ** 2).sum())
    if ss_tot == 0:
        return np.nan
    return 1.0 - ss_res / ss_tot


# ============================================================
#                    FEATURES 151-158
# ============================================================


def f04_topp_151_descending_triangle_at_top_score_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Active only when high within 10% of 252d high. Score = (-slope_high_63d) * (1 - |slope_low_63d|)."""
    rmax_252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    near_top = _safe_div(high, rmax_252) >= 0.90
    slope_h = high.rolling(QDAYS, min_periods=MDAYS).apply(_slope_lr, raw=True)
    slope_l = low.rolling(QDAYS, min_periods=MDAYS).apply(_slope_lr, raw=True)
    score = (-slope_h) * (1.0 - slope_l.abs())
    return score.where(near_top, np.nan)


def f04_topp_152_adam_eve_top_indicator_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """First-half max single-bar log return (sharpness) * second-half quadratic R^2 (dome arc).

    Window = trailing 252d. First half = bars [0..126), second half = bars [126..252).
    """
    lc = _safe_log(close).to_numpy(dtype=float)
    r = np.empty_like(lc)
    r[:] = np.nan
    r[1:] = np.diff(lc)
    c = close.to_numpy(dtype=float)
    n = len(c)
    out = np.full(n, np.nan, dtype=float)
    for t in range(n):
        start = max(0, t - YDAYS + 1)
        if (t - start + 1) < YDAYS:
            continue
        first = r[start:start + HALF_Y]
        second = c[start + HALF_Y:t + 1]
        fv = first[~np.isnan(first)]
        if len(fv) < MDAYS:
            continue
        sharp = float(np.nanmax(fv))
        r2 = _quad_r2(second.astype(float))
        if not np.isfinite(r2):
            continue
        out[t] = sharp * r2
    return pd.Series(out, index=close.index)


def f04_topp_153_v_top_sharpness_42d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """In trailing 42d window: (max(high) - close_at_t) / ATR21_at_t. Larger = sharper top."""
    rmax_42 = high.rolling(WIN_42, min_periods=MDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(rmax_42 - close, atr)


def f04_topp_154_tweezer_top_at_high_count_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of tweezer-top candles (matching highs over 2 bars) within 5% of 252d high in 63d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = _safe_div(high, rmax) >= 0.95
    matching = _safe_div((high - high.shift(1)).abs(), high.shift(1)) < 0.005
    bearish = close < open_
    twz = (matching & near & near.shift(1).fillna(False) & bearish).astype(float)
    return twz.rolling(QDAYS, min_periods=MDAYS).sum()


def f04_topp_155_three_line_strike_bearish_at_high_count_63d(open_: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish three-line strike near 252d high in 63d.

    Pattern: bars t-3, t-2, t-1 each bullish AND each closes higher than previous; bar t bearish
    that closes BELOW open of bar t-3 (engulfs the run). Conditioned on high within 5% of 252d high.
    """
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = _safe_div(high, rmax) >= 0.95
    bull3 = (close.shift(3) > open_.shift(3))
    bull2 = (close.shift(2) > open_.shift(2)) & (close.shift(2) > close.shift(3))
    bull1 = (close.shift(1) > open_.shift(1)) & (close.shift(1) > close.shift(2))
    bear0 = (close < open_) & (close < open_.shift(3))
    pat = (bull3 & bull2 & bull1 & bear0 & near).astype(float)
    return pat.rolling(QDAYS, min_periods=MDAYS).sum()


def f04_topp_156_advance_block_at_high_count_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Advance block near 252d high in 63d.

    Pattern: bars t-2, t-1, t each bullish; each body shorter than previous (decelerating);
    each upper wick longer than previous (resistance). Conditioned on high within 5% of 252d high.
    """
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = _safe_div(high, rmax) >= 0.95
    bull0 = close > open_
    bull1 = close.shift(1) > open_.shift(1)
    bull2 = close.shift(2) > open_.shift(2)
    body0 = (close - open_).abs()
    body1 = (close.shift(1) - open_.shift(1)).abs()
    body2 = (close.shift(2) - open_.shift(2)).abs()
    body_top0 = pd.concat([open_, close], axis=1).max(axis=1)
    body_top1 = pd.concat([open_.shift(1), close.shift(1)], axis=1).max(axis=1)
    body_top2 = pd.concat([open_.shift(2), close.shift(2)], axis=1).max(axis=1)
    uw0 = high - body_top0
    uw1 = high.shift(1) - body_top1
    uw2 = high.shift(2) - body_top2
    decel = (body0 < body1) & (body1 < body2)
    wick_grow = (uw0 > uw1) & (uw1 > uw2)
    pat = (bull0 & bull1 & bull2 & decel & wick_grow & near).astype(float)
    return pat.rolling(QDAYS, min_periods=MDAYS).sum()


def f04_topp_157_lowering_base_pattern_score_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """In trailing 252d: count of consecutive 21d "bases" (low rvol) with monotonically decreasing lows.

    Base = 21d window whose realized vol of log returns is below the 252d median of rvol_21d.
    Track each base's min(low). Count longest run of consecutive non-overlapping bases (chained
    21d apart) with strictly decreasing base-low values, ending at bar t.
    """
    r = _safe_log(close).diff()
    rvol_21 = r.rolling(MDAYS, min_periods=WDAYS).std(ddof=1)
    median_rvol = rvol_21.rolling(YDAYS, min_periods=QDAYS).median()
    rmin_21 = low.rolling(MDAYS, min_periods=WDAYS).min()

    rv = rvol_21.to_numpy(dtype=float)
    mr = median_rvol.to_numpy(dtype=float)
    rl = rmin_21.to_numpy(dtype=float)
    n = len(close)
    out = np.full(n, np.nan, dtype=float)

    for t in range(n):
        start = max(0, t - YDAYS + 1)
        if (t - start + 1) < QDAYS:
            continue
        # Walk backward in 21d chunks ending at t, t-21, t-42, ...
        bases = []  # list of (idx, base_low)
        idx = t
        while idx >= start:
            if not np.isfinite(rv[idx]) or not np.isfinite(mr[idx]) or not np.isfinite(rl[idx]):
                break
            if rv[idx] < mr[idx]:
                bases.append(rl[idx])
                idx -= MDAYS
            else:
                break
        # bases listed t -> earlier; check strictly decreasing low going forward in time
        if len(bases) < 2:
            out[t] = 0.0
            continue
        # bases[0] is most recent; for "each base low < prior base low" going forward in time,
        # require bases[k] < bases[k+1] (since k+1 is earlier in time, "prior" in forward order).
        count = 0
        for k in range(len(bases) - 1):
            if bases[k] < bases[k + 1]:
                count += 1
            else:
                break
        out[t] = float(count)
    return pd.Series(out, index=close.index)


def f04_topp_158_three_peaks_domed_house_score_252d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Lindsay three-peaks-domed-house composite.

    In trailing 252d: count distinct local-max peaks (past-only pivot-3) at similar levels
    (within 5% of the 252d max). Require >= 3 such peaks. Then check subsequent rounded top
    via quadratic R^2 on the last 84d, and a final lower-high (high[t] < 252d max). Score is
    composite product (0 if any condition fails or count<3).
    """
    h = high
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
    ).fillna(False)
    sh_arr = swing_high.to_numpy(dtype=bool)
    h_arr = h.to_numpy(dtype=float)
    c_arr = close.to_numpy(dtype=float)
    n = len(close)
    out = np.full(n, np.nan, dtype=float)

    # rolling 252d max of high
    rmax_252 = h.rolling(YDAYS, min_periods=QDAYS).max().to_numpy(dtype=float)
    # rolling 84d r2 of close (quadratic)
    r2_84 = close.rolling(WIN_84, min_periods=MDAYS).apply(_quad_r2, raw=True).to_numpy(dtype=float)

    for t in range(n):
        start = max(0, t - YDAYS + 1)
        if (t - start + 1) < QDAYS:
            continue
        rmx = rmax_252[t]
        if not np.isfinite(rmx) or rmx <= 0:
            continue
        # peak values inside the window where the swing-high condition fired; the swing-high
        # detection produces the centered peak value via center_h = high.shift(3), so we use
        # h_arr[i-3] for swing_high[i].
        peak_vals = []
        for i in range(start, t + 1):
            if sh_arr[i] and i - 3 >= 0:
                pv = h_arr[i - 3]
                if np.isfinite(pv):
                    peak_vals.append(pv)
        if len(peak_vals) < 3:
            out[t] = 0.0
            continue
        peak_arr = np.asarray(peak_vals, dtype=float)
        similar = (peak_arr >= 0.95 * rmx).sum()
        if similar < 3:
            out[t] = 0.0
            continue
        r2_val = r2_84[t]
        if not np.isfinite(r2_val) or r2_val <= 0:
            out[t] = 0.0
            continue
        # lower-high formation check: current high strictly below 252d max
        h_t = h_arr[t]
        if not np.isfinite(h_t) or h_t >= rmx:
            out[t] = 0.0
            continue
        lower_high_score = (rmx - h_t) / rmx
        out[t] = float(similar) * float(r2_val) * float(lower_high_score)
    return pd.Series(out, index=close.index)


# ============================================================
#                    REGISTRY
# ============================================================

TOPPING_PATTERN_BASE_REGISTRY_151_225 = {
    "f04_topp_151_descending_triangle_at_top_score_63d": {"inputs": ["close", "high", "low"], "func": f04_topp_151_descending_triangle_at_top_score_63d},
    "f04_topp_152_adam_eve_top_indicator_252d": {"inputs": ["close", "high", "low"], "func": f04_topp_152_adam_eve_top_indicator_252d},
    "f04_topp_153_v_top_sharpness_42d": {"inputs": ["close", "high", "low"], "func": f04_topp_153_v_top_sharpness_42d},
    "f04_topp_154_tweezer_top_at_high_count_63d": {"inputs": ["open", "high", "low", "close"], "func": f04_topp_154_tweezer_top_at_high_count_63d},
    "f04_topp_155_three_line_strike_bearish_at_high_count_63d": {"inputs": ["open", "high", "close"], "func": f04_topp_155_three_line_strike_bearish_at_high_count_63d},
    "f04_topp_156_advance_block_at_high_count_63d": {"inputs": ["open", "high", "low", "close"], "func": f04_topp_156_advance_block_at_high_count_63d},
    "f04_topp_157_lowering_base_pattern_score_252d": {"inputs": ["close", "high", "low"], "func": f04_topp_157_lowering_base_pattern_score_252d},
    "f04_topp_158_three_peaks_domed_house_score_252d": {"inputs": ["close", "high"], "func": f04_topp_158_three_peaks_domed_house_score_252d},
}
