"""volume_dryup_at_high d1 features 076-150 — Pipeline 1b-technical.

150 distinct hypotheses across base__001_075 and base__076_150. Each feature
encodes a *different concept* in the volume-dryup-at-high theme: declining
participation while price sits near multi-year extremes — z-score / dispersion /
entropy / regime / compound-state / decay.

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


# ---------------------------- family helpers ----------------------------

def _rolling_pct_rank(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _rk(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    return s.rolling(window, min_periods=min_periods).apply(_rk, raw=True)


def _rolling_quantile(s, window, q, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).quantile(q)


def _consecutive_true_streak(b: pd.Series) -> pd.Series:
    grp = (~b.fillna(False)).cumsum()
    return b.fillna(False).astype(int).groupby(grp).cumsum()


def _rolling_spearman(a, b, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 5)
    def _sp(arr_pair):
        return 0.0  # placeholder unused
    # use pandas rolling on a single combined frame
    ra = a.rolling(window, min_periods=min_periods).rank()
    rb = b.rolling(window, min_periods=min_periods).rank()
    # compute rolling correlation of the rank series within the same window
    return ra.rolling(window, min_periods=min_periods).corr(rb)


def _rolling_corr(a, b, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 5)
    return a.rolling(window, min_periods=min_periods).corr(b)


def _np_autocorr_lag(w, lag):
    v = w[~np.isnan(w)]
    if v.size < lag + 3:
        return np.nan
    a = v[:-lag] - v[:-lag].mean()
    b = v[lag:] - v[lag:].mean()
    den = np.sqrt((a * a).sum() * (b * b).sum())
    if den <= 0:
        return np.nan
    return float((a * b).sum() / den)


def _rolling_gini(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 5)
    def _g(w):
        v = w[~np.isnan(w)]
        if v.size < 5 or np.all(v == 0):
            return np.nan
        v = np.sort(v)
        n = v.size
        idx = np.arange(1, n + 1)
        s = v.sum()
        if s <= 0:
            return np.nan
        return float((2.0 * (idx * v).sum() / s - (n + 1)) / n)
    return s.rolling(window, min_periods=min_periods).apply(_g, raw=True)


def _rolling_hhi_norm(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 5)
    def _h(w):
        v = w[~np.isnan(w)]
        n = v.size
        if n < 5:
            return np.nan
        s = v.sum()
        if s <= 0:
            return np.nan
        p = v / s
        return float((p * p).sum())
    return s.rolling(window, min_periods=min_periods).apply(_h, raw=True)


# ============================================================
# Bucket L — Silent distribution (lower-high vol decay) (076-082)
# ============================================================

def f20_vdah_076_silent_distribution_swing_vol_decay_5_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of volume across the 5 highest closes in trailing 63d (ordered by closing-price rank). Negative = silent distribution."""
    def _sd(idx_window):
        return 0.0
    def _calc(w_close, w_vol):
        return 0.0
    # Vectorize via .apply on rolling DataFrame
    df = pd.concat([close, volume], axis=1)
    df.columns = ["close", "volume"]
    def _f(arr):
        n = arr.shape[0] if arr.ndim > 1 else 0
        return 0.0
    def _per_window(window_idx):
        c = close.iloc[window_idx]
        v = volume.iloc[window_idx]
        cc = c.dropna()
        if cc.size < 10:
            return np.nan
        top_idx = cc.nlargest(5).index
        vv = v.loc[top_idx].dropna()
        if vv.size < 3:
            return np.nan
        x = np.arange(vv.size, dtype=float)
        # order by close descending so x=0 is the highest close
        order = cc.loc[vv.index].sort_values(ascending=False).index
        y = v.loc[order].values
        x = np.arange(y.size, dtype=float)
        xm = x.mean(); ym = y.mean()
        den = ((x - xm) ** 2).sum()
        return float(((x - xm) * (y - ym)).sum() / den) if den > 0 else np.nan
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(QDAYS - 1, n):
        out.iloc[i] = _per_window(range(i - QDAYS + 1, i + 1))
    return (out).diff()


def f20_vdah_077_vol_lower_highs_minus_higher_highs_252d_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean vol on lower-high bars minus mean vol on higher-high bars, both in trailing 252d. Negative = silent distribution."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    new_h = high >= rmax21
    # new local high vs prior local high direction
    prev_max = rmax21.shift(1)
    higher = new_h & (high > prev_max)
    lower = new_h & (high < prev_max)
    vol_h = volume.where(higher, np.nan)
    vol_l = volume.where(lower, np.nan)
    mh = vol_h.rolling(YDAYS, min_periods=QDAYS).mean()
    ml = vol_l.rolling(YDAYS, min_periods=QDAYS).mean()
    return (ml - mh).diff()


def f20_vdah_078_median_vol_at_252d_top10_bars_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Median volume on the trailing-252d top-10-highest-high bars."""
    def _m(idx):
        h_w = high.iloc[idx].dropna()
        if h_w.size < 30:
            return np.nan
        top = h_w.nlargest(10).index
        v = volume.loc[top].dropna()
        return float(v.median()) if v.size > 0 else np.nan
    out = pd.Series(np.nan, index=high.index, dtype=float)
    n = len(high)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _m(range(i - YDAYS + 1, i + 1))
    return (out).diff()


def f20_vdah_079_vol_zscore_on_top10_close_bars_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean log-vol z-score on the trailing-252d top-10-highest-close bars."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    def _m(idx):
        c_w = close.iloc[idx].dropna()
        if c_w.size < 30:
            return np.nan
        top = c_w.nlargest(10).index
        zv = z.loc[top].dropna()
        return float(zv.mean()) if zv.size > 0 else np.nan
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _m(range(i - YDAYS + 1, i + 1))
    return (out).diff()


def f20_vdah_080_regression_slope_vol_against_close_rank_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Regression slope of volume against close-rank (within window) over 252d. Negative = higher closes get less volume."""
    def _r(idx):
        c_w = close.iloc[idx]
        v_w = volume.iloc[idx]
        mask = c_w.notna() & v_w.notna()
        if mask.sum() < 30:
            return np.nan
        c = c_w[mask]; v = v_w[mask].astype(float).values
        x = c.rank().values
        xm = x.mean(); ym = v.mean()
        den = ((x - xm) ** 2).sum()
        return float(((x - xm) * (v - ym)).sum() / den) if den > 0 else np.nan
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _r(range(i - YDAYS + 1, i + 1))
    return (out).diff()


def f20_vdah_081_spearman_close_vol_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Spearman rank correlation between close and volume over trailing 252d. Negative = silent distribution."""
    return (_rolling_spearman(close, volume, YDAYS)).diff()


def f20_vdah_082_pearson_close_vol_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pearson correlation between close and volume over trailing 63d."""
    return (_rolling_corr(close, volume, QDAYS)).diff()


# ============================================================
# Bucket M — Exhaustion gaps with vacuum (083-088)
# ============================================================

def f20_vdah_083_exhaustion_gap_low_vol_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when bar is a gap-up (low > prior_high) AND in top decile of 252d range AND vol below 252d median."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    gap = low > high.shift(1)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((gap & (pos >= 0.90) & (volume < med)).astype(float)).diff()


def f20_vdah_084_count_exhaustion_gaps_low_vol_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d count of exhaustion-gap-low-vol events."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    gap = low > high.shift(1)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = (gap & (pos >= 0.90) & (volume < med)).astype(float)
    return (flag.rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f20_vdah_085_post_exhaustion_gap_vol_decay_21d_mean_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean post-gap 5-bar volume decay ratio over 21d window."""
    gap = (low > high.shift(1)).astype(float)
    next_vol = volume.shift(1)  # cannot — PIT — use rolling on shifted-back instead
    # Reframe: at each bar, compute (volume / volume at most-recent gap in past 21d)
    def _r(idx):
        v_w = volume.iloc[idx]
        g_w = gap.iloc[idx]
        if g_w.sum() == 0:
            return np.nan
        # last gap position
        last_gap = np.where(g_w.values == 1)[0]
        if len(last_gap) == 0:
            return np.nan
        gi = last_gap[-1]
        if gi >= len(v_w) - 1:
            return np.nan
        peak = v_w.iloc[gi]
        post = v_w.iloc[gi + 1 :].dropna()
        if not np.isfinite(peak) or peak <= 0 or post.size == 0:
            return np.nan
        return float(post.mean() / peak)
    out = pd.Series(np.nan, index=volume.index, dtype=float)
    n = len(volume)
    for i in range(MDAYS - 1, n):
        out.iloc[i] = _r(range(i - MDAYS + 1, i + 1))
    return (out).diff()


def f20_vdah_086_gap_up_vol_zscore_252d_mean_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean log-vol z-score on gap-up bars over trailing 252d."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    gap = low > high.shift(1)
    return (z.where(gap, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()).diff()


def f20_vdah_087_ratio_gap_up_vol_to_pre_gap_vol_21d_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Most recent gap-up bar vol divided by mean vol over the prior 5 bars, in trailing 21d window."""
    gap = low > high.shift(1)
    def _r(idx):
        g_w = gap.iloc[idx]
        v_w = volume.iloc[idx]
        gpos = np.where(g_w.values)[0]
        if len(gpos) == 0:
            return np.nan
        gi = gpos[-1]
        if gi < 5:
            return np.nan
        peak = v_w.iloc[gi]
        pre = v_w.iloc[max(0, gi - 5) : gi].dropna()
        if pre.size < 3 or not np.isfinite(peak):
            return np.nan
        base = pre.mean()
        if base <= 0:
            return np.nan
        return float(peak / base)
    out = pd.Series(np.nan, index=volume.index, dtype=float)
    n = len(volume)
    for i in range(MDAYS - 1, n):
        out.iloc[i] = _r(range(i - MDAYS + 1, i + 1))
    return (out).diff()


def f20_vdah_088_post_gap_no_followthrough_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when gap-up bar in past 5 days was followed by close BELOW the gap-bar close on subsequent day."""
    gap_close = close.where(low > high.shift(1), np.nan)
    # forward-fill last gap close into next bars
    last_gap = gap_close.ffill()
    days_since = gap_close.notna().astype(int)
    days_since = (~gap_close.notna()).astype(int).groupby(gap_close.notna().cumsum()).cumsum()
    recent = days_since <= 5
    return (((close < last_gap.shift(1)) & recent).astype(float)).diff()


# ============================================================
# Bucket N — Dwell time in low-vol regime (089-094)
# ============================================================

def f20_vdah_089_dwell_consec_below_med_vol_252d_d1(volume: pd.Series) -> pd.Series:
    """Current consecutive-bar dwell in below-252d-median-vol state, capped at 252d window."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return (_consecutive_true_streak(volume < med).astype(float).clip(upper=float(YDAYS))).diff()


def f20_vdah_090_cum_time_below_med_vol_252d_d1(volume: pd.Series) -> pd.Series:
    """Cumulative count of days below 252d median vol within trailing 252d."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((volume < med).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f20_vdah_091_cum_time_below_q20_vol_252d_d1(volume: pd.Series) -> pd.Series:
    """Cumulative count of days below 20%-quantile of 252d vol within trailing 252d."""
    q = _rolling_quantile(volume, YDAYS, 0.20)
    return ((volume <= q).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f20_vdah_092_dwell_close_top_decile_and_below_med_vol_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current consecutive-bar streak with close in top decile of 252d range AND vol < 252d median."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    cond = (pos >= 0.90) & (volume < med)
    return (_consecutive_true_streak(cond).astype(float)).diff()


def f20_vdah_093_low_vol_regime_persistence_252d_d1(volume: pd.Series) -> pd.Series:
    """Fraction of last 252d in below-252d-median-vol state."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((volume < med).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()).diff()


def f20_vdah_094_longest_low_vol_window_252d_d1(volume: pd.Series) -> pd.Series:
    """Max consecutive below-median streak over trailing 252d."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    streak = _consecutive_true_streak(volume < med).astype(float)
    return (streak.rolling(YDAYS, min_periods=QDAYS).max()).diff()


# ============================================================
# Bucket O — Tail asymmetry near high (095-100)
# ============================================================

def f20_vdah_095_skew_logvol_252d_d1(volume: pd.Series) -> pd.Series:
    """Rolling skewness of log-volume over 252d."""
    return (_safe_log(volume).rolling(YDAYS, min_periods=QDAYS).skew()).diff()


def f20_vdah_096_kurt_logvol_252d_d1(volume: pd.Series) -> pd.Series:
    """Rolling excess kurtosis of log-volume over 252d."""
    return (_safe_log(volume).rolling(YDAYS, min_periods=QDAYS).kurt()).diff()


def f20_vdah_097_skew_logvol_63d_d1(volume: pd.Series) -> pd.Series:
    """Rolling skewness of log-volume over 63d."""
    return (_safe_log(volume).rolling(QDAYS, min_periods=MDAYS).skew()).diff()


def f20_vdah_098_left_tail_mass_logvol_q05_252d_d1(volume: pd.Series) -> pd.Series:
    """Trailing-252d fraction of bars with log-vol below 5%-quantile of trailing 252d."""
    lv = _safe_log(volume)
    q = _rolling_quantile(lv, YDAYS, 0.05)
    return ((lv <= q).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()).diff()


def f20_vdah_099_right_tail_mass_logvol_q95_252d_d1(volume: pd.Series) -> pd.Series:
    """Trailing-252d fraction of bars with log-vol above 95%-quantile of trailing 252d."""
    lv = _safe_log(volume)
    q = _rolling_quantile(lv, YDAYS, 0.95)
    return ((lv >= q).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()).diff()


def f20_vdah_100_tail_balance_index_logvol_252d_d1(volume: pd.Series) -> pd.Series:
    """Left-tail mass (q05) minus right-tail mass (q95) of log-vol over trailing 252d."""
    lv = _safe_log(volume)
    qlo = _rolling_quantile(lv, YDAYS, 0.05)
    qhi = _rolling_quantile(lv, YDAYS, 0.95)
    left = (lv <= qlo).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    right = (lv >= qhi).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    return (left - right).diff()


# ============================================================
# Bucket P — Volume autocorrelation collapse (101-106)
# ============================================================

def f20_vdah_101_autocorr_lag1_logvol_252d_d1(volume: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of log-volume over 252d."""
    return (_safe_log(volume).rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _np_autocorr_lag(w, 1), raw=True)).diff()


def f20_vdah_102_autocorr_lag5_logvol_252d_d1(volume: pd.Series) -> pd.Series:
    """Lag-5 autocorrelation of log-volume over 252d."""
    return (_safe_log(volume).rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _np_autocorr_lag(w, 5), raw=True)).diff()


def f20_vdah_103_ljung_box_proxy_logvol_252d_d1(volume: pd.Series) -> pd.Series:
    """Sum of squared lag-1..5 autocorrelations of log-vol over 252d — Ljung-Box-style serial-dependence proxy."""
    lv = _safe_log(volume)
    def _lb(w):
        out = 0.0
        ok = True
        for lag in range(1, 6):
            a = _np_autocorr_lag(w, lag)
            if np.isnan(a):
                ok = False; break
            out += a * a
        return out if ok else np.nan
    return (lv.rolling(YDAYS, min_periods=QDAYS).apply(_lb, raw=True)).diff()


def f20_vdah_104_acf_decay_logvol_252d_d1(volume: pd.Series) -> pd.Series:
    """Lag-1 minus lag-5 autocorrelation of log-vol over 252d — decay magnitude."""
    lv = _safe_log(volume)
    def _decay(w):
        a1 = _np_autocorr_lag(w, 1)
        a5 = _np_autocorr_lag(w, 5)
        if np.isnan(a1) or np.isnan(a5):
            return np.nan
        return a1 - a5
    return (lv.rolling(YDAYS, min_periods=QDAYS).apply(_decay, raw=True)).diff()


def f20_vdah_105_autocorr_lag1_logvol_63d_d1(volume: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of log-volume over 63d."""
    return (_safe_log(volume).rolling(QDAYS, min_periods=MDAYS).apply(lambda w: _np_autocorr_lag(w, 1), raw=True)).diff()


def f20_vdah_106_autocorr_lag1_change_63_minus_252_d1(volume: pd.Series) -> pd.Series:
    """Lag-1 autocorr(63d) minus lag-1 autocorr(252d) of log-vol — short-vs-long persistence diff."""
    lv = _safe_log(volume)
    a63 = lv.rolling(QDAYS, min_periods=MDAYS).apply(lambda w: _np_autocorr_lag(w, 1), raw=True)
    a252 = lv.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _np_autocorr_lag(w, 1), raw=True)
    return (a63 - a252).diff()


# ============================================================
# Bucket Q — Intraday range thinness compounded with low volume (107-112)
# ============================================================

def f20_vdah_107_close_top_quintile_low_vol_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when (close - low) / (high - low) >= 0.8 AND vol < 252d median, else 0."""
    pos = _safe_div(close - low, high - low)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return (((pos >= 0.8) & (volume < med)).astype(float)).diff()


def f20_vdah_108_count_close_top_quintile_low_vol_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing-63d count of close-in-top-quintile-of-bar-range bars with vol below 252d median."""
    pos = _safe_div(close - low, high - low)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return (((pos >= 0.8) & (volume < med)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f20_vdah_109_frac_close_top_quintile_low_vol_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing-63d fraction of close-in-top-quintile-of-bar-range bars with vol below 252d median."""
    pos = _safe_div(close - low, high - low)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return (((pos >= 0.8) & (volume < med)).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()).diff()


def f20_vdah_110_close_pos_weighted_by_inverse_vol_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean over 63d of close-position-in-bar-range weighted by 1/(volume+epsilon) — strength on no-supply."""
    pos = _safe_div(close - low, high - low)
    iv = _safe_div(pd.Series(1.0, index=volume.index), volume + 1.0)
    num = (pos * iv).rolling(QDAYS, min_periods=MDAYS).sum()
    den = iv.rolling(QDAYS, min_periods=MDAYS).sum()
    return (_safe_div(num, den)).diff()


def f20_vdah_111_dollar_close_strength_low_vol_compound_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - low)/(high - low) * indicator(vol < 252d med), summed over 21d — accumulated strength on no-supply."""
    pos = _safe_div(close - low, high - low)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = (volume < med).astype(float)
    return ((pos * flag).rolling(MDAYS, min_periods=WDAYS).sum()).diff()


def f20_vdah_112_high_close_low_vol_compound_index_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d sum of (close_position_in_range >= 0.9) * (vol < q20_252d) — high-close + low-supply count."""
    pos = _safe_div(close - low, high - low)
    q = _rolling_quantile(volume, YDAYS, 0.20)
    return (((pos >= 0.9) & (volume <= q)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff()


# ============================================================
# Bucket R — Vol decile conditional on price decile (113-118)
# ============================================================

def f20_vdah_113_vol_decile_when_close_in_top1pct_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol percentile rank (252d) on bars when close is in top 1% of trailing 252d closes, mean over 252d."""
    pr_c = _rolling_pct_rank(close, YDAYS)
    pr_v = _rolling_pct_rank(volume, YDAYS)
    return (pr_v.where(pr_c >= 0.99, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()).diff()


def f20_vdah_114_vol_decile_when_close_in_top5pct_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol pct rank on bars when close is in top 5% of trailing 252d closes, mean over 252d."""
    pr_c = _rolling_pct_rank(close, YDAYS)
    pr_v = _rolling_pct_rank(volume, YDAYS)
    return (pr_v.where(pr_c >= 0.95, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()).diff()


def f20_vdah_115_vol_decile_when_close_in_top10pct_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol pct rank on bars when close is in top decile of trailing 252d closes, mean over 252d."""
    pr_c = _rolling_pct_rank(close, YDAYS)
    pr_v = _rolling_pct_rank(volume, YDAYS)
    return (pr_v.where(pr_c >= 0.90, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()).diff()


def f20_vdah_116_median_vol_decile_when_close_top_decile_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Median (not mean) vol pct rank on top-decile-close bars over trailing 252d."""
    pr_c = _rolling_pct_rank(close, YDAYS)
    pr_v = _rolling_pct_rank(volume, YDAYS)
    return (pr_v.where(pr_c >= 0.90, np.nan).rolling(YDAYS, min_periods=QDAYS).median()).diff()


def f20_vdah_117_count_low_vol_decile_when_close_top_decile_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count over 252d of bars where close in top decile AND vol in bottom decile (both pct-ranked vs 252d)."""
    pr_c = _rolling_pct_rank(close, YDAYS)
    pr_v = _rolling_pct_rank(volume, YDAYS)
    return (((pr_c >= 0.90) & (pr_v <= 0.10)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f20_vdah_118_frac_low_vol_decile_when_close_top_decile_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Of top-decile-close bars in trailing 252d, fraction with vol in bottom decile."""
    pr_c = _rolling_pct_rank(close, YDAYS)
    pr_v = _rolling_pct_rank(volume, YDAYS)
    top_c = (pr_c >= 0.90).astype(float)
    low_v_top_c = ((pr_c >= 0.90) & (pr_v <= 0.10)).astype(float)
    return (_safe_div(low_v_top_c.rolling(YDAYS, min_periods=QDAYS).sum(), top_c.rolling(YDAYS, min_periods=QDAYS).sum())).diff()


# ============================================================
# Bucket S — Multi-horizon contrasts (119-124)
# ============================================================

def f20_vdah_119_vol_zscore_21d_minus_252d_d1(volume: pd.Series) -> pd.Series:
    """Log-vol z-score(21d) minus z-score(252d) — recent burst vs long baseline."""
    lv = _safe_log(volume)
    return (_rolling_zscore(lv, MDAYS) - _rolling_zscore(lv, YDAYS)).diff()


def f20_vdah_120_vol_pct_rank_21d_minus_252d_d1(volume: pd.Series) -> pd.Series:
    """Log-vol pct-rank(21d) minus pct-rank(252d) — short-vs-long rank shift."""
    lv = _safe_log(volume)
    return (_rolling_pct_rank(lv, MDAYS) - _rolling_pct_rank(lv, YDAYS)).diff()


def f20_vdah_121_vol_mean_21d_to_252d_ratio_d1(volume: pd.Series) -> pd.Series:
    """Mean vol(21d) divided by mean vol(252d) — short-vs-long regime ratio."""
    m21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    m252 = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(m21, m252)).diff()


def f20_vdah_122_vol_mean_5d_to_63d_ratio_d1(volume: pd.Series) -> pd.Series:
    """Mean vol(5d) divided by mean vol(63d)."""
    m5 = volume.rolling(WDAYS, min_periods=2).mean()
    m63 = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    return (_safe_div(m5, m63)).diff()


def f20_vdah_123_vol_zscore_21d_minus_63d_d1(volume: pd.Series) -> pd.Series:
    """Log-vol z-score(21d) minus z-score(63d)."""
    lv = _safe_log(volume)
    return (_rolling_zscore(lv, MDAYS) - _rolling_zscore(lv, QDAYS)).diff()


def f20_vdah_124_vol_regime_collapse_ratio_long_to_short_d1(volume: pd.Series) -> pd.Series:
    """Mean vol(252d) divided by mean vol(21d) — > 1 = recent regime has shrunk vs long-term."""
    m21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    m252 = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(m252, m21)).diff()


# ============================================================
# Bucket T — Vol-weighted distance to peak (125-130)
# ============================================================

def f20_vdah_125_vol_weighted_dist_from_252d_max_63d_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d volume-weighted mean of (log_high - log_252d_max). Negative when prices are below their peak."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dist = _safe_log(high) - _safe_log(rmax)
    num = (dist * volume).rolling(QDAYS, min_periods=MDAYS).sum()
    den = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    return (_safe_div(num, den)).diff()


def f20_vdah_126_vol_weighted_close_dist_from_252d_high_63d_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d volume-weighted mean of (log_close - log_252d_max)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dist = _safe_log(close) - _safe_log(rmax)
    num = (dist * volume).rolling(QDAYS, min_periods=MDAYS).sum()
    den = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    return (_safe_div(num, den)).diff()


def f20_vdah_127_vol_weighted_close_dist_from_alltime_high_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding-window volume-weighted mean of (log_close - log_expanding_max)."""
    rmax = close.expanding(min_periods=YDAYS).max()
    dist = _safe_log(close) - _safe_log(rmax)
    num = (dist * volume).expanding(min_periods=YDAYS).sum()
    den = volume.expanding(min_periods=YDAYS).sum()
    return (_safe_div(num, den)).diff()


def f20_vdah_128_inverse_vol_weighted_dist_252d_high_63d_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d inverse-volume-weighted mean of (log_close - log_252d_max). Heavier weight on low-vol bars."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dist = _safe_log(close) - _safe_log(rmax)
    iv = _safe_div(pd.Series(1.0, index=volume.index), volume + 1.0)
    num = (dist * iv).rolling(QDAYS, min_periods=MDAYS).sum()
    den = iv.rolling(QDAYS, min_periods=MDAYS).sum()
    return (_safe_div(num, den)).diff()


def f20_vdah_129_dryup_index_compound_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: (top_decile_indicator) * (1 - vol_pct_rank_252d), summed over 252d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    pr_v = _rolling_pct_rank(volume, YDAYS)
    score = (pos >= 0.90).astype(float) * (1.0 - pr_v).clip(lower=0.0)
    return (score.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f20_vdah_130_atr_dist_at_high_with_low_vol_index_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d sum of ATR-normalized distance below 252d high, weighted by below-median-vol indicator."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    dist = _safe_div(close - rmax, atr)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = (volume < med).astype(float)
    return ((dist * flag).rolling(QDAYS, min_periods=MDAYS).sum()).diff()


# ============================================================
# Bucket U — Additional dryup primitives (131-150)
# ============================================================

def f20_vdah_131_zscore_vol_change_252d_d1(volume: pd.Series) -> pd.Series:
    """Z-score (vs 252d) of daily volume change (vol_t - vol_{t-1})."""
    dv = volume.diff()
    return (_rolling_zscore(dv, YDAYS)).diff()


def f20_vdah_132_slope_log_vol_63d_d1(volume: pd.Series) -> pd.Series:
    """Linear-regression slope of log-volume over trailing 63d — quarterly participation trend."""
    return (_rolling_slope(_safe_log(volume), QDAYS)).diff()


def f20_vdah_133_slope_log_vol_252d_d1(volume: pd.Series) -> pd.Series:
    """Linear-regression slope of log-volume over trailing 252d — annual participation trend."""
    return (_rolling_slope(_safe_log(volume), YDAYS)).diff()


def f20_vdah_134_r2_log_vol_trend_252d_d1(volume: pd.Series) -> pd.Series:
    """R² of linear regression of log-volume over 252d (paired with slope_252d, captures trend cleanliness)."""
    lv = _safe_log(volume)
    def _r2(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        x = np.arange(v.size, dtype=float)
        xm = x.mean(); ym = v.mean()
        sxx = ((x - xm) ** 2).sum()
        syy = ((v - ym) ** 2).sum()
        sxy = ((x - xm) * (v - ym)).sum()
        if sxx <= 0 or syy <= 0:
            return np.nan
        r = sxy / np.sqrt(sxx * syy)
        return float(r * r)
    return (lv.rolling(YDAYS, min_periods=QDAYS).apply(_r2, raw=True)).diff()


def f20_vdah_135_cusum_neg_excess_logvol_252d_d1(volume: pd.Series) -> pd.Series:
    """Negative-side CUSUM of (log_vol - rolling 252d median log_vol) — cumulative deficit measure."""
    lv = _safe_log(volume)
    med = lv.rolling(YDAYS, min_periods=QDAYS).median()
    devs = (lv - med).clip(upper=0.0)
    return (devs.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f20_vdah_136_drawdown_from_running_max_logvol_252d_d1(volume: pd.Series) -> pd.Series:
    """Log-volume minus 252d trailing max log-volume (always <= 0)."""
    lv = _safe_log(volume)
    rmax = lv.rolling(YDAYS, min_periods=QDAYS).max()
    return (lv - rmax).diff()


def f20_vdah_137_time_since_logvol_above_p1sigma_252d_d1(volume: pd.Series) -> pd.Series:
    """Bars since last day when log-vol z(vs 252d) > +1 — staleness of the last vol burst."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    flag = (z > 1.0).astype(int)
    grp = flag.cumsum()
    return ((~flag.astype(bool)).astype(int).groupby(grp).cumsum().astype(float)).diff()


def f20_vdah_138_ratio_dryup_to_blowoff_days_252d_d1(volume: pd.Series) -> pd.Series:
    """Ratio of (count z<-1) to (count z>+1) of log-vol over trailing 252d. Higher = more dryup-skewed."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    dry = (z < -1.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    blow = (z > 1.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return (_safe_div(dry, blow + 1.0)).diff()


def f20_vdah_139_median_logvol_when_close_at_252d_max_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Median log-vol on bars where close equals 252d trailing max (at-high bars), over trailing 252d."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    at_high = close >= rmax
    return (_safe_log(volume).where(at_high, np.nan).rolling(YDAYS, min_periods=QDAYS).median()).diff()


def f20_vdah_140_gini_volume_252d_d1(volume: pd.Series) -> pd.Series:
    """Rolling Gini coefficient of raw volume over 252d — concentration of vol across days."""
    return (_rolling_gini(volume, YDAYS)).diff()


def f20_vdah_141_hhi_volume_252d_d1(volume: pd.Series) -> pd.Series:
    """Rolling Herfindahl-Hirschman index of volume shares over 252d."""
    return (_rolling_hhi_norm(volume, YDAYS)).diff()


def f20_vdah_142_max_streak_no_vol_above_median_63d_d1(volume: pd.Series) -> pd.Series:
    """Max consecutive-bar streak with vol < median(63d) in trailing 63d."""
    med = volume.rolling(QDAYS, min_periods=MDAYS).median()
    streak = _consecutive_true_streak(volume < med).astype(float)
    return (streak.rolling(QDAYS, min_periods=MDAYS).max()).diff()


def f20_vdah_143_median_gap_between_top10_vol_bars_252d_d1(volume: pd.Series) -> pd.Series:
    """Median inter-bar gap between the top-10 highest-vol days in trailing 252d (large = vol concentrated rarely)."""
    def _g(idx):
        v_w = volume.iloc[idx].dropna()
        if v_w.size < 20:
            return np.nan
        top = v_w.nlargest(10).index
        pos = sorted([volume.index.get_loc(i) for i in top])
        gaps = np.diff(pos)
        return float(np.median(gaps)) if gaps.size > 0 else np.nan
    out = pd.Series(np.nan, index=volume.index, dtype=float)
    n = len(volume)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _g(range(i - YDAYS + 1, i + 1))
    return (out).diff()


def f20_vdah_144_count_zero_vol_bars_252d_d1(volume: pd.Series) -> pd.Series:
    """Count of zero-volume bars in trailing 252d (extreme thinning)."""
    return ((volume <= 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f20_vdah_145_top10_vol_share_252d_d1(volume: pd.Series) -> pd.Series:
    """Sum of the top-10 vol days divided by total vol over trailing 252d — concentration share."""
    def _s(w):
        v = w[~np.isnan(w)]
        if v.size < 20:
            return np.nan
        s = v.sum()
        if s <= 0:
            return np.nan
        top = np.sort(v)[-10:]
        return float(top.sum() / s)
    return (volume.rolling(YDAYS, min_periods=QDAYS).apply(_s, raw=True)).diff()


def f20_vdah_146_close_pos_inverse_vol_weighted_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Inverse-vol weighted mean close-position in bar-range over trailing 21d."""
    pos = _safe_div(close - low, high - low)
    iv = _safe_div(pd.Series(1.0, index=volume.index), volume + 1.0)
    num = (pos * iv).rolling(MDAYS, min_periods=WDAYS).sum()
    den = iv.rolling(MDAYS, min_periods=WDAYS).sum()
    return (_safe_div(num, den)).diff()


def f20_vdah_147_log_vol_zscore_diff_5d_minus_252d_d1(volume: pd.Series) -> pd.Series:
    """Log-vol z-score(5d) minus z-score(252d) — very-short burst vs long baseline."""
    lv = _safe_log(volume)
    return (_rolling_zscore(lv, WDAYS) - _rolling_zscore(lv, YDAYS)).diff()


def f20_vdah_148_kurt_logvol_63d_d1(volume: pd.Series) -> pd.Series:
    """Rolling excess kurtosis of log-vol over 63d — tail-heaviness in short window."""
    return (_safe_log(volume).rolling(QDAYS, min_periods=MDAYS).kurt()).diff()


def f20_vdah_149_vol_smashed_ratio_21d_to_5y_d1(volume: pd.Series) -> pd.Series:
    """Mean vol(21d) divided by mean vol(5y) — multi-year regime collapse ratio."""
    m21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    m5y = volume.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    return (_safe_div(m21, m5y)).diff()


def f20_vdah_150_composite_dryup_score_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite score = sum of [vol_pct_rank_252d<0.25, vol<med252, close_pos_in_252d_range>0.9, vol_z_252d<-1] (each as 0/1)."""
    pr_v = _rolling_pct_rank(volume, YDAYS)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    score = ((pr_v < 0.25).astype(float)
             + (volume < med).astype(float)
             + (pos >= 0.90).astype(float)
             + (z < -1.0).astype(float))
    return (score).diff()


# ============================================================
#                         REGISTRY 076-150
# ============================================================

VOLUME_DRYUP_AT_HIGH_D1_REGISTRY_076_150 = {
    "f20_vdah_076_silent_distribution_swing_vol_decay_5_d1": {"inputs": ["close", "volume"], "func": f20_vdah_076_silent_distribution_swing_vol_decay_5_d1},
    "f20_vdah_077_vol_lower_highs_minus_higher_highs_252d_d1": {"inputs": ["high", "volume"], "func": f20_vdah_077_vol_lower_highs_minus_higher_highs_252d_d1},
    "f20_vdah_078_median_vol_at_252d_top10_bars_d1": {"inputs": ["high", "volume"], "func": f20_vdah_078_median_vol_at_252d_top10_bars_d1},
    "f20_vdah_079_vol_zscore_on_top10_close_bars_252d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_079_vol_zscore_on_top10_close_bars_252d_d1},
    "f20_vdah_080_regression_slope_vol_against_close_rank_252d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_080_regression_slope_vol_against_close_rank_252d_d1},
    "f20_vdah_081_spearman_close_vol_252d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_081_spearman_close_vol_252d_d1},
    "f20_vdah_082_pearson_close_vol_63d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_082_pearson_close_vol_63d_d1},
    "f20_vdah_083_exhaustion_gap_low_vol_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_083_exhaustion_gap_low_vol_indicator_d1},
    "f20_vdah_084_count_exhaustion_gaps_low_vol_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_084_count_exhaustion_gaps_low_vol_63d_d1},
    "f20_vdah_085_post_exhaustion_gap_vol_decay_21d_mean_d1": {"inputs": ["high", "low", "volume"], "func": f20_vdah_085_post_exhaustion_gap_vol_decay_21d_mean_d1},
    "f20_vdah_086_gap_up_vol_zscore_252d_mean_d1": {"inputs": ["high", "low", "volume"], "func": f20_vdah_086_gap_up_vol_zscore_252d_mean_d1},
    "f20_vdah_087_ratio_gap_up_vol_to_pre_gap_vol_21d_d1": {"inputs": ["high", "low", "volume"], "func": f20_vdah_087_ratio_gap_up_vol_to_pre_gap_vol_21d_d1},
    "f20_vdah_088_post_gap_no_followthrough_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_088_post_gap_no_followthrough_indicator_d1},
    "f20_vdah_089_dwell_consec_below_med_vol_252d_d1": {"inputs": ["volume"], "func": f20_vdah_089_dwell_consec_below_med_vol_252d_d1},
    "f20_vdah_090_cum_time_below_med_vol_252d_d1": {"inputs": ["volume"], "func": f20_vdah_090_cum_time_below_med_vol_252d_d1},
    "f20_vdah_091_cum_time_below_q20_vol_252d_d1": {"inputs": ["volume"], "func": f20_vdah_091_cum_time_below_q20_vol_252d_d1},
    "f20_vdah_092_dwell_close_top_decile_and_below_med_vol_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_092_dwell_close_top_decile_and_below_med_vol_d1},
    "f20_vdah_093_low_vol_regime_persistence_252d_d1": {"inputs": ["volume"], "func": f20_vdah_093_low_vol_regime_persistence_252d_d1},
    "f20_vdah_094_longest_low_vol_window_252d_d1": {"inputs": ["volume"], "func": f20_vdah_094_longest_low_vol_window_252d_d1},
    "f20_vdah_095_skew_logvol_252d_d1": {"inputs": ["volume"], "func": f20_vdah_095_skew_logvol_252d_d1},
    "f20_vdah_096_kurt_logvol_252d_d1": {"inputs": ["volume"], "func": f20_vdah_096_kurt_logvol_252d_d1},
    "f20_vdah_097_skew_logvol_63d_d1": {"inputs": ["volume"], "func": f20_vdah_097_skew_logvol_63d_d1},
    "f20_vdah_098_left_tail_mass_logvol_q05_252d_d1": {"inputs": ["volume"], "func": f20_vdah_098_left_tail_mass_logvol_q05_252d_d1},
    "f20_vdah_099_right_tail_mass_logvol_q95_252d_d1": {"inputs": ["volume"], "func": f20_vdah_099_right_tail_mass_logvol_q95_252d_d1},
    "f20_vdah_100_tail_balance_index_logvol_252d_d1": {"inputs": ["volume"], "func": f20_vdah_100_tail_balance_index_logvol_252d_d1},
    "f20_vdah_101_autocorr_lag1_logvol_252d_d1": {"inputs": ["volume"], "func": f20_vdah_101_autocorr_lag1_logvol_252d_d1},
    "f20_vdah_102_autocorr_lag5_logvol_252d_d1": {"inputs": ["volume"], "func": f20_vdah_102_autocorr_lag5_logvol_252d_d1},
    "f20_vdah_103_ljung_box_proxy_logvol_252d_d1": {"inputs": ["volume"], "func": f20_vdah_103_ljung_box_proxy_logvol_252d_d1},
    "f20_vdah_104_acf_decay_logvol_252d_d1": {"inputs": ["volume"], "func": f20_vdah_104_acf_decay_logvol_252d_d1},
    "f20_vdah_105_autocorr_lag1_logvol_63d_d1": {"inputs": ["volume"], "func": f20_vdah_105_autocorr_lag1_logvol_63d_d1},
    "f20_vdah_106_autocorr_lag1_change_63_minus_252_d1": {"inputs": ["volume"], "func": f20_vdah_106_autocorr_lag1_change_63_minus_252_d1},
    "f20_vdah_107_close_top_quintile_low_vol_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_107_close_top_quintile_low_vol_indicator_d1},
    "f20_vdah_108_count_close_top_quintile_low_vol_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_108_count_close_top_quintile_low_vol_63d_d1},
    "f20_vdah_109_frac_close_top_quintile_low_vol_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_109_frac_close_top_quintile_low_vol_63d_d1},
    "f20_vdah_110_close_pos_weighted_by_inverse_vol_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_110_close_pos_weighted_by_inverse_vol_63d_d1},
    "f20_vdah_111_dollar_close_strength_low_vol_compound_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_111_dollar_close_strength_low_vol_compound_d1},
    "f20_vdah_112_high_close_low_vol_compound_index_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_112_high_close_low_vol_compound_index_252d_d1},
    "f20_vdah_113_vol_decile_when_close_in_top1pct_252d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_113_vol_decile_when_close_in_top1pct_252d_d1},
    "f20_vdah_114_vol_decile_when_close_in_top5pct_252d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_114_vol_decile_when_close_in_top5pct_252d_d1},
    "f20_vdah_115_vol_decile_when_close_in_top10pct_252d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_115_vol_decile_when_close_in_top10pct_252d_d1},
    "f20_vdah_116_median_vol_decile_when_close_top_decile_252d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_116_median_vol_decile_when_close_top_decile_252d_d1},
    "f20_vdah_117_count_low_vol_decile_when_close_top_decile_252d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_117_count_low_vol_decile_when_close_top_decile_252d_d1},
    "f20_vdah_118_frac_low_vol_decile_when_close_top_decile_252d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_118_frac_low_vol_decile_when_close_top_decile_252d_d1},
    "f20_vdah_119_vol_zscore_21d_minus_252d_d1": {"inputs": ["volume"], "func": f20_vdah_119_vol_zscore_21d_minus_252d_d1},
    "f20_vdah_120_vol_pct_rank_21d_minus_252d_d1": {"inputs": ["volume"], "func": f20_vdah_120_vol_pct_rank_21d_minus_252d_d1},
    "f20_vdah_121_vol_mean_21d_to_252d_ratio_d1": {"inputs": ["volume"], "func": f20_vdah_121_vol_mean_21d_to_252d_ratio_d1},
    "f20_vdah_122_vol_mean_5d_to_63d_ratio_d1": {"inputs": ["volume"], "func": f20_vdah_122_vol_mean_5d_to_63d_ratio_d1},
    "f20_vdah_123_vol_zscore_21d_minus_63d_d1": {"inputs": ["volume"], "func": f20_vdah_123_vol_zscore_21d_minus_63d_d1},
    "f20_vdah_124_vol_regime_collapse_ratio_long_to_short_d1": {"inputs": ["volume"], "func": f20_vdah_124_vol_regime_collapse_ratio_long_to_short_d1},
    "f20_vdah_125_vol_weighted_dist_from_252d_max_63d_d1": {"inputs": ["high", "close", "volume"], "func": f20_vdah_125_vol_weighted_dist_from_252d_max_63d_d1},
    "f20_vdah_126_vol_weighted_close_dist_from_252d_high_63d_d1": {"inputs": ["high", "close", "volume"], "func": f20_vdah_126_vol_weighted_close_dist_from_252d_high_63d_d1},
    "f20_vdah_127_vol_weighted_close_dist_from_alltime_high_d1": {"inputs": ["close", "volume"], "func": f20_vdah_127_vol_weighted_close_dist_from_alltime_high_d1},
    "f20_vdah_128_inverse_vol_weighted_dist_252d_high_63d_d1": {"inputs": ["high", "close", "volume"], "func": f20_vdah_128_inverse_vol_weighted_dist_252d_high_63d_d1},
    "f20_vdah_129_dryup_index_compound_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_129_dryup_index_compound_252d_d1},
    "f20_vdah_130_atr_dist_at_high_with_low_vol_index_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_130_atr_dist_at_high_with_low_vol_index_63d_d1},
    "f20_vdah_131_zscore_vol_change_252d_d1": {"inputs": ["volume"], "func": f20_vdah_131_zscore_vol_change_252d_d1},
    "f20_vdah_132_slope_log_vol_63d_d1": {"inputs": ["volume"], "func": f20_vdah_132_slope_log_vol_63d_d1},
    "f20_vdah_133_slope_log_vol_252d_d1": {"inputs": ["volume"], "func": f20_vdah_133_slope_log_vol_252d_d1},
    "f20_vdah_134_r2_log_vol_trend_252d_d1": {"inputs": ["volume"], "func": f20_vdah_134_r2_log_vol_trend_252d_d1},
    "f20_vdah_135_cusum_neg_excess_logvol_252d_d1": {"inputs": ["volume"], "func": f20_vdah_135_cusum_neg_excess_logvol_252d_d1},
    "f20_vdah_136_drawdown_from_running_max_logvol_252d_d1": {"inputs": ["volume"], "func": f20_vdah_136_drawdown_from_running_max_logvol_252d_d1},
    "f20_vdah_137_time_since_logvol_above_p1sigma_252d_d1": {"inputs": ["volume"], "func": f20_vdah_137_time_since_logvol_above_p1sigma_252d_d1},
    "f20_vdah_138_ratio_dryup_to_blowoff_days_252d_d1": {"inputs": ["volume"], "func": f20_vdah_138_ratio_dryup_to_blowoff_days_252d_d1},
    "f20_vdah_139_median_logvol_when_close_at_252d_max_d1": {"inputs": ["high", "close", "volume"], "func": f20_vdah_139_median_logvol_when_close_at_252d_max_d1},
    "f20_vdah_140_gini_volume_252d_d1": {"inputs": ["volume"], "func": f20_vdah_140_gini_volume_252d_d1},
    "f20_vdah_141_hhi_volume_252d_d1": {"inputs": ["volume"], "func": f20_vdah_141_hhi_volume_252d_d1},
    "f20_vdah_142_max_streak_no_vol_above_median_63d_d1": {"inputs": ["volume"], "func": f20_vdah_142_max_streak_no_vol_above_median_63d_d1},
    "f20_vdah_143_median_gap_between_top10_vol_bars_252d_d1": {"inputs": ["volume"], "func": f20_vdah_143_median_gap_between_top10_vol_bars_252d_d1},
    "f20_vdah_144_count_zero_vol_bars_252d_d1": {"inputs": ["volume"], "func": f20_vdah_144_count_zero_vol_bars_252d_d1},
    "f20_vdah_145_top10_vol_share_252d_d1": {"inputs": ["volume"], "func": f20_vdah_145_top10_vol_share_252d_d1},
    "f20_vdah_146_close_pos_inverse_vol_weighted_21d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_146_close_pos_inverse_vol_weighted_21d_d1},
    "f20_vdah_147_log_vol_zscore_diff_5d_minus_252d_d1": {"inputs": ["volume"], "func": f20_vdah_147_log_vol_zscore_diff_5d_minus_252d_d1},
    "f20_vdah_148_kurt_logvol_63d_d1": {"inputs": ["volume"], "func": f20_vdah_148_kurt_logvol_63d_d1},
    "f20_vdah_149_vol_smashed_ratio_21d_to_5y_d1": {"inputs": ["volume"], "func": f20_vdah_149_vol_smashed_ratio_21d_to_5y_d1},
    "f20_vdah_150_composite_dryup_score_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_150_composite_dryup_score_252d_d1},
}
