import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
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
            x = x[valid]; wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _typical_price(high, low, close):
    return (high + low + close) / 3.0


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
    arr = mask.fillna(False).values.astype(bool)
    n = len(arr)
    out = np.zeros(n, dtype=float)
    run = 0
    for i in range(n):
        run = run + 1 if arr[i] else 0
        out[i] = float(run)
    return pd.Series(out, index=mask.index)


def _anchored_vwap_from_event(typical, volume, anchor_mask):
    aid = anchor_mask.fillna(False).astype(int).cumsum()
    pv = (typical * volume)
    pv_cum = pv.groupby(aid).cumsum()
    v_cum = volume.groupby(aid).cumsum()
    out = _safe_div(pv_cum, v_cum)
    return out.where(aid > 0, np.nan)


def _anchored_atwap_from_event(typical, anchor_mask):
    aid = anchor_mask.fillna(False).astype(int).cumsum()
    p_cum = typical.groupby(aid).cumsum()
    cnt = pd.Series(1.0, index=typical.index).groupby(aid).cumsum()
    out = _safe_div(p_cum, cnt)
    return out.where(aid > 0, np.nan)


def _anchored_vwap_sigma_from_event(typical, volume, anchor_mask):
    aid = anchor_mask.fillna(False).astype(int).cumsum()
    pv = (typical * volume)
    p2v = (typical * typical * volume)
    pv_cum = pv.groupby(aid).cumsum()
    p2v_cum = p2v.groupby(aid).cumsum()
    v_cum = volume.groupby(aid).cumsum()
    mean = _safe_div(pv_cum, v_cum)
    mean2 = _safe_div(p2v_cum, v_cum)
    var = (mean2 - mean * mean).clip(lower=0.0)
    sig = np.sqrt(var)
    return sig.where(aid > 0, np.nan)


def _expanding_avwap(typical, volume):
    pv = (typical * volume).cumsum()
    v = volume.cumsum()
    return _safe_div(pv, v)


def _rolling_avwap(typical, volume, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    pv = (typical * volume).rolling(window, min_periods=min_periods).sum()
    v = volume.rolling(window, min_periods=min_periods).sum()
    return _safe_div(pv, v)


def _event_mask_new_window_low(low, n):
    rmin = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return (low <= rmin) & rmin.notna()


def _event_mask_new_window_high(high, n):
    rmax = high.rolling(n, min_periods=max(n // 3, 2)).max()
    return (high >= rmax) & rmax.notna()


def _event_mask_high_volume_zscore(volume, n, k):
    m = volume.rolling(n, min_periods=max(n // 3, 2)).mean()
    sd = volume.rolling(n, min_periods=max(n // 3, 2)).std()
    z = _safe_div(volume - m, sd)
    return (z >= k) & z.notna()


def _calendar_year_start_mask(index_like):
    idx = index_like.index if hasattr(index_like, "index") else index_like
    yrs = pd.DatetimeIndex(idx).year if not isinstance(idx, pd.DatetimeIndex) else idx.year
    s = pd.Series(yrs, index=idx)
    return s.ne(s.shift(1)).fillna(True)


def _calendar_quarter_start_mask(index_like):
    idx = index_like.index if hasattr(index_like, "index") else index_like
    dt = pd.DatetimeIndex(idx) if not isinstance(idx, pd.DatetimeIndex) else idx
    code = pd.Series(dt.year * 4 + (dt.quarter - 1), index=idx)
    return code.ne(code.shift(1)).fillna(True)


def _calendar_month_start_mask(index_like):
    idx = index_like.index if hasattr(index_like, "index") else index_like
    dt = pd.DatetimeIndex(idx) if not isinstance(idx, pd.DatetimeIndex) else idx
    code = pd.Series(dt.year * 12 + (dt.month - 1), index=idx)
    return code.ne(code.shift(1)).fillna(True)


def _anchor_at_argmax_in_window(high_series, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    rmax = high_series.rolling(n, min_periods=min_periods).max()
    return (high_series >= rmax) & rmax.notna()


def _anchor_at_argmin_in_window(low_series, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    rmin = low_series.rolling(n, min_periods=min_periods).min()
    return (low_series <= rmin) & rmin.notna()


def _anchored_vwap_from_argmin_in_252d(typical, volume, low):
    return _anchored_vwap_from_event(typical, volume, _event_mask_new_window_low(low, YDAYS))


def _anchored_vwap_from_argmax_in_252d(typical, volume, high):
    return _anchored_vwap_from_event(typical, volume, _event_mask_new_window_high(high, YDAYS))


def _drawdown_bottom_anchor_mask(close, n):
    rmin_c = close.rolling(n, min_periods=max(n // 3, 2)).min()
    return (close <= rmin_c) & rmin_c.notna()


def _sma(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    return s.rolling(n, min_periods=min_periods).mean()


def _first_close_above_sma_in_window_mask(close, sma_series, n):
    above = (close > sma_series).astype(int).where(sma_series.notna(), np.nan)
    cross_up = ((above.shift(1) == 0) & (above == 1)).fillna(False)
    return cross_up


def _first_close_below_sma_in_window_mask(close, sma_series, n):
    above = (close > sma_series).astype(int).where(sma_series.notna(), np.nan)
    cross_dn = ((above.shift(1) == 1) & (above == 0)).fillna(False)
    return cross_dn


def f15_avwx_151_log_dist_avwap_from_calendar_year_start(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _calendar_year_start_mask(close))
    return _safe_log(close) - _safe_log(av)


def f15_avwx_152_log_dist_avwap_from_calendar_quarter_start(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _calendar_quarter_start_mask(close))
    return _safe_log(close) - _safe_log(av)


def f15_avwx_153_log_dist_avwap_from_calendar_month_start(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _calendar_month_start_mask(close))
    return _safe_log(close) - _safe_log(av)


def f15_avwx_154_log_dist_avwap_from_most_recent_252d_high_static(high, low, close, volume):
    tp = _typical_price(high, low, close)
    mask_new = _event_mask_new_window_high(high, YDAYS)
    confirm = high >= high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    av = _anchored_vwap_from_event(tp, volume, mask_new & confirm.fillna(False))
    return _safe_log(close) - _safe_log(av)


def f15_avwx_155_log_dist_avwap_from_most_recent_252d_low_static(high, low, close, volume):
    tp = _typical_price(high, low, close)
    mask_new = _event_mask_new_window_low(low, YDAYS)
    confirm = low <= low.rolling(MDAYS, min_periods=WDAYS).min().shift(1)
    av = _anchored_vwap_from_event(tp, volume, mask_new & confirm.fillna(False))
    return _safe_log(close) - _safe_log(av)


def f15_avwx_156_log_dist_avwap_from_climactic_vol_3sigma_bar(high, low, close, volume):
    tp = _typical_price(high, low, close)
    mask = _event_mask_high_volume_zscore(volume, YDAYS, 3.0)
    av = _anchored_vwap_from_event(tp, volume, mask)
    return _safe_log(close) - _safe_log(av)


def f15_avwx_157_log_dist_avwap_from_first_close_above_sma200_252d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    sma200 = _sma(close, 200)
    cross = _first_close_above_sma_in_window_mask(close, sma200, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, cross)
    return _safe_log(close) - _safe_log(av)


def f15_avwx_158_log_dist_avwap_from_first_close_below_sma200_252d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    sma200 = _sma(close, 200)
    cross = _first_close_below_sma_in_window_mask(close, sma200, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, cross)
    return _safe_log(close) - _safe_log(av)


def f15_avwx_159_log_dist_avwap_from_first_new_52w_high_in_252d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    new_hi = _event_mask_new_window_high(high, YDAYS)
    first_in_window = new_hi & (~new_hi.rolling(YDAYS, min_periods=1).max().shift(1).fillna(False).astype(bool))
    av = _anchored_vwap_from_event(tp, volume, first_in_window.fillna(False))
    return _safe_log(close) - _safe_log(av)


def f15_avwx_160_log_dist_avwap_from_drawdown_bottom_252d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    bot = _drawdown_bottom_anchor_mask(close, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, bot)
    return _safe_log(close) - _safe_log(av)


def f15_avwx_161_avwap_252dlow_plus_1sigma_breach_count_63d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    sig = _anchored_vwap_sigma_from_event(tp, volume, anc)
    upper = av + sig
    breach = (close > upper).astype(float).where(av.notna() & sig.notna(), np.nan)
    return breach.rolling(QDAYS, min_periods=MDAYS).sum()


def f15_avwx_162_avwap_252dlow_plus_2sigma_breach_count_63d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    sig = _anchored_vwap_sigma_from_event(tp, volume, anc)
    upper = av + 2 * sig
    breach = (close > upper).astype(float).where(av.notna() & sig.notna(), np.nan)
    return breach.rolling(QDAYS, min_periods=MDAYS).sum()


def f15_avwx_163_avwap_252dlow_plus_3sigma_breach_count_63d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    sig = _anchored_vwap_sigma_from_event(tp, volume, anc)
    upper = av + 3 * sig
    breach = (close > upper).astype(float).where(av.notna() & sig.notna(), np.nan)
    return breach.rolling(QDAYS, min_periods=MDAYS).sum()


def f15_avwx_164_close_distance_avwap_252dlow_in_sigma_units(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    sig = _anchored_vwap_sigma_from_event(tp, volume, anc)
    return _safe_div(close - av, sig)


def f15_avwx_165_max_streak_above_avwap_252dlow_plus_1sigma_63d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    sig = _anchored_vwap_sigma_from_event(tp, volume, anc)
    upper = av + sig
    flag = (close > upper).fillna(False)
    s = _streak_true(flag)
    return s.rolling(QDAYS, min_periods=MDAYS).max()


def f15_avwx_166_avwap_252dlow_1sigma_band_compression_event(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    sig = _anchored_vwap_sigma_from_event(tp, volume, anc)
    med = sig.rolling(QDAYS, min_periods=MDAYS).median()
    comp = sig < 0.5 * med
    return comp.astype(float).where(sig.notna() & med.notna(), np.nan)


def f15_avwx_167_avwap_252dlow_1sigma_band_expansion_event(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    sig = _anchored_vwap_sigma_from_event(tp, volume, anc)
    med = sig.rolling(QDAYS, min_periods=MDAYS).median()
    exp_ev = sig > 1.5 * med
    return exp_ev.astype(float).where(sig.notna() & med.notna(), np.nan)


def f15_avwx_168_avwap_252dlow_upper_band_walk_5bar_event(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    sig = _anchored_vwap_sigma_from_event(tp, volume, anc)
    upper = av + sig
    flag = (close > upper).fillna(False)
    s = _streak_true(flag)
    return (s >= 5).astype(float)


def f15_avwx_169_avwap_252dlow_band_failure_then_extension(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    sig = _anchored_vwap_sigma_from_event(tp, volume, anc)
    upper = av + sig
    breach = (close > upper).fillna(False)
    ret = (close < av).fillna(False)
    rmax_high = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    new_hi = (high > rmax_high).fillna(False)
    had_breach = breach.rolling(MDAYS, min_periods=1).max().fillna(0).astype(bool)
    had_return = ret.rolling(MDAYS, min_periods=1).max().fillna(0).astype(bool)
    pattern = (had_breach & had_return & new_hi).astype(float)
    return pattern.rolling(QDAYS, min_periods=MDAYS).sum()


def f15_avwx_170_avwap_252dlow_lower_band_break_count_63d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    sig = _anchored_vwap_sigma_from_event(tp, volume, anc)
    lower = av - sig
    breach = (close < lower).astype(float).where(av.notna() & sig.notna(), np.nan)
    return breach.rolling(QDAYS, min_periods=MDAYS).sum()


def f15_avwx_171_avwap_252dlow_retest_count_63d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    was_above = (close.shift(1) > av.shift(1) * 1.05).fillna(False)
    touched = (low <= av * 1.01).fillna(False)
    ev = (was_above & touched).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum()


def f15_avwx_172_avwap_252dlow_rejection_count_63d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    touched = (low <= av).fillna(False)
    held = (close > av).fillna(False)
    above_prev = (close.shift(1) > av.shift(1)).fillna(False)
    ev = (touched & held & above_prev).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum()


def f15_avwx_173_avwap_252dlow_failed_support_count_63d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    was_above = (close.shift(1) > av.shift(1)).fillna(False)
    now_below = (close < av).fillna(False)
    ev = (was_above & now_below).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum()


def f15_avwx_174_bars_since_last_avwap_252dhigh_touch(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_high(high, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    touched = (high >= av * 0.99).fillna(False)
    return _bars_since_true(touched)


def f15_avwx_175_avwap_252dhigh_rejection_count_63d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_high(high, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    touched = (high >= av).fillna(False)
    rejected = (close < av).fillna(False)
    below_prev = (close.shift(1) < av.shift(1)).fillna(False)
    ev = (touched & rejected & below_prev).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum()


def f15_avwx_176_avwap_252dlow_above_close_streak_max_63d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    flag = (av > close).fillna(False)
    s = _streak_true(flag)
    return s.rolling(QDAYS, min_periods=MDAYS).max()


def f15_avwx_177_avwap_252dlow_retest_volume_confirmation_63d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    was_above = (close.shift(1) > av.shift(1) * 1.05).fillna(False)
    touched = (low <= av * 1.01).fillna(False)
    vol21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    heavy = (volume > 1.5 * vol21).fillna(False)
    ev = (was_above & touched & heavy).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum()


def f15_avwx_178_avwap_252dlow_retest_doji_pattern_count_63d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    op = close.shift(1)
    bar_range = (high - low).replace(0, np.nan)
    body = (close - op).abs()
    doji = (body <= 0.3 * bar_range).fillna(False)
    was_above = (close.shift(1) > av.shift(1) * 1.03).fillna(False)
    touched = (low <= av * 1.02).fillna(False)
    ev = (was_above & touched & doji).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum()


def f15_avwx_179_multi_anchor_vwap_simultaneous_retest_count_63d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    a1 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    a2 = _rolling_avwap(tp, volume, YDAYS)
    t1 = (low <= a1 * 1.01) & (low >= a1 * 0.99)
    t2 = (low <= a2 * 1.01) & (low >= a2 * 0.99)
    ev = (t1 & t2).fillna(False).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum()


def f15_avwx_180_avwap_252dlow_retest_then_lower_high_count_63d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    was_above = (close.shift(1) > av.shift(1) * 1.03).fillna(False)
    touched = (low <= av * 1.02).fillna(False)
    retest = (was_above & touched).fillna(False)
    h5 = high.rolling(WDAYS, min_periods=2).max()
    h21_prior = high.shift(WDAYS).rolling(MDAYS, min_periods=WDAYS).max()
    lower_high = (h5 < h21_prior).fillna(False)
    retest_recent = retest.rolling(WDAYS, min_periods=1).max().fillna(0).astype(bool)
    ev = (retest_recent & lower_high).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum()


def _five_anchor_set(high, low, close, volume):
    tp = _typical_price(high, low, close)
    a1 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    a2 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    a3 = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, DDAYS_2Y))
    a4 = _expanding_avwap(tp, volume)
    a5 = _anchored_vwap_from_event(tp, volume, _event_mask_high_volume_zscore(volume, YDAYS, 2.0))
    return a1, a2, a3, a4, a5


def f15_avwx_181_multi_anchor_consensus_close_above_count(high, low, close, volume):
    a1, a2, a3, a4, a5 = _five_anchor_set(high, low, close, volume)
    above_all = ((close > a1) & (close > a2) & (close > a3) & (close > a4) & (close > a5)).fillna(False)
    return above_all.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f15_avwx_182_multi_anchor_consensus_close_below_count(high, low, close, volume):
    a1, a2, a3, a4, a5 = _five_anchor_set(high, low, close, volume)
    below_all = ((close < a1) & (close < a2) & (close < a3) & (close < a4) & (close < a5)).fillna(False)
    return below_all.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f15_avwx_183_multi_anchor_dispersion_zscore_252d(high, low, close, volume):
    a1, a2, a3, a4, a5 = _five_anchor_set(high, low, close, volume)
    pieces = pd.concat([a1.rename("p1"), a2.rename("p2"), a3.rename("p3"),
                        a4.rename("p4"), a5.rename("p5")], axis=1)
    s = pieces.std(axis=1)
    return _rolling_zscore(s, YDAYS)


def f15_avwx_184_multi_anchor_overlap_zone_count(high, low, close, volume):
    a1, a2, a3, a4, a5 = _five_anchor_set(high, low, close, volume)
    arr = [a1, a2, a3, a4, a5]
    cnt = pd.Series(0.0, index=close.index)
    for i in range(5):
        for j in range(i + 1, 5):
            ratio = _safe_div(arr[i] - arr[j], (arr[i] + arr[j]).abs() / 2.0).abs()
            close_pair = (ratio <= 0.02).fillna(False)
            cnt = cnt + close_pair.astype(float)
    return cnt


def f15_avwx_185_multi_anchor_breakdown_event_5d(high, low, close, volume):
    a1, a2, a3, a4, a5 = _five_anchor_set(high, low, close, volume)
    def _broken_in_5d(av):
        was = (close.shift(1) > av.shift(1)).fillna(False)
        now = (close < av).fillna(False)
        evt = (was & now).astype(float)
        return evt.rolling(WDAYS, min_periods=1).max().fillna(0).astype(bool)
    bk = (_broken_in_5d(a1) & _broken_in_5d(a2) & _broken_in_5d(a3) & _broken_in_5d(a4) & _broken_in_5d(a5))
    return bk.astype(float)


def f15_avwx_186_multi_anchor_skew_index(high, low, close, volume):
    a1, a2, a3, a4, a5 = _five_anchor_set(high, low, close, volume)
    above = ((a1 > close).astype(float).fillna(0) + (a2 > close).astype(float).fillna(0)
             + (a3 > close).astype(float).fillna(0) + (a4 > close).astype(float).fillna(0)
             + (a5 > close).astype(float).fillna(0))
    below = ((a1 < close).astype(float).fillna(0) + (a2 < close).astype(float).fillna(0)
             + (a3 < close).astype(float).fillna(0) + (a4 < close).astype(float).fillna(0)
             + (a5 < close).astype(float).fillna(0))
    return (above - below) / 5.0


def f15_avwx_187_multi_anchor_cluster_compression_63d(high, low, close, volume):
    a1, a2, a3, a4, a5 = _five_anchor_set(high, low, close, volume)
    pieces = pd.concat([a1.rename("p1"), a2.rename("p2"), a3.rename("p3"),
                        a4.rename("p4"), a5.rename("p5")], axis=1)
    s = pieces.std(axis=1)
    return _safe_div(s, s.rolling(QDAYS, min_periods=MDAYS).mean())


def f15_avwx_188_multi_anchor_alignment_score_21d(high, low, close, volume):
    a1, a2, a3, a4, a5 = _five_anchor_set(high, low, close, volume)
    slopes = [_rolling_slope(a, MDAYS) for a in (a1, a2, a3, a4, a5)]
    signs = pd.concat([np.sign(s).rename(f"s{i}") for i, s in enumerate(slopes)], axis=1)
    return signs.mean(axis=1)


def f15_avwx_189_avwap_252dlow_slope_at_current_bar_5d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    return _rolling_slope(av, WDAYS)


def f15_avwx_190_avwap_252dlow_slope_acceleration_21d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    sl = _rolling_slope(av, MDAYS)
    return _rolling_slope(sl, MDAYS)


def f15_avwx_191_avwap_252dlow_slope_decay_rate_63d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    sl = _rolling_slope(av, MDAYS)
    return _safe_div(sl - sl.shift(QDAYS), sl.shift(QDAYS).abs())


def f15_avwx_192_avwap_252dhigh_slope_post_peak_steepness_63d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_high(high, YDAYS))
    sl = _rolling_slope(av, MDAYS)
    return sl.rolling(QDAYS, min_periods=MDAYS).min()


def f15_avwx_193_avwap_252dlow_slope_inflection_count_252d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    sl = _rolling_slope(av, MDAYS)
    sign = np.sign(sl).where(sl.notna(), np.nan)
    flip = (sign.diff().abs() > 0).astype(float)
    return flip.rolling(YDAYS, min_periods=QDAYS).sum()


def f15_avwx_194_multi_anchor_slope_dispersion(high, low, close, volume):
    a1, a2, a3, a4, a5 = _five_anchor_set(high, low, close, volume)
    slopes = pd.concat([
        _rolling_slope(a1, MDAYS).rename("s1"),
        _rolling_slope(a2, MDAYS).rename("s2"),
        _rolling_slope(a3, MDAYS).rename("s3"),
        _rolling_slope(a4, MDAYS).rename("s4"),
        _rolling_slope(a5, MDAYS).rename("s5"),
    ], axis=1)
    return slopes.std(axis=1)


def f15_avwx_195_avwap_252dlow_slope_sign_flip_recent_5d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    sl = _rolling_slope(av, MDAYS)
    sign = np.sign(sl).where(sl.notna(), np.nan)
    flip = (sign.diff().abs() > 0).astype(float).fillna(0)
    return (flip.rolling(WDAYS, min_periods=1).sum() > 0).astype(float)


def f15_avwx_196_avwap_252dlow_slope_zscore_252d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    sl = _rolling_slope(av, MDAYS)
    return _rolling_zscore(sl, YDAYS)


def f15_avwx_197_avwap_vs_atwap_distance_from_252dlow(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    at = _anchored_atwap_from_event(tp, anc)
    return _safe_div(av - at, close)


def f15_avwx_198_avwap_vs_atwap_divergence_acceleration_63d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    at = _anchored_atwap_from_event(tp, anc)
    div = (av - at)
    return _rolling_slope(div, QDAYS)


def f15_avwx_199_atwap_from_252dlow_distance(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    at = _anchored_atwap_from_event(tp, anc)
    return _safe_log(close) - _safe_log(at)


def f15_avwx_200_avwap_vs_atwap_skew_indicator(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    at = _anchored_atwap_from_event(tp, anc)
    return (av > at).astype(float).where(av.notna() & at.notna(), np.nan)


def f15_avwx_201_atwap_minus_avwap_at_peak_event(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    at = _anchored_atwap_from_event(tp, anc)
    spread = at - av
    peak_mask = _event_mask_new_window_high(high, YDAYS)
    snap = spread.where(peak_mask)
    return snap.ffill()


def f15_avwx_202_vwap_of_vwap_5d_distance(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av21 = _rolling_avwap(tp, volume, MDAYS)
    smoothed = av21.rolling(WDAYS, min_periods=2).mean()
    return _safe_log(close) - _safe_log(smoothed)


def f15_avwx_203_ytd_cumulative_avwap_distance_pct(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _calendar_year_start_mask(close))
    return _safe_div(close - av, av)


def f15_avwx_204_qtd_cumulative_avwap_distance_pct(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _calendar_quarter_start_mask(close))
    return _safe_div(close - av, av)


def f15_avwx_205_mtd_cumulative_avwap_distance_pct(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _calendar_month_start_mask(close))
    return _safe_div(close - av, av)


def f15_avwx_206_multi_window_rolling_vwap_consensus(high, low, close, volume):
    tp = _typical_price(high, low, close)
    v5 = _rolling_avwap(tp, volume, WDAYS)
    v21 = _rolling_avwap(tp, volume, MDAYS)
    v63 = _rolling_avwap(tp, volume, QDAYS)
    v252 = _rolling_avwap(tp, volume, YDAYS)
    return ((close > v5).astype(float).fillna(0) + (close > v21).astype(float).fillna(0)
            + (close > v63).astype(float).fillna(0) + (close > v252).astype(float).fillna(0))


def f15_avwx_207_rolling_vwap_envelope_breach_count_63d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, MDAYS)
    breach = ((close > av * 1.02) | (close < av * 0.98)).fillna(False)
    return breach.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f15_avwx_208_avwap_252dlow_dist_when_within_5pct_of_252dhigh(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    near_top = (close >= h252 * 0.95).fillna(False)
    raw = _safe_log(close) - _safe_log(av)
    return raw.where(near_top, np.nan)


def f15_avwx_209_avwap_252dlow_dist_conditional_high_vol_regime(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    ret = _safe_log(close).diff()
    rv = ret.rolling(MDAYS, min_periods=WDAYS).std()
    med = rv.rolling(QDAYS, min_periods=MDAYS).median()
    hv = (rv > med).fillna(False)
    raw = _safe_log(close) - _safe_log(av)
    return raw.where(hv, np.nan)


def f15_avwx_210_avwap_252dlow_dist_conditional_low_vol_regime(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    ret = _safe_log(close).diff()
    rv = ret.rolling(MDAYS, min_periods=WDAYS).std()
    med = rv.rolling(QDAYS, min_periods=MDAYS).median()
    lv = (rv <= med).fillna(False)
    raw = _safe_log(close) - _safe_log(av)
    return raw.where(lv, np.nan)


def f15_avwx_211_avwap_252dlow_dist_conditional_uptrend_sma200(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    sma200 = _sma(close, 200)
    up = (close > sma200).fillna(False)
    raw = _safe_log(close) - _safe_log(av)
    return raw.where(up, np.nan)


def f15_avwx_212_avwap_252dlow_dist_conditional_downtrend_sma200(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    sma200 = _sma(close, 200)
    dn = (close < sma200).fillna(False)
    raw = _safe_log(close) - _safe_log(av)
    return raw.where(dn, np.nan)


def f15_avwx_213_avwap_252dlow_retest_during_drawdown_count_63d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    drawdown = (close <= 0.85 * h252).fillna(False)
    was_above = (close.shift(1) > av.shift(1) * 1.03).fillna(False)
    touched = (low <= av * 1.02).fillna(False)
    ev = (was_above & touched & drawdown).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum()


def f15_avwx_214_avwap_band_compression_during_consolidation(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    sig = _anchored_vwap_sigma_from_event(tp, volume, anc)
    med_sig = sig.rolling(QDAYS, min_periods=MDAYS).median()
    sig_comp = (sig < 0.6 * med_sig).fillna(False)
    ret = _safe_log(close).diff()
    rv = ret.rolling(MDAYS, min_periods=WDAYS).std()
    med_rv = rv.rolling(QDAYS, min_periods=MDAYS).median()
    rv_comp = (rv < med_rv).fillna(False)
    return (sig_comp & rv_comp).astype(float)


def f15_avwx_215_avwap_breakdown_velocity_in_high_vol_regime(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    was = (close.shift(1) > av.shift(1)).fillna(False)
    now = (close < av).fillna(False)
    cross_dn = (was & now).astype(bool)
    bars_since = _bars_since_true(cross_dn)
    ret = _safe_log(close).diff()
    rv = ret.rolling(MDAYS, min_periods=WDAYS).std()
    med = rv.rolling(QDAYS, min_periods=MDAYS).median()
    hv = (rv > med).astype(float)
    return _safe_div(1.0, 1.0 + bars_since) * hv  # higher when very recent + high vol


def f15_avwx_216_pricing_efficiency_above_avwap_corr_63d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    d = _safe_div(close - av, close)
    r = _safe_log(close).diff()
    return d.rolling(QDAYS, min_periods=MDAYS).corr(r)


def f15_avwx_217_mean_excess_return_above_avwap_252d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    r = _safe_log(close).diff()
    flag = (close > av).fillna(False)
    masked = r.where(flag, np.nan)
    return masked.rolling(YDAYS, min_periods=QDAYS).mean()


def f15_avwx_218_vwap_arbitrage_proxy_lag1_autocorr_63d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, MDAYS)
    spread = close - av
    def _ac1(w):
        if np.isnan(w).all() or len(w) < 10:
            return np.nan
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        a = v[:-1] - v[:-1].mean(); b = v[1:] - v[1:].mean()
        den = np.sqrt((a * a).sum() * (b * b).sum())
        if den <= 0:
            return np.nan
        return float((a * b).sum() / den)
    return spread.rolling(QDAYS, min_periods=MDAYS).apply(_ac1, raw=True)


def f15_avwx_219_avwap_252dlow_residual_volatility_63d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    res = _safe_log(close) - _safe_log(av)
    return res.rolling(QDAYS, min_periods=MDAYS).std()


def f15_avwx_220_avwap_meanreversion_speed_63d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _rolling_avwap(tp, volume, MDAYS)
    spread = close - av
    def _mrs(w):
        if np.isnan(w).all() or len(w) < 15:
            return np.nan
        v = w[~np.isnan(w)]
        if v.size < 15:
            return np.nan
        a = v[:-1] - v[:-1].mean(); b = v[1:] - v[1:].mean()
        den = (a * a).sum()
        if den <= 0:
            return np.nan
        rho = (a * b).sum() / den
        if rho <= 0 or rho >= 1:
            return np.nan
        return float(-np.log(rho))
    return spread.rolling(QDAYS, min_periods=MDAYS).apply(_mrs, raw=True)


def f15_avwx_221_avwap_persistence_above_5pct_distance_streak_63d(high, low, close, volume):
    tp = _typical_price(high, low, close)
    av = _anchored_vwap_from_event(tp, volume, _event_mask_new_window_low(low, YDAYS))
    flag = (close > av * 1.05).fillna(False)
    s = _streak_true(flag)
    return s.rolling(QDAYS, min_periods=MDAYS).max()


def f15_avwx_222_multi_anchor_breakdown_confluence_composite(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    sig = _anchored_vwap_sigma_from_event(tp, volume, anc)
    s1 = (_safe_div(close - av, sig) > 2).astype(float).fillna(0)
    a1, a2, a3, a4, a5 = _five_anchor_set(high, low, close, volume)
    s2 = ((close > a1) & (close > a2) & (close > a3) & (close > a4) & (close > a5)).astype(float).fillna(0)
    sl = _rolling_slope(av, MDAYS)
    s3 = (sl < 0).astype(float).fillna(0)
    return (s1 + s2 + s3) / 3.0


def f15_avwx_223_band_breach_x_retest_failure_composite(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_low(low, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    sig = _anchored_vwap_sigma_from_event(tp, volume, anc)
    upper = av + 2 * sig
    lower = av - sig
    up_breach = (close > upper).astype(float).where(av.notna() & sig.notna(), np.nan)
    dn_breach = (close < lower).astype(float).where(av.notna() & sig.notna(), np.nan)
    cnt_up = up_breach.rolling(QDAYS, min_periods=MDAYS).sum()
    cnt_dn = dn_breach.rolling(QDAYS, min_periods=MDAYS).sum()
    s1 = (cnt_up / QDAYS).clip(0, 1).fillna(0)
    was_above = (close.shift(1) > av.shift(1)).fillna(False)
    now_below = (close < av).fillna(False)
    fail = (was_above & now_below).astype(float)
    s2 = (fail.rolling(QDAYS, min_periods=MDAYS).sum() / 5.0).clip(0, 1).fillna(0)
    asy = _safe_div(cnt_up, cnt_dn.replace(0, 1.0))
    s3 = (asy > 3).astype(float).fillna(0)
    return (s1 + s2 + s3) / 3.0


def f15_avwx_224_vwap_anchored_terminal_distribution_composite(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_high(high, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    bs = _bars_since_true(anc)
    s1 = (bs > 21).astype(float).fillna(0)
    s2 = (close < av).astype(float).fillna(0)
    sl = _rolling_slope(av, MDAYS)
    s3 = (sl < 0).astype(float).fillna(0)
    streak = _streak_true((close < av).fillna(False))
    s4 = (streak >= 5).astype(float)
    return (s1 + s2 + s3 + s4) / 4.0


def f15_avwx_225_post_peak_vwap_deterioration_composite(high, low, close, volume):
    tp = _typical_price(high, low, close)
    anc = _event_mask_new_window_high(high, YDAYS)
    av = _anchored_vwap_from_event(tp, volume, anc)
    sl = _rolling_slope(av, MDAYS)
    q1 = sl.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    s1 = (sl <= q1).astype(float).fillna(0)
    was = (close.shift(1) > av.shift(1)).fillna(False)
    now = (close < av).fillna(False)
    cross = (was & now).astype(float)
    s2 = (cross.rolling(MDAYS, min_periods=WDAYS).sum() >= 2).astype(float).fillna(0)
    d = _safe_log(close) - _safe_log(av)
    mn = d.rolling(QDAYS, min_periods=MDAYS).min()
    s3 = (mn < -0.10).astype(float).fillna(0)
    return (s1 + s2 + s3) / 3.0


def f15_avwx_151_log_dist_avwap_from_calendar_year_start_d1(high, low, close, volume):
    return f15_avwx_151_log_dist_avwap_from_calendar_year_start(high, low, close, volume).diff()


def f15_avwx_152_log_dist_avwap_from_calendar_quarter_start_d1(high, low, close, volume):
    return f15_avwx_152_log_dist_avwap_from_calendar_quarter_start(high, low, close, volume).diff()


def f15_avwx_153_log_dist_avwap_from_calendar_month_start_d1(high, low, close, volume):
    return f15_avwx_153_log_dist_avwap_from_calendar_month_start(high, low, close, volume).diff()


def f15_avwx_154_log_dist_avwap_from_most_recent_252d_high_static_d1(high, low, close, volume):
    return f15_avwx_154_log_dist_avwap_from_most_recent_252d_high_static(high, low, close, volume).diff()


def f15_avwx_155_log_dist_avwap_from_most_recent_252d_low_static_d1(high, low, close, volume):
    return f15_avwx_155_log_dist_avwap_from_most_recent_252d_low_static(high, low, close, volume).diff()


def f15_avwx_156_log_dist_avwap_from_climactic_vol_3sigma_bar_d1(high, low, close, volume):
    return f15_avwx_156_log_dist_avwap_from_climactic_vol_3sigma_bar(high, low, close, volume).diff()


def f15_avwx_157_log_dist_avwap_from_first_close_above_sma200_252d_d1(high, low, close, volume):
    return f15_avwx_157_log_dist_avwap_from_first_close_above_sma200_252d(high, low, close, volume).diff()


def f15_avwx_158_log_dist_avwap_from_first_close_below_sma200_252d_d1(high, low, close, volume):
    return f15_avwx_158_log_dist_avwap_from_first_close_below_sma200_252d(high, low, close, volume).diff()


def f15_avwx_159_log_dist_avwap_from_first_new_52w_high_in_252d_d1(high, low, close, volume):
    return f15_avwx_159_log_dist_avwap_from_first_new_52w_high_in_252d(high, low, close, volume).diff()


def f15_avwx_160_log_dist_avwap_from_drawdown_bottom_252d_d1(high, low, close, volume):
    return f15_avwx_160_log_dist_avwap_from_drawdown_bottom_252d(high, low, close, volume).diff()


def f15_avwx_161_avwap_252dlow_plus_1sigma_breach_count_63d_d1(high, low, close, volume):
    return f15_avwx_161_avwap_252dlow_plus_1sigma_breach_count_63d(high, low, close, volume).diff()


def f15_avwx_162_avwap_252dlow_plus_2sigma_breach_count_63d_d1(high, low, close, volume):
    return f15_avwx_162_avwap_252dlow_plus_2sigma_breach_count_63d(high, low, close, volume).diff()


def f15_avwx_163_avwap_252dlow_plus_3sigma_breach_count_63d_d1(high, low, close, volume):
    return f15_avwx_163_avwap_252dlow_plus_3sigma_breach_count_63d(high, low, close, volume).diff()


def f15_avwx_164_close_distance_avwap_252dlow_in_sigma_units_d1(high, low, close, volume):
    return f15_avwx_164_close_distance_avwap_252dlow_in_sigma_units(high, low, close, volume).diff()


def f15_avwx_165_max_streak_above_avwap_252dlow_plus_1sigma_63d_d1(high, low, close, volume):
    return f15_avwx_165_max_streak_above_avwap_252dlow_plus_1sigma_63d(high, low, close, volume).diff()


def f15_avwx_166_avwap_252dlow_1sigma_band_compression_event_d1(high, low, close, volume):
    return f15_avwx_166_avwap_252dlow_1sigma_band_compression_event(high, low, close, volume).diff()


def f15_avwx_167_avwap_252dlow_1sigma_band_expansion_event_d1(high, low, close, volume):
    return f15_avwx_167_avwap_252dlow_1sigma_band_expansion_event(high, low, close, volume).diff()


def f15_avwx_168_avwap_252dlow_upper_band_walk_5bar_event_d1(high, low, close, volume):
    return f15_avwx_168_avwap_252dlow_upper_band_walk_5bar_event(high, low, close, volume).diff()


def f15_avwx_169_avwap_252dlow_band_failure_then_extension_d1(high, low, close, volume):
    return f15_avwx_169_avwap_252dlow_band_failure_then_extension(high, low, close, volume).diff()


def f15_avwx_170_avwap_252dlow_lower_band_break_count_63d_d1(high, low, close, volume):
    return f15_avwx_170_avwap_252dlow_lower_band_break_count_63d(high, low, close, volume).diff()


def f15_avwx_171_avwap_252dlow_retest_count_63d_d1(high, low, close, volume):
    return f15_avwx_171_avwap_252dlow_retest_count_63d(high, low, close, volume).diff()


def f15_avwx_172_avwap_252dlow_rejection_count_63d_d1(high, low, close, volume):
    return f15_avwx_172_avwap_252dlow_rejection_count_63d(high, low, close, volume).diff()


def f15_avwx_173_avwap_252dlow_failed_support_count_63d_d1(high, low, close, volume):
    return f15_avwx_173_avwap_252dlow_failed_support_count_63d(high, low, close, volume).diff()


def f15_avwx_174_bars_since_last_avwap_252dhigh_touch_d1(high, low, close, volume):
    return f15_avwx_174_bars_since_last_avwap_252dhigh_touch(high, low, close, volume).diff()


def f15_avwx_175_avwap_252dhigh_rejection_count_63d_d1(high, low, close, volume):
    return f15_avwx_175_avwap_252dhigh_rejection_count_63d(high, low, close, volume).diff()


def f15_avwx_176_avwap_252dlow_above_close_streak_max_63d_d1(high, low, close, volume):
    return f15_avwx_176_avwap_252dlow_above_close_streak_max_63d(high, low, close, volume).diff()


def f15_avwx_177_avwap_252dlow_retest_volume_confirmation_63d_d1(high, low, close, volume):
    return f15_avwx_177_avwap_252dlow_retest_volume_confirmation_63d(high, low, close, volume).diff()


def f15_avwx_178_avwap_252dlow_retest_doji_pattern_count_63d_d1(high, low, close, volume):
    return f15_avwx_178_avwap_252dlow_retest_doji_pattern_count_63d(high, low, close, volume).diff()


def f15_avwx_179_multi_anchor_vwap_simultaneous_retest_count_63d_d1(high, low, close, volume):
    return f15_avwx_179_multi_anchor_vwap_simultaneous_retest_count_63d(high, low, close, volume).diff()


def f15_avwx_180_avwap_252dlow_retest_then_lower_high_count_63d_d1(high, low, close, volume):
    return f15_avwx_180_avwap_252dlow_retest_then_lower_high_count_63d(high, low, close, volume).diff()


def f15_avwx_181_multi_anchor_consensus_close_above_count_d1(high, low, close, volume):
    return f15_avwx_181_multi_anchor_consensus_close_above_count(high, low, close, volume).diff()


def f15_avwx_182_multi_anchor_consensus_close_below_count_d1(high, low, close, volume):
    return f15_avwx_182_multi_anchor_consensus_close_below_count(high, low, close, volume).diff()


def f15_avwx_183_multi_anchor_dispersion_zscore_252d_d1(high, low, close, volume):
    return f15_avwx_183_multi_anchor_dispersion_zscore_252d(high, low, close, volume).diff()


def f15_avwx_184_multi_anchor_overlap_zone_count_d1(high, low, close, volume):
    return f15_avwx_184_multi_anchor_overlap_zone_count(high, low, close, volume).diff()


def f15_avwx_185_multi_anchor_breakdown_event_5d_d1(high, low, close, volume):
    return f15_avwx_185_multi_anchor_breakdown_event_5d(high, low, close, volume).diff()


def f15_avwx_186_multi_anchor_skew_index_d1(high, low, close, volume):
    return f15_avwx_186_multi_anchor_skew_index(high, low, close, volume).diff()


def f15_avwx_187_multi_anchor_cluster_compression_63d_d1(high, low, close, volume):
    return f15_avwx_187_multi_anchor_cluster_compression_63d(high, low, close, volume).diff()


def f15_avwx_188_multi_anchor_alignment_score_21d_d1(high, low, close, volume):
    return f15_avwx_188_multi_anchor_alignment_score_21d(high, low, close, volume).diff()


def f15_avwx_189_avwap_252dlow_slope_at_current_bar_5d_d1(high, low, close, volume):
    return f15_avwx_189_avwap_252dlow_slope_at_current_bar_5d(high, low, close, volume).diff()


def f15_avwx_190_avwap_252dlow_slope_acceleration_21d_d1(high, low, close, volume):
    return f15_avwx_190_avwap_252dlow_slope_acceleration_21d(high, low, close, volume).diff()


def f15_avwx_191_avwap_252dlow_slope_decay_rate_63d_d1(high, low, close, volume):
    return f15_avwx_191_avwap_252dlow_slope_decay_rate_63d(high, low, close, volume).diff()


def f15_avwx_192_avwap_252dhigh_slope_post_peak_steepness_63d_d1(high, low, close, volume):
    return f15_avwx_192_avwap_252dhigh_slope_post_peak_steepness_63d(high, low, close, volume).diff()


def f15_avwx_193_avwap_252dlow_slope_inflection_count_252d_d1(high, low, close, volume):
    return f15_avwx_193_avwap_252dlow_slope_inflection_count_252d(high, low, close, volume).diff()


def f15_avwx_194_multi_anchor_slope_dispersion_d1(high, low, close, volume):
    return f15_avwx_194_multi_anchor_slope_dispersion(high, low, close, volume).diff()


def f15_avwx_195_avwap_252dlow_slope_sign_flip_recent_5d_d1(high, low, close, volume):
    return f15_avwx_195_avwap_252dlow_slope_sign_flip_recent_5d(high, low, close, volume).diff()


def f15_avwx_196_avwap_252dlow_slope_zscore_252d_d1(high, low, close, volume):
    return f15_avwx_196_avwap_252dlow_slope_zscore_252d(high, low, close, volume).diff()


def f15_avwx_197_avwap_vs_atwap_distance_from_252dlow_d1(high, low, close, volume):
    return f15_avwx_197_avwap_vs_atwap_distance_from_252dlow(high, low, close, volume).diff()


def f15_avwx_198_avwap_vs_atwap_divergence_acceleration_63d_d1(high, low, close, volume):
    return f15_avwx_198_avwap_vs_atwap_divergence_acceleration_63d(high, low, close, volume).diff()


def f15_avwx_199_atwap_from_252dlow_distance_d1(high, low, close, volume):
    return f15_avwx_199_atwap_from_252dlow_distance(high, low, close, volume).diff()


def f15_avwx_200_avwap_vs_atwap_skew_indicator_d1(high, low, close, volume):
    return f15_avwx_200_avwap_vs_atwap_skew_indicator(high, low, close, volume).diff()


def f15_avwx_201_atwap_minus_avwap_at_peak_event_d1(high, low, close, volume):
    return f15_avwx_201_atwap_minus_avwap_at_peak_event(high, low, close, volume).diff()


def f15_avwx_202_vwap_of_vwap_5d_distance_d1(high, low, close, volume):
    return f15_avwx_202_vwap_of_vwap_5d_distance(high, low, close, volume).diff()


def f15_avwx_203_ytd_cumulative_avwap_distance_pct_d1(high, low, close, volume):
    return f15_avwx_203_ytd_cumulative_avwap_distance_pct(high, low, close, volume).diff()


def f15_avwx_204_qtd_cumulative_avwap_distance_pct_d1(high, low, close, volume):
    return f15_avwx_204_qtd_cumulative_avwap_distance_pct(high, low, close, volume).diff()


def f15_avwx_205_mtd_cumulative_avwap_distance_pct_d1(high, low, close, volume):
    return f15_avwx_205_mtd_cumulative_avwap_distance_pct(high, low, close, volume).diff()


def f15_avwx_206_multi_window_rolling_vwap_consensus_d1(high, low, close, volume):
    return f15_avwx_206_multi_window_rolling_vwap_consensus(high, low, close, volume).diff()


def f15_avwx_207_rolling_vwap_envelope_breach_count_63d_d1(high, low, close, volume):
    return f15_avwx_207_rolling_vwap_envelope_breach_count_63d(high, low, close, volume).diff()


def f15_avwx_208_avwap_252dlow_dist_when_within_5pct_of_252dhigh_d1(high, low, close, volume):
    return f15_avwx_208_avwap_252dlow_dist_when_within_5pct_of_252dhigh(high, low, close, volume).diff()


def f15_avwx_209_avwap_252dlow_dist_conditional_high_vol_regime_d1(high, low, close, volume):
    return f15_avwx_209_avwap_252dlow_dist_conditional_high_vol_regime(high, low, close, volume).diff()


def f15_avwx_210_avwap_252dlow_dist_conditional_low_vol_regime_d1(high, low, close, volume):
    return f15_avwx_210_avwap_252dlow_dist_conditional_low_vol_regime(high, low, close, volume).diff()


def f15_avwx_211_avwap_252dlow_dist_conditional_uptrend_sma200_d1(high, low, close, volume):
    return f15_avwx_211_avwap_252dlow_dist_conditional_uptrend_sma200(high, low, close, volume).diff()


def f15_avwx_212_avwap_252dlow_dist_conditional_downtrend_sma200_d1(high, low, close, volume):
    return f15_avwx_212_avwap_252dlow_dist_conditional_downtrend_sma200(high, low, close, volume).diff()


def f15_avwx_213_avwap_252dlow_retest_during_drawdown_count_63d_d1(high, low, close, volume):
    return f15_avwx_213_avwap_252dlow_retest_during_drawdown_count_63d(high, low, close, volume).diff()


def f15_avwx_214_avwap_band_compression_during_consolidation_d1(high, low, close, volume):
    return f15_avwx_214_avwap_band_compression_during_consolidation(high, low, close, volume).diff()


def f15_avwx_215_avwap_breakdown_velocity_in_high_vol_regime_d1(high, low, close, volume):
    return f15_avwx_215_avwap_breakdown_velocity_in_high_vol_regime(high, low, close, volume).diff()


def f15_avwx_216_pricing_efficiency_above_avwap_corr_63d_d1(high, low, close, volume):
    return f15_avwx_216_pricing_efficiency_above_avwap_corr_63d(high, low, close, volume).diff()


def f15_avwx_217_mean_excess_return_above_avwap_252d_d1(high, low, close, volume):
    return f15_avwx_217_mean_excess_return_above_avwap_252d(high, low, close, volume).diff()


def f15_avwx_218_vwap_arbitrage_proxy_lag1_autocorr_63d_d1(high, low, close, volume):
    return f15_avwx_218_vwap_arbitrage_proxy_lag1_autocorr_63d(high, low, close, volume).diff()


def f15_avwx_219_avwap_252dlow_residual_volatility_63d_d1(high, low, close, volume):
    return f15_avwx_219_avwap_252dlow_residual_volatility_63d(high, low, close, volume).diff()


def f15_avwx_220_avwap_meanreversion_speed_63d_d1(high, low, close, volume):
    return f15_avwx_220_avwap_meanreversion_speed_63d(high, low, close, volume).diff()


def f15_avwx_221_avwap_persistence_above_5pct_distance_streak_63d_d1(high, low, close, volume):
    return f15_avwx_221_avwap_persistence_above_5pct_distance_streak_63d(high, low, close, volume).diff()


def f15_avwx_222_multi_anchor_breakdown_confluence_composite_d1(high, low, close, volume):
    return f15_avwx_222_multi_anchor_breakdown_confluence_composite(high, low, close, volume).diff()


def f15_avwx_223_band_breach_x_retest_failure_composite_d1(high, low, close, volume):
    return f15_avwx_223_band_breach_x_retest_failure_composite(high, low, close, volume).diff()


def f15_avwx_224_vwap_anchored_terminal_distribution_composite_d1(high, low, close, volume):
    return f15_avwx_224_vwap_anchored_terminal_distribution_composite(high, low, close, volume).diff()


def f15_avwx_225_post_peak_vwap_deterioration_composite_d1(high, low, close, volume):
    return f15_avwx_225_post_peak_vwap_deterioration_composite(high, low, close, volume).diff()


ANCHORED_VWAP_EXTENSION_D1_REGISTRY_151_225 = {
    "f15_avwx_151_log_dist_avwap_from_calendar_year_start_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_151_log_dist_avwap_from_calendar_year_start_d1},
    "f15_avwx_152_log_dist_avwap_from_calendar_quarter_start_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_152_log_dist_avwap_from_calendar_quarter_start_d1},
    "f15_avwx_153_log_dist_avwap_from_calendar_month_start_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_153_log_dist_avwap_from_calendar_month_start_d1},
    "f15_avwx_154_log_dist_avwap_from_most_recent_252d_high_static_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_154_log_dist_avwap_from_most_recent_252d_high_static_d1},
    "f15_avwx_155_log_dist_avwap_from_most_recent_252d_low_static_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_155_log_dist_avwap_from_most_recent_252d_low_static_d1},
    "f15_avwx_156_log_dist_avwap_from_climactic_vol_3sigma_bar_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_156_log_dist_avwap_from_climactic_vol_3sigma_bar_d1},
    "f15_avwx_157_log_dist_avwap_from_first_close_above_sma200_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_157_log_dist_avwap_from_first_close_above_sma200_252d_d1},
    "f15_avwx_158_log_dist_avwap_from_first_close_below_sma200_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_158_log_dist_avwap_from_first_close_below_sma200_252d_d1},
    "f15_avwx_159_log_dist_avwap_from_first_new_52w_high_in_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_159_log_dist_avwap_from_first_new_52w_high_in_252d_d1},
    "f15_avwx_160_log_dist_avwap_from_drawdown_bottom_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_160_log_dist_avwap_from_drawdown_bottom_252d_d1},
    "f15_avwx_161_avwap_252dlow_plus_1sigma_breach_count_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_161_avwap_252dlow_plus_1sigma_breach_count_63d_d1},
    "f15_avwx_162_avwap_252dlow_plus_2sigma_breach_count_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_162_avwap_252dlow_plus_2sigma_breach_count_63d_d1},
    "f15_avwx_163_avwap_252dlow_plus_3sigma_breach_count_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_163_avwap_252dlow_plus_3sigma_breach_count_63d_d1},
    "f15_avwx_164_close_distance_avwap_252dlow_in_sigma_units_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_164_close_distance_avwap_252dlow_in_sigma_units_d1},
    "f15_avwx_165_max_streak_above_avwap_252dlow_plus_1sigma_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_165_max_streak_above_avwap_252dlow_plus_1sigma_63d_d1},
    "f15_avwx_166_avwap_252dlow_1sigma_band_compression_event_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_166_avwap_252dlow_1sigma_band_compression_event_d1},
    "f15_avwx_167_avwap_252dlow_1sigma_band_expansion_event_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_167_avwap_252dlow_1sigma_band_expansion_event_d1},
    "f15_avwx_168_avwap_252dlow_upper_band_walk_5bar_event_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_168_avwap_252dlow_upper_band_walk_5bar_event_d1},
    "f15_avwx_169_avwap_252dlow_band_failure_then_extension_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_169_avwap_252dlow_band_failure_then_extension_d1},
    "f15_avwx_170_avwap_252dlow_lower_band_break_count_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_170_avwap_252dlow_lower_band_break_count_63d_d1},
    "f15_avwx_171_avwap_252dlow_retest_count_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_171_avwap_252dlow_retest_count_63d_d1},
    "f15_avwx_172_avwap_252dlow_rejection_count_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_172_avwap_252dlow_rejection_count_63d_d1},
    "f15_avwx_173_avwap_252dlow_failed_support_count_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_173_avwap_252dlow_failed_support_count_63d_d1},
    "f15_avwx_174_bars_since_last_avwap_252dhigh_touch_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_174_bars_since_last_avwap_252dhigh_touch_d1},
    "f15_avwx_175_avwap_252dhigh_rejection_count_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_175_avwap_252dhigh_rejection_count_63d_d1},
    "f15_avwx_176_avwap_252dlow_above_close_streak_max_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_176_avwap_252dlow_above_close_streak_max_63d_d1},
    "f15_avwx_177_avwap_252dlow_retest_volume_confirmation_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_177_avwap_252dlow_retest_volume_confirmation_63d_d1},
    "f15_avwx_178_avwap_252dlow_retest_doji_pattern_count_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_178_avwap_252dlow_retest_doji_pattern_count_63d_d1},
    "f15_avwx_179_multi_anchor_vwap_simultaneous_retest_count_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_179_multi_anchor_vwap_simultaneous_retest_count_63d_d1},
    "f15_avwx_180_avwap_252dlow_retest_then_lower_high_count_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_180_avwap_252dlow_retest_then_lower_high_count_63d_d1},
    "f15_avwx_181_multi_anchor_consensus_close_above_count_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_181_multi_anchor_consensus_close_above_count_d1},
    "f15_avwx_182_multi_anchor_consensus_close_below_count_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_182_multi_anchor_consensus_close_below_count_d1},
    "f15_avwx_183_multi_anchor_dispersion_zscore_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_183_multi_anchor_dispersion_zscore_252d_d1},
    "f15_avwx_184_multi_anchor_overlap_zone_count_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_184_multi_anchor_overlap_zone_count_d1},
    "f15_avwx_185_multi_anchor_breakdown_event_5d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_185_multi_anchor_breakdown_event_5d_d1},
    "f15_avwx_186_multi_anchor_skew_index_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_186_multi_anchor_skew_index_d1},
    "f15_avwx_187_multi_anchor_cluster_compression_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_187_multi_anchor_cluster_compression_63d_d1},
    "f15_avwx_188_multi_anchor_alignment_score_21d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_188_multi_anchor_alignment_score_21d_d1},
    "f15_avwx_189_avwap_252dlow_slope_at_current_bar_5d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_189_avwap_252dlow_slope_at_current_bar_5d_d1},
    "f15_avwx_190_avwap_252dlow_slope_acceleration_21d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_190_avwap_252dlow_slope_acceleration_21d_d1},
    "f15_avwx_191_avwap_252dlow_slope_decay_rate_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_191_avwap_252dlow_slope_decay_rate_63d_d1},
    "f15_avwx_192_avwap_252dhigh_slope_post_peak_steepness_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_192_avwap_252dhigh_slope_post_peak_steepness_63d_d1},
    "f15_avwx_193_avwap_252dlow_slope_inflection_count_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_193_avwap_252dlow_slope_inflection_count_252d_d1},
    "f15_avwx_194_multi_anchor_slope_dispersion_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_194_multi_anchor_slope_dispersion_d1},
    "f15_avwx_195_avwap_252dlow_slope_sign_flip_recent_5d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_195_avwap_252dlow_slope_sign_flip_recent_5d_d1},
    "f15_avwx_196_avwap_252dlow_slope_zscore_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_196_avwap_252dlow_slope_zscore_252d_d1},
    "f15_avwx_197_avwap_vs_atwap_distance_from_252dlow_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_197_avwap_vs_atwap_distance_from_252dlow_d1},
    "f15_avwx_198_avwap_vs_atwap_divergence_acceleration_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_198_avwap_vs_atwap_divergence_acceleration_63d_d1},
    "f15_avwx_199_atwap_from_252dlow_distance_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_199_atwap_from_252dlow_distance_d1},
    "f15_avwx_200_avwap_vs_atwap_skew_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_200_avwap_vs_atwap_skew_indicator_d1},
    "f15_avwx_201_atwap_minus_avwap_at_peak_event_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_201_atwap_minus_avwap_at_peak_event_d1},
    "f15_avwx_202_vwap_of_vwap_5d_distance_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_202_vwap_of_vwap_5d_distance_d1},
    "f15_avwx_203_ytd_cumulative_avwap_distance_pct_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_203_ytd_cumulative_avwap_distance_pct_d1},
    "f15_avwx_204_qtd_cumulative_avwap_distance_pct_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_204_qtd_cumulative_avwap_distance_pct_d1},
    "f15_avwx_205_mtd_cumulative_avwap_distance_pct_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_205_mtd_cumulative_avwap_distance_pct_d1},
    "f15_avwx_206_multi_window_rolling_vwap_consensus_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_206_multi_window_rolling_vwap_consensus_d1},
    "f15_avwx_207_rolling_vwap_envelope_breach_count_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_207_rolling_vwap_envelope_breach_count_63d_d1},
    "f15_avwx_208_avwap_252dlow_dist_when_within_5pct_of_252dhigh_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_208_avwap_252dlow_dist_when_within_5pct_of_252dhigh_d1},
    "f15_avwx_209_avwap_252dlow_dist_conditional_high_vol_regime_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_209_avwap_252dlow_dist_conditional_high_vol_regime_d1},
    "f15_avwx_210_avwap_252dlow_dist_conditional_low_vol_regime_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_210_avwap_252dlow_dist_conditional_low_vol_regime_d1},
    "f15_avwx_211_avwap_252dlow_dist_conditional_uptrend_sma200_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_211_avwap_252dlow_dist_conditional_uptrend_sma200_d1},
    "f15_avwx_212_avwap_252dlow_dist_conditional_downtrend_sma200_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_212_avwap_252dlow_dist_conditional_downtrend_sma200_d1},
    "f15_avwx_213_avwap_252dlow_retest_during_drawdown_count_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_213_avwap_252dlow_retest_during_drawdown_count_63d_d1},
    "f15_avwx_214_avwap_band_compression_during_consolidation_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_214_avwap_band_compression_during_consolidation_d1},
    "f15_avwx_215_avwap_breakdown_velocity_in_high_vol_regime_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_215_avwap_breakdown_velocity_in_high_vol_regime_d1},
    "f15_avwx_216_pricing_efficiency_above_avwap_corr_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_216_pricing_efficiency_above_avwap_corr_63d_d1},
    "f15_avwx_217_mean_excess_return_above_avwap_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_217_mean_excess_return_above_avwap_252d_d1},
    "f15_avwx_218_vwap_arbitrage_proxy_lag1_autocorr_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_218_vwap_arbitrage_proxy_lag1_autocorr_63d_d1},
    "f15_avwx_219_avwap_252dlow_residual_volatility_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_219_avwap_252dlow_residual_volatility_63d_d1},
    "f15_avwx_220_avwap_meanreversion_speed_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_220_avwap_meanreversion_speed_63d_d1},
    "f15_avwx_221_avwap_persistence_above_5pct_distance_streak_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_221_avwap_persistence_above_5pct_distance_streak_63d_d1},
    "f15_avwx_222_multi_anchor_breakdown_confluence_composite_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_222_multi_anchor_breakdown_confluence_composite_d1},
    "f15_avwx_223_band_breach_x_retest_failure_composite_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_223_band_breach_x_retest_failure_composite_d1},
    "f15_avwx_224_vwap_anchored_terminal_distribution_composite_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_224_vwap_anchored_terminal_distribution_composite_d1},
    "f15_avwx_225_post_peak_vwap_deterioration_composite_d1": {"inputs": ["high", "low", "close", "volume"], "func": f15_avwx_225_post_peak_vwap_deterioration_composite_d1},
}
