"""range_estimators_family base features 076-150 — Pipeline 1b-technical.

Continuation of 150 distinct hypotheses (see __base__001_075.py for buckets A-J).
This file covers buckets K (compression), L (wick asymmetry), M (overnight gap
range), N (intraday/overnight var ratio), O (range-of-range vol-of-range),
P (range-jump detection), Q (volume-weighted range), R (cumulative range),
S (range-vs-return divergence), T (true-range / ATR extensions), and additional
bar-shape / range-cross-scale concepts.

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


def _pct_rank(w):
    if np.isnan(w).all():
        return np.nan
    last = w[-1]
    if np.isnan(last):
        return np.nan
    v = w[~np.isnan(w)]
    if v.size == 0:
        return np.nan
    return float((v <= last).sum()) / float(v.size)


# ============================================================
# Bucket K — Range compression detection (076-081)
# ============================================================

def f37_rges_076_count_log_hl_below_20pct_quantile_year_in_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count bars in trailing 21d with log(H/L) below 20th percentile of trailing 252d."""
    lhl = _safe_log(high) - _safe_log(low)
    q20 = lhl.rolling(YDAYS, min_periods=QDAYS).quantile(0.20)
    below = (lhl < q20).astype(float)
    return below.rolling(MDAYS, min_periods=WDAYS).sum()


def f37_rges_077_count_log_hl_below_10pct_quantile_year_in_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count bars in trailing 21d with log(H/L) below 10th percentile of trailing 252d — tight compression."""
    lhl = _safe_log(high) - _safe_log(low)
    q10 = lhl.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    below = (lhl < q10).astype(float)
    return below.rolling(MDAYS, min_periods=WDAYS).sum()


def f37_rges_078_min_log_hl_in_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Smallest single-bar log(H/L) in trailing 21d — narrow-range extreme."""
    lhl = _safe_log(high) - _safe_log(low)
    return lhl.rolling(MDAYS, min_periods=WDAYS).min()


def f37_rges_079_min_log_hl_in_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Smallest single-bar log(H/L) in trailing 63d — quarterly narrow-range extreme."""
    lhl = _safe_log(high) - _safe_log(low)
    return lhl.rolling(QDAYS, min_periods=MDAYS).min()


def f37_rges_080_compression_index_parkinson_21d_over_252d_low(high: pd.Series, low: pd.Series) -> pd.Series:
    """Parkinson 21d variance divided by its trailing 252d MIN — compression = ratio near 1."""
    lhl = _safe_log(high) - _safe_log(low)
    par = (lhl ** 2).rolling(MDAYS, min_periods=WDAYS).mean() / (4.0 * np.log(2.0))
    par_min = par.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_div(par, par_min)


def f37_rges_081_consecutive_narrow_range_5d_streak(high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive-day streak: today's log(H/L) is the smallest in trailing 5d window (NR5 streak)."""
    lhl = _safe_log(high) - _safe_log(low)
    rmin = lhl.rolling(WDAYS, min_periods=2).min()
    is_nr5 = (lhl <= rmin).astype(float).values
    n = len(is_nr5)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if np.isnan(lhl.iat[i]) or np.isnan(rmin.iat[i]):
            streak = 0
            out[i] = np.nan
        else:
            streak = streak + 1 if is_nr5[i] > 0 else 0
            out[i] = float(streak)
    return pd.Series(out, index=high.index)


# ============================================================
# Bucket L — Range truncation / wick asymmetry (082-089)
# Bar-shape asymmetry from upper/lower wick (NOT return-sign asymmetry).
# ============================================================

def f37_rges_082_upper_wick_minus_lower_wick_daily(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Daily (H - max(C,O)) − (min(C,O) − L) — net upper wick magnitude over lower."""
    upper_wick = high - pd.concat([close, open_], axis=1).max(axis=1)
    lower_wick = pd.concat([close, open_], axis=1).min(axis=1) - low
    return upper_wick - lower_wick


def f37_rges_083_wick_asymmetry_ratio_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean upper wick / mean lower wick over 21d — bar-shape asymmetry."""
    upper_wick = high - pd.concat([close, open_], axis=1).max(axis=1)
    lower_wick = pd.concat([close, open_], axis=1).min(axis=1) - low
    u_mean = upper_wick.rolling(MDAYS, min_periods=WDAYS).mean()
    l_mean = lower_wick.rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(u_mean, l_mean)


def f37_rges_084_wick_asymmetry_ratio_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean upper wick / mean lower wick over 63d — quarterly bar-shape asymmetry."""
    upper_wick = high - pd.concat([close, open_], axis=1).max(axis=1)
    lower_wick = pd.concat([close, open_], axis=1).min(axis=1) - low
    u_mean = upper_wick.rolling(QDAYS, min_periods=MDAYS).mean()
    l_mean = lower_wick.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(u_mean, l_mean)


def f37_rges_085_high_minus_close_over_range_daily(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Daily (H-C)/(H-L) — fraction of intraday range above the close (upper wick fraction)."""
    return _safe_div(high - close, high - low)


def f37_rges_086_close_minus_low_over_range_daily(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Daily (C-L)/(H-L) — fraction of intraday range below the close (lower wick fraction)."""
    return _safe_div(close - low, high - low)


def f37_rges_087_mean_high_minus_close_over_range_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (H-C)/(H-L) over 21d — monthly upper-wick fraction regime."""
    return _safe_div(high - close, high - low).rolling(MDAYS, min_periods=WDAYS).mean()


def f37_rges_088_mean_high_minus_close_over_range_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (H-C)/(H-L) over 63d — quarterly upper-wick fraction regime."""
    return _safe_div(high - close, high - low).rolling(QDAYS, min_periods=MDAYS).mean()


def f37_rges_089_wick_asymmetry_log_ratio_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """log( mean_upper_wick / mean_lower_wick ), 252d — annual log-asymmetry of bar shape."""
    upper_wick = high - pd.concat([close, open_], axis=1).max(axis=1)
    lower_wick = pd.concat([close, open_], axis=1).min(axis=1) - low
    u_mean = upper_wick.rolling(YDAYS, min_periods=QDAYS).mean()
    l_mean = lower_wick.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_log(u_mean) - _safe_log(l_mean)


# ============================================================
# Bucket M — Overnight gap range (090-095)
# ============================================================

def f37_rges_090_abs_overnight_gap_log_daily(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Daily |log(O / C_prev)| — absolute overnight gap magnitude."""
    return (_safe_log(open_) - _safe_log(close).shift(1)).abs()


def f37_rges_091_mean_abs_overnight_gap_21d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Mean |overnight log gap| over trailing 21d — monthly gap-volatility magnitude."""
    g = (_safe_log(open_) - _safe_log(close).shift(1)).abs()
    return g.rolling(MDAYS, min_periods=WDAYS).mean()


def f37_rges_092_mean_abs_overnight_gap_63d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Mean |overnight log gap| over trailing 63d — quarterly gap-volatility magnitude."""
    g = (_safe_log(open_) - _safe_log(close).shift(1)).abs()
    return g.rolling(QDAYS, min_periods=MDAYS).mean()


def f37_rges_093_overnight_gap_share_of_total_range_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean |overnight gap| / mean log(H/L) over 21d — overnight share of total bar range."""
    g = (_safe_log(open_) - _safe_log(close).shift(1)).abs()
    lhl = _safe_log(high) - _safe_log(low)
    return _safe_div(g.rolling(MDAYS, min_periods=WDAYS).mean(), lhl.rolling(MDAYS, min_periods=WDAYS).mean())


def f37_rges_094_overnight_gap_share_of_total_range_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean |overnight gap| / mean log(H/L) over 63d — quarterly overnight share."""
    g = (_safe_log(open_) - _safe_log(close).shift(1)).abs()
    lhl = _safe_log(high) - _safe_log(low)
    return _safe_div(g.rolling(QDAYS, min_periods=MDAYS).mean(), lhl.rolling(QDAYS, min_periods=MDAYS).mean())


def f37_rges_095_max_abs_overnight_gap_63d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Max |overnight log gap| in trailing 63d — extreme single overnight gap observed."""
    g = (_safe_log(open_) - _safe_log(close).shift(1)).abs()
    return g.rolling(QDAYS, min_periods=MDAYS).max()


# ============================================================
# Bucket N — Intraday vs overnight variance ratios (096-101)
# ============================================================

def f37_rges_096_intraday_o2c_var_to_overnight_var_21d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Variance of open-to-close / variance of overnight returns over 21d — session balance."""
    o2c = _safe_log(close) - _safe_log(open_)
    ovn = _safe_log(open_) - _safe_log(close).shift(1)
    return _safe_div(o2c.rolling(MDAYS, min_periods=WDAYS).var(), ovn.rolling(MDAYS, min_periods=WDAYS).var())


def f37_rges_097_intraday_o2c_var_to_overnight_var_63d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Variance of open-to-close / variance of overnight returns over 63d — quarterly session balance."""
    o2c = _safe_log(close) - _safe_log(open_)
    ovn = _safe_log(open_) - _safe_log(close).shift(1)
    return _safe_div(o2c.rolling(QDAYS, min_periods=MDAYS).var(), ovn.rolling(QDAYS, min_periods=MDAYS).var())


def f37_rges_098_intraday_range_var_to_overnight_var_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Var(log(H/L)) / Var(overnight gap), 21d — intraday range vol vs gap vol."""
    lhl = _safe_log(high) - _safe_log(low)
    ovn = _safe_log(open_) - _safe_log(close).shift(1)
    return _safe_div(lhl.rolling(MDAYS, min_periods=WDAYS).var(), ovn.rolling(MDAYS, min_periods=WDAYS).var())


def f37_rges_099_overnight_var_share_of_total_var_63d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Var(overnight) / (Var(overnight) + Var(open-to-close)) over 63d — overnight share of session variance."""
    o2c = _safe_log(close) - _safe_log(open_)
    ovn = _safe_log(open_) - _safe_log(close).shift(1)
    vo = ovn.rolling(QDAYS, min_periods=MDAYS).var()
    vc = o2c.rolling(QDAYS, min_periods=MDAYS).var()
    return _safe_div(vo, vo + vc)


def f37_rges_100_overnight_var_share_of_total_var_252d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Overnight share of total session variance over 252d — annual baseline."""
    o2c = _safe_log(close) - _safe_log(open_)
    ovn = _safe_log(open_) - _safe_log(close).shift(1)
    vo = ovn.rolling(YDAYS, min_periods=QDAYS).var()
    vc = o2c.rolling(YDAYS, min_periods=QDAYS).var()
    return _safe_div(vo, vo + vc)


def f37_rges_101_intraday_to_full_day_range_ratio_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean log(H/L) / (mean log(H/L) + mean |overnight gap|) over 63d — intraday share of all-session range."""
    lhl = _safe_log(high) - _safe_log(low)
    g = (_safe_log(open_) - _safe_log(close).shift(1)).abs()
    lh = lhl.rolling(QDAYS, min_periods=MDAYS).mean()
    gg = g.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(lh, lh + gg)


# ============================================================
# Bucket O — Range-of-range / vol-of-range (102-106)
# ============================================================

def f37_rges_102_std_log_hl_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Std-dev of daily log(H/L) over 21d — monthly vol-of-range."""
    lhl = _safe_log(high) - _safe_log(low)
    return lhl.rolling(MDAYS, min_periods=WDAYS).std()


def f37_rges_103_std_log_hl_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Std-dev of daily log(H/L) over 63d — quarterly vol-of-range."""
    lhl = _safe_log(high) - _safe_log(low)
    return lhl.rolling(QDAYS, min_periods=MDAYS).std()


def f37_rges_104_std_log_hl_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Std-dev of daily log(H/L) over 252d — annual vol-of-range baseline."""
    lhl = _safe_log(high) - _safe_log(low)
    return lhl.rolling(YDAYS, min_periods=QDAYS).std()


def f37_rges_105_cv_log_hl_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Coefficient of variation of daily log(H/L) over 63d — std/mean of range."""
    lhl = _safe_log(high) - _safe_log(low)
    m = lhl.rolling(QDAYS, min_periods=MDAYS).mean()
    s = lhl.rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(s, m)


def f37_rges_106_iqr_log_hl_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """IQR (Q75-Q25) of daily log(H/L) over 252d — annual range-distribution spread."""
    lhl = _safe_log(high) - _safe_log(low)
    q75 = lhl.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    q25 = lhl.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return q75 - q25


# ============================================================
# Bucket P — Range jump detection (107-111)
# ============================================================

def f37_rges_107_range_jump_indicator_3x_21d_mean_daily(high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: today's log(H/L) > 3 × trailing-21d mean log(H/L)."""
    lhl = _safe_log(high) - _safe_log(low)
    base = lhl.rolling(MDAYS, min_periods=WDAYS).mean()
    return (lhl > 3.0 * base).astype(float).where(base.notna() & lhl.notna(), np.nan)


def f37_rges_108_count_range_jumps_3x_21d_mean_in_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of range-jump days (log(H/L) > 3 × 21d mean) in trailing 63d."""
    lhl = _safe_log(high) - _safe_log(low)
    base = lhl.rolling(MDAYS, min_periods=WDAYS).mean()
    jump = (lhl > 3.0 * base).astype(float)
    return jump.rolling(QDAYS, min_periods=MDAYS).sum()


def f37_rges_109_count_range_jumps_3x_21d_mean_in_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of range-jump days in trailing 252d — annual jump count."""
    lhl = _safe_log(high) - _safe_log(low)
    base = lhl.rolling(MDAYS, min_periods=WDAYS).mean()
    jump = (lhl > 3.0 * base).astype(float)
    return jump.rolling(YDAYS, min_periods=QDAYS).sum()


def f37_rges_110_bars_since_last_range_jump_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since last range-jump day (log(H/L) > 3 × 21d mean), capped by 252d window."""
    lhl = _safe_log(high) - _safe_log(low)
    base = lhl.rolling(MDAYS, min_periods=WDAYS).mean()
    jump = (lhl > 3.0 * base).astype(float)
    def _bsl(w):
        if np.isnan(w).all():
            return np.nan
        idx = np.where(w > 0)[0]
        if idx.size == 0:
            return float(len(w))
        return float((len(w) - 1) - idx[-1])
    return jump.rolling(YDAYS, min_periods=QDAYS).apply(_bsl, raw=True)


def f37_rges_111_max_range_jump_magnitude_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Max ratio log(H/L) / 21d-mean-log(H/L) observed in trailing 252d — largest jump magnitude."""
    lhl = _safe_log(high) - _safe_log(low)
    base = lhl.rolling(MDAYS, min_periods=WDAYS).mean()
    ratio = _safe_div(lhl, base)
    return ratio.rolling(YDAYS, min_periods=QDAYS).max()


# ============================================================
# Bucket Q — Volume-weighted range (112-117)
# ============================================================

def f37_rges_112_volume_x_log_hl_daily(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Daily volume × log(H/L) — volume-weighted range magnitude."""
    return volume * (_safe_log(high) - _safe_log(low))


def f37_rges_113_log_hl_over_volume_daily(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Daily log(H/L) / volume — range produced per share traded (efficiency of price impact)."""
    return _safe_div(_safe_log(high) - _safe_log(low), volume)


def f37_rges_114_mean_volume_x_log_hl_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean (volume × log(H/L)) over 21d — monthly volume-weighted range regime."""
    return (volume * (_safe_log(high) - _safe_log(low))).rolling(MDAYS, min_periods=WDAYS).mean()


def f37_rges_115_mean_log_hl_over_volume_63d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean (log(H/L) / volume) over 63d — quarterly range-per-volume efficiency."""
    return _safe_div(_safe_log(high) - _safe_log(low), volume).rolling(QDAYS, min_periods=MDAYS).mean()


def f37_rges_116_vol_weighted_parkinson_var_63d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted Parkinson variance over 63d: sum(v_i * log(H/L)²_i) / sum(v_i) / (4 ln 2)."""
    lhl = _safe_log(high) - _safe_log(low)
    num = (volume * lhl ** 2).rolling(QDAYS, min_periods=MDAYS).sum()
    den = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(num, den) / (4.0 * np.log(2.0))


def f37_rges_117_dollar_range_intensity_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean of (close × volume) × log(H/L) over 63d — dollar-weighted range intensity."""
    return (close * volume * (_safe_log(high) - _safe_log(low))).rolling(QDAYS, min_periods=MDAYS).mean()


# ============================================================
# Bucket R — Cumulative range (118-122)
# ============================================================

def f37_rges_118_sum_log_hl_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of daily log(H/L) over 21d — total range traversed in last month."""
    lhl = _safe_log(high) - _safe_log(low)
    return lhl.rolling(MDAYS, min_periods=WDAYS).sum()


def f37_rges_119_sum_log_hl_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of daily log(H/L) over 63d — quarterly cumulative range."""
    lhl = _safe_log(high) - _safe_log(low)
    return lhl.rolling(QDAYS, min_periods=MDAYS).sum()


def f37_rges_120_sum_log_hl_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of daily log(H/L) over 252d — annual cumulative range."""
    lhl = _safe_log(high) - _safe_log(low)
    return lhl.rolling(YDAYS, min_periods=QDAYS).sum()


def f37_rges_121_cum_range_over_log_net_return_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum(log(H/L)) / |sum(log close return)| over 63d — total range divided by net move (path efficiency)."""
    lhl = _safe_log(high) - _safe_log(low)
    ret = _safe_log(close).diff()
    num = lhl.rolling(QDAYS, min_periods=MDAYS).sum()
    den = ret.rolling(QDAYS, min_periods=MDAYS).sum().abs()
    return _safe_div(num, den)


def f37_rges_122_cum_range_over_log_net_return_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum(log(H/L)) / |sum(log close return)| over 252d — annual path efficiency / fractal length."""
    lhl = _safe_log(high) - _safe_log(low)
    ret = _safe_log(close).diff()
    num = lhl.rolling(YDAYS, min_periods=QDAYS).sum()
    den = ret.rolling(YDAYS, min_periods=QDAYS).sum().abs()
    return _safe_div(num, den)


# ============================================================
# Bucket S — Range-vs-return divergence (123-128)
# Parkinson sigma minus realized sigma; flags days/regimes where intraday vol >> close-to-close.
# ============================================================

def f37_rges_123_parkinson_sigma_minus_cc_sigma_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Parkinson sigma − close-to-close sigma over 21d — sign indicates which dominates."""
    lhl = _safe_log(high) - _safe_log(low)
    par_var = (lhl ** 2).rolling(MDAYS, min_periods=WDAYS).mean() / (4.0 * np.log(2.0))
    ret = _safe_log(close).diff()
    cc_var = ret.rolling(MDAYS, min_periods=WDAYS).var()
    return np.sqrt(par_var.clip(lower=0)) - np.sqrt(cc_var.clip(lower=0))


def f37_rges_124_parkinson_sigma_minus_cc_sigma_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Parkinson sigma − close-to-close sigma over 63d."""
    lhl = _safe_log(high) - _safe_log(low)
    par_var = (lhl ** 2).rolling(QDAYS, min_periods=MDAYS).mean() / (4.0 * np.log(2.0))
    ret = _safe_log(close).diff()
    cc_var = ret.rolling(QDAYS, min_periods=MDAYS).var()
    return np.sqrt(par_var.clip(lower=0)) - np.sqrt(cc_var.clip(lower=0))


def f37_rges_125_gk_sigma_minus_cc_sigma_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Garman-Klass sigma − close-to-close sigma over 63d — drift-adjusted range-vol vs RV."""
    lhl = _safe_log(high) - _safe_log(low)
    lco = _safe_log(close) - _safe_log(open_)
    a = 0.5 * (lhl ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    b = (2.0 * np.log(2.0) - 1.0) * (lco ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    gk_var = (a - b).clip(lower=0)
    ret = _safe_log(close).diff()
    cc_var = ret.rolling(QDAYS, min_periods=MDAYS).var()
    return np.sqrt(gk_var) - np.sqrt(cc_var.clip(lower=0))


def f37_rges_126_rs_sigma_minus_cc_sigma_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rogers-Satchell sigma − close-to-close sigma over 63d."""
    lho = _safe_log(high) - _safe_log(open_)
    lhc = _safe_log(high) - _safe_log(close)
    llo = _safe_log(low) - _safe_log(open_)
    llc = _safe_log(low) - _safe_log(close)
    rs_var = (lhc * lho + llc * llo).rolling(QDAYS, min_periods=MDAYS).mean()
    ret = _safe_log(close).diff()
    cc_var = ret.rolling(QDAYS, min_periods=MDAYS).var()
    return np.sqrt(rs_var.clip(lower=0)) - np.sqrt(cc_var.clip(lower=0))


def f37_rges_127_log_parkinson_to_cc_var_ratio_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """log(Parkinson var / CC var), 63d — symmetric log-divergence around equality."""
    lhl = _safe_log(high) - _safe_log(low)
    par_var = (lhl ** 2).rolling(QDAYS, min_periods=MDAYS).mean() / (4.0 * np.log(2.0))
    ret = _safe_log(close).diff()
    cc_var = ret.rolling(QDAYS, min_periods=MDAYS).var()
    return _safe_log(par_var) - _safe_log(cc_var)


def f37_rges_128_yz_sigma_minus_cc_sigma_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Yang-Zhang sigma − close-to-close sigma over 63d — full session vol vs CC."""
    log_open = _safe_log(open_)
    log_close = _safe_log(close)
    log_high = _safe_log(high)
    log_low = _safe_log(low)
    ovn = log_open - log_close.shift(1)
    o2c = log_close - log_open
    lho = log_high - log_open
    lhc = log_high - log_close
    llo = log_low - log_open
    llc = log_low - log_close
    rs_term = lhc * lho + llc * llo
    var_ovn = ovn.rolling(QDAYS, min_periods=MDAYS).var()
    var_o2c = o2c.rolling(QDAYS, min_periods=MDAYS).var()
    var_rs = rs_term.rolling(QDAYS, min_periods=MDAYS).mean()
    n = QDAYS
    k = 0.34 / (1.34 + (n + 1.0) / (n - 1.0))
    yz_var = (var_ovn + k * var_o2c + (1.0 - k) * var_rs).clip(lower=0)
    ret = log_close.diff()
    cc_var = ret.rolling(QDAYS, min_periods=MDAYS).var()
    return np.sqrt(yz_var) - np.sqrt(cc_var.clip(lower=0))


# ============================================================
# Bucket T — True range and ATR-based extensions (129-136)
# ============================================================

def f37_rges_129_atr_21d_over_close(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21 / close — true-range scaled by price (volatility-normalized close measure)."""
    return _safe_div(_atr(high, low, close, n=MDAYS), close)


def f37_rges_130_atr_63d_over_close(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR63 / close — quarterly true-range scaled by price."""
    return _safe_div(_atr(high, low, close, n=QDAYS), close)


def f37_rges_131_atr_252d_over_close(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR252 / close — annual true-range scaled by price (long-horizon vol-as-fraction-of-price)."""
    return _safe_div(_atr(high, low, close, n=YDAYS), close)


def f37_rges_132_atr_21d_over_atr_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21 / ATR252 — fast-vs-slow true-range expansion (volatility-of-volatility regime via ATR)."""
    return _safe_div(_atr(high, low, close, n=MDAYS), _atr(high, low, close, n=YDAYS))


def f37_rges_133_atr_63d_over_atr_504d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR63 / ATR504 — quarterly vs biennial true-range expansion."""
    return _safe_div(_atr(high, low, close, n=QDAYS), _atr(high, low, close, n=DDAYS_2Y))


def f37_rges_134_true_range_pct_rank_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Today's true range percentile rank in trailing 252d distribution."""
    tr = _true_range(high, low, close)
    return tr.rolling(YDAYS, min_periods=QDAYS).apply(_pct_rank, raw=True)


def f37_rges_135_true_range_zscore_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of today's true range vs 252d distribution."""
    tr = _true_range(high, low, close)
    return _rolling_zscore(tr, YDAYS, min_periods=QDAYS)


def f37_rges_136_true_range_vs_log_hl_excess_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean( log(TR / (H-L)) ) over 63d — quantifies how much gaps inflate true range vs intraday range."""
    tr = _true_range(high, low, close)
    hl = high - low
    return (_safe_log(tr) - _safe_log(hl)).rolling(QDAYS, min_periods=MDAYS).mean()


# ============================================================
# Extras — additional bar-shape / range concepts (137-150)
# ============================================================

def f37_rges_137_close_to_open_log_abs_daily(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Daily |log(C/O)| — body-magnitude single-bar measure."""
    return (_safe_log(close) - _safe_log(open_)).abs()


def f37_rges_138_body_to_range_ratio_daily(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """|C-O| / (H-L), daily — body fraction of total intraday range (Marubozu-ness)."""
    return _safe_div((close - open_).abs(), high - low)


def f37_rges_139_mean_body_to_range_ratio_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean |C-O|/(H-L) over 21d — monthly body-fraction regime."""
    return _safe_div((close - open_).abs(), high - low).rolling(MDAYS, min_periods=WDAYS).mean()


def f37_rges_140_mean_body_to_range_ratio_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean |C-O|/(H-L) over 63d — quarterly body-fraction regime."""
    return _safe_div((close - open_).abs(), high - low).rolling(QDAYS, min_periods=MDAYS).mean()


def f37_rges_141_doji_share_in_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Share of bars in 63d where |C-O|/(H-L) < 0.1 — doji density (indecision via bar shape)."""
    ratio = _safe_div((close - open_).abs(), high - low)
    doji = (ratio < 0.1).astype(float)
    return doji.rolling(QDAYS, min_periods=MDAYS).mean()


def f37_rges_142_marubozu_share_in_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Share of bars in 63d where |C-O|/(H-L) > 0.9 — marubozu density (full-body bars)."""
    ratio = _safe_div((close - open_).abs(), high - low)
    maru = (ratio > 0.9).astype(float)
    return maru.rolling(QDAYS, min_periods=MDAYS).mean()


def f37_rges_143_range_vs_prior_close_proxy_log_tr_over_close_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean log(TR/close_prev) over 63d — average gap-aware range normalized by prior close."""
    tr = _true_range(high, low, close)
    pc = close.shift(1)
    return (_safe_log(tr) - _safe_log(pc)).rolling(QDAYS, min_periods=MDAYS).mean()


def f37_rges_144_range_skew_log_hl_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Skew of daily log(H/L) over 63d — third moment of intraday-range distribution."""
    lhl = _safe_log(high) - _safe_log(low)
    return lhl.rolling(QDAYS, min_periods=MDAYS).skew()


def f37_rges_145_range_kurtosis_log_hl_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Kurtosis of daily log(H/L) over 63d — fourth moment of intraday-range distribution."""
    lhl = _safe_log(high) - _safe_log(low)
    return lhl.rolling(QDAYS, min_periods=MDAYS).kurt()


def f37_rges_146_overnight_range_skew_63d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Skew of overnight log gap over 63d — overnight-distribution asymmetry by magnitude."""
    g = (_safe_log(open_) - _safe_log(close).shift(1)).abs()
    return g.rolling(QDAYS, min_periods=MDAYS).skew()


def f37_rges_147_parkinson_slope_21d_in_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Linear-regression slope of 21d Parkinson variance over trailing 63d — range-vol trend."""
    lhl = _safe_log(high) - _safe_log(low)
    par = (lhl ** 2).rolling(MDAYS, min_periods=WDAYS).mean() / (4.0 * np.log(2.0))
    return _rolling_slope(par, QDAYS)


def f37_rges_148_yz_slope_63d_in_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Linear-regression slope of 63d Yang-Zhang variance over trailing 252d — composite vol trend."""
    log_open = _safe_log(open_)
    log_close = _safe_log(close)
    log_high = _safe_log(high)
    log_low = _safe_log(low)
    ovn = log_open - log_close.shift(1)
    o2c = log_close - log_open
    lho = log_high - log_open
    lhc = log_high - log_close
    llo = log_low - log_open
    llc = log_low - log_close
    rs_term = lhc * lho + llc * llo
    var_ovn = ovn.rolling(QDAYS, min_periods=MDAYS).var()
    var_o2c = o2c.rolling(QDAYS, min_periods=MDAYS).var()
    var_rs = rs_term.rolling(QDAYS, min_periods=MDAYS).mean()
    n = QDAYS
    k = 0.34 / (1.34 + (n + 1.0) / (n - 1.0))
    yz = var_ovn + k * var_o2c + (1.0 - k) * var_rs
    return _rolling_slope(yz, YDAYS)


def f37_rges_149_range_autocorr_lag1_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of daily log(H/L) over trailing 63d — range persistence."""
    lhl = _safe_log(high) - _safe_log(low)
    def _ac1(w):
        v = w[~np.isnan(w)]
        if v.size < 5:
            return np.nan
        x = v[:-1] - v[:-1].mean()
        y = v[1:] - v[1:].mean()
        den = np.sqrt((x ** 2).sum() * (y ** 2).sum())
        if den == 0:
            return np.nan
        return float((x * y).sum() / den)
    return lhl.rolling(QDAYS, min_periods=MDAYS).apply(_ac1, raw=True)


def f37_rges_150_range_persistence_252d_minus_21d_pct_rank(high: pd.Series, low: pd.Series) -> pd.Series:
    """Difference: pct-rank of Parkinson 252d vs pct-rank of Parkinson 21d (each in its own 504d cone)
    — long-term range vol cone position minus short-term range vol cone position."""
    lhl = _safe_log(high) - _safe_log(low)
    par21 = (lhl ** 2).rolling(MDAYS, min_periods=WDAYS).mean() / (4.0 * np.log(2.0))
    par252 = (lhl ** 2).rolling(YDAYS, min_periods=QDAYS).mean() / (4.0 * np.log(2.0))
    r21 = par21.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_pct_rank, raw=True)
    r252 = par252.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_pct_rank, raw=True)
    return r252 - r21


# ============================================================
#                         REGISTRY 076-150
# ============================================================

RANGE_ESTIMATORS_FAMILY_BASE_REGISTRY_076_150 = {
    "f37_rges_076_count_log_hl_below_20pct_quantile_year_in_21d": {"inputs": ["high", "low"], "func": f37_rges_076_count_log_hl_below_20pct_quantile_year_in_21d},
    "f37_rges_077_count_log_hl_below_10pct_quantile_year_in_21d": {"inputs": ["high", "low"], "func": f37_rges_077_count_log_hl_below_10pct_quantile_year_in_21d},
    "f37_rges_078_min_log_hl_in_21d": {"inputs": ["high", "low"], "func": f37_rges_078_min_log_hl_in_21d},
    "f37_rges_079_min_log_hl_in_63d": {"inputs": ["high", "low"], "func": f37_rges_079_min_log_hl_in_63d},
    "f37_rges_080_compression_index_parkinson_21d_over_252d_low": {"inputs": ["high", "low"], "func": f37_rges_080_compression_index_parkinson_21d_over_252d_low},
    "f37_rges_081_consecutive_narrow_range_5d_streak": {"inputs": ["high", "low"], "func": f37_rges_081_consecutive_narrow_range_5d_streak},
    "f37_rges_082_upper_wick_minus_lower_wick_daily": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_082_upper_wick_minus_lower_wick_daily},
    "f37_rges_083_wick_asymmetry_ratio_21d": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_083_wick_asymmetry_ratio_21d},
    "f37_rges_084_wick_asymmetry_ratio_63d": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_084_wick_asymmetry_ratio_63d},
    "f37_rges_085_high_minus_close_over_range_daily": {"inputs": ["high", "low", "close"], "func": f37_rges_085_high_minus_close_over_range_daily},
    "f37_rges_086_close_minus_low_over_range_daily": {"inputs": ["high", "low", "close"], "func": f37_rges_086_close_minus_low_over_range_daily},
    "f37_rges_087_mean_high_minus_close_over_range_21d": {"inputs": ["high", "low", "close"], "func": f37_rges_087_mean_high_minus_close_over_range_21d},
    "f37_rges_088_mean_high_minus_close_over_range_63d": {"inputs": ["high", "low", "close"], "func": f37_rges_088_mean_high_minus_close_over_range_63d},
    "f37_rges_089_wick_asymmetry_log_ratio_252d": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_089_wick_asymmetry_log_ratio_252d},
    "f37_rges_090_abs_overnight_gap_log_daily": {"inputs": ["open", "close"], "func": f37_rges_090_abs_overnight_gap_log_daily},
    "f37_rges_091_mean_abs_overnight_gap_21d": {"inputs": ["open", "close"], "func": f37_rges_091_mean_abs_overnight_gap_21d},
    "f37_rges_092_mean_abs_overnight_gap_63d": {"inputs": ["open", "close"], "func": f37_rges_092_mean_abs_overnight_gap_63d},
    "f37_rges_093_overnight_gap_share_of_total_range_21d": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_093_overnight_gap_share_of_total_range_21d},
    "f37_rges_094_overnight_gap_share_of_total_range_63d": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_094_overnight_gap_share_of_total_range_63d},
    "f37_rges_095_max_abs_overnight_gap_63d": {"inputs": ["open", "close"], "func": f37_rges_095_max_abs_overnight_gap_63d},
    "f37_rges_096_intraday_o2c_var_to_overnight_var_21d": {"inputs": ["open", "close"], "func": f37_rges_096_intraday_o2c_var_to_overnight_var_21d},
    "f37_rges_097_intraday_o2c_var_to_overnight_var_63d": {"inputs": ["open", "close"], "func": f37_rges_097_intraday_o2c_var_to_overnight_var_63d},
    "f37_rges_098_intraday_range_var_to_overnight_var_21d": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_098_intraday_range_var_to_overnight_var_21d},
    "f37_rges_099_overnight_var_share_of_total_var_63d": {"inputs": ["open", "close"], "func": f37_rges_099_overnight_var_share_of_total_var_63d},
    "f37_rges_100_overnight_var_share_of_total_var_252d": {"inputs": ["open", "close"], "func": f37_rges_100_overnight_var_share_of_total_var_252d},
    "f37_rges_101_intraday_to_full_day_range_ratio_63d": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_101_intraday_to_full_day_range_ratio_63d},
    "f37_rges_102_std_log_hl_21d": {"inputs": ["high", "low"], "func": f37_rges_102_std_log_hl_21d},
    "f37_rges_103_std_log_hl_63d": {"inputs": ["high", "low"], "func": f37_rges_103_std_log_hl_63d},
    "f37_rges_104_std_log_hl_252d": {"inputs": ["high", "low"], "func": f37_rges_104_std_log_hl_252d},
    "f37_rges_105_cv_log_hl_63d": {"inputs": ["high", "low"], "func": f37_rges_105_cv_log_hl_63d},
    "f37_rges_106_iqr_log_hl_252d": {"inputs": ["high", "low"], "func": f37_rges_106_iqr_log_hl_252d},
    "f37_rges_107_range_jump_indicator_3x_21d_mean_daily": {"inputs": ["high", "low"], "func": f37_rges_107_range_jump_indicator_3x_21d_mean_daily},
    "f37_rges_108_count_range_jumps_3x_21d_mean_in_63d": {"inputs": ["high", "low"], "func": f37_rges_108_count_range_jumps_3x_21d_mean_in_63d},
    "f37_rges_109_count_range_jumps_3x_21d_mean_in_252d": {"inputs": ["high", "low"], "func": f37_rges_109_count_range_jumps_3x_21d_mean_in_252d},
    "f37_rges_110_bars_since_last_range_jump_252d": {"inputs": ["high", "low"], "func": f37_rges_110_bars_since_last_range_jump_252d},
    "f37_rges_111_max_range_jump_magnitude_252d": {"inputs": ["high", "low"], "func": f37_rges_111_max_range_jump_magnitude_252d},
    "f37_rges_112_volume_x_log_hl_daily": {"inputs": ["high", "low", "volume"], "func": f37_rges_112_volume_x_log_hl_daily},
    "f37_rges_113_log_hl_over_volume_daily": {"inputs": ["high", "low", "volume"], "func": f37_rges_113_log_hl_over_volume_daily},
    "f37_rges_114_mean_volume_x_log_hl_21d": {"inputs": ["high", "low", "volume"], "func": f37_rges_114_mean_volume_x_log_hl_21d},
    "f37_rges_115_mean_log_hl_over_volume_63d": {"inputs": ["high", "low", "volume"], "func": f37_rges_115_mean_log_hl_over_volume_63d},
    "f37_rges_116_vol_weighted_parkinson_var_63d": {"inputs": ["high", "low", "volume"], "func": f37_rges_116_vol_weighted_parkinson_var_63d},
    "f37_rges_117_dollar_range_intensity_63d": {"inputs": ["high", "low", "close", "volume"], "func": f37_rges_117_dollar_range_intensity_63d},
    "f37_rges_118_sum_log_hl_21d": {"inputs": ["high", "low"], "func": f37_rges_118_sum_log_hl_21d},
    "f37_rges_119_sum_log_hl_63d": {"inputs": ["high", "low"], "func": f37_rges_119_sum_log_hl_63d},
    "f37_rges_120_sum_log_hl_252d": {"inputs": ["high", "low"], "func": f37_rges_120_sum_log_hl_252d},
    "f37_rges_121_cum_range_over_log_net_return_63d": {"inputs": ["high", "low", "close"], "func": f37_rges_121_cum_range_over_log_net_return_63d},
    "f37_rges_122_cum_range_over_log_net_return_252d": {"inputs": ["high", "low", "close"], "func": f37_rges_122_cum_range_over_log_net_return_252d},
    "f37_rges_123_parkinson_sigma_minus_cc_sigma_21d": {"inputs": ["high", "low", "close"], "func": f37_rges_123_parkinson_sigma_minus_cc_sigma_21d},
    "f37_rges_124_parkinson_sigma_minus_cc_sigma_63d": {"inputs": ["high", "low", "close"], "func": f37_rges_124_parkinson_sigma_minus_cc_sigma_63d},
    "f37_rges_125_gk_sigma_minus_cc_sigma_63d": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_125_gk_sigma_minus_cc_sigma_63d},
    "f37_rges_126_rs_sigma_minus_cc_sigma_63d": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_126_rs_sigma_minus_cc_sigma_63d},
    "f37_rges_127_log_parkinson_to_cc_var_ratio_63d": {"inputs": ["high", "low", "close"], "func": f37_rges_127_log_parkinson_to_cc_var_ratio_63d},
    "f37_rges_128_yz_sigma_minus_cc_sigma_63d": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_128_yz_sigma_minus_cc_sigma_63d},
    "f37_rges_129_atr_21d_over_close": {"inputs": ["high", "low", "close"], "func": f37_rges_129_atr_21d_over_close},
    "f37_rges_130_atr_63d_over_close": {"inputs": ["high", "low", "close"], "func": f37_rges_130_atr_63d_over_close},
    "f37_rges_131_atr_252d_over_close": {"inputs": ["high", "low", "close"], "func": f37_rges_131_atr_252d_over_close},
    "f37_rges_132_atr_21d_over_atr_252d": {"inputs": ["high", "low", "close"], "func": f37_rges_132_atr_21d_over_atr_252d},
    "f37_rges_133_atr_63d_over_atr_504d": {"inputs": ["high", "low", "close"], "func": f37_rges_133_atr_63d_over_atr_504d},
    "f37_rges_134_true_range_pct_rank_in_252d": {"inputs": ["high", "low", "close"], "func": f37_rges_134_true_range_pct_rank_in_252d},
    "f37_rges_135_true_range_zscore_in_252d": {"inputs": ["high", "low", "close"], "func": f37_rges_135_true_range_zscore_in_252d},
    "f37_rges_136_true_range_vs_log_hl_excess_63d": {"inputs": ["high", "low", "close"], "func": f37_rges_136_true_range_vs_log_hl_excess_63d},
    "f37_rges_137_close_to_open_log_abs_daily": {"inputs": ["open", "close"], "func": f37_rges_137_close_to_open_log_abs_daily},
    "f37_rges_138_body_to_range_ratio_daily": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_138_body_to_range_ratio_daily},
    "f37_rges_139_mean_body_to_range_ratio_21d": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_139_mean_body_to_range_ratio_21d},
    "f37_rges_140_mean_body_to_range_ratio_63d": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_140_mean_body_to_range_ratio_63d},
    "f37_rges_141_doji_share_in_63d": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_141_doji_share_in_63d},
    "f37_rges_142_marubozu_share_in_63d": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_142_marubozu_share_in_63d},
    "f37_rges_143_range_vs_prior_close_proxy_log_tr_over_close_63d": {"inputs": ["high", "low", "close"], "func": f37_rges_143_range_vs_prior_close_proxy_log_tr_over_close_63d},
    "f37_rges_144_range_skew_log_hl_63d": {"inputs": ["high", "low"], "func": f37_rges_144_range_skew_log_hl_63d},
    "f37_rges_145_range_kurtosis_log_hl_63d": {"inputs": ["high", "low"], "func": f37_rges_145_range_kurtosis_log_hl_63d},
    "f37_rges_146_overnight_range_skew_63d": {"inputs": ["open", "close"], "func": f37_rges_146_overnight_range_skew_63d},
    "f37_rges_147_parkinson_slope_21d_in_63d": {"inputs": ["high", "low"], "func": f37_rges_147_parkinson_slope_21d_in_63d},
    "f37_rges_148_yz_slope_63d_in_252d": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_148_yz_slope_63d_in_252d},
    "f37_rges_149_range_autocorr_lag1_63d": {"inputs": ["high", "low"], "func": f37_rges_149_range_autocorr_lag1_63d},
    "f37_rges_150_range_persistence_252d_minus_21d_pct_rank": {"inputs": ["high", "low"], "func": f37_rges_150_range_persistence_252d_minus_21d_pct_rank},
}
