"""
104_mean_reversion_potential — Base Features 076-150
Domain: distance-from-equilibrium, reversion half-life and elastic stretch
        metrics (extended horizons, autocorrelation structure, channel
        overshoot, Hurst / efficiency composites).
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


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _zscore(s: pd.Series, w: int) -> pd.Series:
    return _safe_div(s - _rolling_mean(s, w), _rolling_std(s, w))


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs()
    ], axis=1).max(axis=1)


def _stretch(close: pd.Series, w: int) -> pd.Series:
    """Deviation of close from its w-day SMA in w-day-std units."""
    return _safe_div(close - _rolling_mean(close, w), _rolling_std(close, w))


def _ar1(s: pd.Series, w: int) -> pd.Series:
    """Rolling lag-1 autocorrelation of a series over window w."""
    return s.rolling(w, min_periods=max(5, w // 2)).corr(s.shift(1))


def _half_life(phi: pd.Series) -> pd.Series:
    p = phi.clip(lower=_EPS, upper=1 - 1e-4)
    return -np.log(2.0) / np.log(p)


def _wma(s: pd.Series, w: int) -> pd.Series:
    """Linearly-weighted moving average over window w."""
    wts = np.arange(1, w + 1, dtype=float)

    def f(x):
        k = len(x)
        ww = wts[-k:]
        return float(np.dot(x, ww) / ww.sum())
    return s.rolling(w, min_periods=max(2, w // 2)).apply(f, raw=True)


def _hurst_rs(x: np.ndarray) -> float:
    x = np.asarray(x, dtype=float)
    n = len(x)
    if n < 16:
        return np.nan
    m = x.mean()
    dev = np.cumsum(x - m)
    rng = dev.max() - dev.min()
    s = x.std()
    if s <= 0 or rng <= 0:
        return np.nan
    return float(np.log(rng / s) / np.log(n))


def _hurst(close: pd.Series, w: int) -> pd.Series:
    lr = _log_safe(close).diff(1)
    return lr.rolling(w, min_periods=max(16, w // 2)).apply(_hurst_rs, raw=True)


def _efficiency_ratio(close: pd.Series, w: int) -> pd.Series:
    net = (close - close.shift(w)).abs()
    path = _rolling_sum(close.diff(1).abs(), w)
    return _safe_div(net, path)


def _variance_ratio(close: pd.Series, q: int, w: int) -> pd.Series:
    lr = _log_safe(close).diff(1)
    lrq = _log_safe(close).diff(q)
    var1 = _rolling_std(lr, w) ** 2
    varq = _rolling_std(lrq, w) ** 2
    return _safe_div(varq, var1 * q)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group A (076-090): Stretch across extended horizons ---

def mrp_076_stretch_from_sma10(close: pd.Series) -> pd.Series:
    """Deviation of close from its 10-day SMA in 10-day-std units."""
    return _stretch(close, 10)


def mrp_077_stretch_from_sma200(close: pd.Series) -> pd.Series:
    """Deviation of close from its 200-day SMA in 200-day-std units."""
    return _stretch(close, 200)


def mrp_078_stretch_from_ema21(close: pd.Series) -> pd.Series:
    """Deviation of close from its 21-day EMA in 21-day-std units."""
    return _safe_div(close - _ewm_mean(close, _TD_MON), _rolling_std(close, _TD_MON))


def mrp_079_stretch_from_ema126(close: pd.Series) -> pd.Series:
    """Deviation of close from its 126-day EMA in 126-day-std units."""
    return _safe_div(close - _ewm_mean(close, _TD_HALF), _rolling_std(close, _TD_HALF))


def mrp_080_stretch_from_wma63(close: pd.Series) -> pd.Series:
    """Deviation of close from its 63-day weighted MA in 63-day-std units."""
    return _safe_div(close - _wma(close, _TD_QTR), _rolling_std(close, _TD_QTR))


def mrp_081_stretch_log_63d(close: pd.Series) -> pd.Series:
    """Log-close minus its 63-day mean log-close (log-space stretch)."""
    lc = _log_safe(close)
    return lc - _rolling_mean(lc, _TD_QTR)


def mrp_082_stretch_pct_from_252d_mean(close: pd.Series) -> pd.Series:
    """Percent deviation of close from its 252-day SMA."""
    ma = _rolling_mean(close, _TD_YEAR)
    return _safe_div(close - ma, ma)


def mrp_083_stretch_atr_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Deviation of close from its 126-day SMA in ATR units."""
    atr = _rolling_mean(_tr(close, high, low), _TD_QTR)
    return _safe_div(close - _rolling_mean(close, _TD_HALF), atr)


def mrp_084_stretch_dispersion_across_tf(close: pd.Series) -> pd.Series:
    """Cross-horizon standard deviation of the stretch readings."""
    parts = [_stretch(close, w) for w in (_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR)]
    return pd.concat(parts, axis=1).std(axis=1)


def mrp_085_max_abs_stretch(close: pd.Series) -> pd.Series:
    """Largest absolute stretch across the 21/63/126/252-day horizons."""
    parts = [_stretch(close, w).abs() for w in (_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR)]
    return pd.concat(parts, axis=1).max(axis=1)


def mrp_086_stretch_ewm_smoothed(close: pd.Series) -> pd.Series:
    """21-day EWM-smoothed 63-day stretch (noise-reduced equilibrium gap)."""
    return _ewm_mean(_stretch(close, _TD_QTR), _TD_MON)


def mrp_087_stretch_below_2std_count(close: pd.Series) -> pd.Series:
    """Count of horizons whose stretch is below -2 (multi-horizon overshoot)."""
    return sum((_stretch(close, w) < -2.0).astype(float)
               for w in (_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR))


def mrp_088_stretch_skew_63d(close: pd.Series) -> pd.Series:
    """Skewness of the 21-day stretch series over a trailing 63-day window."""
    return _stretch(close, _TD_MON).rolling(_TD_QTR, min_periods=_TD_MON).skew()


def mrp_089_stretch_kurtosis_63d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of the 21-day stretch over a trailing 63-day window."""
    return _stretch(close, _TD_MON).rolling(_TD_QTR, min_periods=_TD_MON).kurt()


def mrp_090_stretch_min_504d(close: pd.Series) -> pd.Series:
    """Most negative 63-day stretch observed within a trailing 504-day window."""
    return _rolling_min(_stretch(close, _TD_QTR), 504)


# --- Group B (091-105): Autocorrelation / variance ratio (extended) ---

def mrp_091_ar1_returns_126d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of daily returns over a 126-day window."""
    return _ar1(_daily_ret(close), _TD_HALF)


def mrp_092_ar1_price_252d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of the close level over a 252-day window."""
    return _ar1(close, _TD_YEAR)


def mrp_093_ar1_price_126d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of the close level over a 126-day window."""
    return _ar1(close, _TD_HALF)


def mrp_094_autocorr_lag2_63d(close: pd.Series) -> pd.Series:
    """Lag-2 autocorrelation of daily returns over a 63-day window."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=_TD_MON).corr(ret.shift(2))


def mrp_095_autocorr_lag10_126d(close: pd.Series) -> pd.Series:
    """Lag-10 autocorrelation of daily returns over a 126-day window."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_HALF, min_periods=_TD_QTR).corr(ret.shift(10))


def mrp_096_variance_ratio_2_252d(close: pd.Series) -> pd.Series:
    """Variance ratio VR(2) over a 252-day window."""
    return _variance_ratio(close, 2, _TD_YEAR)


def mrp_097_variance_ratio_20_252d(close: pd.Series) -> pd.Series:
    """Variance ratio VR(20) over a 252-day window."""
    return _variance_ratio(close, 20, _TD_YEAR)


def mrp_098_variance_ratio_mean_across_q(close: pd.Series) -> pd.Series:
    """Mean variance ratio across q = 2/5/10/20 over a 252-day window."""
    parts = [_variance_ratio(close, q, _TD_YEAR) for q in (2, 5, 10, 20)]
    return pd.concat(parts, axis=1).mean(axis=1)


def mrp_099_vr_below_1_flag(close: pd.Series) -> pd.Series:
    """Flag: VR(5) over 252 days is below 1 (mean-reverting price)."""
    return (_variance_ratio(close, 5, _TD_YEAR) < 1.0).astype(float)


def mrp_100_half_life_126d(close: pd.Series) -> pd.Series:
    """Mean-reversion half-life implied by 126-day AR(1) of detrended price."""
    detr = close - _rolling_mean(close, _TD_HALF)
    return _half_life(_ar1(detr, _TD_HALF))


def mrp_101_reversion_rate_zscore(close: pd.Series) -> pd.Series:
    """Z-score of the OU reversion rate over a trailing 252-day window."""
    detr = close - _rolling_mean(close, _TD_QTR)
    phi = _ar1(detr, _TD_QTR).clip(lower=_EPS, upper=1 - 1e-4)
    theta = -np.log(phi)
    return _zscore(theta, _TD_YEAR)


def mrp_102_ar1_stability(close: pd.Series) -> pd.Series:
    """Standard deviation of the 63-day price AR(1) over a trailing 126 days."""
    return _rolling_std(_ar1(close, _TD_QTR), _TD_HALF)


def mrp_103_partial_autocorr_proxy(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation minus squared lag-1 (partial-autocorr proxy)."""
    a1 = _ar1(_daily_ret(close), _TD_QTR)
    return a1 - a1 * a1


def mrp_104_return_reversal_frequency(close: pd.Series) -> pd.Series:
    """Fraction of last 63 days where the daily return sign reversed."""
    sign = np.sign(_daily_ret(close))
    reversal = (sign != sign.shift(1)).astype(float)
    return _rolling_mean(reversal, _TD_QTR)


def mrp_105_reversion_consistency_score(close: pd.Series) -> pd.Series:
    """Fraction of last 126 days the return autocorrelation was negative."""
    a1 = _ar1(_daily_ret(close), _TD_QTR)
    return _rolling_mean((a1 < 0).astype(float), _TD_HALF)


# --- Group C (106-120): Channel / band overshoot (extended) ---

def mrp_106_below_lower_bollinger_126d(close: pd.Series) -> pd.Series:
    """Distance below the 126-day lower Bollinger band, in std units."""
    return (_stretch(close, _TD_HALF) + 2.0).clip(upper=0)


def mrp_107_below_lower_bollinger_252d(close: pd.Series) -> pd.Series:
    """Distance below the 252-day lower Bollinger band, in std units."""
    return (_stretch(close, _TD_YEAR) + 2.0).clip(upper=0)


def mrp_108_pct_b_126d(close: pd.Series) -> pd.Series:
    """Bollinger %B over the 126-day window."""
    ma = _rolling_mean(close, _TD_HALF)
    sd = _rolling_std(close, _TD_HALF)
    return _safe_div(close - (ma - 2.0 * sd), 4.0 * sd)


def mrp_109_pct_b_252d(close: pd.Series) -> pd.Series:
    """Bollinger %B over the 252-day window."""
    ma = _rolling_mean(close, _TD_YEAR)
    sd = _rolling_std(close, _TD_YEAR)
    return _safe_div(close - (ma - 2.0 * sd), 4.0 * sd)


def mrp_110_pct_b_min_across_tf(close: pd.Series) -> pd.Series:
    """Minimum Bollinger %B across the 21/63/126/252-day horizons."""
    parts = []
    for w in (_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR):
        ma = _rolling_mean(close, w)
        sd = _rolling_std(close, w)
        parts.append(_safe_div(close - (ma - 2.0 * sd), 4.0 * sd))
    return pd.concat(parts, axis=1).min(axis=1)


def mrp_111_keltner_position_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Position of close vs its 21-day Keltner midline, in ATR units."""
    atr = _rolling_mean(_tr(close, high, low), _TD_MON)
    return _safe_div(close - _rolling_mean(close, _TD_MON), atr)


def mrp_112_keltner_position_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Position of close vs its 252-day Keltner midline, in ATR units."""
    atr = _rolling_mean(_tr(close, high, low), _TD_QTR)
    return _safe_div(close - _rolling_mean(close, _TD_YEAR), atr)


def mrp_113_donchian_undershoot_21d(close: pd.Series) -> pd.Series:
    """Position of close within the 21-day Donchian channel (0 = at the low)."""
    lo = _rolling_min(close, _TD_MON)
    hi = _rolling_max(close, _TD_MON)
    return _safe_div(close - lo, hi - lo)


def mrp_114_donchian_undershoot_252d(close: pd.Series) -> pd.Series:
    """Position of close within the 252-day Donchian channel (0 = at the low)."""
    lo = _rolling_min(close, _TD_YEAR)
    hi = _rolling_max(close, _TD_YEAR)
    return _safe_div(close - lo, hi - lo)


def mrp_115_band_overshoot_252d(close: pd.Series) -> pd.Series:
    """Magnitude of the 252-day stretch beyond the -2 std Bollinger band."""
    return (-(_stretch(close, _TD_YEAR) + 2.0)).clip(lower=0)


def mrp_116_days_below_lower_band_63d(close: pd.Series) -> pd.Series:
    """Count of last 63 days the close was below the 63-day lower band."""
    return _rolling_sum((_stretch(close, _TD_QTR) < -2.0).astype(float), _TD_QTR)


def mrp_117_band_breach_frequency_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days the close breached the 63-day lower band."""
    return _rolling_mean((_stretch(close, _TD_QTR) < -2.0).astype(float), _TD_YEAR)


def mrp_118_mean_band_position(close: pd.Series) -> pd.Series:
    """Mean Bollinger %B across the 21/63/126-day windows."""
    parts = []
    for w in (_TD_MON, _TD_QTR, _TD_HALF):
        ma = _rolling_mean(close, w)
        sd = _rolling_std(close, w)
        parts.append(_safe_div(close - (ma - 2.0 * sd), 4.0 * sd))
    return pd.concat(parts, axis=1).mean(axis=1)


def mrp_119_deepest_band_breach(close: pd.Series) -> pd.Series:
    """Deepest band overshoot (in std units) across 21/63/126/252 horizons."""
    parts = [(-(_stretch(close, w) + 2.0)).clip(lower=0)
             for w in (_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR)]
    return pd.concat(parts, axis=1).max(axis=1)


def mrp_120_band_reversion_gap(close: pd.Series) -> pd.Series:
    """Percent distance from the close up to the 63-day lower Bollinger band."""
    ma = _rolling_mean(close, _TD_QTR)
    lower = ma - 2.0 * _rolling_std(close, _TD_QTR)
    return _safe_div(lower - close, close)


# --- Group D (121-135): Distance / displacement (extended) ---

def mrp_121_distance_from_vwap_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percent deviation of close from the 21-day volume-weighted mean price."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    return _safe_div(close - vwap, vwap)


def mrp_122_distance_from_anchored_vwap(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percent deviation of close from the expanding (anchored) VWAP."""
    cv = (close * volume).expanding(min_periods=5).sum()
    vv = volume.expanding(min_periods=5).sum()
    vwap = _safe_div(cv, vv)
    return _safe_div(close - vwap, vwap)


def mrp_123_reversion_gap_252d(close: pd.Series) -> pd.Series:
    """Percent gap between the close and its 252-day equilibrium mean."""
    ma = _rolling_mean(close, _TD_YEAR)
    return _safe_div(ma - close, ma)


def mrp_124_cumulative_deviation_252d(close: pd.Series) -> pd.Series:
    """Sum over 252 days of the percent deviation from the 252-day mean."""
    ma = _rolling_mean(close, _TD_YEAR)
    return _rolling_sum(_safe_div(close - ma, ma), _TD_YEAR)


def mrp_125_time_below_mean_504d(close: pd.Series) -> pd.Series:
    """Fraction of the last 504 days the close sat below its 252-day mean."""
    below = (close < _rolling_mean(close, _TD_YEAR)).astype(float)
    return _rolling_mean(below, 504)


def mrp_126_distance_below_mean_zscore(close: pd.Series) -> pd.Series:
    """Z-score of the percent distance below the 126-day mean."""
    ma = _rolling_mean(close, _TD_HALF)
    dist = _safe_div(close - ma, ma)
    return _zscore(dist, _TD_YEAR)


def mrp_127_displacement_from_median_63d(close: pd.Series) -> pd.Series:
    """Percent deviation of close from its 63-day rolling median."""
    med = _rolling_median(close, _TD_QTR)
    return _safe_div(close - med, med)


def mrp_128_mean_absolute_deviation_63d(close: pd.Series) -> pd.Series:
    """Close deviation from the 63-day mean scaled by 63-day mean abs deviation."""
    ma = _rolling_mean(close, _TD_QTR)
    mad = (close - ma).abs().rolling(_TD_QTR, min_periods=_TD_MON).mean()
    return _safe_div(close - ma, mad)


def mrp_129_deviation_area_under_curve(close: pd.Series) -> pd.Series:
    """Sum over 63 days of the negative part of the deviation from the mean."""
    ma = _rolling_mean(close, _TD_QTR)
    dev = _safe_div(close - ma, ma).clip(upper=0)
    return _rolling_sum(dev, _TD_QTR)


def mrp_130_overshoot_count_252d(close: pd.Series) -> pd.Series:
    """Count of last 252 days the close was below the 63-day lower band."""
    return _rolling_sum((_stretch(close, _TD_QTR) < -2.0).astype(float), _TD_YEAR)


def mrp_131_distance_to_5y_mean(close: pd.Series) -> pd.Series:
    """Percent deviation of close from its 1260-day (5-year) mean."""
    ma = _rolling_mean(close, 1260)
    return _safe_div(close - ma, ma)


def mrp_132_normalized_displacement_atr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Gap between close and 252-day mean expressed in ATR units."""
    atr = _rolling_mean(_tr(close, high, low), _TD_QTR)
    return _safe_div(close - _rolling_mean(close, _TD_YEAR), atr)


def mrp_133_stretch_recovery_fraction(close: pd.Series) -> pd.Series:
    """How far the 63-day stretch has recovered from its trailing-252d minimum."""
    stretch = _stretch(close, _TD_QTR)
    lo = _rolling_min(stretch, _TD_YEAR)
    hi = _rolling_max(stretch, _TD_YEAR)
    return _safe_div(stretch - lo, hi - lo)


def mrp_134_elastic_tension_63d(close: pd.Series) -> pd.Series:
    """Signed squared 63-day stretch (elastic tension stored in the spring)."""
    s = _stretch(close, _TD_QTR)
    return -(s.clip(upper=0) ** 2)


def mrp_135_displacement_persistence_score(close: pd.Series) -> pd.Series:
    """Mean negative deviation from the 126-day mean over the last 63 days."""
    ma = _rolling_mean(close, _TD_HALF)
    dev = _safe_div(close - ma, ma).clip(upper=0)
    return _rolling_mean(dev, _TD_QTR)


# --- Group E (136-150): Hurst / efficiency / composites (extended) ---

def mrp_136_hurst_exponent_252d(close: pd.Series) -> pd.Series:
    """Rescaled-range Hurst exponent of log returns over a 252-day window."""
    return _hurst(close, _TD_YEAR)


def mrp_137_hurst_below_half_fraction(close: pd.Series) -> pd.Series:
    """Fraction of last 126 days the 63-day Hurst exponent was below 0.5."""
    return _rolling_mean((_hurst(close, _TD_QTR) < 0.5).astype(float), _TD_HALF)


def mrp_138_efficiency_ratio_126d(close: pd.Series) -> pd.Series:
    """Kaufman efficiency ratio over 126 days (low = mean-reverting / choppy)."""
    return _efficiency_ratio(close, _TD_HALF)


def mrp_139_efficiency_ratio_252d(close: pd.Series) -> pd.Series:
    """Kaufman efficiency ratio over 252 days."""
    return _efficiency_ratio(close, _TD_YEAR)


def mrp_140_choppiness_index_63d(close: pd.Series) -> pd.Series:
    """Choppiness index over 63 days (high = sideways / mean-reverting)."""
    path = _rolling_sum(close.diff(1).abs(), _TD_QTR)
    rng = _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR)
    return 100.0 * _safe_div(np.log10(_safe_div(path, rng).clip(lower=_EPS)),
                             pd.Series(np.log10(_TD_QTR), index=close.index))


def mrp_141_detrended_range_ratio(close: pd.Series) -> pd.Series:
    """63-day range of detrended log-price relative to its 63-day std."""
    lc = _log_safe(close)
    detr = lc - _rolling_mean(lc, _TD_QTR)
    rng = _rolling_max(detr, _TD_QTR) - _rolling_min(detr, _TD_QTR)
    return _safe_div(rng, _rolling_std(detr, _TD_QTR))


def mrp_142_fractal_dimension_proxy(close: pd.Series) -> pd.Series:
    """Fractal-dimension proxy: 2 minus the 126-day Hurst exponent."""
    return 2.0 - _hurst(close, _TD_HALF)


def mrp_143_reversion_potential_252d(close: pd.Series) -> pd.Series:
    """252-day equilibrium gap times reversion speed (long-horizon potential)."""
    gap = _safe_div(_rolling_mean(close, _TD_YEAR) - close,
                    _rolling_mean(close, _TD_YEAR)).clip(lower=0)
    speed = (1.0 - _ar1(close, _TD_YEAR)).clip(lower=0)
    return gap * speed


def mrp_144_deep_value_snapback_score(close: pd.Series) -> pd.Series:
    """Below-band overshoot times the gap up to the 126-day mean."""
    overshoot = (-(_stretch(close, _TD_QTR) + 2.0)).clip(lower=0)
    gap = _safe_div(_rolling_mean(close, _TD_HALF) - close,
                    _rolling_mean(close, _TD_HALF)).clip(lower=0)
    return overshoot * gap


def mrp_145_elastic_capitulation_flag(close: pd.Series) -> pd.Series:
    """Flag: deep band breach (< -2.5 std) in a mean-reverting Hurst regime."""
    breach = _stretch(close, _TD_QTR) < -2.5
    reverting = _hurst(close, _TD_HALF) < 0.5
    return (breach & reverting).astype(float)


def mrp_146_distance_halflife_hurst_composite(close: pd.Series) -> pd.Series:
    """Equilibrium gap divided by half-life, scaled by mean-reversion regime."""
    ma = _rolling_mean(close, _TD_QTR)
    gap = _safe_div(ma - close, ma).clip(lower=0)
    detr = close - ma
    hl = _half_life(_ar1(detr, _TD_QTR)).clip(lower=1.0)
    regime = (2.0 - _hurst(close, _TD_HALF)).clip(lower=0)
    return _safe_div(gap, hl) * regime


def mrp_147_mean_reversion_zscore_index(close: pd.Series) -> pd.Series:
    """Z-score of the 63-day stretch combined with its 252-day stretch z-score."""
    s63 = _zscore(_stretch(close, _TD_QTR), _TD_YEAR)
    s252 = _zscore(_stretch(close, _TD_YEAR), _TD_YEAR)
    return (s63 + s252) / 2.0


def mrp_148_overshoot_reversion_alignment(close: pd.Series) -> pd.Series:
    """Below-band overshoot present with a negative return autocorrelation."""
    overshoot = (-(_stretch(close, _TD_QTR) + 2.0)).clip(lower=0)
    reverting = (_ar1(_daily_ret(close), _TD_QTR) < 0).astype(float)
    return overshoot * reverting


def mrp_149_capitulation_elastic_index(close: pd.Series) -> pd.Series:
    """Composite: overshoot depth, time below mean and efficiency-ratio choppiness."""
    overshoot = (-_stretch(close, _TD_QTR)).clip(lower=0) / 3.0
    below = _rolling_mean((close < _rolling_mean(close, _TD_YEAR)).astype(float), _TD_YEAR)
    chop = 1.0 - _efficiency_ratio(close, _TD_QTR)
    return overshoot * (0.5 + below) * (0.5 + chop)


def mrp_150_master_mean_reversion_potential_index(close: pd.Series) -> pd.Series:
    """Master index: equilibrium gap, overshoot, reversion speed and regime."""
    gap = _safe_div(_rolling_mean(close, _TD_HALF) - close,
                    _rolling_mean(close, _TD_HALF)).clip(lower=0)
    overshoot = (-_stretch(close, _TD_QTR)).clip(lower=0) / 3.0
    speed = (1.0 - _ar1(close, _TD_QTR)).clip(lower=0, upper=2.0) / 2.0
    regime = (2.0 - _hurst(close, _TD_HALF)).clip(lower=0, upper=2.0) / 2.0
    return (gap + overshoot) * (0.5 + speed) * (0.5 + regime)


# ── Registry ──────────────────────────────────────────────────────────────────

MEAN_REVERSION_POTENTIAL_REGISTRY_076_150 = {
    "mrp_076_stretch_from_sma10": {"inputs": ["close"], "func": mrp_076_stretch_from_sma10},
    "mrp_077_stretch_from_sma200": {"inputs": ["close"], "func": mrp_077_stretch_from_sma200},
    "mrp_078_stretch_from_ema21": {"inputs": ["close"], "func": mrp_078_stretch_from_ema21},
    "mrp_079_stretch_from_ema126": {"inputs": ["close"], "func": mrp_079_stretch_from_ema126},
    "mrp_080_stretch_from_wma63": {"inputs": ["close"], "func": mrp_080_stretch_from_wma63},
    "mrp_081_stretch_log_63d": {"inputs": ["close"], "func": mrp_081_stretch_log_63d},
    "mrp_082_stretch_pct_from_252d_mean": {"inputs": ["close"], "func": mrp_082_stretch_pct_from_252d_mean},
    "mrp_083_stretch_atr_126d": {"inputs": ["close", "high", "low"], "func": mrp_083_stretch_atr_126d},
    "mrp_084_stretch_dispersion_across_tf": {"inputs": ["close"], "func": mrp_084_stretch_dispersion_across_tf},
    "mrp_085_max_abs_stretch": {"inputs": ["close"], "func": mrp_085_max_abs_stretch},
    "mrp_086_stretch_ewm_smoothed": {"inputs": ["close"], "func": mrp_086_stretch_ewm_smoothed},
    "mrp_087_stretch_below_2std_count": {"inputs": ["close"], "func": mrp_087_stretch_below_2std_count},
    "mrp_088_stretch_skew_63d": {"inputs": ["close"], "func": mrp_088_stretch_skew_63d},
    "mrp_089_stretch_kurtosis_63d": {"inputs": ["close"], "func": mrp_089_stretch_kurtosis_63d},
    "mrp_090_stretch_min_504d": {"inputs": ["close"], "func": mrp_090_stretch_min_504d},
    "mrp_091_ar1_returns_126d": {"inputs": ["close"], "func": mrp_091_ar1_returns_126d},
    "mrp_092_ar1_price_252d": {"inputs": ["close"], "func": mrp_092_ar1_price_252d},
    "mrp_093_ar1_price_126d": {"inputs": ["close"], "func": mrp_093_ar1_price_126d},
    "mrp_094_autocorr_lag2_63d": {"inputs": ["close"], "func": mrp_094_autocorr_lag2_63d},
    "mrp_095_autocorr_lag10_126d": {"inputs": ["close"], "func": mrp_095_autocorr_lag10_126d},
    "mrp_096_variance_ratio_2_252d": {"inputs": ["close"], "func": mrp_096_variance_ratio_2_252d},
    "mrp_097_variance_ratio_20_252d": {"inputs": ["close"], "func": mrp_097_variance_ratio_20_252d},
    "mrp_098_variance_ratio_mean_across_q": {"inputs": ["close"], "func": mrp_098_variance_ratio_mean_across_q},
    "mrp_099_vr_below_1_flag": {"inputs": ["close"], "func": mrp_099_vr_below_1_flag},
    "mrp_100_half_life_126d": {"inputs": ["close"], "func": mrp_100_half_life_126d},
    "mrp_101_reversion_rate_zscore": {"inputs": ["close"], "func": mrp_101_reversion_rate_zscore},
    "mrp_102_ar1_stability": {"inputs": ["close"], "func": mrp_102_ar1_stability},
    "mrp_103_partial_autocorr_proxy": {"inputs": ["close"], "func": mrp_103_partial_autocorr_proxy},
    "mrp_104_return_reversal_frequency": {"inputs": ["close"], "func": mrp_104_return_reversal_frequency},
    "mrp_105_reversion_consistency_score": {"inputs": ["close"], "func": mrp_105_reversion_consistency_score},
    "mrp_106_below_lower_bollinger_126d": {"inputs": ["close"], "func": mrp_106_below_lower_bollinger_126d},
    "mrp_107_below_lower_bollinger_252d": {"inputs": ["close"], "func": mrp_107_below_lower_bollinger_252d},
    "mrp_108_pct_b_126d": {"inputs": ["close"], "func": mrp_108_pct_b_126d},
    "mrp_109_pct_b_252d": {"inputs": ["close"], "func": mrp_109_pct_b_252d},
    "mrp_110_pct_b_min_across_tf": {"inputs": ["close"], "func": mrp_110_pct_b_min_across_tf},
    "mrp_111_keltner_position_21d": {"inputs": ["close", "high", "low"], "func": mrp_111_keltner_position_21d},
    "mrp_112_keltner_position_252d": {"inputs": ["close", "high", "low"], "func": mrp_112_keltner_position_252d},
    "mrp_113_donchian_undershoot_21d": {"inputs": ["close"], "func": mrp_113_donchian_undershoot_21d},
    "mrp_114_donchian_undershoot_252d": {"inputs": ["close"], "func": mrp_114_donchian_undershoot_252d},
    "mrp_115_band_overshoot_252d": {"inputs": ["close"], "func": mrp_115_band_overshoot_252d},
    "mrp_116_days_below_lower_band_63d": {"inputs": ["close"], "func": mrp_116_days_below_lower_band_63d},
    "mrp_117_band_breach_frequency_252d": {"inputs": ["close"], "func": mrp_117_band_breach_frequency_252d},
    "mrp_118_mean_band_position": {"inputs": ["close"], "func": mrp_118_mean_band_position},
    "mrp_119_deepest_band_breach": {"inputs": ["close"], "func": mrp_119_deepest_band_breach},
    "mrp_120_band_reversion_gap": {"inputs": ["close"], "func": mrp_120_band_reversion_gap},
    "mrp_121_distance_from_vwap_21d": {"inputs": ["close", "volume"], "func": mrp_121_distance_from_vwap_21d},
    "mrp_122_distance_from_anchored_vwap": {"inputs": ["close", "volume"], "func": mrp_122_distance_from_anchored_vwap},
    "mrp_123_reversion_gap_252d": {"inputs": ["close"], "func": mrp_123_reversion_gap_252d},
    "mrp_124_cumulative_deviation_252d": {"inputs": ["close"], "func": mrp_124_cumulative_deviation_252d},
    "mrp_125_time_below_mean_504d": {"inputs": ["close"], "func": mrp_125_time_below_mean_504d},
    "mrp_126_distance_below_mean_zscore": {"inputs": ["close"], "func": mrp_126_distance_below_mean_zscore},
    "mrp_127_displacement_from_median_63d": {"inputs": ["close"], "func": mrp_127_displacement_from_median_63d},
    "mrp_128_mean_absolute_deviation_63d": {"inputs": ["close"], "func": mrp_128_mean_absolute_deviation_63d},
    "mrp_129_deviation_area_under_curve": {"inputs": ["close"], "func": mrp_129_deviation_area_under_curve},
    "mrp_130_overshoot_count_252d": {"inputs": ["close"], "func": mrp_130_overshoot_count_252d},
    "mrp_131_distance_to_5y_mean": {"inputs": ["close"], "func": mrp_131_distance_to_5y_mean},
    "mrp_132_normalized_displacement_atr": {"inputs": ["close", "high", "low"], "func": mrp_132_normalized_displacement_atr},
    "mrp_133_stretch_recovery_fraction": {"inputs": ["close"], "func": mrp_133_stretch_recovery_fraction},
    "mrp_134_elastic_tension_63d": {"inputs": ["close"], "func": mrp_134_elastic_tension_63d},
    "mrp_135_displacement_persistence_score": {"inputs": ["close"], "func": mrp_135_displacement_persistence_score},
    "mrp_136_hurst_exponent_252d": {"inputs": ["close"], "func": mrp_136_hurst_exponent_252d},
    "mrp_137_hurst_below_half_fraction": {"inputs": ["close"], "func": mrp_137_hurst_below_half_fraction},
    "mrp_138_efficiency_ratio_126d": {"inputs": ["close"], "func": mrp_138_efficiency_ratio_126d},
    "mrp_139_efficiency_ratio_252d": {"inputs": ["close"], "func": mrp_139_efficiency_ratio_252d},
    "mrp_140_choppiness_index_63d": {"inputs": ["close"], "func": mrp_140_choppiness_index_63d},
    "mrp_141_detrended_range_ratio": {"inputs": ["close"], "func": mrp_141_detrended_range_ratio},
    "mrp_142_fractal_dimension_proxy": {"inputs": ["close"], "func": mrp_142_fractal_dimension_proxy},
    "mrp_143_reversion_potential_252d": {"inputs": ["close"], "func": mrp_143_reversion_potential_252d},
    "mrp_144_deep_value_snapback_score": {"inputs": ["close"], "func": mrp_144_deep_value_snapback_score},
    "mrp_145_elastic_capitulation_flag": {"inputs": ["close"], "func": mrp_145_elastic_capitulation_flag},
    "mrp_146_distance_halflife_hurst_composite": {"inputs": ["close"], "func": mrp_146_distance_halflife_hurst_composite},
    "mrp_147_mean_reversion_zscore_index": {"inputs": ["close"], "func": mrp_147_mean_reversion_zscore_index},
    "mrp_148_overshoot_reversion_alignment": {"inputs": ["close"], "func": mrp_148_overshoot_reversion_alignment},
    "mrp_149_capitulation_elastic_index": {"inputs": ["close"], "func": mrp_149_capitulation_elastic_index},
    "mrp_150_master_mean_reversion_potential_index": {"inputs": ["close"], "func": mrp_150_master_mean_reversion_potential_index},
}
