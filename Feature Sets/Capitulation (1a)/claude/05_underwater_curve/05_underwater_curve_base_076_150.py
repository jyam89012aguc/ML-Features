"""
05_underwater_curve — Base Features 076-150
Domain: area and depth of the underwater equity curve (accumulated severity)
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _uw_rolling(close: pd.Series, w: int) -> pd.Series:
    """Underwater series vs rolling w-day peak: (close/peak - 1), <= 0."""
    peak = _rolling_max(close, w)
    return _safe_div(close - peak, peak)


def _uw_expanding(close: pd.Series) -> pd.Series:
    """Underwater series vs all-time expanding high: (close/ATH - 1), <= 0."""
    peak = close.expanding(min_periods=1).max()
    return _safe_div(close - peak, peak)


def _log_uw_rolling(close: pd.Series, w: int) -> pd.Series:
    """Log-space underwater: log(close/peak), <= 0."""
    peak = _rolling_max(close, w)
    return np.log((close / peak.replace(0, np.nan)).clip(lower=_EPS))


def _log_uw_expanding(close: pd.Series) -> pd.Series:
    """Log-space underwater vs ATH: log(close/ATH), <= 0."""
    peak = close.expanding(min_periods=1).max()
    return np.log((close / peak.replace(0, np.nan)).clip(lower=_EPS))


def _atr(high: pd.Series, low: pd.Series, close: pd.Series, w: int) -> pd.Series:
    """Average True Range over w days."""
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)
    return _rolling_mean(tr, w)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Z-score and percentile-rank of area metrics ---

def uw_076_area_252d_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of 252d underwater area over a 504-day trailing window."""
    area = _rolling_sum(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    m = area.rolling(504, min_periods=max(1, 252)).mean()
    s = area.rolling(504, min_periods=max(1, 252)).std()
    return _safe_div(area - m, s)


def uw_077_area_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63d underwater area over a 252-day trailing window."""
    area = _rolling_sum(_uw_rolling(close, _TD_QTR).abs(), _TD_QTR)
    m = area.rolling(_TD_YEAR, min_periods=max(1, _TD_QTR)).mean()
    s = area.rolling(_TD_YEAR, min_periods=max(1, _TD_QTR)).std()
    return _safe_div(area - m, s)


def uw_078_ulcer_index_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 252d Ulcer Index over trailing 504-day window."""
    uw = _uw_rolling(close, _TD_YEAR)
    ui = np.sqrt(_rolling_mean(uw ** 2, _TD_YEAR))
    m = ui.rolling(504, min_periods=max(1, 252)).mean()
    s = ui.rolling(504, min_periods=max(1, 252)).std()
    return _safe_div(ui - m, s)


def uw_079_pain_index_zscore_expanding(close: pd.Series) -> pd.Series:
    """Expanding z-score of 252d Pain Index vs all-history (extreme pain marker)."""
    pi = _rolling_mean(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    m = pi.expanding(min_periods=5).mean()
    s = pi.expanding(min_periods=5).std()
    return _safe_div(pi - m, s)


def uw_080_area_252d_pct_rank_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of 252d area within trailing 504-day window."""
    area = _rolling_sum(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    return area.rolling(504, min_periods=max(1, 252)).rank(pct=True)


def uw_081_pain_index_pct_rank_1260d(close: pd.Series) -> pd.Series:
    """Percentile rank of 252d Pain Index within trailing 1260-day window."""
    pi = _rolling_mean(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    return pi.rolling(1260, min_periods=max(1, 504)).rank(pct=True)


def uw_082_ulcer_index_pct_rank_1260d(close: pd.Series) -> pd.Series:
    """Percentile rank of 252d Ulcer Index within trailing 1260-day window."""
    uw = _uw_rolling(close, _TD_YEAR)
    ui = np.sqrt(_rolling_mean(uw ** 2, _TD_YEAR))
    return ui.rolling(1260, min_periods=max(1, 504)).rank(pct=True)


def uw_083_area_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252d area (all-history rank of current pain)."""
    area = _rolling_sum(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    return area.expanding(min_periods=5).rank(pct=True)


def uw_084_pain_index_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21d Pain Index within trailing 252-day window."""
    pi21 = _rolling_mean(_uw_rolling(close, _TD_MON).abs(), _TD_MON)
    m = pi21.rolling(_TD_YEAR, min_periods=max(1, _TD_QTR)).mean()
    s = pi21.rolling(_TD_YEAR, min_periods=max(1, _TD_QTR)).std()
    return _safe_div(pi21 - m, s)


def uw_085_area_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21d area within trailing 252-day window."""
    area21 = _rolling_sum(_uw_rolling(close, _TD_MON).abs(), _TD_MON)
    return area21.rolling(_TD_YEAR, min_periods=max(1, _TD_QTR)).rank(pct=True)


def uw_086_ulcer_index_252d_vs_63d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 252d Ulcer Index to 63d Ulcer Index (long-term vs short-term severity)."""
    ui252 = np.sqrt(_rolling_mean(_uw_rolling(close, _TD_YEAR) ** 2, _TD_YEAR))
    ui63 = np.sqrt(_rolling_mean(_uw_rolling(close, _TD_QTR) ** 2, _TD_QTR))
    return _safe_div(ui252, ui63 + _EPS)


def uw_087_area_504d_zscore_1260d(close: pd.Series) -> pd.Series:
    """Z-score of 504d area within trailing 1260-day window."""
    area = _rolling_sum(_uw_rolling(close, 504).abs(), 504)
    m = area.rolling(1260, min_periods=max(1, 504)).mean()
    s = area.rolling(1260, min_periods=max(1, 504)).std()
    return _safe_div(area - m, s)


def uw_088_uw_dispersion_ratio_252d_vs_63d(close: pd.Series) -> pd.Series:
    """Ratio of 252d depth std to 63d depth std (widening or narrowing pain range)."""
    std252 = _rolling_std(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    std63 = _rolling_std(_uw_rolling(close, _TD_QTR).abs(), _TD_QTR)
    return _safe_div(std252, std63 + _EPS)


def uw_089_pain_index_504d_zscore_expanding(close: pd.Series) -> pd.Series:
    """Expanding z-score of 504d Pain Index."""
    pi504 = _rolling_mean(_uw_rolling(close, 504).abs(), 504)
    m = pi504.expanding(min_periods=5).mean()
    s = pi504.expanding(min_periods=5).std()
    return _safe_div(pi504 - m, s)


def uw_090_ulcer_252d_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252d Ulcer Index."""
    ui = np.sqrt(_rolling_mean(_uw_rolling(close, _TD_YEAR) ** 2, _TD_YEAR))
    return ui.expanding(min_periods=5).rank(pct=True)


# --- Group G (091-105): Composite pain metrics and multi-scale blends ---

def uw_091_composite_pain_score_equal_weighted(close: pd.Series) -> pd.Series:
    """Equal-weight composite: avg of 21d, 63d, 252d Pain Indices."""
    pi21 = _rolling_mean(_uw_rolling(close, _TD_MON).abs(), _TD_MON)
    pi63 = _rolling_mean(_uw_rolling(close, _TD_QTR).abs(), _TD_QTR)
    pi252 = _rolling_mean(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    return (pi21 + pi63 + pi252) / 3.0


def uw_092_composite_pain_score_decay_weighted(close: pd.Series) -> pd.Series:
    """Decay-weighted composite: 50% 21d + 30% 63d + 20% 252d Pain Indices."""
    pi21 = _rolling_mean(_uw_rolling(close, _TD_MON).abs(), _TD_MON)
    pi63 = _rolling_mean(_uw_rolling(close, _TD_QTR).abs(), _TD_QTR)
    pi252 = _rolling_mean(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    return 0.50 * pi21 + 0.30 * pi63 + 0.20 * pi252


def uw_093_composite_ulcer_score(close: pd.Series) -> pd.Series:
    """Equal-weight composite of 63d, 252d, 504d Ulcer Indices."""
    ui63 = np.sqrt(_rolling_mean(_uw_rolling(close, _TD_QTR) ** 2, _TD_QTR))
    ui252 = np.sqrt(_rolling_mean(_uw_rolling(close, _TD_YEAR) ** 2, _TD_YEAR))
    ui504 = np.sqrt(_rolling_mean(_uw_rolling(close, 504) ** 2, 504))
    return (ui63 + ui252 + ui504) / 3.0


def uw_094_composite_area_score(close: pd.Series) -> pd.Series:
    """Normalized composite: sum of normalized 63d, 252d, 504d areas."""
    a63 = _rolling_sum(_uw_rolling(close, _TD_QTR).abs(), _TD_QTR) / _TD_QTR
    a252 = _rolling_sum(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR) / _TD_YEAR
    a504 = _rolling_sum(_uw_rolling(close, 504).abs(), 504) / 504
    return (a63 + a252 + a504) / 3.0


def uw_095_pain_ulcer_geometric_mean_252d(close: pd.Series) -> pd.Series:
    """Geometric mean of Pain Index and Ulcer Index over 252d."""
    pi = _rolling_mean(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    ui = np.sqrt(_rolling_mean(_uw_rolling(close, _TD_YEAR) ** 2, _TD_YEAR))
    return np.sqrt((pi * ui).clip(lower=0))


def uw_096_area_weighted_by_depth_severity_252d(close: pd.Series) -> pd.Series:
    """Depth-squared weighted area: sum(depth^2) over 252d (penalizes extreme events more)."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    return _rolling_sum(uw ** 2, _TD_YEAR)


def uw_097_area_weighted_by_depth_severity_63d(close: pd.Series) -> pd.Series:
    """Depth-squared weighted area over 63d."""
    uw = _uw_rolling(close, _TD_QTR).abs()
    return _rolling_sum(uw ** 2, _TD_QTR)


def uw_098_cube_root_area_252d(close: pd.Series) -> pd.Series:
    """Cube root of 252d area (compression of outliers, stable scale)."""
    area = _rolling_sum(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    return np.cbrt(area)


def uw_099_square_root_ulcer_252d(close: pd.Series) -> pd.Series:
    """Square root of Ulcer Index over 252d (further compression)."""
    ui = np.sqrt(_rolling_mean(_uw_rolling(close, _TD_YEAR) ** 2, _TD_YEAR))
    return np.sqrt(ui.clip(lower=0))


def uw_100_log1p_area_252d(close: pd.Series) -> pd.Series:
    """log(1 + 252d area): log-scale pain measure."""
    area = _rolling_sum(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    return np.log1p(area)


def uw_101_log1p_area_63d(close: pd.Series) -> pd.Series:
    """log(1 + 63d area): log-scale pain measure."""
    area = _rolling_sum(_uw_rolling(close, _TD_QTR).abs(), _TD_QTR)
    return np.log1p(area)


def uw_102_log1p_area_ath(close: pd.Series) -> pd.Series:
    """log(1 + ATH expanding area): log-scale all-time pain."""
    area = _uw_expanding(close).abs().expanding(min_periods=1).sum()
    return np.log1p(area)


def uw_103_area_acceleration_63d(close: pd.Series) -> pd.Series:
    """Second difference of 63d area: acceleration of pain accumulation."""
    area = _rolling_sum(_uw_rolling(close, _TD_QTR).abs(), _TD_QTR)
    return area.diff(5).diff(5)


def uw_104_area_acceleration_252d(close: pd.Series) -> pd.Series:
    """Second difference of 252d area: acceleration of annual pain."""
    area = _rolling_sum(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    return area.diff(_TD_MON).diff(_TD_MON)


def uw_105_pain_momentum_63d(close: pd.Series) -> pd.Series:
    """Rate of change in 63d Pain Index over 21 days (pain momentum)."""
    pi = _rolling_mean(_uw_rolling(close, _TD_QTR).abs(), _TD_QTR)
    return pi.diff(_TD_MON)


# --- Group H (106-120): Volume and high/low panel features ---

def uw_106_hl_spread_weighted_area_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Underwater area where each day's depth is weighted by its intraday range."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    hl_ratio = _safe_div(high - low, close)
    return _rolling_sum(uw * hl_ratio, _TD_YEAR)


def uw_107_low_based_uw_area_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday-low-based underwater area: low vs 63-day high-of-lows."""
    peak_low = _rolling_max(low, _TD_QTR)
    uw_low = _safe_div(low - peak_low, peak_low).abs()
    return _rolling_sum(uw_low, _TD_QTR)


def uw_108_low_based_uw_area_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday-low-based underwater area vs 252-day peak-of-lows."""
    peak_low = _rolling_max(low, _TD_YEAR)
    uw_low = _safe_div(low - peak_low, peak_low).abs()
    return _rolling_sum(uw_low, _TD_YEAR)


def uw_109_open_based_uw_area_252d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Open-price-based underwater area: open vs 252-day peak close."""
    peak = _rolling_max(close, _TD_YEAR)
    uw_open = _safe_div(open_ - peak, peak).abs()
    return _rolling_sum(uw_open, _TD_YEAR)


def uw_110_volume_surge_uw_area_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Area on days where volume is 2+ stddev above mean, weighted by depth."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    std_vol = _rolling_std(volume, _TD_YEAR)
    surge = (volume > avg_vol + 2 * std_vol).astype(float)
    return _rolling_sum(uw * surge, _TD_YEAR)


def uw_111_atr_normalized_uw_area_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63d underwater area normalized by ATR (pain per unit of volatility)."""
    area = _rolling_sum(_uw_rolling(close, _TD_QTR).abs(), _TD_QTR)
    atr63 = _atr(high, low, close, _TD_QTR)
    return _safe_div(area, atr63 + _EPS)


def uw_112_atr_normalized_uw_area_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252d underwater area normalized by ATR."""
    area = _rolling_sum(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    atr252 = _atr(high, low, close, _TD_YEAR)
    return _safe_div(area, atr252 + _EPS)


def uw_113_volume_decline_uw_area_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Underwater area on days with volume below 50-day avg (dry-volume capitulation signal)."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    avg_vol = _rolling_mean(volume, 50)
    low_vol_day = (volume < avg_vol).astype(float)
    return _rolling_sum(uw * low_vol_day, _TD_YEAR)


def uw_114_down_day_uw_area_63d(close: pd.Series) -> pd.Series:
    """Underwater area on down-price days only over 63d (pain from declines)."""
    uw = _uw_rolling(close, _TD_QTR).abs()
    down = (close.pct_change() < 0).astype(float)
    return _rolling_sum(uw * down, _TD_QTR)


def uw_115_up_day_uw_area_63d(close: pd.Series) -> pd.Series:
    """Underwater area on up-price days over 63d (residual pain despite bounces)."""
    uw = _uw_rolling(close, _TD_QTR).abs()
    up = (close.pct_change() > 0).astype(float)
    return _rolling_sum(uw * up, _TD_QTR)


def uw_116_down_vs_up_uw_area_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of down-day uw area to up-day uw area over 63d (pain asymmetry)."""
    uw = _uw_rolling(close, _TD_QTR).abs()
    ret = close.pct_change()
    down = (ret < 0).astype(float)
    up = (ret > 0).astype(float)
    down_area = _rolling_sum(uw * down, _TD_QTR)
    up_area = _rolling_sum(uw * up, _TD_QTR)
    return _safe_div(down_area, up_area + _EPS)


def uw_117_high_peak_vs_close_uw_diff_area_252d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Difference in area: intraday-high-based vs close-based underwater over 252d."""
    peak_high = _rolling_max(high, _TD_YEAR)
    peak_close = _rolling_max(close, _TD_YEAR)
    uw_high = _safe_div(close - peak_high, peak_high).abs()
    uw_close = _safe_div(close - peak_close, peak_close).abs()
    diff = uw_high - uw_close
    return _rolling_sum(diff, _TD_YEAR)


def uw_118_volume_weighted_ulcer_index_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted Ulcer Index: sqrt(mean(vol_norm * depth^2)) over 252d."""
    uw = _uw_rolling(close, _TD_YEAR)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    v_norm = _safe_div(volume, avg_vol + _EPS)
    return np.sqrt(_rolling_mean(v_norm * uw ** 2, _TD_YEAR))


def uw_119_high_volume_pain_concentration_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of volume-weighted area attributable to top-10% volume days over 252d."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    vol_thresh = volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.90)
    high_vol_flag = (volume >= vol_thresh).astype(float)
    total_area = _rolling_sum(uw, _TD_YEAR)
    top_area = _rolling_sum(uw * high_vol_flag, _TD_YEAR)
    return _safe_div(top_area, total_area + _EPS)


def uw_120_pain_ratio_open_to_close_252d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Ratio of open-based area to close-based area over 252d (gap-open pain)."""
    peak = _rolling_max(close, _TD_YEAR)
    uw_open = _safe_div(open_ - peak, peak).abs()
    uw_close = _safe_div(close - peak, peak).abs()
    open_area = _rolling_sum(uw_open, _TD_YEAR)
    close_area = _rolling_sum(uw_close, _TD_YEAR)
    return _safe_div(open_area, close_area + _EPS)


# --- Group I (121-135): Tail, threshold, and advanced shape metrics ---

def uw_121_uw_tail_area_q90_252d(close: pd.Series) -> pd.Series:
    """Area contributed by days with depth in top 10% over 252d (tail concentration)."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    q90 = uw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.90)
    return _rolling_sum(uw.where(uw >= q90, 0.0), _TD_YEAR)


def uw_122_uw_tail_concentration_ratio_252d(close: pd.Series) -> pd.Series:
    """Fraction of total area from top-10% deepest days over 252d."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    q90 = uw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.90)
    tail_area = _rolling_sum(uw.where(uw >= q90, 0.0), _TD_YEAR)
    total_area = _rolling_sum(uw, _TD_YEAR)
    return _safe_div(tail_area, total_area + _EPS)


def uw_123_uw_gini_coefficient_63d(close: pd.Series) -> pd.Series:
    """Gini coefficient of underwater depths over 63d (inequality of pain distribution)."""
    uw = _uw_rolling(close, _TD_QTR).abs()
    def _gini(y: np.ndarray) -> float:
        y = np.sort(y[~np.isnan(y)])
        n = len(y)
        if n < 2 or y.sum() < _EPS:
            return 0.0
        idx = np.arange(1, n + 1, dtype=float)
        return float((2.0 * np.sum(idx * y) / (n * y.sum())) - (n + 1.0) / n)
    return uw.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_gini, raw=True)


def uw_124_uw_gini_coefficient_252d(close: pd.Series) -> pd.Series:
    """Gini coefficient of underwater depths over 252d."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    def _gini(y: np.ndarray) -> float:
        y = np.sort(y[~np.isnan(y)])
        n = len(y)
        if n < 2 or y.sum() < _EPS:
            return 0.0
        idx = np.arange(1, n + 1, dtype=float)
        return float((2.0 * np.sum(idx * y) / (n * y.sum())) - (n + 1.0) / n)
    return uw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_gini, raw=True)


def uw_125_uw_days_above_mean_depth_252d(close: pd.Series) -> pd.Series:
    """Fraction of 252d where depth exceeds the window's own mean depth."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    mean_uw = _rolling_mean(uw, _TD_YEAR)
    above = (uw > mean_uw).astype(float)
    return _rolling_mean(above, _TD_YEAR)


def uw_126_uw_days_above_ulcer_threshold_252d(close: pd.Series) -> pd.Series:
    """Fraction of 252d where depth exceeds the 252d Ulcer Index threshold."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    ui = np.sqrt(_rolling_mean(uw ** 2, _TD_YEAR))
    above = (uw > ui).astype(float)
    return _rolling_mean(above, _TD_YEAR)


def uw_127_uw_entropy_63d(close: pd.Series) -> pd.Series:
    """Shannon entropy of binned underwater depth distribution over 63d."""
    uw = _uw_rolling(close, _TD_QTR).abs()
    def _ent(y: np.ndarray) -> float:
        y = y[~np.isnan(y)]
        if len(y) < 2:
            return 0.0
        hist, _ = np.histogram(y, bins=8, density=True)
        hist = hist[hist > 0]
        if len(hist) == 0:
            return 0.0
        return float(-np.sum(hist * np.log(hist + _EPS)))
    return uw.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_ent, raw=True)


def uw_128_uw_entropy_252d(close: pd.Series) -> pd.Series:
    """Shannon entropy of binned underwater depth distribution over 252d."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    def _ent(y: np.ndarray) -> float:
        y = y[~np.isnan(y)]
        if len(y) < 2:
            return 0.0
        hist, _ = np.histogram(y, bins=10, density=True)
        hist = hist[hist > 0]
        if len(hist) == 0:
            return 0.0
        return float(-np.sum(hist * np.log(hist + _EPS)))
    return uw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_ent, raw=True)


def uw_129_uw_cvar_5pct_252d(close: pd.Series) -> pd.Series:
    """Conditional Value-at-Risk (CVaR) at 5th pct of underwater depths over 252d."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    q05 = uw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.05)
    below = uw.where(uw <= q05)
    return below.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


def uw_130_uw_cvar_10pct_252d(close: pd.Series) -> pd.Series:
    """CVaR at 10th pct of underwater depths over 252d."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    q10 = uw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.10)
    below = uw.where(uw <= q10)
    return below.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


def uw_131_uw_range_in_window_252d(close: pd.Series) -> pd.Series:
    """Range of underwater depths (max - min) within 252d window."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    return (uw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).max()
            - uw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min())


def uw_132_uw_range_in_window_63d(close: pd.Series) -> pd.Series:
    """Range of underwater depths within 63d window."""
    uw = _uw_rolling(close, _TD_QTR).abs()
    return (uw.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).max()
            - uw.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min())


def uw_133_uw_depth_trend_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of underwater depth series over 63d (is distress trending up or down?)."""
    uw = _uw_rolling(close, _TD_QTR).abs()
    n = _TD_QTR
    x = np.arange(n, dtype=float)
    x_mean = x.mean()
    x_var = ((x - x_mean) ** 2).sum()
    def _slope(y: np.ndarray) -> float:
        m = len(y)
        if m < 2:
            return float('nan')
        xx = np.arange(m, dtype=float)
        xx_mean = xx.mean()
        yy_mean = y.mean()
        num = float(np.sum((xx - xx_mean) * (y - yy_mean)))
        den = float(np.sum((xx - xx_mean) ** 2))
        return num / den if abs(den) > _EPS else float('nan')
    return uw.rolling(n, min_periods=max(1, n // 2)).apply(_slope, raw=True)


def uw_134_uw_depth_trend_slope_252d(close: pd.Series) -> pd.Series:
    """OLS slope of underwater depth series over 252d."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    n = _TD_YEAR
    def _slope(y: np.ndarray) -> float:
        m = len(y)
        if m < 2:
            return float('nan')
        xx = np.arange(m, dtype=float)
        xx_mean = xx.mean()
        yy_mean = y.mean()
        num = float(np.sum((xx - xx_mean) * (y - yy_mean)))
        den = float(np.sum((xx - xx_mean) ** 2))
        return num / den if abs(den) > _EPS else float('nan')
    return uw.rolling(n, min_periods=max(1, n // 2)).apply(_slope, raw=True)


def uw_135_uw_area_integral_curvature_252d(close: pd.Series) -> pd.Series:
    """Integral of squared second differences of depth over 252d (curvature of pain curve)."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    d2 = uw.diff(1).diff(1)
    return _rolling_sum(d2 ** 2, _TD_YEAR)


# --- Group J (136-150): Intraday, multi-price, and advanced constructs ---

def uw_136_uw_open_close_gap_area_252d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Area of gap (|open - prev_close|/prev_close) on underwater days over 252d."""
    gap = (open_ - close.shift(1)).abs() / close.shift(1).replace(0, np.nan)
    uw = _uw_rolling(close, _TD_YEAR).abs()
    submerged = (uw > 0).astype(float)
    return _rolling_sum(gap * submerged, _TD_YEAR)


def uw_137_uw_body_area_252d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Underwater days * candle body size (|close - open|) area over 252d."""
    body = (close - open_).abs() / close.replace(0, np.nan)
    uw = _uw_rolling(close, _TD_YEAR).abs()
    return _rolling_sum(uw * body, _TD_YEAR)


def uw_138_uw_area_expanding_ma_cross_63d(close: pd.Series) -> pd.Series:
    """63d uw area on days when close is below its 63d SMA (MA-confirmed distress)."""
    uw = _uw_rolling(close, _TD_QTR).abs()
    sma63 = _rolling_mean(close, _TD_QTR)
    below_ma = (close < sma63).astype(float)
    return _rolling_sum(uw * below_ma, _TD_QTR)


def uw_139_uw_area_expanding_ma_cross_252d(close: pd.Series) -> pd.Series:
    """252d uw area on days when close is below its 252d SMA."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    sma252 = _rolling_mean(close, _TD_YEAR)
    below_ma = (close < sma252).astype(float)
    return _rolling_sum(uw * below_ma, _TD_YEAR)


def uw_140_uw_consecutive_run_area_252d(close: pd.Series) -> pd.Series:
    """Mean length of consecutive underwater runs times mean depth over 252d."""
    uw = _uw_rolling(close, _TD_YEAR)
    is_uw = (uw < 0).astype(float)
    run_start = is_uw.diff(1).clip(lower=0)
    run_len = is_uw.groupby((run_start == 1).cumsum()).cumsum()
    depth = uw.abs()
    return _rolling_mean(run_len * depth, _TD_YEAR)


def uw_141_uw_drawdown_recovery_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of negative area to positive area changes in uw series over 63d."""
    uw = _uw_rolling(close, _TD_QTR)
    d = uw.diff(1)
    neg_area = d.where(d < 0, 0.0).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    pos_area = d.where(d > 0, 0.0).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    return _safe_div(neg_area, pos_area + _EPS)


def uw_142_uw_drawdown_recovery_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of negative area to positive area changes in uw series over 252d."""
    uw = _uw_rolling(close, _TD_YEAR)
    d = uw.diff(1)
    neg_area = d.where(d < 0, 0.0).abs().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).sum()
    pos_area = d.where(d > 0, 0.0).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).sum()
    return _safe_div(neg_area, pos_area + _EPS)


def uw_143_uw_area_vs_hl_range_ratio_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252d uw area divided by 252d high-low range (pain relative to price range)."""
    area = _rolling_sum(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    hl_range = (_rolling_max(high, _TD_YEAR) - _rolling_min(low, _TD_YEAR)) / close
    return _safe_div(area, hl_range + _EPS)


def uw_144_uw_area_atr_units_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252d uw area expressed in ATR-normalized units per day."""
    area = _rolling_sum(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    atr = _atr(high, low, close, _TD_YEAR)
    return _safe_div(area / _TD_YEAR, atr / close)


def uw_145_uw_area_exponential_integral_63d(close: pd.Series) -> pd.Series:
    """Exponentially-decayed integral of 63d uw depth (recent pain weighted most)."""
    uw = _uw_rolling(close, _TD_QTR).abs()
    decay = np.exp(-np.arange(_TD_QTR, dtype=float) / _TD_MON)[::-1]
    def _exp_int(y: np.ndarray) -> float:
        n = len(y)
        d = decay[-n:]
        return float(np.sum(y * d))
    return uw.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_exp_int, raw=True)


def uw_146_uw_area_exponential_integral_252d(close: pd.Series) -> pd.Series:
    """Exponentially-decayed integral of 252d uw depth (span=63)."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    decay = np.exp(-np.arange(_TD_YEAR, dtype=float) / _TD_QTR)[::-1]
    def _exp_int(y: np.ndarray) -> float:
        n = len(y)
        d = decay[-n:]
        return float(np.sum(y * d))
    return uw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_exp_int, raw=True)


def uw_147_uw_conditional_vol_downside_252d(close: pd.Series) -> pd.Series:
    """Std dev of daily returns conditioned on being underwater over 252d."""
    ret = close.pct_change()
    uw = _uw_rolling(close, _TD_YEAR)
    cond_ret = ret.where(uw < 0)
    return cond_ret.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).std()


def uw_148_uw_pain_index_high_price_252d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Pain Index using intraday high vs 252-day high-of-highs (best-case pain)."""
    peak_high = _rolling_max(high, _TD_YEAR)
    uw_high = _safe_div(high - peak_high, peak_high).abs()
    return _rolling_mean(uw_high, _TD_YEAR)


def uw_149_uw_area_ath_normalized_by_years(close: pd.Series) -> pd.Series:
    """Expanding ATH area divided by number of years of data (annualized pain rate)."""
    uw_area = _uw_expanding(close).abs().expanding(min_periods=1).sum()
    n_years = pd.Series(
        np.arange(1, len(close) + 1, dtype=float) / _TD_YEAR,
        index=close.index
    )
    return _safe_div(uw_area, n_years)


def uw_150_uw_composite_distress_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Multi-factor composite: combines Pain Index, Ulcer Index, vol-adj area, and vol-weighted area."""
    pi252 = _rolling_mean(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    ui252 = np.sqrt(_rolling_mean(_uw_rolling(close, _TD_YEAR) ** 2, _TD_YEAR))
    area252 = _rolling_sum(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)
    ret_vol = close.pct_change().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).std()
    vol_adj = _safe_div(area252, ret_vol + _EPS)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    v_norm = _safe_div(volume, avg_vol + _EPS)
    vol_wt = _rolling_mean(_uw_rolling(close, _TD_YEAR).abs() * v_norm, _TD_YEAR)
    return 0.25 * pi252 + 0.25 * ui252 + 0.25 * vol_adj.clip(upper=10) / 10 + 0.25 * vol_wt


# ── Registry ──────────────────────────────────────────────────────────────────

UNDERWATER_CURVE_REGISTRY_076_150 = {
    "uw_076_area_252d_zscore_504d": {"inputs": ["close"], "func": uw_076_area_252d_zscore_504d},
    "uw_077_area_63d_zscore_252d": {"inputs": ["close"], "func": uw_077_area_63d_zscore_252d},
    "uw_078_ulcer_index_zscore_252d": {"inputs": ["close"], "func": uw_078_ulcer_index_zscore_252d},
    "uw_079_pain_index_zscore_expanding": {"inputs": ["close"], "func": uw_079_pain_index_zscore_expanding},
    "uw_080_area_252d_pct_rank_504d": {"inputs": ["close"], "func": uw_080_area_252d_pct_rank_504d},
    "uw_081_pain_index_pct_rank_1260d": {"inputs": ["close"], "func": uw_081_pain_index_pct_rank_1260d},
    "uw_082_ulcer_index_pct_rank_1260d": {"inputs": ["close"], "func": uw_082_ulcer_index_pct_rank_1260d},
    "uw_083_area_expanding_pct_rank": {"inputs": ["close"], "func": uw_083_area_expanding_pct_rank},
    "uw_084_pain_index_21d_zscore_252d": {"inputs": ["close"], "func": uw_084_pain_index_21d_zscore_252d},
    "uw_085_area_21d_pct_rank_252d": {"inputs": ["close"], "func": uw_085_area_21d_pct_rank_252d},
    "uw_086_ulcer_index_252d_vs_63d_ratio": {"inputs": ["close"], "func": uw_086_ulcer_index_252d_vs_63d_ratio},
    "uw_087_area_504d_zscore_1260d": {"inputs": ["close"], "func": uw_087_area_504d_zscore_1260d},
    "uw_088_uw_dispersion_ratio_252d_vs_63d": {"inputs": ["close"], "func": uw_088_uw_dispersion_ratio_252d_vs_63d},
    "uw_089_pain_index_504d_zscore_expanding": {"inputs": ["close"], "func": uw_089_pain_index_504d_zscore_expanding},
    "uw_090_ulcer_252d_expanding_pct_rank": {"inputs": ["close"], "func": uw_090_ulcer_252d_expanding_pct_rank},
    "uw_091_composite_pain_score_equal_weighted": {"inputs": ["close"], "func": uw_091_composite_pain_score_equal_weighted},
    "uw_092_composite_pain_score_decay_weighted": {"inputs": ["close"], "func": uw_092_composite_pain_score_decay_weighted},
    "uw_093_composite_ulcer_score": {"inputs": ["close"], "func": uw_093_composite_ulcer_score},
    "uw_094_composite_area_score": {"inputs": ["close"], "func": uw_094_composite_area_score},
    "uw_095_pain_ulcer_geometric_mean_252d": {"inputs": ["close"], "func": uw_095_pain_ulcer_geometric_mean_252d},
    "uw_096_area_weighted_by_depth_severity_252d": {"inputs": ["close"], "func": uw_096_area_weighted_by_depth_severity_252d},
    "uw_097_area_weighted_by_depth_severity_63d": {"inputs": ["close"], "func": uw_097_area_weighted_by_depth_severity_63d},
    "uw_098_cube_root_area_252d": {"inputs": ["close"], "func": uw_098_cube_root_area_252d},
    "uw_099_square_root_ulcer_252d": {"inputs": ["close"], "func": uw_099_square_root_ulcer_252d},
    "uw_100_log1p_area_252d": {"inputs": ["close"], "func": uw_100_log1p_area_252d},
    "uw_101_log1p_area_63d": {"inputs": ["close"], "func": uw_101_log1p_area_63d},
    "uw_102_log1p_area_ath": {"inputs": ["close"], "func": uw_102_log1p_area_ath},
    "uw_103_area_acceleration_63d": {"inputs": ["close"], "func": uw_103_area_acceleration_63d},
    "uw_104_area_acceleration_252d": {"inputs": ["close"], "func": uw_104_area_acceleration_252d},
    "uw_105_pain_momentum_63d": {"inputs": ["close"], "func": uw_105_pain_momentum_63d},
    "uw_106_hl_spread_weighted_area_252d": {"inputs": ["close", "high", "low"], "func": uw_106_hl_spread_weighted_area_252d},
    "uw_107_low_based_uw_area_63d": {"inputs": ["close", "low"], "func": uw_107_low_based_uw_area_63d},
    "uw_108_low_based_uw_area_252d": {"inputs": ["close", "low"], "func": uw_108_low_based_uw_area_252d},
    "uw_109_open_based_uw_area_252d": {"inputs": ["close", "open"], "func": uw_109_open_based_uw_area_252d},
    "uw_110_volume_surge_uw_area_252d": {"inputs": ["close", "volume"], "func": uw_110_volume_surge_uw_area_252d},
    "uw_111_atr_normalized_uw_area_63d": {"inputs": ["close", "high", "low"], "func": uw_111_atr_normalized_uw_area_63d},
    "uw_112_atr_normalized_uw_area_252d": {"inputs": ["close", "high", "low"], "func": uw_112_atr_normalized_uw_area_252d},
    "uw_113_volume_decline_uw_area_252d": {"inputs": ["close", "volume"], "func": uw_113_volume_decline_uw_area_252d},
    "uw_114_down_day_uw_area_63d": {"inputs": ["close"], "func": uw_114_down_day_uw_area_63d},
    "uw_115_up_day_uw_area_63d": {"inputs": ["close"], "func": uw_115_up_day_uw_area_63d},
    "uw_116_down_vs_up_uw_area_ratio_63d": {"inputs": ["close"], "func": uw_116_down_vs_up_uw_area_ratio_63d},
    "uw_117_high_peak_vs_close_uw_diff_area_252d": {"inputs": ["close", "high"], "func": uw_117_high_peak_vs_close_uw_diff_area_252d},
    "uw_118_volume_weighted_ulcer_index_252d": {"inputs": ["close", "volume"], "func": uw_118_volume_weighted_ulcer_index_252d},
    "uw_119_high_volume_pain_concentration_252d": {"inputs": ["close", "volume"], "func": uw_119_high_volume_pain_concentration_252d},
    "uw_120_pain_ratio_open_to_close_252d": {"inputs": ["close", "open"], "func": uw_120_pain_ratio_open_to_close_252d},
    "uw_121_uw_tail_area_q90_252d": {"inputs": ["close"], "func": uw_121_uw_tail_area_q90_252d},
    "uw_122_uw_tail_concentration_ratio_252d": {"inputs": ["close"], "func": uw_122_uw_tail_concentration_ratio_252d},
    "uw_123_uw_gini_coefficient_63d": {"inputs": ["close"], "func": uw_123_uw_gini_coefficient_63d},
    "uw_124_uw_gini_coefficient_252d": {"inputs": ["close"], "func": uw_124_uw_gini_coefficient_252d},
    "uw_125_uw_days_above_mean_depth_252d": {"inputs": ["close"], "func": uw_125_uw_days_above_mean_depth_252d},
    "uw_126_uw_days_above_ulcer_threshold_252d": {"inputs": ["close"], "func": uw_126_uw_days_above_ulcer_threshold_252d},
    "uw_127_uw_entropy_63d": {"inputs": ["close"], "func": uw_127_uw_entropy_63d},
    "uw_128_uw_entropy_252d": {"inputs": ["close"], "func": uw_128_uw_entropy_252d},
    "uw_129_uw_cvar_5pct_252d": {"inputs": ["close"], "func": uw_129_uw_cvar_5pct_252d},
    "uw_130_uw_cvar_10pct_252d": {"inputs": ["close"], "func": uw_130_uw_cvar_10pct_252d},
    "uw_131_uw_range_in_window_252d": {"inputs": ["close"], "func": uw_131_uw_range_in_window_252d},
    "uw_132_uw_range_in_window_63d": {"inputs": ["close"], "func": uw_132_uw_range_in_window_63d},
    "uw_133_uw_depth_trend_slope_63d": {"inputs": ["close"], "func": uw_133_uw_depth_trend_slope_63d},
    "uw_134_uw_depth_trend_slope_252d": {"inputs": ["close"], "func": uw_134_uw_depth_trend_slope_252d},
    "uw_135_uw_area_integral_curvature_252d": {"inputs": ["close"], "func": uw_135_uw_area_integral_curvature_252d},
    "uw_136_uw_open_close_gap_area_252d": {"inputs": ["close", "open"], "func": uw_136_uw_open_close_gap_area_252d},
    "uw_137_uw_body_area_252d": {"inputs": ["close", "open"], "func": uw_137_uw_body_area_252d},
    "uw_138_uw_area_expanding_ma_cross_63d": {"inputs": ["close"], "func": uw_138_uw_area_expanding_ma_cross_63d},
    "uw_139_uw_area_expanding_ma_cross_252d": {"inputs": ["close"], "func": uw_139_uw_area_expanding_ma_cross_252d},
    "uw_140_uw_consecutive_run_area_252d": {"inputs": ["close"], "func": uw_140_uw_consecutive_run_area_252d},
    "uw_141_uw_drawdown_recovery_ratio_63d": {"inputs": ["close"], "func": uw_141_uw_drawdown_recovery_ratio_63d},
    "uw_142_uw_drawdown_recovery_ratio_252d": {"inputs": ["close"], "func": uw_142_uw_drawdown_recovery_ratio_252d},
    "uw_143_uw_area_vs_hl_range_ratio_252d": {"inputs": ["close", "high", "low"], "func": uw_143_uw_area_vs_hl_range_ratio_252d},
    "uw_144_uw_area_atr_units_252d": {"inputs": ["close", "high", "low"], "func": uw_144_uw_area_atr_units_252d},
    "uw_145_uw_area_exponential_integral_63d": {"inputs": ["close"], "func": uw_145_uw_area_exponential_integral_63d},
    "uw_146_uw_area_exponential_integral_252d": {"inputs": ["close"], "func": uw_146_uw_area_exponential_integral_252d},
    "uw_147_uw_conditional_vol_downside_252d": {"inputs": ["close"], "func": uw_147_uw_conditional_vol_downside_252d},
    "uw_148_uw_pain_index_high_price_252d": {"inputs": ["close", "high"], "func": uw_148_uw_pain_index_high_price_252d},
    "uw_149_uw_area_ath_normalized_by_years": {"inputs": ["close"], "func": uw_149_uw_area_ath_normalized_by_years},
    "uw_150_uw_composite_distress_score": {"inputs": ["close", "volume"], "func": uw_150_uw_composite_distress_score},
}
