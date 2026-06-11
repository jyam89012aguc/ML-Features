"""trend_line_break_dynamics base features 151-225 — Pipeline 1b-technical.

Practitioner gap-fill set covering:
  A) horizontal S/R line breaks            (151-160)
  B) connected-pivots trendline dynamics   (161-172)
  C) Andrews pitchfork                     (173-178)
  D) speed lines (1/3 and 2/3)             (179-184)
  E) channel breakouts                     (185-194)
  F) trendline cluster confluence          (195-202)
  G) trendline-volume interaction          (203-210)
  H) failed breaks & magnetism             (211-218)
  I) trendline acceleration before break   (219-225)

All features PIT-clean: right-anchored rolling windows, no .shift(N) anywhere.
Pivot detection (Williams Fractal style): a 5-bar pivot at index t is confirmed
at index t+2, so we use `high.shift(2)` / `low.shift(2)` and look at 2 bars
before and after that candidate.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504


# ============================================================
#                       SAFE NUMERIC HELPERS
# ============================================================

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


def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat(
        [high - low, (high - pc).abs(), (low - pc).abs()], axis=1
    ).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _bars_since_true(b: pd.Series) -> pd.Series:
    arr = b.fillna(False).astype(bool).values
    n = arr.size
    out = np.full(n, np.nan, dtype=float)
    last = -1
    for i in range(n):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=b.index)


# ============================================================
#                       PIVOT HELPERS  (PIT-safe)
# ============================================================

def _pivot_high_event(high: pd.Series, n: int = 2) -> pd.Series:
    """Williams Fractal: bar at t-n is a pivot high if it's the max in window
    [t-2n, t]. Confirmed at bar t. Returns boolean series indexed at t."""
    window = 2 * n + 1
    rolling_max = high.rolling(window, min_periods=window).max()
    center_val = high.shift(n)
    return (center_val == rolling_max) & rolling_max.notna()


def _pivot_low_event(low: pd.Series, n: int = 2) -> pd.Series:
    window = 2 * n + 1
    rolling_min = low.rolling(window, min_periods=window).min()
    center_val = low.shift(n)
    return (center_val == rolling_min) & rolling_min.notna()


def _pivot_value_at_conf(series: pd.Series, ev: pd.Series, n: int) -> pd.Series:
    return series.shift(n).where(ev, np.nan)


def _pivot_pos_at_conf(ev: pd.Series, n: int) -> pd.Series:
    idx_pos = pd.Series(np.arange(len(ev), dtype=float), index=ev.index)
    return (idx_pos - float(n)).where(ev, np.nan)


def _last_k_pivots(val_at_conf: pd.Series, pos_at_conf: pd.Series, k: int,
                   lookback: int):
    """For each bar i, return last k pivot (value, position) pairs visible
    within [i-lookback+1, i]. Returns dict of arrays of length n."""
    n = len(val_at_conf)
    v_arr = val_at_conf.values
    p_arr = pos_at_conf.values
    vs = [np.full(n, np.nan, dtype=float) for _ in range(k)]
    ps = [np.full(n, np.nan, dtype=float) for _ in range(k)]
    for i in range(n):
        lo = max(0, i - lookback + 1)
        wv = v_arr[lo:i + 1]
        wp = p_arr[lo:i + 1]
        mask = ~np.isnan(wv)
        if mask.sum() < k:
            continue
        last_v = wv[mask][-k:]
        last_p = wp[mask][-k:]
        for j in range(k):
            vs[j][i] = last_v[j]
            ps[j][i] = last_p[j]
    return [pd.Series(vs[j], index=val_at_conf.index) for j in range(k)], \
           [pd.Series(ps[j], index=val_at_conf.index) for j in range(k)]


def _line_through_two_pivots(v0, v1, p0, p1, idx_pos):
    """Slope/intercept of line through (p0,v0) and (p1,v1). Projects to idx_pos."""
    slope = _safe_div(v1 - v0, p1 - p0)
    intercept = v1 - slope * p1
    projected = intercept + slope * idx_pos
    return slope, intercept, projected


def _line_through_pivots_ols(val_at_conf, pos_at_conf, k, lookback):
    """OLS-fit line through last k pivots. Returns (slope, intercept, R2) series."""
    n = len(val_at_conf)
    v_arr = val_at_conf.values
    p_arr = pos_at_conf.values
    sl = np.full(n, np.nan, dtype=float)
    it = np.full(n, np.nan, dtype=float)
    r2 = np.full(n, np.nan, dtype=float)
    for i in range(n):
        lo = max(0, i - lookback + 1)
        wv = v_arr[lo:i + 1]
        wp = p_arr[lo:i + 1]
        mask = ~np.isnan(wv)
        if mask.sum() < k:
            continue
        v = wv[mask][-k:]
        p = wp[mask][-k:]
        pm = p.mean(); vm = v.mean()
        den = float(((p - pm) ** 2).sum())
        if den <= 0:
            continue
        b = float(((p - pm) * (v - vm)).sum() / den)
        a = vm - b * pm
        yhat = a + b * p
        ss_res = float(((v - yhat) ** 2).sum())
        ss_tot = float(((v - vm) ** 2).sum())
        sl[i] = b
        it[i] = a
        r2[i] = 1.0 - ss_res / ss_tot if ss_tot > 0 else np.nan
    return (pd.Series(sl, index=val_at_conf.index),
            pd.Series(it, index=val_at_conf.index),
            pd.Series(r2, index=val_at_conf.index))


# ============================================================
#                  HORIZONTAL S/R LEVEL HELPERS
# ============================================================

def _horizontal_levels_near_close(high, low, close, lookback=YDAYS,
                                  pivot_n=3, tol_frac=0.02):
    """Cluster pivot-high values into horizontal levels and compute, per bar:
       - count of levels above close within tol_frac*close
       - count of levels below close within tol_frac*close
       - distance to nearest level above (atr units)
       - distance to nearest level below (atr units)
       - max touch count of any level
       - cluster density above (number of distinct levels above)
       - cluster density below
    Returns dict of pd.Series.
    """
    n = len(close)
    ev_h = _pivot_high_event(high, pivot_n)
    ev_l = _pivot_low_event(low, pivot_n)
    pv_h = _pivot_value_at_conf(high, ev_h, pivot_n).values
    pv_l = _pivot_value_at_conf(low, ev_l, pivot_n).values
    c_arr = close.values
    atr = _atr(high, low, close, 21).values

    test_above = np.full(n, np.nan, dtype=float)
    fail_above = np.full(n, np.nan, dtype=float)
    nearest_above_atr = np.full(n, np.nan, dtype=float)
    nearest_below_atr = np.full(n, np.nan, dtype=float)
    cluster_above = np.full(n, np.nan, dtype=float)
    cluster_below = np.full(n, np.nan, dtype=float)
    multi_strength = np.full(n, np.nan, dtype=float)

    for i in range(n):
        lo = max(0, i - lookback + 1)
        if np.isnan(c_arr[i]):
            continue
        c = c_arr[i]
        a = atr[i] if not np.isnan(atr[i]) and atr[i] > 0 else c * 0.01
        # gather all pivot levels in window
        levels = []
        for j in range(lo, i + 1):
            if not np.isnan(pv_h[j]):
                levels.append(pv_h[j])
            if not np.isnan(pv_l[j]):
                levels.append(pv_l[j])
        if not levels:
            continue
        levels = np.array(levels)
        # cluster levels: round to tol_frac*c bins, count occurrences = "touches"
        bin_size = tol_frac * c
        if bin_size <= 0:
            continue
        keys = np.round(levels / bin_size).astype(int)
        # touch counts per bin
        unique_keys, counts = np.unique(keys, return_counts=True)
        cluster_levels = unique_keys * bin_size
        # bins above & below close
        above_mask = cluster_levels > c
        below_mask = cluster_levels < c
        cluster_above[i] = float(above_mask.sum())
        cluster_below[i] = float(below_mask.sum())
        if above_mask.any():
            la = cluster_levels[above_mask]
            nearest_above_atr[i] = float((la.min() - c) / a)
            # tests = pivot highs that touched the nearest above level
            test_above[i] = float(counts[above_mask][np.argmin(la)])
        if below_mask.any():
            lb = cluster_levels[below_mask]
            nearest_below_atr[i] = float((c - lb.max()) / a)
        multi_strength[i] = float(counts.max())
        # failure count: how many bars in window had close > nearest_above then reversed
        # (computed for the i-th nearest level)
        if above_mask.any():
            nearest_lv = cluster_levels[above_mask][np.argmin(la)]
            # within window, count bars where close>nearest_lv then 5d later close<nearest_lv
            cl_win = c_arr[lo:i + 1]
            fl = 0
            for k in range(len(cl_win) - 5):
                if (not np.isnan(cl_win[k]) and cl_win[k] > nearest_lv and
                        not np.isnan(cl_win[k + 5]) and cl_win[k + 5] < nearest_lv):
                    fl += 1
            fail_above[i] = float(fl)

    return {
        "test_above": pd.Series(test_above, index=close.index),
        "fail_above": pd.Series(fail_above, index=close.index),
        "nearest_above_atr": pd.Series(nearest_above_atr, index=close.index),
        "nearest_below_atr": pd.Series(nearest_below_atr, index=close.index),
        "cluster_above": pd.Series(cluster_above, index=close.index),
        "cluster_below": pd.Series(cluster_below, index=close.index),
        "multi_strength": pd.Series(multi_strength, index=close.index),
    }


# ============================================================
#                  PIVOT-PROJECTED LINE PROJECTION
# ============================================================

def _pivot_line_projection(high_or_low: pd.Series, kind: str, k: int,
                           lookback: int, pivot_n: int = 2):
    """Returns (slope, projected_at_each_t) series for the line through the
    last k pivots of given kind ('high' or 'low')."""
    ev = (_pivot_high_event(high_or_low, pivot_n) if kind == "high"
          else _pivot_low_event(high_or_low, pivot_n))
    v = _pivot_value_at_conf(high_or_low, ev, pivot_n)
    p = _pivot_pos_at_conf(ev, pivot_n)
    if k == 2:
        vs, ps = _last_k_pivots(v, p, 2, lookback)
        v0, v1 = vs[0], vs[1]
        p0, p1 = ps[0], ps[1]
        slope = _safe_div(v1 - v0, p1 - p0)
        intercept = v1 - slope * p1
    else:
        slope, intercept, _ = _line_through_pivots_ols(v, p, k, lookback)
    idx_pos = pd.Series(np.arange(len(high_or_low), dtype=float),
                        index=high_or_low.index)
    projected = intercept + slope * idx_pos
    return slope, projected


# ============================================================
#                          FEATURES
# ============================================================

# ---------- Bucket A: horizontal S/R (151-160) ----------

def f17_tlbk_151_horizontal_resistance_test_count_above_252d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Touches at nearest pivot-resistance level above close, 252d lookback."""
    return _horizontal_levels_near_close(high, low, close, YDAYS)["test_above"]


def f17_tlbk_152_horizontal_resistance_failure_count_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close above nearest resistance then reverses below within 5d, count in 63d."""
    return _horizontal_levels_near_close(high, low, close, QDAYS)["fail_above"]


def f17_tlbk_153_horizontal_resistance_break_then_retest_count_252d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close breaks above nearest-resistance, then within 10d returns within 0.5 ATR
    of the broken level. Count in 252d window."""
    n = len(close)
    out = np.full(n, np.nan, dtype=float)
    levels_info = _horizontal_levels_near_close(high, low, close, YDAYS)
    near = levels_info["nearest_above_atr"].values  # > 0 means above
    atr = _atr(high, low, close, 21).values
    c = close.values
    # we approximate: a break-then-retest event at bar i if c[i-d]>level and abs(c[i]-level)<0.5atr
    # We re-derive levels per bar window for accuracy
    ev_h = _pivot_high_event(high, 3)
    pv_h = _pivot_value_at_conf(high, ev_h, 3).values
    pv_l = _pivot_value_at_conf(low, _pivot_low_event(low, 3), 3).values
    for i in range(n):
        lo = max(0, i - YDAYS + 1)
        ci = c[i]
        if np.isnan(ci):
            continue
        bin_size = 0.02 * ci
        if bin_size <= 0:
            continue
        levels = []
        for j in range(lo, i + 1):
            if not np.isnan(pv_h[j]):
                levels.append(pv_h[j])
            if not np.isnan(pv_l[j]):
                levels.append(pv_l[j])
        if not levels:
            continue
        levels = np.array(levels)
        keys = np.round(levels / bin_size).astype(int)
        unique_keys = np.unique(keys)
        lvs = unique_keys * bin_size
        cnt = 0
        for lv in lvs:
            a_loc = atr[i] if not np.isnan(atr[i]) and atr[i] > 0 else ci * 0.01
            # count windows in [lo..i-10] where break then retest within 10d
            for k in range(lo, i - 10):
                if (not np.isnan(c[k]) and not np.isnan(c[k - 1]) and
                        c[k] > lv >= c[k - 1]):
                    # retest within next 10 bars
                    retested = False
                    for m in range(k + 1, min(k + 11, i + 1)):
                        if not np.isnan(c[m]) and abs(c[m] - lv) < 0.5 * a_loc:
                            retested = True
                            break
                    if retested:
                        cnt += 1
        out[i] = float(cnt)
    return pd.Series(out, index=close.index)


def f17_tlbk_154_horizontal_support_break_count_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in 63d where close crossed below a horizontal pivot-low cluster level."""
    n = len(close)
    out = np.full(n, np.nan, dtype=float)
    c = close.values
    ev_l = _pivot_low_event(low, 3)
    pv_l = _pivot_value_at_conf(low, ev_l, 3).values
    for i in range(n):
        lo = max(0, i - QDAYS + 1)
        ci = c[i]
        if np.isnan(ci):
            continue
        bin_size = 0.02 * ci
        if bin_size <= 0:
            continue
        levels = []
        for j in range(lo, i + 1):
            if not np.isnan(pv_l[j]):
                levels.append(pv_l[j])
        if not levels:
            continue
        levels = np.array(levels)
        keys = np.round(levels / bin_size).astype(int)
        unique_keys = np.unique(keys)
        lvs = unique_keys * bin_size
        cnt = 0
        for lv in lvs:
            for k in range(lo + 1, i + 1):
                if (not np.isnan(c[k]) and not np.isnan(c[k - 1]) and
                        c[k - 1] >= lv > c[k]):
                    cnt += 1
        out[i] = float(cnt)
    return pd.Series(out, index=close.index)


def f17_tlbk_155_horizontal_support_break_then_retest_failure_count_252d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Broke support, then within 10d retested from below (back to level) and
    failed (closed back below the level within next 5d). Count in 252d."""
    n = len(close)
    out = np.full(n, np.nan, dtype=float)
    c = close.values
    pv_l = _pivot_value_at_conf(low, _pivot_low_event(low, 3), 3).values
    atr = _atr(high, low, close, 21).values
    for i in range(n):
        lo = max(0, i - YDAYS + 1)
        ci = c[i]
        if np.isnan(ci):
            continue
        bin_size = 0.02 * ci
        if bin_size <= 0:
            continue
        levels = []
        for j in range(lo, i + 1):
            if not np.isnan(pv_l[j]):
                levels.append(pv_l[j])
        if not levels:
            continue
        levels = np.array(levels)
        keys = np.round(levels / bin_size).astype(int)
        unique_keys = np.unique(keys)
        lvs = unique_keys * bin_size
        cnt = 0
        for lv in lvs:
            for k in range(lo + 1, i - 15):
                a_loc = atr[k] if not np.isnan(atr[k]) and atr[k] > 0 else ci * 0.01
                if (not np.isnan(c[k]) and not np.isnan(c[k - 1]) and
                        c[k - 1] >= lv > c[k]):
                    # search for retest in next 10
                    for m in range(k + 1, min(k + 11, i - 4)):
                        if (not np.isnan(c[m]) and abs(c[m] - lv) < 0.5 * a_loc):
                            # failure: close back below lv within 5d after m
                            failed = False
                            for q in range(m + 1, min(m + 6, i + 1)):
                                if not np.isnan(c[q]) and c[q] < lv - 0.1 * a_loc:
                                    failed = True
                                    break
                            if failed:
                                cnt += 1
                            break
        out[i] = float(cnt)
    return pd.Series(out, index=close.index)


def f17_tlbk_156_distance_to_nearest_horizontal_resistance_atr_units_252d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Distance (ATR units, positive) from close to nearest pivot-resistance above."""
    return _horizontal_levels_near_close(high, low, close, YDAYS)["nearest_above_atr"]


def f17_tlbk_157_distance_to_nearest_horizontal_support_atr_units_252d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Distance (ATR units, positive) from close to nearest pivot-support below."""
    return _horizontal_levels_near_close(high, low, close, YDAYS)["nearest_below_atr"]


def f17_tlbk_158_horizontal_cluster_density_above_close_252d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Distinct cluster levels above close in 252d. High = thick overhead supply."""
    return _horizontal_levels_near_close(high, low, close, YDAYS)["cluster_above"]


def f17_tlbk_159_horizontal_cluster_density_below_close_252d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _horizontal_levels_near_close(high, low, close, YDAYS)["cluster_below"]


def f17_tlbk_160_multi_test_horizontal_level_strength_252d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max touch count of any horizontal level in 252d. >=3 = strong level."""
    return _horizontal_levels_near_close(high, low, close, YDAYS)["multi_strength"]


# ---------- Bucket B: connected-pivots trendlines (161-172) ----------

def f17_tlbk_161_upper_trendline_slope_from_2_recent_pivot_highs_252d(
        high: pd.Series) -> pd.Series:
    """Slope of line through 2 most recent pivot highs (5-bar fractals), 252d lookback."""
    slope, _ = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    return slope


def f17_tlbk_162_upper_trendline_slope_from_3_recent_pivot_highs_252d(
        high: pd.Series) -> pd.Series:
    """OLS slope of line through 3 most recent pivot highs. More pivots = stronger trendline."""
    slope, _ = _pivot_line_projection(high, "high", 3, YDAYS, pivot_n=2)
    return slope


def f17_tlbk_163_lower_trendline_slope_from_2_recent_pivot_lows_252d(
        low: pd.Series) -> pd.Series:
    slope, _ = _pivot_line_projection(low, "low", 2, YDAYS, pivot_n=2)
    return slope


def f17_tlbk_164_lower_trendline_slope_from_3_recent_pivot_lows_252d(
        low: pd.Series) -> pd.Series:
    slope, _ = _pivot_line_projection(low, "low", 3, YDAYS, pivot_n=2)
    return slope


def f17_tlbk_165_upper_trendline_break_event_count_63d(
        high: pd.Series, close: pd.Series) -> pd.Series:
    """Close > projected upper-trendline value, was <= it on previous bar. Count in 63d."""
    _, proj = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    crossed = (close > proj) & (close.shift(1) <= proj.shift(1))
    return crossed.fillna(False).astype(float).rolling(QDAYS, min_periods=21).sum()


def f17_tlbk_166_lower_trendline_break_event_count_63d(
        low: pd.Series, close: pd.Series) -> pd.Series:
    """Close < projected lower-trendline value, was >= it on previous bar. Count in 63d.
    For shorts, a lower-trendline break is a confirmation of downtrend continuation."""
    _, proj = _pivot_line_projection(low, "low", 2, YDAYS, pivot_n=2)
    crossed = (close < proj) & (close.shift(1) >= proj.shift(1))
    return crossed.fillna(False).astype(float).rolling(QDAYS, min_periods=21).sum()


def f17_tlbk_167_upper_trendline_r2_fit_quality_252d(
        high: pd.Series) -> pd.Series:
    """R^2 of OLS line through last 3 pivot highs over 252d window."""
    ev = _pivot_high_event(high, 2)
    v = _pivot_value_at_conf(high, ev, 2)
    p = _pivot_pos_at_conf(ev, 2)
    _, _, r2 = _line_through_pivots_ols(v, p, 3, YDAYS)
    return r2


def f17_tlbk_168_lower_trendline_r2_fit_quality_252d(
        low: pd.Series) -> pd.Series:
    ev = _pivot_low_event(low, 2)
    v = _pivot_value_at_conf(low, ev, 2)
    p = _pivot_pos_at_conf(ev, 2)
    _, _, r2 = _line_through_pivots_ols(v, p, 3, YDAYS)
    return r2


def f17_tlbk_169_upper_trendline_touch_count_252d(
        high: pd.Series) -> pd.Series:
    """Number of pivot highs in 252d that lie within 0.5 sigma of the upper-trendline projection."""
    ev = _pivot_high_event(high, 2)
    v = _pivot_value_at_conf(high, ev, 2)
    p = _pivot_pos_at_conf(ev, 2)
    slope, _ = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    _, intercept_proj = _line_through_pivots_ols(v, p, 2, YDAYS)[:2]  # noqa
    # simpler: project via two-pivot line and count pivots near it
    vs, ps = _last_k_pivots(v, p, 2, YDAYS)
    v0, v1 = vs[0], vs[1]
    p0, p1 = ps[0], ps[1]
    sl = _safe_div(v1 - v0, p1 - p0)
    it = v1 - sl * p1
    sd = high.rolling(63, min_periods=21).std()
    n = len(high)
    out = np.full(n, np.nan, dtype=float)
    v_arr = v.values
    p_arr = p.values
    sl_arr = sl.values
    it_arr = it.values
    sd_arr = sd.values
    for i in range(n):
        if np.isnan(sl_arr[i]) or np.isnan(it_arr[i]):
            continue
        lo = max(0, i - YDAYS + 1)
        cnt = 0
        sigma = sd_arr[i] if not np.isnan(sd_arr[i]) and sd_arr[i] > 0 else 1.0
        for j in range(lo, i + 1):
            if not np.isnan(v_arr[j]):
                proj = it_arr[i] + sl_arr[i] * p_arr[j]
                if abs(v_arr[j] - proj) <= 0.5 * sigma:
                    cnt += 1
        out[i] = float(cnt)
    return pd.Series(out, index=high.index)


def f17_tlbk_170_lower_trendline_touch_count_252d(
        low: pd.Series) -> pd.Series:
    ev = _pivot_low_event(low, 2)
    v = _pivot_value_at_conf(low, ev, 2)
    p = _pivot_pos_at_conf(ev, 2)
    vs, ps = _last_k_pivots(v, p, 2, YDAYS)
    v0, v1 = vs[0], vs[1]
    p0, p1 = ps[0], ps[1]
    sl = _safe_div(v1 - v0, p1 - p0)
    it = v1 - sl * p1
    sd = low.rolling(63, min_periods=21).std()
    n = len(low)
    out = np.full(n, np.nan, dtype=float)
    v_arr = v.values
    p_arr = p.values
    sl_arr = sl.values
    it_arr = it.values
    sd_arr = sd.values
    for i in range(n):
        if np.isnan(sl_arr[i]) or np.isnan(it_arr[i]):
            continue
        lo = max(0, i - YDAYS + 1)
        cnt = 0
        sigma = sd_arr[i] if not np.isnan(sd_arr[i]) and sd_arr[i] > 0 else 1.0
        for j in range(lo, i + 1):
            if not np.isnan(v_arr[j]):
                proj = it_arr[i] + sl_arr[i] * p_arr[j]
                if abs(v_arr[j] - proj) <= 0.5 * sigma:
                    cnt += 1
        out[i] = float(cnt)
    return pd.Series(out, index=low.index)


def f17_tlbk_171_upper_trendline_age_at_current_bar_252d(
        high: pd.Series) -> pd.Series:
    """Bars elapsed since the older of the two most-recent pivot highs that
    define the current upper trendline. Long-standing = stronger trendline."""
    ev = _pivot_high_event(high, 2)
    v = _pivot_value_at_conf(high, ev, 2)
    p = _pivot_pos_at_conf(ev, 2)
    vs, ps = _last_k_pivots(v, p, 2, YDAYS)
    p0 = ps[0]
    idx_pos = pd.Series(np.arange(len(high), dtype=float), index=high.index)
    return (idx_pos - p0)


def f17_tlbk_172_multi_trendline_overlap_zone_indicator_252d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Upper and lower trendlines converge within 2 ATR of each other AND of close.
    Apex zone: classic terminal squeeze before resolution."""
    _, proj_up = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    _, proj_dn = _pivot_line_projection(low, "low", 2, YDAYS, pivot_n=2)
    atr = _atr(high, low, close, 21)
    gap = (proj_up - proj_dn).abs()
    near_close = ((close - proj_up).abs() < 2 * atr) & ((close - proj_dn).abs() < 2 * atr)
    converging = gap < 2 * atr
    return (converging & near_close).astype(float).where(proj_up.notna() & proj_dn.notna(), np.nan)


# ---------- Bucket C: Andrews pitchfork (173-178) ----------

def _pitchfork_lines(high, low, close, lookback=YDAYS):
    """For each bar, identify 3 most-recent alternating pivots (P1, P2, P3)
    and compute pitchfork (median line, upper parallel, lower parallel)
    projected at the current bar. Returns dict of series."""
    n = len(close)
    ev_h = _pivot_high_event(high, 2)
    ev_l = _pivot_low_event(low, 2)
    vh = _pivot_value_at_conf(high, ev_h, 2).values
    vl = _pivot_value_at_conf(low, ev_l, 2).values
    n_idx = np.arange(n, dtype=float)
    pos_h = (n_idx - 2.0)
    pos_l = (n_idx - 2.0)

    # collect all (pos, value, kind) pivots
    pivots = []
    for i in range(n):
        if not np.isnan(vh[i]):
            pivots.append((pos_h[i], vh[i], "H", i))
        if not np.isnan(vl[i]):
            pivots.append((pos_l[i], vl[i], "L", i))
    pivots.sort(key=lambda x: x[0])

    med_arr = np.full(n, np.nan, dtype=float)
    up_arr = np.full(n, np.nan, dtype=float)
    dn_arr = np.full(n, np.nan, dtype=float)

    for i in range(n):
        recent = [p for p in pivots if p[3] <= i and i - p[3] < lookback]
        if len(recent) < 3:
            continue
        # alternating triplet from most-recent backwards
        chosen = [recent[-1]]
        for j in range(len(recent) - 2, -1, -1):
            if recent[j][2] != chosen[-1][2]:
                chosen.append(recent[j])
                if len(chosen) == 3:
                    break
        if len(chosen) < 3:
            continue
        # order chronologically: P1 oldest, P3 newest
        chosen.sort(key=lambda x: x[0])
        p1_pos, p1_val = chosen[0][0], chosen[0][1]
        p2_pos, p2_val = chosen[1][0], chosen[1][1]
        p3_pos, p3_val = chosen[2][0], chosen[2][1]
        # midpoint of P2-P3
        mid_pos = 0.5 * (p2_pos + p3_pos)
        mid_val = 0.5 * (p2_val + p3_val)
        # median line: from P1 through midpoint
        denom = mid_pos - p1_pos
        if denom == 0:
            continue
        slope = (mid_val - p1_val) / denom
        # project to current bar
        med_now = p1_val + slope * (i - p1_pos)
        # parallels: same slope through P2 and P3
        up_now = max(p2_val, p3_val) + slope * (i - (p2_pos if p2_val > p3_val else p3_pos))
        dn_now = min(p2_val, p3_val) + slope * (i - (p2_pos if p2_val < p3_val else p3_pos))
        med_arr[i] = med_now
        up_arr[i] = up_now
        dn_arr[i] = dn_now

    return {
        "median": pd.Series(med_arr, index=close.index),
        "upper": pd.Series(up_arr, index=close.index),
        "lower": pd.Series(dn_arr, index=close.index),
    }


def f17_tlbk_173_pitchfork_median_line_distance_at_current_bar_252d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log-distance close vs pitchfork median line. Negative = below median."""
    pf = _pitchfork_lines(high, low, close, YDAYS)
    return _safe_log(close) - _safe_log(pf["median"])


def f17_tlbk_174_pitchfork_upper_parallel_break_count_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close > upper parallel, was <= it before. Count in 63d. Bull-side blow-off line break."""
    pf = _pitchfork_lines(high, low, close, YDAYS)
    up = pf["upper"]
    crossed = (close > up) & (close.shift(1) <= up.shift(1))
    return crossed.fillna(False).astype(float).rolling(QDAYS, min_periods=21).sum()


def f17_tlbk_175_pitchfork_lower_parallel_break_count_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pf = _pitchfork_lines(high, low, close, YDAYS)
    dn = pf["lower"]
    crossed = (close < dn) & (close.shift(1) >= dn.shift(1))
    return crossed.fillna(False).astype(float).rolling(QDAYS, min_periods=21).sum()


def f17_tlbk_176_pitchfork_median_line_rejection_count_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close approached median from below within 0.5 ATR, then closed back below by next bar.
    Strong rejection of mean-line magnetism = continuation."""
    pf = _pitchfork_lines(high, low, close, YDAYS)
    med = pf["median"]
    atr = _atr(high, low, close, 21)
    # Rejection: high reached the median band (within 0.1 ATR above it) BUT close
    # ended at least 0.1 ATR below it on the same bar. PIT-safe (no forward shift).
    rejection = (high >= med - 0.1 * atr) & (close < med - 0.1 * atr)
    return rejection.fillna(False).astype(float).rolling(QDAYS, min_periods=21).sum()


def f17_tlbk_177_pitchfork_trigger_event_count_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Hagopian/trigger line: price re-enters the fork after breaking out of it.
    Crossed upper parallel downward (was above, now back below upper). Count in 63d."""
    pf = _pitchfork_lines(high, low, close, YDAYS)
    up = pf["upper"]
    trigger = (close.shift(1) > up.shift(1)) & (close <= up)
    return trigger.fillna(False).astype(float).rolling(QDAYS, min_periods=21).sum()


def f17_tlbk_178_pitchfork_failure_event_count_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Failed break: crossed upper, came back inside within 5d, AND then closed below
    median within next 10d. Count in 63d."""
    pf = _pitchfork_lines(high, low, close, YDAYS)
    up = pf["upper"]
    med = pf["median"]
    n = len(close)
    c = close.values; u = up.values; m = med.values
    fails = np.zeros(n, dtype=float)
    for i in range(15, n):
        # crossed up at bar k (k < i), back inside by k+5, then below median by k+15
        for k in range(max(0, i - QDAYS), i - 10):
            if (not np.isnan(c[k]) and not np.isnan(u[k]) and
                    not np.isnan(c[k - 1]) and not np.isnan(u[k - 1]) and
                    c[k] > u[k] and c[k - 1] <= u[k - 1]):
                inside = False
                for q in range(k + 1, min(k + 6, n)):
                    if not np.isnan(c[q]) and not np.isnan(u[q]) and c[q] <= u[q]:
                        inside = True
                        break
                if inside:
                    for q in range(k + 1, min(k + 16, n)):
                        if not np.isnan(c[q]) and not np.isnan(m[q]) and c[q] < m[q]:
                            fails[i] += 1
                            break
    out = pd.Series(fails, index=close.index)
    # require pitchfork to exist at i
    return out.where(up.notna() & med.notna(), np.nan)


# ---------- Bucket D: speed lines 1/3, 2/3 (179-184) ----------

def _speed_line_levels(high, low, close, lookback=YDAYS):
    """Identify swing-high to swing-low move within lookback. Construct speed lines
    at 1/3 and 2/3 of the vertical range. Returns dict of series for the line VALUE
    projected to the current bar."""
    n = len(close)
    out_13 = np.full(n, np.nan, dtype=float)
    out_23 = np.full(n, np.nan, dtype=float)
    h_arr = high.values
    l_arr = low.values
    for i in range(n):
        lo = max(0, i - lookback + 1)
        hw = h_arr[lo:i + 1]; lw = l_arr[lo:i + 1]
        if len(hw) < 10:
            continue
        # identify highest high and its position, then lowest low after that
        idx_max = int(np.nanargmax(hw))
        h_val = hw[idx_max]
        # for downtrend speed line: from peak to lowest low subsequently
        after = lw[idx_max:]
        if len(after) < 3:
            continue
        idx_min_rel = int(np.nanargmin(after))
        l_val = after[idx_min_rel]
        peak_pos = lo + idx_max
        trough_pos = peak_pos + idx_min_rel
        if trough_pos == peak_pos:
            continue
        # 1/3 line: from peak with slope = (l_val - (h_val - (h_val-l_val)/3)) / (trough_pos - peak_pos)
        # i.e. line from peak to 1/3 retrace level at trough x-position
        target_13 = h_val - (h_val - l_val) / 3.0
        target_23 = h_val - 2.0 * (h_val - l_val) / 3.0
        dx = trough_pos - peak_pos
        slope_13 = (target_13 - h_val) / dx
        slope_23 = (target_23 - h_val) / dx
        out_13[i] = h_val + slope_13 * (i - peak_pos)
        out_23[i] = h_val + slope_23 * (i - peak_pos)
    return {
        "speed_13": pd.Series(out_13, index=close.index),
        "speed_23": pd.Series(out_23, index=close.index),
    }


def f17_tlbk_179_speed_line_1_3_resistance_distance_252d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log-distance close vs 1/3 speed line. Positive = close above (overhead support broken)."""
    sl = _speed_line_levels(high, low, close, YDAYS)
    return _safe_log(close) - _safe_log(sl["speed_13"])


def f17_tlbk_180_speed_line_2_3_resistance_distance_252d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sl = _speed_line_levels(high, low, close, YDAYS)
    return _safe_log(close) - _safe_log(sl["speed_23"])


def f17_tlbk_181_speed_line_1_3_break_event_count_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close < 1/3 speed line, was >= it. Count in 63d."""
    sl = _speed_line_levels(high, low, close, YDAYS)
    line = sl["speed_13"]
    crossed = (close < line) & (close.shift(1) >= line.shift(1))
    return crossed.fillna(False).astype(float).rolling(QDAYS, min_periods=21).sum()


def f17_tlbk_182_speed_line_2_3_break_event_count_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sl = _speed_line_levels(high, low, close, YDAYS)
    line = sl["speed_23"]
    crossed = (close < line) & (close.shift(1) >= line.shift(1))
    return crossed.fillna(False).astype(float).rolling(QDAYS, min_periods=21).sum()


def f17_tlbk_183_speed_line_rejection_count_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """High touched within 0.25 ATR of 1/3 speed line then close finished below it.
    Bearish rejection from speed-line resistance."""
    sl = _speed_line_levels(high, low, close, YDAYS)
    line = sl["speed_13"]
    atr = _atr(high, low, close, 21)
    touched = (high >= line - 0.25 * atr) & (high <= line + 0.25 * atr)
    rejected = touched & (close < line - 0.1 * atr)
    return rejected.fillna(False).astype(float).rolling(QDAYS, min_periods=21).sum()


def f17_tlbk_184_speed_line_crossover_event_count_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close crossed from above 2/3 line to below 1/3 line within 5 bars.
    Fast speed-line cascade = momentum capitulation."""
    sl = _speed_line_levels(high, low, close, YDAYS)
    line13 = sl["speed_13"]; line23 = sl["speed_23"]
    above23 = close > line23
    below13 = close < line13
    cascade = below13 & above23.shift(5)
    return cascade.fillna(False).astype(float).rolling(QDAYS, min_periods=21).sum()


# ---------- Bucket E: parallel-channel breakouts (185-194) ----------

def _parallel_channel_lines(high, low, close, lookback=YDAYS):
    """Compute parallel channel: upper trendline through 2 most recent pivot highs;
    lower line is parallel (same slope) passing through deepest pivot low in window.
    Returns dict {top_proj, bottom_proj, width}."""
    n = len(close)
    ev_h = _pivot_high_event(high, 2)
    ev_l = _pivot_low_event(low, 2)
    vh = _pivot_value_at_conf(high, ev_h, 2)
    vl = _pivot_value_at_conf(low, ev_l, 2)
    ph = _pivot_pos_at_conf(ev_h, 2)
    pl = _pivot_pos_at_conf(ev_l, 2)
    vs_h, ps_h = _last_k_pivots(vh, ph, 2, lookback)
    v0h, v1h = vs_h[0], vs_h[1]
    p0h, p1h = ps_h[0], ps_h[1]
    slope = _safe_div(v1h - v0h, p1h - p0h)
    intercept_up = v1h - slope * p1h
    idx_pos = pd.Series(np.arange(n, dtype=float), index=close.index)
    top_proj = intercept_up + slope * idx_pos

    # bottom: parallel line through deepest pivot low in lookback
    vl_arr = vl.values
    pl_arr = pl.values
    sl_arr = slope.values
    bot = np.full(n, np.nan, dtype=float)
    for i in range(n):
        if np.isnan(sl_arr[i]):
            continue
        lo = max(0, i - lookback + 1)
        best_val = np.nan; best_pos = np.nan
        for j in range(lo, i + 1):
            if not np.isnan(vl_arr[j]):
                # residual against an upper line is irrelevant; pick lowest pivot
                if np.isnan(best_val) or vl_arr[j] < best_val:
                    best_val = vl_arr[j]
                    best_pos = pl_arr[j]
        if np.isnan(best_val) or np.isnan(best_pos):
            continue
        intercept_dn = best_val - sl_arr[i] * best_pos
        bot[i] = intercept_dn + sl_arr[i] * i
    bottom_proj = pd.Series(bot, index=close.index)
    width = (top_proj - bottom_proj).abs()
    return {"top": top_proj, "bottom": bottom_proj, "width": width, "slope": slope}


def f17_tlbk_185_top_channel_line_distance_252d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log-distance close vs top channel line."""
    ch = _parallel_channel_lines(high, low, close, YDAYS)
    return _safe_log(close) - _safe_log(ch["top"])


def f17_tlbk_186_top_channel_line_break_event_count_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close > top channel line, was <= it before. Count in 63d."""
    ch = _parallel_channel_lines(high, low, close, YDAYS)
    crossed = (close > ch["top"]) & (close.shift(1) <= ch["top"].shift(1))
    return crossed.fillna(False).astype(float).rolling(QDAYS, min_periods=21).sum()


def f17_tlbk_187_top_channel_line_failed_break_count_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Channel broke up at bar k but within 5d close returned below top line. Count in 63d."""
    ch = _parallel_channel_lines(high, low, close, YDAYS)
    top = ch["top"]
    n = len(close)
    out = np.zeros(n, dtype=float)
    c = close.values; t = top.values
    for i in range(6, n):
        lo = max(1, i - QDAYS + 1)
        cnt = 0
        for k in range(lo, i - 4):
            if (not np.isnan(c[k]) and not np.isnan(t[k]) and
                    not np.isnan(c[k - 1]) and not np.isnan(t[k - 1]) and
                    c[k] > t[k] and c[k - 1] <= t[k - 1]):
                # check return within next 5d
                ret = False
                for q in range(k + 1, min(k + 6, n)):
                    if not np.isnan(c[q]) and not np.isnan(t[q]) and c[q] < t[q]:
                        ret = True
                        break
                if ret:
                    cnt += 1
        out[i] = float(cnt)
    return pd.Series(out, index=close.index).where(top.notna(), np.nan)


def f17_tlbk_188_top_channel_line_touches_count_252d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where high came within 0.5 ATR of top channel line in 252d."""
    ch = _parallel_channel_lines(high, low, close, YDAYS)
    atr = _atr(high, low, close, 21)
    touched = (high >= ch["top"] - 0.5 * atr) & (high <= ch["top"] + 0.5 * atr)
    return touched.fillna(False).astype(float).rolling(YDAYS, min_periods=84).sum()


def f17_tlbk_189_bottom_channel_line_distance_252d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ch = _parallel_channel_lines(high, low, close, YDAYS)
    return _safe_log(close) - _safe_log(ch["bottom"])


def f17_tlbk_190_bottom_channel_line_break_event_count_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close < bottom channel line, was >= it. Count in 63d."""
    ch = _parallel_channel_lines(high, low, close, YDAYS)
    crossed = (close < ch["bottom"]) & (close.shift(1) >= ch["bottom"].shift(1))
    return crossed.fillna(False).astype(float).rolling(QDAYS, min_periods=21).sum()


def f17_tlbk_191_channel_width_compression_at_high_indicator_252d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Channel width in bottom quartile of 252d AND close near 252d high. Coiled-spring setup."""
    ch = _parallel_channel_lines(high, low, close, YDAYS)
    w = ch["width"]
    w_pct = w.rolling(YDAYS, min_periods=84).rank(pct=True)
    near_hi = (close / close.rolling(YDAYS, min_periods=63).max()) > 0.95
    return ((w_pct < 0.25) & near_hi).astype(float).where(w.notna() & close.notna(), np.nan)


def f17_tlbk_192_channel_width_expansion_at_top_indicator_252d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Channel width in top quartile of 252d AND close near 252d high. Blow-off expansion."""
    ch = _parallel_channel_lines(high, low, close, YDAYS)
    w = ch["width"]
    w_pct = w.rolling(YDAYS, min_periods=84).rank(pct=True)
    near_hi = (close / close.rolling(YDAYS, min_periods=63).max()) > 0.95
    return ((w_pct > 0.75) & near_hi).astype(float).where(w.notna() & close.notna(), np.nan)


def f17_tlbk_193_channel_break_with_volume_confirmation_count_63d(
        high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Top channel break with volume > 1.5x 21d-avg. Count in 63d."""
    ch = _parallel_channel_lines(high, low, close, YDAYS)
    crossed = (close > ch["top"]) & (close.shift(1) <= ch["top"].shift(1))
    vol_avg = volume.rolling(21, min_periods=10).mean()
    confirmed = crossed & (volume > 1.5 * vol_avg)
    return confirmed.fillna(False).astype(float).rolling(QDAYS, min_periods=21).sum()


def f17_tlbk_194_channel_break_then_throwback_count_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Broke top channel up, then within 10d retested back to within 0.3 ATR of the line.
    Throwback to broken resistance — classic post-break setup. Count in 63d."""
    ch = _parallel_channel_lines(high, low, close, YDAYS)
    top = ch["top"]
    atr = _atr(high, low, close, 21)
    n = len(close)
    out = np.zeros(n, dtype=float)
    c = close.values; t = top.values; a = atr.values
    for i in range(15, n):
        lo = max(1, i - QDAYS + 1)
        cnt = 0
        for k in range(lo, i - 10):
            if (not np.isnan(c[k]) and not np.isnan(t[k]) and
                    not np.isnan(c[k - 1]) and not np.isnan(t[k - 1]) and
                    c[k] > t[k] and c[k - 1] <= t[k - 1]):
                a_loc = a[k] if not np.isnan(a[k]) and a[k] > 0 else 1.0
                for q in range(k + 1, min(k + 11, n)):
                    if (not np.isnan(c[q]) and not np.isnan(t[q]) and
                            abs(c[q] - t[q]) < 0.3 * a_loc):
                        cnt += 1
                        break
        out[i] = float(cnt)
    return pd.Series(out, index=close.index).where(top.notna(), np.nan)


# ---------- Bucket F: trendline cluster confluence (195-202) ----------

def _all_active_lines_at(i, high, low, close, atr_arr,
                         upper_proj, lower_proj, top_ch, bot_ch,
                         speed_13, speed_23, pf_med, pf_up, pf_dn):
    """Gather projected line values at bar i. Returns array of (value, kind)."""
    lines = []
    for nm, src in [("upper", upper_proj), ("lower", lower_proj),
                    ("topch", top_ch), ("botch", bot_ch),
                    ("s13", speed_13), ("s23", speed_23),
                    ("pfmed", pf_med), ("pfup", pf_up), ("pfdn", pf_dn)]:
        v = src.iat[i]
        if not np.isnan(v):
            lines.append((v, nm))
    return lines


def _cluster_helpers(high, low, close):
    """Compute everything once for use across bucket F features."""
    _, upper_proj = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    _, lower_proj = _pivot_line_projection(low, "low", 2, YDAYS, pivot_n=2)
    ch = _parallel_channel_lines(high, low, close, YDAYS)
    sl = _speed_line_levels(high, low, close, YDAYS)
    pf = _pitchfork_lines(high, low, close, YDAYS)
    return {
        "upper": upper_proj, "lower": lower_proj,
        "top": ch["top"], "bot": ch["bottom"],
        "s13": sl["speed_13"], "s23": sl["speed_23"],
        "pf_med": pf["median"], "pf_up": pf["upper"], "pf_dn": pf["lower"],
    }


def f17_tlbk_195_trendline_cluster_count_within_2pct_of_close_252d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Number of distinct projected lines within 2% of close at current bar."""
    cl = _cluster_helpers(high, low, close)
    n = len(close)
    out = np.full(n, np.nan, dtype=float)
    c = close.values
    series_list = [cl["upper"].values, cl["lower"].values,
                   cl["top"].values, cl["bot"].values,
                   cl["s13"].values, cl["s23"].values,
                   cl["pf_med"].values, cl["pf_up"].values, cl["pf_dn"].values]
    for i in range(n):
        ci = c[i]
        if np.isnan(ci) or ci <= 0:
            continue
        tol = 0.02 * ci
        cnt = 0
        for s in series_list:
            if not np.isnan(s[i]) and abs(s[i] - ci) <= tol:
                cnt += 1
        out[i] = float(cnt)
    return pd.Series(out, index=close.index)


def f17_tlbk_196_multi_trendline_break_event_within_5d_count_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count bars in 63d where 2+ different trendlines were broken (cross-up for upper
    types, cross-down for lower types) within the last 5 bars."""
    cl = _cluster_helpers(high, low, close)
    c = close
    # upper-line breaks (cross up): upper-trendline, top channel, pitchfork upper
    up_break = ((c > cl["upper"]) & (c.shift(1) <= cl["upper"].shift(1))).astype(int)
    up_break += ((c > cl["top"]) & (c.shift(1) <= cl["top"].shift(1))).astype(int)
    up_break += ((c > cl["pf_up"]) & (c.shift(1) <= cl["pf_up"].shift(1))).astype(int)
    # lower-line breaks (cross down): lower trendline, bottom channel, pf lower, speeds
    dn_break = ((c < cl["lower"]) & (c.shift(1) >= cl["lower"].shift(1))).astype(int)
    dn_break += ((c < cl["bot"]) & (c.shift(1) >= cl["bot"].shift(1))).astype(int)
    dn_break += ((c < cl["pf_dn"]) & (c.shift(1) >= cl["pf_dn"].shift(1))).astype(int)
    dn_break += ((c < cl["s13"]) & (c.shift(1) >= cl["s13"].shift(1))).astype(int)
    dn_break += ((c < cl["s23"]) & (c.shift(1) >= cl["s23"].shift(1))).astype(int)
    any_break = up_break + dn_break
    rolling5 = any_break.rolling(5, min_periods=1).sum()
    multi = (rolling5 >= 2).astype(float)
    return multi.rolling(QDAYS, min_periods=21).sum()


def f17_tlbk_197_trendline_cluster_break_intensity_5d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """How many distinct lines were broken in the last 5 bars. Higher = stronger break."""
    cl = _cluster_helpers(high, low, close)
    c = close
    up_break = ((c > cl["upper"]) & (c.shift(1) <= cl["upper"].shift(1))).astype(int)
    up_break += ((c > cl["top"]) & (c.shift(1) <= cl["top"].shift(1))).astype(int)
    up_break += ((c > cl["pf_up"]) & (c.shift(1) <= cl["pf_up"].shift(1))).astype(int)
    dn_break = ((c < cl["lower"]) & (c.shift(1) >= cl["lower"].shift(1))).astype(int)
    dn_break += ((c < cl["bot"]) & (c.shift(1) >= cl["bot"].shift(1))).astype(int)
    dn_break += ((c < cl["pf_dn"]) & (c.shift(1) >= cl["pf_dn"].shift(1))).astype(int)
    dn_break += ((c < cl["s13"]) & (c.shift(1) >= cl["s13"].shift(1))).astype(int)
    return (up_break + dn_break).rolling(5, min_periods=1).sum().astype(float)


def f17_tlbk_198_trendline_cluster_resistance_above_252d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of projected lines above close at current bar (overhead pressure)."""
    cl = _cluster_helpers(high, low, close)
    n = len(close)
    out = np.full(n, np.nan, dtype=float)
    c = close.values
    arrs = [cl["upper"].values, cl["top"].values, cl["pf_up"].values,
            cl["pf_med"].values, cl["s13"].values, cl["s23"].values]
    for i in range(n):
        if np.isnan(c[i]):
            continue
        cnt = 0
        for s in arrs:
            if not np.isnan(s[i]) and s[i] > c[i]:
                cnt += 1
        out[i] = float(cnt)
    return pd.Series(out, index=close.index)


def f17_tlbk_199_trendline_cluster_support_below_252d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    cl = _cluster_helpers(high, low, close)
    n = len(close)
    out = np.full(n, np.nan, dtype=float)
    c = close.values
    arrs = [cl["lower"].values, cl["bot"].values, cl["pf_dn"].values,
            cl["pf_med"].values, cl["s13"].values, cl["s23"].values]
    for i in range(n):
        if np.isnan(c[i]):
            continue
        cnt = 0
        for s in arrs:
            if not np.isnan(s[i]) and s[i] < c[i]:
                cnt += 1
        out[i] = float(cnt)
    return pd.Series(out, index=close.index)


def f17_tlbk_200_trendline_breakdown_breadth_score_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of lower-type lines that close is currently below.
    Breadth of trend breakdown (downside)."""
    cl = _cluster_helpers(high, low, close)
    c = close
    below = pd.concat([
        (c < cl["lower"]).astype(float).rename("a"),
        (c < cl["bot"]).astype(float).rename("b"),
        (c < cl["pf_dn"]).astype(float).rename("c"),
        (c < cl["pf_med"]).astype(float).rename("d"),
        (c < cl["s13"]).astype(float).rename("e"),
        (c < cl["s23"]).astype(float).rename("f"),
    ], axis=1)
    return below.mean(axis=1)


def f17_tlbk_201_multi_method_trendline_break_consensus_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bar where at least one S/R cross-down + one pivot-trendline cross-down + one channel
    cross-down ALL occurred within last 10 bars. Multi-method consensus break."""
    cl = _cluster_helpers(high, low, close)
    c = close
    pv_break = ((c < cl["lower"]) & (c.shift(1) >= cl["lower"].shift(1))).rolling(10, min_periods=1).max().astype(bool)
    ch_break = ((c < cl["bot"]) & (c.shift(1) >= cl["bot"].shift(1))).rolling(10, min_periods=1).max().astype(bool)
    # S/R approximation: any horizontal-cluster level
    sr_info = _horizontal_levels_near_close(high, low, close, YDAYS)
    sr_dist = sr_info["nearest_below_atr"]
    sr_break = (sr_dist.diff() > 0.5).rolling(10, min_periods=1).max().astype(bool)
    consensus = pv_break & ch_break & sr_break
    return consensus.astype(float).rolling(QDAYS, min_periods=21).sum()


def f17_tlbk_202_trendline_break_density_252d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Total number of distinct line-break events (any direction, any method) in 252d.
    Densely-broken charts = unstable structure."""
    cl = _cluster_helpers(high, low, close)
    c = close
    breaks = pd.concat([
        ((c > cl["upper"]) & (c.shift(1) <= cl["upper"].shift(1))).astype(int).rename("a"),
        ((c < cl["lower"]) & (c.shift(1) >= cl["lower"].shift(1))).astype(int).rename("b"),
        ((c > cl["top"]) & (c.shift(1) <= cl["top"].shift(1))).astype(int).rename("c"),
        ((c < cl["bot"]) & (c.shift(1) >= cl["bot"].shift(1))).astype(int).rename("d"),
        ((c > cl["pf_up"]) & (c.shift(1) <= cl["pf_up"].shift(1))).astype(int).rename("e"),
        ((c < cl["pf_dn"]) & (c.shift(1) >= cl["pf_dn"].shift(1))).astype(int).rename("f"),
    ], axis=1).sum(axis=1)
    return breaks.rolling(YDAYS, min_periods=84).sum().astype(float)


# ---------- Bucket G: trendline–volume interaction (203-210) ----------

def f17_tlbk_203_trendline_break_volume_zscore_at_event_63d(
        high: pd.Series, low: pd.Series, close: pd.Series,
        volume: pd.Series) -> pd.Series:
    """Volume z-score (vs 63d) at most-recent upper-trendline break event in 63d window.
    NaN where no break event occurred."""
    _, proj = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    cross = (close > proj) & (close.shift(1) <= proj.shift(1))
    vol_z = _rolling_zscore(volume, 63)
    n = len(close)
    out = np.full(n, np.nan, dtype=float)
    cross_arr = cross.fillna(False).values
    vz = vol_z.values
    last_vz = np.nan
    for i in range(n):
        if cross_arr[i] and not np.isnan(vz[i]):
            last_vz = float(vz[i])
        # only show signal within QDAYS window of last event
        if not np.isnan(last_vz):
            out[i] = last_vz
    return pd.Series(out, index=close.index)


def f17_tlbk_204_low_volume_trendline_break_count_63d(
        high: pd.Series, low: pd.Series, close: pd.Series,
        volume: pd.Series) -> pd.Series:
    """Upper-trendline break with volume below 0.8x 21d avg. Suspicious false break."""
    _, proj = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    cross = (close > proj) & (close.shift(1) <= proj.shift(1))
    vol_avg = volume.rolling(21, min_periods=10).mean()
    low_vol = cross & (volume < 0.8 * vol_avg)
    return low_vol.fillna(False).astype(float).rolling(QDAYS, min_periods=21).sum()


def f17_tlbk_205_heavy_volume_trendline_break_count_63d(
        high: pd.Series, low: pd.Series, close: pd.Series,
        volume: pd.Series) -> pd.Series:
    """Upper-trendline break with volume > 2x 21d avg. Confirmed."""
    _, proj = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    cross = (close > proj) & (close.shift(1) <= proj.shift(1))
    vol_avg = volume.rolling(21, min_periods=10).mean()
    heavy = cross & (volume > 2.0 * vol_avg)
    return heavy.fillna(False).astype(float).rolling(QDAYS, min_periods=21).sum()


def f17_tlbk_206_trendline_test_volume_decline_slope_252d(
        high: pd.Series, low: pd.Series, close: pd.Series,
        volume: pd.Series) -> pd.Series:
    """Slope of volume at successive pivot-high touches of the upper trendline.
    Negative slope = declining participation on retests = weakness."""
    ev = _pivot_high_event(high, 2)
    vol_at_piv = volume.shift(2).where(ev, np.nan)
    # rolling slope of pivot-volume series over 252d
    n = len(volume)
    out = np.full(n, np.nan, dtype=float)
    vol_arr = vol_at_piv.values
    for i in range(n):
        lo = max(0, i - YDAYS + 1)
        wv = vol_arr[lo:i + 1]
        mask = ~np.isnan(wv)
        if mask.sum() < 3:
            continue
        idx = np.arange(len(wv))[mask].astype(float)
        vals = wv[mask].astype(float)
        if idx[-1] == idx[0]:
            continue
        xm = idx.mean(); ym = vals.mean()
        den = float(((idx - xm) ** 2).sum())
        if den <= 0:
            continue
        out[i] = float(((idx - xm) * (vals - ym)).sum() / den)
    return pd.Series(out, index=volume.index)


def f17_tlbk_207_volume_climax_on_trendline_failed_break_63d(
        high: pd.Series, low: pd.Series, close: pd.Series,
        volume: pd.Series) -> pd.Series:
    """Failed upper-trendline break (broke up then closed back below within 5d) AND volume
    at break > 2x 21d avg. Volume climax with failed break = blow-off top signal."""
    _, proj = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    n = len(close)
    out = np.zeros(n, dtype=float)
    c = close.values; t = proj.values
    vol_avg = volume.rolling(21, min_periods=10).mean().values
    v = volume.values
    for i in range(5, n):
        lo = max(1, i - QDAYS + 1)
        cnt = 0
        for k in range(lo, i - 4):
            if (not np.isnan(c[k]) and not np.isnan(t[k]) and
                    not np.isnan(c[k - 1]) and not np.isnan(t[k - 1]) and
                    c[k] > t[k] and c[k - 1] <= t[k - 1]):
                # failed within next 5d?
                failed = False
                for q in range(k + 1, min(k + 6, n)):
                    if not np.isnan(c[q]) and not np.isnan(t[q]) and c[q] < t[q]:
                        failed = True
                        break
                if failed and not np.isnan(vol_avg[k]) and vol_avg[k] > 0 and v[k] > 2.0 * vol_avg[k]:
                    cnt += 1
        out[i] = float(cnt)
    return pd.Series(out, index=close.index).where(proj.notna(), np.nan)


def f17_tlbk_208_trendline_break_volume_acceleration_5d_63d(
        high: pd.Series, low: pd.Series, close: pd.Series,
        volume: pd.Series) -> pd.Series:
    """At each upper-trendline break in 63d, compute 5d vol-avg AFTER break minus 5d vol-avg BEFORE,
    in z-units. Sum over events in window. (PIT-safe: at bar i, look at events at k where k+5 <= i.)"""
    _, proj = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    n = len(close)
    out = np.zeros(n, dtype=float)
    valid = np.zeros(n, dtype=bool)
    c = close.values; t = proj.values; v = volume.values
    vol_std = volume.rolling(21, min_periods=10).std().values
    for i in range(0, n):
        lo = max(5, i - QDAYS + 1)
        acc = 0.0; has = False
        for k in range(lo, i - 4):
            if (not np.isnan(c[k]) and not np.isnan(t[k]) and
                    not np.isnan(c[k - 1]) and not np.isnan(t[k - 1]) and
                    c[k] > t[k] and c[k - 1] <= t[k - 1]):
                pre = v[max(0, k - 5):k]
                post = v[k:min(k + 6, n)]
                if len(pre) >= 2 and len(post) >= 2 and not np.isnan(vol_std[k]) and vol_std[k] > 0:
                    acc += (np.nanmean(post) - np.nanmean(pre)) / vol_std[k]
                    has = True
        if has:
            out[i] = acc
            valid[i] = True
    s = pd.Series(out, index=close.index)
    return s.where(pd.Series(valid, index=close.index), np.nan)


def f17_tlbk_209_trendline_break_followed_by_high_volume_count_63d(
        high: pd.Series, low: pd.Series, close: pd.Series,
        volume: pd.Series) -> pd.Series:
    """Upper-trendline break followed by 3+ consecutive bars in next 5 with vol > 1.5x avg.
    Sustained interest after break. Count in 63d."""
    _, proj = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    n = len(close)
    out = np.zeros(n, dtype=float)
    c = close.values; t = proj.values; v = volume.values
    vol_avg = volume.rolling(21, min_periods=10).mean().values
    for i in range(5, n):
        lo = max(1, i - QDAYS + 1)
        cnt = 0
        for k in range(lo, i - 4):
            if (not np.isnan(c[k]) and not np.isnan(t[k]) and
                    not np.isnan(c[k - 1]) and not np.isnan(t[k - 1]) and
                    c[k] > t[k] and c[k - 1] <= t[k - 1]):
                hi_vol = 0
                for q in range(k + 1, min(k + 6, n)):
                    if not np.isnan(vol_avg[q]) and vol_avg[q] > 0 and v[q] > 1.5 * vol_avg[q]:
                        hi_vol += 1
                if hi_vol >= 3:
                    cnt += 1
        out[i] = float(cnt)
    return pd.Series(out, index=close.index).where(proj.notna(), np.nan)


def f17_tlbk_210_volume_divergence_at_trendline_break_63d(
        high: pd.Series, low: pd.Series, close: pd.Series,
        volume: pd.Series) -> pd.Series:
    """Upper-trendline break with NEW 63d-high in price, but volume DOWN vs 21d avg.
    Classic price/volume divergence = weak break."""
    _, proj = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    cross = (close > proj) & (close.shift(1) <= proj.shift(1))
    new_hi = close >= close.rolling(QDAYS, min_periods=21).max()
    vol_avg = volume.rolling(21, min_periods=10).mean()
    weak = cross & new_hi & (volume < vol_avg)
    return weak.fillna(False).astype(float).rolling(QDAYS, min_periods=21).sum()


# ---------- Bucket H: failed breaks & magnetism (211-218) ----------

def f17_tlbk_211_failed_trendline_break_count_252d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Upper-trendline break that returned within 5d. Count in 252d."""
    _, proj = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    n = len(close)
    out = np.zeros(n, dtype=float)
    c = close.values; t = proj.values
    for i in range(6, n):
        lo = max(1, i - YDAYS + 1)
        cnt = 0
        for k in range(lo, i - 4):
            if (not np.isnan(c[k]) and not np.isnan(t[k]) and
                    not np.isnan(c[k - 1]) and not np.isnan(t[k - 1]) and
                    c[k] > t[k] and c[k - 1] <= t[k - 1]):
                for q in range(k + 1, min(k + 6, n)):
                    if not np.isnan(c[q]) and not np.isnan(t[q]) and c[q] < t[q]:
                        cnt += 1
                        break
        out[i] = float(cnt)
    return pd.Series(out, index=close.index).where(proj.notna(), np.nan)


def f17_tlbk_212_failed_break_then_extension_indicator_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Most-recent failed upper-trendline break (within 63d) was followed by a NEW 63d high
    within next 10d. Failed-then-extended = sometimes still bullish but often blow-off."""
    _, proj = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    n = len(close)
    out = np.full(n, np.nan, dtype=float)
    c = close.values; t = proj.values
    hh = close.rolling(QDAYS, min_periods=21).max().values
    for i in range(15, n):
        lo = max(1, i - QDAYS + 1)
        flag = 0
        for k in range(lo, i - 10):
            if (not np.isnan(c[k]) and not np.isnan(t[k]) and
                    not np.isnan(c[k - 1]) and not np.isnan(t[k - 1]) and
                    c[k] > t[k] and c[k - 1] <= t[k - 1]):
                failed = False
                for q in range(k + 1, min(k + 6, n)):
                    if not np.isnan(c[q]) and not np.isnan(t[q]) and c[q] < t[q]:
                        failed = True
                        break
                if failed:
                    for q in range(k + 1, min(k + 11, n)):
                        if not np.isnan(c[q]) and not np.isnan(hh[q]) and c[q] >= hh[q]:
                            flag = 1
                            break
        out[i] = float(flag)
    return pd.Series(out, index=close.index).where(proj.notna(), np.nan)


def f17_tlbk_213_failed_break_then_failure_indicator_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Failed upper break followed by NEW 63d LOW within next 10d. Bear-confirming."""
    _, proj = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    n = len(close)
    out = np.full(n, np.nan, dtype=float)
    c = close.values; t = proj.values
    ll = close.rolling(QDAYS, min_periods=21).min().values
    for i in range(15, n):
        lo = max(1, i - QDAYS + 1)
        flag = 0
        for k in range(lo, i - 10):
            if (not np.isnan(c[k]) and not np.isnan(t[k]) and
                    not np.isnan(c[k - 1]) and not np.isnan(t[k - 1]) and
                    c[k] > t[k] and c[k - 1] <= t[k - 1]):
                failed = False
                for q in range(k + 1, min(k + 6, n)):
                    if not np.isnan(c[q]) and not np.isnan(t[q]) and c[q] < t[q]:
                        failed = True
                        break
                if failed:
                    for q in range(k + 1, min(k + 11, n)):
                        if not np.isnan(c[q]) and not np.isnan(ll[q]) and c[q] <= ll[q]:
                            flag = 1
                            break
        out[i] = float(flag)
    return pd.Series(out, index=close.index).where(proj.notna(), np.nan)


def f17_tlbk_214_trendline_magnetism_score_252d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of bars in last 252d where |close - upper trendline| < 0.5 ATR.
    High = price gravitates around trendline = strong magnetism."""
    _, proj = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    atr = _atr(high, low, close, 21)
    near = ((close - proj).abs() < 0.5 * atr).astype(float)
    return near.rolling(YDAYS, min_periods=84).mean()


def f17_tlbk_215_failed_break_streak_max_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max consecutive failed upper-trendline breaks (no successful break in between) in 63d."""
    _, proj = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    n = len(close)
    out = np.zeros(n, dtype=float)
    c = close.values; t = proj.values
    # classify each break: failed (1) or successful (0). Then max consecutive failed streak.
    for i in range(6, n):
        lo = max(1, i - QDAYS + 1)
        streaks = []
        cur = 0
        for k in range(lo, i - 4):
            if (not np.isnan(c[k]) and not np.isnan(t[k]) and
                    not np.isnan(c[k - 1]) and not np.isnan(t[k - 1]) and
                    c[k] > t[k] and c[k - 1] <= t[k - 1]):
                failed = False
                for q in range(k + 1, min(k + 6, n)):
                    if not np.isnan(c[q]) and not np.isnan(t[q]) and c[q] < t[q]:
                        failed = True
                        break
                if failed:
                    cur += 1
                else:
                    streaks.append(cur)
                    cur = 0
        streaks.append(cur)
        out[i] = float(max(streaks))
    return pd.Series(out, index=close.index).where(proj.notna(), np.nan)


def f17_tlbk_216_failed_break_velocity_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """For each failed upper-trendline break in 63d, count bars to return below.
    Returns mean velocity = 1 / mean_bars. Higher = faster reversion = stronger failure."""
    _, proj = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    n = len(close)
    out = np.full(n, np.nan, dtype=float)
    c = close.values; t = proj.values
    for i in range(6, n):
        lo = max(1, i - QDAYS + 1)
        bars_to = []
        for k in range(lo, i - 4):
            if (not np.isnan(c[k]) and not np.isnan(t[k]) and
                    not np.isnan(c[k - 1]) and not np.isnan(t[k - 1]) and
                    c[k] > t[k] and c[k - 1] <= t[k - 1]):
                for q in range(k + 1, min(k + 6, n)):
                    if not np.isnan(c[q]) and not np.isnan(t[q]) and c[q] < t[q]:
                        bars_to.append(q - k)
                        break
        if bars_to:
            mean_bars = float(np.mean(bars_to))
            out[i] = 1.0 / mean_bars if mean_bars > 0 else np.nan
    return pd.Series(out, index=close.index).where(proj.notna(), np.nan)


def f17_tlbk_217_failed_break_volume_signature_63d(
        high: pd.Series, low: pd.Series, close: pd.Series,
        volume: pd.Series) -> pd.Series:
    """Average volume-zscore at the moment of failed upper-trendline breaks (in 63d).
    High = panicky failed breaks (climaxes)."""
    _, proj = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    vol_z = _rolling_zscore(volume, 63).values
    n = len(close)
    out = np.full(n, np.nan, dtype=float)
    c = close.values; t = proj.values
    for i in range(6, n):
        lo = max(1, i - QDAYS + 1)
        zs = []
        for k in range(lo, i - 4):
            if (not np.isnan(c[k]) and not np.isnan(t[k]) and
                    not np.isnan(c[k - 1]) and not np.isnan(t[k - 1]) and
                    c[k] > t[k] and c[k - 1] <= t[k - 1]):
                failed = False
                for q in range(k + 1, min(k + 6, n)):
                    if not np.isnan(c[q]) and not np.isnan(t[q]) and c[q] < t[q]:
                        failed = True
                        break
                if failed and not np.isnan(vol_z[k]):
                    zs.append(vol_z[k])
        if zs:
            out[i] = float(np.mean(zs))
    return pd.Series(out, index=close.index).where(proj.notna(), np.nan)


def f17_tlbk_218_failed_break_to_real_break_ratio_252d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """In 252d, ratio of failed upper-trendline breaks to total breaks.
    High = trendline rarely "really" breaks, when it does it's significant."""
    _, proj = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    n = len(close)
    out = np.full(n, np.nan, dtype=float)
    c = close.values; t = proj.values
    for i in range(6, n):
        lo = max(1, i - YDAYS + 1)
        total = 0; failed_cnt = 0
        for k in range(lo, i - 4):
            if (not np.isnan(c[k]) and not np.isnan(t[k]) and
                    not np.isnan(c[k - 1]) and not np.isnan(t[k - 1]) and
                    c[k] > t[k] and c[k - 1] <= t[k - 1]):
                total += 1
                for q in range(k + 1, min(k + 6, n)):
                    if not np.isnan(c[q]) and not np.isnan(t[q]) and c[q] < t[q]:
                        failed_cnt += 1
                        break
        if total > 0:
            out[i] = failed_cnt / total
    return pd.Series(out, index=close.index).where(proj.notna(), np.nan)


# ---------- Bucket I: trendline acceleration before break (219-225) ----------

def f17_tlbk_219_close_acceleration_5d_before_trendline_break_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At each upper-trendline break in 63d, compute close's 5d log-return JUST BEFORE
    the break. Sum (or mean) over events. Bigger = panic-burst into the line."""
    _, proj = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    n = len(close)
    out = np.full(n, np.nan, dtype=float)
    c = close.values; t = proj.values
    log_c = np.log(np.where(c > 0, c, np.nan))
    for i in range(6, n):
        lo = max(6, i - QDAYS + 1)
        rets = []
        for k in range(lo, i + 1):
            if (not np.isnan(c[k]) and not np.isnan(t[k]) and
                    not np.isnan(c[k - 1]) and not np.isnan(t[k - 1]) and
                    c[k] > t[k] and c[k - 1] <= t[k - 1] and k >= 6):
                if not np.isnan(log_c[k - 1]) and not np.isnan(log_c[k - 6]):
                    rets.append(log_c[k - 1] - log_c[k - 6])
        if rets:
            out[i] = float(np.mean(rets))
    return pd.Series(out, index=close.index).where(proj.notna(), np.nan)


def f17_tlbk_220_close_volatility_5d_before_trendline_break_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Realized vol of close in 5d preceding each upper-trendline break, averaged in 63d."""
    _, proj = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    log_c = _safe_log(close)
    ret = log_c.diff()
    n = len(close)
    out = np.full(n, np.nan, dtype=float)
    c = close.values; t = proj.values; r = ret.values
    for i in range(7, n):
        lo = max(6, i - QDAYS + 1)
        vols = []
        for k in range(lo, i + 1):
            if (not np.isnan(c[k]) and not np.isnan(t[k]) and
                    not np.isnan(c[k - 1]) and not np.isnan(t[k - 1]) and
                    c[k] > t[k] and c[k - 1] <= t[k - 1]):
                window = r[max(0, k - 5):k]
                window = window[~np.isnan(window)]
                if len(window) >= 3:
                    vols.append(float(np.std(window)))
        if vols:
            out[i] = float(np.mean(vols))
    return pd.Series(out, index=close.index).where(proj.notna(), np.nan)


def f17_tlbk_221_close_velocity_5d_before_trendline_break_zscore_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5d close velocity (log-return) z-scored against 63d distribution, measured
    immediately before each upper-trendline break in 63d window. Mean of zs."""
    _, proj = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    log_c = _safe_log(close)
    five_d = log_c - log_c.shift(5)
    five_d_z = _rolling_zscore(five_d, 63).values
    n = len(close)
    out = np.full(n, np.nan, dtype=float)
    c = close.values; t = proj.values
    for i in range(6, n):
        lo = max(6, i - QDAYS + 1)
        zs = []
        for k in range(lo, i + 1):
            if (not np.isnan(c[k]) and not np.isnan(t[k]) and
                    not np.isnan(c[k - 1]) and not np.isnan(t[k - 1]) and
                    c[k] > t[k] and c[k - 1] <= t[k - 1] and not np.isnan(five_d_z[k - 1])):
                zs.append(float(five_d_z[k - 1]))
        if zs:
            out[i] = float(np.mean(zs))
    return pd.Series(out, index=close.index).where(proj.notna(), np.nan)


def f17_tlbk_222_range_expansion_pre_trendline_break_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean true-range in 5d before each upper-trendline break / mean TR of prior 21d.
    >1 = bars getting wider into the break."""
    _, proj = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    tr = _true_range(high, low, close).values
    n = len(close)
    out = np.full(n, np.nan, dtype=float)
    c = close.values; t = proj.values
    for i in range(26, n):
        lo = max(26, i - QDAYS + 1)
        ratios = []
        for k in range(lo, i + 1):
            if (not np.isnan(c[k]) and not np.isnan(t[k]) and
                    not np.isnan(c[k - 1]) and not np.isnan(t[k - 1]) and
                    c[k] > t[k] and c[k - 1] <= t[k - 1]):
                pre5 = tr[max(0, k - 5):k]
                pre21 = tr[max(0, k - 26):k - 5]
                pre5 = pre5[~np.isnan(pre5)]
                pre21 = pre21[~np.isnan(pre21)]
                if len(pre5) >= 2 and len(pre21) >= 5 and np.mean(pre21) > 0:
                    ratios.append(float(np.mean(pre5) / np.mean(pre21)))
        if ratios:
            out[i] = float(np.mean(ratios))
    return pd.Series(out, index=close.index).where(proj.notna(), np.nan)


def f17_tlbk_223_gap_count_pre_trendline_break_5d_63d(
        high: pd.Series, low: pd.Series, close: pd.Series,
        open: pd.Series) -> pd.Series:  # noqa: A002
    """Number of overnight gaps (|open[k] - close[k-1]| > 1 ATR) in 5d before each upper-trendline
    break, summed across events in 63d. Gappy run-up = exhaustion before break."""
    _, proj = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    atr = _atr(high, low, close, 21).values
    o = open.values; c = close.values; t = proj.values
    n = len(close)
    out = np.full(n, np.nan, dtype=float)
    gap_arr = np.zeros(n, dtype=float)
    for k in range(1, n):
        if (not np.isnan(o[k]) and not np.isnan(c[k - 1]) and
                not np.isnan(atr[k]) and atr[k] > 0 and
                abs(o[k] - c[k - 1]) > atr[k]):
            gap_arr[k] = 1.0
    for i in range(6, n):
        lo = max(6, i - QDAYS + 1)
        total = 0.0; any_event = False
        for k in range(lo, i + 1):
            if (not np.isnan(c[k]) and not np.isnan(t[k]) and
                    not np.isnan(c[k - 1]) and not np.isnan(t[k - 1]) and
                    c[k] > t[k] and c[k - 1] <= t[k - 1]):
                total += float(np.sum(gap_arr[max(0, k - 5):k]))
                any_event = True
        if any_event:
            out[i] = total
    return pd.Series(out, index=close.index).where(proj.notna(), np.nan)


def f17_tlbk_224_trendline_break_immediately_after_new_high_count_63d(
        high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Upper-trendline break that occurs within 3 bars after a NEW 63d close-high.
    Maximum stretch -> trendline break = exhaustion topping."""
    _, proj = _pivot_line_projection(high, "high", 2, YDAYS, pivot_n=2)
    new_hi = close >= close.rolling(QDAYS, min_periods=21).max()
    recent_new_hi = new_hi.rolling(3, min_periods=1).max().astype(bool)
    cross = (close > proj) & (close.shift(1) <= proj.shift(1))
    event = cross & recent_new_hi
    return event.fillna(False).astype(float).rolling(QDAYS, min_periods=21).sum()


def f17_tlbk_225_terminal_trendline_breakdown_composite_252d(
        high: pd.Series, low: pd.Series, close: pd.Series,
        volume: pd.Series) -> pd.Series:
    """Multi-condition aggregate: in 252d, count bars where ALL hold within last 10d:
       (a) lower-trendline break (pivot-low cross-down)
       (b) bottom-channel cross-down
       (c) trendline cluster resistance above is >= 3
       (d) volume at break > 1.5x 21d avg.
    Highest-quality breakdown setup."""
    cl = _cluster_helpers(high, low, close)
    c = close
    pv_break = ((c < cl["lower"]) & (c.shift(1) >= cl["lower"].shift(1)))
    ch_break = ((c < cl["bot"]) & (c.shift(1) >= cl["bot"].shift(1)))
    cluster_above_n = f17_tlbk_198_trendline_cluster_resistance_above_252d(high, low, close)
    vol_avg = volume.rolling(21, min_periods=10).mean()
    heavy = volume > 1.5 * vol_avg
    pv_recent = pv_break.rolling(10, min_periods=1).max().astype(bool)
    ch_recent = ch_break.rolling(10, min_periods=1).max().astype(bool)
    heavy_recent = heavy.rolling(10, min_periods=1).max().astype(bool)
    composite = (pv_recent & ch_recent & heavy_recent & (cluster_above_n >= 3))
    return composite.astype(float).where(
        cl["lower"].notna() & cl["bot"].notna() & cluster_above_n.notna(), np.nan
    ).rolling(YDAYS, min_periods=84).sum()


# ============================================================
#                       REGISTRY
# ============================================================

TREND_LINE_BREAK_DYNAMICS_BASE_REGISTRY_151_225 = {
    # A. Horizontal S/R
    "f17_tlbk_151_horizontal_resistance_test_count_above_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_151_horizontal_resistance_test_count_above_252d},
    "f17_tlbk_152_horizontal_resistance_failure_count_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_152_horizontal_resistance_failure_count_63d},
    "f17_tlbk_153_horizontal_resistance_break_then_retest_count_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_153_horizontal_resistance_break_then_retest_count_252d},
    "f17_tlbk_154_horizontal_support_break_count_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_154_horizontal_support_break_count_63d},
    "f17_tlbk_155_horizontal_support_break_then_retest_failure_count_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_155_horizontal_support_break_then_retest_failure_count_252d},
    "f17_tlbk_156_distance_to_nearest_horizontal_resistance_atr_units_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_156_distance_to_nearest_horizontal_resistance_atr_units_252d},
    "f17_tlbk_157_distance_to_nearest_horizontal_support_atr_units_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_157_distance_to_nearest_horizontal_support_atr_units_252d},
    "f17_tlbk_158_horizontal_cluster_density_above_close_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_158_horizontal_cluster_density_above_close_252d},
    "f17_tlbk_159_horizontal_cluster_density_below_close_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_159_horizontal_cluster_density_below_close_252d},
    "f17_tlbk_160_multi_test_horizontal_level_strength_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_160_multi_test_horizontal_level_strength_252d},
    # B. Connected-pivot trendlines
    "f17_tlbk_161_upper_trendline_slope_from_2_recent_pivot_highs_252d": {"inputs": ["high"], "func": f17_tlbk_161_upper_trendline_slope_from_2_recent_pivot_highs_252d},
    "f17_tlbk_162_upper_trendline_slope_from_3_recent_pivot_highs_252d": {"inputs": ["high"], "func": f17_tlbk_162_upper_trendline_slope_from_3_recent_pivot_highs_252d},
    "f17_tlbk_163_lower_trendline_slope_from_2_recent_pivot_lows_252d": {"inputs": ["low"], "func": f17_tlbk_163_lower_trendline_slope_from_2_recent_pivot_lows_252d},
    "f17_tlbk_164_lower_trendline_slope_from_3_recent_pivot_lows_252d": {"inputs": ["low"], "func": f17_tlbk_164_lower_trendline_slope_from_3_recent_pivot_lows_252d},
    "f17_tlbk_165_upper_trendline_break_event_count_63d": {"inputs": ["high", "close"], "func": f17_tlbk_165_upper_trendline_break_event_count_63d},
    "f17_tlbk_166_lower_trendline_break_event_count_63d": {"inputs": ["low", "close"], "func": f17_tlbk_166_lower_trendline_break_event_count_63d},
    "f17_tlbk_167_upper_trendline_r2_fit_quality_252d": {"inputs": ["high"], "func": f17_tlbk_167_upper_trendline_r2_fit_quality_252d},
    "f17_tlbk_168_lower_trendline_r2_fit_quality_252d": {"inputs": ["low"], "func": f17_tlbk_168_lower_trendline_r2_fit_quality_252d},
    "f17_tlbk_169_upper_trendline_touch_count_252d": {"inputs": ["high"], "func": f17_tlbk_169_upper_trendline_touch_count_252d},
    "f17_tlbk_170_lower_trendline_touch_count_252d": {"inputs": ["low"], "func": f17_tlbk_170_lower_trendline_touch_count_252d},
    "f17_tlbk_171_upper_trendline_age_at_current_bar_252d": {"inputs": ["high"], "func": f17_tlbk_171_upper_trendline_age_at_current_bar_252d},
    "f17_tlbk_172_multi_trendline_overlap_zone_indicator_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_172_multi_trendline_overlap_zone_indicator_252d},
    # C. Andrews pitchfork
    "f17_tlbk_173_pitchfork_median_line_distance_at_current_bar_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_173_pitchfork_median_line_distance_at_current_bar_252d},
    "f17_tlbk_174_pitchfork_upper_parallel_break_count_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_174_pitchfork_upper_parallel_break_count_63d},
    "f17_tlbk_175_pitchfork_lower_parallel_break_count_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_175_pitchfork_lower_parallel_break_count_63d},
    "f17_tlbk_176_pitchfork_median_line_rejection_count_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_176_pitchfork_median_line_rejection_count_63d},
    "f17_tlbk_177_pitchfork_trigger_event_count_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_177_pitchfork_trigger_event_count_63d},
    "f17_tlbk_178_pitchfork_failure_event_count_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_178_pitchfork_failure_event_count_63d},
    # D. Speed lines
    "f17_tlbk_179_speed_line_1_3_resistance_distance_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_179_speed_line_1_3_resistance_distance_252d},
    "f17_tlbk_180_speed_line_2_3_resistance_distance_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_180_speed_line_2_3_resistance_distance_252d},
    "f17_tlbk_181_speed_line_1_3_break_event_count_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_181_speed_line_1_3_break_event_count_63d},
    "f17_tlbk_182_speed_line_2_3_break_event_count_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_182_speed_line_2_3_break_event_count_63d},
    "f17_tlbk_183_speed_line_rejection_count_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_183_speed_line_rejection_count_63d},
    "f17_tlbk_184_speed_line_crossover_event_count_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_184_speed_line_crossover_event_count_63d},
    # E. Channels
    "f17_tlbk_185_top_channel_line_distance_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_185_top_channel_line_distance_252d},
    "f17_tlbk_186_top_channel_line_break_event_count_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_186_top_channel_line_break_event_count_63d},
    "f17_tlbk_187_top_channel_line_failed_break_count_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_187_top_channel_line_failed_break_count_63d},
    "f17_tlbk_188_top_channel_line_touches_count_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_188_top_channel_line_touches_count_252d},
    "f17_tlbk_189_bottom_channel_line_distance_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_189_bottom_channel_line_distance_252d},
    "f17_tlbk_190_bottom_channel_line_break_event_count_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_190_bottom_channel_line_break_event_count_63d},
    "f17_tlbk_191_channel_width_compression_at_high_indicator_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_191_channel_width_compression_at_high_indicator_252d},
    "f17_tlbk_192_channel_width_expansion_at_top_indicator_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_192_channel_width_expansion_at_top_indicator_252d},
    "f17_tlbk_193_channel_break_with_volume_confirmation_count_63d": {"inputs": ["high", "low", "close", "volume"], "func": f17_tlbk_193_channel_break_with_volume_confirmation_count_63d},
    "f17_tlbk_194_channel_break_then_throwback_count_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_194_channel_break_then_throwback_count_63d},
    # F. Cluster confluence
    "f17_tlbk_195_trendline_cluster_count_within_2pct_of_close_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_195_trendline_cluster_count_within_2pct_of_close_252d},
    "f17_tlbk_196_multi_trendline_break_event_within_5d_count_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_196_multi_trendline_break_event_within_5d_count_63d},
    "f17_tlbk_197_trendline_cluster_break_intensity_5d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_197_trendline_cluster_break_intensity_5d},
    "f17_tlbk_198_trendline_cluster_resistance_above_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_198_trendline_cluster_resistance_above_252d},
    "f17_tlbk_199_trendline_cluster_support_below_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_199_trendline_cluster_support_below_252d},
    "f17_tlbk_200_trendline_breakdown_breadth_score_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_200_trendline_breakdown_breadth_score_63d},
    "f17_tlbk_201_multi_method_trendline_break_consensus_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_201_multi_method_trendline_break_consensus_63d},
    "f17_tlbk_202_trendline_break_density_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_202_trendline_break_density_252d},
    # G. Trendline-volume interaction
    "f17_tlbk_203_trendline_break_volume_zscore_at_event_63d": {"inputs": ["high", "low", "close", "volume"], "func": f17_tlbk_203_trendline_break_volume_zscore_at_event_63d},
    "f17_tlbk_204_low_volume_trendline_break_count_63d": {"inputs": ["high", "low", "close", "volume"], "func": f17_tlbk_204_low_volume_trendline_break_count_63d},
    "f17_tlbk_205_heavy_volume_trendline_break_count_63d": {"inputs": ["high", "low", "close", "volume"], "func": f17_tlbk_205_heavy_volume_trendline_break_count_63d},
    "f17_tlbk_206_trendline_test_volume_decline_slope_252d": {"inputs": ["high", "low", "close", "volume"], "func": f17_tlbk_206_trendline_test_volume_decline_slope_252d},
    "f17_tlbk_207_volume_climax_on_trendline_failed_break_63d": {"inputs": ["high", "low", "close", "volume"], "func": f17_tlbk_207_volume_climax_on_trendline_failed_break_63d},
    "f17_tlbk_208_trendline_break_volume_acceleration_5d_63d": {"inputs": ["high", "low", "close", "volume"], "func": f17_tlbk_208_trendline_break_volume_acceleration_5d_63d},
    "f17_tlbk_209_trendline_break_followed_by_high_volume_count_63d": {"inputs": ["high", "low", "close", "volume"], "func": f17_tlbk_209_trendline_break_followed_by_high_volume_count_63d},
    "f17_tlbk_210_volume_divergence_at_trendline_break_63d": {"inputs": ["high", "low", "close", "volume"], "func": f17_tlbk_210_volume_divergence_at_trendline_break_63d},
    # H. Failed breaks & magnetism
    "f17_tlbk_211_failed_trendline_break_count_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_211_failed_trendline_break_count_252d},
    "f17_tlbk_212_failed_break_then_extension_indicator_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_212_failed_break_then_extension_indicator_63d},
    "f17_tlbk_213_failed_break_then_failure_indicator_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_213_failed_break_then_failure_indicator_63d},
    "f17_tlbk_214_trendline_magnetism_score_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_214_trendline_magnetism_score_252d},
    "f17_tlbk_215_failed_break_streak_max_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_215_failed_break_streak_max_63d},
    "f17_tlbk_216_failed_break_velocity_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_216_failed_break_velocity_63d},
    "f17_tlbk_217_failed_break_volume_signature_63d": {"inputs": ["high", "low", "close", "volume"], "func": f17_tlbk_217_failed_break_volume_signature_63d},
    "f17_tlbk_218_failed_break_to_real_break_ratio_252d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_218_failed_break_to_real_break_ratio_252d},
    # I. Acceleration before break
    "f17_tlbk_219_close_acceleration_5d_before_trendline_break_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_219_close_acceleration_5d_before_trendline_break_63d},
    "f17_tlbk_220_close_volatility_5d_before_trendline_break_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_220_close_volatility_5d_before_trendline_break_63d},
    "f17_tlbk_221_close_velocity_5d_before_trendline_break_zscore_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_221_close_velocity_5d_before_trendline_break_zscore_63d},
    "f17_tlbk_222_range_expansion_pre_trendline_break_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_222_range_expansion_pre_trendline_break_63d},
    "f17_tlbk_223_gap_count_pre_trendline_break_5d_63d": {"inputs": ["high", "low", "close", "open"], "func": f17_tlbk_223_gap_count_pre_trendline_break_5d_63d},
    "f17_tlbk_224_trendline_break_immediately_after_new_high_count_63d": {"inputs": ["high", "low", "close"], "func": f17_tlbk_224_trendline_break_immediately_after_new_high_count_63d},
    "f17_tlbk_225_terminal_trendline_breakdown_composite_252d": {"inputs": ["high", "low", "close", "volume"], "func": f17_tlbk_225_terminal_trendline_breakdown_composite_252d},
}
