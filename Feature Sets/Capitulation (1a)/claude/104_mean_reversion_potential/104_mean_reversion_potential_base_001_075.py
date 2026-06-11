"""
104_mean_reversion_potential — Base Features 001-075
Domain: distance-from-equilibrium, reversion half-life and elastic stretch
        metrics. Captures the "potential energy" stored in a price that has
        been pulled far below its own equilibrium — the snap-back capacity
        that characterises an exhausted capitulation low.
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


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _zscore(s: pd.Series, w: int) -> pd.Series:
    """Z-score of a series over a trailing w-day window."""
    return _safe_div(s - _rolling_mean(s, w), _rolling_std(s, w))


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs()
    ], axis=1).max(axis=1)


def _ar1(s: pd.Series, w: int) -> pd.Series:
    """Rolling lag-1 autocorrelation of a series over window w."""
    return s.rolling(w, min_periods=max(5, w // 2)).corr(s.shift(1))


def _half_life(phi: pd.Series) -> pd.Series:
    """Mean-reversion half-life implied by an AR(1) coefficient phi."""
    p = phi.clip(lower=_EPS, upper=1 - 1e-4)
    return -np.log(2.0) / np.log(p)


def _hurst_rs(x: np.ndarray) -> float:
    """Single-window rescaled-range Hurst estimate (~0.5 = random walk)."""
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
    """Rolling rescaled-range Hurst exponent of daily log returns."""
    lr = _log_safe(close).diff(1)
    return lr.rolling(w, min_periods=max(16, w // 2)).apply(_hurst_rs, raw=True)


def _efficiency_ratio(close: pd.Series, w: int) -> pd.Series:
    """Kaufman efficiency ratio: net move over total path length (0-1)."""
    net = (close - close.shift(w)).abs()
    path = _rolling_sum(close.diff(1).abs(), w)
    return _safe_div(net, path)


def _variance_ratio(close: pd.Series, q: int, w: int) -> pd.Series:
    """Lo-MacKinlay-style variance ratio VR(q) over a trailing window w."""
    lr = _log_safe(close).diff(1)
    lrq = _log_safe(close).diff(q)
    var1 = _rolling_std(lr, w) ** 2
    varq = _rolling_std(lrq, w) ** 2
    return _safe_div(varq, var1 * q)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Distance from equilibrium ---

def mrp_001_stretch_from_sma21(close: pd.Series) -> pd.Series:
    """Deviation of close from its 21-day SMA in 21-day-std units."""
    ma = _rolling_mean(close, _TD_MON)
    return _safe_div(close - ma, _rolling_std(close, _TD_MON))


def mrp_002_stretch_from_sma63(close: pd.Series) -> pd.Series:
    """Deviation of close from its 63-day SMA in 63-day-std units."""
    ma = _rolling_mean(close, _TD_QTR)
    return _safe_div(close - ma, _rolling_std(close, _TD_QTR))


def mrp_003_stretch_from_sma126(close: pd.Series) -> pd.Series:
    """Deviation of close from its 126-day SMA in 126-day-std units."""
    ma = _rolling_mean(close, _TD_HALF)
    return _safe_div(close - ma, _rolling_std(close, _TD_HALF))


def mrp_004_stretch_from_sma252(close: pd.Series) -> pd.Series:
    """Deviation of close from its 252-day SMA in 252-day-std units."""
    ma = _rolling_mean(close, _TD_YEAR)
    return _safe_div(close - ma, _rolling_std(close, _TD_YEAR))


def mrp_005_stretch_from_ema63(close: pd.Series) -> pd.Series:
    """Deviation of close from its 63-day EMA in 63-day-std units."""
    ma = _ewm_mean(close, _TD_QTR)
    return _safe_div(close - ma, _rolling_std(close, _TD_QTR))


def mrp_006_distance_below_mean_252d(close: pd.Series) -> pd.Series:
    """Negative part of the percent deviation from the 252-day mean."""
    ma = _rolling_mean(close, _TD_YEAR)
    return _safe_div(close - ma, ma).clip(upper=0)


def mrp_007_stretch_atr_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Deviation of close from its 21-day SMA in ATR units."""
    atr = _rolling_mean(_tr(close, high, low), _TD_MON)
    return _safe_div(close - _rolling_mean(close, _TD_MON), atr)


def mrp_008_stretch_atr_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Deviation of close from its 63-day SMA in ATR units."""
    atr = _rolling_mean(_tr(close, high, low), _TD_QTR)
    return _safe_div(close - _rolling_mean(close, _TD_QTR), atr)


def mrp_009_max_stretch_below(close: pd.Series) -> pd.Series:
    """Most negative stretch across the 21/63/126/252-day equilibria."""
    parts = [_safe_div(close - _rolling_mean(close, w), _rolling_std(close, w))
             for w in (_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR)]
    return pd.concat(parts, axis=1).min(axis=1)


def mrp_010_mean_stretch(close: pd.Series) -> pd.Series:
    """Mean stretch across the 21/63/126/252-day equilibria."""
    parts = [_safe_div(close - _rolling_mean(close, w), _rolling_std(close, w))
             for w in (_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR)]
    return pd.concat(parts, axis=1).mean(axis=1)


def mrp_011_stretch_pctile_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of the 63-day stretch within a trailing 252-day window."""
    stretch = _safe_div(close - _rolling_mean(close, _TD_QTR), _rolling_std(close, _TD_QTR))
    return _rolling_rank_pct(stretch, _TD_YEAR)


def mrp_012_elastic_potential_energy(close: pd.Series) -> pd.Series:
    """Squared deviation from the 63-day mean (elastic potential energy)."""
    ma = _rolling_mean(close, _TD_QTR)
    dev = _safe_div(close - ma, ma)
    return dev * dev * np.sign(dev)


def mrp_013_distance_from_anchored_mean(close: pd.Series) -> pd.Series:
    """Percent deviation of close from its expanding (all-history) mean."""
    am = close.expanding(min_periods=5).mean()
    return _safe_div(close - am, am)


def mrp_014_deviation_from_log_trend(close: pd.Series) -> pd.Series:
    """Residual of log-close from its own 126-day moving average (log trend)."""
    lc = _log_safe(close)
    return lc - _rolling_mean(lc, _TD_HALF)


def mrp_015_stretch_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of the 63-day stretch over a trailing 252-day window."""
    stretch = _safe_div(close - _rolling_mean(close, _TD_QTR), _rolling_std(close, _TD_QTR))
    return _zscore(stretch, _TD_YEAR)


# --- Group B (016-030): Reversion half-life / AR(1) / autocorrelation ---

def mrp_016_ar1_returns_63d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of daily returns over a 63-day window."""
    return _ar1(_daily_ret(close), _TD_QTR)


def mrp_017_ar1_returns_252d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of daily returns over a 252-day window."""
    return _ar1(_daily_ret(close), _TD_YEAR)


def mrp_018_ar1_price_63d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of the close level over a 63-day window."""
    return _ar1(close, _TD_QTR)


def mrp_019_reversion_half_life_63d(close: pd.Series) -> pd.Series:
    """Mean-reversion half-life implied by 63-day AR(1) of detrended price."""
    detr = close - _rolling_mean(close, _TD_QTR)
    return _half_life(_ar1(detr, _TD_QTR))


def mrp_020_reversion_half_life_252d(close: pd.Series) -> pd.Series:
    """Mean-reversion half-life implied by 252-day AR(1) of detrended price."""
    detr = close - _rolling_mean(close, _TD_YEAR)
    return _half_life(_ar1(detr, _TD_YEAR))


def mrp_021_autocorr_lag1_21d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of daily returns over a 21-day window."""
    return _ar1(_daily_ret(close), _TD_MON)


def mrp_022_autocorr_lag5_63d(close: pd.Series) -> pd.Series:
    """Lag-5 autocorrelation of daily returns over a 63-day window."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=_TD_MON).corr(ret.shift(5))


def mrp_023_return_autocorr_negative_flag(close: pd.Series) -> pd.Series:
    """Flag: 63-day return autocorrelation is negative (mean-reverting)."""
    return (_ar1(_daily_ret(close), _TD_QTR) < 0).astype(float)


def mrp_024_variance_ratio_2_63d(close: pd.Series) -> pd.Series:
    """Variance ratio VR(2) over a 63-day window (<1 = mean-reverting)."""
    return _variance_ratio(close, 2, _TD_QTR)


def mrp_025_variance_ratio_5_252d(close: pd.Series) -> pd.Series:
    """Variance ratio VR(5) over a 252-day window."""
    return _variance_ratio(close, 5, _TD_YEAR)


def mrp_026_variance_ratio_10_252d(close: pd.Series) -> pd.Series:
    """Variance ratio VR(10) over a 252-day window."""
    return _variance_ratio(close, 10, _TD_YEAR)


def mrp_027_reversion_speed_proxy(close: pd.Series) -> pd.Series:
    """Reversion speed proxy: 1 minus the 63-day price AR(1) coefficient."""
    return 1.0 - _ar1(close, _TD_QTR)


def mrp_028_mean_reversion_strength(close: pd.Series) -> pd.Series:
    """Negative AR(1) of detrended price (positive = stronger reversion)."""
    detr = close - _rolling_mean(close, _TD_QTR)
    return -_ar1(detr, _TD_QTR)


def mrp_029_ou_theta_estimate(close: pd.Series) -> pd.Series:
    """Ornstein-Uhlenbeck reversion rate theta = -ln(AR1) of detrended price."""
    detr = close - _rolling_mean(close, _TD_QTR)
    phi = _ar1(detr, _TD_QTR).clip(lower=_EPS, upper=1 - 1e-4)
    return -np.log(phi)


def mrp_030_half_life_normalized(close: pd.Series) -> pd.Series:
    """63-day reversion half-life normalized by the 63-day window length."""
    detr = close - _rolling_mean(close, _TD_QTR)
    return _half_life(_ar1(detr, _TD_QTR)) / _TD_QTR


# --- Group C (031-045): Channel / band overshoot ---

def mrp_031_below_lower_bollinger_21d(close: pd.Series) -> pd.Series:
    """Distance below the 21-day lower Bollinger band, in std units."""
    z = _safe_div(close - _rolling_mean(close, _TD_MON), _rolling_std(close, _TD_MON))
    return (z + 2.0).clip(upper=0)


def mrp_032_below_lower_bollinger_63d(close: pd.Series) -> pd.Series:
    """Distance below the 63-day lower Bollinger band, in std units."""
    z = _safe_div(close - _rolling_mean(close, _TD_QTR), _rolling_std(close, _TD_QTR))
    return (z + 2.0).clip(upper=0)


def mrp_033_below_lower_keltner_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance below the 21-day lower Keltner channel, in ATR units."""
    atr = _rolling_mean(_tr(close, high, low), _TD_MON)
    pos = _safe_div(close - _rolling_mean(close, _TD_MON), atr)
    return (pos + 2.0).clip(upper=0)


def mrp_034_donchian_undershoot_63d(close: pd.Series) -> pd.Series:
    """Position of close within the 63-day Donchian channel (0 = at the low)."""
    lo = _rolling_min(close, _TD_QTR)
    hi = _rolling_max(close, _TD_QTR)
    return _safe_div(close - lo, hi - lo)


def mrp_035_band_overshoot_magnitude(close: pd.Series) -> pd.Series:
    """Magnitude of the 63-day stretch beyond the -2 std Bollinger band."""
    z = _safe_div(close - _rolling_mean(close, _TD_QTR), _rolling_std(close, _TD_QTR))
    return (-(z + 2.0)).clip(lower=0)


def mrp_036_band_overshoot_3std(close: pd.Series) -> pd.Series:
    """Magnitude of the 63-day stretch beyond the -3 std Bollinger band."""
    z = _safe_div(close - _rolling_mean(close, _TD_QTR), _rolling_std(close, _TD_QTR))
    return (-(z + 3.0)).clip(lower=0)


def mrp_037_pct_b_21d(close: pd.Series) -> pd.Series:
    """Bollinger %B over the 21-day window (0 = lower band, 1 = upper)."""
    ma = _rolling_mean(close, _TD_MON)
    sd = _rolling_std(close, _TD_MON)
    return _safe_div(close - (ma - 2.0 * sd), 4.0 * sd)


def mrp_038_pct_b_63d(close: pd.Series) -> pd.Series:
    """Bollinger %B over the 63-day window."""
    ma = _rolling_mean(close, _TD_QTR)
    sd = _rolling_std(close, _TD_QTR)
    return _safe_div(close - (ma - 2.0 * sd), 4.0 * sd)


def mrp_039_distance_to_midline_63d(close: pd.Series) -> pd.Series:
    """Percent distance from the 63-day channel midline (mid of high-low)."""
    mid = (_rolling_max(close, _TD_QTR) + _rolling_min(close, _TD_QTR)) / 2.0
    return _safe_div(close - mid, mid)


def mrp_040_keltner_position_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Position of close relative to its 63-day Keltner midline, in ATR units."""
    atr = _rolling_mean(_tr(close, high, low), _TD_QTR)
    return _safe_div(close - _rolling_mean(close, _TD_QTR), atr)


def mrp_041_band_walk_down_count(close: pd.Series) -> pd.Series:
    """Consecutive-day streak of close below the 21-day lower Bollinger band."""
    z = _safe_div(close - _rolling_mean(close, _TD_MON), _rolling_std(close, _TD_MON))
    f = (z < -2.0).astype(float)
    return f.groupby((f == 0).cumsum()).cumsum()


def mrp_042_overshoot_below_lower_atr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance below the 63-day Keltner lower channel, in ATR units."""
    atr = _rolling_mean(_tr(close, high, low), _TD_QTR)
    pos = _safe_div(close - _rolling_mean(close, _TD_QTR), atr)
    return (-(pos + 2.0)).clip(lower=0)


def mrp_043_channel_extension_252d(close: pd.Series) -> pd.Series:
    """Position of close within the 252-day Donchian channel (0 = low)."""
    lo = _rolling_min(close, _TD_YEAR)
    hi = _rolling_max(close, _TD_YEAR)
    return _safe_div(close - lo, hi - lo)


def mrp_044_mean_distance_below_all_bands(close: pd.Series) -> pd.Series:
    """Mean overshoot below the -2 std band across 21/63/126-day windows."""
    parts = []
    for w in (_TD_MON, _TD_QTR, _TD_HALF):
        z = _safe_div(close - _rolling_mean(close, w), _rolling_std(close, w))
        parts.append((-(z + 2.0)).clip(lower=0))
    return pd.concat(parts, axis=1).mean(axis=1)


def mrp_045_extreme_band_breach_flag(close: pd.Series) -> pd.Series:
    """Flag: close is beyond the -2.5 std Bollinger band on the 63-day window."""
    z = _safe_div(close - _rolling_mean(close, _TD_QTR), _rolling_std(close, _TD_QTR))
    return (z < -2.5).astype(float)


# --- Group D (046-060): Stretch dynamics & overshoot vs history ---

def mrp_046_stretch_vs_trailing_min(close: pd.Series) -> pd.Series:
    """Current 63-day stretch relative to its trailing 252-day minimum."""
    stretch = _safe_div(close - _rolling_mean(close, _TD_QTR), _rolling_std(close, _TD_QTR))
    return _safe_div(stretch, _rolling_min(stretch, _TD_YEAR))


def mrp_047_stretch_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of the 252-day stretch within a trailing 252-day window."""
    stretch = _safe_div(close - _rolling_mean(close, _TD_YEAR), _rolling_std(close, _TD_YEAR))
    return _rolling_rank_pct(stretch, _TD_YEAR)


def mrp_048_max_historical_overshoot_ratio(close: pd.Series) -> pd.Series:
    """Current overshoot below the band vs the worst overshoot in 252 days."""
    z = _safe_div(close - _rolling_mean(close, _TD_QTR), _rolling_std(close, _TD_QTR))
    overshoot = (-(z + 2.0)).clip(lower=0)
    return _safe_div(overshoot, _rolling_max(overshoot, _TD_YEAR))


def mrp_049_stretch_504d_zscore(close: pd.Series) -> pd.Series:
    """Z-score of the 63-day stretch over a trailing 504-day window."""
    stretch = _safe_div(close - _rolling_mean(close, _TD_QTR), _rolling_std(close, _TD_QTR))
    return _zscore(stretch, 504)


def mrp_050_deviation_volume_weighted(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Deviation from the 63-day mean weighted by relative trading volume."""
    ma = _rolling_mean(close, _TD_QTR)
    dev = _safe_div(close - ma, ma)
    v_norm = _safe_div(volume, _rolling_mean(volume, _TD_QTR))
    return dev * v_norm


def mrp_051_reversion_gap(close: pd.Series) -> pd.Series:
    """Percent gap between the close and its 126-day equilibrium mean."""
    ma = _rolling_mean(close, _TD_HALF)
    return _safe_div(ma - close, ma)


def mrp_052_reversion_gap_atr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Gap between close and its 126-day mean, expressed in ATR units."""
    atr = _rolling_mean(_tr(close, high, low), _TD_QTR)
    return _safe_div(_rolling_mean(close, _TD_HALF) - close, atr)


def mrp_053_cumulative_deviation_63d(close: pd.Series) -> pd.Series:
    """Sum over 63 days of the percent deviation from the 63-day mean."""
    ma = _rolling_mean(close, _TD_QTR)
    dev = _safe_div(close - ma, ma)
    return _rolling_sum(dev, _TD_QTR)


def mrp_054_time_below_mean_252d(close: pd.Series) -> pd.Series:
    """Fraction of the last 252 days the close sat below its 252-day mean."""
    below = (close < _rolling_mean(close, _TD_YEAR)).astype(float)
    return _rolling_mean(below, _TD_YEAR)


def mrp_055_longest_below_mean_streak(close: pd.Series) -> pd.Series:
    """Current consecutive-day streak of close below its 126-day mean."""
    f = (close < _rolling_mean(close, _TD_HALF)).astype(float)
    return f.groupby((f == 0).cumsum()).cumsum()


def mrp_056_distance_from_vwap_proxy(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percent deviation of close from the 63-day volume-weighted mean price."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_QTR), _rolling_sum(volume, _TD_QTR))
    return _safe_div(close - vwap, vwap)


def mrp_057_vwap_deviation_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percent deviation of close from the 252-day volume-weighted mean price."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))
    return _safe_div(close - vwap, vwap)


def mrp_058_displacement_from_median_252d(close: pd.Series) -> pd.Series:
    """Percent deviation of close from its 252-day rolling median."""
    med = _rolling_median(close, _TD_YEAR)
    return _safe_div(close - med, med)


def mrp_059_overshoot_persistence(close: pd.Series) -> pd.Series:
    """Fraction of last 63 days the close was beyond the -2 std band."""
    z = _safe_div(close - _rolling_mean(close, _TD_QTR), _rolling_std(close, _TD_QTR))
    return _rolling_mean((z < -2.0).astype(float), _TD_QTR)


def mrp_060_stretch_distance_from_min(close: pd.Series) -> pd.Series:
    """Gap between the current 63-day stretch and its trailing 252-day min."""
    stretch = _safe_div(close - _rolling_mean(close, _TD_QTR), _rolling_std(close, _TD_QTR))
    return stretch - _rolling_min(stretch, _TD_YEAR)


# --- Group E (061-075): Hurst / efficiency / composites ---

def mrp_061_hurst_exponent_63d(close: pd.Series) -> pd.Series:
    """Rescaled-range Hurst exponent of log returns over a 63-day window."""
    return _hurst(close, _TD_QTR)


def mrp_062_hurst_exponent_126d(close: pd.Series) -> pd.Series:
    """Rescaled-range Hurst exponent of log returns over a 126-day window."""
    return _hurst(close, _TD_HALF)


def mrp_063_mean_reverting_regime_flag(close: pd.Series) -> pd.Series:
    """Flag: 126-day Hurst exponent below 0.5 (mean-reverting regime)."""
    return (_hurst(close, _TD_HALF) < 0.5).astype(float)


def mrp_064_detrended_fluctuation_proxy(close: pd.Series) -> pd.Series:
    """Std of detrended log-price (deviation from 63-day mean log-price)."""
    lc = _log_safe(close)
    detr = lc - _rolling_mean(lc, _TD_QTR)
    return _rolling_std(detr, _TD_QTR)


def mrp_065_efficiency_ratio_63d(close: pd.Series) -> pd.Series:
    """Kaufman efficiency ratio over 63 days (low = choppy / mean-reverting)."""
    return _efficiency_ratio(close, _TD_QTR)


def mrp_066_efficiency_ratio_21d(close: pd.Series) -> pd.Series:
    """Kaufman efficiency ratio over 21 days."""
    return _efficiency_ratio(close, _TD_MON)


def mrp_067_range_vs_displacement_63d(close: pd.Series) -> pd.Series:
    """Total path length vs net displacement over 63 days (1/efficiency)."""
    net = (close - close.shift(_TD_QTR)).abs()
    path = _rolling_sum(close.diff(1).abs(), _TD_QTR)
    return _safe_div(path, net)


def mrp_068_zigzag_ratio_63d(close: pd.Series) -> pd.Series:
    """Direction-change frequency of daily returns over 63 days (choppiness)."""
    sign_change = (np.sign(close.diff(1)) != np.sign(close.diff(1).shift(1))).astype(float)
    return _rolling_mean(sign_change, _TD_QTR)


def mrp_069_reversion_potential_score(close: pd.Series) -> pd.Series:
    """Overshoot magnitude times reversion speed (stored snap-back energy)."""
    z = _safe_div(close - _rolling_mean(close, _TD_QTR), _rolling_std(close, _TD_QTR))
    overshoot = (-z).clip(lower=0)
    speed = (1.0 - _ar1(close, _TD_QTR)).clip(lower=0)
    return overshoot * speed


def mrp_070_elastic_snapback_potential(close: pd.Series) -> pd.Series:
    """Gap to the 126-day mean scaled by mean-reversion strength."""
    gap = _safe_div(_rolling_mean(close, _TD_HALF) - close, _rolling_mean(close, _TD_HALF))
    detr = close - _rolling_mean(close, _TD_QTR)
    strength = (-_ar1(detr, _TD_QTR)).clip(lower=0)
    return gap.clip(lower=0) * (0.5 + strength)


def mrp_071_distance_x_halflife(close: pd.Series) -> pd.Series:
    """Distance below the 63-day mean divided by the reversion half-life."""
    ma = _rolling_mean(close, _TD_QTR)
    dist = _safe_div(ma - close, ma).clip(lower=0)
    detr = close - ma
    hl = _half_life(_ar1(detr, _TD_QTR)).clip(lower=1.0)
    return _safe_div(dist, hl)


def mrp_072_oversold_reversion_setup(close: pd.Series) -> pd.Series:
    """Below-band overshoot present in a confirmed mean-reverting regime."""
    z = _safe_div(close - _rolling_mean(close, _TD_QTR), _rolling_std(close, _TD_QTR))
    overshoot = (-(z + 2.0)).clip(lower=0)
    reverting = (_hurst(close, _TD_HALF) < 0.5).astype(float)
    return overshoot * reverting


def mrp_073_deep_undershoot_flag(close: pd.Series) -> pd.Series:
    """Flag: 63-day stretch is beyond -3 std (deep elastic undershoot)."""
    z = _safe_div(close - _rolling_mean(close, _TD_QTR), _rolling_std(close, _TD_QTR))
    return (z < -3.0).astype(float)


def mrp_074_mean_reversion_capitulation_score(close: pd.Series) -> pd.Series:
    """Composite: overshoot depth, time below mean and reversion strength."""
    z = _safe_div(close - _rolling_mean(close, _TD_QTR), _rolling_std(close, _TD_QTR))
    overshoot = (-z).clip(lower=0) / 3.0
    below = _rolling_mean((close < _rolling_mean(close, _TD_YEAR)).astype(float), _TD_YEAR)
    detr = close - _rolling_mean(close, _TD_QTR)
    strength = (-_ar1(detr, _TD_QTR)).clip(lower=0)
    return overshoot * (0.5 + below) * (0.5 + strength)


def mrp_075_mean_reversion_potential_index(close: pd.Series) -> pd.Series:
    """Master index: equilibrium gap, overshoot and reversion speed combined."""
    gap = _safe_div(_rolling_mean(close, _TD_HALF) - close,
                    _rolling_mean(close, _TD_HALF)).clip(lower=0)
    z = _safe_div(close - _rolling_mean(close, _TD_QTR), _rolling_std(close, _TD_QTR))
    overshoot = (-z).clip(lower=0) / 3.0
    speed = (1.0 - _ar1(close, _TD_QTR)).clip(lower=0, upper=2.0) / 2.0
    return (gap + overshoot) * (0.5 + speed)


# ── Registry ──────────────────────────────────────────────────────────────────

MEAN_REVERSION_POTENTIAL_REGISTRY_001_075 = {
    "mrp_001_stretch_from_sma21": {"inputs": ["close"], "func": mrp_001_stretch_from_sma21},
    "mrp_002_stretch_from_sma63": {"inputs": ["close"], "func": mrp_002_stretch_from_sma63},
    "mrp_003_stretch_from_sma126": {"inputs": ["close"], "func": mrp_003_stretch_from_sma126},
    "mrp_004_stretch_from_sma252": {"inputs": ["close"], "func": mrp_004_stretch_from_sma252},
    "mrp_005_stretch_from_ema63": {"inputs": ["close"], "func": mrp_005_stretch_from_ema63},
    "mrp_006_distance_below_mean_252d": {"inputs": ["close"], "func": mrp_006_distance_below_mean_252d},
    "mrp_007_stretch_atr_21d": {"inputs": ["close", "high", "low"], "func": mrp_007_stretch_atr_21d},
    "mrp_008_stretch_atr_63d": {"inputs": ["close", "high", "low"], "func": mrp_008_stretch_atr_63d},
    "mrp_009_max_stretch_below": {"inputs": ["close"], "func": mrp_009_max_stretch_below},
    "mrp_010_mean_stretch": {"inputs": ["close"], "func": mrp_010_mean_stretch},
    "mrp_011_stretch_pctile_252d": {"inputs": ["close"], "func": mrp_011_stretch_pctile_252d},
    "mrp_012_elastic_potential_energy": {"inputs": ["close"], "func": mrp_012_elastic_potential_energy},
    "mrp_013_distance_from_anchored_mean": {"inputs": ["close"], "func": mrp_013_distance_from_anchored_mean},
    "mrp_014_deviation_from_log_trend": {"inputs": ["close"], "func": mrp_014_deviation_from_log_trend},
    "mrp_015_stretch_zscore_252d": {"inputs": ["close"], "func": mrp_015_stretch_zscore_252d},
    "mrp_016_ar1_returns_63d": {"inputs": ["close"], "func": mrp_016_ar1_returns_63d},
    "mrp_017_ar1_returns_252d": {"inputs": ["close"], "func": mrp_017_ar1_returns_252d},
    "mrp_018_ar1_price_63d": {"inputs": ["close"], "func": mrp_018_ar1_price_63d},
    "mrp_019_reversion_half_life_63d": {"inputs": ["close"], "func": mrp_019_reversion_half_life_63d},
    "mrp_020_reversion_half_life_252d": {"inputs": ["close"], "func": mrp_020_reversion_half_life_252d},
    "mrp_021_autocorr_lag1_21d": {"inputs": ["close"], "func": mrp_021_autocorr_lag1_21d},
    "mrp_022_autocorr_lag5_63d": {"inputs": ["close"], "func": mrp_022_autocorr_lag5_63d},
    "mrp_023_return_autocorr_negative_flag": {"inputs": ["close"], "func": mrp_023_return_autocorr_negative_flag},
    "mrp_024_variance_ratio_2_63d": {"inputs": ["close"], "func": mrp_024_variance_ratio_2_63d},
    "mrp_025_variance_ratio_5_252d": {"inputs": ["close"], "func": mrp_025_variance_ratio_5_252d},
    "mrp_026_variance_ratio_10_252d": {"inputs": ["close"], "func": mrp_026_variance_ratio_10_252d},
    "mrp_027_reversion_speed_proxy": {"inputs": ["close"], "func": mrp_027_reversion_speed_proxy},
    "mrp_028_mean_reversion_strength": {"inputs": ["close"], "func": mrp_028_mean_reversion_strength},
    "mrp_029_ou_theta_estimate": {"inputs": ["close"], "func": mrp_029_ou_theta_estimate},
    "mrp_030_half_life_normalized": {"inputs": ["close"], "func": mrp_030_half_life_normalized},
    "mrp_031_below_lower_bollinger_21d": {"inputs": ["close"], "func": mrp_031_below_lower_bollinger_21d},
    "mrp_032_below_lower_bollinger_63d": {"inputs": ["close"], "func": mrp_032_below_lower_bollinger_63d},
    "mrp_033_below_lower_keltner_21d": {"inputs": ["close", "high", "low"], "func": mrp_033_below_lower_keltner_21d},
    "mrp_034_donchian_undershoot_63d": {"inputs": ["close"], "func": mrp_034_donchian_undershoot_63d},
    "mrp_035_band_overshoot_magnitude": {"inputs": ["close"], "func": mrp_035_band_overshoot_magnitude},
    "mrp_036_band_overshoot_3std": {"inputs": ["close"], "func": mrp_036_band_overshoot_3std},
    "mrp_037_pct_b_21d": {"inputs": ["close"], "func": mrp_037_pct_b_21d},
    "mrp_038_pct_b_63d": {"inputs": ["close"], "func": mrp_038_pct_b_63d},
    "mrp_039_distance_to_midline_63d": {"inputs": ["close"], "func": mrp_039_distance_to_midline_63d},
    "mrp_040_keltner_position_63d": {"inputs": ["close", "high", "low"], "func": mrp_040_keltner_position_63d},
    "mrp_041_band_walk_down_count": {"inputs": ["close"], "func": mrp_041_band_walk_down_count},
    "mrp_042_overshoot_below_lower_atr": {"inputs": ["close", "high", "low"], "func": mrp_042_overshoot_below_lower_atr},
    "mrp_043_channel_extension_252d": {"inputs": ["close"], "func": mrp_043_channel_extension_252d},
    "mrp_044_mean_distance_below_all_bands": {"inputs": ["close"], "func": mrp_044_mean_distance_below_all_bands},
    "mrp_045_extreme_band_breach_flag": {"inputs": ["close"], "func": mrp_045_extreme_band_breach_flag},
    "mrp_046_stretch_vs_trailing_min": {"inputs": ["close"], "func": mrp_046_stretch_vs_trailing_min},
    "mrp_047_stretch_rank_252d": {"inputs": ["close"], "func": mrp_047_stretch_rank_252d},
    "mrp_048_max_historical_overshoot_ratio": {"inputs": ["close"], "func": mrp_048_max_historical_overshoot_ratio},
    "mrp_049_stretch_504d_zscore": {"inputs": ["close"], "func": mrp_049_stretch_504d_zscore},
    "mrp_050_deviation_volume_weighted": {"inputs": ["close", "volume"], "func": mrp_050_deviation_volume_weighted},
    "mrp_051_reversion_gap": {"inputs": ["close"], "func": mrp_051_reversion_gap},
    "mrp_052_reversion_gap_atr": {"inputs": ["close", "high", "low"], "func": mrp_052_reversion_gap_atr},
    "mrp_053_cumulative_deviation_63d": {"inputs": ["close"], "func": mrp_053_cumulative_deviation_63d},
    "mrp_054_time_below_mean_252d": {"inputs": ["close"], "func": mrp_054_time_below_mean_252d},
    "mrp_055_longest_below_mean_streak": {"inputs": ["close"], "func": mrp_055_longest_below_mean_streak},
    "mrp_056_distance_from_vwap_proxy": {"inputs": ["close", "volume"], "func": mrp_056_distance_from_vwap_proxy},
    "mrp_057_vwap_deviation_252d": {"inputs": ["close", "volume"], "func": mrp_057_vwap_deviation_252d},
    "mrp_058_displacement_from_median_252d": {"inputs": ["close"], "func": mrp_058_displacement_from_median_252d},
    "mrp_059_overshoot_persistence": {"inputs": ["close"], "func": mrp_059_overshoot_persistence},
    "mrp_060_stretch_distance_from_min": {"inputs": ["close"], "func": mrp_060_stretch_distance_from_min},
    "mrp_061_hurst_exponent_63d": {"inputs": ["close"], "func": mrp_061_hurst_exponent_63d},
    "mrp_062_hurst_exponent_126d": {"inputs": ["close"], "func": mrp_062_hurst_exponent_126d},
    "mrp_063_mean_reverting_regime_flag": {"inputs": ["close"], "func": mrp_063_mean_reverting_regime_flag},
    "mrp_064_detrended_fluctuation_proxy": {"inputs": ["close"], "func": mrp_064_detrended_fluctuation_proxy},
    "mrp_065_efficiency_ratio_63d": {"inputs": ["close"], "func": mrp_065_efficiency_ratio_63d},
    "mrp_066_efficiency_ratio_21d": {"inputs": ["close"], "func": mrp_066_efficiency_ratio_21d},
    "mrp_067_range_vs_displacement_63d": {"inputs": ["close"], "func": mrp_067_range_vs_displacement_63d},
    "mrp_068_zigzag_ratio_63d": {"inputs": ["close"], "func": mrp_068_zigzag_ratio_63d},
    "mrp_069_reversion_potential_score": {"inputs": ["close"], "func": mrp_069_reversion_potential_score},
    "mrp_070_elastic_snapback_potential": {"inputs": ["close"], "func": mrp_070_elastic_snapback_potential},
    "mrp_071_distance_x_halflife": {"inputs": ["close"], "func": mrp_071_distance_x_halflife},
    "mrp_072_oversold_reversion_setup": {"inputs": ["close"], "func": mrp_072_oversold_reversion_setup},
    "mrp_073_deep_undershoot_flag": {"inputs": ["close"], "func": mrp_073_deep_undershoot_flag},
    "mrp_074_mean_reversion_capitulation_score": {"inputs": ["close"], "func": mrp_074_mean_reversion_capitulation_score},
    "mrp_075_mean_reversion_potential_index": {"inputs": ["close"], "func": mrp_075_mean_reversion_potential_index},
}
