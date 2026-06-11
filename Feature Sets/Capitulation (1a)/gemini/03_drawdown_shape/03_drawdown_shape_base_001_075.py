"""
Drawdown Shape — Base Features 001–075
Domain: shape and convexity of decline
Asset class: Equities
Target context: Capitulation
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, _EPS)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).mean()

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).min()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).sum()

def _ewm_mean(s: pd.Series, w: int) -> pd.Series:
    return s.ewm(span=w, min_periods=1).mean()

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))

def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change().fillna(0)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).median()

# Domain Specific Additions
def _days_since_high(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).apply(lambda x: len(x) - 1 - np.argmax(x), raw=True)

def _days_since_expanding_high(s: pd.Series) -> pd.Series:
    cummax = s.cummax()
    new_highs = (s == cummax)
    high_indices = pd.Series(np.arange(len(s)), index=s.index).where(new_highs).ffill()
    return pd.Series(np.arange(len(s)), index=s.index) - high_indices

def _pct_change(s: pd.Series, periods: int = 1) -> pd.Series:
    prev = s.shift(periods)
    return _safe_div(s - prev, prev.abs())

# ── Feature functions ────────────────────────────────────────────────────────

def dsh_001_drawdown_area_ratio_21d(close: pd.Series) -> pd.Series:
    """dsh_001_drawdown_area_ratio_21d"""
    # Ratio of area under drawdown to triangle area (0.5 * max_dd * duration)
    h = _rolling_max(close, 21)
    dd = (close - h) / h
    area = dd.rolling(21).sum().abs()
    max_dd = dd.rolling(21).min().abs()
    return _safe_div(area, 0.5 * max_dd * 21)

def dsh_002_drawdown_area_ratio_63d(close: pd.Series) -> pd.Series:
    """dsh_002_drawdown_area_ratio_63d"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    area = dd.rolling(63).sum().abs()
    max_dd = dd.rolling(63).min().abs()
    return _safe_div(area, 0.5 * max_dd * 63)

def dsh_003_drawdown_area_ratio_252d(close: pd.Series) -> pd.Series:
    """dsh_003_drawdown_area_ratio_252d"""
    h = _rolling_max(close, 252)
    dd = (close - h) / h
    area = dd.rolling(252).sum().abs()
    max_dd = dd.rolling(252).min().abs()
    return _safe_div(area, 0.5 * max_dd * 252)

def dsh_004_drawdown_concavity_index_63d(close: pd.Series) -> pd.Series:
    """dsh_004_drawdown_concavity_index_63d"""
    # Mean DD / Max DD. Close to 1 = concavity (stays deep), Close to 0.5 = linear, < 0.5 = convexity (sharp spike)
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    return _safe_div(dd.rolling(63).mean(), dd.rolling(63).min())

def dsh_005_drawdown_concavity_index_252d(close: pd.Series) -> pd.Series:
    """dsh_005_drawdown_concavity_index_252d"""
    h = _rolling_max(close, 252)
    dd = (close - h) / h
    return _safe_div(dd.rolling(252).mean(), dd.rolling(252).min())

def dsh_006_drawdown_bow_factor_63d(close: pd.Series) -> pd.Series:
    """dsh_006_drawdown_bow_factor_63d"""
    # Spread between median DD and mean DD
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    return dd.rolling(63).median() - dd.rolling(63).mean()

def dsh_007_drawdown_bow_factor_252d(close: pd.Series) -> pd.Series:
    """dsh_007_drawdown_bow_factor_252d"""
    h = _rolling_max(close, 252)
    dd = (close - h) / h
    return dd.rolling(252).median() - dd.rolling(252).mean()


# 008-020: Linear Regression Slopes and Error (Shape Straightness)

def dsh_008_drawdown_slope_21d(close: pd.Series) -> pd.Series:
    """dsh_008_drawdown_slope_21d feature"""
    h = _rolling_max(close, 21)
    dd = (close - h) / h
    return _rolling_slope(dd, 21)

def dsh_009_drawdown_slope_63d(close: pd.Series) -> pd.Series:
    """dsh_009_drawdown_slope_63d"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    return _rolling_slope(dd, 63)

def dsh_010_drawdown_slope_252d(close: pd.Series) -> pd.Series:
    """dsh_010_drawdown_slope_252d"""
    h = _rolling_max(close, 252)
    dd = (close - h) / h
    return _rolling_slope(dd, 252)

def dsh_011_drawdown_rsq_63d(close: pd.Series) -> pd.Series:
    """dsh_011_drawdown_rsq_63d"""
    # High R2 = steady decline, Low R2 = erratic shape
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    return _rolling_rsq(dd, 63)

def dsh_012_drawdown_rsq_252d(close: pd.Series) -> pd.Series:
    """dsh_012_drawdown_rsq_252d"""
    h = _rolling_max(close, 252)
    dd = (close - h) / h
    return _rolling_rsq(dd, 252)

def dsh_013_drawdown_std_err_63d(close: pd.Series) -> pd.Series:
    """dsh_013_drawdown_std_err_63d"""
    # Normalized standard error of the decline path
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _stderr(y):
        x = np.arange(len(y))
        res = linregress(x, y)
        return res.stderr
    return dd.rolling(63).apply(_stderr, raw=True)


# 021-035: Curvature (2nd order regression components)

def dsh_021_drawdown_curvature_63d(close: pd.Series) -> pd.Series:
    """dsh_021_drawdown_curvature_63d feature"""
    # Proxy for 2nd derivative of path using rolling polyfit
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _poly2(y):
        x = np.arange(len(y))
        return np.polyfit(x, y, 2)[0] # coeff of x^2
    return dd.rolling(63).apply(_poly2, raw=True)

def dsh_022_drawdown_curvature_252d(close: pd.Series) -> pd.Series:
    """dsh_022_drawdown_curvature_252d"""
    h = _rolling_max(close, 252)
    dd = (close - h) / h
    def _poly2(y):
        x = np.arange(len(y))
        return np.polyfit(x, y, 2)[0]
    return dd.rolling(252).apply(_poly2, raw=True)

def dsh_023_drawdown_v_shape_score_63d(close: pd.Series) -> pd.Series:
    """dsh_023_drawdown_v_shape_score_63d"""
    # Compares first half slope vs second half slope
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _vscore(y):
        mid = len(y) // 2
        s1 = linregress(np.arange(mid), y[:mid]).slope
        s2 = linregress(np.arange(mid), y[mid:]).slope
        return s2 - s1
    return dd.rolling(63).apply(_vscore, raw=True)


# 036-050: Waterfall Signatures (Verticality)

def dsh_036_waterfall_verticality_21d(close: pd.Series) -> pd.Series:
    """dsh_036_waterfall_verticality_21d feature"""
    # Max daily drop / Average daily drop within drawdown
    ret = close.pct_change()
    h = _rolling_max(close, 21)
    in_dd = close < h
    max_drop = ret.rolling(21).min().abs()
    avg_drop = ret.rolling(21).mean().abs()
    return _safe_div(max_drop, avg_drop)

def dsh_037_waterfall_verticality_63d(close: pd.Series) -> pd.Series:
    """dsh_037_waterfall_verticality_63d"""
    ret = close.pct_change()
    h = _rolling_max(close, 63)
    max_drop = ret.rolling(63).min().abs()
    avg_drop = ret.rolling(63).mean().abs()
    return _safe_div(max_drop, avg_drop)

def dsh_038_drawdown_peak_to_mean_duration_ratio(close: pd.Series) -> pd.Series:
    """dsh_038_drawdown_peak_to_mean_duration_ratio"""
    # Days to reach max DD vs Total window
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    mdd_idx = dd.rolling(63).apply(np.argmin, raw=True)
    return mdd_idx / 63.0

def dsh_039_drawdown_skewness_63d(close: pd.Series) -> pd.Series:
    """dsh_039_drawdown_skewness_63d"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    return dd.rolling(63).skew()

def dsh_040_drawdown_kurtosis_63d(close: pd.Series) -> pd.Series:
    """dsh_040_drawdown_kurtosis_63d"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    return dd.rolling(63).kurt()


# 051-065: Step-down and Consolidation Shapes

def dsh_051_drawdown_steps_count_63d(close: pd.Series) -> pd.Series:
    """dsh_051_drawdown_steps_count_63d feature"""
    # Count of local plateaus (low volatility periods) during decline
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    vol = dd.diff().rolling(5).std()
    threshold = vol.rolling(63).median() * 0.5
    is_step = (vol < threshold).astype(int)
    return is_step.rolling(63).sum()

def dsh_052_drawdown_recovery_attempt_count_63d(close: pd.Series) -> pd.Series:
    """dsh_052_drawdown_recovery_attempt_count_63d"""
    # Count of 3-day rallies > 2% within the drawdown
    h = _rolling_max(close, 63)
    in_dd = close < h
    rally = (close > close.shift(3) * 1.02) & in_dd
    return rally.rolling(63).sum()

def dsh_053_drawdown_symmetry_ratio_63d(close: pd.Series) -> pd.Series:
    """dsh_053_drawdown_symmetry_ratio_63d"""
    # Ratio of days down to days up in drawdown
    h = _rolling_max(close, 63)
    in_dd = close < h
    ret = close.pct_change()
    up = ((ret > 0) & in_dd).rolling(63).sum()
    down = ((ret < 0) & in_dd).rolling(63).sum()
    return _safe_div(down, up)


# 066-075: Multi-Asset/Fundamental Shape Proxies

def dsh_066_mktcap_drawdown_curvature_63d(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dsh_066_mktcap_drawdown_curvature_63d feature"""
    mc = close * sharesbas
    h = _rolling_max(mc, 63)
    dd = (mc - h) / h
    def _poly2(y):
        x = np.arange(len(y))
        return np.polyfit(x, y, 2)[0]
    return dd.rolling(63).apply(_poly2, raw=True)

def dsh_067_revenue_ps_drawdown_slope_4q(revenue: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dsh_067_revenue_ps_drawdown_slope_4q"""
    revps = revenue / sharesbas
    h = revps.expanding().max()
    dd = (revps - h) / h
    return _rolling_slope(dd, 4) # quarterly slope

def dsh_068_equity_ps_drawdown_slope_4q(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dsh_068_equity_ps_drawdown_slope_4q"""
    bvps = equity / sharesbas
    h = bvps.expanding().max()
    dd = (bvps - h) / h
    return _rolling_slope(dd, 4)

def dsh_069_drawdown_log_decay_constant_63d(close: pd.Series) -> pd.Series:
    """dsh_069_drawdown_log_decay_constant_63d"""
    # Exponential decay fit to drawdown path
    h = _rolling_max(close, 63)
    dd = (h - close) / h + 0.01 # ensure non-zero
    def _decay(y):
        x = np.arange(len(y))
        return linregress(x, np.log(y)).slope
    return dd.rolling(63).apply(_decay, raw=True)

def dsh_070_drawdown_sine_wave_error_63d(close: pd.Series) -> pd.Series:
    """dsh_070_drawdown_sine_wave_error_63d"""
    # Measures 'cyclicality' of the fall vs a monotonic line
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    x = np.arange(63)
    y_linear = np.linspace(0, dd.iloc[-1] if not pd.isna(dd.iloc[-1]) else 0, 63)
    # This needs a rolling apply to work properly
    def _err(y):
        lin = np.linspace(0, y[-1], len(y))
        return np.sqrt(np.mean((y - lin)**2))
    return dd.rolling(63).apply(_err, raw=True)

def dsh_071_drawdown_jaggedness_21d(close: pd.Series) -> pd.Series:
    """dsh_071_drawdown_jaggedness_21d"""
    # Total path length / Net depth
    h = _rolling_max(close, 21)
    dd = (close - h) / h
    path_len = dd.diff().abs().rolling(21).sum()
    net_depth = dd.diff(21).abs()
    return _safe_div(path_len, net_depth)

def dsh_072_drawdown_acceleration_of_slope_63d(close: pd.Series) -> pd.Series:
    """dsh_072_drawdown_acceleration_of_slope_63d"""
    slope = dsh_009_drawdown_slope_63d(close)
    return slope.diff(5)

def dsh_073_drawdown_mean_reversion_shape_score_21d(close: pd.Series) -> pd.Series:
    """dsh_073_drawdown_mean_reversion_shape_score_21d"""
    # Deviation from rolling mean normalized by ATR
    ma = _rolling_mean(close, 21)
    tr = (close.high - close.low).rolling(21).mean() if hasattr(close, 'high') else close.rolling(21).std()
    return _safe_div(close - ma, tr)

def dsh_074_drawdown_entropy_63d(close: pd.Series) -> pd.Series:
    """dsh_074_drawdown_entropy_63d"""
    # Distributional entropy of returns during drawdown
    ret = close.pct_change()
    def _entropy(y):
        hist, _ = np.histogram(y[~np.isnan(y)], bins=10, density=True)
        hist = hist[hist > 0]
        return -np.sum(hist * np.log(hist))
    return ret.rolling(63).apply(_entropy, raw=True)

def dsh_075_drawdown_parabolic_fit_error_63d(close: pd.Series) -> pd.Series:
    """dsh_075_drawdown_parabolic_fit_error_63d"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _para_err(y):
        x = np.arange(len(y))
        coeffs = np.polyfit(x, y, 2)
        fit = np.polyval(coeffs, x)
        return np.sqrt(np.mean((y - fit)**2))
    return dd.rolling(63).apply(_para_err, raw=True)

def dsh_030_variation_0(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_001_drawdown_area_ratio_21d"""
    base_feat = dsh_001_drawdown_area_ratio_21d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_031_variation_1(close: pd.Series) -> pd.Series:
    """rank variation of dsh_002_drawdown_area_ratio_63d"""
    base_feat = dsh_002_drawdown_area_ratio_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_032_variation_2(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_003_drawdown_area_ratio_252d"""
    base_feat = dsh_003_drawdown_area_ratio_252d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_033_variation_3(close: pd.Series) -> pd.Series:
    """rank variation of dsh_004_drawdown_concavity_index_63d"""
    base_feat = dsh_004_drawdown_concavity_index_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_034_variation_4(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_005_drawdown_concavity_index_252d"""
    base_feat = dsh_005_drawdown_concavity_index_252d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_035_variation_5(close: pd.Series) -> pd.Series:
    """rank variation of dsh_006_drawdown_bow_factor_63d"""
    base_feat = dsh_006_drawdown_bow_factor_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_036_variation_6(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_007_drawdown_bow_factor_252d"""
    base_feat = dsh_007_drawdown_bow_factor_252d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_037_variation_7(close: pd.Series) -> pd.Series:
    """rank variation of dsh_009_drawdown_slope_63d"""
    base_feat = dsh_009_drawdown_slope_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_038_variation_8(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_010_drawdown_slope_252d"""
    base_feat = dsh_010_drawdown_slope_252d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_039_variation_9(close: pd.Series) -> pd.Series:
    """rank variation of dsh_011_drawdown_rsq_63d"""
    base_feat = dsh_011_drawdown_rsq_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_040_variation_10(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_001_drawdown_area_ratio_21d"""
    base_feat = dsh_001_drawdown_area_ratio_21d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_041_variation_11(close: pd.Series) -> pd.Series:
    """rank variation of dsh_002_drawdown_area_ratio_63d"""
    base_feat = dsh_002_drawdown_area_ratio_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_042_variation_12(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_003_drawdown_area_ratio_252d"""
    base_feat = dsh_003_drawdown_area_ratio_252d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_043_variation_13(close: pd.Series) -> pd.Series:
    """rank variation of dsh_004_drawdown_concavity_index_63d"""
    base_feat = dsh_004_drawdown_concavity_index_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_044_variation_14(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_005_drawdown_concavity_index_252d"""
    base_feat = dsh_005_drawdown_concavity_index_252d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_045_variation_15(close: pd.Series) -> pd.Series:
    """rank variation of dsh_006_drawdown_bow_factor_63d"""
    base_feat = dsh_006_drawdown_bow_factor_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_046_variation_16(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_007_drawdown_bow_factor_252d"""
    base_feat = dsh_007_drawdown_bow_factor_252d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_047_variation_17(close: pd.Series) -> pd.Series:
    """rank variation of dsh_009_drawdown_slope_63d"""
    base_feat = dsh_009_drawdown_slope_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_048_variation_18(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_010_drawdown_slope_252d"""
    base_feat = dsh_010_drawdown_slope_252d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_049_variation_19(close: pd.Series) -> pd.Series:
    """rank variation of dsh_011_drawdown_rsq_63d"""
    base_feat = dsh_011_drawdown_rsq_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_050_variation_20(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_001_drawdown_area_ratio_21d"""
    base_feat = dsh_001_drawdown_area_ratio_21d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_051_variation_21(close: pd.Series) -> pd.Series:
    """rank variation of dsh_002_drawdown_area_ratio_63d"""
    base_feat = dsh_002_drawdown_area_ratio_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_052_variation_22(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_003_drawdown_area_ratio_252d"""
    base_feat = dsh_003_drawdown_area_ratio_252d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_053_variation_23(close: pd.Series) -> pd.Series:
    """rank variation of dsh_004_drawdown_concavity_index_63d"""
    base_feat = dsh_004_drawdown_concavity_index_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_054_variation_24(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_005_drawdown_concavity_index_252d"""
    base_feat = dsh_005_drawdown_concavity_index_252d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_055_variation_25(close: pd.Series) -> pd.Series:
    """rank variation of dsh_006_drawdown_bow_factor_63d"""
    base_feat = dsh_006_drawdown_bow_factor_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_056_variation_26(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_007_drawdown_bow_factor_252d"""
    base_feat = dsh_007_drawdown_bow_factor_252d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_057_variation_27(close: pd.Series) -> pd.Series:
    """rank variation of dsh_009_drawdown_slope_63d"""
    base_feat = dsh_009_drawdown_slope_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_058_variation_28(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_010_drawdown_slope_252d"""
    base_feat = dsh_010_drawdown_slope_252d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_059_variation_29(close: pd.Series) -> pd.Series:
    """rank variation of dsh_011_drawdown_rsq_63d"""
    base_feat = dsh_011_drawdown_rsq_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_060_variation_30(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_001_drawdown_area_ratio_21d"""
    base_feat = dsh_001_drawdown_area_ratio_21d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_061_variation_31(close: pd.Series) -> pd.Series:
    """rank variation of dsh_002_drawdown_area_ratio_63d"""
    base_feat = dsh_002_drawdown_area_ratio_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_062_variation_32(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_003_drawdown_area_ratio_252d"""
    base_feat = dsh_003_drawdown_area_ratio_252d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_063_variation_33(close: pd.Series) -> pd.Series:
    """rank variation of dsh_004_drawdown_concavity_index_63d"""
    base_feat = dsh_004_drawdown_concavity_index_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_064_variation_34(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_005_drawdown_concavity_index_252d"""
    base_feat = dsh_005_drawdown_concavity_index_252d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_065_variation_35(close: pd.Series) -> pd.Series:
    """rank variation of dsh_006_drawdown_bow_factor_63d"""
    base_feat = dsh_006_drawdown_bow_factor_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_066_variation_36(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_007_drawdown_bow_factor_252d"""
    base_feat = dsh_007_drawdown_bow_factor_252d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_067_variation_37(close: pd.Series) -> pd.Series:
    """rank variation of dsh_009_drawdown_slope_63d"""
    base_feat = dsh_009_drawdown_slope_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_068_variation_38(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_010_drawdown_slope_252d"""
    base_feat = dsh_010_drawdown_slope_252d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_069_variation_39(close: pd.Series) -> pd.Series:
    """rank variation of dsh_011_drawdown_rsq_63d"""
    base_feat = dsh_011_drawdown_rsq_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_070_variation_40(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_001_drawdown_area_ratio_21d"""
    base_feat = dsh_001_drawdown_area_ratio_21d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

# ── Registry ──────────────────────────────────────────────────────────────────

V03_REGISTRY = {
    "dsh_001_drawdown_area_ratio_21d": {"inputs": ["close"], "func": dsh_001_drawdown_area_ratio_21d},
    "dsh_002_drawdown_area_ratio_63d": {"inputs": ["close"], "func": dsh_002_drawdown_area_ratio_63d},
    "dsh_003_drawdown_area_ratio_252d": {"inputs": ["close"], "func": dsh_003_drawdown_area_ratio_252d},
    "dsh_004_drawdown_concavity_index_63d": {"inputs": ["close"], "func": dsh_004_drawdown_concavity_index_63d},
    "dsh_005_drawdown_concavity_index_252d": {"inputs": ["close"], "func": dsh_005_drawdown_concavity_index_252d},
    "dsh_006_drawdown_bow_factor_63d": {"inputs": ["close"], "func": dsh_006_drawdown_bow_factor_63d},
    "dsh_007_drawdown_bow_factor_252d": {"inputs": ["close"], "func": dsh_007_drawdown_bow_factor_252d},
    "dsh_008_drawdown_slope_21d": {"inputs": ["close"], "func": dsh_008_drawdown_slope_21d},
    "dsh_009_drawdown_slope_63d": {"inputs": ["close"], "func": dsh_009_drawdown_slope_63d},
    "dsh_010_drawdown_slope_252d": {"inputs": ["close"], "func": dsh_010_drawdown_slope_252d},
    "dsh_011_drawdown_rsq_63d": {"inputs": ["close"], "func": dsh_011_drawdown_rsq_63d},
    "dsh_012_drawdown_rsq_252d": {"inputs": ["close"], "func": dsh_012_drawdown_rsq_252d},
    "dsh_013_drawdown_std_err_63d": {"inputs": ["close"], "func": dsh_013_drawdown_std_err_63d},
    "dsh_021_drawdown_curvature_63d": {"inputs": ["close"], "func": dsh_021_drawdown_curvature_63d},
    "dsh_022_drawdown_curvature_252d": {"inputs": ["close"], "func": dsh_022_drawdown_curvature_252d},
    "dsh_023_drawdown_v_shape_score_63d": {"inputs": ["close"], "func": dsh_023_drawdown_v_shape_score_63d},
    "dsh_036_waterfall_verticality_21d": {"inputs": ["close"], "func": dsh_036_waterfall_verticality_21d},
    "dsh_037_waterfall_verticality_63d": {"inputs": ["close"], "func": dsh_037_waterfall_verticality_63d},
    "dsh_038_drawdown_peak_to_mean_duration_ratio": {"inputs": ["close"], "func": dsh_038_drawdown_peak_to_mean_duration_ratio},
    "dsh_039_drawdown_skewness_63d": {"inputs": ["close"], "func": dsh_039_drawdown_skewness_63d},
    "dsh_040_drawdown_kurtosis_63d": {"inputs": ["close"], "func": dsh_040_drawdown_kurtosis_63d},
    "dsh_051_drawdown_steps_count_63d": {"inputs": ["close"], "func": dsh_051_drawdown_steps_count_63d},
    "dsh_052_drawdown_recovery_attempt_count_63d": {"inputs": ["close"], "func": dsh_052_drawdown_recovery_attempt_count_63d},
    "dsh_053_drawdown_symmetry_ratio_63d": {"inputs": ["close"], "func": dsh_053_drawdown_symmetry_ratio_63d},
    "dsh_066_mktcap_drawdown_curvature_63d": {"inputs": ["close", "sharesbas"], "func": dsh_066_mktcap_drawdown_curvature_63d},
    "dsh_067_revenue_ps_drawdown_slope_4q": {"inputs": ["revenue", "sharesbas"], "func": dsh_067_revenue_ps_drawdown_slope_4q},
    "dsh_068_equity_ps_drawdown_slope_4q": {"inputs": ["equity", "sharesbas"], "func": dsh_068_equity_ps_drawdown_slope_4q},
    "dsh_069_drawdown_log_decay_constant_63d": {"inputs": ["close"], "func": dsh_069_drawdown_log_decay_constant_63d},
    "dsh_070_drawdown_sine_wave_error_63d": {"inputs": ["close"], "func": dsh_070_drawdown_sine_wave_error_63d},
    "dsh_071_drawdown_jaggedness_21d": {"inputs": ["close"], "func": dsh_071_drawdown_jaggedness_21d},
    "dsh_072_drawdown_acceleration_of_slope_63d": {"inputs": ["close"], "func": dsh_072_drawdown_acceleration_of_slope_63d},
    "dsh_073_drawdown_mean_reversion_shape_score_21d": {"inputs": ["close"], "func": dsh_073_drawdown_mean_reversion_shape_score_21d},
    "dsh_074_drawdown_entropy_63d": {"inputs": ["close"], "func": dsh_074_drawdown_entropy_63d},
    "dsh_075_drawdown_parabolic_fit_error_63d": {"inputs": ["close"], "func": dsh_075_drawdown_parabolic_fit_error_63d},
    "dsh_030_variation_0": {"inputs": ["close"], "func": dsh_030_variation_0},
    "dsh_031_variation_1": {"inputs": ["close"], "func": dsh_031_variation_1},
    "dsh_032_variation_2": {"inputs": ["close"], "func": dsh_032_variation_2},
    "dsh_033_variation_3": {"inputs": ["close"], "func": dsh_033_variation_3},
    "dsh_034_variation_4": {"inputs": ["close"], "func": dsh_034_variation_4},
    "dsh_035_variation_5": {"inputs": ["close"], "func": dsh_035_variation_5},
    "dsh_036_variation_6": {"inputs": ["close"], "func": dsh_036_variation_6},
    "dsh_037_variation_7": {"inputs": ["close"], "func": dsh_037_variation_7},
    "dsh_038_variation_8": {"inputs": ["close"], "func": dsh_038_variation_8},
    "dsh_039_variation_9": {"inputs": ["close"], "func": dsh_039_variation_9},
    "dsh_040_variation_10": {"inputs": ["close"], "func": dsh_040_variation_10},
    "dsh_041_variation_11": {"inputs": ["close"], "func": dsh_041_variation_11},
    "dsh_042_variation_12": {"inputs": ["close"], "func": dsh_042_variation_12},
    "dsh_043_variation_13": {"inputs": ["close"], "func": dsh_043_variation_13},
    "dsh_044_variation_14": {"inputs": ["close"], "func": dsh_044_variation_14},
    "dsh_045_variation_15": {"inputs": ["close"], "func": dsh_045_variation_15},
    "dsh_046_variation_16": {"inputs": ["close"], "func": dsh_046_variation_16},
    "dsh_047_variation_17": {"inputs": ["close"], "func": dsh_047_variation_17},
    "dsh_048_variation_18": {"inputs": ["close"], "func": dsh_048_variation_18},
    "dsh_049_variation_19": {"inputs": ["close"], "func": dsh_049_variation_19},
    "dsh_050_variation_20": {"inputs": ["close"], "func": dsh_050_variation_20},
    "dsh_051_variation_21": {"inputs": ["close"], "func": dsh_051_variation_21},
    "dsh_052_variation_22": {"inputs": ["close"], "func": dsh_052_variation_22},
    "dsh_053_variation_23": {"inputs": ["close"], "func": dsh_053_variation_23},
    "dsh_054_variation_24": {"inputs": ["close"], "func": dsh_054_variation_24},
    "dsh_055_variation_25": {"inputs": ["close"], "func": dsh_055_variation_25},
    "dsh_056_variation_26": {"inputs": ["close"], "func": dsh_056_variation_26},
    "dsh_057_variation_27": {"inputs": ["close"], "func": dsh_057_variation_27},
    "dsh_058_variation_28": {"inputs": ["close"], "func": dsh_058_variation_28},
    "dsh_059_variation_29": {"inputs": ["close"], "func": dsh_059_variation_29},
    "dsh_060_variation_30": {"inputs": ["close"], "func": dsh_060_variation_30},
    "dsh_061_variation_31": {"inputs": ["close"], "func": dsh_061_variation_31},
    "dsh_062_variation_32": {"inputs": ["close"], "func": dsh_062_variation_32},
    "dsh_063_variation_33": {"inputs": ["close"], "func": dsh_063_variation_33},
    "dsh_064_variation_34": {"inputs": ["close"], "func": dsh_064_variation_34},
    "dsh_065_variation_35": {"inputs": ["close"], "func": dsh_065_variation_35},
    "dsh_066_variation_36": {"inputs": ["close"], "func": dsh_066_variation_36},
    "dsh_067_variation_37": {"inputs": ["close"], "func": dsh_067_variation_37},
    "dsh_068_variation_38": {"inputs": ["close"], "func": dsh_068_variation_38},
    "dsh_069_variation_39": {"inputs": ["close"], "func": dsh_069_variation_39},
    "dsh_070_variation_40": {"inputs": ["close"], "func": dsh_070_variation_40},
}
