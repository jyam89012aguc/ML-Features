"""linear_regression_channel d3 features 076-150 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __d3__001_075.py. Each
feature encodes a different concept in the LR-channel theme:
slope / R² / residual / channel-width / band-touch / multi-horizon disagreement /
SNR / rotation / decay / composite topping.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family imports.
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


def _rolling_lr_endpoint(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _f(w):
        valid = ~np.isnan(w)
        nv = int(valid.sum())
        if nv < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        yv = w
        if not valid.all():
            x = x[valid]; yv = w[valid]
        xm = x.mean(); ym = yv.mean()
        den = float(((x - xm) ** 2).sum())
        if den <= 0:
            return np.nan
        b = float(((x - xm) * (yv - ym)).sum() / den)
        a = ym - b * xm
        return float(a + b * (len(w) - 1))
    return s.rolling(n, min_periods=min_periods).apply(_f, raw=True)


def _rolling_resid_std(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _f(w):
        valid = ~np.isnan(w)
        nv = int(valid.sum())
        if nv < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        yv = w
        if not valid.all():
            x = x[valid]; yv = w[valid]
        xm = x.mean(); ym = yv.mean()
        den = float(((x - xm) ** 2).sum())
        if den <= 0:
            return np.nan
        b = float(((x - xm) * (yv - ym)).sum() / den)
        a = ym - b * xm
        r = yv - (a + b * x)
        if r.size < 2:
            return np.nan
        return float(np.std(r, ddof=1))
    return s.rolling(n, min_periods=min_periods).apply(_f, raw=True)


def _rolling_r2(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _f(w):
        valid = ~np.isnan(w)
        nv = int(valid.sum())
        if nv < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        yv = w
        if not valid.all():
            x = x[valid]; yv = w[valid]
        xm = x.mean(); ym = yv.mean()
        tss = float(((yv - ym) ** 2).sum())
        if tss <= 0:
            return np.nan
        den = float(((x - xm) ** 2).sum())
        if den <= 0:
            return np.nan
        b = float(((x - xm) * (yv - ym)).sum() / den)
        a = ym - b * xm
        yhat = a + b * x
        rss = float(((yv - yhat) ** 2).sum())
        return 1.0 - rss / tss
    return s.rolling(n, min_periods=min_periods).apply(_f, raw=True)


def _rolling_resid_skew(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _f(w):
        valid = ~np.isnan(w)
        nv = int(valid.sum())
        if nv < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        yv = w
        if not valid.all():
            x = x[valid]; yv = w[valid]
        xm = x.mean(); ym = yv.mean()
        den = float(((x - xm) ** 2).sum())
        if den <= 0:
            return np.nan
        b = float(((x - xm) * (yv - ym)).sum() / den)
        a = ym - b * xm
        r = yv - (a + b * x)
        if r.size < 5:
            return np.nan
        sd = float(np.std(r, ddof=1))
        if sd <= 0:
            return np.nan
        return float(np.mean(((r - r.mean()) / sd) ** 3))
    return s.rolling(n, min_periods=min_periods).apply(_f, raw=True)


def f18_lrch_076_channel_snr_slope_over_width_21d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    sl = _rolling_slope(lc, 21, min_periods=7)
    w = _rolling_resid_std(lc, 21, min_periods=7)
    out = _safe_div(sl * 21.0, w)
    return out.diff().diff().diff()


def f18_lrch_077_channel_snr_slope_over_width_63d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    sl = _rolling_slope(lc, 63, min_periods=21)
    w = _rolling_resid_std(lc, 63, min_periods=21)
    out = _safe_div(sl * 63.0, w)
    return out.diff().diff().diff()


def f18_lrch_078_channel_snr_slope_over_width_252d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    sl = _rolling_slope(lc, 252, min_periods=84)
    w = _rolling_resid_std(lc, 252, min_periods=84)
    out = _safe_div(sl * 252.0, w)
    return out.diff().diff().diff()


def f18_lrch_079_channel_snr_slope_over_width_504d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    sl = _rolling_slope(lc, 504, min_periods=168)
    w = _rolling_resid_std(lc, 504, min_periods=168)
    out = _safe_div(sl * 504.0, w)
    return out.diff().diff().diff()


def f18_lrch_080_channel_abs_snr_252d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    sl = _rolling_slope(lc, 252, min_periods=84).abs()
    w = _rolling_resid_std(lc, 252, min_periods=84)
    out = _safe_div(sl * 252.0, w)
    return out.diff().diff().diff()


def f18_lrch_081_channel_snr_top_quintile_63d_in_252d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    sl = _rolling_slope(lc, 63, min_periods=21)
    w = _rolling_resid_std(lc, 63, min_periods=21)
    snr = _safe_div(sl * 63.0, w)
    def _rk(arr):
        if np.isnan(arr).all():
            return np.nan
        last = arr[-1]
        if np.isnan(last):
            return np.nan
        v = arr[~np.isnan(arr)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    rk = snr.rolling(252, min_periods=84).apply(_rk, raw=True)
    out = (rk >= 0.8).astype(float).where(rk.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_082_channel_snr_zscore_63d_in_252d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    sl = _rolling_slope(lc, 63, min_periods=21)
    w = _rolling_resid_std(lc, 63, min_periods=21)
    snr = _safe_div(sl * 63.0, w)
    out = _rolling_zscore(snr, 252, min_periods=84)
    return out.diff().diff().diff()


def f18_lrch_083_channel_snr_decay_21d_63d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    sl = _rolling_slope(lc, 63, min_periods=21)
    w = _rolling_resid_std(lc, 63, min_periods=21)
    snr = _safe_div(sl * 63.0, w)
    out = snr - snr.shift(21)
    return out.diff().diff().diff()


def f18_lrch_084_channel_snr_decay_63d_252d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    sl = _rolling_slope(lc, 252, min_periods=84)
    w = _rolling_resid_std(lc, 252, min_periods=84)
    snr = _safe_div(sl * 252.0, w)
    out = snr - snr.shift(63)
    return out.diff().diff().diff()


def f18_lrch_085_channel_snr_sign_change_event_63d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    sl = _rolling_slope(lc, 63, min_periods=21)
    w = _rolling_resid_std(lc, 63, min_periods=21)
    snr = _safe_div(sl * 63.0, w)
    sg = np.sign(snr)
    out = (sg != sg.shift(1)).astype(float).where(snr.notna() & snr.shift(1).notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_086_longest_pos_snr_streak_252d_63d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    sl = _rolling_slope(lc, 63, min_periods=21)
    w = _rolling_resid_std(lc, 63, min_periods=21)
    snr = _safe_div(sl * 63.0, w)
    pos = (snr > 0).astype(float)
    def _ms(arr):
        if arr.size == 0 or np.isnan(arr).all():
            return np.nan
        best = 0; cur = 0
        for v in arr:
            if v > 0.5:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    out = pos.rolling(252, min_periods=84).apply(_ms, raw=True)
    return out.diff().diff().diff()


def f18_lrch_087_channel_snr_norm_by_r2_63d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    sl = _rolling_slope(lc, 63, min_periods=21)
    w = _rolling_resid_std(lc, 63, min_periods=21)
    snr = _safe_div(sl * 63.0, w)
    r2 = _rolling_r2(lc, 63, min_periods=21)
    out = _safe_div(snr, r2.replace(0, np.nan))
    return out.diff().diff().diff()


def f18_lrch_088_channel_slope_tstat_63d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    sl = _rolling_slope(lc, 63, min_periods=21)
    w = _rolling_resid_std(lc, 63, min_periods=21)
    # SE(b) = sigma_resid / sqrt(sum((x-xm)^2)) — approx with n*var(x)
    n = 63.0
    se = w / np.sqrt(n * ((n*n - 1.0) / 12.0))
    out = _safe_div(sl, se)
    return out.diff().diff().diff()


def f18_lrch_089_channel_slope_tstat_252d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    sl = _rolling_slope(lc, 252, min_periods=84)
    w = _rolling_resid_std(lc, 252, min_periods=84)
    n = 252.0
    se = w / np.sqrt(n * ((n*n - 1.0) / 12.0))
    out = _safe_div(sl, se)
    return out.diff().diff().diff()


def f18_lrch_090_snr_sign_disagree_63_vs_252_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    sl63 = _rolling_slope(lc, 63, min_periods=21); w63 = _rolling_resid_std(lc, 63, min_periods=21)
    snr63 = _safe_div(sl63 * 63.0, w63)
    sl252 = _rolling_slope(lc, 252, min_periods=84); w252 = _rolling_resid_std(lc, 252, min_periods=84)
    snr252 = _safe_div(sl252 * 252.0, w252)
    out = (np.sign(snr63) != np.sign(snr252)).astype(float).where(snr63.notna() & snr252.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_091_channel_slope_flip_event_63d_d3(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    sg = np.sign(sl)
    out = (sg != sg.shift(1)).astype(float).where(sl.notna() & sl.shift(1).notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_092_channel_slope_flip_event_252d_d3(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 252, min_periods=84)
    sg = np.sign(sl)
    out = (sg != sg.shift(1)).astype(float).where(sl.notna() & sl.shift(1).notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_093_channel_slope_magnitude_change_21d_63d_d3(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    out = _safe_div(sl - sl.shift(21), sl.shift(21).abs())
    return out.diff().diff().diff()


def f18_lrch_094_bars_since_slope_flip_63d_d3(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    sg = np.sign(sl)
    fl = (sg != sg.shift(1)).fillna(False)
    arr = fl.values
    n = arr.size
    out_arr = np.full(n, np.nan)
    last = -1
    for i in range(n):
        if arr[i] and not np.isnan(sl.values[i]):
            last = i
        if last >= 0:
            out_arr[i] = float(i - last)
    out = pd.Series(out_arr, index=sl.index)
    return out.diff().diff().diff()


def f18_lrch_095_channel_slope_accel_21d_63d_d3(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    out = (sl - sl.shift(21)) / 21.0
    return out.diff().diff().diff()


def f18_lrch_096_channel_slope_accel_63d_252d_d3(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 252, min_periods=84)
    out = (sl - sl.shift(63)) / 63.0
    return out.diff().diff().diff()


def f18_lrch_097_trend_topped_then_rolled_over_63d_d3(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    def _rk(arr):
        if np.isnan(arr).all():
            return np.nan
        last = arr[-1]
        if np.isnan(last):
            return np.nan
        v = arr[~np.isnan(arr)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    rk = sl.rolling(252, min_periods=84).apply(_rk, raw=True)
    top_past = (rk.shift(21) > 0.8).astype(float)
    neg_now = (sl < 0).astype(float)
    out = (top_past * neg_now).where(rk.shift(21).notna() & sl.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_098_slope_accel_extreme_indicator_63d_d3(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    acc = (sl - sl.shift(21)).abs()
    def _rk(arr):
        if np.isnan(arr).all():
            return np.nan
        last = arr[-1]
        if np.isnan(last):
            return np.nan
        v = arr[~np.isnan(arr)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    rk = acc.rolling(252, min_periods=84).apply(_rk, raw=True)
    out = (rk > 0.95).astype(float).where(rk.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_099_cum_slope_flip_count_252d_63d_d3(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    sg = np.sign(sl)
    fl = (sg != sg.shift(1)).astype(float).where(sl.notna() & sl.shift(1).notna(), np.nan)
    out = fl.rolling(252, min_periods=84).sum()
    return out.diff().diff().diff()


def f18_lrch_100_max_slope_change_63d_window_63d_slope_d3(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    out = (sl.rolling(63, min_periods=21).max() - sl.rolling(63, min_periods=21).min())
    return out.diff().diff().diff()


def f18_lrch_101_axis_rotation_above_30deg_63d_d3(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    ang = np.degrees(np.arctan(sl))
    rot = (ang - ang.shift(63)).abs()
    out = (rot > 30.0).astype(float).where(rot.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_102_rotation_15deg_count_252d_63d_d3(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    ang = np.degrees(np.arctan(sl))
    rot = (ang.diff().abs() > 15.0).astype(float).where(ang.notna() & ang.shift(1).notna(), np.nan)
    out = rot.rolling(252, min_periods=84).sum()
    return out.diff().diff().diff()


def f18_lrch_103_slope_below_own_63d_mean_63d_d3(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    m = sl.rolling(63, min_periods=21).mean()
    out = (sl < m).astype(float).where(sl.notna() & m.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_104_slope_of_slope_21d_63d_d3(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    out = _rolling_slope(sl, 21, min_periods=7)
    return out.diff().diff().diff()


def f18_lrch_105_abs_slope_decay_63d_63d_d3(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21).abs()
    out = sl - sl.shift(63)
    return out.diff().diff().diff()


def f18_lrch_106_width_compression_cross_event_63d_d3(close: pd.Series) -> pd.Series:
    w = _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    m = w.rolling(252, min_periods=84).median()
    comp = (w < 0.5 * m).astype(float)
    out = ((comp.shift(1) < 0.5) & (comp > 0.5)).astype(float).where(m.notna() & m.shift(1).notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_107_width_expansion_cross_event_63d_d3(close: pd.Series) -> pd.Series:
    w = _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    m = w.rolling(252, min_periods=84).median()
    exp = (w > 2.0 * m).astype(float)
    out = ((exp.shift(1) < 0.5) & (exp > 0.5)).astype(float).where(m.notna() & m.shift(1).notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_108_current_compressed_width_streak_63d_d3(close: pd.Series) -> pd.Series:
    w = _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    m = w.rolling(252, min_periods=84).median()
    comp = (w < 0.5 * m).astype(int).where(m.notna(), 0)
    block = (comp != comp.shift(1)).fillna(False).cumsum()
    st = comp.groupby(block).cumcount().astype(float)
    out = (st * (comp > 0)).where(m.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_109_current_expanded_width_streak_63d_d3(close: pd.Series) -> pd.Series:
    w = _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    m = w.rolling(252, min_periods=84).median()
    exp_ = (w > 2.0 * m).astype(int).where(m.notna(), 0)
    block = (exp_ != exp_.shift(1)).fillna(False).cumsum()
    st = exp_.groupby(block).cumcount().astype(float)
    out = (st * (exp_ > 0)).where(m.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_110_width_ratio_to_252d_min_63d_d3(close: pd.Series) -> pd.Series:
    w = _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    mn = w.rolling(252, min_periods=84).min()
    out = _safe_div(w, mn)
    return out.diff().diff().diff()


def f18_lrch_111_width_ratio_to_252d_max_63d_d3(close: pd.Series) -> pd.Series:
    w = _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    mx = w.rolling(252, min_periods=84).max()
    out = _safe_div(w, mx)
    return out.diff().diff().diff()


def f18_lrch_112_width_relative_change_21d_63d_d3(close: pd.Series) -> pd.Series:
    w = _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    out = _safe_div(w - w.shift(21), w.shift(21))
    return out.diff().diff().diff()


def f18_lrch_113_width_expand_slope_decline_63d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    w = _rolling_resid_std(lc, 63, min_periods=21)
    sl = _rolling_slope(lc, 63, min_periods=21).abs()
    dw = w - w.shift(21)
    ds = sl - sl.shift(21)
    out = ((dw > 0) & (ds < 0)).astype(float).where(dw.notna() & ds.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_114_width_stability_inv_std_63d_d3(close: pd.Series) -> pd.Series:
    w = _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    sd = w.rolling(63, min_periods=21).std()
    out = 1.0 / sd.replace(0, np.nan)
    return out.diff().diff().diff()


def f18_lrch_115_width_regime_entropy_252d_63d_d3(close: pd.Series) -> pd.Series:
    w = _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    m = w.rolling(252, min_periods=84).median()
    state = np.where(w < 0.5 * m, 0, np.where(w > 2.0 * m, 2, 1))
    state = pd.Series(state, index=w.index).where(m.notna(), np.nan)
    def _ent(arr):
        valid = arr[~np.isnan(arr)]
        if valid.size < 5:
            return np.nan
        p = np.array([(valid == k).sum() / valid.size for k in (0, 1, 2)])
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    out = state.rolling(252, min_periods=84).apply(_ent, raw=True)
    return out.diff().diff().diff()


def f18_lrch_116_mean_width_252d_63d_d3(close: pd.Series) -> pd.Series:
    w = _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    out = w.rolling(252, min_periods=84).mean()
    return out.diff().diff().diff()


def f18_lrch_117_width_vs_atr_ratio_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    w = _rolling_resid_std(close, 63, min_periods=21)
    out = _safe_div(w, _atr(high, low, close, n=21))
    return out.diff().diff().diff()


def f18_lrch_118_width_slope_over_252d_63d_d3(close: pd.Series) -> pd.Series:
    w = _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    out = _rolling_slope(w, 252, min_periods=84)
    return out.diff().diff().diff()


def f18_lrch_119_width_excess_over_realized_vol_63d_d3(close: pd.Series) -> pd.Series:
    w = _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    rv = _safe_log(close).diff().rolling(21, min_periods=7).std() * np.sqrt(63.0)
    out = w - rv
    return out.diff().diff().diff()


def f18_lrch_120_regime_transition_count_252d_63d_d3(close: pd.Series) -> pd.Series:
    w = _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    m = w.rolling(252, min_periods=84).median()
    state = np.where(w < 0.5 * m, 0, np.where(w > 2.0 * m, 2, 1))
    state_s = pd.Series(state, index=w.index).where(m.notna(), np.nan)
    ch = (state_s != state_s.shift(1)).astype(float).where(state_s.notna() & state_s.shift(1).notna(), np.nan)
    out = ch.rolling(252, min_periods=84).sum()
    return out.diff().diff().diff()


def f18_lrch_121_slope_sign_disagree_21_vs_63_d3(close: pd.Series) -> pd.Series:
    s1 = np.sign(_rolling_slope(_safe_log(close), 21, min_periods=7))
    s2 = np.sign(_rolling_slope(_safe_log(close), 63, min_periods=21))
    out = (s1 != s2).astype(float).where(s1.notna() & s2.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_122_slope_sign_disagree_63_vs_252_d3(close: pd.Series) -> pd.Series:
    s1 = np.sign(_rolling_slope(_safe_log(close), 63, min_periods=21))
    s2 = np.sign(_rolling_slope(_safe_log(close), 252, min_periods=84))
    out = (s1 != s2).astype(float).where(s1.notna() & s2.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_123_slope_unanimous_up_21_63_252_d3(close: pd.Series) -> pd.Series:
    s1 = _rolling_slope(_safe_log(close), 21, min_periods=7)
    s2 = _rolling_slope(_safe_log(close), 63, min_periods=21)
    s3 = _rolling_slope(_safe_log(close), 252, min_periods=84)
    out = ((s1 > 0) & (s2 > 0) & (s3 > 0)).astype(float).where(s1.notna() & s2.notna() & s3.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_124_slope_unanimous_down_21_63_252_d3(close: pd.Series) -> pd.Series:
    s1 = _rolling_slope(_safe_log(close), 21, min_periods=7)
    s2 = _rolling_slope(_safe_log(close), 63, min_periods=21)
    s3 = _rolling_slope(_safe_log(close), 252, min_periods=84)
    out = ((s1 < 0) & (s2 < 0) & (s3 < 0)).astype(float).where(s1.notna() & s2.notna() & s3.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_125_abs_slope_ratio_21_over_252_d3(close: pd.Series) -> pd.Series:
    s1 = _rolling_slope(_safe_log(close), 21, min_periods=7).abs()
    s2 = _rolling_slope(_safe_log(close), 252, min_periods=84).abs()
    out = _safe_div(s1, s2)
    return out.diff().diff().diff()


def f18_lrch_126_r2_ratio_63_over_252_d3(close: pd.Series) -> pd.Series:
    r1 = _rolling_r2(_safe_log(close), 63, min_periods=21)
    r2 = _rolling_r2(_safe_log(close), 252, min_periods=84)
    out = _safe_div(r1, r2.replace(0, np.nan))
    return out.diff().diff().diff()


def f18_lrch_127_channel_pos_zscore_63_minus_252_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl1 = _rolling_lr_endpoint(lc, 63, min_periods=21); rs1 = _rolling_resid_std(lc, 63, min_periods=21)
    tl2 = _rolling_lr_endpoint(lc, 252, min_periods=84); rs2 = _rolling_resid_std(lc, 252, min_periods=84)
    p1 = _safe_div(lc - tl1, rs1)
    p2 = _safe_div(lc - tl2, rs2)
    out = p1 - p2
    return out.diff().diff().diff()


def f18_lrch_128_top21d_bottom252d_channel_divergence_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl1 = _rolling_lr_endpoint(lc, 21, min_periods=7); rs1 = _rolling_resid_std(lc, 21, min_periods=7)
    tl2 = _rolling_lr_endpoint(lc, 252, min_periods=84); rs2 = _rolling_resid_std(lc, 252, min_periods=84)
    z1 = _safe_div(lc - tl1, rs1); z2 = _safe_div(lc - tl2, rs2)
    out = ((z1 > 1.0) & (z2 < -1.0)).astype(float).where(z1.notna() & z2.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_129_trendlines_21_vs_252_cross_age_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl1 = _rolling_lr_endpoint(lc, 21, min_periods=7)
    tl2 = _rolling_lr_endpoint(lc, 252, min_periods=84)
    above = (tl1 > tl2).astype(int).where(tl1.notna() & tl2.notna(), 0)
    block = (above != above.shift(1)).fillna(False).cumsum()
    age = above.groupby(block).cumcount().astype(float)
    out = age.where(tl1.notna() & tl2.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_130_slope_agreement_fraction_3horizons_d3(close: pd.Series) -> pd.Series:
    s1 = np.sign(_rolling_slope(_safe_log(close), 21, min_periods=7))
    s2 = np.sign(_rolling_slope(_safe_log(close), 63, min_periods=21))
    s3 = np.sign(_rolling_slope(_safe_log(close), 252, min_periods=84))
    agree = ((s1 == s2).astype(float) + (s2 == s3).astype(float) + (s1 == s3).astype(float)) / 3.0
    out = agree.where(s1.notna() & s2.notna() & s3.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_131_snr_avg_3horizons_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    def _snr(h, mp):
        sl = _rolling_slope(lc, h, min_periods=mp); w = _rolling_resid_std(lc, h, min_periods=mp)
        return _safe_div(sl * float(h), w)
    out = (_snr(21, 7) + _snr(63, 21) + _snr(252, 84)) / 3.0
    return out.diff().diff().diff()


def f18_lrch_132_slope_spread_max_minus_min_3horizons_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    s1 = _rolling_slope(lc, 21, min_periods=7)
    s2 = _rolling_slope(lc, 63, min_periods=21)
    s3 = _rolling_slope(lc, 252, min_periods=84)
    mx = pd.concat([s1.rename(0), s2.rename(1), s3.rename(2)], axis=1).max(axis=1)
    mn = pd.concat([s1.rename(0), s2.rename(1), s3.rename(2)], axis=1).min(axis=1)
    out = mx - mn
    return out.diff().diff().diff()


def f18_lrch_133_short_pos_vs_long_pos_pct_rank_diff_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl1 = _rolling_lr_endpoint(lc, 21, min_periods=7); rs1 = _rolling_resid_std(lc, 21, min_periods=7)
    tl2 = _rolling_lr_endpoint(lc, 252, min_periods=84); rs2 = _rolling_resid_std(lc, 252, min_periods=84)
    p1 = _safe_div(lc - tl1, rs1)
    p2 = _safe_div(lc - tl2, rs2)
    def _rk(arr):
        if np.isnan(arr).all():
            return np.nan
        last = arr[-1]
        if np.isnan(last):
            return np.nan
        v = arr[~np.isnan(arr)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    r1 = p1.rolling(252, min_periods=84).apply(_rk, raw=True)
    r2 = p2.rolling(252, min_periods=84).apply(_rk, raw=True)
    out = r1 - r2
    return out.diff().diff().diff()


def f18_lrch_134_width_63_minus_252_log_d3(close: pd.Series) -> pd.Series:
    w1 = _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    w2 = _rolling_resid_std(_safe_log(close), 252, min_periods=84)
    out = w1 - w2
    return out.diff().diff().diff()


def f18_lrch_135_slope_sign_entropy_3horizons_d3(close: pd.Series) -> pd.Series:
    s1 = np.sign(_rolling_slope(_safe_log(close), 21, min_periods=7))
    s2 = np.sign(_rolling_slope(_safe_log(close), 63, min_periods=21))
    s3 = np.sign(_rolling_slope(_safe_log(close), 252, min_periods=84))
    stack = pd.concat([s1.rename(0), s2.rename(1), s3.rename(2)], axis=1)
    def _e(row):
        a = row.dropna().values
        if a.size < 2:
            return np.nan
        p_pos = (a > 0).sum() / a.size
        p_neg = (a < 0).sum() / a.size
        p_z = (a == 0).sum() / a.size
        p = np.array([p_pos, p_neg, p_z])
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    out = stack.apply(_e, axis=1)
    return out.diff().diff().diff()


def f18_lrch_136_declining_r2_rising_price_63d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    r2 = _rolling_r2(lc, 63, min_periods=21)
    dr2 = r2 - r2.shift(21)
    ret = lc - lc.shift(21)
    out = ((dr2 < 0) & (ret > 0)).astype(float).where(dr2.notna() & ret.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_137_declining_slope_at_upper_band_63d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    sl = _rolling_slope(lc, 63, min_periods=21)
    ds = sl - sl.shift(21)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21); rs = _rolling_resid_std(lc, 63, min_periods=21)
    at_upper = (lc > tl + 1.5 * rs).astype(float)
    out = ((ds < 0) & (at_upper > 0.5)).astype(float).where(ds.notna() & rs.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_138_rotation_then_lower_band_pierce_63d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    sl = _rolling_slope(lc, 63, min_periods=21)
    ang = np.degrees(np.arctan(sl))
    rot = ((ang.shift(21) - ang).abs() > 20.0).astype(float)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21); rs = _rolling_resid_std(lc, 63, min_periods=21)
    lb = tl - 2.0 * rs
    pierce = (lc < lb).astype(float)
    out = (rot * pierce).where(rs.notna() & ang.notna() & ang.shift(21).notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_139_cum_time_upper_decile_channel_252d_63d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    resid = lc - tl
    def _rk(arr):
        if np.isnan(arr).all():
            return np.nan
        last = arr[-1]
        if np.isnan(last):
            return np.nan
        v = arr[~np.isnan(arr)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    rk = resid.rolling(252, min_periods=84).apply(_rk, raw=True)
    top = (rk >= 0.9).astype(float).where(rk.notna(), np.nan)
    out = top.rolling(252, min_periods=84).sum()
    return out.diff().diff().diff()


def f18_lrch_140_hampel_outlier_at_upper_band_252d_63d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    resid = lc - tl
    med = resid.rolling(252, min_periods=84).median()
    mad = (resid - med).abs().rolling(252, min_periods=84).median()
    z = _safe_div(resid - med, 1.4826 * mad)
    out = ((z > 3.0)).astype(float).where(z.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_141_slope_flip_width_compress_21d_63d_d3(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    sg = np.sign(sl)
    fl = (sg != sg.shift(21)).astype(float)
    w = _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    m = w.rolling(252, min_periods=84).median()
    comp = (w < 0.5 * m).astype(float)
    out = (fl * comp).where(sg.notna() & sg.shift(21).notna() & m.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_142_trendline_endpoint_below_63d_mean_63d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    m = tl.rolling(63, min_periods=21).mean()
    out = (tl < m).astype(float).where(tl.notna() & m.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_143_axis_declining_close_above_63d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    dtl = tl - tl.shift(21)
    out = ((dtl < 0) & (lc > tl)).astype(float).where(dtl.notna() & tl.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_144_upper_walk_then_lower_break_63d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21); rs = _rolling_resid_std(lc, 63, min_periods=21)
    ut = (lc >= tl + 2.0 * rs).astype(float).where(rs.notna(), np.nan).rolling(63, min_periods=21).sum()
    lb = tl - 2.0 * rs
    break_e = (lc < lb).astype(float)
    out = ((ut.shift(1) > 5) & (break_e > 0.5)).astype(float).where(ut.shift(1).notna() & rs.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_145_long_term_channel_z_above_2_504d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 504, min_periods=168)
    rs = _rolling_resid_std(lc, 504, min_periods=168)
    z = _safe_div(lc - tl, rs)
    out = (z > 2.0).astype(float).where(z.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_146_spike_then_channel_compress_63d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21); rs = _rolling_resid_std(lc, 63, min_periods=21)
    z = _safe_div(lc - tl, rs)
    spike = (z.shift(21) > 3.0).astype(float)
    w = _rolling_resid_std(lc, 63, min_periods=21)
    m = w.rolling(252, min_periods=84).median()
    comp = (w < 0.5 * m).astype(float)
    out = (spike * comp).where(z.shift(21).notna() & m.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_147_r2_spike_then_fall_21d_63d_d3(close: pd.Series) -> pd.Series:
    r2 = _rolling_r2(_safe_log(close), 63, min_periods=21)
    peak = (r2.shift(21) > 0.8).astype(float)
    fall = ((r2.shift(21) - r2) > 0.3).astype(float)
    out = (peak * fall).where(r2.notna() & r2.shift(21).notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_148_angle_decel_increasing_63d_d3(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    ang = np.degrees(np.arctan(sl))
    dang = ang - ang.shift(21)
    d2ang = dang - dang.shift(21)
    out = ((dang < 0) & (d2ang < 0)).astype(float).where(d2ang.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_149_terminal_channel_composite_63d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21); rs = _rolling_resid_std(lc, 63, min_periods=21)
    resid = lc - tl
    def _rk(arr):
        if np.isnan(arr).all():
            return np.nan
        last = arr[-1]
        if np.isnan(last):
            return np.nan
        v = arr[~np.isnan(arr)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    rk = resid.rolling(63, min_periods=21).apply(_rk, raw=True)
    top = (rk > 0.8).astype(float)
    r2 = _rolling_r2(lc, 63, min_periods=21)
    dr2 = (r2.shift(21) - r2 > 0.1).astype(float)
    w = _rolling_resid_std(lc, 63, min_periods=21)
    dw = (w - w.shift(21) > 0).astype(float)
    out = (top + dr2 + dw).where(rk.notna() & r2.notna() & w.notna(), np.nan)
    return out.diff().diff().diff()


def f18_lrch_150_comp_3sigma_pierce_then_rotation_neg_63d_d3(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21); rs = _rolling_resid_std(lc, 63, min_periods=21)
    pierce = (lc.shift(21) > tl.shift(21) + 3.0 * rs.shift(21)).astype(float)
    sl = _rolling_slope(lc, 63, min_periods=21)
    rot_neg = ((sl < 0) & (sl.shift(21) > 0)).astype(float)
    out = (pierce * rot_neg).where(rs.shift(21).notna() & sl.notna() & sl.shift(21).notna(), np.nan)
    return out.diff().diff().diff()


# ============================================================
#                         REGISTRY 076_150 (d3)
# ============================================================

LINEAR_REGRESSION_CHANNEL_D3_REGISTRY_076_150 = {
    "f18_lrch_076_channel_snr_slope_over_width_21d_d3": {"inputs": ["close"], "func": f18_lrch_076_channel_snr_slope_over_width_21d_d3},
    "f18_lrch_077_channel_snr_slope_over_width_63d_d3": {"inputs": ["close"], "func": f18_lrch_077_channel_snr_slope_over_width_63d_d3},
    "f18_lrch_078_channel_snr_slope_over_width_252d_d3": {"inputs": ["close"], "func": f18_lrch_078_channel_snr_slope_over_width_252d_d3},
    "f18_lrch_079_channel_snr_slope_over_width_504d_d3": {"inputs": ["close"], "func": f18_lrch_079_channel_snr_slope_over_width_504d_d3},
    "f18_lrch_080_channel_abs_snr_252d_d3": {"inputs": ["close"], "func": f18_lrch_080_channel_abs_snr_252d_d3},
    "f18_lrch_081_channel_snr_top_quintile_63d_in_252d_d3": {"inputs": ["close"], "func": f18_lrch_081_channel_snr_top_quintile_63d_in_252d_d3},
    "f18_lrch_082_channel_snr_zscore_63d_in_252d_d3": {"inputs": ["close"], "func": f18_lrch_082_channel_snr_zscore_63d_in_252d_d3},
    "f18_lrch_083_channel_snr_decay_21d_63d_d3": {"inputs": ["close"], "func": f18_lrch_083_channel_snr_decay_21d_63d_d3},
    "f18_lrch_084_channel_snr_decay_63d_252d_d3": {"inputs": ["close"], "func": f18_lrch_084_channel_snr_decay_63d_252d_d3},
    "f18_lrch_085_channel_snr_sign_change_event_63d_d3": {"inputs": ["close"], "func": f18_lrch_085_channel_snr_sign_change_event_63d_d3},
    "f18_lrch_086_longest_pos_snr_streak_252d_63d_d3": {"inputs": ["close"], "func": f18_lrch_086_longest_pos_snr_streak_252d_63d_d3},
    "f18_lrch_087_channel_snr_norm_by_r2_63d_d3": {"inputs": ["close"], "func": f18_lrch_087_channel_snr_norm_by_r2_63d_d3},
    "f18_lrch_088_channel_slope_tstat_63d_d3": {"inputs": ["close"], "func": f18_lrch_088_channel_slope_tstat_63d_d3},
    "f18_lrch_089_channel_slope_tstat_252d_d3": {"inputs": ["close"], "func": f18_lrch_089_channel_slope_tstat_252d_d3},
    "f18_lrch_090_snr_sign_disagree_63_vs_252_d3": {"inputs": ["close"], "func": f18_lrch_090_snr_sign_disagree_63_vs_252_d3},
    "f18_lrch_091_channel_slope_flip_event_63d_d3": {"inputs": ["close"], "func": f18_lrch_091_channel_slope_flip_event_63d_d3},
    "f18_lrch_092_channel_slope_flip_event_252d_d3": {"inputs": ["close"], "func": f18_lrch_092_channel_slope_flip_event_252d_d3},
    "f18_lrch_093_channel_slope_magnitude_change_21d_63d_d3": {"inputs": ["close"], "func": f18_lrch_093_channel_slope_magnitude_change_21d_63d_d3},
    "f18_lrch_094_bars_since_slope_flip_63d_d3": {"inputs": ["close"], "func": f18_lrch_094_bars_since_slope_flip_63d_d3},
    "f18_lrch_095_channel_slope_accel_21d_63d_d3": {"inputs": ["close"], "func": f18_lrch_095_channel_slope_accel_21d_63d_d3},
    "f18_lrch_096_channel_slope_accel_63d_252d_d3": {"inputs": ["close"], "func": f18_lrch_096_channel_slope_accel_63d_252d_d3},
    "f18_lrch_097_trend_topped_then_rolled_over_63d_d3": {"inputs": ["close"], "func": f18_lrch_097_trend_topped_then_rolled_over_63d_d3},
    "f18_lrch_098_slope_accel_extreme_indicator_63d_d3": {"inputs": ["close"], "func": f18_lrch_098_slope_accel_extreme_indicator_63d_d3},
    "f18_lrch_099_cum_slope_flip_count_252d_63d_d3": {"inputs": ["close"], "func": f18_lrch_099_cum_slope_flip_count_252d_63d_d3},
    "f18_lrch_100_max_slope_change_63d_window_63d_slope_d3": {"inputs": ["close"], "func": f18_lrch_100_max_slope_change_63d_window_63d_slope_d3},
    "f18_lrch_101_axis_rotation_above_30deg_63d_d3": {"inputs": ["close"], "func": f18_lrch_101_axis_rotation_above_30deg_63d_d3},
    "f18_lrch_102_rotation_15deg_count_252d_63d_d3": {"inputs": ["close"], "func": f18_lrch_102_rotation_15deg_count_252d_63d_d3},
    "f18_lrch_103_slope_below_own_63d_mean_63d_d3": {"inputs": ["close"], "func": f18_lrch_103_slope_below_own_63d_mean_63d_d3},
    "f18_lrch_104_slope_of_slope_21d_63d_d3": {"inputs": ["close"], "func": f18_lrch_104_slope_of_slope_21d_63d_d3},
    "f18_lrch_105_abs_slope_decay_63d_63d_d3": {"inputs": ["close"], "func": f18_lrch_105_abs_slope_decay_63d_63d_d3},
    "f18_lrch_106_width_compression_cross_event_63d_d3": {"inputs": ["close"], "func": f18_lrch_106_width_compression_cross_event_63d_d3},
    "f18_lrch_107_width_expansion_cross_event_63d_d3": {"inputs": ["close"], "func": f18_lrch_107_width_expansion_cross_event_63d_d3},
    "f18_lrch_108_current_compressed_width_streak_63d_d3": {"inputs": ["close"], "func": f18_lrch_108_current_compressed_width_streak_63d_d3},
    "f18_lrch_109_current_expanded_width_streak_63d_d3": {"inputs": ["close"], "func": f18_lrch_109_current_expanded_width_streak_63d_d3},
    "f18_lrch_110_width_ratio_to_252d_min_63d_d3": {"inputs": ["close"], "func": f18_lrch_110_width_ratio_to_252d_min_63d_d3},
    "f18_lrch_111_width_ratio_to_252d_max_63d_d3": {"inputs": ["close"], "func": f18_lrch_111_width_ratio_to_252d_max_63d_d3},
    "f18_lrch_112_width_relative_change_21d_63d_d3": {"inputs": ["close"], "func": f18_lrch_112_width_relative_change_21d_63d_d3},
    "f18_lrch_113_width_expand_slope_decline_63d_d3": {"inputs": ["close"], "func": f18_lrch_113_width_expand_slope_decline_63d_d3},
    "f18_lrch_114_width_stability_inv_std_63d_d3": {"inputs": ["close"], "func": f18_lrch_114_width_stability_inv_std_63d_d3},
    "f18_lrch_115_width_regime_entropy_252d_63d_d3": {"inputs": ["close"], "func": f18_lrch_115_width_regime_entropy_252d_63d_d3},
    "f18_lrch_116_mean_width_252d_63d_d3": {"inputs": ["close"], "func": f18_lrch_116_mean_width_252d_63d_d3},
    "f18_lrch_117_width_vs_atr_ratio_63d_d3": {"inputs": ["high", "low", "close"], "func": f18_lrch_117_width_vs_atr_ratio_63d_d3},
    "f18_lrch_118_width_slope_over_252d_63d_d3": {"inputs": ["close"], "func": f18_lrch_118_width_slope_over_252d_63d_d3},
    "f18_lrch_119_width_excess_over_realized_vol_63d_d3": {"inputs": ["close"], "func": f18_lrch_119_width_excess_over_realized_vol_63d_d3},
    "f18_lrch_120_regime_transition_count_252d_63d_d3": {"inputs": ["close"], "func": f18_lrch_120_regime_transition_count_252d_63d_d3},
    "f18_lrch_121_slope_sign_disagree_21_vs_63_d3": {"inputs": ["close"], "func": f18_lrch_121_slope_sign_disagree_21_vs_63_d3},
    "f18_lrch_122_slope_sign_disagree_63_vs_252_d3": {"inputs": ["close"], "func": f18_lrch_122_slope_sign_disagree_63_vs_252_d3},
    "f18_lrch_123_slope_unanimous_up_21_63_252_d3": {"inputs": ["close"], "func": f18_lrch_123_slope_unanimous_up_21_63_252_d3},
    "f18_lrch_124_slope_unanimous_down_21_63_252_d3": {"inputs": ["close"], "func": f18_lrch_124_slope_unanimous_down_21_63_252_d3},
    "f18_lrch_125_abs_slope_ratio_21_over_252_d3": {"inputs": ["close"], "func": f18_lrch_125_abs_slope_ratio_21_over_252_d3},
    "f18_lrch_126_r2_ratio_63_over_252_d3": {"inputs": ["close"], "func": f18_lrch_126_r2_ratio_63_over_252_d3},
    "f18_lrch_127_channel_pos_zscore_63_minus_252_d3": {"inputs": ["close"], "func": f18_lrch_127_channel_pos_zscore_63_minus_252_d3},
    "f18_lrch_128_top21d_bottom252d_channel_divergence_d3": {"inputs": ["close"], "func": f18_lrch_128_top21d_bottom252d_channel_divergence_d3},
    "f18_lrch_129_trendlines_21_vs_252_cross_age_d3": {"inputs": ["close"], "func": f18_lrch_129_trendlines_21_vs_252_cross_age_d3},
    "f18_lrch_130_slope_agreement_fraction_3horizons_d3": {"inputs": ["close"], "func": f18_lrch_130_slope_agreement_fraction_3horizons_d3},
    "f18_lrch_131_snr_avg_3horizons_d3": {"inputs": ["close"], "func": f18_lrch_131_snr_avg_3horizons_d3},
    "f18_lrch_132_slope_spread_max_minus_min_3horizons_d3": {"inputs": ["close"], "func": f18_lrch_132_slope_spread_max_minus_min_3horizons_d3},
    "f18_lrch_133_short_pos_vs_long_pos_pct_rank_diff_d3": {"inputs": ["close"], "func": f18_lrch_133_short_pos_vs_long_pos_pct_rank_diff_d3},
    "f18_lrch_134_width_63_minus_252_log_d3": {"inputs": ["close"], "func": f18_lrch_134_width_63_minus_252_log_d3},
    "f18_lrch_135_slope_sign_entropy_3horizons_d3": {"inputs": ["close"], "func": f18_lrch_135_slope_sign_entropy_3horizons_d3},
    "f18_lrch_136_declining_r2_rising_price_63d_d3": {"inputs": ["close"], "func": f18_lrch_136_declining_r2_rising_price_63d_d3},
    "f18_lrch_137_declining_slope_at_upper_band_63d_d3": {"inputs": ["close"], "func": f18_lrch_137_declining_slope_at_upper_band_63d_d3},
    "f18_lrch_138_rotation_then_lower_band_pierce_63d_d3": {"inputs": ["close"], "func": f18_lrch_138_rotation_then_lower_band_pierce_63d_d3},
    "f18_lrch_139_cum_time_upper_decile_channel_252d_63d_d3": {"inputs": ["close"], "func": f18_lrch_139_cum_time_upper_decile_channel_252d_63d_d3},
    "f18_lrch_140_hampel_outlier_at_upper_band_252d_63d_d3": {"inputs": ["close"], "func": f18_lrch_140_hampel_outlier_at_upper_band_252d_63d_d3},
    "f18_lrch_141_slope_flip_width_compress_21d_63d_d3": {"inputs": ["close"], "func": f18_lrch_141_slope_flip_width_compress_21d_63d_d3},
    "f18_lrch_142_trendline_endpoint_below_63d_mean_63d_d3": {"inputs": ["close"], "func": f18_lrch_142_trendline_endpoint_below_63d_mean_63d_d3},
    "f18_lrch_143_axis_declining_close_above_63d_d3": {"inputs": ["close"], "func": f18_lrch_143_axis_declining_close_above_63d_d3},
    "f18_lrch_144_upper_walk_then_lower_break_63d_d3": {"inputs": ["close"], "func": f18_lrch_144_upper_walk_then_lower_break_63d_d3},
    "f18_lrch_145_long_term_channel_z_above_2_504d_d3": {"inputs": ["close"], "func": f18_lrch_145_long_term_channel_z_above_2_504d_d3},
    "f18_lrch_146_spike_then_channel_compress_63d_d3": {"inputs": ["close"], "func": f18_lrch_146_spike_then_channel_compress_63d_d3},
    "f18_lrch_147_r2_spike_then_fall_21d_63d_d3": {"inputs": ["close"], "func": f18_lrch_147_r2_spike_then_fall_21d_63d_d3},
    "f18_lrch_148_angle_decel_increasing_63d_d3": {"inputs": ["close"], "func": f18_lrch_148_angle_decel_increasing_63d_d3},
    "f18_lrch_149_terminal_channel_composite_63d_d3": {"inputs": ["close"], "func": f18_lrch_149_terminal_channel_composite_63d_d3},
    "f18_lrch_150_comp_3sigma_pierce_then_rotation_neg_63d_d3": {"inputs": ["close"], "func": f18_lrch_150_comp_3sigma_pierce_then_rotation_neg_63d_d3},
}
