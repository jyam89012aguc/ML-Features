"""options_skew_at_peak base features 001-075 — Pipeline 1a-inverse short-side blowup family.

Theme: extreme options-market signatures AT THE PEAK — IV climaxes, skew
flattening (call-heavy complacency), term-structure inversion, volatility
risk-premium compression, call-volume blowoffs, and put-call OI mix shifts.
150 distinct hypotheses (continued in __base__076_150.py). Inputs: OPT2
(ORATS) columns. OPT2 is OPTIONAL per HANDOFF §2 — when absent, the binder
must NaN-stub the input Series and these functions return NaN-aligned
Series. PIT-clean: right-anchored rolling, explicit min_periods, no centered
windows, no .shift(-N).
"""
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
    idx = num.index if hasattr(num, "index") else None
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
        return (np.searchsorted(np.sort(w), w[-1], side="right") - 0.5) / len(w)
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


# ============================================================
#                  FEATURES 001-075
# ============================================================

def f17_oskp_001_atm_iv_30d_zscore_252d(atm_iv_30d: pd.Series) -> pd.Series:
    """ATM 30d-IV z-score vs 252d — annual-baseline IV extremity at peak."""
    return _rolling_zscore(atm_iv_30d, YDAYS)


def f17_oskp_002_atm_iv_30d_zscore_63d(atm_iv_30d: pd.Series) -> pd.Series:
    """ATM 30d-IV z-score vs 63d — quarterly extremity."""
    return _rolling_zscore(atm_iv_30d, QDAYS)


def f17_oskp_003_atm_iv_30d_rank_pct_252d(atm_iv_30d: pd.Series) -> pd.Series:
    """Percentile rank of 30d-IV in 252d distribution — classic IV rank."""
    return _rolling_rank_pct(atm_iv_30d, YDAYS)


def f17_oskp_004_atm_iv_30d_rank_pct_63d(atm_iv_30d: pd.Series) -> pd.Series:
    """Percentile rank of 30d-IV in 63d distribution — short-window IV rank."""
    return _rolling_rank_pct(atm_iv_30d, QDAYS)


def f17_oskp_005_atm_iv_60d_zscore_252d(atm_iv_60d: pd.Series) -> pd.Series:
    """ATM 60d-IV z-score vs 252d — mid-term IV extremity."""
    return _rolling_zscore(atm_iv_60d, YDAYS)


def f17_oskp_006_atm_iv_60d_rank_pct_252d(atm_iv_60d: pd.Series) -> pd.Series:
    """Percentile rank of 60d-IV in 252d distribution."""
    return _rolling_rank_pct(atm_iv_60d, YDAYS)


def f17_oskp_007_atm_iv_90d_zscore_252d(atm_iv_90d: pd.Series) -> pd.Series:
    """ATM 90d-IV z-score vs 252d — back-month IV extremity."""
    return _rolling_zscore(atm_iv_90d, YDAYS)


def f17_oskp_008_atm_iv_30d_log_distance_to_252d_max(atm_iv_30d: pd.Series) -> pd.Series:
    """Log distance of current 30d-IV to its 252d rolling max — IV at-or-near ATH."""
    mx = atm_iv_30d.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_log(atm_iv_30d) - _safe_log(mx)


def f17_oskp_009_days_since_atm_iv_30d_max_252d(atm_iv_30d: pd.Series) -> pd.Series:
    """Bars since 30d-IV touched its 252d rolling max — recency of IV climax."""
    return _days_since_max(atm_iv_30d, YDAYS)


def f17_oskp_010_days_since_atm_iv_30d_min_252d(atm_iv_30d: pd.Series) -> pd.Series:
    """Bars since 30d-IV touched its 252d rolling min — distance from complacency."""
    return _days_since_min(atm_iv_30d, YDAYS)


def f17_oskp_011_atm_iv_30d_vs_yearly_median_ratio(atm_iv_30d: pd.Series) -> pd.Series:
    """30d-IV / 252d median — robust ratio of current IV to annual baseline."""
    med = atm_iv_30d.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(atm_iv_30d, med)


def f17_oskp_012_atm_iv_30d_above_p95_count_63d(atm_iv_30d: pd.Series) -> pd.Series:
    """Bars in last 63d where 30d-IV exceeded its trailing 252d p95 — fat-tail IV regime."""
    thr = atm_iv_30d.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    flag = (atm_iv_30d >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f17_oskp_013_atm_iv_30d_above_p99_count_252d(atm_iv_30d: pd.Series) -> pd.Series:
    """Bars in last 252d where 30d-IV exceeded its trailing p99 — extreme tail recurrence."""
    thr = atm_iv_30d.rolling(YDAYS, min_periods=QDAYS).quantile(0.99)
    flag = (atm_iv_30d >= thr).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f17_oskp_014_atm_iv_30d_min_max_range_normalized_63d(atm_iv_30d: pd.Series) -> pd.Series:
    """(max-min)/mean of 30d-IV over 63d — IV range-of-motion normalized."""
    mx = atm_iv_30d.rolling(QDAYS, min_periods=MDAYS).max()
    mn = atm_iv_30d.rolling(QDAYS, min_periods=MDAYS).min()
    m = atm_iv_30d.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(mx - mn, m)


def f17_oskp_015_atm_iv_30d_kurtosis_63d(atm_iv_30d: pd.Series) -> pd.Series:
    """Excess kurtosis of 30d-IV over 63d — fat-tailed IV bursting."""
    def _k(w):
        if np.isnan(w).any():
            return np.nan
        sd = w.std()
        if sd == 0:
            return np.nan
        return float(((w - w.mean()) ** 4).mean() / (sd ** 4) - 3.0)
    return atm_iv_30d.rolling(QDAYS, min_periods=MDAYS).apply(_k, raw=True)


def f17_oskp_016_atm_iv_30d_skewness_63d(atm_iv_30d: pd.Series) -> pd.Series:
    """Skewness of 30d-IV over 63d — directional IV regime asymmetry."""
    def _sk(w):
        if np.isnan(w).any():
            return np.nan
        sd = w.std()
        if sd == 0:
            return np.nan
        return float(((w - w.mean()) ** 3).mean() / (sd ** 3))
    return atm_iv_30d.rolling(QDAYS, min_periods=MDAYS).apply(_sk, raw=True)


def f17_oskp_017_atm_iv_30d_pct_above_long_mean_63d(atm_iv_30d: pd.Series) -> pd.Series:
    """Fraction of last 63d bars where 30d-IV exceeded 252d mean — persistence above baseline."""
    m252 = atm_iv_30d.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (atm_iv_30d > m252).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).mean()


def f17_oskp_018_atm_iv_30d_recency_break_above_2sigma_63d(atm_iv_30d: pd.Series) -> pd.Series:
    """Bars since the last 30d-IV > (mean+2*std over 252d) event — recency of IV blowoff."""
    m = atm_iv_30d.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = atm_iv_30d.rolling(YDAYS, min_periods=QDAYS).std()
    flag = (atm_iv_30d > (m + 2.0 * sd)).astype(float)
    def _r(w):
        if np.isnan(w).all():
            return np.nan
        nz = np.where(w > 0)[0]
        if len(nz) == 0:
            return float(len(w))
        return float(len(w) - 1 - nz[-1])
    return flag.rolling(YDAYS, min_periods=QDAYS).apply(_r, raw=True)


def f17_oskp_019_atm_iv_30d_streak_above_p75_252d(atm_iv_30d: pd.Series) -> pd.Series:
    """Current consecutive-bar streak of 30d-IV above its trailing-252d p75."""
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
    return flag.rolling(QDAYS, min_periods=WDAYS).apply(_streak, raw=True)


def f17_oskp_020_atm_iv_30d_ema5_to_ema63(atm_iv_30d: pd.Series) -> pd.Series:
    """EMA(5)/EMA(63) of 30d-IV — short-term IV acceleration vs quarterly baseline."""
    return _safe_div(_ema(atm_iv_30d, WDAYS), _ema(atm_iv_30d, QDAYS))


def f17_oskp_021_iv_term_slope_30_60_level(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    """Raw term slope (60d − 30d) — negative = backwardation (peak topping signal)."""
    return atm_iv_60d - atm_iv_30d


def f17_oskp_022_iv_term_slope_30_60_zscore_252d(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    """Z-score of (60d − 30d) term slope vs 252d."""
    slope = atm_iv_60d - atm_iv_30d
    return _rolling_zscore(slope, YDAYS)


def f17_oskp_023_iv_term_slope_30_60_rank_pct_252d(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    """Percentile rank of (60d − 30d) term slope vs 252d."""
    slope = atm_iv_60d - atm_iv_30d
    return _rolling_rank_pct(slope, YDAYS)


def f17_oskp_024_iv_term_slope_30_60_inversion_recency_252d(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    """Bars since term slope (60d − 30d) last went negative — backwardation recency."""
    slope = atm_iv_60d - atm_iv_30d
    flag = (slope < 0).astype(float)
    def _r(w):
        if np.isnan(w).all():
            return np.nan
        nz = np.where(w > 0)[0]
        if len(nz) == 0:
            return float(len(w))
        return float(len(w) - 1 - nz[-1])
    return flag.rolling(YDAYS, min_periods=QDAYS).apply(_r, raw=True)


def f17_oskp_025_iv_term_slope_60_90_level(atm_iv_60d: pd.Series, atm_iv_90d: pd.Series) -> pd.Series:
    """Raw term slope (90d − 60d) — back-end of term structure."""
    return atm_iv_90d - atm_iv_60d


def f17_oskp_026_iv_term_slope_60_90_zscore_252d(atm_iv_60d: pd.Series, atm_iv_90d: pd.Series) -> pd.Series:
    """Z-score of (90d − 60d) back-term slope vs 252d."""
    slope = atm_iv_90d - atm_iv_60d
    return _rolling_zscore(slope, YDAYS)


def f17_oskp_027_iv_term_curvature_30_60_90(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series, atm_iv_90d: pd.Series) -> pd.Series:
    """Term curvature (90d − 2*60d + 30d) — humped/bowed term-structure shape."""
    return atm_iv_90d - 2.0 * atm_iv_60d + atm_iv_30d


def f17_oskp_028_iv_term_curvature_zscore_252d(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series, atm_iv_90d: pd.Series) -> pd.Series:
    """Z-score of term curvature vs 252d."""
    c = atm_iv_90d - 2.0 * atm_iv_60d + atm_iv_30d
    return _rolling_zscore(c, YDAYS)


def f17_oskp_029_iv_term_flatness_count_63d(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    """Bars in last 63d where |60d − 30d|/30d < 0.05 — flat-term-structure regime."""
    rel = (atm_iv_60d - atm_iv_30d).abs() / atm_iv_30d.replace(0, np.nan)
    flag = (rel < 0.05).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f17_oskp_030_iv_term_inversion_count_63d(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    """Bars in last 63d with 30d-IV > 60d-IV — front-month inversion persistence."""
    flag = (atm_iv_30d > atm_iv_60d).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f17_oskp_031_iv_term_inversion_count_21d(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    """Bars in last 21d with 30d-IV > 60d-IV — short-window inversion intensity."""
    flag = (atm_iv_30d > atm_iv_60d).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f17_oskp_032_iv_term_inversion_intensity_63d(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    """Mean of max(0, 30d-IV − 60d-IV) over 63d — average inversion magnitude."""
    inv = (atm_iv_30d - atm_iv_60d).clip(lower=0)
    return inv.rolling(QDAYS, min_periods=MDAYS).mean()


def f17_oskp_033_iv_term_slope_change_21d(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    """21d change in (60d − 30d) term slope — term-structure thrust."""
    slope = atm_iv_60d - atm_iv_30d
    return slope.diff(MDAYS)


def f17_oskp_034_iv_term_slope_change_63d(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    """63d change in (60d − 30d) term slope — quarterly term-structure thrust."""
    slope = atm_iv_60d - atm_iv_30d
    return slope.diff(QDAYS)


def f17_oskp_035_iv_term_30_60_log_ratio(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    """log(60d-IV / 30d-IV) — scale-invariant term-structure indicator."""
    return _safe_log(atm_iv_60d) - _safe_log(atm_iv_30d)


def f17_oskp_036_iv_skew_30d_level(iv_skew_30d: pd.Series) -> pd.Series:
    """Raw 30d skew level — high skew = put-side fear, low skew = call-side complacency."""
    return iv_skew_30d.astype(float)


def f17_oskp_037_iv_skew_30d_zscore_252d(iv_skew_30d: pd.Series) -> pd.Series:
    """Z-score of 30d skew vs 252d — skew extremity."""
    return _rolling_zscore(iv_skew_30d, YDAYS)


def f17_oskp_038_iv_skew_30d_rank_pct_252d(iv_skew_30d: pd.Series) -> pd.Series:
    """Percentile rank of 30d skew vs 252d — skew percentile."""
    return _rolling_rank_pct(iv_skew_30d, YDAYS)


def f17_oskp_039_iv_skew_30d_above_p95_count_63d(iv_skew_30d: pd.Series) -> pd.Series:
    """Bars in last 63d with skew exceeding trailing-252d p95 — tail skew persistence."""
    thr = iv_skew_30d.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    flag = (iv_skew_30d >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f17_oskp_040_iv_skew_30d_streak_above_long_mean(iv_skew_30d: pd.Series) -> pd.Series:
    """Current consecutive-bar streak of 30d skew above its 252d mean."""
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
    return flag.rolling(QDAYS, min_periods=WDAYS).apply(_streak, raw=True)


def f17_oskp_041_iv_skew_60d_level(iv_skew_60d: pd.Series) -> pd.Series:
    """Raw 60d skew level — mid-term skew."""
    return iv_skew_60d.astype(float)


def f17_oskp_042_iv_skew_60d_zscore_252d(iv_skew_60d: pd.Series) -> pd.Series:
    """Z-score of 60d skew vs 252d."""
    return _rolling_zscore(iv_skew_60d, YDAYS)


def f17_oskp_043_iv_skew_60d_rank_pct_252d(iv_skew_60d: pd.Series) -> pd.Series:
    """Percentile rank of 60d skew vs 252d."""
    return _rolling_rank_pct(iv_skew_60d, YDAYS)


def f17_oskp_044_skew_term_30_60_diff(iv_skew_30d: pd.Series, iv_skew_60d: pd.Series) -> pd.Series:
    """(60d skew − 30d skew) — term structure of skew itself."""
    return iv_skew_60d - iv_skew_30d


def f17_oskp_045_put_minus_call_iv_30d_abs(put_iv_30d: pd.Series, call_iv_30d: pd.Series) -> pd.Series:
    """Put-IV minus Call-IV at 30d — raw asymmetry in IV smile wings."""
    return put_iv_30d - call_iv_30d


def f17_oskp_046_put_minus_call_iv_30d_zscore_252d(put_iv_30d: pd.Series, call_iv_30d: pd.Series) -> pd.Series:
    """Z-score of (put-IV − call-IV) 30d vs 252d."""
    return _rolling_zscore(put_iv_30d - call_iv_30d, YDAYS)


def f17_oskp_047_put_minus_call_iv_60d_abs(put_iv_60d: pd.Series, call_iv_60d: pd.Series) -> pd.Series:
    """Put-IV minus Call-IV at 60d — mid-term wing asymmetry."""
    return put_iv_60d - call_iv_60d


def f17_oskp_048_put_call_iv_ratio_30d(put_iv_30d: pd.Series, call_iv_30d: pd.Series) -> pd.Series:
    """put-IV / call-IV at 30d — scale-invariant wing asymmetry."""
    return _safe_div(put_iv_30d, call_iv_30d)


def f17_oskp_049_put_call_iv_ratio_zscore_252d(put_iv_30d: pd.Series, call_iv_30d: pd.Series) -> pd.Series:
    """Z-score of put-IV / call-IV ratio vs 252d."""
    r = _safe_div(put_iv_30d, call_iv_30d)
    return _rolling_zscore(r, YDAYS)


def f17_oskp_050_skew_steepening_21d(iv_skew_30d: pd.Series) -> pd.Series:
    """21d change in 30d skew — short-window steepening thrust (rising = put-side fear)."""
    return iv_skew_30d.diff(MDAYS)


def f17_oskp_051_skew_steepening_63d(iv_skew_30d: pd.Series) -> pd.Series:
    """63d change in 30d skew — quarterly steepening thrust."""
    return iv_skew_30d.diff(QDAYS)


def f17_oskp_052_skew_flattening_streak(iv_skew_30d: pd.Series) -> pd.Series:
    """Current consecutive-bar streak of negative skew diff — sustained flattening (complacency)."""
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
    return flag.rolling(QDAYS, min_periods=WDAYS).apply(_streak, raw=True)


def f17_oskp_053_days_since_skew_minimum_252d(iv_skew_30d: pd.Series) -> pd.Series:
    """Bars since 30d skew was at its 252d trailing minimum — call-skew complacency recency."""
    return _days_since_min(iv_skew_30d, YDAYS)


def f17_oskp_054_skew_below_p5_count_63d(iv_skew_30d: pd.Series) -> pd.Series:
    """Bars in last 63d with skew below trailing-252d p5 — extreme call-side bias persistence."""
    thr = iv_skew_30d.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    flag = (iv_skew_30d <= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f17_oskp_055_skew_complacency_composite_63d(iv_skew_30d: pd.Series, atm_iv_30d: pd.Series) -> pd.Series:
    """Composite of (low skew percentile) AND (low IV percentile) over 63d — fused complacency."""
    sk_r = _rolling_rank_pct(iv_skew_30d, YDAYS)
    iv_r = _rolling_rank_pct(atm_iv_30d, YDAYS)
    score = (1.0 - sk_r) * (1.0 - iv_r)
    return score.rolling(QDAYS, min_periods=MDAYS).mean()


def f17_oskp_056_iv_realized_spread_30d(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    """30d IV minus 30d realized vol — raw variance risk premium (VRP)."""
    return atm_iv_30d - iv_realized_30d


def f17_oskp_057_iv_realized_spread_zscore_252d(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    """Z-score of VRP vs 252d."""
    vrp = atm_iv_30d - iv_realized_30d
    return _rolling_zscore(vrp, YDAYS)


def f17_oskp_058_iv_realized_ratio_30d(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    """30d IV / 30d realized — scale-invariant VRP."""
    return _safe_div(atm_iv_30d, iv_realized_30d)


def f17_oskp_059_iv_realized_ratio_zscore_252d(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    """Z-score of IV/realized ratio vs 252d."""
    r = _safe_div(atm_iv_30d, iv_realized_30d)
    return _rolling_zscore(r, YDAYS)


def f17_oskp_060_iv_minus_realized_count_above_5pct_63d(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    """Bars in last 63d where IV − realized > 0.05 — sustained-rich-VRP persistence."""
    flag = ((atm_iv_30d - iv_realized_30d) > 0.05).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f17_oskp_061_iv_realized_log_diff_30d(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    """log(IV) − log(realized) — symmetric VRP for both directions."""
    return _safe_log(atm_iv_30d) - _safe_log(iv_realized_30d)


def f17_oskp_062_iv_realized_ratio_max_63d(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    """Max IV/realized over last 63d — peak VRP intensity in window."""
    r = _safe_div(atm_iv_30d, iv_realized_30d)
    return r.rolling(QDAYS, min_periods=MDAYS).max()


def f17_oskp_063_iv_realized_ratio_min_63d(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    """Min IV/realized over last 63d — VRP collapse (realized chasing IV)."""
    r = _safe_div(atm_iv_30d, iv_realized_30d)
    return r.rolling(QDAYS, min_periods=MDAYS).min()


def f17_oskp_064_iv_realized_spread_kurtosis_63d(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    """Excess kurtosis of VRP over 63d — fat-tailed VRP regime."""
    vrp = atm_iv_30d - iv_realized_30d
    def _k(w):
        if np.isnan(w).any():
            return np.nan
        sd = w.std()
        if sd == 0:
            return np.nan
        return float(((w - w.mean()) ** 4).mean() / (sd ** 4) - 3.0)
    return vrp.rolling(QDAYS, min_periods=MDAYS).apply(_k, raw=True)


def f17_oskp_065_iv_realized_ratio_rank_pct_252d(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    """Percentile rank of IV/realized ratio vs 252d."""
    r = _safe_div(atm_iv_30d, iv_realized_30d)
    return _rolling_rank_pct(r, YDAYS)


def f17_oskp_066_vrp_premium_compression_streak(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where IV < realized (premium compression)."""
    flag = ((atm_iv_30d - iv_realized_30d) < 0).astype(int)
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
    return flag.rolling(QDAYS, min_periods=WDAYS).apply(_streak, raw=True)


def f17_oskp_067_vrp_squeeze_under_p5_count_63d(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    """Bars in last 63d where VRP is below its trailing-252d p5 — extreme premium squeeze."""
    vrp = atm_iv_30d - iv_realized_30d
    thr = vrp.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    flag = (vrp <= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f17_oskp_068_vrp_zscore_change_21d(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    """21d change in (VRP z-score vs 252d) — VRP regime-shift acceleration."""
    vrp = atm_iv_30d - iv_realized_30d
    z = _rolling_zscore(vrp, YDAYS)
    return z.diff(MDAYS)


def f17_oskp_069_vrp_log_diff_21d(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    """21d change of log(IV/realized) — short-window VRP thrust."""
    return (_safe_log(atm_iv_30d) - _safe_log(iv_realized_30d)).diff(MDAYS)


def f17_oskp_070_vrp_log_diff_63d(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    """63d change of log(IV/realized) — quarterly VRP thrust."""
    return (_safe_log(atm_iv_30d) - _safe_log(iv_realized_30d)).diff(QDAYS)


def f17_oskp_071_put_call_volume_ratio_level(put_volume: pd.Series, call_volume: pd.Series) -> pd.Series:
    """put_volume / call_volume — raw daily flow asymmetry."""
    return _safe_div(put_volume, call_volume)


def f17_oskp_072_put_call_volume_ratio_zscore_252d(put_volume: pd.Series, call_volume: pd.Series) -> pd.Series:
    """Z-score of put/call volume ratio vs 252d."""
    r = _safe_div(put_volume, call_volume)
    return _rolling_zscore(r, YDAYS)


def f17_oskp_073_put_call_volume_ratio_rank_pct_63d(put_volume: pd.Series, call_volume: pd.Series) -> pd.Series:
    """Percentile rank of put/call volume ratio in trailing 63d."""
    r = _safe_div(put_volume, call_volume)
    return _rolling_rank_pct(r, QDAYS)


def f17_oskp_074_call_volume_zscore_252d(call_volume: pd.Series) -> pd.Series:
    """Z-score of call volume vs 252d — extreme call participation."""
    return _rolling_zscore(call_volume, YDAYS)


def f17_oskp_075_call_volume_log_diff_5d(call_volume: pd.Series) -> pd.Series:
    """5d log change in call volume — week-scale call-flow thrust."""
    return _safe_log(call_volume).diff(WDAYS)


# ============================================================
#                        REGISTRY
# ============================================================

OPTIONS_SKEW_AT_PEAK_BASE_REGISTRY_001_075 = {
    "f17_oskp_001_atm_iv_30d_zscore_252d": {"inputs": ["atm_iv_30d"], "func": f17_oskp_001_atm_iv_30d_zscore_252d},
    "f17_oskp_002_atm_iv_30d_zscore_63d": {"inputs": ["atm_iv_30d"], "func": f17_oskp_002_atm_iv_30d_zscore_63d},
    "f17_oskp_003_atm_iv_30d_rank_pct_252d": {"inputs": ["atm_iv_30d"], "func": f17_oskp_003_atm_iv_30d_rank_pct_252d},
    "f17_oskp_004_atm_iv_30d_rank_pct_63d": {"inputs": ["atm_iv_30d"], "func": f17_oskp_004_atm_iv_30d_rank_pct_63d},
    "f17_oskp_005_atm_iv_60d_zscore_252d": {"inputs": ["atm_iv_60d"], "func": f17_oskp_005_atm_iv_60d_zscore_252d},
    "f17_oskp_006_atm_iv_60d_rank_pct_252d": {"inputs": ["atm_iv_60d"], "func": f17_oskp_006_atm_iv_60d_rank_pct_252d},
    "f17_oskp_007_atm_iv_90d_zscore_252d": {"inputs": ["atm_iv_90d"], "func": f17_oskp_007_atm_iv_90d_zscore_252d},
    "f17_oskp_008_atm_iv_30d_log_distance_to_252d_max": {"inputs": ["atm_iv_30d"], "func": f17_oskp_008_atm_iv_30d_log_distance_to_252d_max},
    "f17_oskp_009_days_since_atm_iv_30d_max_252d": {"inputs": ["atm_iv_30d"], "func": f17_oskp_009_days_since_atm_iv_30d_max_252d},
    "f17_oskp_010_days_since_atm_iv_30d_min_252d": {"inputs": ["atm_iv_30d"], "func": f17_oskp_010_days_since_atm_iv_30d_min_252d},
    "f17_oskp_011_atm_iv_30d_vs_yearly_median_ratio": {"inputs": ["atm_iv_30d"], "func": f17_oskp_011_atm_iv_30d_vs_yearly_median_ratio},
    "f17_oskp_012_atm_iv_30d_above_p95_count_63d": {"inputs": ["atm_iv_30d"], "func": f17_oskp_012_atm_iv_30d_above_p95_count_63d},
    "f17_oskp_013_atm_iv_30d_above_p99_count_252d": {"inputs": ["atm_iv_30d"], "func": f17_oskp_013_atm_iv_30d_above_p99_count_252d},
    "f17_oskp_014_atm_iv_30d_min_max_range_normalized_63d": {"inputs": ["atm_iv_30d"], "func": f17_oskp_014_atm_iv_30d_min_max_range_normalized_63d},
    "f17_oskp_015_atm_iv_30d_kurtosis_63d": {"inputs": ["atm_iv_30d"], "func": f17_oskp_015_atm_iv_30d_kurtosis_63d},
    "f17_oskp_016_atm_iv_30d_skewness_63d": {"inputs": ["atm_iv_30d"], "func": f17_oskp_016_atm_iv_30d_skewness_63d},
    "f17_oskp_017_atm_iv_30d_pct_above_long_mean_63d": {"inputs": ["atm_iv_30d"], "func": f17_oskp_017_atm_iv_30d_pct_above_long_mean_63d},
    "f17_oskp_018_atm_iv_30d_recency_break_above_2sigma_63d": {"inputs": ["atm_iv_30d"], "func": f17_oskp_018_atm_iv_30d_recency_break_above_2sigma_63d},
    "f17_oskp_019_atm_iv_30d_streak_above_p75_252d": {"inputs": ["atm_iv_30d"], "func": f17_oskp_019_atm_iv_30d_streak_above_p75_252d},
    "f17_oskp_020_atm_iv_30d_ema5_to_ema63": {"inputs": ["atm_iv_30d"], "func": f17_oskp_020_atm_iv_30d_ema5_to_ema63},
    "f17_oskp_021_iv_term_slope_30_60_level": {"inputs": ["atm_iv_30d", "atm_iv_60d"], "func": f17_oskp_021_iv_term_slope_30_60_level},
    "f17_oskp_022_iv_term_slope_30_60_zscore_252d": {"inputs": ["atm_iv_30d", "atm_iv_60d"], "func": f17_oskp_022_iv_term_slope_30_60_zscore_252d},
    "f17_oskp_023_iv_term_slope_30_60_rank_pct_252d": {"inputs": ["atm_iv_30d", "atm_iv_60d"], "func": f17_oskp_023_iv_term_slope_30_60_rank_pct_252d},
    "f17_oskp_024_iv_term_slope_30_60_inversion_recency_252d": {"inputs": ["atm_iv_30d", "atm_iv_60d"], "func": f17_oskp_024_iv_term_slope_30_60_inversion_recency_252d},
    "f17_oskp_025_iv_term_slope_60_90_level": {"inputs": ["atm_iv_60d", "atm_iv_90d"], "func": f17_oskp_025_iv_term_slope_60_90_level},
    "f17_oskp_026_iv_term_slope_60_90_zscore_252d": {"inputs": ["atm_iv_60d", "atm_iv_90d"], "func": f17_oskp_026_iv_term_slope_60_90_zscore_252d},
    "f17_oskp_027_iv_term_curvature_30_60_90": {"inputs": ["atm_iv_30d", "atm_iv_60d", "atm_iv_90d"], "func": f17_oskp_027_iv_term_curvature_30_60_90},
    "f17_oskp_028_iv_term_curvature_zscore_252d": {"inputs": ["atm_iv_30d", "atm_iv_60d", "atm_iv_90d"], "func": f17_oskp_028_iv_term_curvature_zscore_252d},
    "f17_oskp_029_iv_term_flatness_count_63d": {"inputs": ["atm_iv_30d", "atm_iv_60d"], "func": f17_oskp_029_iv_term_flatness_count_63d},
    "f17_oskp_030_iv_term_inversion_count_63d": {"inputs": ["atm_iv_30d", "atm_iv_60d"], "func": f17_oskp_030_iv_term_inversion_count_63d},
    "f17_oskp_031_iv_term_inversion_count_21d": {"inputs": ["atm_iv_30d", "atm_iv_60d"], "func": f17_oskp_031_iv_term_inversion_count_21d},
    "f17_oskp_032_iv_term_inversion_intensity_63d": {"inputs": ["atm_iv_30d", "atm_iv_60d"], "func": f17_oskp_032_iv_term_inversion_intensity_63d},
    "f17_oskp_033_iv_term_slope_change_21d": {"inputs": ["atm_iv_30d", "atm_iv_60d"], "func": f17_oskp_033_iv_term_slope_change_21d},
    "f17_oskp_034_iv_term_slope_change_63d": {"inputs": ["atm_iv_30d", "atm_iv_60d"], "func": f17_oskp_034_iv_term_slope_change_63d},
    "f17_oskp_035_iv_term_30_60_log_ratio": {"inputs": ["atm_iv_30d", "atm_iv_60d"], "func": f17_oskp_035_iv_term_30_60_log_ratio},
    "f17_oskp_036_iv_skew_30d_level": {"inputs": ["iv_skew_30d"], "func": f17_oskp_036_iv_skew_30d_level},
    "f17_oskp_037_iv_skew_30d_zscore_252d": {"inputs": ["iv_skew_30d"], "func": f17_oskp_037_iv_skew_30d_zscore_252d},
    "f17_oskp_038_iv_skew_30d_rank_pct_252d": {"inputs": ["iv_skew_30d"], "func": f17_oskp_038_iv_skew_30d_rank_pct_252d},
    "f17_oskp_039_iv_skew_30d_above_p95_count_63d": {"inputs": ["iv_skew_30d"], "func": f17_oskp_039_iv_skew_30d_above_p95_count_63d},
    "f17_oskp_040_iv_skew_30d_streak_above_long_mean": {"inputs": ["iv_skew_30d"], "func": f17_oskp_040_iv_skew_30d_streak_above_long_mean},
    "f17_oskp_041_iv_skew_60d_level": {"inputs": ["iv_skew_60d"], "func": f17_oskp_041_iv_skew_60d_level},
    "f17_oskp_042_iv_skew_60d_zscore_252d": {"inputs": ["iv_skew_60d"], "func": f17_oskp_042_iv_skew_60d_zscore_252d},
    "f17_oskp_043_iv_skew_60d_rank_pct_252d": {"inputs": ["iv_skew_60d"], "func": f17_oskp_043_iv_skew_60d_rank_pct_252d},
    "f17_oskp_044_skew_term_30_60_diff": {"inputs": ["iv_skew_30d", "iv_skew_60d"], "func": f17_oskp_044_skew_term_30_60_diff},
    "f17_oskp_045_put_minus_call_iv_30d_abs": {"inputs": ["put_iv_30d", "call_iv_30d"], "func": f17_oskp_045_put_minus_call_iv_30d_abs},
    "f17_oskp_046_put_minus_call_iv_30d_zscore_252d": {"inputs": ["put_iv_30d", "call_iv_30d"], "func": f17_oskp_046_put_minus_call_iv_30d_zscore_252d},
    "f17_oskp_047_put_minus_call_iv_60d_abs": {"inputs": ["put_iv_60d", "call_iv_60d"], "func": f17_oskp_047_put_minus_call_iv_60d_abs},
    "f17_oskp_048_put_call_iv_ratio_30d": {"inputs": ["put_iv_30d", "call_iv_30d"], "func": f17_oskp_048_put_call_iv_ratio_30d},
    "f17_oskp_049_put_call_iv_ratio_zscore_252d": {"inputs": ["put_iv_30d", "call_iv_30d"], "func": f17_oskp_049_put_call_iv_ratio_zscore_252d},
    "f17_oskp_050_skew_steepening_21d": {"inputs": ["iv_skew_30d"], "func": f17_oskp_050_skew_steepening_21d},
    "f17_oskp_051_skew_steepening_63d": {"inputs": ["iv_skew_30d"], "func": f17_oskp_051_skew_steepening_63d},
    "f17_oskp_052_skew_flattening_streak": {"inputs": ["iv_skew_30d"], "func": f17_oskp_052_skew_flattening_streak},
    "f17_oskp_053_days_since_skew_minimum_252d": {"inputs": ["iv_skew_30d"], "func": f17_oskp_053_days_since_skew_minimum_252d},
    "f17_oskp_054_skew_below_p5_count_63d": {"inputs": ["iv_skew_30d"], "func": f17_oskp_054_skew_below_p5_count_63d},
    "f17_oskp_055_skew_complacency_composite_63d": {"inputs": ["iv_skew_30d", "atm_iv_30d"], "func": f17_oskp_055_skew_complacency_composite_63d},
    "f17_oskp_056_iv_realized_spread_30d": {"inputs": ["atm_iv_30d", "iv_realized_30d"], "func": f17_oskp_056_iv_realized_spread_30d},
    "f17_oskp_057_iv_realized_spread_zscore_252d": {"inputs": ["atm_iv_30d", "iv_realized_30d"], "func": f17_oskp_057_iv_realized_spread_zscore_252d},
    "f17_oskp_058_iv_realized_ratio_30d": {"inputs": ["atm_iv_30d", "iv_realized_30d"], "func": f17_oskp_058_iv_realized_ratio_30d},
    "f17_oskp_059_iv_realized_ratio_zscore_252d": {"inputs": ["atm_iv_30d", "iv_realized_30d"], "func": f17_oskp_059_iv_realized_ratio_zscore_252d},
    "f17_oskp_060_iv_minus_realized_count_above_5pct_63d": {"inputs": ["atm_iv_30d", "iv_realized_30d"], "func": f17_oskp_060_iv_minus_realized_count_above_5pct_63d},
    "f17_oskp_061_iv_realized_log_diff_30d": {"inputs": ["atm_iv_30d", "iv_realized_30d"], "func": f17_oskp_061_iv_realized_log_diff_30d},
    "f17_oskp_062_iv_realized_ratio_max_63d": {"inputs": ["atm_iv_30d", "iv_realized_30d"], "func": f17_oskp_062_iv_realized_ratio_max_63d},
    "f17_oskp_063_iv_realized_ratio_min_63d": {"inputs": ["atm_iv_30d", "iv_realized_30d"], "func": f17_oskp_063_iv_realized_ratio_min_63d},
    "f17_oskp_064_iv_realized_spread_kurtosis_63d": {"inputs": ["atm_iv_30d", "iv_realized_30d"], "func": f17_oskp_064_iv_realized_spread_kurtosis_63d},
    "f17_oskp_065_iv_realized_ratio_rank_pct_252d": {"inputs": ["atm_iv_30d", "iv_realized_30d"], "func": f17_oskp_065_iv_realized_ratio_rank_pct_252d},
    "f17_oskp_066_vrp_premium_compression_streak": {"inputs": ["atm_iv_30d", "iv_realized_30d"], "func": f17_oskp_066_vrp_premium_compression_streak},
    "f17_oskp_067_vrp_squeeze_under_p5_count_63d": {"inputs": ["atm_iv_30d", "iv_realized_30d"], "func": f17_oskp_067_vrp_squeeze_under_p5_count_63d},
    "f17_oskp_068_vrp_zscore_change_21d": {"inputs": ["atm_iv_30d", "iv_realized_30d"], "func": f17_oskp_068_vrp_zscore_change_21d},
    "f17_oskp_069_vrp_log_diff_21d": {"inputs": ["atm_iv_30d", "iv_realized_30d"], "func": f17_oskp_069_vrp_log_diff_21d},
    "f17_oskp_070_vrp_log_diff_63d": {"inputs": ["atm_iv_30d", "iv_realized_30d"], "func": f17_oskp_070_vrp_log_diff_63d},
    "f17_oskp_071_put_call_volume_ratio_level": {"inputs": ["put_volume", "call_volume"], "func": f17_oskp_071_put_call_volume_ratio_level},
    "f17_oskp_072_put_call_volume_ratio_zscore_252d": {"inputs": ["put_volume", "call_volume"], "func": f17_oskp_072_put_call_volume_ratio_zscore_252d},
    "f17_oskp_073_put_call_volume_ratio_rank_pct_63d": {"inputs": ["put_volume", "call_volume"], "func": f17_oskp_073_put_call_volume_ratio_rank_pct_63d},
    "f17_oskp_074_call_volume_zscore_252d": {"inputs": ["call_volume"], "func": f17_oskp_074_call_volume_zscore_252d},
    "f17_oskp_075_call_volume_log_diff_5d": {"inputs": ["call_volume"], "func": f17_oskp_075_call_volume_log_diff_5d},
}
