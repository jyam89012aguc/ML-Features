"""anchored_vwap_extension base features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py. Each feature
encodes a *different concept* in the anchored-VWAP theme: AVWAP distance from
event anchors (52w-low, 252d-high, multi-year-low/high, IPO-proxy), rolling
AVWAPs at distinct horizons, AVWAP slope/velocity, multi-anchor agreement,
channel position, anchor spread.

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


# Family-specific helpers.

def _typical_price(high, low, close):
    return (high + low + close) / 3.0


def _rolling_avwap(typical, volume, window, min_periods=None):
    """Trailing-window AVWAP = sum(price*vol)/sum(vol) over window."""
    if min_periods is None:
        min_periods = max(window // 3, 2)
    pv = (typical * volume).rolling(window, min_periods=min_periods).sum()
    v = volume.rolling(window, min_periods=min_periods).sum()
    return _safe_div(pv, v)


def _anchored_vwap_from_event(typical, volume, anchor_mask):
    """AVWAP from most recent True in anchor_mask (incl. that bar) up to current bar.
    Group bars by cumulative anchor count, then within-group cumsum(p*v)/cumsum(v).
    Bars before the first anchor return NaN.
    """
    aid = anchor_mask.fillna(False).astype(int).cumsum()
    pv = (typical * volume)
    pv_cum = pv.groupby(aid).cumsum()
    v_cum = volume.groupby(aid).cumsum()
    out = _safe_div(pv_cum, v_cum)
    return out.where(aid > 0, np.nan)


def _anchored_vwap_window_min(typical, volume, low, n, min_periods=None):
    """AVWAP from argmin-low-in-trailing-n-window to current bar. O(N*n)."""
    if min_periods is None:
        min_periods = max(n // 3, 2)
    p = typical.values; v = volume.values; lo = low.values
    nb = len(p)
    out = np.full(nb, np.nan)
    for i in range(nb):
        s = max(0, i - n + 1)
        wlen = i - s + 1
        if wlen < min_periods:
            continue
        w = lo[s:i + 1]
        if np.isnan(w).all():
            continue
        amin = int(np.nanargmin(w)) + s
        pw = p[amin:i + 1]
        vw = v[amin:i + 1]
        valid = ~(np.isnan(pw) | np.isnan(vw))
        if valid.sum() == 0:
            continue
        denom = vw[valid].sum()
        if denom == 0:
            continue
        out[i] = (pw[valid] * vw[valid]).sum() / denom
    return pd.Series(out, index=typical.index)


def _anchored_vwap_window_max(typical, volume, high, n, min_periods=None):
    """AVWAP from argmax-high-in-trailing-n-window to current bar."""
    if min_periods is None:
        min_periods = max(n // 3, 2)
    p = typical.values; v = volume.values; hi = high.values
    nb = len(p)
    out = np.full(nb, np.nan)
    for i in range(nb):
        s = max(0, i - n + 1)
        wlen = i - s + 1
        if wlen < min_periods:
            continue
        w = hi[s:i + 1]
        if np.isnan(w).all():
            continue
        amax = int(np.nanargmax(w)) + s
        pw = p[amax:i + 1]
        vw = v[amax:i + 1]
        valid = ~(np.isnan(pw) | np.isnan(vw))
        if valid.sum() == 0:
            continue
        denom = vw[valid].sum()
        if denom == 0:
            continue
        out[i] = (pw[valid] * vw[valid]).sum() / denom
    return pd.Series(out, index=typical.index)


def _expanding_avwap(typical, volume):
    """AVWAP from first bar to current bar (IPO-proxy anchor)."""
    pv = (typical * volume).cumsum()
    v = volume.cumsum()
    return _safe_div(pv, v)


def _bars_since_true(mask):
    arr = mask.values.astype(bool)
    n = len(arr)
    out = np.full(n, np.nan)
    last = -1
    for i in range(n):
        if arr[i]:
            last = i; out[i] = 0.0
        elif last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=mask.index)


def _streak_true(mask):
    arr = mask.values.astype(bool)
    n = len(arr)
    out = np.zeros(n, dtype=float)
    run = 0
    for i in range(n):
        run = run + 1 if arr[i] else 0
        out[i] = float(run)
    return pd.Series(out, index=mask.index)


def _event_mask_new_window_low(low, n):
    """True when low equals trailing-n-window min (new low event)."""
    rmin = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return (low <= rmin) & rmin.notna()


def _event_mask_new_window_high(high, n):
    """True when high equals trailing-n-window max (new high event)."""
    rmax = high.rolling(n, min_periods=max(n // 3, 2)).max()
    return (high >= rmax) & rmax.notna()


def _vwap_sigma_band(typical, volume, window, k, min_periods=None):
    """Rolling-window VWAP ± k × volume-weighted std of typical-price. Returns (upper, mid, lower)."""
    if min_periods is None:
        min_periods = max(window // 3, 2)
    mp = min_periods
    pv = (typical * volume).rolling(window, min_periods=mp).sum()
    vs = volume.rolling(window, min_periods=mp).sum()
    vwap = _safe_div(pv, vs)
    sqd = (typical - vwap) ** 2
    wsqd = (sqd * volume).rolling(window, min_periods=mp).sum()
    vwstd = _safe_div(wsqd, vs).pow(0.5)
    return vwap + k * vwstd, vwap, vwap - k * vwstd


def _volume_profile_poc(typical, volume, window, n_bins=20, min_periods=None):
    """Point of Control: price-bin with max volume in trailing window. Returns Series of POC price."""
    if min_periods is None:
        min_periods = max(window // 3, 2)
    p = typical.values; v = volume.values
    nb = len(p)
    out = np.full(nb, np.nan)
    for i in range(nb):
        s = max(0, i - window + 1)
        if i - s + 1 < min_periods:
            continue
        wp = p[s:i + 1]; wv = v[s:i + 1]
        valid = ~(np.isnan(wp) | np.isnan(wv))
        if valid.sum() < min_periods:
            continue
        wp = wp[valid]; wv = wv[valid]
        lo, hi = wp.min(), wp.max()
        if hi <= lo:
            out[i] = lo; continue
        bin_idx = np.minimum(((wp - lo) / (hi - lo) * n_bins).astype(int), n_bins - 1)
        bin_vol = np.zeros(n_bins)
        for j in range(len(bin_idx)):
            bin_vol[bin_idx[j]] += wv[j]
        poc_bin = int(np.argmax(bin_vol))
        out[i] = lo + (poc_bin + 0.5) * (hi - lo) / n_bins
    return pd.Series(out, index=typical.index)


def _value_area_high_low(typical, volume, window, n_bins=20, pct=0.7, min_periods=None):
    """Value Area (VAH, VAL): contiguous price range around POC containing pct of total volume."""
    if min_periods is None:
        min_periods = max(window // 3, 2)
    p = typical.values; v = volume.values
    nb = len(p)
    vah_out = np.full(nb, np.nan); val_out = np.full(nb, np.nan)
    for i in range(nb):
        s = max(0, i - window + 1)
        if i - s + 1 < min_periods:
            continue
        wp = p[s:i + 1]; wv = v[s:i + 1]
        valid = ~(np.isnan(wp) | np.isnan(wv))
        if valid.sum() < min_periods:
            continue
        wp = wp[valid]; wv = wv[valid]
        lo, hi = wp.min(), wp.max()
        if hi <= lo:
            vah_out[i] = hi; val_out[i] = lo; continue
        bin_idx = np.minimum(((wp - lo) / (hi - lo) * n_bins).astype(int), n_bins - 1)
        bin_vol = np.zeros(n_bins)
        for j in range(len(bin_idx)):
            bin_vol[bin_idx[j]] += wv[j]
        total_vol = bin_vol.sum()
        if total_vol <= 0:
            continue
        target = total_vol * pct
        poc_bin = int(np.argmax(bin_vol))
        lo_bin = hi_bin = poc_bin
        acc = bin_vol[poc_bin]
        while acc < target:
            below = bin_vol[lo_bin - 1] if lo_bin > 0 else -1.0
            above = bin_vol[hi_bin + 1] if hi_bin < n_bins - 1 else -1.0
            if below < 0 and above < 0:
                break
            if above >= below:
                hi_bin += 1; acc += bin_vol[hi_bin]
            else:
                lo_bin -= 1; acc += bin_vol[lo_bin]
        vah_out[i] = lo + (hi_bin + 1) * (hi - lo) / n_bins
        val_out[i] = lo + lo_bin * (hi - lo) / n_bins
    return pd.Series(vah_out, index=typical.index), pd.Series(val_out, index=typical.index)


def _twap(typical, window, min_periods=None):
    """Time-weighted average price (simple SMA of typical price)."""
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return typical.rolling(window, min_periods=min_periods).mean()


def _volume_profile_asymmetry(typical, volume, window, min_periods=None):
    """Σ(volume above mid_typical) / Σ(volume below mid_typical) in trailing window."""
    if min_periods is None:
        min_periods = max(window // 3, 2)
    p = typical.values; v = volume.values
    nb = len(p)
    out = np.full(nb, np.nan)
    for i in range(nb):
        s = max(0, i - window + 1)
        if i - s + 1 < min_periods:
            continue
        wp = p[s:i + 1]; wv = v[s:i + 1]
        valid = ~(np.isnan(wp) | np.isnan(wv))
        if valid.sum() < min_periods:
            continue
        wp = wp[valid]; wv = wv[valid]
        mid = (wp.max() + wp.min()) / 2.0
        vu = wv[wp > mid].sum()
        vd = wv[wp < mid].sum()
        if vd > 0:
            out[i] = float(vu / vd)
    return pd.Series(out, index=typical.index)


# ============================================================
# Bucket A — AVWAP from 52w-low (252d-low) anchor (001-012)
# ============================================================

def f15_avwx_001_log_dist_close_to_avwap_from_252d_low(high, low, close, volume):
    """Log distance close above AVWAP anchored at each new 252d-low event."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    return _safe_log(close) - _safe_log(av)


def f15_avwx_002_atr_dist_close_to_avwap_from_252d_low(high, low, close, volume):
    """(close − AVWAP-from-252d-low) / ATR(21) — ATR-normalized anchor extension."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    return _safe_div(close - av, _atr(high, low, close, n=MDAYS))


def f15_avwx_003_pct_dist_close_to_avwap_from_252d_low(high, low, close, volume):
    """Percent distance close above AVWAP-from-52w-low."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    return _safe_div(close - av, av)


def f15_avwx_004_bars_since_252d_low_anchor(high, low, close):
    """Bars since most recent new 252d-low event — anchor age."""
    return _bars_since_true(_event_mask_new_window_low(low, YDAYS))


def f15_avwx_005_slope_avwap_from_252d_low_21d(high, low, close, volume):
    """Slope of AVWAP-from-52w-low over trailing 21d."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    return _rolling_slope(av, MDAYS)


def f15_avwx_006_zscore_dist_close_avwap_252dlow_in_252d(high, low, close, volume):
    """Z-score of (close − AVWAP-from-52w-low)/close in trailing 252d."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    return _rolling_zscore(_safe_div(close - av, close), YDAYS)


def f15_avwx_007_pctile_rank_dist_close_avwap_252dlow_252d(high, low, close, volume):
    """Empirical percentile rank of (close − AVWAP-from-52w-low)/close in 252d distribution."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    raw = _safe_div(close - av, close)
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        v = w[~np.isnan(w)]
        return float((v <= last).sum()) / float(v.size) if v.size else np.nan
    return raw.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)


def f15_avwx_008_close_position_in_avwap_sigma_band_252dlow(high, low, close, volume):
    """Position of close in [AVWAP ± 2σ] band of AVWAP-from-52w-low (σ = 63d residual std)."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    sigma = (close - av).rolling(QDAYS, min_periods=MDAYS).std()
    upper = av + 2 * sigma
    lower = av - 2 * sigma
    return _safe_div(close - lower, upper - lower)


def f15_avwx_009_frac_bars_close_above_avwap_from_252d_low_63d(high, low, close, volume):
    """Fraction of bars in 63d where close > AVWAP-from-52w-low."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    above = (close > av).astype(float).where(av.notna(), np.nan)
    return above.rolling(QDAYS, min_periods=MDAYS).mean()


def f15_avwx_010_max_log_dist_close_avwap_252dlow_21d(high, low, close, volume):
    """Max log distance close above AVWAP-from-52w-low over trailing 21d."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    d = _safe_log(close) - _safe_log(av)
    return d.rolling(MDAYS, min_periods=WDAYS).max()


def f15_avwx_011_half_life_dev_close_avwap_252dlow_252d(high, low, close, volume):
    """Implied half-life of (close − AVWAP-from-52w-low) deviations in 252d (AR(1) ρ → ln2/-lnρ)."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    dev = close - av
    def _hl(w):
        if not np.isfinite(w).all() or len(w) < 30:
            return np.nan
        a = w[:-1] - w[:-1].mean(); b = w[1:] - w[1:].mean()
        den = (a * a).sum()
        if den <= 0:
            return np.nan
        rho = (a * b).sum() / den
        if rho <= 0 or rho >= 1:
            return np.nan
        return float(np.log(2.0) / -np.log(rho))
    return dev.rolling(YDAYS, min_periods=QDAYS).apply(_hl, raw=True)


def f15_avwx_012_years_since_52w_low(high, low, close):
    """Bars since 52w-low divided by 252 (anchor age in years)."""
    return _bars_since_true(_event_mask_new_window_low(low, YDAYS)) / float(YDAYS)


# ============================================================
# Bucket B — AVWAP from 252d-high anchor (013-022)
# ============================================================

def f15_avwx_013_log_dist_close_to_avwap_from_252d_high(high, low, close, volume):
    """Log distance close above (negative when below) AVWAP-from-252d-high — post-peak position."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    return _safe_log(close) - _safe_log(av)


def f15_avwx_014_atr_dist_close_to_avwap_from_252d_high(high, low, close, volume):
    """(close − AVWAP-from-252d-high) / ATR(21)."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    return _safe_div(close - av, _atr(high, low, close, n=MDAYS))


def f15_avwx_015_slope_avwap_from_252d_high_63d(high, low, close, volume):
    """Slope of AVWAP-from-252d-high over trailing 63d — post-peak AVWAP rate."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    return _rolling_slope(av, QDAYS)


def f15_avwx_016_zscore_dist_close_avwap_252dhigh_in_252d(high, low, close, volume):
    """Z-score of (close − AVWAP-from-252d-high)/close in 252d."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    return _rolling_zscore(_safe_div(close - av, close), YDAYS)


def f15_avwx_017_bars_since_252d_high_anchor(high, low, close):
    """Bars since most recent new 252d-high event."""
    return _bars_since_true(_event_mask_new_window_high(high, YDAYS))


def f15_avwx_018_indicator_close_crossed_below_avwap_252dhigh_in_21d(high, low, close, volume):
    """Indicator: close crossed below AVWAP-from-252d-high (close-prev>av, close<=av) within last 21d."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    cross = ((close.shift(1) > av.shift(1)) & (close <= av)).astype(float).where(av.notna(), np.nan)
    return (cross.rolling(MDAYS, min_periods=1).sum() > 0).astype(float)


def f15_avwx_019_count_crosses_avwap_from_252d_high_in_252d(high, low, close, volume):
    """Total close-crosses (above or below) of AVWAP-from-252d-high in trailing 252d."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    above = (close > av).astype(int).where(av.notna(), np.nan)
    cross = (above.diff().abs() > 0).astype(float)
    return cross.rolling(YDAYS, min_periods=QDAYS).sum()


def f15_avwx_020_max_drawdown_vs_avwap_from_252d_high_63d(high, low, close, volume):
    """Max log-drawdown of close vs AVWAP-from-252d-high over trailing 63d (most-negative log-distance)."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    d = _safe_log(close) - _safe_log(av)
    return d.rolling(QDAYS, min_periods=MDAYS).min()


def f15_avwx_021_pct_dist_close_to_avwap_from_252d_high(high, low, close, volume):
    """Percent distance close above AVWAP-from-252d-high."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    return _safe_div(close - av, av)


def f15_avwx_022_ratio_bars_below_above_avwap_from_252d_high_63d(high, low, close, volume):
    """Ratio of bars below to bars above AVWAP-from-252d-high in trailing 63d — post-peak structure."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    below = (close < av).astype(float).where(av.notna(), np.nan)
    above = (close > av).astype(float).where(av.notna(), np.nan)
    return _safe_div(below.rolling(QDAYS, min_periods=MDAYS).sum(), above.rolling(QDAYS, min_periods=MDAYS).sum())


# ============================================================
# Bucket C — AVWAP from 504d/1260d-low anchors (023-030)
# ============================================================

def f15_avwx_023_log_dist_close_to_avwap_from_504d_low(high, low, close, volume):
    """Log distance close above AVWAP from 2-year-low anchor (504d new-low events)."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, DDAYS_2Y))
    return _safe_log(close) - _safe_log(av)


def f15_avwx_024_atr_dist_close_to_avwap_from_504d_low(high, low, close, volume):
    """(close − AVWAP-from-504d-low) / ATR(63) — long-horizon stop-equivalent."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, DDAYS_2Y))
    return _safe_div(close - av, _atr(high, low, close, n=QDAYS))


def f15_avwx_025_log_dist_close_to_avwap_from_1260d_low(high, low, close, volume):
    """Log distance close above AVWAP from 5-year-low anchor — multi-year structural extension."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, DDAYS_5Y))
    return _safe_log(close) - _safe_log(av)


def f15_avwx_026_bars_since_504d_low_anchor(high, low, close):
    """Bars since most recent new 504d-low event."""
    return _bars_since_true(_event_mask_new_window_low(low, DDAYS_2Y))


def f15_avwx_027_bars_since_1260d_low_anchor(high, low, close):
    """Bars since most recent new 1260d-low event."""
    return _bars_since_true(_event_mask_new_window_low(low, DDAYS_5Y))


def f15_avwx_028_slope_avwap_from_504d_low_63d(high, low, close, volume):
    """Slope of AVWAP-from-504d-low over trailing 63d."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, DDAYS_2Y))
    return _rolling_slope(av, QDAYS)


def f15_avwx_029_slope_avwap_from_1260d_low_252d(high, low, close, volume):
    """Slope of AVWAP-from-1260d-low over trailing 252d."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, DDAYS_5Y))
    return _rolling_slope(av, YDAYS)


def f15_avwx_030_log_dist_close_to_mtd_anchored_vwap(high, low, close, volume):
    """Log distance close to MTD (month-to-date) anchored VWAP — cumulative VWAP since 1st trading day of each calendar month."""
    tp = _typical_price(high, low, close)
    if not isinstance(close.index, pd.DatetimeIndex):
        return pd.Series(np.nan, index=close.index)
    ym = pd.Series(close.index.year * 100 + close.index.month, index=close.index)
    anchor_mask = ym.diff().ne(0)
    anchor_mask.iloc[0] = True
    av = _anchored_vwap_from_event(tp, volume, anchor_mask)
    return _safe_log(close) - _safe_log(av)


# ============================================================
# Bucket D — AVWAP from 504d/1260d-high anchors (031-035)
# ============================================================

def f15_avwx_031_log_dist_close_to_avwap_from_504d_high(high, low, close, volume):
    """Log distance close above AVWAP from 504d-high anchor — multi-year peak position."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, DDAYS_2Y))
    return _safe_log(close) - _safe_log(av)


def f15_avwx_032_log_dist_close_to_avwap_from_1260d_high(high, low, close, volume):
    """Log distance close above AVWAP from 1260d-high anchor (5y peak)."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, DDAYS_5Y))
    return _safe_log(close) - _safe_log(av)


def f15_avwx_033_slope_avwap_from_504d_high_252d(high, low, close, volume):
    """Slope of AVWAP-from-504d-high over 252d — long-horizon AVWAP rate."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, DDAYS_2Y))
    return _rolling_slope(av, YDAYS)


def f15_avwx_034_bars_since_504d_high_anchor(high, low, close):
    """Bars since most recent new 504d-high event."""
    return _bars_since_true(_event_mask_new_window_high(high, DDAYS_2Y))


def f15_avwx_035_bars_since_1260d_high_anchor(high, low, close):
    """Bars since most recent new 1260d-high event."""
    return _bars_since_true(_event_mask_new_window_high(high, DDAYS_5Y))


# ============================================================
# Bucket E — Expanding all-time anchored AVWAP (IPO-proxy) (036-042)
# ============================================================

def f15_avwx_036_log_dist_close_to_expanding_avwap(high, low, close, volume):
    """Log distance close above expanding AVWAP from first known bar (IPO-proxy)."""
    tp = _typical_price(high, low, close)
    av = _expanding_avwap(tp, volume)
    return _safe_log(close) - _safe_log(av)


def f15_avwx_037_atr_dist_close_to_expanding_avwap(high, low, close, volume):
    """(close − expanding AVWAP) / ATR(63) — multi-year extension above IPO-proxy AVWAP."""
    tp = _typical_price(high, low, close)
    av = _expanding_avwap(tp, volume)
    return _safe_div(close - av, _atr(high, low, close, n=QDAYS))


def f15_avwx_038_slope_expanding_avwap_252d(high, low, close, volume):
    """Slope of expanding AVWAP over trailing 252d."""
    tp = _typical_price(high, low, close)
    av = _expanding_avwap(tp, volume)
    return _rolling_slope(av, YDAYS)


def f15_avwx_039_zscore_dist_close_expanding_avwap_252d(high, low, close, volume):
    """Z-score of (close − expanding AVWAP)/close in 252d window."""
    tp = _typical_price(high, low, close)
    av = _expanding_avwap(tp, volume)
    return _rolling_zscore(_safe_div(close - av, close), YDAYS)


def f15_avwx_040_pctile_rank_dist_close_expanding_avwap_252d(high, low, close, volume):
    """Empirical percentile rank of (close − expanding AVWAP)/close in 252d."""
    tp = _typical_price(high, low, close)
    av = _expanding_avwap(tp, volume)
    raw = _safe_div(close - av, close)
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        v = w[~np.isnan(w)]
        return float((v <= last).sum()) / float(v.size) if v.size else np.nan
    return raw.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)


def f15_avwx_041_bars_since_first_known_bar(high, low, close):
    """Expanding count of bars since first known bar — IPO-proxy anchor age."""
    arr = close.notna().astype(int).values
    nb = len(arr)
    out = np.full(nb, np.nan)
    seen = False
    counter = 0
    for i in range(nb):
        if arr[i]:
            seen = True
        if seen:
            out[i] = float(counter)
            counter += 1
    return pd.Series(out, index=close.index)


def f15_avwx_042_residual_std_close_expanding_avwap_252d(high, low, close, volume):
    """Std of (close − expanding AVWAP) over trailing 252d — residual volatility around IPO-proxy AVWAP."""
    tp = _typical_price(high, low, close)
    av = _expanding_avwap(tp, volume)
    return (close - av).rolling(YDAYS, min_periods=QDAYS).std()


# ============================================================
# Bucket F — Rolling-window AVWAPs (043-060)
# ============================================================

def f15_avwx_043_log_dist_close_to_rolling_avwap_21d(high, low, close, volume):
    """Log distance close above rolling-21d AVWAP — short-term volume-weighted reference."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, MDAYS)
    return _safe_log(close) - _safe_log(av)


def f15_avwx_044_log_dist_close_to_rolling_avwap_63d(high, low, close, volume):
    """Log distance close above rolling-63d AVWAP."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, QDAYS)
    return _safe_log(close) - _safe_log(av)


def f15_avwx_045_position_close_in_rolling_vwap_252d_1sigma_band(high, low, close, volume):
    """Position of close in (rolling-252d VWAP ± 1σ vol-weighted) band — institutional ±1σ envelope position."""
    tp = _typical_price(high, low, close)
    u, m, l = _vwap_sigma_band(tp, volume, YDAYS, 1.0)
    return _safe_div(close - l, u - l)


def f15_avwx_046_log_dist_close_to_rolling_avwap_252d(high, low, close, volume):
    """Log distance close above rolling-252d AVWAP."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, YDAYS)
    return _safe_log(close) - _safe_log(av)


def f15_avwx_047_log_dist_close_to_rolling_avwap_504d(high, low, close, volume):
    """Log distance close above rolling-504d (2y) AVWAP."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, DDAYS_2Y)
    return _safe_log(close) - _safe_log(av)


def f15_avwx_048_volume_profile_poc_drift_velocity_63d(high, low, close, volume):
    """(POC_now − POC_63d_ago) / close — Point-of-Control drift velocity. Rising POC = healthy migration; flat = distribution."""
    tp = _typical_price(high, low, close)
    poc = _volume_profile_poc(tp, volume, YDAYS, n_bins=20)
    return _safe_div(poc - poc.shift(QDAYS), close)


def f15_avwx_049_ratio_close_dist_21d_to_252d_avwap(high, low, close, volume):
    """(close − rolling-21d AVWAP) / (close − rolling-252d AVWAP) — fast vs slow extension ratio."""
    tp = _typical_price(high, low, close)
    a21 = _rolling_avwap(tp, volume, MDAYS)
    a252 = _rolling_avwap(tp, volume, YDAYS)
    return _safe_div(close - a21, close - a252)


def f15_avwx_050_zscore_dist_close_rolling_avwap_252d_in_252d(high, low, close, volume):
    """Z-score of (close − rolling-252d AVWAP)/close in 252d."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, YDAYS)
    return _rolling_zscore(_safe_div(close - av, close), YDAYS)


def f15_avwx_051_atr_dist_close_to_rolling_avwap_63d(high, low, close, volume):
    """(close − rolling-63d AVWAP) / ATR(21)."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, QDAYS)
    return _safe_div(close - av, _atr(high, low, close, n=MDAYS))


def f15_avwx_052_slope_rolling_avwap_21d_over_21d(high, low, close, volume):
    """Slope of rolling-21d AVWAP over trailing 21d."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, MDAYS)
    return _rolling_slope(av, MDAYS)


def f15_avwx_053_log_dist_close_to_volume_profile_poc_504d(high, low, close, volume):
    """Log distance close to POC in trailing-504d (2y) volume profile — longer-horizon POC than f116 (252d)."""
    tp = _typical_price(high, low, close)
    poc = _volume_profile_poc(tp, volume, DDAYS_2Y, n_bins=20)
    return _safe_log(close) - _safe_log(poc)


def f15_avwx_054_diff_fast_slow_rolling_avwap_norm_close(high, low, close, volume):
    """(rolling-21d AVWAP − rolling-252d AVWAP) / close — fast vs slow VWAP spread."""
    tp = _typical_price(high, low, close)
    a21 = _rolling_avwap(tp, volume, MDAYS)
    a252 = _rolling_avwap(tp, volume, YDAYS)
    return _safe_div(a21 - a252, close)


def f15_avwx_055_mean_reversion_target_dist_rolling_252d_avwap(high, low, close, volume):
    """rolling-252d AVWAP / close − 1 — mean-reversion target distance (negative when extended)."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, YDAYS)
    return _safe_div(av, close) - 1.0


def f15_avwx_056_cross_count_21d_vs_63d_rolling_avwap_252d(high, low, close, volume):
    """Count of rolling-21d-AVWAP / rolling-63d-AVWAP crosses in 252d."""
    tp = _typical_price(high, low, close)
    a21 = _rolling_avwap(tp, volume, MDAYS)
    a63 = _rolling_avwap(tp, volume, QDAYS)
    above = (a21 > a63).astype(int).where(a21.notna() & a63.notna(), np.nan)
    cross = (above.diff().abs() > 0).astype(float)
    return cross.rolling(YDAYS, min_periods=QDAYS).sum()


def f15_avwx_057_bars_since_close_crossed_below_rolling_avwap_252d(high, low, close, volume):
    """Bars since most recent close-cross-below rolling-252d AVWAP."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, YDAYS)
    cross = ((close.shift(1) > av.shift(1)) & (close <= av)).astype(bool)
    return _bars_since_true(cross)


def f15_avwx_058_frac_bars_close_above_rolling_avwap_252d_in_252d(high, low, close, volume):
    """Fraction of bars in 252d where close > rolling-252d AVWAP."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, YDAYS)
    above = (close > av).astype(float).where(av.notna(), np.nan)
    return above.rolling(YDAYS, min_periods=QDAYS).mean()


def f15_avwx_059_cum_dev_close_rolling_avwap_252d_in_63d(high, low, close, volume):
    """Σ (close − rolling-252d AVWAP)/close over 63d — cumulative-deviation magnitude."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, YDAYS)
    return _safe_div(close - av, close).rolling(QDAYS, min_periods=MDAYS).sum()


def f15_avwx_060_max_log_dist_close_above_rolling_avwap_252d_21d(high, low, close, volume):
    """Max log-distance close above rolling-252d AVWAP over trailing 21d."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, YDAYS)
    d = _safe_log(close) - _safe_log(av)
    return d.rolling(MDAYS, min_periods=WDAYS).max()


# ============================================================
# Bucket G — AVWAP slope / velocity / acceleration (061-068)
# ============================================================

def f15_avwx_061_slope_avwap_from_252d_low_over_21d(high, low, close, volume):
    """Short-horizon slope (21d) of AVWAP-from-52w-low — anchor-AVWAP velocity, monthly view."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    return _rolling_slope(av, MDAYS)


def f15_avwx_062_slope_avwap_from_252d_high_over_21d(high, low, close, volume):
    """Short-horizon slope (21d) of AVWAP-from-252d-high — post-peak anchor-AVWAP velocity."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    return _rolling_slope(av, MDAYS)


def f15_avwx_063_slope_expanding_avwap_over_63d(high, low, close, volume):
    """Slope of expanding (IPO-proxy) AVWAP over trailing 63d."""
    tp = _typical_price(high, low, close)
    av = _expanding_avwap(tp, volume)
    return _rolling_slope(av, QDAYS)


def f15_avwx_064_curvature_fast_slow_rolling_avwap_slope_diff(high, low, close, volume):
    """Slope of rolling-21d AVWAP − slope of rolling-252d AVWAP (both 21d window) — curvature proxy."""
    tp = _typical_price(high, low, close)
    a21 = _rolling_avwap(tp, volume, MDAYS)
    a252 = _rolling_avwap(tp, volume, YDAYS)
    return _rolling_slope(a21, MDAYS) - _rolling_slope(a252, MDAYS)


def f15_avwx_065_acceleration_rolling_avwap_21d(high, low, close, volume):
    """Second-difference (acceleration) of rolling-21d AVWAP smoothed 5d."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, MDAYS)
    return av.diff().diff().rolling(WDAYS, min_periods=2).mean()


def f15_avwx_066_volume_profile_asymmetry_252d(high, low, close, volume):
    """Σ(volume above mid_typical) / Σ(volume below mid_typical) in 252d. >1 = top-heavy (distribution); <1 = bottom-heavy (accumulation)."""
    tp = _typical_price(high, low, close)
    return _volume_profile_asymmetry(tp, volume, YDAYS)


def f15_avwx_067_slope_avwap_from_504d_low_over_252d(high, low, close, volume):
    """Slope of AVWAP-from-504d-low over 252d — long-trend anchor-AVWAP slope."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, DDAYS_2Y))
    return _rolling_slope(av, YDAYS)


def f15_avwx_068_slope_decay_rolling_avwap_252d(high, low, close, volume):
    """Δ slope of rolling-252d AVWAP between now and 63d ago — slope-decay/acceleration of long AVWAP."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, YDAYS)
    sl = _rolling_slope(av, QDAYS)
    return sl - sl.shift(QDAYS)


# ============================================================
# Bucket H — Multi-anchor agreement / spread (069-075)
# ============================================================

def f15_avwx_069_count_anchors_below_close(high, low, close, volume):
    """Count of (AVWAP-from 52w-low / 252d-high / 504d-low / IPO-proxy) below current close."""
    tp = _typical_price(high, low, close)
    a1 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    a2 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    a3 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, DDAYS_2Y))
    a4 = _expanding_avwap(tp, volume)
    return ((close > a1).astype(float).fillna(0) + (close > a2).astype(float).fillna(0)
            + (close > a3).astype(float).fillna(0) + (close > a4).astype(float).fillna(0))


def f15_avwx_070_std_anchors_avwap(high, low, close, volume):
    """Std across (4 anchor AVWAPs) at current bar — anchor dispersion."""
    tp = _typical_price(high, low, close)
    a1 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    a2 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    a3 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, DDAYS_2Y))
    a4 = _expanding_avwap(tp, volume)
    pieces = pd.concat([a1.rename("a1"), a2.rename("a2"), a3.rename("a3"), a4.rename("a4")], axis=1)
    return pieces.std(axis=1)


def f15_avwx_071_range_ratio_anchors_max_to_min(high, low, close, volume):
    """Max-anchor-AVWAP / min-anchor-AVWAP — range ratio across anchor set."""
    tp = _typical_price(high, low, close)
    a1 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    a2 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    a3 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, DDAYS_2Y))
    a4 = _expanding_avwap(tp, volume)
    pieces = pd.concat([a1.rename("a1"), a2.rename("a2"), a3.rename("a3"), a4.rename("a4")], axis=1)
    return _safe_div(pieces.max(axis=1), pieces.min(axis=1))


def f15_avwx_072_spread_avwap_52wlow_minus_252dhigh_norm_close(high, low, close, volume):
    """(AVWAP-52w-low − AVWAP-252d-high) / close — structural anchor spread."""
    tp = _typical_price(high, low, close)
    a1 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    a2 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    return _safe_div(a1 - a2, close)


def f15_avwx_073_count_anchors_extended_above_by_1atr(high, low, close, volume):
    """Count of anchor AVWAPs where close > anchor AVWAP by ≥ 1×ATR(21)."""
    tp = _typical_price(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    a1 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    a2 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    a3 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, DDAYS_2Y))
    a4 = _expanding_avwap(tp, volume)
    return ((close - a1 > atr).astype(float).fillna(0)
            + (close - a2 > atr).astype(float).fillna(0)
            + (close - a3 > atr).astype(float).fillna(0)
            + (close - a4 > atr).astype(float).fillna(0))


def f15_avwx_074_anchor_spread_compression_ratio_252d(high, low, close, volume):
    """Current anchor-AVWAP std / 252d-mean of anchor-AVWAP std — compression < 1 = squeeze."""
    tp = _typical_price(high, low, close)
    a1 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    a2 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    a3 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, DDAYS_2Y))
    a4 = _expanding_avwap(tp, volume)
    pieces = pd.concat([a1.rename("a1"), a2.rename("a2"), a3.rename("a3"), a4.rename("a4")], axis=1)
    s = pieces.std(axis=1)
    return _safe_div(s, s.rolling(YDAYS, min_periods=QDAYS).mean())


def f15_avwx_075_indicator_close_above_all_four_anchors(high, low, close, volume):
    """Indicator: close > each of (4 anchor AVWAPs) — full anchor-bullish alignment."""
    tp = _typical_price(high, low, close)
    a1 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    a2 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    a3 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, DDAYS_2Y))
    a4 = _expanding_avwap(tp, volume)
    return ((close > a1) & (close > a2) & (close > a3) & (close > a4)).astype(float)


# ============================================================
#                         REGISTRY 001-075
# ============================================================

ANCHORED_VWAP_EXTENSION_BASE_REGISTRY_001_075 = {
    "f15_avwx_001_log_dist_close_to_avwap_from_252d_low": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_001_log_dist_close_to_avwap_from_252d_low},
    "f15_avwx_002_atr_dist_close_to_avwap_from_252d_low": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_002_atr_dist_close_to_avwap_from_252d_low},
    "f15_avwx_003_pct_dist_close_to_avwap_from_252d_low": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_003_pct_dist_close_to_avwap_from_252d_low},
    "f15_avwx_004_bars_since_252d_low_anchor": {"inputs": ["high", "low", "close"], "func": f15_avwx_004_bars_since_252d_low_anchor},
    "f15_avwx_005_slope_avwap_from_252d_low_21d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_005_slope_avwap_from_252d_low_21d},
    "f15_avwx_006_zscore_dist_close_avwap_252dlow_in_252d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_006_zscore_dist_close_avwap_252dlow_in_252d},
    "f15_avwx_007_pctile_rank_dist_close_avwap_252dlow_252d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_007_pctile_rank_dist_close_avwap_252dlow_252d},
    "f15_avwx_008_close_position_in_avwap_sigma_band_252dlow": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_008_close_position_in_avwap_sigma_band_252dlow},
    "f15_avwx_009_frac_bars_close_above_avwap_from_252d_low_63d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_009_frac_bars_close_above_avwap_from_252d_low_63d},
    "f15_avwx_010_max_log_dist_close_avwap_252dlow_21d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_010_max_log_dist_close_avwap_252dlow_21d},
    "f15_avwx_011_half_life_dev_close_avwap_252dlow_252d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_011_half_life_dev_close_avwap_252dlow_252d},
    "f15_avwx_012_years_since_52w_low": {"inputs": ["high", "low", "close"], "func": f15_avwx_012_years_since_52w_low},
    "f15_avwx_013_log_dist_close_to_avwap_from_252d_high": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_013_log_dist_close_to_avwap_from_252d_high},
    "f15_avwx_014_atr_dist_close_to_avwap_from_252d_high": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_014_atr_dist_close_to_avwap_from_252d_high},
    "f15_avwx_015_slope_avwap_from_252d_high_63d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_015_slope_avwap_from_252d_high_63d},
    "f15_avwx_016_zscore_dist_close_avwap_252dhigh_in_252d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_016_zscore_dist_close_avwap_252dhigh_in_252d},
    "f15_avwx_017_bars_since_252d_high_anchor": {"inputs": ["high", "low", "close"], "func": f15_avwx_017_bars_since_252d_high_anchor},
    "f15_avwx_018_indicator_close_crossed_below_avwap_252dhigh_in_21d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_018_indicator_close_crossed_below_avwap_252dhigh_in_21d},
    "f15_avwx_019_count_crosses_avwap_from_252d_high_in_252d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_019_count_crosses_avwap_from_252d_high_in_252d},
    "f15_avwx_020_max_drawdown_vs_avwap_from_252d_high_63d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_020_max_drawdown_vs_avwap_from_252d_high_63d},
    "f15_avwx_021_pct_dist_close_to_avwap_from_252d_high": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_021_pct_dist_close_to_avwap_from_252d_high},
    "f15_avwx_022_ratio_bars_below_above_avwap_from_252d_high_63d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_022_ratio_bars_below_above_avwap_from_252d_high_63d},
    "f15_avwx_023_log_dist_close_to_avwap_from_504d_low": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_023_log_dist_close_to_avwap_from_504d_low},
    "f15_avwx_024_atr_dist_close_to_avwap_from_504d_low": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_024_atr_dist_close_to_avwap_from_504d_low},
    "f15_avwx_025_log_dist_close_to_avwap_from_1260d_low": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_025_log_dist_close_to_avwap_from_1260d_low},
    "f15_avwx_026_bars_since_504d_low_anchor": {"inputs": ["high", "low", "close"], "func": f15_avwx_026_bars_since_504d_low_anchor},
    "f15_avwx_027_bars_since_1260d_low_anchor": {"inputs": ["high", "low", "close"], "func": f15_avwx_027_bars_since_1260d_low_anchor},
    "f15_avwx_028_slope_avwap_from_504d_low_63d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_028_slope_avwap_from_504d_low_63d},
    "f15_avwx_029_slope_avwap_from_1260d_low_252d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_029_slope_avwap_from_1260d_low_252d},
    "f15_avwx_030_log_dist_close_to_mtd_anchored_vwap": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_030_log_dist_close_to_mtd_anchored_vwap},
    "f15_avwx_031_log_dist_close_to_avwap_from_504d_high": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_031_log_dist_close_to_avwap_from_504d_high},
    "f15_avwx_032_log_dist_close_to_avwap_from_1260d_high": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_032_log_dist_close_to_avwap_from_1260d_high},
    "f15_avwx_033_slope_avwap_from_504d_high_252d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_033_slope_avwap_from_504d_high_252d},
    "f15_avwx_034_bars_since_504d_high_anchor": {"inputs": ["high", "low", "close"], "func": f15_avwx_034_bars_since_504d_high_anchor},
    "f15_avwx_035_bars_since_1260d_high_anchor": {"inputs": ["high", "low", "close"], "func": f15_avwx_035_bars_since_1260d_high_anchor},
    "f15_avwx_036_log_dist_close_to_expanding_avwap": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_036_log_dist_close_to_expanding_avwap},
    "f15_avwx_037_atr_dist_close_to_expanding_avwap": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_037_atr_dist_close_to_expanding_avwap},
    "f15_avwx_038_slope_expanding_avwap_252d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_038_slope_expanding_avwap_252d},
    "f15_avwx_039_zscore_dist_close_expanding_avwap_252d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_039_zscore_dist_close_expanding_avwap_252d},
    "f15_avwx_040_pctile_rank_dist_close_expanding_avwap_252d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_040_pctile_rank_dist_close_expanding_avwap_252d},
    "f15_avwx_041_bars_since_first_known_bar": {"inputs": ["high", "low", "close"], "func": f15_avwx_041_bars_since_first_known_bar},
    "f15_avwx_042_residual_std_close_expanding_avwap_252d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_042_residual_std_close_expanding_avwap_252d},
    "f15_avwx_043_log_dist_close_to_rolling_avwap_21d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_043_log_dist_close_to_rolling_avwap_21d},
    "f15_avwx_044_log_dist_close_to_rolling_avwap_63d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_044_log_dist_close_to_rolling_avwap_63d},
    "f15_avwx_045_position_close_in_rolling_vwap_252d_1sigma_band": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_045_position_close_in_rolling_vwap_252d_1sigma_band},
    "f15_avwx_046_log_dist_close_to_rolling_avwap_252d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_046_log_dist_close_to_rolling_avwap_252d},
    "f15_avwx_047_log_dist_close_to_rolling_avwap_504d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_047_log_dist_close_to_rolling_avwap_504d},
    "f15_avwx_048_volume_profile_poc_drift_velocity_63d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_048_volume_profile_poc_drift_velocity_63d},
    "f15_avwx_049_ratio_close_dist_21d_to_252d_avwap": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_049_ratio_close_dist_21d_to_252d_avwap},
    "f15_avwx_050_zscore_dist_close_rolling_avwap_252d_in_252d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_050_zscore_dist_close_rolling_avwap_252d_in_252d},
    "f15_avwx_051_atr_dist_close_to_rolling_avwap_63d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_051_atr_dist_close_to_rolling_avwap_63d},
    "f15_avwx_052_slope_rolling_avwap_21d_over_21d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_052_slope_rolling_avwap_21d_over_21d},
    "f15_avwx_053_log_dist_close_to_volume_profile_poc_504d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_053_log_dist_close_to_volume_profile_poc_504d},
    "f15_avwx_054_diff_fast_slow_rolling_avwap_norm_close": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_054_diff_fast_slow_rolling_avwap_norm_close},
    "f15_avwx_055_mean_reversion_target_dist_rolling_252d_avwap": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_055_mean_reversion_target_dist_rolling_252d_avwap},
    "f15_avwx_056_cross_count_21d_vs_63d_rolling_avwap_252d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_056_cross_count_21d_vs_63d_rolling_avwap_252d},
    "f15_avwx_057_bars_since_close_crossed_below_rolling_avwap_252d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_057_bars_since_close_crossed_below_rolling_avwap_252d},
    "f15_avwx_058_frac_bars_close_above_rolling_avwap_252d_in_252d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_058_frac_bars_close_above_rolling_avwap_252d_in_252d},
    "f15_avwx_059_cum_dev_close_rolling_avwap_252d_in_63d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_059_cum_dev_close_rolling_avwap_252d_in_63d},
    "f15_avwx_060_max_log_dist_close_above_rolling_avwap_252d_21d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_060_max_log_dist_close_above_rolling_avwap_252d_21d},
    "f15_avwx_061_slope_avwap_from_252d_low_over_21d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_061_slope_avwap_from_252d_low_over_21d},
    "f15_avwx_062_slope_avwap_from_252d_high_over_21d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_062_slope_avwap_from_252d_high_over_21d},
    "f15_avwx_063_slope_expanding_avwap_over_63d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_063_slope_expanding_avwap_over_63d},
    "f15_avwx_064_curvature_fast_slow_rolling_avwap_slope_diff": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_064_curvature_fast_slow_rolling_avwap_slope_diff},
    "f15_avwx_065_acceleration_rolling_avwap_21d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_065_acceleration_rolling_avwap_21d},
    "f15_avwx_066_volume_profile_asymmetry_252d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_066_volume_profile_asymmetry_252d},
    "f15_avwx_067_slope_avwap_from_504d_low_over_252d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_067_slope_avwap_from_504d_low_over_252d},
    "f15_avwx_068_slope_decay_rolling_avwap_252d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_068_slope_decay_rolling_avwap_252d},
    "f15_avwx_069_count_anchors_below_close": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_069_count_anchors_below_close},
    "f15_avwx_070_std_anchors_avwap": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_070_std_anchors_avwap},
    "f15_avwx_071_range_ratio_anchors_max_to_min": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_071_range_ratio_anchors_max_to_min},
    "f15_avwx_072_spread_avwap_52wlow_minus_252dhigh_norm_close": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_072_spread_avwap_52wlow_minus_252dhigh_norm_close},
    "f15_avwx_073_count_anchors_extended_above_by_1atr": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_073_count_anchors_extended_above_by_1atr},
    "f15_avwx_074_anchor_spread_compression_ratio_252d": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_074_anchor_spread_compression_ratio_252d},
    "f15_avwx_075_indicator_close_above_all_four_anchors": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_075_indicator_close_above_all_four_anchors},
}
