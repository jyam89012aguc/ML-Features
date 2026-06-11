"""15_anchored_vwap_extension d2 features 226-300 — order-2 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
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
    idx = num.index if hasattr(num, 'index') else None
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
        xm = x.mean()
        wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def _expanding_anchor_idx_argmax(metric: pd.Series) -> np.ndarray:
    """For each bar i, return the index j (0..i) where metric[j] is max so far."""
    arr = metric.values.astype(float)
    n = len(arr)
    out = np.full(n, -1, dtype=np.int64)
    cur_max = -np.inf
    cur_idx = -1
    for i in range(n):
        v = arr[i]
        if not np.isnan(v) and v >= cur_max:
            cur_max = v
            cur_idx = i
        out[i] = cur_idx
    return out

def _rolling_anchor_idx_argmax(metric: pd.Series, window: int) -> np.ndarray:
    """For each bar i, return absolute index j in [i-window+1..i] of max metric."""
    arr = metric.values.astype(float)
    n = len(arr)
    out = np.full(n, -1, dtype=np.int64)
    for i in range(n):
        lo = max(0, i - window + 1)
        w = arr[lo:i + 1]
        if np.isnan(w).all():
            continue
        rel = int(np.nanargmax(w))
        out[i] = lo + rel
    return out

def _avwap_from_anchor_idx(price: pd.Series, vol: pd.Series, anchor_idx: np.ndarray) -> pd.Series:
    """Compute anchored VWAP series given per-bar anchor index.
    AVWAP at bar i = sum(price*vol)[anchor:i+1] / sum(vol)[anchor:i+1].
    Uses cumulative sums to keep O(N).
    """
    p = price.values.astype(float)
    v = vol.values.astype(float)
    pv = np.where(np.isfinite(p) & np.isfinite(v), p * v, 0.0)
    vv = np.where(np.isfinite(v), v, 0.0)
    cum_pv = np.concatenate(([0.0], np.cumsum(pv)))
    cum_v = np.concatenate(([0.0], np.cumsum(vv)))
    n = len(p)
    out = np.full(n, np.nan, dtype=float)
    for i in range(n):
        a = anchor_idx[i]
        if a < 0 or a > i:
            continue
        num = cum_pv[i + 1] - cum_pv[a]
        den = cum_v[i + 1] - cum_v[a]
        if den > 0:
            out[i] = num / den
    return pd.Series(out, index=price.index)

def _cum_vol_since_anchor(vol: pd.Series, anchor_idx: np.ndarray) -> pd.Series:
    v = vol.values.astype(float)
    vv = np.where(np.isfinite(v), v, 0.0)
    cum_v = np.concatenate(([0.0], np.cumsum(vv)))
    n = len(v)
    out = np.full(n, np.nan, dtype=float)
    for i in range(n):
        a = anchor_idx[i]
        if a < 0 or a > i:
            continue
        out[i] = cum_v[i + 1] - cum_v[a]
    return pd.Series(out, index=vol.index)

def _cum_dollar_vol_since_anchor(price: pd.Series, vol: pd.Series, anchor_idx: np.ndarray) -> pd.Series:
    p = price.values.astype(float)
    v = vol.values.astype(float)
    dv = np.where(np.isfinite(p) & np.isfinite(v), p * v, 0.0)
    cum_dv = np.concatenate(([0.0], np.cumsum(dv)))
    n = len(p)
    out = np.full(n, np.nan, dtype=float)
    for i in range(n):
        a = anchor_idx[i]
        if a < 0 or a > i:
            continue
        out[i] = cum_dv[i + 1] - cum_dv[a]
    return pd.Series(out, index=price.index)

def _typical(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (high + low + close) / 3.0

def _largest_gap_up_metric(open_: pd.Series, close: pd.Series) -> pd.Series:
    return open_ - close.shift(1)

def _largest_gap_down_metric(open_: pd.Series, close: pd.Series) -> pd.Series:
    return close.shift(1) - open_

def _wyckoff_buying_climax_metric(high, low, close, volume) -> pd.Series:
    """Composite: vol z-score + close-in-lower-third + new 252d high."""
    vol_z = _rolling_zscore(volume, YDAYS, min_periods=QDAYS).fillna(0.0)
    pos = _safe_div(close - low, high - low).fillna(0.5)
    lower_third = (1.0 - pos).clip(lower=0.0)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    new_high = (high >= rmax).astype(float)
    return vol_z + 2.0 * lower_third + 1.5 * new_high

def _wyckoff_selling_climax_metric(high, low, close, volume) -> pd.Series:
    vol_z = _rolling_zscore(volume, YDAYS, min_periods=QDAYS).fillna(0.0)
    pos = _safe_div(close - low, high - low).fillna(0.5)
    upper_third = pos.clip(lower=0.0)
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    new_low = (low <= rmin).astype(float)
    return vol_z + 2.0 * upper_third + 1.5 * new_low

def _largest_1d_return_metric(close: pd.Series) -> pd.Series:
    return close.pct_change().abs()

def _anchor_largest_gap_up_252d(open_, close):
    m = _largest_gap_up_metric(open_, close)
    return _rolling_anchor_idx_argmax(m, YDAYS)

def _anchor_largest_gap_down_252d(open_, close):
    m = _largest_gap_down_metric(open_, close)
    return _rolling_anchor_idx_argmax(m, YDAYS)

def _anchor_largest_1d_return_252d(close):
    m = _largest_1d_return_metric(close)
    return _rolling_anchor_idx_argmax(m, YDAYS)

def _anchor_widest_range_252d(high, low):
    return _rolling_anchor_idx_argmax(high - low, YDAYS)

def _anchor_widest_dollar_vol_252d(close, volume):
    return _rolling_anchor_idx_argmax(close * volume, YDAYS)

def _anchor_lifetime_high(high):
    return _expanding_anchor_idx_argmax(high)

def _anchor_lifetime_low(low):
    neg = -low
    return _expanding_anchor_idx_argmax(neg)

def _anchor_ipo(price):
    n = len(price)
    arr = price.values
    out = np.full(n, -1, dtype=np.int64)
    first = -1
    for i in range(n):
        if first < 0 and (not np.isnan(arr[i])):
            first = i
        out[i] = first
    return out

def _anchor_252d_high(high):
    return _rolling_anchor_idx_argmax(high, YDAYS)

def _anchor_52w_low(low):
    return _rolling_anchor_idx_argmax(-low, YDAYS)

def _anchor_wyckoff_bc_252d(high, low, close, volume):
    m = _wyckoff_buying_climax_metric(high, low, close, volume)
    return _rolling_anchor_idx_argmax(m, YDAYS)

def _anchor_wyckoff_sc_252d(high, low, close, volume):
    m = _wyckoff_selling_climax_metric(high, low, close, volume)
    return _rolling_anchor_idx_argmax(m, YDAYS)

def _anchor_prior_252d_high(high):
    """For each bar i, find the SECOND-most-recent local-252d-high anchor:
    i.e., the prior peak that held 252d-high status before being overtaken.
    Implementation: track the previous index that produced a strict reset.
    """
    arr = high.values
    n = len(arr)
    out = np.full(n, -1, dtype=np.int64)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max().values
    last_anchor = -1
    prev_anchor = -1
    last_max = -np.inf
    for i in range(n):
        v = arr[i]
        if not np.isnan(v) and (not np.isnan(rmax[i])):
            if v >= rmax[i]:
                if last_anchor != i:
                    prev_anchor = last_anchor
                    last_anchor = i
                    last_max = v
        out[i] = prev_anchor
    return out

def _anchor_252d_high_static_global(high):
    """Static argmax of 252d rolling high — same as _anchor_252d_high. Distinct alias."""
    return _anchor_252d_high(high)

def _sigma_band_series(close, vol, anchor_idx, k):
    """Return AVWAP ± k*sigma (sigma = rolling std of close - AVWAP since anchor).
    We use a 63d trailing std of (close - avwap) as a tractable approximation
    of post-anchor residual scale, then build the band.
    """
    av = _avwap_from_anchor_idx(close, vol, anchor_idx)
    resid = close - av
    sd = resid.rolling(QDAYS, min_periods=MDAYS).std()
    upper = av + k * sd
    lower = av - k * sd
    return (av, sd, upper, lower)

def _build_4anchor_avwaps(high, low, close, volume):
    a1 = _anchor_252d_high(high)
    a2 = _anchor_52w_low(low)
    a3 = _anchor_ipo(close)
    a4 = _anchor_wyckoff_bc_252d(high, low, close, volume)
    av1 = _avwap_from_anchor_idx(close, volume, a1)
    av2 = _avwap_from_anchor_idx(close, volume, a2)
    av3 = _avwap_from_anchor_idx(close, volume, a3)
    av4 = _avwap_from_anchor_idx(close, volume, a4)
    return (av1, av2, av3, av4)

def _anchor_post_break_peak(high, close, volume):
    """For each bar i, identify the most recent bar where close lost AVWAP(252d-high)
    (i.e., a 'break' event), and set the anchor to the prior peak bar at the time of break.
    Implementation: each break event sets a new sticky anchor (the bar where the break occurred).
    """
    a_peak = _anchor_252d_high(high)
    av = _avwap_from_anchor_idx(close, volume, a_peak).values
    c = close.values
    n = len(c)
    out = np.full(n, -1, dtype=np.int64)
    cur_anchor = -1
    prev_above = None
    for i in range(n):
        if np.isnan(av[i]) or np.isnan(c[i]):
            out[i] = cur_anchor
            continue
        above = c[i] > av[i]
        if prev_above is True and (not above):
            cur_anchor = i
        prev_above = above
        out[i] = cur_anchor
    return out

def f15_avwx_226_log_dist_close_to_avwap_from_largest_gap_up_252d_d2(open_, high, low, close, volume) -> pd.Series:
    """AVWAP anchored at largest overnight gap-up in trailing 252d (earnings-proxy anchor)."""
    a = _anchor_largest_gap_up_252d(open_, close)
    av = _avwap_from_anchor_idx(close, volume, a)
    return (_safe_log(close) - _safe_log(av)).diff().diff()

def f15_avwx_227_bars_since_largest_gap_up_anchor_252d_d2(open_, close) -> pd.Series:
    """Bars since the 252d-largest gap-up anchor."""
    a = _anchor_largest_gap_up_252d(open_, close)
    n = len(close)
    out = np.array([float(i - a[i]) if a[i] >= 0 else np.nan for i in range(n)])
    return pd.Series(out, index=close.index).diff().diff()

def f15_avwx_228_slope_avwap_from_largest_gap_up_63d_d2(open_, close, volume) -> pd.Series:
    """63d slope of AVWAP anchored at largest gap-up — trajectory of gap-up VWAP."""
    a = _anchor_largest_gap_up_252d(open_, close)
    av = _avwap_from_anchor_idx(close, volume, a)
    return _rolling_slope(av, QDAYS).diff().diff()

def f15_avwx_229_atr_dist_close_to_avwap_from_largest_gap_up_d2(open_, high, low, close, volume) -> pd.Series:
    """ATR-normalized distance close to largest-gap-up AVWAP."""
    a = _anchor_largest_gap_up_252d(open_, close)
    av = _avwap_from_anchor_idx(close, volume, a)
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(close - av, atr).diff().diff()

def f15_avwx_230_log_dist_close_to_avwap_from_prior_252d_high_d2(high, close, volume) -> pd.Series:
    """AVWAP anchored at PRIOR (second-most-recent) 252d-high anchor."""
    a = _anchor_prior_252d_high(high)
    av = _avwap_from_anchor_idx(close, volume, a)
    return (_safe_log(close) - _safe_log(av)).diff().diff()

def f15_avwx_231_bars_since_prior_252d_high_anchor_d2(high) -> pd.Series:
    a = _anchor_prior_252d_high(high)
    n = len(high)
    out = np.array([float(i - a[i]) if a[i] >= 0 else np.nan for i in range(n)])
    return pd.Series(out, index=high.index).diff().diff()

def f15_avwx_232_slope_avwap_from_prior_252d_high_63d_d2(high, close, volume) -> pd.Series:
    a = _anchor_prior_252d_high(high)
    av = _avwap_from_anchor_idx(close, volume, a)
    return _rolling_slope(av, QDAYS).diff().diff()

def f15_avwx_233_log_dist_close_to_avwap_from_lifetime_high_d2(high, close, volume) -> pd.Series:
    """AVWAP anchored at lifetime (expanding) high — secular distribution anchor."""
    a = _anchor_lifetime_high(high)
    av = _avwap_from_anchor_idx(close, volume, a)
    return (_safe_log(close) - _safe_log(av)).diff().diff()

def f15_avwx_234_bars_since_lifetime_high_anchor_d2(high) -> pd.Series:
    a = _anchor_lifetime_high(high)
    n = len(high)
    out = np.array([float(i - a[i]) if a[i] >= 0 else np.nan for i in range(n)])
    return pd.Series(out, index=high.index).diff().diff()

def f15_avwx_235_log_dist_close_to_avwap_from_ipo_bar_d2(close, volume) -> pd.Series:
    """AVWAP anchored at first-known bar — IPO-since accumulated VWAP."""
    a = _anchor_ipo(close)
    av = _avwap_from_anchor_idx(close, volume, a)
    return (_safe_log(close) - _safe_log(av)).diff().diff()

def f15_avwx_236_log_dist_close_to_avwap_from_lifetime_low_d2(low, close, volume) -> pd.Series:
    a = _anchor_lifetime_low(low)
    av = _avwap_from_anchor_idx(close, volume, a)
    return (_safe_log(close) - _safe_log(av)).diff().diff()

def f15_avwx_237_log_dist_close_to_avwap_from_largest_gap_down_252d_d2(open_, close, volume) -> pd.Series:
    a = _anchor_largest_gap_down_252d(open_, close)
    av = _avwap_from_anchor_idx(close, volume, a)
    return (_safe_log(close) - _safe_log(av)).diff().diff()

def f15_avwx_238_bars_since_largest_gap_down_anchor_252d_d2(open_, close) -> pd.Series:
    a = _anchor_largest_gap_down_252d(open_, close)
    n = len(close)
    out = np.array([float(i - a[i]) if a[i] >= 0 else np.nan for i in range(n)])
    return pd.Series(out, index=close.index).diff().diff()

def f15_avwx_239_log_dist_close_to_avwap_from_largest_1d_return_252d_d2(close, volume) -> pd.Series:
    """AVWAP anchored at largest |1d return| bar in trailing 252d."""
    a = _anchor_largest_1d_return_252d(close)
    av = _avwap_from_anchor_idx(close, volume, a)
    return (_safe_log(close) - _safe_log(av)).diff().diff()

def f15_avwx_240_log_dist_close_to_avwap_from_wyckoff_buying_climax_d2(high, low, close, volume) -> pd.Series:
    """AVWAP anchored at Wyckoff BC bar (vol z + lower-third + new 252d high)."""
    a = _anchor_wyckoff_bc_252d(high, low, close, volume)
    av = _avwap_from_anchor_idx(close, volume, a)
    return (_safe_log(close) - _safe_log(av)).diff().diff()

def f15_avwx_241_bars_since_wyckoff_buying_climax_anchor_d2(high, low, close, volume) -> pd.Series:
    a = _anchor_wyckoff_bc_252d(high, low, close, volume)
    n = len(close)
    out = np.array([float(i - a[i]) if a[i] >= 0 else np.nan for i in range(n)])
    return pd.Series(out, index=close.index).diff().diff()

def f15_avwx_242_slope_avwap_from_wyckoff_buying_climax_63d_d2(high, low, close, volume) -> pd.Series:
    a = _anchor_wyckoff_bc_252d(high, low, close, volume)
    av = _avwap_from_anchor_idx(close, volume, a)
    return _rolling_slope(av, QDAYS).diff().diff()

def f15_avwx_243_log_dist_close_to_avwap_from_wyckoff_selling_climax_d2(high, low, close, volume) -> pd.Series:
    """Mirror anchor: AVWAP from Wyckoff SC bar (vol z + upper-third + new 252d low)."""
    a = _anchor_wyckoff_sc_252d(high, low, close, volume)
    av = _avwap_from_anchor_idx(close, volume, a)
    return (_safe_log(close) - _safe_log(av)).diff().diff()

def f15_avwx_244_bars_since_wyckoff_selling_climax_anchor_d2(high, low, close, volume) -> pd.Series:
    a = _anchor_wyckoff_sc_252d(high, low, close, volume)
    n = len(close)
    out = np.array([float(i - a[i]) if a[i] >= 0 else np.nan for i in range(n)])
    return pd.Series(out, index=close.index).diff().diff()

def f15_avwx_245_log_dist_close_to_avwap_from_highest_range_bar_252d_d2(high, low, close, volume) -> pd.Series:
    """AVWAP anchored at widest H-L range bar in trailing 252d."""
    a = _anchor_widest_range_252d(high, low)
    av = _avwap_from_anchor_idx(close, volume, a)
    return (_safe_log(close) - _safe_log(av)).diff().diff()

def f15_avwx_246_log_dist_close_to_avwap_from_widest_dollar_vol_bar_252d_d2(close, volume) -> pd.Series:
    a = _anchor_widest_dollar_vol_252d(close, volume)
    av = _avwap_from_anchor_idx(close, volume, a)
    return (_safe_log(close) - _safe_log(av)).diff().diff()

def f15_avwx_247_failed_reclaim_count_avwap_252dhigh_63d_d2(high, close, volume) -> pd.Series:
    """Count of bars in last 63d where high>=AVWAP(252d-high) but close<AVWAP — failed reclaim attempts."""
    a = _anchor_252d_high(high)
    av = _avwap_from_anchor_idx(close, volume, a)
    failed = ((high >= av) & (close < av)).astype(float)
    return failed.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f15_avwx_248_failed_reclaim_max_wick_avwap_252dhigh_63d_d2(high, close, volume) -> pd.Series:
    """Severity: max wick-over-AVWAP (high - AVWAP) where close<AVWAP, over last 63d."""
    a = _anchor_252d_high(high)
    av = _avwap_from_anchor_idx(close, volume, a)
    wick = (high - av).where((high >= av) & (close < av), np.nan)
    return wick.rolling(QDAYS, min_periods=MDAYS).max().diff().diff()

def f15_avwx_249_bars_since_last_failed_reclaim_avwap_252dhigh_d2(high, close, volume) -> pd.Series:
    """Bars since the most recent failed-reclaim event of AVWAP(252d-high)."""
    a = _anchor_252d_high(high)
    av = _avwap_from_anchor_idx(close, volume, a)
    failed = ((high >= av) & (close < av)).astype(float).values
    n = len(failed)
    out = np.full(n, np.nan, dtype=float)
    last = -1
    for i in range(n):
        if failed[i] > 0:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=high.index).diff().diff()

def f15_avwx_250_failed_reclaim_count_avwap_lifetime_high_252d_d2(high, close, volume) -> pd.Series:
    """Count of failed reclaims of AVWAP(lifetime-high) in trailing 252d."""
    a = _anchor_lifetime_high(high)
    av = _avwap_from_anchor_idx(close, volume, a)
    failed = ((high >= av) & (close < av)).astype(float)
    return failed.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f15_avwx_251_post_break_retest_drawdown_avwap_252dhigh_d2(high, low, close, volume) -> pd.Series:
    """After close<AVWAP(peak), max drawdown from any subsequent peak-retest within 21d.
    Defined as: rolling 21d (close - AVWAP)/AVWAP min when in 'broken' regime.
    """
    a = _anchor_252d_high(high)
    av = _avwap_from_anchor_idx(close, volume, a)
    rel = _safe_div(close - av, av)
    broken = (close < av).astype(float)
    dd = rel.rolling(MDAYS, min_periods=WDAYS).min()
    return dd.where(broken > 0, np.nan).diff().diff()

def f15_avwx_252_days_break_to_retest_avwap_252dhigh_d2(high, close, volume) -> pd.Series:
    """Days between first break (close<AVWAP) and first subsequent retest (high>=AVWAP).
    Reported on every bar since the retest as the recorded gap; NaN before first event pair.
    """
    a = _anchor_252d_high(high)
    av = _avwap_from_anchor_idx(close, volume, a)
    c = close.values
    h = high.values
    v = av.values
    n = len(c)
    out = np.full(n, np.nan, dtype=float)
    state = 0
    break_idx = -1
    recorded = np.nan
    for i in range(n):
        if np.isnan(v[i]):
            out[i] = recorded
            continue
        if state == 0:
            if c[i] < v[i]:
                state = 1
                break_idx = i
        elif state == 1:
            if h[i] >= v[i]:
                recorded = float(i - break_idx)
                state = 2
        out[i] = recorded
    return pd.Series(out, index=close.index).diff().diff()

def f15_avwx_253_indicator_avwap_252dhigh_minus_3sigma_lower_breach_21d_d2(high, close, volume) -> pd.Series:
    """Indicator: any bar in last 21d closed below AVWAP(252d-high) − 3σ band (capitulation)."""
    a = _anchor_252d_high(high)
    av, sd, upper, lower = _sigma_band_series(close, volume, a, k=3.0)
    breach = (close < lower).astype(float)
    cnt = breach.rolling(MDAYS, min_periods=WDAYS).sum()
    return (cnt > 0).astype(float).where(av.notna(), np.nan).diff().diff()

def f15_avwx_254_close_position_in_avwap_252dhigh_3sigma_band_d2(high, close, volume) -> pd.Series:
    """Continuous position of close within ±3σ band of AVWAP(252d-high)."""
    a = _anchor_252d_high(high)
    av, sd, upper, lower = _sigma_band_series(close, volume, a, k=3.0)
    return _safe_div(close - lower, upper - lower).diff().diff()

def f15_avwx_255_touch_count_avwap_252dhigh_upper_2sigma_252d_d2(high, close, volume) -> pd.Series:
    """Count of bars in trailing 252d where high>=AVWAP(252d-high)+2σ (upper-band touches)."""
    a = _anchor_252d_high(high)
    av, sd, upper, lower = _sigma_band_series(close, volume, a, k=2.0)
    touch = (high >= upper).astype(float)
    return touch.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f15_avwx_256_walking_upper_band_peak_avwap_indicator_d2(high, close, volume) -> pd.Series:
    """Indicator: 3+ consecutive bars touching +1σ of peak AVWAP."""
    a = _anchor_252d_high(high)
    av, sd, upper, lower = _sigma_band_series(close, volume, a, k=1.0)
    touch = (high >= upper).astype(float).values
    n = len(touch)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if np.isnan(touch[i]):
            streak = 0
            out[i] = np.nan
        else:
            streak = streak + 1 if touch[i] > 0 else 0
            out[i] = 1.0 if streak >= 3 else 0.0
    return pd.Series(out, index=high.index).diff().diff()

def f15_avwx_257_close_position_in_avwap_ipo_2sigma_band_d2(close, volume) -> pd.Series:
    """Position of close in ±2σ band of AVWAP(IPO)."""
    a = _anchor_ipo(close)
    av, sd, upper, lower = _sigma_band_series(close, volume, a, k=2.0)
    return _safe_div(close - lower, upper - lower).diff().diff()

def f15_avwx_258_count_anchors_with_close_above_3sigma_d2(high, low, close, volume) -> pd.Series:
    """Count of anchors (peak / 52w-low / IPO / climax) where close>=AVWAP+3σ — extension breadth."""
    anchors = [_anchor_252d_high(high), _anchor_52w_low(low), _anchor_ipo(close), _anchor_wyckoff_bc_252d(high, low, close, volume)]
    cnt = pd.Series(0.0, index=close.index)
    for a in anchors:
        av, sd, upper, lower = _sigma_band_series(close, volume, a, k=3.0)
        cnt = cnt + (close >= upper).astype(float).fillna(0.0)
    return cnt.diff().diff()

def f15_avwx_259_count_avwaps_currently_above_close_d2(high, low, close, volume) -> pd.Series:
    """Number of anchor-AVWAPs currently above price (bearish stack)."""
    av1, av2, av3, av4 = _build_4anchor_avwaps(high, low, close, volume)
    df = pd.concat([(av1 > close).rename('a1'), (av2 > close).rename('a2'), (av3 > close).rename('a3'), (av4 > close).rename('a4')], axis=1).astype(float)
    return df.sum(axis=1).diff().diff()

def f15_avwx_260_bars_since_close_above_all_avwaps_simultaneously_d2(high, low, close, volume) -> pd.Series:
    """Bars since the last bar where close was above all 4 anchor AVWAPs simultaneously."""
    av1, av2, av3, av4 = _build_4anchor_avwaps(high, low, close, volume)
    all_above = ((close > av1) & (close > av2) & (close > av3) & (close > av4)).astype(float).values
    n = len(all_above)
    out = np.full(n, np.nan, dtype=float)
    last = -1
    for i in range(n):
        if all_above[i] > 0:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=close.index).diff().diff()

def f15_avwx_261_max_consec_bars_close_below_all_anchors_252d_d2(high, low, close, volume) -> pd.Series:
    """Max consecutive bars (in trailing 252d) where close was below all 4 anchor AVWAPs."""
    av1, av2, av3, av4 = _build_4anchor_avwaps(high, low, close, volume)
    all_below = ((close < av1) & (close < av2) & (close < av3) & (close < av4)).astype(float).values
    n = len(all_below)
    s = pd.Series(all_below, index=close.index)

    def _max_run(w):
        if np.isnan(w).all():
            return np.nan
        best = 0
        cur = 0
        for x in w:
            if x > 0:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    return s.rolling(YDAYS, min_periods=QDAYS).apply(_max_run, raw=True).diff().diff()

def f15_avwx_262_count_anchor_avwap_crosses_by_close_21d_d2(high, low, close, volume) -> pd.Series:
    """Count of any-anchor cross events by close in trailing 21d."""
    av1, av2, av3, av4 = _build_4anchor_avwaps(high, low, close, volume)

    def _crosses(av):
        s = np.sign(close - av).fillna(0.0)
        return (s.diff().abs() > 0).astype(float)
    total = _crosses(av1) + _crosses(av2) + _crosses(av3) + _crosses(av4)
    return total.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f15_avwx_263_anchor_slope_sign_agreement_score_d2(high, low, close, volume) -> pd.Series:
    """Fraction of anchor AVWAPs with negative 21d slope."""
    av1, av2, av3, av4 = _build_4anchor_avwaps(high, low, close, volume)
    s1 = _rolling_slope(av1, MDAYS)
    s2 = _rolling_slope(av2, MDAYS)
    s3 = _rolling_slope(av3, MDAYS)
    s4 = _rolling_slope(av4, MDAYS)
    df = pd.concat([(s1 < 0).rename('s1'), (s2 < 0).rename('s2'), (s3 < 0).rename('s3'), (s4 < 0).rename('s4')], axis=1).astype(float)
    return (df.sum(axis=1) / 4.0).diff().diff()

def f15_avwx_264_bars_since_first_negative_slope_avwap_252dhigh_d2(high, close, volume) -> pd.Series:
    """Bars since AVWAP(252d-high) first showed a negative 21d slope (post-peak)."""
    a = _anchor_252d_high(high)
    av = _avwap_from_anchor_idx(close, volume, a)
    sl = _rolling_slope(av, MDAYS).values
    n = len(sl)
    out = np.full(n, np.nan, dtype=float)
    anchor_seen = -1
    for i in range(n):
        if not np.isnan(sl[i]) and sl[i] < 0 and (anchor_seen < 0):
            anchor_seen = i
        if anchor_seen >= 0:
            out[i] = float(i - anchor_seen)
    return pd.Series(out, index=close.index).diff().diff()

def f15_avwx_265_slope_acceleration_avwap_252dhigh_21d_d2(high, close, volume) -> pd.Series:
    """2nd derivative (curvature) of AVWAP(252d-high) over 21d — diff of 21d slope."""
    a = _anchor_252d_high(high)
    av = _avwap_from_anchor_idx(close, volume, a)
    sl = _rolling_slope(av, MDAYS)
    return sl.diff(MDAYS).diff().diff()

def f15_avwx_266_indicator_peak_avwap_slope_lt_zero_for_21d_d2(high, close, volume) -> pd.Series:
    """Indicator: peak AVWAP slope has been <0 for all 21 of the last 21 bars."""
    a = _anchor_252d_high(high)
    av = _avwap_from_anchor_idx(close, volume, a)
    sl = _rolling_slope(av, MDAYS)
    neg = (sl < 0).astype(float)
    cnt = neg.rolling(MDAYS, min_periods=WDAYS).sum()
    return (cnt >= MDAYS).astype(float).where(sl.notna(), np.nan).diff().diff()

def f15_avwx_267_diff_avwap_252dhigh_minus_avwap_ipo_norm_close_d2(high, close, volume) -> pd.Series:
    """Anchor convergence: (AVWAP_peak − AVWAP_IPO) / close."""
    a1 = _anchor_252d_high(high)
    a2 = _anchor_ipo(close)
    av1 = _avwap_from_anchor_idx(close, volume, a1)
    av2 = _avwap_from_anchor_idx(close, volume, a2)
    return _safe_div(av1 - av2, close).diff().diff()

def f15_avwx_268_diff_avwap_252dhigh_minus_avwap_climax_norm_close_d2(high, low, close, volume) -> pd.Series:
    a1 = _anchor_252d_high(high)
    a2 = _anchor_wyckoff_bc_252d(high, low, close, volume)
    av1 = _avwap_from_anchor_idx(close, volume, a1)
    av2 = _avwap_from_anchor_idx(close, volume, a2)
    return _safe_div(av1 - av2, close).diff().diff()

def f15_avwx_269_diff_avwap_252dhigh_minus_avwap_lifetime_high_norm_close_d2(high, close, volume) -> pd.Series:
    a1 = _anchor_252d_high(high)
    a2 = _anchor_lifetime_high(high)
    av1 = _avwap_from_anchor_idx(close, volume, a1)
    av2 = _avwap_from_anchor_idx(close, volume, a2)
    return _safe_div(av1 - av2, close).diff().diff()

def f15_avwx_270_cross_event_avwap_252dhigh_above_avwap_52wlow_21d_d2(high, low, close, volume) -> pd.Series:
    """Bearish stack inversion: count of bars in last 21d where AVWAP_peak crossed above AVWAP_52wlow."""
    a1 = _anchor_252d_high(high)
    a2 = _anchor_52w_low(low)
    av1 = _avwap_from_anchor_idx(close, volume, a1)
    av2 = _avwap_from_anchor_idx(close, volume, a2)
    s = np.sign(av1 - av2)
    cross = ((s == 1) & (s.shift(1) == -1)).astype(float)
    return cross.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f15_avwx_271_bars_since_cross_avwap_peak_vs_avwap_ipo_d2(high, close, volume) -> pd.Series:
    """Bars since the last cross between AVWAP_peak and AVWAP_IPO."""
    a1 = _anchor_252d_high(high)
    a2 = _anchor_ipo(close)
    av1 = _avwap_from_anchor_idx(close, volume, a1)
    av2 = _avwap_from_anchor_idx(close, volume, a2)
    s = np.sign(av1 - av2)
    cross = (s.diff().abs() > 0).astype(float).values
    n = len(cross)
    out = np.full(n, np.nan, dtype=float)
    last = -1
    for i in range(n):
        if cross[i] > 0:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=close.index).diff().diff()

def f15_avwx_272_count_avwap_avwap_crosses_among_4anchors_252d_d2(high, low, close, volume) -> pd.Series:
    """Pairwise cross events among 4 anchor AVWAPs in trailing 252d (6 pairs)."""
    av1, av2, av3, av4 = _build_4anchor_avwaps(high, low, close, volume)
    pairs = [(av1, av2), (av1, av3), (av1, av4), (av2, av3), (av2, av4), (av3, av4)]
    total = pd.Series(0.0, index=close.index)
    for a, b in pairs:
        s = np.sign(a - b)
        cross = (s.diff().abs() > 0).astype(float).fillna(0.0)
        total = total + cross
    return total.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f15_avwx_273_min_pairwise_dist_among_anchor_avwaps_norm_close_d2(high, low, close, volume) -> pd.Series:
    """Confluence zone: smallest pairwise distance among 4 anchor AVWAPs (normalized by close)."""
    av1, av2, av3, av4 = _build_4anchor_avwaps(high, low, close, volume)
    pairs = [(av1 - av2).abs(), (av1 - av3).abs(), (av1 - av4).abs(), (av2 - av3).abs(), (av2 - av4).abs(), (av3 - av4).abs()]
    df = pd.concat([p.rename(f'p{i}') for i, p in enumerate(pairs)], axis=1)
    mn = df.min(axis=1)
    return _safe_div(mn, close).diff().diff()

def f15_avwx_274_anchor_avwap_convergence_velocity_21d_d2(high, low, close, volume) -> pd.Series:
    """21d slope of min pairwise distance among anchor AVWAPs — convergence/divergence velocity."""
    s = f15_avwx_273_min_pairwise_dist_among_anchor_avwaps_norm_close_d2(high, low, close, volume)
    return _rolling_slope(s, MDAYS).diff().diff()

def f15_avwx_275_frac_bars_close_within_half_atr_avwap_252dhigh_21d_d2(high, low, close, volume) -> pd.Series:
    """Fraction of bars in last 21d with |close − AVWAP(peak)| <= 0.5*ATR — standing-by-AVWAP."""
    a = _anchor_252d_high(high)
    av = _avwap_from_anchor_idx(close, volume, a)
    atr = _atr(high, low, close, n=MDAYS)
    near = ((close - av).abs() <= 0.5 * atr).astype(float)
    return near.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f15_avwx_276_frac_bars_close_within_half_atr_avwap_52wlow_21d_d2(high, low, close, volume) -> pd.Series:
    a = _anchor_52w_low(low)
    av = _avwap_from_anchor_idx(close, volume, a)
    atr = _atr(high, low, close, n=MDAYS)
    near = ((close - av).abs() <= 0.5 * atr).astype(float)
    return near.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f15_avwx_277_max_consec_bars_clinging_avwap_252dhigh_d2(high, low, close, volume) -> pd.Series:
    """Current consecutive-bars-within-0.5*ATR streak of close vs AVWAP(peak)."""
    a = _anchor_252d_high(high)
    av = _avwap_from_anchor_idx(close, volume, a)
    atr = _atr(high, low, close, n=MDAYS)
    near = ((close - av).abs() <= 0.5 * atr).astype(float).values
    n = len(near)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if np.isnan(near[i]):
            streak = 0
            out[i] = np.nan
        else:
            streak = streak + 1 if near[i] > 0 else 0
            out[i] = float(streak)
    return pd.Series(out, index=high.index).diff().diff()

def f15_avwx_278_cum_share_volume_since_252d_high_anchor_d2(high, volume) -> pd.Series:
    """Cumulative share volume since the current 252d-high anchor bar (accumulation/distribution proxy)."""
    a = _anchor_252d_high(high)
    return _cum_vol_since_anchor(volume, a).diff().diff()

def f15_avwx_279_cum_dollar_volume_since_252d_high_anchor_d2(high, close, volume) -> pd.Series:
    a = _anchor_252d_high(high)
    return _cum_dollar_vol_since_anchor(close, volume, a).diff().diff()

def f15_avwx_280_avg_daily_dollar_vol_since_252d_high_anchor_d2(high, close, volume) -> pd.Series:
    """Average daily dollar volume since the peak anchor."""
    a = _anchor_252d_high(high)
    cum_dv = _cum_dollar_vol_since_anchor(close, volume, a)
    n = len(close)
    bars = np.array([float(i - a[i] + 1) if a[i] >= 0 else np.nan for i in range(n)])
    bars_s = pd.Series(bars, index=close.index)
    return _safe_div(cum_dv, bars_s).diff().diff()

def f15_avwx_281_cum_dollar_volume_since_ipo_anchor_log_d2(close, volume) -> pd.Series:
    a = _anchor_ipo(close)
    cum_dv = _cum_dollar_vol_since_anchor(close, volume, a)
    return _safe_log(cum_dv).diff().diff()

def f15_avwx_282_cum_share_volume_since_largest_gap_up_anchor_d2(open_, close, volume) -> pd.Series:
    a = _anchor_largest_gap_up_252d(open_, close)
    return _cum_vol_since_anchor(volume, a).diff().diff()

def f15_avwx_283_cum_dollar_vol_above_vs_below_avwap_252dhigh_ratio_d2(high, close, volume) -> pd.Series:
    """Ratio of cumulative dollar-volume on bars where close>AVWAP(peak) vs close<AVWAP(peak), since anchor."""
    a = _anchor_252d_high(high)
    av = _avwap_from_anchor_idx(close, volume, a)
    dv = (close * volume).fillna(0.0)
    above = dv.where(close > av, 0.0)
    below = dv.where(close < av, 0.0)
    cum_above = _cum_dollar_vol_since_anchor(pd.Series(np.where(close > av, close, 0.0), index=close.index), pd.Series(np.where(close > av, volume, 0.0), index=close.index), a)
    cum_below = _cum_dollar_vol_since_anchor(pd.Series(np.where(close < av, close, 0.0), index=close.index), pd.Series(np.where(close < av, volume, 0.0), index=close.index), a)
    return _safe_div(cum_above, cum_below).diff().diff()

def f15_avwx_284_signed_cum_volume_imbalance_since_peak_anchor_d2(high, close, volume) -> pd.Series:
    """CVD analog: cumulative-since-anchor signed volume = sign(close-AVWAP)*volume summed."""
    a = _anchor_252d_high(high)
    av = _avwap_from_anchor_idx(close, volume, a)
    signed = np.sign(close - av).fillna(0.0) * volume.fillna(0.0)
    sv = signed.values
    cum_sv = np.concatenate(([0.0], np.cumsum(sv)))
    n = len(close)
    out = np.full(n, np.nan, dtype=float)
    for i in range(n):
        ai = a[i]
        if ai < 0 or ai > i:
            continue
        out[i] = cum_sv[i + 1] - cum_sv[ai]
    return pd.Series(out, index=close.index).diff().diff()

def f15_avwx_285_dollar_weighted_dist_close_to_avwap_252dhigh_63d_d2(high, close, volume) -> pd.Series:
    """63d dollar-volume-weighted average of (close − AVWAP(peak)) / close."""
    a = _anchor_252d_high(high)
    av = _avwap_from_anchor_idx(close, volume, a)
    rel = _safe_div(close - av, close)
    dv = (close * volume).fillna(0.0)
    num = (rel * dv).rolling(QDAYS, min_periods=MDAYS).sum()
    den = dv.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(num, den).diff().diff()

def f15_avwx_286_max_excursion_above_avwap_252dhigh_norm_sigma_252d_d2(high, close, volume) -> pd.Series:
    """Max excursion (close − AVWAP) / sigma over trailing 252d."""
    a = _anchor_252d_high(high)
    av, sd, upper, lower = _sigma_band_series(close, volume, a, k=1.0)
    excess = _safe_div(close - av, sd)
    return excess.rolling(YDAYS, min_periods=QDAYS).max().diff().diff()

def f15_avwx_287_max_excursion_below_avwap_252dhigh_norm_sigma_252d_d2(high, close, volume) -> pd.Series:
    a = _anchor_252d_high(high)
    av, sd, upper, lower = _sigma_band_series(close, volume, a, k=1.0)
    excess = _safe_div(close - av, sd)
    return excess.rolling(YDAYS, min_periods=QDAYS).min().diff().diff()

def f15_avwx_288_recovery_ratio_after_peak_avwap_break_d2(high, close, volume) -> pd.Series:
    """(max subsequent close − AVWAP) / (peak − AVWAP) — fraction of peak recovered after break.
    Tracked per current anchor: numerator = trailing max of close since anchor minus av at anchor;
    denominator = (price at anchor) − av at anchor.
    """
    a = _anchor_252d_high(high)
    av = _avwap_from_anchor_idx(close, volume, a)
    c = close.values
    h = high.values
    v = av.values
    n = len(c)
    out = np.full(n, np.nan, dtype=float)
    last_anchor = -1
    peak_h = np.nan
    av_at_anchor = np.nan
    running_max_close = -np.inf
    for i in range(n):
        if a[i] != last_anchor and a[i] >= 0:
            last_anchor = a[i]
            peak_h = h[last_anchor]
            av_at_anchor = v[last_anchor] if not np.isnan(v[last_anchor]) else np.nan
            running_max_close = -np.inf
        if last_anchor >= 0 and (not np.isnan(c[i])):
            if c[i] > running_max_close:
                running_max_close = c[i]
            denom = peak_h - av_at_anchor
            if denom is not None and (not np.isnan(denom)) and (denom > 0):
                num = running_max_close - av_at_anchor
                out[i] = num / denom
    return pd.Series(out, index=close.index).diff().diff()

def f15_avwx_289_avwap_extension_at_252d_high_norm_atr_d2(high, low, close, volume) -> pd.Series:
    """At the 252d-high bar, (high − AVWAP(IPO))/ATR — extension at peak in vol units.
    Reported on the peak bar; forward-filled until anchor moves."""
    a_peak = _anchor_252d_high(high)
    a_ipo = _anchor_ipo(close)
    av_ipo = _avwap_from_anchor_idx(close, volume, a_ipo)
    atr = _atr(high, low, close, n=MDAYS)
    h = high.values
    ai = av_ipo.values
    at = atr.values
    n = len(close)
    out = np.full(n, np.nan, dtype=float)
    last_anchor = -1
    recorded = np.nan
    for i in range(n):
        if a_peak[i] != last_anchor and a_peak[i] >= 0:
            last_anchor = a_peak[i]
            ap = last_anchor
            if not np.isnan(h[ap]) and (not np.isnan(ai[ap])) and (not np.isnan(at[ap])) and (at[ap] > 0):
                recorded = (h[ap] - ai[ap]) / at[ap]
        out[i] = recorded
    return pd.Series(out, index=close.index).diff().diff()

def f15_avwx_290_avwap_extension_at_252d_high_norm_sigma_d2(high, close, volume) -> pd.Series:
    """At the 252d-high bar, (high − AVWAP(IPO))/sigma_close_63d at that bar."""
    a_peak = _anchor_252d_high(high)
    a_ipo = _anchor_ipo(close)
    av_ipo = _avwap_from_anchor_idx(close, volume, a_ipo)
    ret = _safe_log(close).diff()
    sigma = ret.rolling(QDAYS, min_periods=MDAYS).std()
    h = high.values
    ai = av_ipo.values
    sg = sigma.values
    n = len(close)
    out = np.full(n, np.nan, dtype=float)
    last_anchor = -1
    recorded = np.nan
    for i in range(n):
        if a_peak[i] != last_anchor and a_peak[i] >= 0:
            last_anchor = a_peak[i]
            ap = last_anchor
            if not np.isnan(h[ap]) and (not np.isnan(ai[ap])) and (not np.isnan(sg[ap])) and (sg[ap] > 0):
                recorded = (h[ap] - ai[ap]) / sg[ap]
        out[i] = recorded
    return pd.Series(out, index=close.index).diff().diff()

def f15_avwx_291_dist_close_to_avwap_from_post_break_anchor_peak_d2(high, close, volume) -> pd.Series:
    """Log distance close to AVWAP from new anchor set at the bar where peak-AVWAP broke."""
    a = _anchor_post_break_peak(high, close, volume)
    av = _avwap_from_anchor_idx(close, volume, a)
    return (_safe_log(close) - _safe_log(av)).diff().diff()

def f15_avwx_292_bars_since_post_break_anchor_peak_d2(high, close, volume) -> pd.Series:
    a = _anchor_post_break_peak(high, close, volume)
    n = len(close)
    out = np.array([float(i - a[i]) if a[i] >= 0 else np.nan for i in range(n)])
    return pd.Series(out, index=close.index).diff().diff()

def f15_avwx_293_slope_avwap_from_post_break_anchor_63d_d2(high, close, volume) -> pd.Series:
    a = _anchor_post_break_peak(high, close, volume)
    av = _avwap_from_anchor_idx(close, volume, a)
    return _rolling_slope(av, QDAYS).diff().diff()

def f15_avwx_294_indicator_close_lost_avwap_ipo_after_above_252d_d2(close, volume) -> pd.Series:
    """Indicator: close currently below AVWAP(IPO) AND was above it at some point in last 252d (secular break)."""
    a = _anchor_ipo(close)
    av = _avwap_from_anchor_idx(close, volume, a)
    below = (close < av).astype(float)
    above = (close > av).astype(float)
    was_above_recent = above.rolling(YDAYS, min_periods=QDAYS).max()
    return (below * was_above_recent).where(av.notna(), np.nan).diff().diff()

def f15_avwx_295_bars_since_close_lost_avwap_ipo_d2(close, volume) -> pd.Series:
    """Bars since the most recent bar that closed below AVWAP(IPO) for the first time after being above."""
    a = _anchor_ipo(close)
    av = _avwap_from_anchor_idx(close, volume, a)
    c = close.values
    v = av.values
    n = len(c)
    out = np.full(n, np.nan, dtype=float)
    prev_above = None
    last_break = -1
    for i in range(n):
        if np.isnan(v[i]) or np.isnan(c[i]):
            continue
        cur_above = c[i] > v[i]
        if prev_above is True and (not cur_above):
            last_break = i
        prev_above = cur_above
        if last_break >= 0:
            out[i] = float(i - last_break)
    return pd.Series(out, index=close.index).diff().diff()

def f15_avwx_296_count_clusters_anchor_avwaps_within_2pct_252d_d2(high, low, close, volume) -> pd.Series:
    """Number of clusters among 4 anchor AVWAPs where pairwise distance / close < 2%."""
    av1, av2, av3, av4 = _build_4anchor_avwaps(high, low, close, volume)
    n = len(close)
    out = np.full(n, np.nan, dtype=float)
    c = close.values
    a = av1.values
    b = av2.values
    cc = av3.values
    d = av4.values
    for i in range(n):
        vals = [a[i], b[i], cc[i], d[i]]
        if any((np.isnan(x) for x in vals)) or np.isnan(c[i]) or c[i] <= 0:
            continue
        parent = list(range(4))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = (find(x), find(y))
            if rx != ry:
                parent[rx] = ry
        for ii in range(4):
            for jj in range(ii + 1, 4):
                if abs(vals[ii] - vals[jj]) / c[i] < 0.02:
                    union(ii, jj)
        roots = set((find(k) for k in range(4)))
        out[i] = float(len(roots))
    return pd.Series(out, index=close.index).diff().diff()

def f15_avwx_297_dist_close_to_nearest_anchor_avwap_norm_atr_d2(high, low, close, volume) -> pd.Series:
    """Distance from close to nearest anchor AVWAP, normalized by ATR."""
    av1, av2, av3, av4 = _build_4anchor_avwaps(high, low, close, volume)
    atr = _atr(high, low, close, n=MDAYS)
    df = pd.concat([(close - av1).abs().rename('a1'), (close - av2).abs().rename('a2'), (close - av3).abs().rename('a3'), (close - av4).abs().rename('a4')], axis=1)
    return _safe_div(df.min(axis=1), atr).diff().diff()

def f15_avwx_298_dist_close_to_farthest_anchor_avwap_norm_atr_d2(high, low, close, volume) -> pd.Series:
    av1, av2, av3, av4 = _build_4anchor_avwaps(high, low, close, volume)
    atr = _atr(high, low, close, n=MDAYS)
    df = pd.concat([(close - av1).abs().rename('a1'), (close - av2).abs().rename('a2'), (close - av3).abs().rename('a3'), (close - av4).abs().rename('a4')], axis=1)
    return _safe_div(df.max(axis=1), atr).diff().diff()

def f15_avwx_299_indicator_close_above_peak_avwap_plus_2sigma_for_5d_d2(high, close, volume) -> pd.Series:
    """Indicator: close has been > AVWAP(peak)+2σ for all of the last 5 bars (blow-off persistence)."""
    a = _anchor_252d_high(high)
    av, sd, upper, lower = _sigma_band_series(close, volume, a, k=2.0)
    above = (close > upper).astype(float)
    cnt = above.rolling(WDAYS, min_periods=2).sum()
    return (cnt >= WDAYS).astype(float).where(av.notna(), np.nan).diff().diff()

def f15_avwx_300_composite_distribution_topping_score_peak_anchor_d2(high, low, close, volume) -> pd.Series:
    """Multi-criteria composite (0-7) over peak AVWAP regime:
      + close < AVWAP(peak)
      + AVWAP(peak) slope < 0 (21d)
      + failed-reclaim count 63d >= 3
      + close < AVWAP(peak) − 1σ
      + bars-since-peak-anchor >= 21
      + cum-dollar-vol-below-AVWAP > cum-dollar-vol-above-AVWAP since anchor
      + count anchors above close >= 2
    """
    a = _anchor_252d_high(high)
    av, sd, upper, lower = _sigma_band_series(close, volume, a, k=1.0)
    sl = _rolling_slope(av, MDAYS)
    failed = ((high >= av) & (close < av)).astype(float)
    fr_cnt = failed.rolling(QDAYS, min_periods=MDAYS).sum()
    n = len(close)
    bsa = np.array([float(i - a[i]) if a[i] >= 0 else np.nan for i in range(n)])
    bsa_s = pd.Series(bsa, index=close.index)
    above_dv = _safe_div(_cum_dollar_vol_since_anchor(pd.Series(np.where(close > av, close, 0.0), index=close.index), pd.Series(np.where(close > av, volume, 0.0), index=close.index), a), 1.0)
    below_dv = _safe_div(_cum_dollar_vol_since_anchor(pd.Series(np.where(close < av, close, 0.0), index=close.index), pd.Series(np.where(close < av, volume, 0.0), index=close.index), a), 1.0)
    av1, av2, av3, av4 = _build_4anchor_avwaps(high, low, close, volume)
    above_cnt = (av1 > close).astype(float).fillna(0.0) + (av2 > close).astype(float).fillna(0.0) + (av3 > close).astype(float).fillna(0.0) + (av4 > close).astype(float).fillna(0.0)
    score = (close < av).astype(float).fillna(0.0) + (sl < 0).astype(float).fillna(0.0) + (fr_cnt >= 3).astype(float).fillna(0.0) + (close < lower).astype(float).fillna(0.0) + (bsa_s >= MDAYS).astype(float).fillna(0.0) + (below_dv > above_dv).astype(float).fillna(0.0) + (above_cnt >= 2).astype(float).fillna(0.0)
    return score.where(av.notna(), np.nan).diff().diff()
ANCHORED_VWAP_EXTENSION_D2_REGISTRY_226_300 = {'f15_avwx_226_log_dist_close_to_avwap_from_largest_gap_up_252d_d2': {'inputs': ['open', 'high', 'low', 'close', 'volume'], 'func': f15_avwx_226_log_dist_close_to_avwap_from_largest_gap_up_252d_d2}, 'f15_avwx_227_bars_since_largest_gap_up_anchor_252d_d2': {'inputs': ['open', 'close'], 'func': f15_avwx_227_bars_since_largest_gap_up_anchor_252d_d2}, 'f15_avwx_228_slope_avwap_from_largest_gap_up_63d_d2': {'inputs': ['open', 'close', 'volume'], 'func': f15_avwx_228_slope_avwap_from_largest_gap_up_63d_d2}, 'f15_avwx_229_atr_dist_close_to_avwap_from_largest_gap_up_d2': {'inputs': ['open', 'high', 'low', 'close', 'volume'], 'func': f15_avwx_229_atr_dist_close_to_avwap_from_largest_gap_up_d2}, 'f15_avwx_230_log_dist_close_to_avwap_from_prior_252d_high_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_230_log_dist_close_to_avwap_from_prior_252d_high_d2}, 'f15_avwx_231_bars_since_prior_252d_high_anchor_d2': {'inputs': ['high'], 'func': f15_avwx_231_bars_since_prior_252d_high_anchor_d2}, 'f15_avwx_232_slope_avwap_from_prior_252d_high_63d_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_232_slope_avwap_from_prior_252d_high_63d_d2}, 'f15_avwx_233_log_dist_close_to_avwap_from_lifetime_high_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_233_log_dist_close_to_avwap_from_lifetime_high_d2}, 'f15_avwx_234_bars_since_lifetime_high_anchor_d2': {'inputs': ['high'], 'func': f15_avwx_234_bars_since_lifetime_high_anchor_d2}, 'f15_avwx_235_log_dist_close_to_avwap_from_ipo_bar_d2': {'inputs': ['close', 'volume'], 'func': f15_avwx_235_log_dist_close_to_avwap_from_ipo_bar_d2}, 'f15_avwx_236_log_dist_close_to_avwap_from_lifetime_low_d2': {'inputs': ['low', 'close', 'volume'], 'func': f15_avwx_236_log_dist_close_to_avwap_from_lifetime_low_d2}, 'f15_avwx_237_log_dist_close_to_avwap_from_largest_gap_down_252d_d2': {'inputs': ['open', 'close', 'volume'], 'func': f15_avwx_237_log_dist_close_to_avwap_from_largest_gap_down_252d_d2}, 'f15_avwx_238_bars_since_largest_gap_down_anchor_252d_d2': {'inputs': ['open', 'close'], 'func': f15_avwx_238_bars_since_largest_gap_down_anchor_252d_d2}, 'f15_avwx_239_log_dist_close_to_avwap_from_largest_1d_return_252d_d2': {'inputs': ['close', 'volume'], 'func': f15_avwx_239_log_dist_close_to_avwap_from_largest_1d_return_252d_d2}, 'f15_avwx_240_log_dist_close_to_avwap_from_wyckoff_buying_climax_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_240_log_dist_close_to_avwap_from_wyckoff_buying_climax_d2}, 'f15_avwx_241_bars_since_wyckoff_buying_climax_anchor_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_241_bars_since_wyckoff_buying_climax_anchor_d2}, 'f15_avwx_242_slope_avwap_from_wyckoff_buying_climax_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_242_slope_avwap_from_wyckoff_buying_climax_63d_d2}, 'f15_avwx_243_log_dist_close_to_avwap_from_wyckoff_selling_climax_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_243_log_dist_close_to_avwap_from_wyckoff_selling_climax_d2}, 'f15_avwx_244_bars_since_wyckoff_selling_climax_anchor_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_244_bars_since_wyckoff_selling_climax_anchor_d2}, 'f15_avwx_245_log_dist_close_to_avwap_from_highest_range_bar_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_245_log_dist_close_to_avwap_from_highest_range_bar_252d_d2}, 'f15_avwx_246_log_dist_close_to_avwap_from_widest_dollar_vol_bar_252d_d2': {'inputs': ['close', 'volume'], 'func': f15_avwx_246_log_dist_close_to_avwap_from_widest_dollar_vol_bar_252d_d2}, 'f15_avwx_247_failed_reclaim_count_avwap_252dhigh_63d_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_247_failed_reclaim_count_avwap_252dhigh_63d_d2}, 'f15_avwx_248_failed_reclaim_max_wick_avwap_252dhigh_63d_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_248_failed_reclaim_max_wick_avwap_252dhigh_63d_d2}, 'f15_avwx_249_bars_since_last_failed_reclaim_avwap_252dhigh_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_249_bars_since_last_failed_reclaim_avwap_252dhigh_d2}, 'f15_avwx_250_failed_reclaim_count_avwap_lifetime_high_252d_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_250_failed_reclaim_count_avwap_lifetime_high_252d_d2}, 'f15_avwx_251_post_break_retest_drawdown_avwap_252dhigh_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_251_post_break_retest_drawdown_avwap_252dhigh_d2}, 'f15_avwx_252_days_break_to_retest_avwap_252dhigh_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_252_days_break_to_retest_avwap_252dhigh_d2}, 'f15_avwx_253_indicator_avwap_252dhigh_minus_3sigma_lower_breach_21d_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_253_indicator_avwap_252dhigh_minus_3sigma_lower_breach_21d_d2}, 'f15_avwx_254_close_position_in_avwap_252dhigh_3sigma_band_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_254_close_position_in_avwap_252dhigh_3sigma_band_d2}, 'f15_avwx_255_touch_count_avwap_252dhigh_upper_2sigma_252d_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_255_touch_count_avwap_252dhigh_upper_2sigma_252d_d2}, 'f15_avwx_256_walking_upper_band_peak_avwap_indicator_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_256_walking_upper_band_peak_avwap_indicator_d2}, 'f15_avwx_257_close_position_in_avwap_ipo_2sigma_band_d2': {'inputs': ['close', 'volume'], 'func': f15_avwx_257_close_position_in_avwap_ipo_2sigma_band_d2}, 'f15_avwx_258_count_anchors_with_close_above_3sigma_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_258_count_anchors_with_close_above_3sigma_d2}, 'f15_avwx_259_count_avwaps_currently_above_close_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_259_count_avwaps_currently_above_close_d2}, 'f15_avwx_260_bars_since_close_above_all_avwaps_simultaneously_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_260_bars_since_close_above_all_avwaps_simultaneously_d2}, 'f15_avwx_261_max_consec_bars_close_below_all_anchors_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_261_max_consec_bars_close_below_all_anchors_252d_d2}, 'f15_avwx_262_count_anchor_avwap_crosses_by_close_21d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_262_count_anchor_avwap_crosses_by_close_21d_d2}, 'f15_avwx_263_anchor_slope_sign_agreement_score_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_263_anchor_slope_sign_agreement_score_d2}, 'f15_avwx_264_bars_since_first_negative_slope_avwap_252dhigh_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_264_bars_since_first_negative_slope_avwap_252dhigh_d2}, 'f15_avwx_265_slope_acceleration_avwap_252dhigh_21d_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_265_slope_acceleration_avwap_252dhigh_21d_d2}, 'f15_avwx_266_indicator_peak_avwap_slope_lt_zero_for_21d_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_266_indicator_peak_avwap_slope_lt_zero_for_21d_d2}, 'f15_avwx_267_diff_avwap_252dhigh_minus_avwap_ipo_norm_close_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_267_diff_avwap_252dhigh_minus_avwap_ipo_norm_close_d2}, 'f15_avwx_268_diff_avwap_252dhigh_minus_avwap_climax_norm_close_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_268_diff_avwap_252dhigh_minus_avwap_climax_norm_close_d2}, 'f15_avwx_269_diff_avwap_252dhigh_minus_avwap_lifetime_high_norm_close_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_269_diff_avwap_252dhigh_minus_avwap_lifetime_high_norm_close_d2}, 'f15_avwx_270_cross_event_avwap_252dhigh_above_avwap_52wlow_21d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_270_cross_event_avwap_252dhigh_above_avwap_52wlow_21d_d2}, 'f15_avwx_271_bars_since_cross_avwap_peak_vs_avwap_ipo_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_271_bars_since_cross_avwap_peak_vs_avwap_ipo_d2}, 'f15_avwx_272_count_avwap_avwap_crosses_among_4anchors_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_272_count_avwap_avwap_crosses_among_4anchors_252d_d2}, 'f15_avwx_273_min_pairwise_dist_among_anchor_avwaps_norm_close_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_273_min_pairwise_dist_among_anchor_avwaps_norm_close_d2}, 'f15_avwx_274_anchor_avwap_convergence_velocity_21d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_274_anchor_avwap_convergence_velocity_21d_d2}, 'f15_avwx_275_frac_bars_close_within_half_atr_avwap_252dhigh_21d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_275_frac_bars_close_within_half_atr_avwap_252dhigh_21d_d2}, 'f15_avwx_276_frac_bars_close_within_half_atr_avwap_52wlow_21d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_276_frac_bars_close_within_half_atr_avwap_52wlow_21d_d2}, 'f15_avwx_277_max_consec_bars_clinging_avwap_252dhigh_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_277_max_consec_bars_clinging_avwap_252dhigh_d2}, 'f15_avwx_278_cum_share_volume_since_252d_high_anchor_d2': {'inputs': ['high', 'volume'], 'func': f15_avwx_278_cum_share_volume_since_252d_high_anchor_d2}, 'f15_avwx_279_cum_dollar_volume_since_252d_high_anchor_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_279_cum_dollar_volume_since_252d_high_anchor_d2}, 'f15_avwx_280_avg_daily_dollar_vol_since_252d_high_anchor_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_280_avg_daily_dollar_vol_since_252d_high_anchor_d2}, 'f15_avwx_281_cum_dollar_volume_since_ipo_anchor_log_d2': {'inputs': ['close', 'volume'], 'func': f15_avwx_281_cum_dollar_volume_since_ipo_anchor_log_d2}, 'f15_avwx_282_cum_share_volume_since_largest_gap_up_anchor_d2': {'inputs': ['open', 'close', 'volume'], 'func': f15_avwx_282_cum_share_volume_since_largest_gap_up_anchor_d2}, 'f15_avwx_283_cum_dollar_vol_above_vs_below_avwap_252dhigh_ratio_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_283_cum_dollar_vol_above_vs_below_avwap_252dhigh_ratio_d2}, 'f15_avwx_284_signed_cum_volume_imbalance_since_peak_anchor_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_284_signed_cum_volume_imbalance_since_peak_anchor_d2}, 'f15_avwx_285_dollar_weighted_dist_close_to_avwap_252dhigh_63d_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_285_dollar_weighted_dist_close_to_avwap_252dhigh_63d_d2}, 'f15_avwx_286_max_excursion_above_avwap_252dhigh_norm_sigma_252d_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_286_max_excursion_above_avwap_252dhigh_norm_sigma_252d_d2}, 'f15_avwx_287_max_excursion_below_avwap_252dhigh_norm_sigma_252d_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_287_max_excursion_below_avwap_252dhigh_norm_sigma_252d_d2}, 'f15_avwx_288_recovery_ratio_after_peak_avwap_break_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_288_recovery_ratio_after_peak_avwap_break_d2}, 'f15_avwx_289_avwap_extension_at_252d_high_norm_atr_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_289_avwap_extension_at_252d_high_norm_atr_d2}, 'f15_avwx_290_avwap_extension_at_252d_high_norm_sigma_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_290_avwap_extension_at_252d_high_norm_sigma_d2}, 'f15_avwx_291_dist_close_to_avwap_from_post_break_anchor_peak_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_291_dist_close_to_avwap_from_post_break_anchor_peak_d2}, 'f15_avwx_292_bars_since_post_break_anchor_peak_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_292_bars_since_post_break_anchor_peak_d2}, 'f15_avwx_293_slope_avwap_from_post_break_anchor_63d_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_293_slope_avwap_from_post_break_anchor_63d_d2}, 'f15_avwx_294_indicator_close_lost_avwap_ipo_after_above_252d_d2': {'inputs': ['close', 'volume'], 'func': f15_avwx_294_indicator_close_lost_avwap_ipo_after_above_252d_d2}, 'f15_avwx_295_bars_since_close_lost_avwap_ipo_d2': {'inputs': ['close', 'volume'], 'func': f15_avwx_295_bars_since_close_lost_avwap_ipo_d2}, 'f15_avwx_296_count_clusters_anchor_avwaps_within_2pct_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_296_count_clusters_anchor_avwaps_within_2pct_252d_d2}, 'f15_avwx_297_dist_close_to_nearest_anchor_avwap_norm_atr_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_297_dist_close_to_nearest_anchor_avwap_norm_atr_d2}, 'f15_avwx_298_dist_close_to_farthest_anchor_avwap_norm_atr_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_298_dist_close_to_farthest_anchor_avwap_norm_atr_d2}, 'f15_avwx_299_indicator_close_above_peak_avwap_plus_2sigma_for_5d_d2': {'inputs': ['high', 'close', 'volume'], 'func': f15_avwx_299_indicator_close_above_peak_avwap_plus_2sigma_for_5d_d2}, 'f15_avwx_300_composite_distribution_topping_score_peak_anchor_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_300_composite_distribution_topping_score_peak_anchor_d2}}