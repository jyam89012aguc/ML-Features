"""options_skew_at_peak d3 features 001_075 — 3rd-derivative wrappers.

Each function inlines the corresponding base body and appends .diff().diff().diff() so the output is the third bar-over-bar derivative of the base signal. Helpers, constants, and PIT discipline are identical to the matching __base__001_075.py."""
import numpy as np
import pandas as pd
YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5

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

def _rolling_rank_pct(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)

    def _r(w):
        if np.isnan(w).any():
            return np.nan
        return (np.searchsorted(np.sort(w), w[-1], side='right') - 0.5) / len(w)
    return s.rolling(window, min_periods=min_periods).apply(_r, raw=True)

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

def _days_since_max(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)

    def _f(w):
        if np.isnan(w).all():
            return np.nan
        return float(len(w) - 1 - int(np.nanargmax(w)))
    return s.rolling(window, min_periods=min_periods).apply(_f, raw=True)

def _days_since_min(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)

    def _f(w):
        if np.isnan(w).all():
            return np.nan
        return float(len(w) - 1 - int(np.nanargmin(w)))
    return s.rolling(window, min_periods=min_periods).apply(_f, raw=True)

def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(span // 3, 2)).mean()

def f17_oskp_001_atm_iv_30d_zscore_252d_d3(atm_iv_30d: pd.Series) -> pd.Series:
    return _rolling_zscore(atm_iv_30d, YDAYS).diff().diff().diff()

def f17_oskp_002_atm_iv_30d_zscore_63d_d3(atm_iv_30d: pd.Series) -> pd.Series:
    return _rolling_zscore(atm_iv_30d, QDAYS).diff().diff().diff()

def f17_oskp_003_atm_iv_30d_rank_pct_252d_d3(atm_iv_30d: pd.Series) -> pd.Series:
    return _rolling_rank_pct(atm_iv_30d, YDAYS).diff().diff().diff()

def f17_oskp_004_atm_iv_30d_rank_pct_63d_d3(atm_iv_30d: pd.Series) -> pd.Series:
    return _rolling_rank_pct(atm_iv_30d, QDAYS).diff().diff().diff()

def f17_oskp_005_atm_iv_60d_zscore_252d_d3(atm_iv_60d: pd.Series) -> pd.Series:
    return _rolling_zscore(atm_iv_60d, YDAYS).diff().diff().diff()

def f17_oskp_006_atm_iv_60d_rank_pct_252d_d3(atm_iv_60d: pd.Series) -> pd.Series:
    return _rolling_rank_pct(atm_iv_60d, YDAYS).diff().diff().diff()

def f17_oskp_007_atm_iv_90d_zscore_252d_d3(atm_iv_90d: pd.Series) -> pd.Series:
    return _rolling_zscore(atm_iv_90d, YDAYS).diff().diff().diff()

def f17_oskp_008_atm_iv_30d_log_distance_to_252d_max_d3(atm_iv_30d: pd.Series) -> pd.Series:
    mx = atm_iv_30d.rolling(YDAYS, min_periods=QDAYS).max()
    return (_safe_log(atm_iv_30d) - _safe_log(mx)).diff().diff().diff()

def f17_oskp_009_days_since_atm_iv_30d_max_252d_d3(atm_iv_30d: pd.Series) -> pd.Series:
    return _days_since_max(atm_iv_30d, YDAYS).diff().diff().diff()

def f17_oskp_010_days_since_atm_iv_30d_min_252d_d3(atm_iv_30d: pd.Series) -> pd.Series:
    return _days_since_min(atm_iv_30d, YDAYS).diff().diff().diff()

def f17_oskp_011_atm_iv_30d_vs_yearly_median_ratio_d3(atm_iv_30d: pd.Series) -> pd.Series:
    med = atm_iv_30d.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(atm_iv_30d, med).diff().diff().diff()

def f17_oskp_012_atm_iv_30d_above_p95_count_63d_d3(atm_iv_30d: pd.Series) -> pd.Series:
    thr = atm_iv_30d.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    flag = (atm_iv_30d >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f17_oskp_013_atm_iv_30d_above_p99_count_252d_d3(atm_iv_30d: pd.Series) -> pd.Series:
    thr = atm_iv_30d.rolling(YDAYS, min_periods=QDAYS).quantile(0.99)
    flag = (atm_iv_30d >= thr).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f17_oskp_014_atm_iv_30d_min_max_range_normalized_63d_d3(atm_iv_30d: pd.Series) -> pd.Series:
    mx = atm_iv_30d.rolling(QDAYS, min_periods=MDAYS).max()
    mn = atm_iv_30d.rolling(QDAYS, min_periods=MDAYS).min()
    m = atm_iv_30d.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(mx - mn, m).diff().diff().diff()

def f17_oskp_015_atm_iv_30d_kurtosis_63d_d3(atm_iv_30d: pd.Series) -> pd.Series:

    def _k(w):
        if np.isnan(w).any():
            return np.nan
        sd = w.std()
        if sd == 0:
            return np.nan
        return float(((w - w.mean()) ** 4).mean() / sd ** 4 - 3.0)
    return atm_iv_30d.rolling(QDAYS, min_periods=MDAYS).apply(_k, raw=True).diff().diff().diff()

def f17_oskp_016_atm_iv_30d_skewness_63d_d3(atm_iv_30d: pd.Series) -> pd.Series:

    def _sk(w):
        if np.isnan(w).any():
            return np.nan
        sd = w.std()
        if sd == 0:
            return np.nan
        return float(((w - w.mean()) ** 3).mean() / sd ** 3)
    return atm_iv_30d.rolling(QDAYS, min_periods=MDAYS).apply(_sk, raw=True).diff().diff().diff()

def f17_oskp_017_atm_iv_30d_pct_above_long_mean_63d_d3(atm_iv_30d: pd.Series) -> pd.Series:
    m252 = atm_iv_30d.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (atm_iv_30d > m252).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff().diff()

def f17_oskp_018_atm_iv_30d_recency_break_above_2sigma_63d_d3(atm_iv_30d: pd.Series) -> pd.Series:
    m = atm_iv_30d.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = atm_iv_30d.rolling(YDAYS, min_periods=QDAYS).std()
    flag = (atm_iv_30d > m + 2.0 * sd).astype(float)

    def _r(w):
        if np.isnan(w).all():
            return np.nan
        nz = np.where(w > 0)[0]
        if len(nz) == 0:
            return float(len(w))
        return float(len(w) - 1 - nz[-1])
    return flag.rolling(YDAYS, min_periods=QDAYS).apply(_r, raw=True).diff().diff().diff()

def f17_oskp_019_atm_iv_30d_streak_above_p75_252d_d3(atm_iv_30d: pd.Series) -> pd.Series:
    thr = atm_iv_30d.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    flag = (atm_iv_30d > thr).astype(int)

    def _streak(w):
        if np.isnan(w).any():
            return np.nan
        n = 0
        for v in w[::-1]:
            if v > 0:
                n += 1
            else:
                break
        return float(n)
    return flag.rolling(QDAYS, min_periods=WDAYS).apply(_streak, raw=True).diff().diff().diff()

def f17_oskp_020_atm_iv_30d_ema5_to_ema63_d3(atm_iv_30d: pd.Series) -> pd.Series:
    return _safe_div(_ema(atm_iv_30d, WDAYS), _ema(atm_iv_30d, QDAYS)).diff().diff().diff()

def f17_oskp_021_iv_term_slope_30_60_level_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    return (atm_iv_60d - atm_iv_30d).diff().diff().diff()

def f17_oskp_022_iv_term_slope_30_60_zscore_252d_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    slope = atm_iv_60d - atm_iv_30d
    return _rolling_zscore(slope, YDAYS).diff().diff().diff()

def f17_oskp_023_iv_term_slope_30_60_rank_pct_252d_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    slope = atm_iv_60d - atm_iv_30d
    return _rolling_rank_pct(slope, YDAYS).diff().diff().diff()

def f17_oskp_024_iv_term_slope_30_60_inversion_recency_252d_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    slope = atm_iv_60d - atm_iv_30d
    flag = (slope < 0).astype(float)

    def _r(w):
        if np.isnan(w).all():
            return np.nan
        nz = np.where(w > 0)[0]
        if len(nz) == 0:
            return float(len(w))
        return float(len(w) - 1 - nz[-1])
    return flag.rolling(YDAYS, min_periods=QDAYS).apply(_r, raw=True).diff().diff().diff()

def f17_oskp_025_iv_term_slope_60_90_level_d3(atm_iv_60d: pd.Series, atm_iv_90d: pd.Series) -> pd.Series:
    return (atm_iv_90d - atm_iv_60d).diff().diff().diff()

def f17_oskp_026_iv_term_slope_60_90_zscore_252d_d3(atm_iv_60d: pd.Series, atm_iv_90d: pd.Series) -> pd.Series:
    slope = atm_iv_90d - atm_iv_60d
    return _rolling_zscore(slope, YDAYS).diff().diff().diff()

def f17_oskp_027_iv_term_curvature_30_60_90_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series, atm_iv_90d: pd.Series) -> pd.Series:
    return (atm_iv_90d - 2.0 * atm_iv_60d + atm_iv_30d).diff().diff().diff()

def f17_oskp_028_iv_term_curvature_zscore_252d_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series, atm_iv_90d: pd.Series) -> pd.Series:
    c = atm_iv_90d - 2.0 * atm_iv_60d + atm_iv_30d
    return _rolling_zscore(c, YDAYS).diff().diff().diff()

def f17_oskp_029_iv_term_flatness_count_63d_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    rel = (atm_iv_60d - atm_iv_30d).abs() / atm_iv_30d.replace(0, np.nan)
    flag = (rel < 0.05).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f17_oskp_030_iv_term_inversion_count_63d_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    flag = (atm_iv_30d > atm_iv_60d).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f17_oskp_031_iv_term_inversion_count_21d_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    flag = (atm_iv_30d > atm_iv_60d).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f17_oskp_032_iv_term_inversion_intensity_63d_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    inv = (atm_iv_30d - atm_iv_60d).clip(lower=0)
    return inv.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff().diff()

def f17_oskp_033_iv_term_slope_change_21d_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    slope = atm_iv_60d - atm_iv_30d
    return slope.diff(MDAYS).diff().diff().diff()

def f17_oskp_034_iv_term_slope_change_63d_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    slope = atm_iv_60d - atm_iv_30d
    return slope.diff(QDAYS).diff().diff().diff()

def f17_oskp_035_iv_term_30_60_log_ratio_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    return (_safe_log(atm_iv_60d) - _safe_log(atm_iv_30d)).diff().diff().diff()

def f17_oskp_036_iv_skew_30d_level_d3(iv_skew_30d: pd.Series) -> pd.Series:
    return iv_skew_30d.astype(float).diff().diff().diff()

def f17_oskp_037_iv_skew_30d_zscore_252d_d3(iv_skew_30d: pd.Series) -> pd.Series:
    return _rolling_zscore(iv_skew_30d, YDAYS).diff().diff().diff()

def f17_oskp_038_iv_skew_30d_rank_pct_252d_d3(iv_skew_30d: pd.Series) -> pd.Series:
    return _rolling_rank_pct(iv_skew_30d, YDAYS).diff().diff().diff()

def f17_oskp_039_iv_skew_30d_above_p95_count_63d_d3(iv_skew_30d: pd.Series) -> pd.Series:
    thr = iv_skew_30d.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    flag = (iv_skew_30d >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f17_oskp_040_iv_skew_30d_streak_above_long_mean_d3(iv_skew_30d: pd.Series) -> pd.Series:
    m = iv_skew_30d.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (iv_skew_30d > m).astype(int)

    def _streak(w):
        if np.isnan(w).any():
            return np.nan
        n = 0
        for v in w[::-1]:
            if v > 0:
                n += 1
            else:
                break
        return float(n)
    return flag.rolling(QDAYS, min_periods=WDAYS).apply(_streak, raw=True).diff().diff().diff()

def f17_oskp_041_iv_skew_60d_level_d3(iv_skew_60d: pd.Series) -> pd.Series:
    return iv_skew_60d.astype(float).diff().diff().diff()

def f17_oskp_042_iv_skew_60d_zscore_252d_d3(iv_skew_60d: pd.Series) -> pd.Series:
    return _rolling_zscore(iv_skew_60d, YDAYS).diff().diff().diff()

def f17_oskp_043_iv_skew_60d_rank_pct_252d_d3(iv_skew_60d: pd.Series) -> pd.Series:
    return _rolling_rank_pct(iv_skew_60d, YDAYS).diff().diff().diff()

def f17_oskp_044_skew_term_30_60_diff_d3(iv_skew_30d: pd.Series, iv_skew_60d: pd.Series) -> pd.Series:
    return (iv_skew_60d - iv_skew_30d).diff().diff().diff()

def f17_oskp_045_put_minus_call_iv_30d_abs_d3(put_iv_30d: pd.Series, call_iv_30d: pd.Series) -> pd.Series:
    return (put_iv_30d - call_iv_30d).diff().diff().diff()

def f17_oskp_046_put_minus_call_iv_30d_zscore_252d_d3(put_iv_30d: pd.Series, call_iv_30d: pd.Series) -> pd.Series:
    return _rolling_zscore(put_iv_30d - call_iv_30d, YDAYS).diff().diff().diff()

def f17_oskp_047_put_minus_call_iv_60d_abs_d3(put_iv_60d: pd.Series, call_iv_60d: pd.Series) -> pd.Series:
    return (put_iv_60d - call_iv_60d).diff().diff().diff()

def f17_oskp_048_put_call_iv_ratio_30d_d3(put_iv_30d: pd.Series, call_iv_30d: pd.Series) -> pd.Series:
    return _safe_div(put_iv_30d, call_iv_30d).diff().diff().diff()

def f17_oskp_049_put_call_iv_ratio_zscore_252d_d3(put_iv_30d: pd.Series, call_iv_30d: pd.Series) -> pd.Series:
    r = _safe_div(put_iv_30d, call_iv_30d)
    return _rolling_zscore(r, YDAYS).diff().diff().diff()

def f17_oskp_050_skew_steepening_21d_d3(iv_skew_30d: pd.Series) -> pd.Series:
    return iv_skew_30d.diff(MDAYS).diff().diff().diff()

def f17_oskp_051_skew_steepening_63d_d3(iv_skew_30d: pd.Series) -> pd.Series:
    return iv_skew_30d.diff(QDAYS).diff().diff().diff()

def f17_oskp_052_skew_flattening_streak_d3(iv_skew_30d: pd.Series) -> pd.Series:
    d = iv_skew_30d.diff()
    flag = (d < 0).astype(int)

    def _streak(w):
        if np.isnan(w).any():
            return np.nan
        n = 0
        for v in w[::-1]:
            if v > 0:
                n += 1
            else:
                break
        return float(n)
    return flag.rolling(QDAYS, min_periods=WDAYS).apply(_streak, raw=True).diff().diff().diff()

def f17_oskp_053_days_since_skew_minimum_252d_d3(iv_skew_30d: pd.Series) -> pd.Series:
    return _days_since_min(iv_skew_30d, YDAYS).diff().diff().diff()

def f17_oskp_054_skew_below_p5_count_63d_d3(iv_skew_30d: pd.Series) -> pd.Series:
    thr = iv_skew_30d.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    flag = (iv_skew_30d <= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f17_oskp_055_skew_complacency_composite_63d_d3(iv_skew_30d: pd.Series, atm_iv_30d: pd.Series) -> pd.Series:
    sk_r = _rolling_rank_pct(iv_skew_30d, YDAYS)
    iv_r = _rolling_rank_pct(atm_iv_30d, YDAYS)
    score = (1.0 - sk_r) * (1.0 - iv_r)
    return score.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff().diff()

def f17_oskp_056_iv_realized_spread_30d_d3(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    return (atm_iv_30d - iv_realized_30d).diff().diff().diff()

def f17_oskp_057_iv_realized_spread_zscore_252d_d3(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    vrp = atm_iv_30d - iv_realized_30d
    return _rolling_zscore(vrp, YDAYS).diff().diff().diff()

def f17_oskp_058_iv_realized_ratio_30d_d3(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    return _safe_div(atm_iv_30d, iv_realized_30d).diff().diff().diff()

def f17_oskp_059_iv_realized_ratio_zscore_252d_d3(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    r = _safe_div(atm_iv_30d, iv_realized_30d)
    return _rolling_zscore(r, YDAYS).diff().diff().diff()

def f17_oskp_060_iv_minus_realized_count_above_5pct_63d_d3(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    flag = (atm_iv_30d - iv_realized_30d > 0.05).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f17_oskp_061_iv_realized_log_diff_30d_d3(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    return (_safe_log(atm_iv_30d) - _safe_log(iv_realized_30d)).diff().diff().diff()

def f17_oskp_062_iv_realized_ratio_max_63d_d3(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    r = _safe_div(atm_iv_30d, iv_realized_30d)
    return r.rolling(QDAYS, min_periods=MDAYS).max().diff().diff().diff()

def f17_oskp_063_iv_realized_ratio_min_63d_d3(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    r = _safe_div(atm_iv_30d, iv_realized_30d)
    return r.rolling(QDAYS, min_periods=MDAYS).min().diff().diff().diff()

def f17_oskp_064_iv_realized_spread_kurtosis_63d_d3(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    vrp = atm_iv_30d - iv_realized_30d

    def _k(w):
        if np.isnan(w).any():
            return np.nan
        sd = w.std()
        if sd == 0:
            return np.nan
        return float(((w - w.mean()) ** 4).mean() / sd ** 4 - 3.0)
    return vrp.rolling(QDAYS, min_periods=MDAYS).apply(_k, raw=True).diff().diff().diff()

def f17_oskp_065_iv_realized_ratio_rank_pct_252d_d3(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    r = _safe_div(atm_iv_30d, iv_realized_30d)
    return _rolling_rank_pct(r, YDAYS).diff().diff().diff()

def f17_oskp_066_vrp_premium_compression_streak_d3(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    flag = (atm_iv_30d - iv_realized_30d < 0).astype(int)

    def _streak(w):
        if np.isnan(w).any():
            return np.nan
        n = 0
        for v in w[::-1]:
            if v > 0:
                n += 1
            else:
                break
        return float(n)
    return flag.rolling(QDAYS, min_periods=WDAYS).apply(_streak, raw=True).diff().diff().diff()

def f17_oskp_067_vrp_squeeze_under_p5_count_63d_d3(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    vrp = atm_iv_30d - iv_realized_30d
    thr = vrp.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    flag = (vrp <= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f17_oskp_068_vrp_zscore_change_21d_d3(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    vrp = atm_iv_30d - iv_realized_30d
    z = _rolling_zscore(vrp, YDAYS)
    return z.diff(MDAYS).diff().diff().diff()

def f17_oskp_069_vrp_log_diff_21d_d3(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    return (_safe_log(atm_iv_30d) - _safe_log(iv_realized_30d)).diff(MDAYS).diff().diff().diff()

def f17_oskp_070_vrp_log_diff_63d_d3(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    return (_safe_log(atm_iv_30d) - _safe_log(iv_realized_30d)).diff(QDAYS).diff().diff().diff()

def f17_oskp_071_put_call_volume_ratio_level_d3(put_volume: pd.Series, call_volume: pd.Series) -> pd.Series:
    return _safe_div(put_volume, call_volume).diff().diff().diff()

def f17_oskp_072_put_call_volume_ratio_zscore_252d_d3(put_volume: pd.Series, call_volume: pd.Series) -> pd.Series:
    r = _safe_div(put_volume, call_volume)
    return _rolling_zscore(r, YDAYS).diff().diff().diff()

def f17_oskp_073_put_call_volume_ratio_rank_pct_63d_d3(put_volume: pd.Series, call_volume: pd.Series) -> pd.Series:
    r = _safe_div(put_volume, call_volume)
    return _rolling_rank_pct(r, QDAYS).diff().diff().diff()

def f17_oskp_074_call_volume_zscore_252d_d3(call_volume: pd.Series) -> pd.Series:
    return _rolling_zscore(call_volume, YDAYS).diff().diff().diff()

def f17_oskp_075_call_volume_log_diff_5d_d3(call_volume: pd.Series) -> pd.Series:
    return _safe_log(call_volume).diff(WDAYS).diff().diff().diff()
OPTIONS_SKEW_AT_PEAK_D3_REGISTRY_001_075 = {'f17_oskp_001_atm_iv_30d_zscore_252d_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_001_atm_iv_30d_zscore_252d_d3}, 'f17_oskp_002_atm_iv_30d_zscore_63d_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_002_atm_iv_30d_zscore_63d_d3}, 'f17_oskp_003_atm_iv_30d_rank_pct_252d_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_003_atm_iv_30d_rank_pct_252d_d3}, 'f17_oskp_004_atm_iv_30d_rank_pct_63d_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_004_atm_iv_30d_rank_pct_63d_d3}, 'f17_oskp_005_atm_iv_60d_zscore_252d_d3': {'inputs': ['atm_iv_60d'], 'func': f17_oskp_005_atm_iv_60d_zscore_252d_d3}, 'f17_oskp_006_atm_iv_60d_rank_pct_252d_d3': {'inputs': ['atm_iv_60d'], 'func': f17_oskp_006_atm_iv_60d_rank_pct_252d_d3}, 'f17_oskp_007_atm_iv_90d_zscore_252d_d3': {'inputs': ['atm_iv_90d'], 'func': f17_oskp_007_atm_iv_90d_zscore_252d_d3}, 'f17_oskp_008_atm_iv_30d_log_distance_to_252d_max_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_008_atm_iv_30d_log_distance_to_252d_max_d3}, 'f17_oskp_009_days_since_atm_iv_30d_max_252d_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_009_days_since_atm_iv_30d_max_252d_d3}, 'f17_oskp_010_days_since_atm_iv_30d_min_252d_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_010_days_since_atm_iv_30d_min_252d_d3}, 'f17_oskp_011_atm_iv_30d_vs_yearly_median_ratio_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_011_atm_iv_30d_vs_yearly_median_ratio_d3}, 'f17_oskp_012_atm_iv_30d_above_p95_count_63d_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_012_atm_iv_30d_above_p95_count_63d_d3}, 'f17_oskp_013_atm_iv_30d_above_p99_count_252d_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_013_atm_iv_30d_above_p99_count_252d_d3}, 'f17_oskp_014_atm_iv_30d_min_max_range_normalized_63d_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_014_atm_iv_30d_min_max_range_normalized_63d_d3}, 'f17_oskp_015_atm_iv_30d_kurtosis_63d_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_015_atm_iv_30d_kurtosis_63d_d3}, 'f17_oskp_016_atm_iv_30d_skewness_63d_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_016_atm_iv_30d_skewness_63d_d3}, 'f17_oskp_017_atm_iv_30d_pct_above_long_mean_63d_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_017_atm_iv_30d_pct_above_long_mean_63d_d3}, 'f17_oskp_018_atm_iv_30d_recency_break_above_2sigma_63d_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_018_atm_iv_30d_recency_break_above_2sigma_63d_d3}, 'f17_oskp_019_atm_iv_30d_streak_above_p75_252d_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_019_atm_iv_30d_streak_above_p75_252d_d3}, 'f17_oskp_020_atm_iv_30d_ema5_to_ema63_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_020_atm_iv_30d_ema5_to_ema63_d3}, 'f17_oskp_021_iv_term_slope_30_60_level_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d'], 'func': f17_oskp_021_iv_term_slope_30_60_level_d3}, 'f17_oskp_022_iv_term_slope_30_60_zscore_252d_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d'], 'func': f17_oskp_022_iv_term_slope_30_60_zscore_252d_d3}, 'f17_oskp_023_iv_term_slope_30_60_rank_pct_252d_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d'], 'func': f17_oskp_023_iv_term_slope_30_60_rank_pct_252d_d3}, 'f17_oskp_024_iv_term_slope_30_60_inversion_recency_252d_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d'], 'func': f17_oskp_024_iv_term_slope_30_60_inversion_recency_252d_d3}, 'f17_oskp_025_iv_term_slope_60_90_level_d3': {'inputs': ['atm_iv_60d', 'atm_iv_90d'], 'func': f17_oskp_025_iv_term_slope_60_90_level_d3}, 'f17_oskp_026_iv_term_slope_60_90_zscore_252d_d3': {'inputs': ['atm_iv_60d', 'atm_iv_90d'], 'func': f17_oskp_026_iv_term_slope_60_90_zscore_252d_d3}, 'f17_oskp_027_iv_term_curvature_30_60_90_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d', 'atm_iv_90d'], 'func': f17_oskp_027_iv_term_curvature_30_60_90_d3}, 'f17_oskp_028_iv_term_curvature_zscore_252d_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d', 'atm_iv_90d'], 'func': f17_oskp_028_iv_term_curvature_zscore_252d_d3}, 'f17_oskp_029_iv_term_flatness_count_63d_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d'], 'func': f17_oskp_029_iv_term_flatness_count_63d_d3}, 'f17_oskp_030_iv_term_inversion_count_63d_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d'], 'func': f17_oskp_030_iv_term_inversion_count_63d_d3}, 'f17_oskp_031_iv_term_inversion_count_21d_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d'], 'func': f17_oskp_031_iv_term_inversion_count_21d_d3}, 'f17_oskp_032_iv_term_inversion_intensity_63d_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d'], 'func': f17_oskp_032_iv_term_inversion_intensity_63d_d3}, 'f17_oskp_033_iv_term_slope_change_21d_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d'], 'func': f17_oskp_033_iv_term_slope_change_21d_d3}, 'f17_oskp_034_iv_term_slope_change_63d_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d'], 'func': f17_oskp_034_iv_term_slope_change_63d_d3}, 'f17_oskp_035_iv_term_30_60_log_ratio_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d'], 'func': f17_oskp_035_iv_term_30_60_log_ratio_d3}, 'f17_oskp_036_iv_skew_30d_level_d3': {'inputs': ['iv_skew_30d'], 'func': f17_oskp_036_iv_skew_30d_level_d3}, 'f17_oskp_037_iv_skew_30d_zscore_252d_d3': {'inputs': ['iv_skew_30d'], 'func': f17_oskp_037_iv_skew_30d_zscore_252d_d3}, 'f17_oskp_038_iv_skew_30d_rank_pct_252d_d3': {'inputs': ['iv_skew_30d'], 'func': f17_oskp_038_iv_skew_30d_rank_pct_252d_d3}, 'f17_oskp_039_iv_skew_30d_above_p95_count_63d_d3': {'inputs': ['iv_skew_30d'], 'func': f17_oskp_039_iv_skew_30d_above_p95_count_63d_d3}, 'f17_oskp_040_iv_skew_30d_streak_above_long_mean_d3': {'inputs': ['iv_skew_30d'], 'func': f17_oskp_040_iv_skew_30d_streak_above_long_mean_d3}, 'f17_oskp_041_iv_skew_60d_level_d3': {'inputs': ['iv_skew_60d'], 'func': f17_oskp_041_iv_skew_60d_level_d3}, 'f17_oskp_042_iv_skew_60d_zscore_252d_d3': {'inputs': ['iv_skew_60d'], 'func': f17_oskp_042_iv_skew_60d_zscore_252d_d3}, 'f17_oskp_043_iv_skew_60d_rank_pct_252d_d3': {'inputs': ['iv_skew_60d'], 'func': f17_oskp_043_iv_skew_60d_rank_pct_252d_d3}, 'f17_oskp_044_skew_term_30_60_diff_d3': {'inputs': ['iv_skew_30d', 'iv_skew_60d'], 'func': f17_oskp_044_skew_term_30_60_diff_d3}, 'f17_oskp_045_put_minus_call_iv_30d_abs_d3': {'inputs': ['put_iv_30d', 'call_iv_30d'], 'func': f17_oskp_045_put_minus_call_iv_30d_abs_d3}, 'f17_oskp_046_put_minus_call_iv_30d_zscore_252d_d3': {'inputs': ['put_iv_30d', 'call_iv_30d'], 'func': f17_oskp_046_put_minus_call_iv_30d_zscore_252d_d3}, 'f17_oskp_047_put_minus_call_iv_60d_abs_d3': {'inputs': ['put_iv_60d', 'call_iv_60d'], 'func': f17_oskp_047_put_minus_call_iv_60d_abs_d3}, 'f17_oskp_048_put_call_iv_ratio_30d_d3': {'inputs': ['put_iv_30d', 'call_iv_30d'], 'func': f17_oskp_048_put_call_iv_ratio_30d_d3}, 'f17_oskp_049_put_call_iv_ratio_zscore_252d_d3': {'inputs': ['put_iv_30d', 'call_iv_30d'], 'func': f17_oskp_049_put_call_iv_ratio_zscore_252d_d3}, 'f17_oskp_050_skew_steepening_21d_d3': {'inputs': ['iv_skew_30d'], 'func': f17_oskp_050_skew_steepening_21d_d3}, 'f17_oskp_051_skew_steepening_63d_d3': {'inputs': ['iv_skew_30d'], 'func': f17_oskp_051_skew_steepening_63d_d3}, 'f17_oskp_052_skew_flattening_streak_d3': {'inputs': ['iv_skew_30d'], 'func': f17_oskp_052_skew_flattening_streak_d3}, 'f17_oskp_053_days_since_skew_minimum_252d_d3': {'inputs': ['iv_skew_30d'], 'func': f17_oskp_053_days_since_skew_minimum_252d_d3}, 'f17_oskp_054_skew_below_p5_count_63d_d3': {'inputs': ['iv_skew_30d'], 'func': f17_oskp_054_skew_below_p5_count_63d_d3}, 'f17_oskp_055_skew_complacency_composite_63d_d3': {'inputs': ['iv_skew_30d', 'atm_iv_30d'], 'func': f17_oskp_055_skew_complacency_composite_63d_d3}, 'f17_oskp_056_iv_realized_spread_30d_d3': {'inputs': ['atm_iv_30d', 'iv_realized_30d'], 'func': f17_oskp_056_iv_realized_spread_30d_d3}, 'f17_oskp_057_iv_realized_spread_zscore_252d_d3': {'inputs': ['atm_iv_30d', 'iv_realized_30d'], 'func': f17_oskp_057_iv_realized_spread_zscore_252d_d3}, 'f17_oskp_058_iv_realized_ratio_30d_d3': {'inputs': ['atm_iv_30d', 'iv_realized_30d'], 'func': f17_oskp_058_iv_realized_ratio_30d_d3}, 'f17_oskp_059_iv_realized_ratio_zscore_252d_d3': {'inputs': ['atm_iv_30d', 'iv_realized_30d'], 'func': f17_oskp_059_iv_realized_ratio_zscore_252d_d3}, 'f17_oskp_060_iv_minus_realized_count_above_5pct_63d_d3': {'inputs': ['atm_iv_30d', 'iv_realized_30d'], 'func': f17_oskp_060_iv_minus_realized_count_above_5pct_63d_d3}, 'f17_oskp_061_iv_realized_log_diff_30d_d3': {'inputs': ['atm_iv_30d', 'iv_realized_30d'], 'func': f17_oskp_061_iv_realized_log_diff_30d_d3}, 'f17_oskp_062_iv_realized_ratio_max_63d_d3': {'inputs': ['atm_iv_30d', 'iv_realized_30d'], 'func': f17_oskp_062_iv_realized_ratio_max_63d_d3}, 'f17_oskp_063_iv_realized_ratio_min_63d_d3': {'inputs': ['atm_iv_30d', 'iv_realized_30d'], 'func': f17_oskp_063_iv_realized_ratio_min_63d_d3}, 'f17_oskp_064_iv_realized_spread_kurtosis_63d_d3': {'inputs': ['atm_iv_30d', 'iv_realized_30d'], 'func': f17_oskp_064_iv_realized_spread_kurtosis_63d_d3}, 'f17_oskp_065_iv_realized_ratio_rank_pct_252d_d3': {'inputs': ['atm_iv_30d', 'iv_realized_30d'], 'func': f17_oskp_065_iv_realized_ratio_rank_pct_252d_d3}, 'f17_oskp_066_vrp_premium_compression_streak_d3': {'inputs': ['atm_iv_30d', 'iv_realized_30d'], 'func': f17_oskp_066_vrp_premium_compression_streak_d3}, 'f17_oskp_067_vrp_squeeze_under_p5_count_63d_d3': {'inputs': ['atm_iv_30d', 'iv_realized_30d'], 'func': f17_oskp_067_vrp_squeeze_under_p5_count_63d_d3}, 'f17_oskp_068_vrp_zscore_change_21d_d3': {'inputs': ['atm_iv_30d', 'iv_realized_30d'], 'func': f17_oskp_068_vrp_zscore_change_21d_d3}, 'f17_oskp_069_vrp_log_diff_21d_d3': {'inputs': ['atm_iv_30d', 'iv_realized_30d'], 'func': f17_oskp_069_vrp_log_diff_21d_d3}, 'f17_oskp_070_vrp_log_diff_63d_d3': {'inputs': ['atm_iv_30d', 'iv_realized_30d'], 'func': f17_oskp_070_vrp_log_diff_63d_d3}, 'f17_oskp_071_put_call_volume_ratio_level_d3': {'inputs': ['put_volume', 'call_volume'], 'func': f17_oskp_071_put_call_volume_ratio_level_d3}, 'f17_oskp_072_put_call_volume_ratio_zscore_252d_d3': {'inputs': ['put_volume', 'call_volume'], 'func': f17_oskp_072_put_call_volume_ratio_zscore_252d_d3}, 'f17_oskp_073_put_call_volume_ratio_rank_pct_63d_d3': {'inputs': ['put_volume', 'call_volume'], 'func': f17_oskp_073_put_call_volume_ratio_rank_pct_63d_d3}, 'f17_oskp_074_call_volume_zscore_252d_d3': {'inputs': ['call_volume'], 'func': f17_oskp_074_call_volume_zscore_252d_d3}, 'f17_oskp_075_call_volume_log_diff_5d_d3': {'inputs': ['call_volume'], 'func': f17_oskp_075_call_volume_log_diff_5d_d3}}
