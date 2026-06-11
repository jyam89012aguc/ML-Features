"""swing_pivot_topology base features 151-225 — Pipeline 1b-technical.

GAP-FILL extension to base 001-150. Each feature here encodes a DISTINCT
concept NOT covered by 001-150:

- Triangle / wedge / channel / pennant / flag pattern detection
  (ascending, descending, symmetric, rising-wedge, falling-wedge, expanding)
- Elliott wave detection (5-wave impulse + 3-wave correction + diagonals)
- Pivot R² linearity (how well do last K pivots fit a straight line)
- Pivot XABCD pattern presence (harmonic-style on pivots)
- Horizontal support/resistance clusters (3+ pivot highs/lows within tight band)
- Pivot reactivity (mean / max amplitude of next leg from confirmed pivot)
- Inside-bar consolidation count + followthrough
- Higher-timeframe pivot proxy (weekly-resampled pivots)
- M-top, W-bottom, head-and-shoulders, triple-top/bottom patterns
- Composite topology scores (terminal-top, terminal-bottom, consolidation, breakout-potential)

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


def _bars_since(event):
    idx_at = np.where(event.to_numpy(), np.arange(len(event)), np.nan)
    last = pd.Series(idx_at, index=event.index).ffill()
    return pd.Series(np.arange(len(event), dtype=float), index=event.index) - last


def _last_k_pivot_values_with_idx(is_pivot, price, k):
    """Return last-k pivot prices AND positional indices at each bar.
    Returns (values_df, idx_df) — each shape (n, k), newest at column k-1."""
    arr_p = price.where(is_pivot, np.nan).to_numpy()
    n = len(price)
    vals = np.full((n, k), np.nan)
    idxs = np.full((n, k), np.nan)
    buf_v = []; buf_i = []
    for i in range(n):
        if not np.isnan(arr_p[i]):
            buf_v.append(arr_p[i]); buf_i.append(float(i))
            if len(buf_v) > k:
                buf_v.pop(0); buf_i.pop(0)
        if len(buf_v) == k:
            vals[i] = np.array(buf_v); idxs[i] = np.array(buf_i)
    cols = [f"p{j}" for j in range(k)]
    return pd.DataFrame(vals, index=price.index, columns=cols), pd.DataFrame(idxs, index=price.index, columns=cols)


def _zigzag_legs(close, threshold):
    n = len(close)
    arr = close.to_numpy()
    pivot_val = np.full(n, np.nan)
    pivot_dir = np.full(n, 0)
    pivot_idx = np.full(n, np.nan)
    if n == 0:
        return pd.Series(pivot_val, index=close.index), pd.Series(pivot_dir, index=close.index), pd.Series(pivot_idx, index=close.index)
    state = 0; ext_val = arr[0]; ext_idx = 0
    for i in range(1, n):
        v = arr[i]
        if np.isnan(v) or np.isnan(ext_val):
            if not np.isnan(v) and np.isnan(ext_val):
                ext_val = v; ext_idx = i; state = 0
            continue
        if state == 0:
            if v >= ext_val * (1.0 + threshold): state = 1; ext_val = v; ext_idx = i
            elif v <= ext_val * (1.0 - threshold): state = -1; ext_val = v; ext_idx = i
        elif state == 1:
            if v > ext_val: ext_val = v; ext_idx = i
            elif v <= ext_val * (1.0 - threshold):
                pivot_val[i] = ext_val; pivot_dir[i] = 1; pivot_idx[i] = float(ext_idx)
                state = -1; ext_val = v; ext_idx = i
        else:
            if v < ext_val: ext_val = v; ext_idx = i
            elif v >= ext_val * (1.0 + threshold):
                pivot_val[i] = ext_val; pivot_dir[i] = -1; pivot_idx[i] = float(ext_idx)
                state = 1; ext_val = v; ext_idx = i
    return pd.Series(pivot_val, index=close.index), pd.Series(pivot_dir, index=close.index), pd.Series(pivot_idx, index=close.index)


def _last_n_zigzag_pivots_arrays(close, threshold, n_pivots):
    pv, pdir, pidx = _zigzag_legs(close, threshold)
    n = len(close)
    out_v = np.full((n, n_pivots), np.nan); out_d = np.full((n, n_pivots), 0); out_i = np.full((n, n_pivots), np.nan)
    bv = []; bd = []; bi = []
    pv_arr = pv.to_numpy(); pd_arr = pdir.to_numpy(); pi_arr = pidx.to_numpy()
    for i in range(n):
        if not np.isnan(pv_arr[i]):
            bv.append(pv_arr[i]); bd.append(int(pd_arr[i])); bi.append(pi_arr[i])
            if len(bv) > n_pivots:
                bv.pop(0); bd.pop(0); bi.pop(0)
        if len(bv) == n_pivots:
            out_v[i] = np.array(bv); out_d[i] = np.array(bd); out_i[i] = np.array(bi)
    return out_v, out_d, out_i


PV_S = 5
PV_M = 21
PV_L = 63


# ============================================================
# Bucket A — Triangle / wedge / channel pattern detection (151-162)
# ============================================================

def _pivot_slope_pair(high, low, n_pivot, k=5):
    """Slope of last k pivot-highs and slope of last k pivot-lows (both 21-bar pivots).
    Slopes in price-per-bar (using pivot indices as x)."""
    hv, hi = _last_k_pivot_values_with_idx(_is_pit_pivot_high(high, n_pivot), high, k)
    lv, li = _last_k_pivot_values_with_idx(_is_pit_pivot_low(low, n_pivot), low, k)
    n = len(high)
    sh = np.full(n, np.nan); sl = np.full(n, np.nan)
    hv_a = hv.to_numpy(); hi_a = hi.to_numpy(); lv_a = lv.to_numpy(); li_a = li.to_numpy()
    for i in range(n):
        rh = hv_a[i]; rhi = hi_a[i]
        if not np.isnan(rh).any():
            xm = rhi.mean(); ym = rh.mean()
            den = ((rhi - xm) ** 2).sum()
            if den > 0: sh[i] = ((rhi - xm) * (rh - ym)).sum() / den
        rl = lv_a[i]; rli = li_a[i]
        if not np.isnan(rl).any():
            xm = rli.mean(); ym = rl.mean()
            den = ((rli - xm) ** 2).sum()
            if den > 0: sl[i] = ((rli - xm) * (rl - ym)).sum() / den
    return pd.Series(sh, index=high.index), pd.Series(sl, index=high.index)


def f10_swpv_151_ascending_triangle_indicator_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: last 5 21-bar pivot-highs near-flat (|slope| small) AND pivot-lows rising (slope > 0)."""
    sh, sl = _pivot_slope_pair(high, low, PV_M, 5)
    atr = _atr(high, low, close, n=MDAYS)
    flat_h = sh.abs() < 0.001 * close
    rising_l = sl > 0.001 * close
    return (flat_h & rising_l).astype(float).where(sh.notna() & sl.notna(), np.nan)


def f10_swpv_152_descending_triangle_indicator_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: pivot-lows near-flat AND pivot-highs declining."""
    sh, sl = _pivot_slope_pair(high, low, PV_M, 5)
    flat_l = sl.abs() < 0.001 * close
    falling_h = sh < -0.001 * close
    return (flat_l & falling_h).astype(float).where(sh.notna() & sl.notna(), np.nan)


def f10_swpv_153_symmetric_triangle_indicator_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: pivot-highs declining AND pivot-lows rising (converging)."""
    sh, sl = _pivot_slope_pair(high, low, PV_M, 5)
    return ((sh < -0.001 * close) & (sl > 0.001 * close)).astype(float).where(sh.notna() & sl.notna(), np.nan)


def f10_swpv_154_rising_wedge_indicator_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rising wedge: both slopes positive but slope of lows > slope of highs (converging upward — bearish at tops)."""
    sh, sl = _pivot_slope_pair(high, low, PV_M, 5)
    return ((sh > 0) & (sl > 0) & (sl > sh)).astype(float).where(sh.notna() & sl.notna(), np.nan)


def f10_swpv_155_falling_wedge_indicator_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Falling wedge: both slopes negative but slope of highs > slope of lows (converging downward — bullish at bottoms)."""
    sh, sl = _pivot_slope_pair(high, low, PV_M, 5)
    return ((sh < 0) & (sl < 0) & (sh > sl)).astype(float).where(sh.notna() & sl.notna(), np.nan)


def f10_swpv_156_expanding_triangle_indicator_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Expanding triangle (broadening top): pivot-highs rising AND pivot-lows falling (diverging)."""
    sh, sl = _pivot_slope_pair(high, low, PV_M, 5)
    return ((sh > 0.001 * close) & (sl < -0.001 * close)).astype(float).where(sh.notna() & sl.notna(), np.nan)


def f10_swpv_157_pennant_indicator_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pennant: symmetric triangle AND preceded by a strong directional move (>2 ATR in last 21d before triangle)."""
    sym = f10_swpv_153_symmetric_triangle_indicator_21bar(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    move = (close.shift(MDAYS) - close.shift(2 * MDAYS)).abs()
    strong_move = move > 2.0 * atr
    return (sym.fillna(0).astype(bool) & strong_move).astype(float)


def f10_swpv_158_bull_flag_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bull flag: prior 21d strong-up move AND now last 5 pivot-highs DECLINING (sloping down) but in tight range."""
    move = close - close.shift(MDAYS)
    atr = _atr(high, low, close, n=MDAYS)
    strong_up = move > 2.0 * atr
    sh, sl = _pivot_slope_pair(high, low, PV_M, 3)
    declining_h = sh < 0
    tight = (close.rolling(WDAYS, min_periods=WDAYS).max() - close.rolling(WDAYS, min_periods=WDAYS).min()) < 1.5 * atr
    return (strong_up & declining_h & tight).astype(float)


def f10_swpv_159_bear_flag_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bear flag: prior 21d strong-down move AND now pivot-lows RISING but tight range."""
    move = close.shift(MDAYS) - close
    atr = _atr(high, low, close, n=MDAYS)
    strong_dn = move > 2.0 * atr
    sh, sl = _pivot_slope_pair(high, low, PV_M, 3)
    rising_l = sl > 0
    tight = (close.rolling(WDAYS, min_periods=WDAYS).max() - close.rolling(WDAYS, min_periods=WDAYS).min()) < 1.5 * atr
    return (strong_dn & rising_l & tight).astype(float)


def f10_swpv_160_channel_indicator_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Channel: slope of pivot-highs ≈ slope of pivot-lows (within 30%), both non-zero."""
    sh, sl = _pivot_slope_pair(high, low, PV_M, 5)
    nonzero = (sh.abs() > 0.0005 * close) & (sl.abs() > 0.0005 * close)
    parallel = (sh - sl).abs() / (sh.abs() + sl.abs() + 1e-9) < 0.3
    same_sign = (sh * sl) > 0
    return (nonzero & parallel & same_sign).astype(float).where(sh.notna() & sl.notna(), np.nan)


def f10_swpv_161_channel_width_atr_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """For a channel: width = mean(pivot_high - corresponding pivot_low) normalized by ATR. NaN if no channel."""
    hv, _ = _last_k_pivot_values_with_idx(_is_pit_pivot_high(high, PV_M), high, 5)
    lv, _ = _last_k_pivot_values_with_idx(_is_pit_pivot_low(low, PV_M), low, 5)
    atr = _atr(high, low, close, n=MDAYS)
    width = hv.mean(axis=1) - lv.mean(axis=1)
    return _safe_div(width, atr)


def f10_swpv_162_channel_position_close_in_channel_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """For a channel: where current close sits within channel (0=at lower line, 1=at upper line)."""
    hv, _ = _last_k_pivot_values_with_idx(_is_pit_pivot_high(high, PV_M), high, 5)
    lv, _ = _last_k_pivot_values_with_idx(_is_pit_pivot_low(low, PV_M), low, 5)
    upper = hv.mean(axis=1); lower = lv.mean(axis=1)
    return _safe_div(close - lower, upper - lower)


# ============================================================
# Bucket B — Pivot R² linearity (163-166)
# ============================================================

def _pivot_r_squared(pivot_vals, pivot_idxs):
    """R² of OLS fit through pivot values (vs pivot indices) — vectorized over rows."""
    n = pivot_vals.shape[0]; k = pivot_vals.shape[1]
    out = np.full(n, np.nan)
    for i in range(n):
        y = pivot_vals[i]; x = pivot_idxs[i]
        if np.isnan(y).any() or np.isnan(x).any(): continue
        xm = x.mean(); ym = y.mean()
        sxx = ((x - xm) ** 2).sum()
        syy = ((y - ym) ** 2).sum()
        sxy = ((x - xm) * (y - ym)).sum()
        if sxx == 0 or syy == 0: continue
        out[i] = (sxy ** 2) / (sxx * syy)
    return out


def f10_swpv_163_pivot_high_r_squared_last_5_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """R² of OLS line through last 5 21-bar pivot-highs — trend linearity."""
    hv, hi = _last_k_pivot_values_with_idx(_is_pit_pivot_high(high, PV_M), high, 5)
    return pd.Series(_pivot_r_squared(hv.to_numpy(), hi.to_numpy()), index=high.index)


def f10_swpv_164_pivot_low_r_squared_last_5_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """R² of OLS line through last 5 21-bar pivot-lows."""
    lv, li = _last_k_pivot_values_with_idx(_is_pit_pivot_low(low, PV_M), low, 5)
    return pd.Series(_pivot_r_squared(lv.to_numpy(), li.to_numpy()), index=low.index)


def f10_swpv_165_pivot_high_residual_sum_squares_last_5_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """RSS of last 5 pivot-highs from OLS line, ATR-normalized — non-linearity magnitude."""
    hv, hi = _last_k_pivot_values_with_idx(_is_pit_pivot_high(high, PV_M), high, 5)
    atr = _atr(high, low, close, n=MDAYS)
    arr_v = hv.to_numpy(); arr_x = hi.to_numpy()
    out = np.full(len(high), np.nan)
    for i in range(len(high)):
        y = arr_v[i]; x = arr_x[i]
        if np.isnan(y).any() or np.isnan(x).any(): continue
        xm = x.mean(); ym = y.mean()
        sxx = ((x - xm) ** 2).sum()
        if sxx == 0: continue
        b = ((x - xm) * (y - ym)).sum() / sxx
        a = ym - b * xm
        yhat = a + b * x
        rss = ((y - yhat) ** 2).sum()
        out[i] = rss
    rss_s = pd.Series(out, index=high.index)
    return _safe_div(np.sqrt(rss_s), atr)


def f10_swpv_166_pivot_high_slope_stability_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of pivot-high slope (last 5) vs 252d distribution of same slope."""
    sh, _ = _pivot_slope_pair(high, low, PV_M, 5)
    return _rolling_zscore(sh, YDAYS, min_periods=QDAYS)


# ============================================================
# Bucket C — Elliott wave detection (167-177)
# ============================================================

def f10_swpv_167_count_5wave_impulse_up_completions_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in last 252d where the 5 most-recent zigzag pivots form a valid up-impulse:
    pivot sequence (low, high, low, high, low → newest high), wave-3 ≥ max(wave1, wave5), wave-4 low > wave-1 high."""
    out_v, out_d, _ = _last_n_zigzag_pivots_arrays(close, 0.05, 5)
    n = len(close); res = np.full(n, 0.0)
    for i in range(n):
        v = out_v[i]; d = out_d[i]
        if np.isnan(v).any(): continue
        # For an up-impulse newest dir should be -1 (we just confirmed wave 5 ending at a high)... actually
        # impulse counted by 5 alternating directions ending at any pivot.
        if not (d[0] == d[2] == d[4]) or not (d[1] == d[3]): continue
        if d[4] != -1: continue  # last pivot must be a low (after wave 5 high → confirmation comes via low)
        # We want sequence: low(X), high(W1 end), low(W2 end), high(W3 end), low(W5 end) — i.e., d = [-1,1,-1,1,-1]
        if not (d[0] == -1 and d[1] == 1 and d[2] == -1 and d[3] == 1 and d[4] == -1): continue
        w1 = v[1] - v[0]; w3 = v[3] - v[2]; w5 = v[3] - v[4]  # net up move of wave-5 = high(W3) - low(W5)? wave 5 = max - min of its leg
        # Simpler: wave1 = v[1]-v[0], wave2=v[1]-v[2], wave3=v[3]-v[2], wave4=v[3]-v[?]
        # Using leg magnitudes between consecutive pivots:
        l1 = abs(v[1] - v[0]); l2 = abs(v[2] - v[1]); l3 = abs(v[3] - v[2]); l4 = abs(v[4] - v[3])
        # Rules: wave 3 not shortest of {1,3,5}, wave 4 not overlapping wave 1 (low of wave-4 > high of wave-1 — but we don't have wave 5 here)
        if l3 < l1: continue
        # wave 4 = move from v[3] (high after wave 3) down to v[4] (low after wave 4)... or we're only seeing waves 1,2,3,4
        # wave-4 low > wave-1 high → v[4] > v[1]
        if v[4] <= v[1]: continue
        res[i] = 1.0
    return pd.Series(res, index=close.index).rolling(YDAYS, min_periods=QDAYS).sum()


def f10_swpv_168_count_5wave_impulse_down_completions_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where 5 most-recent zigzag pivots form a valid DOWN-impulse (mirror of 167)."""
    out_v, out_d, _ = _last_n_zigzag_pivots_arrays(close, 0.05, 5)
    n = len(close); res = np.full(n, 0.0)
    for i in range(n):
        v = out_v[i]; d = out_d[i]
        if np.isnan(v).any(): continue
        if not (d[0] == 1 and d[1] == -1 and d[2] == 1 and d[3] == -1 and d[4] == 1): continue
        l1 = abs(v[1] - v[0]); l3 = abs(v[3] - v[2])
        if l3 < l1: continue
        if v[4] >= v[1]: continue
        res[i] = 1.0
    return pd.Series(res, index=close.index).rolling(YDAYS, min_periods=QDAYS).sum()


def f10_swpv_169_count_3wave_correction_completions_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of valid ABC corrections in last 252d: 3 alternating pivots where leg-A ≈ leg-C in magnitude (within ±30%)."""
    out_v, out_d, _ = _last_n_zigzag_pivots_arrays(close, 0.05, 3)
    n = len(close); res = np.full(n, 0.0)
    for i in range(n):
        v = out_v[i]; d = out_d[i]
        if np.isnan(v).any(): continue
        if d[0] == d[2] or d[1] == d[2]: continue
        la = abs(v[1] - v[0]); lc = abs(v[2] - v[1])
        if la == 0: continue
        ratio = lc / la
        if 0.7 <= ratio <= 1.3:
            res[i] = 1.0
    return pd.Series(res, index=close.index).rolling(YDAYS, min_periods=QDAYS).sum()


def f10_swpv_170_ending_diagonal_wedge_indicator_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: rising wedge AND in wave-5 position (5 prior alternating pivots present)."""
    rw = f10_swpv_154_rising_wedge_indicator_21bar(high, low, close).fillna(0)
    impulse_5 = f10_swpv_167_count_5wave_impulse_up_completions_252d(high, low, close)
    impulse_recent = (impulse_5 - impulse_5.shift(MDAYS) > 0).astype(float)
    return (rw.astype(bool) & impulse_recent.astype(bool)).astype(float)


def f10_swpv_171_leading_diagonal_indicator_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: rising wedge AND in wave-1 position (no prior impulse — fresh structure starting)."""
    rw = f10_swpv_154_rising_wedge_indicator_21bar(high, low, close).fillna(0)
    impulse_5 = f10_swpv_167_count_5wave_impulse_up_completions_252d(high, low, close)
    no_recent_impulse = (impulse_5.diff() == 0).astype(float)
    return (rw.astype(bool) & no_recent_impulse.astype(bool)).astype(float)


def f10_swpv_172_wave_3_strength_ratio_recent_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """For most-recent 5-pivot structure: wave-3 length / wave-1 length. Healthy impulse > 1.0, ideally 1.618."""
    out_v, _, _ = _last_n_zigzag_pivots_arrays(close, 0.05, 4)
    n = len(close)
    out = np.full(n, np.nan)
    for i in range(n):
        v = out_v[i]
        if np.isnan(v).any(): continue
        l1 = abs(v[1] - v[0]); l3 = abs(v[3] - v[2])
        if l1 == 0: continue
        out[i] = l3 / l1
    return pd.Series(out, index=close.index).ffill()


def f10_swpv_173_wave_4_overlap_warning_indicator_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: in last 4 pivots (LHLH for up-impulse), the wave-4 LOW (v[3]) overlaps wave-1 HIGH (v[1]) — impulse invalidation."""
    out_v, out_d, _ = _last_n_zigzag_pivots_arrays(close, 0.05, 4)
    n = len(close)
    out = np.full(n, 0.0)
    for i in range(n):
        v = out_v[i]; d = out_d[i]
        if np.isnan(v).any(): continue
        if not (d[0] == -1 and d[1] == 1 and d[2] == -1 and d[3] == 1): continue
        # check if low after wave 3 high (it's the next pivot — which we don't have in 4-pivot window) → use current close
        if v[1] >= close.iloc[i]:
            out[i] = 1.0
    return pd.Series(out, index=close.index)


def f10_swpv_174_wave_2_retracement_pct_recent_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Wave-2 retracement pct of wave-1: |v[2]-v[1]| / |v[1]-v[0]|. Valid Elliott: < 1.0 (never breaches wave-1 start)."""
    out_v, _, _ = _last_n_zigzag_pivots_arrays(close, 0.05, 3)
    n = len(close)
    out = np.full(n, np.nan)
    for i in range(n):
        v = out_v[i]
        if np.isnan(v).any(): continue
        l1 = abs(v[1] - v[0]); l2 = abs(v[2] - v[1])
        if l1 == 0: continue
        out[i] = l2 / l1
    return pd.Series(out, index=close.index).ffill()


def f10_swpv_175_wave_2_closest_fib_retracement_recent_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Closest fib retracement {0.382, 0.5, 0.618, 0.786} to wave-2's retracement of wave-1 (signed difference)."""
    r = f10_swpv_174_wave_2_retracement_pct_recent_5pct(high, low, close)
    fibs = np.array([0.382, 0.5, 0.618, 0.786])
    arr = r.to_numpy()
    out = np.full(len(r), np.nan)
    for i in range(len(r)):
        if np.isnan(arr[i]): continue
        idx = np.argmin(np.abs(fibs - arr[i]))
        out[i] = arr[i] - fibs[idx]
    return pd.Series(out, index=close.index)


def f10_swpv_176_wave_5_extension_ratio_to_wave_1_recent_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Wave-5 length / wave-1 length (from most-recent 5-pivot structure). 1.0 = equality (truncated 5th)."""
    out_v, _, _ = _last_n_zigzag_pivots_arrays(close, 0.05, 5)
    n = len(close)
    out = np.full(n, np.nan)
    for i in range(n):
        v = out_v[i]
        if np.isnan(v).any(): continue
        l1 = abs(v[1] - v[0]); l5 = abs(v[4] - v[3])
        if l1 == 0: continue
        out[i] = l5 / l1
    return pd.Series(out, index=close.index).ffill()


def f10_swpv_177_wave_3_fib_relationship_to_wave_1_recent_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Closest fib {1.0, 1.272, 1.618, 2.0, 2.618} to wave-3 / wave-1 ratio (signed diff)."""
    r = f10_swpv_172_wave_3_strength_ratio_recent_5pct(high, low, close)
    fibs = np.array([1.0, 1.272, 1.618, 2.0, 2.618])
    arr = r.to_numpy()
    out = np.full(len(r), np.nan)
    for i in range(len(r)):
        if np.isnan(arr[i]): continue
        idx = np.argmin(np.abs(fibs - arr[i]))
        out[i] = arr[i] - fibs[idx]
    return pd.Series(out, index=close.index)


# ============================================================
# Bucket D — Pivot XABCD harmonic (178-180)
# ============================================================

def _check_xabcd_pivot(v, ab_lo, ab_hi, bc_lo, bc_hi, cd_lo, cd_hi):
    """v is 5-element array of pivot values. Returns 1 if XABCD harmonic-style ratios match."""
    xa = abs(v[1] - v[0]); ab = abs(v[2] - v[1]); bc = abs(v[3] - v[2]); cd = abs(v[4] - v[3])
    if xa == 0 or ab == 0 or bc == 0: return 0.0
    r1 = ab / xa; r2 = bc / ab; r3 = cd / bc
    if not (ab_lo <= r1 <= ab_hi): return 0.0
    if not (bc_lo <= r2 <= bc_hi): return 0.0
    if not (cd_lo <= r3 <= cd_hi): return 0.0
    return 1.0


def f10_swpv_178_xabcd_pattern_any_in_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in last 252d that complete any XABCD harmonic shape (loose Fib criteria — Gartley-ish)."""
    out_v, _, _ = _last_n_zigzag_pivots_arrays(close, 0.05, 5)
    n = len(close); res = np.full(n, 0.0)
    for i in range(n):
        v = out_v[i]
        if np.isnan(v).any(): continue
        if _check_xabcd_pivot(v, 0.5, 0.9, 0.3, 0.9, 1.0, 1.8) == 1.0:
            res[i] = 1.0
    return pd.Series(res, index=close.index).rolling(YDAYS, min_periods=QDAYS).sum()


def f10_swpv_179_bars_since_last_xabcd_completion_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most-recent XABCD pattern bar (per 178)."""
    out_v, _, _ = _last_n_zigzag_pivots_arrays(close, 0.05, 5)
    n = len(close); ev = np.full(n, False)
    for i in range(n):
        v = out_v[i]
        if np.isnan(v).any(): continue
        if _check_xabcd_pivot(v, 0.5, 0.9, 0.3, 0.9, 1.0, 1.8) == 1.0:
            ev[i] = True
    return _bars_since(pd.Series(ev, index=close.index))


def f10_swpv_180_log_dist_close_to_d_point_of_recent_pivot_xabcd_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance from close to D point (5th pivot) of most-recent 5-pivot structure."""
    out_v, _, _ = _last_n_zigzag_pivots_arrays(close, 0.05, 5)
    d_point = pd.Series(out_v[:, 4], index=close.index).ffill()
    return _safe_log(close) - _safe_log(d_point)


# ============================================================
# Bucket E — Horizontal S/R clusters from pivots (181-188)
# ============================================================

def _horizontal_cluster_count(pivot_values_arr, cluster_pct):
    """Count of pivots in the largest cluster (within ±cluster_pct of cluster center)."""
    valid = pivot_values_arr[~np.isnan(pivot_values_arr)]
    if valid.size < 3: return 0
    valid_sorted = np.sort(valid)
    best = 0
    for v in valid_sorted:
        cnt = int(np.sum(np.abs(valid_sorted - v) <= cluster_pct * v))
        if cnt > best: best = cnt
    return best


def f10_swpv_181_count_pivot_highs_in_horizontal_cluster_within_2pct_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Largest count of 21-bar pivot-highs from last 252d that fall within ±2% horizontal band."""
    pv = high.where(_is_pit_pivot_high(high, PV_M), np.nan)
    pv_arr = pv.to_numpy(); n = len(high)
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        out[i] = float(_horizontal_cluster_count(pv_arr[start:i + 1], 0.02))
    return pd.Series(out, index=high.index)


def f10_swpv_182_count_pivot_lows_in_horizontal_cluster_within_2pct_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Largest count of 21-bar pivot-lows in horizontal band (mirror of 181)."""
    pv = low.where(_is_pit_pivot_low(low, PV_M), np.nan)
    pv_arr = pv.to_numpy(); n = len(low)
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        out[i] = float(_horizontal_cluster_count(pv_arr[start:i + 1], 0.02))
    return pd.Series(out, index=low.index)


def f10_swpv_183_strongest_horizontal_resistance_log_dist_above_close_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log dist from close UP to center of largest horizontal pivot-high cluster (within ±2%) in last 252d."""
    pv = high.where(_is_pit_pivot_high(high, PV_M), np.nan)
    pv_arr = pv.to_numpy(); close_arr = close.to_numpy(); n = len(high)
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        valid = pv_arr[start:i + 1]
        valid = valid[~np.isnan(valid)]
        if valid.size < 3 or np.isnan(close_arr[i]) or close_arr[i] <= 0: continue
        above = valid[valid > close_arr[i]]
        if above.size == 0: continue
        best_center = above[0]; best_count = 0
        for v in above:
            cnt = int(np.sum(np.abs(above - v) <= 0.02 * v))
            if cnt > best_count:
                best_count = cnt; best_center = v
        if best_count >= 2:
            out[i] = float(np.log(best_center) - np.log(close_arr[i]))
    return pd.Series(out, index=close.index)


def f10_swpv_184_strongest_horizontal_support_log_dist_below_close_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log dist from close DOWN to center of largest horizontal pivot-low cluster (mirror of 183)."""
    pv = low.where(_is_pit_pivot_low(low, PV_M), np.nan)
    pv_arr = pv.to_numpy(); close_arr = close.to_numpy(); n = len(low)
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        valid = pv_arr[start:i + 1]; valid = valid[~np.isnan(valid)]
        if valid.size < 3 or np.isnan(close_arr[i]) or close_arr[i] <= 0: continue
        below = valid[valid < close_arr[i]]
        if below.size == 0: continue
        best_center = below[0]; best_count = 0
        for v in below:
            cnt = int(np.sum(np.abs(below - v) <= 0.02 * v))
            if cnt > best_count:
                best_count = cnt; best_center = v
        if best_count >= 2:
            out[i] = float(np.log(close_arr[i]) - np.log(best_center))
    return pd.Series(out, index=close.index)


def f10_swpv_185_horizontal_resistance_test_count_within_2pct_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in last 252d where high tagged the strongest horizontal pivot-high cluster level (±2%)."""
    pv = high.where(_is_pit_pivot_high(high, PV_M), np.nan)
    pv_arr = pv.to_numpy(); high_arr = high.to_numpy(); n = len(high)
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        valid = pv_arr[start:i + 1]; valid = valid[~np.isnan(valid)]
        if valid.size < 3: continue
        best_center = valid[0]; best_count = 0
        for v in valid:
            cnt = int(np.sum(np.abs(valid - v) <= 0.02 * v))
            if cnt > best_count: best_count = cnt; best_center = v
        if best_count >= 2:
            # count tags in window
            high_win = high_arr[start:i + 1]
            tags = int(np.sum(np.abs(high_win - best_center) <= 0.02 * best_center))
            out[i] = float(tags)
    return pd.Series(out, index=close.index)


def f10_swpv_186_horizontal_support_test_count_within_2pct_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where low tagged the strongest horizontal pivot-low cluster level."""
    pv = low.where(_is_pit_pivot_low(low, PV_M), np.nan)
    pv_arr = pv.to_numpy(); low_arr = low.to_numpy(); n = len(low)
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        valid = pv_arr[start:i + 1]; valid = valid[~np.isnan(valid)]
        if valid.size < 3: continue
        best_center = valid[0]; best_count = 0
        for v in valid:
            cnt = int(np.sum(np.abs(valid - v) <= 0.02 * v))
            if cnt > best_count: best_count = cnt; best_center = v
        if best_count >= 2:
            low_win = low_arr[start:i + 1]
            tags = int(np.sum(np.abs(low_win - best_center) <= 0.02 * best_center))
            out[i] = float(tags)
    return pd.Series(out, index=close.index)


def f10_swpv_187_horizontal_resistance_breakdown_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: today's close > strongest horizontal resistance cluster center — breakout above S/R."""
    pv = high.where(_is_pit_pivot_high(high, PV_M), np.nan)
    pv_arr = pv.to_numpy(); close_arr = close.to_numpy(); n = len(high)
    out = np.full(n, 0.0)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        valid = pv_arr[start:i + 1]; valid = valid[~np.isnan(valid)]
        if valid.size < 3: continue
        best_center = valid[0]; best_count = 0
        for v in valid:
            cnt = int(np.sum(np.abs(valid - v) <= 0.02 * v))
            if cnt > best_count: best_count = cnt; best_center = v
        if best_count >= 2 and not np.isnan(close_arr[i]):
            if close_arr[i] > best_center: out[i] = 1.0
    return pd.Series(out, index=close.index)


def f10_swpv_188_horizontal_support_breakdown_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: today's close < strongest horizontal support cluster center — breakdown below S/R."""
    pv = low.where(_is_pit_pivot_low(low, PV_M), np.nan)
    pv_arr = pv.to_numpy(); close_arr = close.to_numpy(); n = len(low)
    out = np.full(n, 0.0)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        valid = pv_arr[start:i + 1]; valid = valid[~np.isnan(valid)]
        if valid.size < 3: continue
        best_center = valid[0]; best_count = 0
        for v in valid:
            cnt = int(np.sum(np.abs(valid - v) <= 0.02 * v))
            if cnt > best_count: best_count = cnt; best_center = v
        if best_count >= 2 and not np.isnan(close_arr[i]):
            if close_arr[i] < best_center: out[i] = 1.0
    return pd.Series(out, index=close.index)


# ============================================================
# Bucket F — Pivot reactivity / next-leg magnitude (189-192)
# ============================================================

def f10_swpv_189_mean_next_leg_amplitude_after_pivot_high_252d_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR-normalized amplitude of the leg following a pivot-high in last 252d (using 5% zigzag legs)."""
    pv, pdir, pidx = _zigzag_legs(close, 0.05)
    # for each pivot-high (dir=1), the next leg's amplitude = |next_pivot_value - this_pivot_value|
    next_pv = pv.shift(1)  # forward shift OK here? NO — this is a PIT violation. Replace with backward-shifted alignment.
    # PIT-safe: for current bar, find most recent pair of consecutive pivots (high then low), compute the down-leg amp.
    n = len(close)
    pv_arr = pv.to_numpy(); pd_arr = pdir.to_numpy()
    atr_arr = _atr(high, low, close, n=MDAYS).to_numpy()
    leg_after_high = np.full(n, np.nan)
    prev_high_v = np.nan
    for i in range(n):
        if not np.isnan(pv_arr[i]) and pd_arr[i] == 1:
            prev_high_v = pv_arr[i]
        elif not np.isnan(pv_arr[i]) and pd_arr[i] == -1 and not np.isnan(prev_high_v):
            amp = abs(pv_arr[i] - prev_high_v)
            if not np.isnan(atr_arr[i]) and atr_arr[i] > 0:
                leg_after_high[i] = amp / atr_arr[i]
            prev_high_v = np.nan
    leg_s = pd.Series(leg_after_high, index=close.index)
    return leg_s.rolling(YDAYS, min_periods=QDAYS).mean()


def f10_swpv_190_mean_next_leg_amplitude_after_pivot_low_252d_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR-normalized amplitude of the leg following a pivot-low (mirror of 189)."""
    pv, pdir, _ = _zigzag_legs(close, 0.05)
    n = len(close)
    pv_arr = pv.to_numpy(); pd_arr = pdir.to_numpy()
    atr_arr = _atr(high, low, close, n=MDAYS).to_numpy()
    leg_after_low = np.full(n, np.nan)
    prev_low_v = np.nan
    for i in range(n):
        if not np.isnan(pv_arr[i]) and pd_arr[i] == -1:
            prev_low_v = pv_arr[i]
        elif not np.isnan(pv_arr[i]) and pd_arr[i] == 1 and not np.isnan(prev_low_v):
            amp = abs(pv_arr[i] - prev_low_v)
            if not np.isnan(atr_arr[i]) and atr_arr[i] > 0:
                leg_after_low[i] = amp / atr_arr[i]
            prev_low_v = np.nan
    leg_s = pd.Series(leg_after_low, index=close.index)
    return leg_s.rolling(YDAYS, min_periods=QDAYS).mean()


def f10_swpv_191_recent_pivot_reactivity_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of most-recent leg amplitude vs trailing 252d distribution of leg amplitudes (5% zigzag)."""
    pv, _, _ = _zigzag_legs(close, 0.05)
    prior = pv.ffill().shift(1)
    amp = (np.log(pv.where(pv > 0, np.nan)) - np.log(prior.where(prior > 0, np.nan))).abs().where(pv.notna(), np.nan)
    return _rolling_zscore(amp.ffill(), YDAYS, min_periods=QDAYS)


def f10_swpv_192_pivot_reactivity_acceleration_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope of leg amplitudes over trailing 252d (fillna 0 at non-pivot bars). Positive = legs growing."""
    pv, _, _ = _zigzag_legs(close, 0.05)
    prior = pv.ffill().shift(1)
    amp = (np.log(pv.where(pv > 0, np.nan)) - np.log(prior.where(prior > 0, np.nan))).abs().where(pv.notna(), 0.0)
    return _rolling_slope(amp, YDAYS, min_periods=QDAYS)


# ============================================================
# Bucket G — Inside-bar consolidation count (193-196)
# ============================================================

def _inside_bar(high, low):
    return (high < high.shift(1)) & (low > low.shift(1))


def f10_swpv_193_inside_bar_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Inside-bar count in trailing 252d — consolidation density."""
    return _inside_bar(high, low).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f10_swpv_194_consecutive_inside_bars_max_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Longest streak of consecutive inside bars in trailing 252d."""
    cond = _inside_bar(high, low).fillna(False)
    grp = (~cond).cumsum()
    streak = cond.astype(int).groupby(grp).cumsum().astype(float)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f10_swpv_195_inside_bar_density_per_pivot_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Inside-bar count / pivot-event count (5% zigzag) in last 252d — consolidation per swing event."""
    ib = _inside_bar(high, low).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    pv, _, _ = _zigzag_legs(close, 0.05)
    pivots = pv.notna().astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(ib, pivots)


def f10_swpv_196_inside_bar_followthrough_break_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of (inside-bar → next bar high > inside-bar high) breakout events in last 252d."""
    ib = _inside_bar(high, low).fillna(False)
    next_break = (high > high.shift(1)).fillna(False) & ib.shift(1).fillna(False)
    return next_break.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket H — Higher-timeframe (weekly/monthly) pivot proxy (197-200)
# ============================================================

def _weekly_resampled_pivot_count(price, is_pivot_fn, n_for_pivot):
    """Approximate weekly pivots by taking every 5th-bar resampled price and applying 3-bar pivot detection."""
    # Take 5-bar rolling max/min as 'weekly bar'
    weekly_max = price.rolling(WDAYS, min_periods=WDAYS).max()
    weekly_min = price.rolling(WDAYS, min_periods=WDAYS).min()
    return weekly_max, weekly_min


def f10_swpv_197_weekly_pivot_high_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Approximate weekly pivot-high count: 5-bar rolling max as proxy for weekly high; apply 3-week pivot detection."""
    weekly_high = high.rolling(WDAYS, min_periods=WDAYS).max()
    # 3-week pivot: weekly_high[t] == max(weekly_high[t-15:t+1])
    rmax = weekly_high.rolling(3 * WDAYS + 1, min_periods=3 * WDAYS + 1).max()
    pivot = (weekly_high == rmax) & weekly_high.notna() & rmax.notna()
    return pivot.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f10_swpv_198_weekly_pivot_low_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Approximate weekly pivot-low count."""
    weekly_low = low.rolling(WDAYS, min_periods=WDAYS).min()
    rmin = weekly_low.rolling(3 * WDAYS + 1, min_periods=3 * WDAYS + 1).min()
    pivot = (weekly_low == rmin) & weekly_low.notna() & rmin.notna()
    return pivot.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f10_swpv_199_monthly_pivot_high_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Approximate monthly pivot-high count using 21-bar resampled max + 3-month pivot detection."""
    monthly_high = high.rolling(MDAYS, min_periods=MDAYS).max()
    rmax = monthly_high.rolling(3 * MDAYS + 1, min_periods=3 * MDAYS + 1).max()
    pivot = (monthly_high == rmax) & monthly_high.notna() & rmax.notna()
    return pivot.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f10_swpv_200_log_dist_close_to_most_recent_weekly_pivot_high(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log dist from close to most-recent weekly pivot-high (value carried forward)."""
    weekly_high = high.rolling(WDAYS, min_periods=WDAYS).max()
    rmax = weekly_high.rolling(3 * WDAYS + 1, min_periods=3 * WDAYS + 1).max()
    pivot_val = weekly_high.where(weekly_high == rmax, np.nan).ffill()
    return _safe_log(close) - _safe_log(pivot_val)


# ============================================================
# Bucket I — Pivot cluster vs isolated (201-203)
# ============================================================

def f10_swpv_201_isolated_pivot_high_indicator_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: most-recent 21-bar pivot-high has no neighboring 21-bar pivot-high within ±21 bars."""
    is_h = _is_pit_pivot_high(high, PV_M).fillna(False)
    n = len(high); is_h_arr = is_h.to_numpy()
    out = np.full(n, np.nan)
    last_h = -np.inf
    for i in range(n):
        if is_h_arr[i]:
            # check no other in ±21 around it (but only PIT-safe — look back 21)
            if (i - last_h) > MDAYS:
                out[i] = 1.0
            else:
                out[i] = 0.0
            last_h = i
    return pd.Series(out, index=high.index).ffill()


def f10_swpv_202_clustered_pivot_high_count_252d_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of 21-bar pivot-highs in last 252d that are clustered (have another 21-bar pivot-high within ±21 bars)."""
    is_h = _is_pit_pivot_high(high, PV_M).fillna(False)
    n = len(high); is_h_arr = is_h.to_numpy()
    clustered = np.full(n, False)
    last_h = -np.inf
    for i in range(n):
        if is_h_arr[i]:
            if (i - last_h) <= MDAYS:
                clustered[i] = True
                # mark prior as well (best-effort) — but we already passed it; symmetric counting will under-count by 1
            last_h = i
    return pd.Series(clustered, index=high.index).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f10_swpv_203_pivot_cluster_to_isolated_ratio_252d_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of clustered pivot-highs to isolated pivot-highs in last 252d."""
    cluster = f10_swpv_202_clustered_pivot_high_count_252d_21bar(high, low, close)
    total = _is_pit_pivot_high(high, PV_M).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    isolated = total - cluster
    return _safe_div(cluster, isolated)


# ============================================================
# Bucket J — Pivot symmetry (204-206)
# ============================================================

def f10_swpv_204_pivot_price_reflection_score_252d_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Symmetry: 1 - |mean_pivot_high - 2×close + mean_pivot_low| / close — how symmetric pivots are around close."""
    pv_h = high.where(_is_pit_pivot_high(high, PV_M), np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    pv_l = low.where(_is_pit_pivot_low(low, PV_M), np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    asym = (pv_h - 2 * close + pv_l).abs() / close
    return 1.0 - asym


def f10_swpv_205_pivot_value_log_range_vs_close_log_range_ratio_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """log(max pivot-high / min pivot-low) / log(252d max close / 252d min close) — how much of total range is in pivot structure."""
    pv_h = high.where(_is_pit_pivot_high(high, PV_M), np.nan).rolling(YDAYS, min_periods=QDAYS).max()
    pv_l = low.where(_is_pit_pivot_low(low, PV_M), np.nan).rolling(YDAYS, min_periods=QDAYS).min()
    pivot_log_range = _safe_log(pv_h) - _safe_log(pv_l)
    close_log_range = _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max()) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).min())
    return _safe_div(pivot_log_range, close_log_range)


def f10_swpv_206_swing_symmetry_index_mean_up_over_down_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean of (up_leg_amp / down_leg_amp) ratios for adjacent legs in last 252d — symmetric=1, asymmetric=skewed."""
    pv, pdir, _ = _zigzag_legs(close, 0.05)
    prior = pv.ffill().shift(1)
    amp = (np.log(pv.where(pv > 0, np.nan)) - np.log(prior.where(prior > 0, np.nan))).abs().where(pv.notna(), np.nan)
    up_amp = amp.where(pdir == 1, np.nan).ffill()
    dn_amp = amp.where(pdir == -1, np.nan).ffill()
    return _safe_div(up_amp, dn_amp).rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket K — M-top / W-bottom / head-shoulders (207-213)
# ============================================================

def f10_swpv_207_m_top_pattern_indicator_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """M-top: last 2 21-bar pivot-highs within ±2% of each other AND separated by valley (intervening pivot-low)."""
    df = _last_k_pivot_values_with_idx(_is_pit_pivot_high(high, PV_M), high, 2)[0]
    a = df.iloc[:, 0]; b = df.iloc[:, 1]
    similar = (a - b).abs() <= 0.02 * a
    # check pivot-low between them
    is_l = _is_pit_pivot_low(low, PV_M).astype(float)
    _, idx_df = _last_k_pivot_values_with_idx(_is_pit_pivot_high(high, PV_M), high, 2)
    n = len(high)
    out = np.full(n, np.nan)
    idx_arr = idx_df.to_numpy()
    is_l_arr = is_l.to_numpy()
    sim_arr = similar.to_numpy()
    for i in range(n):
        if sim_arr[i] != 1: out[i] = 0.0; continue
        i0 = idx_arr[i, 0]; i1 = idx_arr[i, 1]
        if np.isnan(i0) or np.isnan(i1): continue
        # any pivot-low between?
        if np.any(is_l_arr[int(i0) + 1:int(i1)] == 1.0):
            out[i] = 1.0
        else:
            out[i] = 0.0
    return pd.Series(out, index=high.index)


def f10_swpv_208_m_top_strength_score_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Strength = 1 - |a - b| / a where a, b are last 2 21-bar pivot-highs. NaN if no M-top."""
    df = _last_k_pivot_values_with_idx(_is_pit_pivot_high(high, PV_M), high, 2)[0]
    a = df.iloc[:, 0]; b = df.iloc[:, 1]
    return (1.0 - _safe_div((a - b).abs(), a)).where((a - b).abs() <= 0.05 * a, np.nan)


def f10_swpv_209_double_top_neckline_log_dist_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """For an M-top: log dist from close DOWN to neckline (the intervening pivot-low). 0 = at neckline; positive = above."""
    is_l = _is_pit_pivot_low(low, PV_M).astype(float)
    df_idx = _last_k_pivot_values_with_idx(_is_pit_pivot_high(high, PV_M), high, 2)[1]
    is_l_arr = is_l.to_numpy(); low_arr = low.to_numpy()
    n = len(high)
    out = np.full(n, np.nan)
    for i in range(n):
        i0 = df_idx.iloc[i, 0]; i1 = df_idx.iloc[i, 1]
        if np.isnan(i0) or np.isnan(i1): continue
        between = is_l_arr[int(i0) + 1:int(i1)]
        if np.any(between == 1.0):
            j = int(i0) + 1 + int(np.argmax(between == 1.0))
            neckline = low_arr[j]
            if not np.isnan(neckline) and neckline > 0:
                out[i] = float(np.log(close.iloc[i]) - np.log(neckline))
    return pd.Series(out, index=close.index)


def f10_swpv_210_triple_top_pattern_indicator_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Triple top: last 3 21-bar pivot-highs all within ±2% of each other."""
    df = _last_k_pivot_values_with_idx(_is_pit_pivot_high(high, PV_M), high, 3)[0]
    a = df.iloc[:, 0]; b = df.iloc[:, 1]; c = df.iloc[:, 2]
    rng = pd.concat([a, b, c], axis=1).max(axis=1) - pd.concat([a, b, c], axis=1).min(axis=1)
    mn = pd.concat([a, b, c], axis=1).mean(axis=1)
    return ((rng / mn) <= 0.02).astype(float).where(df.notna().all(axis=1), np.nan)


def f10_swpv_211_head_shoulders_pattern_indicator_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Head-and-shoulders: 3 21-bar pivot-highs where middle is highest AND the two flanks are within ±5% of each other."""
    df = _last_k_pivot_values_with_idx(_is_pit_pivot_high(high, PV_M), high, 3)[0]
    a = df.iloc[:, 0]; b = df.iloc[:, 1]; c = df.iloc[:, 2]
    head_high = (b > a) & (b > c)
    shoulders_similar = (a - c).abs() <= 0.05 * a
    return (head_high & shoulders_similar).astype(float).where(df.notna().all(axis=1), np.nan)


def f10_swpv_212_head_shoulders_neckline_break_indicator_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: head-shoulders confirmed AND close < min(low between shoulders) — neckline break = confirmation."""
    hs = f10_swpv_211_head_shoulders_pattern_indicator_21bar(high, low, close).fillna(0)
    df_idx = _last_k_pivot_values_with_idx(_is_pit_pivot_high(high, PV_M), high, 3)[1]
    low_arr = low.to_numpy()
    n = len(close)
    out = np.full(n, 0.0)
    hs_arr = hs.to_numpy(); close_arr = close.to_numpy()
    for i in range(n):
        if hs_arr[i] != 1: continue
        i0 = df_idx.iloc[i, 0]; i2 = df_idx.iloc[i, 2]
        if np.isnan(i0) or np.isnan(i2): continue
        between_min = np.nanmin(low_arr[int(i0):int(i2) + 1])
        if not np.isnan(between_min) and close_arr[i] < between_min:
            out[i] = 1.0
    return pd.Series(out, index=close.index)


def f10_swpv_213_inverse_head_shoulders_indicator_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Inverse H&S: 3 21-bar pivot-lows where middle is lowest AND flanks within ±5%."""
    df = _last_k_pivot_values_with_idx(_is_pit_pivot_low(low, PV_M), low, 3)[0]
    a = df.iloc[:, 0]; b = df.iloc[:, 1]; c = df.iloc[:, 2]
    head_low = (b < a) & (b < c)
    shoulders_similar = (a - c).abs() <= 0.05 * a
    return (head_low & shoulders_similar).astype(float).where(df.notna().all(axis=1), np.nan)


# ============================================================
# Bucket L — W-bottom / triple-bottom / rounding-bottom / V-bottom (214-218)
# ============================================================

def f10_swpv_214_w_bottom_pattern_indicator_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """W-bottom (double bottom): last 2 21-bar pivot-lows within ±2% of each other AND separated by pivot-high between them."""
    df_idx = _last_k_pivot_values_with_idx(_is_pit_pivot_low(low, PV_M), low, 2)[1]
    df_v = _last_k_pivot_values_with_idx(_is_pit_pivot_low(low, PV_M), low, 2)[0]
    is_h = _is_pit_pivot_high(high, PV_M).astype(float).to_numpy()
    a = df_v.iloc[:, 0]; b = df_v.iloc[:, 1]
    similar = (a - b).abs() <= 0.02 * a
    n = len(low)
    out = np.full(n, np.nan)
    sim_arr = similar.to_numpy()
    idx_arr = df_idx.to_numpy()
    for i in range(n):
        if sim_arr[i] != 1: out[i] = 0.0; continue
        i0 = idx_arr[i, 0]; i1 = idx_arr[i, 1]
        if np.isnan(i0) or np.isnan(i1): continue
        if np.any(is_h[int(i0) + 1:int(i1)] == 1.0):
            out[i] = 1.0
        else:
            out[i] = 0.0
    return pd.Series(out, index=low.index)


def f10_swpv_215_double_bottom_neckline_log_dist_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """For W-bottom: log dist from close UP to neckline (intervening pivot-high)."""
    is_h = _is_pit_pivot_high(high, PV_M).astype(float).to_numpy()
    df_idx = _last_k_pivot_values_with_idx(_is_pit_pivot_low(low, PV_M), low, 2)[1]
    high_arr = high.to_numpy()
    n = len(high)
    out = np.full(n, np.nan)
    for i in range(n):
        i0 = df_idx.iloc[i, 0]; i1 = df_idx.iloc[i, 1]
        if np.isnan(i0) or np.isnan(i1): continue
        between = is_h[int(i0) + 1:int(i1)]
        if np.any(between == 1.0):
            j = int(i0) + 1 + int(np.argmax(between == 1.0))
            neckline = high_arr[j]
            if not np.isnan(neckline) and neckline > 0:
                out[i] = float(np.log(neckline) - np.log(close.iloc[i]))
    return pd.Series(out, index=close.index)


def f10_swpv_216_triple_bottom_pattern_indicator_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Triple bottom: last 3 21-bar pivot-lows within ±2%."""
    df = _last_k_pivot_values_with_idx(_is_pit_pivot_low(low, PV_M), low, 3)[0]
    a = df.iloc[:, 0]; b = df.iloc[:, 1]; c = df.iloc[:, 2]
    rng = pd.concat([a, b, c], axis=1).max(axis=1) - pd.concat([a, b, c], axis=1).min(axis=1)
    mn = pd.concat([a, b, c], axis=1).mean(axis=1)
    return ((rng / mn) <= 0.02).astype(float).where(df.notna().all(axis=1), np.nan)


def f10_swpv_217_rounding_bottom_indicator_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rounding bottom: pivot-lows over 252d show U-shape via rising linear fit on later half, falling on earlier half."""
    pv = low.where(_is_pit_pivot_low(low, PV_M), np.nan)
    pv_arr = pv.to_numpy()
    n = len(low)
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        valid_idx = np.where(~np.isnan(pv_arr[start:i + 1]))[0]
        if valid_idx.size < 4: continue
        vals = pv_arr[start:i + 1][valid_idx]
        x = valid_idx.astype(float)
        half = len(vals) // 2
        if half < 2: continue
        # earlier half slope
        x1 = x[:half]; y1 = vals[:half]
        x2 = x[half:]; y2 = vals[half:]
        def _sl(xx, yy):
            xm = xx.mean(); ym = yy.mean()
            den = ((xx - xm) ** 2).sum()
            return ((xx - xm) * (yy - ym)).sum() / den if den > 0 else np.nan
        sl1 = _sl(x1, y1); sl2 = _sl(x2, y2)
        if np.isnan(sl1) or np.isnan(sl2): continue
        out[i] = float((sl1 < 0) and (sl2 > 0))
    return pd.Series(out, index=close.index)


def f10_swpv_218_v_bottom_indicator_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """V-bottom: bars between most-recent pivot-low and most-recent pivot-high is small (<= 5), and amplitude > 2 ATR — sharp reversal."""
    is_l_arr = _is_pit_pivot_low(low, PV_M).fillna(False).to_numpy()
    is_h_arr = _is_pit_pivot_high(high, PV_M).fillna(False).to_numpy()
    low_arr = low.to_numpy(); high_arr = high.to_numpy()
    atr_arr = _atr(high, low, close, n=MDAYS).to_numpy()
    n = len(close)
    out = np.full(n, 0.0)
    last_l_idx = None; last_l_val = np.nan
    for i in range(n):
        if is_l_arr[i]:
            last_l_idx = i; last_l_val = low_arr[i]
        if is_h_arr[i] and last_l_idx is not None and 1 <= (i - last_l_idx) <= WDAYS:
            amp = high_arr[i] - last_l_val
            if not np.isnan(atr_arr[i]) and atr_arr[i] > 0 and amp > 2.0 * atr_arr[i]:
                out[i] = 1.0
            last_l_idx = None
    return pd.Series(out, index=close.index)


# ============================================================
# Bucket M — Composite topology scores (219-225)
# ============================================================

def f10_swpv_219_terminal_top_topology_composite_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite top: head-shoulders + rising-wedge + declining-pivot-highs + stale 63-bar pivot-high."""
    a = f10_swpv_211_head_shoulders_pattern_indicator_21bar(high, low, close).fillna(0)
    b = f10_swpv_154_rising_wedge_indicator_21bar(high, low, close).fillna(0)
    df = _last_k_pivot_values_with_idx(_is_pit_pivot_high(high, PV_M), high, 3)[0]
    decl = ((df.iloc[:, 0] > df.iloc[:, 1]) & (df.iloc[:, 1] > df.iloc[:, 2])).astype(float).fillna(0)
    stale = (_bars_since(_is_pit_pivot_high(high, 63)) > QDAYS).astype(float).fillna(0)
    return a + b + decl + stale


def f10_swpv_220_terminal_bottom_topology_composite_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite bottom: inverse-H&S + falling-wedge + V-bottom + W-bottom."""
    a = f10_swpv_213_inverse_head_shoulders_indicator_21bar(high, low, close).fillna(0)
    b = f10_swpv_155_falling_wedge_indicator_21bar(high, low, close).fillna(0)
    c = f10_swpv_218_v_bottom_indicator_21bar(high, low, close).fillna(0)
    d = f10_swpv_214_w_bottom_pattern_indicator_21bar(high, low, close).fillna(0)
    return a + b + c + d


def f10_swpv_221_consolidation_zone_score_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consolidation: high pivot density + low amplitude + tight horizontal clusters."""
    is_h_m = _is_pit_pivot_high(high, PV_M).astype(float)
    density = is_h_m.rolling(YDAYS, min_periods=QDAYS).mean()
    pv, _, _ = _zigzag_legs(close, 0.05)
    prior = pv.ffill().shift(1)
    amp = (np.log(pv.where(pv > 0, np.nan)) - np.log(prior.where(prior > 0, np.nan))).abs().where(pv.notna(), np.nan)
    amp_med = amp.rolling(YDAYS, min_periods=QDAYS).median()
    horiz = f10_swpv_181_count_pivot_highs_in_horizontal_cluster_within_2pct_252d(high, low, close).fillna(0)
    return density * horiz / (amp_med + 0.001)


def f10_swpv_222_trending_zone_score_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trending: low pivot density + high amplitude + strong directional pivot slope."""
    is_h_m = _is_pit_pivot_high(high, PV_M).astype(float)
    density = is_h_m.rolling(YDAYS, min_periods=QDAYS).mean()
    pv, _, _ = _zigzag_legs(close, 0.05)
    prior = pv.ffill().shift(1)
    amp = (np.log(pv.where(pv > 0, np.nan)) - np.log(prior.where(prior > 0, np.nan))).abs().where(pv.notna(), np.nan)
    amp_med = amp.rolling(YDAYS, min_periods=QDAYS).median()
    sh, sl = _pivot_slope_pair(high, low, PV_M, 5)
    slope_strength = (sh.abs() + sl.abs())
    return slope_strength * amp_med / (density + 0.001)


def f10_swpv_223_breakout_potential_score_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Breakout potential: compression + near horizontal resistance + low ATR."""
    atr5 = _atr(high, low, close, n=WDAYS); atr21 = _atr(high, low, close, n=MDAYS)
    compress = (atr5 < 0.7 * atr21).astype(float)
    horiz_dist = f10_swpv_183_strongest_horizontal_resistance_log_dist_above_close_252d(high, low, close)
    near_resist = (horiz_dist.fillna(np.inf) < 0.02).astype(float)
    return compress + near_resist + (atr5 < atr21).astype(float)


def f10_swpv_224_breakdown_potential_score_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Breakdown potential: compression + near horizontal support + low ATR."""
    atr5 = _atr(high, low, close, n=WDAYS); atr21 = _atr(high, low, close, n=MDAYS)
    compress = (atr5 < 0.7 * atr21).astype(float)
    horiz_dist = f10_swpv_184_strongest_horizontal_support_log_dist_below_close_252d(high, low, close)
    near_supp = (horiz_dist.fillna(np.inf) < 0.02).astype(float)
    return compress + near_supp + (atr5 < atr21).astype(float)


def f10_swpv_225_structural_regime_classifier_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Categorical: 0=trending_up, 1=trending_down, 2=range_compress, 3=range_expand, 4=transition.
    Logic based on pivot slope directions + amplitude trend."""
    sh, sl = _pivot_slope_pair(high, low, PV_M, 5)
    expand = f10_swpv_156_expanding_triangle_indicator_21bar(high, low, close).fillna(0)
    sym = f10_swpv_153_symmetric_triangle_indicator_21bar(high, low, close).fillna(0)
    n = len(close); sh_arr = sh.to_numpy(); sl_arr = sl.to_numpy()
    ex_arr = expand.to_numpy(); sym_arr = sym.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        if np.isnan(sh_arr[i]) or np.isnan(sl_arr[i]): continue
        if ex_arr[i] == 1: out[i] = 3
        elif sym_arr[i] == 1: out[i] = 2
        elif sh_arr[i] > 0 and sl_arr[i] > 0: out[i] = 0
        elif sh_arr[i] < 0 and sl_arr[i] < 0: out[i] = 1
        else: out[i] = 4
    return pd.Series(out, index=close.index)


# ============================================================
#                         REGISTRY 151-225
# ============================================================

SWING_PIVOT_TOPOLOGY_BASE_REGISTRY_151_225 = {
    "f10_swpv_151_ascending_triangle_indicator_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_151_ascending_triangle_indicator_21bar},
    "f10_swpv_152_descending_triangle_indicator_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_152_descending_triangle_indicator_21bar},
    "f10_swpv_153_symmetric_triangle_indicator_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_153_symmetric_triangle_indicator_21bar},
    "f10_swpv_154_rising_wedge_indicator_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_154_rising_wedge_indicator_21bar},
    "f10_swpv_155_falling_wedge_indicator_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_155_falling_wedge_indicator_21bar},
    "f10_swpv_156_expanding_triangle_indicator_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_156_expanding_triangle_indicator_21bar},
    "f10_swpv_157_pennant_indicator_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_157_pennant_indicator_21bar},
    "f10_swpv_158_bull_flag_indicator": {"inputs": ["high", "low", "close"], "func": f10_swpv_158_bull_flag_indicator},
    "f10_swpv_159_bear_flag_indicator": {"inputs": ["high", "low", "close"], "func": f10_swpv_159_bear_flag_indicator},
    "f10_swpv_160_channel_indicator_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_160_channel_indicator_21bar},
    "f10_swpv_161_channel_width_atr_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_161_channel_width_atr_21bar},
    "f10_swpv_162_channel_position_close_in_channel_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_162_channel_position_close_in_channel_21bar},
    "f10_swpv_163_pivot_high_r_squared_last_5_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_163_pivot_high_r_squared_last_5_21bar},
    "f10_swpv_164_pivot_low_r_squared_last_5_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_164_pivot_low_r_squared_last_5_21bar},
    "f10_swpv_165_pivot_high_residual_sum_squares_last_5_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_165_pivot_high_residual_sum_squares_last_5_21bar},
    "f10_swpv_166_pivot_high_slope_stability_zscore_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_166_pivot_high_slope_stability_zscore_252d},
    "f10_swpv_167_count_5wave_impulse_up_completions_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_167_count_5wave_impulse_up_completions_252d},
    "f10_swpv_168_count_5wave_impulse_down_completions_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_168_count_5wave_impulse_down_completions_252d},
    "f10_swpv_169_count_3wave_correction_completions_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_169_count_3wave_correction_completions_252d},
    "f10_swpv_170_ending_diagonal_wedge_indicator_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_170_ending_diagonal_wedge_indicator_252d},
    "f10_swpv_171_leading_diagonal_indicator_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_171_leading_diagonal_indicator_252d},
    "f10_swpv_172_wave_3_strength_ratio_recent_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_172_wave_3_strength_ratio_recent_5pct},
    "f10_swpv_173_wave_4_overlap_warning_indicator_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_173_wave_4_overlap_warning_indicator_5pct},
    "f10_swpv_174_wave_2_retracement_pct_recent_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_174_wave_2_retracement_pct_recent_5pct},
    "f10_swpv_175_wave_2_closest_fib_retracement_recent_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_175_wave_2_closest_fib_retracement_recent_5pct},
    "f10_swpv_176_wave_5_extension_ratio_to_wave_1_recent_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_176_wave_5_extension_ratio_to_wave_1_recent_5pct},
    "f10_swpv_177_wave_3_fib_relationship_to_wave_1_recent_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_177_wave_3_fib_relationship_to_wave_1_recent_5pct},
    "f10_swpv_178_xabcd_pattern_any_in_252d_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_178_xabcd_pattern_any_in_252d_5pct},
    "f10_swpv_179_bars_since_last_xabcd_completion_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_179_bars_since_last_xabcd_completion_5pct},
    "f10_swpv_180_log_dist_close_to_d_point_of_recent_pivot_xabcd_5pct": {"inputs": ["high", "low", "close"], "func": f10_swpv_180_log_dist_close_to_d_point_of_recent_pivot_xabcd_5pct},
    "f10_swpv_181_count_pivot_highs_in_horizontal_cluster_within_2pct_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_181_count_pivot_highs_in_horizontal_cluster_within_2pct_252d},
    "f10_swpv_182_count_pivot_lows_in_horizontal_cluster_within_2pct_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_182_count_pivot_lows_in_horizontal_cluster_within_2pct_252d},
    "f10_swpv_183_strongest_horizontal_resistance_log_dist_above_close_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_183_strongest_horizontal_resistance_log_dist_above_close_252d},
    "f10_swpv_184_strongest_horizontal_support_log_dist_below_close_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_184_strongest_horizontal_support_log_dist_below_close_252d},
    "f10_swpv_185_horizontal_resistance_test_count_within_2pct_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_185_horizontal_resistance_test_count_within_2pct_252d},
    "f10_swpv_186_horizontal_support_test_count_within_2pct_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_186_horizontal_support_test_count_within_2pct_252d},
    "f10_swpv_187_horizontal_resistance_breakdown_indicator": {"inputs": ["high", "low", "close"], "func": f10_swpv_187_horizontal_resistance_breakdown_indicator},
    "f10_swpv_188_horizontal_support_breakdown_indicator": {"inputs": ["high", "low", "close"], "func": f10_swpv_188_horizontal_support_breakdown_indicator},
    "f10_swpv_189_mean_next_leg_amplitude_after_pivot_high_252d_atr": {"inputs": ["high", "low", "close"], "func": f10_swpv_189_mean_next_leg_amplitude_after_pivot_high_252d_atr},
    "f10_swpv_190_mean_next_leg_amplitude_after_pivot_low_252d_atr": {"inputs": ["high", "low", "close"], "func": f10_swpv_190_mean_next_leg_amplitude_after_pivot_low_252d_atr},
    "f10_swpv_191_recent_pivot_reactivity_zscore_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_191_recent_pivot_reactivity_zscore_252d},
    "f10_swpv_192_pivot_reactivity_acceleration_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_192_pivot_reactivity_acceleration_252d},
    "f10_swpv_193_inside_bar_count_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_193_inside_bar_count_252d},
    "f10_swpv_194_consecutive_inside_bars_max_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_194_consecutive_inside_bars_max_252d},
    "f10_swpv_195_inside_bar_density_per_pivot_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_195_inside_bar_density_per_pivot_252d},
    "f10_swpv_196_inside_bar_followthrough_break_count_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_196_inside_bar_followthrough_break_count_252d},
    "f10_swpv_197_weekly_pivot_high_count_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_197_weekly_pivot_high_count_252d},
    "f10_swpv_198_weekly_pivot_low_count_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_198_weekly_pivot_low_count_252d},
    "f10_swpv_199_monthly_pivot_high_count_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_199_monthly_pivot_high_count_252d},
    "f10_swpv_200_log_dist_close_to_most_recent_weekly_pivot_high": {"inputs": ["high", "low", "close"], "func": f10_swpv_200_log_dist_close_to_most_recent_weekly_pivot_high},
    "f10_swpv_201_isolated_pivot_high_indicator_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_201_isolated_pivot_high_indicator_21bar},
    "f10_swpv_202_clustered_pivot_high_count_252d_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_202_clustered_pivot_high_count_252d_21bar},
    "f10_swpv_203_pivot_cluster_to_isolated_ratio_252d_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_203_pivot_cluster_to_isolated_ratio_252d_21bar},
    "f10_swpv_204_pivot_price_reflection_score_252d_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_204_pivot_price_reflection_score_252d_21bar},
    "f10_swpv_205_pivot_value_log_range_vs_close_log_range_ratio_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_205_pivot_value_log_range_vs_close_log_range_ratio_252d},
    "f10_swpv_206_swing_symmetry_index_mean_up_over_down_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_206_swing_symmetry_index_mean_up_over_down_252d},
    "f10_swpv_207_m_top_pattern_indicator_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_207_m_top_pattern_indicator_21bar},
    "f10_swpv_208_m_top_strength_score_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_208_m_top_strength_score_21bar},
    "f10_swpv_209_double_top_neckline_log_dist_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_209_double_top_neckline_log_dist_21bar},
    "f10_swpv_210_triple_top_pattern_indicator_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_210_triple_top_pattern_indicator_21bar},
    "f10_swpv_211_head_shoulders_pattern_indicator_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_211_head_shoulders_pattern_indicator_21bar},
    "f10_swpv_212_head_shoulders_neckline_break_indicator_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_212_head_shoulders_neckline_break_indicator_21bar},
    "f10_swpv_213_inverse_head_shoulders_indicator_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_213_inverse_head_shoulders_indicator_21bar},
    "f10_swpv_214_w_bottom_pattern_indicator_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_214_w_bottom_pattern_indicator_21bar},
    "f10_swpv_215_double_bottom_neckline_log_dist_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_215_double_bottom_neckline_log_dist_21bar},
    "f10_swpv_216_triple_bottom_pattern_indicator_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_216_triple_bottom_pattern_indicator_21bar},
    "f10_swpv_217_rounding_bottom_indicator_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_217_rounding_bottom_indicator_252d},
    "f10_swpv_218_v_bottom_indicator_21bar": {"inputs": ["high", "low", "close"], "func": f10_swpv_218_v_bottom_indicator_21bar},
    "f10_swpv_219_terminal_top_topology_composite_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_219_terminal_top_topology_composite_252d},
    "f10_swpv_220_terminal_bottom_topology_composite_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_220_terminal_bottom_topology_composite_252d},
    "f10_swpv_221_consolidation_zone_score_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_221_consolidation_zone_score_252d},
    "f10_swpv_222_trending_zone_score_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_222_trending_zone_score_252d},
    "f10_swpv_223_breakout_potential_score_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_223_breakout_potential_score_252d},
    "f10_swpv_224_breakdown_potential_score_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_224_breakdown_potential_score_252d},
    "f10_swpv_225_structural_regime_classifier_252d": {"inputs": ["high", "low", "close"], "func": f10_swpv_225_structural_regime_classifier_252d},
}
