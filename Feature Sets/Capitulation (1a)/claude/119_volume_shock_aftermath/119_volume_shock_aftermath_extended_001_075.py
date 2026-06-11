"""
119_volume_shock_aftermath — Extended Features 001-075
Domain: volume-shock aftermath — deeper variants, multi-threshold composites,
        cross-window confluences, nonlinear shock metrics, regime-aware aftermath
        indicators, and higher-order volume-price interaction features
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _vol_zscore(volume: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(volume, w)
    s = _rolling_std(volume, w)
    return _safe_div(volume - m, s.clip(lower=_EPS))


def _shock_flag(volume: pd.Series, w: int, z_thresh: float = 2.0) -> pd.Series:
    return (_vol_zscore(volume, w) > z_thresh).astype(float)


def _days_since_last_shock(volume: pd.Series, w: int, z_thresh: float = 2.0) -> pd.Series:
    flag = _shock_flag(volume, w, z_thresh)
    idx = pd.Series(np.arange(len(flag), dtype=float), index=flag.index)
    last = idx.where(flag == 1.0).ffill().fillna(-1.0)
    elapsed = idx - last
    return elapsed.where(last >= 0.0, np.nan)


def _price_return_since_shock(close: pd.Series, volume: pd.Series,
                               w: int, z_thresh: float = 2.0) -> pd.Series:
    flag = _shock_flag(volume, w, z_thresh)
    shock_close = close.where(flag == 1.0).ffill()
    return _safe_div(close - shock_close, shock_close.clip(lower=_EPS))


def _typical_price(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (high + low + close) / 3.0


def _dollar_volume(close: pd.Series, volume: pd.Series) -> pd.Series:
    return close * volume


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── Extended Feature Functions 001-075 ───────────────────────────────────────

# --- Group A (001-010): Multi-threshold shock cross-confirmation ---

def vsa_ext_001_shock_triple_confirm_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: all three windows (21d/63d/252d) simultaneously show z>2 shock."""
    f21 = _shock_flag(volume, _TD_MON, 2.0)
    f63 = _shock_flag(volume, _TD_QTR, 2.0)
    f252 = _shock_flag(volume, _TD_YEAR, 2.0)
    return ((f21 == 1.0) & (f63 == 1.0) & (f252 == 1.0)).astype(float)


def vsa_ext_002_shock_agreement_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of windows (21d, 63d, 252d) with z>2 shock today (0-3 scale)."""
    f21 = _shock_flag(volume, _TD_MON, 2.0)
    f63 = _shock_flag(volume, _TD_QTR, 2.0)
    f252 = _shock_flag(volume, _TD_YEAR, 2.0)
    return f21 + f63 + f252


def vsa_ext_003_shock_score_z3_triple(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of windows (21d, 63d, 252d) with z>3 severe shock today."""
    f21 = _shock_flag(volume, _TD_MON, 3.0)
    f63 = _shock_flag(volume, _TD_QTR, 3.0)
    f252 = _shock_flag(volume, _TD_YEAR, 3.0)
    return f21 + f63 + f252


def vsa_ext_004_days_since_shock_min_window(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Min of days-since-shock across 21d and 63d windows (most recent shock)."""
    d21 = _days_since_last_shock(volume, _TD_MON, 2.0)
    d63 = _days_since_last_shock(volume, _TD_QTR, 2.0)
    return pd.concat([d21, d63], axis=1).min(axis=1)


def vsa_ext_005_shock_count_trend_21d_vs_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day shock density minus 63-day shock density (recent vs long-term rate)."""
    d21 = _rolling_sum(_shock_flag(volume, _TD_MON, 2.0), _TD_MON) / _TD_MON
    d63 = _rolling_sum(_shock_flag(volume, _TD_QTR, 2.0), _TD_QTR) / _TD_QTR
    return d21 - d63


def vsa_ext_006_multi_window_shock_recency_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Weighted recency: 1/(d21+1)*0.6 + 1/(d63+1)*0.4 (short-term weighted)."""
    d21 = _days_since_last_shock(volume, _TD_MON, 2.0).fillna(999.0)
    d63 = _days_since_last_shock(volume, _TD_QTR, 2.0).fillna(999.0)
    r21 = 1.0 / (d21 + 1.0)
    r63 = 1.0 / (d63 + 1.0)
    return 0.6 * r21 + 0.4 * r63


def vsa_ext_007_shock_and_price_decline_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days in 21d with shock AND negative close return simultaneously."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    neg = (close.pct_change(1) < 0.0).astype(float)
    return _rolling_sum(flag * neg, _TD_MON)


def vsa_ext_008_shock_and_price_decline_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days in 63d with shock AND negative close return."""
    flag = _shock_flag(volume, _TD_QTR, 2.0)
    neg = (close.pct_change(1) < 0.0).astype(float)
    return _rolling_sum(flag * neg, _TD_QTR)


def vsa_ext_009_shock_amplitude_sum_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (vol_zscore - 2) for all shock days in 21d (above-threshold amplitude)."""
    z = _vol_zscore(volume, _TD_MON)
    excess = (z - 2.0).clip(lower=0.0) * _shock_flag(volume, _TD_MON, 2.0)
    return _rolling_sum(excess, _TD_MON)


def vsa_ext_010_shock_amplitude_sum_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (vol_zscore - 2) for all shock days in 63d."""
    z = _vol_zscore(volume, _TD_QTR)
    excess = (z - 2.0).clip(lower=0.0) * _shock_flag(volume, _TD_QTR, 2.0)
    return _rolling_sum(excess, _TD_QTR)


# --- Group B (011-020): Nonlinear and regime-aware shock metrics ---

def vsa_ext_011_vol_zscore_squared_21d_sum(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of squared vol z-scores over 21 days (nonlinear shock energy)."""
    z = _vol_zscore(volume, _TD_MON)
    return _rolling_sum(z ** 2, _TD_MON)


def vsa_ext_012_vol_zscore_cubed_21d_sum(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of signed cubed vol z-scores (skewness measure; large positives dominate)."""
    z = _vol_zscore(volume, _TD_MON)
    return _rolling_sum(z ** 3, _TD_MON)


def vsa_ext_013_shock_exponential_decay_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Exponentially decayed shock score: exp(-days_since_shock / 10)."""
    d = _days_since_last_shock(volume, _TD_MON, 2.0).fillna(999.0)
    return np.exp(-d / 10.0)


def vsa_ext_014_shock_exponential_decay_score_slow(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slowly decayed shock score: exp(-days_since_shock / 21)."""
    d = _days_since_last_shock(volume, _TD_MON, 2.0).fillna(999.0)
    return np.exp(-d / 21.0)


def vsa_ext_015_vol_regime_flag_elevated(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: 21d mean volume > 1.5x 252d mean volume (elevated volume regime)."""
    r = _safe_div(_rolling_mean(volume, _TD_MON),
                  _rolling_mean(volume, _TD_YEAR).clip(lower=_EPS))
    return (r > 1.5).astype(float)


def vsa_ext_016_vol_regime_flag_depressed(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: 21d mean volume < 0.7x 252d mean volume (depressed regime)."""
    r = _safe_div(_rolling_mean(volume, _TD_MON),
                  _rolling_mean(volume, _TD_YEAR).clip(lower=_EPS))
    return (r < 0.7).astype(float)


def vsa_ext_017_vol_high_regime_shock_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Shock count in 63d during elevated-volume-regime days only."""
    elevated = (_safe_div(_rolling_mean(volume, _TD_MON),
                          _rolling_mean(volume, _TD_YEAR).clip(lower=_EPS)) > 1.2).astype(float)
    shock = _shock_flag(volume, _TD_QTR, 2.0)
    return _rolling_sum(elevated * shock, _TD_QTR)


def vsa_ext_018_vol_zscore_log1p_21d_sum(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of log1p(max(z,0)) over 21 days (log-compressed shock intensity)."""
    z = _vol_zscore(volume, _TD_MON).clip(lower=0.0)
    return _rolling_sum(np.log1p(z), _TD_MON)


def vsa_ext_019_shock_negative_price_product_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d sum of (shock z-score * negative return size); capitulation signal."""
    z = _vol_zscore(volume, _TD_MON).clip(lower=0.0)
    neg_ret = close.pct_change(1).clip(upper=0.0).abs()
    return _rolling_sum(z * neg_ret, _TD_MON)


def vsa_ext_020_shock_at_price_low_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: last shock day coincided with a 21d price low (capitulation pattern)."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    low21 = _rolling_min(close, _TD_MON)
    at_low = (close <= low21 * 1.001).astype(float)
    shock_at_low = (flag == 1.0) & (at_low == 1.0)
    return shock_at_low.astype(float).where(flag == 1.0).ffill().fillna(0.0)


# --- Group C (021-030): VWAP and typical-price deeper variants ---

def vsa_ext_021_vwap_63d(close: pd.Series, high: pd.Series,
                          low: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day VWAP (volume-weighted average typical price)."""
    tp = _typical_price(high, low, close)
    return _safe_div(_rolling_sum(tp * volume, _TD_QTR),
                     _rolling_sum(volume, _TD_QTR).clip(lower=_EPS))


def vsa_ext_022_close_vs_vwap_126d(close: pd.Series, high: pd.Series,
                                    low: pd.Series, volume: pd.Series) -> pd.Series:
    """Close relative to 126-day VWAP: (close - vwap) / vwap."""
    tp = _typical_price(high, low, close)
    vwap = _safe_div(_rolling_sum(tp * volume, _TD_HALF),
                     _rolling_sum(volume, _TD_HALF).clip(lower=_EPS))
    return _safe_div(close - vwap, vwap.clip(lower=_EPS))


def vsa_ext_023_shock_day_close_vs_vwap_63d(close: pd.Series, high: pd.Series,
                                              low: pd.Series, volume: pd.Series) -> pd.Series:
    """Close vs 63d VWAP on last shock day (63d/z2)."""
    flag = _shock_flag(volume, _TD_QTR, 2.0)
    tp = _typical_price(high, low, close)
    vwap = _safe_div(_rolling_sum(tp * volume, _TD_QTR),
                     _rolling_sum(volume, _TD_QTR).clip(lower=_EPS))
    dev = _safe_div(close - vwap, vwap.clip(lower=_EPS))
    return dev.where(flag == 1.0).ffill()


def vsa_ext_024_vol_weighted_avg_return_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average daily return over trailing 5 days."""
    ret = close.pct_change(1).fillna(0.0)
    return _safe_div(_rolling_sum(ret * volume, _TD_WEEK),
                     _rolling_sum(volume, _TD_WEEK).clip(lower=_EPS))


def vsa_ext_025_vol_weighted_range_21d(close: pd.Series, high: pd.Series,
                                        low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day volume-weighted average bar range (normalized by close)."""
    bar_range = _safe_div(high - low, close.clip(lower=_EPS))
    return _safe_div(_rolling_sum(bar_range * volume, _TD_MON),
                     _rolling_sum(volume, _TD_MON).clip(lower=_EPS))


def vsa_ext_026_vwap_deviation_zscore_21d(close: pd.Series, high: pd.Series,
                                           low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of close vs 21d VWAP deviation over trailing 63 days."""
    tp = _typical_price(high, low, close)
    vwap = _safe_div(_rolling_sum(tp * volume, _TD_MON),
                     _rolling_sum(volume, _TD_MON).clip(lower=_EPS))
    dev = _safe_div(close - vwap, vwap.clip(lower=_EPS))
    m = _rolling_mean(dev, _TD_QTR)
    s = _rolling_std(dev, _TD_QTR)
    return _safe_div(dev - m, s.clip(lower=_EPS))


def vsa_ext_027_shock_day_vol_to_vwap_vol(close: pd.Series, high: pd.Series,
                                           low: pd.Series, volume: pd.Series) -> pd.Series:
    """Shock-day volume / 21d VWAP-period volume (shock size vs average)."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    shock_vol = volume.where(flag == 1.0).ffill()
    avg_vol = _rolling_mean(volume, _TD_MON)
    return _safe_div(shock_vol, avg_vol.clip(lower=_EPS))


def vsa_ext_028_post_shock_below_vwap_consec(close: pd.Series, high: pd.Series,
                                              low: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days close below 21d VWAP (bearish post-shock regime)."""
    tp = _typical_price(high, low, close)
    vwap = _safe_div(_rolling_sum(tp * volume, _TD_MON),
                     _rolling_sum(volume, _TD_MON).clip(lower=_EPS))
    return _consec_streak((close < vwap).astype(bool))


def vsa_ext_029_vwap_21d_trend_slope(close: pd.Series, high: pd.Series,
                                      low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day OLS slope of 21d VWAP (is VWAP itself declining?)."""
    tp = _typical_price(high, low, close)
    vwap = _safe_div(_rolling_sum(tp * volume, _TD_MON),
                     _rolling_sum(volume, _TD_MON).clip(lower=_EPS))
    return _linslope(vwap, _TD_MON)


def vsa_ext_030_shock_day_close_pct_from_low(close: pd.Series, high: pd.Series,
                                              low: pd.Series, volume: pd.Series) -> pd.Series:
    """On last shock day: (close - low) / (high - low) — where in range did close."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    hl = (high - low).replace(0, np.nan)
    cl = _safe_div(close - low, hl)
    return cl.where(flag == 1.0).ffill()


# --- Group D (031-040): Extended OBV and flow ---

def vsa_ext_031_obv_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of daily OBV change vs its 21-day distribution."""
    obv_delta = np.sign(close.diff(1)) * volume
    return _vol_zscore(obv_delta, _TD_MON)


def vsa_ext_032_obv_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of daily OBV change vs its 63-day distribution."""
    obv_delta = np.sign(close.diff(1)) * volume
    return _vol_zscore(obv_delta, _TD_QTR)


def vsa_ext_033_obv_expanding_percentile(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of OBV."""
    obv = (np.sign(close.diff(1)) * volume).fillna(0.0).cumsum()
    return obv.expanding(min_periods=5).rank(pct=True)


def vsa_ext_034_vol_flow_imbalance_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(Up-vol - Down-vol) / Total-vol over 21 days; in [-1, 1]."""
    up_vol = _rolling_sum((close.diff(1) > 0.0).astype(float) * volume, _TD_MON)
    dn_vol = _rolling_sum((close.diff(1) < 0.0).astype(float) * volume, _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    return _safe_div(up_vol - dn_vol, total_vol.clip(lower=_EPS))


def vsa_ext_035_vol_flow_imbalance_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(Up-vol - Down-vol) / Total-vol over 63 days."""
    up_vol = _rolling_sum((close.diff(1) > 0.0).astype(float) * volume, _TD_QTR)
    dn_vol = _rolling_sum((close.diff(1) < 0.0).astype(float) * volume, _TD_QTR)
    total_vol = _rolling_sum(volume, _TD_QTR)
    return _safe_div(up_vol - dn_vol, total_vol.clip(lower=_EPS))


def vsa_ext_036_neg_flow_imbalance_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21d negative volume flow vs 63d baseline."""
    dn_vol = _rolling_sum((close.diff(1) < 0.0).astype(float) * volume, _TD_MON)
    return _vol_zscore(dn_vol, _TD_QTR)


def vsa_ext_037_vol_flow_imbalance_trend_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day volume flow imbalance (velocity of flow change)."""
    up_vol = _rolling_sum((close.diff(1) > 0.0).astype(float) * volume, _TD_MON)
    dn_vol = _rolling_sum((close.diff(1) < 0.0).astype(float) * volume, _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    imb = _safe_div(up_vol - dn_vol, total_vol.clip(lower=_EPS))
    return imb.diff(_TD_WEEK)


def vsa_ext_038_shock_negative_flow_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: shock day had negative OBV flow (down-volume dominated shock)."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    obv_delta = np.sign(close.diff(1)) * volume
    neg_flow = (obv_delta < 0.0).astype(float)
    shock_neg = (flag == 1.0) & (neg_flow == 1.0)
    return shock_neg.astype(float).where(flag == 1.0).ffill().fillna(0.0)


def vsa_ext_039_shock_negative_flow_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of shock days in 63d with negative OBV flow."""
    flag = _shock_flag(volume, _TD_QTR, 2.0)
    obv_delta = np.sign(close.diff(1)) * volume
    neg_flow = (obv_delta < 0.0).astype(float)
    return _rolling_sum(flag * neg_flow, _TD_QTR)


def vsa_ext_040_obv_pct_change_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day percentage change in OBV (cumulative directional volume change)."""
    obv = (np.sign(close.diff(1)) * volume).fillna(0.0).cumsum()
    prev = obv.shift(_TD_MON)
    return _safe_div(obv - prev, prev.abs().clip(lower=_EPS))


# --- Group E (041-050): Extended price aftermath metrics ---

def vsa_ext_041_price_recovery_since_shock_63dz3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Return since last severe shock day (63d/z3)."""
    return _price_return_since_shock(close, volume, _TD_QTR, 3.0)


def vsa_ext_042_price_below_shock_low_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: close is below the low-of-shock-day (deeper capitulation)."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    # Use close as proxy; close on shock day saved via ffill
    shock_close = close.where(flag == 1.0).ffill()
    # Approximate: close < shock close * 0.99 (slightly below shock close)
    return (close < shock_close * 0.99).astype(float)


def vsa_ext_043_post_shock_drawdown_depth_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max decline from last shock-day close, measured in trailing 63d window."""
    flag = _shock_flag(volume, _TD_QTR, 2.0)
    shock_close = close.where(flag == 1.0).ffill()
    ret = _safe_div(close - shock_close, shock_close.clip(lower=_EPS))
    # Minimum (worst drawdown) of this return over trailing 63d
    return _rolling_min(ret, _TD_QTR)


def vsa_ext_044_price_acceleration_post_shock_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day acceleration of close (second diff of 5-day return)."""
    ret5 = close.pct_change(_TD_WEEK)
    return ret5.diff(_TD_WEEK)


def vsa_ext_045_close_momentum_vs_shock_window_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day close momentum divided by shock-window volatility (Sharpe-like)."""
    ret21 = close.pct_change(_TD_MON)
    std21 = close.pct_change(1).rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).std()
    return _safe_div(ret21, std21.clip(lower=_EPS))


def vsa_ext_046_price_decline_post_shock_5d_count(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days in trailing 5 days where shock occurred 5d ago and price declined."""
    shock_5ago = _shock_flag(volume, _TD_QTR, 2.0).shift(5).fillna(0.0)
    declined = (close < close.shift(5)).astype(float)
    return _rolling_sum(shock_5ago * declined, _TD_WEEK)


def vsa_ext_047_post_shock_high_below_shock_close(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: 5-day rolling max of close is still below shock-day close (stuck below)."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    shock_close = close.where(flag == 1.0).ffill()
    max5 = _rolling_max(close, _TD_WEEK)
    return (max5 < shock_close).astype(float)


def vsa_ext_048_price_channel_post_shock_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(Close - 21d-min) / (21d-max - 21d-min) in aftermath; 0 = at bottom."""
    lo = _rolling_min(close, _TD_MON)
    hi = _rolling_max(close, _TD_MON)
    return _safe_div(close - lo, (hi - lo).clip(lower=_EPS))


def vsa_ext_049_shock_day_return_signed_magnitude(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Signed return magnitude on last shock day (neg = bearish shock)."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    ret = close.pct_change(1)
    return ret.where(flag == 1.0).ffill()


def vsa_ext_050_post_shock_close_trend_slope_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day OLS slope of close normalized by 21d std (short-term trend after shock)."""
    std21 = close.pct_change(1).rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).std()
    normed = _safe_div(close, std21.clip(lower=_EPS))
    return _linslope(normed, _TD_WEEK)


# --- Group F (051-060): Extended vol-after-shock texture ---

def vsa_ext_051_vol_entropy_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Shannon entropy of volume distribution over 21d (high = uneven)."""
    def ent(x):
        x = x[~np.isnan(x)]
        x = x[x > 0]
        if len(x) < 3:
            return np.nan
        p = x / x.sum()
        return float(-np.sum(p * np.log(p + 1e-15)))
    return volume.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(ent, raw=True)


def vsa_ext_052_vol_entropy_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Shannon entropy of volume distribution over 63d."""
    def ent(x):
        x = x[~np.isnan(x)]
        x = x[x > 0]
        if len(x) < 5:
            return np.nan
        p = x / x.sum()
        return float(-np.sum(p * np.log(p + 1e-15)))
    return volume.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(ent, raw=True)


def vsa_ext_053_vol_skewness_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling skewness of volume over 21 days (positive = right tail / shock prone)."""
    def skew(x):
        x = x[~np.isnan(x)]
        if len(x) < 4:
            return np.nan
        m = x.mean()
        s = x.std()
        if s < _EPS:
            return np.nan
        return float(((x - m) ** 3).mean() / s ** 3)
    return volume.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(skew, raw=True)


def vsa_ext_054_vol_kurtosis_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling kurtosis of volume over 63 days (heavy tail = shock concentration)."""
    def kurt(x):
        x = x[~np.isnan(x)]
        if len(x) < 6:
            return np.nan
        m = x.mean()
        s = x.std()
        if s < _EPS:
            return np.nan
        return float(((x - m) ** 4).mean() / s ** 4) - 3.0
    return volume.rolling(_TD_QTR, min_periods=max(6, _TD_QTR // 2)).apply(kurt, raw=True)


def vsa_ext_055_vol_shock_gap_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean gap between consecutive shock days in trailing 21d period."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    # Days since previous shock = days_since shifted by 1
    d = _days_since_last_shock(volume, _TD_MON, 2.0)
    return _rolling_mean(d, _TD_MON)


def vsa_ext_056_vol_above_2x_mean_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days in 21d where volume > 2x its 63d mean."""
    ratio = _safe_div(volume, _rolling_mean(volume, _TD_QTR).clip(lower=_EPS))
    return _rolling_sum((ratio > 2.0).astype(float), _TD_MON)


def vsa_ext_057_vol_above_3x_mean_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days in 63d where volume > 3x its 63d mean."""
    ratio = _safe_div(volume, _rolling_mean(volume, _TD_QTR).clip(lower=_EPS))
    return _rolling_sum((ratio > 3.0).astype(float), _TD_QTR)


def vsa_ext_058_vol_autocorr_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1-day autocorrelation of volume over trailing 21 days (persistence)."""
    return volume.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).corr(volume.shift(1))


def vsa_ext_059_vol_shock_reversion_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: volume has fallen below its 21d mean within 5 days of last shock."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    d = _days_since_last_shock(volume, _TD_MON, 2.0)
    reverted = (volume < _rolling_mean(volume, _TD_MON)).astype(float)
    return ((d <= _TD_WEEK) & (reverted == 1.0)).astype(float)


def vsa_ext_060_vol_shock_count_per_year_expanding(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Annualized shock rate: expanding count / (expanding days / 252)."""
    cnt = _shock_flag(volume, _TD_QTR, 2.0).expanding(min_periods=5).sum()
    days = pd.Series(np.arange(1, len(cnt) + 1, dtype=float), index=cnt.index)
    return _safe_div(cnt * _TD_YEAR, days.clip(lower=_EPS))


# --- Group G (061-075): Composite and cross-domain extended features ---

def vsa_ext_061_shock_vol_price_composite_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day: shock_intensity * neg_flow_frac * decay_ratio composite."""
    intensity = _rolling_sum(_vol_zscore(volume, _TD_MON).clip(lower=0.0), _TD_MON)
    dn_vol = _rolling_sum((close.diff(1) < 0.0).astype(float) * volume, _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    neg_frac = _safe_div(dn_vol, total_vol.clip(lower=_EPS))
    return intensity * neg_frac


def vsa_ext_062_shock_vol_price_composite_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day: shock_intensity * neg_flow_frac composite."""
    intensity = _rolling_sum(_vol_zscore(volume, _TD_QTR).clip(lower=0.0), _TD_QTR)
    dn_vol = _rolling_sum((close.diff(1) < 0.0).astype(float) * volume, _TD_QTR)
    total_vol = _rolling_sum(volume, _TD_QTR)
    neg_frac = _safe_div(dn_vol, total_vol.clip(lower=_EPS))
    return intensity * neg_frac


def vsa_ext_063_vol_shock_capitulation_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Combined score: shock_density_21d * post_shock_return_negativity * 100."""
    density = _rolling_sum(_shock_flag(volume, _TD_MON, 2.0), _TD_MON) / _TD_MON
    ret21 = close.pct_change(_TD_MON)
    neg_ret = (-ret21).clip(lower=0.0)
    return density * neg_ret * 100.0


def vsa_ext_064_shock_recency_x_severity(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Recency score (1/d) * peak z-score in 21d (proximity x severity)."""
    d = _days_since_last_shock(volume, _TD_MON, 2.0).fillna(999.0)
    recency = 1.0 / (d + 1.0)
    peak_z = _rolling_max(_vol_zscore(volume, _TD_MON), _TD_MON)
    return recency * peak_z.clip(lower=0.0)


def vsa_ext_065_vol_decay_x_price_decline(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol decay ratio * price decline since shock (both bearish = high score)."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    shock_vol = volume.where(flag == 1.0).ffill()
    decay = _safe_div(volume, shock_vol.clip(lower=_EPS)).fillna(1.0)
    ret = _price_return_since_shock(close, volume, _TD_MON, 2.0).fillna(0.0)
    neg_ret = (-ret).clip(lower=0.0)
    return decay * neg_ret


def vsa_ext_066_vol_shock_duration_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Duration of current elevated-volume streak (> 1.5x mean, days consecutive)."""
    return _consec_streak(
        (_safe_div(volume, _rolling_mean(volume, _TD_MON).clip(lower=_EPS)) > 1.5).astype(bool)
    )


def vsa_ext_067_vol_shock_duration_63d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d rolling mean of elevated-volume streak length over 63d context."""
    streak = _consec_streak(
        (_safe_div(volume, _rolling_mean(volume, _TD_QTR).clip(lower=_EPS)) > 1.5).astype(bool)
    )
    return _rolling_mean(streak, _TD_MON)


def vsa_ext_068_shock_and_new_price_low_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in 21d where shock AND close = new 21d low simultaneously."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    lo21 = _rolling_min(close, _TD_MON)
    at_low = (close <= lo21 * 1.001).astype(float)
    return _rolling_sum(flag * at_low, _TD_MON)


def vsa_ext_069_post_shock_close_new_low_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: close today is at a new 63d low AND a shock occurred in last 21d."""
    lo63 = _rolling_min(close, _TD_QTR)
    at_lo = (close <= lo63 * 1.001).astype(float)
    shock_cnt21 = _rolling_sum(_shock_flag(volume, _TD_MON, 2.0), _TD_MON)
    return ((at_lo == 1.0) & (shock_cnt21 >= 1.0)).astype(float)


def vsa_ext_070_shock_vol_neg_price_skew(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Asymmetry: negative-return shock days / positive-return shock days (63d)."""
    flag = _shock_flag(volume, _TD_QTR, 2.0)
    neg_shock = flag * (close.pct_change(1) < 0.0).astype(float)
    pos_shock = flag * (close.pct_change(1) > 0.0).astype(float)
    neg_cnt = _rolling_sum(neg_shock, _TD_QTR)
    pos_cnt = _rolling_sum(pos_shock, _TD_QTR)
    return _safe_div(neg_cnt, (pos_cnt + 1.0).clip(lower=_EPS))


def vsa_ext_071_shock_vol_rolling_beta_to_price(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d beta of volume changes to absolute price returns."""
    vol_chg = volume.pct_change(1).fillna(0.0)
    abs_ret = close.pct_change(1).abs().fillna(0.0)
    cov = vol_chg.rolling(_TD_QTR, min_periods=max(10, _TD_QTR // 2)).cov(abs_ret)
    var = abs_ret.rolling(_TD_QTR, min_periods=max(10, _TD_QTR // 2)).var()
    return _safe_div(cov, var.clip(lower=_EPS))


def vsa_ext_072_post_shock_vol_price_divergence_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Score: vol declining AND price declining (double negative = capitulation)."""
    vol_ret = volume.pct_change(_TD_WEEK)
    price_ret = close.pct_change(_TD_WEEK)
    both_down = (vol_ret < 0.0).astype(float) * (price_ret < 0.0).astype(float)
    return _rolling_sum(both_down, _TD_MON)


def vsa_ext_073_vol_shock_price_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day sum of (shock z-score * abs daily return) / close (intensity/price)."""
    z = _vol_zscore(volume, _TD_QTR).clip(lower=0.0)
    abs_ret = close.pct_change(1).abs().fillna(0.0)
    return _rolling_sum(z * abs_ret, _TD_QTR)


def vsa_ext_074_vol_shock_momentum_reversal_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: volume spiked (21d/z>2) but price closed ABOVE prior close (reversal)."""
    shock = _shock_flag(volume, _TD_MON, 2.0)
    up = (close.pct_change(1) > 0.0).astype(float)
    reversal = shock * up
    return _rolling_sum(reversal, _TD_MON)


def vsa_ext_075_aftermath_distress_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Final composite: shock_density * neg_vol_fraction * (1 + days_since_shock_recency)."""
    density = _rolling_sum(_shock_flag(volume, _TD_MON, 2.0), _TD_MON) / _TD_MON
    dn_vol = _rolling_sum((close.diff(1) < 0.0).astype(float) * volume, _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    neg_frac = _safe_div(dn_vol, total_vol.clip(lower=_EPS))
    d = _days_since_last_shock(volume, _TD_MON, 2.0).fillna(999.0)
    recency = 1.0 / (d + 1.0)
    return density * neg_frac * (1.0 + recency)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_SHOCK_AFTERMATH_EXTENDED_REGISTRY_001_075 = {
    "vsa_ext_001_shock_triple_confirm_flag": {"inputs": ["close", "volume"], "func": vsa_ext_001_shock_triple_confirm_flag},
    "vsa_ext_002_shock_agreement_score": {"inputs": ["close", "volume"], "func": vsa_ext_002_shock_agreement_score},
    "vsa_ext_003_shock_score_z3_triple": {"inputs": ["close", "volume"], "func": vsa_ext_003_shock_score_z3_triple},
    "vsa_ext_004_days_since_shock_min_window": {"inputs": ["close", "volume"], "func": vsa_ext_004_days_since_shock_min_window},
    "vsa_ext_005_shock_count_trend_21d_vs_63d": {"inputs": ["close", "volume"], "func": vsa_ext_005_shock_count_trend_21d_vs_63d},
    "vsa_ext_006_multi_window_shock_recency_index": {"inputs": ["close", "volume"], "func": vsa_ext_006_multi_window_shock_recency_index},
    "vsa_ext_007_shock_and_price_decline_21d": {"inputs": ["close", "volume"], "func": vsa_ext_007_shock_and_price_decline_21d},
    "vsa_ext_008_shock_and_price_decline_63d": {"inputs": ["close", "volume"], "func": vsa_ext_008_shock_and_price_decline_63d},
    "vsa_ext_009_shock_amplitude_sum_21d": {"inputs": ["close", "volume"], "func": vsa_ext_009_shock_amplitude_sum_21d},
    "vsa_ext_010_shock_amplitude_sum_63d": {"inputs": ["close", "volume"], "func": vsa_ext_010_shock_amplitude_sum_63d},
    "vsa_ext_011_vol_zscore_squared_21d_sum": {"inputs": ["close", "volume"], "func": vsa_ext_011_vol_zscore_squared_21d_sum},
    "vsa_ext_012_vol_zscore_cubed_21d_sum": {"inputs": ["close", "volume"], "func": vsa_ext_012_vol_zscore_cubed_21d_sum},
    "vsa_ext_013_shock_exponential_decay_score": {"inputs": ["close", "volume"], "func": vsa_ext_013_shock_exponential_decay_score},
    "vsa_ext_014_shock_exponential_decay_score_slow": {"inputs": ["close", "volume"], "func": vsa_ext_014_shock_exponential_decay_score_slow},
    "vsa_ext_015_vol_regime_flag_elevated": {"inputs": ["close", "volume"], "func": vsa_ext_015_vol_regime_flag_elevated},
    "vsa_ext_016_vol_regime_flag_depressed": {"inputs": ["close", "volume"], "func": vsa_ext_016_vol_regime_flag_depressed},
    "vsa_ext_017_vol_high_regime_shock_count_63d": {"inputs": ["close", "volume"], "func": vsa_ext_017_vol_high_regime_shock_count_63d},
    "vsa_ext_018_vol_zscore_log1p_21d_sum": {"inputs": ["close", "volume"], "func": vsa_ext_018_vol_zscore_log1p_21d_sum},
    "vsa_ext_019_shock_negative_price_product_21d": {"inputs": ["close", "volume"], "func": vsa_ext_019_shock_negative_price_product_21d},
    "vsa_ext_020_shock_at_price_low_flag": {"inputs": ["close", "volume"], "func": vsa_ext_020_shock_at_price_low_flag},
    "vsa_ext_021_vwap_63d": {"inputs": ["close", "high", "low", "volume"], "func": vsa_ext_021_vwap_63d},
    "vsa_ext_022_close_vs_vwap_126d": {"inputs": ["close", "high", "low", "volume"], "func": vsa_ext_022_close_vs_vwap_126d},
    "vsa_ext_023_shock_day_close_vs_vwap_63d": {"inputs": ["close", "high", "low", "volume"], "func": vsa_ext_023_shock_day_close_vs_vwap_63d},
    "vsa_ext_024_vol_weighted_avg_return_5d": {"inputs": ["close", "volume"], "func": vsa_ext_024_vol_weighted_avg_return_5d},
    "vsa_ext_025_vol_weighted_range_21d": {"inputs": ["close", "high", "low", "volume"], "func": vsa_ext_025_vol_weighted_range_21d},
    "vsa_ext_026_vwap_deviation_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": vsa_ext_026_vwap_deviation_zscore_21d},
    "vsa_ext_027_shock_day_vol_to_vwap_vol": {"inputs": ["close", "high", "low", "volume"], "func": vsa_ext_027_shock_day_vol_to_vwap_vol},
    "vsa_ext_028_post_shock_below_vwap_consec": {"inputs": ["close", "high", "low", "volume"], "func": vsa_ext_028_post_shock_below_vwap_consec},
    "vsa_ext_029_vwap_21d_trend_slope": {"inputs": ["close", "high", "low", "volume"], "func": vsa_ext_029_vwap_21d_trend_slope},
    "vsa_ext_030_shock_day_close_pct_from_low": {"inputs": ["close", "high", "low", "volume"], "func": vsa_ext_030_shock_day_close_pct_from_low},
    "vsa_ext_031_obv_zscore_21d": {"inputs": ["close", "volume"], "func": vsa_ext_031_obv_zscore_21d},
    "vsa_ext_032_obv_zscore_63d": {"inputs": ["close", "volume"], "func": vsa_ext_032_obv_zscore_63d},
    "vsa_ext_033_obv_expanding_percentile": {"inputs": ["close", "volume"], "func": vsa_ext_033_obv_expanding_percentile},
    "vsa_ext_034_vol_flow_imbalance_21d": {"inputs": ["close", "volume"], "func": vsa_ext_034_vol_flow_imbalance_21d},
    "vsa_ext_035_vol_flow_imbalance_63d": {"inputs": ["close", "volume"], "func": vsa_ext_035_vol_flow_imbalance_63d},
    "vsa_ext_036_neg_flow_imbalance_zscore_63d": {"inputs": ["close", "volume"], "func": vsa_ext_036_neg_flow_imbalance_zscore_63d},
    "vsa_ext_037_vol_flow_imbalance_trend_5d": {"inputs": ["close", "volume"], "func": vsa_ext_037_vol_flow_imbalance_trend_5d},
    "vsa_ext_038_shock_negative_flow_flag": {"inputs": ["close", "volume"], "func": vsa_ext_038_shock_negative_flow_flag},
    "vsa_ext_039_shock_negative_flow_count_63d": {"inputs": ["close", "volume"], "func": vsa_ext_039_shock_negative_flow_count_63d},
    "vsa_ext_040_obv_pct_change_21d": {"inputs": ["close", "volume"], "func": vsa_ext_040_obv_pct_change_21d},
    "vsa_ext_041_price_recovery_since_shock_63dz3": {"inputs": ["close", "volume"], "func": vsa_ext_041_price_recovery_since_shock_63dz3},
    "vsa_ext_042_price_below_shock_low_flag": {"inputs": ["close", "volume"], "func": vsa_ext_042_price_below_shock_low_flag},
    "vsa_ext_043_post_shock_drawdown_depth_63d": {"inputs": ["close", "volume"], "func": vsa_ext_043_post_shock_drawdown_depth_63d},
    "vsa_ext_044_price_acceleration_post_shock_5d": {"inputs": ["close", "volume"], "func": vsa_ext_044_price_acceleration_post_shock_5d},
    "vsa_ext_045_close_momentum_vs_shock_window_21d": {"inputs": ["close", "volume"], "func": vsa_ext_045_close_momentum_vs_shock_window_21d},
    "vsa_ext_046_price_decline_post_shock_5d_count": {"inputs": ["close", "volume"], "func": vsa_ext_046_price_decline_post_shock_5d_count},
    "vsa_ext_047_post_shock_high_below_shock_close": {"inputs": ["close", "volume"], "func": vsa_ext_047_post_shock_high_below_shock_close},
    "vsa_ext_048_price_channel_post_shock_21d": {"inputs": ["close", "volume"], "func": vsa_ext_048_price_channel_post_shock_21d},
    "vsa_ext_049_shock_day_return_signed_magnitude": {"inputs": ["close", "volume"], "func": vsa_ext_049_shock_day_return_signed_magnitude},
    "vsa_ext_050_post_shock_close_trend_slope_5d": {"inputs": ["close", "volume"], "func": vsa_ext_050_post_shock_close_trend_slope_5d},
    "vsa_ext_051_vol_entropy_21d": {"inputs": ["close", "volume"], "func": vsa_ext_051_vol_entropy_21d},
    "vsa_ext_052_vol_entropy_63d": {"inputs": ["close", "volume"], "func": vsa_ext_052_vol_entropy_63d},
    "vsa_ext_053_vol_skewness_21d": {"inputs": ["close", "volume"], "func": vsa_ext_053_vol_skewness_21d},
    "vsa_ext_054_vol_kurtosis_63d": {"inputs": ["close", "volume"], "func": vsa_ext_054_vol_kurtosis_63d},
    "vsa_ext_055_vol_shock_gap_days_21d": {"inputs": ["close", "volume"], "func": vsa_ext_055_vol_shock_gap_days_21d},
    "vsa_ext_056_vol_above_2x_mean_count_21d": {"inputs": ["close", "volume"], "func": vsa_ext_056_vol_above_2x_mean_count_21d},
    "vsa_ext_057_vol_above_3x_mean_count_63d": {"inputs": ["close", "volume"], "func": vsa_ext_057_vol_above_3x_mean_count_63d},
    "vsa_ext_058_vol_autocorr_5d": {"inputs": ["close", "volume"], "func": vsa_ext_058_vol_autocorr_5d},
    "vsa_ext_059_vol_shock_reversion_flag": {"inputs": ["close", "volume"], "func": vsa_ext_059_vol_shock_reversion_flag},
    "vsa_ext_060_vol_shock_count_per_year_expanding": {"inputs": ["close", "volume"], "func": vsa_ext_060_vol_shock_count_per_year_expanding},
    "vsa_ext_061_shock_vol_price_composite_21d": {"inputs": ["close", "volume"], "func": vsa_ext_061_shock_vol_price_composite_21d},
    "vsa_ext_062_shock_vol_price_composite_63d": {"inputs": ["close", "volume"], "func": vsa_ext_062_shock_vol_price_composite_63d},
    "vsa_ext_063_vol_shock_capitulation_score": {"inputs": ["close", "volume"], "func": vsa_ext_063_vol_shock_capitulation_score},
    "vsa_ext_064_shock_recency_x_severity": {"inputs": ["close", "volume"], "func": vsa_ext_064_shock_recency_x_severity},
    "vsa_ext_065_vol_decay_x_price_decline": {"inputs": ["close", "volume"], "func": vsa_ext_065_vol_decay_x_price_decline},
    "vsa_ext_066_vol_shock_duration_21d": {"inputs": ["close", "volume"], "func": vsa_ext_066_vol_shock_duration_21d},
    "vsa_ext_067_vol_shock_duration_63d_mean": {"inputs": ["close", "volume"], "func": vsa_ext_067_vol_shock_duration_63d_mean},
    "vsa_ext_068_shock_and_new_price_low_21d": {"inputs": ["close", "volume"], "func": vsa_ext_068_shock_and_new_price_low_21d},
    "vsa_ext_069_post_shock_close_new_low_flag": {"inputs": ["close", "volume"], "func": vsa_ext_069_post_shock_close_new_low_flag},
    "vsa_ext_070_shock_vol_neg_price_skew": {"inputs": ["close", "volume"], "func": vsa_ext_070_shock_vol_neg_price_skew},
    "vsa_ext_071_shock_vol_rolling_beta_to_price": {"inputs": ["close", "volume"], "func": vsa_ext_071_shock_vol_rolling_beta_to_price},
    "vsa_ext_072_post_shock_vol_price_divergence_score": {"inputs": ["close", "volume"], "func": vsa_ext_072_post_shock_vol_price_divergence_score},
    "vsa_ext_073_vol_shock_price_ratio_63d": {"inputs": ["close", "volume"], "func": vsa_ext_073_vol_shock_price_ratio_63d},
    "vsa_ext_074_vol_shock_momentum_reversal_flag": {"inputs": ["close", "volume"], "func": vsa_ext_074_vol_shock_momentum_reversal_flag},
    "vsa_ext_075_aftermath_distress_index": {"inputs": ["close", "volume"], "func": vsa_ext_075_aftermath_distress_index},
}
