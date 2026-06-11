"""15_anchored_vwap_extension d1 features 076-150 — order-1 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff(). Self-contained; helpers redefined locally per HANDOFF."""
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

def _typical_price(high, low, close):
    return (high + low + close) / 3.0

def _rolling_avwap(typical, volume, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    pv = (typical * volume).rolling(window, min_periods=min_periods).sum()
    v = volume.rolling(window, min_periods=min_periods).sum()
    return _safe_div(pv, v)

def _anchored_vwap_from_event(typical, volume, anchor_mask):
    aid = anchor_mask.fillna(False).astype(int).cumsum()
    pv = typical * volume
    pv_cum = pv.groupby(aid).cumsum()
    v_cum = volume.groupby(aid).cumsum()
    out = _safe_div(pv_cum, v_cum)
    return out.where(aid > 0, np.nan)

def _expanding_avwap(typical, volume):
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
            last = i
            out[i] = 0.0
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
    rmin = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return (low <= rmin) & rmin.notna()

def _event_mask_new_window_high(high, n):
    rmax = high.rolling(n, min_periods=max(n // 3, 2)).max()
    return (high >= rmax) & rmax.notna()

def _event_mask_high_volume(volume, n, q):
    """True when volume >= q-th percentile of trailing-n window."""
    qv = volume.rolling(n, min_periods=max(n // 3, 2)).quantile(q)
    return (volume >= qv) & qv.notna()

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
    return (vwap + k * vwstd, vwap, vwap - k * vwstd)

def _volume_profile_poc(typical, volume, window, n_bins=20, min_periods=None):
    """Point of Control: price-bin with max volume in trailing window. Returns Series of POC price."""
    if min_periods is None:
        min_periods = max(window // 3, 2)
    p = typical.values
    v = volume.values
    nb = len(p)
    out = np.full(nb, np.nan)
    for i in range(nb):
        s = max(0, i - window + 1)
        if i - s + 1 < min_periods:
            continue
        wp = p[s:i + 1]
        wv = v[s:i + 1]
        valid = ~(np.isnan(wp) | np.isnan(wv))
        if valid.sum() < min_periods:
            continue
        wp = wp[valid]
        wv = wv[valid]
        lo, hi = (wp.min(), wp.max())
        if hi <= lo:
            out[i] = lo
            continue
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
    p = typical.values
    v = volume.values
    nb = len(p)
    vah_out = np.full(nb, np.nan)
    val_out = np.full(nb, np.nan)
    for i in range(nb):
        s = max(0, i - window + 1)
        if i - s + 1 < min_periods:
            continue
        wp = p[s:i + 1]
        wv = v[s:i + 1]
        valid = ~(np.isnan(wp) | np.isnan(wv))
        if valid.sum() < min_periods:
            continue
        wp = wp[valid]
        wv = wv[valid]
        lo, hi = (wp.min(), wp.max())
        if hi <= lo:
            vah_out[i] = hi
            val_out[i] = lo
            continue
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
                hi_bin += 1
                acc += bin_vol[hi_bin]
            else:
                lo_bin -= 1
                acc += bin_vol[lo_bin]
        vah_out[i] = lo + (hi_bin + 1) * (hi - lo) / n_bins
        val_out[i] = lo + lo_bin * (hi - lo) / n_bins
    return (pd.Series(vah_out, index=typical.index), pd.Series(val_out, index=typical.index))

def _twap(typical, window, min_periods=None):
    """Time-weighted average price (simple SMA of typical price)."""
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return typical.rolling(window, min_periods=min_periods).mean()

def _largest_gap_up_anchor_mask(open_, close, n):
    """True at the bar with the largest gap-up ((open - prev_close)/prev_close) in trailing n window."""
    gap = _safe_div(open_ - close.shift(1), close.shift(1))
    rmax = gap.rolling(n, min_periods=max(n // 3, 2)).max()
    return (gap >= rmax) & gap.notna() & (gap > 0)

def _volume_profile_lvn_indicator(typical, volume, close, window, n_bins=20, pct=0.25, min_periods=None):
    """Indicator: close is in a price bin whose volume is below pct-th percentile of all bins in trailing window."""
    if min_periods is None:
        min_periods = max(window // 3, 2)
    p = typical.values
    v = volume.values
    c = close.values
    nb = len(p)
    out = np.full(nb, np.nan)
    for i in range(nb):
        s = max(0, i - window + 1)
        if i - s + 1 < min_periods:
            continue
        wp = p[s:i + 1]
        wv = v[s:i + 1]
        valid = ~(np.isnan(wp) | np.isnan(wv))
        if valid.sum() < min_periods:
            continue
        wp = wp[valid]
        wv = wv[valid]
        lo, hi = (wp.min(), wp.max())
        if hi <= lo or np.isnan(c[i]):
            continue
        bin_idx = np.minimum(((wp - lo) / (hi - lo) * n_bins).astype(int), n_bins - 1)
        bin_vol = np.zeros(n_bins)
        for j in range(len(bin_idx)):
            bin_vol[bin_idx[j]] += wv[j]
        if c[i] < lo or c[i] > hi:
            out[i] = 1.0
            continue
        close_bin = min(int((c[i] - lo) / (hi - lo) * n_bins), n_bins - 1)
        threshold = float(np.quantile(bin_vol, pct))
        out[i] = 1.0 if bin_vol[close_bin] < threshold else 0.0
    return pd.Series(out, index=typical.index)

def _four_anchor_avwaps(high, low, close, volume):
    tp = _typical_price(high, low, close)
    a1 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    a2 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    a3 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, DDAYS_2Y))
    a4 = _expanding_avwap(tp, volume)
    return (a1, a2, a3, a4)

def _rolling_corr_r2(y, x, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    return y.rolling(n, min_periods=min_periods).corr(x) ** 2

def f15_avwx_076_bars_since_close_crossed_below_avwap_from_252d_low_d1(high, low, close, volume):
    """Bars since most recent close-cross-below AVWAP-from-52w-low (close prev>av and now<=av)."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    cross = ((close.shift(1) > av.shift(1)) & (close <= av)).astype(bool)
    return _bars_since_true(cross).diff()

def f15_avwx_077_count_close_crosses_avwap_from_252d_low_252d_d1(high, low, close, volume):
    """Total close-crosses of AVWAP-from-52w-low in trailing 252d (above-to-below or back)."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    above = (close > av).astype(int).where(av.notna(), np.nan)
    cross = (above.diff().abs() > 0).astype(float)
    return cross.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f15_avwx_078_bars_since_close_crossed_below_avwap_from_252d_high_d1(high, low, close, volume):
    """Bars since most recent close-cross-below AVWAP-from-252d-high."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    cross = ((close.shift(1) > av.shift(1)) & (close <= av)).astype(bool)
    return _bars_since_true(cross).diff()

def f15_avwx_079_count_close_crosses_rolling_avwap_21d_63d_d1(high, low, close, volume):
    """Count of close-crosses of rolling-21d AVWAP in trailing 63d."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, MDAYS)
    above = (close > av).astype(int).where(av.notna(), np.nan)
    cross = (above.diff().abs() > 0).astype(float)
    return cross.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f15_avwx_080_count_close_crosses_rolling_avwap_252d_252d_d1(high, low, close, volume):
    """Count of close-crosses of rolling-252d AVWAP in trailing 252d."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, YDAYS)
    above = (close > av).astype(int).where(av.notna(), np.nan)
    cross = (above.diff().abs() > 0).astype(float)
    return cross.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f15_avwx_081_first_cross_below_avwap_252dlow_after_new_252d_high_d1(high, low, close, volume):
    """Indicator: most recent 252d-high was followed (within 63d) by a close-cross-below AVWAP-from-52w-low."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    cross = ((close.shift(1) > av.shift(1)) & (close <= av)).astype(int).where(av.notna(), 0).astype(int)
    bsp = _bars_since_true(_event_mask_new_window_high(high, YDAYS))
    bsc = _bars_since_true(cross.astype(bool))
    cond = bsc.notna() & bsp.notna() & (bsc < bsp) & (bsp - bsc <= QDAYS)
    return cond.astype(float).diff()

def f15_avwx_082_indicator_close_crossed_expanding_avwap_in_5d_d1(high, low, close, volume):
    """Indicator: close crossed expanding AVWAP (either direction) within last 5d."""
    tp = _typical_price(high, low, close)
    av = _expanding_avwap(tp, volume)
    above = (close > av).astype(int).where(av.notna(), np.nan)
    cross = (above.diff().abs() > 0).astype(float)
    return (cross.rolling(WDAYS, min_periods=1).sum() > 0).astype(float).diff()

def f15_avwx_083_cross_rate_rolling_avwap_21d_per_bar_63d_d1(high, low, close, volume):
    """Crosses-per-bar of rolling-21d AVWAP averaged over 63d (frequency)."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, MDAYS)
    above = (close > av).astype(int).where(av.notna(), np.nan)
    cross = (above.diff().abs() > 0).astype(float)
    return cross.rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f15_avwx_084_std_cross_spacings_rolling_avwap_252d_d1(high, low, close, volume):
    """Std of inter-cross spacings of rolling-252d AVWAP in trailing 252d — cross irregularity."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, YDAYS)
    above = (close > av).astype(int).where(av.notna(), np.nan)
    cross = (above.diff().abs() > 0).astype(bool)

    def _stdgap(w):
        idx = np.flatnonzero(w)
        if idx.size < 3:
            return np.nan
        return float(np.diff(idx).std())
    return cross.rolling(YDAYS, min_periods=QDAYS).apply(_stdgap, raw=True).diff()

def f15_avwx_085_signed_bars_since_cross_avwap_from_252d_low_d1(high, low, close, volume):
    """Bars-since-most-recent-cross of AVWAP-from-52w-low, signed (+ if close above, − if below)."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    above = (close > av).astype(int).where(av.notna(), np.nan)
    cross = (above.diff().abs() > 0).astype(bool)
    bsc = _bars_since_true(cross)
    sign = above.replace(0, -1).fillna(0)
    return (bsc * sign).diff()

def f15_avwx_086_frac_clinging_rolling_avwap_21d_in_21d_d1(high, low, close, volume):
    """Fraction of bars in 21d where |close − rolling-21d AVWAP|/close < 0.005 — clinging to fast AVWAP."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, MDAYS)
    cling = (_safe_div((close - av).abs(), close) < 0.005).astype(float)
    return cling.rolling(MDAYS, min_periods=WDAYS).mean().diff()

def f15_avwx_087_frac_close_above_rolling_avwap_252d_by_10pct_63d_d1(high, low, close, volume):
    """Fraction of bars in 63d where close > rolling-252d AVWAP × 1.10 — sustained 10%+ extension."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, YDAYS)
    ext = (close > 1.1 * av).astype(float).where(av.notna(), np.nan)
    return ext.rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f15_avwx_088_frac_close_above_avwap_from_252d_low_by_20pct_63d_d1(high, low, close, volume):
    """Fraction of bars in 63d where close > AVWAP-from-52w-low × 1.20."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    ext = (close > 1.2 * av).astype(float).where(av.notna(), np.nan)
    return ext.rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f15_avwx_089_max_consec_bars_close_above_rolling_avwap_21d_252d_d1(high, low, close, volume):
    """Longest run of consecutive bars in 252d with close > rolling-21d AVWAP."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, MDAYS)
    above = (close > av).astype(float).where(av.notna(), np.nan)

    def _longest(w):
        run = best = 0
        for v in w:
            if v > 0:
                run += 1
                if run > best:
                    best = run
            elif np.isnan(v):
                run = 0
            else:
                run = 0
        return float(best)
    return above.rolling(YDAYS, min_periods=QDAYS).apply(_longest, raw=True).diff()

def f15_avwx_090_frac_close_within_half_sigma_rolling_avwap_63d_in_21d_d1(high, low, close, volume):
    """Fraction of bars in 21d where |close − rolling-63d AVWAP| < 0.5 × σ_63d (σ = 63d return std × close)."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, QDAYS)
    sigma = close.pct_change().rolling(QDAYS, min_periods=MDAYS).std() * close
    near = ((close - av).abs() < 0.5 * sigma).astype(float)
    return near.rolling(MDAYS, min_periods=WDAYS).mean().diff()

def f15_avwx_091_cum_time_extended_above_avwap_52wlow_by_50pct_252d_d1(high, low, close, volume):
    """Cumulative bars in 252d where close > AVWAP-from-52w-low × 1.50."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    ext = (close > 1.5 * av).astype(float).where(av.notna(), np.nan)
    return ext.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f15_avwx_092_indicator_5_of_5_bars_above_rolling_avwap_252d_d1(high, low, close, volume):
    """Indicator: each of last 5 bars closed above rolling-252d AVWAP."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, YDAYS)
    above = (close > av).astype(int).where(av.notna(), np.nan)
    return (above.rolling(WDAYS, min_periods=WDAYS).sum() == WDAYS).astype(float).where(av.notna(), np.nan).diff()

def f15_avwx_093_pctile_rank_dist_close_avwap_52wlow_252d_d1(high, low, close, volume):
    """Empirical percentile rank of (close − AVWAP-from-52w-low)/close in 252d (variant of f007 anchor)."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    raw = _safe_div(close - av, close)

    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        v = w[~np.isnan(w)]
        return float((v <= last).sum()) / float(v.size) if v.size else np.nan
    return raw.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True).diff()

def f15_avwx_094_pctile_rank_dist_close_avwap_252dhigh_252d_d1(high, low, close, volume):
    """Empirical percentile rank of (close − AVWAP-from-252d-high)/close in 252d."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    raw = _safe_div(close - av, close)

    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        v = w[~np.isnan(w)]
        return float((v <= last).sum()) / float(v.size) if v.size else np.nan
    return raw.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True).diff()

def f15_avwx_095_pctile_rank_dist_close_rolling_avwap_252d_504d_d1(high, low, close, volume):
    """Empirical percentile rank of (close − rolling-252d AVWAP)/close in trailing 504d."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, YDAYS)
    raw = _safe_div(close - av, close)

    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        v = w[~np.isnan(w)]
        return float((v <= last).sum()) / float(v.size) if v.size else np.nan
    return raw.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_rk, raw=True).diff()

def f15_avwx_096_indicator_close_above_rolling_vwap_252d_3sigma_upper_d1(high, low, close, volume):
    """Indicator: close > rolling-252d VWAP + 3σ volume-weighted std — extreme upper-σ breach."""
    tp = _typical_price(high, low, close)
    u, m, l = _vwap_sigma_band(tp, volume, YDAYS, 3.0)
    return (close > u).astype(float).where(u.notna(), np.nan).diff()

def f15_avwx_097_mad_zscore_dist_close_rolling_avwap_252d_in_252d_d1(high, low, close, volume):
    """Robust (MAD-based) z-score of (close − rolling-252d AVWAP)/close in 252d."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, YDAYS)
    raw = _safe_div(close - av, close)
    med = raw.rolling(YDAYS, min_periods=QDAYS).median()
    mad = (raw - med).abs().rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(raw - med, 1.4826 * mad).diff()

def f15_avwx_098_log_dist_close_to_ytd_anchored_vwap_d1(high, low, close, volume):
    """Log distance close above YTD-anchored VWAP (cumulative since Jan 1 each calendar year)."""
    tp = _typical_price(high, low, close)
    if not isinstance(close.index, pd.DatetimeIndex):
        return pd.Series(np.nan, index=close.index)
    year_series = pd.Series(close.index.year, index=close.index)
    year_anchor_mask = year_series.diff().ne(0)
    year_anchor_mask.iloc[0] = True
    av = _anchored_vwap_from_event(tp, volume, year_anchor_mask)
    return (_safe_log(close) - _safe_log(av)).diff()

def f15_avwx_099_pctile_rank_dist_close_rolling_avwap_21d_252d_d1(high, low, close, volume):
    """Empirical percentile rank of (close − rolling-21d AVWAP)/close in 252d."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, MDAYS)
    raw = _safe_div(close - av, close)

    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        v = w[~np.isnan(w)]
        return float((v <= last).sum()) / float(v.size) if v.size else np.nan
    return raw.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True).diff()

def f15_avwx_100_log_dist_close_to_avwap_from_climax_volume_event_d1(high, low, close, volume):
    """Log distance close above AVWAP from most-recent bar with volume ≥ 95th-pct(252d) — climax-vol anchor."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_high_volume(volume, YDAYS, 0.95))
    return (_safe_log(close) - _safe_log(av)).diff()

def f15_avwx_101_bars_since_climax_volume_event_252d_d1(high, low, close, volume):
    """Bars since most recent climax-volume event (vol ≥ 95th-pct of trailing 252d)."""
    return _bars_since_true(_event_mask_high_volume(volume, YDAYS, 0.95)).diff()

def f15_avwx_102_log_dist_close_to_avwap_from_largest_gap_up_252d_d1(open, high, low, close, volume):
    """Log distance close to AVWAP anchored at the largest gap-up bar in trailing 252d (institutional entry-mark anchor)."""
    tp = _typical_price(high, low, close)
    anchor = _largest_gap_up_anchor_mask(open, close, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anchor)
    return (_safe_log(close) - _safe_log(av)).diff()

def f15_avwx_103_log_dist_close_to_avwap_from_new_252d_high_event_d1(high, low, close, volume):
    """Log distance close above AVWAP from most-recent new-252d-high event (peak-cluster anchor)."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    return (_safe_log(close) - _safe_log(av)).diff()

def f15_avwx_104_bars_since_new_252d_high_event_d1(high, low, close):
    """Bars since most-recent new 252d-high event."""
    return _bars_since_true(_event_mask_new_window_high(high, YDAYS)).diff()

def f15_avwx_105_slope_climax_volume_avwap_63d_d1(high, low, close, volume):
    """Slope of AVWAP-from-climax-vol-event over trailing 63d."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_high_volume(volume, YDAYS, 0.95))
    return _rolling_slope(av, QDAYS).diff()

def f15_avwx_106_count_climax_volume_anchor_resets_504d_d1(high, low, close, volume):
    """Count of climax-volume anchor resets in trailing 504d."""
    return _event_mask_high_volume(volume, YDAYS, 0.95).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff()

def f15_avwx_107_diff_avwap_climax_vs_new_high_anchor_norm_close_d1(high, low, close, volume):
    """(AVWAP-from-climax-vol-event − AVWAP-from-new-252d-high-event) / close — anchor disagreement."""
    tp = _typical_price(high, low, close)
    a_vol = _anchored_vwap_from_event(tp, volume, _event_mask_high_volume(volume, YDAYS, 0.95))
    a_pk = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    return _safe_div(a_vol - a_pk, close).diff()

def f15_avwx_108_indicator_close_extended_above_climax_avwap_by_20pct_d1(high, low, close, volume):
    """Indicator: close > AVWAP-from-climax-vol-event × 1.20 — extension above climax."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_high_volume(volume, YDAYS, 0.95))
    return (close > 1.2 * av).astype(float).where(av.notna(), np.nan).diff()

def f15_avwx_109_count_anchors_close_above_by_10pct_d1(high, low, close, volume):
    """Count of (4 anchor AVWAPs) where close > anchor × 1.10 — 10%-extension consensus."""
    a1, a2, a3, a4 = _four_anchor_avwaps(high, low, close, volume)
    return ((close > 1.1 * a1).astype(float).fillna(0) + (close > 1.1 * a2).astype(float).fillna(0) + (close > 1.1 * a3).astype(float).fillna(0) + (close > 1.1 * a4).astype(float).fillna(0)).diff()

def f15_avwx_110_max_distance_close_above_anchor_avwaps_d1(high, low, close, volume):
    """Max of {(close − a_i)/close} across 4 anchor AVWAPs — strongest current extension."""
    a1, a2, a3, a4 = _four_anchor_avwaps(high, low, close, volume)
    d1 = _safe_div(close - a1, close)
    d2 = _safe_div(close - a2, close)
    d3 = _safe_div(close - a3, close)
    d4 = _safe_div(close - a4, close)
    pieces = pd.concat([d1.rename('a'), d2.rename('b'), d3.rename('c'), d4.rename('d')], axis=1)
    return pieces.max(axis=1).diff()

def f15_avwx_111_std_distances_close_to_anchor_avwaps_d1(high, low, close, volume):
    """Std (across 4 anchors) of (close − anchor)/close — spread of anchor distances."""
    a1, a2, a3, a4 = _four_anchor_avwaps(high, low, close, volume)
    d1 = _safe_div(close - a1, close)
    d2 = _safe_div(close - a2, close)
    d3 = _safe_div(close - a3, close)
    d4 = _safe_div(close - a4, close)
    pieces = pd.concat([d1.rename('a'), d2.rename('b'), d3.rename('c'), d4.rename('d')], axis=1)
    return pieces.std(axis=1).diff()

def f15_avwx_112_above_below_sign_code_entropy_63d_d1(high, low, close, volume):
    """Entropy over 63d of the 16 possible (above/below) sign codes across 4 anchor AVWAPs."""
    a1, a2, a3, a4 = _four_anchor_avwaps(high, low, close, volume)
    b1 = (close > a1).astype(int).fillna(0)
    b2 = (close > a2).astype(int).fillna(0)
    b3 = (close > a3).astype(int).fillna(0)
    b4 = (close > a4).astype(int).fillna(0)
    code = (b1 * 8 + b2 * 4 + b3 * 2 + b4).astype(float)

    def _ent(w):
        v = w[~np.isnan(w)].astype(int)
        if v.size < 8:
            return np.nan
        counts = np.bincount(v, minlength=16)
        p = counts / counts.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    return code.rolling(QDAYS, min_periods=MDAYS).apply(_ent, raw=True).diff()

def f15_avwx_113_avwap_slope_sign_agreement_count_4anchors_63d_d1(high, low, close, volume):
    """Count (0-4) of the 4 anchor AVWAPs with positive 63d slope (52w-low, 252d-high, 504d-low, IPO-proxy). 4=trending, 0=topping."""
    a1, a2, a3, a4 = _four_anchor_avwaps(high, low, close, volume)
    return ((_rolling_slope(a1, QDAYS) > 0).astype(float).fillna(0) + (_rolling_slope(a2, QDAYS) > 0).astype(float).fillna(0) + (_rolling_slope(a3, QDAYS) > 0).astype(float).fillna(0) + (_rolling_slope(a4, QDAYS) > 0).astype(float).fillna(0)).diff()

def f15_avwx_114_median_dist_close_to_anchor_avwaps_d1(high, low, close, volume):
    """Median (across 4 anchors) of (close − anchor)/close."""
    a1, a2, a3, a4 = _four_anchor_avwaps(high, low, close, volume)
    d1 = _safe_div(close - a1, close)
    d2 = _safe_div(close - a2, close)
    d3 = _safe_div(close - a3, close)
    d4 = _safe_div(close - a4, close)
    pieces = pd.concat([d1.rename('a'), d2.rename('b'), d3.rename('c'), d4.rename('d')], axis=1)
    return pieces.median(axis=1).diff()

def f15_avwx_115_composite_anchor_disagreement_indicator_d1(high, low, close, volume):
    """Indicator: close > some of the 4 anchor AVWAPs AND close < others — split signal = topping/distribution divergence."""
    a1, a2, a3, a4 = _four_anchor_avwaps(high, low, close, volume)
    above = (close > a1).astype(int).fillna(0) + (close > a2).astype(int).fillna(0) + (close > a3).astype(int).fillna(0) + (close > a4).astype(int).fillna(0)
    return ((above >= 1) & (above <= 3)).astype(float).diff()

def f15_avwx_116_log_dist_close_to_volume_profile_poc_252d_d1(high, low, close, volume):
    """Log distance close to Point of Control (POC) in trailing-252d volume profile (max-vol price bin)."""
    tp = _typical_price(high, low, close)
    poc = _volume_profile_poc(tp, volume, YDAYS, n_bins=20)
    return (_safe_log(close) - _safe_log(poc)).diff()

def f15_avwx_117_ratio_max_to_min_anchor_distance_d1(high, low, close, volume):
    """Max / Min of (close − anchor)/close across 4 anchors — extension range ratio."""
    a1, a2, a3, a4 = _four_anchor_avwaps(high, low, close, volume)
    d1 = _safe_div(close - a1, close)
    d2 = _safe_div(close - a2, close)
    d3 = _safe_div(close - a3, close)
    d4 = _safe_div(close - a4, close)
    pieces = pd.concat([d1.rename('a'), d2.rename('b'), d3.rename('c'), d4.rename('d')], axis=1)
    return _safe_div(pieces.max(axis=1), pieces.min(axis=1)).diff()

def f15_avwx_118_rolling_21d_sum_count_anchors_above_d1(high, low, close, volume):
    """Trailing 21d sum of (count of anchors close>anchor) — anchor-bullish persistence."""
    a1, a2, a3, a4 = _four_anchor_avwaps(high, low, close, volume)
    cnt = (close > a1).astype(float).fillna(0) + (close > a2).astype(float).fillna(0) + (close > a3).astype(float).fillna(0) + (close > a4).astype(float).fillna(0)
    return cnt.rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f15_avwx_119_close_position_in_avwap_52wlow_2sigma_band_d1(high, low, close, volume):
    """Position of close in (AVWAP-from-52w-low ± 2σ) band where σ = 63d std of (close − AVWAP)."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    sigma = (close - av).rolling(QDAYS, min_periods=MDAYS).std()
    upper = av + 2 * sigma
    lower = av - 2 * sigma
    return _safe_div(close - lower, upper - lower).diff()

def f15_avwx_120_close_position_in_rolling_avwap_252d_2sigma_band_d1(high, low, close, volume):
    """Position of close in (rolling-252d AVWAP ± 2σ_252d_residuals) band."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, YDAYS)
    sigma = (close - av).rolling(YDAYS, min_periods=QDAYS).std()
    upper = av + 2 * sigma
    lower = av - 2 * sigma
    return _safe_div(close - lower, upper - lower).diff()

def f15_avwx_121_indicator_walking_upper_channel_avwap_52wlow_d1(high, low, close, volume):
    """Indicator: close > AVWAP-from-52w-low + 2σ_63d_residuals — walking the upper channel."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    sigma = (close - av).rolling(QDAYS, min_periods=MDAYS).std()
    return (close > av + 2 * sigma).astype(float).where(av.notna() & sigma.notna(), np.nan).diff()

def f15_avwx_122_count_upper_channel_touches_rolling_avwap_252d_d1(high, low, close, volume):
    """Count of bars in 252d where high > rolling-252d AVWAP + 2σ — upper-channel touches."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, YDAYS)
    sigma = (close - av).rolling(YDAYS, min_periods=QDAYS).std()
    touch = (high > av + 2 * sigma).astype(float).where(av.notna() & sigma.notna(), np.nan)
    return touch.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f15_avwx_123_dwell_time_upper_channel_rolling_avwap_252d_63d_d1(high, low, close, volume):
    """Fraction of bars in 63d where close > rolling-252d AVWAP + 1σ — upper-channel dwell."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, YDAYS)
    sigma = (close - av).rolling(YDAYS, min_periods=QDAYS).std()
    dwell = (close > av + sigma).astype(float).where(av.notna() & sigma.notna(), np.nan)
    return dwell.rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f15_avwx_124_ratio_upper_to_lower_channel_touches_252d_d1(high, low, close, volume):
    """Upper-channel touches / lower-channel touches of rolling-252d AVWAP in 252d — asymmetry."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, YDAYS)
    sigma = (close - av).rolling(YDAYS, min_periods=QDAYS).std()
    upper = (high > av + 2 * sigma).astype(float).where(av.notna() & sigma.notna(), np.nan)
    lower = (low < av - 2 * sigma).astype(float).where(av.notna() & sigma.notna(), np.nan)
    return _safe_div(upper.rolling(YDAYS, min_periods=QDAYS).sum(), lower.rolling(YDAYS, min_periods=QDAYS).sum()).diff()

def f15_avwx_125_max_excursion_above_rolling_avwap_252d_norm_sigma_d1(high, low, close, volume):
    """Max of (close − rolling-252d AVWAP) / σ over trailing 21d (sigma-normalized peak extension)."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, YDAYS)
    sigma = (close - av).rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(close - av, sigma).rolling(MDAYS, min_periods=WDAYS).max().diff()

def f15_avwx_126_regression_slope_close_on_avwap_52wlow_21d_d1(high, low, close, volume):
    """Slope of OLS regression of close ~ AVWAP-from-52w-low over 21d window."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    cov = close.rolling(MDAYS, min_periods=WDAYS).cov(av)
    var = av.rolling(MDAYS, min_periods=WDAYS).var()
    return _safe_div(cov, var).diff()

def f15_avwx_127_r2_close_on_avwap_52wlow_63d_d1(high, low, close, volume):
    """R² of close ~ AVWAP-from-52w-low over 63d window."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    return _rolling_corr_r2(close, av, QDAYS).diff()

def f15_avwx_128_lvn_indicator_252d_p25_d1(high, low, close, volume):
    """Indicator: close is in a price bin with volume < 25th-pct of all 252d-profile bins (Low Volume Node — no support, unstable level)."""
    tp = _typical_price(high, low, close)
    return _volume_profile_lvn_indicator(tp, volume, close, YDAYS, n_bins=20, pct=0.25).diff()

def f15_avwx_129_regression_slope_close_on_rolling_avwap_252d_21d_d1(high, low, close, volume):
    """Slope of OLS regression close ~ rolling-252d AVWAP over 21d."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, YDAYS)
    cov = close.rolling(MDAYS, min_periods=WDAYS).cov(av)
    var = av.rolling(MDAYS, min_periods=WDAYS).var()
    return _safe_div(cov, var).diff()

def f15_avwx_130_r2_close_on_rolling_avwap_252d_63d_d1(high, low, close, volume):
    """R² of close ~ rolling-252d AVWAP over 63d."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, YDAYS)
    return _rolling_corr_r2(close, av, QDAYS).diff()

def f15_avwx_131_lag1_autocorr_residual_close_rolling_avwap_252d_63d_d1(high, low, close, volume):
    """Lag-1 autocorrelation of residuals (close − rolling-252d AVWAP) over 63d — persistence proxy."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, YDAYS)
    res = close - av
    return res.rolling(QDAYS, min_periods=MDAYS).apply(lambda w: np.corrcoef(w[:-1], w[1:])[0, 1] if np.isfinite(w).all() and len(w) > 2 else np.nan, raw=True).diff()

def f15_avwx_132_position_close_in_value_area_252d_d1(high, low, close, volume):
    """Position of close in trailing-252d Value Area (70% volume zone): 0=VAL, 1=VAH."""
    tp = _typical_price(high, low, close)
    vah, val = _value_area_high_low(tp, volume, YDAYS, n_bins=20, pct=0.7)
    return _safe_div(close - val, vah - val).diff()

def f15_avwx_133_product_extension_above_52wlow_x_slope_below_252dhigh_d1(high, low, close, volume):
    """(close − AVWAP-52w-low)/close × slope of AVWAP-from-252d-high over 63d — extension × decline."""
    tp = _typical_price(high, low, close)
    a_lo = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    a_hi = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    return (_safe_div(close - a_lo, close) * _rolling_slope(a_hi, QDAYS)).diff()

def f15_avwx_134_count_death_crosses_rolling_avwap_21_vs_252_in_252d_d1(high, low, close, volume):
    """Count of rolling-21d-AVWAP crossing below rolling-252d-AVWAP ('death-cross') events in 252d."""
    tp = _typical_price(high, low, close)
    a21 = _rolling_avwap(tp, volume, MDAYS)
    a252 = _rolling_avwap(tp, volume, YDAYS)
    dc = ((a21.shift(1) >= a252.shift(1)) & (a21 < a252)).astype(float).where(a21.notna() & a252.notna(), np.nan)
    return dc.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f15_avwx_135_avwap_spread_compression_21d_vs_252d_med_d1(high, low, close, volume):
    """Mean (rolling-21d AVWAP − rolling-252d AVWAP)/close in 21d / its 252d-median — compression."""
    tp = _typical_price(high, low, close)
    a21 = _rolling_avwap(tp, volume, MDAYS)
    a252 = _rolling_avwap(tp, volume, YDAYS)
    spread = _safe_div(a21 - a252, close)
    m21 = spread.rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(m21, spread.rolling(YDAYS, min_periods=QDAYS).median()).diff()

def f15_avwx_136_composite_extension_score_sum_zscores_4anchors_d1(high, low, close, volume):
    """Σ z(close − anchor)/close over 252d, summed across 4 anchors — composite extension z-score."""
    a1, a2, a3, a4 = _four_anchor_avwaps(high, low, close, volume)
    z1 = _rolling_zscore(_safe_div(close - a1, close), YDAYS)
    z2 = _rolling_zscore(_safe_div(close - a2, close), YDAYS)
    z3 = _rolling_zscore(_safe_div(close - a3, close), YDAYS)
    z4 = _rolling_zscore(_safe_div(close - a4, close), YDAYS)
    return (z1.fillna(0) + z2.fillna(0) + z3.fillna(0) + z4.fillna(0)).diff()

def f15_avwx_137_naked_poc_indicator_21d_d1(high, low, close, volume):
    """Indicator: trailing-252d POC has NOT been touched by [low,high] of any of the last 21 bars (naked POC)."""
    tp = _typical_price(high, low, close)
    poc = _volume_profile_poc(tp, volume, YDAYS, n_bins=20)
    touched = ((low <= poc) & (high >= poc)).astype(int).where(poc.notna(), 0)
    touch_in_21 = touched.rolling(MDAYS, min_periods=1).sum().fillna(0)
    return ((touch_in_21 == 0) & poc.notna()).astype(float).diff()

def f15_avwx_138_peak_to_avwap_52wlow_ratio_at_252d_high_d1(high, low, close, volume):
    """At bars at 252d high: high / AVWAP-from-52w-low — peak-relative anchor extension."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    at_peak = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(high, av).where(at_peak, np.nan).diff()

def f15_avwx_139_cum_extension_close_above_avwap_52wlow_252d_d1(high, low, close, volume):
    """Σ max((close − AVWAP-52wlow)/close, 0) over 252d — cumulative above-anchor extension."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    ext = _safe_div(close - av, close).clip(lower=0)
    return ext.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f15_avwx_140_indicator_avwap_252dhigh_slope_sign_flip_in_21d_d1(high, low, close, volume):
    """Indicator: slope of AVWAP-from-252d-high changed sign within trailing 21d."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    sl = _rolling_slope(av, MDAYS)
    sign_change = (np.sign(sl) != np.sign(sl.shift(MDAYS))).astype(float).where(sl.notna() & sl.shift(MDAYS).notna(), np.nan)
    return sign_change.diff()

def f15_avwx_141_total_crosses_three_rolling_avwaps_252d_d1(high, low, close, volume):
    """Total close-crosses across rolling-21/63/252d AVWAPs in 252d — composite cross frequency."""
    tp = _typical_price(high, low, close)
    a21 = _rolling_avwap(tp, volume, MDAYS)
    a63 = _rolling_avwap(tp, volume, QDAYS)
    a252 = _rolling_avwap(tp, volume, YDAYS)
    c1 = ((close > a21).astype(int).where(a21.notna(), np.nan).diff().abs() > 0).astype(float)
    c2 = ((close > a63).astype(int).where(a63.notna(), np.nan).diff().abs() > 0).astype(float)
    c3 = ((close > a252).astype(int).where(a252.notna(), np.nan).diff().abs() > 0).astype(float)
    return (c1 + c2 + c3).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f15_avwx_142_acceleration_dist_close_to_rolling_avwap_252d_d1(high, low, close, volume):
    """Second-difference of (close − rolling-252d AVWAP)/close smoothed by 5d mean."""
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, YDAYS)
    return _safe_div(close - av, close).diff().diff().rolling(WDAYS, min_periods=2).mean().diff()

def f15_avwx_143_current_streak_all_anchors_above_d1(high, low, close, volume):
    """Current consecutive-bar streak where all 4 anchor AVWAPs are below close (anchor-bullish streak)."""
    a1, a2, a3, a4 = _four_anchor_avwaps(high, low, close, volume)
    cond = (close > a1) & (close > a2) & (close > a3) & (close > a4)
    return _streak_true(cond).diff()

def f15_avwx_144_cum_dollar_volume_above_avwap_52wlow_63d_d1(high, low, close, volume):
    """Σ (close × volume) over 63d for bars where close > AVWAP-from-52w-low — dollar-weighted extension."""
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    dv = close * volume
    return dv.where(close > av, 0.0).rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f15_avwx_145_anchor_stack_spread_d1(high, low, close, volume):
    """Stack spread: AVWAP-IPO − AVWAP-1260dlow − AVWAP-504dlow − AVWAP-252dlow — anchor cascade height."""
    tp = _typical_price(high, low, close)
    a_ipo = _expanding_avwap(tp, volume)
    a1260 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, DDAYS_5Y))
    a504 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, DDAYS_2Y))
    a252 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    return (a_ipo - a1260 - a504 - a252).diff()

def f15_avwx_146_anchor_spread_norm_rolling_avwap_252d_d1(high, low, close, volume):
    """Std across (4 anchor AVWAPs) divided by rolling-252d AVWAP — normalized anchor spread."""
    tp = _typical_price(high, low, close)
    a1, a2, a3, a4 = _four_anchor_avwaps(high, low, close, volume)
    pieces = pd.concat([a1.rename('a'), a2.rename('b'), a3.rename('c'), a4.rename('d')], axis=1)
    s = pieces.std(axis=1)
    av252 = _rolling_avwap(tp, volume, YDAYS)
    return _safe_div(s, av252).diff()

def f15_avwx_147_composite_topping_quality_score_d1(high, low, close, volume):
    """(extension above AVWAP-52w-low) × (-extension above AVWAP-252d-high) × bars-since-52w-low — composite."""
    tp = _typical_price(high, low, close)
    a_lo = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    a_hi = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    bsl = _bars_since_true(_event_mask_new_window_low(low, YDAYS))
    ext_lo = _safe_div(close - a_lo, close)
    ext_hi = _safe_div(close - a_hi, close)
    return (ext_lo * -ext_hi * bsl).diff()

def f15_avwx_148_twap_vs_rolling_vwap_252d_divergence_d1(high, low, close, volume):
    """(TWAP_252d − rolling-252d VWAP) / close — TWAP vs VWAP divergence (institutional-flow proxy)."""
    tp = _typical_price(high, low, close)
    twap = _twap(tp, YDAYS)
    vwap = _rolling_avwap(tp, volume, YDAYS)
    return _safe_div(twap - vwap, close).diff()

def f15_avwx_149_avwap_confluence_count_within_1pct_d1(high, low, close, volume):
    """Count of pairs among (AVWAP-52wlow, AVWAP-252dhigh, AVWAP-504dlow, expanding-AVWAP) within 1% of each other — anchor confluence."""
    a1, a2, a3, a4 = _four_anchor_avwaps(high, low, close, volume)
    pairs = [(a1, a2), (a1, a3), (a1, a4), (a2, a3), (a2, a4), (a3, a4)]
    cnt = sum((((p[0] - p[1]).abs() / close < 0.01).astype(float).fillna(0) for p in pairs))
    return cnt.diff()

def f15_avwx_150_composite_anchor_strain_count_z_above_2_d1(high, low, close, volume):
    """Count of anchors (out of 4) where 252d-z-score of residual (close − anchor) > 2 — anchor strain count."""
    a1, a2, a3, a4 = _four_anchor_avwaps(high, low, close, volume)
    z1 = _rolling_zscore(close - a1, YDAYS)
    z2 = _rolling_zscore(close - a2, YDAYS)
    z3 = _rolling_zscore(close - a3, YDAYS)
    z4 = _rolling_zscore(close - a4, YDAYS)
    return ((z1 > 2).astype(float).fillna(0) + (z2 > 2).astype(float).fillna(0) + (z3 > 2).astype(float).fillna(0) + (z4 > 2).astype(float).fillna(0)).diff()
ANCHORED_VWAP_EXTENSION_D1_REGISTRY_076_150 = {'f15_avwx_076_bars_since_close_crossed_below_avwap_from_252d_low_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_076_bars_since_close_crossed_below_avwap_from_252d_low_d1}, 'f15_avwx_077_count_close_crosses_avwap_from_252d_low_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_077_count_close_crosses_avwap_from_252d_low_252d_d1}, 'f15_avwx_078_bars_since_close_crossed_below_avwap_from_252d_high_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_078_bars_since_close_crossed_below_avwap_from_252d_high_d1}, 'f15_avwx_079_count_close_crosses_rolling_avwap_21d_63d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_079_count_close_crosses_rolling_avwap_21d_63d_d1}, 'f15_avwx_080_count_close_crosses_rolling_avwap_252d_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_080_count_close_crosses_rolling_avwap_252d_252d_d1}, 'f15_avwx_081_first_cross_below_avwap_252dlow_after_new_252d_high_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_081_first_cross_below_avwap_252dlow_after_new_252d_high_d1}, 'f15_avwx_082_indicator_close_crossed_expanding_avwap_in_5d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_082_indicator_close_crossed_expanding_avwap_in_5d_d1}, 'f15_avwx_083_cross_rate_rolling_avwap_21d_per_bar_63d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_083_cross_rate_rolling_avwap_21d_per_bar_63d_d1}, 'f15_avwx_084_std_cross_spacings_rolling_avwap_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_084_std_cross_spacings_rolling_avwap_252d_d1}, 'f15_avwx_085_signed_bars_since_cross_avwap_from_252d_low_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_085_signed_bars_since_cross_avwap_from_252d_low_d1}, 'f15_avwx_086_frac_clinging_rolling_avwap_21d_in_21d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_086_frac_clinging_rolling_avwap_21d_in_21d_d1}, 'f15_avwx_087_frac_close_above_rolling_avwap_252d_by_10pct_63d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_087_frac_close_above_rolling_avwap_252d_by_10pct_63d_d1}, 'f15_avwx_088_frac_close_above_avwap_from_252d_low_by_20pct_63d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_088_frac_close_above_avwap_from_252d_low_by_20pct_63d_d1}, 'f15_avwx_089_max_consec_bars_close_above_rolling_avwap_21d_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_089_max_consec_bars_close_above_rolling_avwap_21d_252d_d1}, 'f15_avwx_090_frac_close_within_half_sigma_rolling_avwap_63d_in_21d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_090_frac_close_within_half_sigma_rolling_avwap_63d_in_21d_d1}, 'f15_avwx_091_cum_time_extended_above_avwap_52wlow_by_50pct_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_091_cum_time_extended_above_avwap_52wlow_by_50pct_252d_d1}, 'f15_avwx_092_indicator_5_of_5_bars_above_rolling_avwap_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_092_indicator_5_of_5_bars_above_rolling_avwap_252d_d1}, 'f15_avwx_093_pctile_rank_dist_close_avwap_52wlow_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_093_pctile_rank_dist_close_avwap_52wlow_252d_d1}, 'f15_avwx_094_pctile_rank_dist_close_avwap_252dhigh_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_094_pctile_rank_dist_close_avwap_252dhigh_252d_d1}, 'f15_avwx_095_pctile_rank_dist_close_rolling_avwap_252d_504d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_095_pctile_rank_dist_close_rolling_avwap_252d_504d_d1}, 'f15_avwx_096_indicator_close_above_rolling_vwap_252d_3sigma_upper_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_096_indicator_close_above_rolling_vwap_252d_3sigma_upper_d1}, 'f15_avwx_097_mad_zscore_dist_close_rolling_avwap_252d_in_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_097_mad_zscore_dist_close_rolling_avwap_252d_in_252d_d1}, 'f15_avwx_098_log_dist_close_to_ytd_anchored_vwap_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_098_log_dist_close_to_ytd_anchored_vwap_d1}, 'f15_avwx_099_pctile_rank_dist_close_rolling_avwap_21d_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_099_pctile_rank_dist_close_rolling_avwap_21d_252d_d1}, 'f15_avwx_100_log_dist_close_to_avwap_from_climax_volume_event_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_100_log_dist_close_to_avwap_from_climax_volume_event_d1}, 'f15_avwx_101_bars_since_climax_volume_event_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_101_bars_since_climax_volume_event_252d_d1}, 'f15_avwx_102_log_dist_close_to_avwap_from_largest_gap_up_252d_d1': {'inputs': ['open', 'high', 'low', 'close', 'volume'], 'func': f15_avwx_102_log_dist_close_to_avwap_from_largest_gap_up_252d_d1}, 'f15_avwx_103_log_dist_close_to_avwap_from_new_252d_high_event_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_103_log_dist_close_to_avwap_from_new_252d_high_event_d1}, 'f15_avwx_104_bars_since_new_252d_high_event_d1': {'inputs': ['high', 'low', 'close'], 'func': f15_avwx_104_bars_since_new_252d_high_event_d1}, 'f15_avwx_105_slope_climax_volume_avwap_63d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_105_slope_climax_volume_avwap_63d_d1}, 'f15_avwx_106_count_climax_volume_anchor_resets_504d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_106_count_climax_volume_anchor_resets_504d_d1}, 'f15_avwx_107_diff_avwap_climax_vs_new_high_anchor_norm_close_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_107_diff_avwap_climax_vs_new_high_anchor_norm_close_d1}, 'f15_avwx_108_indicator_close_extended_above_climax_avwap_by_20pct_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_108_indicator_close_extended_above_climax_avwap_by_20pct_d1}, 'f15_avwx_109_count_anchors_close_above_by_10pct_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_109_count_anchors_close_above_by_10pct_d1}, 'f15_avwx_110_max_distance_close_above_anchor_avwaps_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_110_max_distance_close_above_anchor_avwaps_d1}, 'f15_avwx_111_std_distances_close_to_anchor_avwaps_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_111_std_distances_close_to_anchor_avwaps_d1}, 'f15_avwx_112_above_below_sign_code_entropy_63d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_112_above_below_sign_code_entropy_63d_d1}, 'f15_avwx_113_avwap_slope_sign_agreement_count_4anchors_63d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_113_avwap_slope_sign_agreement_count_4anchors_63d_d1}, 'f15_avwx_114_median_dist_close_to_anchor_avwaps_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_114_median_dist_close_to_anchor_avwaps_d1}, 'f15_avwx_115_composite_anchor_disagreement_indicator_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_115_composite_anchor_disagreement_indicator_d1}, 'f15_avwx_116_log_dist_close_to_volume_profile_poc_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_116_log_dist_close_to_volume_profile_poc_252d_d1}, 'f15_avwx_117_ratio_max_to_min_anchor_distance_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_117_ratio_max_to_min_anchor_distance_d1}, 'f15_avwx_118_rolling_21d_sum_count_anchors_above_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_118_rolling_21d_sum_count_anchors_above_d1}, 'f15_avwx_119_close_position_in_avwap_52wlow_2sigma_band_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_119_close_position_in_avwap_52wlow_2sigma_band_d1}, 'f15_avwx_120_close_position_in_rolling_avwap_252d_2sigma_band_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_120_close_position_in_rolling_avwap_252d_2sigma_band_d1}, 'f15_avwx_121_indicator_walking_upper_channel_avwap_52wlow_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_121_indicator_walking_upper_channel_avwap_52wlow_d1}, 'f15_avwx_122_count_upper_channel_touches_rolling_avwap_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_122_count_upper_channel_touches_rolling_avwap_252d_d1}, 'f15_avwx_123_dwell_time_upper_channel_rolling_avwap_252d_63d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_123_dwell_time_upper_channel_rolling_avwap_252d_63d_d1}, 'f15_avwx_124_ratio_upper_to_lower_channel_touches_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_124_ratio_upper_to_lower_channel_touches_252d_d1}, 'f15_avwx_125_max_excursion_above_rolling_avwap_252d_norm_sigma_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_125_max_excursion_above_rolling_avwap_252d_norm_sigma_d1}, 'f15_avwx_126_regression_slope_close_on_avwap_52wlow_21d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_126_regression_slope_close_on_avwap_52wlow_21d_d1}, 'f15_avwx_127_r2_close_on_avwap_52wlow_63d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_127_r2_close_on_avwap_52wlow_63d_d1}, 'f15_avwx_128_lvn_indicator_252d_p25_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_128_lvn_indicator_252d_p25_d1}, 'f15_avwx_129_regression_slope_close_on_rolling_avwap_252d_21d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_129_regression_slope_close_on_rolling_avwap_252d_21d_d1}, 'f15_avwx_130_r2_close_on_rolling_avwap_252d_63d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_130_r2_close_on_rolling_avwap_252d_63d_d1}, 'f15_avwx_131_lag1_autocorr_residual_close_rolling_avwap_252d_63d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_131_lag1_autocorr_residual_close_rolling_avwap_252d_63d_d1}, 'f15_avwx_132_position_close_in_value_area_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_132_position_close_in_value_area_252d_d1}, 'f15_avwx_133_product_extension_above_52wlow_x_slope_below_252dhigh_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_133_product_extension_above_52wlow_x_slope_below_252dhigh_d1}, 'f15_avwx_134_count_death_crosses_rolling_avwap_21_vs_252_in_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_134_count_death_crosses_rolling_avwap_21_vs_252_in_252d_d1}, 'f15_avwx_135_avwap_spread_compression_21d_vs_252d_med_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_135_avwap_spread_compression_21d_vs_252d_med_d1}, 'f15_avwx_136_composite_extension_score_sum_zscores_4anchors_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_136_composite_extension_score_sum_zscores_4anchors_d1}, 'f15_avwx_137_naked_poc_indicator_21d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_137_naked_poc_indicator_21d_d1}, 'f15_avwx_138_peak_to_avwap_52wlow_ratio_at_252d_high_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_138_peak_to_avwap_52wlow_ratio_at_252d_high_d1}, 'f15_avwx_139_cum_extension_close_above_avwap_52wlow_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_139_cum_extension_close_above_avwap_52wlow_252d_d1}, 'f15_avwx_140_indicator_avwap_252dhigh_slope_sign_flip_in_21d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_140_indicator_avwap_252dhigh_slope_sign_flip_in_21d_d1}, 'f15_avwx_141_total_crosses_three_rolling_avwaps_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_141_total_crosses_three_rolling_avwaps_252d_d1}, 'f15_avwx_142_acceleration_dist_close_to_rolling_avwap_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_142_acceleration_dist_close_to_rolling_avwap_252d_d1}, 'f15_avwx_143_current_streak_all_anchors_above_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_143_current_streak_all_anchors_above_d1}, 'f15_avwx_144_cum_dollar_volume_above_avwap_52wlow_63d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_144_cum_dollar_volume_above_avwap_52wlow_63d_d1}, 'f15_avwx_145_anchor_stack_spread_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_145_anchor_stack_spread_d1}, 'f15_avwx_146_anchor_spread_norm_rolling_avwap_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_146_anchor_spread_norm_rolling_avwap_252d_d1}, 'f15_avwx_147_composite_topping_quality_score_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_147_composite_topping_quality_score_d1}, 'f15_avwx_148_twap_vs_rolling_vwap_252d_divergence_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_148_twap_vs_rolling_vwap_252d_divergence_d1}, 'f15_avwx_149_avwap_confluence_count_within_1pct_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_149_avwap_confluence_count_within_1pct_d1}, 'f15_avwx_150_composite_anchor_strain_count_z_above_2_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f15_avwx_150_composite_anchor_strain_count_z_above_2_d1}}