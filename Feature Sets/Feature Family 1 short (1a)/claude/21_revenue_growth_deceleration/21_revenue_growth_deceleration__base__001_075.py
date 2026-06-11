"""revenue_growth_deceleration base features 001-075 — Pipeline 1a-inverse short-side blowup family.

75 distinct hypotheses about top-line growth slowdown (continued in __base__076_150.py).
Inputs: SF1 quarterly fundamentals. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no forward-looking shifts. Quarterly windows only (4, 8, 12, 16, 20).
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


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


def _safe_log(s, eps=1e-12):
    if isinstance(s, pd.Series):
        return np.log(s.where(s > eps, np.nan))
    arr = np.where(s > eps, s, np.nan)
    return np.log(arr)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


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


def _ttm(s):
    return s.rolling(4, min_periods=1).sum()


def _avg4(s):
    return s.rolling(4, min_periods=1).mean()


def _yoy(s):
    return s - s.shift(4)


def _yoy_pct(s):
    return _safe_div(s - s.shift(4), s.shift(4).abs())


def _qoq(s):
    return s.diff()


def _qoq_pct(s):
    return _safe_div(s.diff(), s.shift(1).abs())


def _cagr(s, lag, years):
    den = s.shift(lag)
    ratio = _safe_div(s, den)
    ratio = ratio.where(ratio > 0, np.nan)
    return ratio.pow(1.0 / years) - 1.0


def _consec_true_streak(b):
    b = b.fillna(False).astype(bool)
    grp = (~b).cumsum()
    return b.astype(int).groupby(grp).cumsum()


def _max_consec_true(b, window):
    streak = _consec_true_streak(b)
    return streak.rolling(window, min_periods=1).max()


def _rolling_count(b, window):
    return b.fillna(False).astype(float).rolling(window, min_periods=1).sum()


def _rolling_frac(b, window):
    return b.fillna(False).astype(float).rolling(window, min_periods=1).mean()


# ============================================================
#                    FEATURES 001-075
# ============================================================

# ---- Block A: Growth-rate primitives (001-020) ----

def f21_rgdc_001_rev_yoy_pct(revenue):
    return _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())


def f21_rgdc_002_rev_qoq_pct(revenue):
    return _safe_div(revenue - revenue.shift(1), revenue.shift(1).abs())


def f21_rgdc_003_rev_ttm_yoy_pct(revenue):
    ttm = _ttm(revenue)
    return _safe_div(ttm - ttm.shift(4), ttm.shift(4).abs())


def f21_rgdc_004_rev_2y_pct(revenue):
    return _safe_div(revenue - revenue.shift(8), revenue.shift(8).abs())


def f21_rgdc_005_rev_3y_pct(revenue):
    return _safe_div(revenue - revenue.shift(12), revenue.shift(12).abs())


def f21_rgdc_006_rev_cagr_2y(revenue):
    return _cagr(revenue, 8, 2.0)


def f21_rgdc_007_rev_cagr_3y(revenue):
    return _cagr(revenue, 12, 3.0)


def f21_rgdc_008_rev_cagr_5y(revenue):
    return _cagr(revenue, 20, 5.0)


def f21_rgdc_009_rev_yoy_minus_qoq_annualized(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    qoq = _safe_div(revenue - revenue.shift(1), revenue.shift(1).abs())
    return yoy - ((1.0 + qoq) ** 4 - 1.0)


def f21_rgdc_010_rev_yoy_deceleration_lag1(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return yoy - yoy.shift(1)


def f21_rgdc_011_rev_qoq_deceleration_lag1(revenue):
    qoq = _safe_div(revenue - revenue.shift(1), revenue.shift(1).abs())
    return qoq - qoq.shift(1)


def f21_rgdc_012_rev_ttm_yoy_deceleration_lag1(revenue):
    ttm = _ttm(revenue)
    yoy = _safe_div(ttm - ttm.shift(4), ttm.shift(4).abs())
    return yoy - yoy.shift(1)


def f21_rgdc_013_rev_yoy_pct_8q_min(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return yoy.rolling(8, min_periods=3).min()


def f21_rgdc_014_rev_yoy_pct_8q_max(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return yoy.rolling(8, min_periods=3).max()


def f21_rgdc_015_rev_yoy_pct_8q_range(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return yoy.rolling(8, min_periods=3).max() - yoy.rolling(8, min_periods=3).min()


def f21_rgdc_016_rev_yoy_pct_drop_from_8q_max(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return yoy - yoy.rolling(8, min_periods=3).max()


def f21_rgdc_017_rev_yoy_pct_recovery_from_8q_min(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return yoy - yoy.rolling(8, min_periods=3).min()


def f21_rgdc_018_rev_yoy_pct_zscore_8q(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return _rolling_zscore(yoy, 8)


def f21_rgdc_019_rev_yoy_pct_zscore_12q(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return _rolling_zscore(yoy, 12)


def f21_rgdc_020_rev_growth_decay_proxy(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return _cagr(revenue, 8, 2.0) - yoy


# ---- Block B: Growth-rate trend/slope (021-040) ----

def f21_rgdc_021_rev_yoy_pct_4q_slope(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return _rolling_slope(yoy, 4)


def f21_rgdc_022_rev_yoy_pct_8q_slope(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return _rolling_slope(yoy, 8)


def f21_rgdc_023_rev_yoy_pct_12q_slope(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return _rolling_slope(yoy, 12)


def f21_rgdc_024_rev_qoq_pct_4q_slope(revenue):
    qoq = _safe_div(revenue - revenue.shift(1), revenue.shift(1).abs())
    return _rolling_slope(qoq, 4)


def f21_rgdc_025_rev_qoq_pct_8q_slope(revenue):
    qoq = _safe_div(revenue - revenue.shift(1), revenue.shift(1).abs())
    return _rolling_slope(qoq, 8)


def f21_rgdc_026_rev_ttm_4q_slope(revenue):
    return _rolling_slope(_ttm(revenue), 4)


def f21_rgdc_027_rev_ttm_8q_slope(revenue):
    return _rolling_slope(_ttm(revenue), 8)


def f21_rgdc_028_rev_yoy_pct_4q_negative_streak(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return _consec_true_streak(yoy < 0).clip(upper=4)


def f21_rgdc_029_rev_yoy_pct_below_5pct_count_4q(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return _rolling_count(yoy < 0.05, 4)


def f21_rgdc_030_rev_yoy_pct_below_5pct_count_8q(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return _rolling_count(yoy < 0.05, 8)


def f21_rgdc_031_rev_yoy_pct_consec_decel_streak(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return _consec_true_streak(yoy < yoy.shift(1))


def f21_rgdc_032_rev_qoq_pct_consec_negative_streak(revenue):
    qoq = _safe_div(revenue - revenue.shift(1), revenue.shift(1).abs())
    return _consec_true_streak(qoq < 0)


def f21_rgdc_033_rev_yoy_pct_max_consec_decel_8q(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return _max_consec_true(yoy < yoy.shift(1), 8)


def f21_rgdc_034_rev_yoy_pct_acceleration(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return yoy.diff()


def f21_rgdc_035_rev_yoy_pct_jerk(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return yoy.diff().diff()


def f21_rgdc_036_rev_yoy_pct_4q_mean(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return yoy.rolling(4, min_periods=2).mean()


def f21_rgdc_037_rev_yoy_pct_8q_mean(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return yoy.rolling(8, min_periods=3).mean()


def f21_rgdc_038_rev_yoy_pct_12q_mean(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return yoy.rolling(12, min_periods=4).mean()


def f21_rgdc_039_rev_yoy_pct_4q_vs_8q_mean_diff(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return yoy.rolling(4, min_periods=2).mean() - yoy.rolling(8, min_periods=3).mean()


def f21_rgdc_040_rev_yoy_pct_8q_vs_12q_mean_diff(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return yoy.rolling(8, min_periods=3).mean() - yoy.rolling(12, min_periods=4).mean()


# ---- Block C: Cross-horizon decay (041-060) ----

def f21_rgdc_041_rev_3y_cagr_minus_1y_yoy(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return _cagr(revenue, 12, 3.0) - yoy


def f21_rgdc_042_rev_5y_cagr_minus_1y_yoy(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return _cagr(revenue, 20, 5.0) - yoy


def f21_rgdc_043_rev_2y_cagr_minus_1y_yoy(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return _cagr(revenue, 8, 2.0) - yoy


def f21_rgdc_044_rev_3y_cagr_minus_2y_cagr(revenue):
    return _cagr(revenue, 12, 3.0) - _cagr(revenue, 8, 2.0)


def f21_rgdc_045_rev_5y_cagr_minus_3y_cagr(revenue):
    return _cagr(revenue, 20, 5.0) - _cagr(revenue, 12, 3.0)


def f21_rgdc_046_rev_growth_term_structure_slope(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    c2 = _cagr(revenue, 8, 2.0)
    c3 = _cagr(revenue, 12, 3.0)
    c5 = _cagr(revenue, 20, 5.0)
    x = np.array([20.0, 12.0, 8.0, 4.0])
    xm = x.mean()
    df = pd.concat([c5, c3, c2, yoy], axis=1)
    arr = df.values
    ym = np.nanmean(arr, axis=1, keepdims=True)
    num = np.nansum((x - xm) * (arr - ym), axis=1)
    den = ((x - xm) ** 2).sum()
    out = num / den if den != 0 else np.full(len(arr), np.nan)
    valid = (~np.isnan(arr)).sum(axis=1) >= 3
    out = np.where(valid, out, np.nan)
    return pd.Series(out, index=revenue.index)


def f21_rgdc_047_rev_growth_inversion_signal_5pt(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    c3 = _cagr(revenue, 12, 3.0)
    return (yoy + 0.05 < c3).astype(float)


def f21_rgdc_048_rev_growth_inversion_signal_10pt(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    c3 = _cagr(revenue, 12, 3.0)
    return (yoy + 0.10 < c3).astype(float)


def f21_rgdc_049_rev_yoy_below_3y_cagr_count_8q(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    c3 = _cagr(revenue, 12, 3.0)
    return _rolling_count(yoy < c3, 8)


def f21_rgdc_050_rev_yoy_below_5y_cagr_count_8q(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    c5 = _cagr(revenue, 20, 5.0)
    return _rolling_count(yoy < c5, 8)


def f21_rgdc_051_rev_growth_rolloff_rate_4q(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return (yoy - yoy.shift(4)) / 4.0


def f21_rgdc_052_rev_growth_rolloff_rate_8q(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return (yoy - yoy.shift(8)) / 8.0


def f21_rgdc_053_rev_growth_rolloff_rate_12q(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return (yoy - yoy.shift(12)) / 12.0


def f21_rgdc_054_rev_4q_geomean_growth(revenue):
    den = revenue.shift(4)
    ratio = _safe_div(revenue, den)
    ratio = ratio.where(ratio > 0, np.nan)
    return ratio.pow(1.0 / 4.0) - 1.0


def f21_rgdc_055_rev_8q_geomean_growth(revenue):
    den = revenue.shift(8)
    ratio = _safe_div(revenue, den)
    ratio = ratio.where(ratio > 0, np.nan)
    return ratio.pow(1.0 / 8.0) - 1.0


def f21_rgdc_056_rev_4q_geomean_minus_8q_geomean(revenue):
    r4 = _safe_div(revenue, revenue.shift(4)).where(lambda x: x > 0, np.nan).pow(1.0 / 4.0) - 1.0
    r8 = _safe_div(revenue, revenue.shift(8)).where(lambda x: x > 0, np.nan).pow(1.0 / 8.0) - 1.0
    return r4 - r8


def f21_rgdc_057_rev_8q_geomean_minus_12q_geomean(revenue):
    r8 = _safe_div(revenue, revenue.shift(8)).where(lambda x: x > 0, np.nan).pow(1.0 / 8.0) - 1.0
    r12 = _safe_div(revenue, revenue.shift(12)).where(lambda x: x > 0, np.nan).pow(1.0 / 12.0) - 1.0
    return r8 - r12


def f21_rgdc_058_rev_seasonal_2y_yoy_pct(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return yoy.rolling(4, min_periods=2).mean()


def f21_rgdc_059_rev_seasonal_yoy_4q_mean(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return yoy.rolling(4, min_periods=2).mean()


def f21_rgdc_060_rev_seasonal_yoy_acceleration(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return yoy - yoy.rolling(4, min_periods=2).mean()


# ---- Block D part 1: Volatility & quality of growth (061-075) ----

def f21_rgdc_061_rev_qoq_pct_std_4q(revenue):
    qoq = _safe_div(revenue - revenue.shift(1), revenue.shift(1).abs())
    return qoq.rolling(4, min_periods=2).std()


def f21_rgdc_062_rev_qoq_pct_std_8q(revenue):
    qoq = _safe_div(revenue - revenue.shift(1), revenue.shift(1).abs())
    return qoq.rolling(8, min_periods=3).std()


def f21_rgdc_063_rev_yoy_pct_std_8q(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return yoy.rolling(8, min_periods=3).std()


def f21_rgdc_064_rev_yoy_pct_std_12q(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return yoy.rolling(12, min_periods=4).std()


def f21_rgdc_065_rev_growth_coefvar_8q(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    sd = yoy.rolling(8, min_periods=3).std()
    m = yoy.rolling(8, min_periods=3).mean().abs().replace(0, np.nan)
    return sd / m


def f21_rgdc_066_rev_qoq_negative_fraction_8q(revenue):
    qoq = _safe_div(revenue - revenue.shift(1), revenue.shift(1).abs())
    return _rolling_frac(qoq < 0, 8)


def f21_rgdc_067_rev_qoq_negative_fraction_12q(revenue):
    qoq = _safe_div(revenue - revenue.shift(1), revenue.shift(1).abs())
    return _rolling_frac(qoq < 0, 12)


def f21_rgdc_068_rev_yoy_negative_fraction_8q(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return _rolling_frac(yoy < 0, 8)


def f21_rgdc_069_rev_yoy_negative_fraction_12q(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return _rolling_frac(yoy < 0, 12)


def f21_rgdc_070_rev_growth_skewness_8q(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return yoy.rolling(8, min_periods=4).skew()


def f21_rgdc_071_rev_growth_kurtosis_8q(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return yoy.rolling(8, min_periods=4).kurt()


def f21_rgdc_072_rev_growth_max_drawdown_4q(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return yoy.rolling(4, min_periods=2).min() - yoy.rolling(4, min_periods=2).max()


def f21_rgdc_073_rev_growth_max_drawdown_8q(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return yoy.rolling(8, min_periods=3).min() - yoy.rolling(8, min_periods=3).max()


def f21_rgdc_074_rev_growth_max_drawdown_12q(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    return yoy.rolling(12, min_periods=4).min() - yoy.rolling(12, min_periods=4).max()


def f21_rgdc_075_rev_growth_choppiness_8q(revenue):
    yoy = _safe_div(revenue - revenue.shift(4), revenue.shift(4).abs())
    d = yoy.diff()
    sgn_flip = ((np.sign(d) * np.sign(d.shift(1))) < 0).astype(float)
    return sgn_flip.rolling(8, min_periods=3).sum()


# ============================================================
#                        REGISTRY
# ============================================================

REVENUE_GROWTH_DECELERATION_BASE_REGISTRY_001_075 = {
    "f21_rgdc_001_rev_yoy_pct": {"inputs": ["revenue"], "func": f21_rgdc_001_rev_yoy_pct},
    "f21_rgdc_002_rev_qoq_pct": {"inputs": ["revenue"], "func": f21_rgdc_002_rev_qoq_pct},
    "f21_rgdc_003_rev_ttm_yoy_pct": {"inputs": ["revenue"], "func": f21_rgdc_003_rev_ttm_yoy_pct},
    "f21_rgdc_004_rev_2y_pct": {"inputs": ["revenue"], "func": f21_rgdc_004_rev_2y_pct},
    "f21_rgdc_005_rev_3y_pct": {"inputs": ["revenue"], "func": f21_rgdc_005_rev_3y_pct},
    "f21_rgdc_006_rev_cagr_2y": {"inputs": ["revenue"], "func": f21_rgdc_006_rev_cagr_2y},
    "f21_rgdc_007_rev_cagr_3y": {"inputs": ["revenue"], "func": f21_rgdc_007_rev_cagr_3y},
    "f21_rgdc_008_rev_cagr_5y": {"inputs": ["revenue"], "func": f21_rgdc_008_rev_cagr_5y},
    "f21_rgdc_009_rev_yoy_minus_qoq_annualized": {"inputs": ["revenue"], "func": f21_rgdc_009_rev_yoy_minus_qoq_annualized},
    "f21_rgdc_010_rev_yoy_deceleration_lag1": {"inputs": ["revenue"], "func": f21_rgdc_010_rev_yoy_deceleration_lag1},
    "f21_rgdc_011_rev_qoq_deceleration_lag1": {"inputs": ["revenue"], "func": f21_rgdc_011_rev_qoq_deceleration_lag1},
    "f21_rgdc_012_rev_ttm_yoy_deceleration_lag1": {"inputs": ["revenue"], "func": f21_rgdc_012_rev_ttm_yoy_deceleration_lag1},
    "f21_rgdc_013_rev_yoy_pct_8q_min": {"inputs": ["revenue"], "func": f21_rgdc_013_rev_yoy_pct_8q_min},
    "f21_rgdc_014_rev_yoy_pct_8q_max": {"inputs": ["revenue"], "func": f21_rgdc_014_rev_yoy_pct_8q_max},
    "f21_rgdc_015_rev_yoy_pct_8q_range": {"inputs": ["revenue"], "func": f21_rgdc_015_rev_yoy_pct_8q_range},
    "f21_rgdc_016_rev_yoy_pct_drop_from_8q_max": {"inputs": ["revenue"], "func": f21_rgdc_016_rev_yoy_pct_drop_from_8q_max},
    "f21_rgdc_017_rev_yoy_pct_recovery_from_8q_min": {"inputs": ["revenue"], "func": f21_rgdc_017_rev_yoy_pct_recovery_from_8q_min},
    "f21_rgdc_018_rev_yoy_pct_zscore_8q": {"inputs": ["revenue"], "func": f21_rgdc_018_rev_yoy_pct_zscore_8q},
    "f21_rgdc_019_rev_yoy_pct_zscore_12q": {"inputs": ["revenue"], "func": f21_rgdc_019_rev_yoy_pct_zscore_12q},
    "f21_rgdc_020_rev_growth_decay_proxy": {"inputs": ["revenue"], "func": f21_rgdc_020_rev_growth_decay_proxy},
    "f21_rgdc_021_rev_yoy_pct_4q_slope": {"inputs": ["revenue"], "func": f21_rgdc_021_rev_yoy_pct_4q_slope},
    "f21_rgdc_022_rev_yoy_pct_8q_slope": {"inputs": ["revenue"], "func": f21_rgdc_022_rev_yoy_pct_8q_slope},
    "f21_rgdc_023_rev_yoy_pct_12q_slope": {"inputs": ["revenue"], "func": f21_rgdc_023_rev_yoy_pct_12q_slope},
    "f21_rgdc_024_rev_qoq_pct_4q_slope": {"inputs": ["revenue"], "func": f21_rgdc_024_rev_qoq_pct_4q_slope},
    "f21_rgdc_025_rev_qoq_pct_8q_slope": {"inputs": ["revenue"], "func": f21_rgdc_025_rev_qoq_pct_8q_slope},
    "f21_rgdc_026_rev_ttm_4q_slope": {"inputs": ["revenue"], "func": f21_rgdc_026_rev_ttm_4q_slope},
    "f21_rgdc_027_rev_ttm_8q_slope": {"inputs": ["revenue"], "func": f21_rgdc_027_rev_ttm_8q_slope},
    "f21_rgdc_028_rev_yoy_pct_4q_negative_streak": {"inputs": ["revenue"], "func": f21_rgdc_028_rev_yoy_pct_4q_negative_streak},
    "f21_rgdc_029_rev_yoy_pct_below_5pct_count_4q": {"inputs": ["revenue"], "func": f21_rgdc_029_rev_yoy_pct_below_5pct_count_4q},
    "f21_rgdc_030_rev_yoy_pct_below_5pct_count_8q": {"inputs": ["revenue"], "func": f21_rgdc_030_rev_yoy_pct_below_5pct_count_8q},
    "f21_rgdc_031_rev_yoy_pct_consec_decel_streak": {"inputs": ["revenue"], "func": f21_rgdc_031_rev_yoy_pct_consec_decel_streak},
    "f21_rgdc_032_rev_qoq_pct_consec_negative_streak": {"inputs": ["revenue"], "func": f21_rgdc_032_rev_qoq_pct_consec_negative_streak},
    "f21_rgdc_033_rev_yoy_pct_max_consec_decel_8q": {"inputs": ["revenue"], "func": f21_rgdc_033_rev_yoy_pct_max_consec_decel_8q},
    "f21_rgdc_034_rev_yoy_pct_acceleration": {"inputs": ["revenue"], "func": f21_rgdc_034_rev_yoy_pct_acceleration},
    "f21_rgdc_035_rev_yoy_pct_jerk": {"inputs": ["revenue"], "func": f21_rgdc_035_rev_yoy_pct_jerk},
    "f21_rgdc_036_rev_yoy_pct_4q_mean": {"inputs": ["revenue"], "func": f21_rgdc_036_rev_yoy_pct_4q_mean},
    "f21_rgdc_037_rev_yoy_pct_8q_mean": {"inputs": ["revenue"], "func": f21_rgdc_037_rev_yoy_pct_8q_mean},
    "f21_rgdc_038_rev_yoy_pct_12q_mean": {"inputs": ["revenue"], "func": f21_rgdc_038_rev_yoy_pct_12q_mean},
    "f21_rgdc_039_rev_yoy_pct_4q_vs_8q_mean_diff": {"inputs": ["revenue"], "func": f21_rgdc_039_rev_yoy_pct_4q_vs_8q_mean_diff},
    "f21_rgdc_040_rev_yoy_pct_8q_vs_12q_mean_diff": {"inputs": ["revenue"], "func": f21_rgdc_040_rev_yoy_pct_8q_vs_12q_mean_diff},
    "f21_rgdc_041_rev_3y_cagr_minus_1y_yoy": {"inputs": ["revenue"], "func": f21_rgdc_041_rev_3y_cagr_minus_1y_yoy},
    "f21_rgdc_042_rev_5y_cagr_minus_1y_yoy": {"inputs": ["revenue"], "func": f21_rgdc_042_rev_5y_cagr_minus_1y_yoy},
    "f21_rgdc_043_rev_2y_cagr_minus_1y_yoy": {"inputs": ["revenue"], "func": f21_rgdc_043_rev_2y_cagr_minus_1y_yoy},
    "f21_rgdc_044_rev_3y_cagr_minus_2y_cagr": {"inputs": ["revenue"], "func": f21_rgdc_044_rev_3y_cagr_minus_2y_cagr},
    "f21_rgdc_045_rev_5y_cagr_minus_3y_cagr": {"inputs": ["revenue"], "func": f21_rgdc_045_rev_5y_cagr_minus_3y_cagr},
    "f21_rgdc_046_rev_growth_term_structure_slope": {"inputs": ["revenue"], "func": f21_rgdc_046_rev_growth_term_structure_slope},
    "f21_rgdc_047_rev_growth_inversion_signal_5pt": {"inputs": ["revenue"], "func": f21_rgdc_047_rev_growth_inversion_signal_5pt},
    "f21_rgdc_048_rev_growth_inversion_signal_10pt": {"inputs": ["revenue"], "func": f21_rgdc_048_rev_growth_inversion_signal_10pt},
    "f21_rgdc_049_rev_yoy_below_3y_cagr_count_8q": {"inputs": ["revenue"], "func": f21_rgdc_049_rev_yoy_below_3y_cagr_count_8q},
    "f21_rgdc_050_rev_yoy_below_5y_cagr_count_8q": {"inputs": ["revenue"], "func": f21_rgdc_050_rev_yoy_below_5y_cagr_count_8q},
    "f21_rgdc_051_rev_growth_rolloff_rate_4q": {"inputs": ["revenue"], "func": f21_rgdc_051_rev_growth_rolloff_rate_4q},
    "f21_rgdc_052_rev_growth_rolloff_rate_8q": {"inputs": ["revenue"], "func": f21_rgdc_052_rev_growth_rolloff_rate_8q},
    "f21_rgdc_053_rev_growth_rolloff_rate_12q": {"inputs": ["revenue"], "func": f21_rgdc_053_rev_growth_rolloff_rate_12q},
    "f21_rgdc_054_rev_4q_geomean_growth": {"inputs": ["revenue"], "func": f21_rgdc_054_rev_4q_geomean_growth},
    "f21_rgdc_055_rev_8q_geomean_growth": {"inputs": ["revenue"], "func": f21_rgdc_055_rev_8q_geomean_growth},
    "f21_rgdc_056_rev_4q_geomean_minus_8q_geomean": {"inputs": ["revenue"], "func": f21_rgdc_056_rev_4q_geomean_minus_8q_geomean},
    "f21_rgdc_057_rev_8q_geomean_minus_12q_geomean": {"inputs": ["revenue"], "func": f21_rgdc_057_rev_8q_geomean_minus_12q_geomean},
    "f21_rgdc_058_rev_seasonal_2y_yoy_pct": {"inputs": ["revenue"], "func": f21_rgdc_058_rev_seasonal_2y_yoy_pct},
    "f21_rgdc_059_rev_seasonal_yoy_4q_mean": {"inputs": ["revenue"], "func": f21_rgdc_059_rev_seasonal_yoy_4q_mean},
    "f21_rgdc_060_rev_seasonal_yoy_acceleration": {"inputs": ["revenue"], "func": f21_rgdc_060_rev_seasonal_yoy_acceleration},
    "f21_rgdc_061_rev_qoq_pct_std_4q": {"inputs": ["revenue"], "func": f21_rgdc_061_rev_qoq_pct_std_4q},
    "f21_rgdc_062_rev_qoq_pct_std_8q": {"inputs": ["revenue"], "func": f21_rgdc_062_rev_qoq_pct_std_8q},
    "f21_rgdc_063_rev_yoy_pct_std_8q": {"inputs": ["revenue"], "func": f21_rgdc_063_rev_yoy_pct_std_8q},
    "f21_rgdc_064_rev_yoy_pct_std_12q": {"inputs": ["revenue"], "func": f21_rgdc_064_rev_yoy_pct_std_12q},
    "f21_rgdc_065_rev_growth_coefvar_8q": {"inputs": ["revenue"], "func": f21_rgdc_065_rev_growth_coefvar_8q},
    "f21_rgdc_066_rev_qoq_negative_fraction_8q": {"inputs": ["revenue"], "func": f21_rgdc_066_rev_qoq_negative_fraction_8q},
    "f21_rgdc_067_rev_qoq_negative_fraction_12q": {"inputs": ["revenue"], "func": f21_rgdc_067_rev_qoq_negative_fraction_12q},
    "f21_rgdc_068_rev_yoy_negative_fraction_8q": {"inputs": ["revenue"], "func": f21_rgdc_068_rev_yoy_negative_fraction_8q},
    "f21_rgdc_069_rev_yoy_negative_fraction_12q": {"inputs": ["revenue"], "func": f21_rgdc_069_rev_yoy_negative_fraction_12q},
    "f21_rgdc_070_rev_growth_skewness_8q": {"inputs": ["revenue"], "func": f21_rgdc_070_rev_growth_skewness_8q},
    "f21_rgdc_071_rev_growth_kurtosis_8q": {"inputs": ["revenue"], "func": f21_rgdc_071_rev_growth_kurtosis_8q},
    "f21_rgdc_072_rev_growth_max_drawdown_4q": {"inputs": ["revenue"], "func": f21_rgdc_072_rev_growth_max_drawdown_4q},
    "f21_rgdc_073_rev_growth_max_drawdown_8q": {"inputs": ["revenue"], "func": f21_rgdc_073_rev_growth_max_drawdown_8q},
    "f21_rgdc_074_rev_growth_max_drawdown_12q": {"inputs": ["revenue"], "func": f21_rgdc_074_rev_growth_max_drawdown_12q},
    "f21_rgdc_075_rev_growth_choppiness_8q": {"inputs": ["revenue"], "func": f21_rgdc_075_rev_growth_choppiness_8q},
}
