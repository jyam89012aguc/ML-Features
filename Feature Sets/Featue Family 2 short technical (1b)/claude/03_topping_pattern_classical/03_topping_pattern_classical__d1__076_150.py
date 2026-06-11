"""topping_pattern_classical base 076-150 — Pipeline 1b-technical.

Continuation of 03_topping_pattern_classical (see __base__001_075.py for the
first 75 hypotheses). This file covers:
- Diamond top refinements (076-080)
- Bump-and-Run Reversal (BARR / Bulkowski) family (081-088)
- Adam / Eve double-top typology (089-096)
- Lindsay / Schabacker / Wyckoff specialist patterns (097-104)
- Universal pattern symmetry & timing metrics (105-116)
- Pattern failure / completion detection (117-126)
- Pattern projection / measured-move metrics (127-134)
- Composite pattern scores (narrow pattern-internal scope) (135-150)

Inputs: SEP OHLCV only. PIT-clean. Self-contained helpers.
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


def _pivot_highs_mask(high, k=5):
    h = high.values.astype(float)
    n = len(h)
    win = 2 * k + 1
    out = np.full(n, np.nan)
    if n < win:
        return pd.Series(out, index=high.index)
    for i in range(win - 1, n):
        seg = h[i - 2 * k:i + 1]
        if np.isnan(seg).any():
            out[i] = np.nan
            continue
        mid = seg[k]
        if mid == seg.max() and mid > seg[0] and mid > seg[-1]:
            out[i] = 1.0
        else:
            out[i] = 0.0
    return pd.Series(out, index=high.index)


def _pivot_lows_mask(low, k=5):
    l = low.values.astype(float)
    n = len(l)
    win = 2 * k + 1
    out = np.full(n, np.nan)
    if n < win:
        return pd.Series(out, index=low.index)
    for i in range(win - 1, n):
        seg = l[i - 2 * k:i + 1]
        if np.isnan(seg).any():
            out[i] = np.nan
            continue
        mid = seg[k]
        if mid == seg.min() and mid < seg[0] and mid < seg[-1]:
            out[i] = 1.0
        else:
            out[i] = 0.0
    return pd.Series(out, index=low.index)


def f03_tpcl_076_diamond_top_declining_volume_during_contraction_252d_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Inside the contraction-half of a diamond (last 126d of 252d), volume slope.
    Negative = textbook diamond top (volume contracting as price contracts)."""
    rng = high - low
    def _f(w_r, w_v):
        n = len(w_r)
        if n < 30 or np.isnan(w_r).any():
            return np.nan
        h = n // 2
        v_second = w_v[h:]
        valid = ~np.isnan(v_second)
        if valid.sum() < 5:
            return np.nan
        x = np.arange(len(v_second), dtype=float)[valid]
        y = v_second[valid]
        if y.std() == 0:
            return 0.0
        xm = x.mean(); ym = y.mean()
        num = ((x - xm) * (y - ym)).sum()
        den = ((x - xm) ** 2).sum()
        return float(num / den) if den != 0 else np.nan
    out = np.full(len(high), np.nan)
    r_v = rng.values; v_v = volume.values
    for i in range(QDAYS, len(high)):
        lo = max(0, i - YDAYS + 1)
        out[i] = _f(r_v[lo:i + 1], v_v[lo:i + 1])
    return (pd.Series(out, index=high.index)).diff()


def f03_tpcl_077_diamond_top_breakout_direction_indicator_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Once diamond top contracts (last 21d range < 0.5 * peak-range), +1 if close
    breaks above prior high, -1 if breaks below prior low, 0 inside."""
    rng = high - low
    peak_rng = rng.rolling(YDAYS, min_periods=QDAYS).max()
    short_rng = rng.rolling(MDAYS, min_periods=WDAYS).mean()
    contracted = short_rng < 0.5 * peak_rng
    rh = high.rolling(MDAYS, min_periods=WDAYS).max()
    rl = low.rolling(MDAYS, min_periods=WDAYS).min()
    d = np.where(close > rh.shift(1), 1.0, np.where(close < rl.shift(1), -1.0, 0.0))
    return (pd.Series(d, index=high.index).where(contracted, np.nan)).diff()


def f03_tpcl_078_diamond_top_breakdown_magnitude_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Magnitude of breakdown from diamond top: (diamond-low - close) / diamond-range.
    Positive = real breakdown."""
    rng_max = (high - low).rolling(YDAYS, min_periods=QDAYS).max()
    rl = low.rolling(YDAYS, min_periods=QDAYS).min()
    return (_safe_div(rl - close, rng_max)).diff()


def f03_tpcl_079_diamond_top_vs_broadening_differentiator_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Differentiator: range-slope-first-half MINUS range-slope-second-half. Diamond
    is positive (expansion then contraction); pure broadening is positive both halves
    so diff is small. Larger positive value = more diamond-like, less broadening."""
    rng = high - low
    def _f(w):
        if np.isnan(w).any():
            return np.nan
        n = len(w)
        h = n // 2
        if h < 5:
            return np.nan
        s1 = np.polyfit(np.arange(h), w[:h], 1)[0]
        s2 = np.polyfit(np.arange(n - h), w[h:], 1)[0]
        return float(s1 - s2)
    return (rng.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)).diff()


def f03_tpcl_080_diamond_top_quality_R2_fit_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fit quality of diamond template (quadratic with negative coefficient on range
    over 252d) — R² of quadratic fit on bar-range."""
    rng = high - low
    def _r2(w):
        if np.isnan(w).any():
            return np.nan
        try:
            x = np.arange(len(w), dtype=float)
            coefs = np.polyfit(x, w, 2)
            if coefs[0] >= 0:
                return 0.0
            yhat = np.polyval(coefs, x)
            ss_res = float(((w - yhat) ** 2).sum())
            ss_tot = float(((w - w.mean()) ** 2).sum())
            if ss_tot == 0:
                return np.nan
            return float(1.0 - ss_res / ss_tot)
        except Exception:
            return np.nan
    return (rng.rolling(YDAYS, min_periods=QDAYS).apply(_r2, raw=True)).diff()


def f03_tpcl_081_barr_lead_in_slope_252d_d1(close: pd.Series) -> pd.Series:
    """Lead-in phase: slope of close over the first half (oldest 126d) of 252d.
    Bulkowski's BARR expects a GENTLE positive lead-in slope."""
    def _s(w):
        n = len(w)
        if n < 30 or np.isnan(w).any():
            return np.nan
        h = n // 2
        x = np.arange(h, dtype=float); y = w[:h]
        return float(np.polyfit(x, y, 1)[0])
    return (close.rolling(YDAYS, min_periods=QDAYS).apply(_s, raw=True)).diff()


def f03_tpcl_082_barr_bump_slope_252d_d1(close: pd.Series) -> pd.Series:
    """Bump phase: slope of close over the second half (newest 126d) of 252d.
    BARR expects a STEEP positive bump slope (acceleration)."""
    def _s(w):
        n = len(w)
        if n < 30 or np.isnan(w).any():
            return np.nan
        h = n // 2
        x = np.arange(n - h, dtype=float); y = w[h:]
        return float(np.polyfit(x, y, 1)[0])
    return (close.rolling(YDAYS, min_periods=QDAYS).apply(_s, raw=True)).diff()


def f03_tpcl_083_barr_bump_to_lead_in_slope_ratio_252d_d1(close: pd.Series) -> pd.Series:
    """Slope ratio: bump-slope / lead-in-slope. Bulkowski's BARR confirms when
    ratio >= 2.0. Larger value = textbook BARR."""
    def _r(w):
        n = len(w)
        if n < 30 or np.isnan(w).any():
            return np.nan
        h = n // 2
        s_lead = float(np.polyfit(np.arange(h, dtype=float), w[:h], 1)[0])
        s_bump = float(np.polyfit(np.arange(n - h, dtype=float), w[h:], 1)[0])
        if s_lead <= 0:
            return np.nan
        return s_bump / s_lead
    return (close.rolling(YDAYS, min_periods=QDAYS).apply(_r, raw=True)).diff()


def f03_tpcl_084_barr_target_estimate_252d_d1(close: pd.Series, low: pd.Series) -> pd.Series:
    """BARR target: projected drop to lead-in trendline level — distance from
    current close to start-of-window value, as a ratio of close."""
    def _t(w):
        n = len(w)
        if n < 30 or np.isnan(w).any():
            return np.nan
        last = float(w[-1])
        first = float(w[0])
        if last <= 0:
            return np.nan
        return (last - first) / last
    return (close.rolling(YDAYS, min_periods=QDAYS).apply(_t, raw=True)).diff()


def f03_tpcl_085_barr_completion_event_indicator_252d_d1(close: pd.Series) -> pd.Series:
    """BARR completes when close pierces the lead-in trendline (proxied as
    252d-back value). Indicator 0/1."""
    lead_in_level = close.shift(YDAYS - 1)
    return ((close < lead_in_level).astype(float).where(lead_in_level.notna(), np.nan)).diff()


def f03_tpcl_086_barr_bump_phase_volume_profile_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume slope in the bump phase (second half of 252d). Strong rising volume
    is textbook BARR confirmation."""
    def _s(w):
        n = len(w)
        if n < 30 or np.isnan(w).any():
            return np.nan
        h = n // 2
        x = np.arange(n - h, dtype=float); y = w[h:]
        return float(np.polyfit(x, y, 1)[0])
    return (volume.rolling(YDAYS, min_periods=QDAYS).apply(_s, raw=True)).diff()


def f03_tpcl_087_barr_lead_in_line_break_event_indicator_252d_d1(close: pd.Series) -> pd.Series:
    """Lead-in line break: extrapolate lead-in slope forward; indicator if close
    is below extrapolated line at current bar. Proxy: lead-in slope projected
    over second half + start value."""
    def _b(w):
        n = len(w)
        if n < 30 or np.isnan(w).any():
            return np.nan
        h = n // 2
        x = np.arange(h, dtype=float); y = w[:h]
        sl, ic = np.polyfit(x, y, 1)
        # extrapolate to position n-1
        line_val = sl * (n - 1) + ic
        return float(1.0 if w[-1] < line_val else 0.0)
    return (close.rolling(YDAYS, min_periods=QDAYS).apply(_b, raw=True)).diff()


def f03_tpcl_088_barr_breakdown_follow_through_magnitude_252d_d1(close: pd.Series) -> pd.Series:
    """Once BARR breaks (close below extrapolated lead-in line), magnitude of
    follow-through: (lead-in line - close) / close."""
    def _b(w):
        n = len(w)
        if n < 30 or np.isnan(w).any():
            return np.nan
        h = n // 2
        x = np.arange(h, dtype=float); y = w[:h]
        sl, ic = np.polyfit(x, y, 1)
        line_val = sl * (n - 1) + ic
        if w[-1] >= line_val or w[-1] <= 0:
            return 0.0
        return float((line_val - w[-1]) / w[-1])
    return (close.rolling(YDAYS, min_periods=QDAYS).apply(_b, raw=True)).diff()


def f03_tpcl_089_adam_sharp_then_eve_round_double_top_63d_d1(high: pd.Series) -> pd.Series:
    """Adam-Eve: top-2 pivots, first is sharp (narrow), second is rounded (wide).
    Score: (right-peak-width / left-peak-width). Higher = more Eve right of Adam."""
    piv_h = high.where(_pivot_highs_mask(high, k=3) > 0, np.nan)
    def _f(w):
        mask = ~np.isnan(w)
        if mask.sum() < 2:
            return np.nan
        idxs = np.where(mask)[0]
        vals = w[mask]
        sv = np.argsort(vals)[::-1][:2]
        pos = np.sort(idxs[sv])
        p1, p2 = int(pos[0]), int(pos[1])
        # Width = bars within 1% of the peak around each pivot
        peak1 = w[p1]; peak2 = w[p2]
        def width(c, val):
            cnt = 1
            j = c - 1
            while j >= 0 and not np.isnan(w[j]) and w[j] >= 0.99 * val:
                cnt += 1; j -= 1
            j = c + 1
            while j < len(w) and not np.isnan(w[j]) and w[j] >= 0.99 * val:
                cnt += 1; j += 1
            return cnt
        w1 = width(p1, peak1); w2 = width(p2, peak2)
        if w1 == 0:
            return np.nan
        return float(w2 / w1)
    out = np.full(len(high), np.nan)
    pv = high.values
    h_vals = piv_h.values
    for i in range(MDAYS, len(high)):
        lo = max(0, i - QDAYS + 1)
        # need raw highs in same window for width measurement
        h_window = pv[lo:i + 1].copy()
        # use pivot mask but width based on full bar window
        mask = ~np.isnan(h_vals[lo:i + 1])
        if mask.sum() < 2:
            continue
        idxs = np.where(mask)[0]
        vals = h_vals[lo:i + 1][mask]
        sv = np.argsort(vals)[::-1][:2]
        pos = np.sort(idxs[sv])
        p1, p2 = int(pos[0]), int(pos[1])
        peak1 = h_window[p1]; peak2 = h_window[p2]
        def width(c, val):
            cnt = 1
            j = c - 1
            while j >= 0 and not np.isnan(h_window[j]) and h_window[j] >= 0.99 * val:
                cnt += 1; j -= 1
            j = c + 1
            while j < len(h_window) and not np.isnan(h_window[j]) and h_window[j] >= 0.99 * val:
                cnt += 1; j += 1
            return cnt
        w1 = width(p1, peak1); w2 = width(p2, peak2)
        if w1 == 0:
            continue
        out[i] = float(w2 / w1)
    return (pd.Series(out, index=high.index)).diff()


def f03_tpcl_090_eve_round_then_adam_sharp_double_top_63d_d1(high: pd.Series) -> pd.Series:
    """Eve-Adam variant: first peak rounded, second peak sharp. Score
    = (left-width / right-width). Higher = textbook Eve-Adam."""
    out = np.full(len(high), np.nan)
    h_vals = high.values
    piv_h = high.where(_pivot_highs_mask(high, k=3) > 0, np.nan).values
    for i in range(MDAYS, len(high)):
        lo = max(0, i - QDAYS + 1)
        w_p = piv_h[lo:i + 1]
        w_h = h_vals[lo:i + 1]
        mask = ~np.isnan(w_p)
        if mask.sum() < 2:
            continue
        idxs = np.where(mask)[0]
        vals = w_p[mask]
        sv = np.argsort(vals)[::-1][:2]
        pos = np.sort(idxs[sv])
        p1, p2 = int(pos[0]), int(pos[1])
        def width(c, val):
            cnt = 1
            j = c - 1
            while j >= 0 and not np.isnan(w_h[j]) and w_h[j] >= 0.99 * val:
                cnt += 1; j -= 1
            j = c + 1
            while j < len(w_h) and not np.isnan(w_h[j]) and w_h[j] >= 0.99 * val:
                cnt += 1; j += 1
            return cnt
        w1 = width(p1, w_h[p1]); w2 = width(p2, w_h[p2])
        if w2 == 0:
            continue
        out[i] = float(w1 / w2)
    return (pd.Series(out, index=high.index)).diff()


def f03_tpcl_091_eve_eve_double_top_both_rounded_63d_d1(high: pd.Series) -> pd.Series:
    """Eve-Eve: both peaks rounded (both widths >= 4 bars). Score = min(w1,w2)."""
    out = np.full(len(high), np.nan)
    h_vals = high.values
    piv_h = high.where(_pivot_highs_mask(high, k=3) > 0, np.nan).values
    for i in range(MDAYS, len(high)):
        lo = max(0, i - QDAYS + 1)
        w_p = piv_h[lo:i + 1]; w_h = h_vals[lo:i + 1]
        mask = ~np.isnan(w_p)
        if mask.sum() < 2:
            continue
        idxs = np.where(mask)[0]; vals = w_p[mask]
        sv = np.argsort(vals)[::-1][:2]
        pos = np.sort(idxs[sv])
        p1, p2 = int(pos[0]), int(pos[1])
        def width(c, val):
            cnt = 1
            j = c - 1
            while j >= 0 and not np.isnan(w_h[j]) and w_h[j] >= 0.99 * val:
                cnt += 1; j -= 1
            j = c + 1
            while j < len(w_h) and not np.isnan(w_h[j]) and w_h[j] >= 0.99 * val:
                cnt += 1; j += 1
            return cnt
        w1 = width(p1, w_h[p1]); w2 = width(p2, w_h[p2])
        if w1 < 4 or w2 < 4:
            out[i] = 0.0
        else:
            out[i] = float(min(w1, w2))
    return (pd.Series(out, index=high.index)).diff()


def f03_tpcl_092_adam_adam_double_top_both_sharp_63d_d1(high: pd.Series) -> pd.Series:
    """Adam-Adam: both peaks sharp (single-bar pivots, both widths <= 2). Indicator."""
    out = np.full(len(high), np.nan)
    h_vals = high.values
    piv_h = high.where(_pivot_highs_mask(high, k=3) > 0, np.nan).values
    for i in range(MDAYS, len(high)):
        lo = max(0, i - QDAYS + 1)
        w_p = piv_h[lo:i + 1]; w_h = h_vals[lo:i + 1]
        mask = ~np.isnan(w_p)
        if mask.sum() < 2:
            continue
        idxs = np.where(mask)[0]; vals = w_p[mask]
        sv = np.argsort(vals)[::-1][:2]
        pos = np.sort(idxs[sv])
        p1, p2 = int(pos[0]), int(pos[1])
        def width(c, val):
            cnt = 1
            j = c - 1
            while j >= 0 and not np.isnan(w_h[j]) and w_h[j] >= 0.99 * val:
                cnt += 1; j -= 1
            j = c + 1
            while j < len(w_h) and not np.isnan(w_h[j]) and w_h[j] >= 0.99 * val:
                cnt += 1; j += 1
            return cnt
        w1 = width(p1, w_h[p1]); w2 = width(p2, w_h[p2])
        out[i] = float(1.0 if (w1 <= 2 and w2 <= 2) else 0.0)
    return (pd.Series(out, index=high.index)).diff()


def f03_tpcl_093_sharp_peak_single_bar_height_vs_neighbors_21d_d1(high: pd.Series) -> pd.Series:
    """Sharp-peak metric: ratio of today's high to mean of 21d high. Large value =
    today's bar is a sharp solitary peak."""
    mn = high.rolling(MDAYS, min_periods=WDAYS).mean()
    return (_safe_div(high, mn)).diff()


def f03_tpcl_094_rounded_peak_smooth_arc_score_21d_d1(high: pd.Series) -> pd.Series:
    """Rounded-peak: R² of quadratic fit on highs over 21d with negative coefficient."""
    def _f(w):
        if np.isnan(w).any():
            return np.nan
        try:
            x = np.arange(len(w), dtype=float)
            coefs = np.polyfit(x, w, 2)
            if coefs[0] >= 0:
                return 0.0
            yhat = np.polyval(coefs, x)
            ss_res = float(((w - yhat) ** 2).sum())
            ss_tot = float(((w - w.mean()) ** 2).sum())
            if ss_tot == 0:
                return np.nan
            return float(1.0 - ss_res / ss_tot)
        except Exception:
            return np.nan
    return (high.rolling(MDAYS, min_periods=WDAYS).apply(_f, raw=True)).diff()


def f03_tpcl_095_adam_vs_eve_classifier_21d_d1(high: pd.Series) -> pd.Series:
    """Classifier in the range [-1, 1]: -1 = pure Adam (sharp), +1 = pure Eve
    (rounded). Computed as: rounded-score minus sharp-score, normalised."""
    sharp = _safe_div(high, high.rolling(MDAYS, min_periods=WDAYS).mean()) - 1.0
    rounded = high.rolling(MDAYS, min_periods=WDAYS).apply(
        lambda w: float(1.0 - np.var(w - np.poly1d(np.polyfit(np.arange(len(w)), w, 2))(np.arange(len(w)))) / np.var(w)) if not np.isnan(w).any() and np.var(w) > 0 else np.nan,
        raw=True
    )
    diff = rounded - sharp.abs()
    return (diff.clip(-1.0, 1.0)).diff()


def f03_tpcl_096_bowl_of_spoon_sharp_peak_long_handle_252d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bowl-of-the-spoon: a sharp peak in 252d followed by an extended sideways
    "handle" (range-bound for 21d) below the peak. Indicator 0/1."""
    peak_252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    days_since_peak = (high == peak_252).astype(float)
    # bars since peak
    # we want days_since_peak >= 21 AND 21d-range is small
    def _dsp(w):
        idx = np.where(w > 0)[0]
        if idx.size == 0:
            return np.nan
        return float(len(w) - 1 - idx[-1])
    bars_since = days_since_peak.rolling(YDAYS, min_periods=QDAYS).apply(_dsp, raw=True)
    short_rng = (high.rolling(MDAYS, min_periods=WDAYS).max() -
                 high.rolling(MDAYS, min_periods=WDAYS).min())
    typical_rng = (high.rolling(QDAYS, min_periods=MDAYS).max() -
                   high.rolling(QDAYS, min_periods=MDAYS).min())
    sideways = (short_rng < 0.3 * typical_rng).astype(float)
    return (((bars_since >= MDAYS) & (sideways > 0)).astype(float).where(bars_since.notna(), np.nan)).diff()


def f03_tpcl_097_three_peaks_domed_house_lindsay_refinement_252d_d1(high: pd.Series) -> pd.Series:
    """Lindsay's three-peaks-and-a-domed-house refinement: requires 3 ascending
    pivot-highs followed by a rounded structure (positive 2nd-deriv proxy
    NEGATIVE on close after the 3rd peak)."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _f(w):
        mask = ~np.isnan(w)
        if mask.sum() < 3:
            return np.nan
        idxs = np.where(mask)[0]; vals = w[mask]
        sv = np.argsort(vals)[::-1][:3]
        pos = idxs[sv]
        order = np.argsort(pos)
        h_chron = vals[sv][order]
        pos_sorted = pos[order]
        if not (h_chron[0] < h_chron[1] < h_chron[2]):
            return 0.0
        # check after third peak the highs rounded over
        last_seg = w[pos_sorted[-1]:]
        v_last = last_seg[~np.isnan(last_seg)]
        if v_last.size < 5:
            return 0.0
        x = np.arange(v_last.size, dtype=float)
        try:
            a, b, c = np.polyfit(x, v_last, 2)
            return float(1.0 if a < 0 else 0.0)
        except Exception:
            return np.nan
    return (piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)).diff()


def f03_tpcl_098_three_pushes_up_then_fail_wyckoff_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Wyckoff three-pushes-up-then-fail: 3 ascending pivots followed by close
    below the trough between push-2 and push-3."""
    piv_h_m = _pivot_highs_mask(high, k=5)
    out = np.full(len(high), np.nan)
    pv = high.where(piv_h_m > 0, np.nan).values
    l_v = low.values; c_v = close.values
    for i in range(QDAYS, len(high)):
        lo = max(0, i - YDAYS + 1)
        w = pv[lo:i + 1]; wl = l_v[lo:i + 1]
        mask = ~np.isnan(w)
        if mask.sum() < 3:
            continue
        idxs = np.where(mask)[0]; vals = w[mask]
        sv = np.argsort(vals)[::-1][:3]
        pos = idxs[sv]; order = np.argsort(pos)
        h_chron = vals[sv][order]
        pos_sorted = pos[order]
        if not (h_chron[0] < h_chron[1] < h_chron[2]):
            continue
        trough = float(np.nanmin(wl[pos_sorted[1]:pos_sorted[2] + 1]))
        if c_v[i] < trough:
            out[i] = 1.0
        else:
            out[i] = 0.0
    return (pd.Series(out, index=high.index)).diff()


def f03_tpcl_099_two_day_reversal_pattern_at_high_count_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Two-day reversal: day 1 makes new 21d high with strong close near high,
    day 2 closes near low of day 1. Count of such occurrences in 63d."""
    rh21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    new_high = high >= rh21
    strong_close = ((close - low) / (high - low).replace(0, np.nan)) > 0.8
    weak_next = close < low.shift(1)
    event = (new_high.shift(1) & strong_close.shift(1) & weak_next).astype(float)
    return (event.rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f03_tpcl_100_outside_day_reversal_at_high_strength_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Outside-day reversal AT the 252d high: today's high > prior high AND
    today's low < prior low AND close in bottom-25% of today's range AND
    today's high is at/within 1% of 252d-high."""
    rh = high.rolling(YDAYS, min_periods=QDAYS).max()
    outside = (high > high.shift(1)) & (low < low.shift(1))
    weak = ((close - low) / (high - low).replace(0, np.nan)) < 0.25
    at_top = high >= 0.99 * rh
    return ((outside & weak & at_top).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f03_tpcl_101_specialist_buying_climax_pattern_indicator_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Buying climax: new 252d high on extreme volume (>2× 63d avg) with close in
    bottom-40% of bar range — classic specialist's distribution day."""
    rh = high.rolling(YDAYS, min_periods=QDAYS).max()
    avg_v = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    pos = (close - low) / (high - low).replace(0, np.nan)
    return (((high >= rh) & (volume > 2 * avg_v) & (pos < 0.4)).astype(float).where(close.notna(), np.nan)).diff()


def f03_tpcl_102_specialist_upthrust_after_distribution_indicator_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Upthrust after distribution: brief spike above a recent range, then close
    back inside. Range = trailing 21d max/min; spike = today's high > range-max
    AND close <= range-max."""
    rh21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    upthrust = (high > rh21) & (close <= rh21)
    return (upthrust.astype(float).where(rh21.notna(), np.nan)).diff()


def f03_tpcl_103_steidlmayer_minus_development_at_top_252d_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Steidlmayer minus-development: at/near 252d high, range and volume both
    declining (low conviction at top). Indicator 0/1 — both 21d-range slope
    AND 21d-volume slope are negative AND price within 5% of 252d high."""
    rh = high.rolling(YDAYS, min_periods=QDAYS).max()
    rng = high - low
    sr = _rolling_slope(rng, MDAYS)
    sv = _rolling_slope(volume, MDAYS)
    near_top = high >= 0.95 * rh
    return (((sr < 0) & (sv < 0) & near_top).astype(float).where(rh.notna(), np.nan)).diff()


def f03_tpcl_104_steidlmayer_plus_development_failure_252d_d1(high: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    """Steidlmayer plus-development failure: expanding range and rising volume
    BUT price drifting DOWN — failed acceptance at higher value. Indicator."""
    sl_close = _rolling_slope(close, MDAYS)
    sl_vol = _rolling_slope(volume, MDAYS)
    sl_rng = _rolling_slope(high - close, MDAYS)
    return (((sl_close < 0) & (sl_vol > 0) & (sl_rng > 0)).astype(float).where(close.notna(), np.nan)).diff()


def f03_tpcl_105_time_to_pattern_completion_estimate_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Estimate of bars to pattern completion: (close - 252d-low) / (mean 21d
    decline rate). Negative or NaN = pattern already completed."""
    nl = low.rolling(YDAYS, min_periods=QDAYS).min()
    rate = (-close.diff(MDAYS) / MDAYS)
    return (_safe_div(close - nl, rate.where(rate > 0, np.nan))).diff()


def f03_tpcl_106_bars_since_pattern_recognition_252d_d1(high: pd.Series) -> pd.Series:
    """Bars since most recent pivot-high inside 252d (a proxy for "pattern
    started here"). Larger = aged pattern."""
    piv = _pivot_highs_mask(high, k=5)
    def _bsl(w):
        idx = np.where(w > 0)[0]
        if idx.size == 0:
            return np.nan
        return float(len(w) - 1 - idx[-1])
    return (piv.rolling(YDAYS, min_periods=QDAYS).apply(_bsl, raw=True)).diff()


def f03_tpcl_107_pattern_recognition_confidence_composite_252d_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite confidence: average of (mirror-symmetry, downsloping-neckline,
    declining-volume) — universal pattern-quality proxy."""
    def _ms(w):
        if np.isnan(w).any():
            return np.nan
        n = len(w); h = n // 2
        if h < 5:
            return np.nan
        left = w[:h]; right = w[-h:][::-1]
        if left.std() == 0 or right.std() == 0:
            return np.nan
        return float(np.corrcoef(left, right)[0, 1])
    sym = high.rolling(YDAYS, min_periods=QDAYS).apply(_ms, raw=True)
    sl_l = _rolling_slope(low, YDAYS, min_periods=QDAYS)
    sl_v = _rolling_slope(volume, YDAYS, min_periods=QDAYS)
    nl_score = (sl_l < 0).astype(float)
    vol_score = (sl_v < 0).astype(float)
    return ((sym.clip(0, 1) + nl_score + vol_score) / 3.0).diff()


def f03_tpcl_108_pattern_quality_vs_ideal_template_R2_252d_d1(high: pd.Series) -> pd.Series:
    """R² fit of highs to an ideal H&S template (inverse-parabola). Higher = better
    match to ideal pattern."""
    def _r2(w):
        if np.isnan(w).any():
            return np.nan
        try:
            x = np.arange(len(w), dtype=float)
            coefs = np.polyfit(x, w, 4)
            yhat = np.polyval(coefs, x)
            ss_res = float(((w - yhat) ** 2).sum())
            ss_tot = float(((w - w.mean()) ** 2).sum())
            if ss_tot == 0:
                return np.nan
            return float(1.0 - ss_res / ss_tot)
        except Exception:
            return np.nan
    return (high.rolling(YDAYS, min_periods=QDAYS).apply(_r2, raw=True)).diff()


def f03_tpcl_109_pattern_volume_confirmation_strength_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Strength of volume-pattern confirmation: 63d correlation between |daily
    return| and volume — strong correlation = patterns are volume-confirmed."""
    ret = close.pct_change().abs()
    def _c(w_r, w_v):
        m = ~np.isnan(w_r) & ~np.isnan(w_v)
        if m.sum() < 10:
            return np.nan
        r = w_r[m]; v = w_v[m]
        if r.std() == 0 or v.std() == 0:
            return np.nan
        return float(np.corrcoef(r, v)[0, 1])
    out = np.full(len(close), np.nan)
    r_v = ret.values; v_v = volume.values
    for i in range(MDAYS, len(close)):
        lo = max(0, i - QDAYS + 1)
        out[i] = _c(r_v[lo:i + 1], v_v[lo:i + 1])
    return (pd.Series(out, index=close.index)).diff()


def f03_tpcl_110_multi_pattern_co_occurrence_count_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of distinct concurrent patterns detected at this bar: H&S (3-peak,
    mid-highest), Double-top (top-2 within 3%), Triple-top (top-3 within 3%),
    Diamond (range expand then contract), Rising-wedge."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _hs(w):
        mask = ~np.isnan(w)
        if mask.sum() < 3:
            return 0.0
        idxs = np.where(mask)[0]; vals = w[mask]
        sv = np.argsort(vals)[::-1][:3]
        pos = idxs[sv]; order = np.argsort(pos)
        h = vals[sv][order]
        return float(1.0 if h[1] > h[0] and h[1] > h[2] else 0.0)
    def _dt(w):
        mask = ~np.isnan(w)
        if mask.sum() < 2:
            return 0.0
        v = w[mask]
        top2 = np.sort(v)[::-1][:2]
        if top2[0] <= 0:
            return 0.0
        return float(1.0 if abs(top2[0] - top2[1]) / top2[0] <= 0.03 else 0.0)
    def _tt(w):
        mask = ~np.isnan(w)
        if mask.sum() < 3:
            return 0.0
        v = w[mask]
        top3 = np.sort(v)[::-1][:3]
        if top3[0] <= 0:
            return 0.0
        return float(1.0 if (top3[0] - top3[-1]) / top3[0] <= 0.03 else 0.0)
    hs = piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_hs, raw=True)
    dt = piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_dt, raw=True)
    tt = piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_tt, raw=True)
    rng = high - low
    def _dm(w):
        if np.isnan(w).any():
            return 0.0
        n = len(w); h = n // 2
        if h < 5:
            return 0.0
        s1 = np.polyfit(np.arange(h), w[:h], 1)[0]
        s2 = np.polyfit(np.arange(n - h), w[h:], 1)[0]
        return float(1.0 if (s1 > 0 and s2 < 0) else 0.0)
    dm = rng.rolling(YDAYS, min_periods=QDAYS).apply(_dm, raw=True)
    sl_h = _rolling_slope(high, YDAYS, min_periods=QDAYS)
    sl_l = _rolling_slope(low, YDAYS, min_periods=QDAYS)
    rw = ((sl_h > 0) & (sl_l > sl_h)).astype(float)
    df = pd.concat([(hs).rename("hs"), (dt).rename("dt"), (tt).rename("tt"), (dm).rename("dm"), (rw).rename("rw")], axis=1)
    return (df.sum(axis=1, min_count=1)).diff()


def f03_tpcl_110_multi_pattern_co_occurrence_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of distinct concurrent patterns detected at this bar: H&S (3-peak,
    mid-highest), Double-top (top-2 within 3%), Triple-top (top-3 within 3%),
    Diamond (range expand then contract), Rising-wedge."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _hs(w):
        mask = ~np.isnan(w)
        if mask.sum() < 3:
            return 0.0
        idxs = np.where(mask)[0]; vals = w[mask]
        sv = np.argsort(vals)[::-1][:3]
        pos = idxs[sv]; order = np.argsort(pos)
        h = vals[sv][order]
        return float(1.0 if h[1] > h[0] and h[1] > h[2] else 0.0)
    def _dt(w):
        mask = ~np.isnan(w)
        if mask.sum() < 2:
            return 0.0
        v = w[mask]
        top2 = np.sort(v)[::-1][:2]
        if top2[0] <= 0:
            return 0.0
        return float(1.0 if abs(top2[0] - top2[1]) / top2[0] <= 0.03 else 0.0)
    def _tt(w):
        mask = ~np.isnan(w)
        if mask.sum() < 3:
            return 0.0
        v = w[mask]
        top3 = np.sort(v)[::-1][:3]
        if top3[0] <= 0:
            return 0.0
        return float(1.0 if (top3[0] - top3[-1]) / top3[0] <= 0.03 else 0.0)
    hs = piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_hs, raw=True)
    dt = piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_dt, raw=True)
    tt = piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_tt, raw=True)
    rng = high - low
    def _dm(w):
        if np.isnan(w).any():
            return 0.0
        n = len(w); h = n // 2
        if h < 5:
            return 0.0
        s1 = np.polyfit(np.arange(h), w[:h], 1)[0]
        s2 = np.polyfit(np.arange(n - h), w[h:], 1)[0]
        return float(1.0 if (s1 > 0 and s2 < 0) else 0.0)
    dm = rng.rolling(YDAYS, min_periods=QDAYS).apply(_dm, raw=True)
    sl_h = _rolling_slope(high, YDAYS, min_periods=QDAYS)
    sl_l = _rolling_slope(low, YDAYS, min_periods=QDAYS)
    rw = ((sl_h > 0) & (sl_l > sl_h)).astype(float)
    df = pd.concat([(hs).rename("hs"), (dt).rename("dt"), (tt).rename("tt"), (dm).rename("dm"), (rw).rename("rw")], axis=1)
    return df.sum(axis=1, min_count=1)


def f03_tpcl_111_pattern_within_pattern_nested_indicator_d1(high: pd.Series) -> pd.Series:
    """Nested pattern: H&S detected at 63d AND H&S detected at 252d — nested
    multi-scale topping structure."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _hs(w):
        mask = ~np.isnan(w)
        if mask.sum() < 3:
            return 0.0
        idxs = np.where(mask)[0]; vals = w[mask]
        sv = np.argsort(vals)[::-1][:3]
        pos = idxs[sv]; order = np.argsort(pos)
        h = vals[sv][order]
        return float(1.0 if h[1] > h[0] and h[1] > h[2] else 0.0)
    a = piv_h.rolling(QDAYS, min_periods=MDAYS).apply(_hs, raw=True)
    b = piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_hs, raw=True)
    return (((a > 0) & (b > 0)).astype(float).where(a.notna() & b.notna(), np.nan)).diff()


def f03_tpcl_112_universal_pattern_symmetry_index_252d_d1(close: pd.Series) -> pd.Series:
    """Universal pattern symmetry index: 1 - |mean(left-half) - mean(right-half)|
    / std(window) on close over 252d. Higher = more symmetric overall pattern."""
    def _f(w):
        if np.isnan(w).any():
            return np.nan
        n = len(w); h = n // 2
        if h < 5 or w.std() == 0:
            return np.nan
        return float(1.0 - abs(w[:h].mean() - w[h:].mean()) / w.std())
    return (close.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)).diff()


def f03_tpcl_113_universal_pattern_asymmetry_penalty_252d_d1(close: pd.Series) -> pd.Series:
    """Asymmetry penalty: |mean(left-half) - mean(right-half)| / mean(window).
    Higher = more asymmetric pattern."""
    def _f(w):
        if np.isnan(w).any():
            return np.nan
        n = len(w); h = n // 2
        if h < 5 or w.mean() == 0:
            return np.nan
        return float(abs(w[:h].mean() - w[h:].mean()) / abs(w.mean()))
    return (close.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)).diff()


def f03_tpcl_114_pattern_duration_relative_typical_252d_d1(high: pd.Series) -> pd.Series:
    """Bars from first pivot in the window to most recent pivot, divided by 90
    (Bulkowski-typical). Smaller = compressed pattern."""
    piv = _pivot_highs_mask(high, k=5)
    def _f(w):
        idx = np.where(w > 0)[0]
        if idx.size < 2:
            return np.nan
        return float(idx[-1] - idx[0]) / 90.0
    return (piv.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)).diff()


def f03_tpcl_115_multi_scale_pattern_consensus_63_and_252_indicator_d1(high: pd.Series) -> pd.Series:
    """Same pattern (rising-wedge) detected at BOTH 63d and 252d windows.
    Indicator 0/1."""
    sl_h_63 = _rolling_slope(high, QDAYS, min_periods=MDAYS)
    sl_h_252 = _rolling_slope(high, YDAYS, min_periods=QDAYS)
    return (((sl_h_63 > 0) & (sl_h_252 > 0)).astype(float).where(sl_h_252.notna(), np.nan)).diff()


def f03_tpcl_116_pattern_detection_robustness_tolerance_252d_d1(high: pd.Series) -> pd.Series:
    """Robustness: would double-top still be detected with peak-equality tolerance
    relaxed from 2% to 10%? Score = 1 if yes, 0 if no."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _f(w):
        mask = ~np.isnan(w)
        if mask.sum() < 2:
            return np.nan
        v = w[mask]
        top2 = np.sort(v)[::-1][:2]
        if top2[0] <= 0:
            return np.nan
        return float(1.0 if abs(top2[0] - top2[1]) / top2[0] <= 0.10 else 0.0)
    return (piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)).diff()


def f03_tpcl_117_hs_neckline_not_broken_within_21d_after_right_shoulder_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """H&S without breakdown: pattern recognised but close has NOT broken neckline
    within the last 21d. Pattern-failure (so far) indicator."""
    nl = low.rolling(YDAYS, min_periods=QDAYS).min()
    broken_recently = (close.rolling(MDAYS, min_periods=WDAYS).min() < nl.shift(MDAYS)).astype(float)
    has_hs = _proxy_hs_indicator(high)
    return (((has_hs > 0) & (broken_recently == 0)).astype(float).where(has_hs.notna(), np.nan)).diff()


def _proxy_hs_indicator(high):
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _hs(w):
        mask = ~np.isnan(w)
        if mask.sum() < 3:
            return 0.0
        idxs = np.where(mask)[0]; vals = w[mask]
        sv = np.argsort(vals)[::-1][:3]
        pos = idxs[sv]; order = np.argsort(pos)
        h = vals[sv][order]
        return float(1.0 if h[1] > h[0] and h[1] > h[2] else 0.0)
    return piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_hs, raw=True)


def f03_tpcl_118_double_top_not_below_midpoint_low_failure_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Double-top failure: 2 peaks established but close hasn't broken the trough
    between them (no neckline break)."""
    piv_h_mask = _pivot_highs_mask(high, k=5)
    piv_h = high.where(piv_h_mask > 0, np.nan)
    out = np.full(len(high), np.nan)
    h_v = piv_h.values; l_v = low.values; c_v = close.values
    for i in range(QDAYS, len(high)):
        lo = max(0, i - YDAYS + 1)
        w = h_v[lo:i + 1]; wl = l_v[lo:i + 1]
        mask = ~np.isnan(w)
        if mask.sum() < 2:
            continue
        idxs = np.where(mask)[0]; vals = w[mask]
        sv = np.argsort(vals)[::-1][:2]
        pos = np.sort(idxs[sv])
        if pos[1] <= pos[0]:
            continue
        trough = float(np.nanmin(wl[pos[0]:pos[1] + 1]))
        post_min = float(np.nanmin(wl[pos[1]:])) if pos[1] < len(wl) else np.nan
        out[i] = float(1.0 if post_min >= trough else 0.0)
    return (pd.Series(out, index=high.index)).diff()


def f03_tpcl_119_triple_top_continuation_to_new_high_failure_252d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Triple-top failure: 3 peaks within 3% AND close has subsequently exceeded
    the highest peak (continuation, not reversal)."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    out = np.full(len(high), np.nan)
    h_v = piv_h.values; c_v = close.values
    for i in range(QDAYS, len(high)):
        lo = max(0, i - YDAYS + 1)
        w = h_v[lo:i + 1]
        mask = ~np.isnan(w)
        if mask.sum() < 3:
            continue
        v = w[mask]
        top3 = np.sort(v)[::-1][:3]
        if top3[0] <= 0:
            continue
        if (top3[0] - top3[-1]) / top3[0] > 0.03:
            continue
        out[i] = float(1.0 if c_v[i] > top3[0] else 0.0)
    return (pd.Series(out, index=high.index)).diff()


def f03_tpcl_120_wedge_broke_opposite_direction_failure_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Wedge failure: rising wedge that broke UP instead of expected DOWN."""
    sl_h = _rolling_slope(high, YDAYS, min_periods=QDAYS)
    sl_l = _rolling_slope(low, YDAYS, min_periods=QDAYS)
    rh = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_rising_wedge = (sl_h > 0) & (sl_l > sl_h)
    return (((close > rh) & is_rising_wedge).astype(float).where(close.notna(), np.nan)).diff()


def f03_tpcl_121_barr_lead_in_line_held_failure_252d_d1(close: pd.Series) -> pd.Series:
    """BARR failure: bump phase occurred but lead-in trendline never broke."""
    def _f(w):
        n = len(w)
        if n < 30 or np.isnan(w).any():
            return np.nan
        h = n // 2
        s_lead = float(np.polyfit(np.arange(h, dtype=float), w[:h], 1)[0])
        s_bump = float(np.polyfit(np.arange(n - h, dtype=float), w[h:], 1)[0])
        if s_lead <= 0 or s_bump < 2 * s_lead:
            return np.nan
        # ratio confirms BARR; check if lead-in line was broken in second half
        sl, ic = np.polyfit(np.arange(h, dtype=float), w[:h], 1)
        for j in range(h, n):
            line_val = sl * j + ic
            if w[j] < line_val:
                return 0.0
        return 1.0
    return (close.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)).diff()


def f03_tpcl_122_pattern_failure_event_count_252d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of pattern-failure events in 252d: new-21d-high followed by close
    back inside prior 21d range within 5 bars."""
    rh21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    rl21 = high.rolling(MDAYS, min_periods=WDAYS).min().shift(1)
    new_high = high > rh21
    came_back = pd.Series(False, index=close.index)
    for k in range(1, WDAYS + 1):
        came_back = came_back | (close.shift(k).fillna(close.iloc[-1] if len(close) else 0) < rh21)
    # PIT-safe alt: shift backward — instead, check forward via past-only:
    # at bar t, look back 5 bars: did the bar (t-5) print a new high and is current close < that high?
    new_high_past = (high.shift(WDAYS) > rh21.shift(WDAYS))
    came_back_past = (close < rh21.shift(WDAYS))
    event = (new_high_past & came_back_past).astype(float)
    return (event.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f03_tpcl_123_average_pattern_failure_rate_504d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Average pattern failure rate over 504d: count of new-21d-highs that
    failed (close back below) divided by total new-21d-high count."""
    rh21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    new_high = (high > rh21).astype(float)
    failed = ((high.shift(WDAYS) > rh21.shift(WDAYS)) & (close < rh21.shift(WDAYS))).astype(float)
    cnt_nh = new_high.rolling(DDAYS_2Y, min_periods=YDAYS).sum()
    cnt_fail = failed.rolling(DDAYS_2Y, min_periods=YDAYS).sum()
    return (_safe_div(cnt_fail, cnt_nh)).diff()


def f03_tpcl_124_failed_pattern_then_extension_count_252d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count: failed pattern (new-high then back-inside) followed by continued
    extension to new highs within 21d. Bullish-failure-pattern count."""
    rh21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    failed_in_past = ((high.shift(MDAYS) > rh21.shift(MDAYS)) & (close.shift(MDAYS - WDAYS) < rh21.shift(MDAYS))).astype(float)
    extension_now = (high > rh21).astype(float)
    return ((failed_in_past * extension_now).rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f03_tpcl_124_failed_pattern_then_extension_count_252d(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count: failed pattern (new-high then back-inside) followed by continued
    extension to new highs within 21d. Bullish-failure-pattern count."""
    rh21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    failed_in_past = ((high.shift(MDAYS) > rh21.shift(MDAYS)) & (close.shift(MDAYS - WDAYS) < rh21.shift(MDAYS))).astype(float)
    extension_now = (high > rh21).astype(float)
    return (failed_in_past * extension_now).rolling(YDAYS, min_periods=QDAYS).sum()


def f03_tpcl_125_failed_pattern_then_pullback_count_252d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of: failed pattern followed by pullback (close 21d later is below
    failure-event price)."""
    rh21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    fail_event = ((high.shift(MDAYS) > rh21.shift(MDAYS)) & (close.shift(MDAYS - WDAYS) < rh21.shift(MDAYS))).astype(float)
    pull = (close < close.shift(MDAYS)).astype(float)
    return ((fail_event * pull).rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f03_tpcl_125_failed_pattern_then_pullback_count_252d(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of: failed pattern followed by pullback (close 21d later is below
    failure-event price)."""
    rh21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    fail_event = ((high.shift(MDAYS) > rh21.shift(MDAYS)) & (close.shift(MDAYS - WDAYS) < rh21.shift(MDAYS))).astype(float)
    pull = (close < close.shift(MDAYS)).astype(float)
    return (fail_event * pull).rolling(YDAYS, min_periods=QDAYS).sum()


def f03_tpcl_126_pattern_completion_rate_at_stock_vs_historical_504d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Completion rate at this stock: fraction of detected patterns (new-252d-highs)
    that completed (close fell >5% within 21d) over 504d."""
    rh = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_new = (high >= rh).astype(float)
    drop = (close.shift(MDAYS) / close - 1.0)
    # PIT: invert — completed_past = a bar 21d ago hit new high AND close today is >5% below close 21d ago
    is_new_past = (high.shift(MDAYS) >= rh.shift(MDAYS)).astype(float)
    drop_past = (close / close.shift(MDAYS) - 1.0)
    completed = (is_new_past * (drop_past < -0.05).astype(float))
    cnt_new = is_new_past.rolling(DDAYS_2Y, min_periods=YDAYS).sum()
    cnt_comp = completed.rolling(DDAYS_2Y, min_periods=YDAYS).sum()
    return (_safe_div(cnt_comp, cnt_new)).diff()


def f03_tpcl_127_hs_measured_move_target_distance_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """H&S measured-move target: project (head - neckline) below neckline. Output
    is distance of close from target, normalised by close. Negative = target hit."""
    head = high.rolling(YDAYS, min_periods=QDAYS).max()
    neck = low.rolling(YDAYS, min_periods=QDAYS).min()
    target = neck - (head - neck)
    return (_safe_div(close - target, close)).diff()


def f03_tpcl_128_double_top_measured_move_target_distance_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Double-top measured-move: project (peak - trough) below trough.
    Distance of close from this projected target / close."""
    rh = high.rolling(YDAYS, min_periods=QDAYS).max()
    rl = low.rolling(YDAYS, min_periods=QDAYS).min()
    target = rl - (rh - rl)
    return (_safe_div(close - target, close)).diff()


def f03_tpcl_129_triple_top_measured_move_target_distance_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Triple-top measured-move target: median-peak minus (max-peak - lowest-trough)
    projected below. Distance from close, normalised."""
    piv_h_mask = _pivot_highs_mask(high, k=5)
    out = np.full(len(high), np.nan)
    h_v = high.where(piv_h_mask > 0, np.nan).values
    l_v = low.values; c_v = close.values
    for i in range(QDAYS, len(high)):
        lo = max(0, i - YDAYS + 1)
        w = h_v[lo:i + 1]; wl = l_v[lo:i + 1]
        mask = ~np.isnan(w)
        if mask.sum() < 3:
            continue
        v = w[mask]
        top3 = np.sort(v)[::-1][:3]
        med_peak = float(np.median(top3))
        trough = float(np.nanmin(wl))
        target = trough - (med_peak - trough)
        if c_v[i] == 0:
            continue
        out[i] = (c_v[i] - target) / c_v[i]
    return (pd.Series(out, index=high.index)).diff()


def f03_tpcl_130_wedge_measured_move_channel_height_projection_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Wedge measured-move: project channel-height below lower bound. Distance
    from close to projected target, normalised by close."""
    rh = high.rolling(YDAYS, min_periods=QDAYS).max()
    rl = low.rolling(YDAYS, min_periods=QDAYS).min()
    height = rh - rl
    target = rl - height
    return (_safe_div(close - target, close)).diff()


def f03_tpcl_131_diamond_measured_move_target_distance_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Diamond pattern measured-move: tallest peak minus shortest trough projected
    below shortest trough."""
    rh = high.rolling(YDAYS, min_periods=QDAYS).max()
    rl = low.rolling(YDAYS, min_periods=QDAYS).min()
    target = rl - (rh - rl) * 0.7
    return (_safe_div(close - target, close)).diff()


def f03_tpcl_132_bars_to_target_estimate_252d_d1(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Estimated bars to projected target: distance to target divided by mean 21d
    abs return."""
    rh = high.rolling(YDAYS, min_periods=QDAYS).max()
    rl = low.rolling(YDAYS, min_periods=QDAYS).min()
    target = rl - (rh - rl)
    dist = close - target
    speed = close.diff().abs().rolling(MDAYS, min_periods=WDAYS).mean()
    return (_safe_div(dist, speed)).diff()


def f03_tpcl_133_distance_from_current_close_to_target_atr_norm_252d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalised distance from current close to measured-move target."""
    rh = high.rolling(YDAYS, min_periods=QDAYS).max()
    rl = low.rolling(YDAYS, min_periods=QDAYS).min()
    target = rl - (rh - rl)
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - target, atr)).diff()


def f03_tpcl_134_measured_move_overshoot_undershoot_history_504d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Historical overshoot/undershoot ratio: at past 252d highs, how far did
    the subsequent low go relative to measured-move target? Average over 504d."""
    rh_past = high.shift(YDAYS).rolling(YDAYS, min_periods=QDAYS).max()
    rl_past = low.shift(YDAYS).rolling(YDAYS, min_periods=QDAYS).min()
    target_past = rl_past - (rh_past - rl_past)
    actual_low_recent = low.rolling(YDAYS, min_periods=QDAYS).min()
    ratio = _safe_div(rh_past - actual_low_recent, rh_past - target_past)
    return (ratio.rolling(DDAYS_2Y, min_periods=YDAYS).mean()).diff()


def f03_tpcl_135_multi_pattern_co_occurrence_aggregate_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Aggregate score: 1 + sum of indicators (HS, DT, TT, Diamond, Wedge) all
    detected at the same bar — multi-pattern density."""
    return (f03_tpcl_110_multi_pattern_co_occurrence_count_252d(high, low, close)).diff()


def f03_tpcl_136_pattern_quality_consensus_high_R2_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Consensus on pattern quality: average R² of quadratic fits on highs AND lows
    over 252d. Higher = both bands well-defined."""
    def _r2(w):
        if np.isnan(w).any():
            return np.nan
        try:
            x = np.arange(len(w), dtype=float)
            coefs = np.polyfit(x, w, 2)
            yhat = np.polyval(coefs, x)
            ss_res = float(((w - yhat) ** 2).sum())
            ss_tot = float(((w - w.mean()) ** 2).sum())
            if ss_tot == 0:
                return np.nan
            return float(1.0 - ss_res / ss_tot)
        except Exception:
            return np.nan
    rh = high.rolling(YDAYS, min_periods=QDAYS).apply(_r2, raw=True)
    rl = low.rolling(YDAYS, min_periods=QDAYS).apply(_r2, raw=True)
    return ((rh + rl) / 2.0).diff()


def f03_tpcl_137_pattern_plus_measured_move_alignment_composite_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: pattern detected (any of HS/DT/TT) AND realised drop already
    exceeds 50% of measured-move target."""
    count = f03_tpcl_110_multi_pattern_co_occurrence_count_252d(high, low, close)
    rh = high.rolling(YDAYS, min_periods=QDAYS).max()
    rl = low.rolling(YDAYS, min_periods=QDAYS).min()
    target_drop = rh - rl
    realised = rh - close
    progress = _safe_div(realised, target_drop)
    return ((count > 0).astype(float) * progress.clip(lower=0.0, upper=2.0)).diff()


def f03_tpcl_138_pattern_plus_volume_confirmation_composite_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: pattern detected AND volume-pattern correlation positive in 63d."""
    count = f03_tpcl_110_multi_pattern_co_occurrence_count_252d(high, low, close)
    ret = close.pct_change().abs()
    out = np.full(len(close), np.nan)
    r_v = ret.values; v_v = volume.values
    for i in range(MDAYS, len(close)):
        lo = max(0, i - QDAYS + 1)
        r = r_v[lo:i + 1]; v = v_v[lo:i + 1]
        m = ~np.isnan(r) & ~np.isnan(v)
        if m.sum() < 10:
            continue
        rr = r[m]; vv = v[m]
        if rr.std() == 0 or vv.std() == 0:
            continue
        out[i] = float(np.corrcoef(rr, vv)[0, 1])
    corr = pd.Series(out, index=close.index)
    return ((count > 0).astype(float) * corr.clip(lower=0.0)).diff()


def f03_tpcl_139_pattern_plus_neckline_break_composite_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pattern detected AND close has just broken below 252d-min-low (neckline)
    in last 5 bars."""
    count = f03_tpcl_110_multi_pattern_co_occurrence_count_252d(high, low, close)
    nl = low.rolling(YDAYS, min_periods=QDAYS).min()
    broke = (close.rolling(WDAYS, min_periods=2).min() < nl.shift(WDAYS)).astype(float)
    return ((count > 0).astype(float) * broke).diff()


def f03_tpcl_140_pattern_plus_retest_failure_composite_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pattern detected AND retest of neckline failed: after breaking neckline,
    price bounced back to neckline but couldn't hold."""
    count = f03_tpcl_110_multi_pattern_co_occurrence_count_252d(high, low, close)
    nl = low.rolling(YDAYS, min_periods=QDAYS).min()
    bounce = (high.rolling(MDAYS, min_periods=WDAYS).max() >= nl).astype(float)
    fail = (close < nl).astype(float)
    return ((count > 0).astype(float) * bounce * fail).diff()


def f03_tpcl_141_multi_scale_pattern_consensus_composite_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Same pattern (rising-channel) detected at 63d AND 252d AND 504d windows
    simultaneously — strong multi-scale consensus."""
    sl_63 = _rolling_slope(close, QDAYS, min_periods=MDAYS)
    sl_252 = _rolling_slope(close, YDAYS, min_periods=QDAYS)
    sl_504 = _rolling_slope(close, DDAYS_2Y, min_periods=YDAYS)
    return (((sl_63 > 0) & (sl_252 > 0) & (sl_504 > 0)).astype(float).where(sl_504.notna(), np.nan)).diff()


def f03_tpcl_142_pattern_failure_then_extension_warning_252d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Warning composite: count of failed-then-extension events in 252d, scaled
    by 252d range (higher = pattern-failure-rich regime)."""
    return (f03_tpcl_124_failed_pattern_then_extension_count_252d(high, close)).diff()


def f03_tpcl_143_pattern_detection_density_per_252d_d1(high: pd.Series) -> pd.Series:
    """Density of pattern detection events: pivot-high count in trailing 252d
    divided by 252 (typical Bulkowski density)."""
    piv = _pivot_highs_mask(high, k=5)
    cnt = piv.rolling(YDAYS, min_periods=QDAYS).sum()
    return (cnt / float(YDAYS)).diff()


def f03_tpcl_144_pattern_symmetry_aggregate_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Aggregate symmetry across H&S amplitude-symm, diamond symm, and universal
    symm — average."""
    def _ms(w):
        if np.isnan(w).any():
            return np.nan
        n = len(w); h = n // 2
        if h < 5:
            return np.nan
        left = w[:h]; right = w[-h:][::-1]
        if left.std() == 0 or right.std() == 0:
            return np.nan
        return float(np.corrcoef(left, right)[0, 1])
    s_close = close.rolling(YDAYS, min_periods=QDAYS).apply(_ms, raw=True)
    s_high = high.rolling(YDAYS, min_periods=QDAYS).apply(_ms, raw=True)
    s_low = low.rolling(YDAYS, min_periods=QDAYS).apply(_ms, raw=True)
    return ((s_close + s_high + s_low) / 3.0).diff()


def f03_tpcl_145_pattern_projection_alignment_composite_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Projection alignment: do H&S target, DT target, and wedge target all sit
    within 5% of each other? Indicator that multiple pattern projections cluster."""
    rh = high.rolling(YDAYS, min_periods=QDAYS).max()
    rl = low.rolling(YDAYS, min_periods=QDAYS).min()
    t_hs = rl - (rh - rl)
    t_dt = rl - (rh - rl) * 0.9
    t_w = rl - (rh - rl) * 1.1
    span = pd.concat([(t_hs).rename("hs"), (t_dt).rename("dt"), (t_w).rename("w")], axis=1)
    rng = span.max(axis=1) - span.min(axis=1)
    return ((rng / close.replace(0, np.nan) < 0.05).astype(float).where(close.notna(), np.nan)).diff()


def f03_tpcl_146_pattern_aged_still_active_composite_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pattern detected AND most recent pivot-high was >21 bars ago — aged but
    still-active pattern."""
    count = f03_tpcl_110_multi_pattern_co_occurrence_count_252d(high, low, close)
    piv = _pivot_highs_mask(high, k=5)
    def _bsl(w):
        idx = np.where(w > 0)[0]
        if idx.size == 0:
            return np.nan
        return float(len(w) - 1 - idx[-1])
    bsl = piv.rolling(YDAYS, min_periods=QDAYS).apply(_bsl, raw=True)
    return ((count > 0).astype(float) * (bsl >= MDAYS).astype(float)).diff()


def f03_tpcl_147_pattern_newly_completed_composite_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pattern completed within last 5 bars: detection-count went from 0 to >0 in
    last 5 bars OR close broke below 63d-low in last 5 bars."""
    count = f03_tpcl_110_multi_pattern_co_occurrence_count_252d(high, low, close)
    new = ((count > 0) & (count.shift(WDAYS).fillna(0) == 0)).astype(float)
    nl = low.rolling(QDAYS, min_periods=MDAYS).min()
    broke = (close.rolling(WDAYS, min_periods=2).min() < nl.shift(WDAYS)).astype(float)
    return (((new > 0) | (broke > 0)).astype(float).where(close.notna(), np.nan)).diff()


def f03_tpcl_148_pattern_completion_imminent_composite_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pattern detected AND close within 2% of neckline (about to break)."""
    count = f03_tpcl_110_multi_pattern_co_occurrence_count_252d(high, low, close)
    nl = low.rolling(YDAYS, min_periods=QDAYS).min()
    near = ((close - nl).abs() / close.replace(0, np.nan) < 0.02).astype(float)
    return ((count > 0).astype(float) * near).diff()


def f03_tpcl_149_pattern_failure_then_pullback_composite_252d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: high pattern-failure count AND recent pullback (close < 21d-back close)."""
    fail_count = f03_tpcl_125_failed_pattern_then_pullback_count_252d(high, close)
    pull = (close < close.shift(MDAYS)).astype(float)
    return (fail_count * pull).diff()


def f03_tpcl_150_terminal_pattern_aggregate_sum_of_reversal_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Terminal pattern aggregate: sum of (HS-confidence + DT-completion +
    TT-completion + diamond-detected + rising-wedge-detected + BARR-completed)."""
    piv_h = high.where(_pivot_highs_mask(high, k=5) > 0, np.nan)
    def _hs(w):
        mask = ~np.isnan(w)
        if mask.sum() < 3:
            return 0.0
        idxs = np.where(mask)[0]; vals = w[mask]
        sv = np.argsort(vals)[::-1][:3]
        pos = idxs[sv]; order = np.argsort(pos)
        h = vals[sv][order]
        return float(1.0 if h[1] > h[0] and h[1] > h[2] else 0.0)
    hs_s = piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_hs, raw=True)
    def _dt(w):
        mask = ~np.isnan(w)
        if mask.sum() < 2:
            return 0.0
        v = w[mask]
        top2 = np.sort(v)[::-1][:2]
        if top2[0] <= 0:
            return 0.0
        return float(1.0 if abs(top2[0] - top2[1]) / top2[0] <= 0.03 else 0.0)
    dt_s = piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_dt, raw=True)
    def _tt(w):
        mask = ~np.isnan(w)
        if mask.sum() < 3:
            return 0.0
        v = w[mask]
        top3 = np.sort(v)[::-1][:3]
        if top3[0] <= 0:
            return 0.0
        return float(1.0 if (top3[0] - top3[-1]) / top3[0] <= 0.03 else 0.0)
    tt_s = piv_h.rolling(YDAYS, min_periods=QDAYS).apply(_tt, raw=True)
    rng = high - low
    def _dm(w):
        if np.isnan(w).any():
            return 0.0
        n = len(w); h = n // 2
        if h < 5:
            return 0.0
        s1 = np.polyfit(np.arange(h), w[:h], 1)[0]
        s2 = np.polyfit(np.arange(n - h), w[h:], 1)[0]
        return float(1.0 if (s1 > 0 and s2 < 0) else 0.0)
    dm_s = rng.rolling(YDAYS, min_periods=QDAYS).apply(_dm, raw=True)
    sl_h = _rolling_slope(high, YDAYS, min_periods=QDAYS)
    sl_l = _rolling_slope(low, YDAYS, min_periods=QDAYS)
    rw_s = ((sl_h > 0) & (sl_l > sl_h)).astype(float)
    barr_s = (close < close.shift(YDAYS - 1)).astype(float)
    df = pd.concat([(hs_s).rename("hs"), (dt_s).rename("dt"), (tt_s).rename("tt"),
                    (dm_s).rename("dm"), (rw_s).rename("rw"), (barr_s).rename("br")], axis=1)
    return (df.sum(axis=1, min_count=1)).diff()


TOPPING_PATTERN_CLASSICAL_D1_REGISTRY_076_150 = {
    "f03_tpcl_076_diamond_top_declining_volume_during_contraction_252d_d1": {"inputs": ["high", "low", "volume"], "func": f03_tpcl_076_diamond_top_declining_volume_during_contraction_252d_d1},
    "f03_tpcl_077_diamond_top_breakout_direction_indicator_252d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_077_diamond_top_breakout_direction_indicator_252d_d1},
    "f03_tpcl_078_diamond_top_breakdown_magnitude_252d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_078_diamond_top_breakdown_magnitude_252d_d1},
    "f03_tpcl_079_diamond_top_vs_broadening_differentiator_252d_d1": {"inputs": ["high", "low"], "func": f03_tpcl_079_diamond_top_vs_broadening_differentiator_252d_d1},
    "f03_tpcl_080_diamond_top_quality_R2_fit_252d_d1": {"inputs": ["high", "low"], "func": f03_tpcl_080_diamond_top_quality_R2_fit_252d_d1},
    "f03_tpcl_081_barr_lead_in_slope_252d_d1": {"inputs": ["close"], "func": f03_tpcl_081_barr_lead_in_slope_252d_d1},
    "f03_tpcl_082_barr_bump_slope_252d_d1": {"inputs": ["close"], "func": f03_tpcl_082_barr_bump_slope_252d_d1},
    "f03_tpcl_083_barr_bump_to_lead_in_slope_ratio_252d_d1": {"inputs": ["close"], "func": f03_tpcl_083_barr_bump_to_lead_in_slope_ratio_252d_d1},
    "f03_tpcl_084_barr_target_estimate_252d_d1": {"inputs": ["close", "low"], "func": f03_tpcl_084_barr_target_estimate_252d_d1},
    "f03_tpcl_085_barr_completion_event_indicator_252d_d1": {"inputs": ["close"], "func": f03_tpcl_085_barr_completion_event_indicator_252d_d1},
    "f03_tpcl_086_barr_bump_phase_volume_profile_252d_d1": {"inputs": ["close", "volume"], "func": f03_tpcl_086_barr_bump_phase_volume_profile_252d_d1},
    "f03_tpcl_087_barr_lead_in_line_break_event_indicator_252d_d1": {"inputs": ["close"], "func": f03_tpcl_087_barr_lead_in_line_break_event_indicator_252d_d1},
    "f03_tpcl_088_barr_breakdown_follow_through_magnitude_252d_d1": {"inputs": ["close"], "func": f03_tpcl_088_barr_breakdown_follow_through_magnitude_252d_d1},
    "f03_tpcl_089_adam_sharp_then_eve_round_double_top_63d_d1": {"inputs": ["high"], "func": f03_tpcl_089_adam_sharp_then_eve_round_double_top_63d_d1},
    "f03_tpcl_090_eve_round_then_adam_sharp_double_top_63d_d1": {"inputs": ["high"], "func": f03_tpcl_090_eve_round_then_adam_sharp_double_top_63d_d1},
    "f03_tpcl_091_eve_eve_double_top_both_rounded_63d_d1": {"inputs": ["high"], "func": f03_tpcl_091_eve_eve_double_top_both_rounded_63d_d1},
    "f03_tpcl_092_adam_adam_double_top_both_sharp_63d_d1": {"inputs": ["high"], "func": f03_tpcl_092_adam_adam_double_top_both_sharp_63d_d1},
    "f03_tpcl_093_sharp_peak_single_bar_height_vs_neighbors_21d_d1": {"inputs": ["high"], "func": f03_tpcl_093_sharp_peak_single_bar_height_vs_neighbors_21d_d1},
    "f03_tpcl_094_rounded_peak_smooth_arc_score_21d_d1": {"inputs": ["high"], "func": f03_tpcl_094_rounded_peak_smooth_arc_score_21d_d1},
    "f03_tpcl_095_adam_vs_eve_classifier_21d_d1": {"inputs": ["high"], "func": f03_tpcl_095_adam_vs_eve_classifier_21d_d1},
    "f03_tpcl_096_bowl_of_spoon_sharp_peak_long_handle_252d_d1": {"inputs": ["high", "close"], "func": f03_tpcl_096_bowl_of_spoon_sharp_peak_long_handle_252d_d1},
    "f03_tpcl_097_three_peaks_domed_house_lindsay_refinement_252d_d1": {"inputs": ["high"], "func": f03_tpcl_097_three_peaks_domed_house_lindsay_refinement_252d_d1},
    "f03_tpcl_098_three_pushes_up_then_fail_wyckoff_252d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_098_three_pushes_up_then_fail_wyckoff_252d_d1},
    "f03_tpcl_099_two_day_reversal_pattern_at_high_count_63d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_099_two_day_reversal_pattern_at_high_count_63d_d1},
    "f03_tpcl_100_outside_day_reversal_at_high_strength_63d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_100_outside_day_reversal_at_high_strength_63d_d1},
    "f03_tpcl_101_specialist_buying_climax_pattern_indicator_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f03_tpcl_101_specialist_buying_climax_pattern_indicator_252d_d1},
    "f03_tpcl_102_specialist_upthrust_after_distribution_indicator_252d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_102_specialist_upthrust_after_distribution_indicator_252d_d1},
    "f03_tpcl_103_steidlmayer_minus_development_at_top_252d_d1": {"inputs": ["high", "low", "volume"], "func": f03_tpcl_103_steidlmayer_minus_development_at_top_252d_d1},
    "f03_tpcl_104_steidlmayer_plus_development_failure_252d_d1": {"inputs": ["high", "volume", "close"], "func": f03_tpcl_104_steidlmayer_plus_development_failure_252d_d1},
    "f03_tpcl_105_time_to_pattern_completion_estimate_252d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_105_time_to_pattern_completion_estimate_252d_d1},
    "f03_tpcl_106_bars_since_pattern_recognition_252d_d1": {"inputs": ["high"], "func": f03_tpcl_106_bars_since_pattern_recognition_252d_d1},
    "f03_tpcl_107_pattern_recognition_confidence_composite_252d_d1": {"inputs": ["high", "low", "volume"], "func": f03_tpcl_107_pattern_recognition_confidence_composite_252d_d1},
    "f03_tpcl_108_pattern_quality_vs_ideal_template_R2_252d_d1": {"inputs": ["high"], "func": f03_tpcl_108_pattern_quality_vs_ideal_template_R2_252d_d1},
    "f03_tpcl_109_pattern_volume_confirmation_strength_63d_d1": {"inputs": ["close", "volume"], "func": f03_tpcl_109_pattern_volume_confirmation_strength_63d_d1},
    "f03_tpcl_110_multi_pattern_co_occurrence_count_252d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_110_multi_pattern_co_occurrence_count_252d_d1},
    "f03_tpcl_111_pattern_within_pattern_nested_indicator_d1": {"inputs": ["high"], "func": f03_tpcl_111_pattern_within_pattern_nested_indicator_d1},
    "f03_tpcl_112_universal_pattern_symmetry_index_252d_d1": {"inputs": ["close"], "func": f03_tpcl_112_universal_pattern_symmetry_index_252d_d1},
    "f03_tpcl_113_universal_pattern_asymmetry_penalty_252d_d1": {"inputs": ["close"], "func": f03_tpcl_113_universal_pattern_asymmetry_penalty_252d_d1},
    "f03_tpcl_114_pattern_duration_relative_typical_252d_d1": {"inputs": ["high"], "func": f03_tpcl_114_pattern_duration_relative_typical_252d_d1},
    "f03_tpcl_115_multi_scale_pattern_consensus_63_and_252_indicator_d1": {"inputs": ["high"], "func": f03_tpcl_115_multi_scale_pattern_consensus_63_and_252_indicator_d1},
    "f03_tpcl_116_pattern_detection_robustness_tolerance_252d_d1": {"inputs": ["high"], "func": f03_tpcl_116_pattern_detection_robustness_tolerance_252d_d1},
    "f03_tpcl_117_hs_neckline_not_broken_within_21d_after_right_shoulder_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_117_hs_neckline_not_broken_within_21d_after_right_shoulder_d1},
    "f03_tpcl_118_double_top_not_below_midpoint_low_failure_252d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_118_double_top_not_below_midpoint_low_failure_252d_d1},
    "f03_tpcl_119_triple_top_continuation_to_new_high_failure_252d_d1": {"inputs": ["high", "close"], "func": f03_tpcl_119_triple_top_continuation_to_new_high_failure_252d_d1},
    "f03_tpcl_120_wedge_broke_opposite_direction_failure_252d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_120_wedge_broke_opposite_direction_failure_252d_d1},
    "f03_tpcl_121_barr_lead_in_line_held_failure_252d_d1": {"inputs": ["close"], "func": f03_tpcl_121_barr_lead_in_line_held_failure_252d_d1},
    "f03_tpcl_122_pattern_failure_event_count_252d_d1": {"inputs": ["high", "close"], "func": f03_tpcl_122_pattern_failure_event_count_252d_d1},
    "f03_tpcl_123_average_pattern_failure_rate_504d_d1": {"inputs": ["high", "close"], "func": f03_tpcl_123_average_pattern_failure_rate_504d_d1},
    "f03_tpcl_124_failed_pattern_then_extension_count_252d_d1": {"inputs": ["high", "close"], "func": f03_tpcl_124_failed_pattern_then_extension_count_252d_d1},
    "f03_tpcl_125_failed_pattern_then_pullback_count_252d_d1": {"inputs": ["high", "close"], "func": f03_tpcl_125_failed_pattern_then_pullback_count_252d_d1},
    "f03_tpcl_126_pattern_completion_rate_at_stock_vs_historical_504d_d1": {"inputs": ["high", "close"], "func": f03_tpcl_126_pattern_completion_rate_at_stock_vs_historical_504d_d1},
    "f03_tpcl_127_hs_measured_move_target_distance_252d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_127_hs_measured_move_target_distance_252d_d1},
    "f03_tpcl_128_double_top_measured_move_target_distance_252d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_128_double_top_measured_move_target_distance_252d_d1},
    "f03_tpcl_129_triple_top_measured_move_target_distance_252d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_129_triple_top_measured_move_target_distance_252d_d1},
    "f03_tpcl_130_wedge_measured_move_channel_height_projection_252d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_130_wedge_measured_move_channel_height_projection_252d_d1},
    "f03_tpcl_131_diamond_measured_move_target_distance_252d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_131_diamond_measured_move_target_distance_252d_d1},
    "f03_tpcl_132_bars_to_target_estimate_252d_d1": {"inputs": ["close", "low", "high"], "func": f03_tpcl_132_bars_to_target_estimate_252d_d1},
    "f03_tpcl_133_distance_from_current_close_to_target_atr_norm_252d_d1": {"inputs": ["close", "high", "low"], "func": f03_tpcl_133_distance_from_current_close_to_target_atr_norm_252d_d1},
    "f03_tpcl_134_measured_move_overshoot_undershoot_history_504d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_134_measured_move_overshoot_undershoot_history_504d_d1},
    "f03_tpcl_135_multi_pattern_co_occurrence_aggregate_252d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_135_multi_pattern_co_occurrence_aggregate_252d_d1},
    "f03_tpcl_136_pattern_quality_consensus_high_R2_252d_d1": {"inputs": ["high", "low"], "func": f03_tpcl_136_pattern_quality_consensus_high_R2_252d_d1},
    "f03_tpcl_137_pattern_plus_measured_move_alignment_composite_252d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_137_pattern_plus_measured_move_alignment_composite_252d_d1},
    "f03_tpcl_138_pattern_plus_volume_confirmation_composite_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f03_tpcl_138_pattern_plus_volume_confirmation_composite_252d_d1},
    "f03_tpcl_139_pattern_plus_neckline_break_composite_252d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_139_pattern_plus_neckline_break_composite_252d_d1},
    "f03_tpcl_140_pattern_plus_retest_failure_composite_252d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_140_pattern_plus_retest_failure_composite_252d_d1},
    "f03_tpcl_141_multi_scale_pattern_consensus_composite_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_141_multi_scale_pattern_consensus_composite_d1},
    "f03_tpcl_142_pattern_failure_then_extension_warning_252d_d1": {"inputs": ["high", "close"], "func": f03_tpcl_142_pattern_failure_then_extension_warning_252d_d1},
    "f03_tpcl_143_pattern_detection_density_per_252d_d1": {"inputs": ["high"], "func": f03_tpcl_143_pattern_detection_density_per_252d_d1},
    "f03_tpcl_144_pattern_symmetry_aggregate_252d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_144_pattern_symmetry_aggregate_252d_d1},
    "f03_tpcl_145_pattern_projection_alignment_composite_252d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_145_pattern_projection_alignment_composite_252d_d1},
    "f03_tpcl_146_pattern_aged_still_active_composite_252d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_146_pattern_aged_still_active_composite_252d_d1},
    "f03_tpcl_147_pattern_newly_completed_composite_63d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_147_pattern_newly_completed_composite_63d_d1},
    "f03_tpcl_148_pattern_completion_imminent_composite_252d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_148_pattern_completion_imminent_composite_252d_d1},
    "f03_tpcl_149_pattern_failure_then_pullback_composite_252d_d1": {"inputs": ["high", "close"], "func": f03_tpcl_149_pattern_failure_then_pullback_composite_252d_d1},
    "f03_tpcl_150_terminal_pattern_aggregate_sum_of_reversal_252d_d1": {"inputs": ["high", "low", "close"], "func": f03_tpcl_150_terminal_pattern_aggregate_sum_of_reversal_252d_d1},
}
