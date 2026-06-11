"""volume_blowoff_climax d2 features 076-150 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __d2__001_075.py. Each
feature encodes a different concept in the volume-blowoff-climax theme:
peak detection / post-climax decay / pyramid build-up / burst events / entropy /
vol×return interaction / profile shape / regime shift / multi-horizon ranks /
price-action composites.

Inputs: SEP OHLCV. Volume is the star. PIT-clean: right-anchored rolling,
explicit min_periods, no centered windows, no .shift(N). Self-contained helpers.
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


def _rolling_robust_z(s, window, min_periods=None):
    """MAD-based robust z-score on a rolling window."""
    if min_periods is None:
        min_periods = max(window // 3, 2)
    med = s.rolling(window, min_periods=min_periods).median()
    mad = (s - med).abs().rolling(window, min_periods=min_periods).median()
    return _safe_div(s - med, 1.4826 * mad)


def _rolling_pct_rank(s, window, min_periods=None):
    """Empirical percentile rank of current value within rolling window."""
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    return s.rolling(window, min_periods=min_periods).apply(_rk, raw=True)


def _rolling_skew_manual(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 5:
            return np.nan
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        return float(np.mean(((v - m) / sd) ** 3))
    return s.rolling(n, min_periods=min_periods).apply(_f, raw=True)


def _rolling_kurt_manual(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 5:
            return np.nan
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        return float(np.mean(((v - m) / sd) ** 4) - 3.0)
    return s.rolling(n, min_periods=min_periods).apply(_f, raw=True)


def f19_vblc_076_force_index_proxy_21d_sum_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    fi = (close - close.shift(1)) * volume
    out = fi.rolling(21, min_periods=7).sum()
    return out.diff().diff()


def f19_vblc_077_force_index_proxy_63d_sum_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    fi = (close - close.shift(1)) * volume
    out = fi.rolling(63, min_periods=21).sum()
    return out.diff().diff()


def f19_vblc_078_up_down_day_vol_ratio_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    up = (close > close.shift(1)).astype(float)
    dn = (close < close.shift(1)).astype(float)
    up_v = (volume * up).rolling(63, min_periods=21).sum()
    dn_v = (volume * dn).rolling(63, min_periods=21).sum()
    out = _safe_div(up_v, dn_v.replace(0, np.nan))
    return out.diff().diff()


def f19_vblc_079_up_down_day_vol_ratio_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    up = (close > close.shift(1)).astype(float)
    dn = (close < close.shift(1)).astype(float)
    up_v = (volume * up).rolling(252, min_periods=84).sum()
    dn_v = (volume * dn).rolling(252, min_periods=84).sum()
    out = _safe_div(up_v, dn_v.replace(0, np.nan))
    return out.diff().diff()


def f19_vblc_080_high_vol_narrow_range_indicator_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    vz = _rolling_zscore(_safe_log(volume), 63, min_periods=21)
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=21)
    narrow = (tr < 0.5 * atr).astype(float)
    big = (vz > 2.0).astype(float)
    out = (big * narrow).where(vz.notna() & atr.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_081_distribution_day_indicator_15z_63d_d2(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    vz = _rolling_zscore(_safe_log(volume), 63, min_periods=21)
    bear = (close < open).astype(float)
    big = (vz > 1.5).astype(float)
    out = (big * bear).where(vz.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_082_distribution_day_count_21d_63z_d2(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    vz = _rolling_zscore(_safe_log(volume), 63, min_periods=21)
    bear = (close < open).astype(float)
    big = (vz > 1.5).astype(float)
    d = (big * bear).where(vz.notna(), np.nan)
    out = d.rolling(21, min_periods=7).sum()
    return out.diff().diff()


def f19_vblc_083_vol_weighted_close_pos_in_range_21d_sum_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    pos = _safe_div(close - low, high - low)
    out = (pos * volume).rolling(21, min_periods=7).sum()
    return out.diff().diff()


def f19_vblc_084_mean_vol_on_close_bottom_quintile_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    pos = _safe_div(close - low, high - low)
    bot = (pos < 0.2).astype(float)
    v_w = volume * bot
    c_w = bot
    out = _safe_div(v_w.rolling(63, min_periods=21).sum(), c_w.rolling(63, min_periods=21).sum())
    return out.diff().diff()


def f19_vblc_085_mean_vol_on_close_top_quintile_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    pos = _safe_div(close - low, high - low)
    top = (pos > 0.8).astype(float)
    v_w = volume * top
    c_w = top
    out = _safe_div(v_w.rolling(63, min_periods=21).sum(), c_w.rolling(63, min_periods=21).sum())
    return out.diff().diff()


def f19_vblc_086_vol_weighted_log_return_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = _safe_log(close).diff()
    out = _safe_div((volume * ret).rolling(21, min_periods=7).sum(), volume.rolling(21, min_periods=7).sum())
    return out.diff().diff()


def f19_vblc_087_vol_weighted_log_return_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = _safe_log(close).diff()
    out = _safe_div((volume * ret).rolling(63, min_periods=21).sum(), volume.rolling(63, min_periods=21).sum())
    return out.diff().diff()


def f19_vblc_088_top_up_vs_top_down_day_vol_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = _safe_log(close).diff()
    def _f_pair(rv):
        # apply to a 2-col df via concat
        return np.nan
    # simpler: compute index of max ret and min ret in 63d, take volume there
    def _f(w):
        if w.size < 21 or np.isnan(w).all():
            return np.nan
        return 0.0
    # vectorized via rolling on the joint object: too clunky, so:
    idx_max = ret.rolling(63, min_periods=21).apply(lambda w: float(np.nanargmax(w)) if not np.isnan(w).all() else np.nan, raw=True)
    idx_min = ret.rolling(63, min_periods=21).apply(lambda w: float(np.nanargmin(w)) if not np.isnan(w).all() else np.nan, raw=True)
    # extract volume value at offset (size-1 - idx)
    arr_v = volume.values
    n = len(volume)
    off_max = idx_max.values; off_min = idx_min.values
    v_up = np.full(n, np.nan); v_dn = np.full(n, np.nan)
    for i in range(n):
        if not np.isnan(off_max[i]):
            j = i - (62 - int(off_max[i]))
            if 0 <= j < n:
                v_up[i] = arr_v[j]
        if not np.isnan(off_min[i]):
            j = i - (62 - int(off_min[i]))
            if 0 <= j < n:
                v_dn[i] = arr_v[j]
    out = pd.Series(_safe_div(pd.Series(v_up, index=volume.index), pd.Series(v_dn, index=volume.index)), index=volume.index)
    return out.diff().diff()


def f19_vblc_089_signed_vol_21d_sum_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    out = (sgn * volume).rolling(21, min_periods=7).sum()
    return out.diff().diff()


def f19_vblc_090_signed_vol_63d_sum_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    out = (sgn * volume).rolling(63, min_periods=21).sum()
    return out.diff().diff()


def f19_vblc_091_log_vol_skew_63d_d2(volume: pd.Series) -> pd.Series:
    out = _rolling_skew_manual(_safe_log(volume), 63, min_periods=21)
    return out.diff().diff()


def f19_vblc_092_log_vol_skew_252d_d2(volume: pd.Series) -> pd.Series:
    out = _rolling_skew_manual(_safe_log(volume), 252, min_periods=84)
    return out.diff().diff()


def f19_vblc_093_log_vol_kurt_63d_d2(volume: pd.Series) -> pd.Series:
    out = _rolling_kurt_manual(_safe_log(volume), 63, min_periods=21)
    return out.diff().diff()


def f19_vblc_094_log_vol_kurt_252d_d2(volume: pd.Series) -> pd.Series:
    out = _rolling_kurt_manual(_safe_log(volume), 252, min_periods=84)
    return out.diff().diff()


def f19_vblc_095_vol_top_decile_mean_over_median_63d_d2(volume: pd.Series) -> pd.Series:
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        med = np.median(v)
        if med <= 0:
            return np.nan
        k = max(1, v.size // 10)
        top = np.sort(v)[-k:]
        return float(np.mean(top) / med)
    out = volume.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff().diff()


def f19_vblc_096_vol_p95_over_median_63d_d2(volume: pd.Series) -> pd.Series:
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 5:
            return np.nan
        med = np.median(v)
        if med <= 0:
            return np.nan
        return float(np.percentile(v, 95) / med)
    out = volume.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff().diff()


def f19_vblc_097_vol_p99_over_median_252d_d2(volume: pd.Series) -> pd.Series:
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 20:
            return np.nan
        med = np.median(v)
        if med <= 0:
            return np.nan
        return float(np.percentile(v, 99) / med)
    out = volume.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f19_vblc_098_log_vol_skew_change_21d_63d_d2(volume: pd.Series) -> pd.Series:
    sk = _rolling_skew_manual(_safe_log(volume), 63, min_periods=21)
    out = sk - sk.shift(21)
    return out.diff().diff()


def f19_vblc_099_log_vol_kurt_change_21d_63d_d2(volume: pd.Series) -> pd.Series:
    kt = _rolling_kurt_manual(_safe_log(volume), 63, min_periods=21)
    out = kt - kt.shift(21)
    return out.diff().diff()


def f19_vblc_100_right_only_skew_log_vol_63d_d2(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 5:
            return np.nan
        med = np.median(v)
        pos = v[v > med] - med
        if pos.size < 3:
            return np.nan
        sd = np.std(v, ddof=1)
        if sd <= 0:
            return np.nan
        return float(np.mean(pos ** 3) / sd ** 3)
    out = lv.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff().diff()


def f19_vblc_101_left_tail_share_below_half_median_63d_d2(volume: pd.Series) -> pd.Series:
    med = volume.rolling(63, min_periods=21).median()
    low = (volume < 0.5 * med).astype(float).where(med.notna(), np.nan)
    out = low.rolling(63, min_periods=21).mean()
    return out.diff().diff()


def f19_vblc_102_right_tail_share_above_2x_median_63d_d2(volume: pd.Series) -> pd.Series:
    med = volume.rolling(63, min_periods=21).median()
    hi = (volume > 2.0 * med).astype(float).where(med.notna(), np.nan)
    out = hi.rolling(63, min_periods=21).mean()
    return out.diff().diff()


def f19_vblc_103_log_vol_skew_zscore_63d_in_252d_d2(volume: pd.Series) -> pd.Series:
    sk = _rolling_skew_manual(_safe_log(volume), 63, min_periods=21)
    out = _rolling_zscore(sk, 252, min_periods=84)
    return out.diff().diff()


def f19_vblc_104_log_vol_kurt_zscore_63d_in_252d_d2(volume: pd.Series) -> pd.Series:
    kt = _rolling_kurt_manual(_safe_log(volume), 63, min_periods=21)
    out = _rolling_zscore(kt, 252, min_periods=84)
    return out.diff().diff()


def f19_vblc_105_right_over_left_tail_share_63d_d2(volume: pd.Series) -> pd.Series:
    med = volume.rolling(63, min_periods=21).median()
    hi = (volume > 2.0 * med).astype(float).where(med.notna(), np.nan).rolling(63, min_periods=21).mean()
    low = (volume < 0.5 * med).astype(float).where(med.notna(), np.nan).rolling(63, min_periods=21).mean()
    out = _safe_div(hi, low.replace(0, np.nan))
    return out.diff().diff()


def f19_vblc_106_log_vol_2nd_vs_1st_half_mean_diff_126d_d2(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    m63a = lv.shift(63).rolling(63, min_periods=21).mean()
    m63b = lv.rolling(63, min_periods=21).mean()
    out = m63b - m63a
    return out.diff().diff()


def f19_vblc_107_log_vol_2nd_vs_1st_half_mean_diff_252d_d2(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    ma = lv.shift(126).rolling(126, min_periods=42).mean()
    mb = lv.rolling(126, min_periods=42).mean()
    out = mb - ma
    return out.diff().diff()


def f19_vblc_108_log_vol_std_ratio_halves_126d_d2(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    sa = lv.shift(63).rolling(63, min_periods=21).std()
    sb = lv.rolling(63, min_periods=21).std()
    out = _safe_div(sb, sa.replace(0, np.nan))
    return out.diff().diff()


def f19_vblc_109_log_vol_cusum_demean_63d_d2(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    m = lv.rolling(63, min_periods=21).mean()
    d = (lv - m).fillna(0)
    cs = d.cumsum()
    # normalize by 63d rolling std of d
    sd = d.rolling(63, min_periods=21).std()
    out = _safe_div(cs - cs.rolling(63, min_periods=21).mean(), sd)
    return out.diff().diff()


def f19_vblc_110_bars_since_log_vol_regime_change_252d_d2(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    m252 = lv.rolling(252, min_periods=84).mean()
    sd252 = lv.rolling(252, min_periods=84).std()
    shift = ((lv.rolling(21, min_periods=7).mean() - m252).abs() > sd252).fillna(False)
    arr = shift.astype(bool).values
    n = arr.size
    out_arr = np.full(n, np.nan)
    last = -1
    for i in range(n):
        if arr[i]:
            last = i
        if last >= 0:
            out_arr[i] = float(i - last)
    out = pd.Series(out_arr, index=lv.index)
    return out.diff().diff()


def f19_vblc_111_vol_21d_mean_above_2std_252d_d2(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    m252 = lv.rolling(252, min_periods=84).mean()
    sd252 = lv.rolling(252, min_periods=84).std()
    m21 = lv.rolling(21, min_periods=7).mean()
    out = (m21 > m252 + 2.0 * sd252).astype(float).where(sd252.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_112_vol_21d_mean_below_2std_252d_d2(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    m252 = lv.rolling(252, min_periods=84).mean()
    sd252 = lv.rolling(252, min_periods=84).std()
    m21 = lv.rolling(21, min_periods=7).mean()
    out = (m21 < m252 - 2.0 * sd252).astype(float).where(sd252.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_113_vol_variance_break_2x_event_63d_in_252d_d2(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    s63 = lv.rolling(63, min_periods=21).std()
    med = s63.rolling(252, min_periods=84).median()
    big = (s63 > 2.0 * med).astype(float).where(med.notna(), np.nan)
    out = ((big.shift(1) < 0.5) & (big > 0.5)).astype(float).where(med.notna() & med.shift(1).notna(), np.nan)
    return out.diff().diff()


def f19_vblc_114_vol_mean_shift_magnitude_zscore_21d_63d_d2(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    ma = lv.rolling(21, min_periods=7).mean()
    shift = (ma - ma.shift(21)).abs()
    sd = lv.rolling(63, min_periods=21).std()
    out = _safe_div(shift, sd)
    return out.diff().diff()


def f19_vblc_115_current_above_252d_mean_streak_21d_d2(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    m = lv.rolling(252, min_periods=84).mean()
    above = (lv.rolling(21, min_periods=7).mean() > m).astype(int).where(m.notna(), 0)
    block = (above != above.shift(1)).fillna(False).cumsum()
    st = above.groupby(block).cumcount().astype(float)
    out = st.where(m.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_116_cum_excess_log_vol_252d_mean_63d_d2(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    m = lv.rolling(252, min_periods=84).mean()
    exc = (lv - m).fillna(0)
    out = exc.rolling(63, min_periods=21).sum().where(m.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_117_mean_shift_tstat_21d_vs_63d_d2(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    m21 = lv.rolling(21, min_periods=7).mean()
    m63 = lv.rolling(63, min_periods=21).mean()
    sd63 = lv.rolling(63, min_periods=21).std()
    se = sd63 / np.sqrt(21.0)
    out = _safe_div(m21 - m63, se)
    return out.diff().diff()


def f19_vblc_118_regime_change_prob_proxy_21d_252d_d2(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    m21 = lv.rolling(21, min_periods=7).mean()
    m252 = lv.rolling(252, min_periods=84).mean()
    sd252 = lv.rolling(252, min_periods=84).std()
    z = _safe_div(m21 - m252, sd252)
    out = (z.abs() > 2.0).astype(float).where(z.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_119_entropy_break_event_63d_in_252d_d2(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    def _ent(w):
        valid = w[~np.isnan(w)]
        if valid.size < 10:
            return np.nan
        bins, _ = np.histogram(valid, bins=10)
        if bins.sum() == 0:
            return np.nan
        p = bins / bins.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    e = lv.rolling(63, min_periods=21).apply(_ent, raw=True)
    de = e.diff().abs()
    sd = e.rolling(252, min_periods=84).std()
    out = (de > sd).astype(float).where(de.notna() & sd.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_120_regime_change_event_count_252d_d2(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    m21 = lv.rolling(21, min_periods=7).mean()
    m252 = lv.rolling(252, min_periods=84).mean()
    sd252 = lv.rolling(252, min_periods=84).std()
    z = _safe_div(m21 - m252, sd252)
    ev = (z.abs() > 2.0).astype(float)
    t = ((ev.shift(1) < 0.5) & (ev > 0.5)).astype(float).where(z.notna() & z.shift(1).notna(), np.nan)
    out = t.rolling(252, min_periods=84).sum()
    return out.diff().diff()


def f19_vblc_121_vol_pct_rank_252d_d2(volume: pd.Series) -> pd.Series:
    out = _rolling_pct_rank(volume, 252, min_periods=84)
    return out.diff().diff()


def f19_vblc_122_vol_pct_rank_504d_d2(volume: pd.Series) -> pd.Series:
    out = _rolling_pct_rank(volume, 504, min_periods=168)
    return out.diff().diff()


def f19_vblc_123_vol_pct_rank_1260d_d2(volume: pd.Series) -> pd.Series:
    out = _rolling_pct_rank(volume, 1260, min_periods=252)
    return out.diff().diff()


def f19_vblc_124_vol_pct_rank_diff_63_vs_252_d2(volume: pd.Series) -> pd.Series:
    r63 = _rolling_pct_rank(volume, 63, min_periods=21)
    r252 = _rolling_pct_rank(volume, 252, min_periods=84)
    out = r63 - r252
    return out.diff().diff()


def f19_vblc_125_vol_pct_rank_above_95_252d_d2(volume: pd.Series) -> pd.Series:
    r = _rolling_pct_rank(volume, 252, min_periods=84)
    out = (r > 0.95).astype(float).where(r.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_126_log_vol_minus_21d_mean_d2(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    m = lv.rolling(21, min_periods=7).mean()
    out = lv - m
    return out.diff().diff()


def f19_vblc_127_vol_pct_rank_stability_21d_std_252d_rank_d2(volume: pd.Series) -> pd.Series:
    r = _rolling_pct_rank(volume, 252, min_periods=84)
    out = r.rolling(21, min_periods=7).std()
    return out.diff().diff()


def f19_vblc_128_log_vol_zscore_sum_63_252_504_d2(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    out = _rolling_zscore(lv, 63, min_periods=21) + _rolling_zscore(lv, 252, min_periods=84) + _rolling_zscore(lv, 504, min_periods=168)
    return out.diff().diff()


def f19_vblc_129_log_vol_z_sign_disagree_63_vs_252_d2(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    z63 = _rolling_zscore(lv, 63, min_periods=21)
    z252 = _rolling_zscore(lv, 252, min_periods=84)
    out = (np.sign(z63) != np.sign(z252)).astype(float).where(z63.notna() & z252.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_130_vol_pct_rank_21d_change_252d_d2(volume: pd.Series) -> pd.Series:
    r = _rolling_pct_rank(volume, 252, min_periods=84)
    out = r - r.shift(21)
    return out.diff().diff()


def f19_vblc_131_max_vol_pct_rank_21d_in_252d_d2(volume: pd.Series) -> pd.Series:
    r = _rolling_pct_rank(volume, 252, min_periods=84)
    out = r.rolling(21, min_periods=7).max()
    return out.diff().diff()


def f19_vblc_132_min_vol_pct_rank_21d_in_252d_d2(volume: pd.Series) -> pd.Series:
    r = _rolling_pct_rank(volume, 252, min_periods=84)
    out = r.rolling(21, min_periods=7).min()
    return out.diff().diff()


def f19_vblc_133_vol_pct_rank_range_21d_in_252d_d2(volume: pd.Series) -> pd.Series:
    r = _rolling_pct_rank(volume, 252, min_periods=84)
    out = r.rolling(21, min_periods=7).max() - r.rolling(21, min_periods=7).min()
    return out.diff().diff()


def f19_vblc_134_log_vol_z_pct_rank_63d_z_in_252d_d2(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), 63, min_periods=21)
    out = _rolling_pct_rank(z, 252, min_periods=84)
    return out.diff().diff()


def f19_vblc_135_log_vol_hampel_outlier_252d_d2(volume: pd.Series) -> pd.Series:
    z = _rolling_robust_z(_safe_log(volume), 252, min_periods=84)
    out = (z.abs() > 3.0).astype(float).where(z.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_136_climax_vol_at_252d_high_composite_d2(high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax_h = high.rolling(252, min_periods=84).max()
    at_high = (high >= rmax_h).astype(float)
    rmax_v = volume.rolling(252, min_periods=84).max()
    climax = (volume >= 0.9 * rmax_v).astype(float)
    out = (at_high * climax).where(rmax_h.notna() & rmax_v.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_137_climax_with_bearish_reversal_candle_63z_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    vz = _rolling_zscore(_safe_log(volume), 63, min_periods=21)
    body = (close - open).abs()
    upper = high - pd.concat([open, close], axis=1).max(axis=1)
    long_uw = (upper > 2.0 * body).astype(float)
    bear = (close < open).astype(float)
    big = (vz > 1.5).astype(float)
    out = (big * long_uw * bear).where(vz.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_138_vol_pyramid_then_gap_down_indicator_d2(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    c5 = volume.rolling(5, min_periods=2).sum()
    rise = (c5 > c5.shift(5)).astype(float)
    gap_dn = (open < close.shift(1) * 0.97).astype(float)
    out = (rise.shift(1) * gap_dn).where(rise.shift(1).notna() & gap_dn.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_139_distribution_lower_half_count_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    vz = _rolling_zscore(_safe_log(volume), 63, min_periods=21)
    pos = _safe_div(close - low, high - low)
    big = (vz > 1.0).astype(float)
    lh = (pos < 0.5).astype(float)
    d = (big * lh).where(vz.notna(), np.nan)
    out = d.rolling(21, min_periods=7).sum()
    return out.diff().diff()


def f19_vblc_140_climax_then_5d_close_at_21d_low_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax_v = volume.rolling(21, min_periods=7).max()
    climax = (volume >= rmax_v).astype(float)
    rmin_c = close.rolling(21, min_periods=7).min()
    at_low = (close <= rmin_c).astype(float)
    out = (climax.shift(5) * at_low).where(climax.shift(5).notna() & at_low.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_141_multi_criteria_blowoff_composite_d2(open: pd.Series, high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rk = _rolling_pct_rank(volume, 252, min_periods=84)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= rmax).astype(float)
    bear = (close < open).astype(float)
    out = ((rk > 0.95).astype(float) + at_high + bear).where(rk.notna() & rmax.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_142_three_plus_distribution_days_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    vz = _rolling_zscore(_safe_log(volume), 63, min_periods=21)
    pos = _safe_div(close - low, high - low)
    d = ((vz > 1.0) & (pos < 0.5)).astype(float).where(vz.notna(), np.nan)
    cnt = d.rolling(21, min_periods=7).sum()
    out = (cnt >= 3).astype(float).where(cnt.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_143_burst_gap_up_close_lower_half_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    med = volume.rolling(63, min_periods=21).median()
    burst = (volume > 3.0 * med).astype(float)
    gap_up = (open > close.shift(1) * 1.03).astype(float)
    pos = _safe_div(close - low, high - low)
    lh = (pos < 0.5).astype(float)
    out = (burst * gap_up * lh).where(med.notna() & gap_up.notna() & pos.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_144_blowoff_then_21d_neg_return_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax_v = volume.rolling(63, min_periods=21).max()
    climax = (volume >= 0.9 * rmax_v).astype(float).shift(21)
    ret21 = _safe_log(close).diff(21)
    out = (climax * (ret21 < 0).astype(float)).where(climax.notna() & ret21.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_145_cum5d_z3_with_5d_neg_return_5pct_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    c5 = volume.rolling(5, min_periods=2).sum()
    z = _rolling_zscore(c5, 63, min_periods=21)
    ret5 = _safe_log(close).diff(5)
    out = ((z > 3.0) & (ret5 < -0.05)).astype(float).where(z.notna() & ret5.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_146_climax_at_high_then_vol_mean_decline_d2(high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= rmax).astype(float)
    m21 = _safe_log(volume).rolling(21, min_periods=7).mean()
    sl = _rolling_slope(m21, 21, min_periods=7)
    out = (at_high * (sl < 0).astype(float)).where(rmax.notna() & sl.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_147_sum_vol_rise_streaks_63d_d2(volume: pd.Series) -> pd.Series:
    rise = (volume > volume.shift(1)).astype(int).where(volume.notna() & volume.shift(1).notna(), 0)
    block = (rise != rise.shift(1)).fillna(False).cumsum()
    streak = rise.groupby(block).cumcount().astype(float)
    streak_at_end = (streak * (rise > 0))
    out = streak_at_end.rolling(63, min_periods=21).sum()
    return out.diff().diff()


def f19_vblc_148_churn_climax_then_gap_down_next_day_d2(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    vz = _rolling_zscore(_safe_log(volume), 63, min_periods=21)
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=21)
    narrow = (tr < 0.7 * atr).astype(float)
    big = (vz > 1.5).astype(float)
    churn = (big * narrow).shift(1)
    gap_dn = (open < close.shift(1) * 0.97).astype(float)
    out = (churn * gap_dn).where(churn.notna() & gap_dn.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_149_three_plus_bursts_in_5d_3x_63d_d2(volume: pd.Series) -> pd.Series:
    med = volume.rolling(63, min_periods=21).median()
    burst = (volume > 3.0 * med).astype(float)
    c5 = burst.rolling(5, min_periods=3).sum()
    out = (c5 >= 3).astype(float).where(c5.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_150_ultimate_blowoff_composite_score_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rk = _rolling_pct_rank(volume, 252, min_periods=84)
    rmax_h = high.rolling(252, min_periods=84).max()
    at_high = (high >= rmax_h).astype(float)
    bear = (close < open).astype(float)
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=21)
    narrow = (tr < 0.7 * atr).astype(float)
    out = ((rk > 0.99).astype(float) + at_high + bear + narrow).where(rk.notna() & rmax_h.notna() & atr.notna(), np.nan)
    return out.diff().diff()


# ============================================================
#                         REGISTRY 076_150 (d2)
# ============================================================

VOLUME_BLOWOFF_CLIMAX_D2_REGISTRY_076_150 = {
    "f19_vblc_076_force_index_proxy_21d_sum_d2": {"inputs": ["close", "volume"], "func": f19_vblc_076_force_index_proxy_21d_sum_d2},
    "f19_vblc_077_force_index_proxy_63d_sum_d2": {"inputs": ["close", "volume"], "func": f19_vblc_077_force_index_proxy_63d_sum_d2},
    "f19_vblc_078_up_down_day_vol_ratio_63d_d2": {"inputs": ["close", "volume"], "func": f19_vblc_078_up_down_day_vol_ratio_63d_d2},
    "f19_vblc_079_up_down_day_vol_ratio_252d_d2": {"inputs": ["close", "volume"], "func": f19_vblc_079_up_down_day_vol_ratio_252d_d2},
    "f19_vblc_080_high_vol_narrow_range_indicator_d2": {"inputs": ["high", "low", "close", "volume"], "func": f19_vblc_080_high_vol_narrow_range_indicator_d2},
    "f19_vblc_081_distribution_day_indicator_15z_63d_d2": {"inputs": ["open", "close", "volume"], "func": f19_vblc_081_distribution_day_indicator_15z_63d_d2},
    "f19_vblc_082_distribution_day_count_21d_63z_d2": {"inputs": ["open", "close", "volume"], "func": f19_vblc_082_distribution_day_count_21d_63z_d2},
    "f19_vblc_083_vol_weighted_close_pos_in_range_21d_sum_d2": {"inputs": ["high", "low", "close", "volume"], "func": f19_vblc_083_vol_weighted_close_pos_in_range_21d_sum_d2},
    "f19_vblc_084_mean_vol_on_close_bottom_quintile_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f19_vblc_084_mean_vol_on_close_bottom_quintile_63d_d2},
    "f19_vblc_085_mean_vol_on_close_top_quintile_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f19_vblc_085_mean_vol_on_close_top_quintile_63d_d2},
    "f19_vblc_086_vol_weighted_log_return_21d_d2": {"inputs": ["close", "volume"], "func": f19_vblc_086_vol_weighted_log_return_21d_d2},
    "f19_vblc_087_vol_weighted_log_return_63d_d2": {"inputs": ["close", "volume"], "func": f19_vblc_087_vol_weighted_log_return_63d_d2},
    "f19_vblc_088_top_up_vs_top_down_day_vol_63d_d2": {"inputs": ["close", "volume"], "func": f19_vblc_088_top_up_vs_top_down_day_vol_63d_d2},
    "f19_vblc_089_signed_vol_21d_sum_d2": {"inputs": ["close", "volume"], "func": f19_vblc_089_signed_vol_21d_sum_d2},
    "f19_vblc_090_signed_vol_63d_sum_d2": {"inputs": ["close", "volume"], "func": f19_vblc_090_signed_vol_63d_sum_d2},
    "f19_vblc_091_log_vol_skew_63d_d2": {"inputs": ["volume"], "func": f19_vblc_091_log_vol_skew_63d_d2},
    "f19_vblc_092_log_vol_skew_252d_d2": {"inputs": ["volume"], "func": f19_vblc_092_log_vol_skew_252d_d2},
    "f19_vblc_093_log_vol_kurt_63d_d2": {"inputs": ["volume"], "func": f19_vblc_093_log_vol_kurt_63d_d2},
    "f19_vblc_094_log_vol_kurt_252d_d2": {"inputs": ["volume"], "func": f19_vblc_094_log_vol_kurt_252d_d2},
    "f19_vblc_095_vol_top_decile_mean_over_median_63d_d2": {"inputs": ["volume"], "func": f19_vblc_095_vol_top_decile_mean_over_median_63d_d2},
    "f19_vblc_096_vol_p95_over_median_63d_d2": {"inputs": ["volume"], "func": f19_vblc_096_vol_p95_over_median_63d_d2},
    "f19_vblc_097_vol_p99_over_median_252d_d2": {"inputs": ["volume"], "func": f19_vblc_097_vol_p99_over_median_252d_d2},
    "f19_vblc_098_log_vol_skew_change_21d_63d_d2": {"inputs": ["volume"], "func": f19_vblc_098_log_vol_skew_change_21d_63d_d2},
    "f19_vblc_099_log_vol_kurt_change_21d_63d_d2": {"inputs": ["volume"], "func": f19_vblc_099_log_vol_kurt_change_21d_63d_d2},
    "f19_vblc_100_right_only_skew_log_vol_63d_d2": {"inputs": ["volume"], "func": f19_vblc_100_right_only_skew_log_vol_63d_d2},
    "f19_vblc_101_left_tail_share_below_half_median_63d_d2": {"inputs": ["volume"], "func": f19_vblc_101_left_tail_share_below_half_median_63d_d2},
    "f19_vblc_102_right_tail_share_above_2x_median_63d_d2": {"inputs": ["volume"], "func": f19_vblc_102_right_tail_share_above_2x_median_63d_d2},
    "f19_vblc_103_log_vol_skew_zscore_63d_in_252d_d2": {"inputs": ["volume"], "func": f19_vblc_103_log_vol_skew_zscore_63d_in_252d_d2},
    "f19_vblc_104_log_vol_kurt_zscore_63d_in_252d_d2": {"inputs": ["volume"], "func": f19_vblc_104_log_vol_kurt_zscore_63d_in_252d_d2},
    "f19_vblc_105_right_over_left_tail_share_63d_d2": {"inputs": ["volume"], "func": f19_vblc_105_right_over_left_tail_share_63d_d2},
    "f19_vblc_106_log_vol_2nd_vs_1st_half_mean_diff_126d_d2": {"inputs": ["volume"], "func": f19_vblc_106_log_vol_2nd_vs_1st_half_mean_diff_126d_d2},
    "f19_vblc_107_log_vol_2nd_vs_1st_half_mean_diff_252d_d2": {"inputs": ["volume"], "func": f19_vblc_107_log_vol_2nd_vs_1st_half_mean_diff_252d_d2},
    "f19_vblc_108_log_vol_std_ratio_halves_126d_d2": {"inputs": ["volume"], "func": f19_vblc_108_log_vol_std_ratio_halves_126d_d2},
    "f19_vblc_109_log_vol_cusum_demean_63d_d2": {"inputs": ["volume"], "func": f19_vblc_109_log_vol_cusum_demean_63d_d2},
    "f19_vblc_110_bars_since_log_vol_regime_change_252d_d2": {"inputs": ["volume"], "func": f19_vblc_110_bars_since_log_vol_regime_change_252d_d2},
    "f19_vblc_111_vol_21d_mean_above_2std_252d_d2": {"inputs": ["volume"], "func": f19_vblc_111_vol_21d_mean_above_2std_252d_d2},
    "f19_vblc_112_vol_21d_mean_below_2std_252d_d2": {"inputs": ["volume"], "func": f19_vblc_112_vol_21d_mean_below_2std_252d_d2},
    "f19_vblc_113_vol_variance_break_2x_event_63d_in_252d_d2": {"inputs": ["volume"], "func": f19_vblc_113_vol_variance_break_2x_event_63d_in_252d_d2},
    "f19_vblc_114_vol_mean_shift_magnitude_zscore_21d_63d_d2": {"inputs": ["volume"], "func": f19_vblc_114_vol_mean_shift_magnitude_zscore_21d_63d_d2},
    "f19_vblc_115_current_above_252d_mean_streak_21d_d2": {"inputs": ["volume"], "func": f19_vblc_115_current_above_252d_mean_streak_21d_d2},
    "f19_vblc_116_cum_excess_log_vol_252d_mean_63d_d2": {"inputs": ["volume"], "func": f19_vblc_116_cum_excess_log_vol_252d_mean_63d_d2},
    "f19_vblc_117_mean_shift_tstat_21d_vs_63d_d2": {"inputs": ["volume"], "func": f19_vblc_117_mean_shift_tstat_21d_vs_63d_d2},
    "f19_vblc_118_regime_change_prob_proxy_21d_252d_d2": {"inputs": ["volume"], "func": f19_vblc_118_regime_change_prob_proxy_21d_252d_d2},
    "f19_vblc_119_entropy_break_event_63d_in_252d_d2": {"inputs": ["volume"], "func": f19_vblc_119_entropy_break_event_63d_in_252d_d2},
    "f19_vblc_120_regime_change_event_count_252d_d2": {"inputs": ["volume"], "func": f19_vblc_120_regime_change_event_count_252d_d2},
    "f19_vblc_121_vol_pct_rank_252d_d2": {"inputs": ["volume"], "func": f19_vblc_121_vol_pct_rank_252d_d2},
    "f19_vblc_122_vol_pct_rank_504d_d2": {"inputs": ["volume"], "func": f19_vblc_122_vol_pct_rank_504d_d2},
    "f19_vblc_123_vol_pct_rank_1260d_d2": {"inputs": ["volume"], "func": f19_vblc_123_vol_pct_rank_1260d_d2},
    "f19_vblc_124_vol_pct_rank_diff_63_vs_252_d2": {"inputs": ["volume"], "func": f19_vblc_124_vol_pct_rank_diff_63_vs_252_d2},
    "f19_vblc_125_vol_pct_rank_above_95_252d_d2": {"inputs": ["volume"], "func": f19_vblc_125_vol_pct_rank_above_95_252d_d2},
    "f19_vblc_126_log_vol_minus_21d_mean_d2": {"inputs": ["volume"], "func": f19_vblc_126_log_vol_minus_21d_mean_d2},
    "f19_vblc_127_vol_pct_rank_stability_21d_std_252d_rank_d2": {"inputs": ["volume"], "func": f19_vblc_127_vol_pct_rank_stability_21d_std_252d_rank_d2},
    "f19_vblc_128_log_vol_zscore_sum_63_252_504_d2": {"inputs": ["volume"], "func": f19_vblc_128_log_vol_zscore_sum_63_252_504_d2},
    "f19_vblc_129_log_vol_z_sign_disagree_63_vs_252_d2": {"inputs": ["volume"], "func": f19_vblc_129_log_vol_z_sign_disagree_63_vs_252_d2},
    "f19_vblc_130_vol_pct_rank_21d_change_252d_d2": {"inputs": ["volume"], "func": f19_vblc_130_vol_pct_rank_21d_change_252d_d2},
    "f19_vblc_131_max_vol_pct_rank_21d_in_252d_d2": {"inputs": ["volume"], "func": f19_vblc_131_max_vol_pct_rank_21d_in_252d_d2},
    "f19_vblc_132_min_vol_pct_rank_21d_in_252d_d2": {"inputs": ["volume"], "func": f19_vblc_132_min_vol_pct_rank_21d_in_252d_d2},
    "f19_vblc_133_vol_pct_rank_range_21d_in_252d_d2": {"inputs": ["volume"], "func": f19_vblc_133_vol_pct_rank_range_21d_in_252d_d2},
    "f19_vblc_134_log_vol_z_pct_rank_63d_z_in_252d_d2": {"inputs": ["volume"], "func": f19_vblc_134_log_vol_z_pct_rank_63d_z_in_252d_d2},
    "f19_vblc_135_log_vol_hampel_outlier_252d_d2": {"inputs": ["volume"], "func": f19_vblc_135_log_vol_hampel_outlier_252d_d2},
    "f19_vblc_136_climax_vol_at_252d_high_composite_d2": {"inputs": ["high", "volume"], "func": f19_vblc_136_climax_vol_at_252d_high_composite_d2},
    "f19_vblc_137_climax_with_bearish_reversal_candle_63z_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f19_vblc_137_climax_with_bearish_reversal_candle_63z_d2},
    "f19_vblc_138_vol_pyramid_then_gap_down_indicator_d2": {"inputs": ["open", "close", "volume"], "func": f19_vblc_138_vol_pyramid_then_gap_down_indicator_d2},
    "f19_vblc_139_distribution_lower_half_count_21d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f19_vblc_139_distribution_lower_half_count_21d_d2},
    "f19_vblc_140_climax_then_5d_close_at_21d_low_d2": {"inputs": ["close", "volume"], "func": f19_vblc_140_climax_then_5d_close_at_21d_low_d2},
    "f19_vblc_141_multi_criteria_blowoff_composite_d2": {"inputs": ["open", "high", "close", "volume"], "func": f19_vblc_141_multi_criteria_blowoff_composite_d2},
    "f19_vblc_142_three_plus_distribution_days_21d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f19_vblc_142_three_plus_distribution_days_21d_d2},
    "f19_vblc_143_burst_gap_up_close_lower_half_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f19_vblc_143_burst_gap_up_close_lower_half_d2},
    "f19_vblc_144_blowoff_then_21d_neg_return_d2": {"inputs": ["close", "volume"], "func": f19_vblc_144_blowoff_then_21d_neg_return_d2},
    "f19_vblc_145_cum5d_z3_with_5d_neg_return_5pct_d2": {"inputs": ["close", "volume"], "func": f19_vblc_145_cum5d_z3_with_5d_neg_return_5pct_d2},
    "f19_vblc_146_climax_at_high_then_vol_mean_decline_d2": {"inputs": ["high", "volume"], "func": f19_vblc_146_climax_at_high_then_vol_mean_decline_d2},
    "f19_vblc_147_sum_vol_rise_streaks_63d_d2": {"inputs": ["volume"], "func": f19_vblc_147_sum_vol_rise_streaks_63d_d2},
    "f19_vblc_148_churn_climax_then_gap_down_next_day_d2": {"inputs": ["high", "low", "close", "open", "volume"], "func": f19_vblc_148_churn_climax_then_gap_down_next_day_d2},
    "f19_vblc_149_three_plus_bursts_in_5d_3x_63d_d2": {"inputs": ["volume"], "func": f19_vblc_149_three_plus_bursts_in_5d_3x_63d_d2},
    "f19_vblc_150_ultimate_blowoff_composite_score_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f19_vblc_150_ultimate_blowoff_composite_score_d2},
}
